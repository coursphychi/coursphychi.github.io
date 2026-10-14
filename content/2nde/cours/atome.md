+++
title = "L'atome"
draft = false
hidden = true
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-ql-q { font-size: 1.05em; text-align: center; margin: 0.5em 0 0.7em !important; min-height: 1.6em; }
.nt-ql-btns { display: flex; flex-wrap: wrap; gap: 0.45em; justify-content: center; }
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
.nt-lab .nt-msg { margin-top: 1em !important; }
.nt-lab [hidden] { display: none !important; }
.nt-tr-ans { display: flex; align-items: center; justify-content: center; gap: 0.5em; flex-wrap: wrap; margin: 0.6em 0; }
.nt-champ { display: inline-flex; align-items: center; gap: 0.35em; white-space: nowrap; margin: 0 0.7em; }
.nt-champ label { display: inline; margin: 0; font-weight: 600; }
.nt-champ input[type="text"] { width: 4.5em !important; min-width: 0; margin: 0; padding: 0.25em 0.5em; text-align: right; font: inherit; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-champ .nt-u { color: var(--slate); }
.nt-svgbox { margin: 0.6em auto; }
.nt-svgbox svg { display: block; width: 100%; height: auto; }
.nt-not { display: inline-flex; align-items: stretch; vertical-align: middle; line-height: 1; }
.nt-nuc { display: flex; flex-direction: column; justify-content: space-between; text-align: right; font-size: 0.5em; line-height: 1; padding: 0.04em 0.08em 0.02em 0; }
.nt-sym { line-height: 1; }
.nt-chg { align-self: flex-start; font-size: 0.55em; line-height: 1; margin-left: 0.06em; margin-top: 0.02em; }
.nt-prog { display: flex; flex-wrap: wrap; gap: 0.4em; justify-content: center; margin: 0.3em 0 0.5em; }
.nt-prog i { width: 0.85em; height: 0.85em; border-radius: 50%; background: #E2E8F0; transition: background .25s; }
.nt-prog i.ok { background: #22C55E; } .nt-prog i.ko { background: #F43F5E; } .nt-prog i.cur { box-shadow: 0 0 0 2.5px var(--blue); }
.nt-qnum { text-align: center; font-size: 0.82em; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; color: var(--blue); margin: 0; }
.nt-qcard { background: linear-gradient(180deg, #FFFFFF, #F8FAFC); border: 1px solid var(--line); border-radius: 16px; padding: 0.9em 1em 1em; margin: 0.4em auto 0.6em; max-width: 620px; box-shadow: 0 6px 18px rgba(15,23,42,.06); }
.nt-qvis { font-family: Georgia, serif; font-size: 2.8em; text-align: center; margin: 0.15em 0 0.25em; }
.nt-qcomp { font-family: system-ui, sans-serif; font-size: 0.5em; } .nt-qcomp .p { color: #E11D48; } .nt-qcomp .n { color: #16A34A; }
.nt-ql-btns .nt-choix { padding: 0.6em 1.1em; border-radius: 12px; font-size: 1em; transition: transform .12s, box-shadow .12s; }
.nt-ql-btns .nt-choix:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37,99,235,.18); }
.nt-choix-ok { background: #DCFCE7 !important; border-color: #16A34A !important; color: #166534 !important; }
.nt-choix-ko { background: #FFE4E6 !important; border-color: #E11D48 !important; color: #9F1239 !important; }
.nt-msg.nt-fb { border-radius: 12px; padding: 0.6em 0.9em; text-align: left; }
.nt-msg.nt-fb.ok { background: #F0FDF4; border-left: 4px solid #22C55E; } .nt-msg.nt-fb.ko { background: #FFF1F2; border-left: 4px solid #F43F5E; }
.nt-at-nota { font-family: Georgia, serif; font-size: 2.2em; text-align: center; margin: 0.1em 0 0.3em; }
.nt-at-grid { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 1em; align-items: start; }
@media (max-width: 640px) { .nt-at-grid { grid-template-columns: 1fr; } }
.nt-at-info p { margin: 0.25em 0 !important; }
.nt-at-ctrl { display: grid; grid-template-columns: auto auto auto auto; gap: 0.4em 0.6em; align-items: center; justify-content: center; margin: 0.6em 0; }
.nt-at-ctrl .nt-btn { padding: 0.15em 0.8em; min-width: 2.4em; }
.nt-at-ctrl b { min-width: 1.6em; text-align: center; }
.nt-at-ctrl .p { color: #E11D48; } .nt-at-ctrl .n { color: #16A34A; } .nt-at-ctrl .e { color: #2563EB; }
.nt-at-defi { text-align: center; margin: 0.4em 0 0; }
.nt-tab-leg { display: flex; flex-wrap: wrap; gap: 0.4em 1.2em; justify-content: center; font-size: 0.9em; margin: 0.4em 0; }
.nt-tab-leg i { display: inline-block; width: 0.95em; height: 0.95em; border-radius: 3px; margin-right: 0.35em; vertical-align: -0.12em; border: 1px solid rgba(100,116,139,.45); }
.nt-tab-fiche { text-align: center; }
.nt-tab-fiche p { margin: 0.2em 0 !important; }
.nt-mol3d { background: #fff; border-radius: 10px; border: 1px solid var(--line); }
.nt-molrow { display: flex; flex-wrap: wrap; gap: 1.2em; justify-content: center; align-items: center; margin: 1em 0; }
.nt-molrow figure { margin: 0; text-align: center; }
.nt-molrow figcaption { font-size: 0.88em; color: var(--muted); margin-top: 0.4em; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## La taille de l'atome et de son noyau {.nt-h2}

<p class="nt-lead">Pour exprimer des longueurs aussi petites, on utilise des sous-multiples du mètre&nbsp;:</p>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Préfixe</th><th>Symbole</th><th>Valeur</th><th>Exemple</th></tr></thead>
<tbody>
<tr><td>milli</td><td>m</td><td>$\pu{E-3}$</td><td>1&nbsp;mm = $\pu{E-3 m}$</td></tr>
<tr><td>micro</td><td>µ</td><td>$\pu{E-6}$</td><td>1&nbsp;µm = $\pu{E-6 m}$</td></tr>
<tr><td>nano</td><td>n</td><td>$\pu{E-9}$</td><td>1&nbsp;nm = $\pu{E-9 m}$</td></tr>
<tr><td>pico</td><td>p</td><td>$\pu{E-12}$</td><td>1&nbsp;pm = $\pu{E-12 m}$</td></tr>
<tr><td>femto</td><td>f</td><td>$\pu{E-15}$</td><td>1&nbsp;fm = $\pu{E-15 m}$</td></tr>
</tbody>
</table>
</div>
<p class="nt-note">D'un sous-multiple au suivant, on divise par 1&nbsp;000.</p>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-ruler"></i>Taille d'un atome</p>
<p class="nt-f-math">$$\pu{0,1 nm} = \pu{E-10 m}$$</p>
<div class="nt-f-units"><span>ordre de grandeur</span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-ruler"></i>Taille d'un noyau</p>
<p class="nt-f-math">$$\pu{1 fm} = \pu{E-15 m}$$</p>
<div class="nt-f-units"><span>ordre de grandeur</span></div>
</div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Le noyau est donc environ <span class="imp nt-hole">100&nbsp;000 fois</span> plus petit que l'atome.</li>
<li>Si l'atome avait la taille d'un stade, son noyau serait une <span class="imp nt-hole">tête d'épingle</span>.</li>
<li>L'atome est essentiellement fait de <span class="imp nt-hole">vide</span>&nbsp;: entre le noyau et les électrons, il n'y a rien.</li>
</ul>
</div>

{{< youtube-plus id="7WhRJV_bAiE" ratio="16x9" width="500" shadow=true rounded=true >}}

<div class="nt-lab" id="lab-echelle">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Du cheveu au noyau&nbsp;: l'échelle des tailles</p>
<canvas style="height:220px;" aria-label="Une règle graduée en puissances de dix, de 1 mètre à 10 puissance moins 16 mètre, sur laquelle sont placés un cheveu, un globule rouge, une bactérie, un virus, une molécule d'eau, un atome et un noyau"></canvas>
<div class="nt-btns">
<button type="button" class="nt-btn" data-obj="0">cheveu</button>
<button type="button" class="nt-btn" data-obj="1">globule rouge</button>
<button type="button" class="nt-btn" data-obj="2">bactérie</button>
<button type="button" class="nt-btn" data-obj="3">virus</button>
<button type="button" class="nt-btn" data-obj="4">molécule d'eau</button>
<button type="button" class="nt-btn" data-obj="5">atome</button>
<button type="button" class="nt-btn" data-obj="6">noyau</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### Comment sait-on que l'atome est essentiellement vide&nbsp;? {.nt-h3}

<p class="nt-lead">En 1909, sous la direction d'Ernest Rutherford, Hans Geiger et Ernest Marsden bombardent une très fine feuille d'or avec des particules α (des noyaux d'hélium), et observent où elles arrivent. Presque toutes traversent la feuille sans être déviées&nbsp;: elles ne rencontrent rien. Mais quelques rares particules sont fortement déviées, et certaines rebondissent même vers l'arrière&nbsp;! Rutherford en conclut en 1911 que la charge positive et presque toute la masse de l'atome sont concentrées dans un noyau minuscule.</p>

<div class="nt-lab" id="lab-rutherford">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'expérience de Rutherford</p>
<canvas style="height:300px;" aria-label="Des particules alpha sont envoyées sur une feuille d'or ; la plupart la traversent sans déviation, quelques-unes passent près d'un noyau et sont déviées, très rarement vers l'arrière"></canvas>
<div class="nt-read" aria-live="polite"><span>traversent sans déviation&nbsp;: <b class="out-0"></b></span><span>déviées&nbsp;: <b class="out-1"></b></span><span>renvoyées vers l'arrière&nbsp;: <b class="out-2"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
<button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Remettre les compteurs à zéro</button>
</div>
<p class="nt-note">Une particule n'est fortement déviée que si elle passe tout près d'un noyau. Pour que l'animation soit lisible, les noyaux y sont dessinés bien plus gros qu'en réalité&nbsp;: dans l'expérience, à peine une particule sur 8&nbsp;000 était renvoyée vers l'arrière.</p>
</div>

## Le modèle de l'atome {.nt-h2}

<div class="nt-svgbox" style="max-width:640px;"><svg class='nt-svg' viewBox='0 0 640 320' role='img' aria-label="Modèle de l'atome : un nuage électronique formé d'électrons, chargés négativement, entoure un noyau minuscule ; le zoom montre que le noyau est formé de protons, chargés positivement, et de neutrons, de charge nulle, serrés les uns contre les autres. Le dessin n'est pas à l'échelle."><defs><radialGradient id='gNuage' cx='.5' cy='.5' r='.5'><stop offset='0' stop-color='#93C5FD' stop-opacity='.75'/><stop offset='.55' stop-color='#BFDBFE' stop-opacity='.45'/><stop offset='1' stop-color='#DBEAFE' stop-opacity='0'/></radialGradient><radialGradient id='gP' cx='.35' cy='.32' r='.75'><stop offset='0' stop-color='#FECDD3'/><stop offset='.45' stop-color='#FB7185'/><stop offset='1' stop-color='#BE123C'/></radialGradient><radialGradient id='gN' cx='.35' cy='.32' r='.75'><stop offset='0' stop-color='#DCFCE7'/><stop offset='.45' stop-color='#4ADE80'/><stop offset='1' stop-color='#15803D'/></radialGradient><radialGradient id='gZoom' cx='.5' cy='.5' r='.5'><stop offset='0' stop-color='#FFFBEB'/><stop offset='1' stop-color='#FEF3C7'/></radialGradient></defs><circle cx='165' cy='158' r='132' fill='url(#gNuage)'/><circle cx='224.2' cy='176.3' r='6' fill='#2563EB'/><line x1='221.2' y1='176.3' x2='227.2' y2='176.3' stroke='#fff' stroke-width='1.8' stroke-linecap='round'/><circle cx='181.7' cy='254.6' r='6' fill='#2563EB'/><line x1='178.7' y1='254.6' x2='184.7' y2='254.6' stroke='#fff' stroke-width='1.8' stroke-linecap='round'/><circle cx='130.4' cy='196.8' r='6' fill='#2563EB'/><line x1='127.4' y1='196.8' x2='133.4' y2='196.8' stroke='#fff' stroke-width='1.8' stroke-linecap='round'/><circle cx='76.1' cy='143.8' r='6' fill='#2563EB'/><line x1='73.1' y1='143.8' x2='79.1' y2='143.8' stroke='#fff' stroke-width='1.8' stroke-linecap='round'/><circle cx='136.9' cy='93.9' r='6' fill='#2563EB'/><line x1='133.9' y1='93.9' x2='139.9' y2='93.9' stroke='#fff' stroke-width='1.8' stroke-linecap='round'/><circle cx='231.0' cy='77.6' r='6' fill='#2563EB'/><line x1='228.0' y1='77.6' x2='234.0' y2='77.6' stroke='#fff' stroke-width='1.8' stroke-linecap='round'/><circle cx='165' cy='158' r='4.5' fill='#F59E0B'/><line x1='169' y1='154' x2='445' y2='62' stroke='#CBD5E1' stroke-width='1' stroke-dasharray='4 3'/><line x1='169' y1='162' x2='445' y2='254' stroke='#CBD5E1' stroke-width='1' stroke-dasharray='4 3'/><circle cx='520' cy='158' r='100' fill='url(#gZoom)' stroke='#F59E0B' stroke-width='1.5'/><circle cx='498.2' cy='120.2' r='17' fill='url(#gN)' stroke='#fff' stroke-width='1'/><circle cx='525.0' cy='115.6' r='17' fill='url(#gP)' stroke='#fff' stroke-width='1'/><line x1='517.9' y1='115.6' x2='532.1' y2='115.6' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><line x1='525.0' y1='108.5' x2='525.0' y2='122.8' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><circle cx='489.0' cy='145.6' r='17' fill='url(#gN)' stroke='#fff' stroke-width='1'/><circle cx='515.7' cy='140.8' r='17' fill='url(#gN)' stroke='#fff' stroke-width='1'/><circle cx='542.4' cy='136.5' r='17' fill='url(#gN)' stroke='#fff' stroke-width='1'/><circle cx='480.0' cy='171.0' r='17' fill='url(#gP)' stroke='#fff' stroke-width='1'/><line x1='472.8' y1='171.0' x2='487.1' y2='171.0' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><line x1='480.0' y1='163.9' x2='480.0' y2='178.1' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><circle cx='506.5' cy='166.1' r='17' fill='url(#gP)' stroke='#fff' stroke-width='1'/><line x1='499.3' y1='166.1' x2='513.6' y2='166.1' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><line x1='506.5' y1='158.9' x2='506.5' y2='173.2' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><circle cx='533.1' cy='161.8' r='17' fill='url(#gP)' stroke='#fff' stroke-width='1'/><line x1='526.0' y1='161.8' x2='540.3' y2='161.8' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><line x1='533.1' y1='154.6' x2='533.1' y2='168.9' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><circle cx='559.8' cy='157.1' r='17' fill='url(#gP)' stroke='#fff' stroke-width='1'/><line x1='552.7' y1='157.1' x2='566.9' y2='157.1' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><line x1='559.8' y1='149.9' x2='559.8' y2='164.2' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><circle cx='497.0' cy='191.5' r='17' fill='url(#gN)' stroke='#fff' stroke-width='1'/><circle cx='523.3' cy='187.2' r='17' fill='url(#gP)' stroke='#fff' stroke-width='1'/><line x1='516.2' y1='187.2' x2='530.5' y2='187.2' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><line x1='523.3' y1='180.1' x2='523.3' y2='194.3' stroke='#fff' stroke-width='2.2' stroke-linecap='round'/><circle cx='550.1' cy='182.7' r='17' fill='url(#gN)' stroke='#fff' stroke-width='1'/><text x='165' y='20' font-size='13' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>nuage électronique</text><text x='165' y='36' font-size='11.5' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif'>des électrons, de charge négative</text><text x='165' y='308' font-size='12' text-anchor='middle' fill='#B45309' font-family='system-ui, sans-serif' font-weight='700'>noyau, au centre (minuscule)</text><text x='520' y='36' font-size='13' text-anchor='middle' fill='#B45309' font-family='system-ui, sans-serif' font-weight='700'>le noyau, très agrandi</text><circle cx='446' cy='284' r='8' fill='url(#gP)'/><text x='460' y='288' font-size='12' text-anchor='start' fill='#E11D48' font-family='system-ui, sans-serif'>proton : charge positive</text><circle cx='446' cy='304' r='8' fill='url(#gN)'/><text x='460' y='308' font-size='12' text-anchor='start' fill='#16A34A' font-family='system-ui, sans-serif'>neutron : charge nulle</text></svg></div>
<p class="nt-cap">Le modèle de l'atome. Le dessin n'est pas à l'échelle.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Le modèle de l'atome</p>
<p>L'atome est constitué d'un <span class="imp nt-hole">nuage électronique</span> entourant son <span class="imp nt-hole">noyau</span>.</p>
<ul class="nt-facts">
<li>Le nuage électronique est constitué d'<span class="imp nt-hole">électrons</span>, des particules élémentaires ponctuelles portant une charge <span class="imp nt-hole">négative</span>. Il est entièrement responsable de la <span class="imp nt-hole">taille</span> de l'atome.</li>
<li>Le noyau est composé de <span class="imp nt-hole">protons</span>, des particules portant une charge <span class="imp nt-hole">positive</span>, et de <span class="imp nt-hole">neutrons</span>, des particules de charge <span class="imp nt-hole">nulle</span>. Protons et neutrons sont des <span class="imp nt-hole">nucléons</span>.</li>
</ul>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Particule</th><th>Charge</th><th>Masse</th></tr></thead>
<tbody>
<tr><td>électron</td><td>$\pu{-1,6E-19 C}$</td><td>$\pu{9,1E-31 kg}$</td></tr>
<tr><td>proton</td><td>$\pu{+1,6E-19 C}$</td><td>$\pu{1,7E-27 kg}$</td></tr>
<tr><td>neutron</td><td>$\pu{0 C}$</td><td>$\pu{1,7E-27 kg}$</td></tr>
</tbody>
</table>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>La charge électrique élémentaire</p>
<p>La charge d'un proton est la plus petite charge électrique qu'un objet isolé puisse porter&nbsp;: c'est la <span class="imp">charge électrique élémentaire</span>, notée <span class="imp nt-hole">e</span>, avec $e = \pu{1,6E-19 C}$. Un proton porte la charge $+e$, un électron la charge $-e$.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Que remarquez-vous, concernant les charges, puis concernant les masses&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>Les charges</b>&nbsp;: la charge d'un proton est parfaitement <b>opposée</b> à celle d'un électron. Or un atome est électriquement <b>neutre</b>&nbsp;: il contient donc autant d'électrons que de protons.</li>
<li><b>Les masses</b>&nbsp;: protons et neutrons ont quasiment la même masse, environ <b>2&nbsp;000 fois</b> plus grande que celle d'un électron ($\dfrac{\pu{1,7E-27}}{\pu{9,1E-31}} \approx 1\,900$). Le <b>noyau</b> porte donc la quasi-totalité de la masse de l'atome.</li>
</ul>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Un atome est <b>électriquement</b> <span class="imp nt-hole">neutre</span>&nbsp;: il contient <b>autant</b> d'<span class="imp nt-hole">électrons</span> que de <span class="imp nt-hole">protons</span>.</li>
<li>Le <span class="imp nt-hole">noyau</span> porte la quasi-totalité de la <b>masse</b> de l'atome, alors que le <span class="imp nt-hole">nuage électronique</span> en fait la <b>taille</b>.</li>
</ul>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Masse d'un atome</p>
<p class="nt-f-math">$$m_\text{atome} \approx m_\text{noyau} \approx A\times m_\text{nucléon}$$</p>
<div class="nt-f-units"><span>$A$, le nombre de nucléons</span><span>$m_\text{nucléon} \approx \pu{1,67E-27 kg}$</span></div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice&nbsp;: comparer la masse d'un atome et celle de son noyau</p>
<p>Un atome de carbone 12 contient 6 protons, 6 neutrons et 6 électrons. Calculer la masse de son noyau, puis celle de ses électrons. Quelle part de la masse de l'atome les électrons représentent-ils&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li>Noyau&nbsp;: $m_\text{noyau} \approx 12 \times \pu{1,67E-27} \approx \pu{2,0E-26 kg}$.</li>
<li>Électrons&nbsp;: $m_\text{électrons} = 6 \times \pu{9,1E-31} \approx \pu{5,5E-30 kg}$.</li>
<li>Rapport&nbsp;: $\dfrac{m_\text{électrons}}{m_\text{noyau}} \approx \dfrac{\pu{5,5E-30}}{\pu{2,0E-26}} \approx \pu{2,7E-4}$, soit environ 0,03&nbsp;%.</li>
</ul>
<p>Les électrons représentent moins d'un trois-millième de la masse de l'atome&nbsp;: la masse de l'atome est bien, à très peu près, celle de son noyau. Pourtant, l'atome est environ 100&nbsp;000 fois plus grand que son noyau.</p>
</div>
</details>

<div class="nt-lab" id="lab-atome">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Construire un atome, puis un ion</p>
<div class="nt-at-grid">
<div>
<canvas style="height:280px;" aria-label="L'atome construit : un noyau de protons et de neutrons, entouré d'un nuage d'électrons"></canvas>
<div class="nt-at-ctrl">
<span class="p"><b>protons</b></span><button type="button" class="nt-btn" data-sub="p" aria-label="Retirer un proton">−</button><b class="p" data-cnt="p">0</b><button type="button" class="nt-btn" data-add="p" aria-label="Ajouter un proton">+</button>
<span class="n"><b>neutrons</b></span><button type="button" class="nt-btn" data-sub="n" aria-label="Retirer un neutron">−</button><b class="n" data-cnt="n">0</b><button type="button" class="nt-btn" data-add="n" aria-label="Ajouter un neutron">+</button>
<span class="e"><b>électrons</b></span><button type="button" class="nt-btn" data-sub="e" aria-label="Retirer un électron">−</button><b class="e" data-cnt="e">0</b><button type="button" class="nt-btn" data-add="e" aria-label="Ajouter un électron">+</button>
</div>
</div>
<div class="nt-at-info" aria-live="polite"></div>
</div>
<p class="nt-at-defi"></p>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="defi"><i class="fa-solid fa-flag"></i>&nbsp; Défi suivant</button>
<button type="button" class="nt-btn" data-act="vide"><i class="fa-solid fa-rotate-left"></i>&nbsp; Tout retirer</button>
</div>
</div>

## Les ions {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un <span class="imp">ion</span> est un atome ou un assemblage d'atomes qui a <span class="imp nt-hole">gagné</span> ou <span class="imp nt-hole">perdu</span> un ou plusieurs <span class="imp nt-hole">électrons</span>.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Comme les atomes et les molécules sont électriquement <span class="imp nt-hole">neutres</span>, les ions sont <span class="imp nt-hole">chargés</span>&nbsp;:</p>
<ul class="nt-facts">
<li><span class="imp nt-hole">négativement</span> pour les <span class="imp nt-hole">anions</span>, qui ont <b>gagné</b> des électrons&nbsp;;</li>
<li><span class="imp nt-hole">positivement</span> pour les <span class="imp nt-hole">cations</span>, qui ont <b>perdu</b> des électrons.</li>
</ul>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li>Ions monoatomiques&nbsp;: l'ion sodium $\ce{Na+}$ (un électron perdu), l'ion cuivre II $\ce{Cu^2+}$ (deux électrons perdus), l'ion chlorure $\ce{Cl-}$ (un électron gagné), l'ion oxyde $\ce{O^2-}$ (deux électrons gagnés).</li>
<li>Ions polyatomiques&nbsp;: l'ion hydroxyde $\ce{HO-}$, l'ion sulfate $\ce{SO4^2-}$, l'ion ammonium $\ce{NH4+}$.</li>
</ul>
<p>La charge s'écrit en exposant, en multiples de la charge élémentaire $e = \pu{1,6E-19 C}$&nbsp;: $\ce{Cu^2+}$ porte la charge $+2e$.</p>
</div>

## Les molécules {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp">molécule</span> est une entité électriquement <span class="imp nt-hole">neutre</span> comprenant <span class="imp nt-hole">plus d'un atome</span>.</p>
</div>

<p class="nt-lead">Exemple&nbsp;: le saccharose (le sucre de table), de formule $\ce{C12H22O11}$. Chaque molécule compte 12 atomes de carbone, 22 atomes d'hydrogène et 11 atomes d'oxygène, soit 45 atomes.</p>

<div class="nt-molrow">
<figure><div class="nt-svgbox" style="max-width:360px; margin:0;"><svg xmlns='http://www.w3.org/2000/svg' class='nt-mol' role='img' viewBox='0 0 288 147' width='288' height='147'><line x1='33.6' y1='88.3' x2='51.0' y2='97.0' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='51.0' y1='97.0' x2='74.4' y2='81.6' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='74.4' y1='81.6' x2='92.7' y2='88.5' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='105.9' y1='84.8' x2='118.1' y2='69.6' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='118.1' y1='69.6' x2='136.1' y2='88.9' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='136.1' y1='88.9' x2='129.7' y2='107.3' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='118.1' y1='69.6' x2='133.3' y2='57.3' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='147.9' y1='55.0' x2='166.0' y2='61.7' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='166.0' y1='61.7' x2='181.0' y2='49.3' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='195.5' y1='46.9' x2='213.8' y2='53.7' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='213.8' y1='53.7' x2='235.4' y2='35.9' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='235.4' y1='35.9' x2='253.7' y2='42.8' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='213.8' y1='53.7' x2='218.4' y2='81.3' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='218.4' y1='81.3' x2='236.7' y2='88.1' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='218.4' y1='81.3' x2='196.9' y2='99.1' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='196.9' y1='99.1' x2='200.1' y2='118.3' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='196.9' y1='99.1' x2='170.7' y2='89.3' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='170.7' y1='89.3' x2='160.5' y2='98.8' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='118.1' y1='69.6' x2='102.7' y2='46.2' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='102.7' y1='46.2' x2='109.6' y2='28.0' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='102.7' y1='46.2' x2='75.7' y2='53.6' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='75.7' y1='53.6' x2='60.5' y2='41.4' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='75.7' y1='53.6' x2='74.4' y2='81.6' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><line x1='170.7' y1='89.3' x2='166.0' y2='61.7' stroke='#1E293B' stroke-width='1' stroke-linecap='round'/><text x='26.0' y='89.4' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='20.4' y='89.4' font-size='15' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif'>H</text><text x='100.6' y='96.5' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='126.9' y='120.3' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='121.3' y='120.3' font-size='15' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif'>H</text><text x='139.9' y='57.0' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='187.5' y='48.9' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='261.7' y='50.8' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='267.2' y='50.8' font-size='15' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif'>H</text><text x='244.7' y='96.1' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='250.2' y='96.1' font-size='15' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif'>H</text><text x='201.5' y='131.7' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='207.1' y='131.7' font-size='15' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif'>H</text><text x='154.3' y='109.6' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='148.7' y='109.6' font-size='15' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif'>H</text><text x='112.6' y='25.0' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='118.1' y='25.0' font-size='15' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif'>H</text><text x='53.9' y='41.1' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif'>O</text><text x='48.3' y='41.1' font-size='15' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif'>H</text></svg></div><figcaption>la formule topologique du saccharose</figcaption></figure>
<figure><div class="nt-mol3d" data-mol="saccharose" style="width:320px; max-width:100%; height:260px;" role="img" aria-label="Modèle moléculaire du saccharose, en trois dimensions"></div><figcaption>son modèle moléculaire&nbsp;: faites-le tourner&nbsp;!<br>(carbone en gris foncé, oxygène en rouge, hydrogène en blanc)</figcaption></figure>
</div>

## L'élément chimique {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Le noyau renferme l'identité de l'atome</p>
<ul class="nt-facts">
<li>Son <span class="imp nt-hole">nombre de nucléons</span>, noté <span class="imp nt-hole">A</span>, permet de déterminer approximativement sa masse. On appelle aussi $A$ le <span class="imp nt-hole">nombre de masse</span>.</li>
<li>Son <span class="imp nt-hole">nombre de protons</span>, noté <span class="imp nt-hole">Z</span> et appelé <span class="imp nt-hole">numéro atomique</span>, fixe le nombre d'électrons de l'atome, et ainsi toutes ses propriétés chimiques.</li>
</ul>
<p>À un numéro atomique correspond un <span class="imp nt-hole">symbole chimique</span> unique, fait d'une majuscule parfois suivie d'une minuscule. Il désigne l'élément chimique.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Élément chimique</p>
<p>Un <span class="imp">élément chimique</span> est l'ensemble des atomes (isolés ou engagés dans un édifice polyatomique neutre ou chargé) et des ions monoatomiques comportant un même <span class="imp nt-hole">nombre de protons</span> dans leur noyau.</p>
</div>

{{< youtube-plus id="p6ek7RhZXv8" ratio="16x9" width="500" shadow=true rounded=true >}}

<div class="nt-svgbox" style="max-width:600px;"><svg class='nt-svg' viewBox='0 0 660 350' role='img' aria-label="Le cycle du cuivre, en six étapes : le cuivre métallique réagit avec l'acide nitrique pour donner l'ion cuivre II ; la soude le précipite en hydroxyde de cuivre ; le chauffage donne l'oxyde de cuivre ; l'acide sulfurique redonne l'ion cuivre II ; l'ammoniac forme l'ion tétraammine cuivre II ; le magnésium redonne le cuivre métallique. L'élément cuivre se conserve à chaque étape."><line x1='202.0' y1='76.0' x2='224.0' y2='76.0' stroke='#94A3B8' stroke-width='2'/><polygon points='232.0,76.0 222.0,80.5 222.0,71.5' fill='#94A3B8'/><line x1='428.0' y1='76.0' x2='450.0' y2='76.0' stroke='#94A3B8' stroke-width='2'/><polygon points='458.0,76.0 448.0,80.5 448.0,71.5' fill='#94A3B8'/><line x1='556.0' y1='114.0' x2='556.0' y2='230.0' stroke='#94A3B8' stroke-width='2'/><polygon points='556.0,238.0 551.5,228.0 560.5,228.0' fill='#94A3B8'/><line x1='458.0' y1='276.0' x2='436.0' y2='276.0' stroke='#94A3B8' stroke-width='2'/><polygon points='428.0,276.0 438.0,271.5 438.0,280.5' fill='#94A3B8'/><line x1='232.0' y1='276.0' x2='210.0' y2='276.0' stroke='#94A3B8' stroke-width='2'/><polygon points='202.0,276.0 212.0,271.5 212.0,280.5' fill='#94A3B8'/><line x1='104.0' y1='238.0' x2='104.0' y2='122.0' stroke='#94A3B8' stroke-width='2'/><polygon points='104.0,114.0 108.5,124.0 99.5,124.0' fill='#94A3B8'/><rect x='160.0' y='15.0' width='114.0' height='20' rx='10' fill='#F5F3FF' stroke='#C4B5FD'/><text x='217.0' y='29.5' font-size='11.5' text-anchor='middle' fill='#6D28D9' font-family='system-ui, sans-serif' font-weight='600'>acide nitrique</text><rect x='417.5' y='15.0' width='51.0' height='20' rx='10' fill='#F5F3FF' stroke='#C4B5FD'/><text x='443.0' y='29.5' font-size='11.5' text-anchor='middle' fill='#6D28D9' font-family='system-ui, sans-serif' font-weight='600'>soude</text><rect x='566.0' y='163.0' width='79.0' height='20' rx='10' fill='#F5F3FF' stroke='#C4B5FD'/><text x='605.5' y='177.5' font-size='11.5' text-anchor='middle' fill='#6D28D9' font-family='system-ui, sans-serif' font-weight='600'>chauffage</text><rect x='379.0' y='319.0' width='128.0' height='20' rx='10' fill='#F5F3FF' stroke='#C4B5FD'/><text x='443.0' y='333.5' font-size='11.5' text-anchor='middle' fill='#6D28D9' font-family='system-ui, sans-serif' font-weight='600'>acide sulfurique</text><rect x='181.0' y='319.0' width='72.0' height='20' rx='10' fill='#F5F3FF' stroke='#C4B5FD'/><text x='217.0' y='333.5' font-size='11.5' text-anchor='middle' fill='#6D28D9' font-family='system-ui, sans-serif' font-weight='600'>ammoniac</text><rect x='114.0' y='163.0' width='79.0' height='20' rx='10' fill='#F5F3FF' stroke='#C4B5FD'/><text x='153.5' y='177.5' font-size='11.5' text-anchor='middle' fill='#6D28D9' font-family='system-ui, sans-serif' font-weight='600'>magnésium</text><rect x='10.0' y='42.0' width='188' height='68' rx='12' fill='#fff' stroke='#B45309' stroke-width='2'/><text x='104.0' y='68.0' font-size='18' text-anchor='middle' fill='#B45309' font-family='Georgia, serif' font-weight='700'>Cu</text><text x='104.0' y='86.0' font-size='11.5' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='600'>cuivre métallique</text><text x='104.0' y='101.0' font-size='10.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>métal rouge-orangé</text><rect x='236.0' y='42.0' width='188' height='68' rx='12' fill='#fff' stroke='#2563EB' stroke-width='2'/><text x='330.0' y='68.0' font-size='18' text-anchor='middle' fill='#2563EB' font-family='Georgia, serif' font-weight='700'>Cu²⁺</text><text x='330.0' y='86.0' font-size='11.5' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='600'>ion cuivre II</text><text x='330.0' y='101.0' font-size='10.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>solution bleue</text><rect x='462.0' y='42.0' width='188' height='68' rx='12' fill='#fff' stroke='#3B82F6' stroke-width='2'/><text x='556.0' y='68.0' font-size='18' text-anchor='middle' fill='#3B82F6' font-family='Georgia, serif' font-weight='700'>Cu(OH)₂</text><text x='556.0' y='86.0' font-size='11.5' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='600'>hydroxyde de cuivre</text><text x='556.0' y='101.0' font-size='10.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>précipité bleu</text><rect x='462.0' y='242.0' width='188' height='68' rx='12' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='556.0' y='268.0' font-size='18' text-anchor='middle' fill='#1E293B' font-family='Georgia, serif' font-weight='700'>CuO</text><text x='556.0' y='286.0' font-size='11.5' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='600'>oxyde de cuivre</text><text x='556.0' y='301.0' font-size='10.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>solide noir</text><rect x='236.0' y='242.0' width='188' height='68' rx='12' fill='#fff' stroke='#2563EB' stroke-width='2'/><text x='330.0' y='268.0' font-size='18' text-anchor='middle' fill='#2563EB' font-family='Georgia, serif' font-weight='700'>Cu²⁺</text><text x='330.0' y='286.0' font-size='11.5' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='600'>ion cuivre II</text><text x='330.0' y='301.0' font-size='10.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>solution bleue</text><rect x='10.0' y='242.0' width='188' height='68' rx='12' fill='#fff' stroke='#1D4ED8' stroke-width='2'/><text x='104.0' y='268.0' font-size='18' text-anchor='middle' fill='#1D4ED8' font-family='Georgia, serif' font-weight='700'>[Cu(NH₃)₄]²⁺</text><text x='104.0' y='286.0' font-size='11.5' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='600'>ion tétraammine cuivre II</text><text x='104.0' y='301.0' font-size='10.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>solution bleu céleste</text><ellipse cx='330' cy='176.0' rx='86' ry='40' fill='#FEF3C7'/><text x='330.0' y='170.0' font-size='13' text-anchor='middle' fill='#B45309' font-family='system-ui, sans-serif' font-weight='800'>l'élément cuivre</text><text x='330.0' y='188.0' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, sans-serif' font-weight='700'>se conserve</text></svg></div>
<p class="nt-cap">Le cycle du cuivre, dans l'ordre de la vidéo. L'ion tétraammine cuivre II, $\ce{[Cu(NH3)4]^2+}$, est un ion polyatomique&nbsp;: un ion cuivre II associé à quatre molécules d'ammoniac $\ce{NH3}$.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les manipulations du cycle, étape par étape</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p><b>Cuivre + acide nitrique.</b> Le métal est attaqué et disparaît&nbsp;: le cuivre passe en solution sous forme d'ions cuivre II, $\ce{Cu^2+}$. Il se dégage des vapeurs rousses de dioxyde d'azote, toxique&nbsp;: la manipulation se fait sous la hotte.</p></li>
<li><p><b>Ajout d'eau distillée.</b> On dilue la solution, qui prend la couleur bleue caractéristique des ions cuivre II. Le cuivre n'est pas transformé.</p></li>
<li><p><b>Ajout de soude</b> (une solution d'hydroxyde de sodium). Les ions hydroxyde $\ce{HO-}$ s'associent aux ions cuivre II&nbsp;: il se forme un précipité bleu d'hydroxyde de cuivre, $\ce{Cu(OH)2}$, un solide qui ne se dissout pas dans l'eau.</p></li>
<li><p><b>Chauffage.</b> L'hydroxyde de cuivre perd de l'eau et se transforme en oxyde de cuivre, $\ce{CuO}$, un solide noir.</p></li>
<li><p><b>Rinçages et décantations.</b> On laisse l'oxyde de cuivre se déposer, on retire le liquide, puis on rince à l'eau&nbsp;: on élimine ainsi les ions restés en solution (sodium, nitrate). Le cuivre n'est pas transformé.</p></li>
<li><p><b>Ajout d'acide sulfurique.</b> L'oxyde de cuivre se dissout&nbsp;: on retrouve des ions cuivre II en solution, bleue.</p></li>
<li><p><b>Ajout d'ammoniac.</b> Les molécules d'ammoniac $\ce{NH3}$ s'associent aux ions cuivre II pour former l'ion polyatomique tétraammine cuivre II, $\ce{[Cu(NH3)4]^2+}$&nbsp;: la solution devient d'un bleu céleste intense.</p></li>
<li><p><b>Chauffage jusqu'à ébullition.</b> La solution garde le même aspect&nbsp;: l'ion tétraammine cuivre II est stable, il ne se décompose pas.</p></li>
<li><p><b>Ajout de magnésium</b>, en continuant de chauffer doucement. Le magnésium est un métal plus «&nbsp;réactif&nbsp;» que le cuivre&nbsp;: il cède des électrons aux ions cuivre II, qui redeviennent du cuivre métallique. Un dépôt rouge-orangé de cuivre apparaît, et la solution se décolore peu à peu.</p></li>
<li><p><b>Ajout d'acide chlorhydrique.</b> Il dissout le magnésium en excès (avec un dégagement de dihydrogène), mais pas le cuivre. On isole ainsi le cuivre métallique&nbsp;: le cycle est bouclé.</p></li>
</ol>
<p class="nt-note">Si toutes les étapes sont soignées, on récupère presque toute la masse de cuivre de départ&nbsp;: il ne s'est ni créé ni perdu de cuivre, il a seulement changé de forme.</p>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le cuivre n'a jamais disparu&nbsp;: la preuve, on le retrouve à la fin. Son noyau n'est jamais modifié par les transformations chimiques&nbsp;; seul son <span class="imp nt-hole">nuage électronique</span> l'est. L'identité de l'élément cuivre est gardée en son cœur, dans les <span class="imp nt-hole">29 protons</span> de son noyau.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Le rêve des alchimistes</p>
<p>Le rêve des alchimistes, transformer le plomb en or, était donc voué à l'échec&nbsp;: aucune réaction chimique ne sera jamais capable de modifier un élément. Seules les <span class="imp nt-hole">réactions nucléaires</span>, beaucoup plus énergétiques, le peuvent.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Transformer du plomb en or… avec un accélérateur de particules</span></summary>
<div class="nt-d-body">
<p>Le rêve des alchimistes a fini par être réalisé, mais par la physique nucléaire. En 1980, l'équipe de Glenn Seaborg, à Berkeley, a transformé quelques milliers d'atomes de bismuth en or, dans un accélérateur de particules. En 2025, l'expérience ALICE du Grand collisionneur de hadrons (LHC), au CERN, a observé la transformation de noyaux de plomb en noyaux d'or&nbsp;: lors de collisions frôlantes, un noyau de plomb ($Z = 82$) peut perdre trois protons et devenir un noyau d'or ($Z = 79$). Les quantités produites sont infimes, de l'ordre du milliardième de milligramme, et ces noyaux se brisent presque aussitôt&nbsp;: aucune fortune à faire&nbsp;!</p>
</div>
</details>

### Le tableau périodique {.nt-h3}

<p class="nt-lead">Tous les éléments connus sont répertoriés dans le <span class="imp">tableau périodique des éléments</span>. Sa première version a été conçue par le chimiste russe Dmitri Mendeleïev, en 1869. Le tableau contient aujourd'hui 118 éléments.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les cases vides de Mendeleïev</span></summary>
<div class="nt-d-body">
<p>Le coup de génie de Mendeleïev fut de laisser des cases vides dans son tableau, là où les propriétés des éléments connus ne s'enchaînaient pas. Il prédit l'existence et les propriétés d'éléments encore inconnus, qu'il appela «&nbsp;éka-aluminium&nbsp;» ou «&nbsp;éka-silicium&nbsp;». Ils furent découverts dans les années suivantes&nbsp;: le gallium (1875), le scandium (1879) et le germanium (1886), avec les propriétés annoncées.</p>
</div>
</details>

<div class="nt-lab" id="lab-tableau">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le tableau périodique des éléments</p>
<div class="nt-ctrl">
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="tmode" value="simple" checked><span>les éléments</span></label>
<label><input type="radio" name="tmode" value="etat"><span>état à 25&nbsp;°C</span></label>
<label><input type="radio" name="tmode" value="bloc"><span>blocs</span></label>
<label><input type="radio" name="tmode" value="radio"><span>radioactivité</span></label>
</div>
</div>
<div class="nt-scroll"><canvas style="height:380px; min-width:600px; cursor:pointer;" aria-label="Le tableau périodique des 118 éléments ; cliquez sur un élément pour afficher sa fiche"></canvas></div>
<div class="nt-tab-leg"></div>
<div class="nt-tab-fiche" aria-live="polite"></div>
<p class="nt-note">Cliquez sur un élément pour afficher sa fiche. Le groupe 3 contient le scandium, l'yttrium, le lutécium et le lawrencium, et le bloc f compte quatorze éléments par ligne&nbsp;: c'est la disposition recommandée par l'IUPAC.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Les éléments radioactifs</p>
<p>À partir du polonium ($Z = 84$), tous les éléments sont radioactifs&nbsp;: aucun de leurs isotopes n'est stable. Le bismuth ($Z = 83$) l'est aussi, mais de façon infime&nbsp;: la moitié de ses atomes met environ $\pu{2E19}$ années à se désintégrer, plus d'un milliard de fois l'âge de l'Univers. Deux éléments plus légers sont également radioactifs&nbsp;: le technétium ($Z = 43$) et le prométhium ($Z = 61$).</p>
</div>

## L'écriture conventionnelle d'un noyau {.nt-h2}

<div class="nt-svgbox" style="max-width:640px;"><svg class='nt-svg' viewBox='0 0 640 250' role='img' aria-label="Écriture conventionnelle d'un noyau : le symbole X de l'élément, avec en haut à gauche le nombre de nucléons A et en bas à gauche le numéro atomique Z. Exemple : le cuivre 63, avec A = 63 et Z = 29."><text x='196' y='158' font-size='92' text-anchor='middle' fill='#1E293B' font-family='Georgia, serif'>X</text><text x='146' y='100' font-size='38' text-anchor='end' fill='#7C3AED' font-family='Georgia, serif' font-style='italic'>A</text><text x='146' y='160' font-size='38' text-anchor='end' fill='#E11D48' font-family='Georgia, serif' font-style='italic'>Z</text><text x='110' y='26' font-size='13' text-anchor='middle' fill='#7C3AED' font-family='system-ui, sans-serif' font-weight='700'>nombre de nucléons</text><text x='110' y='42' font-size='11.5' text-anchor='middle' fill='#7C3AED' font-family='system-ui, sans-serif'>(nombre de masse)</text><line x1='116.0' y1='50.0' x2='123.9' y2='63.1' stroke='#7C3AED' stroke-width='1.4'/><polygon points='128.0,70.0 119.0,63.7 126.7,59.1' fill='#7C3AED'/><text x='110' y='220' font-size='13' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='700'>numéro atomique :</text><text x='110' y='236' font-size='11.5' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif'>nombre de protons</text><line x1='116.0' y1='204.0' x2='125.2' y2='179.5' stroke='#E11D48' stroke-width='1.4'/><polygon points='128.0,172.0 128.7,182.9 120.3,179.8' fill='#E11D48'/><line x1='240.0' y1='124.0' x2='274.0' y2='124.0' stroke='#1E293B' stroke-width='1.4'/><polygon points='282.0,124.0 272.0,128.5 272.0,119.5' fill='#1E293B'/><text x='354' y='112' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>symbole de l'élément</text><text x='354' y='128' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>une majuscule, parfois</text><text x='354' y='143' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>suivie d'une minuscule</text><rect x='466' y='44' width='160' height='160' rx='14' fill='#F8FAFC' stroke='#CBD5E1'/><text x='546' y='66' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif' font-weight='600'>exemple</text><text x='520' y='112' font-size='24' text-anchor='end' fill='#7C3AED' font-family='Georgia, serif'>63</text><text x='520' y='152' font-size='24' text-anchor='end' fill='#E11D48' font-family='Georgia, serif'>29</text><text x='523' y='149' font-size='54' text-anchor='start' fill='#1E293B' font-family='Georgia, serif'>Cu</text><text x='546' y='188' font-size='11.5' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif'>le cuivre 63</text></svg></div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Comme un numéro atomique n'est associé qu'à un unique symbole chimique, on peut se passer de $Z$ pour déterminer la composition du noyau&nbsp;: il suffit de lire le numéro atomique de l'élément dans le tableau périodique. On écrit ainsi $\ce{^{63}Cu}$ au lieu de $\ce{^{63}_{29}Cu}$.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Comment obtenir le nombre de neutrons $N$ d'un noyau, si l'on connaît $Z$ et $A$&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Nombre de neutrons</p>
<p class="nt-f-math">$$N = A - Z$$</p>
</div>
</div>
</details>


<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les isotopes</span></summary>
<div class="nt-d-body">
<p>Des noyaux qui ont le même nombre de protons, mais pas le même nombre de neutrons, sont des <b>isotopes</b>&nbsp;: ils appartiennent au même élément chimique. Par exemple, $\ce{^{12}_{6}C}$ (6 neutrons) et $\ce{^{14}_{6}C}$ (8 neutrons) sont deux isotopes du carbone&nbsp;; ils ont les mêmes propriétés chimiques. Le carbone 14 est radioactif&nbsp;: c'est lui qui permet de dater les restes d'êtres vivants, jusqu'à environ 50&nbsp;000 ans.</p>
</div>
</details>

<div class="nt-lab nt-trainer" id="lab-noyau">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Noyaux et ions</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<div class="nt-qvis" aria-live="polite"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-zone"><div class="nt-tr-ans"><span class="nt-champ"><label for="at-rep">Réponse&nbsp;:</label><input id="at-rep" type="text" inputmode="numeric"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

## Bilan {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-atome">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">L'atome, les ions et l'élément chimique</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Résumé</p>
<p class="nt-center"><i>Les protons donnent à l'élément son identité, et les électrons sa personnalité.</i></p>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function canvasCtx(cv) { var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight; cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); return { ctx: ctx, w: w, h: h }; }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function watch(cv, cb) { if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }).observe(cv); } else { cb(true); } }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function num(s) { return parseFloat(String(s).replace(',', '.').replace(/\s/g, '')); }
  function bilanTxt(r) { return r === 1 ? 'Parfait&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;!' : (r >= 0.5 ? 'C\u2019est un bon début&nbsp;: relisez les cas manqués.' : 'Relisez le cours, puis recommencez.')); }
  function txt(c, s, x, y, color, font, align) { c.save(); c.font = font || '12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round'; c.lineWidth = 4; c.strokeStyle = 'rgba(255,255,255,.92)'; c.strokeText(s, x, y); c.fillStyle = color; c.fillText(s, x, y); c.restore(); }
  function rr(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
  function pastille(c, s, x, y, col, bg, align) { c.save(); c.font = '700 11.5px system-ui, sans-serif'; var lw = c.measureText(s).width + 14, xx = align === 'right' ? x - lw : (align === 'left' ? x : x - lw / 2); rr(c, xx, y - 13, lw, 19, 9.5); c.fillStyle = bg || '#fff'; c.fill(); c.strokeStyle = col; c.lineWidth = 1.2; c.stroke(); c.fillStyle = col; c.textAlign = 'left'; c.fillText(s, xx + 7, y + 1); c.restore(); }
  function puiss(e) { return '10' + String(e).replace('-', '\u207b').replace(/\d/g, function (d) { return '\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079'[+d]; }); }
  var EL = [["H", "hydrogène", 1, 1, "s", "g", 0], ["He", "hélium", 1, 18, "s", "g", 0], ["Li", "lithium", 2, 1, "s", "s", 0], ["Be", "béryllium", 2, 2, "s", "s", 0], ["B", "bore", 2, 13, "p", "s", 0], ["C", "carbone", 2, 14, "p", "s", 0], ["N", "azote", 2, 15, "p", "g", 0], ["O", "oxygène", 2, 16, "p", "g", 0], ["F", "fluor", 2, 17, "p", "g", 0], ["Ne", "néon", 2, 18, "p", "g", 0], ["Na", "sodium", 3, 1, "s", "s", 0], ["Mg", "magnésium", 3, 2, "s", "s", 0], ["Al", "aluminium", 3, 13, "p", "s", 0], ["Si", "silicium", 3, 14, "p", "s", 0], ["P", "phosphore", 3, 15, "p", "s", 0], ["S", "soufre", 3, 16, "p", "s", 0], ["Cl", "chlore", 3, 17, "p", "g", 0], ["Ar", "argon", 3, 18, "p", "g", 0], ["K", "potassium", 4, 1, "s", "s", 0], ["Ca", "calcium", 4, 2, "s", "s", 0], ["Sc", "scandium", 4, 3, "d", "s", 0], ["Ti", "titane", 4, 4, "d", "s", 0], ["V", "vanadium", 4, 5, "d", "s", 0], ["Cr", "chrome", 4, 6, "d", "s", 0], ["Mn", "manganèse", 4, 7, "d", "s", 0], ["Fe", "fer", 4, 8, "d", "s", 0], ["Co", "cobalt", 4, 9, "d", "s", 0], ["Ni", "nickel", 4, 10, "d", "s", 0], ["Cu", "cuivre", 4, 11, "d", "s", 0], ["Zn", "zinc", 4, 12, "d", "s", 0], ["Ga", "gallium", 4, 13, "p", "s", 0], ["Ge", "germanium", 4, 14, "p", "s", 0], ["As", "arsenic", 4, 15, "p", "s", 0], ["Se", "sélénium", 4, 16, "p", "s", 0], ["Br", "brome", 4, 17, "p", "l", 0], ["Kr", "krypton", 4, 18, "p", "g", 0], ["Rb", "rubidium", 5, 1, "s", "s", 0], ["Sr", "strontium", 5, 2, "s", "s", 0], ["Y", "yttrium", 5, 3, "d", "s", 0], ["Zr", "zirconium", 5, 4, "d", "s", 0], ["Nb", "niobium", 5, 5, "d", "s", 0], ["Mo", "molybdène", 5, 6, "d", "s", 0], ["Tc", "technétium", 5, 7, "d", "s", 2], ["Ru", "ruthénium", 5, 8, "d", "s", 0], ["Rh", "rhodium", 5, 9, "d", "s", 0], ["Pd", "palladium", 5, 10, "d", "s", 0], ["Ag", "argent", 5, 11, "d", "s", 0], ["Cd", "cadmium", 5, 12, "d", "s", 0], ["In", "indium", 5, 13, "p", "s", 0], ["Sn", "étain", 5, 14, "p", "s", 0], ["Sb", "antimoine", 5, 15, "p", "s", 0], ["Te", "tellure", 5, 16, "p", "s", 0], ["I", "iode", 5, 17, "p", "s", 0], ["Xe", "xénon", 5, 18, "p", "g", 0], ["Cs", "césium", 6, 1, "s", "s", 0], ["Ba", "baryum", 6, 2, "s", "s", 0], ["La", "lanthane", 9, 3, "f", "s", 0], ["Ce", "cérium", 9, 4, "f", "s", 0], ["Pr", "praséodyme", 9, 5, "f", "s", 0], ["Nd", "néodyme", 9, 6, "f", "s", 0], ["Pm", "prométhium", 9, 7, "f", "s", 2], ["Sm", "samarium", 9, 8, "f", "s", 0], ["Eu", "europium", 9, 9, "f", "s", 0], ["Gd", "gadolinium", 9, 10, "f", "s", 0], ["Tb", "terbium", 9, 11, "f", "s", 0], ["Dy", "dysprosium", 9, 12, "f", "s", 0], ["Ho", "holmium", 9, 13, "f", "s", 0], ["Er", "erbium", 9, 14, "f", "s", 0], ["Tm", "thulium", 9, 15, "f", "s", 0], ["Yb", "ytterbium", 9, 16, "f", "s", 0], ["Lu", "lutécium", 6, 3, "d", "s", 0], ["Hf", "hafnium", 6, 4, "d", "s", 0], ["Ta", "tantale", 6, 5, "d", "s", 0], ["W", "tungstène", 6, 6, "d", "s", 0], ["Re", "rhénium", 6, 7, "d", "s", 0], ["Os", "osmium", 6, 8, "d", "s", 0], ["Ir", "iridium", 6, 9, "d", "s", 0], ["Pt", "platine", 6, 10, "d", "s", 0], ["Au", "or", 6, 11, "d", "s", 0], ["Hg", "mercure", 6, 12, "d", "l", 0], ["Tl", "thallium", 6, 13, "p", "s", 0], ["Pb", "plomb", 6, 14, "p", "s", 0], ["Bi", "bismuth", 6, 15, "p", "s", 1], ["Po", "polonium", 6, 16, "p", "s", 2], ["At", "astate", 6, 17, "p", "s", 2], ["Rn", "radon", 6, 18, "p", "g", 2], ["Fr", "francium", 7, 1, "s", "s", 2], ["Ra", "radium", 7, 2, "s", "s", 2], ["Ac", "actinium", 10, 3, "f", "s", 2], ["Th", "thorium", 10, 4, "f", "s", 2], ["Pa", "protactinium", 10, 5, "f", "s", 2], ["U", "uranium", 10, 6, "f", "s", 2], ["Np", "neptunium", 10, 7, "f", "s", 2], ["Pu", "plutonium", 10, 8, "f", "s", 2], ["Am", "américium", 10, 9, "f", "s", 2], ["Cm", "curium", 10, 10, "f", "s", 2], ["Bk", "berkélium", 10, 11, "f", "s", 2], ["Cf", "californium", 10, 12, "f", "s", 2], ["Es", "einsteinium", 10, 13, "f", "s", 2], ["Fm", "fermium", 10, 14, "f", "?", 2], ["Md", "mendélévium", 10, 15, "f", "?", 2], ["No", "nobélium", 10, 16, "f", "?", 2], ["Lr", "lawrencium", 7, 3, "d", "?", 2], ["Rf", "rutherfordium", 7, 4, "d", "?", 2], ["Db", "dubnium", 7, 5, "d", "?", 2], ["Sg", "seaborgium", 7, 6, "d", "?", 2], ["Bh", "bohrium", 7, 7, "d", "?", 2], ["Hs", "hassium", 7, 8, "d", "?", 2], ["Mt", "meitnérium", 7, 9, "d", "?", 2], ["Ds", "darmstadtium", 7, 10, "d", "?", 2], ["Rg", "roentgenium", 7, 11, "d", "?", 2], ["Cn", "copernicium", 7, 12, "d", "?", 2], ["Nh", "nihonium", 7, 13, "p", "?", 2], ["Fl", "flérovium", 7, 14, "p", "?", 2], ["Mc", "moscovium", 7, 15, "p", "?", 2], ["Lv", "livermorium", 7, 16, "p", "?", 2], ["Ts", "tennesse", 7, 17, "p", "?", 2], ["Og", "oganesson", 7, 18, "p", "?", 2]];   /* [symbole, nom, ligne, colonne, bloc, état à 25 °C (s, l, g, ?), radioactivité (0, 1 : infime, 2)] */
  var AMAJ = { 1: 1, 2: 4, 3: 7, 4: 9, 5: 11, 6: 12, 7: 14, 8: 16, 9: 19, 10: 20, 11: 23, 12: 24, 13: 27, 14: 28, 15: 31, 16: 32, 17: 35, 18: 40, 19: 39, 20: 40, 21: 45, 22: 48, 23: 51, 24: 52, 25: 55, 26: 56, 27: 59, 28: 58, 29: 63, 30: 64, 47: 107, 53: 127, 79: 197, 82: 208, 92: 238 };   /* nombre de masse de l'isotope le plus abondant */
  /* ================= Quiz : l'atome et ses constituants ================= */
  var QUIZ = {
    'quiz-atome': [
      ['Qu\u2019est-ce qui détermine la <b>taille</b> d\u2019un atome&nbsp;?', ['le noyau', 'le nuage électronique'], 1, 'Le noyau est environ 100&nbsp;000 fois plus petit que l\u2019atome&nbsp;: c\u2019est le nuage électronique qui fait sa taille.'],
      ['Qu\u2019est-ce qui porte la quasi-totalité de la <b>masse</b> d\u2019un atome&nbsp;?', ['le noyau', 'le nuage électronique'], 0, 'Protons et neutrons sont environ 2&nbsp;000 fois plus lourds que les électrons&nbsp;: la masse est concentrée dans le noyau.'],
      ['Quelle est la charge d\u2019un neutron&nbsp;?', ['positive', 'négative', 'nulle'], 2, 'Le neutron, comme son nom l\u2019indique, est électriquement neutre.'],
      ['Un atome est électriquement neutre. Il contient donc autant…', ['de protons que de neutrons', 'de protons que d\u2019électrons', 'de neutrons que d\u2019électrons'], 1, 'La charge d\u2019un proton est exactement opposée à celle d\u2019un électron&nbsp;: autant de protons que d\u2019électrons pour une charge totale nulle.'],
      ['Un atome qui a <b>perdu</b> deux électrons devient…', ['un anion', 'un cation'], 1, 'Il a plus de protons que d\u2019électrons&nbsp;: il est chargé positivement, c\u2019est un cation (par exemple Cu<sup>2+</sup>).'],
      ['L\u2019ion chlorure Cl<sup>\u2212</sup> est…', ['un anion', 'un cation'], 0, 'Il porte une charge négative&nbsp;: l\u2019atome de chlore a gagné un électron. C\u2019est un anion.'],
      ['Qu\u2019est-ce qui définit un élément chimique&nbsp;?', ['le nombre de neutrons', 'le nombre de protons', 'le nombre d\u2019électrons'], 1, 'Un élément chimique est défini par son numéro atomique Z, le nombre de protons de son noyau.'],
      ['L\u2019atome de cuivre Cu et l\u2019ion Cu<sup>2+</sup> appartiennent-ils au même élément chimique&nbsp;?', ['oui', 'non'], 0, 'Oui&nbsp;: ils ont le même nombre de protons (29). Seul le nuage électronique diffère.'],
      ['Une réaction chimique peut-elle transformer du plomb en or&nbsp;?', ['oui', 'non'], 1, 'Non&nbsp;: une réaction chimique ne modifie que le nuage électronique. Changer d\u2019élément exige de modifier le noyau&nbsp;: c\u2019est le domaine des réactions nucléaires.']
    ]
  };
  $$(document, '.nt-quizlab').forEach(function (root) {
    var D = QUIZ[root.id]; if (!D) { return; }
    var qEl = $(root, '.nt-ql-q'), bx = $(root, '.nt-ql-btns'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), next = $(root, '[data-act="next"]'), prog = $(root, '.nt-prog'), num0 = $(root, '.nt-qnum'), lbl = next.innerHTML;
    var order = [], k = 0, good = 0, answered = false, fini = false, res = [];
    function progres() { prog.innerHTML = order.map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === k && !fini ? ' cur' : '') + '"></i>'; }).join(''); num0.textContent = fini ? 'Bilan' : 'Question ' + (k + 1) + ' sur ' + order.length; }
    function show() {
      answered = false; var q = D[order[k]]; qEl.innerHTML = q[0]; msg.textContent = ''; msg.className = 'nt-msg'; bx.innerHTML = '';
      q[1].forEach(function (cTxt, i) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn nt-choix'; b.innerHTML = cTxt;
        b.addEventListener('click', function () {
          if (answered) { return; } answered = true; var ok = i === q[2]; res[k] = ok; if (ok) { good++; }
          b.classList.add(ok ? 'nt-choix-ok' : 'nt-choix-ko'); if (!ok) { bx.children[q[2]].classList.add('nt-choix-ok'); }
          msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko'); msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Non.</b> ') + q[3];
          sc.textContent = good + ' / ' + (k + 1); progres();
        });
        bx.appendChild(b);
      });
      next.innerHTML = k === order.length - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lbl; progres();
    }
    function start() { order = shuffle(D.map(function (_, i) { return i; })); k = 0; good = 0; fini = false; res = []; bx.hidden = false; sc.textContent = '0 / 0'; show(); }
    next.addEventListener('click', function () {
      if (fini) { start(); return; }
      if (!answered) { msg.className = 'nt-msg'; msg.textContent = 'Choisissez d\u2019abord une réponse.'; return; }
      k++;
      if (k >= order.length) { fini = true; bx.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + order.length + '</span> ' + bilanTxt(good / order.length); msg.textContent = ''; msg.className = 'nt-msg'; next.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; progres(); return; }
      show();
    });
    start();
  });
  /* ================= Du cheveu au noyau : l'échelle des tailles ================= */
  (function () {
    var root = document.getElementById('lab-echelle');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), S, sel = 5;
    var OBJ = [['épaisseur d\u2019un cheveu', 1e-4, '#92400E', 'l\u2019'], ['globule rouge', 7e-6, '#DC2626', 'le '], ['bactérie', 1e-6, '#16A34A', 'la '], ['virus', 1e-7, '#7C3AED', 'le '], ['molécule d\u2019eau', 3e-10, '#0EA5E9', 'la '], ['atome', 1e-10, '#2563EB', 'l\u2019'], ['noyau d\u2019un atome', 1e-15, '#F59E0B', 'le ']];   /* nom, taille (m), couleur, article */
    var UNITES = [['mm', -3], ['µm', -6], ['nm', -9], ['pm', -12], ['fm', -15]];
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, x0 = 34, x1 = w - 34, e0 = 0, e1 = -16, yB = 132, hb = 16;
      function X(e) { return x0 + (e0 - e) / (e0 - e1) * (x1 - x0); }
      function yb(i) { return yB - 42 - (i % 3) * 26; }   /* trois hauteurs d'étiquettes */
      c.clearRect(0, 0, w, h);
      /* colonne lumineuse sur l'objet choisi */
      var xs = X(Math.log10(OBJ[sel][1])), gl = c.createLinearGradient(0, 8, 0, yB + hb);
      gl.addColorStop(0, 'rgba(255,255,255,0)'); gl.addColorStop(1, OBJ[sel][2] + '33'); c.fillStyle = gl; rr(c, xs - 18, 8, 36, yB + hb - 8, 10); c.fill();
      /* bande graduée, en dégradé du « grand » vers le « petit » */
      var gb = c.createLinearGradient(x0, 0, x1, 0); gb.addColorStop(0, '#FDE68A'); gb.addColorStop(0.45, '#BFDBFE'); gb.addColorStop(1, '#C4B5FD');
      rr(c, x0 - 8, yB - hb / 2, x1 - x0 + 16, hb, hb / 2); c.fillStyle = gb; c.fill(); c.strokeStyle = 'rgba(15,23,42,.25)'; c.lineWidth = 1; c.stroke();
      for (var e = 0; e >= -16; e--) { c.strokeStyle = 'rgba(15,23,42,.55)'; c.lineWidth = e % 3 === 0 ? 1.6 : 0.8; c.beginPath(); c.moveTo(X(e), yB - (e % 3 === 0 ? 7 : 4)); c.lineTo(X(e), yB + (e % 3 === 0 ? 7 : 4)); c.stroke(); if (e % 2 === 0) { txt(c, e === 0 ? '1 m' : puiss(e) + ' m', X(e), yB + 26, '#475569', '11px system-ui'); } }
      /* domaines des sous-multiples */
      UNITES.forEach(function (u) { var xa = X(u[1]), xb = X(u[1] - 3) - 4; c.strokeStyle = '#94A3B8'; c.lineWidth = 1; c.beginPath(); c.moveTo(xa, yB + 36); c.lineTo(xa, yB + 42); c.lineTo(Math.min(xb, x1), yB + 42); c.stroke(); var der = u[1] === -15; pastille(c, '1 ' + u[0] + ' = ' + puiss(u[1]) + ' m', der ? x1 + 8 : xa + 4, yB + 60, '#475569', '#F8FAFC', der ? 'right' : 'left'); });   /* la dernière étiquette s'aligne à droite, dans le cadre */
      /* objets : d'abord les traits et les points, puis les étiquettes par-dessus */
      OBJ.forEach(function (o, i) { var xo = X(Math.log10(o[1])), on = i === sel; c.strokeStyle = o[2]; c.lineWidth = on ? 2 : 1; c.setLineDash(on ? [] : [3, 3]); c.beginPath(); c.moveTo(xo, yb(i) + 6); c.lineTo(xo, yB - 9); c.stroke(); c.setLineDash([]); });
      OBJ.forEach(function (o, i) { var xo = X(Math.log10(o[1])), on = i === sel; c.fillStyle = '#fff'; c.beginPath(); c.arc(xo, yB, on ? 8 : 6, 0, 2 * Math.PI); c.fill(); c.fillStyle = o[2]; c.beginPath(); c.arc(xo, yB, on ? 6 : 4.5, 0, 2 * Math.PI); c.fill(); });
      OBJ.forEach(function (o, i) { pastille(c, o[0], X(Math.log10(o[1])), yb(i), o[2], i === sel ? '#FFF7ED' : '#fff'); });
      var o = OBJ[sel], prev = sel > 0 ? OBJ[sel - 1] : null, ex = Math.floor(Math.log10(o[1]) + 1e-9), ma = o[1] / Math.pow(10, ex), taille = (ma > 1.5 ? fr(ma, 0) + '&nbsp;×&nbsp;' : '') + '10<sup>' + String(ex).replace('-', '\u2212') + '</sup>&nbsp;m';
      msg.innerHTML = '<b>' + o[0].charAt(0).toUpperCase() + o[0].slice(1) + '</b>&nbsp;: environ ' + taille + '.' + (prev ? ' C\u2019est environ <b>' + Math.round(prev[1] / o[1]).toLocaleString('fr-FR') + ' fois</b> plus petit que ' + prev[3] + prev[0] + '.' : '');
      $$(root, '[data-obj]').forEach(function (b) { b.classList.toggle('nt-btn-main', +b.getAttribute('data-obj') === sel); });
    }
    $$(root, '[data-obj]').forEach(function (b) { b.addEventListener('click', function () { sel = +b.getAttribute('data-obj'); draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* écriture conventionnelle en HTML : A en haut, Z en bas, à gauche du symbole */
  function nuc(A, Z, X, q) {   /* A en haut à gauche, Z en bas à gauche, la charge en haut à droite, à la hauteur de A */
    var ch = !q ? '' : (Math.abs(q) > 1 ? Math.abs(q) : '') + (q > 0 ? '+' : '\u2212');
    return '<span class="nt-not"><span class="nt-nuc"><span>' + (A === null ? '&nbsp;' : A) + '</span><span>' + (Z === null ? '&nbsp;' : Z) + '</span></span><span class="nt-sym">' + X + '</span>' + (ch ? '<span class="nt-chg">' + ch + '</span>' : '') + '</span>';
  }
  /* amas de nucléons : relaxation (attraction vers le centre, répulsion entre sphères) ; types répartis au hasard, positions mémorisées */
  function amas(N, r, seed) {
    var s = seed || 7; function rnd() { s = (s * 16807) % 2147483647; return s / 2147483647; }
    var P = []; for (var k = 0; k < N; k++) { P.push([(rnd() - 0.5) * r * 3, (rnd() - 0.5) * r * 3]); }
    var d0 = 1.62 * r;
    for (var it = 0; it < 220; it++) { for (var i = 0; i < N; i++) { P[i][0] *= 0.965; P[i][1] *= 0.965; for (var j = 0; j < N; j++) { if (i === j) { continue; } var dx = P[i][0] - P[j][0], dy = P[i][1] - P[j][1], d = Math.hypot(dx, dy) || 1e-3; if (d < d0) { var f = (d0 - d) / d * 0.5; P[i][0] += dx * f; P[i][1] += dy * f; } } } }
    return P;
  }
  /* ================= Construire un atome, puis un ion ================= */
  (function () {
    var root = document.getElementById('lab-atome');
    if (!root) { return; }
    var cv = $(root, 'canvas'), oInfo = $(root, '.nt-at-info'), oDefi = $(root, '.nt-at-defi'), msg = $(root, '.nt-msg'), S, visible = true, last = null, t = 0;
    var p = 0, n = 0, e = 0, MAX = { p: 30, n: 40, e: 34 }, defi = -1, faits = 0, cache = null;
    var DEFIS = [[2, 2, 2, 'l\u2019atome d\u2019hélium 4'], [6, 6, 6, 'l\u2019atome de carbone 12'], [6, 8, 6, 'l\u2019atome de carbone 14'], [8, 8, 10, 'l\u2019ion oxyde O<sup>2\u2212</sup> (A = 16)'], [11, 12, 10, 'l\u2019ion sodium Na<sup>+</sup> (A = 23)'], [17, 18, 18, 'l\u2019ion chlorure Cl<sup>\u2212</sup> (A = 35)'], [12, 12, 10, 'l\u2019ion magnésium Mg<sup>2+</sup> (A = 24)'], [26, 30, 24, 'l\u2019ion fer II Fe<sup>2+</sup> (A = 56)']];
    function info() {
      var A = p + n, q = p - e, el = p ? EL[p - 1] : null;
      var nat = !p ? 'pas d\u2019élément&nbsp;: un élément est défini par ses protons' : (q === 0 ? 'atome neutre' : (q > 0 ? 'cation (il a perdu ' + q + ' électron' + (q > 1 ? 's' : '') + ')' : 'anion (il a gagné ' + (-q) + ' électron' + (-q > 1 ? 's' : '') + ')'));
      var h = '<div class="nt-at-nota">' + (el ? nuc(A, p, el[0], q) : '—') + '</div>';
      h += '<p><b>élément</b>&nbsp;: ' + (el ? el[1] + ' (' + el[0] + ', Z = ' + p + ')' : 'aucun') + '</p>';
      h += '<p><b>nature</b>&nbsp;: ' + nat + '</p>';
      h += '<p><b>charge</b>&nbsp;: ' + (q === 0 ? '0' : (q > 0 ? '+' : '\u2212') + Math.abs(q) + '&nbsp;e = ' + (q > 0 ? '+' : '\u2212') + fr(Math.abs(q) * 1.6, 1) + '&nbsp;×&nbsp;10<sup>\u221219</sup>&nbsp;C') + '</p>';
      var mm = A * 1.67, ex = -27; while (mm >= 10) { mm /= 10; ex++; }   /* masse ≈ A × 1,67 × 10⁻²⁷ kg, en notation scientifique */
      h += '<p><b>masse</b>&nbsp;: ' + (A ? '≈ ' + A + ' × 1,67&nbsp;×&nbsp;10<sup>\u221227</sup>&nbsp;kg ≈ ' + fr(mm, 1) + '&nbsp;×&nbsp;10<sup>\u2212' + (-ex) + '</sup>&nbsp;kg' : '0') + '</p>';
      if (el && AMAJ[p] && A !== AMAJ[p] && Math.abs(A - AMAJ[p]) > 2) { h += '<p class="nt-note">L\u2019isotope le plus courant du ' + el[1] + ' a A = ' + AMAJ[p] + '.</p>'; }
      if (Math.abs(q) > 3) { h += '<p class="nt-note">Un ion aussi chargé est très improbable&nbsp;: les ions monoatomiques courants portent une à trois charges.</p>'; }
      oInfo.innerHTML = h;
      $$(root, '[data-cnt]').forEach(function (s2) { s2.textContent = { p: p, n: n, e: e }[s2.getAttribute('data-cnt')]; });
      if (defi >= 0) {
        var d = DEFIS[defi];
        if (p === d[0] && n === d[1] && e === d[2]) { faits++; msg.innerHTML = '<span style="color:#16A34A;">Bravo&nbsp;!</span> Vous avez construit ' + d[3] + '&nbsp;: ' + d[0] + ' protons, ' + d[1] + ' neutrons et ' + d[2] + ' électrons.'; defi = -2; }
      }
    }
    function nouveauDefi() { defi = (defi < 0 ? faits : defi + 1) % DEFIS.length; oDefi.innerHTML = '<b>Défi</b>&nbsp;: construisez ' + DEFIS[defi][3] + '.'; msg.textContent = ''; }
    function draw(dt) {
      if (!S) { return; }
      t += dt; var c = S.ctx, w = S.w, h = S.h, cx = w / 2, cy = h / 2, R = Math.min(w, h) / 2 - 12;
      c.clearRect(0, 0, w, h);
      var g = c.createRadialGradient(cx, cy, 4, cx, cy, R); g.addColorStop(0, 'rgba(147,197,253,.55)'); g.addColorStop(0.7, 'rgba(191,219,254,.3)'); g.addColorStop(1, 'rgba(219,234,254,0)');
      c.fillStyle = g; c.beginPath(); c.arc(cx, cy, R, 0, 2 * Math.PI); c.fill();
      /* noyau (très agrandi) : protons et neutrons tassés en amas, répartis au hasard */
      var N = p + n, rn = N > 30 ? 7 : 9;
      if (!cache || cache.N !== N || cache.p !== p || cache.rn !== rn) {
        var P = amas(N, rn, 11 + N), ty = []; for (var k = 0; k < N; k++) { ty.push(k < p ? 'p' : 'n'); }
        var s3 = 97 + p; for (var k2 = N - 1; k2 > 0; k2--) { s3 = (s3 * 16807) % 2147483647; var j2 = s3 % (k2 + 1), tt = ty[k2]; ty[k2] = ty[j2]; ty[j2] = tt; }
        cache = { N: N, p: p, rn: rn, pts: P.map(function (q, k3) { return [q[0], q[1], ty[k3]]; }).sort(function (u, v) { return (u[1] + 0.3 * u[0]) - (v[1] + 0.3 * v[0]); }) };
      }
      cache.pts.forEach(function (q) {
        var x = cx + q[0], y = cy + q[1], gg = c.createRadialGradient(x - rn * 0.35, y - rn * 0.38, 1, x, y, rn);
        gg.addColorStop(0, q[2] === 'p' ? '#FECDD3' : '#DCFCE7'); gg.addColorStop(0.45, q[2] === 'p' ? '#FB7185' : '#4ADE80'); gg.addColorStop(1, q[2] === 'p' ? '#BE123C' : '#15803D');
        c.fillStyle = gg; c.beginPath(); c.arc(x, y, rn, 0, 2 * Math.PI); c.fill(); c.strokeStyle = 'rgba(255,255,255,.85)'; c.lineWidth = 0.9; c.stroke();
        if (q[2] === 'p') { c.strokeStyle = '#fff'; c.lineWidth = 1.8; c.lineCap = 'round'; c.beginPath(); c.moveTo(x - rn * 0.4, y); c.lineTo(x + rn * 0.4, y); c.moveTo(x, y - rn * 0.4); c.lineTo(x, y + rn * 0.4); c.stroke(); }
      });
      /* électrons, en mouvement dans le nuage */
      for (var j = 0; j < e; j++) {
        var rr0 = R * (0.42 + 0.5 * ((j * 0.618) % 1)), om = (RM ? 0.15 : 0.6) * (1 + (j % 3) * 0.3) * (j % 2 ? 1 : -1), an = j * 2.4 + om * t;
        var ex = cx + rr0 * Math.cos(an), ey = cy + rr0 * 0.85 * Math.sin(an);
        c.fillStyle = '#2563EB'; c.beginPath(); c.arc(ex, ey, 6, 0, 2 * Math.PI); c.fill();
        c.strokeStyle = '#fff'; c.lineWidth = 1.8; c.lineCap = 'round'; c.beginPath(); c.moveTo(ex - 3, ey); c.lineTo(ex + 3, ey); c.stroke();   /* signe « − » centré */
      }
      if (!N && !e) { txt(c, 'Ajoutez des particules', cx, cy + 4, '#64748B', '600 13px system-ui'); }
      txt(c, 'noyau très agrandi : dessin pas à l\u2019échelle', cx, h - 6, '#94A3B8', '10.5px system-ui');
    }
    function loop(ts) { var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; if (visible) { draw(dt); } requestAnimationFrame(loop); }
    $$(root, '[data-add]').forEach(function (b) { b.addEventListener('click', function () { var k = b.getAttribute('data-add'); if (k === 'p' && p < MAX.p) { p++; } if (k === 'n' && n < MAX.n) { n++; } if (k === 'e' && e < MAX.e) { e++; } info(); }); });
    $$(root, '[data-sub]').forEach(function (b) { b.addEventListener('click', function () { var k = b.getAttribute('data-sub'); if (k === 'p' && p > 0) { p--; } if (k === 'n' && n > 0) { n--; } if (k === 'e' && e > 0) { e--; } info(); }); });
    $(root, '[data-act="defi"]').addEventListener('click', nouveauDefi);
    $(root, '[data-act="vide"]').addEventListener('click', function () { p = n = e = 0; info(); });
    function setup() { S = canvasCtx(cv); draw(0); }
    watch(cv, function (v) { visible = v; });
    setup(); info(); nouveauDefi(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Le tableau périodique ================= */
  (function () {
    var root = document.getElementById('lab-tableau');
    if (!root) { return; }
    var cv = $(root, 'canvas'), leg = $(root, '.nt-tab-leg'), fiche = $(root, '.nt-tab-fiche'), S, mode = 'simple', sel = 29, geo = null;
    var COUL = {
      simple: function () { return '#EFF6FF'; },
      etat: function (z) { return { s: '#CBD5E1', l: '#7DD3FC', g: '#FDE68A', '?': '#F1F5F9' }[EL[z - 1][5]]; },
      bloc: function (z) { return { s: '#FCA5A5', p: '#FDE68A', d: '#93C5FD', f: '#A7F3D0' }[EL[z - 1][4]]; },
      radio: function (z) { return ['#E2E8F0', '#FDBA74', '#FCA5A5'][EL[z - 1][6]]; }
    };
    var LEG = {
      simple: [['#EFF6FF', 'les 118 éléments connus']],
      etat: [['#CBD5E1', 'solide'], ['#7DD3FC', 'liquide'], ['#FDE68A', 'gaz'], ['#F1F5F9', 'inconnu (produit en quantités infimes)']],
      bloc: [['#FCA5A5', 'bloc s'], ['#FDE68A', 'bloc p'], ['#93C5FD', 'bloc d'], ['#A7F3D0', 'bloc f']],
      radio: [['#E2E8F0', 'au moins un isotope stable'], ['#FDBA74', 'radioactivité infime (bismuth)'], ['#FCA5A5', 'tous les isotopes sont radioactifs']]
    };
    var ETAT = { s: 'solide', l: 'liquide', g: 'gaz', '?': 'inconnu' }, RAD = ['au moins un isotope stable', 'radioactivité infime (demi-vie d\u2019environ 2 × 10<sup>19</sup> ans)', 'radioactif&nbsp;: tous ses isotopes sont instables'];
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, cs = Math.min((w - 8) / 18, (h - 8) / 10.4), ox = (w - cs * 18) / 2, oy = 4;
      geo = { cs: cs, ox: ox, oy: oy };
      c.clearRect(0, 0, w, h);
      EL.forEach(function (el, i) {
        var z = i + 1, r = el[2], col = el[3], x = ox + (col - 1) * cs, y = oy + (r - 1 + (r >= 9 ? 0.4 : 0)) * cs, on = z === sel;
        rr(c, x + 1, y + 1, cs - 2, cs - 2, Math.max(2, cs * 0.12)); c.fillStyle = COUL[mode](z); c.fill();
        c.strokeStyle = on ? '#0F172A' : 'rgba(100,116,139,.45)'; c.lineWidth = on ? 2.2 : 0.8; c.stroke();
        c.save(); c.fillStyle = '#0F172A'; c.textAlign = 'center';
        c.font = '700 ' + Math.max(8, cs * 0.36) + 'px system-ui'; c.fillText(el[0], x + cs / 2, y + cs * 0.66);
        if (cs >= 30) { c.font = Math.max(7, cs * 0.22) + 'px system-ui'; c.fillStyle = '#475569'; c.fillText(String(z), x + cs / 2, y + cs * 0.3); }
        c.restore();
      });
      /* bloc f (La–Yb et Ac–No) : repère entre les groupes 2 et 3, et étiquettes des deux lignes */
      [6, 7].forEach(function (rg) { var x = ox + 2 * cs, y = oy + (rg - 1) * cs; c.save(); c.strokeStyle = '#94A3B8'; c.lineWidth = 2; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(x, y + cs * 0.2); c.lineTo(x, y + cs * 0.8); c.stroke(); c.restore(); });
      [[9, '57\u201370'], [10, '89\u2013102']].forEach(function (q) { var y = oy + (q[0] - 1 + 0.4) * cs; c.save(); c.fillStyle = '#64748B'; c.font = '600 ' + Math.max(8, cs * 0.28) + 'px system-ui'; c.textAlign = 'right'; c.fillText(q[1], ox + 2 * cs - 4, y + cs * 0.6); c.restore(); });
      leg.innerHTML = LEG[mode].map(function (l) { return '<span><i style="background:' + l[0] + '"></i>' + l[1] + '</span>'; }).join('');
      var el = EL[sel - 1];
      fiche.innerHTML = '<div class="nt-at-nota">' + nuc(AMAJ[sel] || null, sel, el[0], 0) + '</div><p><b>' + el[1] + '</b>, numéro atomique Z = ' + sel + ' (' + sel + ' protons)' + (AMAJ[sel] ? '&nbsp;; isotope le plus courant&nbsp;: A = ' + AMAJ[sel] : '') + '.</p><p>état à 25&nbsp;°C&nbsp;: ' + ETAT[el[5]] + '&nbsp;; bloc ' + el[4] + '&nbsp;; ' + RAD[el[6]] + '.</p>';
    }
    cv.addEventListener('click', function (ev) {
      if (!geo) { return; } var r = cv.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top;
      EL.forEach(function (el, i) { var rr2 = el[2], col = el[3], x0 = geo.ox + (col - 1) * geo.cs, y0 = geo.oy + (rr2 - 1 + (rr2 >= 9 ? 0.4 : 0)) * geo.cs; if (x >= x0 && x < x0 + geo.cs && y >= y0 && y < y0 + geo.cs) { sel = i + 1; } });
      draw();
    });
    $$(root, 'input[name="tmode"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= Entraînement : noyaux et ions ================= */
  (function () {
    var root = document.getElementById('lab-noyau');
    if (!root) { return; }
    var qEl = $(root, '.nt-tr-q'), inp = $(root, 'input[type="text"]'), uEl = $(root, '.nt-tr-unit'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), bV = $(root, '[data-act="check"]'), bN = $(root, '[data-act="next"]'), lblN = bN.innerHTML;
    var NQ = 6, n = 0, good = 0, cur, done = false, fini = false;
    var ZS = Object.keys(AMAJ).map(Number);
    var IONS = [[11, 1], [19, 1], [12, 2], [20, 2], [13, 3], [26, 2], [26, 3], [29, 2], [30, 2], [9, -1], [17, -1], [8, -2], [16, -2]];
    var vis = $(root, '.nt-qvis'), prog = $(root, '.nt-prog'), num0 = $(root, '.nt-qnum'), res = [];
    var G = [
      function () { var Z = pick(ZS), A = AMAJ[Z], el = EL[Z - 1];
        return { q: 'Combien de <b>neutrons</b> contient ce noyau&nbsp;?', vis: nuc(A, Z, el[0], 0), rep: A - Z, unit: 'neutrons', expl: 'Z = ' + Z + '&nbsp;: ' + Z + ' protons. A = ' + A + '&nbsp;: ' + A + ' nucléons. Donc N = A − Z = ' + A + ' − ' + Z + ' = ' + (A - Z) + ' neutrons.' }; },
      function () { var Z = pick(ZS), A = AMAJ[Z], el = EL[Z - 1];
        return { q: 'Ce noyau est celui du ' + el[1] + ', de numéro atomique Z = ' + Z + '. Combien contient-il de <b>nucléons</b>&nbsp;?', vis: nuc(A, null, el[0], 0), rep: A, unit: 'nucléons', expl: 'Le nombre de nucléons est le nombre écrit en haut à gauche&nbsp;: A = ' + A + '. (Il contient ' + Z + ' protons et ' + (A - Z) + ' neutrons.)' }; },
      function () { var Z = pick(ZS), A = AMAJ[Z], el = EL[Z - 1];
        return { q: 'Un noyau contient ' + Z + ' protons et ' + (A - Z) + ' neutrons. Quel est son nombre de masse <b>A</b>&nbsp;?', vis: '<span class="nt-qcomp"><b class="p">' + Z + '</b> protons + <b class="n">' + (A - Z) + '</b> neutrons</span>', rep: A, unit: '', expl: 'A = Z + N = ' + Z + ' + ' + (A - Z) + ' = ' + A + '&nbsp;: c\u2019est le noyau ' + nuc(A, Z, el[0], 0) + ' (' + el[1] + ' ' + A + ').' }; },
      function () { var io = pick(IONS), Z = io[0], q = io[1], el = EL[Z - 1], A = AMAJ[Z];
        return { q: 'Combien d\u2019<b>électrons</b> possède cet ion&nbsp;?', vis: nuc(A, Z, el[0], q), rep: Z - q, unit: 'électrons', expl: 'L\u2019atome de ' + el[1] + ' a ' + Z + ' électrons (autant que de protons). L\u2019ion porte la charge ' + (q > 0 ? '+' + q : '\u2212' + (-q)) + '&nbsp;: il a ' + (q > 0 ? 'perdu ' + q : 'gagné ' + (-q)) + ' électron' + (Math.abs(q) > 1 ? 's' : '') + '. Il en a donc ' + Z + (q > 0 ? ' − ' + q : ' + ' + (-q)) + ' = ' + (Z - q) + '.' }; },
      function () { var io = pick(IONS), Z = io[0], q = io[1], el = EL[Z - 1], A = AMAJ[Z];
        return { q: 'Combien de <b>protons</b> possède cet ion&nbsp;?', vis: nuc(A, Z, el[0], q), rep: Z, unit: 'protons', expl: 'Former un ion ne modifie que le nuage électronique&nbsp;: le noyau garde ses ' + Z + ' protons (Z = ' + Z + ').' }; }
    ];
    function progres() { prog.innerHTML = Array.apply(null, Array(NQ)).map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === n - (done ? 1 : 0) && !fini ? ' cur' : '') + '"></i>'; }).join(''); num0.textContent = fini ? 'Bilan' : 'Question ' + Math.min(NQ, n + (done ? 0 : 1)) + ' sur ' + NQ; }
    function nouveau() { cur = pick(G)(); qEl.innerHTML = cur.q; vis.innerHTML = cur.vis; vis.hidden = false; uEl.textContent = cur.unit; inp.value = ''; msg.textContent = ''; msg.className = 'nt-msg'; done = false; bV.disabled = false; inp.disabled = false; bN.innerHTML = n === NQ - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lblN; progres(); }
    function start() { n = 0; good = 0; fini = false; res = []; sc.textContent = '0 / 0'; $(root, '.nt-tr-zone').hidden = false; nouveau(); }
    bV.addEventListener('click', function () {
      if (done || fini) { return; }
      var v = num(inp.value); if (isNaN(v)) { msg.className = 'nt-msg'; msg.textContent = 'Entrez un nombre.'; return; }
      var ok = v === cur.rep; done = true; res[n] = ok; n++; if (ok) { good++; }
      bV.disabled = true; inp.disabled = true; sc.textContent = good + ' / ' + n;
      msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko');
      msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Non</b>&nbsp;: la réponse est ' + cur.rep + '. ') + cur.expl; progres();
    });
    inp.addEventListener('keydown', function (ev) { if (ev.key === 'Enter') { bV.click(); } });
    bN.addEventListener('click', function () {
      if (fini) { start(); return; }
      if (!done) { msg.className = 'nt-msg'; msg.textContent = 'Validez d\u2019abord votre réponse.'; return; }
      if (n >= NQ) { fini = true; $(root, '.nt-tr-zone').hidden = true; vis.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + NQ + '</span> ' + bilanTxt(good / NQ); msg.textContent = ''; msg.className = 'nt-msg'; bN.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; progres(); return; }
      nouveau();
    });
    start();
  })();
  /* ================= L'expérience de Rutherford : l'atome est essentiellement vide ================= */
  (function () {
    var root = document.getElementById('lab-rutherford');
    if (!root) { return; }
    var cv = $(root, 'canvas'), o0 = $(root, '.out-0'), o1 = $(root, '.out-1'), o2 = $(root, '.out-2'), btn = $(root, '[data-act="play"]'), S, visible = true, last = null, run = true, spawn = 0, P = [], cnt = [0, 0, 0], NOY = [];
    var K = 0.15;   /* paramètre de la loi de déviation : θ = 2 arctan(K / b), b = distance de passage au noyau (px) ; seules les particules qui frôlent un noyau sont nettement déviées */
    function geo() { var w = S.w, h = S.h, fx = w * 0.56, R = Math.min(24, (h - 40) / 10); return { w: w, h: h, fx: fx, R: R, y0: 20 + R, rows: Math.floor((h - 40) / (2 * R)) }; }
    function noyaux(g) { NOY = []; for (var r = 0; r < g.rows; r++) { for (var c2 = 0; c2 < 2; c2++) { NOY.push([g.fx + c2 * 2 * g.R * 0.9, g.y0 + r * 2 * g.R + (c2 ? g.R : 0)]); } } }
    function draw(dt) {
      if (!S) { return; }
      var g = geo(), c = S.ctx, w = g.w, h = g.h;
      if (run && dt > 0) {
        spawn += dt * 22; while (spawn >= 1) { spawn -= 1; P.push({ x: 70, y: 22 + Math.random() * (h - 44), vx: 1, vy: 0, done: false, trail: [] }); }
        P.forEach(function (q) {
          var sp = 260 * dt; q.trail.push([q.x, q.y]); if (q.trail.length > 18) { q.trail.shift(); }
          var nx = q.x + q.vx * sp, ny = q.y + q.vy * sp;
          if (!q.done && q.vx > 0) {   /* passage près d'un noyau : déviation selon la loi de Rutherford */
            for (var k = 0; k < NOY.length; k++) { var N0 = NOY[k]; if (q.x < N0[0] && nx >= N0[0]) { var b = Math.abs(q.y - N0[1]); if (b < g.R) { var th = 2 * Math.atan(K / Math.max(b, 0.01)) * (q.y < N0[1] ? -1 : 1); q.vx = Math.cos(th); q.vy = Math.sin(th); q.done = true; var a = Math.abs(th) * 180 / Math.PI; cnt[a < 10 ? 0 : (a < 90 ? 1 : 2)]++;   /* moins de 10° : pas de déviation notable */ } } }
          }
          q.x = nx; q.y = ny;
        });
        P.forEach(function (q) { if (!q.done && q.x > g.fx + 2 * g.R) { q.done = true; cnt[0]++; } });
        P = P.filter(function (q) { return q.x > -10 && q.x < w + 10 && q.y > -10 && q.y < h + 10; });
      }
      c.clearRect(0, 0, w, h);
      /* source de particules α */
      c.fillStyle = '#334155'; rr(c, 8, h / 2 - 34, 56, 68, 8); c.fill(); c.save(); c.fillStyle = '#E2E8F0'; c.font = '600 10.5px system-ui'; c.textAlign = 'center'; c.fillText('source', 36, h / 2 - 4); c.fillText('α', 36, h / 2 + 12); c.restore();
      /* feuille d'or : des atomes (nuages) et leurs noyaux, minuscules */
      NOY.forEach(function (N0) { var gg = c.createRadialGradient(N0[0], N0[1], 1, N0[0], N0[1], g.R); gg.addColorStop(0, 'rgba(250,204,21,.32)'); gg.addColorStop(1, 'rgba(250,204,21,.04)'); c.fillStyle = gg; c.beginPath(); c.arc(N0[0], N0[1], g.R, 0, 2 * Math.PI); c.fill(); c.fillStyle = '#B45309'; c.beginPath(); c.arc(N0[0], N0[1], 1.6, 0, 2 * Math.PI); c.fill(); });
      txt(c, 'feuille d\u2019or (atomes)', g.fx + g.R, 14, '#B45309', '600 11px system-ui');
      P.forEach(function (q) {
        c.strokeStyle = 'rgba(225,29,72,.25)'; c.lineWidth = 1.4; c.beginPath(); q.trail.forEach(function (t2, i2) { if (i2 === 0) { c.moveTo(t2[0], t2[1]); } else { c.lineTo(t2[0], t2[1]); } }); c.lineTo(q.x, q.y); c.stroke();
        c.fillStyle = '#E11D48'; c.beginPath(); c.arc(q.x, q.y, 2.6, 0, 2 * Math.PI); c.fill();
      });
      var tot = cnt[0] + cnt[1] + cnt[2] || 1;
      o0.textContent = cnt[0] + ' (' + Math.round(cnt[0] / tot * 100) + ' %)'; o1.textContent = cnt[1] + ' (' + Math.round(cnt[1] / tot * 100) + ' %)'; o2.textContent = cnt[2] + ' (' + Math.round(cnt[2] / tot * 100) + ' %)';
    }
    function loop(ts) { var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; if (visible) { draw(RM ? dt * 0.4 : dt); } requestAnimationFrame(loop); }
    btn.addEventListener('click', function () { run = !run; btn.innerHTML = run ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Reprendre'; });
    $(root, '[data-act="reset"]').addEventListener('click', function () { P = []; cnt = [0, 0, 0]; draw(0); });
    function setup() { S = canvasCtx(cv); noyaux(geo()); draw(0); }
    watch(cv, function (v) { visible = v; });
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Modèles moléculaires 3D ================= */
  (function () {
    var MODELS = {"saccharose": {"a": [["O", 2.12, -0.988, -2.478], ["C", 3.405, -0.405, -2.268], ["C", 3.523, 0.288, -0.908], ["O", 2.559, 1.378, -0.848], ["C", 1.631, 1.074, 0.225], ["C", 1.116, 2.403, 0.812], ["O", 0.547, 2.233, 2.118], ["O", 0.617, 0.273, -0.386], ["C", -0.551, -0.014, 0.382], ["O", -1.494, 1.027, 0.095], ["C", -2.878, 0.675, 0.107], ["C", -3.363, 0.439, 1.546], ["O", -4.782, 0.35, 1.592], ["C", -3.207, -0.5, -0.845], ["O", -3.796, -0.03, -2.071], ["C", -1.955, -1.296, -1.231], ["O", -2.335, -2.605, -1.688], ["C", -1.051, -1.426, -0.014], ["O", 0.019, -2.345, -0.256], ["C", 2.516, 0.303, 1.221], ["O", 1.861, -0.378, 2.283], ["C", 3.248, -0.637, 0.282], ["O", 4.452, -1.117, 0.88], ["H", 1.466, -0.42, -2.02], ["H", 3.558, 0.322, -3.072], ["H", 4.155, -1.196, -2.367], ["H", 4.519, 0.739, -0.831], ["H", 1.939, 3.121, 0.905], ["H", 0.362, 2.85, 0.156], ["H", 0.146, 3.093, 2.346], ["H", -0.343, -0.018, 1.453], ["H", -3.411, 1.561, -0.261], ["H", -3.035, 1.251, 2.205], ["H", -2.954, -0.484, 1.964], ["H", -5.131, 1.256, 1.666], ["H", -3.957, -1.166, -0.402], ["H", -4.661, 0.357, -1.846], ["H", -1.416, -0.83, -2.065], ["H", -2.906, -2.447, -2.465], ["H", -1.631, -1.862, 0.807], ["H", -0.34, -3.005, -0.884], ["H", 3.249, 0.977, 1.685], ["H", 1.387, 0.318, 2.782], ["H", 2.639, -1.509, 0.021], ["H", 4.164, -1.611, 1.672]], "b": [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [4, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1], [10, 11, 1], [11, 12, 1], [10, 13, 1], [13, 14, 1], [13, 15, 1], [15, 16, 1], [15, 17, 1], [17, 18, 1], [4, 19, 1], [19, 20, 1], [19, 21, 1], [21, 22, 1], [21, 2, 1], [17, 8, 1], [0, 23, 1], [1, 24, 1], [1, 25, 1], [2, 26, 1], [5, 27, 1], [5, 28, 1], [6, 29, 1], [8, 30, 1], [10, 31, 1], [11, 32, 1], [11, 33, 1], [12, 34, 1], [13, 35, 1], [14, 36, 1], [15, 37, 1], [16, 38, 1], [17, 39, 1], [18, 40, 1], [19, 41, 1], [20, 42, 1], [21, 43, 1], [22, 44, 1]]}};   /* coordonnées produites par chem.model3d() : { nom: { a: [[élément, x, y, z], …], b: [[i, j, ordre], …] } } */
    var EL = { C: ['#4B5563', 0.36], H: ['#F8FAFC', 0.24], O: ['#DC2626', 0.36], N: ['#2563EB', 0.36], Cl: ['#16A34A', 0.44], S: ['#EAB308', 0.44] };
    function shade(hex, f) { var r = parseInt(hex.substr(1, 2), 16), g = parseInt(hex.substr(3, 2), 16), b = parseInt(hex.substr(5, 2), 16); function c(v) { return Math.max(0, Math.min(255, Math.round(f > 0 ? v + (255 - v) * f : v * (1 + f)))); } return 'rgb(' + c(r) + ',' + c(g) + ',' + c(b) + ')'; }
    Array.prototype.forEach.call(document.querySelectorAll('.nt-mol3d'), function (box) {
      var M = MODELS[box.getAttribute('data-mol')]; if (!M) { return; }
      var cv = document.createElement('canvas'); cv.style.width = '100%'; cv.style.height = '100%'; cv.style.cursor = 'grab'; cv.style.touchAction = 'none'; box.appendChild(cv);
      var ctx, W, H, rx = -0.4, ry = 0.6, auto = true, drag = null, R = 0;
      M.a.forEach(function (a) { R = Math.max(R, Math.hypot(a[1], a[2], a[3])); });
      function size() { var dpr = window.devicePixelRatio || 1; W = box.clientWidth; H = box.clientHeight; cv.width = W * dpr; cv.height = H * dpr; ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
      function draw() {
        var s = Math.min(W, H) / (2 * (Math.max(R, 1.6) + 0.45)), cx = W / 2, cy = H / 2, cX = Math.cos(rx), sX = Math.sin(rx), cY = Math.cos(ry), sY = Math.sin(ry);
        var P = M.a.map(function (a) { var x = a[1] * cY + a[3] * sY, z1 = -a[1] * sY + a[3] * cY, y = a[2] * cX - z1 * sX, z = a[2] * sX + z1 * cX; return [cx + x * s, cy - y * s, z]; });
        var items = [];
        M.a.forEach(function (a, i) { items.push({ z: P[i][2], f: function () {
          var e = EL[a[0]] || EL.C, r = e[1] * s * (1 + 0.06 * P[i][2] / R), g = ctx.createRadialGradient(P[i][0] - r * 0.35, P[i][1] - r * 0.35, r * 0.1, P[i][0], P[i][1], r);
          g.addColorStop(0, shade(e[0], 0.55)); g.addColorStop(0.7, e[0]); g.addColorStop(1, shade(e[0], -0.35));
          ctx.fillStyle = g; ctx.beginPath(); ctx.arc(P[i][0], P[i][1], r, 0, 2 * Math.PI); ctx.fill();
          ctx.strokeStyle = 'rgba(15,23,42,.25)'; ctx.lineWidth = 0.6; ctx.stroke(); } }); });
        M.b.forEach(function (b) {
          var p = P[b[0]], q = P[b[1]], z = (p[2] + q[2]) / 2 - 0.01;
          items.push({ z: z, f: function () {
            var dx = q[0] - p[0], dy = q[1] - p[1], n = Math.hypot(dx, dy) || 1, nx = -dy / n, ny = dx / n, off = b[2] > 1 ? [-0.09 * s, 0.09 * s] : [0];
            off.forEach(function (o) {
              ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = b[2] > 1 ? 0.07 * s : 0.11 * s; ctx.lineCap = 'round';
              ctx.beginPath(); ctx.moveTo(p[0] + nx * o, p[1] + ny * o); ctx.lineTo(q[0] + nx * o, q[1] + ny * o); ctx.stroke();
            }); } });
        });
        items.sort(function (u, v) { return u.z - v.z; });
        ctx.clearRect(0, 0, W, H); items.forEach(function (it) { it.f(); });
      }
      cv.addEventListener('pointerdown', function (e) { drag = [e.clientX, e.clientY]; auto = false; cv.setPointerCapture(e.pointerId); cv.style.cursor = 'grabbing'; });
      cv.addEventListener('pointermove', function (e) { if (!drag) { return; } ry += (e.clientX - drag[0]) * 0.01; rx += (e.clientY - drag[1]) * 0.01; drag = [e.clientX, e.clientY]; draw(); });
      cv.addEventListener('pointerup', function () { drag = null; cv.style.cursor = 'grab'; });
      var visible = true; if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(box); }
      size(); draw(); window.addEventListener('resize', function () { size(); draw(); });
      (function spin() { if (auto && visible) { ry += 0.006; draw(); } requestAnimationFrame(spin); })();
    });
  })();
})();
</script>
