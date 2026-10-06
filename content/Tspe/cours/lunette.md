+++
title = "Lunette astronomique"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Rappels sur les lentilles {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Lentille convergente</p>
<p>Une lentille convergente est caractérisée par sa <span class="imp nt-hole">distance focale</span> $f'=\overline{\mathrm{OF'}}$, où O est son <span class="imp nt-hole">centre optique</span> et F' son <span class="imp nt-hole">foyer image</span>.</p>
<p>Son <span class="imp">foyer objet</span> F est le symétrique de F' par rapport à O&nbsp;: $\overline{\mathrm{OF}}=-\overline{\mathrm{OF'}}=-f'$.</p>
<p class="nt-note">On la représente par un trait vertical terminé par deux pointes de flèche dirigées vers l'extérieur.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Les rayons émis par un objet très éloigné (objet «&nbsp;à l'infini&nbsp;») arrivent <span class="imp nt-hole">parallèles</span> entre eux.</li>
<li>Après la lentille, ces rayons parallèles <span class="imp nt-hole">convergent en un même point du plan focal image</span>. On trouve ce point grâce au <b>rayon qui passe par O</b>, le seul qui n'est pas dévié.</li>
<li>Si l'objet est dans la direction de l'axe optique, les rayons convergent au foyer image F'&nbsp;: $-\infty \xrightarrow{(L)} \mathrm{F'}$.</li>
<li>Pour que la lentille donne une image à l'infini (rayons émergents parallèles), l'objet doit être dans le <span class="imp nt-hole">plan focal objet</span>&nbsp;: $\mathrm{F} \xrightarrow{(L)} +\infty$.</li>
<li>Notre œil voit un objet sans accommoder (sans effort) lorsque cet objet est très loin, c'est-à-dire à l'infini&nbsp;: il reçoit alors des rayons parallèles.</li>
</ul>
</div>

<div class="nt-lab" id="lab-lentille">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">La lentille convergente et l'infini</p>
<canvas style="height:300px;" aria-label="Lentille convergente : faisceau parallèle qui converge dans le plan focal image, ou point du plan focal objet qui donne un faisceau parallèle"></canvas>
<div class="nt-ctrl">Situation&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="lmode" value="inf" checked><span>objet à l'infini</span></label>
<label><input type="radio" name="lmode" value="foc"><span>objet dans le plan focal objet</span></label>
</div>
</div>
<label class="nt-ctrl">Inclinaison&nbsp;: <b class="out-a"></b><input type="range" min="0" max="15" step="1" value="8"></label>
<p class="nt-msg" aria-live="polite"></p>
</div>

## La lunette afocale {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>L'oculaire</p>
<p>Beaucoup d'instruments d'optique (lunette astronomique, télescope, microscope…) se terminent par une lentille appelée <span class="imp nt-hole">oculaire</span>, dont le rôle est d'envoyer les rayons dans l'œil.</p>
<p>Dans l'idéal, ces rayons doivent être <span class="imp nt-hole">parallèles entre eux</span>&nbsp;: l'œil voit alors l'image sans accommoder.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Lunette afocale</p>
<p>Une lunette astronomique regarde des objets très lointains&nbsp;: les rayons issus d'un point objet arrivent eux aussi parallèles entre eux. Une lunette astronomique bien réglée est donc par définition <span class="imp nt-hole">afocale</span>&nbsp;:</p>
<p class="nt-center">$-\infty \xrightarrow{\text{(lunette astronomique)}}  + \infty$</p>
<p>L'image d'un objet à l'infini est située à l'infini.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-magnifying-glass-plus"></i>Grossir&nbsp;?</p>
<p>Une lunette astronomique permet de «&nbsp;grossir&nbsp;» des objets très éloignés. Grossir, c'est augmenter le <span class="imp nt-hole">diamètre apparent</span> de l'objet, c'est-à-dire l'<span class="imp nt-hole">angle</span> sous lequel l'objet est vu (et non sa taille&nbsp;!).</p>
<p>Si l'objet est vu sous l'angle $\color{#0284C7}\alpha$ sans la lunette et sous l'angle $\color{#BE185D}\alpha'$ à travers la lunette, le <span class="imp">grossissement</span> est&nbsp;:</p>
<p class="nt-center">$G=\dfrac{\color{#BE185D}\alpha'}{\color{#0284C7}\alpha}$</p>
<p class="nt-note">Exemple&nbsp;: le diamètre apparent du Soleil et de la Lune est d'environ 0,5°, soit 30 minutes d'angle.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Deux lentilles convergentes</p>
<p>On utilise <span class="imp">deux lentilles convergentes</span> pour réaliser une lunette astronomique de type Kepler&nbsp;: la première est l'<b style="color:#2A6BC4;">objectif</b>, la seconde l'<b style="color:#DB2777;">oculaire</b>.</p>
<ul class="nt-facts">
<li>Les rayons viennent de l'infini&nbsp;: ${\color{#2A6BC4}-\infty \xrightarrow{(\mathrm{objectif})} \mathrm{F'_{ob}}}$.</li>
<li>L'oculaire doit renvoyer les rayons à l'infini&nbsp;: ${\color{#DB2777}\mathrm{F_{oc}} \xrightarrow{(\mathrm{oculaire})} +\infty}$.</li>
</ul>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Condition d'afocalité</p>
<p>Le foyer image de l'objectif doit être <span class="imp nt-hole">confondu avec le foyer objet de l'oculaire</span>&nbsp;: ${\color{#2A6BC4}\mathrm{F'_{ob}}} = {\color{#DB2777}\mathrm{F_{oc}}}$.</p>
<p><b>Conséquence&nbsp;:</b> la distance $\mathrm{O_{ob}}\mathrm{O_{oc}}$ entre les deux lentilles (approximativement la longueur de la lunette) vaut <span class="imp nt-hole">$f'_\mathrm{ob}+f'_\mathrm{oc}$</span>.</p>
</div>

### Le grossissement de la lunette {.nt-h3}

<p class="nt-lead">Exprimons le grossissement en fonction de $f'_\mathrm{ob}$ et $f'_\mathrm{oc}$, à l'aide de la construction ci-dessous (dernière étape du tuto). $\color{#059669}\mathrm{A_i}\mathrm{B_i}$ est l'image réelle et renversée, par l'objectif, de l'objet lointain $\mathrm{A_\infty}\mathrm{B_\infty}$.</p>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration (à savoir refaire)</p>
<ol class="nt-steps">
<li><p>Dans le triangle rectangle $\mathrm{O_{ob}}\mathrm{A_i}\mathrm{B_i}$&nbsp;: $\mathrm{A_i}\mathrm{B_i}=f'_\mathrm{ob}\times\tan(\alpha)$.</p></li>
<li><p>Dans le triangle rectangle $\mathrm{O_{oc}}\mathrm{A_i}\mathrm{B_i}$&nbsp;: $\mathrm{A_i}\mathrm{B_i}=f'_\mathrm{oc}\times\tan(\alpha')$.</p></li>
<li><p>D'où $f'_\mathrm{ob}\times\tan(\alpha) = f'_\mathrm{oc}\times\tan(\alpha')$, soit $\dfrac{\tan(\alpha')}{\tan(\alpha)} = \dfrac{f'_\mathrm{ob}}{f'_\mathrm{oc}}$.</p></li>
<li><p>Dans l'approximation des petits angles ($\alpha,\alpha'\ll \pu{1 rad}$), $\tan(\alpha)\approx \alpha$ et $\tan(\alpha')\approx\alpha'$ (angles en radians).</p></li>
</ol>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Grossissement d'une lunette afocale</p>
<p class="nt-f-math">$$G =  \frac{\alpha'}{\alpha} = \frac{f'_\mathrm{ob}}{f'_\mathrm{oc}}$$</p>
<div class="nt-f-units"><span>$G > 1 \Leftrightarrow$ <b>$f'_\mathrm{ob} > f'_\mathrm{oc}$</b></span></div>
</div>

## Tuto&nbsp;: tracer la marche des rayons {.nt-h2}

<p class="nt-lead">C'est la compétence clé du chapitre. Suivez le tuto étape par étape, d'abord avec un objet dans la direction de l'axe (inclinaison nulle), puis avec un objet vu sous un angle $\alpha$.</p>

<div class="nt-lab" id="lab-tuto">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Construire, pas à pas, la marche des rayons dans une lunette</p>
<canvas style="height:400px;" aria-label="Lunette astronomique : construction progressive de la marche des rayons à travers l'objectif et l'oculaire"></canvas>
<p class="nt-msg" aria-live="polite" style="min-height:4.5em;"></p>
<div class="nt-btns">
<button type="button" class="nt-btn" data-act="prev"><i class="fa-solid fa-backward-step"></i>&nbsp; Étape précédente</button>
<button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Étape suivante</button>
<button type="button" class="nt-btn" data-act="all">Tout afficher</button>
</div>
<div class="nt-read" aria-live="polite"><span>étape <b class="out-step"></b></span><span>$G = f'_\mathrm{ob}/f'_\mathrm{oc}$ = <b class="out-g"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-preset="0">objet sur l'axe</button>
<button type="button" class="nt-btn" data-preset="5">objet vu sous un angle α</button>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">Angle $\alpha$ (exagéré)&nbsp;: <b class="out-al"></b><input type="range" data-p="al" min="0" max="8" step="0.5" value="5"></label>
<label class="nt-ctrl">$f'_\mathrm{ob}$&nbsp;: <b class="out-fob"></b><input type="range" data-p="fob" min="20" max="100" step="5" value="60"></label>
<label class="nt-ctrl">$f'_\mathrm{oc}$&nbsp;: <b class="out-foc"></b><input type="range" data-p="foc" min="5" max="40" step="1" value="15"></label>
</div>
<p class="nt-note">Sur un schéma, on exagère toujours l'angle $\alpha$, qui est en réalité minuscule pour un objet céleste&nbsp;: sinon, on ne verrait rien.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode&nbsp;: tracer la marche des rayons (objet vu sous un angle α)</p>
<ol class="nt-steps">
<li><p>Placer l'objectif, l'oculaire et les foyers, avec ${\color{#2A6BC4}\mathrm{F'_{ob}}} = {\color{#DB2777}\mathrm{F_{oc}}}$.</p></li>
<li><p>Tracer le rayon incident qui passe par $\mathrm{O_{ob}}$&nbsp;: il n'est pas dévié, et coupe le plan focal image de l'objectif en $\mathrm{B_i}$.</p></li>
<li><p>Placer l'image intermédiaire $\mathrm{A_i}\mathrm{B_i}$, renversée, avec $\mathrm{A_i}$ en $\mathrm{F'_{ob}}$, et prolonger le rayon <b>en ligne droite</b> au-delà de $\mathrm{B_i}$, jusqu'à l'oculaire.</p></li>
<li><p>Tracer en pointillés le rayon fictif $(\mathrm{B_i}\mathrm{O_{oc}})$, qui ne serait pas dévié par l'oculaire.</p></li>
<li><p>Tracer le rayon émergent <b>parallèle à ce rayon fictif</b>, et repérer l'angle $\alpha'$.</p></li>
<li><p>Tracer, si besoin, d'autres rayons&nbsp;: parallèles au premier avant l'objectif, ils passent tous par $\mathrm{B_i}$, puis ressortent tous parallèles au rayon fictif (voir l'astuce ci-dessous).</p></li>
</ol>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-wand-magic-sparkles"></i>L'astuce pour ajouter d'autres rayons</p>
<p>Une fois le premier rayon tracé (celui qui passe par $\mathrm{O_{ob}}$), tous les autres s'en déduisent sans calcul&nbsp;:</p>
<ul class="nt-facts">
<li><b>Avant l'objectif</b>, tous les rayons issus d'un même point à l'infini sont <span class="imp nt-hole">parallèles au premier</span>&nbsp;: on les trace à la règle et à l'équerre, ou en faisant glisser la règle.</li>
<li><b>Entre les lentilles</b>, ils passent tous par le <span class="imp nt-hole">même point $\mathrm{B_i}$</span>&nbsp;: on relie le point où chacun touche l'objectif à $\mathrm{B_i}$, et on prolonge.</li>
<li><b>Après l'oculaire</b>, ils sont tous <span class="imp nt-hole">parallèles au rayon fictif $(\mathrm{B_i}\mathrm{O_{oc}})$</span>&nbsp;: un seul trait de construction suffit pour tous les rayons.</li>
</ul>
<p>Deux points de passage ($\mathrm{O_{ob}}$ et $\mathrm{B_i}$) et deux directions (celle du faisceau incident et celle du rayon fictif) suffisent donc à tracer autant de rayons qu'on veut.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Qu'est-ce qui ne va pas dans le schéma de gauche&nbsp;?</p>
</div>

<svg class="nt-svg" viewBox="0 0 800 245" role="img" aria-label="À gauche, un schéma faux où les rayons changent de direction au point Bi ; à droite, le schéma juste où ils le traversent en ligne droite"><line x1="10" y1="120" x2="390" y2="120" stroke="#475569" stroke-width="1"/><line x1="60" y1="35" x2="60" y2="205" stroke="#2A6BC4" stroke-width="2.6"/><polygon points="60,31 53,41 67,41" fill="#2A6BC4"/><polygon points="60,209 53,199 67,199" fill="#2A6BC4"/><line x1="310" y1="64" x2="310" y2="176" stroke="#DB2777" stroke-width="2.6"/><polygon points="310,60 303,70 317,70" fill="#DB2777"/><polygon points="310,180 303,170 317,170" fill="#DB2777"/><line x1="250" y1="35" x2="250" y2="205" stroke="#94A3B8" stroke-dasharray="4 4"/><polyline points="10.0,113.9 60.0,120.0 250.0,143.3 310.0,120.0 390.0,88.9" fill="none" stroke="#D97706" stroke-width="1.8" stroke-linecap="round"/><polyline points="10.0,164.9 60.0,171.0 250.0,143.3 310.0,137.8 390.0,106.7" fill="none" stroke="#D97706" stroke-width="1.8" stroke-linecap="round"/><polyline points="10.0,62.9 60.0,69.0 250.0,143.3 310.0,102.2 390.0,71.0" fill="none" stroke="#D97706" stroke-width="1.8" stroke-linecap="round"/><circle cx="250" cy="143.3" r="4" fill="#059669"/><text x="256" y="159.3" font-size="13" fill="#059669" font-style="italic" font-weight="700" font-family="Georgia, serif">B<tspan font-size="9" dy="3">i</tspan></text><circle cx="250" cy="143.3" r="16" fill="none" stroke="#E11D48" stroke-width="2.4"/><text x="200" y="232" font-size="13" text-anchor="middle" fill="#E11D48" font-weight="800">✗ Faux : les rayons sont déviés en Bᵢ</text><line x1="410" y1="120" x2="790" y2="120" stroke="#475569" stroke-width="1"/><line x1="460" y1="35" x2="460" y2="205" stroke="#2A6BC4" stroke-width="2.6"/><polygon points="460,31 453,41 467,41" fill="#2A6BC4"/><polygon points="460,209 453,199 467,199" fill="#2A6BC4"/><line x1="710" y1="64" x2="710" y2="176" stroke="#DB2777" stroke-width="2.6"/><polygon points="710,60 703,70 717,70" fill="#DB2777"/><polygon points="710,180 703,170 717,170" fill="#DB2777"/><line x1="650" y1="35" x2="650" y2="205" stroke="#94A3B8" stroke-dasharray="4 4"/><polyline points="410.0,113.9 460.0,120.0 650.0,143.3 710.0,150.7 790.0,119.6" fill="none" stroke="#D97706" stroke-width="1.8" stroke-linecap="round"/><polyline points="410.0,164.9 460.0,171.0 650.0,143.3 710.0,134.6 790.0,103.5" fill="none" stroke="#D97706" stroke-width="1.8" stroke-linecap="round"/><polyline points="410.0,62.9 460.0,69.0 650.0,143.3 710.0,166.8 790.0,135.7" fill="none" stroke="#D97706" stroke-width="1.8" stroke-linecap="round"/><circle cx="650" cy="143.3" r="4" fill="#059669"/><text x="656" y="159.3" font-size="13" fill="#059669" font-style="italic" font-weight="700" font-family="Georgia, serif">B<tspan font-size="9" dy="3">i</tspan></text><text x="600" y="232" font-size="13" text-anchor="middle" fill="#059669" font-weight="800">✓ Juste : les rayons traversent Bᵢ en ligne droite</text></svg>

<p class="nt-cap">Les rayons ne doivent pas être déviés en $\mathrm{B_i}$&nbsp;: il n'y a pas de lentille à cet endroit&nbsp;! Ils le traversent en ligne droite et ne changent de direction qu'en traversant l'oculaire.</p>

### Complément&nbsp;: avec un œil réduit {.nt-h3}

<p class="nt-lead">On peut compléter le schéma en modélisant l'œil de l'observateur par un <b>œil réduit</b>&nbsp;: une lentille convergente (le cristallin) et un écran (la rétine). Un œil au repos voit net un objet à l'infini&nbsp;: la rétine est alors dans le plan focal image du cristallin.</p>

<div class="nt-lab" id="lab-oeil">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'image sur la rétine, à travers la lunette</p>
<canvas style="height:400px;" aria-label="Lunette suivie d'un œil réduit : les rayons parallèles qui sortent de l'oculaire convergent en un point de la rétine"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Angle $\alpha$ (exagéré)&nbsp;: <b class="out-al"></b><input type="range" data-p="al" min="0" max="8" step="0.5" value="4"></label>
<label class="nt-ctrl">$f'_\mathrm{ob}$&nbsp;: <input type="range" data-p="fob" min="20" max="100" step="5" value="60"></label>
<label class="nt-ctrl">$f'_\mathrm{oc}$&nbsp;: <input type="range" data-p="foc" min="5" max="40" step="1" value="15"></label>
</div>
<div class="nt-read" aria-live="polite"><span>taille de l'image sur la rétine (pour l'angle du schéma)&nbsp;: <b class="out-ret"></b></span></div>
<p class="nt-note">L'œil est placé là où le faisceau émergent est le plus étroit (le «&nbsp;cercle oculaire&nbsp;», image de l'objectif par l'oculaire)&nbsp;: tous les rayons y entrent. Les rayons parallèles qui sortent de l'oculaire convergent en un point B' de la rétine, que l'on trouve, là encore, grâce au rayon qui passe par le centre du cristallin.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La taille de l'image sur la rétine est proportionnelle à l'angle sous lequel on voit l'objet&nbsp;: $f'_\text{œil}\times\tan(\alpha)$ à l'œil nu, $f'_\text{œil}\times\tan(\alpha')$ à travers la lunette. Le grossissement $G=\alpha'/\alpha$ est donc aussi le facteur d'agrandissement de l'image sur la rétine&nbsp;: c'est ce que l'on perçoit comme un objet «&nbsp;plus gros&nbsp;».</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Une vidéo et une simulation</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://www.youtube.com/watch?v=rh-o9qHK6Lg" target="_blank" rel="noopener">Une vidéo sur le tracé pas-à-pas des rayons</a>.</li>
<li><a href="https://coursphychi.github.io/lunette.html" target="_blank" rel="noopener">Une simulation de lunette astronomique</a>, pour explorer d'autres réglages.</li>
</ul>
</div>
</details>

## Caractéristiques d'une lunette astronomique {.nt-h2}

<svg class="nt-svg nt-svg-m" viewBox="0 0 640 330" role="img" aria-label="Lunette astronomique : objectif, tube, oculaire, chercheur et trépied"><g transform="rotate(-12 320 150)"><rect x="110" y="120" width="380" height="62" rx="8" fill="#CBD5E1" stroke="#475569" stroke-width="2"/><rect x="80" y="110" width="44" height="82" rx="8" fill="#1E293B"/><ellipse cx="80" cy="151" rx="10" ry="40" fill="#60A5FA" stroke="#1E3A8A" stroke-width="2"/><rect x="490" y="135" width="40" height="32" rx="4" fill="#475569"/><rect x="530" y="140" width="40" height="22" rx="3" fill="#1E293B"/><rect x="566" y="138" width="10" height="26" rx="2" fill="#DB2777"/><rect x="330" y="96" width="120" height="16" rx="5" fill="#64748B"/><rect x="350" y="110" width="8" height="12" fill="#64748B"/><rect x="420" y="110" width="8" height="12" fill="#64748B"/></g><line x1="300" y1="200" x2="230" y2="318" stroke="#475569" stroke-width="6" stroke-linecap="round"/><line x1="320" y1="200" x2="320" y2="322" stroke="#475569" stroke-width="6" stroke-linecap="round"/><line x1="340" y1="200" x2="410" y2="318" stroke="#475569" stroke-width="6" stroke-linecap="round"/><rect x="296" y="186" width="48" height="20" rx="5" fill="#334155"/><line x1="78" y1="200" x2="60" y2="270" stroke="#2A6BC4" stroke-width="1.4"/><text x="66" y="275" font-size="14" text-anchor="start" fill="#2A6BC4" font-weight="700">objectif</text><line x1="240" y1="150" x2="200" y2="70" stroke="#475569" stroke-width="1.4"/><text x="194" y="75" font-size="14" text-anchor="end" fill="#475569" font-weight="700">tube</text><line x1="400" y1="92" x2="420" y2="42" stroke="#475569" stroke-width="1.4"/><text x="420" y="32" font-size="14" text-anchor="middle" fill="#475569" font-weight="700">chercheur (lunette de visée)</text><line x1="568" y1="108" x2="580" y2="150" stroke="#DB2777" stroke-width="1.4"/><text x="580" y="168" font-size="14" text-anchor="middle" fill="#DB2777" font-weight="700">oculaire</text><line x1="410" y1="300" x2="470" y2="300" stroke="#475569" stroke-width="1.4"/><text x="476" y="305" font-size="14" text-anchor="start" fill="#475569" font-weight="700">trépied</text></svg>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-sun"></i>Collecter la lumière</p>
<p>Les étoiles autres que le Soleil sont trop loin pour être vues autrement que comme des points, même à travers une lunette astronomique. Mais la lunette a une autre utilité&nbsp;: elle permet d'augmenter la <span class="imp nt-hole">luminosité</span>, en concentrant la lumière qui traverse l'objectif. Pour cela, l'objectif doit avoir le <span class="imp nt-hole">plus grand diamètre possible</span>.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Les limites des grandes lentilles</p>
<ul class="nt-facts">
<li>Une lentille disperse la lumière&nbsp;: c'est l'<b>aberration chromatique</b> (les couleurs ne convergent pas au même point).</li>
<li>Une grande lentille est très lourde, et ne peut être tenue que par ses bords&nbsp;: elle fléchit sous son propre poids.</li>
<li>L'obtention d'un verre homogène et son polissage sont difficiles et longs&nbsp;: les coûts deviennent prohibitifs.</li>
</ul>
<p>Les miroirs gomment tous ces défauts&nbsp;: c'est pourquoi les grands télescopes sont réflecteurs et non réfracteurs. En pratique, on n'a jamais dépassé 1&nbsp;m pour l'objectif d'une lunette, alors qu'il existe (presque) des télescopes de 40&nbsp;m de diamètre.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les records</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li>La plus grande lunette du monde, à l'observatoire Yerkes (États-Unis), a un objectif de 1,02&nbsp;m de diamètre, pour une longueur de près de 19&nbsp;m.</li>
<li>Le plus grand miroir d'un seul tenant mesure 8,4&nbsp;m (observatoire Vera Rubin, au Chili).</li>
<li>Le plus grand télescope optique en service, le Gran Telescopio Canarias (îles Canaries), a un miroir primaire segmenté de 10,4&nbsp;m.</li>
<li>Le futur ELT (Extremely Large Telescope de l'ESO, en construction au Chili) aura un miroir primaire de 39&nbsp;m, formé de 798 segments.</li>
</ul>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li><b style="color:#2A6BC4;">Rôle de l'objectif&nbsp;:</b> il <span class="imp nt-hole">collecte la lumière</span> et forme l'image intermédiaire $\mathrm{A_i}\mathrm{B_i}$ de l'objet situé à l'infini.</li>
<li><b style="color:#DB2777;">Rôle de l'oculaire&nbsp;:</b> il sert de <span class="imp nt-hole">loupe</span>, en formant l'image de $\mathrm{A_i}\mathrm{B_i}$ à l'infini.</li>
</ul>
<p>Pour avoir la meilleure lunette astronomique, il faut donc&nbsp;:</p>
<ul class="nt-facts">
<li>un objectif de <b>grand diamètre</b>, pour collecter le plus de lumière possible&nbsp;;</li>
<li>une distance focale de l'objectif <b>grande par rapport à celle de l'oculaire</b>, pour avoir le plus grand grossissement possible.</li>
</ul>
<p>L'encombrement de la lunette est alors approximativement donné par la somme des distances focales de l'objectif et de l'oculaire.</p>
</div>

## Réaliser une lunette au banc d'optique (ECE) {.nt-h2}

<div class="nt-b nt-proto">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Protocole&nbsp;: réaliser et vérifier une lunette afocale</p>
<p class="nt-proto-legend"><span><span class="nt-must">surligné</span>&nbsp;: à écrire sur une copie</span><span class="nt-ece">gestes utiles en TP</span></p>
<ol class="nt-steps">
<li><p><span class="nt-must">Identifier l'objectif et l'oculaire&nbsp;: l'objectif est la lentille de plus grande distance focale</span> ($f' = 1/C$, si la vergence $C$ est indiquée en dioptries).</p>
<p class="nt-ece">Pour estimer rapidement une distance focale, former sur un écran (ou un mur) l'image nette d'un objet très lointain, par exemple le paysage vu par la fenêtre&nbsp;: la distance entre la lentille et l'écran vaut alors environ $f'$. La lentille la plus «&nbsp;bombée&nbsp;» est celle qui a la plus petite distance focale.</p></li>
<li><p><span class="nt-must">Disposer d'un objet à l'infini</span>&nbsp;: un objet très lointain, ou un objet lumineux placé dans le plan focal objet d'une lentille auxiliaire (collimateur).</p>
<p class="nt-ece">Pour régler un collimateur, on peut placer un miroir plan juste derrière la lentille auxiliaire&nbsp;: l'objet est dans le plan focal objet quand son image, renvoyée par le miroir, est nette sur l'objet lui-même (autocollimation).</p></li>
<li><p><span class="nt-must">Placer l'objectif, puis repérer sur un écran l'image intermédiaire de l'objet&nbsp;: elle se forme dans le plan focal image de l'objectif, à $f'_\mathrm{ob}$ de celui-ci</span>.</p>
<p class="nt-ece">Vérifier que l'image est nette et renversée, noter la position de l'écran sur le banc, puis retirer l'écran.</p></li>
<li><p><span class="nt-must">Placer l'oculaire de façon que son foyer objet soit confondu avec le foyer image de l'objectif&nbsp;: les deux lentilles sont distantes de $f'_\mathrm{ob}+f'_\mathrm{oc}$</span>.</p></li>
<li><p><span class="nt-must">Vérification à l'œil&nbsp;: en regardant dans l'oculaire, on doit voir l'image de l'objet lointain nette, sans accommoder</span> (œil au repos), et renversée.</p>
<p class="nt-ece">Placer l'œil près de l'oculaire, sur l'axe. Ajuster finement la position de l'oculaire sur le banc jusqu'à obtenir une image nette en gardant l'œil détendu, comme pour regarder au loin. Un élève myope ou hypermétrope garde ses lunettes, ou ajuste l'oculaire pour sa vue.</p></li>
<li><p><span class="nt-must">Vérification à l'écran&nbsp;: éclairée par un faisceau parallèle, la lunette doit en donner un autre en sortie. La tache lumineuse sur un écran placé derrière l'oculaire garde alors le même diamètre quand on éloigne l'écran</span>.</p>
<p class="nt-ece">Éclairer l'objectif avec le collimateur, et déplacer l'écran d'une vingtaine à une soixantaine de centimètres derrière l'oculaire&nbsp;: si la tache grossit ou rétrécit, l'oculaire est mal placé.</p></li>
<li><p><span class="nt-must">Mesurer le grossissement&nbsp;: comparer $G = f'_\mathrm{ob}/f'_\mathrm{oc}$ au rapport $D/d$ du diamètre $D$ du faisceau qui entre dans l'objectif et du diamètre $d$ du faisceau qui sort de l'oculaire</span>.</p>
<p class="nt-ece">Ce rapport vaut bien $G$&nbsp;: le faisceau parallèle entrant converge en $\mathrm{F'_{ob}}$ puis diverge jusqu'à l'oculaire, et les triangles semblables donnent $\dfrac{D}{d} = \dfrac{f'_\mathrm{ob}}{f'_\mathrm{oc}}$. Mesurer $d$ sur l'écran placé juste derrière l'oculaire.</p></li>
</ol>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Sécurité</p>
<p>Ne jamais viser le Soleil avec une lunette ou une lentille, même un instant&nbsp;: la lumière concentrée brûle instantanément et définitivement la rétine.</p>
</div>

<script>
(function () {
  'use strict';
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var COB = '#2A6BC4', COC = '#DB2777', CR = '#EAB308', CRM = '#CA8A04', CI = '#059669', CF = '#64748B';   /* objectif, oculaire, rayons (et rayon principal), image intermédiaire, constructions */   /* objectif, oculaire, rayons, image intermédiaire, constructions */
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
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '700 13px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.92)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  /* lettre avec indice (ex. « F' » + « ob ») */
  function lab(c, s, sub, x, y, color) {
    c.font = 'italic 700 15px Georgia, serif'; c.textAlign = 'left'; c.lineJoin = 'round';
    var w = c.measureText(s).width;
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.92)'; c.strokeText(s, x, y); c.fillStyle = color; c.fillText(s, x, y);
    if (sub) { c.font = 'italic 700 11px Georgia, serif'; c.strokeText(sub, x + w + 1, y + 5); c.fillText(sub, x + w + 1, y + 5); }
  }
  function lens(c, x, y0, H, color, name) {   /* lentille convergente : trait vertical, flèches vers l'extérieur */
    c.strokeStyle = color; c.fillStyle = color; c.lineWidth = 2.6;
    c.beginPath(); c.moveTo(x, y0 - H); c.lineTo(x, y0 + H); c.stroke();
    [[-1, y0 - H], [1, y0 + H]].forEach(function (q) {
      c.beginPath(); c.moveTo(x, q[1] + q[0] * 4); c.lineTo(x - 8, q[1] - q[0] * 9); c.lineTo(x + 8, q[1] - q[0] * 9); c.closePath(); c.fill();
    });
    if (name) { txt(c, name, x, y0 - H - 12, color, '700 13px system-ui, sans-serif'); }
  }
  function tick(c, x, y0, color) { c.strokeStyle = color; c.lineWidth = 2; c.beginPath(); c.moveTo(x, y0 - 6); c.lineTo(x, y0 + 6); c.stroke(); }
  function ray(c, pts, color, w, dash, arrowAt) {
    c.strokeStyle = color; c.lineWidth = w || 2; c.setLineDash(dash || []); c.lineCap = 'round';
    c.beginPath(); c.moveTo(pts[0][0], pts[0][1]); for (var i = 1; i < pts.length; i++) { c.lineTo(pts[i][0], pts[i][1]); } c.stroke(); c.setLineDash([]);
    (arrowAt || []).forEach(function (k) {   /* petite flèche au milieu du segment k */
      var a = pts[k], b = pts[k + 1], mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1], n = Math.hypot(dx, dy); if (n < 30) { return; }
      var ux = dx / n, uy = dy / n; c.fillStyle = color; c.beginPath(); c.moveTo(mx + ux * 6, my + uy * 6); c.lineTo(mx - ux * 5 - uy * 4.5, my - uy * 5 + ux * 4.5); c.lineTo(mx - ux * 5 + uy * 4.5, my - uy * 5 - ux * 4.5); c.closePath(); c.fill();
    });
  }
  function angleArc(c, x, y, r, a0, a1, color) {   /* secteur d'angle (angles en radians, sens écran) */
    c.fillStyle = color; c.globalAlpha = 0.28; c.beginPath(); c.moveTo(x, y); c.arc(x, y, r, a0, a1, a1 < a0); c.closePath(); c.fill(); c.globalAlpha = 1;
    c.strokeStyle = color; c.lineWidth = 1.4; c.beginPath(); c.arc(x, y, r, a0, a1, a1 < a0); c.stroke();
  }
  /* ================= 1. La lentille convergente seule ================= */
  (function () {
    var root = document.getElementById('lab-lentille');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rA = $(root, 'input[type="range"]'), oA = $(root, '.out-a'), msg = $(root, '.nt-msg'), S, mode = 'inf';
    function draw() {
      var al = +rA.value * Math.PI / 180, c = S.ctx, w = S.w, h = S.h, y0 = h / 2 + 10, xL = w * 0.45, f = Math.min(w * 0.22, 170), H = h * 0.36;
      oA.textContent = Math.round(+rA.value) + '\u00b0';
      c.clearRect(0, 0, w, h);
      c.strokeStyle = col('--slate'); c.lineWidth = 1.2; c.beginPath(); c.moveTo(14, y0); c.lineTo(w - 14, y0); c.stroke();
      txt(c, 'axe optique', w - 16, y0 + 18, col('--slate'), '600 11px system-ui, sans-serif', 'right');
      lens(c, xL, y0, H, COB);
      tick(c, xL - f, y0, CF); tick(c, xL + f, y0, CF);
      lab(c, 'O', '', xL + 6, y0 + 20, col('--ink')); lab(c, 'F', '', xL - f - 4, y0 + 22, CF); lab(c, "F'", '', xL + f - 4, y0 + 22, CF);
      var hs = [-0.8, -0.4, 0, 0.4, 0.8].map(function (k) { return k * H; }), t = Math.tan(al);
      if (mode === 'inf') {
        /* faisceau parallèle incliné de α (venant d'en haut à gauche) : converge dans le plan focal image */
        c.strokeStyle = 'rgba(100,116,139,.6)'; c.setLineDash([5, 4]); c.lineWidth = 1.2; c.beginPath(); c.moveTo(xL + f, y0 - H); c.lineTo(xL + f, y0 + H); c.stroke(); c.setLineDash([]);
        txt(c, 'plan focal image', xL + f + 6, y0 - H + 4, CF, '600 11px system-ui, sans-serif', 'left');
        var By = y0 + f * t;
        hs.forEach(function (hk) {
          var yl = y0 + hk, x0 = 20, ys = yl - (xL - x0) * t, xe = Math.min(w - 20, xL + f + 90);
          var ye = yl + (By - yl) * (xe - xL) / f, main = Math.abs(hk) < 1e-6;
          ray(c, [[x0, ys], [xL, yl], [xe, ye]], main ? CRM : CR, main ? 2.8 : 1.8, [], [0, 1]);
        });
        c.fillStyle = CI; c.beginPath(); c.arc(xL + f, By, 5, 0, 2 * Math.PI); c.fill(); lab(c, "B'", '', xL + f + 8, By + (al > 0 ? 18 : -8), CI);
        msg.textContent = al === 0 ? 'Objet à l\u2019infini dans la direction de l\u2019axe : les rayons, parallèles à l\u2019axe, convergent au foyer image F\u2019.'
          : 'Objet à l\u2019infini hors de l\u2019axe : les rayons, parallèles entre eux, convergent en un même point B\u2019 du plan focal image. On le trouve avec le rayon qui passe par O (en plus épais), le seul qui n\u2019est pas dévié.';
      } else {
        /* point objet B dans le plan focal objet : les rayons émergent parallèles au rayon (BO) */
        var Bx = xL - f, By2 = y0 - f * t;
        c.strokeStyle = 'rgba(100,116,139,.6)'; c.setLineDash([5, 4]); c.lineWidth = 1.2; c.beginPath(); c.moveTo(Bx, y0 - H); c.lineTo(Bx, y0 + H); c.stroke(); c.setLineDash([]);
        txt(c, 'plan focal objet', Bx - 6, y0 - H + 4, CF, '600 11px system-ui, sans-serif', 'right');
        var sl = (y0 - By2) / f;   /* pente du rayon (BO), conservée par tous les rayons émergents */
        hs.forEach(function (hk) {
          var yl = y0 + hk, xe = w - 20, ye = yl + sl * (xe - xL), main = Math.abs(hk) < 1e-6;
          ray(c, [[Bx, By2], [xL, yl], [xe, ye]], main ? CRM : CR, main ? 2.8 : 1.8, [], [0, 1]);
        });
        c.fillStyle = CI; c.beginPath(); c.arc(Bx, By2, 5, 0, 2 * Math.PI); c.fill(); lab(c, 'B', '', Bx - 18, By2 - 6, CI);
        msg.textContent = al === 0 ? 'Objet au foyer objet F : les rayons ressortent parallèles à l\u2019axe, l\u2019image est à l\u2019infini.'
          : 'Objet B dans le plan focal objet : tous les rayons ressortent parallèles au rayon qui passe par O (en plus épais). L\u2019image est à l\u2019infini, dans cette direction.';
      }
    }
    rA.addEventListener('input', draw);
    $$(root, 'input[name="lmode"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 2. Lunette : géométrie et tracé communs au tuto et à l'œil réduit ================= */
  function scope(c, w, h, P) {
    /* P : al (rad), fob, foc, step (0 à 6), eye ('simple' ou 'reduit') */
    var y0 = h / 2 + 8, Lw = w - (P.eye === 'reduit' ? 330 : 270), k = Lw / (P.fob + P.foc), xOb = 70, xF = xOb + P.fob * k, xOc = xF + P.foc * k;
    var Hob = h * 0.36, Hoc = Math.min(Hob, Math.max(h * 0.2, Hob * 1.1 * P.foc / P.fob + h * 0.12));
    var t = Math.tan(P.al), Biy = y0 + P.fob * k * t, sl = (y0 - Biy) / (xOc - xF), xEnd = w - 12, step = P.step;
    c.clearRect(0, 0, w, h);
    c.strokeStyle = col('--slate'); c.lineWidth = 1.2; c.beginPath(); c.moveTo(10, y0); c.lineTo(w - 10, y0); c.stroke();
    lens(c, xOb, y0, Hob, COB, 'objectif'); lens(c, xOc, y0, Hoc, COC, 'oculaire');
    tick(c, xF, y0, CF); tick(c, xOc + P.foc * k, y0, CF);
    lab(c, 'O', 'ob', xOb - 26, y0 + 20, COB); lab(c, 'O', 'oc', xOc + 6, y0 + 20, COC);
    lab(c, "F'", 'ob', xF - 34, y0 - 10, COB); lab(c, 'F', 'oc', xF + 5, y0 - 10, COC); lab(c, "F'", 'oc', xOc + P.foc * k - 6, y0 + 22, COC);
    c.strokeStyle = 'rgba(71,85,105,.7)'; c.lineWidth = 1; c.beginPath(); c.moveTo(xOb, y0 + Hob + 14); c.lineTo(xOc, y0 + Hob + 14); c.stroke();
    [xOb, xF, xOc].forEach(function (x) { c.beginPath(); c.moveTo(x, y0 + Hob + 9); c.lineTo(x, y0 + Hob + 19); c.stroke(); });
    lab(c, "f'", 'ob', (xOb + xF) / 2 - 10, y0 + Hob + 32, COB); lab(c, "f'", 'oc', (xF + xOc) / 2 - 10, y0 + Hob + 32, COC);
    if (step >= 1) { c.strokeStyle = 'rgba(100,116,139,.55)'; c.setLineDash([5, 4]); c.lineWidth = 1.1; c.beginPath(); c.moveTo(xF, y0 - Hob); c.lineTo(xF, y0 + Hob); c.stroke(); c.setLineDash([]); }
    /* œil réduit : cristallin (lentille) placé au cercle oculaire, rétine (écran) dans son plan focal */
    var E = null;
    if (P.eye === 'reduit') {
      var xE = xOc + P.foc * (P.fob + P.foc) / P.fob * k, fE = 46, HE = Math.max(26, h * 0.1);
      E = { x: xE, f: fE, H: HE, xr: xE + fE };
      c.strokeStyle = '#94A3B8'; c.lineWidth = 1.5; c.beginPath(); c.ellipse(xE + fE * 0.55, y0, fE * 0.75, HE * 1.45, 0, 0, 2 * Math.PI); c.stroke();
      lens(c, xE, y0, HE, '#0EA5E9');
      c.strokeStyle = '#B91C1C'; c.lineWidth = 3; c.beginPath(); c.moveTo(E.xr, y0 - HE * 1.15); c.lineTo(E.xr, y0 + HE * 1.15); c.stroke();
      txt(c, 'cristallin', xE, y0 - HE - 14, '#0284C7', '700 11px system-ui, sans-serif');
      txt(c, 'rétine', E.xr + 4, y0 + HE * 1.15 + 14, '#B91C1C', '700 11px system-ui, sans-serif', 'left');
      xEnd = xE;
    }
    var hs = [0, 0.75, -0.75, 0.38, -0.38].map(function (q) { return q * Hob * 0.92; }), outY = [];
    hs.forEach(function (hk, i) {
      var main = i === 0;
      if (!main && step < 5) { return; }            /* les autres rayons arrivent en dernier */
      if (main && step < 1) { return; }
      var yl = y0 + hk, ys = yl - (xOb - 10) * t, color = main ? CRM : CR, wd = main ? 2.8 : 1.8;
      var yoc = yl + (Biy - yl) * (xOc - xOb) / (xF - xOb);
      ray(c, [[10, ys], [xOb, yl], [xF, Biy]], color, wd, [], [0, 1]);
      if (main ? step >= 2 : true) { ray(c, [[xF, Biy], [xOc, yoc]], color, wd, [], [0]); }
      if (main ? step >= 4 : true) {
        var ye = yoc + sl * (xEnd - xOc); ray(c, [[xOc, yoc], [xEnd, ye]], color, wd, [], [0]); outY.push(yoc);
        if (E) {   /* dans l'œil : convergence sur la rétine, au point situé sur le rayon passant par le centre du cristallin */
          var yr = y0 + sl * E.f;
          if (Math.abs(ye - y0) < E.H) { ray(c, [[E.x, ye], [E.xr, yr]], color, wd); }
        }
      }
    });
    if (step >= 1 && P.al > 0) { angleArc(c, xOb, y0, 70, 0, Math.atan2(Biy - y0, xF - xOb), '#38BDF8'); lab(c, '\u03b1', '', xOb + 74, y0 + 16, '#0284C7'); }
    if (step >= 1) { c.fillStyle = CI; c.beginPath(); c.arc(xF, Biy, 4.5, 0, 2 * Math.PI); c.fill(); }
    if (step >= 2 && P.al > 0) {
      c.strokeStyle = CI; c.lineWidth = 3; c.beginPath(); c.moveTo(xF, y0); c.lineTo(xF, Biy - 6); c.stroke();
      c.fillStyle = CI; c.beginPath(); c.moveTo(xF, Biy); c.lineTo(xF - 5, Biy - 9); c.lineTo(xF + 5, Biy - 9); c.closePath(); c.fill();
      lab(c, 'B', 'i', xF + 7, Biy + 16, CI); lab(c, 'A', 'i', xF + 7, y0 + 18, CI);
    }
    if (step >= 3 && P.al > 0) { ray(c, [[xF, Biy], [xOc, y0], [xEnd, y0 + sl * (xEnd - xOc)]], CF, 1.6, [6, 5]); }
    if (step >= 4 && P.al > 0) { angleArc(c, xOc, y0, 60, 0, Math.atan2(sl, 1), '#F472B6'); lab(c, '\u03b1\u2019', '', xOc + 64, y0 - 10, '#BE185D'); }
    if (E && step >= 4) {
      var yr2 = y0 + sl * E.f;
      ray(c, [[E.x, y0], [E.xr, yr2]], CF, 1.4, [4, 4]);   /* rayon fictif par le centre du cristallin */
      c.fillStyle = '#B91C1C'; c.beginPath(); c.arc(E.xr, yr2, 4.5, 0, 2 * Math.PI); c.fill(); lab(c, "B'", '', E.xr + 6, yr2 + (sl < 0 ? -6 : 16), '#B91C1C');
    }
    if (!E && step >= 6) {
      var ex = Math.min(xEnd - 34, xOc + P.foc * k + 70), ym = outY.length ? outY.reduce(function (s0, v) { return s0 + v; }, 0) / outY.length : y0, ey = ym + sl * (ex - xOc);
      c.fillStyle = '#fff'; c.strokeStyle = col('--ink'); c.lineWidth = 1.8;
      c.beginPath(); c.ellipse(ex + 14, ey, 16, 12, 0, 0, 2 * Math.PI); c.fill(); c.stroke();
      c.fillStyle = '#0EA5E9'; c.beginPath(); c.arc(ex + 4, ey, 6, 0, 2 * Math.PI); c.fill();
      c.fillStyle = '#0F172A'; c.beginPath(); c.arc(ex + 2, ey, 3, 0, 2 * Math.PI); c.fill();
    }
    return { sl: sl, E: E };
  }
  /* ----- le tuto pas à pas ----- */
  (function () {
    var root = document.getElementById('lab-tuto');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rA = $(root, '[data-p="al"]'), rOb = $(root, '[data-p="fob"]'), rOc = $(root, '[data-p="foc"]');
    var btnN = $(root, '[data-act="next"]'), btnP = $(root, '[data-act="prev"]'), btnA = $(root, '[data-act="all"]'), oA = $(root, '.out-al'), oOb = $(root, '.out-fob'), oOc = $(root, '.out-foc'), oG = $(root, '.out-g'), oS = $(root, '.out-step'), msg = $(root, '.nt-msg');
    var S, step = 0, NSTEP = 6;
    var Fob = "F'<sub>ob</sub>", Foc = 'F<sub>oc</sub>', Oob = 'O<sub>ob</sub>', Ooc = 'O<sub>oc</sub>', Bi = 'B<sub>i</sub>', Ai = 'A<sub>i</sub>', Binf = 'B<sub>\u221e</sub>';
    var MSG_B = [
      'On place l\u2019objectif (bleu) et l\u2019oculaire (rose) sur l\u2019axe optique, de façon que le foyer image de l\u2019objectif ' + Fob + ' soit confondu avec le foyer objet de l\u2019oculaire ' + Foc + '. Les deux lentilles sont donc distantes de f\u2019<sub>ob</sub> + f\u2019<sub>oc</sub>.',
      '<b>1.</b> On trace d\u2019abord le rayon issu de ' + Binf + ' qui passe par le centre optique ' + Oob + ' : il n\u2019est pas dévié. Il coupe le plan focal image de l\u2019objectif en ' + Bi + '.',
      '<b>2.</b> ' + Bi + ' est l\u2019image de ' + Binf + ' par l\u2019objectif : l\u2019image intermédiaire ' + Ai + Bi + ' est renversée, avec ' + Ai + ' en ' + Fob + '. Le rayon continue <b>en ligne droite</b> jusqu\u2019à l\u2019oculaire : il passe par ' + Bi + ' sans y être dévié, car il n\u2019y a pas de lentille en ' + Bi + ' !',
      '<b>3.</b> Pour savoir comment il ressort de l\u2019oculaire, on trace le rayon fictif (en pointillés) qui va de ' + Bi + ' au centre optique ' + Ooc + ' : ce rayon-là ne serait pas dévié.',
      '<b>4.</b> Comme ' + Bi + ' est dans le plan focal objet de l\u2019oculaire, tout rayon issu de ' + Bi + ' ressort parallèle au rayon fictif. Le rayon émergent fait l\u2019angle \u03b1\u2019 avec l\u2019axe : c\u2019est l\u2019angle sous lequel on voit l\u2019objet à travers la lunette.',
      '<b>5.</b> Les autres rayons se tracent alors sans effort : issus de ' + Binf + ', ils arrivent <b>parallèles au premier</b> ; après l\u2019objectif, ils passent <b>tous par ' + Bi + '</b> ; et après l\u2019oculaire, ils ressortent <b>tous parallèles au rayon fictif</b>.',
      '<b>6.</b> L\u2019œil, placé derrière l\u2019oculaire, reçoit des rayons parallèles : il voit l\u2019objet sans accommoder, sous l\u2019angle \u03b1\u2019, plus grand que \u03b1.'
    ];
    var MSG_A = [
      MSG_B[0],
      '<b>1.</b> L\u2019objet est dans la direction de l\u2019axe : le rayon qui passe par ' + Oob + ' est l\u2019axe optique lui-même. Il arrive au foyer image ' + Fob + '.',
      '<b>2.</b> L\u2019image intermédiaire est réduite à un point, en ' + Fob + '. Le rayon continue en ligne droite, le long de l\u2019axe, jusqu\u2019à l\u2019oculaire.',
      '<b>3.</b> Le rayon fictif qui relie ' + Fob + ' à ' + Ooc + ' est ici l\u2019axe optique lui-même.',
      '<b>4.</b> Les rayons issus de ' + Fob + ' = ' + Foc + ' ressortent donc parallèles à l\u2019axe : l\u2019image est à l\u2019infini, la lunette est afocale.',
      '<b>5.</b> Les autres rayons, parallèles à l\u2019axe, convergent tous en ' + Fob + ' après l\u2019objectif, puis ressortent tous parallèles à l\u2019axe. Le faisceau est plus étroit, et ses rayons sont dans l\u2019ordre inverse.',
      '<b>6.</b> L\u2019œil, placé derrière l\u2019oculaire, reçoit des rayons parallèles : il voit l\u2019objet sans accommoder.'
    ];
    function draw() {
      var al = +rA.value * Math.PI / 180, fob = +rOb.value, foc = +rOc.value, G = fob / foc, alp = Math.atan(G * Math.tan(al));
      oA.textContent = fr(+rA.value, 1) + '\u00b0'; oOb.textContent = fob + ' cm'; oOc.textContent = foc + ' cm';
      oG.textContent = fr(G, 1) + (al > 0 ? '  (\u03b1\u2019 = ' + fr(alp * 180 / Math.PI, 1) + '\u00b0 sur le schéma)' : '');
      oS.textContent = step + ' / ' + NSTEP;
      scope(S.ctx, S.w, S.h, { al: al, fob: fob, foc: foc, step: step, eye: 'simple' });
      msg.innerHTML = (al > 0 ? MSG_B : MSG_A)[step];
      btnN.disabled = step >= NSTEP; btnP.disabled = step <= 0;
    }
    btnN.addEventListener('click', function () { if (step < NSTEP) { step++; draw(); } });
    btnP.addEventListener('click', function () { if (step > 0) { step--; draw(); } });
    btnA.addEventListener('click', function () { step = NSTEP; draw(); });
    [rA, rOb, rOc].forEach(function (r) { r.addEventListener('input', draw); });
    $$(root, '[data-preset]').forEach(function (b) { b.addEventListener('click', function () { rA.value = b.getAttribute('data-preset'); step = 0; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ----- complément : l'œil réduit ----- */
  (function () {
    var root = document.getElementById('lab-oeil');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rA = $(root, '[data-p="al"]'), rOb = $(root, '[data-p="fob"]'), rOc = $(root, '[data-p="foc"]'), oA = $(root, '.out-al'), oR = $(root, '.out-ret'), S;
    function draw() {
      var al = +rA.value * Math.PI / 180, fob = +rOb.value, foc = +rOc.value, G = fob / foc;
      oA.textContent = fr(+rA.value, 1) + '\u00b0';
      scope(S.ctx, S.w, S.h, { al: al, fob: fob, foc: foc, step: 6, eye: 'reduit' });
      var fE = 17, alp = Math.atan(G * Math.tan(al));   /* distance cristallin-rétine d'un œil réduit : environ 17 mm */
      oR.innerHTML = 'à l\u2019œil nu\u00a0: ' + fr(fE * Math.tan(al), 2) + ' mm\u00a0; avec la lunette\u00a0: ' + fr(fE * Math.tan(alp), 2) + ' mm (environ ' + fr(G, 1) + ' fois plus grande)';
    }
    [rA, rOb, rOc].forEach(function (r) { r.addEventListener('input', draw); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
})();
</script>
