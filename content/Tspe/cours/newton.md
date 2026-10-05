+++
title = "Lois de Newton"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Point matériel et centre de masse {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On modélise un système mécanique par un <span class="imp nt-hole">point matériel</span>, point géométrique auquel on associe la masse $m$ du système.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On situera le point matériel au <span class="imp nt-hole">centre de masse</span> du système, position moyenne de répartition des masses du système.</p>
<p class="nt-note">On parle aussi de centre d'inertie, ou de centre de gravité dans le cas d'un champ de pesanteur uniforme.</p>
</div>

<div class="nt-lab" id="lab-cdm">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le mouvement d'un objet lancé en tournoyant</p>
<p class="nt-note">Deux boules de masses différentes reliées par une tige légère sont lancées en l'air en tournant sur elles-mêmes (vue au ralenti).</p>
<canvas style="height:320px;" aria-label="Haltère lancé en tournoyant : trajectoires compliquées des boules et trajectoire parabolique du centre de masse"></canvas>
<label class="nt-ctrl">Masse de la boule orange $m_2$&nbsp;: <b class="out-m"></b><input type="range" min="0.5" max="4" step="0.1" value="2"></label>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="boules" checked> trajectoires des boules</label>
<label class="nt-check"><input type="checkbox" data-p="cdm" checked> trajectoire du centre de masse G</label>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-msg">Les boules décrivent des courbes compliquées, mais le centre de masse G suit une simple parabole, comme une petite bille lancée de la même façon. Il est plus proche de la boule la plus lourde.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Modéliser le système par un point matériel placé en son centre de masse, c'est ne s'intéresser qu'au mouvement d'ensemble du système, en laissant de côté ses rotations et ses déformations.</p>
</div>

## Première loi de Newton ou principe d'inertie et référentiels galiléens {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">première loi de Newton</span> permet de définir les <span class="imp nt-hole">référentiels galiléens</span>.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Première loi de Newton</p>
<p>Il existe une famille de référentiels, appelés <span class="imp">référentiels galiléens</span>, tels que tout point matériel <span class="imp nt-hole">pseudo-isolé</span> (qui est soumis à des forces externes dont la somme est nulle) est soit <span class="imp nt-hole">au repos</span>, soit animé d'un <span class="imp nt-hole">mouvement rectiligne uniforme</span> par rapport à l'un de ces référentiels.</p>
<p class="nt-note">On parle aussi de référentiels inertiels.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Sur des <span class="imp nt-hole">durées suffisamment courtes</span> pour pouvoir négliger les effets de la rotation de la surface terrestre, le <b>référentiel terrestre</b> peut être considéré comme <b>galiléen</b>.</p>
</div>

<p class="nt-lead">La détermination d'un bon référentiel galiléen est expérimentale, seule la cohérence entre la théorie (première loi de Newton) et la mesure (mouvement rectiligne uniforme) valide le choix a posteriori.</p>

<div class="nt-lab" id="lab-gal">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Un palet sur un manège&nbsp;: galiléen ou pas&nbsp;?</p>
<p class="nt-note">Un palet glisse sans frottement sur un manège qui tourne (comme sur une table à coussin d'air)&nbsp;: les forces qu'il subit se compensent.</p>
<canvas style="height:340px;" aria-label="Trajectoire d'un palet glissant sur un manège en rotation, vue depuis le sol ou depuis le manège"></canvas>
<div class="nt-ctrl">Référentiel&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="gal" value="sol" checked><span>du sol</span></label>
<label><input type="radio" name="gal" value="manege"><span>du manège</span></label>
</div>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Dans un référentiel galiléen</p>
<p class="nt-f-math">$$\sum \vec{F}_\mathrm{ext} = \vec{0} \Leftrightarrow \vec{v}=\overrightarrow{\text{cte}}\text{ (MRU)}$$</p>
<div class="nt-f-units"><span>où $\vec{F}_\mathrm{ext}$ est une force extérieure agissant sur le système</span></div>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Des vidéos pour voir l'inertie à l'œuvre</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://www.youtube.com/watch?v=wV2UTkkQ0Fg&t=15s" target="_blank" rel="noopener">Une vidéo sur le principe d'inertie</a> (à partir de 0'15'').</li>
</ul>
<p>Un objet posé ne se met pas en mouvement tout seul, et un objet lancé continue sur sa lancée&nbsp;: c'est ce qui rend dangereux un freinage brutal pour les passagers non attachés, qui continuent leur mouvement «&nbsp;sur leur lancée&nbsp;».</p>
</div>
</details>

## Deuxième loi de Newton {.nt-h2}

<p class="nt-lead">La deuxième loi de Newton lie la <b>cinématique</b> à la <b>dynamique</b>, le <b>mouvement</b> aux <b>forces</b>.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Deuxième loi de Newton</p>
<p>Dans un <span class="imp nt-hole">référentiel galiléen</span>, le produit de la masse par l'<span class="imp nt-hole">accélération</span> d'un point matériel est égal à la <span class="imp nt-hole">résultante des forces extérieures</span> qu'il subit.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Dans un référentiel galiléen</p>
<p class="nt-f-math">$$\sum \vec{F}_\mathrm{ext} = m\,\vec{a}$$</p>
<div class="nt-f-units"><span>$F_\mathrm{ext}$ en <span class="nt-hole">$\pu{N}$</span></span><span>$m$ en <span class="nt-hole">$\pu{kg}$</span></span><span>$a$ en <span class="nt-hole">$\pu{m*s-2}$</span></span></div>
</div>

<div class="nt-lab" id="lab-force">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">La force donne la direction de l'accélération, pas celle de la vitesse</p>
<p class="nt-note">Un palet, lancé vers la droite, subit une force constante dont on règle la norme et la direction (les autres forces se compensent).</p>
<canvas style="height:320px;" aria-label="Palet soumis à une force constante : sa trajectoire, son vecteur vitesse, la force et son vecteur accélération"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Norme de la force $F$&nbsp;: <b class="out-F"></b><input type="range" data-p="F" min="0" max="6" step="0.1" value="1"></label>
<label class="nt-ctrl">Direction de la force&nbsp;: <b class="out-ang"></b><input type="range" data-p="ang" min="0" max="360" step="5" value="90"></label>
<label class="nt-ctrl">Masse $m$&nbsp;: <b class="out-m"></b><input type="range" data-p="m" min="0.5" max="4" step="0.1" value="2"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$a = F/m$ = <b class="out-a"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">En rouge&nbsp;: la force&nbsp;; en vert pointillé&nbsp;: l'accélération&nbsp;; en orange&nbsp;: la vitesse. Les points sont espacés de 0,2&nbsp;s.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Qu'obtient-on dans le cas d'un MRU&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Dans un MRU, $\vec{a} = \vec{0}$, donc $\sum \vec{F}_\mathrm{ext} = \vec{0}$.</p>
<p>On pourrait croire alors que la 2<sup>e</sup> loi rend la 1<sup>re</sup> inutile. Mais la 1<sup>re</sup> affirme surtout l'existence de référentiels galiléens, or la 2<sup>e</sup> n'est valide que dans ceux-ci&nbsp;!</p>
</div>
</details>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On appelle aussi la 2<sup>e</sup> loi de Newton le <span class="imp nt-hole">principe fondamental de la dynamique (PFD)</span>.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La forme générale, avec la quantité de mouvement</span></summary>
<div class="nt-d-body">
<p>Newton a énoncé sa deuxième loi avec la <b>quantité de mouvement</b> $\vec{p} = m\,\vec{v}$&nbsp;: $\sum \vec{F}_\mathrm{ext} = \dfrac{\mathrm{d}\vec{p}}{\mathrm{d}t}$.</p>
<p>Quand la masse du système est constante, $\dfrac{\mathrm{d}\vec{p}}{\mathrm{d}t} = m\,\dfrac{\mathrm{d}\vec{v}}{\mathrm{d}t} = m\,\vec{a}$, et l'on retrouve la forme habituelle. La forme générale devient indispensable quand la masse varie, par exemple pour une fusée qui éjecte ses gaz.</p>
<p>Une <a href="https://www.youtube.com/watch?v=sPZ2bjW53c8&t=32s" target="_blank" rel="noopener">vidéo sur la deuxième loi de Newton</a> (à partir de 0'32'').</p>
</div>
</details>

## Troisième loi de Newton ou principe des actions réciproques {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Troisième loi de Newton</p>
<p>Si un système A agit sur un système B, alors le système B agit sur le système A avec une action <span class="imp nt-hole">parfaitement opposée</span> à celle de A sur B.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Principe des actions réciproques</p>
<p class="nt-f-math">$$\vec{F}_{B/A} = -\vec{F}_{A/B}$$</p>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 600 340" role="img" aria-label="Interaction entre la Terre et une pomme : la force exercée par la Terre sur la pomme et la force exercée par la pomme sur la Terre ont même direction, même norme et des sens opposés"><defs><radialGradient id="gEarth" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#BFDBFE"/><stop offset="1" stop-color="#60A5FA"/></radialGradient><radialGradient id="gApple" cx=".35" cy=".35" r=".8"><stop offset="0" stop-color="#FCA5A5"/><stop offset="1" stop-color="#DC2626"/></radialGradient></defs><circle cx="300" cy="250" r="78" fill="url(#gEarth)"/><path d="M248,230 q25,-30 60,-18 q16,14 -4,30 q-30,10 -56,-12z M318,268 q30,-16 52,0 q-8,22 -40,20z" fill="#86EFAC" opacity=".9"/><text x="300" y="318" font-size="14" fill="var(--navy)" text-anchor="middle" font-weight="700">Terre</text><circle cx="300" cy="62" r="22" fill="url(#gApple)"/><path d="M300,41 q3,-11 11,-15" fill="none" stroke="#7C2D12" stroke-width="3" stroke-linecap="round"/><path d="M304,35 q12,-10 22,-2 q-10,8 -22,2z" fill="#22C55E"/><text x="232" y="68" font-size="15" fill="var(--ink)" text-anchor="end" font-weight="700">pomme</text><line x1="300" y1="62" x2="300.0" y2="133.0" stroke="var(--rose)" stroke-width="3.2" stroke-linecap="round"/><polygon points="300.0,142.0 294.5,131.0 305.5,131.0" fill="var(--rose)"/><text x="316" y="120" font-size="19" fill="var(--rose)" font-family="Georgia, serif" font-style="italic" font-weight="700">F<tspan font-size="12" dy="5">Terre/pomme</tspan></text><line x1="316" y1="103" x2="330" y2="103" stroke="var(--rose)" stroke-width="1.5"/><polygon points="333.0,103.0 327.0,106.0 327.0,100.0" fill="var(--rose)"/><line x1="300" y1="250" x2="300.0" y2="179.0" stroke="var(--navy)" stroke-width="3.2" stroke-linecap="round"/><polygon points="300.0,170.0 305.5,181.0 294.5,181.0" fill="var(--navy)"/><text x="316" y="214" font-size="19" fill="var(--navy)" font-family="Georgia, serif" font-style="italic" font-weight="700">F<tspan font-size="12" dy="5">pomme/Terre</tspan></text><line x1="316" y1="197" x2="330" y2="197" stroke="var(--navy)" stroke-width="1.5"/><polygon points="333.0,197.0 327.0,200.0 327.0,194.0" fill="var(--navy)"/><circle cx="300" cy="62" r="4" fill="var(--ink)"/><circle cx="300" cy="250" r="4" fill="var(--navy)"/><text x="570" y="330" font-size="12" fill="var(--slate)" text-anchor="end">échelles non respectées</text></svg>

<p class="nt-cap">La Terre attire la pomme, et la pomme attire la Terre avec une force de même norme. Mais la Terre étant environ $6\times10^{25}$ fois plus massive qu'une pomme de 100&nbsp;g, son accélération est imperceptible.</p>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Les deux forces s'appliquent sur deux systèmes <b>différents</b>&nbsp;: elles ne se compensent donc jamais. Pour étudier le mouvement d'un système, on ne fait la somme que des forces qui s'exercent <b>sur lui</b>.</p>
</div>

<div class="nt-lab" id="lab-react">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Deux patineurs qui se repoussent</p>
<canvas style="height:260px;" aria-label="Deux patineurs immobiles se poussent mutuellement puis s'éloignent l'un de l'autre"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Masse du patineur bleu $m_1$&nbsp;: <b class="out-m1"></b><input type="range" data-p="m1" min="30" max="100" step="5" value="80"></label>
<label class="nt-ctrl">Masse du patineur orange $m_2$&nbsp;: <b class="out-m2"></b><input type="range" data-p="m2" min="30" max="100" step="5" value="40"></label>
</div>
<div class="nt-read" aria-live="polite"><span>force pendant la poussée&nbsp;: <b class="out-F"></b> pour chacun</span><span>$a_1$ = <b class="out-a1"></b>, $a_2$ = <b class="out-a2"></b></span><span>vitesses finales&nbsp;: <b class="out-v1"></b> et <b class="out-v2"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi trois lois, et pas deux&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Pour déduire la 3<sup>e</sup> loi de la 2<sup>e</sup>, il faudrait ajouter au moins une hypothèse globale&nbsp;: la conservation de la quantité de mouvement d'un système isolé dans son ensemble, ou l'homogénéité de l'espace (les lois de la physique sont les mêmes partout), d'après le théorème d'Emmy Noether.</p>
<p>Les trois lois forment ainsi un triptyque minimal&nbsp;: <b>un cadre</b> (la 1<sup>re</sup> définit les référentiels galiléens), <b>un outil</b> (la 2<sup>e</sup> relie forces et mouvement) et <b>une symétrie</b> (la 3<sup>e</sup>). Supprimer l'une ou prétendre la déduire des deux autres ferait perdre soit la définition du référentiel, soit la conservation de la quantité de mouvement, deux piliers de la mécanique classique.</p>
<p>Deux vidéos pour voir la 3<sup>e</sup> loi en action&nbsp;: <a href="https://www.youtube.com/watch?v=36keC5eDUWk&t=80s" target="_blank" rel="noopener">première vidéo</a> et <a href="https://www.youtube.com/watch?v=OnoNITE-CLc&t=80s" target="_blank" rel="noopener">seconde vidéo</a> (à partir de 1'20'').</p>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CV = '#D97706', CA = '#059669', CF = '#E11D48', CP = '#2A6BC4';   /* vitesse, accélération, force, objets */
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function canvasCtx(cv) {
    var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function watchVisible(el, cb) {
    if (!('IntersectionObserver' in window)) { cb(true); return; }
    new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }).observe(el);
  }
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function arrow(c, x1, y1, x2, y2, color, w, dash) {
    var dx = x2 - x1, dy = y2 - y1, n = Math.hypot(dx, dy);
    if (n < 1) { return; }
    var ux = dx / n, uy = dy / n, L = Math.min(12, n * 0.45), W = L * 0.5;
    c.strokeStyle = color; c.fillStyle = color; c.lineWidth = w || 2.6; c.lineCap = 'round'; c.setLineDash(dash || []);
    c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2 - ux * L * 0.8, y2 - uy * L * 0.8); c.stroke(); c.setLineDash([]);
    c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - ux * L - uy * W, y2 - uy * L + ux * W); c.lineTo(x2 - ux * L + uy * W, y2 - uy * L - ux * W); c.closePath(); c.fill();
  }
  /* texte entouré d'un fin contour clair (lisible sans masquer les tracés) */
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '700 13px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.9)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  function vecLabel(c, s, x, y, color, sub) {   /* lettre surmontée d'une flèche, indice éventuel */
    c.font = 'italic 700 15px Georgia, serif'; c.textAlign = 'left'; c.lineJoin = 'round'; c.lineCap = 'round';
    var w = c.measureText(s).width, x0 = x - w / 2;
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.9)'; c.strokeText(s, x0, y);
    c.fillStyle = color; c.fillText(s, x0, y);
    if (sub) { c.font = 'italic 700 11px Georgia, serif'; c.strokeText(sub, x0 + w + 1, y + 4); c.fillText(sub, x0 + w + 1, y + 4); }
    c.strokeStyle = color; c.lineWidth = 1.3; c.beginPath();
    c.moveTo(x0, y - 14); c.lineTo(x0 + w, y - 14); c.moveTo(x0 + w, y - 14); c.lineTo(x0 + w - 4, y - 16.5); c.moveTo(x0 + w, y - 14); c.lineTo(x0 + w - 4, y - 11.5); c.stroke();
  }
  /* ================= 1. Le centre de masse d'un objet lancé ================= */
  (function () {
    var root = document.getElementById('lab-cdm');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rM = $(root, 'input[type="range"]'), cbB = $(root, '[data-p="boules"]'), cbG = $(root, '[data-p="cdm"]'), oM = $(root, '.out-m'), btn = $(root, '[data-act="play"]');
    var S, playing = !RM, visible = true, t = 0, last = null, G = 9.81, VX = 3.2, VY = 6.4, OM = 7.5, Lb = 0.9, TF = 2 * VY / G, SLOW = 2.2;
    function state(s, m2) {
      var m1 = 1, M = m1 + m2, cx = 0.4 + VX * s, cy = 0.4 + VY * s - 0.5 * G * s * s, ph = 0.3 + OM * s;
      var r1 = Lb * m2 / M, r2 = Lb * m1 / M;   /* distances au centre de masse */
      return { g: [cx, cy], b1: [cx - r1 * Math.cos(ph), cy - r1 * Math.sin(ph)], b2: [cx + r2 * Math.cos(ph), cy + r2 * Math.sin(ph)] };
    }
    function draw() {
      if (!S) { return; }
      var m2 = parseFloat(rM.value), c = S.ctx, w = S.w, h = S.h;
      oM.textContent = fr(m2, 1) + ' \u00d7 m\u2081';
      var xmax = 0.4 + VX * TF + 0.8, ymax = 0.4 + VY * VY / (2 * G) + 0.8, k = Math.min((w - 20) / xmax, (h - 20) / ymax);
      function X(x) { return 10 + x * k; }
      function Y(y) { return h - 10 - y * k; }
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#E2E8F0'; c.fillRect(0, Y(0), w, h - Y(0));
      var ts = Math.min((t % (TF * SLOW + 1.2)) / SLOW, TF);
      /* positions successives (stroboscopie) */
      for (var s = 0; s <= ts + 1e-9; s += 0.06) {
        var q = state(s, m2);
        if (cbB.checked) {
          c.fillStyle = 'rgba(42,107,196,.25)'; c.beginPath(); c.arc(X(q.b1[0]), Y(q.b1[1]), 3, 0, 2 * Math.PI); c.fill();
          c.fillStyle = 'rgba(217,119,6,.30)'; c.beginPath(); c.arc(X(q.b2[0]), Y(q.b2[1]), 3, 0, 2 * Math.PI); c.fill();
        }
        if (cbG.checked) { c.fillStyle = 'rgba(225,29,72,.75)'; c.beginPath(); c.arc(X(q.g[0]), Y(q.g[1]), 2.6, 0, 2 * Math.PI); c.fill(); }
      }
      var p = state(ts, m2), r1 = 8 + 3 * Math.cbrt(1), r2 = 8 * Math.cbrt(m2) + 3;
      c.strokeStyle = col('--slate'); c.lineWidth = 3; c.beginPath(); c.moveTo(X(p.b1[0]), Y(p.b1[1])); c.lineTo(X(p.b2[0]), Y(p.b2[1])); c.stroke();
      c.fillStyle = CP; c.beginPath(); c.arc(X(p.b1[0]), Y(p.b1[1]), r1, 0, 2 * Math.PI); c.fill();
      c.fillStyle = CV; c.beginPath(); c.arc(X(p.b2[0]), Y(p.b2[1]), r2, 0, 2 * Math.PI); c.fill();
      /* centre de masse : petite cible */
      var gx = X(p.g[0]), gy = Y(p.g[1]);
      c.fillStyle = '#fff'; c.beginPath(); c.arc(gx, gy, 6, 0, 2 * Math.PI); c.fill();
      c.fillStyle = CF; c.beginPath(); c.moveTo(gx, gy); c.arc(gx, gy, 6, 0, Math.PI / 2); c.lineTo(gx, gy); c.arc(gx, gy, 6, Math.PI, 1.5 * Math.PI); c.closePath(); c.fill();
      c.strokeStyle = CF; c.lineWidth = 1.5; c.beginPath(); c.arc(gx, gy, 6, 0, 2 * Math.PI); c.stroke();
      txt(c, 'G', gx + 14, gy - 8, CF, 'italic 700 14px Georgia, serif');
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    rM.addEventListener('input', function () { t = 0; draw(); });
    [cbB, cbG].forEach(function (x) { x.addEventListener('change', draw); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    if (RM) { t = TF * SLOW; }
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 2. Galiléen ou pas : le palet sur le manège ================= */
  (function () {
    var root = document.getElementById('lab-gal');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), btn = $(root, '[data-act="play"]'), S, mode = 'sol', playing = !RM, visible = true, t = 0, last = null;
    var OMEGA = 0.9, V = 0.55, P0 = [-0.85, -0.25], DIR = [0.93, 0.37], TMAX = 3.2;   /* rayon du manège : 1 */
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, k = Math.min(w, h) * 0.44, cx = w / 2, cy = h / 2;
      c.clearRect(0, 0, w, h);
      var ts = Math.min(t % (TMAX + 1.2), TMAX), rot = mode === 'sol' ? OMEGA * ts : 0;
      /* manège : disque et rayons repères (ils tournent dans le référentiel du sol) */
      c.fillStyle = '#EEF5FE'; c.strokeStyle = col('--blue'); c.lineWidth = 2; c.beginPath(); c.arc(cx, cy, k, 0, 2 * Math.PI); c.fill(); c.stroke();
      c.strokeStyle = 'rgba(42,107,196,.35)'; c.lineWidth = 1.5;
      for (var r = 0; r < 6; r++) { var a = rot + r * Math.PI / 3; c.beginPath(); c.moveTo(cx, cy); c.lineTo(cx + k * Math.cos(a), cy - k * Math.sin(a)); c.stroke(); }
      var hx = cx + k * 0.92 * Math.cos(rot + 0.5), hy = cy - k * 0.92 * Math.sin(rot + 0.5);
      c.fillStyle = col('--amber'); c.beginPath(); c.arc(hx, hy, 7, 0, 2 * Math.PI); c.fill();
      txt(c, 'observateur du manège', hx, hy - 12, col('--amber'), '600 11px system-ui, sans-serif');
      /* palet : mouvement rectiligne uniforme dans le référentiel du sol */
      function pos(s) {
        var x = P0[0] + V * DIR[0] * s, y = P0[1] + V * DIR[1] * s;
        if (mode === 'sol') { return [x, y]; }
        var a = -OMEGA * s;   /* coordonnées dans le référentiel tournant */
        return [x * Math.cos(a) - y * Math.sin(a), x * Math.sin(a) + y * Math.cos(a)];
      }
      for (var s = 0; s <= ts + 1e-9; s += 0.12) { var p = pos(s); c.fillStyle = 'rgba(225,29,72,.55)'; c.beginPath(); c.arc(cx + p[0] * k, cy - p[1] * k, 3.2, 0, 2 * Math.PI); c.fill(); }
      var q = pos(ts); c.fillStyle = CF; c.beginPath(); c.arc(cx + q[0] * k, cy - q[1] * k, 9, 0, 2 * Math.PI); c.fill();
      msg.textContent = mode === 'sol'
        ? 'Dans le référentiel du sol (galiléen), le palet, pseudo-isolé (sans frottement), avance en ligne droite à vitesse constante : la première loi de Newton est vérifiée.'
        : 'Dans le référentiel du manège, le même palet décrit une courbe alors qu\u2019aucune force supplémentaire n\u2019agit sur lui : la première loi n\u2019est pas vérifiée, ce référentiel n\u2019est pas galiléen.';
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    $$(root, 'input[name="gal"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; t = 0; draw(); }); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    if (RM) { t = TMAX; }
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 3. La force oriente l'accélération ================= */
  (function () {
    var root = document.getElementById('lab-force');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rF = $(root, '[data-p="F"]'), rA = $(root, '[data-p="ang"]'), rM = $(root, '[data-p="m"]'), btn = $(root, '[data-act="play"]');
    var oF = $(root, '.out-F'), oA = $(root, '.out-ang'), oM = $(root, '.out-m'), oa = $(root, '.out-a'), msg = $(root, '.nt-msg');
    var S, playing = !RM, visible = true, t = 0, last = null, V0 = 1.6, TMAX = 4.5, X0 = [0.8, 1.0], WX = 10, WY = 5;
    function par() { var F = +rF.value, an = +rA.value * Math.PI / 180, m = +rM.value; return { F: F, an: an, m: m, ax: F / m * Math.cos(an), ay: F / m * Math.sin(an) }; }
    function pos(q, s) { return [X0[0] + V0 * s + 0.5 * q.ax * s * s, X0[1] + 0.5 * q.ay * s * s]; }
    function draw() {
      if (!S) { return; }
      var q = par(), c = S.ctx, w = S.w, h = S.h, k = Math.min(w / WX, h / WY);
      function X(x) { return 10 + x * k; }
      function Y(y) { return h - 10 - y * k; }
      oF.textContent = fr(q.F, 1) + ' N'; oA.textContent = Math.round(+rA.value) + '\u00b0'; oM.textContent = fr(q.m, 1) + ' kg';
      oa.textContent = fr(q.F / q.m, 2) + ' m\u00b7s\u207b\u00b2';
      c.clearRect(0, 0, w, h);
      /* durée : on arrête quand le palet sort du cadre */
      var ts = t % (TMAX + 1.0), tend = TMAX;
      for (var s0 = 0; s0 <= TMAX; s0 += 0.02) { var pp = pos(q, s0); if (pp[0] < 0.3 || pp[0] > WX - 1.4 || pp[1] < 0.6 || pp[1] > WY - 1.3) { tend = s0; break; }   /* marge pour que les vecteurs restent visibles */ }
      ts = Math.min(ts, tend);
      for (var s = 0; s <= ts + 1e-9; s += 0.2) { var p = pos(q, s); c.fillStyle = 'rgba(42,107,196,.45)'; c.beginPath(); c.arc(X(p[0]), Y(p[1]), 3.5, 0, 2 * Math.PI); c.fill(); }
      var P = pos(q, ts), vx = V0 + q.ax * ts, vy = q.ay * ts, px = X(P[0]), py = Y(P[1]);
      c.fillStyle = CP; c.beginPath(); c.arc(px, py, 10, 0, 2 * Math.PI); c.fill();
      var KV = 0.8 * k, KA = 1.5 * k, KF = 0.9 * k;
      function cap(L) { return Math.min(L, 3 * k); }   /* longueur maximale des flèches */
      arrow(c, px, py, px + vx * KV, py - vy * KV, CV, 3);
      if (q.F > 0) {
        var LF = cap(q.F * KF), LA = cap(q.F / q.m * KA), ca = Math.cos(q.an), sa = Math.sin(q.an);
        arrow(c, px, py, px + LF * ca, py - LF * sa, CF, 3);
        var ox = 7 * sa, oy = 7 * ca;   /* décalage latéral : F et a sont colinéaires, on les dessine côte à côte */
        arrow(c, px + ox, py + oy, px + ox + LA * ca, py + oy - LA * sa, CA, 2.6, [6, 4]);
        /* étiquettes de part et d'autre des flèches (elles sont colinéaires) */
        vecLabel(c, 'F', px + LF * ca + 16 * ca - 14 * sa, py - LF * sa - 16 * sa - 14 * ca + 6, CF);
        vecLabel(c, 'a', px + LA * 0.5 * ca + 22 * sa, py - LA * 0.5 * sa + 22 * ca + 6, CA);
      }
      var nv = Math.hypot(vx, vy) || 1;
      vecLabel(c, 'v', px + vx * KV + 14 * vx / nv, py - vy * KV - 14 * vy / nv + 6, CV);
      msg.textContent = q.F === 0 ? 'Aucune force : le palet garde sa vitesse, il est en mouvement rectiligne uniforme (première loi).'
        : 'Le vecteur accélération a toujours la direction et le sens de la force (deuxième loi), quelle que soit la direction de la vitesse : c\u2019est la vitesse qui « tourne » peu à peu vers la force.';
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    [rF, rA, rM].forEach(function (r) { r.addEventListener('input', function () { t = 0; draw(); }); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 4. Deux patineurs qui se repoussent ================= */
  (function () {
    var root = document.getElementById('lab-react');
    if (!root) { return; }
    var cv = $(root, 'canvas'), r1 = $(root, '[data-p="m1"]'), r2 = $(root, '[data-p="m2"]'), btn = $(root, '[data-act="play"]');
    var o1 = $(root, '.out-m1'), o2 = $(root, '.out-m2'), oF = $(root, '.out-F'), oa1 = $(root, '.out-a1'), oa2 = $(root, '.out-a2'), ov1 = $(root, '.out-v1'), ov2 = $(root, '.out-v2'), msg = $(root, '.nt-msg');
    var S, playing = !RM, visible = true, t = 0, last = null, F = 120, TP = 0.6, T0 = 0.8, TMAX = 4.2, GAP = 0.5;
    function st(s) {
      var m1 = +r1.value, m2 = +r2.value, a1 = F / m1, a2 = F / m2, x1 = -GAP / 2, x2 = GAP / 2, v1 = 0, v2 = 0, push = false;
      if (s > T0) {
        var u = Math.min(s - T0, TP); push = s - T0 < TP;
        x1 -= 0.5 * a1 * u * u; x2 += 0.5 * a2 * u * u; v1 = -a1 * u; v2 = a2 * u;
        if (s - T0 > TP) { var d = s - T0 - TP; x1 += v1 * d; x2 += v2 * d; }
      }
      return { m1: m1, m2: m2, a1: a1, a2: a2, x1: x1, x2: x2, v1: v1, v2: v2, push: push };
    }
    function skater(c, x, y, k, m, color) {   /* silhouette proportionnée à la masse */
      var sc = 0.75 + 0.25 * Math.cbrt(m / 60);
      c.strokeStyle = color; c.fillStyle = color; c.lineWidth = 5 * sc; c.lineCap = 'round';
      c.beginPath(); c.arc(x, y - 1.55 * k * sc, 0.14 * k * sc, 0, 2 * Math.PI); c.fill();
      c.beginPath(); c.moveTo(x, y - 1.4 * k * sc); c.lineTo(x, y - 0.8 * k * sc); c.lineTo(x - 0.18 * k * sc, y - 0.05 * k); c.moveTo(x, y - 0.8 * k * sc); c.lineTo(x + 0.18 * k * sc, y - 0.05 * k); c.stroke();
      c.lineWidth = 3; c.beginPath(); c.moveTo(x - 0.3 * k * sc, y); c.lineTo(x + 0.3 * k * sc, y); c.stroke();
    }
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, k = Math.min(w / 9, h / 2.6), cx = w / 2, yg = h - 26;
      var s = Math.min(t % (TMAX + 1.0), TMAX), q = st(s);
      o1.textContent = q.m1 + ' kg'; o2.textContent = q.m2 + ' kg';
      oF.textContent = F + ' N'; oa1.textContent = fr(q.a1, 2) + ' m\u00b7s\u207b\u00b2'; oa2.textContent = fr(q.a2, 2) + ' m\u00b7s\u207b\u00b2';
      var vf1 = q.a1 * TP, vf2 = q.a2 * TP; ov1.textContent = fr(vf1, 2) + ' m\u00b7s\u207b\u00b9'; ov2.textContent = fr(vf2, 2) + ' m\u00b7s\u207b\u00b9';
      c.clearRect(0, 0, w, h);
      var gi = c.createLinearGradient(0, yg, 0, h); gi.addColorStop(0, '#E0F2FE'); gi.addColorStop(1, '#F0F9FF'); c.fillStyle = gi; c.fillRect(0, yg, w, h - yg);
      c.strokeStyle = '#BAE6FD'; c.lineWidth = 1.5; c.beginPath(); c.moveTo(0, yg); c.lineTo(w, yg); c.stroke();
      function X(x) { return cx + x * k; }
      /* centre de masse : il reste immobile */
      var xg = (q.m1 * q.x1 + q.m2 * q.x2) / (q.m1 + q.m2);
      c.strokeStyle = 'rgba(225,29,72,.5)'; c.setLineDash([4, 4]); c.lineWidth = 1.5; c.beginPath(); c.moveTo(X(xg), yg - 2.1 * k); c.lineTo(X(xg), yg); c.stroke(); c.setLineDash([]);
      txt(c, 'G', X(xg) + 10, yg - 2.05 * k, CF, 'italic 700 13px Georgia, serif');
      var x1 = X(q.x1), x2 = X(q.x2);
      if (x1 > -40) { skater(c, x1, yg, k, q.m1, CP); }
      if (x2 < w + 40) { skater(c, x2, yg, k, q.m2, CV); }
      var ya = yg - 1.15 * k;
      if (q.push || s <= T0) {
        /* mains en contact : forces égales et opposées */
        c.strokeStyle = col('--slate'); c.lineWidth = 3; c.beginPath(); c.moveTo(x1, ya); c.lineTo(x1 + 0.22 * k, ya); c.moveTo(x2, ya); c.lineTo(x2 - 0.22 * k, ya); c.stroke();
        if (q.push) {
          var L = 0.9 * k;
          arrow(c, x2, ya - 18, x2 + L, ya - 18, CF, 3); vecLabel(c, 'F', x2 + L / 2, ya - 28, CF, '1/2');
          arrow(c, x1, ya - 18, x1 - L, ya - 18, CF, 3); vecLabel(c, 'F', x1 - L / 2, ya - 28, CF, '2/1');
        }
      } else {
        if (x1 > 0) { arrow(c, x1, ya, x1 + q.v1 * 0.55 * k, ya, CV, 3); }
        if (x2 < w) { arrow(c, x2, ya, x2 + q.v2 * 0.55 * k, ya, CV, 3); }
      }
      msg.textContent = s <= T0 ? 'Les deux patineurs sont immobiles, mains contre mains.'
        : (q.push ? 'Ils se poussent : chacun exerce sur l\u2019autre une force de même norme, de sens opposé (troisième loi).'
          : 'Même force, mais pas même effet : le plus léger acquiert la plus grande vitesse (a = F/m). Le centre de masse G, lui, n\u2019a pas bougé.');
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    [r1, r2].forEach(function (r) { r.addEventListener('input', function () { t = 0; draw(); }); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    if (RM) { t = T0 + TP + 1; }
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
})();
</script>
