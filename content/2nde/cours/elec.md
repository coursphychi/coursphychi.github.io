+++
title = "Électricité"
draft = false
hidden = true
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
.nt-qcard-large { max-width: 720px; }
.nt-qcard .nt-tr-svg { margin: 0 0 0.5em; }
.nt-tr-ans { display: flex; align-items: center; justify-content: center; gap: 0.5em; flex-wrap: wrap; margin: 0.6em 0; }
.nt-champ { display: inline-flex; align-items: center; gap: 0.35em; white-space: nowrap; margin: 0 0.7em; }
.nt-champ label { display: inline; margin: 0; font-weight: 600; }
.nt-champ input[type="text"] { width: 5.5em !important; min-width: 0; margin: 0; padding: 0.25em 0.5em; text-align: right; font: inherit; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-champ .nt-u { color: var(--slate); }
.nt-qcard { background: linear-gradient(180deg, #FFFFFF, #F8FAFC); border: 1px solid var(--line); border-radius: 16px; padding: 0.9em 1em 1em; margin: 0.4em auto 0.6em; max-width: 620px; box-shadow: 0 6px 18px rgba(15,23,42,.06); }
.nt-ql-btns .nt-choix { padding: 0.6em 1.1em; border-radius: 12px; font-size: 1em; transition: transform .12s, box-shadow .12s; }
.nt-ql-btns .nt-choix:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37,99,235,.18); }
.nt-choix-ok { background: #DCFCE7 !important; border-color: #16A34A !important; color: #166534 !important; }
.nt-choix-ko { background: #FFE4E6 !important; border-color: #E11D48 !important; color: #9F1239 !important; }
.nt-msg.nt-fb { border-radius: 12px; padding: 0.6em 0.9em; text-align: left; }
.nt-msg.nt-fb.ok { background: #F0FDF4; border-left: 4px solid #22C55E; } .nt-msg.nt-fb.ko { background: #FFF1F2; border-left: 4px solid #F43F5E; }
.nt-lab .nt-msg { margin-top: 1em !important; }
.nt-lab [hidden] { display: none !important; }
.nt-svgbox { margin: 0.6em 0; }
.nt-svgbox svg { display: block; width: 100%; height: auto; }
.nt-tr-ans { display: flex; align-items: center; justify-content: center; gap: 0.5em; flex-wrap: wrap; margin: 0.6em 0; }
.nt-tr-ans input { font: inherit; width: 7em; padding: 0.3em 0.6em; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-multi-ctrl { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0.8em; margin: 0.8em 0 0.4em; align-items: stretch; }
.nt-multi-ctrl fieldset { border: 1px solid var(--line); background: #fff; border-radius: 14px; padding: 0.7em 0.9em 0.8em; margin: 0; box-shadow: 0 4px 14px rgba(15,23,42,.05); min-width: 0; }
.nt-multi-ctrl legend { float: left; width: 100%; display: flex; align-items: center; gap: 0.5em; font-size: 0.86em; font-weight: 700; color: #1E293B; padding: 0; margin: 0 0 0.55em; }
.nt-multi-ctrl legend + * { clear: both; }
.nt-step { display: inline-grid; place-items: center; width: 1.6em; height: 1.6em; border-radius: 50%; background: var(--fc); color: #fff; font-size: 0.85em; flex: none; }
.nt-optnote { font-size: 0.8em; color: var(--slate); margin: -0.35em 0 0.45em !important; }
.nt-optrow { display: flex; flex-wrap: wrap; align-items: center; gap: 0.35em; margin: 0.25em 0; }
.nt-optcol { display: flex; flex-direction: column; gap: 0.35em; }
.nt-optcat { width: 5.2em; font-size: 0.78em; color: var(--slate); }
.nt-opt { position: relative; display: inline-flex; align-items: center; cursor: pointer; margin: 0; }
.nt-opt input { position: absolute; opacity: 0; pointer-events: none; }
.nt-opt span { display: inline-flex; align-items: center; gap: 0.4em; padding: 0.32em 0.8em; border-radius: 999px; border: 1.5px solid #E2E8F0; background: #F8FAFC; font-size: 0.9em; line-height: 1.25; transition: border-color .15s, background .15s, box-shadow .15s; }
.nt-optcol .nt-opt span { width: 100%; border-radius: 10px; }
.nt-opt:hover span { border-color: color-mix(in srgb, var(--fc) 55%, #fff); }
.nt-opt input:checked + span { background: var(--fb); border-color: var(--fc); color: #0F172A; font-weight: 600; box-shadow: 0 2px 8px color-mix(in srgb, var(--fc) 22%, transparent); }
.nt-opt input:checked + span::before { content: "\2713"; color: var(--fc); font-weight: 800; }
.nt-opt input:focus-visible + span { outline: 3px solid color-mix(in srgb, var(--fc) 40%, transparent); outline-offset: 2px; }
.nt-figs { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8em; margin: 1em 0; }
.nt-figs figure { margin: 0; text-align: center; }
.nt-figs img { width: 100%; border-radius: 10px; }
.nt-figs figcaption { font-size: 0.88em; color: var(--muted); margin-top: 0.3em; }
.nt-bilan-steps li p { margin: 0.2em 0 !important; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>



## Intensité, tension, résistance {.nt-h2}

### L'intensité du courant {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp">intensité</span> $I$ du courant électrique est le <span class="imp nt-hole">débit de charges électriques</span>&nbsp;: elle indique la quantité de charges qui traverse une section du circuit chaque seconde.</p>
<ul class="nt-facts">
<li>Unité&nbsp;: l'<span class="imp nt-hole">ampère</span> (A).</li>
<li>Appareil de mesure&nbsp;: l'<span class="imp nt-hole">ampèremètre</span>.</li>
<li>Branchement&nbsp;: <span class="imp nt-hole">en série</span>&nbsp;: l'ampèremètre doit être <b>traversé</b> par le courant.</li>
</ul>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Analogie</p>
<p>L'intensité est l'équivalent du <b>débit d'une rivière</b>&nbsp;: la quantité d'eau qui passe sous un pont chaque seconde.</p>
</div>

<div class="nt-svgbox"><svg class='nt-svg' viewBox='0 0 720 220' role='img' aria-label="Pour mesurer une intensité, on retire un fil du circuit et on met l'ampèremètre à sa place : il est traversé par le courant, qui y entre par la borne A et en sort par la borne COM"><g><polyline points='60,60 300,60 300,170 60,170 60,60' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='60' cy='115' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='60' y='120' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='46' y='95' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='46' y='145' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><rect x='160' y='52' width='40' height='16' fill='#fff' stroke='#1E293B' stroke-width='2'/><rect x='158' y='162' width='44' height='16' fill='#fff'/><circle cx='158' cy='170' r='3.6' fill='#1E293B'/><circle cx='202' cy='170' r='3.6' fill='#1E293B'/><text x='180' y='196' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>on retire un fil</text><g transform='translate(250,170) rotate(180)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g></g><g transform='translate(360,0)'><polyline points='60,60 300,60 300,170 60,170 60,60' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='60' cy='115' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='60' y='120' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='46' y='95' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='46' y='145' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><rect x='160' y='52' width='40' height='16' fill='#fff' stroke='#1E293B' stroke-width='2'/><circle cx='180' cy='170' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='180' y='175' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='200' y='164' font-size='10.5' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='160' y='164' font-size='10.5' text-anchor='end' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><g transform='translate(250,170) rotate(180)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><text x='250' y='160' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan></text><text x='180' y='210' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>l'ampèremètre prend la place du fil</text></g><path d='M335,115 l18,0' stroke='#94A3B8' stroke-width='2'/><polygon points='358,115 350,110 350,120' fill='#94A3B8'/></svg></div>
<p class="nt-cap">Pour mesurer une intensité, il faut «&nbsp;casser&nbsp;» le circuit&nbsp;: on retire un fil et on met l'ampèremètre à sa place. Le courant y entre par la borne A et en sort par la borne COM.</p>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention aux bornes et aux calibres</p>
<ul class="nt-facts">
<li>Pour une intensité, il y a souvent deux bornes possibles. On commence <b>toujours</b> par celle protégée par un gros fusible (10&nbsp;A ou 20&nbsp;A), avec le calibre correspondant.</li>
<li>Quel que soit l'appareil, on commence toujours par le <span class="imp nt-hole">plus grand calibre</span>, puis on descend tant que la valeur lue est inférieure au calibre suivant.</li>
<li>Un «&nbsp;1&nbsp;» seul à gauche de l'écran signale qu'on est <b>hors calibre</b>&nbsp;: il faut remonter de calibre.</li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>On lit 0,25&nbsp;A sur le calibre 10&nbsp;A. Le calibre suivant indique «&nbsp;200m&nbsp;». Peut-on changer de borne et de calibre&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>0,25&nbsp;A = 250&nbsp;mA, et 250&nbsp;mA &gt; 200&nbsp;mA&nbsp;: la valeur dépasserait le calibre. <b>Non</b>, on reste sur le calibre 10&nbsp;A.</p>
</div>
</details>

### La tension électrique {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">tension</span> $U$ entre deux points d'un circuit traduit une <span class="imp nt-hole">différence d'état électrique</span> entre ces deux points. C'est elle qui met les charges en mouvement.</p>
<ul class="nt-facts">
<li>Unité&nbsp;: le <span class="imp nt-hole">volt</span> (V).</li>
<li>Appareil de mesure&nbsp;: le <span class="imp nt-hole">voltmètre</span>.</li>
<li>Branchement&nbsp;: <span class="imp nt-hole">en dérivation</span>, aux bornes du dipôle.</li>
</ul>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Analogie</p>
<p>La tension est l'équivalent du <b>dénivelé d'une rivière</b>&nbsp;: c'est la différence d'altitude entre deux points qui fait couler l'eau. Sans dénivelé, pas de courant&nbsp;; mais un dénivelé peut exister sans que l'eau coule (un barrage fermé).</p>
</div>

<div class="nt-svgbox" style="max-width:420px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 360 230' role='img' aria-label="Pour mesurer une tension, on branche le voltmètre en dérivation aux bornes du dipôle ; la flèche qui représente la tension pointe vers la borne V du voltmètre"><polyline points='40,150 320,150' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='120,150 120,70 240,70 240,150' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><rect x='160' y='142' width='40' height='16' fill='#fff' stroke='#1E293B' stroke-width='2'/><circle cx='120' cy='150' r='3.6' fill='#1E293B'/><circle cx='240' cy='150' r='3.6' fill='#1E293B'/><circle cx='180' cy='70' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='180' y='75' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='160' y='64' font-size='10.5' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='200' y='64' font-size='10.5' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><line x1='240' y1='185' x2='128' y2='185' stroke='#0891B2' stroke-width='2.2' stroke-linecap='round'/><polygon points='120,185 131,180 131,190' fill='#0891B2'/><text x='180' y='205' font-size='14' text-anchor='middle' fill='#0891B2' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>dipôle</tspan></text><text x='180' y='133' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>dipôle</text></svg></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>On représente une tension par une <span class="imp nt-hole">flèche</span>. Par convention, la flèche pointe vers la <span class="imp nt-hole">borne V</span> du voltmètre.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Pour mesurer la tension aux bornes d'un générateur, vérifiez toujours que le fil est branché sur la <b>borne V</b> du multimètre. Branché sur la borne A, l'appareil se comporte comme un simple fil&nbsp;: le générateur est en <b>court-circuit</b>&nbsp;!</p>
</div>

### La résistance {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">résistance</span> $R$ d'un dipôle relie la tension à ses bornes et l'intensité qui le traverse&nbsp;: c'est leur <span class="imp nt-hole">rapport</span>, $R = \dfrac{U}{I}$.</p>
<ul class="nt-facts">
<li>Unité&nbsp;: l'<span class="imp nt-hole">ohm</span> ($\Omega$).</li>
<li>Appareil de mesure&nbsp;: l'<span class="imp nt-hole">ohmmètre</span>.</li>
</ul>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Pour mesurer la résistance d'un dipôle, il faut le <b>sortir du circuit</b> et brancher l'ohmmètre à ses bornes. Un ohmmètre ne s'utilise jamais dans un circuit alimenté.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-ask" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Peut-on avoir une tension sans intensité&nbsp;? Où&nbsp;?</p>
</div>
<div class="nt-b nt-ask" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Peut-on avoir une intensité sans tension&nbsp;? Où&nbsp;?</p>
</div>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir les réponses</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>Tension sans intensité&nbsp;: oui.</b> Aux bornes d'une pile non branchée, ou d'un interrupteur ouvert relié à un générateur&nbsp;: la tension existe, mais aucun courant ne passe (comme un barrage fermé).</li>
<li><b>Intensité sans tension&nbsp;: oui.</b> Aux bornes d'un fil, d'un interrupteur fermé, d'un très bon conducteur&nbsp;: il suffit que la résistance du dipôle soit nulle ou quasi nulle.</li>
</ul>
<p class="nt-note">En toute rigueur, la résistance n'est strictement nulle que pour un fil parfaitement conducteur, ce qui n'existe qu'avec les supraconducteurs.</p>
</div>
</details>

<div class="nt-lab nt-quizlab" id="quiz-multi">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Les branchements du multimètre</p>
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

<div class="nt-lab" id="lab-multi">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le multimètre virtuel&nbsp;: à vous de brancher&nbsp;!</p>
<p class="nt-note">Le circuit&nbsp;: un générateur de 6,0&nbsp;V, un conducteur ohmique et une lampe. Mesurez l'intensité dans la lampe, la tension à ses bornes, puis sa résistance. Testez aussi les mauvais branchements, pour voir ce qu'ils provoquent.</p>
<div class="nt-svgbox nt-multi-svg"></div>
<div class="nt-multi-ctrl">
<fieldset style="--fc:#B45309; --fb:#FEF3C7;"><legend><span class="nt-step">1</span>Position du sélecteur</legend>
<div class="nt-optrow"><span class="nt-optcat">tension</span>
<label class="nt-opt"><input type="radio" name="msel" value="V20" checked><span>20&nbsp;V</span></label>
<label class="nt-opt"><input type="radio" name="msel" value="V2"><span>2&nbsp;V</span></label></div>
<div class="nt-optrow"><span class="nt-optcat">intensité</span>
<label class="nt-opt"><input type="radio" name="msel" value="A10"><span>10&nbsp;A</span></label>
<label class="nt-opt"><input type="radio" name="msel" value="A200"><span>200&nbsp;mA</span></label></div>
<div class="nt-optrow"><span class="nt-optcat">résistance</span>
<label class="nt-opt"><input type="radio" name="msel" value="O200"><span>200&nbsp;&Omega;</span></label>
<label class="nt-opt"><input type="radio" name="msel" value="O2k"><span>2&nbsp;k&Omega;</span></label></div>
</fieldset>
<fieldset style="--fc:#BE123C; --fb:#FFE4E6;"><legend><span class="nt-step">2</span>Borne du fil rouge</legend>
<p class="nt-optnote">l'autre fil est sur COM</p>
<div class="nt-optrow">
<label class="nt-opt"><input type="radio" name="mbor" value="VO" checked><span>V&nbsp;&Omega;</span></label>
<label class="nt-opt"><input type="radio" name="mbor" value="mA"><span>mA</span></label>
<label class="nt-opt"><input type="radio" name="mbor" value="10A"><span>10&nbsp;A</span></label></div>
</fieldset>
<fieldset style="--fc:#1D4ED8; --fb:#DBEAFE;"><legend><span class="nt-step">3</span>Branchement de l'appareil</legend>
<div class="nt-optcol">
<label class="nt-opt"><input type="radio" name="mpos" value="deriv" checked><span>en dérivation, aux bornes de la lampe</span></label>
<label class="nt-opt"><input type="radio" name="mpos" value="serie"><span>en série dans le circuit</span></label>
<label class="nt-opt"><input type="radio" name="mpos" value="hors"><span>aux bornes de la lampe sortie du circuit</span></label></div>
</fieldset>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

## Lois des nœuds et des mailles {.nt-h2}

### La loi des nœuds {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Loi des nœuds</p>
<p>La <span class="imp nt-hole">somme des intensités</span> des courants qui <b>arrivent</b> à un nœud est égale à la <span class="imp nt-hole">somme des intensités</span> des courants qui en <b>repartent</b>.</p>
<p class="nt-note">Au collège, on l'appelait «&nbsp;loi d'additivité des intensités&nbsp;».</p>
</div>

<div class="nt-svgbox" style="max-width:520px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-m' viewBox='0 0 420 230' role='img' aria-label="Un générateur alimente une lampe et un conducteur ohmique branchés en dérivation : l'intensité I_G qui arrive au nœud se partage en I_L dans la lampe et I_R dans le conducteur ohmique"><polyline points='60,50 360,50 360,200 60,200 60,50' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='210,50 210,200' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='60' cy='125' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='60' y='130' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='46' y='105' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='46' y='155' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><circle cx='210' cy='125' r='14' fill='#fff' stroke='#1E293B' stroke-width='2'/><path d='M200.1,115.1 L219.9,134.9 M219.9,115.1 L200.1,134.9' stroke='#1E293B' stroke-width='2'/><rect x='352' y='105' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><circle cx='210' cy='50' r='3.6' fill='#1E293B'/><circle cx='210' cy='200' r='3.6' fill='#1E293B'/><g transform='translate(135,50) rotate(0)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><text x='135' y='40' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>G</tspan></text><g transform='translate(210,88) rotate(90)'><polygon points='7,0 -6,-6 -6,6' fill='#D97706'/></g><text x='226' y='92' font-size='14' text-anchor='middle' fill='#D97706' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>L</tspan></text><g transform='translate(290,50) rotate(0)'><polygon points='7,0 -6,-6 -6,6' fill='#0891B2'/></g><text x='290' y='40' font-size='14' text-anchor='middle' fill='#0891B2' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>R</tspan></text></svg></div>
<p class="nt-cap">Ici, la loi des nœuds s'écrit&nbsp;: $I_\text{G} = I_\text{L} + I_\text{R}$. Comme l'eau d'une rivière qui se partage en deux bras, le courant se partage entre les branches.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Dans une même branche, les dipôles sont <b>en série</b>&nbsp;: ils sont tous traversés par la <span class="imp nt-hole">même intensité</span>.</p>
</div>

<div class="nt-lab nt-trainer" id="lab-noeuds">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Appliquer la loi des nœuds</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard nt-qcard-large">
<div class="nt-svgbox nt-tr-svg"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-zone"><div class="nt-tr-ans"><span class="nt-champ"><label for="kir-noeuds">Réponse&nbsp;:</label><input id="kir-noeuds" type="text" inputmode="decimal"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Circuit suivant</button></div>
</div>

### La loi des mailles {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Loi des mailles</p>
<p>Dans une maille comportant un générateur, la <span class="imp nt-hole">tension aux bornes du générateur</span> est égale à la <span class="imp nt-hole">somme des tensions</span> aux bornes des récepteurs.</p>
<p class="nt-note">Une maille est une boucle fermée du circuit. Au collège, on parlait de «&nbsp;loi d'additivité des tensions&nbsp;».</p>
</div>

<div class="nt-svgbox" style="max-width:440px; margin-left:auto; margin-right:auto;"><svg class='nt-svg nt-svg-s' viewBox='0 0 380 250' role='img' aria-label="Un générateur, une lampe et un conducteur ohmique en série : la tension U_G aux bornes du générateur est égale à la somme des tensions U_L et U_R aux bornes des récepteurs"><polyline points='90,40 250,40 250,220 90,220 90,40' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='90' cy='130' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='90' y='135' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='76' y='110' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='76' y='160' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><circle cx='250' cy='85' r='14' fill='#fff' stroke='#1E293B' stroke-width='2'/><path d='M240.1,75.1 L259.9,94.9 M259.9,75.1 L240.1,94.9' stroke='#1E293B' stroke-width='2'/><rect x='242' y='150' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><line x1='52' y1='190' x2='52' y2='78' stroke='#E11D48' stroke-width='2.2' stroke-linecap='round'/><polygon points='52,70 57,81 47,81' fill='#E11D48'/><text x='36' y='130' font-size='14' text-anchor='end' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>G</tspan></text><line x1='282' y1='110' x2='282' y2='68' stroke='#D97706' stroke-width='2.2' stroke-linecap='round'/><polygon points='282,60 287,71 277,71' fill='#D97706'/><text x='294' y='85' font-size='14' text-anchor='start' fill='#D97706' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>L</tspan></text><line x1='282' y1='195' x2='282' y2='153' stroke='#0891B2' stroke-width='2.2' stroke-linecap='round'/><polygon points='282,145 287,156 277,156' fill='#0891B2'/><text x='294' y='170' font-size='14' text-anchor='start' fill='#0891B2' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>R</tspan></text></svg></div>
<p class="nt-cap">Ici, la loi des mailles s'écrit&nbsp;: $U_\text{G} = U_\text{L} + U_\text{R}$. Comme pour une rivière, le dénivelé total se partage entre les différents tronçons.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Des dipôles branchés <b>en dérivation</b> entre les deux mêmes points ont la <span class="imp nt-hole">même tension</span> à leurs bornes.</p>
</div>

<div class="nt-lab nt-trainer" id="lab-mailles">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Appliquer la loi des mailles</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard nt-qcard-large">
<div class="nt-svgbox nt-tr-svg"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-zone"><div class="nt-tr-ans"><span class="nt-champ"><label for="kir-mailles">Réponse&nbsp;:</label><input id="kir-mailles" type="text" inputmode="decimal"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Circuit suivant</button></div>
</div>

<p class="nt-center"><a href="https://www.geogebra.org/m/kp2qtnqx" target="_blank" rel="noopener"><i class="fa-solid fa-diagram-project"></i>&nbsp; Applet GeoGebra&nbsp;: loi des nœuds</a> &nbsp;·&nbsp; <a href="https://www.geogebra.org/m/w7snw4aw" target="_blank" rel="noopener">Applet GeoGebra&nbsp;: loi des mailles</a></p>

### Exercices {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 1</p>
<p>Déterminer les intensités $I_2$, $I_4$ et $I_5$.</p>
<div class="nt-svgbox"><svg class='nt-svg nt-svg-m' viewBox='0 0 560 240' role='img' aria-label="Exercice : un générateur alimente une lampe et un conducteur ohmique en dérivation. I1 = 0,120 A et I3 = 80 mA ; il faut trouver I2, I4 et I5"><polyline points='60,50 380,50 380,210 60,210 60,50' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='220,50 220,210' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='60' cy='130' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='60' y='135' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='46' y='110' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='46' y='160' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><circle cx='220' cy='130' r='14' fill='#fff' stroke='#1E293B' stroke-width='2'/><path d='M210.1,120.1 L229.9,139.9 M229.9,120.1 L210.1,139.9' stroke='#1E293B' stroke-width='2'/><rect x='372' y='110' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><circle cx='220' cy='50' r='3.6' fill='#1E293B'/><circle cx='220' cy='210' r='3.6' fill='#1E293B'/><g transform='translate(140,50) rotate(0)'><polygon points='7,0 -6,-6 -6,6' fill='#E11D48'/></g><text x='140' y='40' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>1</tspan></text><g transform='translate(300,50) rotate(0)'><polygon points='7,0 -6,-6 -6,6' fill='#2563EB'/></g><text x='300' y='40' font-size='14' text-anchor='middle' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>3</tspan></text><g transform='translate(220,172) rotate(90)'><polygon points='7,0 -6,-6 -6,6' fill='#D97706'/></g><text x='236' y='176' font-size='14' text-anchor='middle' fill='#D97706' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>2</tspan></text><g transform='translate(380,172) rotate(90)'><polygon points='7,0 -6,-6 -6,6' fill='#7C3AED'/></g><text x='396' y='176' font-size='14' text-anchor='middle' fill='#7C3AED' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>5</tspan></text><g transform='translate(60,178) rotate(-90)'><polygon points='7,0 -6,-6 -6,6' fill='#059669'/></g><text x='44' y='182' font-size='14' text-anchor='middle' fill='#059669' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>I</tspan><tspan font-size='10' dy='4'>4</tspan></text><g font-family='Georgia, serif'><text x='430' y='70' font-size='14' text-anchor='start' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='700'>I<tspan font-size="9" dy="3">1</tspan><tspan dy="-3"> = 0,120 A</tspan></text><text x='430' y='92' font-size='14' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>I<tspan font-size="9" dy="3">3</tspan><tspan dy="-3"> = 80 mA</tspan></text><text x='430' y='132' font-size='14' text-anchor='start' fill='#D97706' font-family='system-ui, sans-serif' font-weight='700'>I<tspan font-size="9" dy="3">2</tspan><tspan dy="-3"> = ?</tspan></text><text x='430' y='154' font-size='14' text-anchor='start' fill='#059669' font-family='system-ui, sans-serif' font-weight='700'>I<tspan font-size="9" dy="3">4</tspan><tspan dy="-3"> = ?</tspan></text><text x='430' y='176' font-size='14' text-anchor='start' fill='#7C3AED' font-family='system-ui, sans-serif' font-weight='700'>I<tspan font-size="9" dy="3">5</tspan><tspan dy="-3"> = ?</tspan></text></g></svg></div>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la correction</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>Loi des nœuds au nœud du haut&nbsp;: $I_1 = I_2 + I_3$. Attention aux unités&nbsp;: $I_1 = 0{,}120$&nbsp;A = 120&nbsp;mA, donc $I_2 = 120 - 80 = 40$&nbsp;mA.</p></li>
<li><p>$I_5$ est dans la même branche que $I_3$ (en série avec le conducteur ohmique)&nbsp;: $I_5 = I_3 = 80$&nbsp;mA.</p></li>
<li><p>$I_4$ traverse le générateur, comme $I_1$&nbsp;: $I_4 = I_1 = 0{,}120$&nbsp;A. On le retrouve par la loi des nœuds au nœud du bas&nbsp;: $I_4 = I_2 + I_5 = 40 + 80 = 120$&nbsp;mA.</p></li>
</ol>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 2</p>
<p>Déterminer les tensions $U_2$, $U_5$ et $U_6$.</p>
<div class="nt-svgbox"><svg class='nt-svg nt-svg-m' viewBox='0 0 600 275' role='img' aria-label="Exercice : un générateur, un conducteur ohmique en série, puis une lampe en dérivation avec une DEL et un conducteur ohmique. U1 = 6,0 V, U3 = 4,2 V et U4 = 3,0 V ; il faut trouver U2, U5 et U6"><polyline points='90,60 400,60 400,230 90,230 90,60' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='260,60 260,230' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='90' cy='145' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='90' y='150' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='76' y='125' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='76' y='175' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><rect x='155' y='52' width='40' height='16' fill='#fff' stroke='#1E293B' stroke-width='2'/><circle cx='260' cy='145' r='14' fill='#fff' stroke='#1E293B' stroke-width='2'/><path d='M250.1,135.1 L269.9,154.9 M269.9,135.1 L250.1,154.9' stroke='#1E293B' stroke-width='2'/><g transform='translate(400,110) rotate(0)'><polygon points='-11,-9 11,-9 0,9' fill='#fff' stroke='#1E293B' stroke-width='2'/><line x1='-11' y1='9' x2='11' y2='9' stroke='#1E293B' stroke-width='2.4'/><path d='M14,-6 l8,-6 M18,-2 l8,-6' stroke='#1E293B' stroke-width='1.4'/><polygon points='22,-12 18,-11 21,-8' fill='#1E293B'/><polygon points='26,-8 22,-7 25,-4' fill='#1E293B'/></g><rect x='392' y='165' width='16' height='40' fill='#fff' stroke='#1E293B' stroke-width='2'/><circle cx='260' cy='60' r='3.6' fill='#1E293B'/><circle cx='260' cy='230' r='3.6' fill='#1E293B'/><line x1='52' y1='205' x2='52' y2='93' stroke='#2563EB' stroke-width='2.2' stroke-linecap='round'/><polygon points='52,85 57,96 47,96' fill='#2563EB'/><text x='38' y='145' font-size='14' text-anchor='end' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>1</tspan></text><line x1='205' y1='34' x2='153' y2='34' stroke='#E11D48' stroke-width='2.2' stroke-linecap='round'/><polygon points='145,34 156,29 156,39' fill='#E11D48'/><text x='175' y='26' font-size='14' text-anchor='middle' fill='#E11D48' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>2</tspan></text><line x1='228' y1='170' x2='228' y2='128' stroke='#059669' stroke-width='2.2' stroke-linecap='round'/><polygon points='228,120 233,131 223,131' fill='#059669'/><text x='216' y='145' font-size='14' text-anchor='end' fill='#059669' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>3</tspan></text><line x1='440' y1='128' x2='440' y2='100' stroke='#D97706' stroke-width='2.2' stroke-linecap='round'/><polygon points='440,92 445,103 435,103' fill='#D97706'/><text x='452' y='114' font-size='14' text-anchor='start' fill='#D97706' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>4</tspan></text><line x1='440' y1='205' x2='440' y2='173' stroke='#7C3AED' stroke-width='2.2' stroke-linecap='round'/><polygon points='440,165 445,176 435,176' fill='#7C3AED'/><text x='452' y='189' font-size='14' text-anchor='start' fill='#7C3AED' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>5</tspan></text><line x1='205' y1='256' x2='153' y2='256' stroke='#0891B2' stroke-width='2.2' stroke-linecap='round'/><polygon points='145,256 156,251 156,261' fill='#0891B2'/><text x='175' y='248' font-size='14' text-anchor='middle' fill='#0891B2' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>U</tspan><tspan font-size='10' dy='4'>6</tspan></text><g><text x='480' y='90' font-size='14' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>U<tspan font-size="9" dy="3">1</tspan><tspan dy="-3"> = 6,0 V</tspan></text><text x='480' y='112' font-size='14' text-anchor='start' fill='#059669' font-family='system-ui, sans-serif' font-weight='700'>U<tspan font-size="9" dy="3">3</tspan><tspan dy="-3"> = 4,2 V</tspan></text><text x='480' y='134' font-size='14' text-anchor='start' fill='#D97706' font-family='system-ui, sans-serif' font-weight='700'>U<tspan font-size="9" dy="3">4</tspan><tspan dy="-3"> = 3,0 V</tspan></text><text x='480' y='172' font-size='14' text-anchor='start' fill='#E11D48' font-family='system-ui, sans-serif' font-weight='700'>U<tspan font-size="9" dy="3">2</tspan><tspan dy="-3"> = ?</tspan></text><text x='480' y='194' font-size='14' text-anchor='start' fill='#7C3AED' font-family='system-ui, sans-serif' font-weight='700'>U<tspan font-size="9" dy="3">5</tspan><tspan dy="-3"> = ?</tspan></text><text x='480' y='216' font-size='14' text-anchor='start' fill='#0891B2' font-family='system-ui, sans-serif' font-weight='700'>U<tspan font-size="9" dy="3">6</tspan><tspan dy="-3"> = ?</tspan></text></g></svg></div>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la correction</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>Maille de gauche (générateur, conducteur ohmique, lampe)&nbsp;: $U_1 = U_2 + U_3$, donc $U_2 = 6{,}0 - 4{,}2 = 1{,}8$&nbsp;V.</p></li>
<li><p>Maille de droite (lampe, DEL, conducteur ohmique)&nbsp;: la lampe est en dérivation avec la branche de droite, donc $U_3 = U_4 + U_5$, d'où $U_5 = 4{,}2 - 3{,}0 = 1{,}2$&nbsp;V.</p></li>
<li><p>$U_6$ est la tension aux bornes d'un simple fil&nbsp;: $U_6 = 0$&nbsp;V.</p></li>
</ol>
</div>
</details>

## Caractéristique d'un dipôle {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">caractéristique</span> d'un dipôle électrique est la <span class="imp nt-hole">relation entre l'intensité</span> $I$ du courant qui le traverse <span class="imp nt-hole">et la tension</span> $U$ à ses bornes. Elle est généralement fournie sous la forme d'un graphique représentant&nbsp;:</p>
<ul class="nt-facts">
<li>soit la tension en fonction de l'intensité&nbsp;: $U = f(I)$&nbsp;;</li>
<li>soit l'intensité en fonction de la tension&nbsp;: $I = g(U)$.</li>
</ul>
</div>

### Le montage pour tracer une caractéristique {.nt-h3}

<div class="nt-svgbox"><svg class='nt-svg' viewBox='0 0 720 250' role='img' aria-label="Deux montages pour tracer la caractéristique d'un dipôle : avec un générateur de tension réglable, ou avec un générateur fixe et un rhéostat en série. Dans les deux cas, l'ampèremètre est en série avec le dipôle et le voltmètre en dérivation à ses bornes"><g><polyline points='50,60 250,60 250,190 50,190 50,60' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='250,85 300,85 300,165 250,165' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='50' cy='125' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='50' y='130' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='36' y='105' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='36' y='155' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><circle cx='150' cy='60' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='150' y='65' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='130' y='54' font-size='10.5' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='170' y='54' font-size='10.5' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><rect x='242' y='105' width='16' height='40' fill='#FEF3C7' stroke='#1E293B' stroke-width='2'/><text x='250' y='129' font-size='13' text-anchor='middle' fill='#92400E' font-family='system-ui, sans-serif' font-weight='700'>?</text><circle cx='300' cy='125' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='300' y='130' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='310' y='109' font-size='10.5' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='310' y='149' font-size='10.5' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><circle cx='250' cy='85' r='3.6' fill='#1E293B'/><circle cx='250' cy='165' r='3.6' fill='#1E293B'/><text x='50' y='175' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'></text><text x='160' y='244' font-size='12.5' text-anchor='middle' fill='#334155' font-family='system-ui, sans-serif' font-weight='700'>générateur de tension réglable</text></g><g transform='translate(370,0)'><polyline points='50,60 250,60 250,190 50,190 50,60' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><polyline points='250,85 300,85 300,165 250,165' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><circle cx='50' cy='125' r='17' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='50' y='130' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>G</text><text x='36' y='105' font-size='15' text-anchor='middle' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>+</text><text x='36' y='155' font-size='15' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>−</text><circle cx='150' cy='60' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='150' y='65' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='130' y='54' font-size='10.5' text-anchor='end' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>A</text><text x='170' y='54' font-size='10.5' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><rect x='242' y='105' width='16' height='40' fill='#FEF3C7' stroke='#1E293B' stroke-width='2'/><text x='250' y='129' font-size='13' text-anchor='middle' fill='#92400E' font-family='system-ui, sans-serif' font-weight='700'>?</text><circle cx='300' cy='125' r='13' fill='#fff' stroke='#1E293B' stroke-width='2'/><text x='300' y='130' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='310' y='109' font-size='10.5' text-anchor='start' fill='#DC2626' font-family='system-ui, sans-serif' font-weight='700'>V</text><text x='310' y='149' font-size='10.5' text-anchor='start' fill='#2563EB' font-family='system-ui, sans-serif' font-weight='700'>COM</text><circle cx='250' cy='85' r='3.6' fill='#1E293B'/><circle cx='250' cy='165' r='3.6' fill='#1E293B'/><rect x='130' y='182' width='40' height='16' fill='#fff' stroke='#1E293B' stroke-width='2'/><line x1='124' y1='204' x2='170.7' y2='178.8' stroke='#1E293B' stroke-width='1.6'/><polygon points='176,176 170,183.8 166.2,176.7' fill='#1E293B'/><text x='150' y='222' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>rhéostat (résistance variable)</text><text x='50' y='175' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'></text><text x='160' y='244' font-size='12.5' text-anchor='middle' fill='#334155' font-family='system-ui, sans-serif' font-weight='700'>générateur fixe + rhéostat</text></g></svg></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour tracer une caractéristique, on mesure en même temps l'intensité qui traverse le dipôle (<span class="imp nt-hole">ampèremètre en série</span>) et la tension à ses bornes (<span class="imp nt-hole">voltmètre en dérivation</span>), pour plusieurs réglages du circuit. Deux montages sont possibles&nbsp;:</p>
<ul class="nt-facts">
<li>avec un <b>générateur de tension réglable</b>&nbsp;;</li>
<li>avec un générateur fixe et une <b>résistance variable</b>, le <span class="imp nt-hole">rhéostat</span>, en série avec le dipôle. C'est souvent le montage préférable&nbsp;: le rhéostat permet de faire varier l'intensité progressivement, et il <b>limite</b> l'intensité qui traverse le dipôle, ce qui le protège.</li>
</ul>
</div>

{{< youtube-plus id="MzIkKmHrtDc" ratio="16x9" width="500" shadow=true rounded=true >}}

<div class="nt-lab" id="lab-carac">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Tracer la caractéristique d'un dipôle</p>
<div class="nt-ctrl">Dipôle étudié&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="cdip" value="ohm" checked><span>conducteur ohmique</span></label>
<label><input type="radio" name="cdip" value="lampe"><span>lampe</span></label>
<label><input type="radio" name="cdip" value="del"><span>DEL</span></label>
<label><input type="radio" name="cdip" value="therm"><span>thermistance</span></label>
</div>
</div>
<div class="nt-ctrl">Montage&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="cmode" value="rheo" checked><span>générateur fixe + rhéostat</span></label>
<label><input type="radio" name="cmode" value="gen"><span>générateur réglable</span></label>
</div>
</div>
<div class="nt-lab-pair" style="grid-template-columns: minmax(0, 1fr) minmax(0, 1.2fr); align-items: center;">
<div class="nt-svgbox nt-carac-svg" style="margin:0;"></div>
<canvas style="height:260px; background:#fff; border-radius:10px;" aria-label="Caractéristique U = f(I) : les points relevés"></canvas>
</div>
<label class="nt-ctrl"><span class="out-slabel">Résistance du rhéostat</span>&nbsp;: <b class="out-s"></b><input type="range" min="0" max="1" step="0.002" value="0.3"></label>
<div class="nt-read" aria-live="polite"><span>U = <b class="out-u"></b></span><span>I = <b class="out-i"></b></span><span>U/I = <b class="out-r"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="pt"><i class="fa-solid fa-location-dot"></i>&nbsp; Relever le point</button>
<button type="button" class="nt-btn" data-act="model"><i class="fa-solid fa-chart-line"></i>&nbsp; Afficher / masquer la courbe</button>
<button type="button" class="nt-btn" data-act="clear"><i class="fa-solid fa-eraser"></i>&nbsp; Effacer</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Avec le générateur réglable, la DEL est protégée par un conducteur ohmique de 100&nbsp;&Omega;&nbsp;: branchée seule, elle serait détruite. Pour la thermistance, l'échauffement dû au courant est pris en compte.</p>
</div>

### La loi d'Ohm {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Si la tension $U_R$ aux bornes d'un dipôle est <span class="imp nt-hole">proportionnelle</span> à l'intensité $I_R$ du courant qui le traverse, alors ce dipôle est un <span class="imp nt-hole">conducteur ohmique</span>&nbsp;: sa caractéristique est une <b>droite qui passe par l'origine</b>, modélisée par une fonction linéaire.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi d'Ohm</p>
<p class="nt-f-math">$$U_R = R\times I_R$$</p>
<div class="nt-f-units"><span>$U_R$ en <b>volts (V)</b></span><span>$R$, la résistance (constante), en <b>ohms (Ω)</b></span><span>$I_R$ en <b>ampères (A)</b></span></div>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention aux unités</p>
<p>Dans la loi d'Ohm, l'intensité doit être en <b>ampères</b>&nbsp;: avec $I$ = 2,0&nbsp;mA = 0,0020&nbsp;A et $R$ = 1&nbsp;500&nbsp;Ω, on trouve $U = 1\,500 \times 0{,}0020 = 3{,}0$&nbsp;V.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Un dipôle peut se comporter comme un conducteur ohmique sur une plage restreinte d'intensité, puis s'en éloigner quand l'intensité sort de cette plage&nbsp;: sa résistance varie alors. C'est le cas de la thermistance, qui chauffe quand l'intensité devient trop grande (voir l'animation ci-dessus).</p>
</div>

### Le point de fonctionnement {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>En superposant sur un même graphique la caractéristique d'un générateur et celle d'un récepteur, on peut prévoir l'intensité du courant délivré par le générateur et la tension aux bornes du récepteur&nbsp;: ce sont les coordonnées du point d'intersection des deux courbes, appelé <span class="imp nt-hole">point de fonctionnement</span> du circuit.</p>
</div>

<div class="nt-lab" id="lab-ptf">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Une lampe branchée sur un générateur</p>
<div class="nt-svgbox nt-ptf-svg" style="max-width:420px; margin-left:auto; margin-right:auto;"></div>
<canvas style="height:270px; background:#fff;" aria-label="Caractéristiques du générateur idéal et de la lampe, et leur point d'intersection"></canvas>
<label class="nt-ctrl">Tension du générateur&nbsp;: <b class="out-E"></b><input type="range" data-p="E" min="1" max="8" step="0.1" value="6"></label>
<div class="nt-read" aria-live="polite"><span>point de fonctionnement&nbsp;: <b class="out-pt"></b></span></div>
<p class="nt-note">Le générateur est idéal&nbsp;: la tension à ses bornes ne dépend pas de l'intensité qu'il débite. Sa caractéristique est donc une droite horizontale. Le point de fonctionnement donne la tension aux bornes de la lampe et l'intensité qui la traverse.</p>
</div>


## Les capteurs&nbsp;: l'exemple de la thermistance {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un <span class="imp">capteur résistif</span> est un dipôle dont la <span class="imp nt-hole">résistance varie</span> avec une grandeur physique&nbsp;: température, éclairement, pression… La <b>thermistance</b> est un capteur de température&nbsp;:</p>
<ul class="nt-facts">
<li>pour une thermistance <b>CTN</b> (coefficient de température négatif), la résistance <b>diminue</b> quand la température augmente&nbsp;;</li>
<li>pour une thermistance <b>CTP</b> (coefficient de température positif), elle <b>augmente</b>.</li>
</ul>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour utiliser un capteur, il faut d'abord l'<span class="imp nt-hole">étalonner</span>&nbsp;: tracer la <span class="imp nt-hole">courbe d'étalonnage</span> qui relie sa résistance à la grandeur d'intérêt, mesurée par ailleurs avec un instrument de référence (ici, un thermomètre). On peut ensuite lire la grandeur à partir de la résistance.</p>
</div>

<div class="nt-lab" id="lab-etal">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Étalonner la thermistance</p>
<canvas class="scene" style="height:270px;" aria-label="Bécher d'eau sur une plaque chauffante, avec un thermomètre et la thermistance reliée à un ohmmètre"></canvas>
<canvas class="graph" style="height:240px; margin-top:8px; background:#fff;" aria-label="Courbe d'étalonnage : résistance de la thermistance en fonction de la température"></canvas>
<div class="nt-btns">
<button type="button" class="nt-btn" data-act="heat"><i class="fa-solid fa-fire"></i>&nbsp; Chauffer</button>
<button type="button" class="nt-btn nt-btn-main" data-act="pt"><i class="fa-solid fa-location-dot"></i>&nbsp; Relever (&theta;, R)</button>
<button type="button" class="nt-btn" data-act="curve"><i class="fa-solid fa-chart-line"></i>&nbsp; Afficher la courbe</button>
<button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Eau glacée</button>
</div>
<div class="nt-read" aria-live="polite"><span>points relevés&nbsp;: <b class="out-n">0</b></span></div>
<p class="nt-msg" aria-live="polite">Eau glacée à 5&nbsp;°C. Allumez la plaque et relevez des points.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">D'autres capteurs autour de nous</span></summary>
<div class="nt-d-body">
<p>La thermistance n'est qu'un exemple parmi de très nombreux capteurs. Beaucoup sont, comme elle, des <b>capteurs résistifs</b>&nbsp;:</p>
<ul class="nt-facts">
<li><b>La photorésistance</b> (LDR)&nbsp;: sa résistance diminue quand elle est éclairée. Elle allume l'éclairage public à la tombée de la nuit.</li>
<li><b>La sonde Pt100</b>&nbsp;: un fil de platine dont la résistance (100&nbsp;Ω à 0&nbsp;°C) augmente de façon presque proportionnelle à la température. Plus précise qu'une thermistance, elle équipe les laboratoires et l'industrie.</li>
<li><b>La jauge de contrainte</b>&nbsp;: un fin réseau conducteur collé sur une pièce, dont la résistance change quand la pièce se déforme. On la trouve dans les pèse-personnes et les balances électroniques.</li>
<li><b>Le capteur de pression piézorésistif</b>&nbsp;: une membrane minuscule dont la résistance varie avec la pression. Il sert d'altimètre dans les smartphones et mesure la pression des pneus.</li>
</ul>
<p>D'autres capteurs ne sont pas résistifs, mais transforment eux aussi une grandeur physique en signal électrique&nbsp;:</p>
<ul class="nt-facts">
<li><b>Le thermocouple</b>&nbsp;: deux métaux différents soudés produisent une tension qui dépend de la température. Il mesure les très hautes températures (fours, moteurs).</li>
<li><b>La photodiode</b>&nbsp;: elle produit un courant quand elle reçoit de la lumière. Un capteur d'appareil photo en contient des millions, une par pixel.</li>
<li><b>Le capteur à effet Hall</b>&nbsp;: il mesure un champ magnétique. C'est la boussole de votre téléphone.</li>
<li><b>L'accéléromètre</b>&nbsp;: une minuscule masse mobile dont on mesure le déplacement. C'est lui qui fait tourner l'écran d'un téléphone quand on le penche.</li>
</ul>
<p class="nt-note">Un smartphone contient plus d'une dizaine de capteurs différents&nbsp;!</p>
</div>
</details>


## Bilan&nbsp;: mesurer une température avec un voltmètre {.nt-h2}

<p>Pour comprendre les océans, les océanographes mesurent la température de l'eau, en surface comme en profondeur, avec un <b>bathythermographe</b>. Cet appareil contient un capteur électrique de température&nbsp;: une <b>thermistance</b>, dont la résistance varie avec la température.</p>
<p>Tout l'intérêt du dispositif est là&nbsp;: seule la thermistance est plongée dans l'eau, parfois à des centaines de mètres de profondeur. Le reste du circuit reste à bord, au sec. On y mesure simplement une <b>tension</b>, aux bornes d'un conducteur ohmique, et on en déduit, grâce aux lois de l'électricité, la <b>température de l'eau</b> autour de la thermistance, bien loin de là.</p>
<p>Comment passe-t-on de cette tension à une température&nbsp;?</p>

<p>Le montage du bathythermographe est représenté ci-dessous. La DEL, associée à un conducteur ohmique de protection $R_P$, joue le rôle d'afficheur&nbsp;: plus l'eau est chaude, plus elle brille. Armés de la caractéristique de l'association DEL + $R_P$ et de la courbe d'étalonnage de la thermistance, on va remonter étape par étape de la tension $U_{R_0}$ mesurée par le voltmètre à la température de l'eau dans laquelle baigne la thermistance.<sup></p>

<div class="nt-lab" id="lab-bilan">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">De la tension mesurée à la température de l'eau</p>
<div class="nt-svgbox nt-bilan-svg" style="max-width:640px; margin-left:auto; margin-right:auto;"></div>
<ol class="nt-steps nt-bilan-steps"></ol>
<div class="nt-lab-pair">
<figure><canvas class="assoc" style="height:230px; background:#fff; border-radius:10px;" aria-label="Caractéristique de l'ensemble DEL et conducteur ohmique de protection, avec la lecture du point de fonctionnement"></canvas><figcaption>caractéristique de l'ensemble DEL + R<sub>P</sub></figcaption></figure>
<figure><canvas class="etal" style="height:230px; background:#fff; border-radius:10px;" aria-label="Courbe d'étalonnage de la thermistance, avec la lecture de la température"></canvas><figcaption>courbe d'étalonnage de la thermistance</figcaption></figure>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Étape suivante</button></div>
<p class="nt-note">Valeurs de l'exemple&nbsp;: générateur de 10,0&nbsp;V, $R_0$ = 1&nbsp;500&nbsp;Ω, $R_P$ = 1&nbsp;kΩ, thermistance CTN de 1&nbsp;500&nbsp;Ω à 25&nbsp;°C. On néglige ici l'échauffement de la thermistance par le courant&nbsp;: plongée dans l'eau, elle est bien refroidie. En TP, ce léger échauffement explique que la résistance calculée soit un peu plus faible que celle mesurée à l'ohmmètre.</p>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function canvasCtx(cv) {
    var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function bilanTxt(r) { return r === 1 ? 'Parfait&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;!' : (r >= 0.5 ? 'C\u2019est un bon début&nbsp;: relisez les cas manqués.' : 'Relisez le cours, puis recommencez.')); }
  function txt(c, s, x, y, color, font, align) { c.font = font || '12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round'; c.lineWidth = 4; c.strokeStyle = 'rgba(255,255,255,.92)'; c.strokeText(s, x, y); c.fillStyle = color; c.fillText(s, x, y); }
  function tex(el) { if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([el]); } }
  function num(s) { return parseFloat(String(s).replace(',', '.').replace(/\s/g, '')); }
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
    function therm(x, y, o) {   /* thermistance : conducteur ohmique traversé d'une diagonale, terminée par un petit segment à chaque bout */
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
    function svg(w, h, body, label, cls) { return "<svg class='" + (cls || 'nt-svg nt-svg-m') + "' viewBox='0 0 " + w + ' ' + h + "' role='img' aria-label=\"" + label + "\">" + body + "</svg>"; }
    return { wire: wire, text: text, qty: qty, node: node, res: res, therm: therm, rheo: rheo, lamp: lamp, gen: gen, meter: meter, led: led, sw: sw, iarr: iarr, uarr: uarr, svg: svg, INK: INK };
  })();
  /* ================= Quiz : les branchements du multimètre ================= */
  var QUIZ = {
    'quiz-multi': [
      ['Pour mesurer l\u2019intensité du courant qui traverse une lampe, on branche l\u2019ampèremètre…', ['en série avec la lampe', 'en dérivation aux bornes de la lampe', 'à la place de la lampe'], 0, 'L\u2019ampèremètre doit être <b>traversé</b> par le courant&nbsp;: on «&nbsp;casse&nbsp;» le circuit et on le place en série.'],
      ['Pour mesurer la tension aux bornes d\u2019une lampe, on branche le voltmètre…', ['en série avec la lampe', 'en dérivation aux bornes de la lampe', 'à la place d\u2019un fil'], 1, 'Le voltmètre se branche <b>en dérivation</b>, ses deux fils aux deux bornes de la lampe&nbsp;: inutile d\u2019ouvrir le circuit.'],
      ['Pour mesurer la résistance d\u2019un dipôle à l\u2019ohmmètre, il faut…', ['laisser le dipôle dans le circuit alimenté', 'sortir le dipôle du circuit', 'brancher l\u2019ohmmètre en série'], 1, 'Un ohmmètre ne s\u2019utilise <b>jamais</b> dans un circuit alimenté&nbsp;: on sort le dipôle et on branche l\u2019ohmmètre à ses bornes.'],
      ['Sur quel calibre commence-t-on une mesure&nbsp;?', ['le plus petit', 'le plus grand', 'n\u2019importe lequel'], 1, 'On commence <b>toujours par le plus grand calibre</b>, puis on descend tant que la valeur lue reste inférieure au calibre suivant.'],
      ['On lit 0,25 A sur le calibre 10 A. Le calibre suivant est 200 mA. Peut-on y passer&nbsp;?', ['oui', 'non'], 1, '0,25 A = 250 mA, et 250 mA &gt; 200 mA&nbsp;: la valeur dépasserait le calibre. On reste sur 10 A.'],
      ['On lit 0,12 A sur le calibre 10 A. Le calibre suivant est 200 mA. Peut-on y passer&nbsp;?', ['oui', 'non'], 0, '0,12 A = 120 mA &lt; 200 mA&nbsp;: on peut descendre au calibre 200 mA (en branchant le fil sur la borne mA), pour une mesure plus précise.'],
      ['L\u2019écran affiche seulement «&nbsp;1&nbsp;» à gauche. Cela signifie…', ['que la valeur mesurée vaut 1', 'que l\u2019on est hors calibre', 'que la pile est déchargée'], 1, 'Un «&nbsp;1&nbsp;» seul à gauche signale que la valeur dépasse le calibre&nbsp;: il faut passer à un calibre plus grand.'],
      ['Pour mesurer une intensité inconnue, on branche le fil sur…', ['la borne mA', 'la borne protégée par le gros fusible (10 A ou 20 A)', 'la borne V Ω'], 1, 'On commence par la borne la mieux protégée (10 A ou 20 A). On ne passe sur la borne mA que si la valeur le permet.'],
      ['On mesure la tension aux bornes d\u2019un générateur avec le fil branché par erreur sur la borne A. Que se passe-t-il&nbsp;?', ['rien de grave', 'le générateur est en court-circuit', 'l\u2019écran affiche la tension'], 1, 'Par la borne A, l\u2019appareil est presque un simple fil&nbsp;: branché aux bornes du générateur, il le met <b>en court-circuit</b>. Toujours vérifier la borne V&nbsp;!'],
      ['Vers quelle borne du voltmètre pointe la flèche qui représente la tension mesurée&nbsp;?', ['la borne V', 'la borne COM'], 0, 'Par convention, la flèche de tension pointe vers la borne V du voltmètre.']
    ]
  };
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
  /* ================= Le multimètre virtuel ================= */
  (function () {
    var root = document.getElementById('lab-multi');
    if (!root) { return; }
    var box = $(root, '.nt-multi-svg'), msg = $(root, '.nt-msg');
    /* circuit : générateur 6,0 V, conducteur ohmique 8,0 Ω et lampe ; en fonctionnement I = 0,250 A, U_L = 4,00 V */
    var E = 6.0, RR = 8.0, IL = 0.25, UL = 4.0, RFROID = 2.4;
    var SEL = { V20: ['V', 20, 'V'], V2: ['V', 2, 'V'], A10: ['A', 10, 'A'], A200: ['A', 0.2, 'mA'], O200: ['O', 200, '\u03a9'], O2k: ['O', 2000, 'k\u03a9'] };
    function lit(v, cal, unit) {   /* affichage de l'écran : « 1. » si hors calibre */
      if (Math.abs(v) > cal) { return '1.'; }
      var d = cal >= 100 ? 1 : (cal >= 10 ? 2 : 3);
      if (unit === 'mA') { return fr(v * 1000, 1); }
      if (unit === 'k\u03a9') { return fr(v / 1000, 3); }
      return fr(v, d);
    }
    function evaluer(sel, bor, pos) {
      var s = SEL[sel], f = s[0], cal = s[1], u = s[2], shunt = bor !== 'VO';
      var r = { aff: '0.00', lampe: 1, ok: false, txt: '' };
      if (pos === 'hors') {
        r.lampe = 0;
        if (f === 'O' && bor === 'VO') { r.aff = lit(RFROID, cal, u); r.ok = r.aff !== '1.'; r.txt = r.ok ? 'Bonne méthode&nbsp;: la lampe est sortie du circuit et l\u2019ohmmètre est branché à ses bornes, sur la borne V&nbsp;Ω. Elle mesure ' + fr(RFROID, 1) + '&nbsp;Ω. Surprise&nbsp;: en fonctionnement, U/I = 4,00/0,250 = 16&nbsp;Ω. La résistance du filament augmente beaucoup quand il chauffe&nbsp;!' : 'Hors calibre&nbsp;: choisissez un calibre plus grand.'; }
        else { r.txt = 'La lampe est sortie du circuit&nbsp;: aucune tension ni aucun courant à mesurer. Hors circuit, on ne mesure que des <b>résistances</b>, à l\u2019ohmmètre, sur la borne V&nbsp;Ω.'; }
        return r;
      }
      if (f === 'O') { r.txt = '<b>Jamais d\u2019ohmmètre dans un circuit alimenté&nbsp;!</b> La mesure n\u2019a aucun sens et l\u2019appareil peut être endommagé. Il faut sortir le dipôle du circuit.'; r.aff = '---'; return r; }
      if (pos === 'serie') {
        if (!shunt) {   /* borne V Ω en série : l'appareil coupe le courant */
          r.lampe = 0;
          if (f === 'V') { r.aff = lit(E, cal, u); r.txt = 'Voltmètre <b>en série</b>&nbsp;: il empêche presque tout courant de passer (la lampe s\u2019éteint) et indique à peu près la tension du générateur. Pour une tension, le voltmètre se branche <b>en dérivation</b>.'; }
          else { r.aff = lit(0, cal, u); r.txt = 'Fil branché sur la borne V&nbsp;Ω alors que le sélecteur est sur «&nbsp;A&nbsp;»&nbsp;: l\u2019appareil coupe le circuit, la lampe s\u2019éteint et il affiche 0. Pour une intensité, le fil va sur la borne A (ou mA).'; }
          return r;
        }
        if (f === 'A') {
          if (bor === 'mA' && IL > 0.2) { r.aff = '1.'; r.lampe = 0; r.txt = '<b>Attention&nbsp;!</b> 0,250 A traverse la borne mA, prévue pour 200 mA au plus&nbsp;: le fusible de protection fond, le circuit s\u2019ouvre et la lampe s\u2019éteint. Il fallait commencer par la borne 10 A.'; return r; }
          if (bor === '10A' && cal < 1) { r.aff = '1.'; r.txt = 'Hors calibre&nbsp;: 0,250 A dépasse 200 mA. Revenez au calibre 10 A.'; return r; }
          r.aff = lit(IL, cal, u); r.ok = true; r.txt = 'Bonne mesure&nbsp;: l\u2019ampèremètre est <b>en série</b>, traversé par le courant&nbsp;: I = 0,25 A. Peut-on descendre au calibre 200 mA&nbsp;? 0,25 A = 250 mA &gt; 200 mA&nbsp;: non, on reste sur 10 A.'; return r;
        }
        r.aff = lit(0.002, cal, u); r.txt = 'Sélecteur sur «&nbsp;V&nbsp;» mais fil sur une borne A&nbsp;: l\u2019appareil se comporte comme un simple fil, la lampe brille normalement et l\u2019écran indique presque 0. Branchement incohérent&nbsp;!'; return r;
      }
      /* en dérivation aux bornes de la lampe */
      if (!shunt) {
        if (f === 'V') { r.aff = lit(UL, cal, u); r.ok = r.aff !== '1.'; r.txt = r.ok ? 'Bonne mesure&nbsp;: le voltmètre est <b>en dérivation</b> aux bornes de la lampe&nbsp;: U<sub>L</sub> = 4,00 V. Le calibre 20 V est le bon (le calibre 2 V serait dépassé).' : 'Hors calibre&nbsp;: 4,00 V dépasse le calibre 2 V. Revenez au calibre 20 V.'; }
        else { r.aff = lit(0, cal, u); r.txt = 'Sélecteur sur «&nbsp;A&nbsp;» mais fil sur la borne V&nbsp;Ω, en dérivation&nbsp;: rien de dangereux, mais la mesure n\u2019a pas de sens.'; }
        return r;
      }
      /* borne A en dérivation : court-circuit de la lampe */
      r.lampe = 0; var Icc = E / RR;
      if (bor === 'mA') { r.aff = '0.00'; r.txt = '<b>Court-circuit&nbsp;!</b> Par la borne mA, l\u2019appareil est presque un fil&nbsp;: il court-circuite la lampe (qui s\u2019éteint). ' + fr(Icc, 2) + '&nbsp;A le traversent et le fusible fond aussitôt. Un ampèremètre ne se branche <b>jamais</b> en dérivation.'; }
      else { r.aff = f === 'A' ? lit(Icc, cal, u) : lit(0.004, cal, u); r.txt = '<b>Court-circuit&nbsp;!</b> Par la borne A, l\u2019appareil est presque un fil&nbsp;: il court-circuite la lampe, qui s\u2019éteint, et une intensité élevée (' + fr(Icc, 2) + '&nbsp;A) le traverse. Un ampèremètre se branche <b>en série</b>.'; }
      return r;
    }
    function gauche(svg, x, y) {   /* appareil vertical : étiquettes V et COM passées à gauche (CI.meter les met à droite, côté où arrivent les cordons) */
      return svg.replace("x='" + (x + 10) + "' y='" + (y - 16) + "'", "x='" + (x - 9) + "' y='" + (y - 16) + "'").replace("x='" + (x + 10) + "' y='" + (y + 24) + "'", "x='" + (x - 9) + "' y='" + (y + 24) + "'").replace(/text-anchor='start'/g, "text-anchor='end'");
    }
    function dessin(sel, bor, pos, r) {
      var s = SEL[sel], L = s[0] === 'O' ? '\u03a9' : s[0], b = '', inSerie = pos === 'serie', hors = pos === 'hors', ap;   /* ap : position du symbole de l'appareil dans le circuit */
      /* ---- circuit : générateur à gauche, conducteur ohmique en haut, lampe à droite ---- */
      if (!hors) {
        b += CI.wire([[50, 60], [250, 60], [250, 210], [50, 210], [50, 60]]);
        b += CI.gen(50, 135, 'v', 't') + CI.res(150, 60, 'h') + CI.lamp(250, 135, r.lampe);
        if (inSerie) { b += CI.meter(150, 210, L, 'r'); ap = [150, 210]; }
        else { b += CI.wire([[250, 95], [310, 95], [310, 175], [250, 175]]) + CI.node(250, 95) + CI.node(250, 175) + gauche(CI.meter(310, 135, L, 't'), 310, 135); ap = [310, 135]; }
      } else {
        b += CI.lamp(180, 135, 0) + CI.wire([[180, 121], [180, 95], [260, 95], [260, 175], [180, 175], [180, 149]]) + gauche(CI.meter(260, 135, L, 't'), 260, 135) + CI.text(180, 210, 'lampe sortie du circuit', '#64748B', 11.5);
        ap = [260, 135];
      }
      /* ---- le multimètre ---- */
      var mx = 410, mw = 190, cxm = mx + mw / 2;
      b += "<defs><linearGradient id='gMm' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#FCD34D'/><stop offset='1' stop-color='#F59E0B'/></linearGradient>"
         + "<radialGradient id='gKnob' cx='.4' cy='.35' r='.7'><stop offset='0' stop-color='#64748B'/><stop offset='1' stop-color='#1E293B'/></radialGradient></defs>";
      b += "<rect x='" + mx + "' y='8' width='" + mw + "' height='272' rx='22' fill='url(#gMm)' stroke='#B45309' stroke-width='1.5'/>";
      b += "<rect x='" + (mx + 10) + "' y='18' width='" + (mw - 20) + "' height='252' rx='14' fill='#334155'/>";
      b += "<rect x='" + (mx + 22) + "' y='30' width='" + (mw - 44) + "' height='48' rx='6' fill='#D9F99D' stroke='#65A30D'/>";
      b += "<text x='" + (mx + mw - 30) + "' y='65' font-size='28' text-anchor='end' fill='#1A2E05' font-family='ui-monospace, Menlo, monospace'>" + r.aff + "</text>";
      b += "<text x='" + (mx + 28) + "' y='44' font-size='9' fill='#3F6212' font-family='system-ui, sans-serif'>" + ({ V: 'V', A: s[2] === 'mA' ? 'mA' : 'A', O: s[2] === 'k\u03a9' ? 'k\u03a9' : '\u03a9' })[s[0]] + "</text>";
      /* sélecteur rotatif : positions autour du bouton */
      var kx = cxm, ky = 150, POS = [['OFF', -90], ['V20', -145, '20', 'V'], ['V2', 180, '2', 'V'], ['O200', 140, '200', '\u03a9'], ['O2k', 40, '2k', '\u03a9'], ['A200', 0, '200m', 'A'], ['A10', -35, '10', 'A']];
      ['V', 'A', '\u03a9'].forEach(function (g, i) { var ang = [-162, -18, 90][i] * Math.PI / 180, rg = i === 2 ? 58 : 70; b += "<text x='" + (kx + rg * Math.cos(ang)).toFixed(1) + "' y='" + (ky + rg * Math.sin(ang) + 4).toFixed(1) + "' font-size='12' text-anchor='middle' fill='#FCD34D' font-family='system-ui, sans-serif' font-weight='800'>" + g + "</text>"; });
      POS.forEach(function (p) {
        var a = p[1] * Math.PI / 180, on = p[0] === sel, lx = kx + 50 * Math.cos(a), ly = ky + 50 * Math.sin(a);
        b += "<line x1='" + (kx + 38 * Math.cos(a)).toFixed(1) + "' y1='" + (ky + 38 * Math.sin(a)).toFixed(1) + "' x2='" + (kx + 43 * Math.cos(a)).toFixed(1) + "' y2='" + (ky + 43 * Math.sin(a)).toFixed(1) + "' stroke='" + (on ? '#FCD34D' : '#94A3B8') + "' stroke-width='2'/>";
        b += "<text x='" + lx.toFixed(1) + "' y='" + (ly + 4).toFixed(1) + "' font-size='" + (on ? 11.5 : 10.5) + "' text-anchor='middle' fill='" + (on ? '#FCD34D' : '#CBD5E1') + "' font-family='system-ui, sans-serif' font-weight='" + (on ? 800 : 500) + "'>" + (p[2] || p[0]) + "</text>";
      });
      var sa = POS.filter(function (p) { return p[0] === sel; })[0][1] * Math.PI / 180;
      b += "<circle cx='" + kx + "' cy='" + ky + "' r='32' fill='url(#gKnob)' stroke='#0F172A' stroke-width='1.5'/>";
      b += "<line x1='" + kx + "' y1='" + ky + "' x2='" + (kx + 30 * Math.cos(sa)).toFixed(1) + "' y2='" + (ky + 30 * Math.sin(sa)).toFixed(1) + "' stroke='#FCD34D' stroke-width='5' stroke-linecap='round'/>";
      b += "<circle cx='" + kx + "' cy='" + ky + "' r='6' fill='#0F172A'/>";
      /* bornes, centrées en bas */
      var BOR = [['10A', '10 A', -60], ['mA', 'mA', -20], ['COM', 'COM', 20], ['VO', 'V\u03a9', 60]];
      BOR.forEach(function (p) {
        var x = cxm + p[2], used = p[0] === 'COM' || p[0] === bor, col = p[0] === 'COM' ? '#0F172A' : '#DC2626';
        b += "<circle cx='" + x + "' cy='232' r='11' fill='" + (used ? col : '#1E293B') + "' stroke='" + (p[0] === 'COM' ? '#94A3B8' : '#F87171') + "' stroke-width='2.5'/>";
        b += "<circle cx='" + x + "' cy='232' r='4' fill='" + (used ? '#F8FAFC' : '#475569') + "'/>";
        b += "<text x='" + x + "' y='259' font-size='10' text-anchor='middle' fill='#E2E8F0' font-family='system-ui, sans-serif' font-weight='700'>" + p[1] + "</text>";
      });
      /* cordons : de la borne utilisée et de COM jusqu'aux bornes de l'appareil dans le circuit (cercle de rayon 13) ;
         appareil vertical (voltmètre, ohmmètre) : borne V en haut, COM en bas ; appareil horizontal (ampèremètre) : borne A à droite, COM à gauche */
      var xr = cxm + BOR.filter(function (p) { return p[0] === bor; })[0][2], xc = cxm + 20, vertical = !inSerie, pr, pc;
      /* cordons souples : une seule courbe continue, sans coude ; ils passent sous le multimètre (bas du boîtier : y = 280)
         appareil vertical : le rouge arrive sur la borne du haut par au-dessus, le noir sur celle du bas par en dessous ; appareil horizontal : un simple arc */
      function fil(d, col, op) { return "<path d='" + d + "' fill='none' stroke='" + col + "' stroke-width='2.2' stroke-opacity='" + op + "' stroke-linecap='round'/>"; }
      if (vertical) {   /* départ vertical, arc en U sous le boîtier, remontée dans l'espace libre, puis arrivée en biais sur la borne (sans longer les fils du circuit) */
        pr = [ap[0] + 2, ap[1] - 13]; pc = [ap[0] + 2, ap[1] + 13];
        var xg = mx - 30, xn = mx - 54;
        b += fil('M' + xr + ',232 L' + xr + ',286 C' + xr + ',326 ' + xg + ',326 ' + xg + ',288 C' + xg + ',' + (pr[1] + 10) + ' ' + (pr[0] + 30) + ',' + (pr[1] - 30) + ' ' + pr[0] + ',' + pr[1], '#DC2626', 0.65);
        b += fil('M' + xc + ',232 L' + xc + ',286 C' + xc + ',318 ' + xn + ',318 ' + xn + ',288 C' + xn + ',' + (pc[1] + 60) + ' ' + (pc[0] + 30) + ',' + (pc[1] + 30) + ' ' + pc[0] + ',' + pc[1], '#0F172A', 0.55);
      } else {
        pr = [ap[0] + 13, ap[1] + 2]; pc = [ap[0] - 13, ap[1] + 2];
        b += fil('M' + xr + ',232 L' + xr + ',286 C' + xr + ',324 ' + pr[0] + ',330 ' + pr[0] + ',' + pr[1], '#DC2626', 0.65);
        b += fil('M' + xc + ',232 L' + xc + ',286 C' + xc + ',318 ' + pc[0] + ',322 ' + pc[0] + ',' + pc[1], '#0F172A', 0.55);
      }
      b += "<circle cx='" + pr[0] + "' cy='" + pr[1] + "' r='3.2' fill='#DC2626'/><circle cx='" + pc[0] + "' cy='" + pc[1] + "' r='3.2' fill='#0F172A'/>";   /* fiches */
      return CI.svg(610, 324, b, 'Le circuit, l\u2019appareil de mesure branché, et le multimètre avec son écran, son sélecteur rotatif et ses bornes', 'nt-svg');
    }
    function maj() {
      var sel = $(root, '[name="msel"]:checked').value, bor = $(root, '[name="mbor"]:checked').value, pos = $(root, '[name="mpos"]:checked').value;
      var r = evaluer(sel, bor, pos);
      box.innerHTML = dessin(sel, bor, pos, r);
      msg.innerHTML = (r.ok ? '<span style="color:#16A34A;">\u2714 </span>' : '<span style="color:#E11D48;">\u2716 </span>') + r.txt;
    }
    $$(root, 'input[type="radio"]').forEach(function (x) { x.addEventListener('change', maj); });
    maj();
  })();
  /* ================= Entraînements : loi des nœuds et loi des mailles ================= */
  var COLS = ['#E11D48', '#2563EB', '#059669', '#D97706', '#7C3AED', '#0891B2'];
  function rnd(a, b, st) { return a + st * Math.floor(Math.random() * ((b - a) / st + 1)); }
  function enA(mA) { return Math.random() < 0.35 ? fr(mA / 1000, 3) + '&nbsp;A' : Math.round(mA) + '&nbsp;mA'; }
  function legende(items) {   /* données et inconnue, à droite du schéma */
    return items.map(function (it, i) {
      return "<text x='420' y='" + (60 + i * 24) + "' font-size='14' fill='" + it[2] + "' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>" + it[0] + "</tspan><tspan font-size='9' dy='3'>" + it[1] + "</tspan><tspan dy='-3' font-family='system-ui, sans-serif'> = " + it[3] + "</tspan></text>";
    }).join('');
  }
  var PB = {
    noeuds: [
      function () {   /* deux branches en dérivation */
        var I2 = rnd(20, 200, 5), I3 = rnd(20, 200, 5), I1 = I2 + I3, inc = pick([1, 2, 3]), V = { 1: I1, 2: I2, 3: I3 };
        var b = CI.wire([[50, 50], [360, 50], [360, 210], [50, 210], [50, 50]]) + CI.wire([[205, 50], [205, 210]]);
        b += CI.gen(50, 130, 'v', 't') + CI.lamp(205, 130) + CI.res(360, 130, 'v') + CI.node(205, 50) + CI.node(205, 210);
        b += CI.iarr(130, 50, 'r', 'I', '1', COLS[0]) + CI.iarr(205, 92, 'd', 'I', '2', COLS[3], 16, 4) + CI.iarr(285, 50, 'r', 'I', '3', COLS[1]);
        b += legende([1, 2, 3].map(function (k) { return ['I', String(k), COLS[{ 1: 0, 2: 3, 3: 1 }[k]], k === inc ? '?' : enA(V[k])]; }));
        return { svg: CI.svg(560, 240, b, 'Circuit à deux branches en dérivation'), q: 'Calculer l\u2019intensité <b>I<sub>' + inc + '</sub></b> (en mA).', rep: V[inc], unit: 'mA',
          expl: 'Loi des nœuds au nœud du haut&nbsp;: I<sub>1</sub> = I<sub>2</sub> + I<sub>3</sub>' + (inc === 1 ? ', donc I<sub>1</sub> = ' + I2 + ' + ' + I3 + ' = ' + I1 + '&nbsp;mA.' : (inc === 2 ? ', donc I<sub>2</sub> = I<sub>1</sub> \u2212 I<sub>3</sub> = ' + I1 + ' \u2212 ' + I3 + ' = ' + I2 + '&nbsp;mA.' : ', donc I<sub>3</sub> = I<sub>1</sub> \u2212 I<sub>2</sub> = ' + I1 + ' \u2212 ' + I2 + ' = ' + I3 + '&nbsp;mA.')) + ' (Pensez à convertir&nbsp;: 1&nbsp;A = 1&nbsp;000&nbsp;mA.)' };
      },
      function () {   /* trois branches */
        var a = rnd(20, 150, 5), bb = rnd(20, 150, 5), cc = rnd(20, 150, 5), I = a + bb + cc, inc = pick([0, 1, 2, 3]), V = [I, a, bb, cc], N = ['I', 'I<sub>1</sub>', 'I<sub>2</sub>', 'I<sub>3</sub>'];
        var b = CI.wire([[50, 50], [380, 50], [380, 210], [50, 210], [50, 50]]) + CI.wire([[170, 50], [170, 210]]) + CI.wire([[275, 50], [275, 210]]);
        b += CI.gen(50, 130, 'v', 't') + CI.lamp(170, 130) + CI.res(275, 130, 'v') + CI.lamp(380, 130) + CI.node(170, 50) + CI.node(275, 50) + CI.node(170, 210) + CI.node(275, 210);
        b += CI.iarr(110, 50, 'r', 'I', '', COLS[0]) + CI.iarr(170, 92, 'd', 'I', '1', COLS[3], 16, 4) + CI.iarr(275, 92, 'd', 'I', '2', COLS[1], 16, 4) + CI.iarr(380, 92, 'd', 'I', '3', COLS[2], 16, 4);
        b += legende([['I', '', COLS[0]], ['I', '1', COLS[3]], ['I', '2', COLS[1]], ['I', '3', COLS[2]]].map(function (it, k) { return [it[0], it[1], it[2], k === inc ? '?' : enA(V[k])]; }));
        return { svg: CI.svg(560, 240, b, 'Circuit à trois branches en dérivation'), q: 'Calculer l\u2019intensité <b>' + N[inc] + '</b> (en mA).', rep: V[inc], unit: 'mA',
          expl: 'Le courant I se partage entre les trois branches&nbsp;: I = I<sub>1</sub> + I<sub>2</sub> + I<sub>3</sub>' + (inc === 0 ? ' = ' + a + ' + ' + bb + ' + ' + cc + ' = ' + I + '&nbsp;mA.' : ', donc ' + N[inc] + ' = ' + I + ' \u2212 ' + [a, bb, cc].filter(function (_, i) { return i !== inc - 1; }).join(' \u2212 ') + ' = ' + V[inc] + '&nbsp;mA.') };
      },
      function () {   /* même intensité en série (exercice du cours) */
        var I1 = rnd(80, 250, 10), I3 = rnd(20, I1 - 20, 5), inc = pick(['4', '5']), rep = inc === '4' ? I1 : I3;
        var b = CI.wire([[50, 50], [360, 50], [360, 210], [50, 210], [50, 50]]) + CI.wire([[205, 50], [205, 210]]);
        b += CI.gen(50, 130, 'v', 't') + CI.lamp(205, 130) + CI.res(360, 130, 'v') + CI.node(205, 50) + CI.node(205, 210);
        b += CI.iarr(130, 50, 'r', 'I', '1', COLS[0]) + CI.iarr(285, 50, 'r', 'I', '3', COLS[1]) + CI.iarr(50, 182, 'u', 'I', '4', COLS[2], -16, 4) + CI.iarr(360, 178, 'd', 'I', '5', COLS[4], 16, 4);
        b += legende([['I', '1', COLS[0], enA(I1)], ['I', '3', COLS[1], enA(I3)], ['I', inc, inc === '4' ? COLS[2] : COLS[4], '?']]);
        return { svg: CI.svg(560, 240, b, 'Circuit à deux branches, avec les intensités dans les fils'), q: 'Calculer l\u2019intensité <b>I<sub>' + inc + '</sub></b> (en mA).', rep: rep, unit: 'mA',
          expl: inc === '4' ? 'I<sub>4</sub> traverse le générateur, comme I<sub>1</sub>&nbsp;: ils sont dans la <b>même branche</b>, donc en série. Dans une même branche, l\u2019intensité est la même partout&nbsp;: I<sub>4</sub> = I<sub>1</sub> = ' + I1 + '&nbsp;mA. (On peut aussi l\u2019obtenir par la loi des nœuds au nœud du bas.)'
            : 'I<sub>5</sub> et I<sub>3</sub> sont dans la <b>même branche</b>, en série avec le conducteur ohmique&nbsp;: I<sub>5</sub> = I<sub>3</sub> = ' + I3 + '&nbsp;mA.' };
      }
    ],
    mailles: [
      function () {   /* une seule maille */
        var UL = rnd(15, 60, 1) / 10, UR = rnd(10, 50, 1) / 10, UG = Math.round((UL + UR) * 10) / 10, inc = pick(['G', 'L', 'R']), V = { G: UG, L: UL, R: UR };
        var b = CI.wire([[90, 40], [250, 40], [250, 220], [90, 220], [90, 40]]);
        b += CI.gen(90, 130, 'v', 't') + CI.lamp(250, 85) + CI.res(250, 170, 'v');
        b += CI.uarr(52, 190, 52, 70, 'U', 'G', COLS[0], -16, 0, 'end') + CI.uarr(282, 110, 282, 60, 'U', 'L', COLS[3], 12, 0, 'start') + CI.uarr(282, 195, 282, 145, 'U', 'R', COLS[5], 12, 0, 'start');
        b += legende([['U', 'G', COLS[0]], ['U', 'L', COLS[3]], ['U', 'R', COLS[5]]].map(function (it) { return [it[0], it[1], it[2], it[1] === inc ? '?' : fr(V[it[1]], 1) + '&nbsp;V']; }));
        return { svg: CI.svg(560, 250, b, 'Circuit à une seule maille'), q: 'Calculer la tension <b>U<sub>' + inc + '</sub></b> (en V).', rep: V[inc], unit: 'V',
          expl: 'Loi des mailles&nbsp;: U<sub>G</sub> = U<sub>L</sub> + U<sub>R</sub>' + (inc === 'G' ? ' = ' + fr(UL, 1) + ' + ' + fr(UR, 1) + ' = ' + fr(UG, 1) + '&nbsp;V.' : ', donc U<sub>' + inc + '</sub> = ' + fr(UG, 1) + ' \u2212 ' + fr(inc === 'L' ? UR : UL, 1) + ' = ' + fr(V[inc], 1) + '&nbsp;V.') };
      },
      function () {   /* deux mailles (exercice du cours) */
        var U1 = rnd(50, 120, 1) / 10, U3 = rnd(25, Math.round(U1 * 10) - 10, 1) / 10, U4 = rnd(18, Math.min(30, Math.round(U3 * 10) - 5), 1) / 10;
        var U2 = Math.round((U1 - U3) * 10) / 10, U5 = Math.round((U3 - U4) * 10) / 10, inc = pick(['2', '5', '3']);
        var b = CI.wire([[90, 60], [400, 60], [400, 230], [90, 230], [90, 60]]) + CI.wire([[260, 60], [260, 230]]);
        b += CI.gen(90, 145, 'v', 't') + CI.res(175, 60, 'h') + CI.lamp(260, 145) + CI.led(400, 110, 'v', 'd') + CI.res(400, 185, 'v') + CI.node(260, 60) + CI.node(260, 230);
        b += CI.uarr(52, 205, 52, 85, 'U', '1', COLS[1], -14, 0, 'end') + CI.uarr(205, 34, 145, 34, 'U', '2', COLS[0], 0, -8) + CI.uarr(228, 170, 228, 120, 'U', '3', COLS[2], -12, 0, 'end') + CI.uarr(440, 128, 440, 92, 'U', '4', COLS[3], 12, 4, 'start') + CI.uarr(440, 205, 440, 165, 'U', '5', COLS[4], 12, 4, 'start');
        var V = { 1: U1, 2: U2, 3: U3, 4: U4, 5: U5 }, show = inc === '3' ? ['1', '2', '4'] : ['1', '3', '4'];
        var leg = show.map(function (k) { return ['U', k, COLS[{ 1: 1, 2: 0, 3: 2, 4: 3 }[k]], fr(V[k], 1) + '&nbsp;V']; }).concat([['U', inc, COLS[{ 2: 0, 3: 2, 5: 4 }[inc]], '?']]);
        var svgb = b.replace(/<text x='420'/g, "<text x='470'") + legende(leg).replace(/x='420'/g, "x='480'");
        var ex = { '2': 'Maille de gauche (générateur, conducteur ohmique, lampe)&nbsp;: U<sub>1</sub> = U<sub>2</sub> + U<sub>3</sub>, donc U<sub>2</sub> = ' + fr(U1, 1) + ' \u2212 ' + fr(U3, 1) + ' = ' + fr(U2, 1) + '&nbsp;V.',
          '3': 'Maille de gauche&nbsp;: U<sub>1</sub> = U<sub>2</sub> + U<sub>3</sub>, donc U<sub>3</sub> = ' + fr(U1, 1) + ' \u2212 ' + fr(U2, 1) + ' = ' + fr(U3, 1) + '&nbsp;V.',
          '5': 'Maille de droite (lampe, DEL, conducteur ohmique)&nbsp;: la lampe et la branche de droite sont en dérivation, donc U<sub>3</sub> = U<sub>4</sub> + U<sub>5</sub>, d\u2019où U<sub>5</sub> = ' + fr(U3, 1) + ' \u2212 ' + fr(U4, 1) + ' = ' + fr(U5, 1) + '&nbsp;V.' }[inc];
        return { svg: CI.svg(620, 265, svgb, 'Circuit à deux mailles'), q: 'Calculer la tension <b>U<sub>' + inc + '</sub></b> (en V).', rep: V[inc], unit: 'V', expl: ex };
      },
      function () {   /* tension aux bornes d'un interrupteur ou d'un fil */
        var UG = rnd(30, 120, 5) / 10, ouvert = Math.random() < 0.5;
        var b = CI.wire([[90, 50], [300, 50], [300, 210], [90, 210], [90, 50]]);
        b += CI.gen(90, 130, 'v', 't') + CI.sw(195, 50, 'h', ouvert) + CI.lamp(300, 130, ouvert ? 0 : 1);
        b += CI.uarr(52, 180, 52, 80, 'U', 'G', COLS[0], -16, 0, 'end') + CI.uarr(225, 24, 165, 24, 'U', 'K', COLS[4], 0, -8);
        b += legende([['U', 'G', COLS[0], fr(UG, 1) + '&nbsp;V'], ['U', 'K', COLS[4], '?']]);
        return { svg: CI.svg(560, 240, b, 'Circuit avec un interrupteur ' + (ouvert ? 'ouvert' : 'fermé') + ' et une lampe'), q: 'L\u2019interrupteur K est <b>' + (ouvert ? 'ouvert' : 'fermé') + '</b>. Calculer la tension <b>U<sub>K</sub></b> à ses bornes (en V).', rep: ouvert ? UG : 0, unit: 'V',
          expl: ouvert ? 'Interrupteur ouvert&nbsp;: aucun courant ne passe, donc la tension aux bornes de la lampe est nulle (U<sub>L</sub> = 0). Loi des mailles&nbsp;: U<sub>G</sub> = U<sub>K</sub> + U<sub>L</sub>, donc U<sub>K</sub> = ' + fr(UG, 1) + '&nbsp;V. Il y a une <b>tension sans intensité</b>&nbsp;!'
            : 'Interrupteur fermé&nbsp;: il se comporte comme un fil, de résistance nulle. La tension à ses bornes est nulle&nbsp;: U<sub>K</sub> = 0&nbsp;V, bien qu\u2019il soit traversé par le courant (<b>intensité sans tension</b>).' };
      }
    ]
  };
  ['noeuds', 'mailles'].forEach(function (type) {   /* interface : numéro de question, pastilles, carte (circuit, question, réponse), retour coloré */
    var root = document.getElementById('lab-' + type);
    if (!root) { return; }
    var box = $(root, '.nt-tr-svg'), qEl = $(root, '.nt-tr-q'), inp = $(root, 'input[type="text"]'), uEl = $(root, '.nt-tr-unit'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), zone = $(root, '.nt-tr-zone'), prog = $(root, '.nt-prog'), num0 = $(root, '.nt-qnum');
    var bV = $(root, '[data-act="check"]'), bN = $(root, '[data-act="next"]'), lblN = bN.innerHTML, NQ = 6, n = 0, good = 0, cur = null, done = false, fini = false, res = [];
    function progres() { prog.innerHTML = Array.apply(null, Array(NQ)).map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === n - (done ? 1 : 0) && !fini ? ' cur' : '') + '"></i>'; }).join(''); num0.textContent = fini ? 'Bilan' : 'Question ' + Math.min(NQ, n + (done ? 0 : 1)) + ' sur ' + NQ; }
    function nouveau() { cur = pick(PB[type])(); box.innerHTML = cur.svg; box.hidden = false; qEl.innerHTML = cur.q; uEl.textContent = cur.unit; inp.value = ''; msg.textContent = ''; msg.className = 'nt-msg'; done = false; bV.disabled = false; inp.disabled = false; bN.innerHTML = n === NQ - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lblN; progres(); }
    function start() { n = 0; good = 0; fini = false; res = []; sc.textContent = '0 / 0'; zone.hidden = false; nouveau(); }
    bV.addEventListener('click', function () {
      if (done || fini) { return; }
      var v = num(inp.value); if (isNaN(v)) { msg.className = 'nt-msg'; msg.textContent = 'Entrez une valeur numérique.'; return; }
      var ok = Math.abs(v - cur.rep) <= Math.max(0.051, Math.abs(cur.rep) * 0.01); done = true; res[n] = ok; n++; if (ok) { good++; }
      bV.disabled = true; inp.disabled = true; sc.textContent = good + ' / ' + n;
      msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko');
      msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Non</b>&nbsp;: la réponse est ' + fr(cur.rep, cur.unit === 'V' ? 1 : 0) + '&nbsp;' + cur.unit + '. ') + cur.expl; progres();
    });
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { bV.click(); } });
    bN.addEventListener('click', function () {
      if (fini) { start(); return; }
      if (!done) { msg.className = 'nt-msg'; msg.textContent = 'Validez d\u2019abord votre réponse.'; return; }
      if (n >= NQ) { fini = true; zone.hidden = true; box.hidden = true; box.innerHTML = ''; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + NQ + '</span> ' + bilanTxt(good / NQ); msg.textContent = ''; msg.className = 'nt-msg'; bN.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; progres(); return; }
      nouveau();
    });
    start();
  });
  /* ================= Modèles des dipôles : U en fonction de I ================= */
  var TH = { R25: 1500, B: 4000, T25: 298.15, Rth: 300 };
  function Rtherm(theta) { return TH.R25 * Math.exp(TH.B * (1 / (theta + 273.15) - 1 / TH.T25)); }
  var IS = 0.02 / Math.exp(2.0 / 0.05);
  var DIP = {
    ohm: { nom: 'conducteur ohmique (220 \u03a9)', U: function (I) { return 220 * I; }, Imax: 0.03, Umax: 6.5, unitI: 'mA', kI: 1000, Rh: [10, 10000], UG: 6 },
    lampe: { nom: 'lampe (6 V ; 0,3 A)', U: function (I) { return I * (4 + 178 * I * I); }, Imax: 0.32, Umax: 6.5, unitI: 'mA', kI: 1000, Rh: [0, 200], UG: 6 },
    del: { nom: 'DEL', U: function (I) { return 0.05 * Math.log(1 + Math.max(0, I) / IS); }, Imax: 0.04, Umax: 2.5, unitI: 'mA', kI: 1000, Rh: [100, 10000], UG: 6 },
    therm: { nom: 'thermistance (CTN)', U: function (I) {   /* auto-échauffement : la thermistance chauffe quand l'intensité augmente */
      var T = TH.T25, U = 0; for (var k = 0; k < 60; k++) { var R = TH.R25 * Math.exp(TH.B * (1 / T - 1 / TH.T25)); U = R * I; T = 0.5 * T + 0.5 * (TH.T25 + TH.Rth * U * I); } return U; }, Imax: 0.005, Umax: 6.5, unitI: 'mA', kI: 1000, Rh: [1000, 20000], UG: 4.5 }
  };
  function solveI(f, lo, hi) { for (var k = 0; k < 70; k++) { var m = (lo + hi) / 2; if (f(m) > 0) { hi = m; } else { lo = m; } } return (lo + hi) / 2; }
  /* ================= Tracer la caractéristique d'un dipôle ================= */
  (function () {
    var root = document.getElementById('lab-carac');
    if (!root) { return; }
    var cv = $(root, 'canvas'), box = $(root, '.nt-carac-svg'), rS = $(root, 'input[type="range"]'), oS = $(root, '.out-s'), oU = $(root, '.out-u'), oI = $(root, '.out-i'), oR = $(root, '.out-r'), msg = $(root, '.nt-msg'), S;
    var dip = 'ohm', mode = 'rheo', pts = [], modele = false, E = 6.0, RP = 100;
    function etat() {
      var d = DIP[dip], s = +rS.value, I, U;
      if (mode === 'gen') {   /* générateur réglable de 0 à 6 V ; la DEL est protégée par un conducteur ohmique de 100 Ω */
        var UG = d.UG * s;
        if (dip === 'del') { I = solveI(function (i) { return d.U(i) + RP * i - UG; }, 0, d.Imax * 1.3); } else { I = solveI(function (i) { return d.U(i) - UG; }, 0, d.Imax * 1.3); }
        return { U: d.U(I), I: I, reg: fr(UG, 2) + ' V' };
      }
      var Rh = d.Rh[0] > 0 ? d.Rh[0] * Math.pow(d.Rh[1] / d.Rh[0], 1 - s) : d.Rh[1] * (1 - s) * (1 - s);   /* plage adaptée au dipôle */
      I = solveI(function (i) { return d.U(i) + Rh * i - E; }, 0, d.Imax * 1.3);
      return { U: d.U(I), I: I, reg: (Rh >= 1000 ? fr(Rh / 1000, 2) + ' k\u03a9' : Math.round(Rh) + ' \u03a9') };
    }
    function schema(st) {
      var b = CI.wire([[50, 60], [250, 60], [250, 190], [50, 190], [50, 60]]) + CI.wire([[250, 85], [310, 85], [310, 165], [250, 165]]);
      b += CI.gen(50, 125, 'v', 't', 'G') + CI.meter(150, 60, 'A', 'l');
      b += dip === 'ohm' ? CI.res(250, 125, 'v') : (dip === 'lampe' ? CI.lamp(250, 125, Math.min(1, st.I / 0.3)) : (dip === 'del' ? CI.led(250, 125, 'v', 'd') : CI.therm(250, 125, 'v')));
      b += CI.meter(310, 125, 'V', 't') + CI.node(250, 85) + CI.node(250, 165);
      if (mode === 'rheo') { b += CI.rheo(150, 190, 'h'); }
      else if (dip === 'del') { b += CI.res(150, 190, 'h') + CI.text(150, 215, 'protection 100 \u03a9', '#64748B', 10.5); }
      b += CI.text(24, 129, mode === 'gen' ? 'réglable' : '6,0 V', '#64748B', 10, 'end');
      /* écrans des appareils */
      b += "<rect x='110' y='4' width='80' height='26' rx='5' fill='#0F172A'/><text x='150' y='22' font-size='13' text-anchor='middle' fill='#4ADE80' font-family='ui-monospace, Menlo, monospace'>" + fr(st.I * 1000, st.I < 0.01 ? 2 : 1) + " mA</text>";
      b += "<rect x='330' y='112' width='74' height='26' rx='5' fill='#0F172A'/><text x='367' y='130' font-size='13' text-anchor='middle' fill='#4ADE80' font-family='ui-monospace, Menlo, monospace'>" + fr(st.U, 2) + " V</text>";
      return CI.svg(410, 230, b, 'Montage de tracé de la caractéristique, avec les valeurs lues sur l\u2019ampèremètre et le voltmètre', 'nt-svg');
    }
    function graphe(st) {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, d = DIP[dip], L = 48, R = w - 14, T = 14, B = h - 34;
      var imax = d.Imax, umax = d.Umax;
      function X(i) { return L + i / imax * (R - L); }
      function Y(u) { return B - u / umax * (B - T); }
      c.clearRect(0, 0, w, h);
      c.strokeStyle = '#E2E8F0'; c.lineWidth = 1;
      var imA = imax * 1000, p10 = Math.pow(10, Math.floor(Math.log10(imA / 5))), si = [1, 2, 5, 10].map(function (m) { return m * p10; }).filter(function (v) { return imA / v <= 7; })[0], su = umax > 3 ? 1 : 0.5;   /* graduations « rondes » */
      for (var k = 0; k * si <= imA + 1e-9; k++) { var xi = X(k * si / 1000); c.beginPath(); c.moveTo(xi, T); c.lineTo(xi, B); c.stroke(); txt(c, fr(k * si, si < 1 ? 1 : 0), xi, B + 15, '#475569', '11px system-ui, sans-serif'); }
      for (var u = 0; u <= umax + 1e-9; u += su) { c.beginPath(); c.moveTo(L, Y(u)); c.lineTo(R, Y(u)); c.stroke(); txt(c, fr(u, su < 1 ? 1 : 0), L - 6, Y(u) + 4, '#475569', '11px system-ui, sans-serif', 'right'); }
      c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
      txt(c, 'I (mA) \u2192', R - 30, B + 28, '#475569', '11px system-ui, sans-serif');
      c.save(); c.translate(14, (T + B) / 2); c.rotate(-Math.PI / 2); txt(c, 'U (V) \u2192', 0, 0, '#475569', '11px system-ui, sans-serif'); c.restore();
      if (modele) {
        c.strokeStyle = 'rgba(37,99,235,.55)'; c.lineWidth = 2; c.setLineDash([5, 4]); c.beginPath();
        for (var j = 0; j <= 200; j++) { var ii = imax * j / 200, uu = d.U(ii); if (uu > umax * 1.02) { break; } if (j === 0) { c.moveTo(X(ii), Y(uu)); } else { c.lineTo(X(ii), Y(uu)); } }
        c.stroke(); c.setLineDash([]);
        if (dip === 'therm') {   /* droite de la loi d'Ohm (R = 1 500 Ω), pour voir où le modèle cesse d'être valable */
          c.strokeStyle = 'rgba(225,29,72,.6)'; c.lineWidth = 1.5; c.beginPath(); c.moveTo(X(0), Y(0)); c.lineTo(X(Math.min(imax, umax / 1500)), Y(Math.min(imax, umax / 1500) * 1500)); c.stroke();
          txt(c, 'loi d\u2019Ohm (1 500 \u03a9)', X(0.0033), Y(5.6), '#E11D48', '600 11px system-ui, sans-serif');
        }
      }
      pts.forEach(function (p) { c.fillStyle = '#E11D48'; c.beginPath(); c.arc(X(p[0]), Y(p[1]), 4, 0, 2 * Math.PI); c.fill(); });
      c.strokeStyle = '#E11D48'; c.lineWidth = 1.5; c.beginPath(); c.arc(X(st.I), Y(st.U), 7, 0, 2 * Math.PI); c.stroke();
    }
    function maj() {
      var st = etat();
      oS.textContent = st.reg; oU.textContent = fr(st.U, 2) + ' V'; oI.textContent = fr(st.I * 1000, st.I < 0.01 ? 2 : 1) + ' mA';
      oR.textContent = st.I > 1e-6 ? Math.round(st.U / st.I) + ' \u03a9' : '\u2014';
      box.innerHTML = schema(st); graphe(st);
      $(root, '.out-slabel').textContent = mode === 'gen' ? 'Tension réglée sur le générateur' : 'Résistance du rhéostat';
    }
    rS.addEventListener('input', maj);
    $(root, '[data-act="pt"]').addEventListener('click', function () { var st = etat(); pts.push([st.I, st.U]); msg.textContent = pts.length + ' point' + (pts.length > 1 ? 's' : '') + ' relevé' + (pts.length > 1 ? 's' : '') + '. Modifiez le réglage et relevez d\u2019autres points.'; maj(); });
    $(root, '[data-act="clear"]').addEventListener('click', function () { pts = []; modele = false; msg.textContent = ''; maj(); });
    $(root, '[data-act="model"]').addEventListener('click', function () {
      modele = !modele;
      msg.innerHTML = !modele ? '' : ({ ohm: 'Une droite qui passe par l\u2019origine&nbsp;: U et I sont proportionnelles. C\u2019est la <b>loi d\u2019Ohm</b>, U = R × I, avec R = 220&nbsp;\u03a9 (le coefficient directeur).',
        lampe: 'Une courbe qui n\u2019est pas une droite&nbsp;: la résistance U/I de la lampe augmente quand elle chauffe. Ce n\u2019est pas un conducteur ohmique.',
        del: 'La DEL ne laisse passer presque aucun courant en dessous d\u2019environ 1,8&nbsp;V (sa tension de seuil), puis l\u2019intensité augmente brusquement.',
        therm: 'Pour de faibles intensités, les points sont alignés avec l\u2019origine&nbsp;: la thermistance suit la loi d\u2019Ohm (R ≈ 1&nbsp;500&nbsp;\u03a9 à 25&nbsp;°C). Au-delà de 2&nbsp;mA environ, elle chauffe, sa résistance diminue, et la courbe s\u2019écarte de la droite&nbsp;: la loi d\u2019Ohm n\u2019est valable que dans une <b>zone de travail</b> limitée.' })[dip];
      maj();
    });
    $$(root, 'input[name="cdip"]').forEach(function (r) { r.addEventListener('change', function () { dip = r.value; pts = []; modele = false; msg.textContent = ''; maj(); }); });
    $$(root, 'input[name="cmode"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; pts = []; msg.textContent = mode === 'gen' ? 'Générateur réglable&nbsp;: on règle directement la tension.' : 'Générateur fixe (6,0 V) et rhéostat&nbsp;: en faisant varier la résistance du rhéostat, on fait varier l\u2019intensité dans le circuit.'; maj(); }); });
    function setup() { S = canvasCtx(cv); maj(); }
    setup(); onResize(setup);
  })();
  /* ================= Le point de fonctionnement : une lampe sur un générateur idéal ================= */
  (function () {
    var root = document.getElementById('lab-ptf');
    if (!root) { return; }
    var cv = $(root, 'canvas'), box = $(root, '.nt-ptf-svg'), rE = $(root, '[data-p="E"]'), oE = $(root, '.out-E'), oP = $(root, '.out-pt'), S;
    function circuit(Eg, I0, U0) {
      var b = CI.wire([[80, 30], [260, 30], [260, 130], [80, 130], [80, 30]]) + CI.gen(80, 80, 'v', 't') + CI.lamp(260, 80, Math.min(1, I0 / 0.3));
      b += CI.uarr(44, 112, 44, 48, '', '', '#E11D48') + CI.qty(36, 86, 'U', 'G', '#E11D48', 'end') + CI.text(44, 150, fr(Eg, 1) + ' V', '#E11D48', 11.5, 'middle', 700);
      b += CI.uarr(294, 112, 294, 48, '', '', '#2563EB') + CI.qty(302, 86, 'U', 'L', '#2563EB', 'start');
      b += CI.iarr(170, 30, 'r', 'I', '', '#B45309', 0, -10);
      return CI.svg(360, 160, b, 'Une lampe branchée directement sur un générateur de tension idéal', 'nt-svg nt-svg-s');
    }
    function draw() {
      var Eg = +rE.value, lamp = DIP.lampe, c = S.ctx, w = S.w, h = S.h, L = 48, R = w - 16, T = 14, B = h - 34, imax = 0.4, umax = 10;
      oE.textContent = fr(Eg, 1) + ' V';
      function X(i) { return L + i / imax * (R - L); }
      function Y(u) { return B - u / umax * (B - T); }
      c.clearRect(0, 0, w, h);
      c.strokeStyle = '#E2E8F0'; c.lineWidth = 1;
      for (var k = 0; k <= 8; k++) { var xi = X(k * 0.05); c.beginPath(); c.moveTo(xi, T); c.lineTo(xi, B); c.stroke(); if (k % 2 === 0) { txt(c, fr(k * 0.05, 1), xi, B + 15, '#475569', '11px system-ui, sans-serif'); } }
      for (var u = 0; u <= umax; u += 2) { c.beginPath(); c.moveTo(L, Y(u)); c.lineTo(R, Y(u)); c.stroke(); txt(c, String(u), L - 6, Y(u) + 4, '#475569', '11px system-ui, sans-serif', 'right'); }
      c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
      txt(c, 'I (A) \u2192', R - 26, B + 28, '#475569', '11px system-ui, sans-serif');
      c.save(); c.translate(14, (T + B) / 2); c.rotate(-Math.PI / 2); txt(c, 'U (V) \u2192', 0, 0, '#475569', '11px system-ui, sans-serif'); c.restore();
      /* générateur idéal : sa tension ne dépend pas de l'intensité (droite horizontale) */
      c.strokeStyle = '#E11D48'; c.lineWidth = 2.4; c.beginPath(); c.moveTo(X(0), Y(Eg)); c.lineTo(X(imax), Y(Eg)); c.stroke();
      txt(c, 'générateur idéal', X(0.02), Y(Eg) - 8, '#E11D48', '600 11.5px system-ui, sans-serif', 'left');
      c.strokeStyle = '#2563EB'; c.lineWidth = 2.4; c.beginPath();
      for (var j = 0; j <= 200; j++) { var ii = imax * j / 200, uu = lamp.U(ii); if (uu > umax) { break; } if (j === 0) { c.moveTo(X(ii), Y(uu)); } else { c.lineTo(X(ii), Y(uu)); } }
      c.stroke(); txt(c, 'lampe', X(0.345), Y(lamp.U(0.345)) + 4, '#2563EB', '600 11.5px system-ui, sans-serif', 'left');
      var I0 = solveI(function (i) { return lamp.U(i) - Eg; }, 0, imax), U0 = Eg;
      c.strokeStyle = 'rgba(30,41,59,.5)'; c.setLineDash([4, 4]); c.lineWidth = 1.2; c.beginPath(); c.moveTo(X(I0), Y(U0)); c.lineTo(X(I0), B); c.stroke(); c.setLineDash([]);
      c.fillStyle = '#F59E0B'; c.beginPath(); c.arc(X(I0), Y(U0), 7, 0, 2 * Math.PI); c.fill(); c.strokeStyle = '#fff'; c.lineWidth = 2; c.stroke();
      txt(c, 'point de fonctionnement', X(I0) + (X(I0) > (L + R) / 2 ? -10 : 10), Y(U0) + 20, '#B45309', '700 11.5px system-ui, sans-serif', X(I0) > (L + R) / 2 ? 'right' : 'left');
      oP.innerHTML = 'I = ' + fr(I0, 3) + '&nbsp;A &nbsp;; U = ' + fr(U0, 2) + '&nbsp;V';
      box.innerHTML = circuit(Eg, I0, U0);
    }
    rE.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* graphe commun : courbe d'étalonnage R = f(θ), avec points relevés, courbe (à la demande) et construction éventuelle */
  function axes(c, L, R, T, B, xs, ys, xl, yl) {
    c.strokeStyle = '#E2E8F0'; c.lineWidth = 1;
    xs.forEach(function (v) { c.beginPath(); c.moveTo(v[0], T); c.lineTo(v[0], B); c.stroke(); txt(c, v[1], v[0], B + 15, '#475569', '11px system-ui, sans-serif'); });
    ys.forEach(function (v) { c.beginPath(); c.moveTo(L, v[0]); c.lineTo(R, v[0]); c.stroke(); txt(c, v[1], L - 6, v[0] + 4, '#475569', '11px system-ui, sans-serif', 'right'); });
    c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
    txt(c, xl, R - 30, B + 28, '#475569', '11px system-ui, sans-serif');
    c.save(); c.translate(L - 40, (T + B) / 2); c.rotate(-Math.PI / 2); txt(c, yl, 0, 0, '#475569', '11px system-ui, sans-serif'); c.restore();
  }
  function grapheEtal(S, pts, cons, courbe) {
    var c = S.ctx, w = S.w, h = S.h, L = 56, R = w - 14, T = 14, B = h - 34, tmax = 85, rmax = 4500;
    function X(t) { return L + t / tmax * (R - L); }
    function Y(r) { return B - r / rmax * (B - T); }
    c.clearRect(0, 0, w, h);
    var xs = [], ys = [];
    for (var t = 0; t <= 80; t += 10) { xs.push([X(t), String(t)]); }
    for (var r = 0; r <= 4000; r += 1000) { ys.push([Y(r), r.toLocaleString('fr-FR')]); }
    axes(c, L, R, T, B, xs, ys, '\u03b8 (°C) \u2192', 'R (\u03a9) \u2192');
    if (courbe) {
      c.strokeStyle = 'rgba(5,150,105,.75)'; c.lineWidth = 2.2; c.beginPath();
      for (var k = 0; k <= 160; k++) { var tt = 2 + 80 * k / 160; if (k === 0) { c.moveTo(X(tt), Y(Rtherm(tt))); } else { c.lineTo(X(tt), Y(Rtherm(tt))); } }
      c.stroke();
    }
    (pts || []).forEach(function (p) { c.fillStyle = '#059669'; c.beginPath(); c.arc(X(p[0]), Y(p[1]), 4.5, 0, 2 * Math.PI); c.fill(); c.strokeStyle = '#fff'; c.lineWidth = 1.5; c.stroke(); });
    if (cons) {
      c.strokeStyle = '#E11D48'; c.lineWidth = 1.6; c.setLineDash([5, 4]);
      c.beginPath(); c.moveTo(L, Y(cons[1])); c.lineTo(X(cons[0]), Y(cons[1])); c.lineTo(X(cons[0]), B); c.stroke(); c.setLineDash([]);
      c.fillStyle = '#E11D48'; c.beginPath(); c.arc(X(cons[0]), Y(cons[1]), 5, 0, 2 * Math.PI); c.fill();
      txt(c, Math.round(cons[1]).toLocaleString('fr-FR') + ' \u03a9', L + 6, Y(cons[1]) - 7, '#E11D48', '700 11.5px system-ui, sans-serif', 'left');
      txt(c, '\u03b8 \u2248 ' + Math.round(cons[0]) + ' °C', X(cons[0]) + 6, B - 8, '#E11D48', '700 11.5px system-ui, sans-serif', 'left');
    }
  }
  function rrp(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
  /* ================= L'étalonnage de la thermistance ================= */
  (function () {
    var root = document.getElementById('lab-etal');
    if (!root) { return; }
    var cvS = $(root, 'canvas.scene'), cvG = $(root, 'canvas.graph'), bH = $(root, '[data-act="heat"]'), bC = $(root, '[data-act="curve"]'), msg = $(root, '.nt-msg'), S, SG;
    var theta = 5, on = false, pts = [], last = null, courbe = false, tclock = 0;
    function scene() {
      var c = S.ctx, w = S.w, h = S.h, bw = Math.min(160, w * 0.3), W = 74 + 26 + bw + 64 + 108, x0 = Math.max(4, (w - W) / 2);   /* composition centrée */
      var bl = x0 + 100, br = bl + bw, bt = 46, bb = h - 50, om = br + 64;
      c.clearRect(0, 0, w, h);
      /* plaque chauffante */
      rrp(c, bl - 22, bb + 4, bw + 44, 22, 5); c.fillStyle = '#E2E8F0'; c.fill(); c.strokeStyle = '#94A3B8'; c.lineWidth = 1; c.stroke();
      c.fillStyle = on ? '#EF4444' : '#94A3B8'; rrp(c, bl - 8, bb, bw + 16, 5, 2); c.fill();
      if (on) { var gl = c.createRadialGradient((bl + br) / 2, bb, 2, (bl + br) / 2, bb, bw * 0.6); gl.addColorStop(0, 'rgba(249,115,22,.35)'); gl.addColorStop(1, 'rgba(249,115,22,0)'); c.fillStyle = gl; c.fillRect(bl - 20, bb - 30, bw + 40, 40); }
      c.fillStyle = on ? '#F97316' : '#CBD5E1'; c.beginPath(); c.arc(br + 12, bb + 15, 4, 0, 2 * Math.PI); c.fill();
      txt(c, on ? 'plaque chauffante allumée' : 'plaque chauffante éteinte', (bl + br) / 2, h - 8, on ? '#C2410C' : '#64748B', '600 11px system-ui, sans-serif');
      /* eau */
      var wt = bt + 34, wg = c.createLinearGradient(0, wt, 0, bb); wg.addColorStop(0, 'rgba(147,197,253,.55)'); wg.addColorStop(1, 'rgba(59,130,246,.45)');
      c.fillStyle = wg; c.fillRect(bl + 2, wt, bw - 4, bb - wt - 1);
      c.strokeStyle = 'rgba(255,255,255,.8)'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(bl + 2, wt); c.lineTo(br - 2, wt); c.stroke();
      if (theta < 9) { c.fillStyle = 'rgba(255,255,255,.88)'; c.strokeStyle = 'rgba(148,163,184,.8)'; [[0.12, -2], [0.38, 3], [0.55, -1]].forEach(function (g) { rrp(c, bl + g[0] * bw, wt + g[1], 16, 12, 3); c.fill(); c.stroke(); }); }
      if (on && theta > 45) {   /* bulles, puis vapeur */
        c.fillStyle = 'rgba(255,255,255,.75)';
        for (var k = 0; k < 7; k++) { var yy = bb - 8 - ((tclock * 40 + k * 31) % (bb - wt - 14)); c.beginPath(); c.arc(bl + 14 + k * (bw - 28) / 6, yy, 2 + (k % 3), 0, 2 * Math.PI); c.fill(); }
        if (theta > 65) { c.strokeStyle = 'rgba(148,163,184,.55)'; c.lineWidth = 2; for (var v = 0; v < 3; v++) { var vx = bl + bw * (0.3 + 0.2 * v); c.beginPath(); c.moveTo(vx, wt - 8); c.bezierCurveTo(vx - 8, wt - 18, vx + 8, wt - 26, vx, wt - 36 - 4 * Math.sin(tclock * 2 + v)); c.stroke(); } }
      }
      /* bécher en verre */
      var gg = c.createLinearGradient(bl, 0, br, 0); gg.addColorStop(0, 'rgba(203,213,225,.45)'); gg.addColorStop(0.5, 'rgba(255,255,255,.15)'); gg.addColorStop(1, 'rgba(203,213,225,.45)');
      c.fillStyle = gg; c.fillRect(bl, bt, bw, bb - bt);
      c.strokeStyle = '#64748B'; c.lineWidth = 1.6; c.lineJoin = 'round'; c.beginPath(); c.moveTo(bl - 7, bt - 5); c.quadraticCurveTo(bl - 1, bt - 2, bl, bt + 7); c.lineTo(bl, bb - 4); c.quadraticCurveTo(bl, bb, bl + 4, bb); c.lineTo(br - 4, bb); c.quadraticCurveTo(br, bb, br, bb - 4); c.lineTo(br, bt); c.stroke();
      /* thermomètre : afficheur à gauche, sonde dans l'eau */
      var px = bl + bw * 0.24;
      c.strokeStyle = '#334155'; c.lineWidth = 2; c.beginPath(); c.moveTo(x0 + 74, 26); c.bezierCurveTo(x0 + 92, 26, px, 6, px, 22); c.stroke();
      c.strokeStyle = '#94A3B8'; c.lineWidth = 4; c.lineCap = 'round'; c.beginPath(); c.moveTo(px, 22); c.lineTo(px, bb - 24); c.stroke();
      rrp(c, x0, 12, 74, 30, 6); c.fillStyle = '#0F172A'; c.fill();
      c.fillStyle = '#4ADE80'; c.font = '14px ui-monospace, Menlo, monospace'; c.textAlign = 'center'; c.fillText(fr(theta, 1) + ' °C', x0 + 37, 32);
      txt(c, 'thermomètre', x0 + 37, 58, '#475569', '600 10.5px system-ui, sans-serif');
      /* thermistance : perle dans l'eau, deux fils qui rejoignent l'ohmmètre sans se croiser */
      var tx = bl + bw * 0.66, ty = bb - 30, x1 = tx - 4, x2 = tx + 4, tA = om + 32, tB = om + 76;
      c.lineWidth = 1.8; c.lineCap = 'round';
      c.strokeStyle = '#DC2626'; c.beginPath(); c.moveTo(x1, ty); c.lineTo(x1, bt - 8); c.bezierCurveTo(x1, 2, tB, 2, tB, 30); c.stroke();
      c.strokeStyle = '#1E293B'; c.beginPath(); c.moveTo(x2, ty); c.lineTo(x2, bt - 8); c.bezierCurveTo(x2, 16, tA, 16, tA, 30); c.stroke();
      c.fillStyle = '#1E293B'; c.beginPath(); c.ellipse(tx, ty + 3, 8, 6, 0, 0, 2 * Math.PI); c.fill();
      txt(c, 'thermistance', tx + 12, ty + 18, '#1E293B', '600 10.5px system-ui, sans-serif', 'left');
      /* ohmmètre */
      rrp(c, om, 32, 108, 132, 14); c.fillStyle = '#F59E0B'; c.fill(); c.strokeStyle = '#B45309'; c.lineWidth = 1.3; c.stroke();
      rrp(c, om + 7, 39, 94, 118, 9); c.fillStyle = '#334155'; c.fill();
      rrp(c, om + 14, 48, 80, 32, 5); c.fillStyle = '#D9F99D'; c.fill();
      c.fillStyle = '#1A2E05'; c.font = '15px ui-monospace, Menlo, monospace'; c.textAlign = 'right'; c.fillText(Math.round(Rtherm(theta)).toLocaleString('fr-FR') + ' \u03a9', om + 90, 70);
      c.fillStyle = '#1E293B'; c.beginPath(); c.arc(om + 54, 112, 17, 0, 2 * Math.PI); c.fill(); c.strokeStyle = '#FCD34D'; c.lineWidth = 3; c.beginPath(); c.moveTo(om + 54, 112); c.lineTo(om + 54 + 14, 112 + 6); c.stroke();
      [tA, tB].forEach(function (x, i) { c.fillStyle = i ? '#DC2626' : '#0F172A'; c.beginPath(); c.arc(x, 30, 5, 0, 2 * Math.PI); c.fill(); });
      txt(c, 'ohmmètre', om + 54, 182, '#475569', '600 10.5px system-ui, sans-serif');
    }
    function draw() { if (!S) { return; } scene(); grapheEtal(SG, pts, null, courbe); $(root, '.out-n').textContent = pts.length; }
    function loop(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; tclock += dt;
      if (on && theta < 80) { theta = Math.min(80, theta + dt * (RM ? 6 : 3)); if (theta >= 80) { on = false; bH.innerHTML = '<i class="fa-solid fa-fire"></i>&nbsp; Chauffer'; msg.textContent = 'L\u2019eau a atteint 80 °C : on arrête de chauffer.'; } }
      draw(); requestAnimationFrame(loop);
    }
    bH.addEventListener('click', function () { on = !on; bH.innerHTML = on ? '<i class="fa-solid fa-pause"></i>&nbsp; Arrêter de chauffer' : '<i class="fa-solid fa-fire"></i>&nbsp; Chauffer'; });
    $(root, '[data-act="pt"]').addEventListener('click', function () {
      pts.push([theta, Rtherm(theta)]);
      msg.innerHTML = 'Point relevé&nbsp;: \u03b8 = ' + fr(theta, 1) + '&nbsp;°C, R = ' + Math.round(Rtherm(theta)).toLocaleString('fr-FR') + '&nbsp;\u03a9. ' + (pts.length < 6 ? 'Relevez des points régulièrement pendant que l\u2019eau chauffe.' : 'Vous avez assez de points pour tracer la courbe d\u2019étalonnage.');
      draw();
    });
    bC.addEventListener('click', function () {
      courbe = !courbe;
      bC.innerHTML = courbe ? '<i class="fa-solid fa-eye-slash"></i>&nbsp; Masquer la courbe' : '<i class="fa-solid fa-chart-line"></i>&nbsp; Afficher la courbe';
      if (courbe) { msg.innerHTML = 'La <b>courbe d\u2019étalonnage</b>&nbsp;: la résistance de la thermistance diminue quand la température augmente (thermistance CTN), et ce n\u2019est pas une droite.'; }
      draw();
    });
    $(root, '[data-act="reset"]').addEventListener('click', function () { theta = 5; on = false; pts = []; courbe = false; bC.innerHTML = '<i class="fa-solid fa-chart-line"></i>&nbsp; Afficher la courbe'; bH.innerHTML = '<i class="fa-solid fa-fire"></i>&nbsp; Chauffer'; msg.textContent = 'Eau glacée à 5 °C. Allumez la plaque et relevez des points.'; draw(); });
    function setup() { S = canvasCtx(cvS); SG = canvasCtx(cvG); draw(); }
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Bilan : le montage du TP, de la tension mesurée à la température ================= */
  (function () {
    var root = document.getElementById('lab-bilan');
    if (!root) { return; }
    var box = $(root, '.nt-bilan-svg'), cvA = $(root, 'canvas.assoc'), cvE = $(root, 'canvas.etal'), steps = $(root, '.nt-bilan-steps'), bN = $(root, '[data-act="next"]'), SA, SE;
    var UG = 10.0, R0 = 1500, RP = 1000, theta, etape = 0, NE = 6;
    function Iass(U) { return U <= 0 ? 0 : solveI(function (i) { return DIP.del.U(i) + RP * i - U; }, 0, 0.1); }   /* DEL + R_P soumis à la tension U */
    function valeurs() {
      var RT = Rtherm(theta);
      var Up = (function () { var lo = 0, hi = UG; for (var k = 0; k < 70; k++) { var m = (lo + hi) / 2; if (m + RT * (m / R0 + Iass(m)) > UG) { hi = m; } else { lo = m; } } return (lo + hi) / 2; })();
      var UR0 = Math.round(Up * 100) / 100, URT = Math.round((UG - UR0) * 100) / 100, I1 = UR0 / R0, I2 = Math.round(Iass(UR0) * 1e5) / 1e5, IG = I1 + I2, RTc = URT / IG;
      var th = solveI(function (t) { return -Rtherm(t) + RTc; }, -20, 120);
      return { UR0: UR0, URT: URT, I1: I1, I2: I2, IG: IG, RT: RTc, th: th };
    }
    function schema(v) {
      var on = function (k) { return etape >= k; }, col = function (k, c) { return on(k) ? c : '#94A3B8'; };
      var F = "font-family='system-ui, sans-serif'", G = "font-family='Georgia, serif'";
      var b = "<defs><linearGradient id='gEau' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#DBEAFE'/><stop offset='1' stop-color='#93C5FD'/></linearGradient></defs>";
      /* bain d'eau autour de la thermistance ; légende à droite du fil */
      b += "<rect x='298' y='50' width='170' height='100' rx='14' fill='url(#gEau)' fill-opacity='.75' stroke='#60A5FA' stroke-width='1.2'/>";
      b += "<path d='M306,64 q8,-5 16,0 t16,0 t16,0 t16,0 t16,0 t16,0 t16,0 t16,0 t16,0' fill='none' stroke='#fff' stroke-width='1.4' stroke-opacity='.9'/>";
      b += "<text x='428' y='100' font-size='11.5' text-anchor='middle' fill='#1E3A8A' " + F + " font-weight='700'>eau</text><text x='428' y='117' font-size='11.5' text-anchor='middle' fill='#1E3A8A' " + F + " font-weight='700'>\u03b8 = ?</text>";
      /* afficheur : cadre vert resserré autour de la DEL et de R_P */
      b += "<rect x='494' y='206' width='52' height='112' rx='10' fill='rgba(187,247,208,.55)' stroke='#4ADE80' stroke-dasharray='5 4'/>";
      /* fils */
      b += CI.wire([[120, 40], [370, 40], [370, 170]]) + CI.wire([[260, 170], [520, 170]]) + CI.wire([[260, 170], [260, 330], [520, 330], [520, 170]]) + CI.wire([[370, 330], [370, 350], [120, 350], [120, 40]]);
      b += CI.wire([[260, 210], [350, 210], [350, 290], [260, 290]]);
      /* dipôles */
      b += CI.gen(120, 192, 'v', 't') + CI.therm(370, 100, 'v') + CI.res(260, 250, 'v') + CI.res(520, 288, 'v');
      var glow = Math.min(1, v.I2 / 0.006);
      if (glow > 0.02) { b += "<circle cx='520' cy='236' r='" + (12 + 15 * glow).toFixed(1) + "' fill='rgba(239,68,68," + (0.4 * glow).toFixed(2) + ")'/>"; }
      b += CI.led(520, 236, 'v', 'd');
      b += CI.node(370, 170) + CI.node(370, 330) + CI.node(260, 210) + CI.node(260, 290) + CI.meter(350, 250, 'V', 't');
      b += "<rect x='368' y='237' width='76' height='26' rx='6' fill='#0F172A'/><text x='406' y='255' font-size='13.5' text-anchor='middle' fill='#4ADE80' font-family='ui-monospace, Menlo, monospace'>" + fr(v.UR0, 2) + " V</text>";
      /* noms et valeurs */
      b += "<text x='348' y='96' font-size='13' text-anchor='end' fill='#1E293B' " + G + " font-weight='700'><tspan font-style='italic'>R</tspan><tspan font-size='9' dy='3'>T</tspan></text>";
      b += "<text x='246' y='246' font-size='13' text-anchor='end' fill='#1E293B' " + G + " font-weight='700'><tspan font-style='italic'>R</tspan><tspan font-size='9' dy='3'>0</tspan></text><text x='246' y='264' font-size='10.5' text-anchor='end' fill='#64748B' " + F + ">1 500 \u03a9</text>";
      b += "<text x='554' y='240' font-size='11' fill='#15803D' " + F + " font-weight='700'>DEL</text>";
      b += "<text x='554' y='286' font-size='13' fill='#1E293B' " + G + " font-weight='700'><tspan font-style='italic'>R</tspan><tspan font-size='9' dy='3'>P</tspan></text><text x='554' y='303' font-size='10.5' fill='#64748B' " + F + ">1 k\u03a9</text>";
      b += "<text x='554' y='262' font-size='10.5' fill='#16A34A' " + F + " font-style='italic'>afficheur</text>";
      /* tensions : chaque nom à côté de sa flèche */
      b += CI.uarr(80, 240, 80, 144, '', '', '#475569') + CI.qty(70, 196, 'U', 'G', '#475569', 'end') + CI.text(80, 262, '10,0 V', '#475569', 11.5, 'middle', 700);
      b += CI.uarr(486, 125, 486, 75, '', '', col(2, '#7C3AED')) + CI.qty(494, 104, 'U', 'RT', col(2, '#7C3AED'), 'start', 13);
      b += CI.uarr(280, 278, 280, 222, '', '', col(1, '#E11D48')) + CI.qty(287, 254, 'U', 'R0', col(1, '#E11D48'), 'start', 12.5);
      /* intensités */
      b += CI.iarr(240, 40, 'r', on(5) ? 'I' : '', 'G', '#2563EB', 0, -10) + CI.iarr(260, 190, 'd', on(3) ? 'I' : '', '1', '#D97706', -14, 4) + CI.iarr(520, 190, 'd', on(4) ? 'I' : '', '2', '#059669', 14, 4);
      return CI.svg(620, 368, b, 'Montage du TP : le générateur alimente la thermistance, plongée dans l\u2019eau, puis deux branches en dérivation : le conducteur ohmique R0, aux bornes duquel un voltmètre mesure la tension, et l\u2019afficheur formé de la DEL et de son conducteur ohmique de protection RP', 'nt-svg');
    }
    function grAssoc(v) {
      var c = SA.ctx, w = SA.w, h = SA.h, L = 56, R = w - 14, T = 14, B = h - 34, umax = 10, imax = 8;
      function X(u) { return L + u / umax * (R - L); }
      function Y(i) { return B - i / imax * (B - T); }
      c.clearRect(0, 0, w, h);
      var xs = [], ys = []; for (var u = 0; u <= 10; u += 2) { xs.push([X(u), String(u)]); } for (var i = 0; i <= 8; i += 2) { ys.push([Y(i), String(i)]); }
      axes(c, L, R, T, B, xs, ys, 'U (V) \u2192', 'I (mA) \u2192');
      c.strokeStyle = '#059669'; c.lineWidth = 2.2; c.beginPath();
      for (var k = 0; k <= 200; k++) { var uu = umax * k / 200, ii = Iass(uu) * 1000; if (k === 0) { c.moveTo(X(uu), Y(ii)); } else { c.lineTo(X(uu), Y(ii)); } }
      c.stroke(); txt(c, 'DEL + R\u209a', X(8.6), Y(Iass(8.6) * 1000) - 10, '#059669', '700 11.5px system-ui, sans-serif');
      if (etape >= 3) {
        var ui = v.UR0, ii2 = v.I2 * 1000;
        c.strokeStyle = '#E11D48'; c.lineWidth = 1.6; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(X(ui), B); c.lineTo(X(ui), Y(ii2)); c.lineTo(L, Y(ii2)); c.stroke(); c.setLineDash([]);
        c.fillStyle = '#E11D48'; c.beginPath(); c.arc(X(ui), Y(ii2), 5, 0, 2 * Math.PI); c.fill();
        txt(c, fr(ii2, 2) + ' mA', L + 6, Y(ii2) - 7, '#E11D48', '700 11.5px system-ui, sans-serif', 'left');
        txt(c, fr(ui, 2) + ' V', X(ui) + 6, B - 8, '#E11D48', '700 11.5px system-ui, sans-serif', 'left');
      }
    }
    var TXT = [
      function (v) { return '<b>Mesure</b>&nbsp;: le voltmètre indique la tension aux bornes du conducteur ohmique&nbsp;: <b>U<sub>R0</sub> = ' + fr(v.UR0, 2) + '&nbsp;V</b>.'; },
      function (v) { return '<b>Loi des mailles</b> (maille générateur, thermistance, R<sub>0</sub>)&nbsp;: U<sub>G</sub> = U<sub>RT</sub> + U<sub>R0</sub>, donc U<sub>RT</sub> = 10,0 \u2212 ' + fr(v.UR0, 2) + ' = <b>' + fr(v.URT, 2) + '&nbsp;V</b>.'; },
      function (v) { return '<b>Loi d\u2019Ohm</b> pour R<sub>0</sub>&nbsp;: I<sub>1</sub> = U<sub>R0</sub> / R<sub>0</sub> = ' + fr(v.UR0, 2) + ' / 1&nbsp;500 = <b>' + fr(v.I1 * 1000, 2) + '&nbsp;mA</b>.'; },
      function (v) { return '<b>Point de fonctionnement</b> de l\u2019ensemble DEL + R<sub>P</sub>&nbsp;: il est en dérivation avec R<sub>0</sub>, donc soumis à la même tension, ' + fr(v.UR0, 2) + '&nbsp;V. On lit sur sa caractéristique (graphique de gauche)&nbsp;: <b>I<sub>2</sub> = ' + fr(v.I2 * 1000, 2) + '&nbsp;mA</b>.'; },
      function (v) { return '<b>Loi des nœuds</b>&nbsp;: le courant qui traverse la thermistance se partage entre les deux branches&nbsp;: I<sub>G</sub> = I<sub>1</sub> + I<sub>2</sub> = ' + fr(v.I1 * 1000, 2) + ' + ' + fr(v.I2 * 1000, 2) + ' = <b>' + fr(v.IG * 1000, 2) + '&nbsp;mA</b>.'; },
      function (v) { return '<b>Loi d\u2019Ohm</b> pour la thermistance&nbsp;: R<sub>T</sub> = U<sub>RT</sub> / I<sub>G</sub> = ' + fr(v.URT, 2) + ' / ' + fr(v.IG, 5) + ' = <b>' + Math.round(v.RT).toLocaleString('fr-FR') + '&nbsp;\u03a9</b>.'; },
      function (v) { return '<b>Courbe d\u2019étalonnage</b> (graphique de droite)&nbsp;: R<sub>T</sub> = ' + Math.round(v.RT).toLocaleString('fr-FR') + '&nbsp;\u03a9 correspond à <b>\u03b8 \u2248 ' + Math.round(v.th) + '&nbsp;°C</b>. Un thermomètre plongé dans l\u2019eau indique ' + fr(theta, 1) + '&nbsp;°C&nbsp;: la mesure est réussie&nbsp;!'; }
    ];
    function maj() {
      var v = valeurs();
      box.innerHTML = schema(v);
      steps.innerHTML = TXT.slice(0, etape + 1).map(function (f) { return '<li><p>' + f(v) + '</p></li>'; }).join('');
      if (SA) { grAssoc(v); grapheEtal(SE, null, etape >= 6 ? [v.th, v.RT] : null, true); }
      bN.innerHTML = etape < NE ? '<i class="fa-solid fa-forward-step"></i>&nbsp; Étape suivante' : '<i class="fa-solid fa-rotate"></i>&nbsp; Une autre eau';
    }
    bN.addEventListener('click', function () { if (etape < NE) { etape++; } else { etape = 0; theta = 8 + Math.round(Math.random() * 650) / 10; } maj(); });
    theta = 8 + Math.round(Math.random() * 650) / 10;
    function setup() { SA = canvasCtx(cvA); SE = canvasCtx(cvE); maj(); }
    setup(); onResize(setup);
  })();
})();
</script>
