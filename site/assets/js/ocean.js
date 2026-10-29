// Laut ASCII di dua tempat:
// - hero beranda: hiu + kawanan ikan, dengan logo Sentra sebagai koin ASCII yang berputar.
// - footer semua halaman: kawanan ikan "><>" saja.
// Gambar dan simulasi berjalan di Web Worker (ocean-worker.js) supaya scroll tetap mulus.
// Browser tanpa OffscreenCanvas memakai cadangan di thread utama dengan kualitas lebih rendah.
var V = "20261029f";

function weakDevice() {
  var c = navigator.connection;
  return (navigator.hardwareConcurrency || 8) <= 4 || (navigator.deviceMemory || 8) <= 4 || !!(c && c.saveData);
}

// HP dan tablet: layar sempit, atau layar sentuh tanpa hover.
function phone() {
  return window.matchMedia("(max-width: 767px), (hover: none) and (pointer: coarse)").matches;
}

function logoTexture(src, n, done) {
  var img = new Image();
  img.onload = function () {
    var c = document.createElement("canvas");
    c.width = c.height = n;
    var g = c.getContext("2d", { willReadFrequently: true });
    g.drawImage(img, 0, 0, n, n);
    done({ data: g.getImageData(0, 0, n, n).data, n: n });
  };
  img.src = src;
}

function mount(canvas, preset, slot) {
  var weak = weakDevice(), reducedMq = window.matchMedia("(prefers-reduced-motion: reduce)");
  var hero = preset === "hero", mobile = phone();
  var level = weak ? (hero && !mobile ? 2 : 1) : 0;
  if (mobile) preset += "-mobile";
  var send = null, queue = [];

  function post(m, transfer) { if (send) send(m, transfer); else queue.push([m, transfer]); }
  function size() {
    var r = canvas.getBoundingClientRect();
    return { w: r.width, h: r.height, dpr: window.devicePixelRatio || 1 };
  }
  function coinGeom() {
    var c = canvas.getBoundingClientRect(), s = slot.getBoundingClientRect();
    return { cx: s.left - c.left + s.width / 2, cy: s.top - c.top + s.height / 2, r: Math.min(s.width, s.height) / 2 };
  }
  function local(e) {
    var r = canvas.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
    return { x: x, y: y, inside: x >= 0 && y >= 0 && x <= r.width && y <= r.height };
  }

  // Cadangan: jalankan scene langsung di thread utama, paling tinggi 30 fps.
  function inline(target) {
    import("./ocean/scene.js?v=" + V).then(function (mod) {
      var scene = new mod.Scene(target, { preset: preset, level: Math.max(level, hero ? 1 : 0) });
      scene.reduced = reducedMq.matches;
      send = function (m) {
        switch (m.type) {
          case "resize": scene.resize(m.w, m.h, m.dpr); break;
          case "coin": scene.setCoin(m.geom, m.tex); break;
          case "visible": scene.setVisible(m.visible); break;
          case "reduced": scene.setReduced(m.reduced); break;
          case "pointer": scene.pointer(m.x, m.y, m.active); break;
          case "splash": scene.splash(m.x, m.y); break;
        }
      };
      var s = size();
      scene.resize(s.w, s.h, s.dpr);
      queue.forEach(function (q) { send(q[0]); });
      queue = [];
    });
  }

  if (canvas.transferControlToOffscreen && window.Worker) {
    var s0 = size(), ready = false, worker;
    try {
      var off = canvas.transferControlToOffscreen();
      worker = new Worker(new URL("./ocean-worker.js?v=" + V, import.meta.url), { type: "module" });
      worker.onmessage = function (e) {
        if (e.data.type !== "ready") return;
        ready = true;
        send = function (m, t) { worker.postMessage(m, t || []); };
        queue.forEach(function (q) { send(q[0], q[1]); });
        queue = [];
      };
      worker.onerror = function () {
        if (ready) return;
        // Worker gagal dimuat (mis. module worker belum didukung): canvas lama sudah diserahkan, jadi ganti baru.
        worker.terminate();
        var fresh = canvas.cloneNode(false);
        canvas.replaceWith(fresh);
        canvas = fresh;
        inline(fresh);
      };
      worker.postMessage({ type: "init", canvas: off, opts: { preset: preset, level: level }, reduced: reducedMq.matches, w: s0.w, h: s0.h, dpr: s0.dpr }, [off]);
    } catch (err) {
      inline(canvas);
    }
  } else {
    inline(canvas);
  }

  function resized() {
    var s = size();
    post({ type: "resize", w: s.w, h: s.h, dpr: s.dpr });
    if (slot) post({ type: "coin", geom: coinGeom() });
  }
  new ResizeObserver(resized).observe(canvas);
  if (slot) {
    new ResizeObserver(resized).observe(slot);
    logoTexture(slot.getAttribute("data-logo"), 256, function (tex) {
      post({ type: "coin", geom: coinGeom(), tex: tex }, [tex.data.buffer]);
    });
  }

  var onScreen = true;
  function visibility() { post({ type: "visible", visible: onScreen && document.visibilityState === "visible" }); }
  new IntersectionObserver(function (e) { onScreen = e[0].isIntersecting; visibility(); }).observe(canvas);
  document.addEventListener("visibilitychange", visibility);
  reducedMq.addEventListener("change", function () { post({ type: "reduced", reduced: reducedMq.matches }); });

  var pending = null;
  window.addEventListener("pointermove", function (e) {
    var p = local(e);
    if (!pending) requestAnimationFrame(function () { post(pending); pending = null; });
    pending = { type: "pointer", x: p.x, y: p.y, active: p.inside && e.pointerType !== "touch" };
  }, { passive: true });
  window.addEventListener("pointerdown", function (e) {
    var p = local(e);
    if (p.inside && !e.target.closest("a,button,summary,input")) post({ type: "splash", x: p.x, y: p.y });
  }, { passive: true });
  document.documentElement.addEventListener("pointerleave", function () { post({ type: "pointer", x: 0, y: 0, active: false }); });
}

var hero = document.querySelector(".hero-ocean canvas"), footer = document.querySelector(".footer-ocean canvas");
if (hero && hero.getContext) mount(hero, "hero", document.querySelector(".hero-coin"));
if (footer && footer.getContext) mount(footer, "footer", null);
