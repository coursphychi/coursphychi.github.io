+++
title = "Le son"
draft = false
hidden = true 
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-h4 { font-size: 1.08em !important; font-weight: 700 !important; color: var(--navy) !important; margin: 1.6em 0 0.6em !important; }
.nt-lab [hidden] { display: none !important; }
.nt-lab .nt-msg { margin-top: 0.8em !important; }
.nt-embed { position: relative; width: 100%; max-width: 760px; margin: 1em auto; aspect-ratio: 5 / 4; }
.nt-embed iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 10px; }
.nt-embed.nt-169 { aspect-ratio: 16 / 9; }
.nt-champ { display: inline-flex; align-items: center; gap: 0.35em; white-space: nowrap; margin: 0 0.5em; }
.nt-champ label { display: inline; margin: 0; font-weight: 600; }
.nt-champ input[type="text"] { width: 5.5em !important; min-width: 0; margin: 0; padding: 0.25em 0.5em; text-align: right; font: inherit; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-champ .nt-u { color: var(--slate); }
.nt-tr-ans { display: flex; align-items: center; justify-content: center; gap: 0.5em; flex-wrap: wrap; margin: 0.6em 0; }
/* interface des quiz et entraînements */
.nt-prog { display: flex; flex-wrap: wrap; gap: 0.4em; justify-content: center; margin: 0.3em 0 0.5em; }
.nt-prog i { width: 0.85em; height: 0.85em; border-radius: 50%; background: #E2E8F0; transition: background .25s; }
.nt-prog i.ok { background: #22C55E; } .nt-prog i.ko { background: #F43F5E; } .nt-prog i.cur { box-shadow: 0 0 0 2.5px var(--blue); }
.nt-qnum { text-align: center; font-size: 0.82em; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; color: var(--blue); margin: 0; }
.nt-qcard { background: linear-gradient(180deg, #FFFFFF, #F8FAFC); border: 1px solid var(--line); border-radius: 16px; padding: 0.9em 1em 1em; margin: 0.4em auto 0.6em; max-width: 620px; box-shadow: 0 6px 18px rgba(15,23,42,.06); }
.nt-qcard.nt-qcard-w { max-width: 720px; }
.nt-qvis { font-family: Georgia, serif; font-size: 2.2em; text-align: center; margin: 0.15em 0 0.25em; color: var(--navy); }
.nt-ql-q { font-size: 1.05em; text-align: center; margin: 0.5em 0 0.7em !important; min-height: 1.6em; }
.nt-ql-btns { display: flex; flex-wrap: wrap; gap: 0.5em; justify-content: center; }
.nt-ql-btns .nt-choix { padding: 0.6em 1.1em; border-radius: 12px; font-size: 1em; transition: transform .12s, box-shadow .12s; }
.nt-ql-btns .nt-choix:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37,99,235,.18); }
.nt-choix-ok { background: #DCFCE7 !important; border-color: #16A34A !important; color: #166534 !important; }
.nt-choix-ko { background: #FFE4E6 !important; border-color: #E11D48 !important; color: #9F1239 !important; }
.nt-msg.nt-fb { border-radius: 12px; padding: 0.6em 0.9em; text-align: left; }
.nt-msg.nt-fb.ok { background: #F0FDF4; border-left: 4px solid #22C55E; } .nt-msg.nt-fb.ko { background: #FFF1F2; border-left: 4px solid #F43F5E; }
.nt-msg.nt-fb.warn { background: #FFF7ED; border-left: 4px solid #F97316; } .nt-msg.nt-fb.warn > b:first-child { color: #C2410C; }
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
@media (prefers-reduced-motion: reduce) { .nt-ql-btns .nt-choix, .nt-prog i { transition: none; } .nt-ql-btns .nt-choix:hover { transform: none; } }
/* chronomètres et afficheurs */
.nt-chrono { font-variant-numeric: tabular-nums; font-size: 2em; font-weight: 300; color: var(--navy); text-align: center; letter-spacing: 0.02em; margin: 0.1em 0 !important; }
.nt-chrono small { font-size: 0.45em; color: var(--slate); margin-left: 0.3em; }
.nt-sono { display: inline-flex; align-items: baseline; gap: 0.3em; padding: 0.15em 0.8em; border-radius: 10px; background: var(--navy); color: #A7F3D0; font-variant-numeric: tabular-nums; font-size: 1.5em; font-weight: 300; }
.nt-sono small { font-size: 0.55em; color: #CBD5E1; }
/* laboratoire du son : les trois caractéristiques */
.nt-feat3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; margin: 0.7em 0 0.4em; }
.nt-feat3 .nt-feat { padding: 0.5em 0.8em; transition: box-shadow .25s, transform .25s; }
.nt-feat3 .nt-feat p { font-size: 0.92em; }
.nt-feat3 .nt-feat.nt-on { box-shadow: 0 0 0 3px color-mix(in srgb, var(--f) 35%, transparent), 0 6px 16px rgba(30, 41, 59, 0.10); transform: translateY(-2px); }
@media (prefers-reduced-motion: reduce) { .nt-feat3 .nt-feat { transition: none; } .nt-feat3 .nt-feat.nt-on { transform: none; } }
.nt-f-haut { --f: var(--c-haut); } .nt-f-timbre { --f: var(--c-timbre); } .nt-f-int { --f: var(--c-int); }
.nt-piano { display: flex; justify-content: center; gap: 3px; margin: 0.6em 0 0.2em; flex-wrap: wrap; }
.nt-piano button { width: 3.1em; height: 5.2em; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; padding-bottom: 0.35em; border: 1px solid #CBD5E1; border-radius: 0 0 8px 8px; background: linear-gradient(#fff, #F1F5F9); cursor: pointer; font-size: 0.78em; color: var(--slate); line-height: 1.25; }
.nt-piano button b { color: var(--ink); font-weight: 600; }
.nt-piano button:hover { background: linear-gradient(#fff, #E0F2FE); }
.nt-piano button.nt-on { background: linear-gradient(#E0F2FE, #BAE6FD); border-color: var(--sky); }
.nt-piano button:focus-visible { outline: 3px solid var(--sky); outline-offset: 2px; }
/* niveaux sonores */
.nt-presets { display: flex; flex-wrap: wrap; gap: 0.35em; justify-content: center; margin: 0.5em 0; }
.nt-presets .nt-btn { font-weight: 600; font-size: 0.82em; padding: 0.25em 0.75em; }
.nt-presets .nt-btn[aria-pressed="true"] { background: var(--blue); color: #fff; }
.nt-info { margin: 0.6em auto 0; max-width: 640px; padding: 0.6em 1em; border-radius: 12px; background: var(--slate-bg); border: 1px solid var(--line); }
.nt-info p { margin: 0.3em 0 !important; line-height: 1.55; }
.nt-heart { display: inline-block; font-size: 2.2em; vertical-align: middle; animation: nt-pulse 0.8s infinite; }
@keyframes nt-pulse { 0%, 100% { transform: scale(1); } 15% { transform: scale(1.18); } 30% { transform: scale(1); } 45% { transform: scale(1.1); } }
@media (prefers-reduced-motion: reduce) { .nt-heart { animation: none; } }
.nt-lamp { display: grid; grid-template-columns: minmax(130px, 0.6fr) 1.4fr; gap: 14px; align-items: center; }
@media (max-width: 600px) { .nt-lamp { grid-template-columns: 1fr; } }
.nt-svg-l { max-width: 720px; }
/* course des signaux : calculs */
.nt-calc { display: grid; gap: 0.4em; max-width: 600px; margin: 0.8em auto 0; }
.nt-calc:empty { display: none; }
.nt-calc .nt-calc-head { text-align: center; font-size: 0.92em; color: var(--slate); margin: 0 0 0.2em !important; }
.nt-calc-row { display: flex; align-items: center; flex-wrap: wrap; gap: 0.3em 0.9em; padding: 0.4em 0.9em; border-radius: 10px; background: #fff; border: 1px solid var(--line); border-left: 5px solid var(--k); }
.nt-calc-n { font-weight: 600; color: var(--k); min-width: 9.5em; }
.nt-calc-row b { color: var(--k); }
.nt-fr { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; line-height: 1.25; font-size: 0.9em; margin: 0 0.15em; }
.nt-fr > span:first-child { border-bottom: 1px solid currentColor; padding: 0 0.35em 0.05em; }
.nt-fr > span + span { padding: 0.05em 0.35em 0; }
/* générateur de sons : icônes des instruments, note entière */
.nt-ico { width: 1.2em; height: 1.2em; vertical-align: -0.25em; margin-right: 0.3em; fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
#lab-son canvas + canvas { margin-top: 8px; }
/* trompettes : mesure au micro */
.nt-mic { margin-top: 1.1em; padding: 0.8em 1em; border-radius: 12px; border: 1px dashed #CBD5E1; background: #F8FAFC; }
.nt-mic-title { font-weight: 700; color: var(--navy); margin: 0 0 0.3em !important; }
.nt-vu { display: flex; align-items: center; gap: 0.8em; max-width: 520px; margin: 0.6em auto; }
.nt-vu-bar { flex: 1; height: 14px; border-radius: 7px; background: #E2E8F0; overflow: hidden; }
.nt-vu-bar > div { height: 100%; width: 0; border-radius: 7px; background: linear-gradient(90deg, #34D399, #FBBF24 60%, #F97316); }
.nt-vu .nt-sono { font-size: 1.2em; min-width: 4.2em; justify-content: center; }
table.nt-mes td, table.nt-mes th { text-align: center; }
/* échelle des niveaux : risque */
#lab-echelle .nt-info { --k: #15803D; border-left: 5px solid var(--k); background: linear-gradient(90deg, color-mix(in srgb, var(--k) 9%, #FFFFFF), #FFFFFF 70%); transition: border-color .25s; }
#lab-echelle .nt-risk-head { font-weight: 700; color: var(--k); font-size: 1.08em; margin-bottom: 0.4em !important; }
#lab-echelle .nt-effet { color: var(--k); }
#lab-echelle .nt-effet b { color: var(--k); }
.nt-jauge { position: relative; height: 1.5em; margin: 0.3em 0 0.5em; border-radius: 0.75em; background: #E2E8F0; overflow: hidden; }
.nt-jauge > div { height: 100%; background: var(--k); opacity: 0.85; border-radius: 0.75em; transition: width .3s; }
.nt-jauge > span { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 0.8em; font-weight: 600; color: #0F172A; text-shadow: 0 0 3px #fff, 0 0 3px #fff; }
@media (prefers-reduced-motion: reduce) { .nt-jauge > div, #lab-echelle .nt-info { transition: none; } }
/* exemple escamotable */
details.nt-d.nt-exd { --c: var(--emerald); --bg: var(--emerald-bg); --c-ink: #065F46; }
details.nt-d.nt-exd pre { overflow-x: auto; margin: 0.6em 0 !important; padding: 0.6em 0.9em; border-radius: 8px; background: #0F172A; color: #E2E8F0; font-size: 0.86em; line-height: 1.5; }
details.nt-d.nt-exd pre code { background: none; color: inherit; padding: 0; }
#lab-trompettes .nt-dots { justify-content: center; }
.nt-b pre { overflow-x: auto; margin: 0.6em 0 !important; padding: 0.6em 0.9em; border-radius: 8px; background: #0F172A; color: #E2E8F0; font-size: 0.86em; line-height: 1.5; }
.nt-b pre code { background: none; color: inherit; padding: 0; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Une corde de guitare, une voix, un coup de tonnerre… Tous les sons ont la même origine&nbsp;: quelque chose <b>vibre</b>. Dans ce chapitre, on suit le son depuis sa source jusqu'à notre oreille, puis on apprend à le décrire avec des grandeurs physiques que l'on sait mesurer&nbsp;: la <b>fréquence</b>, la <b>forme</b> et l'<b>amplitude</b> du signal sonore.</p>

## Émission et perception d'un son {.nt-h2}

### Une vibration qui se propage {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le son est produit par une <span class="imp nt-hole">vibration</span> qui se propage <span class="imp nt-hole">de proche en proche</span> dans un <span class="imp nt-hole">milieu matériel</span>.</p>
<p>Les particules du milieu lui-même ne font qu'<span class="imp nt-hole">osciller sur place</span>.</p>
</div>

<p>Quand la membrane d'un haut-parleur avance, elle pousse les particules d'air qui la touchent&nbsp;; celles-ci poussent à leur tour leurs voisines, qui poussent les suivantes, et ainsi de suite&nbsp;: c'est ce relais que l'on appelle une propagation <b>de proche en proche</b>. Chaque particule revient ensuite vers sa position de départ&nbsp;: elle ne fait qu'aller et venir autour de sa <b>position de repos</b>. Dans l'air se succèdent alors des zones où les particules sont rapprochées (l'air y est <b>comprimé</b>) et des zones où elles sont écartées (l'air y est <b>dilaté</b>)&nbsp;: ce sont ces zones qui voyagent, et non l'air lui-même.</p>

<div class="nt-lab" id="lab-propag">
<p class="nt-tag"><i class="fa-solid fa-wave-square"></i>Animation</p>
<p class="nt-lab-title">Le son se propage de proche en proche</p>
<canvas role="img" aria-label="Haut-parleur à gauche et particules d'air alignées : la vibration de la membrane se transmet de particule en particule vers la droite."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="onoff"><i class="fa-solid fa-play"></i>&nbsp; Faire vibrer le haut-parleur</button><button type="button" class="nt-btn" data-act="clap"><i class="fa-solid fa-hand"></i>&nbsp; Une seule poussée</button></div>
<div class="nt-ctrls"><label class="nt-ctrl">Fréquence de la vibration (très ralentie)&nbsp;: <b class="out-f"></b><input type="range" min="0.4" max="2" step="0.1" value="1" data-in="f"></label></div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="zones" checked> Colorer les zones comprimées</label><label class="nt-check"><input type="checkbox" data-in="suivi" checked> Suivre une particule</label></div>
<p class="nt-msg" aria-live="polite">Lancez le haut-parleur, puis observez la particule rouge&nbsp;: va-t-elle jusqu'au bout de l'écran&nbsp;?</p>
</div>
<p class="nt-cap">La vibration (et les zones comprimées, en bleu) traverse tout l'écran, alors que la particule rouge reste toujours au voisinage de sa position de repos (trait pointillé). L'animation est énormément ralentie&nbsp;: dans l'air, le son parcourt environ 340&nbsp;m en une seconde.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On est en présence d'une <span class="imp nt-hole">onde</span> (l'onde sonore), caractérisée par un <span class="imp nt-hole">transport d'énergie et d'information</span> <span class="imp nt-hole">sans transport de matière</span>.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li><b>Énergie</b>&nbsp;: un son très fort peut faire vibrer une vitre, et même la briser.</li>
<li><b>Information</b>&nbsp;: une parole, une mélodie, une alarme nous renseignent sur ce qui se passe autour de nous.</li>
<li><b>Pas de matière</b>&nbsp;: l'air sorti de la bouche d'un orateur n'arrive pas dans l'oreille de ses auditeurs&nbsp;; seule la vibration voyage. C'est comme la ola dans un stade&nbsp;: la vague fait le tour des tribunes, mais chaque spectateur reste à sa place.</li>
</ul>
</div>

### Pas de son sans milieu matériel {.nt-h3}

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p><span class="imp nt-hole">Sans milieu matériel, pas de son</span>&nbsp;! Le vide spatial est donc <span class="imp nt-hole">silencieux</span>.</p>
<p>Dans les films, les vaisseaux spatiaux explosent dans un fracas assourdissant&nbsp;: c'est physiquement faux. On verrait l'explosion, car la lumière se propage dans le vide, mais on ne l'entendrait pas.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Pas de feu non plus, d'ailleurs&nbsp;! Une flamme est une combustion, qui a besoin d'un comburant&nbsp;: sur Terre, c'est le dioxygène de l'air. Dans le vide, pas de longues flammes qui ondulent comme dans les films (les moteurs de fusée, eux, emportent leur propre comburant).</p>
</div>

<div class="nt-lab" id="lab-cloche">
<p class="nt-tag"><i class="fa-solid fa-flask"></i>Expérience simulée</p>
<p class="nt-lab-title">Un réveil sous une cloche à vide</p>
<canvas role="img" aria-label="Un réveil qui sonne sous une cloche de verre reliée à une pompe à vide ; à droite, un indicateur du son perçu."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="pomper"><i class="fa-solid fa-wind"></i>&nbsp; Pomper l'air</button><button type="button" class="nt-btn" data-act="rentrer"><i class="fa-solid fa-rotate-left"></i>&nbsp; Laisser rentrer l'air</button><label class="nt-check"><input type="checkbox" data-in="son"> Entendre le réveil</label></div>
<div class="nt-ctrls"><label class="nt-ctrl">Pression dans la cloche (en % de la pression atmosphérique)&nbsp;: <b class="out-air"></b><input type="range" min="2" max="100" step="1" value="100" data-in="air"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>
<p class="nt-cap">Une expérience classique, réalisée pour la première fois par Robert Boyle en 1660. Chaque point représente un nombre gigantesque de molécules, et le niveau sonore affiché n'est qu'un ordre de grandeur.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Ce que cette expérience montre… et ce qu'elle ne montre pas</span></summary>
<div class="nt-d-body">
<p>Cette expérience est souvent présentée comme la preuve que le son ne se propage pas dans le vide. Elle est en réalité bien moins démonstrative.</p>
<ul class="nt-facts">
<li><b>La cloche est loin d'être vide.</b> Même à un millième de la pression atmosphérique, chaque centimètre cube d'air contient encore environ 25 millions de milliards de molécules, qui se heurtent sans cesse&nbsp;: le son s'y propage toujours de proche en proche.</li>
<li><b>Ce qui diminue surtout, c'est le passage d'un milieu à l'autre.</b> La sonnerie met mal en mouvement un gaz aussi peu dense, et ce gaz fait à son tour mal vibrer la paroi de verre, beaucoup plus «&nbsp;lourde&nbsp;» que lui (les physiciens parlent de désaccord d'impédance acoustique). Ces deux passages difficiles suffisent à affaiblir énormément le son, alors même qu'il se propage dans l'air de la cloche&nbsp;: à 1&nbsp;% de la pression atmosphérique, l'intensité transmise est environ 10&nbsp;000 fois plus faible (40&nbsp;dB de moins).</li>
<li><b>Une partie du son passe par le socle</b>, qui relie la sonnerie au reste de la paillasse.</li>
</ul>
<p>L'expérience montre donc seulement que <b>moins il y a d'air, moins le son est transmis</b>. Que le son ne passe pas du tout dans le vide en est une extrapolation, raisonnable mais non démontrée par l'expérience. Les arguments les plus directs viennent d'ailleurs&nbsp;: le son est une vibration transmise par des particules, il ne peut donc rien transmettre là où il n'y en a (presque) pas, comme dans l'espace interplanétaire, où l'on compte quelques particules par centimètre cube. C'est pourquoi les astronautes communiquent par radio, grâce à des ondes électromagnétiques qui, comme la lumière du Soleil, traversent le vide.</p>
</div>
</details>

### Vitesse de propagation {.nt-h3}

<p>La vitesse de propagation du son <b>dépend du milieu</b>&nbsp;: elle est en général plus grande dans les liquides que dans les gaz, et plus grande encore dans les solides. Dans l'air, elle dépend aussi un peu de la température (331&nbsp;m/s à 0&nbsp;°C, 343&nbsp;m/s à 20&nbsp;°C)&nbsp;: on retient la valeur approchée de <b>340&nbsp;m/s</b>.</p>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>milieu</th><th>air</th><th>eau</th><th>acier</th></tr></thead>
<tbody><tr><td>vitesse du son (m/s)</td><td>340</td><td>1&nbsp;500</td><td>5&nbsp;800</td></tr></tbody>
</table></div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi le son va-t-il plus vite dans l'acier que dans l'air&nbsp;?</span></summary>
<div class="nt-d-body">
<p>On entend souvent «&nbsp;plus le milieu est dense, plus le son va vite&nbsp;». C'est faux en général&nbsp;! Ce qui compte surtout, c'est la <b>raideur</b> du milieu&nbsp;: la force avec laquelle les particules sont liées les unes aux autres. Dans un solide, elles sont très fortement liées, comme des billes reliées par des ressorts très raides&nbsp;: une poussée se transmet presque immédiatement à la voisine. Dans un gaz, les particules sont éloignées et n'interagissent qu'en se heurtant.</p>
<p>La masse des particules joue au contraire dans l'autre sens&nbsp;: à raideur égale, des particules plus lourdes sont plus lentes à mettre en mouvement, donc le son est <b>plus lent</b> dans un milieu plus dense. Quelques exemples&nbsp;:</p>
<ul class="nt-facts">
<li>l'hélium est environ 7 fois moins dense que l'air, et le son y va environ 3 fois plus vite (près de 1&nbsp;000&nbsp;m/s)&nbsp;;</li>
<li>le dioxyde de carbone est plus dense que l'air, et le son y est plus lent (environ 270&nbsp;m/s)&nbsp;;</li>
<li>le plomb est 4 fois plus dense que l'aluminium, mais le son y est environ 3 fois plus lent (environ 2&nbsp;200&nbsp;m/s contre 6&nbsp;300&nbsp;m/s).</li>
</ul>
<p>Si l'eau et l'acier «&nbsp;battent&nbsp;» l'air, c'est donc parce qu'ils sont beaucoup plus raides (bien plus difficiles à comprimer), et non parce qu'ils sont plus denses.</p>
</div>
</details>

<p>Comparons la vitesse du son à d'autres vitesses que l'on rencontre couramment&nbsp;:</p>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>mobile ou signal</th><th>vitesse (m/s)</th><th>vitesse (km/h)</th></tr></thead>
<tbody>
<tr><td>piéton</td><td>1,4</td><td>5</td></tr>
<tr><td>voiture sur autoroute</td><td>36</td><td>130</td></tr>
<tr><td>TGV</td><td>89</td><td>320</td></tr>
<tr><td>avion de ligne</td><td>250</td><td>900</td></tr>
<tr><td>son dans l'air</td><td>340</td><td>1&nbsp;224</td></tr>
<tr><td>lumière (dans le vide ou dans l'air)</td><td>300&nbsp;000&nbsp;000</td><td>1&nbsp;080&nbsp;000&nbsp;000</td></tr>
</tbody>
</table></div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Un avion qui va plus vite que le son «&nbsp;franchit le mur du son&nbsp;» et produit un «&nbsp;bang&nbsp;» supersonique. Le Concorde volait à environ 2&nbsp;200&nbsp;km/h, soit près de deux fois la vitesse du son.</p>
</div>

<div class="nt-lab" id="lab-course">
<p class="nt-tag"><i class="fa-solid fa-flag-checkered"></i>Animation</p>
<p class="nt-lab-title">La course des signaux</p>
<p class="nt-note nt-center">Quatre signaux partent au même instant pour parcourir la même distance&nbsp;: un éclair de lumière, et un son qui voyage dans l'acier, dans l'eau ou dans l'air. Les chronomètres sont en temps réel.</p>
<canvas role="img" aria-label="Un couloir pour la lumière, séparé de trois couloirs pour le son dans l'acier, dans l'eau et dans l'air. Les signaux partent ensemble et arrivent à des instants différents."></canvas>
<div class="nt-ctrls"><div class="nt-ctrl">Distance à parcourir&nbsp;:<div class="nt-seg" role="radiogroup"><label><input type="radio" name="course-d" value="100"><span>100 m</span></label><label><input type="radio" name="course-d" value="1000" checked><span>1 km</span></label><label><input type="radio" name="course-d" value="3000"><span>3 km</span></label></div></div></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-flag"></i>&nbsp; Top départ&nbsp;!</button><label class="nt-check"><input type="checkbox" data-in="ralenti"> Ralenti (×&nbsp;10)</label></div>
<div class="nt-calc" aria-live="polite"></div>
</div>

### Convertir des vitesses {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Comment convertir en km/h les vitesses du son données plus haut (340&nbsp;m/s, 1&nbsp;500&nbsp;m/s et 5&nbsp;800&nbsp;m/s)&nbsp;?</p>
</div>

<p>Commençons par l'inverse&nbsp;: convertissons des km/h en m/s, en prenant l'exemple de $\pu{72 km/h}$. Une vitesse de 72&nbsp;km/h signifie que l'on parcourt 72&nbsp;km en 1&nbsp;heure&nbsp;; il suffit de remplacer chaque unité par sa valeur en mètres ou en secondes&nbsp;:</p>

<div class="nt-scroll"><p class="nt-big">$\pu{72 km/h} = \dfrac{\pu{72 km}}{\pu{1 h}} = \dfrac{\pu{72E3 m}}{\pu{3600 s}} = \dfrac{\pu{72E3 m}}{\pu{3,6E3 s}}$</p></div>

<div class="nt-scroll"><p class="nt-big">donc $\pu{72 km/h} = \dfrac{72}{\textcolor{#E11D48}{3,6}}\ \pu{m/s} = \pu{20 m/s}$</p></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Il faut <span class="imp nt-hole">diviser par 3,6</span> pour passer <b>des km/h aux m/s</b>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Que doit-on alors faire pour passer des m/s aux km/h&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Faire l'opération inverse</span></summary>
<div class="nt-d-body">
<p>On fait l'opération inverse de la division par 3,6&nbsp;: on <b>multiplie par 3,6</b>. Vérification&nbsp;: $\pu{20 m/s} \times 3,6 = \pu{72 km/h}$, on retrouve bien la vitesse de départ.</p>
<p>Pour ne pas se tromper de sens&nbsp;: en roulant à 1&nbsp;m/s pendant une heure (3&nbsp;600&nbsp;s), on parcourt 3&nbsp;600&nbsp;m, soit 3,6&nbsp;km. Donc $\pu{1 m/s} = \pu{3,6 km/h}$&nbsp;: une même vitesse s'écrit toujours avec un <b>nombre plus grand en km/h</b> qu'en m/s.</p>
</div>
</details>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-s' viewBox='0 0 420 172' role='img' aria-label="Pour passer des km/h aux m/s, on divise par 3,6 ; pour passer des m/s aux km/h, on multiplie par 3,6."><rect x='40' y='62' width='110' height='46' rx='12' fill='#EEF5FE' stroke='#2A6BC4' stroke-width='1.2'/><text x='95' y='92' font-size='19' text-anchor='middle' fill='#12305A' font-family='Georgia, "Times New Roman", serif'>km/h</text><rect x='270' y='62' width='110' height='46' rx='12' fill='#EEF5FE' stroke='#2A6BC4' stroke-width='1.2'/><text x='325' y='92' font-size='19' text-anchor='middle' fill='#12305A' font-family='Georgia, "Times New Roman", serif'>m/s</text><path d='M105,60 C150,8 260,8 302,55' fill='none' stroke='#2A6BC4' stroke-width='1.4'/><polygon points='305,60 296.1,55.8 302.1,50.6' fill='#2A6BC4'/><rect x='174' y='10' width='62' height='24' rx='12' fill='#FFFFFF'/><text x='205' y='27.4' font-size='15' text-anchor='middle' fill='#2A6BC4' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>÷ 3,6</text><path d='M305,110 C260,162 150,162 108,115' fill='none' stroke='#059669' stroke-width='1.4'/><polygon points='105,110 113.9,114.2 107.9,119.4' fill='#059669'/><rect x='174' y='137' width='62' height='24' rx='12' fill='#FFFFFF'/><text x='205' y='154.4' font-size='15' text-anchor='middle' fill='#059669' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>× 3,6</text></svg></div>
<p class="nt-cap">Les deux conversions à connaître.</p>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Les vitesses du son en km/h</span></summary>
<div class="nt-d-body">
<p>On multiplie par 3,6&nbsp;:</p>
<ul class="nt-facts">
<li>dans l'air&nbsp;: $340 \times 3,6 = \pu{1224 km/h}$&nbsp;;</li>
<li>dans l'eau&nbsp;: $1\,500 \times 3,6 = \pu{5400 km/h}$&nbsp;;</li>
<li>dans l'acier&nbsp;: $5\,800 \times 3,6 = \pu{20880 km/h}$.</li>
</ul>
</div>
</details>

### Vitesse, distance et durée {.nt-h3}

<p>Rappel&nbsp;: en appelant $d$ la distance parcourue (en m) et $\Delta t$ la durée écoulée (en s), la vitesse $v$ d'un signal est donnée par la relation&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$v = \dfrac{d}{\Delta t}$</p>
<div class="nt-f-units"><span>$v$&nbsp;: vitesse en <b>m/s</b></span><span>$d$&nbsp;: distance en <b>m</b></span><span>$\Delta t$&nbsp;: durée en <b>s</b></span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On écrit $\Delta t$ car une durée est l'écart entre deux instants, et le symbole $\Delta$ (la lettre grecque «&nbsp;delta&nbsp;» majuscule) désigne, en physique, un écart&nbsp;: $\Delta t = t_\text{final} - t_\text{initial}$.</p>
<p>Symétriquement, on peut aussi considérer la distance comme un écart entre deux positions&nbsp;: au lieu de $d$, on aurait pu écrire $\Delta x$.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Si l'on connaît la vitesse et la durée, comment obtient-on la distance&nbsp;? Et si l'on connaît la distance et la vitesse, comment obtient-on la durée&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Transformer la relation</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>On multiplie les deux membres de $v = \dfrac{d}{\Delta t}$ par $\Delta t$&nbsp;: $v \times \Delta t = d$.</p></li>
<li><p>On divise ensuite les deux membres de $d = v \times \Delta t$ par $v$&nbsp;: $\Delta t = \dfrac{d}{v}$.</p></li>
</ol>
<p>Vérification avec les unités&nbsp;: des m/s multipliés par des s donnent bien des m, et des m divisés par des m/s donnent bien des s.</p>
</div>
</details>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Distance</p>
<p class="nt-f-math">$d = v \times \Delta t$</p>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Durée</p>
<p class="nt-f-math">$\Delta t = \dfrac{d}{v}$</p>
</div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pourquoi doit-on compter approximativement 3&nbsp;s par kilomètre entre l'éclair et le tonnerre&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">La lumière arrive tout de suite, le son prend son temps</span></summary>
<div class="nt-d-body">
<p>L'éclair et le tonnerre sont produits au même instant. Pour parcourir 1&nbsp;km, soit 1&nbsp;000&nbsp;m&nbsp;:</p>
<ul class="nt-facts">
<li>le son met $\Delta t = \dfrac{d}{v} = \dfrac{\pu{1000 m}}{\pu{340 m/s}} \approx \pu{2,9 s}$, soit environ 3&nbsp;s&nbsp;;</li>
<li>la lumière met $\Delta t = \dfrac{\pu{1000 m}}{300\,000\,000\ \pu{m/s}}$, soit environ $0,000\,003\ \pu{s}$&nbsp;: elle nous parvient pratiquement instantanément.</li>
</ul>
<p>Le décalage entre l'éclair et le tonnerre est donc la durée de trajet du son&nbsp;: environ 3&nbsp;s par kilomètre. Il suffit de compter les secondes et de <b>diviser par 3</b> pour obtenir la distance en kilomètres.</p>
</div>
</details>

<div class="nt-lab" id="lab-orage">
<p class="nt-tag"><i class="fa-solid fa-cloud-bolt"></i>Animation</p>
<p class="nt-lab-title">À quelle distance est l'orage&nbsp;?</p>
<canvas role="img" aria-label="Paysage de nuit sous l'orage : un éclair apparaît, puis le tonnerre arrive après un certain délai."></canvas>
<p class="nt-chrono" aria-live="off"><span class="out-chrono">0,0</span><small>s</small></p>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="eclair"><i class="fa-solid fa-bolt"></i>&nbsp; Un éclair&nbsp;!</button><label class="nt-check"><input type="checkbox" data-in="son" checked> Son du tonnerre</label></div>
<div class="nt-tr-ans" hidden><span class="nt-champ"><label for="orage-rep">Distance&nbsp;:</label><input id="orage-rep" type="text" inputmode="decimal"><span class="nt-u">km</span></span><button type="button" class="nt-btn" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
<p class="nt-msg" aria-live="polite">Déclenchez un éclair&nbsp;: le chronomètre part avec l'éclair et s'arrête quand le tonnerre arrive.</p>
</div>

<div class="nt-lab nt-trainer" id="tr-vitesse">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Vitesse, distance, durée et conversions</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<div class="nt-qvis" aria-live="polite"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-ans"><span class="nt-champ"><label for="trv-rep">Réponse&nbsp;:</label><input id="trv-rep" type="text" inputmode="decimal"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>

### Mesurer la vitesse du son {.nt-h3}

<p>Pour mesurer la vitesse du son au laboratoire, on mesure la durée que met un son bref pour parcourir une distance connue. Les durées en jeu sont très courtes (quelques millisecondes pour un mètre), bien trop courtes pour un chronomètre manuel&nbsp;: on confie la mesure à deux microphones reliés à une interface d'acquisition.</p>

<div class="nt-b nt-proto nt-sans-ece">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Protocole</p>
<ol class="nt-steps">
<li><p>Placer deux microphones <span class="nt-must">alignés avec la source</span>, à une distance $d$ l'un de l'autre, et les relier aux deux voies d'une interface d'acquisition (ou d'un oscilloscope).</p><p class="nt-ece">Mesurer $d$ entre les deux membranes au mètre ruban, et la prendre la plus grande possible (au moins un mètre)&nbsp;: l'erreur relative de mesure est alors plus petite.</p></li>
<li><p>Régler l'acquisition pour qu'elle se déclenche sur le signal du premier microphone, avec une durée d'enregistrement de quelques dizaines de millisecondes.</p></li>
<li><p>Produire un son bref (claquement de mains, deux règles frappées l'une contre l'autre) <span class="nt-must">du côté du premier microphone</span>.</p></li>
<li><p>Mesurer le décalage $\Delta t$ entre le début des deux signaux, puis calculer $v = \dfrac{d}{\Delta t}$.</p><p class="nt-ece">Repérer le début de chaque signal au même endroit (premier pic, par exemple)&nbsp;; recommencer la mesure plusieurs fois et faire la moyenne.</p></li>
</ol>
</div>

<div class="nt-lab" id="lab-micros">
<p class="nt-tag"><i class="fa-solid fa-microphone"></i>Expérience simulée</p>
<p class="nt-lab-title">Deux microphones, un claquement</p>
<canvas class="nt-drag" tabindex="0" role="img" aria-label="En haut, une source et deux microphones ; en bas, les deux signaux enregistrés, décalés dans le temps. Deux curseurs verticaux permettent de mesurer le décalage."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Distance entre les microphones&nbsp;: <b class="out-d"></b><input type="range" min="0.5" max="3" step="0.1" value="1.5" data-in="d"></label></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="clap"><i class="fa-solid fa-hands-clapping"></i>&nbsp; Claquer des mains</button></div>
<div class="nt-tr-ans" hidden><span class="nt-champ"><label for="mic-rep">$v$&nbsp;=</label><input id="mic-rep" type="text" inputmode="decimal"><span class="nt-u">m/s</span></span><button type="button" class="nt-btn" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
<p class="nt-msg" aria-live="polite">Claquez des mains, puis faites glisser les deux curseurs (ou utilisez les flèches du clavier, avec Maj pour le second curseur) pour mesurer le décalage.</p>
</div>

### La caisse de résonance {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Pour augmenter l'intensité du son émis, beaucoup d'instruments et d'êtres vivants sont dotés d'une <span class="imp nt-hole">caisse de résonance</span>, qui <span class="imp nt-hole">amplifie</span> et <span class="imp nt-hole">sélectionne</span> les sons.</p>
</div>

<p>Une corde de guitare tendue seule ne met en mouvement que très peu d'air&nbsp;: on l'entend à peine. Fixée sur la caisse de la guitare, elle fait vibrer la grande table d'harmonie et l'air contenu dans la caisse, qui transmettent la vibration à une bien plus grande quantité d'air extérieur&nbsp;: le son devient beaucoup plus fort. La caisse vibre aussi plus facilement à certaines fréquences qu'à d'autres&nbsp;: elle renforce certains sons plus que d'autres, ce qui participe à la «&nbsp;couleur&nbsp;» du son de chaque instrument.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li>Instruments&nbsp;: caisse de la guitare et du violon, fût du tambour, tuyau de la flûte, boîte en bois sur laquelle on monte un diapason.</li>
<li>Êtres vivants&nbsp;: sac vocal gonflé de certaines grenouilles, gorge et bouche chez l'être humain (qui renforcent les sons produits par les cordes vocales), poches aériennes des singes hurleurs.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La caisse de résonance ne fabrique pas d'énergie</span></summary>
<div class="nt-d-body">
<p>Le mot «&nbsp;amplifier&nbsp;» peut tromper&nbsp;: la caisse de résonance n'ajoute aucune énergie, contrairement à un amplificateur électrique branché sur le secteur. Elle permet seulement à l'objet vibrant de <b>céder plus vite son énergie</b> à l'air. Conséquence étonnante&nbsp;: un diapason posé sur sa caisse sonne beaucoup plus fort, mais s'arrête plus tôt que le même diapason tenu à la main.</p>
<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 640 236' role='img' aria-label="Signal d'un diapason frappé : tenu à la main, faible amplitude mais son qui dure longtemps ; posé sur sa caisse, grande amplitude mais son qui s'éteint plus vite."><line x1='40' y1='62' x2='608' y2='62' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><polygon points='614,62 607,65 607,59' fill='#CBD5E1'/><text x='606' y='78' font-size='12' text-anchor='middle' fill='#64748B' font-family='Georgia, "Times New Roman", serif' font-style="italic">t</text><path d='M40,62 L41,57.1 L42,52.8 L43,49.7 L44,48.2 L45,48.4 L46,50.4 L47,53.9 L48,58.3 L49,63.2 L50,68 L51,71.9 L52,74.6 L53,75.7 L54,75 L55,72.6 L56,69 L57,64.4 L58,59.6 L59,55.1 L60,51.5 L61,49.2 L62,48.6 L63,49.7 L64,52.4 L65,56.2 L66,60.8 L67,65.5 L68,69.8 L69,73 L70,74.8 L71,75 L72,73.5 L73,70.6 L74,66.6 L75,62 L76,57.4 L77,53.5 L78,50.6 L79,49.2 L80,49.4 L81,51.3 L82,54.5 L83,58.6 L84,63.1 L85,67.5 L86,71.2 L87,73.7 L88,74.6 L89,74 L90,71.8 L91,68.4 L92,64.2 L93,59.8 L94,55.6 L95,52.3 L96,50.2 L97,49.6 L98,50.6 L99,53.1 L100,56.7 L101,60.9 L102,65.3 L103,69.2 L104,72.2 L105,73.9 L106,74 L107,72.7 L108,70 L109,66.2 L110,62 L111,57.8 L112,54.1 L113,51.5 L114,50.2 L115,50.4 L116,52.1 L117,55 L118,58.9 L119,63.1 L120,67.1 L121,70.5 L122,72.8 L123,73.7 L124,73.1 L125,71.1 L126,68 L127,64.1 L128,59.9 L129,56.1 L130,53 L131,51.1 L132,50.5 L133,51.5 L134,53.7 L135,57.1 L136,61 L137,65 L138,68.6 L139,71.4 L140,73 L141,73.1 L142,71.9 L143,69.4 L144,65.9 L145,62 L146,58.1 L147,54.7 L148,52.3 L149,51.1 L150,51.3 L151,52.8 L152,55.6 L153,59.1 L154,63 L155,66.7 L156,69.9 L157,72 L158,72.8 L159,72.3 L160,70.4 L161,67.5 L162,63.9 L163,60.1 L164,56.5 L165,53.7 L166,51.9 L167,51.4 L168,52.3 L169,54.4 L170,57.4 L171,61.1 L172,64.8 L173,68.2 L174,70.7 L175,72.2 L176,72.3 L177,71.1 L178,68.8 L179,65.6 L180,62 L181,58.4 L182,55.3 L183,53 L184,51.9 L185,52.1 L186,53.5 L187,56 L188,59.3 L189,62.9 L190,66.4 L191,69.3 L192,71.2 L193,72 L194,71.5 L195,69.8 L196,67.1 L197,63.8 L198,60.2 L199,56.9 L200,54.3 L201,52.7 L202,52.2 L203,53 L204,54.9 L205,57.8 L206,61.1 L207,64.6 L208,67.7 L209,70.1 L210,71.4 L211,71.5 L212,70.4 L213,68.3 L214,65.4 L215,62 L216,58.7 L217,55.8 L218,53.7 L219,52.6 L220,52.8 L221,54.2 L222,56.5 L223,59.5 L224,62.8 L225,66 L226,68.7 L227,70.5 L228,71.2 L229,70.8 L230,69.2 L231,66.7 L232,63.6 L233,60.4 L234,57.3 L235,54.9 L236,53.4 L237,52.9 L238,53.7 L239,55.5 L240,58.1 L241,61.2 L242,64.4 L243,67.3 L244,69.5 L245,70.7 L246,70.8 L247,69.8 L248,67.8 L249,65.1 L250,62 L251,58.9 L252,56.2 L253,54.3 L254,53.3 L255,53.5 L256,54.7 L257,56.9 L258,59.7 L259,62.8 L260,65.7 L261,68.2 L262,69.9 L263,70.6 L264,70.1 L265,68.7 L266,66.4 L267,63.5 L268,60.5 L269,57.7 L270,55.4 L271,54 L272,53.6 L273,54.3 L274,56 L275,58.4 L276,61.3 L277,64.2 L278,66.9 L279,68.9 L280,70 L281,70.1 L282,69.2 L283,67.4 L284,64.9 L285,62 L286,59.1 L287,56.7 L288,54.9 L289,54 L290,54.1 L291,55.3 L292,57.3 L293,59.9 L294,62.7 L295,65.5 L296,67.7 L297,69.3 L298,69.9 L299,69.5 L300,68.2 L301,66 L302,63.4 L303,60.6 L304,58 L305,55.9 L306,54.6 L307,54.2 L308,54.9 L309,56.4 L310,58.7 L311,61.3 L312,64 L313,66.5 L314,68.4 L315,69.4 L316,69.5 L317,68.7 L318,67 L319,64.7 L320,62 L321,59.4 L322,57.1 L323,55.4 L324,54.6 L325,54.7 L326,55.8 L327,57.6 L328,60 L329,62.7 L330,65.2 L331,67.3 L332,68.7 L333,69.3 L334,68.9 L335,67.7 L336,65.7 L337,63.3 L338,60.7 L339,58.3 L340,56.4 L341,55.2 L342,54.8 L343,55.4 L344,56.8 L345,58.9 L346,61.4 L347,63.9 L348,66.2 L349,67.9 L350,68.9 L351,69 L352,68.2 L353,66.6 L354,64.5 L355,62 L356,59.6 L357,57.4 L358,55.9 L359,55.2 L360,55.3 L361,56.3 L362,58 L363,60.2 L364,62.6 L365,65 L366,66.9 L367,68.2 L368,68.8 L369,68.4 L370,67.3 L371,65.4 L372,63.2 L373,60.8 L374,58.6 L375,56.8 L376,55.7 L377,55.4 L378,55.9 L379,57.2 L380,59.1 L381,61.4 L382,63.7 L383,65.8 L384,67.5 L385,68.4 L386,68.4 L387,67.7 L388,66.3 L389,64.3 L390,62 L391,59.7 L392,57.8 L393,56.4 L394,55.7 L395,55.8 L396,56.7 L397,58.3 L398,60.3 L399,62.6 L400,64.7 L401,66.5 L402,67.8 L403,68.3 L404,67.9 L405,66.9 L406,65.2 L407,63.1 L408,60.9 L409,58.8 L410,57.2 L411,56.1 L412,55.9 L413,56.4 L414,57.6 L415,59.4 L416,61.5 L417,63.6 L418,65.6 L419,67 L420,67.9 L421,68 L422,67.3 L423,65.9 L424,64.1 L425,62 L426,59.9 L427,58.1 L428,56.8 L429,56.1 L430,56.3 L431,57.1 L432,58.6 L433,60.4 L434,62.5 L435,64.5 L436,66.2 L437,67.3 L438,67.8 L439,67.5 L440,66.5 L441,65 L442,63 L443,61 L444,59.1 L445,57.5 L446,56.6 L447,56.3 L448,56.8 L449,57.9 L450,59.6 L451,61.5 L452,63.5 L453,65.3 L454,66.7 L455,67.4 L456,67.5 L457,66.9 L458,65.6 L459,63.9 L460,62 L461,60.1 L462,58.4 L463,57.2 L464,56.6 L465,56.7 L466,57.5 L467,58.8 L468,60.6 L469,62.5 L470,64.3 L471,65.9 L472,66.9 L473,67.4 L474,67.1 L475,66.2 L476,64.7 L477,62.9 L478,61.1 L479,59.3 L480,57.9 L481,57 L482,56.8 L483,57.2 L484,58.2 L485,59.7 L486,61.5 L487,63.4 L488,65 L489,66.3 L490,67 L491,67.1 L492,66.5 L493,65.4 L494,63.8 L495,62 L496,60.2 L497,58.7 L498,57.5 L499,57 L500,57.1 L501,57.8 L502,59 L503,60.7 L504,62.4 L505,64.2 L506,65.6 L507,66.6 L508,66.9 L509,66.7 L510,65.9 L511,64.5 L512,62.9 L513,61.1 L514,59.5 L515,58.2 L516,57.4 L517,57.1 L518,57.5 L519,58.5 L520,59.9 L521,61.6 L522,63.3 L523,64.8 L524,66 L525,66.6 L526,66.7 L527,66.2 L528,65.1 L529,63.7 L530,62 L531,60.3 L532,58.9 L533,57.9 L534,57.4 L535,57.5 L536,58.1 L537,59.3 L538,60.8 L539,62.4 L540,64 L541,65.3 L542,66.2 L543,66.6 L544,66.3 L545,65.6 L546,64.3 L547,62.8 L548,61.2 L549,59.7 L550,58.5 L551,57.7 L552,57.5 L553,57.9 L554,58.8 L555,60.1 L556,61.6 L557,63.2 L558,64.6 L559,65.7 L560,66.3 L561,66.4 L562,65.9 L563,64.9 L564,63.5 L565,62 L566,60.5 L567,59.1 L568,58.2 L569,57.7 L570,57.8 L571,58.4 L572,59.5 L573,60.9 L574,62.4 L575,63.9 L576,65.1 L577,65.9 L578,66.2 L579,66 L580,65.3 L581,64.2 L582,62.7 L583,61.3 L584,59.9 L585,58.7 L586,58 L587,57.9 L588,58.2 L589,59 L590,60.2 L591,61.6 L592,63.1 L593,64.4 L594,65.4 L595,66 L596,66 L597,65.6 L598,64.7 L599,63.4 L600,62' fill='none' stroke='#2A6BC4' stroke-width='1' stroke-linejoin='round' stroke-linecap='round'/><path d='M40,47.9 L44,48 L48,48.2 L52,48.3 L56,48.4 L60,48.5 L64,48.7 L68,48.8 L72,48.9 L76,49 L80,49.1 L84,49.2 L88,49.4 L92,49.5 L96,49.6 L100,49.7 L104,49.8 L108,49.9 L112,50 L116,50.1 L120,50.2 L124,50.3 L128,50.4 L132,50.5 L136,50.6 L140,50.7 L144,50.8 L148,50.9 L152,51 L156,51.1 L160,51.2 L164,51.3 L168,51.4 L172,51.5 L176,51.6 L180,51.7 L184,51.8 L188,51.9 L192,52 L196,52.1 L200,52.1 L204,52.2 L208,52.3 L212,52.4 L216,52.5 L220,52.6 L224,52.7 L228,52.7 L232,52.8 L236,52.9 L240,53 L244,53.1 L248,53.1 L252,53.2 L256,53.3 L260,53.4 L264,53.5 L268,53.5 L272,53.6 L276,53.7 L280,53.8 L284,53.8 L288,53.9 L292,54 L296,54 L300,54.1 L304,54.2 L308,54.3 L312,54.3 L316,54.4 L320,54.5 L324,54.5 L328,54.6 L332,54.7 L336,54.7 L340,54.8 L344,54.9 L348,54.9 L352,55 L356,55 L360,55.1 L364,55.2 L368,55.2 L372,55.3 L376,55.3 L380,55.4 L384,55.5 L388,55.5 L392,55.6 L396,55.6 L400,55.7 L404,55.8 L408,55.8 L412,55.9 L416,55.9 L420,56 L424,56 L428,56.1 L432,56.1 L436,56.2 L440,56.2 L444,56.3 L448,56.3 L452,56.4 L456,56.4 L460,56.5 L464,56.5 L468,56.6 L472,56.6 L476,56.7 L480,56.7 L484,56.8 L488,56.8 L492,56.9 L496,56.9 L500,57 L504,57 L508,57 L512,57.1 L516,57.1 L520,57.2 L524,57.2 L528,57.3 L532,57.3 L536,57.3 L540,57.4 L544,57.4 L548,57.5 L552,57.5 L556,57.5 L560,57.6 L564,57.6 L568,57.7 L572,57.7 L576,57.7 L580,57.8 L584,57.8 L588,57.9 L592,57.9 L596,57.9 L600,58' fill='none' stroke='#2A6BC4' stroke-width='1' stroke-dasharray='4 3' stroke-linejoin='round' stroke-linecap='round'/><text x='40' y='10' font-size='13' text-anchor='start' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>diapason tenu à la main</text><line x1='40' y1='174' x2='608' y2='174' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><polygon points='614,174 607,177 607,171' fill='#CBD5E1'/><text x='606' y='190' font-size='12' text-anchor='middle' fill='#64748B' font-family='Georgia, "Times New Roman", serif' font-style="italic">t</text><path d='M40,174 L41,159.4 L42,146.9 L43,138.1 L44,133.9 L45,134.8 L46,140.7 L47,150.8 L48,163.6 L49,177.5 L50,190.8 L51,201.7 L52,208.9 L53,211.7 L54,209.6 L55,203 L56,192.9 L57,180.5 L58,167.5 L59,155.6 L60,146.1 L61,140.3 L62,138.9 L63,142 L64,149 L65,159.1 L66,171 L67,183 L68,193.7 L69,201.7 L70,206.1 L71,206.4 L72,202.6 L73,195.2 L74,185.2 L75,174 L76,163 L77,153.5 L78,146.8 L79,143.6 L80,144.3 L81,148.8 L82,156.4 L83,166.1 L84,176.6 L85,186.7 L86,195 L87,200.5 L88,202.5 L89,200.9 L90,196 L91,188.3 L92,178.9 L93,169.1 L94,160 L95,152.9 L96,148.5 L97,147.4 L98,149.7 L99,155.1 L100,162.7 L101,171.7 L102,180.8 L103,188.9 L104,195 L105,198.3 L106,198.5 L107,195.6 L108,190 L109,182.5 L110,174 L111,165.6 L112,158.5 L113,153.4 L114,151 L115,151.5 L116,154.9 L117,160.7 L118,168 L119,176 L120,183.6 L121,189.9 L122,194 L123,195.6 L124,194.4 L125,190.6 L126,184.8 L127,177.7 L128,170.3 L129,163.4 L130,158 L131,154.7 L132,153.9 L133,155.6 L134,159.7 L135,165.5 L136,172.3 L137,179.1 L138,185.3 L139,189.9 L140,192.4 L141,192.6 L142,190.4 L143,186.1 L144,180.4 L145,174 L146,167.7 L147,162.2 L148,158.4 L149,156.6 L150,157 L151,159.5 L152,163.9 L153,169.5 L154,175.5 L155,181.3 L156,186 L157,189.2 L158,190.4 L159,189.5 L160,186.6 L161,182.2 L162,176.8 L163,171.2 L164,166 L165,161.9 L166,159.4 L167,158.8 L168,160.1 L169,163.1 L170,167.5 L171,172.7 L172,177.9 L173,182.6 L174,186 L175,188 L176,188.1 L177,186.4 L178,183.2 L179,178.9 L180,174 L181,169.2 L182,165.1 L183,162.2 L184,160.8 L185,161.1 L186,163.1 L187,166.3 L188,170.6 L189,175.1 L190,179.5 L191,183.1 L192,185.5 L193,186.4 L194,185.7 L195,183.6 L196,180.2 L197,176.1 L198,171.9 L199,167.9 L200,164.8 L201,162.9 L202,162.5 L203,163.5 L204,165.8 L205,169.1 L206,173 L207,177 L208,180.5 L209,183.1 L210,184.6 L211,184.7 L212,183.4 L213,181 L214,177.7 L215,174 L216,170.4 L217,167.3 L218,165 L219,164 L220,164.2 L221,165.7 L222,168.2 L223,171.4 L224,174.9 L225,178.2 L226,180.9 L227,182.7 L228,183.4 L229,182.9 L230,181.2 L231,178.7 L232,175.6 L233,172.4 L234,169.4 L235,167 L236,165.6 L237,165.3 L238,166 L239,167.8 L240,170.3 L241,173.2 L242,176.2 L243,178.9 L244,180.9 L245,182 L246,182.1 L247,181.1 L248,179.3 L249,176.8 L250,174 L251,171.2 L252,168.9 L253,167.2 L254,166.4 L255,166.6 L256,167.7 L257,169.6 L258,172 L259,174.7 L260,177.2 L261,179.2 L262,180.6 L263,181.1 L264,180.7 L265,179.5 L266,177.6 L267,175.2 L268,172.8 L269,170.5 L270,168.7 L271,167.6 L272,167.4 L273,168 L274,169.3 L275,171.2 L276,173.4 L277,175.7 L278,177.7 L279,179.2 L280,180.1 L281,180.1 L282,179.4 L283,178 L284,176.1 L285,174 L286,171.9 L287,170.1 L288,168.9 L289,168.3 L290,168.4 L291,169.2 L292,170.7 L293,172.5 L294,174.5 L295,176.4 L296,178 L297,179 L298,179.4 L299,179.1 L300,178.2 L301,176.7 L302,174.9 L303,173.1 L304,171.4 L305,170 L306,169.2 L307,169 L308,169.4 L309,170.4 L310,171.9 L311,173.6 L312,175.3 L313,176.8 L314,178 L315,178.6 L316,178.6 L317,178.1 L318,177 L319,175.6 L320,174 L321,172.4 L322,171.1 L323,170.1 L324,169.7 L325,169.8 L326,170.4 L327,171.5 L328,172.9 L329,174.4 L330,175.8 L331,177 L332,177.8 L333,178.1 L334,177.9 L335,177.1 L336,176 L337,174.7 L338,173.3 L339,172 L340,171 L341,170.4 L342,170.2 L343,170.5 L344,171.3 L345,172.4 L346,173.7 L347,175 L348,176.1 L349,177 L350,177.5 L351,177.5 L352,177.1 L353,176.3 L354,175.2 L355,174 L356,172.8 L357,171.8 L358,171 L359,170.7 L360,170.8 L361,171.3 L362,172.1 L363,173.1 L364,174.3 L365,175.4 L366,176.3 L367,176.9 L368,177.1 L369,176.9 L370,176.4 L371,175.5 L372,174.5 L373,173.5 L374,172.5 L375,171.7 L376,171.2 L377,171.1 L378,171.4 L379,172 L380,172.8 L381,173.7 L382,174.7 L383,175.6 L384,176.3 L385,176.6 L386,176.7 L387,176.3 L388,175.7 L389,174.9 L390,174 L391,173.1 L392,172.3 L393,171.8 L394,171.5 L395,171.6 L396,171.9 L397,172.6 L398,173.4 L399,174.2 L400,175 L401,175.7 L402,176.2 L403,176.3 L404,176.2 L405,175.8 L406,175.2 L407,174.4 L408,173.6 L409,172.9 L410,172.3 L411,171.9 L412,171.8 L413,172 L414,172.4 L415,173.1 L416,173.8 L417,174.6 L418,175.2 L419,175.7 L420,176 L421,176 L422,175.8 L423,175.3 L424,174.7 L425,174 L426,173.3 L427,172.7 L428,172.3 L429,172.1 L430,172.2 L431,172.4 L432,172.9 L433,173.5 L434,174.2 L435,174.8 L436,175.3 L437,175.6 L438,175.8 L439,175.7 L440,175.4 L441,174.9 L442,174.3 L443,173.7 L444,173.1 L445,172.7 L446,172.4 L447,172.3 L448,172.5 L449,172.8 L450,173.3 L451,173.9 L452,174.4 L453,174.9 L454,175.3 L455,175.5 L456,175.5 L457,175.3 L458,175 L459,174.5 L460,174 L461,173.5 L462,173 L463,172.7 L464,172.6 L465,172.6 L466,172.8 L467,173.2 L468,173.6 L469,174.1 L470,174.6 L471,175 L472,175.2 L473,175.3 L474,175.3 L475,175 L476,174.7 L477,174.2 L478,173.8 L479,173.3 L480,173 L481,172.8 L482,172.7 L483,172.9 L484,173.1 L485,173.5 L486,173.9 L487,174.3 L488,174.7 L489,175 L490,175.1 L491,175.2 L492,175 L493,174.8 L494,174.4 L495,174 L496,173.6 L497,173.3 L498,173 L499,172.9 L500,172.9 L501,173.1 L502,173.4 L503,173.7 L504,174.1 L505,174.5 L506,174.7 L507,174.9 L508,175 L509,175 L510,174.8 L511,174.5 L512,174.2 L513,173.8 L514,173.5 L515,173.2 L516,173.1 L517,173.1 L518,173.1 L519,173.3 L520,173.6 L521,173.9 L522,174.2 L523,174.5 L524,174.7 L525,174.9 L526,174.9 L527,174.8 L528,174.6 L529,174.3 L530,174 L531,173.7 L532,173.4 L533,173.3 L534,173.2 L535,173.2 L536,173.3 L537,173.5 L538,173.8 L539,174.1 L540,174.3 L541,174.6 L542,174.7 L543,174.8 L544,174.7 L545,174.6 L546,174.4 L547,174.1 L548,173.9 L549,173.6 L550,173.4 L551,173.3 L552,173.3 L553,173.3 L554,173.5 L555,173.7 L556,173.9 L557,174.2 L558,174.4 L559,174.6 L560,174.7 L561,174.7 L562,174.6 L563,174.4 L564,174.2 L565,174 L566,173.8 L567,173.6 L568,173.4 L569,173.4 L570,173.4 L571,173.5 L572,173.6 L573,173.8 L574,174.1 L575,174.3 L576,174.4 L577,174.5 L578,174.6 L579,174.6 L580,174.4 L581,174.3 L582,174.1 L583,173.9 L584,173.7 L585,173.6 L586,173.5 L587,173.5 L588,173.5 L589,173.6 L590,173.8 L591,174 L592,174.1 L593,174.3 L594,174.4 L595,174.5 L596,174.5 L597,174.4 L598,174.3 L599,174.2 L600,174' fill='none' stroke='#D97706' stroke-width='1' stroke-linejoin='round' stroke-linecap='round'/><path d='M40,132.2 L44,133.5 L48,134.8 L52,136 L56,137.2 L60,138.3 L64,139.4 L68,140.5 L72,141.6 L76,142.6 L80,143.6 L84,144.5 L88,145.4 L92,146.3 L96,147.2 L100,148 L104,148.8 L108,149.6 L112,150.4 L116,151.1 L120,151.8 L124,152.5 L128,153.2 L132,153.9 L136,154.5 L140,155.1 L144,155.7 L148,156.3 L152,156.8 L156,157.4 L160,157.9 L164,158.4 L168,158.9 L172,159.3 L176,159.8 L180,160.2 L184,160.7 L188,161.1 L192,161.5 L196,161.9 L200,162.3 L204,162.6 L208,163 L212,163.3 L216,163.7 L220,164 L224,164.3 L228,164.6 L232,164.9 L236,165.2 L240,165.5 L244,165.7 L248,166 L252,166.2 L256,166.5 L260,166.7 L264,166.9 L268,167.2 L272,167.4 L276,167.6 L280,167.8 L284,168 L288,168.2 L292,168.3 L296,168.5 L300,168.7 L304,168.9 L308,169 L312,169.2 L316,169.3 L320,169.5 L324,169.6 L328,169.7 L332,169.9 L336,170 L340,170.1 L344,170.3 L348,170.4 L352,170.5 L356,170.6 L360,170.7 L364,170.8 L368,170.9 L372,171 L376,171.1 L380,171.2 L384,171.3 L388,171.4 L392,171.4 L396,171.5 L400,171.6 L404,171.7 L408,171.7 L412,171.8 L416,171.9 L420,172 L424,172 L428,172.1 L432,172.1 L436,172.2 L440,172.3 L444,172.3 L448,172.4 L452,172.4 L456,172.5 L460,172.5 L464,172.6 L468,172.6 L472,172.6 L476,172.7 L480,172.7 L484,172.8 L488,172.8 L492,172.8 L496,172.9 L500,172.9 L504,172.9 L508,173 L512,173 L516,173 L520,173.1 L524,173.1 L528,173.1 L532,173.2 L536,173.2 L540,173.2 L544,173.2 L548,173.3 L552,173.3 L556,173.3 L560,173.3 L564,173.3 L568,173.4 L572,173.4 L576,173.4 L580,173.4 L584,173.4 L588,173.5 L592,173.5 L596,173.5 L600,173.5' fill='none' stroke='#D97706' stroke-width='1' stroke-dasharray='4 3' stroke-linejoin='round' stroke-linecap='round'/><text x='40' y='122' font-size='13' text-anchor='start' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>diapason posé sur sa caisse</text></svg></div>
<p class="nt-cap">Allure du signal d'un diapason frappé de la même façon, tenu à la main ou posé sur sa caisse.</p>
</div>
</details>

## Signal sonore périodique {.nt-h2}

### Visualiser un son {.nt-h3}

<p>Un son est trop rapide pour être observé à l'œil nu. Pour l'étudier, on utilise une <b>chaîne de mesure</b>&nbsp;: un <b>microphone</b> (le capteur) convertit la vibration de l'air en une tension électrique qui varie au même rythme&nbsp;; une interface d'acquisition reliée à un ordinateur (ou un oscilloscope, ou simplement un smartphone avec une application comme phyphox ou FizziQ) affiche alors cette tension en fonction du temps.</p>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 720 208' role='img' aria-label="Chaîne de mesure : une source sonore fait vibrer l'air, un microphone convertit cette vibration en tension électrique, une interface d'acquisition et un ordinateur affichent la représentation temporelle."><rect x='28' y='118' width='96' height='26' rx='3' fill='#F5E6CC' stroke='#B45309' stroke-width='1'/><path d='M76,118 L76,100' fill='none' stroke='#475569' stroke-width='3' stroke-linejoin='round' stroke-linecap='round'/><path d='M64,40 L64,86 Q64,100 76,100 Q88,100 88,86 L88,40' fill='none' stroke='#475569' stroke-width='4' stroke-linecap='round'/><path d='M122.2,56.4 A26,26 0 0 1 122.2,83.6' fill='none' stroke='#458EEC' stroke-width='1.4' opacity='1.0'/><path d='M134.1,49.1 A40,40 0 0 1 134.1,90.9' fill='none' stroke='#458EEC' stroke-width='1.4' opacity='0.78'/><path d='M146,41.8 A54,54 0 0 1 146,98.2' fill='none' stroke='#458EEC' stroke-width='1.4' opacity='0.56'/><rect x='178' y='52' width='44' height='30' rx='15' fill='#E2E8F0' stroke='#1E293B' stroke-width='1.2'/><line x1='186' y1='58' x2='186' y2='76' stroke='#64748B' stroke-width='0.8' stroke-linecap='round'/><line x1='195' y1='58' x2='195' y2='76' stroke='#64748B' stroke-width='0.8' stroke-linecap='round'/><line x1='204' y1='58' x2='204' y2='76' stroke='#64748B' stroke-width='0.8' stroke-linecap='round'/><line x1='213' y1='58' x2='213' y2='76' stroke='#64748B' stroke-width='0.8' stroke-linecap='round'/><path d='M222,67 L232,67' fill='none' stroke='#1E293B' stroke-width='1.2' stroke-linejoin='round' stroke-linecap='round'/><path d='M200,82 L200,140' fill='none' stroke='#1E293B' stroke-width='1.4' stroke-linejoin='round' stroke-linecap='round'/><path d='M184,144 L216,144' fill='none' stroke='#1E293B' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/><path d='M232,67 C270,67 268,112 312,112' fill='none' stroke='#64748B' stroke-width='1.4'/><rect x='312' y='94' width='96' height='40' rx='6' fill='#F8FAFC' stroke='#1E293B' stroke-width='1.2'/><circle cx='328' cy='114' r='5' fill='#fff' stroke='#1E293B' stroke-width='1'/><circle cx='346' cy='114' r='5' fill='#fff' stroke='#1E293B' stroke-width='1'/><rect x='362' y='106' width='36' height='16' rx='2' fill='#DCFCE7' stroke='#059669' stroke-width='0.8'/><path d='M408,114 C440,114 440,128 482,128' fill='none' stroke='#64748B' stroke-width='1.4'/><rect x='488' y='28' width='196' height='116' rx='6' fill='#12305A'/><rect x='496' y='36' width='180' height='100' rx='2' fill='#FFFFFF'/><path d='M470,148 L702,148 L692,156 L480,156 Z' fill='#CBD5E1' stroke='#1E293B' stroke-width='1' stroke-linejoin='round' stroke-linecap='round'/><line x1='526' y1='36' x2='526' y2='136' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='556' y1='36' x2='556' y2='136' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='586' y1='36' x2='586' y2='136' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='616' y1='36' x2='616' y2='136' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='646' y1='36' x2='646' y2='136' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='496' y1='61' x2='676' y2='61' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='496' y1='86' x2='676' y2='86' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='496' y1='111' x2='676' y2='111' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><path d='M496,77.3 L497,73.6 L498,70.8 L499,68.8 L500,67.7 L501,67.3 L502,67.6 L503,68.4 L504,69.5 L505,70.7 L506,71.9 L507,72.8 L508,73.6 L509,74 L510,74.2 L511,74.3 L512,74.2 L513,74.1 L514,74.2 L515,74.4 L516,75 L517,75.8 L518,76.9 L519,78.3 L520,79.8 L521,81.3 L522,82.9 L523,84.3 L524,85.5 L525,86.5 L526,87.2 L527,87.7 L528,88.2 L529,88.6 L530,89.2 L531,90.1 L532,91.2 L533,92.9 L534,95 L535,97.5 L536,100.3 L537,103.3 L538,106.3 L539,109.1 L540,111.4 L541,113.1 L542,113.9 L543,113.7 L544,112.4 L545,110.1 L546,106.8 L547,102.7 L548,98 L549,92.9 L550,87.7 L551,82.8 L552,78.3 L553,74.4 L554,71.4 L555,69.2 L556,67.9 L557,67.4 L558,67.5 L559,68.2 L560,69.2 L561,70.4 L562,71.6 L563,72.6 L564,73.4 L565,73.9 L566,74.2 L567,74.3 L568,74.2 L569,74.1 L570,74.1 L571,74.3 L572,74.8 L573,75.5 L574,76.6 L575,77.9 L576,79.4 L577,80.9 L578,82.5 L579,83.9 L580,85.2 L581,86.2 L582,87 L583,87.6 L584,88.1 L585,88.5 L586,89.1 L587,89.8 L588,90.9 L589,92.4 L590,94.4 L591,96.8 L592,99.6 L593,102.5 L594,105.6 L595,108.4 L596,110.9 L597,112.7 L598,113.8 L599,113.8 L600,112.8 L601,110.8 L602,107.7 L603,103.8 L604,99.2 L605,94.2 L606,89 L607,84 L608,79.4 L609,75.3 L610,72.1 L611,69.7 L612,68.1 L613,67.4 L614,67.4 L615,68 L616,69 L617,70.1 L618,71.3 L619,72.4 L620,73.2 L621,73.8 L622,74.2 L623,74.3 L624,74.2 L625,74.1 L626,74.1 L627,74.3 L628,74.7 L629,75.3 L630,76.3 L631,77.6 L632,79 L633,80.6 L634,82.1 L635,83.6 L636,84.9 L637,86 L638,86.9 L639,87.5 L640,88 L641,88.4 L642,88.9 L643,89.6 L644,90.6 L645,92 L646,93.9 L647,96.2 L648,98.8 L649,101.8 L650,104.8 L651,107.8 L652,110.3 L653,112.3 L654,113.6 L655,113.9 L656,113.2 L657,111.4 L658,108.5 L659,104.8 L660,100.4 L661,95.4 L662,90.3 L663,85.2 L664,80.5 L665,76.3 L666,72.8 L667,70.2 L668,68.4 L669,67.5 L670,67.4 L671,67.8 L672,68.7 L673,69.8 L674,71 L675,72.1 L676,73.1' fill='none' stroke='#2A6BC4' stroke-width='1.5' stroke-linejoin='round' stroke-linecap='round'/><text x='76' y='182' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>source</text><text x='76' y='199' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>sonore</text><text x='200' y='182' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>microphone</text><text x='200' y='199' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>(capteur)</text><text x='360' y='182' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>interface</text><text x='360' y='199' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>d’acquisition</text><text x='586' y='182' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>ordinateur</text><text x='586' y='199' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>ou smartphone</text></svg></div>
<p class="nt-cap">Le microphone convertit la vibration de l'air en une tension électrique&nbsp;; l'ordinateur affiche cette tension en fonction du temps.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La courbe qui donne le signal (ici la tension délivrée par le microphone) en fonction du temps s'appelle la <span class="imp nt-hole">représentation temporelle</span> du signal sonore.</p>
</div>

<p>C'est sur cette représentation que nous allons lire tout ce qui nous intéresse dans un son&nbsp;: la durée du motif qui se répète (la <b>période</b>), la <b>forme</b> de ce motif, et la hauteur de ses pics (l'<b>amplitude</b>). Nous verrons dans la partie suivante que chacune de ces trois grandeurs correspond à une caractéristique de ce que nous entendons.</p>

### Période {.nt-h3}

<p>Les sons musicaux sont des signaux <span class="imp">périodiques</span>.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Un <span class="imp nt-hole">signal périodique</span> est un signal qui se <span class="imp nt-hole">répète à l'identique dans le temps</span>.</p>
<p>La <span class="imp nt-hole">période</span> $T$ d'un signal périodique est la <span class="imp nt-hole">durée d'une répétition</span> (d'un motif). Unité&nbsp;: la <span class="imp nt-hole">seconde</span> (s).</p>
</div>

<div class="nt-lab" id="lab-motif">
<p class="nt-tag"><i class="fa-solid fa-wave-square"></i>Animation</p>
<p class="nt-lab-title">Périodique ou non&nbsp;?</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="motif-s" value="note" checked><span>Note de flûte</span></label><label><input type="radio" name="motif-s" value="bruit"><span>Souffle «&nbsp;chhh&nbsp;»</span></label></div></div>
<canvas role="img" aria-label="Représentation temporelle d'un son : tension en fonction du temps."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="motifs"><i class="fa-solid fa-layer-group"></i>&nbsp; Repérer les motifs</button><label class="nt-check"><input type="checkbox" data-in="piege"> Montrer le piège</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Pour mesurer une période, il faut repérer deux points <b>qui se correspondent</b> dans deux motifs successifs&nbsp;: même valeur <b>et</b> même évolution (le signal monte ou descend de la même façon). Deux points qui ont seulement la même valeur ne sont en général pas séparés d'une période.</p>
</div>

### Fréquence {.nt-h3}

<p>Pour des sons musicaux, la période est souvent très petite, de l'ordre du centième ou du millième de seconde. On lui préfère alors le <span class="imp">nombre de répétitions (de motifs) par seconde</span>, qui est l'inverse de la période et qu'on appelle la <span class="imp">fréquence</span>.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp nt-hole">fréquence</span> $f$ d'un signal périodique est le <span class="imp nt-hole">nombre de motifs par seconde</span>. Unité&nbsp;: le <span class="imp nt-hole">hertz</span> (Hz).</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$f = \dfrac{1}{T}$</p>
<div class="nt-f-units"><span>$f$&nbsp;: fréquence en <b>Hz</b></span><span>$T$&nbsp;: période en <b>s</b></span></div>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Le «&nbsp;la&nbsp;» du diapason a une fréquence $f = \pu{440 Hz}$&nbsp;: ses branches font 440 allers-retours par seconde. Sa période vaut $T = \dfrac{1}{f} = \dfrac{1}{\pu{440 Hz}} \approx \pu{0,00227 s}$, soit environ $\pu{2,27 ms}$.</p>
<p>Attention aux unités&nbsp;: pour obtenir des hertz, la période doit être en <b>secondes</b>. Avec $T = \pu{4 ms} = \pu{0,004 s}$, on trouve $f = \dfrac{1}{0,004} = \pu{250 Hz}$.</p>
</div>

<details class="nt-d nt-exd">
<summary><span class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</span><span class="nt-sum">Produire un son avec un microcontrôleur</span></summary>
<div class="nt-d-body">
<p>Un microcontrôleur (une carte Arduino, par exemple) peut produire un son très simplement. L'instruction <code>tone(8, 440)</code> lui fait basculer la tension de sa broche 8 entre 0&nbsp;V et 5&nbsp;V, 440 fois par seconde&nbsp;: c'est un signal en créneaux de fréquence 440&nbsp;Hz, donc de période $T = 1/440 \approx \pu{2,27 ms}$. Un petit haut-parleur (ou un buzzer) branché sur cette broche le transforme en son&nbsp;: on entend le la du diapason, avec un timbre beaucoup plus «&nbsp;nasillard&nbsp;», car la forme du signal est différente.</p>
<pre><code>void setup() {
  tone(8, 440);   // créneaux de fréquence 440 Hz sur la broche 8
}
void loop() {
}</code></pre>
<p>En remplaçant 440 par 880, on obtient le la de l'octave supérieure. On peut enregistrer ce signal avec un microphone et vérifier sa période sur la représentation temporelle.</p>
</div>
</details>

<p>Pour visualiser le lien entre période et fréquence, on peut manipuler cette <a href="https://www.geogebra.org/m/AFykFRzs" target="_blank" rel="noopener">appliquette GeoGebra</a>.</p>

<div class="nt-lab nt-trainer" id="tr-oscillo">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Mesurer une période sur un oscillogramme</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard nt-qcard-w">
<p class="nt-ql-q nt-tr-q"></p>
<canvas class="nt-drag" tabindex="0" role="img" aria-label="Oscillogramme d'un son périodique sur un quadrillage, avec deux curseurs verticaux déplaçables."></canvas>
<div class="nt-tr-ans"><span class="nt-champ"><label for="osc-T">$T$&nbsp;=</label><input id="osc-T" type="text" inputmode="decimal"><span class="nt-u">ms</span></span><span class="nt-champ"><label for="osc-f">$f$&nbsp;=</label><input id="osc-f" type="text" inputmode="decimal"><span class="nt-u">Hz</span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>
<p class="nt-cap">Faites glisser les curseurs (ou utilisez les flèches du clavier, avec Maj pour le second curseur). Mesurez plusieurs périodes d'un coup, puis divisez&nbsp;: c'est plus précis.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>À savoir</p>
<p>Pour mesurer précisément la période d'un phénomène qui se répète, on mesure la durée $\Delta t$ de <b>plusieurs</b> motifs, par exemple $n = 10$, puis on divise&nbsp;: $T = \dfrac{\Delta t}{n}$.</p>
<p>L'erreur commise en déclenchant et en arrêtant le chronomètre (le temps de réaction, environ 0,2&nbsp;s) est la même que l'on mesure 1 motif ou 10 motifs. Mais en divisant par 10, on divise aussi cette erreur par 10&nbsp;: la mesure est dix fois plus précise. C'est le même principe qu'avec un oscilloscope, où l'on mesure toujours plusieurs périodes d'un coup.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Quelles sont la période et la fréquence du signal lumineux ci-dessous&nbsp;? Chronométrez-le&nbsp;!</p>
</div>

<div class="nt-lab" id="lab-feu">
<p class="nt-tag"><i class="fa-solid fa-stopwatch"></i>Chronométrage</p>
<p class="nt-lab-title">Un signal lumineux périodique</p>
<div class="nt-lamp">
<canvas role="img" aria-label="Une lampe dont la couleur change continûment selon un cycle qui se répète."></canvas>
<div>
<p class="nt-chrono"><span class="out-chrono">0,00</span><small>s</small></p>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="chrono"><i class="fa-solid fa-play"></i>&nbsp; Démarrer</button><button type="button" class="nt-btn" data-act="zero"><i class="fa-solid fa-rotate-left"></i>&nbsp; Remettre à zéro</button></div>
<div class="nt-tr-ans"><span class="nt-champ"><label for="feu-n">Motifs complets&nbsp;:</label><input id="feu-n" type="text" inputmode="numeric" style="width:3.5em !important;"></span><button type="button" class="nt-btn" data-act="calc"><i class="fa-solid fa-calculator"></i>&nbsp; Calculer $T$ et $f$</button></div>
</div>
</div>
<canvas class="nt-frise" role="img" aria-label="Enregistrement des couleurs de la lampe au cours des 12 dernières secondes." hidden></canvas>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="frise"> Afficher l'enregistrement des couleurs</label></div>
<p class="nt-msg" aria-live="polite">Démarrez le chronomètre au passage d'une teinte bien repérable, comptez les motifs (un tour complet des couleurs), puis arrêtez-le au retour de la même teinte.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Période et fréquence du signal lumineux</span></summary>
<div class="nt-d-body">
<p>Les couleurs défilent continûment (vert, jaune, rouge, magenta, bleu, cyan, puis de nouveau vert…) et ce cycle se répète à l'identique&nbsp;: c'est le motif. Il dure $T = \pu{5,3 s}$ (aux erreurs de mesure près), donc $f = \dfrac{1}{T} = \dfrac{1}{\pu{5,3 s}} \approx \pu{0,19 Hz}$&nbsp;: environ 0,19 motif par seconde.</p>
<p>La difficulté&nbsp;: la couleur change sans à-coup, si bien qu'il est difficile de déclencher et d'arrêter le chronomètre exactement au même instant du motif (la même teinte). L'incertitude sur chaque déclenchement dépasse alors le simple temps de réaction&nbsp;: c'est une raison de plus pour chronométrer plusieurs motifs.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p><span class="nt-heart" aria-hidden="true">🫀</span>&nbsp; Quand on «&nbsp;prend son pouls&nbsp;», mesure-t-on une période ou une fréquence&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Une fréquence… dans une unité inhabituelle</span></summary>
<div class="nt-d-body">
<p>On compte le <b>nombre de battements</b> pendant une durée donnée&nbsp;: c'est une <b>fréquence</b>. Elle s'exprime d'habitude en battements par minute plutôt qu'en hertz (battements par seconde).</p>
<p>Exemple&nbsp;: un pouls de 72 battements par minute correspond à $f = \dfrac{72}{\pu{60 s}} = \pu{1,2 Hz}$, donc à une période $T = \dfrac{1}{1,2} \approx \pu{0,83 s}$ entre deux battements. Et comme pour toute mesure de fréquence, on compte les battements pendant 15 à 30 secondes plutôt que pendant une seule&nbsp;: c'est plus précis.</p>
</div>
</details>

## Perception d'un son {.nt-h2}

<p>Notre oreille distingue trois caractéristiques d'un son&nbsp;: sa <b style="color:var(--c-haut)">hauteur</b> (grave ou aigu), son <b style="color:var(--c-timbre)">timbre</b> (l'instrument qui joue) et son <b style="color:var(--c-int)">intensité</b> (faible ou fort). Chacune est liée à l'une des grandeurs que l'on lit sur la représentation temporelle. Le laboratoire ci-dessous permet de les faire varier une par une.</p>

<div class="nt-lab" id="lab-son">
<p class="nt-tag"><i class="fa-solid fa-sliders"></i>Laboratoire</p>
<p class="nt-lab-title">Le générateur de sons</p>
<canvas class="nt-son-osc" role="img" aria-label="Représentation temporelle du son produit, avec sa période et son amplitude, et position de sa fréquence sur l'échelle infrasons, sons audibles, ultrasons."></canvas>
<div class="nt-feat3">
<div class="nt-feat nt-f-haut"><p class="nt-feat-title">Hauteur</p><p>liée à la <span class="nt-feat-key">fréquence</span>&nbsp;: <b class="out-f"></b></p></div>
<div class="nt-feat nt-f-timbre"><p class="nt-feat-title">Timbre</p><p>lié à la <span class="nt-feat-key">forme du signal</span>&nbsp;: <b class="out-forme"></b></p></div>
<div class="nt-feat nt-f-int"><p class="nt-feat-title">Intensité</p><p>liée à l'<span class="nt-feat-key">amplitude</span>&nbsp;: <b class="out-a"></b></p></div>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">Fréquence&nbsp;: <b class="out-f2"></b><input type="range" min="0" max="1000" step="1" value="500" data-in="f"></label>
<label class="nt-ctrl">Amplitude (volume)&nbsp;: <b class="out-a2"></b><input type="range" min="0" max="100" step="1" value="35" data-in="a"></label>
<div class="nt-ctrl">Instrument (forme du signal)&nbsp;:<div class="nt-seg" role="radiogroup"><label><input type="radio" name="son-forme" value="sin" checked><span><svg class="nt-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3v8a4 4 0 0 0 8 0V3M12 15v6"/></svg>Diapason</span></label><label><input type="radio" name="son-forme" value="piano"><span><svg class="nt-ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M8 12v7M12 12v7M16 12v7"/><rect x="6.6" y="5" width="2.8" height="7" fill="currentColor" stroke="none"/><rect x="14.6" y="5" width="2.8" height="7" fill="currentColor" stroke="none"/></svg>Piano</span></label><label><input type="radio" name="son-forme" value="violon"><span><svg class="nt-ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="2.8" r="1.3"/><path d="M12 4.1V9.5M12 9.5c-3 0-4 1.6-4 3s1.3 2 1.3 2.6S8 16 8 17.8 9.8 22 12 22s4-2.4 4-4.2-1.3-2.1-1.3-2.7S16 13.9 16 12.5s-1-3-4-3zM10.6 18h2.8"/></svg>Violon</span></label><label><input type="radio" name="son-forme" value="carre"><span><svg class="nt-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 16h4V8h6v8h6V8h4"/></svg>Carré</span></label></div></div>
</div>
<div class="nt-piano" aria-label="Clavier : notes de do 3 à do 4"></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-volume-high"></i>&nbsp; Écouter</button></div>
<p class="nt-msg" aria-live="polite">Choisissez un instrument, une note sur le clavier ou une fréquence, puis écoutez.</p>
</div>
<p class="nt-cap">Commencez avec un volume faible. Les haut-parleurs d'un ordinateur ou d'un téléphone reproduisent mal les sons très graves (en dessous de 100&nbsp;Hz environ). Pour le piano et le violon, le son est celui d'une vraie note, qui évolue au cours du temps&nbsp;; le motif affiché est une version simplifiée de sa partie stable, pour comparer d'un coup d'œil les quatre formes de même période.</p>

### Sons audibles, infrasons et ultrasons {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Le domaine des fréquences des <span class="imp nt-hole">sons audibles</span> pour l'oreille humaine est situé entre <span class="imp nt-hole">20&nbsp;Hz</span> et <span class="imp nt-hole">20&nbsp;000&nbsp;Hz</span>.</p>
<p>En dessous de 20&nbsp;Hz, on parle d'<span class="imp nt-hole">infrasons</span>&nbsp;; au-dessus de 20&nbsp;000&nbsp;Hz, d'<span class="imp nt-hole">ultrasons</span>.</p>
</div>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 720 304' role='img' aria-label="Domaines de fréquences audibles : infrasons en dessous de 20 Hz, sons audibles de 20 à 20 000 Hz, ultrasons au-dessus. Domaines d'audition de l'être humain, de l'éléphant, du chien, du chat, de la chauve-souris et du dauphin."><rect x='120' y='16' width='143.3' height='30' fill='#EDE9FE'/><text x='191.7' y='36' font-size='13' text-anchor='middle' fill='#6D28D9' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>infrasons</text><rect x='263.3' y='16' width='330.5' height='30' fill='#DBEAFE'/><text x='428.6' y='36' font-size='13' text-anchor='middle' fill='#2A6BC4' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>sons audibles</text><rect x='593.8' y='16' width='110.2' height='30' fill='#FCE7F3'/><text x='648.9' y='36' font-size='13' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>ultrasons</text><line x1='120' y1='50' x2='120' y2='258' stroke='#E2E8F0' stroke-width='0.8' stroke-linecap='round'/><text x='120' y='276' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>1</text><line x1='230.2' y1='50' x2='230.2' y2='258' stroke='#E2E8F0' stroke-width='0.8' stroke-linecap='round'/><text x='230.2' y='276' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>10</text><line x1='340.3' y1='50' x2='340.3' y2='258' stroke='#E2E8F0' stroke-width='0.8' stroke-linecap='round'/><text x='340.3' y='276' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>100</text><line x1='450.5' y1='50' x2='450.5' y2='258' stroke='#E2E8F0' stroke-width='0.8' stroke-linecap='round'/><text x='450.5' y='276' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>1 000</text><line x1='560.7' y1='50' x2='560.7' y2='258' stroke='#E2E8F0' stroke-width='0.8' stroke-linecap='round'/><text x='560.7' y='276' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>10 000</text><line x1='670.8' y1='50' x2='670.8' y2='258' stroke='#E2E8F0' stroke-width='0.8' stroke-linecap='round'/><text x='670.8' y='276' font-size='11.5' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>100 000</text><text x='704' y='296' font-size='12' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-style="italic">fréquence (Hz)</text><line x1='263.3' y1='16' x2='263.3' y2='258' stroke='#2A6BC4' stroke-width='1' stroke-linecap='round' stroke-dasharray='4 3'/><line x1='593.8' y1='16' x2='593.8' y2='258' stroke='#2A6BC4' stroke-width='1' stroke-linecap='round' stroke-dasharray='4 3'/><rect x='241.9' y='48' width='42.8' height='20' rx='10' fill='#FFFFFF' stroke='#2A6BC4' stroke-width='1'/><text x='263.3' y='62' font-size='11' text-anchor='middle' fill='#2A6BC4' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>20 Hz</text><rect x='560.1' y='48' width='67.4' height='20' rx='10' fill='#FFFFFF' stroke='#2A6BC4' stroke-width='1'/><text x='593.8' y='62' font-size='11' text-anchor='middle' fill='#2A6BC4' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>20 000 Hz</text><text x='110' y='96.5' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Être humain</text><rect x='263.3' y='87' width='330.5' height='10' rx='5' fill='#12305A' opacity='1'/><text x='110' y='126.5' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Éléphant</text><rect x='252.7' y='117' width='316.7' height='10' rx='5' fill='#458EEC' opacity='0.75'/><text x='110' y='156.5' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Chien</text><rect x='321.2' y='147' width='311.5' height='10' rx='5' fill='#458EEC' opacity='0.75'/><text x='110' y='186.5' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Chat</text><rect x='302.1' y='177' width='347.4' height='10' rx='5' fill='#458EEC' opacity='0.75'/><text x='110' y='216.5' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Chauve-souris</text><rect x='483.7' y='207' width='191.7' height='10' rx='5' fill='#458EEC' opacity='0.75'/><text x='110' y='246.5' font-size='13' text-anchor='end' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Dauphin</text><rect x='326.6' y='237' width='363.7' height='10' rx='5' fill='#458EEC' opacity='0.75'/></svg></div>
<p class="nt-cap">Domaines d'audition de quelques espèces (ordres de grandeur&nbsp;: ils varient selon les études et les individus). L'axe des fréquences est gradué en multipliant par 10 à chaque graduation.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li><b>Infrasons</b>&nbsp;: produits par les séismes, les éruptions volcaniques, la houle, le vent dans les éoliennes&nbsp;; les éléphants les utilisent pour communiquer à plusieurs kilomètres.</li>
<li><b>Ultrasons</b>&nbsp;: utilisés par les chauves-souris et les dauphins pour se repérer (écholocalisation), et par l'être humain pour l'échographie médicale, le sonar des bateaux ou le nettoyage de petites pièces.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Tout le monde entend-il jusqu'à 20&nbsp;000&nbsp;Hz&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Non&nbsp;! Les limites de 20&nbsp;Hz et 20&nbsp;000&nbsp;Hz sont celles d'une oreille jeune et en bonne santé. Avec l'âge, on perd progressivement les aigus&nbsp;: c'est la <b>presbyacousie</b>. Beaucoup d'adultes n'entendent plus au-delà de 15&nbsp;000&nbsp;Hz, parfois bien moins. Une exposition répétée à des sons trop forts accélère cette perte, et elle est définitive.</p>
<p>Testez-vous avec le générateur de sons ci-dessus (à volume modéré)&nbsp;: à partir de quelle fréquence n'entendez-vous plus rien&nbsp;? Comparez avec vos camarades… et avec vos professeurs. Attention, certains haut-parleurs ne reproduisent pas non plus les fréquences les plus aiguës.</p>
</div>
</details>

### Hauteur {.nt-h3}

<p>Pour un son musical, la <span class="imp">hauteur</span> désigne la note jouée (plus ou moins grave ou aiguë).</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La hauteur est liée à la <span class="imp nt-hole">fréquence</span>&nbsp;: plus la fréquence est grande, plus la hauteur est <span class="imp nt-hole">grande</span> et plus la note est <span class="imp nt-hole">aiguë</span>.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">L'octave&nbsp;: une fréquence multipliée par 2</span></summary>
<div class="nt-d-body">
<p>Jouez le do 3 puis le do 4 sur le clavier du générateur&nbsp;: les deux notes portent le même nom, et on a l'impression d'entendre «&nbsp;la même note, plus haut&nbsp;». Leurs fréquences sont 262&nbsp;Hz et 523&nbsp;Hz&nbsp;: la fréquence a <b>doublé</b>. Deux notes séparées d'une octave ont toujours des fréquences dans un rapport 2. C'est pourquoi le la qui suit le la 3 (440&nbsp;Hz) a une fréquence de 880&nbsp;Hz.</p>
</div>
</details>

### Timbre {.nt-h3}

<p>Le signal de deux notes identiques jouées par des instruments différents possède la même période, mais la <span class="imp">forme des signaux</span> est différente.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On appelle <span class="imp nt-hole">timbre</span> ce qui distingue deux notes de même hauteur. Il est lié à la <span class="imp nt-hole">forme du signal</span>.</p>
</div>

<p>Revenez au générateur de sons, choisissez une note, puis changez d'instrument&nbsp;: la période reste la même (même note), seule la forme du motif change. Le signal en forme de sinusoïde, celui du diapason, correspond à un <b>son pur</b>&nbsp;; les instruments de musique produisent des signaux de formes plus complexes&nbsp;: ce sont des <b>sons complexes</b>.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">L'attaque fait aussi partie du timbre</span></summary>
<div class="nt-d-body">
<p>La forme du motif ne dit pas tout&nbsp;: la façon dont le son commence (l'<b>attaque</b>) et dont il évolue ensuite (l'<b>enveloppe</b>) comptent beaucoup dans la reconnaissance d'un instrument. Écoutez ci-dessous une note de piano à l'envers&nbsp;: le motif est le même, mais le son grandit progressivement au lieu de décroître, et ne ressemble plus du tout à un piano. À l'inverse, les premiers centièmes de seconde d'une note de violon, quand l'archet «&nbsp;accroche&nbsp;» la corde, suffisent souvent à reconnaître l'instrument.</p>
<div class="nt-lab" id="lab-attaque">
<p class="nt-tag"><i class="fa-solid fa-backward"></i>Animation</p>
<p class="nt-lab-title">À l'endroit, à l'envers</p>
<canvas role="img" aria-label="Note de piano et note de violon entières en fonction du temps, à l'endroit ou à l'envers."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-ins="piano" data-dir="1"><i class="fa-solid fa-play"></i>&nbsp; Piano</button><button type="button" class="nt-btn" data-ins="piano" data-dir="-1"><i class="fa-solid fa-backward"></i>&nbsp; Piano à l'envers</button><button type="button" class="nt-btn nt-btn-main" data-ins="violon" data-dir="1"><i class="fa-solid fa-play"></i>&nbsp; Violon</button><button type="button" class="nt-btn" data-ins="violon" data-dir="-1"><i class="fa-solid fa-backward"></i>&nbsp; Violon à l'envers</button></div>
<p class="nt-msg" aria-live="polite">Écoutez chaque note dans les deux sens. Le motif (la forme du signal sur quelques périodes) est le même dans les deux cas&nbsp;; seule l'enveloppe est retournée.</p>
</div>
</div>
</details>

### Intensité sonore et amplitude {.nt-h3}

<p>Enfin, la troisième caractéristique d'un son est son <span class="imp">intensité</span>&nbsp;: c'est elle qui fait qu'on le perçoit comme plus ou moins <b>fort</b>.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>L'<span class="imp nt-hole">amplitude</span> d'un signal sonore est la valeur maximale qu'il atteint, mesurée à partir de zéro.</p>
<p>L'<span class="imp nt-hole">intensité sonore</span>, notée $I$, mesure l'<span class="imp nt-hole">énergie</span> que l'onde sonore apporte chaque seconde sur chaque mètre carré de surface. Elle s'exprime en <span class="imp nt-hole">watts par mètre carré</span> (W/m²).</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Plus l'<span class="imp nt-hole">amplitude</span> du signal sonore est grande, plus l'<span class="imp nt-hole">intensité sonore</span> est grande, et plus le son nous paraît <span class="imp nt-hole">fort</span>.</p>
</div>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 700 232' role='img' aria-label="Trois signaux de même période et d'amplitudes croissantes : son faible, son moyen, son fort."><line x1='20' y1='120' x2='226' y2='120' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><polygon points='232,120 225,123 225,117' fill='#CBD5E1'/><text x='224' y='136' font-size='12' text-anchor='middle' fill='#64748B' font-family='Georgia, "Times New Roman", serif' font-style="italic">t</text><line x1='20' y1='200' x2='20' y2='36' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><path d='M20,120 L21,118.5 L22,116.9 L23,115.4 L24,113.9 L25,112.5 L26,111.1 L27,109.8 L28,108.5 L29,107.3 L30,106.1 L31,105.1 L32,104.1 L33,103.3 L34,102.5 L35,101.9 L36,101.4 L37,100.9 L38,100.6 L39,100.5 L40,100.4 L41,100.5 L42,100.6 L43,100.9 L44,101.4 L45,101.9 L46,102.5 L47,103.3 L48,104.1 L49,105.1 L50,106.1 L51,107.3 L52,108.5 L53,109.8 L54,111.1 L55,112.5 L56,113.9 L57,115.4 L58,116.9 L59,118.5 L60,120 L61,121.5 L62,123.1 L63,124.6 L64,126.1 L65,127.5 L66,128.9 L67,130.2 L68,131.5 L69,132.7 L70,133.9 L71,134.9 L72,135.9 L73,136.7 L74,137.5 L75,138.1 L76,138.6 L77,139.1 L78,139.4 L79,139.5 L80,139.6 L81,139.5 L82,139.4 L83,139.1 L84,138.6 L85,138.1 L86,137.5 L87,136.7 L88,135.9 L89,134.9 L90,133.9 L91,132.7 L92,131.5 L93,130.2 L94,128.9 L95,127.5 L96,126.1 L97,124.6 L98,123.1 L99,121.5 L100,120 L101,118.5 L102,116.9 L103,115.4 L104,113.9 L105,112.5 L106,111.1 L107,109.8 L108,108.5 L109,107.3 L110,106.1 L111,105.1 L112,104.1 L113,103.3 L114,102.5 L115,101.9 L116,101.4 L117,100.9 L118,100.6 L119,100.5 L120,100.4 L121,100.5 L122,100.6 L123,100.9 L124,101.4 L125,101.9 L126,102.5 L127,103.3 L128,104.1 L129,105.1 L130,106.1 L131,107.3 L132,108.5 L133,109.8 L134,111.1 L135,112.5 L136,113.9 L137,115.4 L138,116.9 L139,118.5 L140,120 L141,121.5 L142,123.1 L143,124.6 L144,126.1 L145,127.5 L146,128.9 L147,130.2 L148,131.5 L149,132.7 L150,133.9 L151,134.9 L152,135.9 L153,136.7 L154,137.5 L155,138.1 L156,138.6 L157,139.1 L158,139.4 L159,139.5 L160,139.6 L161,139.5 L162,139.4 L163,139.1 L164,138.6 L165,138.1 L166,137.5 L167,136.7 L168,135.9 L169,134.9 L170,133.9 L171,132.7 L172,131.5 L173,130.2 L174,128.9 L175,127.5 L176,126.1 L177,124.6 L178,123.1 L179,121.5 L180,120 L181,118.5 L182,116.9 L183,115.4 L184,113.9 L185,112.5 L186,111.1 L187,109.8 L188,108.5 L189,107.3 L190,106.1 L191,105.1 L192,104.1 L193,103.3 L194,102.5 L195,101.9 L196,101.4 L197,100.9 L198,100.6 L199,100.5 L200,100.4 L201,100.5 L202,100.6 L203,100.9 L204,101.4 L205,101.9 L206,102.5 L207,103.3 L208,104.1 L209,105.1 L210,106.1 L211,107.3 L212,108.5 L213,109.8 L214,111.1 L215,112.5 L216,113.9 L217,115.4 L218,116.9 L219,118.5 L220,120' fill='none' stroke='#FBBF24' stroke-width='1.6' stroke-linejoin='round' stroke-linecap='round'/><line x1='40' y1='115.2' x2='40' y2='106.2' stroke='#D97706' stroke-width='1' stroke-linecap='round'/><polygon points='40,101.4 43.6,107.4 36.4,107.4' fill='#D97706'/><polygon points='40,120 36.4,114 43.6,114' fill='#D97706'/><text x='120' y='26' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>son faible</text><line x1='248' y1='120' x2='454' y2='120' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><polygon points='460,120 453,123 453,117' fill='#CBD5E1'/><text x='452' y='136' font-size='12' text-anchor='middle' fill='#64748B' font-family='Georgia, "Times New Roman", serif' font-style="italic">t</text><line x1='248' y1='200' x2='248' y2='36' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><path d='M248,120 L249,117 L250,114 L251,111 L252,108.1 L253,105.3 L254,102.5 L255,99.9 L256,97.4 L257,95 L258,92.8 L259,90.7 L260,88.9 L261,87.2 L262,85.7 L263,84.4 L264,83.4 L265,82.6 L266,82 L267,81.6 L268,81.5 L269,81.6 L270,82 L271,82.6 L272,83.4 L273,84.4 L274,85.7 L275,87.2 L276,88.9 L277,90.7 L278,92.8 L279,95 L280,97.4 L281,99.9 L282,102.5 L283,105.3 L284,108.1 L285,111 L286,114 L287,117 L288,120 L289,123 L290,126 L291,129 L292,131.9 L293,134.7 L294,137.5 L295,140.1 L296,142.6 L297,145 L298,147.2 L299,149.3 L300,151.1 L301,152.8 L302,154.3 L303,155.6 L304,156.6 L305,157.4 L306,158 L307,158.4 L308,158.5 L309,158.4 L310,158 L311,157.4 L312,156.6 L313,155.6 L314,154.3 L315,152.8 L316,151.1 L317,149.3 L318,147.2 L319,145 L320,142.6 L321,140.1 L322,137.5 L323,134.7 L324,131.9 L325,129 L326,126 L327,123 L328,120 L329,117 L330,114 L331,111 L332,108.1 L333,105.3 L334,102.5 L335,99.9 L336,97.4 L337,95 L338,92.8 L339,90.7 L340,88.9 L341,87.2 L342,85.7 L343,84.4 L344,83.4 L345,82.6 L346,82 L347,81.6 L348,81.5 L349,81.6 L350,82 L351,82.6 L352,83.4 L353,84.4 L354,85.7 L355,87.2 L356,88.9 L357,90.7 L358,92.8 L359,95 L360,97.4 L361,99.9 L362,102.5 L363,105.3 L364,108.1 L365,111 L366,114 L367,117 L368,120 L369,123 L370,126 L371,129 L372,131.9 L373,134.7 L374,137.5 L375,140.1 L376,142.6 L377,145 L378,147.2 L379,149.3 L380,151.1 L381,152.8 L382,154.3 L383,155.6 L384,156.6 L385,157.4 L386,158 L387,158.4 L388,158.5 L389,158.4 L390,158 L391,157.4 L392,156.6 L393,155.6 L394,154.3 L395,152.8 L396,151.1 L397,149.3 L398,147.2 L399,145 L400,142.6 L401,140.1 L402,137.5 L403,134.7 L404,131.9 L405,129 L406,126 L407,123 L408,120 L409,117 L410,114 L411,111 L412,108.1 L413,105.3 L414,102.5 L415,99.9 L416,97.4 L417,95 L418,92.8 L419,90.7 L420,88.9 L421,87.2 L422,85.7 L423,84.4 L424,83.4 L425,82.6 L426,82 L427,81.6 L428,81.5 L429,81.6 L430,82 L431,82.6 L432,83.4 L433,84.4 L434,85.7 L435,87.2 L436,88.9 L437,90.7 L438,92.8 L439,95 L440,97.4 L441,99.9 L442,102.5 L443,105.3 L444,108.1 L445,111 L446,114 L447,117 L448,120' fill='none' stroke='#F59E0B' stroke-width='1.6' stroke-linejoin='round' stroke-linecap='round'/><line x1='268' y1='115.2' x2='268' y2='87.3' stroke='#D97706' stroke-width='1' stroke-linecap='round'/><polygon points='268,82.5 271.6,88.5 264.4,88.5' fill='#D97706'/><polygon points='268,120 264.4,114 271.6,114' fill='#D97706'/><text x='348' y='26' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>son moyen</text><line x1='476' y1='120' x2='682' y2='120' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><polygon points='688,120 681,123 681,117' fill='#CBD5E1'/><text x='680' y='136' font-size='12' text-anchor='middle' fill='#64748B' font-family='Georgia, "Times New Roman", serif' font-style="italic">t</text><line x1='476' y1='200' x2='476' y2='36' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><path d='M476,120 L477,114.8 L478,109.6 L479,104.5 L480,99.5 L481,94.6 L482,89.8 L483,85.3 L484,80.9 L485,76.8 L486,73 L487,69.4 L488,66.2 L489,63.3 L490,60.7 L491,58.6 L492,56.8 L493,55.3 L494,54.3 L495,53.7 L496,53.5 L497,53.7 L498,54.3 L499,55.3 L500,56.8 L501,58.6 L502,60.7 L503,63.3 L504,66.2 L505,69.4 L506,73 L507,76.8 L508,80.9 L509,85.3 L510,89.8 L511,94.6 L512,99.5 L513,104.5 L514,109.6 L515,114.8 L516,120 L517,125.2 L518,130.4 L519,135.5 L520,140.5 L521,145.4 L522,150.2 L523,154.7 L524,159.1 L525,163.2 L526,167 L527,170.6 L528,173.8 L529,176.7 L530,179.3 L531,181.4 L532,183.2 L533,184.7 L534,185.7 L535,186.3 L536,186.5 L537,186.3 L538,185.7 L539,184.7 L540,183.2 L541,181.4 L542,179.3 L543,176.7 L544,173.8 L545,170.6 L546,167 L547,163.2 L548,159.1 L549,154.7 L550,150.2 L551,145.4 L552,140.5 L553,135.5 L554,130.4 L555,125.2 L556,120 L557,114.8 L558,109.6 L559,104.5 L560,99.5 L561,94.6 L562,89.8 L563,85.3 L564,80.9 L565,76.8 L566,73 L567,69.4 L568,66.2 L569,63.3 L570,60.7 L571,58.6 L572,56.8 L573,55.3 L574,54.3 L575,53.7 L576,53.5 L577,53.7 L578,54.3 L579,55.3 L580,56.8 L581,58.6 L582,60.7 L583,63.3 L584,66.2 L585,69.4 L586,73 L587,76.8 L588,80.9 L589,85.3 L590,89.8 L591,94.6 L592,99.5 L593,104.5 L594,109.6 L595,114.8 L596,120 L597,125.2 L598,130.4 L599,135.5 L600,140.5 L601,145.4 L602,150.2 L603,154.7 L604,159.1 L605,163.2 L606,167 L607,170.6 L608,173.8 L609,176.7 L610,179.3 L611,181.4 L612,183.2 L613,184.7 L614,185.7 L615,186.3 L616,186.5 L617,186.3 L618,185.7 L619,184.7 L620,183.2 L621,181.4 L622,179.3 L623,176.7 L624,173.8 L625,170.6 L626,167 L627,163.2 L628,159.1 L629,154.7 L630,150.2 L631,145.4 L632,140.5 L633,135.5 L634,130.4 L635,125.2 L636,120 L637,114.8 L638,109.6 L639,104.5 L640,99.5 L641,94.6 L642,89.8 L643,85.3 L644,80.9 L645,76.8 L646,73 L647,69.4 L648,66.2 L649,63.3 L650,60.7 L651,58.6 L652,56.8 L653,55.3 L654,54.3 L655,53.7 L656,53.5 L657,53.7 L658,54.3 L659,55.3 L660,56.8 L661,58.6 L662,60.7 L663,63.3 L664,66.2 L665,69.4 L666,73 L667,76.8 L668,80.9 L669,85.3 L670,89.8 L671,94.6 L672,99.5 L673,104.5 L674,109.6 L675,114.8 L676,120' fill='none' stroke='#B45309' stroke-width='1.6' stroke-linejoin='round' stroke-linecap='round'/><line x1='496' y1='115.2' x2='496' y2='59.3' stroke='#D97706' stroke-width='1' stroke-linecap='round'/><polygon points='496,54.5 499.6,60.5 492.4,60.5' fill='#D97706'/><polygon points='496,120 492.4,114 499.6,114' fill='#D97706'/><text x='576' y='26' font-size='13' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>son fort</text><text x='354' y='222' font-size='12' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-style="italic">même période, amplitude de plus en plus grande</text></svg></div>
<p class="nt-cap">Une même note jouée de plus en plus fort&nbsp;: la période (donc la hauteur) ne change pas, l'amplitude augmente.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>L'intensité sonore d'une trompette seule vaut $I_t$ à une certaine distance. Que vaut l'intensité sonore de quatre trompettes identiques jouant ensemble, à la même distance&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Les énergies s'ajoutent</span></summary>
<div class="nt-d-body">
<p>Chaque trompette apporte sa propre énergie sonore, et ces énergies s'ajoutent&nbsp;: l'intensité sonore des quatre trompettes vaut $4\,I_t$.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Amplitude doublée, intensité quadruplée</span></summary>
<div class="nt-d-body">
<p>Si l'amplitude du signal double, les particules d'air vont deux fois plus loin de leur position de repos… pendant la même durée, puisque la période ne change pas. Elles vont donc aussi deux fois plus vite. Or l'énergie d'un objet en mouvement est proportionnelle au <b>carré</b> de sa vitesse&nbsp;: elle est multipliée par $2^2 = 4$. Ainsi, l'intensité sonore est proportionnelle au carré de l'amplitude&nbsp;:</p>
<ul class="nt-facts">
<li>amplitude multipliée par 2&nbsp;: intensité multipliée par 4&nbsp;;</li>
<li>amplitude multipliée par 100&nbsp;: intensité multipliée par $100^2 = 10\,000$.</li>
</ul>
<p>Inversement, les quatre trompettes de la question précédente ne donnent pas un signal d'amplitude 4 fois plus grande, mais seulement environ 2 fois plus grande&nbsp;: leurs vibrations ne sont pas synchronisées et s'annulent en partie, tantôt ici, tantôt là. Les intensités, elles, s'additionnent bien.</p>
</div>
</details>

<p>Mais l'intensité sonore rend mal compte de notre <span class="imp">sensation auditive</span>. On peut par exemple mesurer que l'intensité sonore du son émis par quelqu'un qui parle fort est environ 10&nbsp;000 fois plus grande que celle d'une personne qui chuchote à la même distance&nbsp;! Pourtant, on n'a pas la sensation d'un son 10&nbsp;000 fois plus fort…</p>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p><span class="imp nt-hole">Intensité sonore</span> et <span class="imp nt-hole">sensation auditive</span> ne sont pas <span class="imp nt-hole">proportionnelles</span>&nbsp;!</p>
</div>

### Niveau d'intensité sonore {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Pour tenir compte de cette échelle non proportionnelle, on utilise une autre grandeur&nbsp;: le <span class="imp nt-hole">niveau d'intensité sonore</span>, noté $L$, mesuré en <span class="imp nt-hole">décibels</span> (dB) à l'aide d'un <span class="imp nt-hole">sonomètre</span>.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Lorsque l'intensité sonore augmente, le niveau d'intensité sonore augmente aussi, mais <span class="imp nt-hole">beaucoup moins vite</span>&nbsp;:</p>
<ul class="nt-facts">
<li>intensité multipliée par 2&nbsp;: niveau augmenté de <span class="imp nt-hole">3&nbsp;dB</span>&nbsp;;</li>
<li>intensité multipliée par 10&nbsp;: niveau augmenté de <span class="imp nt-hole">10&nbsp;dB</span>.</li>
</ul>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Un chuchotement correspond à environ 30&nbsp;dB, une personne qui parle fort à environ 70&nbsp;dB. Le niveau a augmenté de 40&nbsp;dB, soit quatre fois 10&nbsp;dB&nbsp;: l'intensité sonore a été multipliée par $10 \times 10 \times 10 \times 10 = 10\,000$. Une augmentation énorme de l'intensité correspond à une augmentation modérée du niveau, bien plus proche de notre sensation.</p>
</div>

<div class="nt-lab" id="lab-trompettes">
<p class="nt-tag"><i class="fa-solid fa-music"></i>Animation</p>
<p class="nt-lab-title">Une, deux, quatre trompettes…</p>
<div class="nt-btns" style="align-items:center;"><span class="nt-note">Nombre de trompettes&nbsp;:</span><div class="nt-seg" role="radiogroup" aria-label="Nombre de trompettes"><label><input type="radio" name="tromp-n" value="1" checked><span>1</span></label><label><input type="radio" name="tromp-n" value="2"><span>2</span></label><label><input type="radio" name="tromp-n" value="4"><span>4</span></label><label><input type="radio" name="tromp-n" value="8"><span>8</span></label><label><input type="radio" name="tromp-n" value="10"><span>10</span></label><label><input type="radio" name="tromp-n" value="100"><span>100</span></label></div></div>
<p class="nt-center nt-note">Chaque pastille représente l'intensité sonore $I_t$ d'une trompette.</p>
<div class="nt-dots" aria-hidden="true"></div>
<div class="nt-bar-row"><span>Intensité</span><div class="nt-bar nt-bar-I"><div></div></div><b class="out-I"></b></div>
<div class="nt-bar-row"><span>Niveau</span><div class="nt-bar nt-bar-L"><div></div></div><b class="out-L"></b></div>
<p class="nt-center"><span class="nt-sono"><span class="out-sono">80</span><small>dB</small></span></p>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-mic">
<p class="nt-mic-title"><i class="fa-solid fa-microphone"></i>&nbsp; Et en vrai&nbsp;? Mesurez avec le micro de votre appareil</p>
<p class="nt-note">La page fait jouer 1, 2 ou 4 trompettes (des sons de synthèse, légèrement désaccordés comme de vrais musiciens) et mesure le niveau reçu par le micro. Ce micro n'est pas étalonné&nbsp;: les valeurs en décibels sont relatives, mais leurs <b>écarts</b> ont bien un sens. Sans micro, la mesure se fait directement sur le signal émis.</p>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="micro"><i class="fa-solid fa-microphone"></i>&nbsp; Activer le micro</button><button type="button" class="nt-btn" data-act="libre" disabled><i class="fa-solid fa-gauge"></i>&nbsp; Sonomètre libre</button></div>
<div class="nt-vu"><div class="nt-vu-bar"><div></div></div><span class="nt-sono out-vu"><span>—</span><small>dB</small></span></div>
<div class="nt-btns" style="align-items:center;"><span class="nt-note">Mesurer le niveau de&nbsp;:</span><button type="button" class="nt-btn nt-btn-main" data-n="1">1 trompette</button><button type="button" class="nt-btn nt-btn-main" data-n="2">2 trompettes</button><button type="button" class="nt-btn nt-btn-main" data-n="4">4 trompettes</button></div>
<div class="nt-scroll"><table class="nt-t nt-mes">
<thead><tr><th>trompettes</th><th>niveau mesuré</th><th>écart mesuré</th><th>écart attendu</th></tr></thead>
<tbody><tr data-n="1"><td>1</td><td>—</td><td>référence</td><td>référence</td></tr><tr data-n="2"><td>2</td><td>—</td><td>—</td><td>+3&nbsp;dB</td></tr><tr data-n="4"><td>4</td><td>—</td><td>—</td><td>+6&nbsp;dB</td></tr></tbody>
</table></div>
<p class="nt-msg nt-mic-msg" aria-live="polite"></p>
</div>
</div>
<p class="nt-cap">Une trompette seule donne ici 80&nbsp;dB. La barre «&nbsp;Niveau&nbsp;» est graduée de 0 à 120&nbsp;dB. Pour la mesure au micro, utilisez de préférence un ordinateur, dans une pièce calme&nbsp;: certains téléphones règlent automatiquement le volume du micro, ce qui fausse les écarts.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La formule du niveau d'intensité sonore (terminale)</span></summary>
<div class="nt-d-body">
<p>En terminale, on définit le niveau d'intensité sonore par $L = 10 \log\left(\dfrac{I}{I_0}\right)$, où $I_0$ est l'intensité sonore la plus faible que l'oreille humaine puisse percevoir (environ un millième de milliardième de W/m²). La fonction logarithme décimal «&nbsp;log&nbsp;» compte, en quelque sorte, le nombre de multiplications par 10&nbsp;: chaque fois que l'intensité est multipliée par 10, le niveau augmente de 10&nbsp;dB. Et comme $10 \log 2 \approx 3$, doubler l'intensité ajoute environ 3&nbsp;dB.</p>
</div>
</details>

### Échelle des niveaux et dangers {.nt-h3}

<div class="nt-lab" id="lab-echelle">
<p class="nt-tag"><i class="fa-solid fa-ear-listen"></i>Animation</p>
<p class="nt-lab-title">L'échelle des niveaux d'intensité sonore</p>
<div class="nt-presets"></div>
<canvas role="img" aria-label="Échelle des niveaux d'intensité sonore de 0 à 140 dB, colorée selon le risque, avec un repère sur le niveau choisi."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Niveau d'intensité sonore&nbsp;: <b class="out-L"></b><input type="range" min="0" max="140" step="1" value="60" data-in="L"></label></div>
<div class="nt-info" aria-live="polite"></div>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple&nbsp;: le son le plus fort jamais enregistré</p>
<p>Le 27 août 1883, l'éruption du volcan <b>Krakatoa</b>, en Indonésie, pulvérise les deux tiers de l'île. À 160&nbsp;km de là, le manomètre de l'usine à gaz de Batavia (l'actuelle Jakarta) enregistre une surpression d'environ 8,5&nbsp;kPa, soit un niveau d'intensité sonore d'environ <b>172&nbsp;dB</b>&nbsp;: 50&nbsp;dB de plus que le seuil de douleur, c'est-à-dire une intensité sonore plus de 100&nbsp;000 fois plus grande, à 160&nbsp;km&nbsp;! Selon les récits de l'époque, des marins qui se trouvaient à une soixantaine de kilomètres ont eu les tympans crevés. L'explosion a été entendue jusqu'à environ 4&nbsp;800&nbsp;km, sur l'île Rodrigues, dans l'océan Indien, et l'onde de pression a fait plusieurs fois le tour de la Terre, enregistrée par les baromètres du monde entier pendant cinq jours.</p>
<p>Le 15 janvier 2022, l'éruption sous-marine du <b>Hunga Tonga</b>, dans le Pacifique, a produit une onde de pression d'ampleur comparable. Cette fois, des instruments modernes l'ont suivie autour du globe, et son grondement a été entendu jusqu'en Alaska, à près de 10&nbsp;000&nbsp;km. Il y est arrivé plus de 7&nbsp;heures après l'éruption&nbsp;: une durée cohérente avec $\Delta t = d/v$ pour une vitesse de quelques centaines de mètres par seconde.</p>
<p>Peut-on aller encore plus haut&nbsp;? Dans l'air, vers 194&nbsp;dB, la surpression de l'onde atteint la pression atmosphérique elle-même&nbsp;: au-delà, la «&nbsp;dépression&nbsp;» devrait descendre sous le vide, ce qui est impossible. L'onde n'est plus un son ordinaire mais une <b>onde de choc</b>, et l'échelle des décibels perd son sens.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Durée limite d'exposition (sans protection) avant dommages&nbsp;:</p>
<ul class="nt-facts">
<li>de 120 à 140&nbsp;dB, quelques secondes suffisent à provoquer des <span class="imp nt-hole">dégâts irréversibles</span>&nbsp;;</li>
<li>95&nbsp;dB&nbsp;: 15&nbsp;min par jour&nbsp;;</li>
<li>86&nbsp;dB&nbsp;: 2&nbsp;h par jour&nbsp;;</li>
<li>80&nbsp;dB&nbsp;: 8&nbsp;h par jour.</li>
</ul>
<p>Au-delà de 80&nbsp;dB, chaque augmentation de 3&nbsp;dB (intensité doublée) divise par deux la durée d'exposition sans danger. Les cellules de l'oreille interne détruites par un son trop fort ne se réparent jamais&nbsp;: la perte d'audition et les acouphènes (sifflements permanents) qui en résultent sont définitifs.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Que se passe-t-il dans l'oreille&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Le tympan et les osselets transmettent la vibration à l'oreille interne, la <b>cochlée</b>, un petit tube enroulé en colimaçon et rempli de liquide. Elle contient environ 15&nbsp;000 <b>cellules ciliées</b>, surmontées de touffes de cils microscopiques, qui transforment la vibration en signal nerveux. Chaque région de la cochlée est sensible à une plage de fréquences&nbsp;: les aigus à l'entrée, les graves au fond.</p>
<ul class="nt-facts">
<li><b>Après un son trop fort</b>, les cils sont tordus et épuisés&nbsp;: l'oreille est «&nbsp;cotonneuse&nbsp;» et siffle. Cette <b>fatigue auditive</b> peut encore disparaître en quelques heures ou quelques jours.</li>
<li><b>Si l'exposition est trop forte ou se répète</b>, les cils se cassent et les cellules meurent. Chez l'être humain, elles ne se régénèrent jamais&nbsp;: la perte est <b>définitive</b>. Les premières touchées sont les cellules ciliées «&nbsp;externes&nbsp;», qui amplifient les sons faibles et aident à distinguer des sons voisins&nbsp;: on entend moins bien, et surtout on peine à suivre une conversation dans le bruit.</li>
<li><b>Même quand l'audition semble revenue</b>, une partie des connexions entre les cellules ciliées et les fibres du nerf auditif peut avoir été détruite&nbsp;: on parle de «&nbsp;surdité cachée&nbsp;», car elle n'apparaît pas toujours aux tests auditifs classiques.</li>
<li><b>La signature du bruit</b>&nbsp;: la perte apparaît d'abord vers 4&nbsp;000&nbsp;Hz, une zone de la cochlée particulièrement sollicitée, avant de s'étendre aux fréquences voisines.</li>
<li><b>Les acouphènes</b> (sifflements ou bourdonnements entendus en l'absence de tout son) et l'<b>hyperacousie</b> (sons ordinaires devenus douloureux) accompagnent souvent ces lésions.</li>
</ul>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>À savoir&nbsp;: se protéger</p>
<ul class="nt-facts">
<li>Au concert ou en discothèque, s'éloigner des enceintes, faire des pauses au calme et porter des bouchons d'oreille.</li>
<li>Avec un casque ou des écouteurs, limiter le volume (pas au maximum) et la durée d'écoute&nbsp;: un baladeur à fond peut dépasser 100&nbsp;dB, directement dans l'oreille.</li>
<li>Après une exposition, des oreilles qui sifflent ou un son «&nbsp;étouffé&nbsp;» sont un signal d'alerte&nbsp;: si cela persiste plus de 24&nbsp;h, il faut consulter rapidement.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Notre oreille n'est pas aussi sensible à toutes les fréquences</span></summary>
<div class="nt-d-body">
<p>Le «&nbsp;seuil d'audibilité&nbsp;» de 0&nbsp;dB correspond, par convention, au son le plus faible que l'on puisse entendre à 1&nbsp;000&nbsp;Hz. En réalité, le niveau le plus faible que l'on puisse entendre dépend beaucoup de la fréquence&nbsp;: notre oreille est très sensible entre 1&nbsp;000 et 5&nbsp;000&nbsp;Hz (la zone des cris et des consonnes de la parole), et beaucoup moins dans les graves et les très aigus. Un son grave de 50&nbsp;Hz doit atteindre environ 40&nbsp;dB pour être simplement perçu&nbsp;!</p>
<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 680 312' role='img' aria-label="Domaine d'audibilité : le seuil d'audibilité est élevé dans les graves et les très aigus, et le plus bas entre 1 000 et 5 000 Hz ; le seuil de douleur se situe vers 120 dB."><line x1='70' y1='270' x2='660' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='252.4' x2='660' y2='252.4' stroke='#E2E8F0' stroke-width='0.9' stroke-linecap='round'/><text x='62' y='256.4' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>0</text><line x1='70' y1='234.9' x2='660' y2='234.9' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='217.3' x2='660' y2='217.3' stroke='#E2E8F0' stroke-width='0.9' stroke-linecap='round'/><text x='62' y='221.3' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>20</text><line x1='70' y1='199.7' x2='660' y2='199.7' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='182.1' x2='660' y2='182.1' stroke='#E2E8F0' stroke-width='0.9' stroke-linecap='round'/><text x='62' y='186.1' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>40</text><line x1='70' y1='164.6' x2='660' y2='164.6' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='147' x2='660' y2='147' stroke='#E2E8F0' stroke-width='0.9' stroke-linecap='round'/><text x='62' y='151' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>60</text><line x1='70' y1='129.4' x2='660' y2='129.4' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='111.9' x2='660' y2='111.9' stroke='#E2E8F0' stroke-width='0.9' stroke-linecap='round'/><text x='62' y='115.9' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>80</text><line x1='70' y1='94.3' x2='660' y2='94.3' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='76.7' x2='660' y2='76.7' stroke='#E2E8F0' stroke-width='0.9' stroke-linecap='round'/><text x='62' y='80.7' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>100</text><line x1='70' y1='59.1' x2='660' y2='59.1' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='41.6' x2='660' y2='41.6' stroke='#E2E8F0' stroke-width='0.9' stroke-linecap='round'/><text x='62' y='45.6' font-size='11.5' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>120</text><line x1='70' y1='24' x2='660' y2='24' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><line x1='70' y1='24' x2='70' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='70' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>20</text><line x1='148.3' y1='24' x2='148.3' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='148.3' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>50</text><line x1='207.5' y1='24' x2='207.5' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='207.5' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>100</text><line x1='266.7' y1='24' x2='266.7' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='266.7' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>200</text><line x1='344.9' y1='24' x2='344.9' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='344.9' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>500</text><line x1='404.1' y1='24' x2='404.1' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='404.1' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>1 000</text><line x1='463.3' y1='24' x2='463.3' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='463.3' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>2 000</text><line x1='541.6' y1='24' x2='541.6' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='541.6' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>5 000</text><line x1='600.8' y1='24' x2='600.8' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='600.8' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>10 000</text><line x1='660' y1='24' x2='660' y2='270' stroke='#E2E8F0' stroke-width='0.6' stroke-linecap='round'/><text x='660' y='287' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>20 000</text><path d='M70,114.5 L73.2,117.4 L76.4,120.2 L79.5,123.1 L82.7,125.9 L85.9,128.8 L89.1,131.6 L92.3,134.3 L95.6,137.1 L98.9,139.8 L102.2,142.5 L105.5,145.1 L108.8,147.7 L112.2,150.2 L115.6,152.8 L119,155.3 L122.4,157.7 L125.8,160 L129.2,162.3 L132.4,164.6 L135.6,166.7 L138.7,168.9 L141.9,170.9 L145.1,173 L148.3,175 L151.6,176.9 L154.8,178.9 L158.1,180.8 L161.4,182.7 L164.7,184.6 L168,186.4 L171.4,188.2 L174.8,190 L178.2,191.8 L181.6,193.5 L185,195.2 L188.4,196.8 L191.6,198.4 L194.8,200 L197.9,201.5 L201.1,202.9 L204.3,204.3 L207.5,205.7 L210.6,207.1 L213.8,208.4 L217,209.7 L220.2,211 L223.3,212.3 L226.5,213.5 L230,214.8 L233.6,216 L237.1,217.3 L240.6,218.5 L244.1,219.7 L247.6,220.8 L250.8,221.9 L254,223 L257.1,224.1 L260.3,225.1 L263.5,226 L266.7,227 L269.8,227.9 L273,228.9 L276.2,229.8 L279.4,230.6 L282.5,231.5 L285.7,232.3 L289,233.2 L292.3,234 L295.6,234.9 L298.9,235.7 L302.2,236.4 L305.5,237.2 L308.9,238 L312.3,238.7 L315.7,239.4 L319.1,240.1 L322.5,240.8 L325.9,241.4 L329,242 L332.2,242.6 L335.4,243.1 L338.6,243.6 L341.8,244.1 L344.9,244.6 L348.2,245.1 L351.5,245.5 L354.8,245.9 L358.1,246.3 L361.4,246.7 L364.7,247 L368.1,247.3 L371.5,247.6 L374.9,247.9 L378.3,248.1 L381.7,248.3 L385.1,248.4 L388.2,248.5 L391.4,248.7 L394.6,248.7 L397.8,248.9 L401,249 L404.1,249.2 L410.8,249.5 L417.5,249.8 L424.2,250.2 L430.9,250.7 L437.6,251.1 L444.3,251.6 L447.5,252.1 L450.6,252.6 L453.8,253.1 L457,253.7 L460.2,254.3 L463.3,255 L466.5,255.7 L469.7,256.5 L472.9,257.3 L476,258.1 L479.2,258.8 L482.4,259.5 L485.7,260.2 L489,260.8 L492.3,261.4 L495.6,261.8 L498.8,262.1 L502.1,262.4 L505.5,262.5 L508.9,262.5 L512.3,262.4 L515.7,262.1 L519.1,261.7 L522.5,261.1 L525.7,260.4 L528.9,259.5 L532.1,258.5 L535.2,257.2 L538.4,255.8 L541.6,254.2 L544.9,252.4 L548.2,250.5 L551.5,248.5 L554.8,246.3 L558,244.2 L561.3,242.1 L564.7,240.1 L568.1,238.1 L571.5,236.1 L574.9,234.3 L578.3,232.7 L581.7,231.3 L584.9,230.1 L588.1,229.1 L591.3,228.2 L594.4,227.4 L597.6,226.6 L600.8,225.7 L604,224.7 L607.2,223.7 L610.3,222.6 L613.5,221.3 L616.7,219.8 L619.9,218.3 L621.5,216.6 L623.1,214.8 L624.7,212.9 L626.3,210.5 L627.9,207.9 L629.5,205 L631.4,201.8 L633.3,198.2 L635.2,194.4 L637.1,190 L639,185.2 L640.9,180.1 L642.6,174.7 L644.3,168.9 L646,162.8 L647.6,156.3 L649.3,149.8 L651,143.2 L652.5,136.6 L654,130 L655.5,123.3 L657,116.5 L658.5,109.8 L660,103.1 L660,31 L650.2,32.1 L640.3,33.1 L630.5,34.1 L620.7,35 L610.8,35.8 L601,36.5 L591.2,37.2 L581.3,37.9 L571.5,38.4 L561.7,38.9 L551.8,39.4 L542,39.8 L532.2,40.1 L522.3,40.4 L512.5,40.7 L502.7,40.9 L492.8,41 L483,41.2 L473.2,41.3 L463.3,41.4 L453.5,41.4 L443.7,41.5 L433.8,41.5 L424,41.5 L414.2,41.6 L404.3,41.6 L394.5,41.6 L384.7,41.6 L374.8,41.6 L365,41.6 L355.2,41.6 L345.3,41.6 L335.5,41.6 L325.7,41.6 L315.8,41.6 L306,41.5 L296.2,41.5 L286.3,41.5 L276.5,41.4 L266.7,41.4 L256.8,41.3 L247,41.2 L237.2,41 L227.3,40.9 L217.5,40.7 L207.7,40.4 L197.8,40.1 L188,39.8 L178.2,39.4 L168.3,38.9 L158.5,38.4 L148.7,37.9 L138.8,37.2 L129,36.5 L119.2,35.8 L109.3,35 L99.5,34.1 L89.7,33.1 L79.8,32.1 L70,31 Z' fill='#DBEAFE' opacity='0.85'/><path d='M70,114.5 L73.2,117.4 L76.4,120.2 L79.5,123.1 L82.7,125.9 L85.9,128.8 L89.1,131.6 L92.3,134.3 L95.6,137.1 L98.9,139.8 L102.2,142.5 L105.5,145.1 L108.8,147.7 L112.2,150.2 L115.6,152.8 L119,155.3 L122.4,157.7 L125.8,160 L129.2,162.3 L132.4,164.6 L135.6,166.7 L138.7,168.9 L141.9,170.9 L145.1,173 L148.3,175 L151.6,176.9 L154.8,178.9 L158.1,180.8 L161.4,182.7 L164.7,184.6 L168,186.4 L171.4,188.2 L174.8,190 L178.2,191.8 L181.6,193.5 L185,195.2 L188.4,196.8 L191.6,198.4 L194.8,200 L197.9,201.5 L201.1,202.9 L204.3,204.3 L207.5,205.7 L210.6,207.1 L213.8,208.4 L217,209.7 L220.2,211 L223.3,212.3 L226.5,213.5 L230,214.8 L233.6,216 L237.1,217.3 L240.6,218.5 L244.1,219.7 L247.6,220.8 L250.8,221.9 L254,223 L257.1,224.1 L260.3,225.1 L263.5,226 L266.7,227 L269.8,227.9 L273,228.9 L276.2,229.8 L279.4,230.6 L282.5,231.5 L285.7,232.3 L289,233.2 L292.3,234 L295.6,234.9 L298.9,235.7 L302.2,236.4 L305.5,237.2 L308.9,238 L312.3,238.7 L315.7,239.4 L319.1,240.1 L322.5,240.8 L325.9,241.4 L329,242 L332.2,242.6 L335.4,243.1 L338.6,243.6 L341.8,244.1 L344.9,244.6 L348.2,245.1 L351.5,245.5 L354.8,245.9 L358.1,246.3 L361.4,246.7 L364.7,247 L368.1,247.3 L371.5,247.6 L374.9,247.9 L378.3,248.1 L381.7,248.3 L385.1,248.4 L388.2,248.5 L391.4,248.7 L394.6,248.7 L397.8,248.9 L401,249 L404.1,249.2 L410.8,249.5 L417.5,249.8 L424.2,250.2 L430.9,250.7 L437.6,251.1 L444.3,251.6 L447.5,252.1 L450.6,252.6 L453.8,253.1 L457,253.7 L460.2,254.3 L463.3,255 L466.5,255.7 L469.7,256.5 L472.9,257.3 L476,258.1 L479.2,258.8 L482.4,259.5 L485.7,260.2 L489,260.8 L492.3,261.4 L495.6,261.8 L498.8,262.1 L502.1,262.4 L505.5,262.5 L508.9,262.5 L512.3,262.4 L515.7,262.1 L519.1,261.7 L522.5,261.1 L525.7,260.4 L528.9,259.5 L532.1,258.5 L535.2,257.2 L538.4,255.8 L541.6,254.2 L544.9,252.4 L548.2,250.5 L551.5,248.5 L554.8,246.3 L558,244.2 L561.3,242.1 L564.7,240.1 L568.1,238.1 L571.5,236.1 L574.9,234.3 L578.3,232.7 L581.7,231.3 L584.9,230.1 L588.1,229.1 L591.3,228.2 L594.4,227.4 L597.6,226.6 L600.8,225.7 L604,224.7 L607.2,223.7 L610.3,222.6 L613.5,221.3 L616.7,219.8 L619.9,218.3 L621.5,216.6 L623.1,214.8 L624.7,212.9 L626.3,210.5 L627.9,207.9 L629.5,205 L631.4,201.8 L633.3,198.2 L635.2,194.4 L637.1,190 L639,185.2 L640.9,180.1 L642.6,174.7 L644.3,168.9 L646,162.8 L647.6,156.3 L649.3,149.8 L651,143.2 L652.5,136.6 L654,130 L655.5,123.3 L657,116.5 L658.5,109.8 L660,103.1' fill='none' stroke='#2A6BC4' stroke-width='1.6' stroke-linejoin='round' stroke-linecap='round'/><path d='M70,31 L79.8,32.1 L89.7,33.1 L99.5,34.1 L109.3,35 L119.2,35.8 L129,36.5 L138.8,37.2 L148.7,37.9 L158.5,38.4 L168.3,38.9 L178.2,39.4 L188,39.8 L197.8,40.1 L207.7,40.4 L217.5,40.7 L227.3,40.9 L237.2,41 L247,41.2 L256.8,41.3 L266.7,41.4 L276.5,41.4 L286.3,41.5 L296.2,41.5 L306,41.5 L315.8,41.6 L325.7,41.6 L335.5,41.6 L345.3,41.6 L355.2,41.6 L365,41.6 L374.8,41.6 L384.7,41.6 L394.5,41.6 L404.3,41.6 L414.2,41.6 L424,41.5 L433.8,41.5 L443.7,41.5 L453.5,41.4 L463.3,41.4 L473.2,41.3 L483,41.2 L492.8,41 L502.7,40.9 L512.5,40.7 L522.3,40.4 L532.2,40.1 L542,39.8 L551.8,39.4 L561.7,38.9 L571.5,38.4 L581.3,37.9 L591.2,37.2 L601,36.5 L610.8,35.8 L620.7,35 L630.5,34.1 L640.3,33.1 L650.2,32.1 L660,31' fill='none' stroke='#E11D48' stroke-width='1.4' stroke-linejoin='round' stroke-linecap='round'/><line x1='70' y1='24' x2='70' y2='270' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><line x1='70' y1='270' x2='660' y2='270' stroke='#CBD5E1' stroke-width='1' stroke-linecap='round'/><rect x='80.8' y='214.1' width='127.9' height='20.5' rx='10.2' fill='#FFFFFF' stroke='#2A6BC4' stroke-width='1'/><text x='144.8' y='228.5' font-size='11.5' text-anchor='middle' fill='#2A6BC4' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>seuil d’audibilité</text><rect x='346.6' y='18.3' width='115' height='20.5' rx='10.2' fill='#FFFFFF' stroke='#E11D48' stroke-width='1'/><text x='404.1' y='32.7' font-size='11.5' text-anchor='middle' fill='#E11D48' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>seuil de douleur</text><text x='404.1' y='143.5' font-size='14' text-anchor='middle' fill='#12305A' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>zone audible</text><text x='660' y='306' font-size='12' text-anchor='end' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-style="italic">fréquence (Hz)</text><text x='62' y='14' font-size='12' text-anchor='start' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-style="italic">niveau (dB)</text></svg></div>
<p class="nt-cap">Domaine d'audibilité d'une oreille humaine jeune (allure)&nbsp;: un son n'est perçu que si son point (fréquence, niveau) se trouve dans la zone bleue.</p>
</div>
</details>

## Testez-vous {.nt-h2}

<p class="nt-lead">Pour finir, un quiz qui balaie tout le chapitre&nbsp;: les questions sont mélangées à chaque essai, et chaque réponse est expliquée.</p>

<div class="nt-lab nt-quizlab" id="quiz-son">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur tout le chapitre</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next">Question suivante</button></div>
</div>

<script>
(function () {
  'use strict';
  /* =================== utilitaires communs =================== */
  var INK = '#1E293B', BLUE = '#2A6BC4', BLUE_LT = '#458EEC', NAVY = '#12305A', SKY = '#0284C7', AMBER = '#D97706', EMER = '#059669', ROSE = '#E11D48', SLATE = '#475569', MUTED = '#94A3B8', GRID = '#E2E8F0', GRID2 = '#CBD5E1';
  var FONT = 'system-ui, -apple-system, "Segoe UI", sans-serif';
  var RM = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  function $(r, s) { return r.querySelector(s); }
  function $$(r, s) { return Array.prototype.slice.call(r.querySelectorAll(s)); }
  function grp(s) {   /* espaces fines entre groupes de trois chiffres, de part et d'autre de la virgule */
    var p = s.split('.'), neg = p[0].charAt(0) === '-'; if (neg) { p[0] = p[0].slice(1); }
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '\u202F');
    if (p[1]) { p[1] = p[1].replace(/(\d{3})(?=\d)/g, '$1\u202F'); }
    return (neg ? '\u2212' : '') + p.join(',');
  }
  function fmt(x, d) { return grp(x.toFixed(d === undefined ? 0 : d)); }
  function sig(x, n) {   /* n chiffres significatifs */
    if (x === 0) { return '0'; }
    var e = Math.floor(Math.log10(Math.abs(x))), d = Math.max(0, n - 1 - e);
    return grp(Number(x.toPrecision(n)).toFixed(d));
  }
  function num(s) {
    s = String(s).trim().replace(/[\s\u202F\u00A0]/g, '').replace(',', '.');
    if (!/^[-+]?(\d+\.?\d*|\.\d+)(e[-+]?\d+)?$/i.test(s)) { return NaN; }
    return parseFloat(s);
  }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function typeset(el) { if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise([el]).catch(function () {}); } }
  function Canvas(cv, hFn, draw) {   /* canevas à la résolution de l'écran, redessiné au redimensionnement */
    var o = { cv: cv, W: 0, H: 0, ctx: null };
    o.size = function () {
      var dpr = window.devicePixelRatio || 1, W = cv.clientWidth || (cv.parentNode && cv.parentNode.clientWidth) || 600;
      var H = hFn(W); cv.style.height = H + 'px'; cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      o.W = W; o.H = H; o.ctx = cv.getContext('2d'); o.ctx.setTransform(dpr, 0, 0, dpr, 0, 0); draw(o);
    };
    var to; window.addEventListener('resize', function () { clearTimeout(to); to = setTimeout(o.size, 80); });
    o.size(); return o;
  }
  function Loop(el, step) {   /* boucle d'animation, suspendue quand l'élément est hors écran ; step(dt) renvoie false pour s'arrêter */
    var vis = true, on = false, want = false, last = 0;
    function frame(t) {
      if (!on) { return; }
      if (!vis) { on = false; return; }
      var dt = last ? Math.min(0.1, (t - last) / 1000) : 0; last = t;
      if (step(dt) === false) { on = false; want = false; return; }
      requestAnimationFrame(frame);
    }
    function kick() { want = true; if (on) { return; } on = true; last = 0; requestAnimationFrame(frame); }
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { vis = es[0].isIntersecting; if (vis && want) { kick(); } }).observe(el); }
    return { kick: kick, stop: function () { want = false; on = false; } };
  }
  function rr(ctx, x, y, w, h, r) {
    ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
  }
  function pill(ctx, s, x, y, o) {   /* étiquette sur pastille de fond */
    o = o || {}; var sz = o.size || 12; ctx.save(); ctx.font = (o.italic ? 'italic ' : '') + sz + 'px ' + (o.serif ? 'Georgia, serif' : FONT);
    var w = ctx.measureText(s).width + 12, h = sz + 8, x0 = o.align === 'left' ? x : (o.align === 'right' ? x - w : x - w / 2);
    rr(ctx, x0, y - h / 2, w, h, h / 2); ctx.fillStyle = o.bg || 'rgba(255,255,255,0.93)'; ctx.fill();
    if (o.stroke) { ctx.strokeStyle = o.stroke; ctx.lineWidth = 1; ctx.stroke(); }
    ctx.fillStyle = o.col || INK; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(s, x0 + w / 2, y + 0.5); ctx.restore(); return w;
  }
  function txt(ctx, s, x, y, o) {
    o = o || {}; ctx.save(); ctx.font = (o.italic ? 'italic ' : '') + (o.size || 12) + 'px ' + (o.serif ? 'Georgia, serif' : FONT);
    ctx.fillStyle = o.col || INK; ctx.textAlign = o.align || 'center'; ctx.textBaseline = o.base || 'middle'; ctx.fillText(s, x, y); ctx.restore();
  }
  function arrow(ctx, x1, y1, x2, y2, col, both, L) {   /* flèche fine, éventuellement double */
    L = L || 7; var dx = x2 - x1, dy = y2 - y1, d = Math.hypot(dx, dy) || 1, ux = dx / d, uy = dy / d;
    ctx.save(); ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = 1.2;
    ctx.beginPath(); ctx.moveTo(x1 + (both ? ux * L * 0.8 : 0), y1 + (both ? uy * L * 0.8 : 0)); ctx.lineTo(x2 - ux * L * 0.8, y2 - uy * L * 0.8); ctx.stroke();
    function hd(x, y, a, b) { ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x - a * L - b * 3.2, y - b * L + a * 3.2); ctx.lineTo(x - a * L + b * 3.2, y - b * L - a * 3.2); ctx.closePath(); ctx.fill(); }
    hd(x2, y2, ux, uy); if (both) { hd(x1, y1, -ux, -uy); }
    ctx.restore();
  }
  var AC = null;
  function audio() {
    if (!AC) { var C = window.AudioContext || window.webkitAudioContext; if (!C) { return null; } AC = new C(); }
    if (AC.state === 'suspended') { AC.resume(); }
    return AC;
  }
  /* série de questions : numéro, pastilles de progression, score, bilan */
  function Serie(root, N, api) {
    var prog = $(root, '.nt-prog'), num0 = $(root, '.nt-qnum'), sc = $(root, '.out-score'), next = $(root, '[data-act="next"]'), msg = $(root, '.nt-msg');
    var S = { k: 0, res: [], good: 0, fini: false, answered: false, N: N };
    S.progres = function () {
      var h = ''; for (var i = 0; i < N; i++) { h += '<i class="' + (S.res[i] === true ? 'ok' : (S.res[i] === false ? 'ko' : '')) + (i === S.k && !S.fini ? ' cur' : '') + '"></i>'; }
      prog.innerHTML = h; num0.textContent = S.fini ? 'Bilan' : 'Question ' + (S.k + 1) + ' sur ' + N;
    };
    S.answer = function (ok, html, pre) {
      S.answered = true; S.res[S.k] = ok; if (ok) { S.good++; }
      msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko'); msg.innerHTML = (pre || (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Pas tout à fait.</b> ')) + html; typeset(msg);
      sc.textContent = S.good + ' / ' + (S.k + 1); S.progres(); next.disabled = false; next.textContent = S.k === N - 1 ? 'Voir le bilan' : 'Question suivante';
    };
    S.go = function () { S.answered = false; msg.className = 'nt-msg'; msg.innerHTML = ''; next.disabled = true; next.textContent = S.k === N - 1 ? 'Voir le bilan' : 'Question suivante'; api.show(S.k); S.progres(); };
    S.start = function () { S.k = 0; S.res = []; S.good = 0; S.fini = false; sc.textContent = '0 / 0'; if (api.init) { api.init(); } S.go(); };
    S.say = function (html) { msg.className = 'nt-msg'; msg.innerHTML = html; };
    next.addEventListener('click', function () {
      if (S.fini) { S.start(); return; }
      if (!S.answered) { return; }
      if (S.k < N - 1) { S.k++; S.go(); }
      else {
        S.fini = true; S.progres(); msg.className = 'nt-msg'; msg.innerHTML = '';
        var r = S.good / N;
        api.bilan(S.good, r >= 0.85 ? 'Excellent&nbsp;: c\u2019est maîtrisé&nbsp;!' : (r >= 0.5 ? 'Bien. Relisez les corrections des questions manquées, puis recommencez avec de nouvelles valeurs.' : 'Relisez le cours, puis recommencez&nbsp;: les valeurs changent à chaque fois.'));
        next.textContent = 'Recommencer'; next.disabled = false;
      }
    });
    return S;
  }

  function seeded(s) { return function () { s = (s * 16807) % 2147483647; return s / 2147483647; }; }
  function poisson(x0, y0, x1, y1, r, rnd) {   /* points répartis au hasard, mais sans amas (échantillonnage de Bridson) */
    var cs = r / Math.SQRT2, gw = Math.ceil((x1 - x0) / cs), gh = Math.ceil((y1 - y0) / cs), grid = new Array(gw * gh), pts = [], act = [];
    function add(p) { pts.push(p); act.push(p); grid[Math.floor((p[0] - x0) / cs) + gw * Math.floor((p[1] - y0) / cs)] = p; }
    add([x0 + rnd() * (x1 - x0), y0 + rnd() * (y1 - y0)]);
    while (act.length) {
      var i = Math.floor(rnd() * act.length), p = act[i], found = false;
      for (var k = 0; k < 30 && !found; k++) {
        var a = rnd() * 2 * Math.PI, d = r * (1 + rnd()), q = [p[0] + d * Math.cos(a), p[1] + d * Math.sin(a)];
        if (q[0] < x0 || q[0] >= x1 || q[1] < y0 || q[1] >= y1) { continue; }
        var gx = Math.floor((q[0] - x0) / cs), gy = Math.floor((q[1] - y0) / cs), ok = true;
        for (var yy = Math.max(0, gy - 2); yy <= Math.min(gh - 1, gy + 2) && ok; yy++) {
          for (var xx = Math.max(0, gx - 2); xx <= Math.min(gw - 1, gx + 2); xx++) {
            var g = grid[xx + gw * yy]; if (g && (g[0] - q[0]) * (g[0] - q[0]) + (g[1] - q[1]) * (g[1] - q[1]) < r * r) { ok = false; break; }
          }
        }
        if (ok) { add(q); found = true; }
      }
      if (!found) { act.splice(i, 1); }
    }
    return pts;
  }

  /* =================== 1. Propagation de proche en proche =================== */
  (function () {
    var root = document.getElementById('lab-propag'); if (!root) { return; }
    var inF = $(root, '[data-in="f"]'), outF = $(root, '.out-f'), chkZ = $(root, '[data-in="zones"]'), chkS = $(root, '[data-in="suivi"]');
    var bOn = $(root, '[data-act="onoff"]'), bClap = $(root, '[data-act="clap"]'), msg = $(root, '.nt-msg');
    var C = 110, A = 6.5, XM = 58;   /* vitesse de l'onde à l'écran (px/s), amplitude (px), position de repos de la membrane */
    var T = 0, phase = 0, on = false, stopAt = -1, clapT = -1, f = 1, hist = [{ t: 0, m: 0 }], fronts = [], lastMove = -100;
    var P = [], tr = 0, cnv, top = 18, bot = 0;
    function mAt(tau) {
      if (tau <= hist[0].t) { return 0; }
      var lo = 0, hi = hist.length - 1; if (tau >= hist[hi].t) { return hist[hi].m; }
      while (hi - lo > 1) { var mid = (lo + hi) >> 1; if (hist[mid].t <= tau) { lo = mid; } else { hi = mid; } }
      var a = hist[lo], b = hist[hi]; return a.m + (b.m - a.m) * (tau - a.t) / ((b.t - a.t) || 1);
    }
    function sAt(x) { return mAt(T - (x - XM) / C); }
    function layout(o) {
      var rnd = seeded(12), r = o.W < 520 ? 10 : 11.5; bot = o.H - 10;
      P = poisson(XM + 9, top + 4, o.W - 5, bot - 4, r, rnd).map(function (p) { return { x: p[0], y: p[1], r: 2 + rnd() * 0.9, c: 0.55 + rnd() * 0.3 }; });
      var cx = XM + 0.42 * (o.W - XM), cy = (top + bot) / 2, best = 1e9;
      P.forEach(function (p, i) { var d = (p.x - cx) * (p.x - cx) + (p.y - cy) * (p.y - cy); if (d < best) { best = d; tr = i; } });
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, x; ctx.clearRect(0, 0, W, H);
      var bg = ctx.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#FFFFFF'); bg.addColorStop(1, '#F1F5F9'); ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
      if (chkZ.checked) {   /* compression locale de l'air : les tranches voisines se rapprochent */
        for (x = XM; x < W; x += 3) {
          var k = (sAt(x) - sAt(x + 3)) / 3;
          if (k > 0.03) { ctx.fillStyle = 'rgba(56,130,226,' + Math.min(0.38, k * 0.55).toFixed(3) + ')'; ctx.fillRect(x, top, 3.2, bot - top); }
        }
      }
      /* haut-parleur : enceinte, aimant, cône et membrane */
      var mm = mAt(T), cy = (top + bot) / 2, hb = (bot - top) / 2;
      var gE = ctx.createLinearGradient(0, 0, 30, 0); gE.addColorStop(0, '#334155'); gE.addColorStop(1, '#475569');
      ctx.fillStyle = gE; rr(ctx, 4, cy - hb * 0.42, 26, hb * 0.84, 6); ctx.fill();
      var gC = ctx.createLinearGradient(30, 0, XM, 0); gC.addColorStop(0, '#CBD5E1'); gC.addColorStop(1, '#F1F5F9');
      ctx.beginPath(); ctx.moveTo(30, cy - hb * 0.22); ctx.lineTo(XM + mm, top + 2); ctx.lineTo(XM + mm, bot - 2); ctx.lineTo(30, cy + hb * 0.22); ctx.closePath();
      ctx.fillStyle = gC; ctx.fill(); ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1; ctx.stroke();
      ctx.strokeStyle = NAVY; ctx.lineWidth = 3; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(XM + mm, top + 2); ctx.lineTo(XM + mm, bot - 2); ctx.stroke(); ctx.lineCap = 'butt';
      /* particules */
      for (var i = 0; i < P.length; i++) {
        if (chkS.checked && i === tr) { continue; }
        var p = P[i]; ctx.fillStyle = 'rgba(71,85,105,' + p.c.toFixed(2) + ')';
        ctx.beginPath(); ctx.arc(p.x + sAt(p.x), p.y, p.r, 0, 2 * Math.PI); ctx.fill();
      }
      if (chkS.checked) {   /* particule suivie, sa position de repos et l'étendue de son mouvement */
        var q = P[tr], xq = q.x + sAt(q.x);
        ctx.save(); ctx.strokeStyle = 'rgba(225,29,72,0.55)'; ctx.lineWidth = 1; ctx.setLineDash([2, 3]);
        ctx.beginPath(); ctx.moveTo(q.x, q.y - 22); ctx.lineTo(q.x, q.y + 22); ctx.stroke(); ctx.setLineDash([]);
        ctx.strokeStyle = 'rgba(225,29,72,0.35)'; ctx.lineWidth = 3; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(q.x - A, q.y + 14); ctx.lineTo(q.x + A, q.y + 14); ctx.stroke(); ctx.restore();
        var gh = ctx.createRadialGradient(xq, q.y, 1, xq, q.y, 11); gh.addColorStop(0, 'rgba(225,29,72,0.35)'); gh.addColorStop(1, 'rgba(225,29,72,0)');
        ctx.fillStyle = gh; ctx.beginPath(); ctx.arc(xq, q.y, 11, 0, 2 * Math.PI); ctx.fill();
        ctx.fillStyle = ROSE; ctx.beginPath(); ctx.arc(xq, q.y, 4.4, 0, 2 * Math.PI); ctx.fill();
      }
      var shown = false;
      fronts.forEach(function (t0) {
        var xf = XM + C * (T - t0); if (xf < XM + 4 || xf > W - 4) { return; } shown = true;
        ctx.save(); ctx.setLineDash([2, 4]); ctx.strokeStyle = NAVY; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(xf, top); ctx.lineTo(xf, bot); ctx.stroke(); ctx.restore();
        pill(ctx, 'front de l\u2019onde', Math.min(W - 52, Math.max(XM + 52, xf)), 10, { size: 11, col: NAVY, stroke: GRID2 });
      });
      if (!shown) { pill(ctx, 'animation très ralentie', W - 6, 10, { size: 11, col: SLATE, align: 'right', stroke: GRID }); }
    }
    function step(dt) {
      T += dt; var m = 0;
      if (on) {
        phase += 2 * Math.PI * f * dt;
        if (stopAt > 0 && phase >= stopAt) { on = false; stopAt = -1; phase = 0; bClap.disabled = false; lbl(); } else { m = A * Math.sin(phase); }
      } else if (clapT >= 0) {
        var u = (T - clapT) * f; if (u < 1) { m = A * Math.sin(2 * Math.PI * u); } else { clapT = -1; bClap.disabled = false; }
      }
      hist.push({ t: T, m: m }); if (m !== 0) { lastMove = T; }
      var keep = T - cnv.W / C - 1; while (hist.length > 2 && hist[1].t < keep) { hist.shift(); }
      fronts = fronts.filter(function (t0) { return XM + C * (T - t0) < cnv.W + 10; });
      draw(cnv);
      return on || clapT >= 0 || T - lastMove < cnv.W / C + 0.3;
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 220 : 250; }, function (o) { layout(o); draw(o); });
    var loop = Loop(root, step);
    function lbl() { bOn.innerHTML = on && stopAt < 0 ? '<i class="fa-solid fa-stop"></i>&nbsp; Arrêter le haut-parleur' : '<i class="fa-solid fa-play"></i>&nbsp; Faire vibrer le haut-parleur'; }
    bOn.addEventListener('click', function () {
      if (on && stopAt < 0) { stopAt = Math.ceil(phase / (2 * Math.PI)) * 2 * Math.PI; msg.textContent = 'La membrane s\u2019arrête… mais l\u2019onde déjà émise continue sa route\u00A0!'; }
      else if (!on) { on = true; phase = 0; stopAt = -1; clapT = -1; fronts.push(T); bClap.disabled = true; msg.textContent = 'La particule rouge oscille autour de sa position de repos (trait pointillé), sans jamais sortir du petit segment rose\u00A0: elle n\u2019avance pas avec l\u2019onde.'; loop.kick(); }
      lbl();
    });
    bClap.addEventListener('click', function () {
      if (on) { return; } clapT = T; fronts.push(T); bClap.disabled = true;
      msg.textContent = 'Une seule poussée\u00A0: une zone comprimée part vers la droite, et chaque particule revient à sa place après son passage.'; loop.kick();
    });
    function setF() { f = parseFloat(inF.value); outF.textContent = f.toFixed(1).replace('.', ',') + ' Hz'; }
    inF.addEventListener('input', setF); setF();
    [chkZ, chkS].forEach(function (c) { c.addEventListener('change', function () { draw(cnv); }); });
  })();

  /* =================== 2. Cloche à vide =================== */
  (function () {
    var root = document.getElementById('lab-cloche'); if (!root) { return; }
    var inA = $(root, '[data-in="air"]'), outA = $(root, '.out-air'), chk = $(root, '[data-in="son"]'), msg = $(root, '.nt-msg');
    var PMIN = 0.02, pr = 1, mode = 0, t = 0, cnv, snd = null;
    var rnd = seeded(5), parts = [];
    function inJar(u, v) { return v < 1.05 ? Math.abs(u) < 0.93 : u * u + (v - 1.05) * (v - 1.05) < 0.93 * 0.93; }   /* u ∈ [−1, 1], v ∈ [0, 2,05] en rayons de cloche */
    while (parts.length < 110) {
      var u0 = rnd() * 2 - 1, v0 = 0.08 + rnd() * 1.92;
      if (inJar(u0, v0)) { var a0 = rnd() * 2 * Math.PI; parts.push({ u: u0, v: v0, vu: 0.5 * Math.cos(a0), vv: 0.5 * Math.sin(a0) }); }
    }
    function geo(o) {
      var R = Math.min(84, o.W * 0.19), cx = Math.max(R + 96, o.W * 0.42), base = o.H - 50;
      return { R: R, cx: cx, base: base, cy: base - R * 0.62 };
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, g = geo(o), R = g.R, cx = g.cx, base = g.base, k;
      ctx.clearRect(0, 0, W, H);
      var bg = ctx.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#FFFFFF'); bg.addColorStop(1, '#EEF2F7'); ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
      ctx.fillStyle = '#E2E8F0'; ctx.fillRect(0, base + 22, W, H - base - 22);   /* paillasse */
      /* tuyau et pompe avec manomètre */
      ctx.strokeStyle = '#64748B'; ctx.lineWidth = 4; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(cx - R * 0.55, base + 12); ctx.lineTo(cx - R * 0.55, base + 20); ctx.lineTo(58, base + 20); ctx.stroke(); ctx.lineCap = 'butt';
      var gp = ctx.createLinearGradient(14, 0, 62, 0); gp.addColorStop(0, '#475569'); gp.addColorStop(1, '#64748B');
      ctx.fillStyle = gp; rr(ctx, 12, base - 4, 50, 36, 8); ctx.fill(); txt(ctx, 'pompe', 37, base + 14, { size: 10.5, col: '#FFFFFF' });
      var mx = 37, my = base - 30;
      ctx.fillStyle = '#FFFFFF'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(mx, my, 20, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1;
      for (k = 0; k <= 10; k++) { var an = Math.PI * (0.8 + 1.4 * k / 10); ctx.beginPath(); ctx.moveTo(mx + Math.cos(an) * 15, my + Math.sin(an) * 15); ctx.lineTo(mx + Math.cos(an) * (k % 5 ? 17 : 19), my + Math.sin(an) * (k % 5 ? 17 : 19)); ctx.stroke(); }
      var na = Math.PI * (0.8 + 1.4 * pr); ctx.strokeStyle = ROSE; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(mx, my); ctx.lineTo(mx + Math.cos(na) * 14, my + Math.sin(na) * 14); ctx.stroke();
      ctx.fillStyle = '#334155'; ctx.beginPath(); ctx.arc(mx, my, 2, 0, 2 * Math.PI); ctx.fill();
      txt(ctx, 'manomètre', mx, my - 30, { size: 10.5, col: SLATE });
      /* intérieur de la cloche : air, ondes, réveil */
      ctx.save(); ctx.beginPath(); ctx.moveTo(cx - R, base); ctx.lineTo(cx - R, base - R * 1.05); ctx.arc(cx, base - R * 1.05, R, Math.PI, 2 * Math.PI); ctx.lineTo(cx + R, base); ctx.closePath(); ctx.clip();
      var gi = ctx.createLinearGradient(cx - R, 0, cx + R, 0); gi.addColorStop(0, 'rgba(224,242,254,0.55)'); gi.addColorStop(1, 'rgba(240,249,255,0.35)'); ctx.fillStyle = gi; ctx.fillRect(cx - R, base - 2.2 * R, 2 * R, 2.2 * R);
      var N = Math.round(parts.length * pr);
      for (k = 0; k < N; k++) { var p = parts[k]; ctx.fillStyle = 'rgba(71,110,170,0.75)'; ctx.beginPath(); ctx.arc(cx + p.u * R, base - p.v * R, 2.1, 0, 2 * Math.PI); ctx.fill(); }
      var cy = g.cy, ring = RM ? 0.3 : t, vis = Math.max(0, 60 + 20 * Math.log10(pr)) / 60;   /* visibilité des ondes : selon le niveau sonore */
      for (k = 0; k < 3; k++) {
        var r = ((ring * 50 + k * 26) % 78) + 30, al = (0.35 + 0.65 * pr) * (1 - (r - 30) / 78) * 0.8;
        if (al > 0.01) { ctx.strokeStyle = 'rgba(42,107,196,' + al.toFixed(3) + ')'; ctx.lineWidth = 1.3; [-1, 1].forEach(function (sg) { ctx.beginPath(); ctx.arc(cx, cy, r, sg > 0 ? -0.55 : Math.PI - 0.55, sg > 0 ? 0.55 : Math.PI + 0.55); ctx.stroke(); }); }
      }
      ctx.restore();
      /* réveil */
      var hx = RM ? 0 : 6 * Math.sin(t * 2 * Math.PI * 9);
      [-1, 1].forEach(function (sg) {
        var gb = ctx.createRadialGradient(cx + sg * 17 - 3, cy - 31, 1, cx + sg * 17, cy - 27, 11); gb.addColorStop(0, '#FEF3C7'); gb.addColorStop(1, '#D97706');
        ctx.fillStyle = gb; ctx.beginPath(); ctx.arc(cx + sg * 17, cy - 26, 10, Math.PI, 2 * Math.PI); ctx.closePath(); ctx.fill();
      });
      ctx.strokeStyle = '#334155'; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(cx, cy - 22); ctx.lineTo(cx + hx, cy - 38); ctx.stroke();
      ctx.fillStyle = '#334155'; ctx.beginPath(); ctx.arc(cx + hx, cy - 39, 2.8, 0, 2 * Math.PI); ctx.fill();
      ctx.beginPath(); ctx.moveTo(cx - 13, cy + 19); ctx.lineTo(cx - 19, cy + 29); ctx.moveTo(cx + 13, cy + 19); ctx.lineTo(cx + 19, cy + 29); ctx.stroke();
      var gf = ctx.createRadialGradient(cx - 6, cy - 6, 2, cx, cy, 24); gf.addColorStop(0, '#FFFFFF'); gf.addColorStop(1, '#E2E8F0');
      ctx.fillStyle = '#DC2626'; ctx.beginPath(); ctx.arc(cx, cy, 24, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = gf; ctx.beginPath(); ctx.arc(cx, cy, 20.5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1; for (k = 0; k < 12; k++) { var ah = k * Math.PI / 6; ctx.beginPath(); ctx.moveTo(cx + Math.cos(ah) * 16.5, cy + Math.sin(ah) * 16.5); ctx.lineTo(cx + Math.cos(ah) * 19, cy + Math.sin(ah) * 19); ctx.stroke(); }
      ctx.strokeStyle = '#1E293B'; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - 12); ctx.moveTo(cx, cy); ctx.lineTo(cx + 9, cy + 4); ctx.stroke();
      /* cloche de verre : contour, reflets, socle */
      ctx.beginPath(); ctx.moveTo(cx - R, base); ctx.lineTo(cx - R, base - R * 1.05); ctx.arc(cx, base - R * 1.05, R, Math.PI, 2 * Math.PI); ctx.lineTo(cx + R, base);
      ctx.strokeStyle = 'rgba(14,116,144,0.55)'; ctx.lineWidth = 2; ctx.stroke();
      ctx.strokeStyle = 'rgba(255,255,255,0.9)'; ctx.lineWidth = 4; ctx.lineCap = 'round'; ctx.beginPath(); ctx.arc(cx, base - R * 1.05, R - 9, Math.PI * 1.12, Math.PI * 1.32); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx - R + 9, base - R * 0.95); ctx.lineTo(cx - R + 9, base - R * 0.35); ctx.stroke(); ctx.lineCap = 'butt';
      ctx.fillStyle = '#334155'; ctx.beginPath(); ctx.arc(cx, base - R * 2.05 - 3, 6, Math.PI, 2 * Math.PI); ctx.fill();
      var gs = ctx.createLinearGradient(0, base, 0, base + 14); gs.addColorStop(0, '#94A3B8'); gs.addColorStop(1, '#64748B');
      ctx.fillStyle = gs; rr(ctx, cx - R - 18, base, 2 * R + 36, 13, 4); ctx.fill();
      ctx.fillStyle = '#475569'; ctx.fillRect(cx - R - 4, base - 2, 2 * R + 8, 3);
      /* ondes transmises vers l'extérieur */
      var ex = cx + R + 6, room = W - ex - 70;
      for (k = 0; k < 4; k++) {
        var r2 = ((ring * 50 + k * 30) % 120) + 4, al2 = vis * (1 - r2 / 126) * 0.75;
        if (al2 > 0.01 && r2 < room) { ctx.strokeStyle = 'rgba(42,107,196,' + al2.toFixed(3) + ')'; ctx.lineWidth = 1.3; ctx.beginPath(); ctx.arc(ex - 14, cy, r2 + 14, -0.45, 0.45); ctx.stroke(); }
      }
      /* sonomètre */
      var sx = W - 50, sy = 40, sh = base - 18 - sy;
      var gm = ctx.createLinearGradient(sx, 0, sx + 30, 0); gm.addColorStop(0, '#1E293B'); gm.addColorStop(1, '#334155');
      ctx.fillStyle = gm; rr(ctx, sx, sy, 30, sh, 8); ctx.fill();
      ctx.fillStyle = '#0F172A'; rr(ctx, sx + 7, sy + 7, 16, sh - 14, 4); ctx.fill();
      var Ld = Math.max(0, 60 + 20 * Math.log10(pr)), lev = Ld / 70, hh = (sh - 18) * lev, gl = ctx.createLinearGradient(0, sy + sh - 9, 0, sy + 9); gl.addColorStop(0, '#34D399'); gl.addColorStop(0.6, '#FBBF24'); gl.addColorStop(1, '#F97316');
      ctx.fillStyle = gl; rr(ctx, sx + 9, sy + sh - 9 - Math.max(2, hh), 12, Math.max(2, hh), 3); ctx.fill();
      txt(ctx, 'son perçu', sx + 15, sy + sh + 12, { size: 10.5, col: SLATE }); pill(ctx, '\u2248\u00A0' + Math.round(Ld) + '\u00A0dB', sx + 15, sy - 12, { size: 11, col: NAVY, stroke: GRID2 });
      pill(ctx, 'pression\u00A0: ' + Math.round(pr * 100) + '\u00A0% de la pression atmosphérique', cx, 11, { size: 11, col: NAVY, stroke: GRID2 });
    }
    function setMsg() {
      msg.textContent = pr > 0.6 ? 'L\u2019air de la cloche transmet la vibration de la sonnerie jusqu\u2019à la paroi, puis à l\u2019air de la pièce.' :
        (pr > 0.06 ? 'Moins il y a d\u2019air, plus le son perçu est faible.' : 'La pompe ne fait jamais le vide parfait\u00A0: il reste de l\u2019air, dans lequel le son se propage encore. Mais la vibration passe très mal de la sonnerie à cet air raréfié, puis de cet air au verre\u00A0: le son perçu est très affaibli.');
      inA.value = Math.round(pr * 100); outA.textContent = Math.round(pr * 100) + '\u00A0%';
      if (snd) { snd.g.gain.setTargetAtTime(0.05 * pr, snd.ac.currentTime, 0.05); }
    }
    function step(dt) {
      t += dt;
      if (mode === -1) { pr = PMIN + (pr - PMIN) * Math.exp(-dt / 1.5); if (pr < PMIN + 0.003) { pr = PMIN; mode = 0; } setMsg(); }
      else if (mode === 1) { pr += (1 - pr) * (1 - Math.exp(-dt / 0.5)); if (pr > 0.995) { pr = 1; mode = 0; } setMsg(); }
      if (!RM) {
        parts.forEach(function (p) {
          var a = (Math.random() - 0.5) * 3 * dt; var c = Math.cos(a), s = Math.sin(a), vu = p.vu * c - p.vv * s; p.vv = p.vu * s + p.vv * c; p.vu = vu;   /* trajectoires un peu erratiques */
          var nu = p.u + p.vu * dt, nv = p.v + p.vv * dt;
          if (inJar(nu, nv) && nv >= 0.06) { p.u = nu; p.v = nv; }
          else { var okV = inJar(p.u, nv) && nv >= 0.06, okU = inJar(nu, p.v); if (!okV) { p.vv = -p.vv; } if (!okU) { p.vu = -p.vu; } if (okV && okU) { p.vu = -p.vu; p.vv = -p.vv; } }
        });
      }
      draw(cnv);
      return !RM || mode !== 0;
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 250 : 270; }, draw);
    var loop = Loop(root, step); if (!RM) { loop.kick(); }
    $(root, '[data-act="pomper"]').addEventListener('click', function () { mode = -1; loop.kick(); });
    $(root, '[data-act="rentrer"]').addEventListener('click', function () { mode = 1; loop.kick(); });
    inA.addEventListener('input', function () { mode = 0; pr = Math.max(PMIN, parseFloat(inA.value) / 100); setMsg(); draw(cnv); });
    chk.addEventListener('change', function () {
      if (chk.checked) {
        var ac = audio(); if (!ac) { return; }
        var o1 = ac.createOscillator(), o2 = ac.createOscillator(), amp = ac.createGain(), lfo = ac.createOscillator(), lg = ac.createGain(), gg = ac.createGain();
        o1.type = 'triangle'; o1.frequency.value = 1480; o2.type = 'sine'; o2.frequency.value = 2220; lfo.type = 'square'; lfo.frequency.value = 9; lg.gain.value = 0.5; amp.gain.value = 0.5;
        lfo.connect(lg); lg.connect(amp.gain); o1.connect(amp); o2.connect(amp); amp.connect(gg); gg.connect(ac.destination); gg.gain.value = 0;
        [o1, o2, lfo].forEach(function (o) { o.start(); }); snd = { ac: ac, g: gg, osc: [o1, o2, lfo] }; setMsg();
      } else if (snd) { var s = snd; snd = null; s.g.gain.setTargetAtTime(0, s.ac.currentTime, 0.03); setTimeout(function () { s.osc.forEach(function (o) { o.stop(); }); }, 200); }
    });
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { if (!es[0].isIntersecting && snd) { chk.checked = false; chk.dispatchEvent(new Event('change')); } }).observe(root); }
    setMsg();
  })();


  /* =================== 3. La course des signaux =================== */
  (function () {
    var root = document.getElementById('lab-course'); if (!root) { return; }
    var L = [{ n: 'lumière', v: 3e8, c: '#CA8A04', bg: '#FEF9C3' }, { n: 'son dans l\u2019acier', v: 5800, c: '#475569', bg: '#F1F5F9' }, { n: 'son dans l\u2019eau', v: 1500, c: SKY, bg: '#E0F2FE' }, { n: 'son dans l\u2019air', v: 340, c: BLUE, bg: '#DBEAFE' }];
    var bGo = $(root, '[data-act="go"]'), chk = $(root, '[data-in="ralenti"]'), calc = $(root, '.nt-calc');
    var d = 1000, t = 0, run = false, cnv;
    function tStr(x) { return x < 1e-3 ? '\u2248\u00A00\u00A0s' : (x < 0.1 ? fmt(x, 3) : fmt(x, 2)) + '\u00A0s'; }
    function laneY(i) { return i === 0 ? 52 : 108 + 42 * (i - 1); }
    function flag(ctx, x, y) {
      ctx.strokeStyle = '#334155'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(x, y + 8); ctx.lineTo(x, y - 14); ctx.stroke();
      for (var a = 0; a < 3; a++) { for (var b = 0; b < 2; b++) { ctx.fillStyle = (a + b) % 2 ? '#FFFFFF' : '#1E293B'; ctx.fillRect(x + 1 + a * 4, y - 14 + b * 4, 4, 4); } }
      ctx.strokeStyle = '#1E293B'; ctx.lineWidth = 0.6; ctx.strokeRect(x + 1, y - 14, 12, 8);
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; ctx.clearRect(0, 0, W, H);
      var bg = ctx.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#FFFFFF'); bg.addColorStop(1, '#F8FAFC'); ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
      var x0 = 16, x1 = W - (W < 520 ? 84 : 96);
      txt(ctx, 'départ', x0, 12, { size: 11, col: SLATE, align: 'left' });
      txt(ctx, 'arrivée\u00A0: ' + (d >= 1000 ? fmt(d / 1000) + '\u00A0km' : d + '\u00A0m'), x1, 12, { size: 11, col: SLATE, align: 'right' });
      ctx.fillStyle = 'rgba(254,249,195,0.45)'; rr(ctx, 6, 22, W - 12, 46, 8); ctx.fill();
      ctx.fillStyle = 'rgba(219,234,254,0.35)'; rr(ctx, 6, 80, W - 12, H - 86, 8); ctx.fill();
      L.forEach(function (l, i) {
        var y = laneY(i), ta = d / l.v, fr = run || t > 0 ? Math.min(1, t / ta) : 0, x = x0 + (x1 - x0) * fr, done = (run || t > 0) && t >= ta;
        txt(ctx, l.n, x0, y - 16, { size: 12.5, col: l.c, align: 'left' });
        ctx.fillStyle = '#E2E8F0'; rr(ctx, x0, y - 3, x1 - x0, 6, 3); ctx.fill();
        if (fr > 0) { ctx.fillStyle = l.bg; rr(ctx, x0, y - 3, Math.max(6, x - x0), 6, 3); ctx.fill(); ctx.strokeStyle = l.c; ctx.globalAlpha = 0.5; ctx.lineWidth = 1; ctx.stroke(); ctx.globalAlpha = 1; }
        flag(ctx, x1, y);
        if (fr > 0) {
          var gl = ctx.createRadialGradient(x, y, 1, x, y, 16); gl.addColorStop(0, l.c); gl.addColorStop(1, 'rgba(255,255,255,0)');
          ctx.globalAlpha = 0.35; ctx.fillStyle = gl; ctx.beginPath(); ctx.arc(x, y, 16, 0, 2 * Math.PI); ctx.fill(); ctx.globalAlpha = 1;
          if (i > 0 && !done) { ctx.strokeStyle = l.c; ctx.lineWidth = 1.2; for (var k = 1; k <= 3; k++) { ctx.globalAlpha = 1 - k * 0.25; ctx.beginPath(); ctx.arc(x - 4, y, 4 + k * 4, -0.8, 0.8); ctx.stroke(); } ctx.globalAlpha = 1; }
          ctx.fillStyle = l.c; ctx.beginPath(); ctx.arc(x, y, 5, 0, 2 * Math.PI); ctx.fill();
          pill(ctx, i === 0 ? '\u2248\u00A00\u00A0s' : tStr(Math.min(t, ta)), x1 + 18, y, { size: 12.5, col: done ? '#FFFFFF' : SLATE, bg: done ? l.c : '#FFFFFF', stroke: done ? null : GRID2, align: 'left' });
        }
      });
    }
    function bilan() {
      var ds = grp(String(d)) + '\u00A0m';
      function fr(a, b) { return '<span class="nt-fr"><span>' + a + '</span><span>' + b + '</span></span>'; }
      var h = '<p class="nt-calc-head">\u0394<i>t</i> = <i>d</i>&nbsp;/&nbsp;<i>v</i>&nbsp;: plus le signal est rapide, plus la durée du trajet est courte.</p>';
      L.slice(1).forEach(function (l) {
        h += '<div class="nt-calc-row" style="--k:' + l.c + '"><span class="nt-calc-n">' + l.n + '</span><span>\u0394<i>t</i> = ' + fr(ds, grp(String(l.v)) + '\u00A0m/s') + ' \u2248 <b>' + tStr(d / l.v) + '</b></span></div>';
      });
      h += '<div class="nt-calc-row" style="--k:#CA8A04"><span class="nt-calc-n">lumière</span><span>\u0394<i>t</i> = ' + fr(ds, '300\u202F000\u202F000\u00A0m/s') + ' \u2248 <b>' + sig(d / 3e8, 2) + '\u00A0s</b>&nbsp;: instantané à notre échelle</span></div>';
      calc.innerHTML = h;
    }
    function step(dt) {
      t += dt / (chk.checked ? 10 : 1); var tmax = d / L[3].v;
      if (t >= tmax) { t = tmax; run = false; bGo.disabled = false; bilan(); }
      draw(cnv); return run;
    }
    cnv = Canvas($(root, 'canvas'), function () { return 214; }, draw);
    var loop = Loop(root, step);
    $$(root, 'input[name="course-d"]').forEach(function (r) { r.addEventListener('change', function () { d = parseFloat(r.value); t = 0; run = false; bGo.disabled = false; calc.innerHTML = ''; draw(cnv); }); });
    bGo.addEventListener('click', function () { t = 0; run = true; bGo.disabled = true; calc.innerHTML = ''; loop.kick(); });
  })();

  /* =================== 4. Orage =================== */
  (function () {
    var root = document.getElementById('lab-orage'); if (!root) { return; }
    var bE = $(root, '[data-act="eclair"]'), chk = $(root, '[data-in="son"]'), out = $(root, '.out-chrono'), ans = $(root, '.nt-tr-ans'), inp = $(root, 'input[type="text"]'), msg = $(root, '.nt-msg');
    var st = 0, t = 0, dT = 0, xb = 0.7, bolt = [], cnv, boom = -1;   /* st : 0 repos, 1 attente du tonnerre, 2 réponse */
    function makeBolt() {
      bolt = []; var x = xb, y = 0.08; bolt.push([x, y]);
      while (y < 0.72) { y += 0.05 + Math.random() * 0.06; x += (Math.random() - 0.5) * 0.06; bolt.push([x, Math.min(y, 0.72)]); }
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, fl = st === 1 && t < 0.18 && !RM ? 1 - t / 0.18 : 0;
      var g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#0B1630'); g.addColorStop(1, '#1E3A5F'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      if (fl > 0) { ctx.fillStyle = 'rgba(219,234,254,' + (0.45 * fl).toFixed(3) + ')'; ctx.fillRect(0, 0, W, H); }
      ctx.fillStyle = '#334155'; for (var k = 0; k < 7; k++) { ctx.beginPath(); ctx.ellipse(W * (0.08 + k * 0.15), 14, W * 0.12, 26, 0, 0, 2 * Math.PI); ctx.fill(); }
      ctx.strokeStyle = 'rgba(148,163,184,0.25)'; ctx.lineWidth = 1;
      for (k = 0; k < 40; k++) { var rx = (k * 97) % W, ry = 40 + (k * 53) % (H * 0.6); ctx.beginPath(); ctx.moveTo(rx, ry); ctx.lineTo(rx - 4, ry + 12); ctx.stroke(); }
      if (st === 1 && t < 0.35) {
        ctx.save(); ctx.strokeStyle = '#F8FAFC'; ctx.lineWidth = 2; if (!RM) { ctx.shadowColor = '#BFDBFE'; ctx.shadowBlur = 14; }
        ctx.beginPath(); bolt.forEach(function (p, i) { if (i) { ctx.lineTo(p[0] * W, p[1] * H); } else { ctx.moveTo(p[0] * W, p[1] * H); } }); ctx.stroke(); ctx.restore();
      }
      ctx.fillStyle = '#0B1222'; ctx.beginPath(); ctx.moveTo(0, H); ctx.lineTo(0, H * 0.78);
      for (var x = 0; x <= W + 20; x += 20) { ctx.lineTo(x, H * 0.74 + 8 * Math.sin(x / 70) + 5 * Math.sin(x / 23)); }
      ctx.lineTo(W, H); ctx.closePath(); ctx.fill();
      var hx = 40, hy = H * 0.86; ctx.fillStyle = '#1E293B'; ctx.fillRect(hx, hy - 22, 34, 22); ctx.beginPath(); ctx.moveTo(hx - 4, hy - 22); ctx.lineTo(hx + 17, hy - 38); ctx.lineTo(hx + 38, hy - 22); ctx.fill();
      ctx.fillStyle = '#FCD34D'; ctx.fillRect(hx + 12, hy - 15, 9, 8);
      if (boom >= 0 && boom < 1.4) {
        var sh = RM ? 0 : 3 * Math.sin(boom * 60) * (1 - boom / 1.4);
        pill(ctx, 'BRRROUM…', W * 0.5 + sh, H * 0.42, { size: 18, col: '#F8FAFC', bg: 'rgba(15,23,42,0.75)' });
      }
    }
    function thunder(dist) {
      var ac = audio(); if (!ac) { return; }
      var dur = 3.6, buf = ac.createBuffer(1, Math.floor(ac.sampleRate * dur), ac.sampleRate), dd = buf.getChannelData(0), last = 0;
      for (var i = 0; i < dd.length; i++) { last = (last + 0.02 * (Math.random() * 2 - 1)) / 1.02; dd[i] = last * 3.5; }
      var src = ac.createBufferSource(), lp = ac.createBiquadFilter(), gg = ac.createGain(), t0 = ac.currentTime, pk = 0.9 / (1 + dist * 0.35);
      src.buffer = buf; lp.type = 'lowpass'; lp.frequency.value = 80 + 700 / (1 + dist * 0.5);
      gg.gain.setValueAtTime(0.0001, t0); gg.gain.exponentialRampToValueAtTime(pk, t0 + 0.06); gg.gain.exponentialRampToValueAtTime(pk * 0.35, t0 + 0.7);
      gg.gain.linearRampToValueAtTime(pk * 0.55, t0 + 1.1); gg.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
      src.connect(lp); lp.connect(gg); gg.connect(ac.destination); src.start(t0); src.stop(t0 + dur);
    }
    function step(dt) {
      if (st === 1) {
        t += dt; out.textContent = fmt(Math.min(t, dT), 1);
        if (t >= dT) { st = 2; out.textContent = fmt(dT, 1); boom = 0; if (chk.checked) { thunder(dT / 3); } ans.hidden = false; inp.value = ''; inp.focus({ preventScroll: true });
          msg.className = 'nt-msg'; msg.innerHTML = 'Le tonnerre est arrivé <b>' + fmt(dT, 1) + '&nbsp;s</b> après l\u2019éclair. À quelle distance la foudre est-elle tombée&nbsp;?'; }
      }
      if (boom >= 0) { boom += dt; if (boom > 1.4) { boom = -1; } }
      draw(cnv); return st === 1 || boom >= 0;
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 200 : 230; }, draw);
    var loop = Loop(root, step);
    bE.addEventListener('click', function () {
      if (st === 1) { return; }
      if (chk.checked) { audio(); }
      dT = Math.round(15 + Math.random() * 105) / 10; xb = 0.3 + Math.random() * 0.6; makeBolt();
      st = 1; t = 0; boom = -1; ans.hidden = true; out.textContent = '0,0'; msg.className = 'nt-msg'; msg.textContent = 'Comptez… le son est en route.'; loop.kick();
    });
    function check() {
      var u = num(inp.value), dk = 0.34 * dT;
      if (isNaN(u)) { msg.className = 'nt-msg'; msg.textContent = 'Entrez une distance en kilomètres (par exemple 2,5).'; return; }
      var ok = Math.abs(u - dk) <= 0.1 * dk;
      msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko');
      msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Pas tout à fait.</b> ') + 'Règle pratique&nbsp;: ' + fmt(dT, 1) + '&nbsp;/&nbsp;3 \u2248 ' + fmt(dT / 3, 1) + '&nbsp;km. Calcul précis&nbsp;: <i>d</i> = <i>v</i> × \u0394<i>t</i> = 340 × ' + fmt(dT, 1) + ' = ' + fmt(340 * dT) + '&nbsp;m, soit environ ' + fmt(dk, 1) + '&nbsp;km. Un nouvel éclair&nbsp;?';
    }
    $(root, '[data-act="check"]').addEventListener('click', check);
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { check(); } });
  })();

  /* =================== 5. Entraînement : vitesse, distance, durée =================== */
  (function () {
    var root = document.getElementById('tr-vitesse'); if (!root) { return; }
    var vis = $(root, '.nt-qvis'), qEl = $(root, '.nt-tr-q'), unit = $(root, '.nt-tr-unit'), inp = $(root, 'input[type="text"]'), bC = $(root, '[data-act="check"]'), zone = $(root, '.nt-tr-ans');
    var V = '<i>v</i>', D = '<i>d</i>', DT = '\u0394<i>t</i>';
    var GEN = [
      function () { var v = pick([36, 54, 72, 90, 108, 126, 144]); return { vis: v + '\u00A0km/h', q: 'Convertir cette vitesse en m/s.', u: 'm/s', a: v / 3.6, c: 'Des km/h vers les m/s, on divise par 3,6&nbsp;: ' + v + ' ÷ 3,6 = <b>' + fmt(v / 3.6) + '&nbsp;m/s</b>.' }; },
      function () { var v = pick([5, 15, 25, 40, 250, 340]); return { vis: v + '\u00A0m/s', q: 'Convertir cette vitesse en km/h.', u: 'km/h', a: v * 3.6, c: 'Des m/s vers les km/h, on multiplie par 3,6&nbsp;: ' + v + ' × 3,6 = <b>' + fmt(v * 3.6) + '&nbsp;km/h</b>.' }; },
      function () { var t = pick([2, 2.5, 3, 4.5, 6, 7.5, 9, 12]); return { vis: '\u0394<i>t</i> = ' + fmt(t, 1) + '\u00A0s', q: 'On compte la durée \u0394t entre l\u2019éclair et le tonnerre. À quelle distance la foudre est-elle tombée&nbsp;? (son dans l\u2019air&nbsp;: 340&nbsp;m/s)', u: 'm', a: 340 * t, c: 'La lumière arrive quasi instantanément, donc \u0394t est la durée de trajet du son&nbsp;: ' + D + ' = ' + V + ' × ' + DT + ' = 340 × ' + fmt(t, 1) + ' = <b>' + fmt(340 * t) + '&nbsp;m</b>.' }; },
      function () { var t = pick([0.4, 0.6, 0.8, 1.2, 1.5, 2]); return { vis: '\u0394<i>t</i> = ' + fmt(t, 1) + '\u00A0s', q: 'Face à une falaise, on crie&nbsp;: l\u2019écho revient \u0394t plus tard. À quelle distance est la falaise&nbsp;? (340&nbsp;m/s)', u: 'm', a: 340 * t / 2, c: 'Le son fait l\u2019aller-retour&nbsp;: il parcourt 2' + D + ' = ' + V + ' × ' + DT + ' = 340 × ' + fmt(t, 1) + ' = ' + fmt(340 * t) + '&nbsp;m. La falaise est donc à ' + D + ' = ' + fmt(340 * t) + ' ÷ 2 = <b>' + fmt(170 * t) + '&nbsp;m</b>.' }; },
      function () { var t = pick([0.2, 0.4, 0.6, 0.8, 1.2, 1.6]); return { vis: '\u0394<i>t</i> = ' + fmt(t, 1) + '\u00A0s', q: 'Le sonar d\u2019un bateau émet des ultrasons vers le fond&nbsp;; l\u2019écho revient \u0394t plus tard. Quelle est la profondeur&nbsp;? (son dans l\u2019eau&nbsp;: 1&nbsp;500&nbsp;m/s)', u: 'm', a: 750 * t, c: 'Aller-retour&nbsp;: 2' + D + ' = ' + V + ' × ' + DT + ' = 1&nbsp;500 × ' + fmt(t, 1) + ' = ' + fmt(1500 * t) + '&nbsp;m, donc ' + D + ' = <b>' + fmt(750 * t) + '&nbsp;m</b>.' }; },
      function () { var d = pick([290, 580, 1160, 1740, 2900]); return { vis: D + ' = ' + fmt(d) + '\u00A0m', q: 'On frappe un rail en acier. Combien de temps le son met-il pour parcourir cette distance dans le rail&nbsp;? (son dans l\u2019acier&nbsp;: 5&nbsp;800&nbsp;m/s)', u: 's', a: d / 5800, c: DT + ' = ' + D + ' / ' + V + ' = ' + fmt(d) + ' ÷ 5&nbsp;800 = <b>' + fmt(d / 5800, 2) + '&nbsp;s</b>. Dans l\u2019air, il mettrait ' + fmt(d / 340, 1) + '&nbsp;s&nbsp;!' }; },
      function () { var d = pick([85, 102, 136, 170, 204]), t = Number((d / 343).toFixed(2)), a = d / t; return { vis: D + ' = ' + d + '\u00A0m\u2003\u0394<i>t</i> = ' + fmt(t, 2) + '\u00A0s', q: 'Un son bref parcourt la distance d en une durée \u0394t. Calculer sa vitesse.', u: 'm/s', a: a, c: V + ' = ' + D + ' / ' + DT + ' = ' + d + ' ÷ ' + fmt(t, 2) + ' \u2248 <b>' + sig(a, 3) + '&nbsp;m/s</b>&nbsp;: c\u2019est bien la vitesse du son dans l\u2019air.' }; }
    ];
    var Q = [], cur = null;
    var S = Serie(root, 6, {
      init: function () { Q = shuffle(GEN.slice()).slice(0, 6).map(function (g) { return g(); }); },
      show: function (k) { cur = Q[k]; vis.innerHTML = cur.vis; qEl.innerHTML = cur.q; unit.textContent = cur.u; inp.value = ''; zone.hidden = false; bC.disabled = false; },
      bilan: function (g, txt0) { vis.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;6</span>'; qEl.innerHTML = txt0; zone.hidden = true; }
    });
    function check() {
      if (S.answered || S.fini) { return; }
      var u = num(inp.value); if (isNaN(u)) { S.say('Entrez une valeur numérique (avec une virgule ou un point).'); return; }
      bC.disabled = true; S.answer(Math.abs(u - cur.a) <= 0.03 * Math.abs(cur.a), cur.c);
    }
    bC.addEventListener('click', check); inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { check(); } });
    S.start();
  })();

  /* =================== 6. Deux microphones =================== */
  (function () {
    var root = document.getElementById('lab-micros'); if (!root) { return; }
    var inD = $(root, '[data-in="d"]'), outD = $(root, '.out-d'), bClap = $(root, '[data-act="clap"]'), zone = $(root, '.nt-tr-ans'), inp = $(root, 'input[type="text"]'), msg = $(root, '.nt-msg');
    var V = 343, d = 1.5, ts = -1, tAcq = 0, done = false, c = [1, 4], act = 0, cnv, geo = {};
    var TW = 12;   /* fenêtre d'acquisition : 12 ms */
    function pulse(tau) { return tau <= 0 ? 0 : Math.exp(-tau / 0.55) * Math.sin(2 * Math.PI * 2.1 * tau) * (1 - Math.exp(-tau / 0.05)); }   /* tau en ms */
    var noise = []; for (var i = 0; i < 400; i++) { noise.push((Math.random() - 0.5) * 0.04); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; ctx.clearRect(0, 0, W, H);
      var sx0 = 60, sx1 = W - 30, sc = (sx1 - 110) / 3, ym = 52, m1 = 110, m2 = 110 + d * sc;
      /* scène */
      ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, 104);
      txt(ctx, '\u270B', 46, ym, { size: 22 });
      [m1, m2].forEach(function (x, k) {
        ctx.fillStyle = '#E2E8F0'; ctx.strokeStyle = INK; ctx.lineWidth = 1; rr(ctx, x - 7, ym - 12, 14, 24, 7); ctx.fill(); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x, ym + 12); ctx.lineTo(x, ym + 30); ctx.stroke(); txt(ctx, 'micro ' + (k + 1), x, ym + 40, { size: 11, col: k ? ROSE : SKY });
      });
      arrow(ctx, m1, 16, m2, 16, SLATE, true, 6); pill(ctx, 'd = ' + fmt(d, 1) + '\u00A0m', (m1 + m2) / 2, 16, { size: 11, col: SLATE });
      /* oscillogrammes */
      var k, gx0 = 12, gx1 = W - 12, gy0 = 112, gy1 = H - 24, nd = TW, dx = (gx1 - gx0) / nd, hh = (gy1 - gy0) / 2;
      geo = { gx0: gx0, gx1: gx1, gy0: gy0, gy1: gy1, dx: dx };
      ctx.fillStyle = '#F8FAFC'; ctx.fillRect(gx0, gy0, gx1 - gx0, gy1 - gy0);
      ctx.strokeStyle = GRID; ctx.lineWidth = 0.8;
      for (k = 0; k <= nd; k++) { ctx.beginPath(); ctx.moveTo(gx0 + k * dx, gy0); ctx.lineTo(gx0 + k * dx, gy1); ctx.stroke(); }
      ctx.strokeStyle = GRID2; ctx.beginPath(); ctx.moveTo(gx0, gy0 + hh); ctx.lineTo(gx1, gy0 + hh); ctx.stroke();
      txt(ctx, '1 division \u2194 1 ms', gx1, H - 9, { size: 11, col: SLATE, align: 'right' });
      if (ts >= 0) {
        var shown = done ? TW : Math.min(TW, tAcq), dl = d / V * 1000;
        [[0, SKY, 1, 0.5], [dl, ROSE, 0.7, 1.5]].forEach(function (s0) {
          var yc = gy0 + hh * s0[3]; ctx.strokeStyle = s0[1]; ctx.lineWidth = 1.4; ctx.beginPath();
          for (var px = 0; px <= (gx1 - gx0) * shown / TW; px++) {
            var tm = px / dx, u = s0[2] * pulse(tm - 0.5 - s0[0]) + noise[px % 400];
            var y = yc - u * hh * 0.4; if (px) { ctx.lineTo(gx0 + px, y); } else { ctx.moveTo(gx0 + px, y); }
          }
          ctx.stroke();
        });
      }
      if (done) {
        c.forEach(function (cc, k) {
          var x = gx0 + cc * dx; ctx.strokeStyle = k ? ROSE : SKY; ctx.lineWidth = 1.2; ctx.setLineDash(k === act ? [] : [4, 3]);
          ctx.beginPath(); ctx.moveTo(x, gy0); ctx.lineTo(x, gy1); ctx.stroke(); ctx.setLineDash([]);
          ctx.fillStyle = k ? ROSE : SKY; ctx.beginPath(); ctx.moveTo(x - 5, gy0 - 8); ctx.lineTo(x + 5, gy0 - 8); ctx.lineTo(x, gy0); ctx.closePath(); ctx.fill();
        });
        pill(ctx, '\u0394t = ' + fmt(Math.abs(c[1] - c[0]), 2) + '\u00A0ms', (gx0 + gx1) / 2, gy0 + hh, { size: 12, col: NAVY, stroke: GRID2 });
      }
      if (ts >= 0) { pill(ctx, 'voie 1', gx1 - 4, gy0 + 11, { size: 11, col: SKY, align: 'right' }); pill(ctx, 'voie 2', gx1 - 4, gy0 + hh + 11, { size: 11, col: ROSE, align: 'right' }); }
      if (ts >= 0 && !done) {   /* onde du claquement, au ralenti, par-dessus tout le reste */
        var xr = m1 + (tAcq - 0.5) * V / 1000 * sc;
        for (var k2 = 0; k2 < 3; k2++) { var r = xr - 46 - k2 * 8; if (r > 6) { ctx.strokeStyle = 'rgba(42,107,196,' + (0.75 - k2 * 0.22) + ')'; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(46, ym, r, -1.25, 1.25); ctx.stroke(); } }
        pill(ctx, 'onde au ralenti', W - 8, ym + 38, { size: 11, col: SLATE, align: 'right', stroke: GRID });
      }
    }
    function step(dt) {
      tAcq += dt * 1000 / 300;   /* ralenti × 300 */
      if (tAcq >= TW) { done = true; zone.hidden = false; msg.className = 'nt-msg'; msg.textContent = 'Placez les curseurs au même endroit des deux signaux (par exemple au début, ou au premier pic), lisez \u0394t, puis calculez v.'; }
      draw(cnv); return !done;
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 270 : 300; }, draw);
    var loop = Loop(root, step);
    function setD() { d = parseFloat(inD.value); outD.textContent = fmt(d, 1) + '\u00A0m'; ts = -1; done = false; zone.hidden = true; draw(cnv); }
    inD.addEventListener('input', setD); setD();
    bClap.addEventListener('click', function () { ts = 0; tAcq = RM ? TW : 0; done = false; c = [1, 4]; zone.hidden = true; inp.value = ''; msg.className = 'nt-msg'; msg.textContent = 'Acquisition…'; if (RM) { step(0); } else { loop.kick(); } });
    var cv = $(root, 'canvas'), drag = -1;
    function at(e) { var r = cv.getBoundingClientRect(); return (e.clientX - r.left - geo.gx0) / geo.dx; }
    cv.addEventListener('pointerdown', function (e) { if (!done) { return; } var x = at(e); drag = Math.abs(x - c[0]) <= Math.abs(x - c[1]) ? 0 : 1; act = drag; c[drag] = Math.max(0, Math.min(TW, x)); cv.setPointerCapture(e.pointerId); draw(cnv); });
    cv.addEventListener('pointermove', function (e) { if (drag < 0) { return; } c[drag] = Math.max(0, Math.min(TW, at(e))); draw(cnv); });
    cv.addEventListener('pointerup', function () { drag = -1; });
    cv.addEventListener('keydown', function (e) {
      if (!done || (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight')) { return; } e.preventDefault(); act = e.shiftKey ? 1 : 0;
      c[act] = Math.max(0, Math.min(TW, c[act] + (e.key === 'ArrowRight' ? 0.02 : -0.02))); draw(cnv);
    });
    function check() {
      var u = num(inp.value), dt = Math.abs(c[1] - c[0]);
      if (isNaN(u)) { msg.className = 'nt-msg'; msg.textContent = 'Entrez une vitesse en m/s.'; return; }
      if (dt < 0.05) { msg.className = 'nt-msg'; msg.textContent = 'Placez d\u2019abord les deux curseurs pour mesurer \u0394t.'; return; }
      var vm = d / (dt / 1000), okCalc = Math.abs(u - vm) <= 0.03 * vm, okMes = Math.abs(vm - V) <= 0.05 * V;
      var h = 'Avec \u0394t = ' + fmt(dt, 2) + '&nbsp;ms = ' + sig(dt / 1000, 3) + '&nbsp;s&nbsp;: <i>v</i> = <i>d</i> / \u0394<i>t</i> = ' + fmt(d, 1) + ' ÷ ' + sig(dt / 1000, 3) + ' \u2248 ' + sig(vm, 3) + '&nbsp;m/s. ';
      h += okMes ? 'Votre mesure est proche de la valeur attendue (' + V + '&nbsp;m/s dans l\u2019air à 20&nbsp;°C).' : 'Attendu&nbsp;: environ ' + V + '&nbsp;m/s dans l\u2019air à 20&nbsp;°C. Vérifiez que les deux curseurs sont au même endroit des deux signaux (le début de chaque signal, ou le premier pic).';
      msg.className = 'nt-msg nt-fb ' + (okCalc && okMes ? 'ok' : 'ko'); msg.innerHTML = (okCalc ? (okMes ? '<b>Bravo&nbsp;!</b> ' : '<b>Calcul juste, mesure à revoir.</b> ') : '<b>Revoyez le calcul</b> (attention à convertir \u0394t en secondes). ') + h;
    }
    $(root, '[data-act="check"]').addEventListener('click', check); inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { check(); } });
  })();

  /* formes de signaux : coefficients des sinusoïdes de fréquences f, 2f, 3f… (les mêmes pour le dessin et pour le son) */
  var FORMES = {
    sin: { nom: 'sinusoïde (son pur)', co: [1] },
    flute: { nom: 'flûte', co: [1, 0.35, 0.12, 0.05] },
    clar: { nom: 'clarinette', co: [1, 0, 0.55, 0, 0.35, 0, 0.22, 0, 0.12] },
    violon: { nom: 'violon', co: [1, 0.45, 0.3, 0.22, 0.17, 0.13, 0.1, 0.08, 0.07, 0.06, 0.05, 0.04] }
  };
  Object.keys(FORMES).forEach(function (k) {   /* normalisation : valeur maximale 1 */
    var co = FORMES[k].co, mx = 0, th0 = 0;
    for (var i = 0; i < 2000; i++) { var th = 2 * Math.PI * i / 2000, u = 0; for (var n = 0; n < co.length; n++) { u += co[n] * Math.sin((n + 1) * th); } if (u > mx) { mx = u; th0 = th; } }
    FORMES[k].mx = mx; FORMES[k].thMax = th0;
    FORMES[k].u = function (th) { var u = 0; for (var n = 0; n < co.length; n++) { u += co[n] * Math.sin((n + 1) * th); } return u / mx; };
  });
  function grille(ctx, x0, y0, x1, y1, nx, ny) {   /* quadrillage d'oscilloscope : fin, plus axe central */
    ctx.fillStyle = '#FFFFFF'; ctx.fillRect(x0, y0, x1 - x0, y1 - y0);
    ctx.strokeStyle = GRID; ctx.lineWidth = 0.8; var i;
    for (i = 0; i <= nx; i++) { var x = x0 + (x1 - x0) * i / nx; ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x, y1); ctx.stroke(); }
    for (i = 0; i <= ny; i++) { var y = y0 + (y1 - y0) * i / ny; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke(); }
    ctx.strokeStyle = GRID2; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(x0, (y0 + y1) / 2); ctx.lineTo(x1, (y0 + y1) / 2); ctx.stroke();
  }

  /* =================== 7. Périodique ou non ? =================== */
  (function () {
    var root = document.getElementById('lab-motif'); if (!root) { return; }
    var chk = $(root, '[data-in="piege"]'), msg = $(root, '.nt-msg'), kind = 'note', show = false, cnv;
    var seed = 3; function rnd() { seed = (seed * 16807) % 2147483647; return seed / 2147483647; }
    var NZ = []; for (var i = 0; i < 18; i++) { NZ.push([3 + rnd() * 45, 0.4 + rnd(), rnd() * 6.28]); }
    function noise0(u) { var s = 0; NZ.forEach(function (c) { s += c[1] * Math.sin(2 * Math.PI * c[0] * u + c[2]); }); return s; }
    var zmx = 0; for (var q0 = 0; q0 <= 2000; q0++) { zmx = Math.max(zmx, Math.abs(noise0(q0 / 2000))); }
    function noise(u) { return noise0(u) / zmx; }
    function note0(th) { return Math.sin(th) + 0.45 * Math.sin(2 * th + 0.6) + 0.25 * Math.sin(3 * th + 1.2); }
    var nmx = 0; for (var q = 0; q < 1000; q++) { nmx = Math.max(nmx, Math.abs(note0(2 * Math.PI * q / 1000))); }
    function note(th) { return note0(th) / nmx; }
    var u0 = note(0), thB = 0; for (var th = 0.05; th < 2 * Math.PI; th += 0.001) { if ((note(th) - u0) * (note(th - 0.001) - u0) <= 0) { thB = th; break; } }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; ctx.clearRect(0, 0, W, H);
      var x0 = 14, x1 = W - 14, y0 = 26, y1 = H - 30, ym = (y0 + y1) / 2, a = (y1 - y0) * 0.42, Tp = (x1 - x0) / 4.2, xs = x0 + 0.35 * Tp;
      grille(ctx, x0, y0, x1, y1, 12, 6);
      txt(ctx, 'temps', x1, H - 12, { size: 11, col: SLATE, align: 'right', italic: true });
      function U(x) { return kind === 'note' ? note(2 * Math.PI * (x - xs) / Tp) : noise((x - x0) / (x1 - x0)); }
      var segs = [];
      if (show && kind === 'note') { segs.push([x0, xs, MUTED]); for (var k = 0; xs + k * Tp < x1; k++) { segs.push([xs + k * Tp, Math.min(x1, xs + (k + 1) * Tp), k % 2 ? AMBER : BLUE]); } }
      else { segs.push([x0, x1, kind === 'note' ? BLUE : SLATE]); }
      segs.forEach(function (s) { ctx.strokeStyle = s[2]; ctx.lineWidth = 1.6; ctx.beginPath(); for (var x = s[0]; x <= s[1]; x += 1) { var y = ym - a * U(x); if (x === s[0]) { ctx.moveTo(x, y); } else { ctx.lineTo(x, y); } } ctx.stroke(); });
      if (show && kind === 'note') {
        arrow(ctx, xs, y0 - 12, xs + Tp, y0 - 12, NAVY, true, 6); pill(ctx, 'T', xs + Tp / 2, y0 - 12, { size: 13, col: NAVY, serif: true, italic: true });
        arrow(ctx, xs + Tp, y0 - 12, xs + 2 * Tp, y0 - 12, NAVY, true, 6); pill(ctx, 'T', xs + 1.5 * Tp, y0 - 12, { size: 13, col: NAVY, serif: true, italic: true });
      }
      if (chk.checked && kind === 'note') {
        var yA = ym - a * u0, xB = xs + thB / (2 * Math.PI) * Tp, xC = xs + Tp;
        ctx.save(); ctx.setLineDash([2, 3]); ctx.strokeStyle = SLATE; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(x0, yA); ctx.lineTo(x1, yA); ctx.stroke(); ctx.restore();
        [[xs, EMER, 'A'], [xB, ROSE, 'B'], [xC, EMER, 'C']].forEach(function (p) { ctx.fillStyle = p[1]; ctx.beginPath(); ctx.arc(p[0], yA, 4.5, 0, 2 * Math.PI); ctx.fill(); pill(ctx, p[2], p[0] - 12, yA - 14, { size: 12, col: p[1] }); });
        arrow(ctx, xs, y1 + 9, xB, y1 + 9, ROSE, true, 5); arrow(ctx, xs, y1 + 22, xC, y1 + 22, EMER, true, 5);
        txt(ctx, 'même valeur, mais pas une période', xB + 8, y1 + 9, { size: 11, col: ROSE, align: 'left' }); txt(ctx, 'une période', xC + 8, y1 + 22, { size: 11, col: EMER, align: 'left' });
      }
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 200 : 230; }, draw);
    function say() {
      if (chk.checked && kind === 'note') { msg.innerHTML = 'Les points A et B ont la même valeur, mais le signal <b>monte</b> en A et <b>descend</b> en B&nbsp;: ils ne se correspondent pas. Le point qui correspond à A est C&nbsp;: la période est la durée de A à C.'; return; }
      if (!show) { msg.textContent = ''; return; }
      msg.innerHTML = kind === 'note' ? 'Le même motif se répète à l\u2019identique&nbsp;: le signal est <b>périodique</b>, et sa période <i>T</i> est la durée d\u2019un motif.' : 'Aucun motif ne se répète à l\u2019identique&nbsp;: ce signal n\u2019est <b>pas périodique</b> (c\u2019est un bruit). Il n\u2019a ni période ni fréquence.';
    }
    $(root, '[data-act="motifs"]').addEventListener('click', function () { show = !show; say(); draw(cnv); });
    $$(root, 'input[name="motif-s"]').forEach(function (r) { r.addEventListener('change', function () { kind = r.value; say(); draw(cnv); }); });
    chk.addEventListener('change', function () { say(); draw(cnv); });
  })();

  /* =================== 8. Entraînement : période sur un oscillogramme =================== */
  (function () {
    var root = document.getElementById('tr-oscillo'); if (!root) { return; }
    var cv = $(root, 'canvas'), qEl = $(root, '.nt-tr-q'), inT = $(root, '#osc-T'), inF = $(root, '#osc-f'), bC = $(root, '[data-act="check"]'), zone = $(root, '.nt-tr-ans');
    var P = null, c = [0.5, 2.5], act = 0, corr = false, fini = false, cnv, geo = {};
    function gen() {
      var b = pick([0.2, 0.5, 1, 2]), n = pick([2, 3, 4, 5]), S = pick([6, 7, 8, 9]);
      return { b: b, n: n, S: S, T: S * b / n, t0: Math.random() * (10 - S) * b, A: 2 + Math.random() * 1.4, sh: pick(['sin', 'flute', 'clar', 'violon']) };
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; ctx.clearRect(0, 0, W, H); if (!P) { return; }
      var x0 = 8, x1 = W - 8, y0 = 22, y1 = H - 26, gx = (x1 - x0) / 10, gy = (y1 - y0) / 8, ym = (y0 + y1) / 2; geo = { x0: x0, gx: gx };
      grille(ctx, x0, y0, x1, y1, 10, 8);
      if (fini) { return; }
      var xc1 = x0 + Math.min(c[0], c[1]) * gx, xc2 = x0 + Math.max(c[0], c[1]) * gx;   /* durée entre les curseurs, en surbrillance */
      ctx.fillStyle = 'rgba(250,204,21,0.18)'; ctx.fillRect(xc1, y0, xc2 - xc1, y1 - y0);
      if (xc2 - xc1 > 24) { arrow(ctx, xc1, y0 + 9, xc2, y0 + 9, '#A16207', true, 5); }
      var F = FORMES[P.sh]; ctx.strokeStyle = BLUE; ctx.lineWidth = 1.6; ctx.beginPath();
      for (var x = x0; x <= x1; x += 0.5) { var t = (x - x0) / gx * P.b, y = ym - P.A * gy * F.u(2 * Math.PI * (t - P.t0) / P.T); if (x === x0) { ctx.moveTo(x, y); } else { ctx.lineTo(x, y); } }
      ctx.stroke();
      txt(ctx, '1 division \u2194 ' + fmt(P.b, P.b < 1 ? 1 : 0) + '\u00A0ms', x1, H - 10, { size: 12, col: SLATE, align: 'right' });
      if (corr) {
        var xa = x0 + P.t0 / P.b * gx, xb = xa + P.S * gx;
        for (var k = 0; k <= P.n; k++) { ctx.fillStyle = EMER; ctx.beginPath(); ctx.arc(xa + k * P.T / P.b * gx, ym, 4, 0, 2 * Math.PI); ctx.fill(); }
        arrow(ctx, xa, y1 - 10, xb, y1 - 10, EMER, true, 6); pill(ctx, P.n + '\u00A0T = ' + P.S + '\u00A0div', (xa + xb) / 2, y1 - 10, { size: 12, col: EMER, stroke: '#A7F3D0' });
      }
      c.forEach(function (cc, k) {
        var xc = x0 + cc * gx, col = k ? ROSE : SKY; ctx.strokeStyle = col; ctx.lineWidth = 1.2; ctx.setLineDash(k === act ? [] : [4, 3]);
        ctx.beginPath(); ctx.moveTo(xc, y0); ctx.lineTo(xc, y1); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = col; ctx.beginPath(); ctx.moveTo(xc - 5, y0 - 9); ctx.lineTo(xc + 5, y0 - 9); ctx.lineTo(xc, y0 - 1); ctx.closePath(); ctx.fill();
      });
      pill(ctx, (W < 520 ? '\u0394t = ' : '\u0394t entre les curseurs = ') + sig(Math.abs(c[1] - c[0]) * P.b, 3) + '\u00A0ms', x0, H - 11, { size: 11.5, col: '#A16207', bg: '#FEF9C3', align: 'left', stroke: '#FDE68A' });
    }
    cnv = Canvas(cv, function (W) { return W < 520 ? 230 : 270; }, draw);
    function at(e) { var r = cv.getBoundingClientRect(); return Math.max(0, Math.min(10, (e.clientX - r.left - geo.x0) / geo.gx)); }
    var drag = -1;
    cv.addEventListener('pointerdown', function (e) { if (fini) { return; } var x = at(e); drag = Math.abs(x - c[0]) <= Math.abs(x - c[1]) ? 0 : 1; act = drag; c[drag] = x; cv.setPointerCapture(e.pointerId); draw(cnv); });
    cv.addEventListener('pointermove', function (e) { if (drag < 0) { return; } c[drag] = at(e); draw(cnv); });
    cv.addEventListener('pointerup', function () { drag = -1; });
    cv.addEventListener('keydown', function (e) {
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') { return; } e.preventDefault(); act = e.shiftKey ? 1 : 0;
      c[act] = Math.max(0, Math.min(10, c[act] + (e.key === 'ArrowRight' ? 0.02 : -0.02))); draw(cnv);
    });
    var S = Serie(root, 6, {
      show: function () {
        P = gen(); c = [0.5, 2.5]; act = 0; corr = false; fini = false; zone.hidden = false; inT.value = ''; inF.value = ''; bC.disabled = false;
        qEl.innerHTML = 'Mesurez la période <i>T</i> de ce signal (en ms), puis calculez sa fréquence <i>f</i> (en Hz).'; draw(cnv);
      },
      bilan: function (g, t0) { fini = true; zone.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;6</span><br>' + t0; draw(cnv); }
    });
    function check() {
      if (S.answered || S.fini) { return; }
      var T = num(inT.value), f = num(inF.value);
      if (isNaN(T) || isNaN(f)) { S.say('Entrez la période (en ms) et la fréquence (en Hz).'); return; }
      var fT = 1000 / P.T, okT = Math.abs(T - P.T) <= 0.03 * P.T, okF = Math.abs(f - fT) <= 0.03 * fT;
      var h = 'Ici, ' + P.n + ' motifs complets occupent ' + P.S + '&nbsp;divisions (points verts)&nbsp;: ' + P.n + '&nbsp;<i>T</i> = ' + P.S + ' × ' + fmt(P.b, P.b < 1 ? 1 : 0) + '&nbsp;ms = ' + sig(P.S * P.b, 3) + '&nbsp;ms, donc <i>T</i> = ' + sig(P.S * P.b, 3) + '&nbsp;/&nbsp;' + P.n + ' = ' + sig(P.T, 3) + '&nbsp;ms = ' + sig(P.T / 1000, 3) + '&nbsp;s. ';
      h += 'Puis <i>f</i> = 1&nbsp;/&nbsp;<i>T</i> = 1&nbsp;/&nbsp;' + sig(P.T / 1000, 3) + ' \u2248 <b>' + sig(fT, 3) + '&nbsp;Hz</b>.';
      var pre = okT && okF ? null : (okT ? '<b>Période juste, fréquence fausse.</b> Pour obtenir des hertz, il faut exprimer la période en secondes. ' : null);
      corr = true; bC.disabled = true; draw(cnv); S.answer(okT && okF, h, pre);
    }
    bC.addEventListener('click', check);
    [inT, inF].forEach(function (i) { i.addEventListener('keydown', function (e) { if (e.key === 'Enter') { check(); } }); });
    S.start();
  })();

  /* =================== 9. Signal lumineux à chronométrer =================== */
  (function () {
    var root = document.getElementById('lab-feu'); if (!root) { return; }
    var TT = 5.3, NBEAUCOUP = 5;
    var out = $(root, '.out-chrono'), bCh = $(root, '[data-act="chrono"]'), inN = $(root, '#feu-n'), msg = $(root, '.nt-msg'), chk = $(root, '[data-in="frise"]'), cvF = $(root, '.nt-frise');
    var t = 0.4, run = false, t1 = null, t2 = null, cnv, cnvF = null;
    function teinte(tt) { var u = ((tt % TT) + TT) % TT / TT; return ((120 - 360 * u) % 360 + 360) % 360; }   /* vert → jaune → rouge → magenta → bleu → cyan → vert */
    function coul(tt, l) { return 'hsl(' + teinte(tt).toFixed(1) + ', 88%, ' + (l || 52) + '%)'; }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, cx = W / 2, cy = H / 2, r = Math.min(W, H) * 0.3; ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = '#1E293B'; rr(ctx, cx - r - 16, cy - r - 16, 2 * r + 32, 2 * r + 32, 18); ctx.fill();
      var g = ctx.createRadialGradient(cx, cy, r * 0.3, cx, cy, r * 1.45); g.addColorStop(0, coul(t, 60)); g.addColorStop(1, 'rgba(30,41,59,0)');
      ctx.globalAlpha = 0.55; ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, r * 1.45, 0, 2 * Math.PI); ctx.fill(); ctx.globalAlpha = 1;
      var g2 = ctx.createRadialGradient(cx - r * 0.3, cy - r * 0.3, r * 0.1, cx, cy, r); g2.addColorStop(0, coul(t, 78)); g2.addColorStop(1, coul(t, 48));
      ctx.fillStyle = g2; ctx.beginPath(); ctx.arc(cx, cy, r, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#0F172A'; ctx.lineWidth = 1; ctx.stroke();
    }
    function drawF(o) {   /* enregistrement de la couleur au cours des 12 dernières secondes */
      var ctx = o.ctx, W = o.W, H = o.H, x0 = 12, x1 = W - 12, span = 12, y0 = 16, h = 26; ctx.clearRect(0, 0, W, H);
      function X(tt) { return x1 - (t - tt) / span * (x1 - x0); }
      for (var px = x0; px < x1; px += 1) { ctx.fillStyle = coul(t - (x1 - px) / (x1 - x0) * span); ctx.fillRect(px, y0, 1.2, h); }
      ctx.strokeStyle = GRID2; ctx.lineWidth = 1; ctx.strokeRect(x0, y0, x1 - x0, h);
      for (var k = 0; k <= span; k++) { var x = X(t - k); ctx.strokeStyle = GRID2; ctx.beginPath(); ctx.moveTo(x, y0 + h); ctx.lineTo(x, y0 + h + 5); ctx.stroke(); if (k % 2 === 0) { txt(ctx, k ? '\u2212' + k + '\u00A0s' : 'maintenant', x, y0 + h + 15, { size: 10.5, col: SLATE, align: k === span ? 'left' : (k ? 'center' : 'right') }); } }
      [[t1, 'départ'], [t2, 'arrêt']].forEach(function (m) { if (m[0] === null) { return; } var x = X(m[0]); if (x < x0 || x > x1) { return; } ctx.strokeStyle = NAVY; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(x, y0 - 4); ctx.lineTo(x, y0 + h + 2); ctx.stroke(); pill(ctx, m[1], x, 7, { size: 10.5, col: NAVY }); });
    }
    function step(dt) {
      t += dt; draw(cnv); if (cnvF && !cvF.hidden) { drawF(cnvF); }
      if (run) { out.textContent = fmt(t - t1, 2); }
      return true;
    }
    cnv = Canvas($(root, '.nt-lamp canvas'), function (W) { return Math.min(190, Math.max(150, W * 0.8)); }, draw);
    var loop = Loop(root, step); loop.kick();
    chk.addEventListener('change', function () { cvF.hidden = !chk.checked; if (chk.checked) { if (!cnvF) { cnvF = Canvas(cvF, function () { return 62; }, drawF); } else { cnvF.size(); } } });
    bCh.addEventListener('click', function () {
      if (!run) { run = true; t1 = t; t2 = null; bCh.innerHTML = '<i class="fa-solid fa-stop"></i>&nbsp; Arrêter'; msg.className = 'nt-msg'; msg.textContent = 'Comptez les motifs complets (un tour complet des couleurs)…'; }
      else { run = false; t2 = t; out.textContent = fmt(t2 - t1, 2); bCh.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Démarrer'; msg.className = 'nt-msg'; msg.textContent = 'Indiquez le nombre de motifs complets chronométrés, puis calculez.'; inN.focus({ preventScroll: true }); }
    });
    $(root, '[data-act="zero"]').addEventListener('click', function () { run = false; t1 = t2 = null; out.textContent = '0,00'; bCh.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Démarrer'; msg.className = 'nt-msg'; msg.textContent = ''; });
    function calc() {
      var n = num(inN.value);
      if (t1 === null || t2 === null) { msg.className = 'nt-msg'; msg.textContent = 'Démarrez puis arrêtez d\u2019abord le chronomètre.'; return; }
      if (!(n >= 1) || Math.round(n) !== n) { msg.className = 'nt-msg'; msg.textContent = 'Le nombre de motifs doit être un nombre entier (1, 2, 3…).'; return; }
      var D = t2 - t1, T = D / n, e = Math.abs(T - TT), cls;
      var h = '<i>T</i> = \u0394<i>t</i>&nbsp;/&nbsp;<i>n</i> = ' + fmt(D, 2) + '&nbsp;/&nbsp;' + n + ' \u2248 ' + fmt(T, 2) + '&nbsp;s, puis <i>f</i> = 1&nbsp;/&nbsp;<i>T</i> \u2248 ' + sig(1 / T, 2) + '&nbsp;Hz. ';
      h += 'Valeur exacte&nbsp;: <i>T</i> = 5,30&nbsp;s, <i>f</i> \u2248 0,189&nbsp;Hz (écart sur <i>T</i>&nbsp;: ' + fmt(e, 2) + '&nbsp;s). ';
      var incert = 'L\u2019incertitude sur le départ et sur l\u2019arrêt est ici un peu plus grande que le temps de réaction (environ 0,2&nbsp;s)&nbsp;: comme la couleur change continûment, il est difficile de repérer exactement la même teinte au départ et à l\u2019arrivée. ';
      if (e <= 0.1) {
        cls = 'ok'; h = '<b>Belle mesure&nbsp;!</b> ' + h + incert + (n > 1 ? 'En chronométrant ' + n + ' motifs, vous l\u2019avez divisée par ' + n + '.' : 'Vous avez eu un peu de chance avec un seul motif&nbsp;: en chronométrant plusieurs motifs, la précision serait meilleure à coup sûr.');
      } else if (e <= 0.3) {
        cls = 'warn';
        h = !(n >= NBEAUCOUP && e > 0.6 / n) ? '<b>Précision améliorable.</b> ' + h + incert + 'Recommencez en chronométrant plus de motifs&nbsp;: cette incertitude sera divisée par le nombre de motifs.'
          : '<b>Erreur de mesure probable.</b> ' + h + 'Avec ' + n + ' motifs, l\u2019incertitude due au déclenchement du chronomètre ne devrait laisser qu\u2019un écart d\u2019environ ' + fmt(0.6 / n, 2) + '&nbsp;s au plus. Vérifiez que vous arrêtez le chronomètre exactement sur la même teinte qu\u2019au départ, et que le nombre de motifs comptés est juste.';
      } else {
        cls = 'ko'; h = '<b>Écart important.</b> ' + h + 'Avez-vous bien compté les motifs complets&nbsp;? Un motif, c\u2019est un tour complet des couleurs, par exemple du vert au vert suivant. Vérifiez aussi que vous repartez de la même teinte.';
      }
      msg.className = 'nt-msg nt-fb ' + cls; msg.innerHTML = h;
    }
    $(root, '[data-act="calc"]').addEventListener('click', calc); inN.addEventListener('keydown', function (e) { if (e.key === 'Enter') { calc(); } });
  })();

  /* =================== 10. Générateur de sons =================== */
  /* synthèse réaliste d'une note de piano ou de violon (le même signal sert au son et au tracé) */
  var SYN = (function () {
    var SR = 44100, DUR = 2.2, TOFF = 1.6, N = Math.round(DUR * SR);
    function normalise(o) { var mx = 0, i; for (i = 0; i < o.length; i++) { mx = Math.max(mx, Math.abs(o[i])); } if (mx > 0) { for (i = 0; i < o.length; i++) { o[i] *= 0.9 / mx; } } return o; }
    function partiel(o, f, a, ka, kb, fa) {   /* sinusoïde (rotation pas à pas) d'amplitude a·[fa·ka^i + (1 − fa)·kb^i] */
      var w = 2 * Math.PI * f / SR, c = Math.cos(w), s = Math.sin(w), ph = Math.random() * 2 * Math.PI, x = Math.cos(ph), y = Math.sin(ph), ea = a * fa, eb = a * (1 - fa);
      for (var i = 0; i < o.length; i++) { o[i] += y * (ea + eb); var xn = x * c - y * s; y = x * s + y * c; x = xn; ea *= ka; eb *= kb; }
    }
    function enveloppe(o, att, rel) { for (var i = 0; i < o.length; i++) { var t = i / SR, g = Math.min(1, t / att); if (t > TOFF) { g *= Math.exp(-(t - TOFF) / rel); } o[i] *= g; } }
    function piano(f0) {
      var o = new Float32Array(N), B = Math.min(0.003, 0.00035 * Math.pow(f0 / 262, 1.3)), tau1 = 3.2 * Math.pow(262 / f0, 0.5), tot = 0;
      for (var n = 1; n <= 36; n++) {
        var fn = n * f0 * Math.sqrt(1 + B * n * n); if (fn > 15000) { break; }
        var an = Math.abs(Math.sin(n * Math.PI * 0.12)) / Math.pow(n, 0.85) / (1 + Math.pow(fn / 3500, 2));   /* marteau frappant vers le 1/8 de la corde, feutre qui adoucit les aigus */
        var tn = tau1 / (1 + 0.12 * (n - 1) + Math.pow(fn / 2500, 1.5)), ka = Math.exp(-1 / (0.2 * tn * SR)), kb = Math.exp(-1 / (1.5 * tn * SR));   /* son « immédiat » puis « rémanent » */
        tot += an;
        [-1, 1].forEach(function (sg) { partiel(o, fn * (1 + sg * 0.0004), an / 2, ka, kb, 0.8); });   /* deux cordes très légèrement désaccordées : battements lents */
      }
      var lp = 0, nb = Math.round(0.04 * SR);
      for (var i = 0; i < nb; i++) { var t = i / SR; lp += 0.12 * ((Math.random() * 2 - 1) - lp); o[i] += lp * 0.5 * tot * Math.exp(-t / 0.005); }   /* choc sourd du marteau */
      enveloppe(o, 0.0015, 0.07); return normalise(o);
    }
    function corpsViolon(SR) {   /* caisse du violon : modes principaux + nombreux modes aléatoires (toujours les mêmes), « colline du chevalet » vers 2,5 kHz */
      var s = 20260214; function rnd() { s = (s * 16807) % 2147483647; return s / 2147483647; }
      var M = [[275, 14, 0.5], [405, 22, 0.3], [470, 28, 0.75], [545, 28, 0.75], [700, 30, 0.6]];
      for (var lf = Math.log(620); lf < Math.log(7500); lf += 0.04 + rnd() * 0.025) {
        var fm = Math.exp(lf), u = Math.log(fm / 2600) / 0.38;
        M.push([fm * (0.98 + 0.04 * rnd()), 25 + 35 * rnd(), (0.3 + 0.7 * rnd()) * Math.pow(fm / 600, 0.9) * (0.6 + 1.2 * Math.exp(-u * u)) / (1 + Math.pow(fm / 4000, 4))]);
      }
      return M.map(function (m) {   /* filtres passe-bande (gain 1 au pic) */
        var w = 2 * Math.PI * m[0] / SR, al = Math.sin(w) / (2 * m[1]), a0 = 1 + al;
        return { f: m[0], g: m[2], b0: al / a0, a1: -2 * Math.cos(w) / a0, a2: (1 - al) / a0 };
      });
    }
    function violonBrut(f0) {
      var corps = CORPS, exc = new Float64Array(N), out = new Float32Array(N), nm = Math.max(1, Math.min(45, Math.floor(14000 / f0))), amps = new Float64Array(nm + 1), n, i;
      var phi = 0, vph = 0, jit = 0, jv = 0, fl = 0, lp = 0, hp = 0;
      for (i = 0; i < N; i++) {
        var t = i / SR, vib = 0.011 * Math.min(1, Math.max(0, (t - 0.22) / 0.35));   /* vibrato d'environ ±19 cents, qui s'installe après l'attaque */
        if (i % 64 === 0) { jv += 0.05 * ((Math.random() * 2 - 1) - jv); jit += 0.05 * (jv - jit); fl += 0.03 * ((Math.random() * 2 - 1) - fl); }   /* petites irrégularités de l'archet */
        vph += 2 * Math.PI * (5.7 + 0.35 * Math.sin(2 * Math.PI * 0.45 * t)) / SR;
        var f = f0 * (1 + vib * Math.sin(vph) + 0.0012 * jit);
        phi += 2 * Math.PI * f / SR;
        if (i % 32 === 0) { for (n = 1; n <= nm; n++) { amps[n] = 1 / n / (1 + (n / 28) * (n / 28)) * (1 - Math.exp(-t / (0.025 + 0.004 * n))); } }   /* mouvement de Helmholtz : dent de scie, les aigus s'installent plus tard */
        var s1 = Math.sin(phi), c2 = 2 * Math.cos(phi), sp = 0, sc = s1, acc = amps[1] * s1;
        for (n = 2; n <= nm; n++) { var sn = c2 * sc - sp; sp = sc; sc = sn; acc += amps[n] * sc; }
        var env = (1 - Math.exp(-t / 0.07)) * (1 + 0.5 * fl); if (t > TOFF) { env *= Math.exp(-(t - TOFF) / 0.25); }
        var wn = Math.random() * 2 - 1; lp += 0.3 * (wn - lp); hp = wn - lp;
        var bruit = hp * (0.09 + 0.35 * Math.exp(-t / 0.035)) * (1 + 0.7 * Math.cos(phi)) * (t > TOFF ? Math.exp(-(t - TOFF) / 0.04) : 1);   /* frottement de l'archet, plus fort au moment du glissement */
        exc[i] = acc * env + bruit * 0.6;
      }
      /* rayonnement par la caisse */
      for (var k = 0; k < corps.length; k++) {
        var m = corps[k], x1 = 0, x2 = 0, y1 = 0, y2 = 0;
        for (i = 0; i < N; i++) { var x = exc[i], y = m.b0 * (x - x2) - m.a1 * y1 - m.a2 * y2; x2 = x1; x1 = x; y2 = y1; y1 = y; out[i] += m.g * y; }
      }
      for (i = 0; i < N; i++) { out[i] += 0.05 * exc[i]; }
      /* un peu de réverbération de salle (réverbérateur de Schroeder) */
      var CD = [1557, 1617, 1491, 1422, 1277, 1356], AD = [225, 556, 341], rev = new Float32Array(N), c;
      for (c = 0; c < CD.length; c++) {
        var d = Math.round(CD[c] * SR / 44100), buf = new Float32Array(d), p = 0, lpf = 0;
        for (i = 0; i < N; i++) { var o = buf[p]; lpf = o * 0.75 + lpf * 0.25; buf[p] = out[i] + lpf * 0.8; p = (p + 1) % d; rev[i] += o / CD.length; }
      }
      for (c = 0; c < AD.length; c++) {
        var da = Math.round(AD[c] * SR / 44100), ba = new Float32Array(da), q = 0;
        for (i = 0; i < N; i++) { var bo = ba[q], v = rev[i] + 0.5 * bo; ba[q] = v; rev[i] = bo - 0.5 * v; q = (q + 1) % da; }
      }
      for (i = 0; i < N; i++) { out[i] = out[i] + 0.35 * rev[i]; var tf = (N - i) / SR; if (tf < 0.1) { out[i] *= tf / 0.1; } }   /* fondu final */
      return out;
    }
    var CORPS = null;
    function violon(f0) { if (!CORPS) { CORPS = corpsViolon(SR); } return normalise(violonBrut(f0)); }
    function reponse(f) {   /* réponse complexe de la caisse à la fréquence f : [module, phase] */
      if (!CORPS) { CORPS = corpsViolon(SR); }
      var w = 2 * Math.PI * f / SR, re = 0.05, im = 0;
      CORPS.forEach(function (m) { var nr = m.b0 * (1 - Math.cos(2 * w)), ni = m.b0 * Math.sin(2 * w), dr = 1 + m.a1 * Math.cos(w) + m.a2 * Math.cos(2 * w), di = -m.a1 * Math.sin(w) - m.a2 * Math.sin(2 * w), dd = dr * dr + di * di; re += m.g * (nr * dr + ni * di) / dd; im += m.g * (ni * dr - nr * di) / dd; });
      return [Math.hypot(re, im), Math.atan2(im, re)];
    }
    var cache = {}, nc = 0;
    function note(ins, f) {
      var k = ins + Math.round(f * 100); if (!cache[k]) { if (++nc > 16) { cache = {}; nc = 1; } cache[k] = (ins === 'piano' ? piano : violon)(f); }
      return cache[k];
    }
    var idle = window.requestIdleCallback || function (f) { return setTimeout(f, 1500); };
    idle(function () { note('violon', 440); });   /* le la du violon, prêt d'avance */
    return { SR: SR, DUR: DUR, TOFF: TOFF, N: N, note: note, reponse: reponse };
  })();
  (function () {   /* forme carrée (créneaux) : harmoniques impairs, adoucis pour éviter les oscillations parasites */
    var co = []; for (var n = 1; n <= 25; n++) { var x = Math.PI * n / 27; co.push(n % 2 ? 4 / (Math.PI * n) * Math.sin(x) / x : 0); }
    var mx = 0, th0 = 0; for (var i = 0; i < 2000; i++) { var th = 2 * Math.PI * i / 2000, u = 0; for (var k = 0; k < co.length; k++) { u += co[k] * Math.sin((k + 1) * th); } if (u > mx) { mx = u; th0 = th; } }
    FORMES.carre = { nom: 'carré', co: co, mx: mx, thMax: th0, u: function (th) { var u = 0; for (var k = 0; k < co.length; k++) { u += co[k] * Math.sin((k + 1) * th); } return u / mx; } };
  })();
  (function () {   /* motifs stables (simplifiés) du piano et du violon, pour l'affichage : mêmes ingrédients que la synthèse, à 440 Hz */
    function cree(nom, co, ph) {
      ph = ph || co.map(function () { return 0; });
      function s(th) { var u = 0; for (var k = 0; k < co.length; k++) { u += co[k] * Math.sin((k + 1) * th + ph[k]); } return u; }
      var mx = 0, th0 = 0; for (var i = 0; i < 2000; i++) { var th = 2 * Math.PI * i / 2000, u = s(th); if (u > mx) { mx = u; th0 = th; } }
      FORMES[nom] = { nom: nom, co: co, mx: mx, thMax: th0, u: function (th) { return s(th) / mx; } };
    }
    var cp = [], cv = [], pv = [];
    for (var n = 1; n <= 20; n++) {
      var fn = 440 * n, tn = 2.47 / (1 + 0.12 * (n - 1) + Math.pow(fn / 2500, 1.5));
      cp.push(Math.abs(Math.sin(n * Math.PI * 0.12)) / Math.pow(n, 0.85) / (1 + Math.pow(fn / 3500, 2)) * Math.exp(-0.15 / (0.2 * tn)));
      var H = SYN.reponse(fn); cv.push(H[0] / n / (1 + (n / 28) * (n / 28))); pv.push(H[1]);
    }
    cree('piano', cp); cree('violon', cv, pv);
  })();
  (function () {
    var root = document.getElementById('lab-son'); if (!root) { return; }
    var inF = $(root, '[data-in="f"]'), inA = $(root, '[data-in="a"]'), bP = $(root, '[data-act="play"]'), kb = $(root, '.nt-piano'), msg = $(root, '.nt-msg');
    var cards = { f: $(root, '.nt-f-haut'), forme: $(root, '.nt-f-timbre'), a: $(root, '.nt-f-int') };
    var INS = {
      sin: { nom: 'sinusoïde (diapason)', c: EMER, t: 'Diapason&nbsp;: un motif <b>sinusoïdal</b>, le plus simple qui soit. C\u2019est un <b>son pur</b>, un peu «&nbsp;terne&nbsp;». Le son est continu&nbsp;: déplacez les curseurs pendant l\u2019écoute.' },
      piano: { c: '#1E40AF', nom: 'piano', t: 'Piano&nbsp;: <b>attaque très brève</b> (le marteau frappe les cordes), puis le son <b>décroît</b> sans qu\u2019on puisse l\u2019entretenir. Les composantes aiguës s\u2019éteignent les premières&nbsp;: au cours de la note, le motif s\u2019arrondit. Le motif affiché est celui de la partie stable de la note.' },
      violon: { c: '#B45309', nom: 'violon', t: 'Violon&nbsp;: <b>attaque progressive</b> (l\u2019archet met quelques centièmes de seconde à installer la vibration), puis un son <b>entretenu</b> tant que l\u2019archet frotte, avec un léger vibrato. La corde vibre en dent de scie, mais la caisse, avec ses nombreuses résonances, transforme profondément ce motif.' },
      carre: { nom: 'carré (créneaux)', c: '#0F766E', t: 'Carré&nbsp;: un motif en créneaux, comme celui que produit un microcontrôleur. Le son est riche et «&nbsp;nasillard&nbsp;», typique des premiers jeux vidéo. Le son est continu&nbsp;: déplacez les curseurs pendant l\u2019écoute.' }
    };
    var NOTES = [['do', 3, 261.63], ['ré', 3, 293.66], ['mi', 3, 329.63], ['fa', 3, 349.23], ['sol', 3, 392.0], ['la', 3, 440.0], ['si', 3, 493.88], ['do', 4, 523.25]];
    var BASES = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20];
    var f = 440, a = 35, ins = 'sin', playing = false, osc = null, gain = null, src = null, srcG = null, cnv, tmr = {};
    function estNote() { return ins === 'piano' || ins === 'violon'; }
    function tStr(ms) { return ms >= 1000 ? sig(ms / 1000, 3) + '\u00A0s' : (ms >= 0.1 ? sig(ms, 3) + '\u00A0ms' : sig(ms * 1000, 3) + '\u00A0µs'); }
    function bStr(b) { return b >= 0.1 ? String(b).replace('.', ',') + '\u00A0ms' : Math.round(b * 1000) + '\u00A0µs'; }
    function haut(f) { return f < 250 ? 'grave' : (f < 2000 ? 'médium' : 'aigu'); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; ctx.clearRect(0, 0, W, H);
      var x0 = 8, x1 = W - 8, y0 = 26, y1 = H - 78, gx = (x1 - x0) / 10, gy = (y1 - y0) / 8, ym = (y0 + y1) / 2, Tms = 1000 / f, col = INS[ins].c;
      var b = BASES[BASES.length - 1]; for (var i = 0; i < BASES.length; i++) { if (10 * BASES[i] / Tms >= 2) { b = BASES[i]; break; } }
      grille(ctx, x0, y0, x1, y1, 10, 8);
      var A = 3.4 * a / 100 * gy, Tpx = Tms / b * gx, xa = null, ymax = 0, x, y;
      ctx.strokeStyle = col; ctx.lineWidth = 1.7; ctx.beginPath();
      var F = FORMES[ins];
      for (x = x0; x <= x1; x += 0.5) { y = ym - A * F.u(2 * Math.PI * (x - x0) / Tpx); if (x === x0) { ctx.moveTo(x, y); } else { ctx.lineTo(x, y); } }
      xa = x0 + Tpx * (1 + F.thMax / (2 * Math.PI)); if (xa > x1 - 10) { xa = x0 + Tpx * F.thMax / (2 * Math.PI); } ymax = A;
      ctx.stroke();
      arrow(ctx, x0, y0 - 12, x0 + Tpx, y0 - 12, SKY, true, 6); pill(ctx, 'T = ' + tStr(Tms), x0 + Tpx / 2, y0 - 12, { size: 12, col: SKY, stroke: '#BAE6FD' });
      if (ymax > 3 && xa !== null) {
        ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = AMBER; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(x0, ym - ymax); ctx.lineTo(x1, ym - ymax); ctx.stroke(); ctx.restore();
        arrow(ctx, xa, ym, xa, ym - ymax, AMBER, true, 6); pill(ctx, 'amplitude', Math.min(xa + 6, x1 - 80), Math.max(y0 - 1, ym - ymax - 12), { size: 12, col: AMBER, align: 'left', stroke: '#FDE68A' });
      }
      txt(ctx, '1 division \u2194 ' + bStr(b), x1, y1 + 12, { size: 11, col: SLATE, align: 'right' });
      /* échelle des fréquences */
      var sx0 = 14, sx1 = W - 14, sy = H - 40, sh = 20;
      function X(ff) { return sx0 + (sx1 - sx0) * Math.log10(ff / 2) / 5; }
      var xm = X(f);
      [[2, 20, '#EDE9FE', '#6D28D9', 'infrasons'], [20, 20000, '#DBEAFE', BLUE, 'sons audibles'], [20000, 200000, '#FCE7F3', '#BE185D', 'ultrasons']].forEach(function (z) {
        var za = X(z[0]), zb = X(z[1]); ctx.fillStyle = z[2]; ctx.fillRect(za, sy, zb - za, sh);
        ctx.font = '11px ' + FONT; var w = ctx.measureText(z[4]).width / 2 + 8;
        var pos = [(za + zb) / 2, za + (zb - za) * 0.25, za + (zb - za) * 0.75].filter(function (p) { return Math.abs(p - xm) > w; });   /* l'étiquette évite le repère */
        if (pos.length && (zb - za) > 2 * w) { txt(ctx, z[4], pos[0], sy + sh / 2, { size: 11, col: z[3] }); }
      });
      if (W < 520) { [20, 200, 2000, 20000].forEach(function (ff, k) { txt(ctx, ['20', '200', '2\u202F000', '20\u202F000\u00A0Hz'][k], X(ff), sy + sh + 11, { size: 10, col: SLATE }); }); }
      else { [2, 20, 200, 2000, 20000, 200000].forEach(function (ff, k) { txt(ctx, ['2', '20', '200', '2\u202F000', '20\u202F000', '200\u202F000\u00A0Hz'][k], X(ff), sy + sh + 11, { size: 10, col: SLATE, align: k === 5 ? 'right' : (k === 0 ? 'left' : 'center') }); }); }
      ctx.fillStyle = NAVY; ctx.beginPath(); ctx.moveTo(xm - 6, sy - 9); ctx.lineTo(xm + 6, sy - 9); ctx.lineTo(xm, sy - 1); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = NAVY; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(xm, sy); ctx.lineTo(xm, sy + sh); ctx.stroke();
    }
    function redraw() { draw(cnv); }
    function lab() {
      $(root, '.out-f').textContent = sig(f, 3) + '\u00A0Hz (' + haut(f) + ')'; $(root, '.out-f2').textContent = sig(f, 3) + '\u00A0Hz, soit T = ' + tStr(1000 / f);
      $(root, '.out-forme').textContent = INS[ins].nom; $(root, '.out-a').textContent = a + '\u00A0%'; $(root, '.out-a2').textContent = a + '\u00A0%';
    }
    function hi(k) { var el = cards[k]; el.classList.add('nt-on'); clearTimeout(tmr[k]); tmr[k] = setTimeout(function () { el.classList.remove('nt-on'); }, 1300); }
    function wave(o, ac) {
      if (ins === 'sin') { o.type = 'sine'; return; }
      var co = FORMES[ins].co, re = new Float32Array(co.length + 1), im = new Float32Array(co.length + 1);
      for (var i = 0; i < co.length; i++) { im[i + 1] = co[i]; } o.setPeriodicWave(ac.createPeriodicWave(re, im));
    }
    function vol() { return 0.22 * a / 100; }
    function etiquette() {
      bP.innerHTML = playing ? '<i class="fa-solid fa-stop"></i>&nbsp; Arrêter' : (estNote() ? '<i class="fa-solid fa-play"></i>&nbsp; Jouer la note' : '<i class="fa-solid fa-volume-high"></i>&nbsp; Écouter');
    }
    function stopTout() {
      if (osc) { var o0 = osc, g0 = gain; g0.gain.setTargetAtTime(0, AC.currentTime, 0.03); setTimeout(function () { try { o0.stop(); } catch (e) {} }, 250); osc = null; gain = null; }
      if (src) { var s0 = src, sg = srcG; src = null; srcG = null; sg.gain.setTargetAtTime(0, AC.currentTime, 0.02); setTimeout(function () { try { s0.stop(); } catch (e) {} }, 150); }
      playing = false; etiquette();
    }
    function continu() {
      var ac = audio(); if (!ac) { return; }
      osc = ac.createOscillator(); gain = ac.createGain(); wave(osc, ac); osc.frequency.value = f; gain.gain.value = 0;
      osc.connect(gain); gain.connect(ac.destination); osc.start(); gain.gain.setTargetAtTime(vol(), ac.currentTime, 0.03);
      playing = true; etiquette();
    }
    function joueNote() {
      stopTout(); var ac = audio(); if (!ac) { return; }
      var bb = ac.createBuffer(1, SYN.N, SYN.SR); bb.getChannelData(0).set(SYN.note(ins, f));
      srcG = ac.createGain(); srcG.gain.value = 1.6 * vol(); src = ac.createBufferSource(); src.buffer = bb; src.connect(srcG); srcG.connect(ac.destination);
      var me = src; src.onended = function () { if (src === me) { src = null; srcG = null; playing = false; etiquette(); } };
      src.start(); playing = true; etiquette();
    }
    function noteCourte() {
      var ac = audio(); if (!ac) { return; } var o = ac.createOscillator(), g = ac.createGain(), tt = ac.currentTime;
      wave(o, ac); o.frequency.value = f; g.gain.setValueAtTime(0, tt); g.gain.linearRampToValueAtTime(vol(), tt + 0.02); g.gain.setTargetAtTime(0, tt + 0.5, 0.08);
      o.connect(g); g.connect(ac.destination); o.start(tt); o.stop(tt + 1.1);
    }
    function majContinu() { if (!osc) { return; } osc.frequency.setTargetAtTime(f, AC.currentTime, 0.02); gain.gain.setTargetAtTime(vol(), AC.currentTime, 0.03); wave(osc, AC); }
    function sliderFromF() { inF.value = Math.round(1000 * Math.log10(f / 20) / 3); }
    cnv = Canvas($(root, '.nt-son-osc'), function (W) { return W < 520 ? 280 : 310; }, draw);
    NOTES.forEach(function (nt) {
      var b = document.createElement('button'); b.type = 'button'; b.innerHTML = '<b>' + nt[0] + '</b>' + nt[1]; b.setAttribute('aria-label', nt[0] + ' ' + nt[1] + ', ' + Math.round(nt[2]) + ' hertz');
      b.addEventListener('click', function () {
        f = nt[2]; sliderFromF(); $$(kb, 'button').forEach(function (x) { x.classList.toggle('nt-on', x === b); });
        lab(); hi('f');
        draw(cnv); if (estNote()) { joueNote(); } else if (playing) { majContinu(); } else { noteCourte(); }
      });
      kb.appendChild(b);
    });
    inF.addEventListener('input', function () {
      f = Number((20 * Math.pow(1000, inF.value / 1000)).toPrecision(3)); $$(kb, 'button').forEach(function (x) { x.classList.remove('nt-on'); }); lab(); hi('f');
      draw(cnv); if (estNote()) { if (playing) { stopTout(); } } else { majContinu(); }
    });
    inA.addEventListener('input', function () { a = parseInt(inA.value, 10); lab(); hi('a'); redraw(); majContinu(); if (srcG) { srcG.gain.setTargetAtTime(1.6 * vol(), AC.currentTime, 0.03); } });
    $$(root, 'input[name="son-forme"]').forEach(function (r) {
      r.addEventListener('change', function () {
        var avant = playing && !estNote(); ins = r.value; lab(); hi('forme'); msg.innerHTML = INS[ins].t;
        redraw(); if (estNote()) { joueNote(); }
        else { if (src) { stopTout(); } if (avant) { majContinu(); } }
        etiquette();
      });
    });
    bP.addEventListener('click', function () { if (playing) { stopTout(); } else if (estNote()) { joueNote(); } else { continu(); } });
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { if (!es[0].isIntersecting && playing) { stopTout(); } }).observe(root); }
    sliderFromF(); lab(); etiquette(); draw(cnv);
  })();

  /* =================== 10 b. L'attaque : à l'endroit, à l'envers =================== */
  (function () {
    var root = document.getElementById('lab-attaque'); if (!root) { return; }
    var det = root.closest('details'), msg = $(root, '.nt-msg'), cnv = null, B = {}, dir = { piano: 1, violon: 1 }, cur = null, t0 = 0, src = null;
    var COL = { piano: '#1E40AF', violon: '#B45309' }, NOM = { piano: 'piano', violon: 'violon' };
    var MSG = {
      'piano1': 'Piano à l\u2019endroit&nbsp;: attaque brutale (le marteau), puis le son décroît. On reconnaît tout de suite un piano.',
      'piano-1': 'Le même son, à l\u2019envers&nbsp;: il enfle progressivement puis s\u2019arrête net. Le motif n\u2019a pas changé, et pourtant on ne reconnaît plus du tout un piano&nbsp;!',
      'violon1': 'Violon à l\u2019endroit&nbsp;: attaque progressive de l\u2019archet, son entretenu, léger vibrato.',
      'violon-1': 'Violon à l\u2019envers&nbsp;: la différence est bien moins frappante, car son enveloppe est presque symétrique (montée et descente progressives). C\u2019est l\u2019attaque brève du piano qui le rend si caractéristique.'
    };
    function bufs() { if (!B.piano) { B.piano = SYN.note('piano', 440); B.violon = SYN.note('violon', 440); } }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, x0 = 12, x1 = W - 12; ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      ['piano', 'violon'].forEach(function (ins, r) {
        var yc = 44 + r * 78, ah = 26, b = B[ins];
        txt(ctx, NOM[ins] + (dir[ins] < 0 ? ', à l\u2019envers' : ', à l\u2019endroit'), x0, yc - ah - 9, { size: 12, col: COL[ins], align: 'left' });
        ctx.strokeStyle = GRID; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(x0, yc); ctx.lineTo(x1, yc); ctx.stroke();
        if (b) {
          ctx.fillStyle = COL[ins]; ctx.globalAlpha = 0.85;
          for (var px = 0; px < x1 - x0; px++) {
            var i0 = Math.floor(px / (x1 - x0) * SYN.N), i1 = Math.floor((px + 1) / (x1 - x0) * SYN.N), mn = 0, mx = 0;
            for (var i = i0; i < i1; i++) { var v = b[dir[ins] > 0 ? i : SYN.N - 1 - i]; if (v > mx) { mx = v; } if (v < mn) { mn = v; } }
            ctx.fillRect(x0 + px, yc - mx * ah, 1, Math.max(0.6, (mx - mn) * ah));
          }
          ctx.globalAlpha = 1;
        }
        if (cur === ins && AC) {
          var xz = x0 + Math.min(1, (AC.currentTime - t0) / SYN.DUR) * (x1 - x0);
          ctx.strokeStyle = ROSE; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(xz, yc - ah - 2); ctx.lineTo(xz, yc + ah + 2); ctx.stroke();
        }
      });
      for (var s = 0; s <= 2; s += 0.5) { txt(ctx, fmt(s, 1) + '\u00A0s', x0 + s / SYN.DUR * (x1 - x0), H - 9, { size: 10, col: SLATE, align: s === 0 ? 'left' : 'center' }); }
    }
    function stop() { if (src) { try { src.stop(); } catch (e) {} src = null; } cur = null; }
    var loop = Loop(root, function () { if (cnv) { draw(cnv); } return !!src; });
    function joue(ins, d) {
      bufs(); stop(); var ac = audio(); if (!ac) { return; } dir[ins] = d;
      var bb = ac.createBuffer(1, SYN.N, SYN.SR), dd = bb.getChannelData(0), b = B[ins];
      for (var i = 0; i < SYN.N; i++) { dd[i] = b[d > 0 ? i : SYN.N - 1 - i]; }
      var g = ac.createGain(); g.gain.value = 0.3; src = ac.createBufferSource(); src.buffer = bb; src.connect(g); g.connect(ac.destination);
      var me = src; src.onended = function () { if (src === me) { src = null; cur = null; if (cnv) { draw(cnv); } } };
      src.start(); t0 = ac.currentTime; cur = ins; msg.innerHTML = MSG[ins + d]; loop.kick();
    }
    $$(root, 'button[data-ins]').forEach(function (b) { b.addEventListener('click', function () { joue(b.getAttribute('data-ins'), parseInt(b.getAttribute('data-dir'), 10)); }); });
    function ouvre() { bufs(); if (!cnv) { cnv = Canvas($(root, 'canvas'), function () { return 176; }, draw); } else { cnv.size(); } }
    if (det) { det.addEventListener('toggle', function () { if (det.open) { ouvre(); } else { stop(); } }); if (det.open) { ouvre(); } } else { ouvre(); }
  })();

  /* =================== 11. Une, deux, quatre trompettes =================== */
  (function () {
    var root = document.getElementById('lab-trompettes'); if (!root) { return; }
    var dots = $(root, '.nt-dots'), bI = $(root, '.nt-bar-I > div'), bL = $(root, '.nt-bar-L > div'), oI = $(root, '.out-I'), oL = $(root, '.out-L'), sono = $(root, '.out-sono'), msg = $(root, '.nt-msg');
    var MSG = {
      1: 'Une trompette seule&nbsp;: 80&nbsp;dB.',
      2: 'Intensité multipliée par 2&nbsp;: le niveau n\u2019augmente que de 3&nbsp;dB.',
      4: 'Intensité multipliée par 4 = 2 × 2&nbsp;: le niveau augmente de 3 + 3 = 6&nbsp;dB.',
      8: 'Intensité multipliée par 8 = 2 × 2 × 2&nbsp;: le niveau augmente de 3 + 3 + 3 = 9&nbsp;dB.',
      10: 'Intensité multipliée par 10&nbsp;: le niveau augmente de 10&nbsp;dB.',
      100: 'Intensité multipliée par 100 = 10 × 10&nbsp;: le niveau n\u2019augmente que de 10 + 10 = 20&nbsp;dB. Cent trompettes ne paraissent pas cent fois plus fortes&nbsp;!'
    };
    function set(n) {
      var L = 80 + 10 * Math.log10(n), h = ''; for (var i = 0; i < n; i++) { h += '<i></i>'; } dots.innerHTML = h;
      bI.style.width = Math.max(1, n) + '%'; bL.style.width = (L / 120 * 100).toFixed(1) + '%';
      oI.innerHTML = n + '&nbsp;×&nbsp;<i>I</i><sub>t</sub>'; oL.textContent = Math.round(L) + '\u00A0dB'; sono.textContent = Math.round(L); msg.innerHTML = MSG[n];
    }
    $$(root, 'input[name="tromp-n"]').forEach(function (r) { r.addEventListener('change', function () { set(parseInt(r.value, 10)); }); });
    set(1);
  })();

  /* =================== 11 b. Trompettes : mesure au micro =================== */
  (function () {
    var root = document.getElementById('lab-trompettes'), box = root && $(root, '.nt-mic'); if (!box) { return; }
    var bMic = $(box, '[data-act="micro"]'), bLib = $(box, '[data-act="libre"]'), bar = $(box, '.nt-vu-bar > div'), vuOut = $(box, '.out-vu'), msg = $(box, '.nt-mic-msg');
    var stream = null, anaMic = null, anaInt = null, libre = null, busy = false, data = new Float32Array(2048), res = {}, OFF = 100, P = 0;
    var DET = [0, 9, -13, 21], CO = [0.6, 0.9, 1.0, 0.9, 0.75, 0.6, 0.45, 0.33, 0.24, 0.17, 0.12, 0.08];   /* spectre d'un cuivre : maximum vers le 3e harmonique */
    function lvl(m) { return 10 * Math.log10(Math.max(m, 1e-12)) + OFF; }
    function mesure(an) { an.getFloatTimeDomainData(data); var s = 0, pk = 0; for (var i = 0; i < data.length; i++) { s += data[i] * data[i]; pk = Math.max(pk, Math.abs(data[i])); } return [s / data.length, pk]; }
    function vu(L) { var ok = isFinite(L) && L > 5; bar.style.width = ok ? Math.max(0, Math.min(100, (L - 20) / 80 * 100)).toFixed(1) + '%' : '0%'; vuOut.firstChild.textContent = ok ? fmt(L, 0) : '\u2014'; }
    function dis(t) { $$(box, 'button[data-n]').forEach(function (b) { b.disabled = t; }); bMic.disabled = t; bLib.disabled = t || !anaMic; }
    function say(h, cls) { msg.className = 'nt-msg nt-mic-msg' + (cls ? ' nt-fb ' + cls : ''); msg.innerHTML = h; }
    function finLibre() { if (libre) { clearInterval(libre); libre = null; bLib.innerHTML = '<i class="fa-solid fa-gauge"></i>&nbsp; Sonomètre libre'; } }
    function coupe() { finLibre(); if (stream) { stream.getTracks().forEach(function (t) { t.stop(); }); } stream = null; anaMic = null; bMic.innerHTML = '<i class="fa-solid fa-microphone"></i>&nbsp; Activer le micro'; bLib.disabled = true; vu(-Infinity); }
    bMic.addEventListener('click', function () {
      if (stream) { coupe(); say('Micro coupé&nbsp;: les mesures se feront directement sur le signal émis.'); return; }
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) { say('Le micro n\u2019est pas accessible sur cet appareil ou dans ce navigateur&nbsp;: les mesures se feront directement sur le signal émis.'); return; }
      var ac = audio(); if (!ac) { return; }
      navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false } }).then(function (s) {
        stream = s; anaMic = ac.createAnalyser(); anaMic.fftSize = 2048; ac.createMediaStreamSource(s).connect(anaMic);
        bMic.innerHTML = '<i class="fa-solid fa-microphone-slash"></i>&nbsp; Couper le micro'; bLib.disabled = false; res = {}; maj();
        say('Micro actif. Placez l\u2019appareil dans une pièce calme, volume assez fort, puis lancez les mesures.');
      }).catch(function () { say('Accès au micro refusé ou impossible&nbsp;: les mesures se feront directement sur le signal émis.'); });
    });
    bLib.addEventListener('click', function () {
      if (libre) { finLibre(); return; }
      if (!anaMic) { return; } P = 0;
      bLib.innerHTML = '<i class="fa-solid fa-stop"></i>&nbsp; Arrêter le sonomètre';
      libre = setInterval(function () { var m = mesure(anaMic)[0]; P = P ? P + (m - P) * 0.15 : m; vu(lvl(P)); }, 50);
      say('Sonomètre en marche&nbsp;: parlez, chuchotez, tapez dans les mains… et comparez les niveaux. Les valeurs sont relatives (micro non étalonné), mais 10&nbsp;dB de plus correspondent bien à une intensité sonore 10 fois plus grande.');
    });
    function trompettes(ac, n, dest) {
      var mix = ac.createGain(), re = new Float32Array(CO.length + 1), im = new Float32Array(CO.length + 1), t = ac.currentTime + 0.08, k;
      for (k = 0; k < CO.length; k++) { im[k + 1] = CO[k]; }
      var w = ac.createPeriodicWave(re, im); mix.connect(ac.destination); dest.forEach(function (d) { mix.connect(d); });
      for (k = 0; k < n; k++) {
        var f = 349.23 * Math.pow(2, DET[k] / 1200), o = ac.createOscillator(), g = ac.createGain(), lfo = ac.createOscillator(), lg = ac.createGain(), ts = t + Math.random() / f;   /* départs décalés : phases indépendantes */
        o.setPeriodicWave(w); o.frequency.value = f; lfo.frequency.value = 5 + 0.37 * k; lg.gain.value = f * 0.003; lfo.connect(lg); lg.connect(o.frequency);
        g.gain.setValueAtTime(0, ts); g.gain.linearRampToValueAtTime(0.13, ts + 0.07); g.gain.setValueAtTime(0.13, t + 2.7); g.gain.linearRampToValueAtTime(0, t + 2.85);
        o.connect(g); g.connect(mix); o.start(ts); lfo.start(ts); o.stop(t + 3); lfo.stop(t + 3);
      }
      return t;
    }
    function maj() {
      [1, 2, 4].forEach(function (n) {
        var tr = $(box, 'tr[data-n="' + n + '"]'), c = tr.children;
        c[1].textContent = res[n] === undefined ? '\u2014' : fmt(res[n], 1) + '\u00A0dB';
        if (n > 1) { c[2].textContent = (res[n] === undefined || res[1] === undefined) ? '\u2014' : (res[n] >= res[1] ? '+' : '\u2212') + fmt(Math.abs(res[n] - res[1]), 1) + '\u00A0dB'; }
      });
    }
    function lance(n) {
      if (busy) { return; } var ac = audio(); if (!ac) { return; }
      busy = true; dis(true); finLibre();
      var r = $(root, 'input[name="tromp-n"][value="' + n + '"]'); if (r) { r.checked = true; r.dispatchEvent(new Event('change')); }
      var micro = !!anaMic, an = anaMic;
      if (!micro) { if (!anaInt) { anaInt = ac.createAnalyser(); anaInt.fftSize = 2048; } an = anaInt; }
      var fond = 0, nf = 0, som = 0, ns = 0, pk = 0, debut = performance.now(), joue = !micro, t0 = 0;
      say(micro ? 'Mesure du bruit ambiant…' : 'Mesure sur le signal émis (sans micro)…');
      if (!micro) { trompettes(ac, n, [an]); t0 = performance.now(); }
      var tm = setInterval(function () {
        var now = performance.now(), m = mesure(an);
        if (micro && !joue) { fond += m[0]; nf++; vu(lvl(m[0])); if (now - debut > 800) { joue = true; trompettes(ac, n, []); t0 = performance.now(); say('Les trompettes jouent… mesure en cours.'); } return; }
        var e = (now - t0) / 1000; vu(lvl(m[0]));
        if (e > 0.6 && e < 2.5) { som += m[0]; ns++; pk = Math.max(pk, m[1]); }
        if (e > 3) {
          clearInterval(tm); busy = false; dis(false); vu(-Infinity);
          var L = lvl(som / Math.max(1, ns)); res[n] = L; maj();
          var h = n + '&nbsp;trompette' + (n > 1 ? 's' : '') + '&nbsp;: <b>' + fmt(L, 1) + '&nbsp;dB</b> (échelle relative). ', cls = 'ok';
          if (micro && nf && L - lvl(fond / nf) < 10) { h += 'Attention&nbsp;: le son mesuré dépasse à peine le bruit ambiant (' + fmt(lvl(fond / nf), 0) + '&nbsp;dB)&nbsp;; montez le volume ou faites le silence.'; cls = 'ko'; }
          else if (pk > 0.98) { h += 'Attention&nbsp;: le micro sature, baissez le volume.'; cls = 'ko'; }
          else if (n > 1 && res[1] !== undefined) {
            var d = L - res[1], att = 10 * Math.log10(n);
            h += 'Écart avec une trompette&nbsp;: ' + (d >= 0 ? '+' : '\u2212') + fmt(Math.abs(d), 1) + '&nbsp;dB, pour ' + fmt(att, 0) + '&nbsp;dB attendus' + (Math.abs(d - att) < 1.5 ? '&nbsp;: c\u2019est cohérent&nbsp;!' : '. Un tel écart peut venir du bruit ambiant, de la position de l\u2019appareil, ou d\u2019un réglage automatique du volume du micro.');
            if (Math.abs(d - att) >= 1.5) { cls = 'ko'; }
          } else if (n === 1) { h += 'Mesurez maintenant 2 puis 4 trompettes.'; }
          say(h, cls);
        }
      }, 40);
    }
    $$(box, 'button[data-n]').forEach(function (b) { b.addEventListener('click', function () { lance(parseInt(b.getAttribute('data-n'), 10)); }); });
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { if (!es[0].isIntersecting) { finLibre(); } }).observe(root); }
  })();

  /* =================== 12. Échelle des niveaux d'intensité sonore =================== */
  (function () {
    var root = document.getElementById('lab-echelle'); if (!root) { return; }
    var inL = $(root, '[data-in="L"]'), outL = $(root, '.out-L'), info = $(root, '.nt-info'), pre = $(root, '.nt-presets'), L = 60, cnv;
    var SRC = [[0, 'seuil d\u2019audibilité', 'ear-listen'], [10, 'respiration calme', 'wind'], [30, 'chuchotement', 'user-secret'], [60, 'conversation', 'comments'], [70, 'parler fort', 'bullhorn'], [80, 'rue animée', 'car'], [90, 'tondeuse à gazon', 'tractor'], [100, 'baladeur au maximum', 'headphones'], [110, 'concert, discothèque', 'guitar'], [120, 'seuil de douleur', 'burst'], [140, 'avion au décollage, de près', 'plane-departure']];
    var RISK = [   /* [niveau minimal, nom, icône, couleur, effet] */
      [0, 'Sans danger', 'circle-check', '#15803D', 'Aucun risque pour l\u2019audition.'],
      [70, 'Bruyant', 'circle-info', '#A16207', 'Pas de lésion de l\u2019oreille, mais un bruit prolongé fatigue, stresse et gêne la concentration.'],
      [80, 'Dangereux si l\u2019exposition dure', 'triangle-exclamation', '#C2410C', 'Au-delà de cette durée, les cellules de l\u2019oreille interne commencent à être détruites&nbsp;: <b>perte d\u2019audition et acouphènes définitifs</b>.'],
      [100, 'Très dangereux', 'triangle-exclamation', '#B91C1C', 'Quelques minutes suffisent&nbsp;: au-delà, <b>lésions définitives de l\u2019oreille interne</b> (perte d\u2019audition, acouphènes).'],
      [120, 'Douleur&nbsp;: lésions immédiates', 'burst', '#7F1D1D', 'Le son fait mal, et quelques secondes suffisent à <b>détruire des cellules de l\u2019oreille interne</b>. Lors d\u2019une explosion très proche, le tympan peut même se déchirer.']
    ];
    function risque(L) { var r = RISK[0]; RISK.forEach(function (x) { if (L >= x[0]) { r = x; } }); return r; }
    function heures(L) { return L < 80 ? Infinity : (L >= 120 ? 0 : 8 / Math.pow(2, (L - 80) / 3)); }
    function duree(h) {
      if (h === Infinity) { return 'pas de limite pour l\u2019audition'; }
      if (h === 0) { return 'aucune&nbsp;: quelques secondes suffisent'; }
      if (h >= 1) { var H = Math.floor(h), m = Math.round((h - H) * 60 / 5) * 5; if (m === 60) { H++; m = 0; } return H + '&nbsp;h' + (m ? '&nbsp;' + m + '&nbsp;min' : '') + ' par jour'; }
      var mn = h * 60; if (mn >= 1) { return (mn >= 10 ? Math.round(mn) : fmt(mn, mn < 2 ? 1 : 0)) + '&nbsp;min par jour'; }
      return Math.round(mn * 60) + '&nbsp;s par jour';
    }
    function rapport(L) {
      if (L === 60) { return 'la même que celle d\u2019une conversation'; }
      var r = Math.pow(10, (L - 60) / 10), big = r > 1 ? r : 1 / r, s = big < 10 ? sig(big, 2) : grp(String(Number(big.toPrecision(2))));
      return 'environ ' + s + ' fois plus ' + (r > 1 ? 'grande' : 'petite') + ' que celle d\u2019une conversation (60&nbsp;dB)';
    }
    function exemple(L) {
      for (var i = 0; i < SRC.length; i++) { if (SRC[i][0] === L) { return '<i class="fa-solid fa-' + SRC[i][2] + '"></i> ' + SRC[i][1]; } }
      for (i = 0; i < SRC.length - 1; i++) { if (L > SRC[i][0] && L < SRC[i + 1][0]) { return 'entre «&nbsp;' + SRC[i][1] + '&nbsp;» et «&nbsp;' + SRC[i + 1][1] + '&nbsp;»'; } }
      return '';
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, x0 = 18, x1 = W - 18, y = 50, h = 18, small = W < 520; ctx.clearRect(0, 0, W, H);
      function X(l) { return x0 + (x1 - x0) * l / 140; }
      var g = ctx.createLinearGradient(x0, 0, x1, 0);
      [[0, '#86EFAC'], [55, '#BEF264'], [70, '#FDE047'], [80, '#FDBA74'], [100, '#F87171'], [120, '#B91C1C'], [140, '#7F1D1D']].forEach(function (s) { g.addColorStop(s[0] / 140, s[1]); });
      ctx.fillStyle = g; rr(ctx, x0, y, x1 - x0, h, 6); ctx.fill();
      ctx.save(); rr(ctx, X(120), y, X(140) - X(120), h, 0); ctx.clip();   /* hachures « danger » au-delà du seuil de douleur */
      ctx.strokeStyle = 'rgba(255,255,255,0.45)'; ctx.lineWidth = 3; for (var k = X(120) - h; k < X(140) + h; k += 9) { ctx.beginPath(); ctx.moveTo(k, y + h); ctx.lineTo(k + h, y); ctx.stroke(); }
      ctx.restore();
      ctx.save(); ctx.setLineDash([3, 3]); ctx.strokeStyle = '#7C2D12'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(X(80), y - 6); ctx.lineTo(X(80), y + h + 4); ctx.stroke(); ctx.restore();
      SRC.forEach(function (s) { ctx.fillStyle = 'rgba(15,23,42,0.55)'; ctx.beginPath(); ctx.arc(X(s[0]), y + h / 2, 2, 0, 2 * Math.PI); ctx.fill(); });
      ctx.strokeStyle = GRID2; ctx.lineWidth = 1;
      for (var l = 0; l <= 140; l += 10) { ctx.beginPath(); ctx.moveTo(X(l), y + h + 2); ctx.lineTo(X(l), y + h + (l % 20 ? 5 : 8)); ctx.stroke(); if (l % 20 === 0) { txt(ctx, String(l), X(l), y + h + 17, { size: 10.5, col: SLATE }); } }
      [[0, 70, 'sans danger', 'calme'], [70, 80, small ? '' : 'bruyant', ''], [80, 120, small ? 'risqué' : 'dangereux selon la durée', ''], [120, 140, 'douleur', '']].forEach(function (z) { if (z[2]) { txt(ctx, z[2], (X(z[0]) + X(z[1])) / 2, y + h + 34, { size: 11, col: SLATE }); } });
      var r = risque(L), xm = X(L);
      ctx.fillStyle = r[3]; ctx.beginPath(); ctx.moveTo(xm - 7, y - 4); ctx.lineTo(xm + 7, y - 4); ctx.lineTo(xm, y + 5); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(xm, y + 3); ctx.lineTo(xm, y + h - 1); ctx.stroke();
      ctx.strokeStyle = r[3]; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(xm, y + 3); ctx.lineTo(xm, y + h - 1); ctx.stroke();
      pill(ctx, L + '\u00A0dB', Math.min(x1 - 24, Math.max(x0 + 24, xm)), y - 22, { size: 12.5, col: '#FFFFFF', bg: r[3] });
    }
    function set(v) {
      L = v; inL.value = v; outL.textContent = v + '\u00A0dB';
      var r = risque(v), h = heures(v), frac = h === Infinity ? 1 : Math.min(1, h / 8);
      info.style.setProperty('--k', r[3]);
      info.innerHTML = '<p class="nt-risk-head"><i class="fa-solid fa-' + r[2] + '"></i> ' + r[1] + '</p>' +
        '<p><b>Exemple&nbsp;:</b> ' + exemple(v) + '</p>' +
        '<p><b>Durée maximale d\u2019exposition, sans protection&nbsp;:</b> ' + duree(h) + '</p>' +
        '<div class="nt-jauge" aria-hidden="true"><div style="width:' + (100 * frac).toFixed(1) + '%"></div><span>' + (h === Infinity ? 'toute la journée' : (h === 0 ? 'quelques secondes à peine' : duree(h).replace(' par jour', '') + ' sur une journée de 8&nbsp;h')) + '</span></div>' +
        '<p class="nt-effet">' + r[4] + '</p>' +
        '<p><b>Intensité sonore&nbsp;:</b> ' + rapport(v) + '</p>';
      $$(pre, 'button').forEach(function (b) { b.setAttribute('aria-pressed', String(parseInt(b.getAttribute('data-l'), 10) === v)); });
      draw(cnv);
    }
    SRC.forEach(function (s) { var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn'; b.setAttribute('data-l', s[0]); b.innerHTML = '<i class="fa-solid fa-' + s[2] + '"></i>&nbsp; ' + s[1]; b.addEventListener('click', function () { set(s[0]); }); pre.appendChild(b); });
    cnv = Canvas($(root, 'canvas'), function () { return 116; }, draw);
    inL.addEventListener('input', function () { set(parseInt(inL.value, 10)); });
    set(60);
  })();

  /* =================== 13. Quiz =================== */
  (function () {
    var root = document.getElementById('quiz-son'); if (!root) { return; }
    var Q = [
      ['Un son peut-il se propager dans le vide&nbsp;?', ['Oui, à la vitesse de la lumière', 'Oui, mais très lentement', 'Non&nbsp;: il lui faut un milieu matériel'], 2, 'Le son est une vibration qui se transmet de proche en proche entre les particules d\u2019un milieu matériel. Sans particules, rien ne peut vibrer&nbsp;: le vide est silencieux.'],
      ['Quand un son traverse l\u2019air, les particules d\u2019air…', ['vont de la source jusqu\u2019à l\u2019oreille', 'oscillent autour de leur position de repos', 'restent parfaitement immobiles'], 1, 'Une onde transporte de l\u2019énergie et de l\u2019information, sans transport de matière&nbsp;: chaque particule ne fait qu\u2019aller et venir autour de sa position de repos.'],
      ['Dans quel milieu le son se propage-t-il le plus vite&nbsp;?', ['L\u2019air', 'L\u2019eau', 'L\u2019acier'], 2, 'Environ 340&nbsp;m/s dans l\u2019air, 1&nbsp;500&nbsp;m/s dans l\u2019eau et 5&nbsp;800&nbsp;m/s dans l\u2019acier.'],
      ['Une vitesse de 30&nbsp;m/s correspond à…', ['8,3&nbsp;km/h', '30&nbsp;km/h', '108&nbsp;km/h'], 2, 'Des m/s vers les km/h, on multiplie par 3,6&nbsp;: 30 × 3,6 = 108&nbsp;km/h.'],
      ['On compte 9&nbsp;s entre l\u2019éclair et le tonnerre. L\u2019orage est à environ…', ['3&nbsp;km', '9&nbsp;km', '27&nbsp;km'], 0, 'Le son parcourt environ 1&nbsp;km en 3&nbsp;s&nbsp;: 9 / 3 = 3&nbsp;km (précisément, 340 × 9 = 3&nbsp;060&nbsp;m).'],
      ['Un signal sonore a une période <i>T</i> = 2&nbsp;ms. Sa fréquence vaut…', ['0,5&nbsp;Hz', '2&nbsp;Hz', '500&nbsp;Hz'], 2, '<i>f</i> = 1 / <i>T</i> avec <i>T</i> en secondes&nbsp;: <i>T</i> = 0,002&nbsp;s, donc <i>f</i> = 1 / 0,002 = 500&nbsp;Hz.'],
      ['Un son de fréquence 30&nbsp;000&nbsp;Hz est…', ['un infrason', 'un son aigu audible', 'un ultrason'], 2, 'Au-delà de 20&nbsp;000&nbsp;Hz, l\u2019oreille humaine n\u2019entend plus rien&nbsp;: ce sont des ultrasons (les chiens et les chauves-souris, eux, les entendent).'],
      ['Si la fréquence d\u2019un son augmente, il paraît…', ['plus aigu', 'plus grave', 'plus fort'], 0, 'La hauteur est liée à la fréquence&nbsp;: plus la fréquence est grande, plus le son est aigu.'],
      ['Une flûte et un violon jouent la même note. Leurs sons diffèrent par…', ['leur fréquence', 'la forme de leur signal (le timbre)', 'leur période'], 1, 'Même note, donc même fréquence et même période&nbsp;: c\u2019est la forme du signal, donc le timbre, qui permet de distinguer les instruments.'],
      ['Si l\u2019amplitude d\u2019un signal sonore augmente…', ['le son devient plus aigu', 'l\u2019intensité sonore augmente&nbsp;: le son paraît plus fort', 'la période augmente'], 1, 'L\u2019intensité sonore augmente avec l\u2019amplitude. La période, donc la hauteur, ne change pas.'],
      ['Deux sources identiques produisent chacune 70&nbsp;dB. Ensemble, elles produisent environ…', ['70&nbsp;dB', '73&nbsp;dB', '140&nbsp;dB'], 1, 'Les intensités s\u2019additionnent&nbsp;: l\u2019intensité double, et doubler l\u2019intensité n\u2019ajoute que 3&nbsp;dB au niveau d\u2019intensité sonore.'],
      ['À partir de quel niveau une exposition prolongée devient-elle dangereuse pour l\u2019audition&nbsp;?', ['40&nbsp;dB', '80&nbsp;dB', 'seulement 140&nbsp;dB'], 1, 'À partir de 80&nbsp;dB, la durée d\u2019exposition doit être limitée (8&nbsp;h par jour à 80&nbsp;dB, puis deux fois moins à chaque fois que le niveau augmente de 3&nbsp;dB).']
    ];
    var qEl = $(root, '.nt-ql-q'), bx = $(root, '.nt-ql-btns'), order = [];
    var S = Serie(root, Q.length, {
      init: function () { order = shuffle(Q.map(function (_, i) { return i; })); },
      show: function (k) {
        var q = Q[order[k]]; qEl.innerHTML = q[0]; bx.innerHTML = ''; bx.hidden = false;
        q[1].forEach(function (cTxt, i) {
          var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn nt-choix'; b.innerHTML = cTxt;
          b.addEventListener('click', function () {
            if (S.answered) { return; } var ok = i === q[2];
            b.classList.add(ok ? 'nt-choix-ok' : 'nt-choix-ko'); if (!ok) { bx.children[q[2]].classList.add('nt-choix-ok'); }
            S.answer(ok, q[3], ok ? null : '<b>Non.</b> ');
          });
          bx.appendChild(b);
        });
      },
      bilan: function (g) { var r = g / Q.length; qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;' + Q.length + '</span><br>' + (r >= 0.85 ? 'Excellent&nbsp;: le chapitre est maîtrisé&nbsp;!' : (r >= 0.5 ? 'Bien. Relisez les explications des questions manquées, puis recommencez.' : 'Relisez le cours, puis recommencez&nbsp;: les questions seront mélangées.')); bx.innerHTML = ''; bx.hidden = true; }
    });
    S.start();
  })();

})();
</script>
