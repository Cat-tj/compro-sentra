/* Daftar minat produk & layanan Sentra (dari keranjang Altora, tanpa harga).
   Tombol: <button class="cart-add" data-cart-id data-cart-name data-cart-meta data-cart-img>.
   Isi disimpan di localStorage browser pengunjung, lalu dikirim sebagai pesan WhatsApp.
   Teks mengikuti bahasa halaman (window.SENTRA_UI dari generator). */
(function () {
  'use strict';
  var KEY = 'sentra-cart-v1';
  var WA = '6282255443380';
  var D = {
    fab: 'Daftar minat', fab_aria: 'Buka daftar minat', title: 'Daftar minat', close: 'Tutup', empty: 'Daftar masih kosong.', see: 'Lihat produk',
    form_title: 'Data untuk demo', optional: '(opsional)', name: 'Nama', org: 'Instansi / perusahaan', loc: 'Lokasi', loc_ph: 'mis. Samarinda',
    demo: 'Jadwalkan demo', notes: 'Catatan', notes_ph: 'Jumlah pengguna, titik kamera, target waktu…', note: 'Detail kebutuhan kita diskusikan lewat WhatsApp.',
    send: 'Kirim via WhatsApp', clear: 'Kosongkan daftar', confirm: 'Kosongkan semua isi daftar?', less: 'Kurangi', more: 'Tambah', qty: 'Jumlah', del: 'Hapus',
    in_cart: 'Di daftar', add: 'Tambah ke daftar', added: 'ditambahkan ke daftar',
    msg_intro: 'Halo Sentra Technology, saya tertarik dengan produk/layanan berikut:', msg_total: 'Total', msg_items: 'item',
    msg_demo: 'Demo', msg_demo_yes: 'Ya, mohon dijadwalkan', msg_demo_no: 'Informasi dulu', msg_name: 'Nama', msg_org: 'Instansi', msg_loc: 'Lokasi',
    msg_notes: 'Catatan', msg_from: 'Dikirim dari daftar minat sentratechnology.com', home: '/produk'
  };
  var T = Object.assign({}, D, (window.SENTRA_UI && window.SENTRA_UI.cart) || {});
  var items = load();

  function load() {
    try { var v = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(v) ? v : []; } catch (e) { return []; }
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(items)); } catch (e) { /* mode privat: keranjang tetap jalan selama halaman terbuka */ }
  }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; });
  }
  function count() { return items.reduce(function (n, it) { return n + it.qty; }, 0); }
  function find(id) { for (var i = 0; i < items.length; i++) if (items[i].id === id) return items[i]; return null; }

  var hasProducts = !!document.querySelector('.cart-add');

  // ── elemen UI ──
  var fab = document.createElement('button');
  fab.type = 'button';
  fab.className = 'cart-fab';
  fab.setAttribute('aria-label', T.fab_aria);
  fab.innerHTML = '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M3 4h2.2l2.2 10.5h10.2L20 7.5H6.4"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/></svg><span>' + esc(T.fab) + '</span><b class="cart-count">0</b>';

  var drawer = document.createElement('div');
  drawer.className = 'cart-drawer';
  drawer.hidden = true;
  drawer.innerHTML =
    '<div class="cart-backdrop" data-cart-close></div>' +
    '<aside aria-labelledby="cartTitle" aria-modal="true" class="cart-panel" role="dialog">' +
    '<header class="cart-head"><h2 id="cartTitle">' + esc(T.title) + '</h2><button aria-label="' + esc(T.close) + '" class="cart-x" data-cart-close type="button">×</button></header>' +
    '<div class="cart-body"><ul class="cart-list"></ul>' +
    '<div class="cart-empty"><p>' + esc(T.empty) + '</p><a class="btn btn-purple" href="' + esc(T.home) + '">' + esc(T.see) + '</a></div>' +
    '<form class="cart-form" novalidate>' +
    '<p class="cart-form-title">' + esc(T.form_title) + ' <small>' + esc(T.optional) + '</small></p>' +
    '<label>' + esc(T.name) + '<input autocomplete="name" name="nama" type="text"/></label>' +
    '<label>' + esc(T.org) + '<input autocomplete="organization" name="instansi" type="text"/></label>' +
    '<label>' + esc(T.loc) + '<input name="lokasi" placeholder="' + esc(T.loc_ph) + '" type="text"/></label>' +
    '<label class="cart-check"><input checked name="instalasi" type="checkbox"/> ' + esc(T.demo) + '</label>' +
    '<label>' + esc(T.notes) + '<textarea name="catatan" placeholder="' + esc(T.notes_ph) + '" rows="2"></textarea></label>' +
    '</form></div>' +
    '<footer class="cart-foot"><p class="cart-note">' + esc(T.note) + '</p>' +
    '<a class="btn btn-green cart-send" href="#" rel="noopener" target="_blank"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3Z"/></svg>' + esc(T.send) + '</a>' +
    '<button class="cart-clear" type="button">' + esc(T.clear) + '</button></footer>' +
    '</aside>';

  var toast = document.createElement('div');
  toast.className = 'cart-toast';
  toast.setAttribute('role', 'status');
  toast.setAttribute('aria-live', 'polite');

  document.body.appendChild(fab);
  document.body.appendChild(drawer);
  document.body.appendChild(toast);

  var list = drawer.querySelector('.cart-list');
  var form = drawer.querySelector('.cart-form');
  var send = drawer.querySelector('.cart-send');

  function message() {
    var f = form.elements;
    var lines = [T.msg_intro, ''];
    items.forEach(function (it, i) {
      lines.push((i + 1) + '. ' + it.name + (it.meta ? ' (' + it.meta + ')' : '') + (it.qty > 1 ? ' × ' + it.qty : ''));
    });
    lines.push('', T.msg_total + ': ' + items.length + ' ' + T.msg_items);
    lines.push(T.msg_demo + ': ' + (f.instalasi.checked ? T.msg_demo_yes : T.msg_demo_no));
    if (f.nama.value.trim()) lines.push(T.msg_name + ': ' + f.nama.value.trim());
    if (f.instansi.value.trim()) lines.push(T.msg_org + ': ' + f.instansi.value.trim());
    if (f.lokasi.value.trim()) lines.push(T.msg_loc + ': ' + f.lokasi.value.trim());
    if (f.catatan.value.trim()) lines.push(T.msg_notes + ': ' + f.catatan.value.trim());
    lines.push('', T.msg_from);
    return lines.join('\n');
  }

  function render() {
    var n = count();
    fab.querySelector('.cart-count').textContent = n;
    fab.hidden = !hasProducts && n === 0;
    fab.classList.toggle('has-items', n > 0);
    drawer.classList.toggle('is-empty', n === 0);
    list.innerHTML = items.map(function (it) {
      var pic = it.img ? '<img alt="" src="' + esc(it.img) + '"/>' : '';
      return '<li data-id="' + esc(it.id) + '"><span class="cart-pic">' + pic + '</span>' +
        '<span class="cart-info"><b>' + esc(it.name) + '</b><small>' + esc(it.meta || '') + '</small></span>' +
        '<span class="cart-qty"><button aria-label="' + esc(T.less) + '" data-step="-1" type="button">−</button>' +
        '<input aria-label="' + esc(T.qty) + ' ' + esc(it.name) + '" inputmode="numeric" min="1" type="number" value="' + it.qty + '"/>' +
        '<button aria-label="' + esc(T.more) + '" data-step="1" type="button">+</button></span>' +
        '<button aria-label="' + esc(T.del) + ' ' + esc(it.name) + '" class="cart-del" type="button">×</button></li>';
    }).join('');
    send.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(message());
    document.querySelectorAll('.cart-add').forEach(function (b) {
      var it = find(b.getAttribute('data-cart-id'));
      b.classList.toggle('in-cart', !!it);
      b.querySelector('.cart-add-label').textContent = it ? T.in_cart + ' (' + it.qty + ')' : T.add;
    });
  }

  var toastTimer;
  function notify(text) {
    toast.textContent = text;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 2200);
  }

  function open() { drawer.hidden = false; document.documentElement.classList.add('cart-open'); setTimeout(function () { drawer.classList.add('open'); drawer.querySelector('.cart-x').focus(); }, 10); }
  function close() { drawer.classList.remove('open'); document.documentElement.classList.remove('cart-open'); setTimeout(function () { drawer.hidden = true; fab.focus(); }, 220); }

  // tambah dari kartu produk
  document.querySelectorAll('.cart-add').forEach(function (b) {
    if (!b.querySelector('.cart-add-label')) b.innerHTML = '<span aria-hidden="true">+</span><span class="cart-add-label">' + esc(T.add) + '</span>';
  });
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest('.cart-add');
    if (!b) return;
    var id = b.getAttribute('data-cart-id');
    var it = find(id);
    if (it) it.qty += 1;
    else items.push({ id: id, name: b.getAttribute('data-cart-name'), meta: b.getAttribute('data-cart-meta') || '', img: b.getAttribute('data-cart-img') || '', qty: 1 });
    save(); render();
    fab.classList.remove('bump'); void fab.offsetWidth; fab.classList.add('bump');
    notify(b.getAttribute('data-cart-name') + ' ' + T.added);
  });

  fab.addEventListener('click', open);
  drawer.addEventListener('click', function (ev) {
    if (ev.target.closest('[data-cart-close]')) return close();
    var row = ev.target.closest('li[data-id]');
    if (!row) return;
    var it = find(row.getAttribute('data-id'));
    if (!it) return;
    var step = ev.target.closest('[data-step]');
    if (step) { it.qty = Math.max(1, it.qty + Number(step.getAttribute('data-step'))); save(); render(); }
    else if (ev.target.closest('.cart-del')) { items = items.filter(function (x) { return x !== it; }); save(); render(); }
  });
  list.addEventListener('change', function (ev) {
    var row = ev.target.closest('li[data-id]');
    var it = row && find(row.getAttribute('data-id'));
    if (!it) return;
    it.qty = Math.max(1, Math.min(999, parseInt(ev.target.value, 10) || 1));
    save(); render();
  });
  form.addEventListener('input', function () { send.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(message()); });
  form.addEventListener('change', function () { send.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(message()); });
  send.addEventListener('click', function (ev) { if (!items.length) { ev.preventDefault(); } });
  drawer.querySelector('.cart-clear').addEventListener('click', function () {
    if (!items.length || window.confirm(T.confirm)) { items = []; save(); render(); }
  });
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape' && !drawer.hidden) close(); });
  window.addEventListener('storage', function (ev) { if (ev.key === KEY) { items = load(); render(); } });

  render();
}());
