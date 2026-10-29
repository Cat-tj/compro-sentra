/* Sentra Technology — perilaku umum: menu HP, efek muncul saat scroll, tombol carousel. */
(function () {
  'use strict';
  // menu HP
  var burger = document.getElementById('burger'), menu = document.getElementById('mobileMenu');
  if (burger && menu) {
    var set = function (open) {
      menu.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
    };
    burger.addEventListener('click', function () { set(burger.getAttribute('aria-expanded') !== 'true'); });
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { set(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  }
  // pilihan bahasa: tutup saat klik di luar
  document.addEventListener('click', function (e) {
    document.querySelectorAll('details.lang-dd[open]').forEach(function (d) { if (!d.contains(e.target)) d.removeAttribute('open'); });
  });
  // muncul saat discroll
  var els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }
  // tab solusi di beranda
  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = [].slice.call(list.querySelectorAll('[role="tab"]'));
    var pick = function (t, focus) {
      tabs.forEach(function (x) {
        var on = x === t;
        x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1;
        var pnl = document.getElementById(x.getAttribute('aria-controls'));
        if (pnl) pnl.hidden = !on;
      });
      if (focus) t.focus();
    };
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { pick(t); });
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); }
      });
    });
  });
  var still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  // jaringan node bergerak (hero & CTA): garis tersambung saat node berdekatan, putus saat menjauh
  var small = matchMedia('(max-width: 760px)').matches;
  var net = function (hb) {
    var cv = document.createElement('canvas'); cv.className = 'hero-net'; hb.appendChild(cv);
    var ctx = cv.getContext('2d'), nodes = [], W = 0, H = 0, vis = true, lastF = 0;
    var rgb = hb.classList.contains('dark') ? '169,203,255' : '44,91,184';
    var LINK = small ? 120 : 170, FPS = small ? 30 : 60;
    var size = function () {
      var r = hb.getBoundingClientRect(), dpr = Math.min(window.devicePixelRatio || 1, small ? 1.5 : 2);
      W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var want = Math.round(Math.min(small ? 28 : 80, W * H / (small ? 12000 : 15000)));
      while (nodes.length < want) {
        var sp = 0.08 + Math.random() * 0.14, a = Math.random() * 6.283;
        nodes.push({ x: Math.random() * W, y: Math.random() * H, vx: Math.cos(a) * sp, vy: Math.sin(a) * sp, ring: Math.random() < 0.16, r: 2.2 + Math.random() * 1.4 });
      }
      nodes.length = want;
    };
    var draw = function () {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d = dx * dx + dy * dy;
          if (d < LINK * LINK) {
            ctx.strokeStyle = 'rgba(' + rgb + ',' + (0.4 * (1 - Math.sqrt(d) / LINK)).toFixed(3) + ')';
            ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
      }
      for (var k = 0; k < nodes.length; k++) {
        var n = nodes[k];
        if (n.ring) { ctx.strokeStyle = 'rgba(' + rgb + ',.4)'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(n.x, n.y, 9, 0, 6.283); ctx.stroke(); }
        ctx.fillStyle = 'rgba(' + rgb + ',' + (n.ring ? .65 : .42) + ')';
        ctx.beginPath(); ctx.arc(n.x, n.y, n.ring ? 3.6 : n.r, 0, 6.283); ctx.fill();
      }
    };
    var loop = function (t) {
      requestAnimationFrame(loop);
      if (!vis || document.hidden || t - lastF < 1000 / FPS - 2) return;
      var dt = Math.min(50, t - (lastF || t)) / 16.7; lastF = t;
      for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i]; n.x += n.vx * dt; n.y += n.vy * dt;
        if (n.x < -20) n.x = W + 20; else if (n.x > W + 20) n.x = -20;
        if (n.y < -20) n.y = H + 20; else if (n.y > H + 20) n.y = -20;
      }
      draw();
    };
    size(); draw();
    var rt; addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { size(); draw(); }, 150); });
    if (still) return;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; lastF = 0; }).observe(hb);
    requestAnimationFrame(loop);
  };
  if (document.createElement('canvas').getContext) document.querySelectorAll('.hero-bg, .net-bg').forEach(net);
  // carousel: tombol panah; data-auto = berjalan sendiri tanpa ujung (berhenti saat disentuh/hover/di luar layar)
  document.querySelectorAll('.carousel').forEach(function (c) {
    var track = c.querySelector('.track');
    if (!track) return;
    var p = c.querySelector('.c-prev'), n = c.querySelector('.c-next');
    var auto = c.hasAttribute('data-auto') && !still && track.children.length > 1;
    var pos = 0, half = 0, hold = 0, seen = false, last = 0, resume;
    var pause = function (ms) {
      hold++; clearTimeout(resume);
      if (ms) resume = setTimeout(function () { hold = 0; pos = track.scrollLeft; }, ms);
    };
    var step = function (d) {
      if (auto) pause(1600);
      track.scrollBy({ left: d * Math.max(260, track.clientWidth * 0.8), behavior: 'smooth' });
    };
    if (p) p.addEventListener('click', function () { step(-1); });
    if (n) n.addEventListener('click', function () { step(1); });
    if (!auto) return;
    var items = [].slice.call(track.children);
    items.forEach(function (it) {
      var k = it.cloneNode(true);
      k.setAttribute('aria-hidden', 'true'); k.tabIndex = -1;
      track.appendChild(k);
    });
    track.style.scrollSnapType = 'none';
    var measure = function () { half = track.children[items.length].offsetLeft - items[0].offsetLeft; };
    measure(); addEventListener('resize', measure);
    var release = function () { hold = 0; pos = track.scrollLeft; };
    c.addEventListener('mouseenter', function () { pause(); });
    c.addEventListener('mouseleave', release);
    c.addEventListener('focusin', function () { pause(); });
    c.addEventListener('focusout', release);
    track.addEventListener('touchstart', function () { pause(); }, { passive: true });
    track.addEventListener('touchend', function () { pause(2500); }, { passive: true });
    track.addEventListener('scroll', function () {
      if (!hold) return;
      if (track.scrollLeft >= half) track.scrollLeft -= half;
      else if (track.scrollLeft <= 0 && half) track.scrollLeft += half;
    }, { passive: true });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { seen = es[0].isIntersecting; }).observe(c);
    } else { seen = true; }
    var tick = function (t) {
      var dt = Math.min(64, t - (last || t)); last = t;
      if (seen && !hold && !document.hidden && half) {
        pos += dt * 0.04;
        if (pos >= half) pos -= half;
        track.scrollLeft = pos;
      }
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });
})();
