// Medan ASCII: gumpalan noise yang pelan-pelan berubah bentuk, digambar sebagai grid glyph.
// Semua dihitung di GPU (satu fragment shader); CPU hanya mengirim waktu per frame.
// Tanpa WebGL atau saat "kurangi gerakan" aktif: satu frame diam.

var VERT = "attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}";

// Simplex noise 3D: Ian McEwan & Stefan Gustavson (Ashima Arts), MIT License.
var NOISE = [
  "vec3 m289(vec3 x){return x-floor(x*(1./289.))*289.;}",
  "vec4 m289(vec4 x){return x-floor(x*(1./289.))*289.;}",
  "vec4 perm(vec4 x){return m289(((x*34.)+1.)*x);}",
  "vec4 tis(vec4 r){return 1.79284291400159-.85373472095314*r;}",
  "float snoise(vec3 v){const vec2 C=vec2(1./6.,1./3.);const vec4 D=vec4(0.,.5,1.,2.);",
  "vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.-g;",
  "vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);vec3 x1=x0-i1+C.xxx;vec3 x2=x0-i2+C.yyy;vec3 x3=x0-D.yyy;",
  "i=m289(i);vec4 p=perm(perm(perm(i.z+vec4(0.,i1.z,i2.z,1.))+i.y+vec4(0.,i1.y,i2.y,1.))+i.x+vec4(0.,i1.x,i2.x,1.));",
  "float n_=.142857142857;vec3 ns=n_*D.wyz-D.xzx;vec4 j=p-49.*floor(p*ns.z*ns.z);vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.*x_);",
  "vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;vec4 h=1.-abs(x)-abs(y);vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);",
  "vec4 s0=floor(b0)*2.+1.;vec4 s1=floor(b1)*2.+1.;vec4 sh=-step(h,vec4(0.));",
  "vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;",
  "vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);",
  "vec4 norm=tis(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;",
  "vec4 m=max(.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.);m=m*m;",
  "return 42.*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));}",
].join("\n");

var FRAG = [
  "precision mediump float;",
  "uniform vec2 res;uniform float t,cell,scale,thresh;uniform sampler2D atlas;uniform float n;",
  "uniform vec3 bg,bg2,c1,c2;",
  NOISE,
  "float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}",
  "void main(){",
  "  vec2 px=vec2(gl_FragCoord.x,res.y-gl_FragCoord.y);",
  "  vec2 id=floor(px/cell);vec2 uv=fract(px/cell);",
  "  vec2 q=id*cell/scale;",
  // dua oktaf noise + waktu sebagai sumbu ketiga: gumpalan berubah bentuk tanpa bergeser terlalu cepat
  "  float v=snoise(vec3(q*.9,t*.05))*.7+snoise(vec3(q*2.1+7.3,t*.08))*.3;",
  "  v=v*.5+.5;",
  "  float k=clamp((v-thresh)/(1.-thresh),0.,1.);",
  "  vec3 base=mix(bg,bg2,px.y/res.y);vec3 col=base;",
  "  if(k>0.){",
  // glyph dipilih dari kepadatan, sesekali 'teracak' seperti di referensi
  "    float flick=step(.92,hash(id+floor(t*1.5)));",
  "    float g=floor(min(k*1.6+flick*.35,1.)*(n-1.)+.5);",
  "    float a=texture2D(atlas,vec2((g+uv.x)/n,uv.y)).a;",
  "    col=mix(base,mix(c1,c2,smoothstep(.15,.9,k)),a*smoothstep(0.,.08,k));",
  "  }",
  "  gl_FragColor=vec4(col,1.);",
  "}",
].join("\n");

var GLYPHS = ".:-=+*#%@";

function hex(c) {
  var n = parseInt(c.slice(1), 16);
  return [(n >> 16 & 255) / 255, (n >> 8 & 255) / 255, (n & 255) / 255];
}

function atlas(gl, cellPx) {
  var c = document.createElement("canvas"), n = GLYPHS.length;
  c.width = cellPx * n; c.height = cellPx;
  var g = c.getContext("2d");
  g.font = "600 " + Math.round(cellPx * 0.82) + "px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace";
  g.textAlign = "center"; g.textBaseline = "middle"; g.fillStyle = "#fff";
  for (var i = 0; i < n; i++) g.fillText(GLYPHS[i], i * cellPx + cellPx / 2, cellPx / 2 + 1);
  var tex = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, tex);
  gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, c);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
}

// opts: { bg, bg2 (opsional, warna bawah), c1, c2, cell (px CSS), scale (px per unit noise), thresh, fps, onStats }
export function Field(canvas, opts) {
  this.canvas = canvas;
  this.o = opts;
  var gl = canvas.getContext("webgl", { antialias: false, alpha: false, powerPreference: "low-power" });
  if (!gl) { canvas.style.background = "linear-gradient(" + opts.bg + "," + (opts.bg2 || opts.bg) + ")"; this.gl = null; return; }
  this.gl = gl;
  function sh(type, src) { var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s)); return s; }
  var pr = gl.createProgram();
  gl.attachShader(pr, sh(gl.VERTEX_SHADER, VERT)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FRAG)); gl.linkProgram(pr); gl.useProgram(pr);
  var buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  var loc = gl.getAttribLocation(pr, "p");
  gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  var u = this.u = {};
  ["res", "t", "cell", "scale", "thresh", "atlas", "n", "bg", "bg2", "c1", "c2"].forEach(function (k) { u[k] = gl.getUniformLocation(pr, k); });
  gl.uniform3fv(u.bg, hex(opts.bg)); gl.uniform3fv(u.bg2, hex(opts.bg2 || opts.bg)); gl.uniform3fv(u.c1, hex(opts.c1)); gl.uniform3fv(u.c2, hex(opts.c2));
  gl.uniform1f(u.thresh, opts.thresh); gl.uniform1f(u.n, GLYPHS.length); gl.uniform1i(u.atlas, 0);

  this.t0 = performance.now(); this.last = 0; this.raf = 0; this.visible = true;
  this.reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var self = this;
  this.frame = function (now) { self.tick(now); };
  new ResizeObserver(function () { self.resize(); }).observe(canvas);
  new IntersectionObserver(function (e) { self.visible = e[0].isIntersecting; self.schedule(); }).observe(canvas);
  this.resize();
}

Field.prototype.resize = function () {
  var gl = this.gl;
  if (!gl) return;
  var r = this.canvas.getBoundingClientRect(), dpr = Math.min(window.devicePixelRatio || 1, 2);
  this.canvas.width = Math.round(r.width * dpr); this.canvas.height = Math.round(r.height * dpr);
  gl.viewport(0, 0, this.canvas.width, this.canvas.height);
  var cellPx = Math.round(this.o.cell * dpr);
  atlas(gl, cellPx);
  gl.uniform2f(this.u.res, this.canvas.width, this.canvas.height);
  gl.uniform1f(this.u.cell, cellPx);
  gl.uniform1f(this.u.scale, this.o.scale * dpr);
  this.draw(this.reduced ? 0 : (performance.now() - this.t0) / 1000);
  this.schedule();
};

Field.prototype.draw = function (t) {
  var s = performance.now();
  this.gl.uniform1f(this.u.t, t);
  this.gl.drawArrays(this.gl.TRIANGLES, 0, 3);
  return performance.now() - s;
};

Field.prototype.schedule = function () {
  cancelAnimationFrame(this.raf);
  if (this.gl && this.visible && !this.reduced) this.raf = requestAnimationFrame(this.frame);
};

Field.prototype.tick = function (now) {
  this.raf = requestAnimationFrame(this.frame);
  if (now - this.last < 1000 / (this.o.fps || 30) - 2) return;   // gerakannya pelan; 30 fps sudah mulus
  var gap = now - this.last;
  this.last = now;
  var ms = this.draw((now - this.t0) / 1000);
  if (this.o.onStats) this.o.onStats(ms, gap);
};

// Hero beranda (light mode) dan footer semua halaman (gelap, menyambung CTA biru di atasnya).
var hero = document.querySelector(".hero-ocean canvas"), footer = document.querySelector(".footer-ocean canvas");
var small = window.matchMedia("(max-width: 640px)").matches;
if (hero) new Field(hero, { bg: "#D6E8FF", c1: "#7FA6E6", c2: "#2C5BB8", cell: small ? 10 : 12, scale: small ? 180 : 260, thresh: 0.48 });
if (footer) new Field(footer, { bg: "#13306B", bg2: "#081530", c1: "#3E6FCC", c2: "#A9C6F5", cell: small ? 10 : 11, scale: small ? 170 : 220, thresh: 0.5 });
