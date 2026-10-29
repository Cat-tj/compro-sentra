// Inti laut ASCII Sentra: simulasi, render, koin logo, dan kualitas adaptif.
// Tanpa DOM, jadi bisa jalan di Web Worker (OffscreenCanvas) maupun di thread utama sebagai cadangan.
import { World } from "./world.js?v=20261029e";
import { AsciiRenderer } from "./renderer.js?v=20261029e";

var STEP = 1 / 60, MAX_STEPS = 4;
var SPIN = 5.2;            // detik per putaran koin
var LOGO_SCALE = 0.78;     // logo menempati 78% radius muka koin
var LUT_N = 160;           // resolusi horizontal tabel logo per baris
var LEVELS = 8;            // tingkat terang yang dibedakan; tiap tingkat = satu fillStyle
var FACE_RAMP = " .:-=+*%#@";
var PROBE = 45;            // jumlah frame yang diukur sebelum memutuskan tingkat kualitas

export var FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace";

// Tingkat kualitas, dari terbaik ke teringan; null = satu frame diam.
// slow: median waktu frame (ms) yang membuat scene turun satu tingkat.
// Hero dan footer memakai laut yang sama; footer tanpa koin dan lebih hemat.
export var PRESETS = {
  hero: [
    { fps: 60, dpr: 2, sharks: 3, slow: 10 },
    { fps: 30, dpr: 2, sharks: 3, slow: 20 },
    { fps: 20, dpr: 1, sharks: 2, slow: 32 },
    null,
  ],
  footer: [
    { fps: 30, dpr: 2, sharks: 3, slow: 14 },
    { fps: 20, dpr: 1, sharks: 2, slow: 32 },
    null,
  ],
  // HP: hiu lebih sedikit (hiu adalah bagian termahal) dan fps lebih rendah.
  "hero-mobile": [
    { fps: 30, dpr: 2, sharks: 2, slow: 20 },
    { fps: 20, dpr: 1, sharks: 1, slow: 32 },
    null,
  ],
  "footer-mobile": [
    { fps: 20, dpr: 2, sharks: 1, slow: 30 },
    { fps: 15, dpr: 1, sharks: 0, slow: 45 },
    null,
  ],
};

// Gaya ascii-sharks asli: latar hitam, hiu berwarna solid, ikan sebagai -, ><, <=>, <>.
var THEME = {
  bg: "#000",
  sharks: [
    [1.55, 0.88, 0.26],    // oranye
    [0.32, 0.45, 1.5],     // biru
    [0.55, 0.85, 1.3],     // biru muda
  ],
  fish: [                  // urutan = spesies di species.js
    { glyph: "-", far: "rgba(230,238,255,.38)", near: "rgba(230,238,255,.8)" },     // sardine
    { glyph: "-", far: "rgba(230,238,255,.38)", near: "rgba(230,238,255,.8)" },     // anchovy
    { glyph: "><", far: "rgba(150,156,170,.55)", near: "rgba(170,176,190,.9)" },    // silverside
    { glyph: "<=>", far: "rgba(80,96,220,.6)", near: "rgba(96,112,240,.95)" },      // mackerel
    { glyph: "<>", far: "rgba(160,170,195,.5)", near: "rgba(180,190,215,.85)" },    // goby
  ],
};

var raf = typeof requestAnimationFrame === "function" ? requestAnimationFrame.bind(self) : function (cb) { return setTimeout(function () { cb(performance.now()); }, 16); };
var caf = typeof cancelAnimationFrame === "function" ? cancelAnimationFrame.bind(self) : clearTimeout;

function Coin(tex, bg) {
  this.tex = tex;          // { data: Uint8ClampedArray RGBA, n: sisi tekstur }
  this.bg = bg;            // warna latar laut; menutup ikan dan hiu yang lewat di belakang koin
  this.cx = 0; this.cy = 0; this.r = 0;
  this.rows = []; this.palette = []; this.styles = {}; this.buckets = {};
  this.cw = 0; this.ch = 0;
}

Coin.prototype.place = function (g) {
  this.cx = g.cx; this.cy = g.cy; this.r = g.r;
  this.cw = 0;             // paksa tabel dibangun ulang
};

// Untuk tiap baris sel yang dilintasi koin, simpan cakupan logo dan indeks warnanya sepanjang u ∈ [-1, 1].
// Garis cincin logo lebih tipis dari satu sel, jadi cakupan diambil maksimum (bukan rata-rata) setinggi satu sel.
Coin.prototype.build = function (cw, ch) {
  this.cw = cw; this.ch = ch; this.rows = [];
  var R = this.r;
  if (R < 8) return;
  var n = this.tex.n, d = this.tex.data, pal = [], palKey = {};
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
  this.styles = {};
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
  ctx.fillStyle = this.bg;
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

// opts: { preset: nama di PRESETS, level: tingkat awal }
export function Scene(canvas, opts) {
  this.canvas = canvas;
  this.quality = PRESETS[opts.preset];
  this.level = Math.min(opts.level || 0, this.quality.length - 2);
  this.world = new World();
  this.sharkSpecs = this.world.sharkSpecs;   // hiu dipanggil ulang tiap resize; tingkat kualitas memangkas jumlahnya
  this.renderer = new AsciiRenderer(canvas);
  this.renderer.setFontFamily(FONT);
  this.renderer.setTheme(THEME);
  this.ctx = canvas.getContext("2d");
  this.coin = null;
  this.w = 0; this.h = 0; this.dpr = 1;
  this.raf = 0; this.last = 0; this.lastPaint = 0; this.acc = 0;
  this.visible = true; this.reduced = false; this.settled = false; this.samples = [];
  var self = this;
  this.frame = function (now) { self.tick(now); };
}

Scene.prototype.still = function () { return this.reduced || !this.quality[this.level]; };

Scene.prototype.setCoin = function (geom, tex) {
  if (tex) this.coin = new Coin(tex, THEME.bg);
  if (this.coin && geom) this.coin.place(geom);
  if (this.still()) this.paintStill();
};

Scene.prototype.resize = function (w, h, dpr) {
  if (w < 1 || h < 1) return;
  this.w = w; this.h = h; this.dpr = dpr;
  var q = this.quality[this.level] || this.quality[this.quality.length - 2];
  this.world.sharkSpecs = this.sharkSpecs.slice(0, q.sharks);
  this.renderer.resize(w, h, Math.min(dpr, q.dpr));
  // Jarak antarikan dihitung dalam sel; sedikit diperlebar supaya ikan "<=>" dan "><" tidak saling tumpuk.
  this.world.resize(w, h, this.renderer.cellWidth * 1.4, this.renderer.cellHeight);
  if (this.coin) this.coin.cw = 0;
  if (this.still()) this.paintStill(); else this.schedule();
};

Scene.prototype.setVisible = function (v) { this.visible = v; this.schedule(); };
Scene.prototype.setReduced = function (r) { this.reduced = r; if (r) this.paintStill(); else this.schedule(); };
Scene.prototype.pointer = function (x, y, active) { var p = this.world.pointer; p.x = x; p.y = y; p.active = active; };
Scene.prototype.splash = function (x, y) { if (!this.still()) this.world.splash(x, y); };

Scene.prototype.paint = function (dt) {
  this.renderer.render(this.world, dt);
  if (this.coin) this.coin.draw(this.ctx, this.renderer.cellWidth, this.renderer.cellHeight, this.still() ? 0 : this.world.time);
};

// Satu frame diam (reduced motion atau perangkat terlalu lemah): biarkan ekosistem tenang dulu, koin menghadap depan.
Scene.prototype.paintStill = function () {
  caf(this.raf); this.raf = 0;
  if (!this.w) return;
  if (this.world.time < 4) for (var i = 0; i < 240; i++) this.world.step(STEP);
  this.paint(STEP);
};

Scene.prototype.schedule = function () {
  caf(this.raf); this.raf = 0;
  if (!this.visible || this.still() || !this.w) return;
  this.last = this.lastPaint = performance.now();
  this.raf = raf(this.frame);
};

Scene.prototype.tick = function (now) {
  var q = this.quality[this.level];
  if (!q || this.reduced || !this.visible) return;
  this.raf = raf(this.frame);
  if (now - this.lastPaint < 1000 / q.fps - 2) return;   // lewati frame layar sampai giliran fps target
  this.lastPaint = now;

  var t0 = performance.now(), dt = Math.min(0.1, (now - this.last) / 1000), steps = 0;
  this.last = now;
  this.acc += dt;
  while (this.acc >= STEP && steps < MAX_STEPS) { this.world.step(STEP); this.acc -= STEP; steps++; }
  if (steps === MAX_STEPS) this.acc = 0;
  this.paint(dt);
  this.measure(performance.now() - t0, q);
};

// Ukur waktu frame di perangkat pengunjung; kalau terlalu lama, turunkan kualitas satu tingkat.
Scene.prototype.measure = function (ms, q) {
  if (this.settled) return;
  this.samples.push(ms);
  if (this.samples.length < PROBE) return;
  var med = this.samples.sort(function (x, y) { return x - y; })[PROBE >> 1];
  this.samples = [];
  if (med <= q.slow) { this.settled = true; return; }   // cukup cepat: berhenti mengukur
  this.level++;
  if (this.quality[this.level]) this.resize(this.w, this.h, this.dpr);
  else this.paintStill();
};
