// Laut ASCII di dua tempat:
// - hero beranda: hiu + kawanan ikan, dengan logo Sentra sebagai koin ASCII yang berputar.
//   Ikan dan hiu lewat di belakang koin: sel koin selalu menimpa apa pun yang digambar sebelumnya.
// - footer semua halaman: kawanan ikan saja, lebih hemat.
import { World } from "./ocean/world.js";
import { AsciiRenderer, BG } from "./ocean/renderer.js";

var STEP = 1 / 60, MAX_STEPS = 4;
var SPIN = 5.2;            // detik per putaran penuh
var LOGO_SCALE = 0.78;     // logo menempati 78% radius muka koin
var LUT_N = 160;           // resolusi horizontal tabel logo per baris
var LEVELS = 8;            // tingkat terang yang dibedakan; tiap tingkat = satu fillStyle
var FACE_RAMP = " .:-=+*%#@";

// Kualitas bertingkat. Perangkat lemah mulai dari tingkat 1; tingkat naik sendiri kalau frame terlalu lama.
// Tingkat terakhir berarti satu frame diam: hiu berhenti, koin menghadap depan.
var HERO_QUALITY = [
  { fps: 30, dpr: 2, sharks: 4 },
  { fps: 20, dpr: 1, sharks: 2 },
  null,
];
var FOOTER_QUALITY = [
  { fps: 20, dpr: 2, sharks: 0 },
  { fps: 15, dpr: 1, sharks: 0 },
  null,
];
var SLOW_MS = [12, 25];    // median waktu frame yang memicu turun ke tingkat berikutnya (±35% / 50% waktu CPU)
var PROBE = 40;            // jumlah frame yang diukur sebelum memutuskan

function weakDevice() {
  var c = navigator.connection;
  return (navigator.hardwareConcurrency || 8) <= 4 || (navigator.deviceMemory || 8) <= 4 || !!(c && c.saveData);
}

function Coin(slot) {
  this.slot = slot;
  this.img = null;
  this.cx = 0; this.cy = 0; this.r = 0;
  this.rows = [];          // tabel logo per baris layar, dibangun ulang saat ukuran berubah
  this.palette = [];       // warna dasar logo hasil kuantisasi
  this.styles = {};        // cache string fillStyle
  this.buckets = {};       // sel per fillStyle untuk frame ini
  this.onReady = null;
  var self = this, img = new Image();
  img.onload = function () { self.img = img; self.cw = 0; if (self.onReady) self.onReady(); };
  img.src = slot.getAttribute("data-logo");
}

Coin.prototype.place = function (canvas) {
  var c = canvas.getBoundingClientRect(), s = this.slot.getBoundingClientRect();
  this.cx = s.left - c.left + s.width / 2;
  this.cy = s.top - c.top + s.height / 2;
  this.r = Math.min(s.width, s.height) / 2;
  this.cw = 0;             // paksa tabel dibangun ulang
};

// Untuk tiap baris sel yang dilintasi koin, simpan cakupan logo dan indeks warnanya sepanjang u ∈ [-1, 1].
// Garis cincin logo lebih tipis dari satu sel, jadi cakupan diambil maksimum (bukan rata-rata) setinggi satu sel.
Coin.prototype.build = function (cw, ch) {
  this.cw = cw; this.ch = ch; this.rows = [];
  if (!this.img || this.r < 8) return;
  var n = 256, cv = document.createElement("canvas");
  cv.width = cv.height = n;
  var g = cv.getContext("2d", { willReadFrequently: true });
  g.drawImage(this.img, 0, 0, n, n);
  var d = g.getImageData(0, 0, n, n).data, R = this.r, pal = [], palKey = {};
  var r0 = Math.floor((this.cy - R) / ch), r1 = Math.ceil((this.cy + R) / ch), dv = ch / R;
  for (var row = r0; row <= r1; row++) {
    var v = (row * ch + ch / 2 - this.cy) / R;
    if (v <= -1 || v >= 1) continue;
    var cov = new Float32Array(LUT_N), col = new Uint8Array(LUT_N);
    for (var i = 0; i < LUT_N; i++) {
      var u = (i + 0.5) / LUT_N * 2 - 1, best = 0, bi = -1;
      for (var k = -2; k <= 2; k++) {
        var sv = (v + k * 0.2 * dv) / LOGO_SCALE, su = u / LOGO_SCALE;
        var x = Math.round((su * 0.5 + 0.5) * (n - 1)), y = Math.round((sv * 0.5 + 0.5) * (n - 1));
        if (x < 0 || y < 0 || x >= n || y >= n) continue;
        var p = (y * n + x) * 4;
        if (d[p + 3] > best) { best = d[p + 3]; bi = p; }
      }
      cov[i] = best / 255;
      if (bi >= 0 && best > 50) {
        var key = (d[bi] >> 4) + "," + (d[bi + 1] >> 4) + "," + (d[bi + 2] >> 4);
        if (!(key in palKey)) { palKey[key] = pal.length; pal.push([d[bi], d[bi + 1], d[bi + 2]]); }
        col[i] = palKey[key];
      }
    }
    this.rows.push({ row: row, v: v, w: Math.sqrt(1 - v * v), cov: cov, col: col });
  }
  this.palette = pal;
};

Coin.prototype.style = function (key, make) {
  var s = this.styles[key];
  if (s === undefined) s = this.styles[key] = make();
  return s;
};

Coin.prototype.put = function (style, glyph, x, y) {
  var b = this.buckets[style];
  if (!b) b = this.buckets[style] = [];
  b.push(glyph, x, y);
};

Coin.prototype.draw = function (ctx, cw, ch, t) {
  var R = this.r;
  if (R < 8) return;
  if (this.cw !== cw || this.ch !== ch) this.build(cw, ch);
  var th = t * Math.PI * 2 / SPIN;
  var cos = Math.cos(th), sin = Math.sin(th), self = this;
  var a = R * Math.abs(cos);              // setengah lebar muka koin yang terlihat
  var d = R * 0.13 * sin;                 // tebal tepi koin, terlihat saat miring
  var light = 0.5 + 0.5 * Math.abs(cos);
  var glint = sin * 0.9;                  // pita kilau yang menyapu muka koin
  var du = a > 0.5 ? cw / a : 0;
  var rimLevel = Math.round(Math.abs(sin) * 3);
  var rimStyle = this.style("r" + rimLevel, function () { return "rgba(120,150,210," + (0.55 + 0.35 * rimLevel / 3).toFixed(2) + ")"; });
  var rimGlyph = a < cw ? "|" : null;

  for (var key in this.buckets) this.buckets[key].length = 0;
  ctx.fillStyle = BG;
  for (var ri = 0; ri < this.rows.length; ri++) {
    var L = this.rows[ri], v = L.v, y = L.row * ch + ch / 2, half = a * L.w;
    var lo = Math.min(0, -d) - half, hi = Math.max(0, -d) + half;
    var c0 = Math.ceil((this.cx + lo - cw / 2) / cw), c1 = Math.floor((this.cx + hi - cw / 2) / cw);
    if (c1 < c0) continue;
    ctx.fillRect(c0 * cw, L.row * ch, (c1 - c0 + 1) * cw, ch);   // tutup satu baris sekaligus

    for (var col = c0; col <= c1; col++) {
      var x = col * cw + cw / 2, dx = x - this.cx;
      if (!(a > 0.5 && Math.abs(dx) <= half)) {
        this.put(rimStyle, rimGlyph || (dx < 0 ? "[" : "]"), x, y);
        continue;
      }
      var u = dx / a, rr = Math.sqrt(u * u + v * v);
      var shine = Math.exp(-Math.pow(u + v * 0.35 - glint, 2) / 0.04);
      if (rr > 0.9) {
        var k = Math.min(LEVELS - 1, Math.round(Math.min(1, light + shine * 0.5) * (LEVELS - 1)));
        this.put(this.style("o" + k, function () {
          var f = k / (LEVELS - 1);
          return "rgb(" + Math.round(150 * f) + "," + Math.round(180 * f) + "," + Math.round(235 * f) + ")";
        }), rr > 0.96 ? "o" : "O", x, y);
        continue;
      }
      // cakupan terkuat di rentang u yang ditutup sel ini (melebar saat koin miring)
      var best = 0, bc = 0;
      for (var s = -1; s <= 1; s++) {
        var i = Math.floor(((u + s * 0.4 * du) * 0.5 + 0.5) * LUT_N);
        if (i < 0 || i >= LUT_N) continue;
        if (L.cov[i] > best) { best = L.cov[i]; bc = L.col[i]; }
      }
      if (best > 0.2) {
        var lv = Math.min(LEVELS - 1, Math.round((light + shine * 0.6) / 1.6 * (LEVELS - 1)));
        var gi = Math.min(FACE_RAMP.length - 1, 5 + Math.floor(best * 4.99));
        this.put(this.style("l" + bc + "_" + lv, function () {
          var c = self.palette[bc], lift = (lv / (LEVELS - 1)) * 1.6 * 1.7;
          return "rgb(" + Math.min(255, Math.round(c[0] * lift + 40)) + "," + Math.min(255, Math.round(c[1] * lift + 46)) + "," + Math.min(255, Math.round(c[2] * lift + 52)) + ")";
        }), FACE_RAMP[gi], x, y);
      } else if (((col * 7 + L.row * 13) & 3) === 0 || shine > 0.35) {
        var dl = Math.min(3, Math.round(shine * 3));
        this.put(this.style("d" + dl, function () { return "rgba(110,140,200," + (0.1 + 0.15 * dl).toFixed(2) + ")"; }), shine > 0.35 ? ":" : ".", x, y);
      }
    }
  }
  for (var st in this.buckets) {
    var b = this.buckets[st];
    if (!b.length) continue;
    ctx.fillStyle = st;
    for (var j = 0; j < b.length; j += 3) ctx.fillText(b[j], b[j + 1], b[j + 2] + 1);
  }
};

function OceanScene(canvas, quality, slot) {
  this.canvas = canvas;
  this.quality = quality;
  this.world = new World();
  this.sharkSpecs = this.world.sharkSpecs;   // hiu dipanggil ulang tiap resize; tingkat kualitas memangkas jumlahnya
  this.renderer = new AsciiRenderer(canvas);
  this.renderer.setFontFamily(getComputedStyle(canvas).fontFamily);
  this.coin = slot ? new Coin(slot) : null;
  this.ctx = canvas.getContext("2d");
  this.raf = 0; this.last = 0; this.lastPaint = 0; this.acc = 0; this.visible = true;
  this.level = weakDevice() ? 1 : 0;
  this.samples = [];
  this.reduced = window.matchMedia("(prefers-reduced-motion: reduce)");

  var self = this;
  this.frame = function (now) { self.tick(now); };
  new ResizeObserver(function () { self.resize(); }).observe(canvas);
  if (slot) new ResizeObserver(function () { self.resize(); }).observe(slot);
  new IntersectionObserver(function (e) { self.visible = e[0].isIntersecting; self.schedule(); }).observe(canvas);
  this.reduced.addEventListener("change", function () { self.isStill() ? self.still() : self.schedule(); });
  if (this.coin) this.coin.onReady = function () { if (self.isStill()) self.still(); };

  window.addEventListener("pointermove", function (e) {
    var p = self.local(e), ptr = self.world.pointer;
    ptr.x = p.x; ptr.y = p.y; ptr.active = p.inside && e.pointerType !== "touch";
  }, { passive: true });
  window.addEventListener("pointerdown", function (e) {
    var p = self.local(e);
    if (p.inside && !self.isStill() && !e.target.closest("a,button,summary,input")) self.world.splash(p.x, p.y);
  }, { passive: true });
  document.documentElement.addEventListener("pointerleave", function () { self.world.pointer.active = false; });

  this.resize();
  if (document.fonts) document.fonts.load("600 16px " + getComputedStyle(canvas).fontFamily).then(function () { if (self.isStill()) self.still(); });
  this.schedule();
}

OceanScene.prototype.isStill = function () {
  return this.reduced.matches || !this.quality[this.level];
};

OceanScene.prototype.local = function (e) {
  var r = this.canvas.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
  return { x: x, y: y, inside: x >= 0 && y >= 0 && x <= r.width && y <= r.height };
};

OceanScene.prototype.resize = function () {
  var r = this.canvas.getBoundingClientRect();
  if (r.width < 1 || r.height < 1) return;
  var q = this.quality[this.level] || this.quality[this.quality.length - 2];
  this.world.sharkSpecs = this.sharkSpecs.slice(0, q.sharks);
  this.renderer.resize(r.width, r.height, Math.min(window.devicePixelRatio || 1, q.dpr));
  this.world.resize(r.width, r.height, this.renderer.cellWidth, this.renderer.cellHeight);
  if (this.coin) this.coin.place(this.canvas);
  if (this.isStill()) this.still();
};

OceanScene.prototype.paint = function (dt) {
  this.renderer.render(this.world, dt);
  if (this.coin) this.coin.draw(this.ctx, this.renderer.cellWidth, this.renderer.cellHeight, this.isStill() ? 0 : this.world.time);
};

OceanScene.prototype.schedule = function () {
  cancelAnimationFrame(this.raf);
  if (!this.visible || this.isStill()) return;
  this.last = this.lastPaint = performance.now();
  this.raf = requestAnimationFrame(this.frame);
};

OceanScene.prototype.tick = function (now) {
  var q = this.quality[this.level];
  if (!q || this.reduced.matches) return;
  this.raf = requestAnimationFrame(this.frame);
  if (now - this.lastPaint < 1000 / q.fps - 2) return;   // lewati frame layar sampai giliran fps target
  this.lastPaint = now;

  var t0 = performance.now(), dt = Math.min(0.1, (now - this.last) / 1000), steps = 0;
  this.last = now;
  this.acc += dt;
  while (this.acc >= STEP && steps < MAX_STEPS) { this.world.step(STEP); this.acc -= STEP; steps++; }
  if (steps === MAX_STEPS) this.acc = 0;
  this.paint(dt);
  this.measure(performance.now() - t0);
};

// Ukur waktu frame di perangkat pengunjung; kalau terlalu lama, turunkan kualitas satu tingkat.
OceanScene.prototype.measure = function (ms) {
  if (this.settled) return;
  this.samples.push(ms);
  if (this.samples.length < PROBE) return;
  var med = this.samples.sort(function (x, y) { return x - y; })[PROBE >> 1];
  this.samples = [];
  if (med <= SLOW_MS[this.level]) { this.settled = true; return; }   // cukup cepat: berhenti mengukur
  this.level++;
  if (this.quality[this.level]) this.resize();
  else { cancelAnimationFrame(this.raf); this.still(); }
};

// Satu frame diam (reduced motion atau perangkat terlalu lemah): biarkan ekosistem tenang dulu, koin menghadap depan.
OceanScene.prototype.still = function () {
  if (this.world.time < 4) for (var i = 0; i < 240; i++) this.world.step(STEP);
  this.paint(STEP);
};

var hero = document.querySelector(".hero-ocean canvas"), footer = document.querySelector(".footer-ocean canvas");
if (hero && hero.getContext) new OceanScene(hero, HERO_QUALITY, document.querySelector(".hero-coin"));
if (footer && footer.getContext) new OceanScene(footer, FOOTER_QUALITY, null);
