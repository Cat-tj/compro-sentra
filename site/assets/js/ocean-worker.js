// Web Worker laut ASCII: semua simulasi dan gambar terjadi di sini, thread utama tetap bebas untuk scroll dan klik.
import { Scene } from "./ocean/scene.js?v=20261029f";

var scene = null;

self.onmessage = function (e) {
  var m = e.data;
  switch (m.type) {
    case "init":
      scene = new Scene(m.canvas, m.opts);
      scene.reduced = m.reduced;
      if (m.coin) scene.setCoin(m.coin.geom, m.coin.tex);
      scene.resize(m.w, m.h, m.dpr);
      self.postMessage({ type: "ready" });
      break;
    case "resize": scene.resize(m.w, m.h, m.dpr); break;
    case "coin": scene.setCoin(m.geom, m.tex); break;
    case "visible": scene.setVisible(m.visible); break;
    case "reduced": scene.setReduced(m.reduced); break;
    case "pointer": scene.pointer(m.x, m.y, m.active); break;
    case "splash": scene.splash(m.x, m.y); break;
  }
};
