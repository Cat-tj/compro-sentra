// Inti laut ASCII Sentra: simulasi, render, dan kualitas adaptif.
// Tanpa DOM, jadi bisa jalan di Web Worker (OffscreenCanvas) maupun di thread utama sebagai cadangan.
import { World } from "./world.js?v=20261029h";
import { AsciiRenderer } from "./renderer.js?v=20261029h";

var STEP = 1 / 60, MAX_STEPS = 4;
var PROBE = 45;            // jumlah frame yang diukur sebelum memutuskan tingkat kualitas

export var FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace";

// Tingkat kualitas, dari terbaik ke teringan; null = satu frame diam.
// slow: median waktu frame (ms) yang membuat scene turun satu tingkat.
// Hero: laut terang (light mode). Footer: laut gelap, lebih hemat.
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

// Gaya ascii-sharks asli: hiu berwarna solid, ikan sebagai -, ><, <=>, <>.
// Footer: laut gelap, gradient dari biru tua (menyambung CTA di atasnya) ke navy gelap, tidak hitam pekat.
var DARK = {
  bg: "#0E2150",
  bgGradient: ["#13306B", "#081530"],
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

// Hero (light mode): air biru terang, ikan warna-warni seperti ikan hias, hiu yang kontras di latar biru.
var LIGHT = {
  bg: "#C7E2FF",
  grid: "rgba(44,91,184,0.08)",
  wake: [30, 110, 210],
  wakeAlpha: 0.55,
  sharks: [
    [1.95, 1.08, 0.3],     // oranye (lebih terang dari versi gelap supaya tidak kecokelatan di latar biru)
    [0.34, 0.5, 1.6],      // biru tua
    [1.95, 0.72, 0.62],    // coral
  ],
  fish: [
    { glyph: "-", far: "rgba(232,89,12,.55)", near: "rgba(232,89,12,.95)" },       // oranye
    { glyph: "-", far: "rgba(201,140,0,.55)", near: "rgba(201,140,0,.95)" },       // kuning
    { glyph: "><", far: "rgba(214,51,108,.55)", near: "rgba(214,51,108,.95)" },    // pink
    { glyph: "<=>", far: "rgba(8,140,126,.6)", near: "rgba(8,140,126,.95)" },      // toska
    { glyph: "<>", far: "rgba(112,72,232,.55)", near: "rgba(112,72,232,.95)" },    // ungu
  ],
};

var raf = typeof requestAnimationFrame === "function" ? requestAnimationFrame.bind(self) : function (cb) { return setTimeout(function () { cb(performance.now()); }, 16); };
var caf = typeof cancelAnimationFrame === "function" ? cancelAnimationFrame.bind(self) : clearTimeout;

// opts: { preset: nama di PRESETS, level: tingkat awal }
export function Scene(canvas, opts) {
  this.canvas = canvas;
  this.quality = PRESETS[opts.preset];
  this.level = Math.min(opts.level || 0, this.quality.length - 2);
  this.world = new World();
  this.sharkSpecs = this.world.sharkSpecs;   // hiu dipanggil ulang tiap resize; tingkat kualitas memangkas jumlahnya
  this.renderer = new AsciiRenderer(canvas);
  this.renderer.setFontFamily(FONT);
  this.theme = opts.preset.indexOf("hero") === 0 ? LIGHT : DARK;
  this.renderer.setTheme(this.theme);
  this.w = 0; this.h = 0; this.dpr = 1;
  this.raf = 0; this.last = 0; this.lastPaint = 0; this.acc = 0;
  this.visible = true; this.reduced = false; this.settled = false; this.samples = [];
  var self = this;
  this.frame = function (now) { self.tick(now); };
}

Scene.prototype.still = function () { return this.reduced || !this.quality[this.level]; };

Scene.prototype.resize = function (w, h, dpr) {
  if (w < 1 || h < 1) return;
  this.w = w; this.h = h; this.dpr = dpr;
  var q = this.quality[this.level] || this.quality[this.quality.length - 2];
  this.world.sharkSpecs = this.sharkSpecs.slice(0, q.sharks);
  this.renderer.resize(w, h, Math.min(dpr, q.dpr));
  // Jarak antarikan dihitung dalam sel; sedikit diperlebar supaya ikan "<=>" dan "><" tidak saling tumpuk.
  this.world.resize(w, h, this.renderer.cellWidth * 1.4, this.renderer.cellHeight);
  if (this.still()) this.paintStill(); else this.schedule();
};

Scene.prototype.setVisible = function (v) { this.visible = v; this.schedule(); };
Scene.prototype.setReduced = function (r) { this.reduced = r; if (r) this.paintStill(); else this.schedule(); };
Scene.prototype.pointer = function (x, y, active) { var p = this.world.pointer; p.x = x; p.y = y; p.active = active; };
Scene.prototype.splash = function (x, y) { if (!this.still()) this.world.splash(x, y); };

Scene.prototype.paint = function (dt) {
  this.renderer.render(this.world, dt);
};

// Satu frame diam (reduced motion atau perangkat terlalu lemah): biarkan ekosistem tenang dulu.
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
