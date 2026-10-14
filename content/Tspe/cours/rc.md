+++
title = "Condensateurs et circuit RC"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-ql-q { font-size: 1.05em; text-align: center; margin: 0.5em 0 0.7em !important; min-height: 1.6em; }
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
.nt-prog { display: flex; flex-wrap: wrap; gap: 0.4em; justify-content: center; margin: 0.3em 0 0.5em; }
.nt-prog i { width: 0.85em; height: 0.85em; border-radius: 50%; background: #E2E8F0; transition: background .25s; }
.nt-prog i.ok { background: #22C55E; } .nt-prog i.ko { background: #F43F5E; } .nt-prog i.cur { box-shadow: 0 0 0 2.5px var(--blue); }
.nt-qnum { text-align: center; font-size: 0.82em; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; color: var(--blue); margin: 0; }
.nt-qcard { background: linear-gradient(180deg, #FFFFFF, #F8FAFC); border: 1px solid var(--line); border-radius: 16px; padding: 0.9em 1em 1em; margin: 0.4em auto 0.6em; max-width: 620px; box-shadow: 0 6px 18px rgba(15,23,42,.06); }
.nt-qvis { text-align: center; margin: 0.1em 0 0.3em; }
.nt-qdata { display: inline-flex; flex-wrap: wrap; gap: 0.3em 1em; justify-content: center; align-items: center; font-family: Georgia, serif; font-size: 1.4em; color: #0F172A; }
.nt-qdata span { white-space: nowrap; }
.nt-msg.nt-fb { border-radius: 12px; padding: 0.6em 0.9em; text-align: left; }
.nt-msg.nt-fb.ok { background: #F0FDF4; border-left: 4px solid #22C55E; } .nt-msg.nt-fb.ko { background: #FFF1F2; border-left: 4px solid #F43F5E; }
.nt-lab .nt-msg { margin-top: 1em !important; }
.nt-lab [hidden] { display: none !important; }
.nt-tr-ans { display: flex; align-items: center; justify-content: center; gap: 0.5em; flex-wrap: wrap; margin: 0.6em 0; }
.nt-champ { display: inline-flex; align-items: center; gap: 0.35em; white-space: nowrap; margin: 0 0.7em; }
.nt-champ label { display: inline; margin: 0; font-weight: 600; }
.nt-champ input[type="text"] { width: 5.5em !important; min-width: 0; margin: 0; padding: 0.25em 0.5em; text-align: right; font: inherit; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-champ .nt-u { color: var(--slate); }
.nt-svgbox { margin: 0.6em 0; }
.nt-svgbox svg { display: block; width: 100%; height: auto; }
.nt-figs { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8em; margin: 1em 0; }
.nt-figs figure { margin: 0; text-align: center; }
.nt-figs img { width: 100%; border-radius: 10px; }
.nt-figs figcaption { font-size: 0.88em; color: var(--muted); }
.nt-embed { position: relative; width: 100%; max-width: 760px; margin: 1em auto; aspect-ratio: 5 / 4; }
.nt-embed iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 10px; }
.nt-schemas { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1em; align-items: center; margin: 1em 0; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## L'intensité du courant {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp">intensité</span> $i(t)$ d'un courant électrique en un point d'un circuit est le <span class="imp nt-hole">débit de charges électriques</span> en ce point, à l'instant $t$.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>En régime permanent</p>
<p class="nt-f-math">$$i = \frac{Q}{\Delta t}$$</p>
<div class="nt-f-units"><span>$Q$, la charge qui passe pendant $\Delta t$, en <b>coulombs (C)</b></span><span>$\Delta t$ en <b>s</b></span><span>$i$ en <b>A</b></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>En régime variable</p>
<p class="nt-f-math">$$i(t) = \frac{\mathrm{d}q}{\mathrm{d}t}$$</p>
<div class="nt-f-units"><span>la dérivée par rapport au temps de la charge $q(t)$</span></div>
</div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>C'est l'analogue du débit volumique d'un fluide, $D_V = \dfrac{V}{\Delta t}$&nbsp;: l'intensité compte des charges, comme le débit compte des litres. En régime permanent, l'intensité ne dépend pas du temps&nbsp;; en régime variable, il faut dériver la charge.</p>
</div>

## Le comportement capacitif {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On parle de <span class="imp">comportement capacitif</span> lorsqu'il y a <span class="imp nt-hole">accumulation de charges de signes opposés</span> sur des <span class="imp nt-hole">surfaces en regard</span>.</p>
</div>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 760px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/orage.png" alt="Un cumulonimbus d'orage : charges positives au sommet du nuage, charges négatives à sa base, et charges positives induites au sol" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>un nuage d'orage&nbsp;: un gigantesque condensateur naturel</figcaption></figure>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Comment un nuage d'orage se charge-t-il&nbsp;?</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>Les collisions.</b> Dans le nuage, entre 0&nbsp;°C et −40&nbsp;°C, de gros grains de grésil (lourds et poreux) heurtent de petits cristaux de glace, en présence d'eau surfondue (restée liquide malgré une température négative). À chaque collision, des charges sont transférées&nbsp;: le grésil se charge négativement, les cristaux positivement.</li>
<li><b>Le tri par la masse.</b> Les courants ascendants, qui peuvent atteindre 100&nbsp;km/h, emportent les petits cristaux, légers et positifs, vers le sommet du nuage (l'enclume). Le grésil, lourd et négatif, s'accumule dans la partie moyenne et basse.</li>
<li><b>Le résultat.</b> Une zone positive au sommet, une zone négative à la base&nbsp;: des charges opposées en regard. Le champ électrique atteint plusieurs dizaines de kilovolts par mètre, jusqu'au claquage de l'air&nbsp;: l'éclair.</li>
</ul>
</div>
</details>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 620px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/wimshurst.png" alt="Une machine de Wimshurst : deux disques qui tournent en sens inverse, et deux bouteilles de Leyde" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>une machine de Wimshurst et ses deux bouteilles de Leyde, les premiers condensateurs</figcaption></figure>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La catastrophe du Hindenburg</span></summary>
<div class="nt-d-body">
<div class="nt-figs" style="grid-template-columns: minmax(240px, 620px); justify-content: center;">
<figure><img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Hindenburg_disaster,_1937.jpg" alt="Le dirigeable Hindenburg en flammes, le 6 mai 1937" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>l'incendie du dirigeable Hindenburg, le 6 mai 1937</figcaption></figure>
</div>
<p>Le 6 mai 1937, près de New York, un câble déchire l'enveloppe d'un des réservoirs du dirigeable LZ 129 Hindenburg&nbsp;: du dihydrogène fuit et se mélange à l'air. Au moment de l'amarrage, les cordes larguées au sol se mouillent sous la pluie et deviennent conductrices. L'armature métallique du dirigeable est alors reliée à la terre, et des charges opposées s'accumulent sur deux surfaces en regard&nbsp;: l'armature et l'enveloppe extérieure, bien moins conductrice. La tension entre les deux provoque une étincelle, qui enflamme le mélange de dihydrogène et d'air.</p>
</div>
</details>

## Le condensateur {.nt-h2}

<div class="nt-figs" style="grid-template-columns: minmax(240px, 620px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/condensateurs.png" alt="Différents condensateurs : électrochimiques cylindriques, céramiques, à film, variables" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>des condensateurs de toutes formes et de toutes tailles</figcaption></figure>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>À quoi peuvent bien servir ces composants&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Ce sont des sortes de <b>châteaux d'eau à charges électriques</b>&nbsp;:</p>
<ul class="nt-facts">
<li>ils peuvent <b>délivrer une charge électrique en un court laps de temps</b>&nbsp;: défibrillateur, flash d'appareil photo, supercondensateurs des autobus électriques…&nbsp;;</li>
<li>ils peuvent servir d'<b>amortisseurs</b> pour les variations de tension, afin de protéger des composants, ou pour <b>filtrer</b> des signaux&nbsp;;</li>
<li>comme leurs caractéristiques dépendent de leur géométrie, ils peuvent servir de <b>capteurs</b>&nbsp;: mesure d'épaisseur, de niveau de liquide, d'humidité, détection de présence, microphones, écrans tactiles…</li>
</ul>
</div>
</details>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 560px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/appconden.png" alt="Un flash d'appareil photo, un défibrillateur et un autobus électrique à supercondensateurs, en recharge" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>flash, défibrillateur, autobus à supercondensateurs&nbsp;: libérer beaucoup de charges en peu de temps</figcaption></figure>
</div>

<div class="nt-lab" id="lab-del">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Charger, décharger&nbsp;: deux DEL révèlent le sens du courant</p>
<div class="nt-svgbox nt-del-svg" style="max-width:460px; margin-left:auto; margin-right:auto;"></div>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="p1">Position 1&nbsp;: charge</button>
<button type="button" class="nt-btn nt-btn-main" data-act="p2">Position 2&nbsp;: décharge</button>
<button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Condensateur déchargé</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Valeurs de l'exemple&nbsp;: E = 6&nbsp;V, R<sub>1</sub> = 470&nbsp;Ω, R<sub>2</sub> = 1&nbsp;kΩ, C = 2&nbsp;200&nbsp;µF. Une DEL ne laisse passer le courant que dans un sens, et seulement si la tension à ses bornes dépasse sa tension de seuil (environ 2,1&nbsp;V pour la verte, 1,8&nbsp;V pour la rouge).</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">À quoi sert le conducteur ohmique R<sub>2</sub>&nbsp;?</span></summary>
<div class="nt-d-body">
<p>R<sub>2</sub>, en dérivation avec les deux DEL, permet une charge et une décharge <b>complètes</b> du condensateur.</p>
<ul class="nt-facts">
<li>Une DEL ne conduit le courant que si la tension à ses bornes dépasse sa tension de seuil.</li>
<li><b>Sans R<sub>2</sub></b>&nbsp;: dès que la tension aux bornes de la DEL redescend sous ce seuil, le courant s'arrête. Le condensateur ne parviendrait jamais à la tension finale E (ni à 0 lors de la décharge).</li>
<li><b>Avec R<sub>2</sub></b>&nbsp;: le courant dispose d'un chemin permanent. Même quand les DEL sont éteintes, il continue de circuler à travers R<sub>2</sub>, jusqu'à ce que $u_C = E$ (charge) ou $u_C = 0$ (décharge). C'est ce que montre l'animation.</li>
</ul>
</div>
</details>


### Le modèle du condensateur {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un <span class="imp">condensateur</span> est un dipôle électrique constitué de deux <span class="imp nt-hole">surfaces conductrices en regard</span>, les armatures, séparées par un <span class="imp nt-hole">matériau isolant</span>, le diélectrique.</p>
</div>

<div class="nt-svgbox" style="max-width:320px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 300 90' role='img' aria-label="Symbole électrique du condensateur : deux traits parallèles, les armatures, perpendiculaires au fil"><polyline points='30,60 270,60' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><rect x='145' y='44' width='10' height='32' fill='#fff'/><line x1='145' y1='45' x2='145' y2='75' stroke='#1E293B' stroke-width='3'/><line x1='155' y1='45' x2='155' y2='75' stroke='#1E293B' stroke-width='3'/><path d='M136,20 l9,22 M164,20 l-9,22' stroke='#94A3B8' stroke-width='1.2'/><text x='150' y='14' font-size='12' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif' font-weight='600'>armatures</text></svg></div>
<p class="nt-cap">Le symbole électrique du condensateur.</p>

<div class="nt-schemas">
<div>
<div class="nt-b nt-prop" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le condensateur a un comportement capacitif&nbsp;: lorsqu'il est soumis à une tension non nulle, les charges $q_A$ et $q_B$ portées par ses deux armatures A et B sont <span class="imp nt-hole">opposées</span>&nbsp;: $q_A = -q_B$.</p>
</div>
</div>
<div class="nt-svgbox" style="max-width:320px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 300 310' role='img' aria-label="Les deux armatures A et B d’un condensateur portent des charges opposées : qB = −qA ; la tension uAB = uC est représentée par une flèche pointant vers A"><polyline points='30,150 128,150' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='172,150 270,150' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><rect x='128' y='46' width='10' height='208' rx='2' fill='#FCA5A5' stroke='#E11D48' stroke-width='1.5'/><rect x='162' y='46' width='10' height='208' rx='2' fill='#BFDBFE' stroke='#2563EB' stroke-width='1.5'/><text x='118' y='63' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='63' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='83' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='83' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='103' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='103' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='123' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='123' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='143' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='143' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='163' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='163' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='183' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='183' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='203' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='203' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='223' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='223' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><text x='118' y='243' font-size='15' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='800'>+</text><text x='182' y='243' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='800'>−</text><circle cx='50' cy='150' r='3.6' fill='#1E293B'/><circle cx='250' cy='150' r='3.6' fill='#1E293B'/><text x='50' y='138' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='250' y='138' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>B</text><line x1='240' y1='26' x2='68' y2='26' stroke='#16A34A' stroke-width='2.2' stroke-linecap='round'/><polygon points='60,26 71,21 71,31' fill='#16A34A'/><text x='150' y='18' font-size='14' text-anchor='middle' fill='#16A34A' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>u</tspan><tspan font-size='9.5' dy='3'>AB</tspan><tspan dy='-3'> = </tspan><tspan font-style='italic'>u</tspan><tspan font-size='9.5' dy='3'>C</tspan></text><text x='110' y='282' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>q</tspan><tspan font-size='10' dy='4'>A</tspan></text><text x='190' y='282' font-size='14' text-anchor='middle' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>q</tspan><tspan font-size='9.5' dy='3'>B</tspan><tspan dy='-3'> = −</tspan><tspan font-style='italic'>q</tspan><tspan font-size='9.5' dy='3'>A</tspan></text><text x='150' y='302' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>isolant (diélectrique)</text></svg></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La charge $q$ portée par l'armature A est <span class="imp nt-hole">proportionnelle</span> à la tension $u_C = u_{AB}$ entre ses bornes. Le coefficient de proportionnalité est la <span class="imp nt-hole">capacité</span> $C$ du condensateur.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Capacité d'un condensateur</p>
<p class="nt-f-math">$$q = C\times u_C$$</p>
<div class="nt-f-units"><span>$q$ en <b>coulombs (C)</b></span><span>$u_C$ en <b>V</b></span><span>$C$ en <b>farads (F)</b>&nbsp;: 1&nbsp;F = 1&nbsp;C/V</span></div>
</div>

<div class="nt-schemas">
<div class="nt-svgbox" style="max-width:320px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 300 120' role='img' aria-label="Convention : la flèche de la tension uC pointe vers l’armature qui porte la charge q"><polyline points='30,90 270,90' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><rect x='145' y='74' width='10' height='32' fill='#fff'/><line x1='145' y1='75' x2='145' y2='105' stroke='#1E293B' stroke-width='3'/><line x1='155' y1='75' x2='155' y2='105' stroke='#1E293B' stroke-width='3'/><text x='128' y='70' font-size='14' text-anchor='end' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>q</tspan></text><text x='172' y='70' font-size='14' text-anchor='start' fill='#2563EB' font-family='Georgia, serif' font-weight='700'>−<tspan font-style='italic'>q</tspan></text><line x1='220' y1='30' x2='88' y2='30' stroke='#16A34A' stroke-width='2.2' stroke-linecap='round'/><polygon points='80,30 91,25 91,35' fill='#16A34A'/><text x='150' y='22' font-size='14' text-anchor='middle' fill='#16A34A' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>u</tspan><tspan font-size='10' dy='4'>C</tspan></text></svg></div>
<div class="nt-b nt-warn" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Convention</p>
<p>La flèche de la tension $u_C$ <b>pointe vers l'armature qui porte la charge</b> $q$. Ainsi, $u_C$ et $q$ ont le même signe.</p>
</div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Ordres de grandeur</p>
<p>Hormis les supercondensateurs, qui peuvent atteindre plusieurs centaines, voire milliers de farads, les capacités s'étalent typiquement de la dizaine de picofarads ($\pu{1 pF} = \pu{E-12 F}$) à la dizaine de millifarads.</p>
</div>


<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La tension d'une machine de Wimshurst</span></summary>
<div class="nt-d-body">
<p>Avec ses bouteilles de Leyde, une machine de Wimshurst a une capacité de 50 à 100&nbsp;pF. Quand l'étincelle jaillit entre des boules distantes de 1&nbsp;cm, la charge accumulée vaut environ 2&nbsp;µC. On en déduit la tension&nbsp;:</p>
<p class="nt-center">$u = \dfrac{q}{C} = \dfrac{\pu{2E-6 C}}{\pu{50E-12 F}} = \pu{4E4 V}$, soit 40&nbsp;kV&nbsp;!</p>
</div>
</details>



## Le circuit RC série {.nt-h2}

<div class="nt-schemas">
<div class="nt-svgbox" style="max-width:300px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 260 354' role='img' aria-label="Montage pour charger puis décharger un condensateur : en position 1, la source E charge le condensateur C à travers R ; en position 2, le condensateur se décharge à travers R"><polyline points='50,50 124,50 124,62' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='176,62 176,50 210,50 210,300 50,300 50,50' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='150,84 150,300' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='50' cy='175' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><line x1='50' y1='158' x2='50' y2='192' stroke='#1E293B' stroke-width='2'/><text x='64' y='155' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='64' y='205' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><circle cx='124' cy='62' r='3.6' fill='#1E293B'/><circle cx='176' cy='62' r='3.6' fill='#1E293B'/><circle cx='150' cy='84' r='3.6' fill='#1E293B'/><line x1='150' y1='84' x2='144' y2='60' stroke='#1E293B' stroke-width='2.4' stroke-linecap='round'/><text x='113' y='67' font-size='12' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif' font-weight='700'>1</text><text x='187' y='67' font-size='12' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif' font-weight='700'>2</text><rect x='142' y='130' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><rect x='134' y='230' width='32' height='10' fill='#fff'/><line x1='135' y1='230' x2='165' y2='230' stroke='#1E293B' stroke-width='3'/><line x1='135' y1='240' x2='165' y2='240' stroke='#1E293B' stroke-width='3'/><circle cx='150' cy='300' r='3.6' fill='#1E293B'/><line x1='22' y1='220' x2='22' y2='138' stroke='#16A34A' stroke-width='2.2' stroke-linecap='round'/><polygon points='22,130 27,141 17,141' fill='#16A34A'/><text x='14' y='175' font-size='14' text-anchor='end' fill='#16A34A' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>E</tspan></text><line x1='182' y1='255' x2='182' y2='223' stroke='#DB2777' stroke-width='2.2' stroke-linecap='round'/><polygon points='182,215 187,226 177,226' fill='#DB2777'/><text x='190' y='239' font-size='14' text-anchor='start' fill='#DB2777' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>u</tspan><tspan font-size='10' dy='4'>C</tspan></text><text x='130' y='155' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>R</text><text x='130' y='240' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>C</text><text x='150' y='40' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>K</text><text x='130' y='326' font-size='11.5' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif' font-weight='600'>position 1 : charge</text><text x='130' y='344' font-size='11.5' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif' font-weight='600'>position 2 : décharge</text></svg></div>
<div>
<p>Un conducteur ohmique de résistance $R$ et un condensateur de capacité $C$ sont branchés en série. Un interrupteur à deux positions permet&nbsp;:</p>
<ul class="nt-facts">
<li>en position 1, de <b>charger</b> le condensateur sous la tension $E$ de la source&nbsp;;</li>
<li>en position 2, de le <b>décharger</b> à travers le conducteur ohmique.</li>
</ul>
</div>
</div>

### La charge {.nt-h3}

<div class="nt-schemas">
<div class="nt-svgbox" style="max-width:380px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 380 320' role='img' aria-label="Circuit de charge : la source E, l’interrupteur K fermé, le conducteur ohmique R et le condensateur C en série ; le courant i circule dans le sens horaire ; tensions uR et uC en convention récepteur"><polyline points='60,50 300,50 300,300 60,300 60,50' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='60' cy='175' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><line x1='60' y1='158' x2='60' y2='192' stroke='#1E293B' stroke-width='2'/><text x='74' y='155' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='74' y='205' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><rect x='162' y='36' width='36' height='18' fill='#fff'/><circle cx='165' cy='50' r='3.6' fill='#1E293B'/><circle cx='195' cy='50' r='3.6' fill='#1E293B'/><line x1='165' y1='50' x2='193' y2='50' stroke='#1E293B' stroke-width='2.2' stroke-linecap='round'/><rect x='292' y='110' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><rect x='284' y='225' width='32' height='10' fill='#fff'/><line x1='285' y1='225' x2='315' y2='225' stroke='#1E293B' stroke-width='3'/><line x1='285' y1='235' x2='315' y2='235' stroke='#1E293B' stroke-width='3'/><g transform='translate(60,110) rotate(-90)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><text x='46' y='114' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>i</tspan></text><g transform='translate(240,50) rotate(0)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><g transform='translate(180,300) rotate(180)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><line x1='28' y1='220' x2='28' y2='138' stroke='#16A34A' stroke-width='2.2' stroke-linecap='round'/><polygon points='28,130 33,141 23,141' fill='#16A34A'/><text x='20' y='175' font-size='14' text-anchor='end' fill='#16A34A' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>E</tspan></text><line x1='334' y1='155' x2='334' y2='113' stroke='#CA8A04' stroke-width='2.2' stroke-linecap='round'/><polygon points='334,105 339,116 329,116' fill='#CA8A04'/><text x='342' y='134' font-size='14' text-anchor='start' fill='#CA8A04' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>u</tspan><tspan font-size='10' dy='4'>R</tspan></text><line x1='334' y1='255' x2='334' y2='213' stroke='#DB2777' stroke-width='2.2' stroke-linecap='round'/><polygon points='334,205 339,216 329,216' fill='#DB2777'/><text x='342' y='234' font-size='14' text-anchor='start' fill='#DB2777' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>u</tspan><tspan font-size='10' dy='4'>C</tspan></text><text x='280' y='135' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>R</text><text x='280' y='235' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>C</text><text x='180' y='34' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>K</text></svg></div>
<p class="nt-lead">On charge un condensateur de capacité $C$, initialement déchargé, à travers un conducteur ohmique de résistance $R$, sous une tension $E$. À l'instant initial $t = 0$, on ferme l'interrupteur K.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Démonstration&nbsp;: l'équation différentielle</p>
<ol class="nt-steps">
<li><p>Loi des mailles&nbsp;: ${\color{#16A34A}{E}} = {\color{#CA8A04}{u_R(t)}} + \color{#DB2777}{u_C(t)}$.</p></li>
<li><p>Loi d'Ohm, aux bornes du conducteur ohmique&nbsp;: ${\color{#CA8A04}{u_R(t)}} = R\times\color{#E11D48}{i(t)}$.</p></li>
<li><p>Définition de l'intensité&nbsp;: ${\color{#E11D48}{i(t)}} = \color{#E11D48}{\dfrac{\mathrm{d}q}{\mathrm{d}t}}$. Et comme $q(t) = C\times u_C(t)$, avec $C$ constante&nbsp;: ${\color{#E11D48}{\dfrac{\mathrm{d}q}{\mathrm{d}t}}} = \color{#E11D48}{C\,\dfrac{\mathrm{d}u_C}{\mathrm{d}t}}$.</p></li>
<li><p>On réinjecte dans la loi des mailles&nbsp;: $R\,{\color{#E11D48}{C\,\dfrac{\mathrm{d}u_C}{\mathrm{d}t}}} + u_C = E$.</p></li>
<li><p>Après division par $RC$&nbsp;:</p>
<div style="position:relative;margin:-1em auto 1em auto;width:fit-content;border:solid 2px #FF968D;padding:0 20px 0 20px;border-radius:5px">
$$\dfrac{\mathrm{d}u_C}{\mathrm{d}t} + \dfrac{1}{RC}\,u_C(t) = \dfrac{E}{RC}$$
</div>
<p>C'est une <b>équation différentielle du premier ordre</b>, à coefficients constants, avec un second membre constant.</p></li>
</ol>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Démonstration&nbsp;: la solution</p>
<ol class="nt-steps">
<li><p>La solution générale s'écrit $u_C(t) = A\,\mathrm{e}^{-t/\tau} + B$, d'où&nbsp;:</p> 
$$\dfrac{\mathrm{d}u_C}{\mathrm{d}t} = -\dfrac{A}{\tau}\,\mathrm{e}^{-t/\tau}$$</li>
<li style="margin-top:-1.5em;"><p>On l'injecte dans l'équation différentielle&nbsp;: $-\dfrac{A}{\tau}\,\mathrm{e}^{-t/\tau} + \dfrac{1}{RC}\left(A\,\mathrm{e}^{-t/\tau} + B\right) = \dfrac{E}{RC}$, soit</p>
$${\color{#E11D48}{\mathrm{e}^{-t/\tau}}}\left({\color{#2563EB}{-\dfrac{A}{\tau} + \dfrac{A}{RC}}}\right) = \dfrac{1}{RC}\left({\color{#16A34A}{E - B}}\right)$$</li>
<li style="margin-top:-1.5em;"><p>Le membre de gauche dépend du temps, celui de droite est constant&nbsp;: l'égalité ne peut être vraie à tout instant $t \geq 0$ que si les deux membres sont nuls. D'où $\color{#2563EB}{\tau = RC}$ et $\color{#16A34A}{B = E}$&nbsp;:</p> 
$$u_C(t) = A\,\mathrm{e}^{-t/RC} + E$$</p></li>
<li style="margin-top:-1.5em;"><p>Condition initiale&nbsp;: le condensateur est initialement déchargé. On a donc&nbsp;:<br>
 $$
 \begin{array}{lrl}
\phantom{\Leftrightarrow}& u_C(0) &=& 0\\
\Leftrightarrow & A\,\mathrm{e}^0 + E &=& 0\\
\Leftrightarrow&  A+E &=& 0\\
\Leftrightarrow& A &=& -E
 \end{array}
 $$
</li>
</ol>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Charge d'un condensateur</p>
<p class="nt-f-math">$$u_C(t) = E\left(1 - \mathrm{e}^{-t/\tau}\right) \quad\text{avec}\quad \tau = RC$$</p>
<div class="nt-f-units"><span>$\tau$, la constante de temps, en <b>s</b></span><span>$R$ en <b>Ω</b></span><span>$C$ en <b>F</b></span></div>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Une autre méthode&nbsp;: passer par le régime permanent</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>On repart de $u_C(t) = A\,\mathrm{e}^{-t/\tau} + B$, et on se place en $t \to \infty$&nbsp;: c'est le <b>régime permanent</b>.</p></li>
<li><p>L'intensité y est nulle&nbsp;: le condensateur, entièrement chargé, se comporte comme un interrupteur ouvert. Alors $u_R = R\,i = 0$, et la loi des mailles donne $u_C(t\to\infty) = E$.</p></li>
<li><p>Or $\displaystyle\lim_{t\to\infty}\mathrm{e}^{-t/\tau} = 0$, donc $\displaystyle\lim_{t\to\infty} u_C(t) = B$. D'où $B = E$.</p></li>
<li><p>La condition initiale $u_C(0) = 0$ donne $A = -E$.</p></li>
<li><p>Enfin, on injecte $u_C(t) = -E\,\mathrm{e}^{-t/\tau} + E$ dans l'équation différentielle&nbsp;: $\mathrm{e}^{-t/\tau}\left(\dfrac{1}{\tau} - \dfrac{1}{RC}\right) = 0$. Un produit n'est nul que si l'un de ses facteurs est nul, et $\mathrm{e}^{-t/\tau} > 0$&nbsp;: donc $\tau = RC$.</p></li>
</ol>
</div>
</details>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-graduation-cap"></i>Au bac</p>
<p>Le plus souvent, la démarche est guidée&nbsp;:</p>
<ol class="nt-steps">
<li><p>on demande d'<b>établir l'équation différentielle</b> vérifiée par $u_C$, souvent en proposant la forme $\dfrac{\mathrm{d}u_C}{\mathrm{d}t} + \dfrac{u_C}{\tau} = \dfrac{E}{\tau}$, et d'exprimer $\tau$ en fonction de $R$ et de $C$&nbsp;;</p></li>
<li><p>on demande ensuite de <b>vérifier</b> que $u_C(t) = E\left(1 - \mathrm{e}^{-t/\tau}\right)$ est solution&nbsp;: il suffit de l'injecter dans l'équation, et de vérifier que ses deux membres sont égaux.</p></li>
</ol>
<p>Exemple de cet enchaînement&nbsp;: <a href="https://coursphychi.github.io/act-defibrillateur.pdf" target="_blank" rel="noopener">«&nbsp;Défibrillateur cardiaque&nbsp;»</a>. Mais des démonstrations complètes sont parfois demandées&nbsp;: <a href="https://coursphychi.github.io/act-vigneron.pdf" target="_blank" rel="noopener">«&nbsp;La physique au service du vigneron&nbsp;»</a>.</p>
</div>

### La décharge {.nt-h3}

<div class="nt-schemas">
<div class="nt-svgbox" style="max-width:340px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 340 320' role='img' aria-label="Circuit de décharge : le condensateur C, initialement chargé, se décharge à travers le conducteur ohmique R lorsqu’on ferme l’interrupteur K"><polyline points='100,50 280,50 280,158' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='280,192 280,300 100,300 100,50' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><rect x='92' y='100' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><rect x='84' y='225' width='32' height='10' fill='#fff'/><line x1='85' y1='225' x2='115' y2='225' stroke='#1E293B' stroke-width='3'/><line x1='85' y1='235' x2='115' y2='235' stroke='#1E293B' stroke-width='3'/><circle cx='280' cy='160' r='3.6' fill='#1E293B'/><circle cx='280' cy='190' r='3.6' fill='#1E293B'/><line x1='280' y1='190' x2='280' y2='162' stroke='#1E293B' stroke-width='2.2'/><g transform='translate(100,180) rotate(90)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><text x='86' y='184' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>i</tspan></text><line x1='132' y1='145' x2='132' y2='103' stroke='#CA8A04' stroke-width='2.2' stroke-linecap='round'/><polygon points='132,95 137,106 127,106' fill='#CA8A04'/><text x='140' y='124' font-size='14' text-anchor='start' fill='#CA8A04' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>u</tspan><tspan font-size='10' dy='4'>R</tspan></text><line x1='132' y1='255' x2='132' y2='213' stroke='#DB2777' stroke-width='2.2' stroke-linecap='round'/><polygon points='132,205 137,216 127,216' fill='#DB2777'/><text x='140' y='234' font-size='14' text-anchor='start' fill='#DB2777' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>u</tspan><tspan font-size='10' dy='4'>C</tspan></text><text x='80' y='125' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>R</text><text x='80' y='235' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>C</text><text x='300' y='179' font-size='13' text-anchor='start' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>K</text></svg></div>
<p class="nt-lead">On décharge un condensateur de capacité $C$, initialement chargé sous la tension $E$, à travers un conducteur ohmique de résistance $R$. À l'instant $t = 0$, on ferme l'interrupteur.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Démonstration</p>
<p class="nt-center">$\begin{cases} \text{loi des mailles :} & u_C(t) + u_R(t) = \color{#CA8A04}{0}\\ \text{loi d'Ohm :} & u_R(t) = R\times i(t)\\ \text{intensité :} & i(t) = \dfrac{\mathrm{d}q}{\mathrm{d}t}\\ \text{capacité :} & q(t) = C\times u_C(t) \end{cases} \quad\Longrightarrow\quad \dfrac{\mathrm{d}u_C}{\mathrm{d}t} + \dfrac{1}{RC}\,u_C = \color{#CA8A04}{0}$</p>
<p>On obtient à nouveau une équation différentielle du premier ordre à coefficients constants, mais <b>homogène</b> (sans second membre). Sa solution est de la forme $u_C(t) = A\,\mathrm{e}^{-t/\tau}$. En l'injectant dans l'équation, on obtient $\tau = RC$&nbsp;; et la condition initiale $u_C(0) = E$ donne $A = E$.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Décharge d'un condensateur</p>
<p class="nt-f-math">$$u_C(t) = E\,\mathrm{e}^{-t/\tau} \quad\text{avec}\quad \tau = RC$$</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention au sens de i</p>
<p>Pour pouvoir écrire $i = \dfrac{\mathrm{d}q}{\mathrm{d}t}$, la flèche de $i$ doit être orientée <b>vers l'armature qui porte la charge $q$</b>. Et pour écrire $u_R = R\times i$, la flèche de $u_R$ doit être opposée à celle de $i$ (convention récepteur). Avec ces orientations, $i$ est <b>négative</b> pendant la décharge&nbsp;: $q$ diminue, et le courant réel circule dans le sens opposé à la flèche.</p>
</div>

## Simulation {.nt-h2}

<div class="nt-lab" id="lab-rc">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Charge et décharge d'un condensateur</p>
<canvas style="height:330px;" aria-label="Le circuit RC avec son interrupteur, les charges sur les armatures du condensateur et le courant ; à droite, les courbes de la tension uC et de l'intensité i en fonction du temps"></canvas>
<div class="nt-btns">
<button type="button" class="nt-btn" data-act="charge">Position 1&nbsp;: charge</button>
<button type="button" class="nt-btn" data-act="decharge">Position 2&nbsp;: décharge</button>
<button type="button" class="nt-btn" data-act="tau"><i class="fa-solid fa-ruler"></i>&nbsp; Afficher τ</button>
<button type="button" class="nt-btn" data-act="pause"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">Tension E&nbsp;: <b class="out-E"></b><input type="range" data-p="E" min="2" max="12" step="0.5" value="10"></label>
<label class="nt-ctrl">Résistance R&nbsp;: <b class="out-R"></b><input type="range" data-p="R" min="1" max="100" step="1" value="10"></label>
<label class="nt-ctrl">Capacité C&nbsp;: <b class="out-C"></b><input type="range" data-p="C" min="10" max="1000" step="10" value="100"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$\tau = RC$ = <b class="out-tau"></b></span><span>$u_C$ = <b class="out-u"></b></span><span>$i$ = <b class="out-i"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">L'animation se déroule au rythme d'une constante de temps par seconde, quelles que soient les valeurs de R et de C. Les signes + et − sur les armatures sont proportionnels à la charge $q = C\,u_C$. L'intensité est comptée positivement vers l'armature du haut&nbsp;: elle est négative pendant la décharge.</p>
</div>


## Le temps caractéristique {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>$\tau = RC$ a bien la dimension d'un temps&nbsp;: dans l'équation différentielle $\dfrac{\mathrm{d}u_C}{\mathrm{d}t} + \dfrac{u_C}{\tau} = \dfrac{E}{\tau}$, chaque terme est une tension divisée par un temps. Il caractérise la durée du <span class="imp nt-hole">régime transitoire</span>, la partie de l'évolution où les variations sont grandes.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Déterminer τ graphiquement</p>
<ul class="nt-facts">
<li><b>Par la tangente à l'origine</b>&nbsp;: $\tau$ est l'abscisse du point d'intersection de la tangente à l'origine et de l'asymptote horizontale ($u_C = E$ pour la charge, $u_C = 0$ pour la décharge).</li>
<li><b>Par la valeur à t = τ</b>&nbsp;: $\tau$ est l'instant où $u_C$ atteint <span class="imp nt-hole">63&nbsp;%</span> de $E$ (charge), ou descend à <span class="imp nt-hole">37&nbsp;%</span> de $E$ (décharge).</li>
</ul>
<p>Au bout de $5\tau$, on approche le régime permanent ($E$ pour la charge, 0 pour la décharge) à mieux de 99&nbsp;%&nbsp;: c'est un critère de séparation entre <span class="imp nt-hole">régime transitoire</span> et <span class="imp nt-hole">régime permanent</span>.</p>
</div>

<div class="nt-lab" id="lab-tau">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Lire la constante de temps sur une courbe</p>
<p class="nt-ql-q nt-tr-q"></p>
<canvas style="height:300px; background:#fff; border-radius:10px; touch-action:none; cursor:crosshair;" aria-label="Enregistrement de la tension uC lors d'une charge ou d'une décharge, sur un graphique quadrillé ; faites glisser pour tracer la tangente à l'origine"></canvas>
<div class="nt-tr-ans"><span class="nt-champ"><label for="tau-rep">τ =</label><input id="tau-rep" type="text" inputmode="decimal"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Une autre courbe</button></div>
</div>

<p class="nt-center"><a href="https://www.geogebra.org/m/w9aqhfvg" target="_blank" rel="noopener"><i class="fa-solid fa-chart-line"></i>&nbsp; Applet GeoGebra&nbsp;: la constante de temps</a></p>

<div class="nt-lab nt-trainer" id="lab-calc">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Capacité, charge, constante de temps</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<div class="nt-qvis" aria-live="polite"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-zone"><div class="nt-tr-ans"><span class="nt-champ"><label for="rc-rep">Réponse&nbsp;:</label><input id="rc-rep" type="text" inputmode="decimal"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>


<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function nb(x, sig) { if (x === 0) { return '0'; } var a = Math.abs(x), d = Math.max(0, (sig || 3) - 1 - Math.floor(Math.log10(a))); var s = x.toFixed(Math.min(d, 6)), p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '\u202f'); return p.join(',').replace('-', '\u2212'); }
  function canvasCtx(cv) { var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight; cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); return { ctx: ctx, w: w, h: h }; }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function watch(cv, cb) { if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }).observe(cv); } else { cb(true); } }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function num(s) { return parseFloat(String(s).replace(',', '.').replace(/\s/g, '')); }
  function bilanTxt(r) { return r === 1 ? 'Parfait&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;!' : (r >= 0.5 ? 'C\u2019est un bon début&nbsp;: relisez les cas manqués.' : 'Relisez le cours, puis recommencez.')); }
  /* texte : le style de tracé est rétabli ensuite */
  function txt(c, s, x, y, color, font, align) { c.save(); c.font = font || '12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round'; c.lineWidth = 4; c.strokeStyle = 'rgba(255,255,255,.92)'; c.strokeText(s, x, y); c.fillStyle = color; c.fillText(s, x, y); c.restore(); }
  function rr(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
  var CE = '#16A34A', CR = '#CA8A04', CC = '#DB2777', CIc = '#E11D48';
  /* ===== CI : petit moteur de schémas électriques (chaînes SVG), utilisé à la construction et dans la page ===== */
  var CI = (function () {
    var INK = '#1E293B', F = "font-family='system-ui, sans-serif'";
    function n(v) { return Math.round(v * 10) / 10; }
    function wire(pts, col) { return "<polyline points='" + pts.map(function (p) { return n(p[0]) + ',' + n(p[1]); }).join(' ') + "' fill='none' stroke='" + (col || INK) + "' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/>"; }
    function text(x, y, s, col, size, anchor, weight, italic) {
      return "<text x='" + n(x) + "' y='" + n(y) + "' font-size='" + (size || 13) + "' text-anchor='" + (anchor || 'middle') + "' fill='" + (col || INK) + "' " + F + (weight ? " font-weight='" + weight + "'" : '') + (italic ? " font-style='italic'" : '') + ">" + s + "</text>";
    }
    /* étiquette de grandeur : lettre en italique, indice droit */
    function qty(x, y, L, sub, col, anchor, size) {
      size = size || 14;
      return "<text x='" + n(x) + "' y='" + n(y) + "' font-size='" + size + "' text-anchor='" + (anchor || 'middle') + "' fill='" + col + "' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>" + L + "</tspan>" + (sub ? "<tspan font-size='" + Math.round(size * 0.68) + "' dy='" + Math.round(size * 0.28) + "'>" + sub + "</tspan>" : '') + "</text>";
    }
    function node(x, y) { return "<circle cx='" + n(x) + "' cy='" + n(y) + "' r='3.6' fill='" + INK + "'/>"; }
    function res(x, y, o, col) {   /* conducteur ohmique ; o : 'h' ou 'v' */
      var w = o === 'v' ? 16 : 40, h = o === 'v' ? 40 : 16;
      return "<rect x='" + n(x - w / 2) + "' y='" + n(y - h / 2) + "' width='" + w + "' height='" + h + "' fill='" + (col || '#fff') + "' stroke='" + INK + "' stroke-width='2'/>";
    }
    function therm(x, y, o) {
      var s = res(x, y, o), pts = o === 'v' ? [[x - 13, y + 30], [x - 13, y + 19], [x + 13, y - 19], [x + 13, y - 30]] : [[x - 30, y + 13], [x - 19, y + 13], [x + 19, y - 13], [x + 30, y - 13]];
      s += "<polyline points='" + pts.map(function (p) { return n(p[0]) + ',' + n(p[1]); }).join(' ') + "' fill='none' stroke='" + INK + "' stroke-width='1.6' stroke-linejoin='round'/>";
      return s;
    }
    function rheo(x, y, o) {   /* rhéostat : conducteur ohmique traversé d'une flèche oblique */
      var s = res(x, y, o), a = o === 'v' ? [x - 18, y + 20, x + 16, y - 20] : [x - 26, y + 14, x + 26, y - 14];
      var dx = a[2] - a[0], dy = a[3] - a[1], L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
      s += "<line x1='" + n(a[0]) + "' y1='" + n(a[1]) + "' x2='" + n(a[2] - ux * 6) + "' y2='" + n(a[3] - uy * 6) + "' stroke='" + INK + "' stroke-width='1.6'/>";
      s += "<polygon points='" + n(a[2]) + ',' + n(a[3]) + ' ' + n(a[2] - ux * 9 - uy * 4) + ',' + n(a[3] - uy * 9 + ux * 4) + ' ' + n(a[2] - ux * 9 + uy * 4) + ',' + n(a[3] - uy * 9 - ux * 4) + "' fill='" + INK + "'/>";
      return s;
    }
    function lamp(x, y, glow) {
      var s = '';
      if (glow) { s += "<circle cx='" + n(x) + "' cy='" + n(y) + "' r='" + n(14 + 10 * glow) + "' fill='rgba(250,204,21," + (0.35 * glow) + ")'/>"; }
      s += "<circle cx='" + n(x) + "' cy='" + n(y) + "' r='14' fill='" + (glow ? 'rgba(254,240,138,' + (0.4 + 0.6 * glow) + ')' : '#fff') + "' stroke='" + INK + "' stroke-width='2'/>";
      var d = 9.9; s += "<path d='M" + n(x - d) + ',' + n(y - d) + ' L' + n(x + d) + ',' + n(y + d) + ' M' + n(x + d) + ',' + n(y - d) + ' L' + n(x - d) + ',' + n(y + d) + "' stroke='" + INK + "' stroke-width='2'/>";
      return s;
    }
    function gen(x, y, o, plus, lab) {   /* générateur : o 'v' (+ en haut si plus='t') ou 'h' (+ à droite si plus='r') */
      var s = "<circle cx='" + n(x) + "' cy='" + n(y) + "' r='17' fill='#fff' stroke='" + INK + "' stroke-width='2'/>" + text(x, y + 5, lab || 'G', INK, 14, 'middle', 700);
      var pp = { t: [x - 14, y - 20], b: [x - 14, y + 30], r: [x + 22, y - 10], l: [x - 22, y - 10] }, mm = { t: [x - 14, y + 30], b: [x - 14, y - 20], r: [x - 22, y - 10], l: [x + 22, y - 10] };
      s += text(pp[plus][0], pp[plus][1], '+', '#DC2626', 15, 'middle', 700) + text(mm[plus][0], mm[plus][1], '\u2212', '#2563EB', 15, 'middle', 700);
      return s;
    }
    function meter(x, y, L, side, o) {   /* appareil de mesure ; side : côté de la borne A ou V ('l','r','t','b') ; la borne COM est en face */
      var s = "<circle cx='" + n(x) + "' cy='" + n(y) + "' r='13' fill='#fff' stroke='" + INK + "' stroke-width='2'/>" + text(x, y + 5, L, INK, 13, 'middle', 700);
      var off = { l: [-20, -6, 'end'], r: [20, -6, 'start'], t: [10, -16, 'start'], b: [10, 24, 'start'] }, opp = { l: 'r', r: 'l', t: 'b', b: 't' };
      var a = off[side], c = off[opp[side]];
      s += text(x + a[0], y + a[1], L === 'A' ? 'A' : 'V', '#DC2626', 10.5, a[2], 700) + text(x + c[0], y + c[1], 'COM', '#2563EB', 10.5, c[2], 700);
      return s;
    }
    function led(x, y, o, dir) {   /* DEL ; dir : sens passant ('d','u','r','l') */
      var r = { d: 0, u: 180, l: 90, r: -90 }[dir];
      var s = "<g transform='translate(" + n(x) + ',' + n(y) + ") rotate(" + r + ")'><polygon points='-11,-9 11,-9 0,9' fill='#fff' stroke='" + INK + "' stroke-width='2'/><line x1='-11' y1='9' x2='11' y2='9' stroke='" + INK + "' stroke-width='2.4'/>";
      s += "<path d='M14,-6 l8,-6 M18,-2 l8,-6' stroke='" + INK + "' stroke-width='1.4'/><polygon points='22,-12 18,-11 21,-8' fill='" + INK + "'/><polygon points='26,-8 22,-7 25,-4' fill='" + INK + "'/></g>";
      return s;
    }
    function sw(x, y, o, open) {   /* interrupteur horizontal */
      return "<rect x='" + n(x - 16) + "' y='" + n(y - 8) + "' width='32' height='16' fill='#fff'/>" + node(x - 14, y) + node(x + 14, y) +
        "<line x1='" + n(x - 14) + "' y1='" + n(y) + "' x2='" + n(x + 12) + "' y2='" + n(open ? y - 12 : y) + "' stroke='" + INK + "' stroke-width='2'/>";
    }
    function iarr(x, y, dir, L, sub, col, lx, ly) {   /* flèche de courant posée sur un fil, avec son nom */
      var r = { r: 0, d: 90, l: 180, u: -90 }[dir];
      var s = "<g transform='translate(" + n(x) + ',' + n(y) + ") rotate(" + r + ")'><polygon points='7,0 -6,-6 -6,6' fill='" + col + "'/></g>";
      if (L) { s += qty(x + (lx || 0), y + (ly || -10), L, sub, col); }
      return s;
    }
    function uarr(x1, y1, x2, y2, L, sub, col, lx, ly, anchor) {   /* flèche de tension, à côté du dipôle */
      var dx = x2 - x1, dy = y2 - y1, Ln = Math.hypot(dx, dy), ux = dx / Ln, uy = dy / Ln;
      var s = "<line x1='" + n(x1) + "' y1='" + n(y1) + "' x2='" + n(x2 - ux * 8) + "' y2='" + n(y2 - uy * 8) + "' stroke='" + col + "' stroke-width='2.2' stroke-linecap='round'/>";
      s += "<polygon points='" + n(x2) + ',' + n(y2) + ' ' + n(x2 - ux * 11 - uy * 5) + ',' + n(y2 - uy * 11 + ux * 5) + ' ' + n(x2 - ux * 11 + uy * 5) + ',' + n(y2 - uy * 11 - ux * 5) + "' fill='" + col + "'/>";
      if (L) { s += qty((x1 + x2) / 2 + (lx || 0), (y1 + y2) / 2 + (ly || 0), L, sub, col, anchor || 'middle'); }
      return s;
    }
    function cap(x, y, o, col) {   /* condensateur : deux armatures parallèles ; o : 'v' (branche verticale) ou 'h' */
      var c = col || INK;
      if (o === 'v') { return "<rect x='" + n(x - 16) + "' y='" + n(y - 5) + "' width='32' height='10' fill='#fff'/>" + "<line x1='" + n(x - 15) + "' y1='" + n(y - 5) + "' x2='" + n(x + 15) + "' y2='" + n(y - 5) + "' stroke='" + c + "' stroke-width='3'/><line x1='" + n(x - 15) + "' y1='" + n(y + 5) + "' x2='" + n(x + 15) + "' y2='" + n(y + 5) + "' stroke='" + c + "' stroke-width='3'/>"; }
      return "<rect x='" + n(x - 5) + "' y='" + n(y - 16) + "' width='10' height='32' fill='#fff'/>" + "<line x1='" + n(x - 5) + "' y1='" + n(y - 15) + "' x2='" + n(x - 5) + "' y2='" + n(y + 15) + "' stroke='" + c + "' stroke-width='3'/><line x1='" + n(x + 5) + "' y1='" + n(y - 15) + "' x2='" + n(x + 5) + "' y2='" + n(y + 15) + "' stroke='" + c + "' stroke-width='3'/>";
    }
    function src(x, y, plus) {   /* source idéale de tension (branche verticale) : cercle traversé par le fil */
      var s = "<circle cx='" + n(x) + "' cy='" + n(y) + "' r='17' fill='#fff' stroke='" + INK + "' stroke-width='2'/><line x1='" + n(x) + "' y1='" + n(y - 17) + "' x2='" + n(x) + "' y2='" + n(y + 17) + "' stroke='" + INK + "' stroke-width='2'/>";
      s += text(x + 14, plus === 'b' ? y + 30 : y - 20, '+', '#DC2626', 15, 'middle', 700) + text(x + 14, plus === 'b' ? y - 20 : y + 30, '\u2212', '#2563EB', 15, 'middle', 700);
      return s;
    }
    function inter2(x, y, pos, d) {   /* interrupteur à deux positions : pivot en (x, y), plots 1 (à gauche) et 2 (à droite), à la hauteur y − 22 */
      d = d || 26;
      var s = node(x - d, y - 22) + node(x + d, y - 22) + node(x, y);
      var tx = pos === 1 ? x - d + 3 : (pos === 2 ? x + d - 3 : x - 6), ty = pos ? y - 20 : y - 24;
      s += "<line x1='" + n(x) + "' y1='" + n(y) + "' x2='" + n(tx) + "' y2='" + n(ty) + "' stroke='" + INK + "' stroke-width='2.4' stroke-linecap='round'/>";
      s += text(x - d - 11, y - 17, '1', '#475569', 12, 'middle', 700) + text(x + d + 11, y - 17, '2', '#475569', 12, 'middle', 700);   /* numéros à l'extérieur des plots, loin des fils */
      return s;
    }
    function inter(x, y, ferme) {   /* interrupteur simple, horizontal */
      return "<rect x='" + n(x - 18) + "' y='" + n(y - 14) + "' width='36' height='18' fill='#fff'/>" + node(x - 15, y) + node(x + 15, y) + "<line x1='" + n(x - 15) + "' y1='" + n(y) + "' x2='" + n(x + 13) + "' y2='" + n(ferme ? y : y - 12) + "' stroke='" + INK + "' stroke-width='2.2' stroke-linecap='round'/>";
    }
    function svg(w, h, body, label, cls) { return "<svg class='" + (cls || 'nt-svg nt-svg-m') + "' viewBox='0 0 " + w + ' ' + h + "' role='img' aria-label=\"" + label + "\">" + body + "</svg>"; }
    return { cap: cap, src: src, inter2: inter2, inter: inter, wire: wire, text: text, qty: qty, node: node, res: res, therm: therm, rheo: rheo, lamp: lamp, gen: gen, meter: meter, led: led, sw: sw, iarr: iarr, uarr: uarr, svg: svg, INK: INK };
  })();
  /* ================= Charge et décharge d'un condensateur ================= */
  (function () {
    var root = document.getElementById('lab-rc');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rE = $(root, '[data-p="E"]'), rR = $(root, '[data-p="R"]'), rC = $(root, '[data-p="C"]'), oE = $(root, '.out-E'), oR = $(root, '.out-R'), oC = $(root, '.out-C'), oTau = $(root, '.out-tau'), oU = $(root, '.out-u'), oI = $(root, '.out-i'), msg = $(root, '.nt-msg');
    var b1 = $(root, '[data-act="charge"]'), b2 = $(root, '[data-act="decharge"]'), bT = $(root, '[data-act="tau"]'), bP = $(root, '[data-act="pause"]');
    var S, visible = true, last = null, mode = 0, t = 0, u0 = 0, uc = 0, histo = [], montrer = false, pause = false, pts = [];
    function par() { return { E: +rE.value, R: +rR.value * 1000, C: +rC.value * 1e-6 }; }
    function tau() { var p = par(); return p.R * p.C; }
    function uDe(tt) { var p = par(), T = tau(); return mode === 1 ? p.E + (u0 - p.E) * Math.exp(-tt / T) : (mode === 2 ? u0 * Math.exp(-tt / T) : u0); }
    function iDe(tt) { var p = par(), T = tau(); return mode === 1 ? (p.E - u0) / p.R * Math.exp(-tt / T) : (mode === 2 ? -u0 / p.R * Math.exp(-tt / T) : 0); }   /* i = dq/dt, orienté vers l'armature qui porte q */
    function basculer(m) {
      u0 = uc; t = 0; mode = m; histo = [[0, uc, iDe(0)]];
      msg.innerHTML = m === 1 ? '<b>Position 1&nbsp;: charge.</b> Le générateur pousse des charges sur l\u2019armature du haut, qui devient positive, et en retire autant de celle du bas. L\u2019intensité est maximale au départ, puis diminue&nbsp;: plus le condensateur est chargé, plus il «&nbsp;résiste&nbsp;» à l\u2019arrivée de nouvelles charges.'
        : '<b>Position 2&nbsp;: décharge.</b> Le générateur est retiré du circuit. Les charges accumulées sur les armatures se recombinent à travers le conducteur ohmique&nbsp;: le courant circule en sens inverse, donc i &lt; 0 avec notre orientation.';
      b1.classList.toggle('nt-btn-main', m === 1); b2.classList.toggle('nt-btn-main', m === 2);
    }
    function lignes(g) {   /* chemins suivis par le courant : de la source à l'armature du haut, et de l'armature du bas à la source */
      if (mode === 1) { return [[[g.xs0, g.ys - 17], [g.xs0, g.yt], [g.xk - 26, g.yt], [g.xk - 26, g.yk - 22], [g.xk, g.yk], [g.xk, g.ycap - 7]], [[g.xk, g.ycap + 7], [g.xk, g.yb], [g.xs0, g.yb], [g.xs0, g.ys + 17]]]; }
      if (mode === 2) { return [[[g.xk, g.ycap - 7], [g.xk, g.yk], [g.xk + 26, g.yk - 22], [g.xk + 26, g.yt], [g.xr, g.yt], [g.xr, g.yb], [g.xk, g.yb], [g.xk, g.ycap + 7]]]; }
      return [];
    }
    function longueur(P) { var L = 0; for (var k = 1; k < P.length; k++) { L += Math.hypot(P[k][0] - P[k - 1][0], P[k][1] - P[k - 1][1]); } return L; }
    function point(P, s) { for (var k = 1; k < P.length; k++) { var d = Math.hypot(P[k][0] - P[k - 1][0], P[k][1] - P[k - 1][1]); if (s <= d) { var f = s / d; return [P[k - 1][0] + (P[k][0] - P[k - 1][0]) * f, P[k - 1][1] + (P[k][1] - P[k - 1][1]) * f]; } s -= d; } return P[P.length - 1]; }
    function draw(dt) {
      if (!S) { return; }
      var p = par(), T = tau(), c = S.ctx, w = S.w, h = S.h, large = w >= 620;
      if (mode && !pause) { t += dt * T; uc = uDe(t); histo.push([t, uc, iDe(t)]); if (t > 6.5 * T) { t = 6.5 * T; } }
      var ic = mode ? iDe(t) : 0;
      oE.textContent = fr(p.E, 1) + ' V'; oR.textContent = nb(p.R / 1000, 3) + ' k\u03a9'; oC.textContent = nb(p.C * 1e6, 3) + ' \u00b5F';
      oTau.textContent = T >= 0.9995 ? fr(T, 2) + ' s' : nb(T * 1000, 3) + ' ms';   /* 10 kΩ × 100 µF : 1,00 s, malgré l'arrondi numérique */ oU.textContent = fr(uc, 2) + ' V'; oI.textContent = nb(ic * 1000, 3) + ' mA';
      c.clearRect(0, 0, w, h);
      /* ---- circuit ---- */
      var cw = large ? Math.min(300, w * 0.42) : w, g = { xs0: 36, ys: 160, yt: 40, yb: 290, xk: cw * 0.52, yk: 86, ycap: 232, xr: cw - 26 };
      c.lineWidth = 2; c.strokeStyle = '#1E293B'; c.lineCap = 'round'; c.lineJoin = 'round';
      c.beginPath(); c.moveTo(g.xs0, g.ys - 17); c.lineTo(g.xs0, g.yt); c.lineTo(g.xk - 26, g.yt); c.lineTo(g.xk - 26, g.yk - 22); c.stroke();
      c.beginPath(); c.moveTo(g.xk + 26, g.yk - 22); c.lineTo(g.xk + 26, g.yt); c.lineTo(g.xr, g.yt); c.lineTo(g.xr, g.yb); c.lineTo(g.xs0, g.yb); c.lineTo(g.xs0, g.ys + 17); c.stroke();
      c.beginPath(); c.moveTo(g.xk, g.yk); c.lineTo(g.xk, g.ycap - 7); c.moveTo(g.xk, g.ycap + 7); c.lineTo(g.xk, g.yb); c.stroke();
      /* source, interrupteur, conducteur ohmique */
      c.fillStyle = '#fff'; c.beginPath(); c.arc(g.xs0, g.ys, 17, 0, 2 * Math.PI); c.fill(); c.stroke(); c.beginPath(); c.moveTo(g.xs0, g.ys - 17); c.lineTo(g.xs0, g.ys + 17); c.stroke();
      txt(c, '+', g.xs0 + 15, g.ys - 20, '#DC2626', '700 15px system-ui'); txt(c, 'E', g.xs0 - 24, g.ys + 5, CE, 'italic 700 15px Georgia, serif');
      [[g.xk - 26, '1'], [g.xk + 26, '2']].forEach(function (q) { c.fillStyle = '#1E293B'; c.beginPath(); c.arc(q[0], g.yk - 22, 3.5, 0, 2 * Math.PI); c.fill(); txt(c, q[1], q[0] + (q[1] === '1' ? -11 : 11), g.yk - 16, '#475569', '700 12px system-ui'); });
      c.fillStyle = '#1E293B'; c.beginPath(); c.arc(g.xk, g.yk, 3.5, 0, 2 * Math.PI); c.fill();
      c.lineWidth = 2.6; c.beginPath(); c.moveTo(g.xk, g.yk); c.lineTo(mode === 1 ? g.xk - 23 : (mode === 2 ? g.xk + 23 : g.xk - 6), mode ? g.yk - 20 : g.yk - 24); c.stroke(); c.lineWidth = 2;
      txt(c, 'K', g.xk, g.yt - 10, '#1E293B', '700 13px system-ui');
      c.fillStyle = '#fff'; c.fillRect(g.xk - 8, 128, 16, 40); c.strokeRect(g.xk - 8, 128, 16, 40); txt(c, 'R', g.xk - 16, 152, '#1E293B', '700 13px system-ui', 'right');
      /* condensateur : armatures et charges, en proportion de q = C u_C */
      var nq = Math.round(Math.abs(uc) / 12 * 9), pw = 34;
      c.fillStyle = '#fff'; c.fillRect(g.xk - pw - 4, g.ycap - 9, 2 * pw + 8, 18);
      c.fillStyle = uc > 0.05 ? '#FCA5A5' : '#CBD5E1'; c.fillRect(g.xk - pw, g.ycap - 9, 2 * pw, 4);
      c.fillStyle = uc > 0.05 ? '#93C5FD' : '#CBD5E1'; c.fillRect(g.xk - pw, g.ycap + 5, 2 * pw, 4);
      for (var k = 0; k < nq; k++) { var xq = g.xk - pw + 4 + k * (2 * pw - 8) / 8; txt(c, '+', xq, g.ycap - 13, '#DC2626', '800 11px system-ui'); txt(c, '\u2212', xq, g.ycap + 22, '#2563EB', '800 11px system-ui'); }
      txt(c, 'C', g.xk - pw - 8, g.ycap + 5, '#1E293B', '700 13px system-ui', 'right');
      /* courant : points qui circulent, vitesse proportionnelle à |i| */
      var imax = p.E / p.R, chemins = lignes(g);
      if (mode && Math.abs(ic) > imax * 0.004) {
        var v = 140 * Math.abs(ic) / imax;
        chemins.forEach(function (P, j) {
          var L = longueur(P); if (!pts[j]) { pts[j] = []; for (var q = 0; q < 14; q++) { pts[j].push(q / 14); } }
          pts[j] = pts[j].map(function (s) { return (s + (pause ? 0 : v * dt / L)) % 1; });
          pts[j].forEach(function (s) { var xy = point(P, s * L); c.fillStyle = 'rgba(225,29,72,.85)'; c.beginPath(); c.arc(xy[0], xy[1], 3, 0, 2 * Math.PI); c.fill(); });
        });
      }
      /* tension u_C à côté du condensateur */
      c.strokeStyle = CC; c.fillStyle = CC; c.lineWidth = 2; c.beginPath(); c.moveTo(g.xk + pw + 12, g.ycap + 22); c.lineTo(g.xk + pw + 12, g.ycap - 18); c.stroke(); c.beginPath(); c.moveTo(g.xk + pw + 12, g.ycap - 24); c.lineTo(g.xk + pw + 7, g.ycap - 14); c.lineTo(g.xk + pw + 17, g.ycap - 14); c.closePath(); c.fill();
      txt(c, 'u', g.xk + pw + 20, g.ycap + 2, CC, 'italic 700 14px Georgia, serif', 'left'); txt(c, 'C', g.xk + pw + 28, g.ycap + 6, CC, '700 10px Georgia, serif', 'left');
      if (!large) { return; }
      /* ---- courbes u_C(t) et i(t) ---- */
      var L0 = cw + 52, R0 = w - 46, T0 = 16, B0 = h - 34, tmax = 6 * T, uMax = 12;
      function X(s) { return L0 + s / tmax * (R0 - L0); }
      function Y(u) { return B0 - u / uMax * (B0 - T0); }
      function Yi(i) { return (B0 + T0) / 2 - i / imax * (B0 - T0) / 2 * 0.9; }   /* i sur l'axe de droite, centré sur 0 */
      for (var kk = 0; kk <= 6; kk++) { c.strokeStyle = '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(X(kk * T), T0); c.lineTo(X(kk * T), B0); c.stroke(); txt(c, kk === 0 ? '0' : kk + '\u03c4', X(kk * T), B0 + 15, '#475569', '11px system-ui'); }
      for (var uu = 0; uu <= 12; uu += 2) { c.strokeStyle = '#F1F5F9'; c.beginPath(); c.moveTo(L0, Y(uu)); c.lineTo(R0, Y(uu)); c.stroke(); txt(c, String(uu), L0 - 6, Y(uu) + 4, CC, '11px system-ui', 'right'); }
      c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L0, T0); c.lineTo(L0, B0); c.lineTo(R0, B0); c.stroke();
      txt(c, 't \u2192', R0 - 8, B0 + 28, '#475569', '11px system-ui'); txt(c, 'u\u1d04 (V)', L0 - 6, T0 - 4, CC, '700 11px system-ui', 'right'); txt(c, 'i', R0 + 10, T0 - 4, CIc, 'italic 700 12px Georgia, serif');
      txt(c, '+' + nb(imax * 1000, 2) + ' mA', R0 + 4, Yi(imax) + 4, CIc, '10px system-ui', 'left'); txt(c, '0', R0 + 4, Yi(0) + 4, CIc, '10px system-ui', 'left'); txt(c, '\u2212' + nb(imax * 1000, 2), R0 + 4, Yi(-imax) + 4, CIc, '10px system-ui', 'left');
      c.strokeStyle = 'rgba(225,29,72,.25)'; c.setLineDash([2, 3]); c.beginPath(); c.moveTo(L0, Yi(0)); c.lineTo(R0, Yi(0)); c.stroke(); c.setLineDash([]);
      c.strokeStyle = 'rgba(22,163,74,.6)'; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(L0, Y(p.E)); c.lineTo(R0, Y(p.E)); c.stroke(); c.setLineDash([]); txt(c, 'E', L0 + 8, Y(p.E) - 5, CE, 'italic 700 13px Georgia, serif', 'left');
      if (montrer && mode) {   /* constructions : tangente à l'origine, 63 % ou 37 %, τ et 5τ */
        var uf = mode === 1 ? p.E : 0, u63 = uf + (u0 - uf) * Math.exp(-1);
        c.strokeStyle = '#7C3AED'; c.lineWidth = 1.5; c.setLineDash([5, 4]);
        c.beginPath(); c.moveTo(X(0), Y(u0)); c.lineTo(X(T), Y(uf)); c.stroke();
        c.beginPath(); c.moveTo(L0, Y(u63)); c.lineTo(X(T), Y(u63)); c.lineTo(X(T), B0); c.stroke();
        c.strokeStyle = '#059669'; c.beginPath(); c.moveTo(X(5 * T), T0); c.lineTo(X(5 * T), B0); c.stroke(); c.setLineDash([]);
        txt(c, mode === 1 ? '63 % de E' : '37 % de E', L0 + 8, Y(u63) - 6, '#7C3AED', '700 11px system-ui', 'left');
        txt(c, '\u03c4', X(T) + 8, B0 - 8, '#7C3AED', '700 14px Georgia, serif', 'left'); txt(c, '5\u03c4 : régime permanent à 99 %', X(5 * T) - 6, T0 + 12, '#059669', '600 10.5px system-ui', 'right');
      }
      if (histo.length > 1) {
        c.strokeStyle = CIc; c.lineWidth = 2; c.beginPath(); histo.forEach(function (q, j) { if (j === 0) { c.moveTo(X(q[0]), Yi(q[2])); } else { c.lineTo(X(q[0]), Yi(q[2])); } }); c.stroke();
        c.strokeStyle = CC; c.lineWidth = 2.6; c.beginPath(); histo.forEach(function (q, j) { if (j === 0) { c.moveTo(X(q[0]), Y(q[1])); } else { c.lineTo(X(q[0]), Y(q[1])); } }); c.stroke();
        c.fillStyle = CC; c.beginPath(); c.arc(X(t), Y(uc), 5, 0, 2 * Math.PI); c.fill();
      }
      txt(c, 'u\u1d04(t)', R0 - 40, Y(uc) - 10 < T0 + 10 ? T0 + 24 : Y(uc) - 10, CC, '700 12px system-ui'); 
    }
    function loop(ts) { var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; if (visible) { draw(RM ? dt * 0.5 : dt); } requestAnimationFrame(loop); }
    b1.addEventListener('click', function () { basculer(1); });
    b2.addEventListener('click', function () { basculer(2); });
    bT.addEventListener('click', function () { montrer = !montrer; bT.classList.toggle('nt-btn-main', montrer); });
    bP.addEventListener('click', function () { pause = !pause; bP.innerHTML = pause ? '<i class="fa-solid fa-play"></i>&nbsp; Reprendre' : '<i class="fa-solid fa-pause"></i>&nbsp; Pause'; });
    [rE, rR, rC].forEach(function (r) { r.addEventListener('input', function () { if (mode) { basculer(mode); } draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    watch(cv, function (v) { visible = v; });
    msg.innerHTML = 'Le condensateur est déchargé. Basculez l\u2019interrupteur en position 1 pour le charger.';
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Deux DEL qui révèlent le sens du courant ================= */
  (function () {
    var root = document.getElementById('lab-del');
    if (!root) { return; }
    var box = $(root, '.nt-del-svg'), msg = $(root, '.nt-msg'), b1 = $(root, '[data-act="p1"]'), b2 = $(root, '[data-act="p2"]'), bR = $(root, '[data-act="reset"]'), last = null, svgT = 0;
    var E = 6, R1 = 470, R2 = 1000, C = 2200e-6, VS1 = 2.1, VS2 = 1.8, RD = 15, pos = 0, uc = 0, iNow = 0;
    function vnet(i) {   /* tension aux bornes de l'ensemble {D1, R2, D2} en dérivation */
      var a = Math.abs(i), vs = i >= 0 ? VS1 : VS2, v = R2 * a;
      if (v > vs) { var rp = RD * R2 / (RD + R2); v = vs + (a - vs / R2) * rp; }
      return i >= 0 ? v : -v;
    }
    function courant(V) { var lo = -0.05, hi = 0.05; for (var k = 0; k < 60; k++) { var m = (lo + hi) / 2; if (R1 * m + vnet(m) > V) { hi = m; } else { lo = m; } } return (lo + hi) / 2; }
    function eclat(i, d) { var v = Math.abs(vnet(i)), vs = d === 1 ? VS1 : VS2; if ((d === 1 && i <= 0) || (d === 2 && i >= 0) || v <= vs) { return 0; } return Math.min(1, 0.25 + (v - vs) / RD / 0.004); }   /* dès qu'elle conduit, la DEL est nettement visible */
    function schema() {
      var g1 = eclat(iNow, 1), g2 = eclat(iNow, 2), b = '';
      b += CI.wire([[60, 40], [174, 40], [174, 62]]) + CI.wire([[226, 62], [226, 40], [330, 40], [330, 330], [60, 330], [60, 40]]);
      b += CI.wire([[200, 84], [200, 110]]) + CI.wire([[140, 110], [260, 110]]) + CI.wire([[140, 110], [140, 170]]) + CI.wire([[200, 110], [200, 170]]) + CI.wire([[260, 110], [260, 170]]) + CI.wire([[140, 170], [260, 170]]) + CI.wire([[200, 170], [200, 330]]);
      b += CI.wire([[200, 245], [280, 245], [280, 295], [200, 295]]);
      b += CI.src(60, 190, 't') + CI.inter2(200, 84, pos) + CI.res(200, 140, 'v') + CI.res(200, 205, 'v') + CI.cap(200, 270, 'v');
      if (g1 > 0.02) { b += "<circle cx='140' cy='140' r='" + (14 + 16 * g1).toFixed(1) + "' fill='rgba(34,197,94," + (0.65 * g1).toFixed(2) + ")'/>"; }
      if (g2 > 0.02) { b += "<circle cx='260' cy='140' r='" + (14 + 16 * g2).toFixed(1) + "' fill='rgba(239,68,68," + (0.65 * g2).toFixed(2) + ")'/>"; }
      b += CI.led(140, 140, 'v', 'd') + CI.led(260, 140, 'v', 'u');
      if (g1 > 0.02) { b += "<polygon points='129,131 151,131 140,149' fill='rgba(34,197,94," + (0.35 + 0.6 * g1).toFixed(2) + ")'/>"; }   /* triangle coloré : la DEL conduit */
      if (g2 > 0.02) { b += "<polygon points='249,149 271,149 260,131' fill='rgba(239,68,68," + (0.35 + 0.6 * g2).toFixed(2) + ")'/>"; }
      b += CI.node(200, 110) + CI.node(200, 170) + CI.node(200, 245) + CI.node(200, 295) + CI.node(200, 330) + CI.meter(280, 270, 'V', 't');
      b += "<rect x='296' y='257' width='70' height='26' rx='5' fill='#0F172A'/><text x='331' y='275' font-size='13' text-anchor='middle' fill='#4ADE80' font-family='ui-monospace, Menlo, monospace'>" + fr(uc, 2) + " V</text>";
      function nom(x, y, L, i, col, anchor) { return "<text x='" + x + "' y='" + y + "' font-size='13' text-anchor='" + anchor + "' fill='" + col + "' font-family='system-ui, sans-serif' font-weight='700'>" + L + "<tspan font-size='9' dy='3'>" + i + "</tspan></text>"; }
      b += nom(118, 145, 'D', '1', '#15803D', 'end') + nom(282, 145, 'D', '2', '#B91C1C', 'start') + nom(212, 145, 'R', '2', '#1E293B', 'start') + nom(188, 210, 'R', '1', '#1E293B', 'end') + CI.text(178, 275, 'C', '#1E293B', 13, 'end', 700);
      b += CI.uarr(28, 236, 28, 146, 'E', '', CE, -6, 0, 'end') + CI.text(200, 26, 'K', '#1E293B', 13, 'middle', 700);
      return CI.svg(400, 350, b, 'Montage : un générateur, un interrupteur à deux positions, deux DEL tête-bêche en dérivation avec un conducteur ohmique R2, un conducteur ohmique R1 et un condensateur C dont la tension est mesurée au voltmètre', 'nt-svg');
    }
    function etat() {
      if (!pos) { return 'L\u2019interrupteur est ouvert&nbsp;: aucun courant ne circule.'; }
      var g1 = eclat(iNow, 1), g2 = eclat(iNow, 2);
      if (pos === 1) { return g1 > 0.02 ? '<b>Charge</b>&nbsp;: le courant circule vers le bas et traverse la DEL verte D<sub>1</sub>, qui s\u2019allume. Elle faiblit à mesure que le condensateur se charge et que l\u2019intensité diminue.' : '<b>Charge</b>&nbsp;: l\u2019intensité est devenue trop faible pour que la DEL verte reste allumée (sous sa tension de seuil). Le condensateur continue pourtant de se charger, à travers R<sub>2</sub>, jusqu\u2019à u<sub>C</sub> = E.'; }
      return g2 > 0.02 ? '<b>Décharge</b>&nbsp;: le courant circule maintenant vers le haut et traverse la DEL rouge D<sub>2</sub>&nbsp;: <b>le sens du courant s\u2019est inversé</b>.' : '<b>Décharge</b>&nbsp;: la DEL rouge s\u2019est éteinte, mais le condensateur finit de se décharger à travers R<sub>2</sub>, jusqu\u2019à u<sub>C</sub> = 0.';
    }
    function loop(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (pos) { for (var k = 0; k < 10; k++) { iNow = courant((pos === 1 ? E : 0) - uc); uc += iNow / C * dt / 10; } }
      svgT += dt; if (svgT > 0.06) { svgT = 0; box.innerHTML = schema(); msg.innerHTML = etat(); }
      requestAnimationFrame(loop);
    }
    b1.addEventListener('click', function () { pos = 1; }); b2.addEventListener('click', function () { pos = 2; });
    bR.addEventListener('click', function () { pos = 0; uc = 0; iNow = 0; });
    box.innerHTML = schema(); msg.innerHTML = etat(); requestAnimationFrame(loop);
  })();
  /* ================= Entraînement : q = C·u et τ = R·C ================= */
  (function () {
    var root = document.getElementById('lab-calc');
    if (!root) { return; }
    var qEl = $(root, '.nt-tr-q'), inp = $(root, 'input[type="text"]'), uEl = $(root, '.nt-tr-unit'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), bV = $(root, '[data-act="check"]'), bN = $(root, '[data-act="next"]'), lblN = bN.innerHTML;
    var NQ = 6, n = 0, good = 0, cur, done = false, fini = false, res = [], vis = $(root, '.nt-qvis'), prog = $(root, '.nt-prog'), num0 = $(root, '.nt-qnum');
    function progres() { prog.innerHTML = Array.apply(null, Array(NQ)).map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === n - (done ? 1 : 0) && !fini ? ' cur' : '') + '"></i>'; }).join(''); num0.textContent = fini ? 'Bilan' : 'Question ' + Math.min(NQ, n + (done ? 0 : 1)) + ' sur ' + NQ; }
    var G = [
      function () { var Cu = pick([2.2, 4.7, 10, 22, 47, 100, 220, 470]), U = pick([3, 5, 6, 9, 12]), q = Cu * U;
        return { vis: '<span><i>C</i> = ' + nb(Cu, 2) + '&nbsp;µF</span><span><i>u</i><sub>C</sub> = ' + U + '&nbsp;V</span>', q: 'Un condensateur de capacité ' + nb(Cu, 2) + '&nbsp;µF est chargé sous ' + U + '&nbsp;V. Quelle charge q porte son armature positive, en <b>µC</b>&nbsp;?', rep: q, unit: 'µC',
          expl: 'q = C × u<sub>C</sub> = ' + nb(Cu, 2) + ' × 10<sup>−6</sup> × ' + U + ' = ' + nb(q, 3) + ' × 10<sup>−6</sup>&nbsp;C = ' + nb(q, 3) + '&nbsp;µC.' }; },
      function () { var Cu = pick([10, 22, 47, 100, 220]), U = pick([4, 5, 10, 12]), q = Cu * U;
        return { vis: '<span><i>q</i> = ' + nb(q, 3) + '&nbsp;µC</span><span><i>u</i><sub>C</sub> = ' + U + '&nbsp;V</span>', q: 'L\u2019armature positive d\u2019un condensateur porte ' + nb(q, 3) + '&nbsp;µC quand la tension à ses bornes vaut ' + U + '&nbsp;V. Quelle est sa capacité, en <b>µF</b>&nbsp;?', rep: Cu, unit: 'µF',
          expl: 'C = q / u<sub>C</sub> = ' + nb(q, 3) + ' × 10<sup>−6</sup> / ' + U + ' = ' + nb(Cu, 2) + ' × 10<sup>−6</sup>&nbsp;F = ' + nb(Cu, 2) + '&nbsp;µF.' }; },
      function () { var Rk = pick([1, 2.2, 4.7, 10, 22, 47]), Cu = pick([10, 22, 47, 100, 220]), T = Rk * Cu;
        return { vis: '<span><i>R</i> = ' + nb(Rk, 2) + '&nbsp;k\u03a9</span><span><i>C</i> = ' + Cu + '&nbsp;µF</span>', q: 'Un circuit RC série comporte R = ' + nb(Rk, 2) + '&nbsp;k\u03a9 et C = ' + Cu + '&nbsp;µF. Calculer sa constante de temps τ, en <b>ms</b>.', rep: T, unit: 'ms',
          expl: 'τ = R × C = ' + nb(Rk, 2) + ' × 10<sup>3</sup> × ' + Cu + ' × 10<sup>−6</sup> = ' + nb(T / 1000, 3) + '&nbsp;s = ' + nb(T, 3) + '&nbsp;ms. (Astuce&nbsp;: kΩ × µF donne des ms.)' }; },
      function () { var E = pick([5, 6, 10, 12]), ch = Math.random() < 0.5, u = ch ? E * (1 - Math.exp(-1)) : E * Math.exp(-1);
        return { vis: '<span>' + (ch ? 'charge' : 'décharge') + '</span><span><i>E</i> = ' + E + '&nbsp;V</span><span><i>t</i> = <i>τ</i></span>', q: (ch ? 'On charge' : 'On décharge') + ' un condensateur ' + (ch ? 'initialement déchargé, sous la tension E = ' + E + '&nbsp;V' : 'initialement chargé sous E = ' + E + '&nbsp;V') + '. Quelle est la tension u<sub>C</sub> à ses bornes à l\u2019instant t = τ, en <b>V</b>&nbsp;?', rep: u, unit: 'V',
          expl: ch ? 'u<sub>C</sub>(τ) = E(1 − e<sup>−1</sup>) ≈ 0,63 × E = ' + nb(u, 3) + '&nbsp;V&nbsp;: à t = τ, la charge a parcouru 63&nbsp;% du chemin.' : 'u<sub>C</sub>(τ) = E × e<sup>−1</sup> ≈ 0,37 × E = ' + nb(u, 3) + '&nbsp;V&nbsp;: à t = τ, il reste 37&nbsp;% de la tension initiale.' }; },
      function () { var Rk = pick([10, 22, 47, 100]), Cu = pick([100, 220, 470, 1000]), T = Rk * Cu / 1000;
        return { vis: '<span><i>R</i> = ' + Rk + '&nbsp;k\u03a9</span><span><i>C</i> = ' + Cu + '&nbsp;µF</span><span>charge à 99&nbsp;%</span>', q: 'Au bout de combien de temps peut-on considérer qu\u2019un condensateur (C = ' + Cu + '&nbsp;µF), qui se charge à travers R = ' + Rk + '&nbsp;k\u03a9, est chargé, à mieux de 99&nbsp;%&nbsp;? Réponse en <b>s</b>.', rep: 5 * T, unit: 's',
          expl: 'τ = RC = ' + nb(T, 3) + '&nbsp;s. On atteint le régime permanent à mieux de 99&nbsp;% au bout de 5τ = ' + nb(5 * T, 3) + '&nbsp;s.' }; }
    ];
    function nouveau() { cur = pick(G)(); qEl.innerHTML = cur.q; vis.innerHTML = '<span class="nt-qdata">' + cur.vis + '</span>'; vis.hidden = false; uEl.textContent = cur.unit; inp.value = ''; msg.textContent = ''; msg.className = 'nt-msg'; done = false; bV.disabled = false; inp.disabled = false; bN.innerHTML = n === NQ - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lblN; progres(); }
    function start() { n = 0; good = 0; fini = false; res = []; sc.textContent = '0 / 0'; $(root, '.nt-tr-zone').hidden = false; nouveau(); }
    bV.addEventListener('click', function () {
      if (done || fini) { return; }
      var v = num(inp.value); if (isNaN(v)) { msg.className = 'nt-msg'; msg.textContent = 'Entrez une valeur numérique.'; return; }
      var ok = Math.abs(v - cur.rep) <= Math.abs(cur.rep) * 0.025; done = true; res[n] = ok; n++; if (ok) { good++; }
      bV.disabled = true; inp.disabled = true; sc.textContent = good + ' / ' + n;
      msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko');
      msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Non</b>&nbsp;: la réponse est ' + nb(cur.rep, 3) + '&nbsp;' + cur.unit + '. ') + cur.expl; progres();
    });
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { bV.click(); } });
    bN.addEventListener('click', function () {
      if (fini) { start(); return; }
      if (!done) { msg.className = 'nt-msg'; msg.textContent = 'Validez d\u2019abord votre réponse.'; return; }
      if (n >= NQ) { fini = true; $(root, '.nt-tr-zone').hidden = true; vis.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + NQ + '</span> ' + bilanTxt(good / NQ); msg.textContent = ''; msg.className = 'nt-msg'; progres(); bN.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; return; }
      nouveau();
    });
    start();
  })();
  /* ================= Entraînement : lire τ sur une courbe ================= */
  (function () {
    var root = document.getElementById('lab-tau');
    if (!root) { return; }
    var cv = $(root, 'canvas'), qEl = $(root, '.nt-tr-q'), inp = $(root, 'input[type="text"]'), uEl = $(root, '.nt-tr-unit'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), bV = $(root, '[data-act="check"]'), bN = $(root, '[data-act="next"]');
    var S, cur = null, rep = false, n = 0, good = 0, pente = null, glisse = false;   /* pente : pente de la tangente tracée par l'élève (V par unité de temps) */
    function nouveau() {
      var ch = Math.random() < 0.5, E = pick([4, 5, 6, 8, 10, 12]), sc0 = pick([[1, 's'], [1, 'ms']]), T = pick([0.6, 0.8, 1.2, 1.5, 2, 2.4, 3, 3.5, 4]);
      cur = { ch: ch, E: E, T: T, unit: sc0[1], tmax: T * 7 > 20 ? 30 : (T * 7 > 10 ? 20 : 10) };
      rep = false; pente = null; inp.value = ''; inp.disabled = false; bV.disabled = false; uEl.textContent = cur.unit; msg.textContent = '';
      qEl.innerHTML = 'Voici l\u2019enregistrement de la tension u<sub>C</sub> lors de la ' + (ch ? 'charge' : 'décharge') + ' d\u2019un condensateur. Déterminer graphiquement la constante de temps τ, en <b>' + cur.unit + '</b>.';
      msg.innerHTML = '<i class="fa-solid fa-hand-pointer"></i>&nbsp; Faites glisser sur le graphique pour faire pivoter la tangente à l\u2019origine, puis lisez τ à son intersection avec l\u2019asymptote.';
      draw();
    }
    function geo() { var w = S.w, h = S.h; return { L: 52, R: w - 16, T0: 14, B: h - 36, tm: cur.tmax, um: Math.ceil(cur.E * 1.15 / 2) * 2 }; }
    function draw() {
      if (!S || !cur) { return; }
      var c = S.ctx, w = S.w, h = S.h, G = geo(), L = G.L, R = G.R, T0 = G.T0, B = G.B, tm = G.tm, um = G.um;
      function X(t) { return L + t / tm * (R - L); }
      function Y(u) { return B - u / um * (B - T0); }
      function U(t) { return cur.ch ? cur.E * (1 - Math.exp(-t / cur.T)) : cur.E * Math.exp(-t / cur.T); }
      c.clearRect(0, 0, w, h);
      var st = tm / 20; for (var t = 0; t <= tm + 1e-9; t += st) { c.strokeStyle = Math.round(t / st) % 2 ? '#F1F5F9' : '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(X(t), T0); c.lineTo(X(t), B); c.stroke(); if (Math.round(t / st) % 2 === 0) { txt(c, nb(t, 2), X(t), B + 15, '#475569', '11px system-ui'); } }
      for (var u = 0; u <= um + 1e-9; u += 0.5) { c.strokeStyle = u % 1 ? '#F1F5F9' : '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(L, Y(u)); c.lineTo(R, Y(u)); c.stroke(); if (u % 1 === 0) { txt(c, String(u), L - 6, Y(u) + 4, '#475569', '11px system-ui', 'right'); } }
      c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L, T0); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
      txt(c, 't (' + cur.unit + ') \u2192', R - 30, B + 29, '#475569', '11px system-ui');
      c.save(); c.translate(14, (T0 + B) / 2); c.rotate(-Math.PI / 2); txt(c, 'u\u1d04 (V) \u2192', 0, 0, '#475569', '11px system-ui'); c.restore();
      c.strokeStyle = CC; c.lineWidth = 2.6; c.beginPath(); for (var k = 0; k <= 300; k++) { var tt = tm * k / 300; if (k === 0) { c.moveTo(X(tt), Y(U(tt))); } else { c.lineTo(X(tt), Y(U(tt))); } } c.stroke();
      var uf0 = cur.ch ? cur.E : 0, ui0 = cur.ch ? 0 : cur.E;
      if (!rep) {   /* asymptote, puis la tangente tracée par l'élève (demi-droite issue du point de départ) */
        c.strokeStyle = 'rgba(5,150,105,.55)'; c.lineWidth = 1.4; c.setLineDash([6, 4]); c.beginPath(); c.moveTo(L, Y(uf0)); c.lineTo(R, Y(uf0)); c.stroke(); c.setLineDash([]);
        txt(c, 'asymptote', R - 4, Y(uf0) - 6, '#059669', '600 10.5px system-ui', 'right');
        if (pente !== null) {
          var te = tm, ue = ui0 + pente * te;   /* extrémité : là où la demi-droite sort du graphique */
          if (ue > um) { te = (um - ui0) / pente; ue = um; } else if (ue < 0) { te = -ui0 / pente; ue = 0; }
          c.strokeStyle = '#7C3AED'; c.lineWidth = 2.2; c.beginPath(); c.moveTo(X(0), Y(ui0)); c.lineTo(X(te), Y(ue)); c.stroke();
          c.fillStyle = '#7C3AED'; c.beginPath(); c.arc(X(te * 0.8), Y(ui0 + pente * te * 0.8), 6, 0, 2 * Math.PI); c.fill();   /* poignée */
          var ti = (uf0 - ui0) / pente;   /* intersection avec l'asymptote */
          if (ti > 0 && ti <= tm) { c.strokeStyle = '#7C3AED'; c.lineWidth = 1.2; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(X(ti), Y(uf0)); c.lineTo(X(ti), B); c.stroke(); c.setLineDash([]); c.fillStyle = '#fff'; c.beginPath(); c.arc(X(ti), Y(uf0), 5, 0, 2 * Math.PI); c.fill(); c.strokeStyle = '#7C3AED'; c.lineWidth = 2; c.stroke(); }
        }
        c.fillStyle = '#7C3AED'; c.beginPath(); c.arc(X(0), Y(ui0), 4, 0, 2 * Math.PI); c.fill();
      }
      if (rep) {   /* correction : tangente à l'origine et 63 % ou 37 % */
        var uf = cur.ch ? cur.E : 0, u0 = cur.ch ? 0 : cur.E, u63 = U(cur.T);
        c.strokeStyle = '#7C3AED'; c.lineWidth = 1.6; c.setLineDash([6, 4]); c.beginPath(); c.moveTo(X(0), Y(u0)); c.lineTo(X(cur.T * 1.25), Y(u0 + (uf - u0) * 1.25)); c.stroke();
        c.strokeStyle = '#059669'; c.beginPath(); c.moveTo(L, Y(uf)); c.lineTo(R, Y(uf)); c.stroke();
        c.strokeStyle = '#E11D48'; c.beginPath(); c.moveTo(L, Y(u63)); c.lineTo(X(cur.T), Y(u63)); c.moveTo(X(cur.T), Y(Math.max(u63, uf))); c.lineTo(X(cur.T), B); c.stroke(); c.setLineDash([]);   /* le pointillé vertical monte jusqu'à l'intersection de la tangente et de l'asymptote */
        c.fillStyle = '#7C3AED'; c.beginPath(); c.arc(X(cur.T), Y(uf), 4.5, 0, 2 * Math.PI); c.fill();
        txt(c, 'tangente à l\u2019origine', X(cur.T * 0.5) + 8, Y(u0 + (uf - u0) * 0.5), '#7C3AED', '700 11px system-ui', 'left');
        txt(c, (cur.ch ? '63 %' : '37 %') + ' de E = ' + fr(u63, 2) + ' V', L + 6, Y(u63) - 6, '#E11D48', '700 11px system-ui', 'left');
        txt(c, '\u03c4 = ' + nb(cur.T, 2) + ' ' + cur.unit, X(cur.T) + 6, B - 8, '#E11D48', '700 12px system-ui', 'left');
      }
    }
    bV.addEventListener('click', function () {
      if (rep) { return; } var v = num(inp.value); if (isNaN(v)) { msg.textContent = 'Entrez une valeur.'; return; }
      rep = true; n++; var ok = Math.abs(v - cur.T) <= cur.T * 0.08; if (ok) { good++; }
      sc.textContent = good + ' / ' + n; inp.disabled = true; bV.disabled = true;
      msg.innerHTML = (ok ? '<span style="color:#16A34A;">Bravo&nbsp;!</span> ' : '<span style="color:#E11D48;">Non</span>&nbsp;: τ = ' + nb(cur.T, 2) + '&nbsp;' + cur.unit + '. ') + 'Deux méthodes, tracées sur le graphique&nbsp;: la tangente à l\u2019origine coupe l\u2019asymptote u<sub>C</sub> = ' + (cur.ch ? 'E' : '0') + ' à t = τ&nbsp;; et à t = τ, u<sub>C</sub> vaut ' + (cur.ch ? '63&nbsp;%' : '37&nbsp;%') + ' de E.';
      draw();
    });
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { bV.click(); } });
    /* faire pivoter la tangente : la demi-droite passe par le point de départ et par le pointeur */
    function viser(e) {
      if (rep || !cur) { return; }
      var r = cv.getBoundingClientRect(), G = geo(), px = e.clientX - r.left, py = e.clientY - r.top;
      var tt = (px - G.L) / (G.R - G.L) * G.tm, uu = (G.B - py) / (G.B - G.T0) * G.um, ui0 = cur.ch ? 0 : cur.E;
      if (tt <= G.tm * 0.01) { return; }
      pente = (uu - ui0) / tt; draw();
    }
    cv.addEventListener('pointerdown', function (e) { if (rep) { return; } glisse = true; cv.setPointerCapture(e.pointerId); viser(e); e.preventDefault(); });
    cv.addEventListener('pointermove', function (e) { if (glisse) { viser(e); } });
    ['pointerup', 'pointercancel'].forEach(function (ev) { cv.addEventListener(ev, function () { glisse = false; }); });
    bN.addEventListener('click', nouveau);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); nouveau(); onResize(setup);
  })();
})();
</script>
