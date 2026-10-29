// Peta jangkauan Sentra: ganti mode hardware (Kaltim) / software (dunia), putar animasi saat terlihat,
// dan ganti mode otomatis sampai pengunjung memilih sendiri.
(function () {
  var r = document.querySelector('.reach');
  if (!r) return;
  var tabs = [].slice.call(r.querySelectorAll('[role="tab"]'));
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var auto = 0, chosen = false, inView = false;

  function play() {
    r.classList.remove('play');
    void r.offsetWidth;   // mulai ulang animasi CSS
    r.classList.add('play');
  }
  function set(mode) {
    r.setAttribute('data-mode', mode);
    tabs.forEach(function (t) {
      var on = t.getAttribute('data-mode') === mode;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
    });
    play();
  }

  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { chosen = true; clearInterval(auto); set(t.getAttribute('data-mode')); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      var n = tabs[(i + d + tabs.length) % tabs.length];
      n.focus(); n.click();
    });
  });

  new IntersectionObserver(function (e) {
    inView = e[0].isIntersecting;
    r.classList.toggle('in-view', inView);
    if (inView && !r.classList.contains('play')) play();
  }, { threshold: 0.35 }).observe(r);

  if (!reduced.matches) {
    auto = setInterval(function () {
      if (!chosen && inView && !document.hidden) set(r.getAttribute('data-mode') === 'hw' ? 'sw' : 'hw');
    }, 7000);
  }
})();
