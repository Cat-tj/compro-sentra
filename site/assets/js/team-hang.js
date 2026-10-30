/* Kartu tim menggantung. Ayunan pegas ringan, miring mengikuti kursor, dan saat disentuh foto "dimakan" glyph ASCII
   sampai habis lalu bio muncul. Satu loop animasi dipakai bersama dan berhenti sendiri saat semua kartu diam. */
(() => {
  const cards = [...document.querySelectorAll(".hcard")];
  if (!cards.length) return;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const GL = " .:-=+*#%@";
  const CELL = 7;
  const DUR = 0.75;
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

  class Card {
    constructor(li) {
      this.li = li;
      this.swing = li.querySelector(".hc-swing");
      this.btn = li.querySelector(".hc-tilt");
      this.img = li.querySelector("img");
      this.cv = li.querySelector("canvas");
      this.nameEl = li.querySelector(".hc-info");
      this.bioEl = li.querySelector(".hc-bio");
      this.a = 0; this.v = 0;
      this.p = 0; this.target = 0;
      this.ox = 0.5; this.oy = 0.4;
      this.ready = false;
      this.on = false;
    }
    prep() {
      if (this.ready || !this.img.complete || !this.img.naturalWidth) return this.ready;
      const W = this.W = this.btn.offsetWidth, H = this.H = this.btn.offsetHeight;
      this.cv.width = W * DPR; this.cv.height = H * DPR;
      this.ctx = this.cv.getContext("2d");
      this.ctx.scale(DPR, DPR);
      this.cols = Math.ceil(W / CELL); this.rows = Math.ceil(H / CELL);
      const s = this.cover = (() => {
        const k = Math.max(W / this.img.naturalWidth, H / this.img.naturalHeight);
        const w = this.img.naturalWidth * k, h = this.img.naturalHeight * k;
        return { x: (W - w) / 2, y: (H - h) * 0.2, w, h };
      })();
      // contoh warna per sel dari versi kecil foto yang sama
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
        ctx.fillStyle = `rgba(14,37,86,${0.15 + 0.85 * q})`;
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
      this.nameEl.style.opacity = 1 - smooth(p, 0.15, 0.55);
      this.bioEl.style.opacity = smooth(p, 0.75, 1.15);
      this.bioEl.style.transform = `translateY(${(1 - smooth(p, 0.75, 1.2)) * 8}px)`;
      if (this.ready) this.draw();
    }
    setOn(on, e) {
      if (on === this.on) return;
      this.on = on;
      this.btn.setAttribute("aria-pressed", on);
      if (on) {
        this.prep();
        if (e && this.ready) {
          const b = this.btn.getBoundingClientRect();
          this.ox = clamp((e.clientX - b.left) / b.width, 0, 1);
          this.oy = clamp((e.clientY - b.top) / b.height, 0, 1);
        } else { this.ox = 0.5; this.oy = 0.4; }
        if (this.ready) this.thresholds();
      }
      this.target = on ? 1.28 : 0;
      if (reduce) { this.p = this.target; this.paint(); return; }
      active.add(this); kick();
    }
    impulse(dv) { if (reduce) return; this.v = clamp(this.v + dv, -22, 22); active.add(this); kick(); }
    step(dt) {
      let busy = false;
      if (this.v || this.a) {
        this.v += (-46 * this.a - 3.4 * this.v) * dt;
        this.a += this.v * dt;
        if (Math.abs(this.a) < 0.03 && Math.abs(this.v) < 0.12) { this.a = 0; this.v = 0; this.swing.style.transform = ""; }
        else { this.swing.style.transform = `rotate(${this.a.toFixed(3)}deg)`; busy = true; }
      }
      if (this.p !== this.target) {
        const d = (this.target ? 1 : -1) * dt / DUR * 1.28;
        this.p = this.target ? Math.min(this.target, this.p + d) : Math.max(0, this.p + d * 1.4);
        this.paint(); busy = true;
      }
      if (!busy) active.delete(this);
    }
  }

  const list = cards.map((li) => new Card(li));
  list.forEach((c) => {
    const b = c.btn;
    b.addEventListener("pointerenter", (e) => { if (e.pointerType === "mouse") c.setOn(true, e); });
    b.addEventListener("pointerleave", (e) => {
      if (e.pointerType === "mouse") c.setOn(false);
      b.style.setProperty("--rx", "0deg"); b.style.setProperty("--ry", "0deg");
    });
    b.addEventListener("pointermove", (e) => {
      if (e.pointerType !== "mouse") return;
      const r = b.getBoundingClientRect();
      const mx = (e.clientX - r.left) / r.width, my = (e.clientY - r.top) / r.height;
      if (!reduce) {
        b.style.setProperty("--rx", `${((0.5 - my) * 9).toFixed(2)}deg`);
        b.style.setProperty("--ry", `${((mx - 0.5) * 11).toFixed(2)}deg`);
      }
      b.style.setProperty("--mx", `${(mx * 100).toFixed(1)}%`);
      b.style.setProperty("--my", `${(my * 100).toFixed(1)}%`);
      c.impulse(e.movementX * 0.35);
    });
    b.addEventListener("click", (e) => {
      if (e.pointerType === "mouse" && e.detail > 0) return; // di mouse, hover sudah mengurus
      list.forEach((o) => o !== c && o.setOn(false));
      c.setOn(!c.on, e);
    });
    b.addEventListener("keydown", (e) => { if (e.key === "Escape") c.setOn(false); });
  });

  // rel yang bisa digeser: kartu ikut berayun berlawanan arah geseran
  document.querySelectorAll(".hang-rail").forEach((rail) => {
    let x0 = rail.scrollLeft;
    const mine = list.filter((c) => rail.contains(c.li));
    rail.addEventListener("scroll", () => {
      const d = rail.scrollLeft - x0; x0 = rail.scrollLeft;
      mine.forEach((c) => c.impulse(-d * 0.22));
    }, { passive: true });
  });

  // muat gambar lalu siapkan canvas; ukuran dihitung ulang kalau jendela berubah
  list.forEach((c) => { if (c.img.complete) c.prep(); else c.img.addEventListener("load", () => c.prep(), { once: true }); });
  let rz;
  addEventListener("resize", () => { clearTimeout(rz); rz = setTimeout(() => list.forEach((c) => { c.ready = false; if (c.on) { c.prep(); c.thresholds(); c.paint(); } }), 200); });
})();
