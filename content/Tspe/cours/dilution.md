+++
title = "Dilution"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-verres { display: grid; grid-template-columns: repeat(auto-fit, minmax(96px, 1fr)); gap: 10px; margin: 0.8em 0; }
.nt-verre { display: flex; flex-direction: column; align-items: center; gap: 0.3em; padding: 0.5em 0.3em; border-radius: 12px; border: 2px solid var(--line); background: #fff; cursor: pointer; font: inherit; font-size: 0.85em; color: var(--ink); transition: transform 0.15s, box-shadow 0.15s, border-color 0.15s; }
.nt-verre:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(15, 23, 42, 0.1); border-color: #94A3B8; }
.nt-verre:focus-visible { outline: 3px solid var(--blue-lt); outline-offset: 2px; }
.nt-verre.nt-ok { border-color: #16A34A; background: #F0FDF4; }
.nt-verre.nt-ko { border-color: #E11D48; background: #FFF1F2; }
.nt-verre-svg { width: 62px; height: 150px; }
.nt-verre-q { font-size: 1.05em; text-align: center; margin: 0.4em 0 !important; }
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
.nt-lab.nt-fini .nt-verres { display: none; }
.nt-dil-enonce { min-height: 4.5em; padding: 0.6em 1em; border-radius: 10px; background: var(--slate-bg); border: 1px solid var(--line); }
.nt-dil-zone p { margin: 0.5em 0 0.2em !important; font-size: 0.9em; color: var(--slate); }
.nt-dil-zone .nt-btns { justify-content: flex-start; margin-top: 0.2em; }
.nt-dil-inline { display: flex !important; align-items: center; gap: 0.5em; flex-wrap: nowrap; }
.nt-dil-num input { font: inherit; width: 7em; padding: 0.3em 0.6em; border: 1.5px solid var(--line); border-radius: 8px; display: inline-block; margin: 0; }
#lab-dilution .nt-msg { margin-top: 1.1em !important; padding-top: 0.2em; }
#lab-dilution .nt-read { margin-top: 0.8em; }
.nt-dil-num input:focus { outline: 3px solid var(--blue-lt); outline-offset: 1px; }
.nt-fig-prot { display: block; width: 100%; max-width: 760px; margin: 1em auto 0.4em; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Diluer une solution {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp">dilution</span> a pour but de <span class="imp nt-hole">réduire la concentration</span> d'une solution, appelée <b>solution mère</b>, pour obtenir une <b>solution fille</b>.</p>
<p>Principe&nbsp;: on <span class="imp nt-hole">augmente la quantité de solvant</span>, sans changer la quantité de soluté.</p>
</div>

## Le matériel {.nt-h2}

<p class="nt-lead">Une dilution se fait avec deux pièces de verrerie bien choisies. Lesquelles&nbsp;?</p>

<div class="nt-lab" id="lab-verrerie">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Quelle est la verrerie la plus précise&nbsp;?</p>
<p class="nt-verre-q"></p>
<div class="nt-verres">
<button type="button" class="nt-verre" data-v="becher"><svg class='nt-verre-svg' viewBox='0 0 90 220' role='img' aria-label="Un bécher"><defs><linearGradient id='gVb' x1='0' x2='1'><stop offset='0' stop-color='#DCE7F2'/><stop offset='.45' stop-color='#FFFFFF'/><stop offset='1' stop-color='#DCE7F2'/></linearGradient></defs><path d='M6,112 L12,118 L12,196 Q12,204 20,204 L70,204 Q78,204 78,196 L78,116' fill='url(#gVb)' stroke='#475569' stroke-width='1.3' stroke-linejoin='round'/><path d='M13,160 L77,160 L77,196 Q77,203 70,203 L20,203 Q13,203 13,196 Z' fill='#F9A8D4' fill-opacity='.55'/><line x1='70' y1='132.0' x2='64' y2='132.0' stroke='#475569' stroke-width='.7'/><line x1='70' y1='146.0' x2='64' y2='146.0' stroke='#475569' stroke-width='.7'/><line x1='70' y1='160.0' x2='64' y2='160.0' stroke='#475569' stroke-width='.7'/><line x1='70' y1='174.0' x2='64' y2='174.0' stroke='#475569' stroke-width='.7'/><line x1='70' y1='188.0' x2='64' y2='188.0' stroke='#475569' stroke-width='.7'/></svg><span>bécher</span></button>
<button type="button" class="nt-verre" data-v="erlen"><svg class='nt-verre-svg' viewBox='0 0 90 220' role='img' aria-label="Un erlenmeyer"><defs><linearGradient id="linearGradient1" x1="4.666667" y1="84" x2="85.333333" y2="84" gradientUnits="userSpaceOnUse"><stop offset="1e-05" stop-color="#dce7f2" stop-opacity="1"/><stop offset="0.45" stop-color="#ffffff" stop-opacity="1"/><stop offset="1" stop-color="#dce7f2" stop-opacity="1"/></linearGradient></defs><path id="Path" fill="url(#linearGradient1)" stroke="#475569" stroke-width="1.3" stroke-linejoin="round" d="M 37 84 L 37 104 L 5 194 C 3.666667 200.666667 6.333333 204 13 204 L 77 204 C 83.666667 204 86.333333 200.666667 85 194 L 53 104 L 53 84"/><path id="path1" fill="#f9a8d4" fill-opacity="0.55" stroke="none" d="M 21 152 L 70 152 L 84.999992 196 C 85.666659 200.666667 83.333326 203 77.999992 203 L 13 203 C 7.666667 203 5.333333 200.666667 6 196 Z"/></svg><span>erlenmeyer</span></button>
<button type="button" class="nt-verre" data-v="eprouvette"><svg class='nt-verre-svg' viewBox='0 0 90 220' role='img' aria-label="Une éprouvette graduée"><defs><linearGradient id='gVp' x1='0' x2='1'><stop offset='0' stop-color='#DCE7F2'/><stop offset='.45' stop-color='#FFFFFF'/><stop offset='1' stop-color='#DCE7F2'/></linearGradient></defs><path d='M30,16 L33,20 L33,194 L57,194 L57,16' fill='url(#gVp)' stroke='#475569' stroke-width='1.3' stroke-linejoin='round'/><rect x='17' y='194' width='56' height='4' rx='1.5' fill='#E2E8F0' stroke='#475569' stroke-width='1.1'/><rect x='34' y='112' width='22' height='81.5' fill='#F9A8D4' fill-opacity='.55'/><line x1='33' y1='30.0' x2='41' y2='30.0' stroke='#475569' stroke-width='.7'/><line x1='33' y1='35.2' x2='37' y2='35.2' stroke='#475569' stroke-width='.7'/><line x1='33' y1='40.4' x2='37' y2='40.4' stroke='#475569' stroke-width='.7'/><line x1='33' y1='45.6' x2='37' y2='45.6' stroke='#475569' stroke-width='.7'/><line x1='33' y1='50.8' x2='37' y2='50.8' stroke='#475569' stroke-width='.7'/><line x1='33' y1='56.0' x2='41' y2='56.0' stroke='#475569' stroke-width='.7'/><line x1='33' y1='61.2' x2='37' y2='61.2' stroke='#475569' stroke-width='.7'/><line x1='33' y1='66.4' x2='37' y2='66.4' stroke='#475569' stroke-width='.7'/><line x1='33' y1='71.6' x2='37' y2='71.6' stroke='#475569' stroke-width='.7'/><line x1='33' y1='76.8' x2='37' y2='76.8' stroke='#475569' stroke-width='.7'/><line x1='33' y1='82.0' x2='41' y2='82.0' stroke='#475569' stroke-width='.7'/><line x1='33' y1='87.2' x2='37' y2='87.2' stroke='#475569' stroke-width='.7'/><line x1='33' y1='92.4' x2='37' y2='92.4' stroke='#475569' stroke-width='.7'/><line x1='33' y1='97.6' x2='37' y2='97.6' stroke='#475569' stroke-width='.7'/><line x1='33' y1='102.8' x2='37' y2='102.8' stroke='#475569' stroke-width='.7'/><line x1='33' y1='108.0' x2='41' y2='108.0' stroke='#475569' stroke-width='.7'/><line x1='33' y1='113.2' x2='37' y2='113.2' stroke='#475569' stroke-width='.7'/><line x1='33' y1='118.4' x2='37' y2='118.4' stroke='#475569' stroke-width='.7'/><line x1='33' y1='123.6' x2='37' y2='123.6' stroke='#475569' stroke-width='.7'/><line x1='33' y1='128.8' x2='37' y2='128.8' stroke='#475569' stroke-width='.7'/><line x1='33' y1='134.0' x2='41' y2='134.0' stroke='#475569' stroke-width='.7'/><line x1='33' y1='139.2' x2='37' y2='139.2' stroke='#475569' stroke-width='.7'/><line x1='33' y1='144.4' x2='37' y2='144.4' stroke='#475569' stroke-width='.7'/><line x1='33' y1='149.6' x2='37' y2='149.6' stroke='#475569' stroke-width='.7'/><line x1='33' y1='154.8' x2='37' y2='154.8' stroke='#475569' stroke-width='.7'/><line x1='33' y1='160.0' x2='41' y2='160.0' stroke='#475569' stroke-width='.7'/><line x1='33' y1='165.2' x2='37' y2='165.2' stroke='#475569' stroke-width='.7'/><line x1='33' y1='170.4' x2='37' y2='170.4' stroke='#475569' stroke-width='.7'/><line x1='33' y1='175.6' x2='37' y2='175.6' stroke='#475569' stroke-width='.7'/><line x1='33' y1='180.8' x2='37' y2='180.8' stroke='#475569' stroke-width='.7'/><line x1='33' y1='186.0' x2='41' y2='186.0' stroke='#475569' stroke-width='.7'/></svg><span>éprouvette graduée</span></button>
<button type="button" class="nt-verre" data-v="pip_grad"><svg class='nt-verre-svg' viewBox='0 0 90 220' role='img' aria-label="Une pipette graduée"><defs><linearGradient id='gVg' x1='0' x2='1'><stop offset='0' stop-color='#DCE7F2'/><stop offset='.45' stop-color='#FFFFFF'/><stop offset='1' stop-color='#DCE7F2'/></linearGradient></defs><path d='M41,8 L41,182 L43.5,210 L46.5,210 L49,182 L49,8' fill='url(#gVg)' stroke='#475569' stroke-width='1.2' stroke-linejoin='round'/><path d='M41.8,60 L41.8,182 L44,209.3 L46,209.3 L48.2,182 L48.2,60 Z' fill='#F9A8D4' fill-opacity='.65'/><line x1='41' y1='30.0' x2='47' y2='30.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='35.0' x2='44' y2='35.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='40.0' x2='44' y2='40.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='45.0' x2='44' y2='45.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='50.0' x2='44' y2='50.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='55.0' x2='47' y2='55.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='60.0' x2='44' y2='60.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='65.0' x2='44' y2='65.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='70.0' x2='44' y2='70.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='75.0' x2='44' y2='75.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='80.0' x2='47' y2='80.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='85.0' x2='44' y2='85.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='90.0' x2='44' y2='90.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='95.0' x2='44' y2='95.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='100.0' x2='44' y2='100.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='105.0' x2='47' y2='105.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='110.0' x2='44' y2='110.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='115.0' x2='44' y2='115.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='120.0' x2='44' y2='120.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='125.0' x2='44' y2='125.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='130.0' x2='47' y2='130.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='135.0' x2='44' y2='135.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='140.0' x2='44' y2='140.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='145.0' x2='44' y2='145.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='150.0' x2='44' y2='150.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='155.0' x2='47' y2='155.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='160.0' x2='44' y2='160.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='165.0' x2='44' y2='165.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='170.0' x2='44' y2='170.0' stroke='#475569' stroke-width='.7'/><line x1='41' y1='175.0' x2='44' y2='175.0' stroke='#475569' stroke-width='.7'/></svg><span>pipette graduée</span></button>
<button type="button" class="nt-verre" data-v="pip_jaug"><svg class='nt-verre-svg' viewBox='0 0 90 220' role='img' aria-label="Une pipette jaugée"><defs><linearGradient id='gVj' x1='0' x2='1'><stop offset='0' stop-color='#DCE7F2'/><stop offset='.45' stop-color='#FFFFFF'/><stop offset='1' stop-color='#DCE7F2'/></linearGradient></defs><path d='M42.5,4 L42.5,72 Q34,78 34,94 L34,134 Q34,148 42.5,154 L42.5,190 L44,210 L46,210 L47.5,190 L47.5,154 Q56,148 56,134 L56,94 Q56,78 47.5,72 L47.5,4' fill='url(#gVj)' stroke='#475569' stroke-width='1.2' stroke-linejoin='round'/><path d='M43.2,40 L43.2,72.5 Q35,79 35,94 L35,134 Q35,147 43.2,153.5 L43.2,190 L44.6,209.3 L45.4,209.3 L46.8,190 L46.8,153.5 Q55,147 55,134 L55,94 Q55,79 46.8,72.5 L46.8,40 Z' fill='#F9A8D4' fill-opacity='.65'/><line x1='42.5' y1='40' x2='47.5' y2='40' stroke='#1E293B' stroke-width='1.2'/></svg><span>pipette jaugée</span></button>
<button type="button" class="nt-verre" data-v="fiole"><svg class='nt-verre-svg' viewBox='0 0 90 220' role='img' aria-label="Une fiole jaugée"><defs><linearGradient id='gVf' x1='0' x2='1'><stop offset='0' stop-color='#DCE7F2'/><stop offset='.45' stop-color='#FFFFFF'/><stop offset='1' stop-color='#DCE7F2'/></linearGradient></defs><path d='M40,14 L40,124 Q20,142 9,168 Q2,204 31,204 L59,204 Q88,204 81,168 Q70,142 50,124 L50,14' fill='url(#gVf)' stroke='#475569' stroke-width='1.3' stroke-linejoin='round'/><path d='M40.8,56 L40.8,124.4 Q21,142.5 10,168 Q3.5,203 31,203 L59,203 Q86.5,203 80,168 Q69,142.5 49.2,124.4 L49.2,56 Z' fill='#F9A8D4' fill-opacity='.45'/><line x1='40' y1='56' x2='50' y2='56' stroke='#1E293B' stroke-width='1.2'/></svg><span>fiole jaugée</span></button>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le matériel d'une dilution&nbsp;:</p>
<ul class="nt-facts">
<li>une <span class="imp nt-hole">pipette jaugée</span> et une <span class="imp nt-hole">propipette</span> (poire à pipeter), pour <b>prélever</b> précisément la solution mère&nbsp;;</li>
<li>une <span class="imp nt-hole">fiole jaugée</span> et son bouchon, pour <b>contenir</b> précisément la solution fille&nbsp;;</li>
<li>une pissette d'eau distillée, et un bécher pour y verser un peu de solution mère.</li>
</ul>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Il existe des pipettes jaugées à <b>un trait</b> et des pipettes jaugées à <b>deux traits</b>&nbsp;:</p>
<ul class="nt-facts">
<li>avec une pipette à <b>un trait</b>, le volume indiqué est délivré quand on la laisse se vider entièrement&nbsp;;</li>
<li>avec une pipette à <b>deux traits</b>, le volume indiqué est compris entre les deux traits&nbsp;: on ne la vide que jusqu'au second trait, sans laisser s'écouler la fin du liquide.</li>
</ul>
<p>Avant de pipeter, il faut donc toujours regarder combien de traits porte la pipette.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi la verrerie jaugée est-elle si précise&nbsp;?</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>Un seul volume, un seul trait.</b> Une verrerie jaugée est fabriquée et étalonnée pour un unique volume, repéré par un trait de jauge. Elle n'a pas à être juste sur toute une échelle de graduations.</li>
<li><b>Un trait placé sur une partie étroite.</b> Le trait de jauge est gravé sur le col de la fiole, ou sur la tige de la pipette. Si l'on dépasse le trait d'un millimètre, l'erreur de volume est égale à la section du tube multipliée par ce millimètre&nbsp;: plus le tube est étroit, plus elle est faible. Sur un bécher ou une éprouvette, beaucoup plus larges, le même millimètre représente un volume bien plus grand.</li>
<li><b>Un étalonnage adapté à l'usage.</b> La fiole jaugée est étalonnée pour <i>contenir</i> son volume (marquage «&nbsp;In&nbsp;»). La pipette jaugée est étalonnée pour <i>délivrer</i> son volume (marquage «&nbsp;Ex&nbsp;»)&nbsp;: elle tient compte du film de liquide qui reste sur la paroi et de la goutte qui reste dans la pointe. C'est pourquoi on ne souffle jamais cette dernière goutte.</li>
<li><b>Une température de référence.</b> Les volumes sont garantis à 20&nbsp;°C, car le verre et le liquide se dilatent avec la température.</li>
</ul>
<p>Valeurs indicatives des tolérances (verrerie de classe A)&nbsp;:</p>
<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Verrerie</th><th>Volume</th><th>Tolérance</th><th>Incertitude relative</th></tr></thead>
<tbody>
<tr><td>pipette jaugée</td><td>10&nbsp;mL</td><td>±&nbsp;0,02&nbsp;mL</td><td>0,2&nbsp;%</td></tr>
<tr><td>pipette jaugée</td><td>25&nbsp;mL</td><td>±&nbsp;0,03&nbsp;mL</td><td>0,1&nbsp;%</td></tr>
<tr><td>fiole jaugée</td><td>100&nbsp;mL</td><td>±&nbsp;0,10&nbsp;mL</td><td>0,1&nbsp;%</td></tr>
<tr><td>fiole jaugée</td><td>250&nbsp;mL</td><td>±&nbsp;0,15&nbsp;mL</td><td>0,06&nbsp;%</td></tr>
<tr><td>burette graduée</td><td>25&nbsp;mL</td><td>±&nbsp;0,03&nbsp;mL</td><td>0,1&nbsp;%</td></tr>
<tr><td>pipette graduée</td><td>10&nbsp;mL</td><td>±&nbsp;0,05&nbsp;mL</td><td>0,5&nbsp;%</td></tr>
<tr><td>éprouvette graduée</td><td>100&nbsp;mL</td><td>±&nbsp;0,5&nbsp;mL</td><td>0,5&nbsp;%</td></tr>
<tr><td>bécher</td><td>100&nbsp;mL</td><td>environ ±&nbsp;5&nbsp;mL</td><td>environ 5&nbsp;%</td></tr>
</tbody>
</table>
</div>
<p class="nt-note">Les tolérances sont gravées sur la verrerie, avec sa classe (A, la plus précise, ou B, environ deux fois moins précise). Le bécher n'est pas un instrument de mesure&nbsp;: ses graduations ne sont qu'indicatives.</p>
</div>
</details>

### Utiliser une propipette {.nt-h3}

<p class="nt-lead">On utilise une propipette, aussi appelée poire à pipeter, pour aspirer le liquide dans la pipette. La plus courante est une poire en caoutchouc munie de trois valves, marquées A, S et E.</p>

<svg class='nt-svg nt-svg-m' viewBox='-60 0 580 470' role='img' aria-label="Propipette à trois valves montée sur une pipette : la valve A au-dessus de la poire chasse l'air, la valve S sous la poire aspire le liquide, la valve E sur le tube latéral le laisse s'écouler ; la pipette n'est enfoncée que d'environ un centimètre dans l'embout"><defs><radialGradient id='gRub' cx='.35' cy='.35' r='.75'><stop offset='0' stop-color='#F87171'/><stop offset='1' stop-color='#B91C1C'/></radialGradient><linearGradient id='gRubT' x1='0' x2='1'><stop offset='0' stop-color='#B91C1C'/><stop offset='.5' stop-color='#EF4444'/><stop offset='1' stop-color='#B91C1C'/></linearGradient><linearGradient id='gGl' x1='0' x2='1'><stop offset='0' stop-color='#DCE7F2'/><stop offset='.45' stop-color='#fff'/><stop offset='1' stop-color='#DCE7F2'/></linearGradient></defs><rect x='187' y='14' width='26' height='12' rx='3' fill='#9F1D1D'/><rect x='189' y='24' width='22' height='40' rx='5' fill='url(#gRubT)'/><circle cx='200' cy='44' r='7' fill='#E0F2FE' stroke='#64748B' stroke-width='1'/><circle cx='200' cy='120' r='62' fill='url(#gRub)'/><ellipse cx='178' cy='96' rx='16' ry='10' fill='#fff' opacity='.25'/><rect x='189' y='176' width='22' height='150' rx='5' fill='url(#gRubT)'/><circle cx='200' cy='206' r='7' fill='#E0F2FE' stroke='#64748B' stroke-width='1'/><rect x='122' y='252' width='70' height='20' rx='5' fill='url(#gRubT)'/><circle cx='154' cy='262' r='7' fill='#E0F2FE' stroke='#64748B' stroke-width='1'/><rect x='108' y='256' width='16' height='12' rx='3' fill='#9F1D1D'/><path d='M194,300 L194,470 M206,300 L206,470' stroke='#475569' stroke-width='1.3' fill='none'/><rect x='194.6' y='300' width='10.8' height='170' fill='url(#gGl)'/><rect x='195' y='388' width='10' height='82' fill='#F9A8D4' fill-opacity='.7'/><line x1='194' y1='360' x2='206' y2='360' stroke='#1E293B' stroke-width='1.2'/><rect x='189' y='296' width='22' height='30' rx='5' fill='url(#gRubT)' opacity='.9'/><line x1='194' y1='300' x2='206' y2='300' stroke='#FDE68A' stroke-width='2' stroke-dasharray='3 2'/><text x='200' y='48' font-size='11' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif'>A</text><text x='200' y='210' font-size='11' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif'>S</text><text x='154' y='266' font-size='11' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif'>E</text><line x1='208' y1='40' x2='300' y2='40' stroke='#64748B' stroke-width='.9'/><text x='306' y='44' font-size='13' fill='#1E293B' font-family='system-ui, sans-serif'>valve A (air)</text><text x='306' y='61' font-size='11.5' fill='#64748B' font-family='system-ui, sans-serif'>avec la poire : chasser l’air</text><line x1='255' y1='110' x2='300' y2='110' stroke='#64748B' stroke-width='.9'/><text x='306' y='114' font-size='13' fill='#1E293B' font-family='system-ui, sans-serif'>poire en caoutchouc</text><line x1='208' y1='206' x2='300' y2='200' stroke='#64748B' stroke-width='.9'/><text x='306' y='204' font-size='13' fill='#1E293B' font-family='system-ui, sans-serif'>valve S (succion)</text><text x='306' y='221' font-size='11.5' fill='#64748B' font-family='system-ui, sans-serif'>aspirer : le liquide monte</text><line x1='154' y1='270' x2='130' y2='300' stroke='#64748B' stroke-width='.9'/><text x='128' y='314' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, sans-serif'>valve E (écoulement)</text><text x='128' y='331' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, sans-serif'>le liquide descend</text><path d='M216,300 L222,300 L222,326 L216,326' fill='none' stroke='#CA8A04' stroke-width='1.3'/><text x='228' y='310' font-size='12.5' fill='#A16207' font-family='system-ui, sans-serif'>pipette enfoncée</text><text x='228' y='326' font-size='12.5' fill='#A16207' font-family='system-ui, sans-serif'>d’environ 1 cm seulement</text><line x1='208' y1='360' x2='300' y2='372' stroke='#64748B' stroke-width='.9'/><text x='306' y='376' font-size='13' fill='#1E293B' font-family='system-ui, sans-serif'>trait de jauge</text><line x1='206' y1='430' x2='300' y2='430' stroke='#64748B' stroke-width='.9'/><text x='306' y='434' font-size='13' fill='#1E293B' font-family='system-ui, sans-serif'>pipette jaugée</text></svg>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Les trois valves</p>
<ul class="nt-facts">
<li><span class="imp nt-hole">A</span> comme <b>air</b>&nbsp;: en appuyant sur A tout en pressant la poire, on <b>chasse l'air</b> de la poire.</li>
<li><span class="imp nt-hole">S</span> comme <b>succion</b>&nbsp;: en appuyant sur S, on <b>aspire</b> le liquide dans la pipette.</li>
<li><span class="imp nt-hole">E</span> comme <b>écoulement</b>&nbsp;: en appuyant sur E, on laisse <b>descendre</b> le liquide, pour ajuster le niveau ou vider la pipette.</li>
</ul>
</div>

<div class="nt-b nt-proto">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Protocole&nbsp;: utiliser une propipette à trois valves</p>
<p class="nt-proto-legend"><span><span class="nt-must">surligné</span>&nbsp;: à écrire sur une copie</span><span class="nt-ece">gestes utiles en TP</span></p>
<ol class="nt-steps">
<li><p><span class="nt-must">Adapter la propipette sur le haut de la pipette</span>, sans forcer&nbsp;: la pipette ne doit être enfoncée que d'environ 1&nbsp;cm.</p>
<p class="nt-ece">Critère pratique&nbsp;: enfoncer juste assez pour que la pipette tienne seule et que le raccord soit étanche, et jamais au-delà de l'embranchement du tube latéral E. Tenir la pipette près de son extrémité et l'engager en la tournant légèrement&nbsp;: une pipette forcée peut casser et blesser la main.</p></li>
<li><p><span class="nt-must">Chasser l'air de la poire</span>&nbsp;: appuyer sur A et presser la poire en même temps, puis relâcher A avant de relâcher la poire.</p>
<p class="nt-ece">Si l'on relâche la poire avant A, l'air rentre et il faut recommencer. Bien faite, cette étape laisse la poire aplatie.</p></li>
<li><p><span class="nt-must">Plonger la pointe de la pipette dans la solution et appuyer sur S</span>&nbsp;: le liquide monte. S'arrêter un peu au-dessus du trait de jauge.</p>
<p class="nt-ece">Appuyer progressivement&nbsp;: le liquide monte vite. Garder la pointe bien immergée, sinon de l'air est aspiré et des bulles se forment.</p></li>
<li><p><span class="nt-must">Sortir la pipette du liquide et appuyer doucement sur E</span> pour faire descendre le liquide jusqu'à ce que le bas du ménisque affleure le trait de jauge.</p>
<p class="nt-ece">Le trait doit être à hauteur des yeux. Essuyer l'extérieur de la pipette avec un papier avant d'ajuster.</p></li>
<li><p><span class="nt-must">Vider la pipette dans le récipient voulu en appuyant sur E</span>.</p>
<p class="nt-ece">Pointe contre la paroi, sans souffler la dernière goutte. Pour une pipette à deux traits, arrêter l'écoulement au second trait.</p></li>
</ol>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Ne jamais retourner, ni coucher, l'ensemble pipette et propipette quand la pipette contient du liquide&nbsp;: le liquide coulerait dans la poire. Il la contaminerait (et les prélèvements suivants avec elle), et pourrait l'abîmer s'il est corrosif. On tient toujours la pipette verticale, pointe vers le bas. Pour la même raison, on évite d'aspirer trop haut&nbsp;: le liquide ne doit jamais atteindre la poire.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Comment fonctionne une propipette&nbsp;?</span></summary>
<div class="nt-d-body">
<p><b>Des valves à bille.</b> Chaque valve est une bille de verre logée dans un tube de caoutchouc un peu trop étroit pour elle&nbsp;: au repos, le caoutchouc serre la bille, et le passage est fermé. En pinçant la valve, on déforme le caoutchouc autour de la bille, ce qui ouvre un petit passage le long de celle-ci&nbsp;: l'air (ou le liquide) peut circuler. Dès qu'on relâche, le caoutchouc se resserre et la valve se referme.</p>
<p><b>Une dépression.</b> En pressant la poire avec la valve A ouverte, on chasse l'air qu'elle contient. On referme A&nbsp;: la poire, élastique, tend à reprendre sa forme, mais aucun air ne peut entrer. Son volume augmente un peu, et la pression de l'air qu'elle contient devient inférieure à la pression atmosphérique.</p>
<p>En ouvrant S, on met la pipette en communication avec cette poire en dépression. La pression atmosphérique, qui s'exerce sur la surface de la solution, pousse le liquide dans la pipette. Il monte jusqu'à ce que la différence de pression soit compensée par le poids de la colonne de liquide&nbsp;: $P_\text{atm} - P_\text{poire} = \rho \, g \, h$. Pour une colonne d'eau de 40&nbsp;cm, il suffit d'une dépression de 4&nbsp;kPa environ, soit 4&nbsp;% de la pression atmosphérique.</p>
<p>En ouvrant E, on laisse entrer l'air au-dessus du liquide&nbsp;: la pression y redevient égale à la pression atmosphérique, et le liquide redescend sous l'effet de son poids. En pinçant E très légèrement, on contrôle le débit goutte à goutte.</p>
<p><b>Pourquoi ne pas trop enfoncer la pipette&nbsp;?</b> Le haut de la pipette doit rester sous l'embranchement du tube latéral, et loin de la valve S. Trop enfoncée, la pipette vient buter contre la bille de la valve S et peut la déloger de son logement. La valve ne ferme plus correctement&nbsp;: la dépression se perd, le liquide redescend tout seul ou ne monte plus, et la propipette devient inutilisable. Une pipette enfoncée au-delà du tube latéral boucherait aussi la valve E.</p>
</div>
</details>

## Le protocole {.nt-h2}

<img class="nt-fig-prot" src="/protdilution.png" alt="Les quatre étapes d'une dilution : 1. prélever la solution mère à la pipette jaugée munie d'une propipette ; 2. verser le contenu de la pipette dans la fiole jaugée ; 3. boucher et agiter ; 4. compléter à la pissette jusqu'au trait de jauge, le bas du ménisque à hauteur des yeux">

<div class="nt-b nt-proto">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Protocole&nbsp;: préparer une solution par dilution</p>
<p class="nt-proto-legend"><span><span class="nt-must">surligné</span>&nbsp;: à écrire sur une copie</span><span class="nt-ece">gestes utiles en TP</span></p>
<ol class="nt-steps">
<li><p><span class="nt-must">Prélever le volume $V_\text{mère}$ de solution mère avec une pipette jaugée munie d'une propipette</span>&nbsp;: <span class="nt-must">le bas du ménisque doit affleurer le trait de jauge</span>.</p>
<p class="nt-ece">Verser d'abord un peu de solution mère dans un bécher propre et sec&nbsp;: on ne pipette jamais directement dans le flacon, pour ne pas le polluer. Rincer la pipette avec un peu de solution mère (on la jette ensuite). Aspirer au-dessus du trait de jauge, puis ajuster en laissant s'écouler goutte à goutte, le trait à hauteur des yeux. Essuyer l'extérieur de la pipette avant de la vider.</p></li>
<li><p><span class="nt-must">Verser le contenu de la pipette dans une fiole jaugée de volume $V_\text{fille}$</span>.</p>
<p class="nt-ece">La fiole a été rincée à l'eau distillée (elle peut donc contenir un peu d'eau). Laisser la pipette s'écouler librement, pointe contre la paroi intérieure du col, et ne jamais souffler la dernière goutte&nbsp;: la pipette est étalonnée pour la garder. <b>Si la pipette est à deux traits</b>, ne verser que jusqu'au second trait, en arrêtant l'écoulement quand le bas du ménisque affleure ce trait, placé à hauteur des yeux.</p></li>
<li><p><span class="nt-must">Remplir la fiole aux trois quarts environ avec de l'eau distillée, la boucher et agiter</span> pour homogénéiser.</p>
<p class="nt-ece">Agiter en retournant la fiole plusieurs fois, en tenant le bouchon. Agiter avant d'atteindre le trait de jauge permet d'homogénéiser plus facilement, et de laisser le volume se stabiliser.</p></li>
<li><p><span class="nt-must">Compléter avec de l'eau distillée jusqu'au trait de jauge</span>, <span class="nt-must">puis boucher et agiter de nouveau</span>.</p>
<p class="nt-ece">Terminer goutte à goutte, à la pissette ou à la pipette Pasteur&nbsp;: le bas du ménisque doit être tangent au trait de jauge, l'œil à la hauteur du trait. Si l'on dépasse le trait, il faut tout recommencer.</p></li>
</ol>
</div>

<p class="nt-center"><a href="https://www.edumedia.com/fr/media/659-solution-concentration?auth=d8aa1c8b7e725a7b825d68207d1cbe03/75935" target="_blank" rel="noopener"><i class="fa-solid fa-play"></i>&nbsp; Voir le protocole animé sur eduMedia</a></p>

## Théorie {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Lors d'une dilution, <span class="imp nt-hole">la quantité de matière de soluté se conserve</span>&nbsp;: tout le soluté prélevé dans la solution mère se retrouve dans la solution fille.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Conservation du soluté</p>
<p class="nt-f-math">$$n_\text{fille}=n_\text{mère}$$</p>
<div class="nt-f-units"><span>$n$&nbsp;: quantité de matière de soluté, en <b>mol</b></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>En concentrations et volumes</p>
<p class="nt-f-math">$$C_\text{fille}\times V_\text{fille}=C_\text{mère}\times V_\text{mère}$$</p>
<div class="nt-f-units"><span>car $n = C \times V$</span></div>
</div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp">facteur de dilution</span> $F$ est le <span class="imp nt-hole">nombre de fois</span> que la solution a été diluée, c'est-à-dire le nombre par lequel sa concentration a été divisée. On a toujours $F > 1$.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Exprimer $F$ en fonction de $C_\text{mère}$ et $C_\text{fille}$, puis en fonction de $V_\text{mère}$ et $V_\text{fille}$, et enfin en fonction du volume de la fiole $V_\text{fiole}$ et de celui de la pipette $V_\text{pipette}$.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir les expressions</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>Par définition, la concentration est divisée par $F$&nbsp;: $C_\text{fille} = \dfrac{C_\text{mère}}{F}$, soit $F = \dfrac{C_\text{mère}}{C_\text{fille}}$.</p></li>
<li><p>D'après la conservation du soluté, $C_\text{fille}\times V_\text{fille}=C_\text{mère}\times V_\text{mère}$, donc $\dfrac{C_\text{mère}}{C_\text{fille}} = \dfrac{V_\text{fille}}{V_\text{mère}}$.</p></li>
<li><p>Le volume de solution fille est celui de la fiole, et le volume de solution mère est celui de la pipette.</p></li>
</ol>
</div>
</details>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Facteur de dilution</p>
<p class="nt-f-math">$$F = \frac{C_\text{mère}}{C_\text{fille}} = \frac{V_\text{fille}}{V_\text{mère}}= \frac{V_\text{fiole}}{V_\text{pipette}}$$</p>
<div class="nt-f-units"><span>$F$ sans unité, toujours supérieur à 1</span></div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>On veut obtenir 250&nbsp;mL d'une solution diluée 5&nbsp;fois ($F = 5$). Quel matériel doit-on choisir, et comment procède-t-on&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>Données&nbsp;: $V_\text{fille} = \pu{250 mL}$ et $F = 5$.</p></li>
<li><p>$V_\text{mère}=\dfrac{V_\text{fille}}{F}=\dfrac{\pu{250 mL}}{5} =\pu{50 mL}$.</p></li>
<li><p>Il faut donc une <b>pipette jaugée de 50&nbsp;mL</b> et une <b>fiole jaugée de 250&nbsp;mL</b>.</p></li>
<li><p>On prélève 50&nbsp;mL de solution mère avec la pipette, on les verse dans la fiole, on remplit aux trois quarts d'eau distillée en agitant, puis on complète jusqu'au trait de jauge et on agite de nouveau.</p></li>
</ol>
</div>
</details>

<div class="nt-lab" id="lab-dilution">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Choisir sa verrerie, trouver le facteur de dilution</p>
<div class="nt-ctrl">S'entraîner à trouver&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="dilmode" value="mix" checked><span>un peu de tout</span></label>
<label><input type="radio" name="dilmode" value="pip"><span>la pipette</span></label>
<label><input type="radio" name="dilmode" value="fio"><span>la fiole</span></label>
<label><input type="radio" name="dilmode" value="deux"><span>les deux</span></label>
<label><input type="radio" name="dilmode" value="F"><span>le facteur $F$</span></label>
</div>
</div>
<div class="nt-dil-enonce" aria-live="polite"></div>
<div class="nt-dil-zone"><p>Pipettes jaugées disponibles&nbsp;:</p><div class="nt-btns nt-dil-pip"></div></div>
<div class="nt-dil-zone"><p>Fioles jaugées disponibles&nbsp;:</p><div class="nt-btns nt-dil-fio"></div></div>
<div class="nt-dil-zone nt-dil-num"><p>Facteur de dilution&nbsp;:</p><p class="nt-dil-inline"><label for="dil-F">$F$ =</label> <input id="dil-F" type="text" inputmode="decimal" aria-label="Facteur de dilution"></p></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<p class="nt-note">Une série compte 8&nbsp;questions. Pour «&nbsp;les deux&nbsp;», plusieurs couples pipette-fiole peuvent convenir&nbsp;: tous sont acceptés.</p>
</div>

<script>
(function () {
  'use strict';
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function bilanTxt(r) { return r === 1 ? 'Parfait&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;!' : (r >= 0.5 ? 'C\u2019est un bon début&nbsp;: relisez les cas manqués.' : 'Revoyez le cours, puis recommencez.')); }
  /* écriture scientifique, mantisse à 2 chiffres significatifs */
  function sci(x) {
    var e = Math.floor(Math.log10(x) + 1e-9), m = x / Math.pow(10, e);
    if (m >= 9.95) { m /= 10; e += 1; }
    var mm = Math.abs(m * 10 - Math.round(m * 10)) < 1e-9 ? fr(m, 1) : fr(m, 2);   /* 2 ou 3 chiffres significatifs, sans arrondi trompeur */
    return e === 0 ? mm : mm + '\u00d710<sup>' + String(e).replace('-', '\u2212') + '</sup>';
  }
  /* ================= 1. Quelle verrerie est la plus précise ? ================= */
  (function () {
    var root = document.getElementById('lab-verrerie');
    if (!root) { return; }
    var Q = [
      { q: 'Pour <b>prélever</b> un volume précis de solution (et le verser ailleurs), quelle verrerie est la plus précise&nbsp;?', ok: 'pip_jaug',
        why: 'La pipette jaugée est conçue pour <b>délivrer</b> exactement le volume indiqué, repéré par un unique trait de jauge sur une tige étroite.' },
      { q: 'Pour <b>contenir</b> un volume précis de solution (pour la préparer), quelle verrerie est la plus précise&nbsp;?', ok: 'fiole',
        why: 'La fiole jaugée est conçue pour <b>contenir</b> exactement le volume indiqué, repéré par un trait de jauge sur un col étroit.' }
    ];
    var WRONG = {
      becher: 'Le bécher sert à contenir et à verser, pas à mesurer&nbsp;: ses graduations sont seulement indicatives (à environ 5&nbsp;% près).',
      erlen: 'L\u2019erlenmeyer sert à contenir un mélange (et à l\u2019agiter sans projections), pas à mesurer un volume.',
      eprouvette: 'L\u2019éprouvette graduée donne un ordre de grandeur correct, mais son large diamètre rend la lecture bien moins précise que celle d\u2019une verrerie jaugée.',
      pip_grad: 'La pipette graduée permet de prélever des volumes variés, mais elle est moins précise qu\u2019une pipette jaugée, qui n\u2019a qu\u2019un seul volume à délivrer.',
      pip_jaug: 'La pipette jaugée est faite pour prélever et délivrer un volume, pas pour préparer une solution.',
      fiole: 'La fiole jaugée est faite pour contenir un volume précis&nbsp;: elle ne permet pas de prélever un volume pour le transférer.'
    };
    var cards = $$(root, '.nt-verre'), qEl = $(root, '.nt-verre-q'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), next = $(root, '[data-act="next"]'), lbl = next.innerHTML;
    var k = 0, good = 0, answered = false;
    function show() {
      answered = false; qEl.innerHTML = Q[k].q; msg.textContent = 'Cliquez sur une verrerie.';
      cards.forEach(function (c) { c.classList.remove('nt-ok', 'nt-ko'); c.disabled = false; });
      next.innerHTML = k === Q.length - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lbl;
    }
    cards.forEach(function (c) {
      c.addEventListener('click', function () {
        if (answered) { return; }
        answered = true; var id = c.getAttribute('data-v'), q = Q[k];
        if (id === q.ok) { good++; c.classList.add('nt-ok'); msg.innerHTML = '<span style="color:#16A34A;">Bravo&nbsp;!</span> ' + q.why; }
        else {
          c.classList.add('nt-ko'); cards.forEach(function (d) { if (d.getAttribute('data-v') === q.ok) { d.classList.add('nt-ok'); } });
          msg.innerHTML = '<span style="color:#E11D48;">Non.</span> ' + WRONG[id] + ' ' + q.why;
        }
        sc.textContent = good + ' / ' + (k + 1);
      });
    });
    next.addEventListener('click', function () {
      if (!answered) { msg.textContent = 'Choisissez d\u2019abord une verrerie.'; return; }
      if (k === Q.length) { k = 0; good = 0; sc.textContent = '0 / 0'; root.classList.remove('nt-fini'); show(); return; }
      k++;
      if (k === Q.length) {
        root.classList.add('nt-fini'); qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + Q.length + '</span> ' + bilanTxt(good / Q.length);
        msg.innerHTML = 'À retenir&nbsp;: <b>pipette jaugée</b> pour prélever, <b>fiole jaugée</b> pour contenir.';
        next.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; return;
      }
      show();
    });
    show();
  })();
  /* ================= 2. S'exercer : pipette, fiole, facteur de dilution ================= */
  (function () {
    var root = document.getElementById('lab-dilution');
    if (!root) { return; }
    var PIP = [1, 2, 5, 10, 20, 25, 50], FIO = [50, 100, 200, 250, 500, 1000];
    var box = $(root, '.nt-dil-enonce'), zP = $(root, '.nt-dil-pip'), zF = $(root, '.nt-dil-fio'), zN = $(root, '.nt-dil-num'), inp = $(root, '.nt-dil-num input'),
        msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), btnV = $(root, '[data-act="check"]'), btnN = $(root, '[data-act="next"]'), lblN = btnN.innerHTML;
    var NQ = 8, n = 0, good = 0, cur = null, selP = null, selF = null, done = false, mode = 'mix';
    PIP.forEach(function (v) { var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn'; b.textContent = v + ' mL'; b.setAttribute('data-v', v); zP.appendChild(b); });
    FIO.forEach(function (v) { var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn'; b.textContent = v + ' mL'; b.setAttribute('data-v', v); zF.appendChild(b); });
    function pick(zone, set) {
      $$(zone, 'button').forEach(function (b) {
        b.addEventListener('click', function () { if (done) { return; } $$(zone, 'button').forEach(function (x) { x.classList.remove('nt-btn-main'); }); b.classList.add('nt-btn-main'); set(+b.getAttribute('data-v')); });
      });
    }
    pick(zP, function (v) { selP = v; }); pick(zF, function (v) { selF = v; });
    function rnd(a) { return a[Math.floor(Math.random() * a.length)]; }
    function pairs() { var r = []; PIP.forEach(function (p) { FIO.forEach(function (f) { if (f / p >= 2 && f / p <= 100) { r.push([p, f]); } }); }); return r; }
    function newQ() {
      var type = mode === 'mix' ? rnd(['pip', 'fio', 'deux', 'F']) : mode, pr = rnd(pairs()), p = pr[0], f = pr[1], F = f / p, Fs = (F % 1 === 0) ? String(F) : fr(F, 1);
      var Cm = rnd([1.0, 2.0, 5.0, 1.5, 2.5]) * Math.pow(10, -rnd([1, 2, 3])), Cf = Cm / F, useC = Math.random() < 0.5;
      var data = useC ? 'La solution mère a une concentration $C_\\text{mère}$ = ' + sci(Cm) + '&nbsp;mol/L&nbsp;; on veut une solution fille de concentration $C_\\text{fille}$ = ' + sci(Cf) + '&nbsp;mol/L.'
                      : 'On veut diluer la solution mère <b>' + Fs + '&nbsp;fois</b> (facteur de dilution $F$ = ' + Fs + ').';
      var q;
      if (type === 'pip') { q = data + ' On dispose d\u2019une fiole jaugée de <b>' + f + '&nbsp;mL</b>. Quelle pipette jaugée faut-il utiliser&nbsp;?'; }
      else if (type === 'fio') { q = data + ' On prélève la solution mère avec une pipette jaugée de <b>' + p + '&nbsp;mL</b>. Quelle fiole jaugée faut-il utiliser&nbsp;?'; }
      else if (type === 'deux') { q = data + ' Choisissez une pipette jaugée et une fiole jaugée qui conviennent.'; }
      else { q = 'On prélève <b>' + p + '&nbsp;mL</b> de solution mère avec une pipette jaugée, que l\u2019on verse dans une fiole jaugée de <b>' + f + '&nbsp;mL</b> avant de compléter avec de l\u2019eau distillée. Quel est le facteur de dilution $F$&nbsp;?'; }
      cur = { type: type, p: p, f: f, F: F, Fs: Fs.replace(',', '{,}'), useC: useC, Cm: Cm, Cf: Cf };
      box.innerHTML = '<p>' + q + '</p>';
      if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([box]); }
      zP.parentNode.hidden = !(type === 'pip' || type === 'deux'); zF.parentNode.hidden = !(type === 'fio' || type === 'deux'); zN.hidden = type !== 'F';
      selP = selF = null; inp.value = ''; done = false;
      $$(root, '.nt-dil-pip button, .nt-dil-fio button').forEach(function (b) { b.classList.remove('nt-btn-main', 'nt-ok', 'nt-ko'); });
      msg.textContent = ''; btnV.disabled = false;
      btnN.innerHTML = n === NQ - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lblN;
    }
    function expl() {
      var c = cur, s = c.useC ? '$F = \\dfrac{C_\\text{mère}}{C_\\text{fille}} = ' + c.Fs + '$, ' : '';
      if (c.type === 'pip') { return s + 'donc $V_\\text{pipette} = \\dfrac{V_\\text{fiole}}{F} = \\dfrac{' + c.f + '}{' + c.Fs + '} = ' + c.p + '$&nbsp;mL.'; }
      if (c.type === 'fio') { return s + 'donc $V_\\text{fiole} = F \\times V_\\text{pipette} = ' + c.Fs + '\\times' + c.p + ' = ' + c.f + '$&nbsp;mL.'; }
      if (c.type === 'deux') { return s + 'il faut $V_\\text{fiole} = ' + c.Fs + '\\times V_\\text{pipette}$&nbsp;: par exemple une pipette de ' + c.p + '&nbsp;mL et une fiole de ' + c.f + '&nbsp;mL.'; }
      return '$F = \\dfrac{V_\\text{fiole}}{V_\\text{pipette}} = \\dfrac{' + c.f + '}{' + c.p + '} = ' + c.Fs + '$.';
    }
    btnV.addEventListener('click', function () {
      if (done) { return; }
      var c = cur, ok;
      if (c.type === 'pip') { if (selP === null) { msg.textContent = 'Choisissez une pipette.'; return; } ok = selP === c.p; }
      else if (c.type === 'fio') { if (selF === null) { msg.textContent = 'Choisissez une fiole.'; return; } ok = selF === c.f; }
      else if (c.type === 'deux') { if (selP === null || selF === null) { msg.textContent = 'Choisissez une pipette et une fiole.'; return; } ok = Math.abs(selF / selP - c.F) < 1e-9; }
      else { var v = parseFloat(inp.value.replace(',', '.')); if (isNaN(v)) { msg.textContent = 'Entrez une valeur.'; return; } ok = Math.abs(v - c.F) < 1e-6; }
      done = true; btnV.disabled = true; if (ok) { good++; } n++;
      msg.innerHTML = (ok ? '<span style="color:#16A34A;">Bravo&nbsp;!</span> ' : '<span style="color:#E11D48;">Non.</span> ') + expl();
      if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([msg]); }
      sc.textContent = good + ' / ' + n;
    });
    btnN.addEventListener('click', function () {
      if (n >= NQ && done) {
        if (root.classList.contains('nt-fini')) { root.classList.remove('nt-fini'); n = 0; good = 0; sc.textContent = '0 / 0'; newQ(); return; }
        root.classList.add('nt-fini'); box.innerHTML = '<p class="nt-center"><span class="nt-big-score">' + good + ' / ' + NQ + '</span><br>' + bilanTxt(good / NQ) + '</p>';
        zP.parentNode.hidden = zF.parentNode.hidden = true; zN.hidden = true; msg.textContent = ''; btnV.disabled = true;
        btnN.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; return;
      }
      if (!done) { msg.textContent = 'Validez d\u2019abord votre réponse.'; return; }
      newQ();
    });
    $$(root, 'input[name="dilmode"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; n = 0; good = 0; sc.textContent = '0 / 0'; root.classList.remove('nt-fini'); newQ(); }); });
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { btnV.click(); } });
    newQ();
  })();
})();
</script>
