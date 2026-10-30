/* Section tim: satu kartu utama + grid 13 thumbnail, semuanya tampil tanpa scroll. Memilih orang lain membuat foto
   di kartu utama "dimakan" glyph ASCII, isinya berganti, lalu foto baru muncul dari glyph. Satu loop animasi saja. */
(() => {
  const root = document.querySelector(".tmeet");
  if (!root) return;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const GL = " .:-=+*#%@";
  const CELL = 8;
  const DPR = Math.min(2, window.devicePixelRatio || 1);
  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
  const smooth = (x, a, b) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };

  const thumbs = [...root.querySelectorAll(".tm-thumb")];
  const feat = root.querySelector(".tfeat");
  const fimg = feat.querySelector(".tf-photo img");
  const cv = feat.querySelector("canvas");
  const info = feat.querySelector(".tf-info");
  const $ = (s) => info.querySelector(s);
  const ctx = cv.getContext("2d");
  const MAXP = 1.28;

  let cur = 0, want = 0, phase = "idle", p = 0, last = 0, running = false;
  let W = 0, H = 0, cols = 0, rows = 0, th = null, samples = {};

  const measure = () => {
    W = cv.parentNode.offsetWidth; H = cv.parentNode.offsetHeight;
    cv.width = W * DPR; cv.height = H * DPR; ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    cols = Math.ceil(W / CELL); rows = Math.ceil(H / CELL);
    const ox = cols * 0.5, oy = rows * 0.38, maxd = Math.hypot(Math.max(ox, cols - ox), Math.max(oy, rows - oy));
    th = new Float32Array(cols * rows);
    for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++)
      th[r * cols + c] = 0.62 * (Math.hypot(c - ox, r - oy) / maxd) + 0.38 * Math.random();
    samples = {};
  };

  const cover = (im) => {
    const k = Math.max(W / im.naturalWidth, H / im.naturalHeight);
    const w = im.naturalWidth * k, h = im.naturalHeight * k;
    return { x: (W - w) / 2, y: (H - h) * 0.2, w, h };
  };
  const sample = (i) => {
    if (samples[i]) return samples[i];
    const im = thumbs[i].querySelector("img"), s = cover(im);
    const t = document.createElement("canvas"); t.width = cols; t.height = rows;
    const tc = t.getContext("2d", { willReadFrequently: true });
    tc.drawImage(im, s.x / CELL, s.y / CELL, s.w / CELL, s.h / CELL);
    return (samples[i] = tc.getImageData(0, 0, cols, rows).data);
  };

  const draw = () => {
    ctx.clearRect(0, 0, W, H);
    if (p <= 0.001) return;
    const im = thumbs[cur].querySelector("img");
    if (!im.complete || !im.naturalWidth) return;
    const s = cover(im), px = sample(cur);
    ctx.drawImage(im, s.x, s.y, s.w, s.h);
    ctx.font = `500 ${CELL + 1}px "JetBrains Mono", ui-monospace, monospace`;
    ctx.textAlign = "center";
    for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
      const i = r * cols + c, q = clamp((p - th[i]) / 0.28, 0, 1);
      if (q <= 0) continue;
      const x = c * CELL, y = r * CELL;
      ctx.fillStyle = `rgba(22,52,127,${0.15 + 0.85 * q})`;
      ctx.fillRect(x, y, CELL, CELL);
      const o = i * 4, lum = (px[o] * 0.3 + px[o + 1] * 0.59 + px[o + 2] * 0.11) / 255;
      const ch = GL[Math.round(clamp(lum * 1.15, 0, 1) * (GL.length - 1))];
      if (ch === " ") continue;
      const mix = 0.55 + 0.45 * q;
      const R = Math.round(px[o] * (1 - mix) + 120 * mix), G = Math.round(px[o + 1] * (1 - mix) + 170 * mix), B = Math.round(px[o + 2] * (1 - mix) + 245 * mix);
      ctx.fillStyle = `rgba(${R},${G},${B},${q >= 1 ? 0.55 : 0.95})`;
      ctx.fillText(ch, x + CELL / 2, y + CELL - 1);
    }
  };

  const commit = (i) => {
    cur = i;
    const t = thumbs[i];
    fimg.src = t.dataset.src;
    $(".tf-div").textContent = t.dataset.div;
    $(".tf-div").dataset.d = t.dataset.code;
    $(".tf-name").textContent = t.dataset.name;
    $(".tf-role").textContent = t.dataset.role;
    $(".tf-bio").textContent = t.dataset.bio;
  };

  const tick = (now) => {
    const dt = Math.min(0.033, (now - last) / 1000); last = now;
    if (phase === "out") {
      p += dt / 0.34 * MAXP;
      if (p >= MAXP) { p = MAXP; commit(want); phase = "in"; }
    } else if (phase === "in") {
      p -= dt / 0.55 * MAXP;
      if (want !== cur) phase = "out";
      else if (p <= 0) { p = 0; phase = "idle"; }
    }
    info.style.opacity = 1 - smooth(p, 0.1, 0.7);
    info.style.transform = `translateY(${smooth(p, 0.1, 0.9) * 10}px)`;
    draw();
    if (phase !== "idle") requestAnimationFrame(tick); else running = false;
  };

  const select = (i, fromTouch) => {
    thumbs.forEach((t, k) => t.setAttribute("aria-pressed", k === i));
    want = i;
    if (reduce) { commit(i); return; }
    if (phase === "idle" && want === cur) return;
    if (phase === "idle") phase = "out";
    if (!running) { running = true; last = performance.now(); requestAnimationFrame(tick); }
    if (fromTouch && matchMedia("(max-width: 899px)").matches) {
      const r = feat.getBoundingClientRect();
      if (r.top < 70 || r.bottom > innerHeight) feat.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

  let hv;
  thumbs.forEach((t, i) => {
    t.addEventListener("pointerenter", (e) => { if (e.pointerType === "mouse") { clearTimeout(hv); hv = setTimeout(() => select(i), 70); } });
    t.addEventListener("pointerleave", () => clearTimeout(hv));
    t.addEventListener("click", () => select(i, true));
    t.addEventListener("focus", () => select(i));
  });

  // tab divisi: thumbnail di luar divisi meredup, kartu utama pindah ke orang pertama divisi itu
  const tabs = [...document.querySelectorAll(".tg-filter button")];
  tabs.forEach((tb) => tb.addEventListener("click", () => {
    const f = tb.dataset.f;
    tabs.forEach((o) => o.setAttribute("aria-pressed", o === tb));
    root.dataset.f = f;
    let first = -1;
    thumbs.forEach((t, k) => {
      const ok = f === "all" || t.dataset.code === f;
      t.disabled = !ok;
      if (ok && first < 0) first = k;
    });
    if (first >= 0) select(first);
  }));

  const init = () => { measure(); if (p > 0) draw(); };
  init();
  let rz;
  addEventListener("resize", () => { clearTimeout(rz); rz = setTimeout(init, 150); });
})();
