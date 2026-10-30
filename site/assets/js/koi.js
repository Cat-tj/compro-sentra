// Kolam koi ASCII (hero halaman Tentang dan latar section tim): tiga koi berenang, digambar sebagai glyph di GPU.
// Warna air dan ukuran bisa diatur per kanvas lewat data-water, data-water2, data-ripple, data-scale, data-dpr.
// JS hanya menghitung titik tulang punggung tiap koi (3 x 10 titik); shader mengisi setiap sel grid.
import { NOISE, atlas, hex } from "./field.js?v=20261029w";

var NK = 3, NODES = 10, GLYPHS = "~.:-=+*#%@";

var FRAG = [
  "precision mediump float;",
  "uniform vec2 res;uniform float t,cell,n;uniform sampler2D atlas;",
  "uniform vec2 K[30];uniform float len[3];",
  "uniform vec3 water,water2,ripple,white,red,gold,ink;",
  NOISE,
  // lebar sepanjang s (0 kepala, 1 ujung ekor), relatif terhadap panjang koi
  "float bodyW(float s){return .12*pow(sin(3.1416*clamp((s+.06)/.9,0.,1.)),.6);}",          // kepala bulat, pangkal ekor ramping
  "float finW(float s){return s<.2||s>.42?0.:.12*smoothstep(.2,.23,s)*(1.-(s-.2)/.22);}",   // sirip dada: segitiga menyapu ke belakang
  "float tailW(float s){return s<.8?0.:.17*smoothstep(.8,1.,s);}",                           // sirip ekor melebar
  "float wid(float s){return max(bodyW(s)+finW(s),tailW(s));}",
  // jarak relatif terdekat ke koi mana pun: r<1 berarti di dalam siluet
  "vec4 koi(vec2 p){",
  "  float best=9.,bs=0.,bk=-1.,side=0.;",
  "  for(int k=0;k<3;k++){for(int i=0;i<9;i++){",
  "    vec2 a=K[k*10+i],b=K[k*10+i+1];vec2 ab=b-a;float u0=dot(p-a,ab)/max(dot(ab,ab),1e-3);",
  "    if(i==8&&u0>1.)continue;",                                                               // ekor terpotong rata, bukan bundar
  "    float u=clamp(u0,0.,1.);vec2 q=a+ab*u;float s=(float(i)+u)/9.;float w=max(wid(s)*len[k],1.);float r=length(p-q)/w;",
  "    if(r<best){best=r;bs=s;bk=float(k);side=sign(ab.x*(p.y-a.y)-ab.y*(p.x-a.x));}",
  "  }}",
  "  return vec4(best,bs,bk,side);",
  "}",
  "void main(){",
  "  vec2 px=vec2(gl_FragCoord.x,res.y-gl_FragCoord.y);",
  "  vec2 id=floor(px/cell);vec2 uv=fract(px/cell);vec2 c=(id+.5)*cell;",
  "  float wn=snoise(vec3(c/260.,t*.06));",
  "  vec3 col=mix(water,water2,wn*.5+.5);",
  "  vec4 f=koi(c);",
  "  float d=f.x*wid(f.y);",                                                                    // jarak ke tulang punggung, relatif panjang koi
  "  if(f.y>.9&&d<.1*(f.y-.9)/.1)f.x=9.;",                                                       // ekor bercabang
  "  float shade=step(koi(c-vec2(9.,12.)).x,1.);",                                              // bayangan koi di dasar kolam
  "  col=mix(col,col*.72,shade*step(1.,f.x));",
  "  float g=-1.;vec3 gc=ripple;",
  "  if(f.x<1.){",
  "    float k=f.z;float pat=snoise(vec3(f.y*5.5+k*7.3,f.w*.9+d*12.,k*3.1));",
  "    vec3 base=white;",
  "    if(k<.5){ if(pat>.1||f.y<.16) base=red; }",                       // kohaku: putih + bercak merah
  "    else if(k<1.5){ base=mix(gold,red,smoothstep(.2,.6,pat)*.35); }",  // ogon: keemasan
  "    else { base=pat>.25?red:(pat<-.35?ink:white); }",                  // showa: putih, merah, hitam
  "    if(d>bodyW(f.y)+.008||f.y>.84){",                                 // sirip: tipis dan tembus pandang
  "      gc=mix(col,base,.75);g=f.x>.7?2.:3.;",
  "    } else {",
  "      float e=d/max(bodyW(f.y),.01);",
  "      gc=mix(base,base*.7,smoothstep(.55,1.,e));",
  "      g=floor(mix(9.,4.,e)+.5);",
  "      col=mix(col,base*.94,.5-.15*smoothstep(.7,1.,e));",
  "      if(f.y>.05&&f.y<.11&&d>.035&&d<.07){gc=ink;g=9.;}",                // mata
  "    }",
  "  } else {",
  "    float rp=snoise(vec3(c/90.,t*.12));",
  "    if(abs(rp)<.06&&fract(sin(dot(id,vec2(12.9,78.2)))*43758.5)>.35) g=0.;",   // riak air
  "  }",
  "  if(g>=0.){float a=texture2D(atlas,vec2((g+uv.x)/n,uv.y)).a;col=mix(col,gc,a);}",
  "  gl_FragColor=vec4(col,1.);",
  "}",
].join("\n");

// Lintasan per koi: putaran elips yang landai (+ sedikit goyangan) supaya badan tidak terlipat di tikungan.
// rx/ry/wob dalam pecahan lebar/tinggi kanvas, dir -1 = berenang berlawanan arah, L = panjang relatif sisi pendek.
var PATHS = [
  { rx: 0.3, ry: 0.3, p: 0.0, dir: 1, wob: 0.04, v: 40, L: 0.46 },
  { rx: 0.27, ry: 0.26, p: 5.24, dir: -1, wob: 0.03, v: 32, L: 0.4 },
  { rx: 0.34, ry: 0.32, p: 2.09, dir: 1, wob: 0.03, v: 36, L: 0.42 },
];

function Pond(canvas) {
  this.canvas = canvas;
  var gl = canvas.getContext("webgl", { antialias: false, alpha: false, powerPreference: "low-power" });
  var D = canvas.dataset;
  if (!gl) { canvas.style.background = "linear-gradient(" + (D.water || "#2C6E92") + "," + (D.water2 || "#1B4A6B") + ")"; return; }
  this.gl = gl;
  function sh(type, src) { var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s)); return s; }
  var pr = gl.createProgram();
  gl.attachShader(pr, sh(gl.VERTEX_SHADER, "attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}"));
  gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FRAG)); gl.linkProgram(pr); gl.useProgram(pr);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  var loc = gl.getAttribLocation(pr, "p"); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  var u = this.u = {};
  ["res", "t", "cell", "n", "atlas", "K", "len", "water", "water2", "ripple", "white", "red", "gold", "ink"].forEach(function (k) { u[k] = gl.getUniformLocation(pr, k); });
  var C = { water: D.water || "#2C6E92", water2: D.water2 || "#1B4A6B", ripple: D.ripple || "#7DB4D4", white: "#FFFDF8", red: "#E2482F", gold: "#F2A93B", ink: "#1E2433" };
  for (var k in C) gl.uniform3fv(u[k], hex(C[k]));
  gl.uniform1f(u.n, GLYPHS.length); gl.uniform1i(u.atlas, 0);

  this.pos = PATHS.map(function () { return 0; });
  this.K = new Float32Array(NK * NODES * 2);
  this.last = 0; this.t = 0; this.raf = 0; this.visible = true;
  this.scale = parseFloat(D.scale) || 1; this.maxDpr = parseFloat(D.dpr) || 2;
  // HP lemah (RAM kecil atau sedikit core): 20 fps cukup, dan jarang terasa bedanya untuk ikan yang berenang pelan
  this.minDt = 1 / ((navigator.deviceMemory && navigator.deviceMemory <= 2) || (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4) ? 20 : 30);
  this.reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var self = this;
  this.frame = function (now) { self.tick(now); };
  new ResizeObserver(function () { self.resize(); }).observe(canvas);
  new IntersectionObserver(function (e) { self.visible = e[0].isIntersecting; self.schedule(); }).observe(canvas);
  this.resize();
}

Pond.prototype.resize = function () {
  var self = this, gl = this.gl, r = this.canvas.getBoundingClientRect(), dpr = Math.min(window.devicePixelRatio || 1, this.maxDpr);
  if (!gl || r.width < 1) return;
  this.w = r.width * dpr; this.h = r.height * dpr; this.dpr = dpr;
  this.canvas.width = Math.round(this.w); this.canvas.height = Math.round(this.h);
  gl.viewport(0, 0, this.canvas.width, this.canvas.height);
  var cellPx = Math.round((r.width < 420 ? 6 : 7) * dpr);
  atlas(gl, cellPx, GLYPHS);
  gl.uniform2f(this.u.res, this.canvas.width, this.canvas.height);
  gl.uniform1f(this.u.cell, cellPx);
  gl.uniform1fv(this.u.len, PATHS.map(function (p) { return p.L * self.scale * Math.min(r.width, r.height) * dpr; }));
  this.step(0); this.draw();
  this.schedule();
};

Pond.prototype.head = function (p, s) {
  return [this.w * (0.5 + p.rx * Math.sin(s + p.p) + p.wob * Math.sin(2 * s + p.p * 1.7)),
    this.h * (0.5 + p.dir * p.ry * Math.cos(s + p.p) + p.wob * Math.cos(3 * s + p.p))];
};

// Majukan kepala dengan kecepatan piksel tetap, lalu letakkan 10 titik tulang punggung di belakangnya
// mengikuti lintasan yang sama, dengan lenggokan yang makin besar ke arah ekor.
Pond.prototype.step = function (dt) {
  var self = this;
  PATHS.forEach(function (p, k) {
    var s = self.pos[k], h = self.head(p, s), h2 = self.head(p, s + 0.001);
    var speed = Math.hypot(h2[0] - h[0], h2[1] - h[1]) / 0.001 || 1;
    s = self.pos[k] = s + p.v * self.dpr * dt / speed;
    var L = p.L * self.scale * Math.min(self.w, self.h), seg = L / (NODES - 1);
    var prev = self.head(p, s), j = 0, acc = 0, cur = s;
    self.K[(k * NODES) * 2] = prev[0]; self.K[(k * NODES) * 2 + 1] = prev[1];
    for (var n = 1; n < NODES; n++) {
      while (acc < seg && j < 400) {
        cur -= 0.004; j++;
        var q = self.head(p, cur);
        acc += Math.hypot(q[0] - prev[0], q[1] - prev[1]); prev = q;
      }
      acc -= seg;
      var a = self.head(p, cur - 0.01), b = self.head(p, cur + 0.01), tx = b[0] - a[0], ty = b[1] - a[1], tl = Math.hypot(tx, ty) || 1;
      var wig = Math.sin(self.t * 5.5 - n * 0.75 + k) * L * 0.035 * (n / (NODES - 1));
      self.K[(k * NODES + n) * 2] = prev[0] - ty / tl * wig;
      self.K[(k * NODES + n) * 2 + 1] = prev[1] + tx / tl * wig;
    }
  });
};

Pond.prototype.draw = function () {
  var gl = this.gl;
  gl.uniform1f(this.u.t, this.t);
  gl.uniform2fv(this.u.K, this.K);
  gl.drawArrays(gl.TRIANGLES, 0, 3);
};

Pond.prototype.schedule = function () {
  cancelAnimationFrame(this.raf);
  if (this.gl && this.visible && !this.reduced) { this.last = performance.now(); this.raf = requestAnimationFrame(this.frame); }
};

Pond.prototype.tick = function (now) {
  this.raf = requestAnimationFrame(this.frame);
  var dt = (now - this.last) / 1000;
  if (dt < this.minDt - 0.002) return;   // 20-30 fps cukup untuk ikan yang berenang pelan
  this.last = now;
  dt = Math.min(dt, 0.1);
  this.t += dt;
  this.step(dt);
  this.draw();
};

document.querySelectorAll(".koi-pond canvas, .koi-bg canvas").forEach(function (c) { c._pond = new Pond(c); });
