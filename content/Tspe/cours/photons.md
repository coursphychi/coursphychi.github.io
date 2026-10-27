+++
title = "Décrire la lumière par un flux de photons"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-ql-q { font-size: 1.05em; text-align: center; margin: 0.5em 0 0.7em !important; min-height: 1.6em; }
.nt-ql-btns { display: flex; flex-wrap: wrap; gap: 0.45em; justify-content: center; }
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
.nt-prog { display: flex; flex-wrap: wrap; gap: 0.4em; justify-content: center; margin: 0.3em 0 0.5em; }
.nt-prog i { width: 0.85em; height: 0.85em; border-radius: 50%; background: #E2E8F0; transition: background .25s; }
.nt-prog i.ok { background: #22C55E; } .nt-prog i.ko { background: #F43F5E; } .nt-prog i.cur { box-shadow: 0 0 0 2.5px var(--blue); }
.nt-qnum { text-align: center; font-size: 0.82em; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; color: var(--blue); margin: 0; }
.nt-qcard { background: linear-gradient(180deg, #FFFFFF, #F8FAFC); border: 1px solid var(--line); border-radius: 16px; padding: 0.9em 1em 1em; margin: 0.4em auto 0.6em; max-width: 620px; box-shadow: 0 6px 18px rgba(15,23,42,.06); }
.nt-qvis { text-align: center; margin: 0.1em 0 0.3em; }
.nt-qdata { display: inline-flex; flex-wrap: wrap; gap: 0.4em 0.8em; justify-content: center; align-items: center; font-family: Georgia, serif; font-size: 1.55em; color: #0F172A; }
.nt-qdata span { white-space: nowrap; }
.nt-qdata i { display: inline-block; width: 0.75em; height: 0.75em; border-radius: 50%; margin-right: 0.3em; vertical-align: -0.05em; box-shadow: 0 0 0 2px #fff, 0 0 0 3px #CBD5E1; }
.nt-ql-btns .nt-choix { padding: 0.6em 1.1em; border-radius: 12px; font-size: 1em; transition: transform .12s, box-shadow .12s; }
.nt-ql-btns .nt-choix:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37,99,235,.18); }
.nt-choix-ok { background: #DCFCE7 !important; border-color: #16A34A !important; color: #166534 !important; }
.nt-choix-ko { background: #FFE4E6 !important; border-color: #E11D48 !important; color: #9F1239 !important; }
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

## L'effet photoélectrique {.nt-h2}

<p class="nt-lead">Comme souvent, tout part d'une expérience. En 1887, Heinrich Hertz remarque que la lumière ultraviolette facilite le jaillissement d'étincelles entre deux électrodes. L'année suivante, Wilhelm Hallwachs montre qu'une plaque de zinc chargée négativement se décharge quand on l'éclaire en ultraviolet&nbsp;: la lumière arrache des électrons au métal. C'est l'<b>effet photoélectrique</b>.</p>

{{< youtube-plus id="oYnp0WZDhYQ" ratio="16x9" width="500" shadow=true rounded=true >}}

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Ce que montre l'expérience</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li>Une lampe <b>visible</b>, même très lumineuse (et de plus en plus), ne décharge pas la plaque.</li>
<li>Une lampe à ultraviolets proches (UVA, la «&nbsp;lumière noire&nbsp;») non plus.</li>
<li>Une lampe à ultraviolets lointains (UVC, lampe germicide) la décharge&nbsp;! Ces lampes produisent de l'ozone&nbsp;: il faut sortir de la salle.</li>
</ul>
<p>Augmenter l'intensité d'une lumière visible augmente le <b>nombre</b> de photons, mais ne rend pas chacun d'eux plus énergétique. C'est l'énergie de <b>chaque</b> photon, liée à sa fréquence, qui compte.</p>
<p class="nt-note">Historiquement, c'est l'<b>effet photovoltaïque</b>, apparenté à l'effet photoélectrique, qui a été découvert le premier, en 1839, par Edmond Becquerel (avec son père Antoine)&nbsp;: un courant apparaît entre deux électrodes plongées dans un électrolyte et éclairées.</p>
</div>
</details>


<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>L'idée d'Einstein (1905)</p>
<p>Pour expliquer l'effet photoélectrique, Einstein propose une idée révolutionnaire&nbsp;: la lumière est constituée de particules, les <span class="imp nt-hole">photons</span>. L'énergie de chacun de ces «&nbsp;quanta&nbsp;» de lumière est <span class="imp nt-hole">proportionnelle à la fréquence</span> de la lumière, et le coefficient de proportionnalité est la <span class="imp nt-hole">constante de Planck</span> $h$.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Énergie d'un photon</p>
<p class="nt-f-math">$$E = h\nu$$</p>
<div class="nt-f-units"><span>$E$ en <b>J</b></span><span>$\nu$, la fréquence, en <b>Hz</b></span><span>$h = \pu{6,63E-34 J*s}$, la constante de Planck</span></div>
</div>

<div class="nt-svgbox" style="max-width:620px; margin-left:auto; margin-right:auto;"><svg class='nt-svg' viewBox='0 0 560 346' role='img' aria-label="Effet photoélectrique : un photon d’énergie hν cède toute son énergie à un seul électron lié au métal ; une partie, au moins égale à Wext, sert à libérer l’électron ; il repart avec le reste, l’énergie cinétique Ec ; bilan : hν = Wext + Ec"><defs><linearGradient id='gMetal' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#E2E8F0'/><stop offset='1' stop-color='#CBD5E1'/></linearGradient></defs><rect x='30' y='196' width='500' height='64' rx='6' fill='url(#gMetal)' stroke='#94A3B8'/><circle cx='48' cy='212' r='6' fill='#94A3B8'/><circle cx='72' cy='234' r='6' fill='#94A3B8'/><circle cx='96' cy='212' r='6' fill='#94A3B8'/><circle cx='120' cy='234' r='6' fill='#94A3B8'/><circle cx='144' cy='212' r='6' fill='#94A3B8'/><circle cx='168' cy='234' r='6' fill='#94A3B8'/><circle cx='192' cy='212' r='6' fill='#94A3B8'/><circle cx='216' cy='234' r='6' fill='#94A3B8'/><circle cx='240' cy='212' r='6' fill='#94A3B8'/><circle cx='264' cy='234' r='6' fill='#94A3B8'/><circle cx='288' cy='212' r='6' fill='#94A3B8'/><circle cx='312' cy='234' r='6' fill='#94A3B8'/><circle cx='336' cy='212' r='6' fill='#94A3B8'/><circle cx='360' cy='234' r='6' fill='#94A3B8'/><circle cx='384' cy='212' r='6' fill='#94A3B8'/><circle cx='408' cy='234' r='6' fill='#94A3B8'/><circle cx='432' cy='212' r='6' fill='#94A3B8'/><circle cx='456' cy='234' r='6' fill='#94A3B8'/><circle cx='480' cy='212' r='6' fill='#94A3B8'/><circle cx='504' cy='234' r='6' fill='#94A3B8'/><circle cx='58' cy='234' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='106' cy='218' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='154' cy='234' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='202' cy='218' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='250' cy='234' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='346' cy='234' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='394' cy='218' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='442' cy='234' r='3.5' fill='#E11D48' fill-opacity='.55'/><circle cx='490' cy='218' r='3.5' fill='#E11D48' fill-opacity='.55'/><text x='42' y='252' font-size='12' text-anchor='start' fill='#475569' font-family='system-ui, sans-serif' font-weight='600'>métal</text><circle cx='298' cy='222' r='5.5' fill='#E11D48' fill-opacity='.35' stroke='#E11D48' stroke-width='1.2' stroke-dasharray='2 2'/><circle cx='298' cy='222' r='11' fill='none' stroke='#16A34A' stroke-width='2'/><line x1='298' y1='233' x2='298' y2='272' stroke='#16A34A' stroke-width='1' stroke-dasharray='3 3'/><text x='298' y='290' font-size='12' text-anchor='middle' fill='#16A34A' font-family='system-ui, sans-serif'><tspan font-family='Georgia, serif' font-weight='700' font-style='italic' font-size='16'>W</tspan><tspan font-family='Georgia, serif' font-weight='700' font-size='10' dy='3'>ext</tspan><tspan dy='-3'> : énergie minimale à fournir pour libérer cet électron, lié au métal</tspan></text><path d='M150,40 L150.0,40.0 L150.7,41.3 L151.1,43.0 L151.2,44.8 L151.1,46.8 L151.2,48.7 L151.5,50.3 L152.5,51.4 L154.3,51.9 L156.4,52.1 L158.7,52.2 L161.1,52.3 L163.3,52.4 L165.4,52.6 L167.2,53.1 L168.7,53.9 L169.7,55.0 L170.3,56.4 L170.5,58.2 L170.4,60.2 L170.1,62.4 L169.6,64.6 L169.2,66.9 L168.9,69.1 L168.8,71.1 L169.1,72.8 L169.7,74.2 L170.8,75.2 L172.3,76.0 L174.1,76.4 L176.2,76.6 L178.5,76.7 L180.9,76.8 L183.1,76.9 L185.2,77.2 L187.0,77.6 L188.4,78.4 L189.4,79.6 L190.0,81.0 L190.2,82.8 L190.1,84.8 L189.7,87.0 L189.3,89.3 L188.8,91.5 L188.5,93.7 L188.5,95.7 L188.8,97.4 L189.4,98.7 L190.5,99.8 L192.0,100.5 L193.9,100.9 L196.0,101.2 L198.3,101.2 L200.6,101.3 L202.9,101.4 L205.0,101.7 L206.7,102.2 L208.1,103.0 L209.1,104.1 L209.7,105.6 L209.8,107.4 L209.7,109.4 L209.4,111.6 L208.9,113.9 L208.5,116.2 L208.2,118.3 L208.1,120.3 L208.5,122.0 L209.2,123.3 L210.3,124.3 L211.8,125.0 L213.7,125.5 L215.8,125.7 L218.1,125.7 L220.4,125.8 L222.7,125.9 L224.7,126.2 L226.5,126.7 L227.8,127.6 L228.8,128.7 L229.3,130.2 L229.5,132.0 L229.4,134.0 L229.0,136.2 L228.5,138.5 L228.1,140.8 L227.8,142.9 L227.8,144.9 L228.1,146.5 L228.9,147.9 L230.0,148.9 L231.5,149.6 L233.4,150.0 L235.6,150.2 L237.9,150.3 L240.2,150.3 L242.5,150.4 L244.5,150.7 L246.2,151.3 L247.6,152.1 L248.5,153.3 L249.0,154.8 L249.2,156.6 L249.0,158.7 L248.6,160.9 L248.2,163.2 L247.7,165.4 L247.5,167.6 L247.5,169.5 L247.8,171.1 L248.6,172.5 L249.7,173.4 L251.3,174.1 L253.2,174.5 L255.4,174.7 L257.7,174.8 L260.0,174.8 L262.2,174.9 L264.3,175.3 L266.0,175.8 L267.3,176.7 L268.2,177.9 L268.7,179.4 L268.8,181.2 L268.6,183.3 L268.3,185.5 L267.8,187.8 L267.4,190.1 L267.1,192.2 L267.2,194.1 L267.5,195.7 L268.3,197.0 L270.0,197.6 L271.9,198.0 L273.9,198.3 L275.8,198.7 L277.6,199.2 L279.0,199.9 L280.2,201.0 L281.0,202.2 L281.6,203.7' fill='none' stroke='#2563EB' stroke-width='2.2'/><polygon points='288,212 277.2,206.5 285.0,200.3' fill='#2563EB'/><text x='150' y='104' font-size='17' text-anchor='end' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">hν</tspan></text><text x='150' y='122' font-size='11' text-anchor='end' fill='#2563EB' font-family='system-ui, sans-serif'>le photon cède toute</text><text x='150' y='136' font-size='11' text-anchor='end' fill='#2563EB' font-family='system-ui, sans-serif'>son énergie à un seul</text><text x='150' y='150' font-size='11' text-anchor='end' fill='#2563EB' font-family='system-ui, sans-serif'>électron</text><circle cx='312' cy='176' r='5.5' fill='#E11D48'/><line x1='316' y1='170' x2='357.4' y2='99.8' stroke='#E11D48' stroke-width='2.4'/><polygon points='362,92 360.7,104.0 352.1,98.9' fill='#E11D48'/><text x='372' y='96' font-size='17' text-anchor='start' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">E</tspan><tspan font-size="10" dy="3">c</tspan></text><text x='372' y='114' font-size='11' text-anchor='start' fill='#E11D48' font-family='system-ui, sans-serif'>énergie cinétique</text><text x='372' y='128' font-size='11' text-anchor='start' fill='#E11D48' font-family='system-ui, sans-serif'>de l’électron libéré</text><rect x='160' y='308' width='240' height='30' rx='15' fill='#F8FAFC' stroke='#CBD5E1'/><text x='280' y='328' font-size='15' text-anchor='middle' font-family='Georgia, serif' font-weight='700'><tspan fill='#2563EB' font-style='italic'>hν</tspan><tspan fill='#1E293B'> = </tspan><tspan fill='#16A34A' font-style='italic'>W</tspan><tspan fill='#16A34A' font-size='10' dy='3'>ext</tspan><tspan fill='#1E293B' dy='-3'> + </tspan><tspan fill='#E11D48' font-style='italic'>E</tspan><tspan fill='#E11D48' font-size='10' dy='3'>c</tspan></text></svg></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Si la fréquence dépasse un certain <span class="imp nt-hole">seuil</span>, le photon a assez d'énergie pour éjecter un électron du métal. Ce seuil correspond au <span class="imp nt-hole">travail d'extraction</span> $W_\text{ext}$&nbsp;: l'énergie <b>minimale</b> qu'il faut fournir à un électron pour le libérer du métal, auquel il est lié.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>À quelle allure de courbe s'attend-on si l'on trace l'énergie cinétique des électrons éjectés en fonction de la fréquence de la lumière&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<div class="nt-schemas">
<div class="nt-svgbox" style="max-width:440px; margin-left:auto; margin-right:auto;"><svg class='nt-svg' viewBox='0 0 440 290' role='img' aria-label="Bilan d’énergie : le photon apporte hν ; une partie, Wext, sert à extraire l’électron du métal ; le reste devient l’énergie cinétique Ec de l’électron libre"><defs><linearGradient id='gMet' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#BFDBFE'/><stop offset='1' stop-color='#FBCFE8'/></linearGradient></defs><line x1='70' y1='270' x2='70.0' y2='29.0' stroke='#1E293B' stroke-width='1.6'/><polygon points='70,20 75.0,31.0 65.0,31.0' fill='#1E293B'/><text x='80' y='26' font-size='11.5' text-anchor='start' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='600'>énergie de l’électron</text><rect x='90' y='150' width='80' height='110' fill='url(#gMet)'/><text x='130' y='278' font-size='11' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif'>dans le métal</text><line x1='70' y1='150' x2='400' y2='150' stroke='#94A3B8' stroke-dasharray='5 4'/><text x='62' y='154' font-size='12' text-anchor='end' fill='#475569' font-family='system-ui, sans-serif'>0</text><line x1='90' y1='220' x2='260' y2='220' stroke='#DB2777' stroke-width='2'/><text x='180' y='236' font-size='11' text-anchor='start' fill='#DB2777' font-family='system-ui, sans-serif'>électron lié au métal</text><line x1='200' y1='80' x2='400' y2='80' stroke='#E11D48' stroke-width='2'/><text x='300' y='72' font-size='11' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif'>électron libre, en mouvement</text><line x1='210' y1='220' x2='210.0' y2='91.0' stroke='#2563EB' stroke-width='2.4'/><polygon points='210,82 215.0,93.0 205.0,93.0' fill='#2563EB'/><text x='200' y='146' font-size='16' text-anchor='end' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">hν</tspan></text><line x1='260' y1='220' x2='260.0' y2='161.0' stroke='#16A34A' stroke-width='2.4'/><polygon points='260,152 265.0,163.0 255.0,163.0' fill='#16A34A'/><text x='272' y='192' font-size='15' text-anchor='start' fill='#16A34A' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">W</tspan><tspan font-size="10" dy="3">ext</tspan></text><line x1='330' y1='150' x2='330.0' y2='91.0' stroke='#E11D48' stroke-width='2.4'/><polygon points='330,82 335.0,93.0 325.0,93.0' fill='#E11D48'/><text x='342' y='120' font-size='16' text-anchor='start' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">E</tspan><tspan font-size="10" dy="3">c</tspan></text></svg></div>
<div>
<p>Le photon apporte l'énergie $h\nu$&nbsp;; une partie, $W_\text{ext}$, sert à extraire l'électron, et le reste devient son énergie cinétique&nbsp;:</p>
<p class="nt-center">${\color{#E11D48}{E_c}} = {\color{#2563EB}{h\nu}} - {\color{#16A34A}{W_\text{ext}}}$ si ${\color{#2563EB}{h\nu}} > {\color{#16A34A}{W_\text{ext}}}$, et 0 sinon.</p>
<p class="nt-note">Les électrons de conduction sont piégés dans le métal comme dans un puits de potentiel&nbsp;: $W_\text{ext}$ est l'énergie à fournir aux électrons <b>les moins liés</b> pour les en sortir. Les électrons plus profondément liés, ou qui subissent des chocs avant de sortir, repartent avec moins d'énergie&nbsp;: rigoureusement, $E_c = h\nu - W_\text{ext}$ est l'énergie cinétique <b>maximale</b> des électrons éjectés. C'est elle que mesure l'expérience de Millikan&nbsp;: la tension d'arrêt doit arrêter les électrons les plus rapides.</p>
</div>
</div>
<div class="nt-svgbox" style="max-width:470px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 470 300' role='img' aria-label="Énergie cinétique des électrons éjectés en fonction de la fréquence : nulle sous la fréquence seuil ν0 = Wext/h, puis une droite de pente h, dont le prolongement coupe l’axe vertical en −Wext"><line x1='60' y1='160' x2='431.0' y2='160.0' stroke='#1E293B' stroke-width='1.4'/><polygon points='440,160 429.0,165.0 429.0,155.0' fill='#1E293B'/><line x1='90' y1='290' x2='90.0' y2='29.0' stroke='#1E293B' stroke-width='1.4'/><polygon points='90,20 95.0,31.0 85.0,31.0' fill='#1E293B'/><text x='446' y='166' font-size='15' text-anchor='start' fill='#1E293B' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">ν</tspan></text><text x='98' y='26' font-size='15' text-anchor='start' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">E</tspan><tspan font-size="10" dy="3">c</tspan></text><line x1='90' y1='270' x2='200' y2='160' stroke='#94A3B8' stroke-width='1.6' stroke-dasharray='4 4'/><line x1='90' y1='160' x2='200' y2='160' stroke='#E11D48' stroke-width='3'/><line x1='200' y1='160' x2='330' y2='30' stroke='#E11D48' stroke-width='3'/><circle cx='200' cy='160' r='5' fill='#2563EB'/><text x='200' y='186' font-size='14' text-anchor='middle' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">ν</tspan><tspan font-size="10" dy="3">0</tspan><tspan dy="-3"> = </tspan><tspan font-style="italic">W</tspan><tspan font-size="10" dy="3">ext</tspan><tspan dy="-3">/</tspan><tspan font-style="italic">h</tspan></text><circle cx='90' cy='270' r='4.5' fill='#16A34A'/><text x='84' y='274' font-size='14' text-anchor='end' fill='#16A34A' font-family='Georgia, serif' font-weight='700'>−<tspan font-style="italic">W</tspan><tspan font-size="10" dy="3">ext</tspan></text><text x='300' y='70' font-size='12.5' text-anchor='start' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='700'>pente : <tspan font-style="italic">h</tspan></text><text x='145' y='150' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>pas d’électron</text></svg></div>
<p>On attend une demi-droite de pente $h$, à partir de la fréquence seuil $\nu_0 = \dfrac{W_\text{ext}}{h}$.</p>
</div>
</details>

### L'expérience de Millikan {.nt-h3}

<p class="nt-lead">Cette théorie contredit fortement la vision classique&nbsp;: selon la théorie ondulatoire de la lumière, admise jusqu'alors, l'énergie apportée par la lumière ne devrait pas dépendre de sa fréquence (de sa couleur), mais seulement de son intensité. Le physicien américain Robert Millikan, persuadé qu'Einstein se fourvoie, met au point une expérience pour réfuter sa théorie.</p>


<div class="nt-svgbox" style="max-width:580px; margin-left:auto; margin-right:auto;"><svg class='nt-svg' viewBox='0 0 460 330' role='img' aria-label="Principe de l’expérience de Millikan : un photon éjecte un électron de la cathode C ; le générateur impose une tension UCA entre la cathode et l’anode A, qui crée un champ électrique freinant l’électron"><rect x='80' y='40' width='300' height='150' rx='60' fill='rgba(226,232,240,.5)' stroke='#94A3B8' stroke-width='1.6'/><rect x='120' y='70' width='12' height='90' rx='3' fill='#475569'/><rect x='330' y='70' width='12' height='90' rx='3' fill='#475569'/><text x='126' y='62' font-size='12' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>cathode C</text><text x='336' y='62' font-size='12' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>anode A</text><path d='M40,20 L40.0,20.0 L40.9,21.2 L41.5,22.7 L41.9,24.4 L42.3,26.2 L42.7,27.9 L43.3,29.5 L44.4,30.5 L46.1,30.9 L48.0,31.1 L50.1,31.1 L52.2,31.1 L54.3,31.2 L56.2,31.4 L57.9,31.8 L59.4,32.5 L60.5,33.4 L61.3,34.8 L61.8,36.4 L62.1,38.2 L62.2,40.2 L62.2,42.3 L62.2,44.4 L62.4,46.4 L62.6,48.3 L63.2,49.8 L64.0,51.1 L65.2,52.1 L66.7,52.7 L68.4,53.1 L70.4,53.3 L72.4,53.3 L74.6,53.3 L76.6,53.4 L78.5,53.6 L80.2,54.0 L81.7,54.7 L82.8,55.7 L83.6,57.1 L84.1,58.7 L84.3,60.5 L84.4,62.6 L84.4,64.7 L84.5,66.8 L84.6,68.8 L84.9,70.6 L85.5,72.1 L86.3,73.4 L87.5,74.3 L89.0,75.0 L90.7,75.3 L92.7,75.5 L94.8,75.5 L96.9,75.5 L98.9,75.6 L100.9,75.8 L102.4,76.4 L103.4,77.5 L104.1,78.9 L104.6,80.5 L105.1,82.2 L105.5,83.9 L106.0,85.5 L106.8,86.9 L107.8,88.0' fill='none' stroke='#2563EB' stroke-width='2.2'/><polygon points='116,96 104.7,91.8 111.8,84.7' fill='#2563EB'/><text x='36' y='44' font-size='14' text-anchor='end' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">hν</tspan></text><circle cx='170' cy='115' r='5' fill='#E11D48'/><line x1='176' y1='115' x2='241.0' y2='115.0' stroke='#E11D48' stroke-width='2.2'/><polygon points='250,115 239.0,120.0 239.0,110.0' fill='#E11D48'/><text x='212' y='106' font-size='11' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif'>électron</text><line x1='160' y1='145' x2='291.0' y2='145.0' stroke='#7C3AED' stroke-width='1.6'/><polygon points='300,145 289.0,150.0 289.0,140.0' fill='#7C3AED'/><text x='230' y='165' font-size='14' text-anchor='middle' fill='#7C3AED' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">E</tspan></text><line x1='226' y1='152' x2='234' y2='152' stroke='#7C3AED' stroke-width='1.2'/><polygon points='236,152 232,149.5 232,154.5' fill='#7C3AED'/><polyline points='126,160 126,260 213,260' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='247,260 336,260 336,160' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='230' cy='260' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='230' y='265' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='206' y='250' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='254' y='250' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><line x1='316' y1='296' x2='154' y2='296' stroke='#E11D48' stroke-width='2.2' stroke-linecap='round'/><polygon points='146,296 157,291 157,301' fill='#E11D48'/><text x='231' y='318' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">U</tspan><tspan font-size="10" dy="3">CA</tspan></text><text x='232' y='22' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>tube à vide</text></svg></div>
<div>
<p>Pour différentes fréquences, on cherche la <b>tension minimale</b> à appliquer entre la cathode et l'anode pour que le courant soit nul&nbsp;: c'est la <span class="imp nt-hole">tension d'arrêt</span> $U_a$.</p>
<p>Les électrons sortent de la cathode avec une certaine énergie cinétique. Le courant ne peut être nul que si le travail de la force électrique a «&nbsp;consommé&nbsp;» toute cette énergie avant que les électrons atteignent l'anode.</p>
<p class="nt-note">La cathode est toujours l'électrode d'où sortent les électrons. C'est pourquoi, en chimie, c'est l'électrode de la réduction.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Démonstration&nbsp;: la tension d'arrêt</p>
<ol class="nt-steps">
<li><p>Théorème de l'énergie cinétique, entre la cathode C et l'anode A, distantes de $d$&nbsp;:</p>
<p class="nt-center">${\color{#E11D48}{\Delta E_c}} = W_{C\to A}(\vec{F}_e) = \vec{F}_e\cdot\overrightarrow{CA} = (-e)\,\vec{E}\cdot\overrightarrow{CA} = -e\,\dfrac{U_{CA}}{d}\times d = -e\,U_{CA}$</p>
<p>Le travail est bien <b>résistant</b> si $U_{CA} > 0$.</p></li>
<li><p>On veut que les électrons arrivent à l'anode avec une énergie cinétique nulle&nbsp;: ${\color{#E11D48}{E_{c,A}}} = 0$. La tension mesurée alors est la tension d'arrêt $U_a$, et</p>
<p class="nt-center">${\color{#E11D48}{\Delta E_c}} = {\color{#E11D48}{E_{c,A}}} - {\color{#E11D48}{E_{c,C}}} = -{\color{#E11D48}{E_{c,C}}} = -e\,U_a$</p></li>
<li><p>Or, d'après Einstein, ${\color{#E11D48}{E_{c,C}}} = {\color{#2563EB}{h\nu}} - {\color{#16A34A}{W_\text{ext}}}$. Si Einstein a raison, on doit donc trouver&nbsp;:</p>
<p class="nt-center">${\color{#E11D48}{e\,U_a}} = {\color{#2563EB}{h\nu}} - {\color{#16A34A}{W_\text{ext}}}$</p>
<p>La courbe de $eU_a$ en fonction de $\nu$ doit être une droite de pente $h$, qui coupe l'axe vertical en $-W_\text{ext}$. Millikan, lui, s'attendait à une tension d'arrêt <b>indépendante de la fréquence</b>, comme le prévoyait la théorie ondulatoire.</p></li>
</ol>
</div>

<div class="nt-lab" id="lab-pe">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'effet photoélectrique et l'expérience de Millikan</p>
<div class="nt-ctrl">Métal de la cathode&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="metal" value="0" checked><span>césium (2,14 eV)</span></label>
<label><input type="radio" name="metal" value="1"><span>sodium (2,36 eV)</span></label>
<label><input type="radio" name="metal" value="2"><span>calcium (2,87 eV)</span></label>
<label><input type="radio" name="metal" value="3"><span>zinc (4,31 eV)</span></label>
</div>
</div>
<canvas style="height:340px;" aria-label="Un tube à vide éclairé : les photons frappent la cathode, des électrons sont éjectés et freinés par la tension UCA ; à droite, le graphique de eUa en fonction de la fréquence"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Longueur d'onde&nbsp;: <b class="out-l"></b><input type="range" data-p="l" min="200" max="800" step="1" value="400"></label>
<label class="nt-ctrl">Intensité lumineuse&nbsp;: <input type="range" data-p="i" min="5" max="100" step="1" value="50"></label>
<label class="nt-ctrl">Tension $U_{CA}$&nbsp;: <b class="out-u"></b><input type="range" data-p="u" min="-1" max="4.5" step="0.01" value="0"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$E_c$ des électrons éjectés&nbsp;: <b class="out-ec"></b></span><span>courant&nbsp;: <b class="out-i"></b></span><span>$h$ mesurée&nbsp;: <b class="out-h"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="rec"><i class="fa-solid fa-location-dot"></i>&nbsp; Relever le point (ν, eU<sub>a</sub>)</button>
<button type="button" class="nt-btn" data-act="theo"><i class="fa-solid fa-chart-line"></i>&nbsp; Afficher la théorie</button>
<button type="button" class="nt-btn" data-act="clear"><i class="fa-solid fa-eraser"></i>&nbsp; Effacer les points</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Observez aussi qu'augmenter l'intensité lumineuse multiplie les électrons éjectés (le courant augmente), mais ne change pas leur énergie cinétique, ni donc la tension d'arrêt.</p>
</div>


<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Le verdict de l'expérience</p>
<p>Millikan a obtenu une droite parfaite, qui lui a permis de déterminer la constante de Planck avec une précision inégalée à l'époque. Einstein a reçu le prix Nobel de physique 1921, pour sa découverte de la loi de l'effet photoélectrique&nbsp;; Millikan l'a reçu en 1923.</p>
<p>Cela illustre bien qu'une bonne expérience n'est pas censée donner raison à celui qui la mène, mais seulement permettre de <b>trancher</b>.</p>
</div>

## La cellule photoélectrique {.nt-h2}

<div class="nt-schemas">
<div class="nt-figs" style="margin:0;"><figure><img src="https://presentationssite.github.io/phototube.png" alt="Une cellule photoélectrique : une cathode photoémissive et une électrode collectrice dans une ampoule de verre" loading="lazy" style="margin-top:0.5em; margin-bottom:0;max-width:300px;"><figcaption>une cellule photoélectrique</figcaption></figure></div>
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp">cellule photoélectrique</span> est un dispositif photosensible qui tire parti de l'effet photoélectrique&nbsp;: lorsqu'elle est soumise à un rayonnement, une <span class="imp nt-hole">photocathode</span> envoie des électrons sur une anode, ce qui crée un courant électrique.</p>
</div>
</div>

## Le photon {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp">photon</span> est une particule élémentaire&nbsp;: c'est le <span class="imp nt-hole">quantum d'énergie</span> associé aux ondes électromagnétiques.</p>
<ul class="nt-facts">
<li><b>Masse</b>&nbsp;: nulle (expérimentalement, inférieure à $\pu{E-54 kg}$).</li>
<li><b>Vitesse</b>&nbsp;: $c = \pu{299 792 458 m*s-1}$ dans le vide.</li>
<li><b>Énergie</b>&nbsp;: $E = h\nu = \dfrac{hc}{\lambda}$.</li>
</ul>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Énergie d'un photon</p>
<p class="nt-f-math">$$E = h\nu = \frac{hc}{\lambda}$$</p>
<div class="nt-f-units"><span>$\lambda$, la longueur d'onde dans le vide, en <b>m</b></span><span>$c = \pu{3,00E8 m*s-1}$</span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>L'électronvolt</p>
<p>À l'échelle des photons et des électrons, le joule est une unité bien trop grande. On utilise l'<b>électronvolt</b>&nbsp;: $\pu{1 eV} = \pu{1,60E-19 J}$, l'énergie que gagne un électron accéléré sous une tension de 1&nbsp;V. Un photon de lumière visible transporte de 1,6 à 3,3&nbsp;eV environ.</p>
</div>

<div class="nt-lab" id="lab-photon">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'énergie d'un photon</p>
<canvas style="height:405px;" aria-label="Le spectre électromagnétique, l'onde associée au photon choisi, et son énergie comparée à quelques seuils"></canvas>
<label class="nt-ctrl">Longueur d'onde λ&nbsp;: <b class="out-l"></b><input type="range" min="200" max="1300" step="1" value="550"></label>
<div class="nt-read" aria-live="polite"><span>ν = <b class="out-nu"></b></span><span>E = <b class="out-ej"></b></span><span>E = <b class="out-ev"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

## Absorption et émission de photons {.nt-h2}

<div class="nt-svgbox" style="max-width:600px; margin-left:auto; margin-right:auto;"><svg class='nt-svg' viewBox='0 0 420 260' role='img' aria-label="Absorption d’un photon : l’entité passe de l’état fondamental à un état excité ; émission d’un photon : elle redescend de l’état excité à l’état fondamental"><rect x='10' y='4' width='190' height='22' rx='11' fill='#E2E8F0'/><text x='105' y='20' font-size='12' text-anchor='middle' fill='#334155' font-family='system-ui, sans-serif' font-weight='700'>absorption d’un photon</text><line x1='24' y1='250' x2='24.0' y2='49.0' stroke='#1E293B' stroke-width='1.4'/><polygon points='24,40 29.0,51.0 19.0,51.0' fill='#1E293B'/><text x='34' y='48' font-size='14' text-anchor='start' fill='#1E293B' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">E</tspan></text><line x1='40' y1='90' x2='130' y2='90' stroke='#E11D48' stroke-width='2.4'/><text x='85' y='82' font-size='11' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif'>état excité</text><line x1='40' y1='220' x2='130' y2='220' stroke='#2563EB' stroke-width='2.4'/><text x='85' y='238' font-size='11' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif'>état fondamental</text><line x1='85' y1='218' x2='85.0' y2='102.0' stroke='#CA8A04' stroke-width='2.6'/><polygon points='85,93 90.0,104.0 80.0,104.0' fill='#CA8A04'/><path d='M190,170 L190.0,170.0 L188.6,169.4 L187.3,168.5 L186.1,167.2 L184.9,165.8 L183.6,164.6 L182.3,163.6 L180.9,163.3 L179.2,163.8 L177.4,164.7 L175.6,165.7 L173.8,166.8 L172.0,167.8 L170.2,168.6 L168.6,169.1 L167.0,169.3 L165.5,169.0 L164.1,168.3 L162.9,167.2 L161.7,165.8 L160.6,164.1 L159.5,162.3 L158.4,160.5 L157.2,158.8 L156.0,157.4 L154.8,156.4 L153.4,155.7 L151.9,155.5 L150.3,155.7 L148.6,156.2 L146.8,157.1 L145.0,158.1 L143.2,159.2 L141.4,160.2 L139.7,161.0 L138.0,161.5 L136.4,161.7 L135.0,161.4 L133.6,160.6 L132.3,159.5 L131.2,157.8 L130.1,156.1 L128.9,154.6 L127.7,153.5 L126.3,152.7 L124.9,152.2 L123.3,152.1 L121.8,152.2 L120.2,152.4' fill='none' stroke='#CA8A04' stroke-width='2.2'/><polygon points='110,150 121.9,147.8 119.5,157.5' fill='#CA8A04'/><text x='160' y='196' font-size='14' text-anchor='middle' fill='#CA8A04' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">hν</tspan></text><rect x='220' y='4' width='190' height='22' rx='11' fill='#E2E8F0'/><text x='315' y='20' font-size='12' text-anchor='middle' fill='#334155' font-family='system-ui, sans-serif' font-weight='700'>émission d’un photon</text><line x1='234' y1='250' x2='234.0' y2='49.0' stroke='#1E293B' stroke-width='1.4'/><polygon points='234,40 239.0,51.0 229.0,51.0' fill='#1E293B'/><text x='244' y='48' font-size='14' text-anchor='start' fill='#1E293B' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">E</tspan></text><line x1='250' y1='90' x2='340' y2='90' stroke='#E11D48' stroke-width='2.4'/><text x='295' y='82' font-size='11' text-anchor='middle' fill='#E11D48' font-family='system-ui, sans-serif'>état excité</text><line x1='250' y1='220' x2='340' y2='220' stroke='#2563EB' stroke-width='2.4'/><text x='295' y='238' font-size='11' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif'>état fondamental</text><line x1='295' y1='92' x2='295.0' y2='208.0' stroke='#CA8A04' stroke-width='2.6'/><polygon points='295,217 290.0,206.0 300.0,206.0' fill='#CA8A04'/><path d='M320,150 L320.0,150.0 L321.4,150.6 L322.7,151.5 L323.9,152.8 L325.1,154.2 L326.4,155.4 L327.7,156.4 L329.1,156.7 L330.8,156.2 L332.6,155.3 L334.4,154.3 L336.2,153.2 L338.0,152.2 L339.8,151.4 L341.4,150.9 L343.0,150.7 L344.5,151.0 L345.9,151.7 L347.1,152.8 L348.3,154.2 L349.4,155.9 L350.5,157.7 L351.6,159.5 L352.8,161.2 L354.0,162.6 L355.2,163.6 L356.6,164.3 L358.1,164.5 L359.7,164.3 L361.4,163.8 L363.2,162.9 L365.0,161.9 L366.8,160.8 L368.6,159.8 L370.3,159.0 L372.0,158.5 L373.6,158.3 L375.0,158.6 L376.4,159.4 L377.7,160.5 L378.8,162.2 L379.9,163.9 L381.1,165.4 L382.3,166.5 L383.7,167.3 L385.1,167.8 L386.7,167.9 L388.2,167.8 L389.8,167.6' fill='none' stroke='#CA8A04' stroke-width='2.2'/><polygon points='400,170 388.1,172.2 390.5,162.5' fill='#CA8A04'/><text x='370' y='196' font-size='14' text-anchor='middle' fill='#CA8A04' font-family='Georgia, serif' font-weight='700'><tspan font-style="italic">hν</tspan></text></svg></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Comme les atomes, toutes les entités (molécules, ions, noyaux), ainsi que leurs assemblages (métaux, semi-conducteurs…), possèdent des <span class="imp nt-hole">niveaux d'énergie quantifiés</span>. Ils forment parfois des <span class="imp nt-hole">bandes d'énergie</span>, constituées de très nombreux niveaux très proches.</p>
</div>

{{< youtube-plus id="EWLgeBVY-08" ratio="16x9" width="500" shadow=true rounded=true >}}

<div class="nt-svgbox" style="max-width:480px; margin-left:auto; margin-right:auto;"><svg class='nt-svg' viewBox='0 0 440 290' role='img' aria-label="Effet photoélectrique interne : un photon d’énergie hν supérieure au gap est absorbé par un électron du haut de la bande de valence, qui passe au bas de la bande de conduction, en laissant un trou dans la bande de valence"><defs><linearGradient id='gCond' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#FEE2E2'/><stop offset='1' stop-color='#FCA5A5'/></linearGradient><linearGradient id='gVal' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#93C5FD'/><stop offset='1' stop-color='#DBEAFE'/></linearGradient></defs><line x1='26.0' y1='280.0' x2='26.0' y2='22.0' stroke='#1E293B' stroke-width='1.4'/><polygon points='26.0,14.0 30.5,24.0 21.5,24.0' fill='#1E293B'/><text x='36' y='24' font-size='15' text-anchor='start' fill='#1E293B' font-family='Georgia, serif' font-style='italic'>E</text><rect x='96' y='34' width='234' height='74' rx='6' fill='url(#gCond)'/><line x1='96' y1='108' x2='330' y2='108' stroke='#DC2626' stroke-width='1.6'/><rect x='96' y='192' width='234' height='74' rx='6' fill='url(#gVal)'/><line x1='96' y1='192' x2='330' y2='192' stroke='#2563EB' stroke-width='1.6'/><text x='170.0' y='64' font-size='13' text-anchor='middle' fill='#B91C1C' font-family='system-ui, sans-serif'>bande de conduction</text><text x='170.0' y='244' font-size='13' text-anchor='middle' fill='#1D4ED8' font-family='system-ui, sans-serif'>bande de valence</text><line x1='52' y1='108' x2='96' y2='108' stroke='#16A34A' stroke-width='1' stroke-dasharray='3 3'/><line x1='52' y1='192' x2='96' y2='192' stroke='#16A34A' stroke-width='1' stroke-dasharray='3 3'/><line x1='60.0' y1='192.0' x2='60.0' y2='116.0' stroke='#16A34A' stroke-width='1.6'/><polygon points='60.0,108.0 64.5,118.0 55.5,118.0' fill='#16A34A'/><line x1='60.0' y1='108.0' x2='60.0' y2='184.0' stroke='#16A34A' stroke-width='1.6'/><polygon points='60.0,192.0 55.5,182.0 64.5,182.0' fill='#16A34A'/><text x='70' y='155.0' font-size='15' text-anchor='start' fill='#16A34A' font-family='Georgia, serif' font-style='italic'>E<tspan font-size='10' dy='3'>gap</tspan></text><line x1='256.0' y1='193.0' x2='256.0' y2='115.0' stroke='#CA8A04' stroke-width='2.2'/><polygon points='256.0,107.0 260.5,117.0 251.5,117.0' fill='#CA8A04'/><circle cx='256' cy='99' r='6' fill='#1E293B'/><line x1='253' y1='99' x2='259' y2='99' stroke='#fff' stroke-width='1.6' stroke-linecap='round'/><circle cx='256' cy='201' r='6' fill='#fff' stroke='#1E293B' stroke-width='1.6'/><path d='M410,132 L410.0,132.0 L408.5,132.3 L406.8,132.1 L405.0,131.7 L403.2,131.1 L401.4,130.5 L399.7,130.4 L398.3,131.0 L397.3,132.6 L396.5,134.5 L395.7,136.7 L395.0,138.9 L394.2,141.0 L393.3,142.9 L392.3,144.5 L391.2,145.6 L389.8,146.3 L388.3,146.4 L386.5,146.1 L384.7,145.4 L382.7,144.5 L380.6,143.4 L378.6,142.3 L376.6,141.3 L374.7,140.7 L373.0,140.4 L371.5,140.6 L370.2,141.3 L369.0,142.5 L368.0,144.1 L367.2,146.1 L366.4,148.2 L365.7,150.4 L364.9,152.6 L364.0,154.5 L363.0,156.0 L361.8,157.1 L360.5,157.7 L358.9,157.9 L357.2,157.5 L355.3,156.8 L353.3,155.8 L351.2,154.7 L349.2,153.6 L347.2,152.7 L345.4,152.1 L343.7,151.8 L342.1,152.1 L340.8,152.8 L339.7,154.0 L338.7,155.6 L337.9,157.6 L337.1,159.8 L336.4,162.0 L335.6,164.1 L334.7,166.0 L333.7,167.5 L332.5,168.6 L331.1,169.2 L329.6,169.3 L327.8,168.9 L325.9,168.2 L323.9,167.2 L321.9,166.1 L319.8,165.0 L317.9,164.1 L316.0,163.5 L314.3,163.2 L312.8,163.5 L311.5,164.3 L310.4,165.5 L309.4,167.2 L308.6,169.1 L307.8,171.3 L307.1,173.5 L306.3,175.6 L305.4,177.5 L304.4,179.0 L303.2,180.1 L301.8,180.6 L300.2,180.7 L298.4,180.3 L296.5,179.6 L294.5,178.6 L292.5,177.4 L290.4,176.4 L288.5,175.5 L286.6,174.9 L285.0,174.7 L283.6,175.3 L282.5,176.6 L281.5,178.3 L280.6,180.0 L279.6,181.7 L278.6,183.1 L277.4,184.2 L276.1,184.9 L274.6,185.3' fill='none' stroke='#CA8A04' stroke-width='2.2'/><polygon points='264.0,189.0 272.4,180.3 276.1,189.7' fill='#CA8A04'/><text x='392' y='166' font-size='16' text-anchor='middle' fill='#CA8A04' font-family='Georgia, serif' font-style='italic'>hν</text><line x1='265' y1='99' x2='344' y2='99' stroke='#64748B' stroke-width='1'/><text x='350' y='103.5' font-size='13' text-anchor='start' fill='#1E293B' font-family='system-ui, sans-serif'>électron</text><line x1='265' y1='201' x2='344' y2='201' stroke='#64748B' stroke-width='1'/><text x='350' y='205.5' font-size='13' text-anchor='start' fill='#1E293B' font-family='system-ui, sans-serif'>trou</text></svg></div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>L'effet photoélectrique interne</p>
<p>Il concerne les isolants et les semi-conducteurs. L'électron n'est pas arraché au matériau&nbsp;: il est <span class="imp nt-hole">promu de la bande de valence à la bande de conduction</span>, après absorption d'un photon d'énergie supérieure au gap&nbsp;: $h\nu \geq E_\text{gap}$.</p>
<p>Pour ces matériaux, l'énergie du gap joue donc le rôle du travail d'extraction.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Il y a alors création d'une <span class="imp nt-hole">paire électron-trou</span>, qui augmente le nombre de porteurs de charge, donc la conductivité électrique du matériau. On parle de <span class="imp nt-hole">photocourant</span>.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>À savoir&nbsp;: le gap du silicium</p>
<p>Le gap du silicium, le semi-conducteur le plus utilisé, vaut environ $\pu{1 eV}$ ($\pu{1,12 eV}$ précisément). La longueur d'onde $\lambda_\text{gap}$ d'un photon dont l'énergie suffit tout juste à faire franchir le gap à un électron vaut donc</p>
<p class="nt-center">$\lambda_\text{gap} = \dfrac{hc}{E_\text{gap}} = \dfrac{\pu{6,63E-34} \times \pu{3,00E8}}{\pu{1,12} \times \pu{1,60E-19}} \approx \pu{1,1E-6 m}$, soit environ 1&nbsp;µm.</p>
<p>$\lambda_\text{gap}$ est dans le <b>proche infrarouge</b>, un peu au-delà de 800&nbsp;nm.</p>
<p>Bien se rappeler que $E$ augmente quand $\lambda$ diminue&nbsp;: ce sont les photons de longueur d'onde <b>inférieure</b> à $\lambda_\text{gap}$ qui permettent de franchir le gap. C'est donc le cas de tous les photons visibles&nbsp;! Or le visible correspond justement aux longueurs d'onde où la puissance rayonnée par le Soleil est la plus grande&nbsp;: le silicium est bien adapté aux cellules photovoltaïques.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention&nbsp;: deux effets à ne pas confondre</p>
<p>Les exercices de bac, et le programme lui-même, semblent parfois confondre en un seul concept deux phénomènes pourtant distincts&nbsp;:</p>
<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th></th><th>Effet photoélectrique externe</th><th>Effet photoélectrique interne</th></tr></thead>
<tbody>
<tr><td><b>Matériau</b></td><td>un métal</td><td>un semi-conducteur ou un isolant</td></tr>
<tr><td><b>Seuil</b></td><td>le travail d'extraction $W_\text{ext}$</td><td>l'énergie du gap $E_\text{gap}$</td></tr>
<tr><td><b>L'électron…</b></td><td>est <b>extrait</b> du métal</td><td>passe de la bande de valence à la bande de conduction, et <b>reste dans le matériau</b></td></tr>
<tr><td><b>Effet produit</b></td><td>des électrons libres, collectés par une anode</td><td>une paire électron-trou, qui augmente la conductivité</td></tr>
<tr><td><b>Exemples</b></td><td>cellule photoélectrique, photomultiplicateur</td><td>photodiode, cellule photovoltaïque, photorésistance, capteur CMOS</td></tr>
</tbody>
</table>
</div>
<p>Dans les deux cas, la logique est la même&nbsp;: un photon n'agit que si son énergie $h\nu$ dépasse un seuil.</p>
</div>

## Les applications {.nt-h2}

<p class="nt-lead">De nombreux dispositifs mettent en œuvre une interaction entre les photons et la matière.</p>

### Convertir la lumière en signal électrique&nbsp;: la détection {.nt-h3}

<ul class="nt-facts">
<li><b>Photodiodes et phototransistors</b>&nbsp;: ils utilisent l'effet photoélectrique interne dans une jonction. Un photon d'énergie supérieure au gap crée une paire électron-trou, qui génère un photocourant. Ce sont des sortes d'interrupteurs sensibles à la lumière.</li>
<li><b>Cellules photovoltaïques</b>&nbsp;: semblables aux photodiodes, mais optimisées pour convertir l'énergie solaire en énergie électrique.</li>
<li><b>Capteurs CCD et CMOS</b>&nbsp;: des matrices de photodétecteurs en silicium, qui convertissent les photons en charges, stockées dans des «&nbsp;puits de potentiel&nbsp;» pour former une image numérique.</li>
<li><b>Photomultiplicateurs</b>&nbsp;: basés sur l'effet photoélectrique externe (l'électron est émis hors de la matière), suivi d'une cascade d'émissions secondaires qui amplifie le signal.</li>
<li><b>Photorésistances</b> (LDR)&nbsp;: elles exploitent l'effet photoélectrique interne, qui augmente leur conductivité.</li>
</ul>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">L'effet externe a-t-il encore un avenir&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Les composants à semi-conducteurs (photodiodes, CMOS) ont largement remplacé les cellules à effet photoélectrique externe dans l'électronique courante. Mais celles-ci restent irremplaçables là où la sensibilité extrême et la rapidité sont critiques.</p>
<ul class="nt-facts">
<li><b>Le tube photomultiplicateur.</b> Un photon frappe une photocathode&nbsp;; l'électron émis est accéléré vers une série de dynodes, qui multiplient le signal en cascade. Ces tubes détectent un <b>photon unique</b>, avec un gain qui peut atteindre $10^6$ à $10^8$. On les trouve dans les détecteurs de neutrinos (comme Super-Kamiokande), dans les scanners médicaux PET, et en astronomie.</li>
<li><b>La vision nocturne.</b> Dans les jumelles à intensification de lumière, la lumière résiduelle frappe une photocathode&nbsp;; les électrons émis sont multipliés, puis projetés sur un écran phosphorescent qui recrée l'image, sans aucun délai.</li>
<li><b>La détection des ultraviolets.</b> En choisissant le matériau de la photocathode, on fabrique des tubes qui ne réagissent qu'aux UV («&nbsp;aveugles au Soleil&nbsp;»)&nbsp;: détection de flammes, étude de la couche d'ozone, spectroscopie.</li>
</ul>
</div>
</details>

<div class="nt-lab" id="lab-ldr">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Une photorésistance comme capteur de luminosité</p>
<div class="nt-svgbox nt-ldr-svg" style="max-width:420px; margin-left:auto; margin-right:auto;"></div>
<div class="nt-ctrls">
<label class="nt-ctrl">Éclairement&nbsp;: <b class="out-lux"></b><input type="range" data-p="lux" min="0" max="4" step="0.02" value="2.6"></label>
<label class="nt-ctrl">Résistance variable&nbsp;: <b class="out-pot"></b><input type="range" data-p="pot" min="1" max="10" step="0.1" value="10"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$R_\text{LDR}$ = <b class="out-r"></b></span><span>$U_{BE}$ = <b class="out-u"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Comment fonctionne ce montage&nbsp;?</span></summary>
<div class="nt-d-body">
<p>La résistance variable et la photorésistance forment un <b>diviseur de tension</b>&nbsp;: la tension aux bornes de la photorésistance, qui est aussi la tension $U_{BE}$ entre la base et l'émetteur du transistor, vaut</p>
<p class="nt-center">$U_{BE} = U_\text{pile}\times\dfrac{R_\text{LDR}}{R_\text{LDR} + R_\text{pot}}$</p>
<p>Le transistor ne devient passant (courant possible entre le collecteur et l'émetteur, donc dans la DEL) que si $U_{BE}$ dépasse environ 0,7&nbsp;V, la tension de seuil de la jonction base-émetteur. Dans l'obscurité, $R_\text{LDR}$ devient grande, $U_{BE}$ augmente et la DEL s'allume&nbsp;: c'est une <b>veilleuse automatique</b>. La résistance variable règle le seuil de déclenchement.</p>
<p>En échangeant la photorésistance et la résistance variable, la DEL s'allume au contraire à la lumière&nbsp;: c'est une <b>lampe de tiroir</b>.</p>
</div>
</details>

### Convertir de l'énergie en lumière&nbsp;: l'émission {.nt-h3}

<ul class="nt-facts">
<li><b>Diodes électroluminescentes</b> (DEL)&nbsp;: elles reposent sur la recombinaison radiative d'électrons et de trous au sein d'un semi-conducteur (émission spontanée).</li>
<li><b>Laser</b> (<i>Light Amplification by Stimulated Emission of Radiation</i>)&nbsp;: il exploite l'émission stimulée. Un photon incident incite un atome excité à émettre un second photon identique&nbsp;: même phase, même direction, même fréquence.</li>
<li><b>Tubes à décharge et lampes à vapeur spectrale</b>&nbsp;: une décharge électrique excite les atomes d'un gaz (néon, mercure, sodium), qui se désexcitent en émettant un spectre de raies.</li>
</ul>


<p class="nt-lead">Et une application familière en chimie&nbsp;: la spectroscopie UV-visible et infrarouge, qui repose sur l'absorption de photons par les molécules.</p>

<div class="nt-lab nt-quizlab" id="quiz-app">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Quelle interaction entre la lumière et la matière&nbsp;?</p>
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

## Le rendement d'une cellule photovoltaïque {.nt-h2}

<p class="nt-lead">Pour tracer la caractéristique $I = f(U)$ d'une cellule photovoltaïque, on la fait débiter dans une résistance variable, et on mesure l'intensité $I$ et la tension $U$ pour différentes valeurs de la résistance.</p>

<div class="nt-svgbox" style="max-width:480px; margin-left:auto; margin-right:auto;"><svg class='nt-svg' viewBox='0 0 340 270' role='img' aria-label="Montage pour tracer la caractéristique d’une cellule photovoltaïque : la cellule, éclairée, débite dans une résistance variable R ; un ampèremètre en série mesure I, un voltmètre en dérivation mesure U"><polyline points='60,50 300,50 300,250 60,250 60,50' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='200,50 200,250' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='60' cy='150' r='21' fill='#fff' stroke='#1E293B' stroke-width='2'/><line x1='60' y1='129' x2='60' y2='145' stroke='#1E293B' stroke-width='2'/><line x1='60' y1='155' x2='60' y2='171' stroke='#1E293B' stroke-width='2'/><line x1='48' y1='145' x2='72' y2='145' stroke='#1E293B' stroke-width='2'/><line x1='54' y1='155' x2='66' y2='155' stroke='#1E293B' stroke-width='3.4'/><text x='33' y='146' font-size='14' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><line x1='83.3' y1='123.7' x2='75.5' y2='131.5' stroke='#F59E0B' stroke-width='1.6'/><polygon points='72,135 74.1,128.6 78.4,132.9' fill='#F59E0B'/><line x1='93.3' y1='123.7' x2='85.5' y2='131.5' stroke='#F59E0B' stroke-width='1.6'/><polygon points='82,135 84.1,128.6 88.4,132.9' fill='#F59E0B'/><circle cx='130' cy='50' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='130' y='55' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='110' y='44' font-size='10.5' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='150' y='44' font-size='10.5' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><circle cx='200' cy='150' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='200' y='155' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='210' y='134' font-size='10.5' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='210' y='174' font-size='10.5' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><rect x='292' y='130' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><line x1='282' y1='170' x2='312.1' y2='134.6' stroke='#1E293B' stroke-width='1.6'/><polygon points='316,130 313.2,139.4 307.1,134.3' fill='#1E293B'/><circle cx='200' cy='50' r='3.6' fill='#1E293B'/><circle cx='200' cy='250' r='3.6' fill='#1E293B'/><g transform='translate(92,50) rotate(0)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><text x='92' y='40' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan></text><line x1='22' y1='196' x2='22' y2='112' stroke='#2563EB' stroke-width='2.2' stroke-linecap='round'/><polygon points='22,104 27,115 17,115' fill='#2563EB'/><text x='14' y='150' font-size='14' text-anchor='end' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan></text><text x='318' y='154' font-size='13' text-anchor='start' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>R</text><text x='104' y='158' font-size='10.5' text-anchor='start' fill='#475569' font-family='system-ui, sans-serif'>cellule</text></svg></div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Puissance électrique</p>
<p class="nt-f-math">$$P = U\times I$$</p>
<div class="nt-f-units"><span>$P$ en <b>W</b></span><span>$U$ en <b>V</b></span><span>$I$ en <b>A</b></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Puissance lumineuse reçue</p>
<p class="nt-f-math">$$P_\text{lum} = G\times S$$</p>
<div class="nt-f-units"><span>$G$, l'irradiance, en <b>$\pu{W*m-2}$</b></span><span>$S$ en <b>m²</b></span></div>
</div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Rendement</p>
<p>Le <span class="imp">rendement</span> $\eta$ de la cellule est le rapport entre la <span class="imp nt-hole">puissance électrique maximale</span> qu'elle peut délivrer, pour une irradiance donnée, et la <span class="imp nt-hole">puissance lumineuse reçue</span>, pour cette même irradiance&nbsp;:</p>
<p class="nt-center">$\eta = \dfrac{P_\text{utile}}{P_\text{reçue}} = \dfrac{P_\text{max}}{P_\text{lum}}$</p>
</div>

<div class="nt-lab" id="lab-pv">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Caractéristique, puissance et rendement d'une cellule photovoltaïque</p>
<canvas style="height:300px;" aria-label="Caractéristiques I = f(U) et P = f(U) d'une cellule photovoltaïque pour différentes irradiances, avec le point de fonctionnement et la puissance maximale"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Irradiance $G$&nbsp;: <b class="out-G"></b><input type="range" data-p="G" min="100" max="1000" step="50" value="1000"></label>
<label class="nt-ctrl">Résistance de charge $R$&nbsp;: <b class="out-R"></b><input type="range" data-p="R" min="-2" max="0.3" step="0.005" value="-1.4"></label>
</div>
<div class="nt-read" aria-live="polite"><span>U = <b class="out-U"></b></span><span>I = <b class="out-I"></b></span><span>P = <b class="out-P"></b></span><span>η = P / P<sub>lum</sub> = <b class="out-eta"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Modélisation d'une cellule carrée de 6 pouces de côté (15,6&nbsp;cm), soit $S$ = 0,0243&nbsp;m². Les courbes grises correspondent aux irradiances de 200 à 1&nbsp;000&nbsp;$\pu{W*m-2}$.</p>
</div>

<div class="nt-svgbox" style="max-width:640px; margin-left:auto; margin-right:auto;"><svg class='nt-svg' viewBox='0 0 620 280' role='img' aria-label="Chaîne énergétique d’une cellule photovoltaïque : elle reçoit de l’énergie radiative, en convertit une partie en énergie électrique, et perd le reste sous forme d’énergie thermique"><defs><radialGradient id='gCel' cx='.4' cy='.35' r='.75'><stop offset='0' stop-color='#4ADE80'/><stop offset='1' stop-color='#15803D'/></radialGradient><linearGradient id='gRad' x1='0' x2='1'><stop offset='0' stop-color='#FDE68A'/><stop offset='1' stop-color='#F59E0B'/></linearGradient><linearGradient id='gEle' x1='0' x2='1'><stop offset='0' stop-color='#60A5FA'/><stop offset='1' stop-color='#1D4ED8'/></linearGradient><linearGradient id='gThe' x1='0' x2='1'><stop offset='0' stop-color='#F87171'/><stop offset='1' stop-color='#B91C1C'/></linearGradient></defs><path d='M10,78 L178,78 L178,56 L222,105 L178,154 L178,132 L10,132 Z' fill='url(#gRad)'/><text x='96' y='102' font-size='13.5' text-anchor='middle' fill='#78350F' font-family='system-ui, sans-serif' font-weight='700'>énergie</text><text x='96' y='119' font-size='13.5' text-anchor='middle' fill='#78350F' font-family='system-ui, sans-serif' font-weight='700'>radiative</text><path d='M398,78 L566,78 L566,56 L610,105 L566,154 L566,132 L398,132 Z' fill='url(#gEle)'/><text x='484' y='102' font-size='13.5' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif' font-weight='700'>énergie</text><text x='484' y='119' font-size='13.5' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif' font-weight='700'>électrique</text><g transform='translate(355,148) rotate(42)'><path d='M0,-13 L74,-13 L74,-26 L104,0 L74,26 L74,13 L0,13 Z' fill='url(#gThe)'/></g><circle cx='310' cy='105' r='86' fill='url(#gCel)'/><circle cx='310' cy='105' r='86' fill='none' stroke='#fff' stroke-opacity='.35' stroke-width='3'/><text x='310' y='100' font-size='17' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif' font-weight='800'>cellule</text><text x='310' y='122' font-size='16' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif' font-weight='800'>photovoltaïque</text><text x='452' y='250' font-size='13.5' text-anchor='start' fill='#B91C1C' font-family='system-ui, sans-serif' font-weight='700'>énergie thermique</text><text x='452' y='267' font-size='12' text-anchor='start' fill='#B91C1C' font-family='system-ui, sans-serif'>(pertes)</text></svg></div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarques</p>
<ul class="nt-facts">
<li>Dans notre modélisation, on trouve $\eta \approx 18{,}5$&nbsp;% pour $G = \pu{1000 W*m-2}$.</li>
<li>Le rendement n'est pas constant&nbsp;: il dépend de l'irradiance (vérifiez-le dans l'animation) et de la température.</li>
<li>Les cellules au silicium du commerce ont des rendements de l'ordre de 20&nbsp;%&nbsp;; les meilleures cellules de laboratoire, à plusieurs couches, dépassent 40&nbsp;%.</li>
</ul>
</div>

## Entraînement {.nt-h2}

<div class="nt-lab nt-trainer" id="lab-calc">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Photons et effet photoélectrique</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<div class="nt-qvis" aria-live="polite"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-zone"><div class="nt-tr-ans"><span class="nt-champ"><label for="ph-rep">Réponse&nbsp;:</label><input id="ph-rep" type="text" inputmode="decimal"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

## Testez-vous {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-final">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur les interactions entre la lumière et la matière</p>
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

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function nb(x, sig) { if (x === 0) { return '0'; } var a = Math.abs(x), d = Math.max(0, (sig || 3) - 1 - Math.floor(Math.log10(a))); var s = x.toFixed(Math.min(d, 6)), p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '\u202f'); return p.join(',').replace('-', '\u2212'); }
  function sci(x, sig) { if (x === 0) { return '0'; } var e = Math.floor(Math.log10(Math.abs(x))), m = x / Math.pow(10, e); if (Math.abs(m) >= 9.995) { m /= 10; e++; } return fr(m, (sig || 3) - 1) + ' × 10' + String(e).replace('-', '\u207b').replace(/\d/g, function (d) { return '\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079'[+d]; }); }   /* notation scientifique en texte simple */
  function sciH(x, sig) { var e = Math.floor(Math.log10(Math.abs(x))), m = x / Math.pow(10, e); if (Math.abs(m) >= 9.995) { m /= 10; e++; } return fr(m, (sig || 3) - 1) + '&nbsp;×&nbsp;10<sup>' + String(e).replace('-', '\u2212') + '</sup>'; }   /* notation scientifique en HTML */
  function canvasCtx(cv) { var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight; cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); return { ctx: ctx, w: w, h: h }; }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function watch(cv, cb) { if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }).observe(cv); } else { cb(true); } }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function num(s) { return parseFloat(String(s).replace(',', '.').replace(/\s/g, '').replace(/×10\^?/, 'e')); }
  function bilanTxt(r) { return r === 1 ? 'Parfait&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;!' : (r >= 0.5 ? 'C\u2019est un bon début&nbsp;: relisez les cas manqués.' : 'Relisez le cours, puis recommencez.')); }
  function txt(c, s, x, y, color, font, align) { c.save(); c.font = font || '12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round'; c.lineWidth = 4; c.strokeStyle = 'rgba(255,255,255,.92)'; c.strokeText(s, x, y); c.fillStyle = color; c.fillText(s, x, y); c.restore(); }
  function txtN(c, s, x, y, color, font, align) { c.save(); c.font = font || '12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.fillStyle = color; c.fillText(s, x, y); c.restore(); }   /* sans halo, pour les fonds sombres */
  function rr(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
  var H = 6.63e-34, C = 3.00e8, QE = 1.60e-19;
  /* couleur perçue d'une longueur d'onde (nm) ; violet pâle pour l'UV, rouge sombre pour l'IR */
  function couleur(l) {
    var r = 0, g = 0, b = 0;
    if (l < 380) { return 'rgb(167,139,250)'; } if (l > 750) { return 'rgb(127,29,29)'; }
    if (l < 440) { r = -(l - 440) / 60; b = 1; } else if (l < 490) { g = (l - 440) / 50; b = 1; } else if (l < 510) { g = 1; b = -(l - 510) / 20; } else if (l < 580) { r = (l - 510) / 70; g = 1; } else if (l < 645) { r = 1; g = -(l - 645) / 65; } else { r = 1; }
    var f = l < 420 ? 0.3 + 0.7 * (l - 380) / 40 : (l > 700 ? 0.3 + 0.7 * (750 - l) / 50 : 1);
    return 'rgb(' + [r, g, b].map(function (v) { return Math.round(255 * Math.pow(v * f, 0.8)); }).join(',') + ')';
  }
  var METAUX = [['césium', 2.14, '#B45309'], ['sodium', 2.36, '#64748B'], ['calcium', 2.87, '#94A3B8'], ['zinc', 4.31, '#475569']];
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
    function fleches(x, y, ang, col) {   /* deux flèches de lumière qui arrivent, pointes en (x, y) */
      var s = '', c = col || '#F59E0B';
      [[-5, 0], [5, 0]].forEach(function (d) { var x2 = x + d[0], y2 = y + d[1], x1 = x2 - 16 * Math.cos(ang), y1 = y2 - 16 * Math.sin(ang);
        s += "<line x1='" + n(x1) + "' y1='" + n(y1) + "' x2='" + n(x2 - 5 * Math.cos(ang)) + "' y2='" + n(y2 - 5 * Math.sin(ang)) + "' stroke='" + c + "' stroke-width='1.6'/><polygon points='" + n(x2) + ',' + n(y2) + ' ' + n(x2 - 6 * Math.cos(ang) - 3 * Math.sin(ang)) + ',' + n(y2 - 6 * Math.sin(ang) + 3 * Math.cos(ang)) + ' ' + n(x2 - 6 * Math.cos(ang) + 3 * Math.sin(ang)) + ',' + n(y2 - 6 * Math.sin(ang) - 3 * Math.cos(ang)) + "' fill='" + c + "'/>"; });
      return s;
    }
    function pv(x, y, cote) {   /* cellule photovoltaïque (branche verticale) ; cote : côté d'où arrive la lumière (1 : droite, −1 : gauche) */
      var k = cote || 1, s = "<circle cx='" + n(x) + "' cy='" + n(y) + "' r='21' fill='#fff' stroke='" + INK + "' stroke-width='2'/>";
      s += "<line x1='" + n(x) + "' y1='" + n(y - 21) + "' x2='" + n(x) + "' y2='" + n(y - 5) + "' stroke='" + INK + "' stroke-width='2'/><line x1='" + n(x) + "' y1='" + n(y + 5) + "' x2='" + n(x) + "' y2='" + n(y + 21) + "' stroke='" + INK + "' stroke-width='2'/>";
      s += "<line x1='" + n(x - 12) + "' y1='" + n(y - 5) + "' x2='" + n(x + 12) + "' y2='" + n(y - 5) + "' stroke='" + INK + "' stroke-width='2'/><line x1='" + n(x - 6) + "' y1='" + n(y + 5) + "' x2='" + n(x + 6) + "' y2='" + n(y + 5) + "' stroke='" + INK + "' stroke-width='3.4'/>";
      s += text(x - 27 * k, y - 4, '+', '#DC2626', 14, 'middle', 700);   /* à l'extérieur du cercle, au niveau de la grande plaque */
      s += fleches(x + 17 * k, y - 15, k > 0 ? 3 * Math.PI / 4 : Math.PI / 4);
      return s;
    }
    function ldr(x, y, o) {   /* photorésistance : conducteur ohmique et flèches de lumière */
      return res(x, y, o) + (o === 'v' ? fleches(x - 10, y - 8, Math.PI / 4) : fleches(x - 8, y - 10, Math.PI / 4));
    }
    function pile(x, y) {   /* pile (branche verticale) : grand trait (+) en haut, petit trait (−) en bas */
      return "<line x1='" + n(x - 14) + "' y1='" + n(y - 5) + "' x2='" + n(x + 14) + "' y2='" + n(y - 5) + "' stroke='" + INK + "' stroke-width='2'/><line x1='" + n(x - 7) + "' y1='" + n(y + 5) + "' x2='" + n(x + 7) + "' y2='" + n(y + 5) + "' stroke='" + INK + "' stroke-width='3.4'/>" + text(x + 18, y - 4, '+', '#DC2626', 12, 'start', 700);
    }
    function npn(x, y) {   /* transistor NPN : base à gauche (x − 24, y), collecteur en haut (x + 10, y − 24), émetteur en bas (x + 10, y + 24) */
      var s = "<circle cx='" + n(x + 4) + "' cy='" + n(y) + "' r='17' fill='#fff' stroke='" + INK + "' stroke-width='1.8'/>";
      s += "<line x1='" + n(x - 24) + "' y1='" + n(y) + "' x2='" + n(x - 4) + "' y2='" + n(y) + "' stroke='" + INK + "' stroke-width='2'/><line x1='" + n(x - 4) + "' y1='" + n(y - 10) + "' x2='" + n(x - 4) + "' y2='" + n(y + 10) + "' stroke='" + INK + "' stroke-width='3'/>";
      s += "<polyline points='" + n(x - 4) + ',' + n(y - 4) + ' ' + n(x + 10) + ',' + n(y - 12) + ' ' + n(x + 10) + ',' + n(y - 24) + "' fill='none' stroke='" + INK + "' stroke-width='2'/>";
      s += "<polyline points='" + n(x - 4) + ',' + n(y + 4) + ' ' + n(x + 10) + ',' + n(y + 12) + ' ' + n(x + 10) + ',' + n(y + 24) + "' fill='none' stroke='" + INK + "' stroke-width='2'/>";
      s += "<polygon points='" + n(x + 10) + ',' + n(y + 12) + ' ' + n(x + 2) + ',' + n(y + 12) + ' ' + n(x + 6) + ',' + n(y + 6) + "' fill='" + INK + "'/>";
      s += text(x - 14, y - 6, 'B', '#475569', 10, 'middle', 700) + text(x + 18, y - 16, 'C', '#475569', 10, 'start', 700) + text(x + 18, y + 22, 'E', '#475569', 10, 'start', 700);
      return s;
    }
    function svg(w, h, body, label, cls) { return "<svg class='" + (cls || 'nt-svg nt-svg-m') + "' viewBox='0 0 " + w + ' ' + h + "' role='img' aria-label=\"" + label + "\">" + body + "</svg>"; }
    return { fleches: fleches, pv: pv, ldr: ldr, pile: pile, npn: npn, cap: cap, src: src, inter2: inter2, inter: inter, wire: wire, text: text, qty: qty, node: node, res: res, therm: therm, rheo: rheo, lamp: lamp, gen: gen, meter: meter, led: led, sw: sw, iarr: iarr, uarr: uarr, svg: svg, INK: INK };
  })();
  /* ================= Quiz : quelle interaction photon-matière ? ================= */
  var QUIZ = {
    'quiz-app': [
      ['Un photomultiplicateur, capable de détecter un photon unique', 0, 'Un photon arrache un électron d\u2019une photocathode (effet externe), puis cet électron est multiplié par une cascade d\u2019émissions secondaires.'],
      ['Une photodiode', 1, 'Un photon d\u2019énergie supérieure au gap crée une paire électron-trou dans une jonction semi-conductrice&nbsp;: effet interne.'],
      ['Une cellule photovoltaïque', 1, 'Comme une photodiode, mais optimisée pour convertir l\u2019énergie solaire en énergie électrique&nbsp;: effet interne.'],
      ['Un capteur d\u2019appareil photo (CMOS)', 1, 'Une matrice de photodétecteurs en silicium&nbsp;: chaque photon absorbé crée une charge (effet interne).'],
      ['Une photorésistance (LDR)', 1, 'Les paires électron-trou créées par la lumière augmentent la conductivité du matériau&nbsp;: effet interne.'],
      ['Une diode électroluminescente (DEL)', 2, 'Elle <b>émet</b> des photons&nbsp;: des électrons et des trous se recombinent dans le semi-conducteur.'],
      ['Un laser', 2, 'Il <b>émet</b> des photons par émission stimulée&nbsp;: un photon incident provoque l\u2019émission d\u2019un photon identique.'],
      ['Une lampe à vapeur de sodium', 2, 'Les atomes du gaz, excités par une décharge électrique, se désexcitent en <b>émettant</b> des photons&nbsp;: spectre de raies.'],
      ['L\u2019expérience de Hertz et Hallwachs&nbsp;: une plaque de zinc chargée se décharge sous rayonnement ultraviolet', 0, 'Les photons UV arrachent des électrons au zinc&nbsp;: c\u2019est l\u2019effet photoélectrique externe.']
    ]
  };
  var CHOIX = ['effet photoélectrique externe', 'effet photoélectrique interne', 'émission de photons'];
  $$(document, '.nt-quizlab').forEach(function (root) {   /* interface : numéro de question, pastilles de progression, carte, retour coloré */
    var D = QUIZ[root.id]; if (!D) { return; }
    var qEl = $(root, '.nt-ql-q'), bx = $(root, '.nt-ql-btns'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), next = $(root, '[data-act="next"]'), prog = $(root, '.nt-prog'), num0 = $(root, '.nt-qnum'), lbl = next.innerHTML;
    var order = [], k = 0, good = 0, answered = false, fini = false, res = [];
    function progres() {
      prog.innerHTML = order.map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === k && !fini ? ' cur' : '') + '"></i>'; }).join('');
      num0.textContent = fini ? 'Bilan' : 'Question ' + (k + 1) + ' sur ' + order.length;
    }
    function show() {
      answered = false; var q = D[order[k]]; qEl.innerHTML = q[0]; msg.textContent = ''; msg.className = 'nt-msg'; bx.innerHTML = '';
      CHOIX.forEach(function (cTxt, i) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn nt-choix'; b.innerHTML = cTxt;
        b.addEventListener('click', function () {
          if (answered) { return; } answered = true; var ok = i === q[1]; res[k] = ok; if (ok) { good++; }
          b.classList.add(ok ? 'nt-choix-ok' : 'nt-choix-ko'); if (!ok) { bx.children[q[1]].classList.add('nt-choix-ok'); }
          msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko'); msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Non.</b> ') + q[2];
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
  /* ================= L'énergie d'un photon ================= */
  (function () {
    var root = document.getElementById('lab-photon');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rL = $(root, 'input[type="range"]'), oL = $(root, '.out-l'), oN = $(root, '.out-nu'), oJ = $(root, '.out-ej'), oV = $(root, '.out-ev'), msg = $(root, '.nt-msg'), S, visible = true, last = null, ph = 0;
    var SEUILS = [['gap du silicium', 1.12, '#0EA5E9'], ['W\u2091\u2093\u209c du césium', 2.14, '#B45309'], ['W\u2091\u2093\u209c du sodium', 2.36, '#64748B'], ['W\u2091\u2093\u209c du zinc', 4.31, '#475569']];
    function pastille(c, s, x, y, col, bg, align) {   /* étiquette arrondie ; renvoie sa boîte */
      c.save(); c.font = '700 11px system-ui, sans-serif'; var lw = c.measureText(s).width + 14, xx = align === 'right' ? x - lw : (align === 'left' ? x : x - lw / 2);
      if (align === 'mesure') { c.restore(); return lw; }
      rr(c, xx, y - 13, lw, 19, 9.5); c.fillStyle = bg || '#fff'; c.fill(); c.strokeStyle = col; c.lineWidth = 1.2; c.stroke();
      c.fillStyle = col; c.textAlign = 'left'; c.fillText(s, xx + 7, y + 1); c.restore();
      return [xx, y - 13, lw, 19];
    }
    function draw(dt) {
      if (!S) { return; }
      var l = +rL.value, nu = C / (l * 1e-9), E = H * nu, eV = E / QE, c = S.ctx, w = S.w, h = S.h, col = couleur(l), coulT = l < 380 ? '#7C3AED' : (l > 750 ? '#991B1B' : col);
      ph += dt * 6;
      oL.textContent = Math.round(l) + ' nm'; oN.innerHTML = sciH(nu, 3) + '&nbsp;Hz'; oJ.innerHTML = sciH(E, 3) + '&nbsp;J'; oV.textContent = fr(eV, 2) + ' eV';
      c.clearRect(0, 0, w, h);
      /* ---- spectre gradué, régions nommées au-dessus ---- */
      var x0 = 34, x1 = w - 20, l0 = 200, l1 = 1300, ys = 56, hs = 24;   /* la bulle de λ passe au-dessus des noms des régions */
      function XL(v) { return x0 + (v - l0) / (l1 - l0) * (x1 - x0); }
      c.save(); rr(c, x0, ys, x1 - x0, hs, 8); c.clip();
      for (var x = x0; x < x1; x++) { var lx = l0 + (x - x0) / (x1 - x0) * (l1 - l0); c.fillStyle = lx < 380 ? 'rgba(167,139,250,.45)' : (lx > 750 ? 'rgba(153,27,27,' + Math.max(0.12, 0.45 - (lx - 750) / 1500) + ')' : couleur(lx)); c.fillRect(x, ys, 1.2, hs); }
      c.restore(); rr(c, x0, ys, x1 - x0, hs, 8); c.strokeStyle = '#CBD5E1'; c.lineWidth = 1; c.stroke();
      txtN(c, 'ultraviolet', (XL(200) + XL(380)) / 2, ys - 13, '#6D28D9', '700 11.5px system-ui'); txtN(c, 'visible', (XL(380) + XL(750)) / 2, ys - 13, '#0F172A', '700 11.5px system-ui'); txtN(c, 'infrarouge', (XL(750) + XL(1300)) / 2, ys - 13, '#991B1B', '700 11.5px system-ui');
      [380, 750].forEach(function (v) { c.strokeStyle = 'rgba(15,23,42,.35)'; c.setLineDash([2, 2]); c.beginPath(); c.moveTo(XL(v), ys - 4); c.lineTo(XL(v), ys + hs + 4); c.stroke(); c.setLineDash([]); });
      for (var t = 200; t <= 1300; t += 100) { c.strokeStyle = '#94A3B8'; c.lineWidth = 1; c.beginPath(); c.moveTo(XL(t), ys + hs); c.lineTo(XL(t), ys + hs + 4); c.stroke(); if (t % 200 === 0) { txtN(c, String(t), XL(t), ys + hs + 15, '#64748B', '10px system-ui'); } }
      txtN(c, 'nm', x1, ys + hs + 15, '#64748B', '10px system-ui', 'right');
      /* repère de la longueur d'onde choisie */
      var xm = XL(l); c.strokeStyle = '#0F172A'; c.lineWidth = 2; c.beginPath(); c.moveTo(xm, ys - 2); c.lineTo(xm, ys + hs + 2); c.stroke();
      c.fillStyle = '#0F172A'; c.beginPath(); c.moveTo(xm, ys - 2); c.lineTo(xm - 5, ys - 9); c.lineTo(xm + 5, ys - 9); c.closePath(); c.fill();
      pastille(c, 'λ = ' + Math.round(l) + ' nm', Math.max(x0 + 40, Math.min(x1 - 40, xm)), 16, '#0F172A', '#fff');
      /* ---- l'onde du photon, dans son cadre ---- */
      var yW0 = ys + hs + 26, yW1 = yW0 + 62, yW = (yW0 + yW1) / 2, lw = 14 + (l - 200) / 1100 * 80;
      rr(c, x0, yW0, x1 - x0, yW1 - yW0, 10); c.fillStyle = '#0F172A'; c.fill();
      c.save(); rr(c, x0, yW0, x1 - x0, yW1 - yW0, 10); c.clip();
      c.strokeStyle = coulT; c.lineWidth = 2.6; c.shadowColor = coulT; c.shadowBlur = 8; c.beginPath();
      for (var xx = x0 + 6; xx < x1 - 6; xx += 2) { var env = Math.exp(-Math.pow((xx - (x0 + x1) / 2) / ((x1 - x0) * 0.3), 2)), yy = yW + 20 * env * Math.sin(2 * Math.PI * (xx - x0) / lw - ph); if (xx === x0 + 6) { c.moveTo(xx, yy); } else { c.lineTo(xx, yy); } }
      c.stroke(); c.restore();
      txtN(c, 'le photon (λ à l\u2019échelle relative)', x0 + 10, yW0 + 14, '#94A3B8', '10px system-ui', 'left');
      /* ---- énergie du photon et seuils ---- */
      var yt = yW1 + 26, yb = h - 22, eMax = 6.5, xa = x0 + 38;
      function YE(v) { return yb - v / eMax * (yb - yt); }
      for (var v = 0; v <= 6; v++) { c.strokeStyle = '#EEF2F6'; c.lineWidth = 1; c.beginPath(); c.moveTo(xa, YE(v)); c.lineTo(x1, YE(v)); c.stroke(); txtN(c, v + ' eV', xa - 6, YE(v) + 4, '#64748B', '10.5px system-ui', 'right'); }
      c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(xa, yt - 6); c.lineTo(xa, yb); c.lineTo(x1, yb); c.stroke();
      var bw = Math.min(100, (x1 - x0) * 0.18), bx = xa + 22, et = Math.min(eV, eMax);
      var gbar = c.createLinearGradient(0, YE(et), 0, yb); gbar.addColorStop(0, coulT); gbar.addColorStop(1, 'rgba(15,23,42,.15)');
      rr(c, bx, YE(et), bw, yb - YE(et), 8); c.fillStyle = gbar; c.fill();
      var etroit = x1 - x0 < 420, tP = (etroit ? '' : 'photon : ') + fr(eV, 2) + ' eV', wP = pastille(c, tP, 0, 0, '', '', 'mesure');
      var pris = [pastille(c, tP, Math.max(x0 + wP / 2 + 2, bx + bw / 2), YE(et) - 10, '#0F172A', '#fff')], possibles = [];   /* sur téléphone : « 2,26 eV » suffit */
      SEUILS.forEach(function (s2) {   /* lignes des seuils d'abord */
        var y = YE(s2[1]); c.strokeStyle = s2[2]; c.lineWidth = 1.8; c.setLineDash([7, 4]); c.beginPath(); c.moveTo(xa, y); c.lineTo(x1, y); c.stroke(); c.setLineDash([]);
      });
      SEUILS.slice().reverse().forEach(function (s2) {   /* puis les étiquettes, de haut en bas, sans chevauchement : au-dessus de la ligne si possible, sinon en dessous, etc. */
        var y = YE(s2[1]), ok = eV >= s2[1], t = (etroit ? s2[0].replace(' du ', ' ') : s2[0]) + ' : ' + fr(s2[1], 2) + ' eV  ' + (ok ? '\u2714' : '\u2716'), lw = pastille(c, t, 0, 0, '', '', 'mesure');
        var essais = [-4, 16, -24, 36], yy = y - 4;
        for (var k = 0; k < essais.length; k++) { var cand = [x1 - 4 - lw, y + essais[k] - 13, lw, 19]; if (!pris.some(function (b) { return cand[0] < b[0] + b[2] && b[0] < cand[0] + cand[2] && cand[1] < b[1] + b[3] && b[1] < cand[1] + cand[3]; })) { yy = y + essais[k]; break; } }
        pris.push(pastille(c, t, x1 - 4, yy, ok ? '#15803D' : '#B91C1C', ok ? '#F0FDF4' : '#FEF2F2', 'right'));
      });
      SEUILS.forEach(function (s2) { if (eV >= s2[1]) { possibles.push(s2[0].replace('W\u2091\u2093\u209c du ', 'arracher un électron au ').replace('gap du silicium', 'créer une paire électron-trou dans le silicium')); } });
      msg.innerHTML = possibles.length ? 'Ce photon a assez d\u2019énergie pour&nbsp;: ' + possibles.join('&nbsp;; ') + '.' : 'Ce photon n\u2019a assez d\u2019énergie pour aucun de ces seuils&nbsp;: même un flux de photons très intense n\u2019y changerait rien.';
    }
    function loop(ts) { var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; if (visible) { draw(RM ? 0 : dt); } requestAnimationFrame(loop); }
    rL.addEventListener('input', function () { draw(0); });
    function setup() { S = canvasCtx(cv); draw(0); }
    watch(cv, function (v) { visible = v; });
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= L'effet photoélectrique et l'expérience de Millikan ================= */
  (function () {
    var root = document.getElementById('lab-pe');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rL = $(root, '[data-p="l"]'), rI = $(root, '[data-p="i"]'), rU = $(root, '[data-p="u"]'), oL = $(root, '.out-l'), oU = $(root, '.out-u'), oI = $(root, '.out-i'), oEc = $(root, '.out-ec'), oH = $(root, '.out-h'), msg = $(root, '.nt-msg');
    var bRec = $(root, '[data-act="rec"]'), bClr = $(root, '[data-act="clear"]'), bTh = $(root, '[data-act="theo"]');
    var S, visible = true, last = null, metal = 0, photons = [], electrons = [], arrivees = [], pts = [], theorie = false, spawn = 0;
    function etat() { var l = +rL.value, nu = C / (l * 1e-9), eph = H * nu / QE, W = METAUX[metal][1]; return { l: l, nu: nu, eph: eph, W: W, Ec: eph - W, U: +rU.value }; }
    function geo() { var w = S.w, h = S.h, large = w >= 640, tw = large ? w * 0.54 : w; return { large: large, tw: tw, cx: 60, ax: tw - 46, ty: 70, by: 210, w: w, h: h }; }
    function draw(dt) {
      if (!S) { return; }
      var e = etat(), g = geo(), c = S.ctx, w = g.w, h = g.h, d = g.ax - g.cx - 12;
      oL.textContent = Math.round(e.l) + ' nm'; oU.textContent = fr(e.U, 2) + ' V';
      oEc.innerHTML = e.Ec > 0 ? fr(e.Ec, 2) + '&nbsp;eV' : 'aucun électron éjecté';
      /* ---- simulation : photons, électrons freinés par le champ ---- */
      if (dt > 0) {
        spawn += dt * 26 * (+rI.value / 100);
        while (spawn >= 1) { spawn -= 1; photons.push({ s: 0, y: g.ty + 14 + Math.random() * (g.by - g.ty - 28) }); }
        photons.forEach(function (p) { p.s += dt * 1.6; });
        photons = photons.filter(function (p) { if (p.s >= 1) { if (e.Ec > 0) { electrons.push({ x: 0, y: p.y, dir: 1 }); } return false; } return true; });
        electrons.forEach(function (el) {
          var E = e.Ec - e.U * el.x / d;   /* énergie cinétique (eV) à l'abscisse x : le travail du champ vaut −e U_CA x / d */
          if (E <= 0.002 && el.dir > 0) { el.dir = -1; }
          var v = 150 * Math.sqrt(Math.max(E, 0.004));
          el.x += el.dir * v * dt;
        });
        electrons = electrons.filter(function (el) { if (el.x >= d) { arrivees.push(performance.now()); return false; } return el.x > -2; });
      }
      var tnow = performance.now(); arrivees = arrivees.filter(function (t) { return tnow - t < 1000; });
      var cour = arrivees.length * 0.05 * (e.Ec > 0 && e.U < e.Ec ? 1 : 0);
      oI.textContent = cour > 0 ? fr(cour, 2) + ' µA' : '0';
      c.clearRect(0, 0, w, h);
      /* lampe et faisceau */
      var col = couleur(e.l), beam = e.l < 380 ? 'rgba(139,92,246,' : (e.l > 750 ? 'rgba(153,27,27,' : col.replace('rgb', 'rgba').replace(')', ','));
      var lx = g.cx + 92, ly = 22;   /* lampe au-dessus du tube : elle éclaire la cathode en biais */
      c.fillStyle = '#334155'; rr(c, lx, 6, 70, 26, 6); c.fill(); c.fillStyle = beam + '0.95)'; c.fillRect(lx - 8, 12, 8, 14);
      txtN(c, 'lampe', lx + 35, 23, '#E2E8F0', '600 10.5px system-ui');
      var gb = c.createLinearGradient(lx - 8, ly, g.cx, (g.ty + g.by) / 2); gb.addColorStop(0, beam + (0.3 + 0.4 * rI.value / 100) + ')'); gb.addColorStop(1, beam + (0.12 + 0.2 * rI.value / 100) + ')');   /* faisceau bien visible */
      c.fillStyle = gb; c.beginPath(); c.moveTo(lx - 8, 13); c.lineTo(lx - 8, 30); c.lineTo(g.cx + 6, g.by - 6); c.lineTo(g.cx + 6, g.ty + 6); c.closePath(); c.fill();
      photons.forEach(function (p) { var x = lx - 8 + (g.cx + 4 - (lx - 8)) * p.s, y = ly + (p.y - ly) * p.s; c.fillStyle = beam + '1)'; c.beginPath(); c.arc(x, y, 4, 0, 2 * Math.PI); c.fill(); c.strokeStyle = 'rgba(255,255,255,.9)'; c.lineWidth = 1.2; c.stroke(); });
      /* tube à vide, cathode et anode */
      c.fillStyle = 'rgba(226,232,240,.45)'; rr(c, g.cx - 24, g.ty - 26, g.ax - g.cx + 60, g.by - g.ty + 52, 40); c.fill(); c.strokeStyle = '#94A3B8'; c.lineWidth = 1.5; c.stroke();
      c.fillStyle = METAUX[metal][2]; rr(c, g.cx - 6, g.ty, 12, g.by - g.ty, 3); c.fill();
      c.fillStyle = '#475569'; rr(c, g.ax - 6, g.ty, 12, g.by - g.ty, 3); c.fill();
      txt(c, 'cathode (' + METAUX[metal][0] + ')', g.cx + 30, g.ty - 8, '#1E293B', '700 11px system-ui'); txt(c, 'anode', g.ax, g.ty - 8, '#1E293B', '700 11px system-ui');
      electrons.forEach(function (el) { c.fillStyle = '#E11D48'; c.beginPath(); c.arc(g.cx + 8 + el.x, el.y, 3.4, 0, 2 * Math.PI); c.fill(); });
      /* circuit : générateur et ampèremètre */
      var yc = h - 34;
      c.strokeStyle = '#1E293B'; c.lineWidth = 2; c.beginPath(); c.moveTo(g.cx, g.by); c.lineTo(g.cx, yc); c.lineTo(g.ax, yc); c.lineTo(g.ax, g.by); c.stroke();
      var gx = g.cx + (g.ax - g.cx) * 0.36, mx = g.cx + (g.ax - g.cx) * 0.72;
      c.fillStyle = '#fff'; c.beginPath(); c.arc(gx, yc, 17, 0, 2 * Math.PI); c.fill(); c.stroke(); txt(c, 'G', gx, yc + 5, '#1E293B', '700 13px system-ui');
      txt(c, e.U >= 0 ? '+' : '\u2212', gx - 24, yc - 10, e.U >= 0 ? '#DC2626' : '#2563EB', '700 14px system-ui'); txt(c, e.U >= 0 ? '\u2212' : '+', gx + 24, yc - 10, e.U >= 0 ? '#2563EB' : '#DC2626', '700 14px system-ui');
      c.fillStyle = '#fff'; c.beginPath(); c.arc(mx, yc, 15, 0, 2 * Math.PI); c.fill(); c.stroke(); txt(c, 'A', mx, yc + 5, '#1E293B', '700 13px system-ui');
      c.fillStyle = '#0F172A'; rr(c, mx - 34, yc - 52, 68, 24, 5); c.fill(); txtN(c, cour > 0 ? fr(cour, 2) + ' µA' : '0,00 µA', mx, yc - 35, '#4ADE80', '13px ui-monospace, Menlo, monospace');
      c.fillStyle = '#0F172A'; rr(c, gx - 40, yc - 52, 80, 24, 5); c.fill(); txtN(c, 'U = ' + fr(e.U, 2) + ' V', gx, yc - 35, '#FBBF24', '13px ui-monospace, Menlo, monospace');
      if (!g.large) { return; }
      /* ---- graphique e·U_a en fonction de ν ---- */
      var L = g.tw + 46, R = w - 14, T = 18, B = h - 34, numax = 16e14, ymin = -5, ymax = 4.5;
      function X(nu) { return L + nu / numax * (R - L); }
      function Y(v) { return B - (v - ymin) / (ymax - ymin) * (B - T); }
      for (var k = 0; k <= 16; k += 2) { c.strokeStyle = '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(X(k * 1e14), T); c.lineTo(X(k * 1e14), B); c.stroke(); txt(c, String(k), X(k * 1e14), B + 14, '#475569', '10.5px system-ui'); }
      for (var v = -5; v <= 4; v++) { c.strokeStyle = v === 0 ? '#94A3B8' : '#F1F5F9'; c.lineWidth = 1; c.beginPath(); c.moveTo(L, Y(v)); c.lineTo(R, Y(v)); c.stroke(); txt(c, String(v), L - 6, Y(v) + 4, '#475569', '10.5px system-ui', 'right'); }
      c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.stroke();
      txt(c, '\u03bd (10\u00b9\u2074 Hz) \u2192', R - 40, B + 28, '#475569', '11px system-ui'); txt(c, 'eU\u2090 (eV)', L + 6, T - 4, '#475569', '700 11px system-ui', 'left');
      if (theorie) { METAUX.forEach(function (m, i) { if (i !== metal) { return; } c.strokeStyle = m[2]; c.globalAlpha = 0.7; c.lineWidth = 1.6; c.setLineDash([6, 4]); c.beginPath(); c.moveTo(X(0), Y(-m[1])); c.lineTo(X(numax), Y(H * numax / QE - m[1])); c.stroke(); c.setLineDash([]); c.globalAlpha = 1; }); }
      var pm = pts.filter(function (p) { return p[2] === metal; });
      if (pm.length >= 2) {   /* droite des moindres carrés et constante de Planck mesurée */
        var mx2 = pm.reduce(function (s, p) { return s + p[0]; }, 0) / pm.length, my = pm.reduce(function (s, p) { return s + p[1]; }, 0) / pm.length;
        var sxy = pm.reduce(function (s, p) { return s + (p[0] - mx2) * (p[1] - my); }, 0), sxx = pm.reduce(function (s, p) { return s + (p[0] - mx2) * (p[0] - mx2); }, 0);
        if (sxx > 0) {
          var a = sxy / sxx, b0 = my - a * mx2;
          c.strokeStyle = '#E11D48'; c.lineWidth = 2; c.beginPath(); c.moveTo(X(0), Y(b0)); c.lineTo(X(numax), Y(a * numax + b0)); c.stroke();
          oH.innerHTML = sciH(a * QE, 3) + '&nbsp;J·s (W<sub>ext</sub> ≈ ' + fr(-b0, 2) + '&nbsp;eV)';
        }
      } else { oH.textContent = 'relevez au moins deux points'; }
      pts.forEach(function (p) { c.fillStyle = METAUX[p[2]][2]; c.beginPath(); c.arc(X(p[0]), Y(p[1]), 5, 0, 2 * Math.PI); c.fill(); c.strokeStyle = '#fff'; c.lineWidth = 1.5; c.stroke(); });
    }
    function loop(ts) { var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; if (visible) { draw(RM ? dt * 0.4 : dt); } requestAnimationFrame(loop); }
    bRec.addEventListener('click', function () {
      var e = etat(), Ua = e.Ec;
      if (e.Ec <= 0) { msg.innerHTML = 'Aucun électron n\u2019est éjecté&nbsp;: le photon (' + fr(e.eph, 2) + '&nbsp;eV) n\u2019a pas assez d\u2019énergie pour vaincre le travail d\u2019extraction du ' + METAUX[metal][0] + ' (' + fr(e.W, 2) + '&nbsp;eV). Pas de tension d\u2019arrêt à mesurer.'; return; }
      if (e.U < Ua - 0.004) { msg.innerHTML = 'Le courant n\u2019est pas nul&nbsp;: des électrons atteignent encore l\u2019anode. Augmentez U<sub>CA</sub>.'; return; }
      if (e.U > Ua + 0.12) { msg.innerHTML = 'Le courant est bien nul, mais U<sub>CA</sub> est trop grande&nbsp;: cherchez la <b>plus petite</b> tension qui annule le courant.'; return; }
      pts.push([e.nu, e.U, metal]);
      msg.innerHTML = 'Point relevé&nbsp;: ν = ' + sciH(e.nu, 3) + '&nbsp;Hz, eU<sub>a</sub> = ' + fr(e.U, 2) + '&nbsp;eV. Changez de longueur d\u2019onde et recommencez.';
    });
    bClr.addEventListener('click', function () { pts = []; msg.textContent = ''; });
    bTh.addEventListener('click', function () { theorie = !theorie; bTh.classList.toggle('nt-btn-main', theorie); });
    $$(root, 'input[name="metal"]').forEach(function (r) { r.addEventListener('change', function () { metal = +r.value; electrons = []; }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    watch(cv, function (v) { visible = v; });
    msg.innerHTML = 'Choisissez une longueur d\u2019onde, puis augmentez U<sub>CA</sub> jusqu\u2019à ce que le courant s\u2019annule&nbsp;: c\u2019est la tension d\u2019arrêt U<sub>a</sub>. Relevez le point, puis recommencez avec une autre longueur d\u2019onde.';
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Un capteur de luminosité ================= */
  (function () {
    var root = document.getElementById('lab-ldr');
    if (!root) { return; }
    var box = $(root, '.nt-ldr-svg'), rL = $(root, '[data-p="lux"]'), rP = $(root, '[data-p="pot"]'), oL = $(root, '.out-lux'), oR = $(root, '.out-r'), oP = $(root, '.out-pot'), oU = $(root, '.out-u'), msg = $(root, '.nt-msg');
    function maj() {
      var lux = Math.pow(10, +rL.value), Rl = 200e3 * Math.pow(lux, -0.7), Rp = +rP.value * 1000, Ud = 9 * Rl / (Rl + Rp), on = Math.max(0, Math.min(1, (Ud - 0.7) / 0.8));
      oL.textContent = lux >= 1000 ? nb(lux, 2) + ' lux' : Math.round(lux) + ' lux'; oR.textContent = Rl >= 1000 ? nb(Rl / 1000, 3) + ' k\u03a9' : Math.round(Rl) + ' \u03a9'; oP.textContent = nb(Rp / 1000, 2) + ' k\u03a9';
      oU.textContent = Ud > 0.7 ? '0,7 V (transistor passant)' : fr(Ud, 2) + ' V (transistor bloqué)';
      var b = '', ciel = 'hsl(220,' + Math.round(40 + 20 * Math.min(1, +rL.value / 4)) + '%,' + Math.round(14 + 70 * Math.min(1, +rL.value / 4)) + '%)';
      b += "<rect x='0' y='0' width='360' height='330' rx='12' fill='" + ciel + "' fill-opacity='.18'/>";
      b += CI.wire([[60, 40], [300, 40]]) + CI.wire([[60, 40], [60, 170]]) + CI.wire([[60, 180], [60, 310], [300, 310]]) + CI.wire([[180, 40], [180, 310]]) + CI.wire([[180, 175], [266, 175]]) + CI.wire([[300, 40], [300, 151]]) + CI.wire([[300, 199], [300, 310]]);
      if (on > 0.02) { b += "<circle cx='300' cy='75' r='" + (14 + 18 * on).toFixed(1) + "' fill='rgba(250,204,21," + (0.75 * on).toFixed(2) + ")'/>"; }
      b += CI.pile(60, 175) + CI.rheo(180, 105, 'v') + CI.ldr(180, 250, 'v') + CI.led(300, 75, 'v', 'd') + CI.res(300, 120, 'v') + CI.npn(290, 175) + CI.node(180, 40) + CI.node(180, 310) + CI.node(180, 175);
      if (on > 0.02) { b += "<polygon points='289,66 311,66 300,84' fill='rgba(250,204,21," + (0.4 + 0.6 * on).toFixed(2) + ")'/>"; }
      b += CI.text(48, 179, '9 V', '#475569', 12, 'end', 700) + CI.text(160, 109, oP.textContent, '#475569', 11, 'end') + CI.text(160, 254, 'LDR', '#475569', 11, 'end', 700) + CI.text(318, 124, '330 Ω', '#475569', 11, 'start');
      box.innerHTML = CI.svg(360, 330, b, 'Capteur de luminosité : la DEL s\u2019allume quand la lumière ambiante baisse', 'nt-svg');
      msg.innerHTML = on > 0.02 ? 'Il fait sombre&nbsp;: la photorésistance a une grande résistance, la tension à ses bornes dépasse 0,7&nbsp;V, le transistor devient passant et <b>la DEL s\u2019allume</b>.' : 'Il fait clair&nbsp;: la photorésistance conduit bien (petite résistance), la tension à ses bornes reste sous 0,7&nbsp;V&nbsp;: le transistor est bloqué et <b>la DEL reste éteinte</b>.';
    }
    [rL, rP].forEach(function (r) { r.addEventListener('input', maj); });
    maj();
  })();
  /* ================= Caractéristique et rendement d'une cellule photovoltaïque ================= */
  (function () {
    var root = document.getElementById('lab-pv');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rG = $(root, '[data-p="G"]'), rR = $(root, '[data-p="R"]'), oG = $(root, '.out-G'), oR = $(root, '.out-R'), oU = $(root, '.out-U'), oI = $(root, '.out-I'), oP = $(root, '.out-P'), oE = $(root, '.out-eta'), msg = $(root, '.nt-msg'), S;
    var ISC = 9.0, VOC = 0.63, NVT = 0.0334, I0 = ISC / (Math.exp(VOC / NVT) - 1), SURF = 0.156 * 0.156;
    function Icell(U, G) { return ISC * G / 1000 - I0 * (Math.exp(U / NVT) - 1); }
    function Uco(G) { var lo = 0, hi = 0.8; for (var k = 0; k < 50; k++) { var m = (lo + hi) / 2; if (Icell(m, G) > 0) { lo = m; } else { hi = m; } } return lo; }
    function mpp(G) { var best = [0, 0, 0], uc = Uco(G); for (var k = 0; k <= 400; k++) { var U = uc * k / 400, P = U * Icell(U, G); if (P > best[0]) { best = [P, U, Icell(U, G)]; } } return best; }
    function draw() {
      var G = +rG.value, Rl = Math.pow(10, +rR.value), c = S.ctx, w = S.w, h = S.h;
      var lo = 0, hi = Uco(G); for (var k = 0; k < 50; k++) { var m = (lo + hi) / 2; if (Icell(m, G) > m / Rl) { lo = m; } else { hi = m; } }
      var U = lo, I = Icell(U, G), P = U * I, Pl = G * SURF, M = mpp(G);
      oG.textContent = G + ' W·m⁻²'; oR.textContent = Rl < 1 ? nb(Rl * 1000, 3) + ' m\u03a9' : nb(Rl, 3) + ' \u03a9'; oU.textContent = fr(U, 3) + ' V'; oI.textContent = fr(I, 2) + ' A'; oP.textContent = fr(P, 2) + ' W'; oE.textContent = fr(P / Pl * 100, 1) + ' %';
      c.clearRect(0, 0, w, h);
      var large = w >= 620, gw = large ? (w - 30) / 2 : w - 10, gh = large ? h : h / 2;
      function panneau(ox, oy, pw, ph, yMax, yLab, f, isP) {
        var L = ox + 46, R = ox + pw - 10, T = oy + 16, B = oy + ph - 34;
        function X(u) { return L + u / 0.7 * (R - L); }
        function Y(v) { return B - v / yMax * (B - T); }
        for (var u = 0; u <= 0.7 + 1e-9; u += 0.1) { c.strokeStyle = '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(X(u), T); c.lineTo(X(u), B); c.stroke(); txt(c, fr(u, 1), X(u), B + 14, '#475569', '10.5px system-ui'); }
        var st = yMax > 6 ? 2 : 1; for (var v = 0; v <= yMax + 1e-9; v += st) { c.strokeStyle = '#E2E8F0'; c.beginPath(); c.moveTo(L, Y(v)); c.lineTo(R, Y(v)); c.stroke(); txt(c, String(v), L - 6, Y(v) + 4, '#475569', '10.5px system-ui', 'right'); }
        c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
        txt(c, 'U (V) \u2192', R - 22, B + 28, '#475569', '11px system-ui'); txt(c, yLab, L + 6, T - 4, '#475569', '700 11px system-ui', 'left');
        [200, 400, 600, 800, 1000].forEach(function (gg) {
          var cur = gg === G, uc = Uco(gg);
          c.strokeStyle = cur ? (isP ? '#7C3AED' : '#2563EB') : 'rgba(148,163,184,.55)'; c.lineWidth = cur ? 2.6 : 1.2; c.beginPath();
          for (var k2 = 0; k2 <= 120; k2++) { var uu = uc * k2 / 120, vv = f(uu, gg); if (k2 === 0) { c.moveTo(X(uu), Y(vv)); } else { c.lineTo(X(uu), Y(vv)); } }
          c.stroke();
          if (!cur) { txt(c, String(gg), X(uc) + 3, Y(f(uc * 0.5, gg)) + (isP ? -2 : 4), '#94A3B8', '9.5px system-ui', 'left'); }
        });
        if (G % 200 !== 0) { var uc2 = Uco(G); c.strokeStyle = isP ? '#7C3AED' : '#2563EB'; c.lineWidth = 2.6; c.beginPath(); for (var k3 = 0; k3 <= 120; k3++) { var u3 = uc2 * k3 / 120, v3 = f(u3, G); if (k3 === 0) { c.moveTo(X(u3), Y(v3)); } else { c.lineTo(X(u3), Y(v3)); } } c.stroke(); }
        if (!isP) {   /* droite de charge I = U / R */
          c.strokeStyle = 'rgba(234,88,12,.7)'; c.lineWidth = 1.4; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(X(0), Y(0)); var ue = Math.min(0.7, yMax * Rl); c.lineTo(X(ue), Y(ue / Rl)); c.stroke(); c.setLineDash([]);
        } else {   /* puissance maximale */
          c.fillStyle = '#F59E0B'; c.beginPath(); c.arc(X(M[1]), Y(M[0]), 5, 0, 2 * Math.PI); c.fill();
          txt(c, 'P\u2098\u2090\u2093 = ' + fr(M[0], 2) + ' W', X(M[1]) - 6, Y(M[0]) - 10, '#B45309', '700 11.5px system-ui', 'right');
        }
        var yv = isP ? P : I; c.fillStyle = '#E11D48'; c.beginPath(); c.arc(X(U), Y(yv), 6, 0, 2 * Math.PI); c.fill(); c.strokeStyle = '#fff'; c.lineWidth = 2; c.stroke();
      }
      panneau(0, 0, gw, gh, 10, 'I (A)', function (u, gg) { return Math.max(0, Icell(u, gg)); }, false);
      panneau(large ? gw + 20 : 0, large ? 0 : gh, gw, gh, 5, 'P (W)', function (u, gg) { return Math.max(0, u * Icell(u, gg)); }, true);
      var ecart = (M[0] - P) / M[0];
      msg.innerHTML = ecart < 0.02 ? 'La cellule fonctionne à sa <b>puissance maximale</b>&nbsp;: η = P<sub>max</sub> / P<sub>lum</sub> = ' + fr(M[0], 2) + ' / ' + fr(Pl, 1) + ' ≈ ' + fr(M[0] / Pl * 100, 1) + '&nbsp;%.'
        : 'Le point de fonctionnement (en rouge) est à l\u2019intersection de la caractéristique et de la droite I = U / R. Ajustez R pour atteindre la puissance maximale (point orange)&nbsp;: c\u2019est ce que font automatiquement les onduleurs des installations solaires.';
    }
    [rG, rR].forEach(function (r) { r.addEventListener('input', draw); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= Entraînement : énergie des photons ================= */
  (function () {
    var root = document.getElementById('lab-calc');
    if (!root) { return; }
    var qEl = $(root, '.nt-tr-q'), inp = $(root, 'input[type="text"]'), uEl = $(root, '.nt-tr-unit'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), bV = $(root, '[data-act="check"]'), bN = $(root, '[data-act="next"]'), lblN = bN.innerHTML;
    var NQ = 6, n = 0, good = 0, cur, done = false, fini = false, res = [], vis = $(root, '.nt-qvis'), prog = $(root, '.nt-prog'), num0 = $(root, '.nt-qnum');
    function progres() { prog.innerHTML = Array.apply(null, Array(NQ)).map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === n - (done ? 1 : 0) && !fini ? ' cur' : '') + '"></i>'; }).join(''); num0.textContent = fini ? 'Bilan' : 'Question ' + Math.min(NQ, n + (done ? 0 : 1)) + ' sur ' + NQ; }
    var G = [
      function () { var l = pick([254, 400, 450, 532, 589, 633, 700]), E = H * C / (l * 1e-9) / QE;
        return { vis: '<span><i style="background:' + couleur(l) + '"></i>λ = ' + l + '&nbsp;nm</span>', q: 'Quelle est l\u2019énergie d\u2019un photon de longueur d\u2019onde λ = ' + l + '&nbsp;nm, en <b>eV</b>&nbsp;?', rep: E, unit: 'eV',
          expl: 'E = hc / λ = 6,63 × 10<sup>−34</sup> × 3,00 × 10<sup>8</sup> / (' + l + ' × 10<sup>−9</sup>) = ' + sciH(E * QE, 3) + '&nbsp;J, soit ' + fr(E, 2) + '&nbsp;eV (1&nbsp;eV = 1,60 × 10<sup>−19</sup>&nbsp;J).' }; },
      function () { var nu = pick([4.5, 5.0, 6.0, 7.5, 9.0, 12]) * 1e14, E = H * nu;
        return { vis: '<span>ν = ' + sciH(nu, 2) + '&nbsp;Hz</span>', q: 'Quelle est l\u2019énergie d\u2019un photon de fréquence ν = ' + sciH(nu, 2) + '&nbsp;Hz&nbsp;? Réponse en <b>10<sup>−19</sup>&nbsp;J</b>.', rep: E / 1e-19, unit: '× 10⁻¹⁹ J',
          expl: 'E = hν = 6,63 × 10<sup>−34</sup> × ' + sciH(nu, 2) + ' = ' + sciH(E, 3) + '&nbsp;J.' }; },
      function () { var m = pick(METAUX), l0 = H * C / (m[1] * QE) * 1e9;
        return { vis: '<span>' + m[0] + '</span><span>W<sub>ext</sub> = ' + fr(m[1], 2) + '&nbsp;eV</span>', q: 'Le travail d\u2019extraction du ' + m[0] + ' vaut ' + fr(m[1], 2) + '&nbsp;eV. Quelle est la longueur d\u2019onde seuil λ<sub>0</sub> au-delà de laquelle aucun électron n\u2019est éjecté, en <b>nm</b>&nbsp;?', rep: l0, unit: 'nm',
          expl: 'Au seuil, hc / λ<sub>0</sub> = W<sub>ext</sub>, donc λ<sub>0</sub> = hc / W<sub>ext</sub> = 6,63 × 10<sup>−34</sup> × 3,00 × 10<sup>8</sup> / (' + fr(m[1], 2) + ' × 1,60 × 10<sup>−19</sup>) ≈ ' + Math.round(l0) + '&nbsp;nm. Pour λ &gt; λ<sub>0</sub>, les photons n\u2019ont pas assez d\u2019énergie.' }; },
      function () { var m = pick(METAUX.slice(0, 3)), l = pick([250, 300, 350, 400]), Ec = H * C / (l * 1e-9) / QE - m[1];
        return { vis: '<span>' + m[0] + '</span><span>W<sub>ext</sub> = ' + fr(m[1], 2) + '&nbsp;eV</span>' + '<span><i style="background:' + couleur(l) + '"></i>λ = ' + l + '&nbsp;nm</span>', q: 'On éclaire du ' + m[0] + ' (W<sub>ext</sub> = ' + fr(m[1], 2) + '&nbsp;eV) avec une lumière de longueur d\u2019onde ' + l + '&nbsp;nm. Quelle est l\u2019énergie cinétique maximale des électrons éjectés, en <b>eV</b>&nbsp;?', rep: Ec, unit: 'eV',
          expl: 'E<sub>photon</sub> = hc / λ ≈ ' + fr(Ec + m[1], 2) + '&nbsp;eV, puis E<sub>c</sub> = hν − W<sub>ext</sub> = ' + fr(Ec + m[1], 2) + ' − ' + fr(m[1], 2) + ' = ' + fr(Ec, 2) + '&nbsp;eV.' }; },
      function () { var m = pick(METAUX.slice(0, 3)), l = pick([250, 300, 350, 400]), Ec = H * C / (l * 1e-9) / QE - m[1];
        return { vis: '<span>' + m[0] + '</span><span>W<sub>ext</sub> = ' + fr(m[1], 2) + '&nbsp;eV</span>' + '<span><i style="background:' + couleur(l) + '"></i>λ = ' + l + '&nbsp;nm</span>', q: 'Même situation (' + m[0] + ', W<sub>ext</sub> = ' + fr(m[1], 2) + '&nbsp;eV, λ = ' + l + '&nbsp;nm). Quelle tension d\u2019arrêt U<sub>a</sub> faut-il appliquer pour annuler le courant, en <b>V</b>&nbsp;?', rep: Ec, unit: 'V',
          expl: 'eU<sub>a</sub> = E<sub>c</sub> = hν − W<sub>ext</sub> = ' + fr(Ec, 2) + '&nbsp;eV, donc U<sub>a</sub> = ' + fr(Ec, 2) + '&nbsp;V. (Une énergie de 1&nbsp;eV correspond à une tension de 1&nbsp;V pour une charge e.)' }; },
      function () { var l = pick([532, 633, 650]), Pm = pick([1, 2, 5]), N = Pm * 1e-3 * l * 1e-9 / (H * C);
        return { vis: '<span>P = ' + Pm + '&nbsp;mW</span>' + '<span><i style="background:' + couleur(l) + '"></i>λ = ' + l + '&nbsp;nm</span>', q: 'Un pointeur laser de puissance ' + Pm + '&nbsp;mW émet à λ = ' + l + '&nbsp;nm. Combien de photons émet-il chaque seconde&nbsp;? Réponse en <b>10<sup>15</sup> photons par seconde</b>.', rep: N / 1e15, unit: '× 10¹⁵ /s',
          expl: 'Énergie d\u2019un photon&nbsp;: E = hc / λ = ' + sciH(H * C / (l * 1e-9), 3) + '&nbsp;J. Nombre de photons par seconde&nbsp;: N = P / E = ' + Pm + ' × 10<sup>−3</sup> / ' + sciH(H * C / (l * 1e-9), 3) + ' ≈ ' + sciH(N, 3) + '. Un flux énorme&nbsp;!' }; }
    ];
    function nouveau() { cur = pick(G)(); qEl.innerHTML = cur.q; vis.innerHTML = '<span class="nt-qdata">' + cur.vis + '</span>'; vis.hidden = false; uEl.textContent = cur.unit; inp.value = ''; msg.textContent = ''; msg.className = 'nt-msg'; done = false; bV.disabled = false; inp.disabled = false; bN.innerHTML = n === NQ - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lblN; progres(); }
    function start() { n = 0; good = 0; fini = false; res = []; sc.textContent = '0 / 0'; $(root, '.nt-tr-zone').hidden = false; nouveau(); }
    bV.addEventListener('click', function () {
      if (done || fini) { return; }
      var v = num(inp.value); if (isNaN(v)) { msg.className = 'nt-msg'; msg.textContent = 'Entrez une valeur numérique.'; return; }
      var ok = Math.abs(v - cur.rep) <= Math.abs(cur.rep) * 0.03; done = true; res[n] = ok; n++; if (ok) { good++; }
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
})();
</script>

<script>
/* ================= Quiz de fin de chapitre (autonome) ================= */
(function () {
  var root = document.getElementById('quiz-final'); if (!root) { return; }
  var Q = [
    [
    "L'énergie d'un photon de fréquence $\\nu$ vaut…",
    [
    "$E = h\\nu$",
    "$E = \\dfrac{h}{\\nu}$",
    "$E = mc^2$",
    "$E = h\\lambda$"
    ],
    "$h \\approx \\pu{6,63E-34 J*s}$ est la constante de Planck."
    ],
    [
    "Plus la longueur d'onde d'un photon est grande, plus son énergie est…",
    [
    "petite",
    "grande",
    "inchangée",
    "négative"
    ],
    "$E = \\dfrac{hc}{\\lambda}$&nbsp;: un photon infrarouge transporte moins d'énergie qu'un photon ultraviolet."
    ],
    [
    "L'effet photoélectrique n'a lieu que si…",
    [
    "l'énergie des photons est supérieure au travail d'extraction du métal",
    "la lumière est très intense",
    "le métal est chauffé",
    "la lumière est rouge"
    ],
    "Il existe une fréquence seuil&nbsp;: augmenter l'intensité ne suffit pas en dessous de ce seuil."
    ],
    [
    "Le bilan énergétique de l'effet photoélectrique s'écrit…",
    [
    "$h\\nu = W_\\text{ext} + E_\\text{c}$",
    "$h\\nu = W_\\text{ext} - E_\\text{c}$",
    "$E_\\text{c} = h\\nu + W_\\text{ext}$",
    "$W_\\text{ext} = h\\nu + E_\\text{c}$"
    ],
    "L'énergie du photon sert à extraire l'électron&nbsp;; le reste devient de l'énergie cinétique."
    ],
    [
    "L'effet photoélectrique a montré que la lumière…",
    [
    "échange de l'énergie avec la matière par quanta, les photons",
    "est uniquement une onde",
    "ne transporte pas d'énergie",
    "est formée d'électrons"
    ],
    "Einstein a interprété l'effet photoélectrique en 1905."
    ],
    [
    "Un atome absorbe un photon lorsque l'énergie du photon…",
    [
    "est égale à l'écart entre deux de ses niveaux d'énergie",
    "est quelconque",
    "est supérieure à tous ses niveaux",
    "est nulle"
    ],
    "Les niveaux d'énergie sont quantifiés."
    ],
    [
    "Dans une cellule photovoltaïque, un photon absorbé peut…",
    [
    "faire passer un électron de la bande de valence à la bande de conduction, s'il a une énergie supérieure au gap",
    "créer un proton",
    "chauffer le semi-conducteur uniquement",
    "émettre un électron hors du silicium"
    ],
    "Il se crée une paire électron-trou."
    ],
    [
    "Le rendement d'une cellule photovoltaïque est…",
    [
    "le rapport entre la puissance électrique fournie et la puissance lumineuse reçue",
    "la puissance électrique fournie",
    "le rapport entre la tension et l'intensité",
    "toujours égal à 1"
    ],
    "Il est de l'ordre de 15 à 25&nbsp;% pour les cellules au silicium courantes."
    ]
    ];   /* [question, [bonne réponse, autres réponses…], explication] */
  function $(s) { return root.querySelector(s); }
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function compose(el) { if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([el]).catch(function () {}); } }   /* formules des questions et des réponses */
  var qEl = $('.nt-ql-q'), bx = $('.nt-ql-btns'), msg = $('.nt-msg'), sc = $('.out-score'), next = $('[data-act="next"]'), prog = $('.nt-prog'), num = $('.nt-qnum');
  var lbl = '<i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante', order = [], k = 0, good = 0, answered = false, fini = false, res = [];
  function bilan(r) { return r === 1 ? 'Parfait&nbsp;: tout est juste&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;: relisez seulement les points manqués.' : (r >= 0.5 ? 'C\u2019est un début&nbsp;: reprenez les parties du cours correspondant aux erreurs.' : 'Relisez le cours, puis recommencez le quiz.')); }
  function progres() { prog.innerHTML = order.map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === k && !fini ? ' cur' : '') + '"></i>'; }).join(''); num.textContent = fini ? 'Bilan' : 'Question ' + (k + 1) + ' sur ' + order.length; }
  function show() {
    answered = false; var q = Q[order[k]], idx = melange(q[1].map(function (_, i) { return i; }));
    qEl.innerHTML = q[0]; msg.textContent = ''; msg.className = 'nt-msg'; bx.innerHTML = '';
    idx.forEach(function (i) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn nt-choix'; b.innerHTML = q[1][i];
      b.addEventListener('click', function () {
        if (answered) { return; } answered = true; var ok = i === 0; res[k] = ok; if (ok) { good++; }
        b.classList.add(ok ? 'nt-choix-ok' : 'nt-choix-ko'); if (!ok) { bx.children[idx.indexOf(0)].classList.add('nt-choix-ok'); }
        msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko'); msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Non.</b> ') + q[2]; compose(msg);
        sc.textContent = good + ' / ' + (k + 1); progres();
      });
      bx.appendChild(b);
    });
    compose(qEl); compose(bx);
    next.innerHTML = k === order.length - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lbl; progres();
  }
  function start() { order = melange(Q.map(function (_, i) { return i; })); k = 0; good = 0; fini = false; res = []; bx.hidden = false; sc.textContent = '0 / 0'; show(); }
  next.addEventListener('click', function () {
    if (fini) { start(); return; }
    if (!answered) { msg.className = 'nt-msg'; msg.textContent = 'Choisissez d\u2019abord une réponse.'; return; }
    k++;
    if (k >= order.length) { fini = true; bx.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + order.length + '</span> ' + bilan(good / order.length); msg.textContent = ''; msg.className = 'nt-msg'; next.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; progres(); return; }
    show();
  });
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', start); } else { start(); }
})();
</script>
