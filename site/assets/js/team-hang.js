/* Section tim: grid kartu seragam dengan tab divisi. Saat disentuh, foto "dimakan" glyph ASCII mulai dari titik
   kursor masuk sampai habis, lalu bio muncul. Satu loop animasi dipakai bersama dan berhenti sendiri saat diam. */
(() => {
  const grid = document.querySelector(".tgrid");
  if (!grid) return;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const GL = " .:-=+*#%@";
  const CELL = 7;
  const DUR = 0.7;
  const DPR = Math.min(2, window.devicePixelRatio || 1);
  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
  const smooth = (x, a, b) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };

  const active = new Set();
  let running = false, last = 0;
  const kick = () => { if (!running) { running = true; last = performance.now(); requestAnimationFrame(tick); } };
  const tick = (t) => {
    const dt = Math.min(0.033, (t - last) / 1000); last = t;
    active.forEach((c) => c.step(dt));
    if (active.size) requestAnimationFrame(tick); else running = false;
  };

  class Tile {
    constructor(li) {
      this.li = li;
      this.btn = li.querySelector(".tile-btn");
      this.img = li.querySelector("img");
      this.cv = li.querySelector("canvas");
      this.info = li.querySelector(".tile-info");
      this.tag = li.querySelector(".tile-div");
      this.bio = li.querySelector(".tile-bio");
      this.p = 0; this.target = 0; this.ox = 0.5; this.oy = 0.4;
      this.ready = false; this.on = false;
    }
    prep() {
      if (this.ready) return true;
      if (!this.btn.offsetWidth) return false;
      if (!this.img.complete || !this.img.naturalWidth) return false;
      const W = this.W = this.btn.offsetWidth, H = this.H = this.btn.offsetHeight;
      this.cv.width = W * DPR; this.cv.height = H * DPR;
      this.ctx = this.cv.getContext("2d");
      this.ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      this.cols = Math.ceil(W / CELL); this.rows = Math.ceil(H / CELL);
      const k = Math.max(W / this.img.naturalWidth, H / this.img.naturalHeight);
      const w = this.img.naturalWidth * k, h = this.img.naturalHeight * k;
      const s = this.cover = { x: (W - w) / 2, y: (H - h) * 0.2, w, h };
      const tiny = document.createElement("canvas");
      tiny.width = this.cols; tiny.height = this.rows;
      const tc = tiny.getContext("2d", { willReadFrequently: true });
      tc.drawImage(this.img, s.x / CELL, s.y / CELL, s.w / CELL, s.h / CELL);
      this.px = tc.getImageData(0, 0, this.cols, this.rows).data;
      this.rnd = Float32Array.from({ length: this.cols * this.rows }, () => Math.random());
      this.ready = true;
      return true;
    }
    thresholds() {
      const { cols, rows } = this;
      const ox = this.ox * cols, oy = this.oy * rows;
      const maxd = Math.hypot(Math.max(ox, cols - ox), Math.max(oy, rows - oy));
      this.th = new Float32Array(cols * rows);
      for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
        const i = r * cols + c;
        this.th[i] = 0.62 * (Math.hypot(c - ox, r - oy) / maxd) + 0.38 * this.rnd[i];
      }
    }
    draw() {
      const p = this.p, ctx = this.ctx, { W, H, cols, rows, px, th, cover: s } = this;
      ctx.clearRect(0, 0, W, H);
      if (p <= 0.001) return;
      ctx.drawImage(this.img, s.x, s.y, s.w, s.h);
      ctx.font = `500 ${CELL + 1}px "JetBrains Mono", ui-monospace, monospace`;
      ctx.textAlign = "center";
      for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
        const i = r * cols + c;
        const q = clamp((p - th[i]) / 0.28, 0, 1);
        if (q <= 0) continue;
        const x = c * CELL, y = r * CELL;
        ctx.fillStyle = `rgba(22,52,127,${0.15 + 0.85 * q})`;
        ctx.fillRect(x, y, CELL, CELL);
        const o = i * 4, lum = (px[o] * 0.3 + px[o + 1] * 0.59 + px[o + 2] * 0.11) / 255;
        const ch = GL[Math.round(clamp(lum * 1.15, 0, 1) * (GL.length - 1))];
        if (ch === " ") continue;
        const mix = 0.55 + 0.45 * q;
        const R = Math.round(px[o] * (1 - mix) + 120 * mix), G = Math.round(px[o + 1] * (1 - mix) + 170 * mix), B = Math.round(px[o + 2] * (1 - mix) + 245 * mix);
        ctx.fillStyle = `rgba(${R},${G},${B},${q >= 1 ? 0.5 : 0.95})`;
        ctx.fillText(ch, x + CELL / 2, y + CELL - 1);
      }
    }
    paint() {
      const p = this.p;
      const fade = 1 - smooth(p, 0.15, 0.55);
      this.info.style.opacity = fade; this.tag.style.opacity = fade;
      this.bio.style.opacity = smooth(p, 0.75, 1.15);
      this.bio.style.transform = `translateY(${(1 - smooth(p, 0.75, 1.2)) * 8}px)`;
      if (this.ready) this.draw();
    }
    setOn(on, e) {
      if (on === this.on) return;
      this.on = on;
      this.btn.setAttribute("aria-pressed", on);
      if (on) {
        this.prep();
        this.ox = 0.5; this.oy = 0.4;
        if (e && typeof e.clientX === "number" && e.clientX + e.clientY > 0) {
          const b = this.btn.getBoundingClientRect();
          this.ox = clamp((e.clientX - b.left) / b.width, 0, 1);
          this.oy = clamp((e.clientY - b.top) / b.height, 0, 1);
        }
        if (this.ready) this.thresholds();
      }
      this.target = on ? 1.28 : 0;
      if (reduce) { this.p = this.target; this.paint(); return; }
      active.add(this); kick();
    }
    step(dt) {
      if (this.p === this.target) { active.delete(this); return; }
      const d = dt / DUR * 1.28;
      this.p = this.target ? Math.min(this.target, this.p + d) : Math.max(0, this.p - d * 1.4);
      this.paint();
    }
  }

  const tiles = [...grid.querySelectorAll(".tile")].map((li) => new Tile(li));
  tiles.forEach((t) => {
    const b = t.btn;
    b.addEventListener("pointerenter", (e) => { if (e.pointerType === "mouse") t.setOn(true, e); });
    b.addEventListener("pointerleave", (e) => { if (e.pointerType === "mouse") t.setOn(false); });
    b.addEventListener("click", (e) => {
      if (e.pointerType === "mouse" && e.detail > 0) return; // di mouse, hover sudah mengurus
      tiles.forEach((o) => o !== t && o.setOn(false));
      t.setOn(!t.on, e);
    });
    b.addEventListener("keydown", (e) => { if (e.key === "Escape") t.setOn(false); });
    if (t.img.complete) t.prep(); else t.img.addEventListener("load", () => t.prep(), { once: true });
  });

  // tab divisi: kartu yang tidak sesuai disembunyikan, sisanya masuk berurutan dari kiri
  const tabs = [...document.querySelectorAll(".tg-filter button")];
  const apply = (f) => {
    let i = 0;
    tiles.forEach((t) => {
      t.setOn(false);
      const show = f === "all" || t.li.dataset.div === f;
      t.li.hidden = !show;
      if (show) t.li.style.setProperty("--i", i++);
    });
    grid.scrollLeft = 0;
    grid.classList.remove("go"); void grid.offsetWidth; grid.classList.add("go");
    sync();
  };
  tabs.forEach((tb) => tb.addEventListener("click", () => {
    tabs.forEach((o) => o.setAttribute("aria-pressed", o === tb));
    apply(tb.dataset.f);
  }));

  // panah dan garis progres
  const prev = document.querySelector(".tc-prev"), next = document.querySelector(".tc-next"), thumb = document.querySelector(".tc-thumb");
  const sync = () => {
    const max = grid.scrollWidth - grid.clientWidth;
    const frac = grid.clientWidth / Math.max(grid.scrollWidth, 1);
    thumb.style.width = Math.min(100, frac * 100) + "%";
    thumb.style.left = (max > 1 ? (grid.scrollLeft / max) * (100 - frac * 100) : 0) + "%";
    prev.disabled = grid.scrollLeft < 8; next.disabled = grid.scrollLeft > max - 8;
  };
  const step = () => (grid.querySelector(".tile:not([hidden])")?.offsetWidth || 240) + 16;
  prev.addEventListener("click", () => grid.scrollBy({ left: -step() * 2, behavior: reduce ? "auto" : "smooth" }));
  next.addEventListener("click", () => grid.scrollBy({ left: step() * 2, behavior: reduce ? "auto" : "smooth" }));
  grid.addEventListener("scroll", () => requestAnimationFrame(sync), { passive: true });
  sync();

  let rz;
  addEventListener("resize", () => {
    clearTimeout(rz);
    rz = setTimeout(() => { sync(); tiles.forEach((t) => { t.ready = false; t.prep(); if (t.on) { t.thresholds(); t.paint(); } }); }, 200);
  });
})();
