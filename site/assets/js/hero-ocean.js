// Hero beranda: laut ASCII (hiu + kawanan ikan) dengan logo Sentra sebagai koin ASCII yang berputar.
// Ikan dan hiu lewat di belakang koin: sel koin selalu menimpa apa pun yang digambar sebelumnya.
import { World } from "./ocean/world.js";
import { AsciiRenderer, BG } from "./ocean/renderer.js";

var STEP = 1 / 60, MAX_STEPS = 4;
var SPIN = 5.2;            // detik per putaran penuh
var LOGO_SCALE = 0.78;     // logo menempati 78% radius muka koin
var FACE_RAMP = " .:-=+*%#@";

function coinTexture(src, size, done) {
  var img = new Image();
  img.onload = function () {
    var c = document.createElement("canvas");
    c.width = c.height = size;
    var g = c.getContext("2d", { willReadFrequently: true });
    g.drawImage(img, 0, 0, size, size);
    done(g.getImageData(0, 0, size, size).data);
  };
  img.src = src;
}

function Coin(slot) {
  this.slot = slot;
  this.tex = null;
  this.texSize = 220;
  this.cx = 0; this.cy = 0; this.r = 0;
  var self = this;
  coinTexture(slot.getAttribute("data-logo"), this.texSize, function (d) { self.tex = d; });
}

Coin.prototype.place = function (canvas) {
  var c = canvas.getBoundingClientRect(), s = this.slot.getBoundingClientRect();
  this.cx = s.left - c.left + s.width / 2;
  this.cy = s.top - c.top + s.height / 2;
  this.r = Math.min(s.width, s.height) / 2;
};

// Cakupan tekstur terkuat dari 3x3 sampel di dalam satu sel, dalam ruang muka koin [-1, 1].
// Pakai maksimum, bukan rata-rata: garis cincin logo lebih tipis dari satu sel dan akan pudar kalau dirata-rata.
Coin.prototype.sample = function (u, v, du, dv, out) {
  var n = this.texSize, d = this.tex;
  out.a = 0;
  for (var k = 0; k < 9; k++) {
    var su = (u + ((k % 3) - 1) * 0.4 * du) / LOGO_SCALE;
    var sv = (v + (((k / 3) | 0) - 1) * 0.4 * dv) / LOGO_SCALE;
    var x = Math.round((su * 0.5 + 0.5) * (n - 1)), y = Math.round((sv * 0.5 + 0.5) * (n - 1));
    if (x < 0 || y < 0 || x >= n || y >= n) continue;
    var i = (y * n + x) * 4, al = d[i + 3] / 255;
    if (al > out.a) { out.a = al; out.r = d[i]; out.g = d[i + 1]; out.b = d[i + 2]; }
  }
};

Coin.prototype.draw = function (ctx, cw, ch, t) {
  var R = this.r;
  if (R < 8) return;
  var th = t * Math.PI * 2 / SPIN;
  var cos = Math.cos(th), sin = Math.sin(th);
  var a = R * Math.abs(cos);              // setengah lebar muka koin yang terlihat
  var d = R * 0.13 * sin;                 // tebal tepi koin, terlihat saat miring
  var cy = this.cy + Math.sin(t * 1.3) * R * 0.04;
  var light = 0.5 + 0.5 * Math.abs(cos);
  var glint = sin * 0.9;                  // pita kilau yang menyapu muka koin
  var s = { a: 0, r: 0, g: 0, b: 0 };

  var c0 = Math.floor((this.cx - R - Math.abs(d)) / cw), c1 = Math.ceil((this.cx + R + Math.abs(d)) / cw);
  var r0 = Math.floor((cy - R) / ch), r1 = Math.ceil((cy + R) / ch);
  for (var row = r0; row <= r1; row++) {
    var y = row * ch + ch / 2, v = (y - cy) / R;
    if (v <= -1 || v >= 1) continue;
    var w = Math.sqrt(1 - v * v), half = a * w;
    var lo = Math.min(0, -d) - half, hi = Math.max(0, -d) + half;
    for (var col = c0; col <= c1; col++) {
      var x = col * cw + cw / 2, dx = x - this.cx;
      var face = a > 0.5 && Math.abs(dx) <= half;
      if (!face && (dx < lo || dx > hi)) continue;

      ctx.fillStyle = BG;
      ctx.fillRect(col * cw, row * ch, cw, ch);

      if (!face) {
        ctx.fillStyle = "rgba(120,150,210," + (0.55 + 0.35 * Math.abs(sin)).toFixed(2) + ")";
        ctx.fillText(a < cw ? "|" : dx < 0 ? "[" : "]", x, y + 1);
        continue;
      }

      var u = dx / a, rr = Math.sqrt(u * u + v * v);
      var shine = Math.exp(-Math.pow(u + v * 0.35 - glint, 2) / 0.04);
      if (rr > 0.9) {
        var k = Math.min(1, light + shine * 0.5);
        ctx.fillStyle = "rgb(" + Math.round(150 * k) + "," + Math.round(180 * k) + "," + Math.round(235 * k) + ")";
        ctx.fillText(rr > 0.96 ? "o" : "O", x, y + 1);
        continue;
      }
      if (this.tex) this.sample(u, v, cw / a, ch / R, s); else s.a = 0;
      if (s.a > 0.2) {
        var lift = (light + shine * 0.6) * 1.7;
        var gi = Math.min(FACE_RAMP.length - 1, 5 + Math.floor(s.a * 4.99));
        ctx.fillStyle = "rgb(" + Math.min(255, Math.round(s.r * lift + 40)) + "," + Math.min(255, Math.round(s.g * lift + 46)) + "," + Math.min(255, Math.round(s.b * lift + 52)) + ")";
        ctx.fillText(FACE_RAMP[gi], x, y + 1);
      } else if (((col * 7 + row * 13) & 3) === 0 || shine > 0.35) {
        ctx.fillStyle = "rgba(110,140,200," + (0.1 + 0.45 * shine).toFixed(2) + ")";
        ctx.fillText(shine > 0.35 ? ":" : ".", x, y + 1);
      }
    }
  }
};

function OceanHero(canvas, slot) {
  this.canvas = canvas;
  this.world = new World();
  this.renderer = new AsciiRenderer(canvas);
  this.renderer.setFontFamily(getComputedStyle(canvas).fontFamily);
  this.coin = slot ? new Coin(slot) : null;
  this.ctx = canvas.getContext("2d");
  this.raf = 0; this.last = 0; this.acc = 0; this.visible = true;
  this.reduced = window.matchMedia("(prefers-reduced-motion: reduce)");

  var self = this;
  this.frame = function (now) { self.tick(now); };
  new ResizeObserver(function () { self.resize(); }).observe(canvas);
  if (slot) new ResizeObserver(function () { self.resize(); }).observe(slot);
  new IntersectionObserver(function (e) { self.visible = e[0].isIntersecting; self.schedule(); }).observe(canvas);
  this.reduced.addEventListener("change", function () { self.reduced.matches ? self.still() : self.schedule(); });

  window.addEventListener("pointermove", function (e) {
    var p = self.local(e), ptr = self.world.pointer;
    ptr.x = p.x; ptr.y = p.y; ptr.active = p.inside && e.pointerType !== "touch";
  }, { passive: true });
  window.addEventListener("pointerdown", function (e) {
    var p = self.local(e);
    if (p.inside && !self.reduced.matches && !e.target.closest("a,button,summary,input")) self.world.splash(p.x, p.y);
  }, { passive: true });
  document.documentElement.addEventListener("pointerleave", function () { self.world.pointer.active = false; });

  this.resize();
  if (document.fonts) document.fonts.load("600 16px " + getComputedStyle(canvas).fontFamily).then(function () { if (self.reduced.matches) self.still(); });
  this.schedule();
}

OceanHero.prototype.local = function (e) {
  var r = this.canvas.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
  return { x: x, y: y, inside: x >= 0 && y >= 0 && x <= r.width && y <= r.height };
};

OceanHero.prototype.resize = function () {
  var r = this.canvas.getBoundingClientRect();
  if (r.width < 1 || r.height < 1) return;
  this.renderer.resize(r.width, r.height, Math.min(window.devicePixelRatio || 1, 2));
  this.world.resize(r.width, r.height, this.renderer.cellWidth, this.renderer.cellHeight);
  if (this.coin) this.coin.place(this.canvas);
  if (this.reduced.matches) this.still();
};

OceanHero.prototype.paint = function (dt) {
  this.renderer.render(this.world, dt);
  if (this.coin) this.coin.draw(this.ctx, this.renderer.cellWidth, this.renderer.cellHeight, this.reduced.matches ? 0 : this.world.time);
};

OceanHero.prototype.schedule = function () {
  cancelAnimationFrame(this.raf);
  if (!this.visible || this.reduced.matches) return;
  this.last = performance.now();
  this.raf = requestAnimationFrame(this.frame);
};

OceanHero.prototype.tick = function (now) {
  var dt = Math.min(0.1, (now - this.last) / 1000), steps = 0;
  this.last = now;
  this.acc += dt;
  while (this.acc >= STEP && steps < MAX_STEPS) { this.world.step(STEP); this.acc -= STEP; steps++; }
  if (steps === MAX_STEPS) this.acc = 0;
  this.paint(dt);
  this.raf = requestAnimationFrame(this.frame);
};

// Reduced motion: biarkan ekosistem tenang dulu, lalu tampilkan satu frame dengan koin menghadap depan.
OceanHero.prototype.still = function () {
  if (this.world.time < 4) for (var i = 0; i < 240; i++) this.world.step(STEP);
  this.paint(STEP);
};

var canvas = document.querySelector(".hero-ocean canvas");
if (canvas && canvas.getContext) {
  var hero = new OceanHero(canvas, document.querySelector(".hero-coin"));
  // Teksturnya dimuat asinkron; gambar ulang frame diam begitu logo siap.
  if (hero.coin) setTimeout(function () { if (hero.reduced.matches) hero.still(); }, 400);
}
