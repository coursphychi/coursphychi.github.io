---
title: "Photocopieur"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
hidden: true
---


<style>
 	#correc
  {
    color: #006C65;
    border-left: solid 10px #C7DDDC;
  }
 	#comm
  {
    color: #004D80;
    border-left: solid 10px #B3CAD9;
  }
 	#commsum
  {
    color: #004D80;
  }
 	#correcsum
  {
    color: #006C65;
  }

details > summary:first-of-type {
  display: list-item;    
  cursor: pointer;       
}

details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
.pc-figs { display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: center; margin: 1em 0 1.5em; }
.pc-figs svg { flex: 1 1 320px; max-width: 520px; height: auto; }
.pc-box { background: #fff; border: 1px solid #E2E8F0; border-radius: 10px; padding: 12px 12px 14px; margin: 1em 0 1.5em; }
.pc-box svg { display: block; width: 100%; height: auto; }
.pc-ctrl { display: flex; flex-wrap: wrap; gap: 8px 12px; align-items: center; justify-content: center; margin-top: 8px; font-family: system-ui, sans-serif; font-size: 14px; color: #1E293B; }
.pc-btn { font: inherit; font-weight: 600; padding: 7px 14px; border-radius: 8px; border: 2px solid #CBD5E1; background: #fff; color: #1E293B; cursor: pointer; }
.pc-btn:hover { border-color: #94A3B8; }
.pc-btn[aria-pressed="true"] { border-color: #D97706; background: #FEF3C7; color: #92400E; }
.pc-slider { display: flex; align-items: center; gap: 8px; flex: 1 1 260px; max-width: 420px; }
.pc-slider input { flex: 1; accent-color: #D97706; }
.pc-out { display: flex; flex-wrap: wrap; gap: 6px 22px; align-items: center; justify-content: center; margin-top: 10px; font-family: system-ui, sans-serif; font-size: 15px; color: #1E293B; min-height: 74px; }
.pc-out b { font-variant-numeric: tabular-nums; }
.pc-out svg { width: 150px; flex: 0 0 150px; }
.pc-flou { color: #B91C1C; font-weight: 600; }
.pc-net { color: #047857; font-weight: 600; }
</style>





# Photocopieur

<p style="text-align:center;"><i>CCINP</i></p>

<div class="pc-figs">
<svg viewBox="0 0 470 330" role="img" aria-label="Figure 1 : le document (point A) et le récepteur (point A') sont distants de 384 mm ; la lentille divergente L1, de centre O1, est placée à 180 mm du récepteur" font-family="Helvetica, Arial, sans-serif" font-style="italic" fill="#111">
<line x1="15" y1="150" x2="448" y2="150" stroke="#111" stroke-width="1.3"/><polygon points="456,150 446,146 446,154"/>
<line x1="40" y1="45" x2="40" y2="255" stroke="#111" stroke-width="5" stroke-linecap="round"/>
<line x1="424" y1="30" x2="424" y2="265" stroke="#111" stroke-width="5" stroke-linecap="round"/>
<line x1="244" y1="32" x2="244" y2="262" stroke="#111" stroke-width="2"/>
<path d="M238,30 L244,40 L250,30 M238,264 L244,254 L250,264" fill="none" stroke="#111" stroke-width="1.6"/>
<text x="56" y="80" font-size="19">Document</text>
<text x="318" y="215" font-size="19">Récepteur</text>
<text x="50" y="142" font-size="19">A</text>
<text x="250" y="142" font-size="19">O<tspan font-size="13" dy="4">1</tspan></text>
<text x="396" y="142" font-size="19">A’</text>
<text x="203" y="250" font-size="17">(L<tspan font-size="12" dy="4">1</tspan><tspan dy="-4">)</tspan></text>
<line x1="252" y1="18" x2="416" y2="18" stroke="#111" stroke-width="1.2"/><polygon points="246,18 256,14 256,22"/><polygon points="422,18 412,14 412,22"/>
<text x="334" y="11" font-size="17" text-anchor="middle">180 mm</text>
<line x1="48" y1="284" x2="416" y2="284" stroke="#111" stroke-width="1.2"/><polygon points="42,284 52,280 52,288"/><polygon points="422,284 412,280 412,288"/>
<text x="232" y="304" font-size="17" text-anchor="middle">384 mm</text>
<text x="232" y="326" font-size="18" font-weight="700" text-anchor="middle">Figure (1)</text>
</svg>
<svg viewBox="0 0 470 330" role="img" aria-label="Figure 2 : on ajoute une lentille L', de centre O', à 180 mm du document ; la lentille L1 reste à 180 mm du récepteur et la distance document-récepteur vaut toujours 384 mm" font-family="Helvetica, Arial, sans-serif" font-style="italic" fill="#111">
<line x1="15" y1="150" x2="448" y2="150" stroke="#111" stroke-width="1.3"/><polygon points="456,150 446,146 446,154"/>
<line x1="40" y1="45" x2="40" y2="255" stroke="#111" stroke-width="5" stroke-linecap="round"/>
<line x1="424" y1="30" x2="424" y2="265" stroke="#111" stroke-width="5" stroke-linecap="round"/>
<line x1="220" y1="36" x2="220" y2="258" stroke="#111" stroke-width="2"/>
<line x1="244" y1="32" x2="244" y2="262" stroke="#111" stroke-width="2"/>
<path d="M238,30 L244,40 L250,30 M238,264 L244,254 L250,264" fill="none" stroke="#111" stroke-width="1.6"/>
<text x="56" y="80" font-size="19">Document</text>
<text x="318" y="215" font-size="19">Récepteur</text>
<text x="50" y="142" font-size="19">A</text>
<text x="193" y="142" font-size="19">O’</text>
<text x="250" y="142" font-size="19">O<tspan font-size="13" dy="4">1</tspan></text>
<text x="396" y="142" font-size="19">A’</text>
<text x="180" y="250" font-size="17">(L’)</text>
<text x="252" y="250" font-size="17">(L<tspan font-size="12" dy="4">1</tspan><tspan dy="-4">)</tspan></text>
<line x1="48" y1="18" x2="212" y2="18" stroke="#111" stroke-width="1.2"/><polygon points="42,18 52,14 52,22"/><polygon points="218,18 208,14 208,22"/>
<text x="130" y="11" font-size="17" text-anchor="middle">180 mm</text>
<line x1="252" y1="18" x2="416" y2="18" stroke="#111" stroke-width="1.2"/><polygon points="246,18 256,14 256,22"/><polygon points="422,18 412,14 412,22"/>
<text x="334" y="11" font-size="17" text-anchor="middle">180 mm</text>
<line x1="48" y1="284" x2="416" y2="284" stroke="#111" stroke-width="1.2"/><polygon points="42,284 52,280 52,288"/><polygon points="422,284 412,280 412,288"/>
<text x="232" y="304" font-size="17" text-anchor="middle">384 mm</text>
<text x="232" y="326" font-size="18" font-weight="700" text-anchor="middle">Figure (2)</text>
</svg>
</div>

On considère un photocopieur, qui forme l'image d'un document à photocopier sur un récepteur, qui est une surface photosensible. On place à 180 mm du récepteur une lentille (L1) de focale -90 mm (fig.1).
1. Est-il possible de voir quelque chose sur le récepteur ?
2. On place ensuite une lentille (L’) à 180 mm du document (fig. 2). Déterminer sa focale pour obtenir une image sur le récepteur.<br>
En déduire le grandissement  de l’association des deux lentilles et indiquer quel type de tirage permettra cet objectif : transformation de A4 en A3 ou de A4 en A5.
3. (L’) est en réalité un système de deux lentilles (L2) et (L3) accolées, avec (L2) identique à (L1). Calculer la distance focale image  de la lentille (L3). Quelle est la nature de cette lentille mince ?
4. On glisse alors la lentille (L3) afin de l’accoler à (L1). Montrer que l’image du document reste sur le récepteur et calculer le grandissement correspondant  correspondant à l’association de ces trois lentilles ; en déduire le type de tirage obtenu.

<details>
<summary id="commsum">
Animation : la lentille mobile (L<sub>3</sub>) et le tracé des rayons</summary>
<blockquote id="comm">
La lentille (L<sub>3</sub>) glisse de (L<sub>2</sub>) à (L<sub>1</sub>). Les rayons bleus sont issus du bord supérieur du document, les rouges du bord inférieur. Tant que (L<sub>3</sub>) est entre ses deux positions extrêmes, les rayons d'un même faisceau ne se recoupent plus sur le récepteur : l'image y est floue.
<div class="pc-box" id="pc-anim">
<svg viewBox="0 0 760 330" role="img" aria-label="Tracé des rayons issus des deux bords du document à travers les lentilles L2, L3 et L1 jusqu'au récepteur, pour la position choisie de la lentille mobile L3">
<line x1="20" y1="165" x2="738" y2="165" stroke="#94A3B8" stroke-width="1.2"/><polygon points="746,165 736,161 736,169" fill="#94A3B8"/>
<g id="pc-ext" fill="none" stroke-width="1.2" stroke-dasharray="5 4"></g>
<g id="pc-rays" fill="none" stroke-width="1.6" stroke-linejoin="round"></g>
<g id="pc-inter"></g>
<line x1="60" y1="105.6" x2="60" y2="224.4" stroke="#1E293B" stroke-width="5" stroke-linecap="round"/>
<circle cx="60" cy="105.6" r="5" fill="#2563EB"/><circle cx="60" cy="224.4" r="5" fill="#E11D48"/>
<text x="60" y="80" font-size="14" text-anchor="middle" fill="#1E293B" font-family="system-ui, sans-serif" font-weight="700">Document</text>
<line x1="693.6" y1="55" x2="693.6" y2="275" stroke="#CBD5E1" stroke-width="5" stroke-linecap="round"/>
<text x="693.6" y="42" font-size="14" text-anchor="middle" fill="#1E293B" font-family="system-ui, sans-serif" font-weight="700">Récepteur</text>
<g id="pc-img"></g>
<g stroke="#1E293B" stroke-width="2" fill="none">
<path d="M357,70 V260 M351,68 L357,78 L363,68 M351,262 L357,252 L363,262"/>
<path d="M396.6,70 V260 M390.6,68 L396.6,78 L402.6,68 M390.6,262 L396.6,252 L402.6,262"/>
</g>
<text x="342" y="282" font-size="14" text-anchor="end" fill="#1E293B" font-family="Georgia, serif" font-style="italic">(L<tspan font-size="10" dy="4">2</tspan><tspan dy="-4">)</tspan></text>
<text x="411" y="282" font-size="14" text-anchor="start" fill="#1E293B" font-family="Georgia, serif" font-style="italic">(L<tspan font-size="10" dy="4">1</tspan><tspan dy="-4">)</tspan></text>
<g id="pc-l3" transform="translate(357,0)">
<path d="M0,48 V282 M-6,58 L0,48 L6,58 M-6,272 L0,282 L6,272" fill="none" stroke="#D97706" stroke-width="2.6" stroke-linejoin="round"/>
<text x="0" y="38" font-size="14" text-anchor="middle" fill="#B45309" font-family="Georgia, serif" font-style="italic" font-weight="700">(L<tspan font-size="10" dy="4">3</tspan><tspan dy="-4">)</tspan></text>
</g>
<text id="pc-state" x="380" y="318" font-size="13" text-anchor="middle" fill="#64748B" font-family="system-ui, sans-serif"></text>
</svg>
<div class="pc-ctrl">
<button type="button" class="pc-btn" id="pc-b1" aria-pressed="true">Agrandissement (A4 → A3)</button>
<button type="button" class="pc-btn" id="pc-b2" aria-pressed="false">Réduction (A4 → A5)</button>
</div>
<div class="pc-ctrl">
<label class="pc-slider" for="pc-s"><span>Position de (L<sub>3</sub>)</span><input id="pc-s" type="range" min="180" max="204" step="0.1" value="180"><b id="pc-sv"></b></label>
<label><input type="checkbox" id="pc-chk"> image intermédiaire</label>
</div>
<div class="pc-out">
<div id="pc-txt"></div>
<svg viewBox="0 0 150 74" role="img" aria-label="Taille de la copie comparée à celle de l'original">
<rect x="14" y="12" width="35.4" height="50" fill="#F8FAFC" stroke="#64748B" stroke-width="1.2"/>
<text x="31.7" y="41" font-size="10" text-anchor="middle" fill="#64748B" font-family="system-ui, sans-serif">A4</text>
<path d="M56,37 h12" stroke="#94A3B8" stroke-width="1.5"/><polygon points="72,37 66,33.5 66,40.5" fill="#94A3B8"/>
<rect id="pc-copy" x="80" y="12" width="35.4" height="50" fill="#FEF3C7" stroke="#D97706" stroke-width="1.4"/>
<text id="pc-copyt" x="105" y="41" font-size="10" text-anchor="middle" fill="#92400E" font-family="system-ui, sans-serif" font-weight="700"></text>
</svg>
</div>
</div>
</blockquote>
</details>

<script>
(function () {
  var root = document.getElementById('pc-anim');
  if (!root) return;
  var NS = 'http://www.w3.org/2000/svg';
  var X0 = 60, KX = 1.65, CY = 165;          // échelle horizontale : 1,65 px/mm
  var D = 384, XA = 180, XB = 204;           // récepteur, positions extrêmes de L3 (mm)
  var F_DIV = -90, F3 = 35;                  // focales (mm)
  var H = 59.4;                              // demi-hauteur du document (px)
  var AIMS = [26, 4, -18];                   // hauteurs visées dans le plan de L2
  var COL = ['#2563EB', '#E11D48'];
  var gRays = root.querySelector('#pc-rays'), gExt = root.querySelector('#pc-ext');
  var gImg = root.querySelector('#pc-img'), gInter = root.querySelector('#pc-inter');
  var l3 = root.querySelector('#pc-l3'), slider = root.querySelector('#pc-s');
  var sv = root.querySelector('#pc-sv'), txt = root.querySelector('#pc-txt');
  var b1 = root.querySelector('#pc-b1'), b2 = root.querySelector('#pc-b2');
  var chk = root.querySelector('#pc-chk'), state = root.querySelector('#pc-state');
  var copy = root.querySelector('#pc-copy'), copyt = root.querySelector('#pc-copyt');
  var s = XA, raf = null;

  function px(x) { return X0 + KX * x; }
  function py(y) { return CY - y; }
  function fr(v, n) { return v.toFixed(n).replace('.', ',').replace('-', '−'); }
  function el(parent, name, attrs) {
    var e = document.createElementNS(NS, name);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    parent.appendChild(e);
    return e;
  }

  // Marche d'un rayon paraxial : à chaque lentille mince, la pente diminue de y/f'.
  function trace(y0, aim) {
    var lenses = [{ x: XA, f: F_DIV }, { x: s, f: F3 }, { x: XB, f: F_DIV }];
    var x = 0, y = y0, u = (aim - y0) / XA, pts = [[0, y0]], mid = null;
    lenses.forEach(function (L) {
      y += u * (L.x - x); x = L.x;
      if (pts[pts.length - 1][0] !== x) pts.push([x, y]);
      u -= y / L.f;
      if (x < XB) mid = { x: x, y: y, u: u };   // rayon dans l'espace entre O' et O1
    });
    y += u * (D - x);
    pts.push([D, y]);
    return { pts: pts, end: y, mid: mid };
  }

  function draw() {
    gRays.textContent = ''; gExt.textContent = ''; gImg.textContent = ''; gInter.textContent = '';
    l3.setAttribute('transform', 'translate(' + px(s) + ',0)');
    sv.textContent = fr(s, 0) + ' mm';
    var atA = Math.abs(s - XA) < 0.05, atB = Math.abs(s - XB) < 0.05;
    var ends = [], inter = [];
    [H, -H].forEach(function (y0, i) {
      var rays = AIMS.map(function (a) { return trace(y0, i ? -a : a); });
      rays.forEach(function (r) {
        el(gRays, 'polyline', { stroke: COL[i], opacity: 0.85,
          points: r.pts.map(function (p) { return px(p[0]) + ',' + py(p[1]); }).join(' ') });
      });
      var e = rays.map(function (r) { return r.end; });
      ends.push({ min: Math.min.apply(null, e), max: Math.max.apply(null, e), mean: (e[0] + e[1] + e[2]) / 3 });
      // image intermédiaire : point de concours des rayons dans l'espace entre O' et O1
      var a = rays[0].mid, b = rays[2].mid;
      var xi = a.x + (b.y - a.y) / (a.u - b.u);
      inter.push({ x: xi, y: a.y + a.u * (xi - a.x), rays: rays });
    });
    var sharp = ends[0].max - ends[0].min < 0.3;
    if (sharp) {
      el(gImg, 'line', { x1: px(D), x2: px(D), y1: py(ends[0].mean), y2: py(ends[1].mean),
        stroke: '#1E293B', 'stroke-width': 5, 'stroke-linecap': 'round' });
    }
    ends.forEach(function (e, i) {
      if (sharp) el(gImg, 'circle', { cx: px(D), cy: py(e.mean), r: 5, fill: COL[i] });
      else el(gImg, 'line', { x1: px(D), x2: px(D), y1: py(e.min), y2: py(e.max),
        stroke: COL[i], 'stroke-width': 7, 'stroke-linecap': 'round', opacity: 0.55 });
    });
    if (chk.checked && (atA || atB)) {
      inter.forEach(function (it, i) {
        it.rays.forEach(function (r) {
          var from = atA ? r.pts[r.pts.length - 2] : r.pts[1];
          el(gExt, 'line', { x1: px(from[0]), y1: py(from[1]), x2: px(it.x), y2: py(it.y), stroke: COL[i], opacity: 0.7 });
        });
      });
      el(gInter, 'line', { x1: px(inter[0].x), x2: px(inter[1].x), y1: py(inter[0].y), y2: py(inter[1].y),
        stroke: '#64748B', 'stroke-width': 3, 'stroke-linecap': 'round' });
      var t = el(gInter, 'text', { x: px(inter[0].x), y: py(-Math.abs(inter[0].y)) + 18, 'font-size': 12,
        'text-anchor': 'middle', fill: '#334155', 'font-family': 'system-ui, sans-serif', 'font-weight': 600,
        stroke: '#fff', 'stroke-width': 4, 'paint-order': 'stroke', 'stroke-linejoin': 'round' });
      t.textContent = atA ? 'objet virtuel pour (L₁)' : 'image virtuelle donnée par (L₂)';
    }
    b1.setAttribute('aria-pressed', atA); b2.setAttribute('aria-pressed', atB);
    state.textContent = atA ? '(L₃) accolée à (L₂) : ensemble convergent (f′ ≈ 57,3 mm) puis lentille divergente'
      : atB ? '(L₃) accolée à (L₁) : lentille divergente puis ensemble convergent (f′ ≈ 57,3 mm)'
      : '(L₃) entre (L₂) et (L₁)';
    if (sharp) {
      var g = ends[0].mean / H, k = Math.abs(g);
      var fmt = k > 1 ? 'A3' : 'A5';
      txt.innerHTML = '<span class="pc-net">Image nette sur le récepteur</span><br>grandissement <i>γ</i> = <b>' + fr(g, 2) +
        '</b> ≈ ' + (k > 1 ? '−√2' : '−1/√2') + '<br>' + (k > 1 ? 'aire × 2' : 'aire ÷ 2') + ' : A4 → ' + fmt;
      var w = 35.4 * k, h = 50 * k;
      copy.setAttribute('x', 105 - w / 2); copy.setAttribute('y', 37 - h / 2);
      copy.setAttribute('width', w); copy.setAttribute('height', h);
      copy.setAttribute('opacity', 1); copyt.textContent = fmt;
    } else {
      txt.innerHTML = '<span class="pc-flou">Image floue sur le récepteur</span><br>les faisceaux ne convergent plus dans son plan';
      copy.setAttribute('opacity', 0.25); copyt.textContent = '';
    }
  }

  function goTo(target) {
    if (raf) cancelAnimationFrame(raf);
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var from = s, t0 = null, dur = reduce ? 0 : 1400 * Math.abs(target - from) / (XB - XA);
    function step(t) {
      if (t0 === null) t0 = t;
      var k = dur ? Math.min(1, (t - t0) / dur) : 1;
      var e = k < 0.5 ? 2 * k * k : 1 - 2 * (1 - k) * (1 - k);
      s = from + (target - from) * e;
      slider.value = s;
      draw();
      raf = k < 1 ? requestAnimationFrame(step) : null;
    }
    raf = requestAnimationFrame(step);
  }

  b1.addEventListener('click', function () { goTo(XA); });
  b2.addEventListener('click', function () { goTo(XB); });
  slider.addEventListener('input', function () {
    if (raf) { cancelAnimationFrame(raf); raf = null; }
    s = parseFloat(slider.value); draw();
  });
  chk.addEventListener('change', draw);
  draw();
})();
</script>
