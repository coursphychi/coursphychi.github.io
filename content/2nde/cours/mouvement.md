+++
title = "Mouvement"
draft = false
hiddent = true
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-lab [hidden] { display: none !important; }
.nt-lab .nt-msg { margin-top: 0.8em !important; }
.nt-champ { display: inline-flex; align-items: center; gap: 0.35em; white-space: nowrap; margin: 0 0.5em; }
.nt-champ label { display: inline; margin: 0; font-weight: 600; }
.nt-champ input[type="text"] { width: 5.5em !important; min-width: 0; margin: 0; padding: 0.25em 0.5em; text-align: right; font: inherit; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-champ input.nt-large { width: 13em !important; text-align: left; }
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
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
@media (prefers-reduced-motion: reduce) { .nt-ql-btns .nt-choix, .nt-prog i { transition: none; } .nt-ql-btns .nt-choix:hover { transform: none; } }
/* couleurs du chapitre : déplacement en vert, vitesse en orange, trajectoire en rouge */
.nt-dep { color: #00957C; font-weight: 700; } .nt-vit { color: #C98A00; font-weight: 700; } .nt-traj { color: #3B82F6; }
.nt-prop .nt-dep { color: #00806A; } .nt-prop .nt-vit { color: #9A6700; }
.nt-f .nt-dep { color: #5EEAD4; } .nt-f .nt-vit { color: #FFD166; }
.nt-steps-nav { display: flex; align-items: center; justify-content: center; gap: 0.6em; flex-wrap: wrap; margin: 0.6em 0 0.2em; }
.nt-steps-nav .nt-pts { display: flex; gap: 0.35em; }
.nt-steps-nav .nt-pts i { width: 0.7em; height: 0.7em; border-radius: 50%; background: #E2E8F0; cursor: pointer; }
.nt-steps-nav .nt-pts i.fait { background: #93C5FD; } .nt-steps-nav .nt-pts i.cur { background: var(--blue); box-shadow: 0 0 0 2px #BFDBFE; }
.nt-etape { max-width: 680px; margin: 0.6em auto 0 !important; padding: 0.7em 1.1em; border-radius: 12px; background: var(--slate-bg); border: 1px solid var(--line); font-size: 1.02em; line-height: 1.75; text-align: center; min-height: 4.6em; }
.nt-etape b.t { display: block; color: var(--navy); margin-bottom: 0.15em; }
.nt-calc-l { display: inline-block; margin: 0.2em 0; font-family: Georgia, "Times New Roman", serif; font-size: 1.12em; }
.nt-fr { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; line-height: 1.25; font-size: 0.92em; margin: 0 0.15em; }
.nt-fr > span:first-child { border-bottom: 1px solid currentColor; padding: 0 0.35em 0.05em; }
.nt-fr > span + span { padding: 0.05em 0.35em 0; }
.nt-cmp { display: grid; grid-template-columns: auto auto; gap: 0.25em 1em; justify-content: center; margin: 0.5em auto 0; font-size: 0.95em; }
.nt-cmp .oui { color: #15803D; font-weight: 700; } .nt-cmp .non { color: #BE123C; font-weight: 700; }
.nt-data { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4em 1.2em; font-size: 0.95em; margin: 0.3em 0 0.5em; }
.nt-data span { background: #F1F5F9; border: 1px solid var(--line); border-radius: 8px; padding: 0.15em 0.6em; }
.nt-drum { border: 0; background: none; font-size: 1.3em; cursor: pointer; padding: 0 0.15em; vertical-align: -0.1em; }
.nt-drum:focus-visible { outline: 3px solid var(--blue-lt); border-radius: 6px; }
details.nt-d pre { overflow-x: auto; margin: 0.6em 0 !important; padding: 0.7em 1em; border-radius: 8px; background: #0F172A; color: #E2E8F0; font-size: 0.85em; line-height: 1.5; }
details.nt-d pre code { background: none; color: inherit; padding: 0; }
.nt-embed { position: relative; width: 100%; max-width: 640px; margin: 1em auto; }
.nt-embed video { display: block; width: 100%; border-radius: 12px; box-shadow: 0 6px 18px rgba(15,23,42,.15); }
.nt-sits { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; margin: 0.8em 0 0.4em; }
.nt-sit { border: 1.5px solid var(--line); border-radius: 12px; padding: 0.5em; background: #FFFFFF; display: flex; flex-direction: column; gap: 0.35em; }
.nt-sit canvas { border-radius: 8px; }
.nt-sit p { margin: 0 !important; font-size: 0.88em; line-height: 1.45; }
.nt-sit .nt-btn { align-self: center; font-size: 0.85em; }
.nt-sit .nt-btn[aria-pressed="true"] { background: var(--blue); color: #fff; }
.nt-sit.ok { border-color: #16A34A; background: #F0FDF4; } .nt-sit.ko { border-color: #E11D48; background: #FFF1F2; }
.nt-sit .nt-sit-exp { font-size: 0.85em; }
.nt-qsvg { display: block; margin: 0.3em auto; max-width: 100%; height: auto; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Une voiture qui démarre, une balle lancée, la Lune autour de la Terre… Pour décrire un mouvement sans ambiguïté, il faut répondre à trois questions&nbsp;: <b>qu'est-ce qui bouge</b> (le système), <b>par rapport à quoi</b> (le référentiel) et <b>comment</b> (la trajectoire et la vitesse). Ce chapitre introduit pour cela un outil nouveau et très puissant&nbsp;: le <b>vecteur vitesse</b>.</p>

## Relativité du mouvement {.nt-h2}

### Système {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>En physique, un <span class="imp nt-hole">système</span> est l'objet ou l'ensemble d'objets étudiés.</p>
</div>

<p>Définir un système correspond donc à tracer une frontière entre ce qui nous intéresse et son environnement.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<p>Une balle, un marteau, une voiture, la Lune, le système solaire…</p>
</div>

<p>Selon le système étudié, les distances et les durées utiles pour décrire son mouvement sont très différentes&nbsp;: ce sont ses <b>échelles caractéristiques</b>. On choisit les unités en conséquence.</p>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>système</th><th>échelle des distances</th><th>échelle des durées</th></tr></thead>
<tbody>
<tr><td>une fourmi qui se promène</td><td>quelques centimètres</td><td>quelques secondes</td></tr>
<tr><td>un sprinteur sur 100&nbsp;m</td><td>100&nbsp;m</td><td>10&nbsp;s</td></tr>
<tr><td>une voiture sur l'autoroute</td><td>des dizaines de kilomètres</td><td>des heures</td></tr>
<tr><td>la Lune autour de la Terre</td><td>380&nbsp;000&nbsp;km</td><td>27&nbsp;jours</td></tr>
<tr><td>la Terre autour du Soleil</td><td>150 millions de km</td><td>1&nbsp;an</td></tr>
</tbody>
</table></div>

### Référentiel {.nt-h3}

<p>Une fois qu'on a défini le système, il manque encore quelque chose d'important pour pouvoir décrire son mouvement… <span class="imp">le référentiel&nbsp;!</span></p>

<p>Vous êtes assis dans un train à quai, et le train voisin se met en mouvement&nbsp;: pendant un instant, impossible de savoir lequel des deux trains bouge. Qui bouge&nbsp;? Et par rapport à qui&nbsp;?</p>

<div class="nt-lab" id="lab-trains">
<p class="nt-tag"><i class="fa-solid fa-train"></i>Animation</p>
<p class="nt-lab-title">Assis dans le train, en gare… qui bouge&nbsp;?</p>
<p class="nt-note nt-center">Vous êtes assis dans un train, en gare. Par la fenêtre, vous ne voyez que le train d’à côté, qui masque tout le reste. Regardez-le bien.</p>
<canvas class="nt-fen" role="img" aria-label="Vue depuis un siège du train : par la fenêtre, on ne voit que le train d’à côté, qui glisse vers la gauche, s’arrête, puis glisse vers la droite."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Regarder par la fenêtre</button></div>
<p class="nt-msg" aria-live="polite">Lancez l’observation.</p>
<div class="nt-sits" hidden></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="verif" hidden><i class="fa-solid fa-check"></i>&nbsp; Vérifier</button></div>
</div>

<p>Pour décrire un mouvement de manière non ambiguë, il faut donc préciser par rapport à quoi on l'observe.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Pour décrire un mouvement de manière non ambiguë, il faut se placer dans un <span class="imp nt-hole">référentiel</span>&nbsp;: c'est l'objet de référence par rapport auquel on observe le mouvement, en quelque sorte l'observateur.</p>
<p>On le munit d'un <span class="imp nt-hole">repère spatial</span>, qui se déplace avec l'observateur, et d'un <span class="imp nt-hole">repère temporel</span> (une horloge).</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples de référentiels</p>
<ul class="nt-facts">
<li>Le <span class="imp">référentiel terrestre</span>, lié au sol (dans l'animation des trains, on peut imaginer un arbre).</li>
<li>Le référentiel du train vert (ce que voit un passager immobile dans ce train).</li>
<li>Le référentiel du train rouge (ce que voit un passager immobile dans l'autre train).</li>
<li>Le <span class="imp">référentiel géocentrique</span>, lié au centre de la Terre et à des étoiles lointaines, pour étudier par exemple le mouvement d'un satellite.</li>
</ul>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Un passager immobile par rapport au train n'est pas immobile dans le référentiel terrestre si le train avance… <span class="imp nt-hole">Le mouvement est relatif</span>&nbsp;: sa description dépend du référentiel choisi.</p>
</div>

<p>Un parachutiste saute d’un avion en même temps qu’un caméraman, qui le filme en tombant à côté de lui. Sur la vidéo, au moment où le parachute s’ouvre, le parachutiste semble filer vers le haut.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Est-ce que le parachutiste remonte lorsqu'il ouvre son parachute&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Une question mal posée</span></summary>
<div class="nt-d-body">
<p>La question est mal posée, car ambiguë&nbsp;: par rapport à qui est-il censé remonter&nbsp;? Une meilleure question serait&nbsp;: <b>dans quel référentiel</b> le parachutiste remonte-t-il&nbsp;?</p>
<p>Dans le référentiel du caméraman, qui continue de tomber à grande vitesse, le parachutiste remonte bel et bien. Mais dans le référentiel terrestre, il continue de descendre, simplement beaucoup moins vite qu'avant&nbsp;: il ne remonte jamais.</p>
</div>
</details>

<div class="nt-lab" id="lab-parach">
<p class="nt-tag"><i class="fa-solid fa-parachute-box"></i>Animation</p>
<p class="nt-lab-title">Le saut vu par deux observateurs</p>
<canvas role="img" aria-label="À gauche, la chute vue depuis le sol ; à droite, vue par le caméraman qui tombe à côté du parachutiste."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="saut"><i class="fa-solid fa-play"></i>&nbsp; Sauter</button><button type="button" class="nt-btn" data-act="ouvre" disabled><i class="fa-solid fa-parachute-box"></i>&nbsp; Ouvrir le parachute</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<p class="nt-msg" aria-live="polite">Les deux sauteurs tombent ensemble. Ouvrez le parachute quand vous voulez.</p>
</div>

### Petite énigme {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Énigme</p>
<p>Un bateau remonte une rivière et dépasse un radeau qui dérive au fil de l'eau. Une demi-heure après avoir dépassé le radeau, le bateau fait demi-tour. Il recroise le radeau 3&nbsp;km en aval du premier croisement.</p>
<p>On suppose que le bateau avance à vitesse constante par rapport à l'eau de la rivière. Quelle est la vitesse du courant&nbsp;?</p>
</div>

<div class="nt-lab" id="lab-radeau">
<p class="nt-tag"><i class="fa-solid fa-sailboat"></i>Animation</p>
<p class="nt-lab-title">Le bateau et le radeau</p>
<div class="nt-btns"><span class="nt-note">Observer depuis&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="rd-ref" value="terre" checked><span>la berge</span></label><label><input type="radio" name="rd-ref" value="eau"><span>le radeau (l'eau)</span></label></div></div>
<canvas role="img" aria-label="Vue de dessus de la rivière : le bateau, le radeau, et les berges graduées en kilomètres."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-play"></i>&nbsp; Lancer</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<p class="nt-msg" aria-live="polite">Essayez d'abord de résoudre l'énigme… puis observez la scène depuis le radeau.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Tout devient simple dans le bon référentiel</span></summary>
<div class="nt-d-body">
<p>Dans le référentiel terrestre, le calcul est pénible&nbsp;: le bateau ne va pas à la même vitesse en remontant et en descendant le courant. Plaçons-nous plutôt dans le référentiel de l'eau, où le radeau est immobile.</p>
<p>Dans ce référentiel, le bateau s'éloigne du radeau pendant 30&nbsp;minutes, puis revient vers lui à la même vitesse&nbsp;: il met donc aussi 30&nbsp;minutes pour le rejoindre. Les deux croisements sont séparés d'<b>une heure</b>.</p>
<p>Pendant cette heure, le radeau, qui suit le courant, a parcouru 3&nbsp;km par rapport à la berge. La vitesse du courant est donc $v = \dfrac{\pu{3 km}}{\pu{1 h}} = \pu{3 km/h}$, quelle que soit la vitesse du bateau.</p>
</div>
</details>

## Description d'un mouvement {.nt-h2}

<p>Une fois qu'on a choisi le système et le référentiel, il nous reste à décrire le mouvement. Pour cela, on a besoin de sa <span class="imp">trajectoire</span> et de sa <span class="imp" style="color:#C98A00">vitesse</span>.</p>

### Trajectoire {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp nt-hole">trajectoire</span> d'un point, dans un référentiel d'étude donné, correspond à la courbe formée par l'<span class="imp nt-hole">ensemble des positions successivement occupées</span> par ce point au cours de son mouvement.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Les fumigènes d'un avion de voltige laissent dans le ciel une traînée de fumée qui matérialise la trajectoire de l'avion dans le référentiel terrestre. Un deuxième avion qui volerait à côté de lui, exactement à la même vitesse, le verrait immobile&nbsp;: dans son référentiel, la trajectoire se réduirait à un point.</p>
</div>

### Translation et rotation {.nt-h3}

<p>Pour un système étendu, chacun de ses points a sa propre trajectoire. On distingue deux types de mouvements particuliers.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Dans un <span class="imp nt-hole">mouvement de translation</span>, tous les points du système ont des trajectoires identiques (superposables)&nbsp;: le système se déplace sans tourner sur lui-même.</p>
<p>Dans un <span class="imp nt-hole">mouvement de rotation</span> autour d'un axe fixe, tous les points du système (sauf ceux situés sur l'axe) ont pour trajectoire un <span class="imp nt-hole">cercle</span> centré sur l'axe.</p>
</div>

<div class="nt-lab" id="lab-types">
<p class="nt-tag"><i class="fa-solid fa-arrows-spin"></i>Animation</p>
<p class="nt-lab-title">Translation, rotation… ou les deux&nbsp;?</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="ty-m" value="trans" checked><span>Translation rectiligne</span></label><label><input type="radio" name="ty-m" value="circ"><span>Translation circulaire</span></label><label><input type="radio" name="ty-m" value="rot"><span>Rotation</span></label><label><input type="radio" name="ty-m" value="lancer"><span>Marteau lancé</span></label></div></div>
<canvas role="img" aria-label="Un marteau en mouvement ; trois de ses points laissent la trace de leur trajectoire."></canvas>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="chrono" checked> Chronophotographie</label><label class="nt-check"><input type="checkbox" data-in="traces" checked> Trajectoires</label><button type="button" class="nt-btn" data-act="replay"><i class="fa-solid fa-rotate-left"></i>&nbsp; Rejouer</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Une translation n'est pas forcément rectiligne&nbsp;! La nacelle d'une grande roue reste toujours horizontale&nbsp;: tous ses points décrivent des cercles identiques, décalés les uns des autres, et pourtant elle ne tourne pas sur elle-même. C'est une translation circulaire, et non une rotation.</p>
</div>

<p>La plupart des mouvements sont une combinaison des deux&nbsp;: une translation d'ensemble et une rotation propre. Pour un objet libre, lancé dans l'air par exemple, cette rotation se fait autour d'un point précis&nbsp;: le <span class="imp">centre de masse</span> du système (en revanche, une porte ou une roue fixée à un axe tourne autour de cet axe).</p>

<p>Le centre de masse est ainsi le point du système qui a la trajectoire la plus simple&nbsp;: c'est celle que tous les autres points auraient si le mouvement était une pure translation. Dans le lancer de marteau ci-dessus, le centre de masse décrit une simple parabole, alors que le bout du manche décrit une courbe bien plus compliquée.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour simplifier, on réduit souvent le système étudié à <span class="imp nt-hole">un point</span>, en général son centre de masse. Mais on <span class="imp nt-hole">perd</span> alors l'information sur sa <span class="imp nt-hole">rotation</span> (et sur sa forme)&nbsp;: c'est le prix à payer pour la simplicité.</p>
</div>

<p>Dorénavant, on étudiera surtout des systèmes réduits à un point.</p>

### Trajectoires particulières {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>La trajectoire d'un point est dite&nbsp;:</p>
<ul class="nt-facts">
<li><span class="imp nt-hole">rectiligne</span> si elle forme une droite&nbsp;;</li>
<li><span class="imp nt-hole">circulaire</span> si elle forme un cercle (ou un arc de cercle)&nbsp;;</li>
<li><span class="imp nt-hole">curviligne</span> (ou quelconque) dans les autres cas.</li>
</ul>
</div>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 720 190' role='img' aria-label="Positions successives d'un point le long d'une droite, d'un cercle et d'une courbe quelconque."><text x='120' y='22' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>rectiligne</text><line x1='25' y1='155.6' x2='215' y2='48.7' stroke='#3B82F6' stroke-width='1.2' stroke-dasharray='4 4' opacity='0.8'/><path d='M30.5,145.5 L39.5,154.5 M39.5,145.5 L30.5,154.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M62.5,127.5 L71.5,136.5 M71.5,127.5 L62.5,136.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M94.5,109.5 L103.5,118.5 M103.5,109.5 L94.5,118.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M126.5,91.5 L135.5,100.5 M135.5,91.5 L126.5,100.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M158.5,73.5 L167.5,82.5 M167.5,73.5 L158.5,82.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M190.5,55.5 L199.5,64.5 M199.5,55.5 L190.5,64.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><text x='360' y='22' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>circulaire</text><circle cx='360' cy='105' r='62' fill='none' stroke='#3B82F6' stroke-width='1.2' stroke-dasharray='4 4' opacity='0.8'/><path d='M417.5,100.5 L426.5,109.5 M426.5,100.5 L417.5,109.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M405.7,136.9 L414.7,145.9 M414.7,136.9 L405.7,145.9' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M374.7,159.5 L383.7,168.5 M383.7,159.5 L374.7,168.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M336.3,159.5 L345.3,168.5 M345.3,159.5 L336.3,168.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M305.3,136.9 L314.3,145.9 M314.3,136.9 L305.3,145.9' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M293.5,100.5 L302.5,109.5 M302.5,100.5 L293.5,109.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M305.3,64.1 L314.3,73.1 M314.3,64.1 L305.3,73.1' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M336.3,41.5 L345.3,50.5 M345.3,41.5 L336.3,50.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M374.7,41.5 L383.7,50.5 M383.7,41.5 L374.7,50.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M405.7,64.1 L414.7,73.1 M414.7,64.1 L405.7,73.1' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><text x='600' y='22' font-size='14' text-anchor='middle' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>curviligne</text><path d='M510.0,150.0 L513.0,145.0 L516.0,140.0 L519.0,135.0 L522.0,130.0 L525.0,125.1 L528.0,120.2 L531.0,115.5 L534.0,110.9 L537.0,106.5 L540.0,102.3 L543.0,98.3 L546.0,94.6 L549.0,91.3 L552.0,88.2 L555.0,85.5 L558.0,83.2 L561.0,81.2 L564.0,79.5 L567.0,78.3 L570.0,77.3 L573.0,76.7 L576.0,76.4 L579.0,76.3 L582.0,76.5 L585.0,76.9 L588.0,77.5 L591.0,78.2 L594.0,78.9 L597.0,79.8 L600.0,80.6 L603.0,81.5 L606.0,82.3 L609.0,83.1 L612.0,83.8 L615.0,84.4 L618.0,85.0 L621.0,85.5 L624.0,86.0 L627.0,86.4 L630.0,86.9 L633.0,87.5 L636.0,88.1 L639.0,88.8 L642.0,89.8 L645.0,90.9 L648.0,92.3 L651.0,94.0 L654.0,96.1 L657.0,98.5 L660.0,101.4 L663.0,104.6 L666.0,108.2 L669.0,112.3 L672.0,116.8 L675.0,121.6 L678.0,126.8 L681.0,132.3 L684.0,138.1 L687.0,144.0 L690.0,150.0' fill='none' stroke='#3B82F6' stroke-width='1.2' stroke-dasharray='4 4' opacity='0.8'/><path d='M505.5,145.5 L514.5,154.5 M514.5,145.5 L505.5,154.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M531.2,103.8 L540.2,112.8 M540.2,103.8 L531.2,112.8' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M556.9,76.4 L565.9,85.4 M565.9,76.4 L556.9,85.4' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M582.6,72.8 L591.6,81.8 M591.6,72.8 L582.6,81.8' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M608.4,79.4 L617.4,88.4 M617.4,79.4 L608.4,88.4' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M634.1,84.2 L643.1,93.2 M643.1,84.2 L634.1,93.2' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M659.8,101.6 L668.8,110.6 M668.8,101.6 L659.8,110.6' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/><path d='M685.5,145.5 L694.5,154.5 M694.5,145.5 L685.5,154.5' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/></svg></div>
<p class="nt-cap">Chronophotographies de trois mouvements&nbsp;: les croix marquent les positions successives du point étudié, à intervalles de temps égaux.</p>

## Déplacement et vitesse {.nt-h2}

<p>La vitesse est un élément essentiel de la description d'un mouvement. Mais plutôt que de se contenter de sa seule valeur (« 50&nbsp;km/h »), ne pourrait-on pas aussi indiquer <b>dans quelle direction</b> et <b>dans quel sens</b> se fait le mouvement&nbsp;? On introduit alors <button type="button" class="nt-drum" aria-label="roulement de tambour" title="roulement de tambour">🥁</button> le <span class="imp" style="color:#C98A00">vecteur vitesse</span>.</p>

### Rappel&nbsp;: qu'est-ce qu'un vecteur&nbsp;? {.nt-h3}

<p>Un vecteur est un objet mathématique qui se représente par une flèche. Il réunit en un seul objet trois informations.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le vecteur $\overrightarrow{\mathrm{AB}}$, représenté par une flèche allant du point A au point B, est caractérisé par&nbsp;:</p>
<ul class="nt-facts">
<li>sa <span class="imp nt-hole">direction</span>&nbsp;: celle de la droite (AB)&nbsp;;</li>
<li>son <span class="imp nt-hole">sens</span>&nbsp;: de A vers B (une même direction offre deux sens possibles)&nbsp;;</li>
<li>sa <span class="imp nt-hole">norme</span>&nbsp;: la longueur AB de la flèche, notée $\lVert \overrightarrow{\mathrm{AB}} \rVert$ ou simplement AB.</li>
</ul>
<p>Deux vecteurs sont <span class="imp nt-hole">égaux</span> s'ils ont même direction, même sens et même norme, même s'ils ne partent pas du même point.</p>
</div>

<div class="nt-lab" id="lab-vecteur">
<p class="nt-tag"><i class="fa-solid fa-arrow-right-long"></i>Animation</p>
<p class="nt-lab-title">Direction, sens, norme</p>
<canvas class="nt-drag" role="img" aria-label="Deux vecteurs sur un quadrillage ; on peut déplacer leurs extrémités."></canvas>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="dir" checked> Directions</label><label class="nt-check"><input type="checkbox" data-in="norme" checked> Normes</label><button type="button" class="nt-btn" data-act="egaux"><i class="fa-solid fa-equals"></i>&nbsp; Exemple de vecteurs égaux</button><button type="button" class="nt-btn" data-act="opp"><i class="fa-solid fa-right-left"></i>&nbsp; Exemple de sens opposés</button></div>
<div class="nt-cmp" aria-live="polite"></div>
<p class="nt-msg" aria-live="polite">Faites glisser les extrémités des flèches (les points ronds) et comparez les deux vecteurs.</p>
</div>

### Vecteur déplacement {.nt-h3}

<p>Pour définir le vecteur vitesse, on a d'abord besoin du <span class="nt-dep">vecteur déplacement</span>.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Si un point mobile passe par la position M, puis par la position M' un peu plus tard, son <span class="imp nt-hole">vecteur déplacement</span> entre ces deux instants est le vecteur ${\color{#00957C}{\overrightarrow{\mathrm{MM'}}}}$, qui va de la position de départ M à la position d'arrivée M'.</p>
</div>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-m' viewBox='0 -10 740 460' role='img' aria-label="Un point passe de M à M' en suivant un chemin sinueux avec une boucle ; le vecteur déplacement MM' est la flèche rectiligne de M vers M'."><path d='M42.0,360.0 L42.2,358.1 L42.5,355.9 L42.7,353.3 L42.9,350.6 L43.1,347.5 L43.4,344.3 L43.6,340.9 L43.9,337.3 L44.3,333.5 L44.6,329.7 L45.0,325.7 L45.5,321.7 L46.0,317.7 L46.6,313.6 L47.3,309.5 L48.0,305.4 L48.9,301.4 L49.8,297.5 L50.9,293.7 L52.0,290.0 L53.2,286.3 L54.6,282.6 L56.0,278.9 L57.5,275.1 L59.0,271.2 L60.6,267.4 L62.4,263.5 L64.1,259.6 L66.0,255.8 L67.9,251.9 L69.8,248.0 L71.9,244.2 L74.0,240.3 L76.1,236.6 L78.3,232.8 L80.5,229.1 L82.8,225.5 L85.2,221.9 L87.6,218.4 L90.0,215.0 L92.5,211.6 L95.0,208.3 L97.6,204.9 L100.3,201.6 L103.0,198.2 L105.8,195.0 L108.6,191.7 L111.5,188.5 L114.4,185.3 L117.4,182.2 L120.4,179.1 L123.5,176.1 L126.6,173.2 L129.8,170.3 L133.1,167.5 L136.4,164.8 L139.7,162.2 L143.1,159.7 L146.5,157.3 L150.0,155.0 L153.6,152.8 L157.2,150.6 L161.0,148.5 L164.9,146.5 L168.8,144.5 L172.8,142.6 L176.9,140.8 L181.0,139.1 L185.2,137.4 L189.4,135.8 L193.6,134.3 L197.8,132.9 L201.9,131.6 L206.1,130.3 L210.2,129.2 L214.3,128.2 L218.4,127.2 L222.3,126.4 L226.2,125.6 L230.0,125.0 L233.8,124.5 L237.5,124.1 L241.3,123.8 L245.1,123.6 L248.8,123.5 L252.6,123.6 L256.3,123.7 L260.0,123.9 L263.7,124.2 L267.3,124.6 L270.9,125.0 L274.4,125.6 L277.9,126.2 L281.3,126.8 L284.6,127.6 L287.9,128.3 L291.1,129.2 L294.1,130.1 L297.1,131.0 L300.0,132.0 L302.8,133.1 L305.6,134.3 L308.3,135.6 L310.9,137.0 L313.5,138.6 L316.1,140.2 L318.6,141.9 L321.0,143.6 L323.3,145.4 L325.6,147.2 L327.7,149.1 L329.8,151.0 L331.8,152.9 L333.7,154.7 L335.6,156.6 L337.3,158.4 L338.9,160.1 L340.4,161.8 L341.7,163.5 L343.0,165.0 L344.1,166.5 L345.1,168.0 L346.0,169.5 L346.8,171.0 L347.5,172.5 L348.0,174.0 L348.5,175.5 L348.8,176.9 L349.1,178.3 L349.3,179.8 L349.4,181.1 L349.5,182.5 L349.5,183.8 L349.4,185.1 L349.3,186.4 L349.1,187.6 L348.9,188.8 L348.6,189.9 L348.3,191.0 L348.0,192.0 L347.6,193.0 L347.1,194.0 L346.6,195.0 L345.9,195.9 L345.2,196.9 L344.4,197.8 L343.6,198.7 L342.6,199.6 L341.7,200.4 L340.7,201.1 L339.7,201.8 L338.6,202.5 L337.5,203.1 L336.4,203.6 L335.3,204.0 L334.2,204.4 L333.1,204.7 L332.1,204.9 L331.0,205.0 L330.0,205.0 L329.0,204.9 L327.9,204.7 L326.8,204.5 L325.6,204.2 L324.5,203.8 L323.3,203.3 L322.0,202.8 L320.8,202.2 L319.6,201.5 L318.4,200.8 L317.2,200.0 L316.0,199.1 L314.8,198.2 L313.7,197.2 L312.6,196.2 L311.6,195.0 L310.6,193.9 L309.7,192.6 L308.8,191.3 L308.0,190.0 L307.3,188.6 L306.6,187.1 L305.9,185.5 L305.3,183.8 L304.7,182.1 L304.2,180.3 L303.6,178.4 L303.2,176.5 L302.7,174.5 L302.3,172.5 L301.9,170.4 L301.6,168.3 L301.3,166.1 L301.0,163.9 L300.8,161.6 L300.5,159.4 L300.4,157.1 L300.2,154.7 L300.1,152.4 L300.0,150.0 L299.9,147.6 L299.9,145.1 L299.9,142.5 L299.8,139.9 L299.9,137.2 L299.9,134.4 L300.0,131.7 L300.1,128.8 L300.3,126.0 L300.4,123.1 L300.7,120.2 L300.9,117.4 L301.3,114.5 L301.6,111.6 L302.0,108.8 L302.5,105.9 L303.0,103.1 L303.6,100.4 L304.3,97.7 L305.0,95.0 L305.8,92.4 L306.6,89.7 L307.4,87.1 L308.3,84.4 L309.3,81.8 L310.2,79.1 L311.3,76.5 L312.4,73.8 L313.5,71.2 L314.7,68.6 L315.9,66.1 L317.2,63.5 L318.6,61.0 L320.0,58.6 L321.5,56.2 L323.1,53.8 L324.7,51.5 L326.4,49.3 L328.2,47.1 L330.0,45.0 L331.9,42.9 L333.9,40.9 L336.0,38.9 L338.2,36.9 L340.5,34.9 L342.8,33.0 L345.3,31.1 L347.7,29.3 L350.2,27.5 L352.8,25.8 L355.4,24.1 L358.1,22.4 L360.8,20.9 L363.5,19.4 L366.2,18.0 L369.0,16.6 L371.7,15.3 L374.5,14.1 L377.2,13.0 L380.0,12.0 L382.8,11.1 L385.6,10.2 L388.4,9.4 L391.2,8.6 L394.1,7.9 L396.9,7.3 L399.9,6.7 L402.8,6.2 L405.8,5.8 L408.8,5.4 L411.8,5.2 L414.8,4.9 L417.9,4.8 L420.9,4.7 L424.1,4.8 L427.2,4.8 L430.4,5.0 L433.6,5.3 L436.8,5.6 L440.0,6.0 L443.3,6.5 L446.6,7.1 L450.0,7.7 L453.4,8.5 L456.8,9.3 L460.3,10.2 L463.8,11.1 L467.3,12.2 L470.8,13.3 L474.4,14.5 L477.9,15.8 L481.5,17.1 L485.1,18.5 L488.7,19.9 L492.3,21.5 L495.8,23.1 L499.4,24.7 L503.0,26.4 L506.5,28.2 L510.0,30.0 L513.5,31.9 L517.0,33.8 L520.5,35.9 L524.0,38.0 L527.5,40.2 L530.9,42.4 L534.4,44.7 L537.9,47.1 L541.4,49.5 L544.9,52.0 L548.4,54.6 L551.9,57.2 L555.4,59.8 L558.9,62.6 L562.4,65.3 L565.9,68.2 L569.4,71.1 L572.9,74.0 L576.5,77.0 L580.0,80.0 L583.6,83.2 L587.4,86.6 L591.4,90.3 L595.4,94.1 L599.5,98.1 L603.7,102.3 L607.9,106.4 L612.1,110.7 L616.3,114.9 L620.4,119.1 L624.4,123.3 L628.3,127.3 L632.0,131.2 L635.6,135.0 L639.0,138.5 L642.2,141.9 L645.1,144.9 L647.7,147.6 L650.0,150.0 L652.0,152.0' fill='none' stroke='#3A7BC8' stroke-width='3.2' stroke-dasharray='15 11' stroke-linecap='round'/><line x1='42.0' y1='360.0' x2='618.3' y2='163.8' stroke='#00AB8E' stroke-width='8' stroke-linecap='round'/><polygon points='644.0,155.0 616.7,180.2 607.0,151.8' fill='#00AB8E'/><path d='M33,351 L51,369 M51,351 L33,369' stroke='#1E4E79' stroke-width='4' stroke-linecap='round'/><path d='M643,143 L661,161 M661,143 L643,161' stroke='#1E4E79' stroke-width='4' stroke-linecap='round'/><text x='42' y='430' font-size='40' text-anchor='middle' fill='#1E4E79' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>M</text><text x='682' y='222' font-size='40' text-anchor='middle' fill='#1E4E79' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>M′</text></svg></div>
<p class="nt-cap">Le vecteur déplacement ne dit rien du chemin suivi entre M et M' (en pointillés)&nbsp;: il ne retient que le point de départ et le point d'arrivée.</p>

### Vecteur vitesse moyenne {.nt-h3}

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">${\color{#FFD166}{\vec{v}_{\text{moy}}}} = \dfrac{{\color{#5EEAD4}{\overrightarrow{\mathrm{MM'}}}}}{\Delta t}$</p>
<div class="nt-f-units"><span>$\Delta t$&nbsp;: durée pour aller de M à M'</span></div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp nt-hole">vecteur vitesse moyenne</span> ${\color{#C98A00}{\vec{v}_{\text{moy}}}}$ entre M et M' est donc défini comme le vecteur&nbsp;:</p>
<ul class="nt-facts">
<li>de <span class="imp nt-hole">même direction</span> que ${\color{#00957C}{\overrightarrow{\mathrm{MM'}}}}$&nbsp;;</li>
<li>de <span class="imp nt-hole">même sens</span> que ${\color{#00957C}{\overrightarrow{\mathrm{MM'}}}}$&nbsp;;</li>
<li>et de norme ${\color{#C98A00}{v_{\text{moy}}}}$ donnée par&nbsp;: ${\color{#C98A00}{v_{\text{moy}}}} = \dfrac{\mathrm{MM'}}{\Delta t}$.</li>
</ul>
</div>

<p>Diviser un vecteur par un nombre positif (ici $\Delta t$) ne change ni sa direction ni son sens&nbsp;: cela ne change que sa longueur. C'est pourquoi le vecteur vitesse moyenne «&nbsp;pointe&nbsp;» exactement comme le vecteur déplacement.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Dans le <span class="imp">Système international d'unités (SI)</span>&nbsp;: MM' est mesuré en <span class="imp nt-hole">mètres (m)</span>, $\Delta t$ en <span class="imp nt-hole">secondes (s)</span>, et donc $v_{\text{moy}}$ s'exprime en <span class="imp nt-hole">mètres par seconde</span> ($\pu{m*s-1}$, que l'on écrit aussi m/s).</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>MM' est la distance <b>en ligne droite</b> entre M et M'. Si la trajectoire est courbe, elle est plus petite que la distance réellement parcourue le long de la trajectoire. Les deux sont presque égales lorsque M' est très proche de M&nbsp;: c'est pourquoi on choisira toujours des positions M et M' très voisines.</p>
</div>

### Tracer un vecteur vitesse {.nt-h3}

<p>En pratique, on étudie le mouvement sur une <b>chronophotographie</b> (ou sur une vidéo image par image)&nbsp;: les positions successives du point étudié, enregistrées à intervalles de temps égaux $\Delta t$.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Méthode</p>
<p>Pour tracer le vecteur vitesse au point M d'une chronophotographie&nbsp;:</p>
<ol class="nt-steps">
<li><p>Repérer la position suivante M' et tracer le <span class="nt-dep">vecteur déplacement $\overrightarrow{\mathrm{MM'}}$</span>.</p></li>
<li><p>Mesurer la longueur MM' <b>sur le document</b> (en cm), puis la convertir en mètres grâce à l'<b>échelle des distances</b>.</p></li>
<li><p>Calculer la vitesse&nbsp;: $v = \dfrac{\mathrm{MM'}}{\Delta t}$, avec MM' en m et $\Delta t$ en s.</p></li>
<li><p>Convertir cette vitesse en longueur de flèche grâce à l'<b>échelle des vitesses</b>.</p></li>
<li><p>Tracer, <b>à partir du point M</b>, la flèche du <span class="nt-vit">vecteur vitesse</span>&nbsp;: même direction et même sens que $\overrightarrow{\mathrm{MM'}}$, et la longueur calculée.</p></li>
</ol>
</div>

<div class="nt-lab" id="lab-constr">
<p class="nt-tag"><i class="fa-solid fa-pen-ruler"></i>Animation pas à pas</p>
<p class="nt-lab-title">Construire un vecteur vitesse, étape par étape</p>
<canvas role="img" aria-label="Chronophotographie d'une balle, avec la construction du vecteur déplacement, sa mesure à la règle et le tracé du vecteur vitesse."></canvas>
<div class="nt-steps-nav"><button type="button" class="nt-btn" data-act="prec"><i class="fa-solid fa-chevron-left"></i>&nbsp; Étape précédente</button><span class="nt-pts" aria-hidden="true"></span><button type="button" class="nt-btn nt-btn-main" data-act="suiv">Étape suivante&nbsp; <i class="fa-solid fa-chevron-right"></i></button></div>
<div class="nt-etape" aria-live="polite"></div>
</div>

<div class="nt-lab nt-trainer" id="tr-vecteur">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">À vous de tracer des vecteurs vitesse</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard nt-qcard-w">
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-data"></div>
<canvas class="nt-drag" role="img" aria-label="Chronophotographie sur papier quadrillé ; on trace le vecteur vitesse en faisant glisser l'extrémité de la flèche."></canvas>
<div class="nt-tr-ans" data-etape="1"><span class="nt-champ"><label for="trv-v">$v$&nbsp;=</label><input id="trv-v" type="text" inputmode="decimal" autocomplete="off"><span class="nt-u">m/s</span></span><button type="button" class="nt-btn nt-btn-main" data-act="check-v"><i class="fa-solid fa-check"></i>&nbsp; Valider la vitesse</button></div>
<div class="nt-tr-ans" data-etape="2" hidden><span class="nt-note">Faites glisser la pointe de la flèche orange, puis&nbsp;</span><button type="button" class="nt-btn nt-btn-main" data-act="check-f"><i class="fa-solid fa-check"></i>&nbsp; Valider le tracé</button></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>

### Vecteur vitesse en un point {.nt-h3}

<p>Problème&nbsp;: le vecteur vitesse moyenne entre M et M' ne dit pas grand-chose de la vitesse au point M à l'instant $t$, surtout si M' est loin de M et que la trajectoire fait des détours entre les deux. Comment améliorer la définition pour avoir accès à la vitesse <b>au point M</b>&nbsp;?</p>

<div class="nt-lab" id="lab-inst">
<p class="nt-tag"><i class="fa-solid fa-magnifying-glass"></i>Animation</p>
<p class="nt-lab-title">Rapprocher M' de M</p>
<canvas role="img" aria-label="Une trajectoire courbe, le point M fixe et le point M' qui se rapproche ; le vecteur vitesse moyenne tend vers le vecteur vitesse en M, tangent à la trajectoire."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Instant $t$ du passage en M&nbsp;: <b class="out-t"></b><input type="range" min="0" max="100" step="1" value="12" data-in="tm"></label><label class="nt-ctrl">Durée $\Delta t$ entre M et M'&nbsp;: <b class="out-dt"></b><input type="range" min="0" max="100" step="1" value="100" data-in="dt"></label></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="anim"><i class="fa-solid fa-play"></i>&nbsp; Faire tendre $\Delta t$ vers 0</button><label class="nt-check"><input type="checkbox" data-in="tan"> Tangente en M</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Pour passer du vecteur vitesse moyenne entre M et M' au <span class="imp nt-hole">vecteur vitesse en M</span>, noté ${\color{#C98A00}{\vec{v}}}$, on rapproche le plus possible M' de M le long de la trajectoire (on fait tendre $\Delta t$ vers 0).</p>
<p>Le vecteur vitesse en M est alors <span class="imp nt-hole">tangent à la trajectoire</span> en M, orienté dans le <span class="imp nt-hole">sens du mouvement</span>, et sa norme est la vitesse du point à cet instant.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Sur une chronophotographie, on approche le vecteur vitesse au point $\mathrm{M}_i$ par le vecteur vitesse moyenne entre $\mathrm{M}_i$ et la position suivante $\mathrm{M}_{i+1}$&nbsp;:</p>
<p class="nt-big">${\color{#9A6700}{\vec{v}_i}} \approx \dfrac{{\color{#00806A}{\overrightarrow{\mathrm{M}_i\mathrm{M}_{i+1}}}}}{\Delta t}$</p>
<p>L'approximation est d'autant meilleure que $\Delta t$ est petit.</p>
</div>

### Mouvements uniformes et rectilignes {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Si la <span class="imp nt-hole">vitesse $v$ est constante</span> le long de la trajectoire, le mouvement est dit <span class="imp nt-hole">uniforme</span>. Sinon, il est <span class="imp nt-hole">accéléré</span> (la vitesse augmente) ou <span class="imp nt-hole">ralenti</span> (la vitesse diminue).</p>
<p>Si le mouvement est <span class="imp">rectiligne</span>, le vecteur vitesse garde toujours la même direction, celle de la droite trajectoire. S'il est en plus <span class="imp">uniforme</span>, le <span class="imp nt-hole">vecteur vitesse est constant</span>&nbsp;: même direction, même sens et même norme à tout instant.</p>
</div>

<div class="nt-lab" id="lab-chrono">
<p class="nt-tag"><i class="fa-solid fa-camera"></i>Animation</p>
<p class="nt-lab-title">Lire une chronophotographie</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="ch-m" value="ru" checked><span>Rectiligne uniforme</span></label><label><input type="radio" name="ch-m" value="ra"><span>Rectiligne accéléré</span></label><label><input type="radio" name="ch-m" value="rr"><span>Rectiligne ralenti</span></label><label><input type="radio" name="ch-m" value="cu"><span>Circulaire uniforme</span></label><label><input type="radio" name="ch-m" value="pa"><span>Ballon lancé</span></label></div></div>
<canvas role="img" aria-label="Chronophotographie d'un mouvement, avec en option les vecteurs vitesse en chaque position."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="replay"><i class="fa-solid fa-camera"></i>&nbsp; Prendre la chronophotographie</button><label class="nt-check"><input type="checkbox" data-in="vec"> Vecteurs vitesse</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: décrire la variation du vecteur vitesse</p>
<ul class="nt-facts">
<li>Positions <b>également espacées</b> sur une chronophotographie&nbsp;: la vitesse est <span class="imp nt-hole">constante</span>, le mouvement est uniforme.</li>
<li>Positions de <b>plus en plus espacées</b>&nbsp;: la norme du vecteur vitesse <span class="imp nt-hole">augmente</span>, le mouvement est accéléré.</li>
<li>Positions de <b>plus en plus rapprochées</b>&nbsp;: la norme du vecteur vitesse <span class="imp nt-hole">diminue</span>, le mouvement est ralenti.</li>
<li>Trajectoire <b>courbe</b>&nbsp;: la <span class="imp nt-hole">direction</span> du vecteur vitesse change, même si sa norme reste constante (mouvement circulaire uniforme).</li>
</ul>
</div>

<div class="nt-lab nt-quizlab" id="quiz-chrono">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Quel est ce mouvement&nbsp;?</p>
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

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Tracer positions et vecteurs vitesse avec Python</span></summary>
<div class="nt-d-body">
<p>Un programme peut faire tout le travail&nbsp;: à partir des coordonnées $(x, y)$ des positions successives, relevées par exemple sur une vidéo, il calcule les vecteurs vitesse et les trace. Lancez-le avec ▶, puis modifiez les positions ou la durée <code>dt</code> et relancez.</p>
{{< runpython lang="pyodide" height="auto">}}
import matplotlib.pyplot as plt
plt.style.use('bmh')

dt = 0.04                                       # durée entre deux positions (s)
x = [0.00, 0.20, 0.39, 0.57, 0.74, 0.90, 1.05]  # abscisses (m)
y = [0.00, 0.17, 0.30, 0.39, 0.44, 0.45, 0.42]  # ordonnées (m)

plt.plot(x, y, 'r+')                            # positions successives
for i in range(len(x) - 1):
    vx = (x[i+1] - x[i]) / dt                   # coordonnées du vecteur vitesse
    vy = (y[i+1] - y[i]) / dt
    plt.quiver(x[i], y[i], vx, vy, color='orange', angles='xy', scale_units='xy', scale=30)
plt.axis('equal')
plt.show()
{{< /runpython >}}
<p>Le vecteur vitesse au point $\mathrm{M}_i$ a pour coordonnées $v_x = \dfrac{x_{i+1} - x_i}{\Delta t}$ et $v_y = \dfrac{y_{i+1} - y_i}{\Delta t}$&nbsp;: c'est exactement la relation ${\vec{v}_i} \approx \dfrac{\overrightarrow{\mathrm{M}_i\mathrm{M}_{i+1}}}{\Delta t}$, écrite coordonnée par coordonnée.</p>
</div>
</details>

## Vitesse et trajectoire dépendent du référentiel {.nt-h2}

<p>Un rebondeur saute sur un trampoline installé sur une remorque, tirée à vitesse constante par un tracteur. Il monte et redescend… et retombe toujours sur le trampoline, alors que la remorque a avancé pendant son saut.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Quelle est la trajectoire du rebondeur dans le référentiel du tracteur&nbsp;? Et dans le référentiel terrestre&nbsp;?</p>
<p>Que peut-on dire de la composante horizontale de sa vitesse (la vitesse de son ombre sur le sol) dans ces deux référentiels&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Un aller-retour vertical… ou une succession d'arches</span></summary>
<div class="nt-d-body">
<p>Dans le référentiel du tracteur, le rebondeur monte et redescend à la verticale, toujours au-dessus du même endroit du trampoline&nbsp;: sa trajectoire est un <b>segment de droite vertical</b>, parcouru dans un sens puis dans l'autre.</p>
<p>Dans le référentiel terrestre, il avance en même temps que la remorque&nbsp;: sa trajectoire est une succession d'<b>arches</b> (des paraboles).</p>
<p>La composante horizontale de sa vitesse, celle de son ombre, est <b>nulle</b> dans le référentiel du tracteur, et <b>égale à la vitesse du tracteur</b> dans le référentiel terrestre. Elle reste constante pendant tout le saut&nbsp;: une fois en l'air, rien ne freine ni ne pousse horizontalement le rebondeur, il continue simplement d'avancer à la vitesse qu'il avait au départ. C'est pourquoi il retombe toujours sur le trampoline.</p>
</div>
</details>

<div class="nt-lab" id="lab-tramp">
<p class="nt-tag"><i class="fa-solid fa-tractor"></i>Animation</p>
<p class="nt-lab-title">Une balle qui rebondit sur une remorque</p>
<div class="nt-btns"><span class="nt-note">Observer depuis&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="tp-ref" value="tracteur" checked><span>le tracteur</span></label><label><input type="radio" name="tp-ref" value="sol"><span>le sol</span></label></div></div>
<canvas role="img" aria-label="Une balle rebondit sur un trampoline tiré par un tracteur ; trajectoire en pointillés et vecteur vitesse de la balle."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="acc"><i class="fa-solid fa-gauge-high"></i>&nbsp; Accélérer</button><button type="button" class="nt-btn" data-act="frein"><i class="fa-solid fa-hand"></i>&nbsp; Freiner</button><button type="button" class="nt-btn nt-btn-main" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="comp" checked> Décomposer la vitesse</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>Autre expérience, encore plus surprenante&nbsp;: un pick-up roule à 50&nbsp;km/h. À l’arrière, un canon horizontal tire un ballon de football <b>vers l’arrière</b>, à 50&nbsp;km/h par rapport au pick-up.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Quelle est la vitesse horizontale du ballon dans le référentiel terrestre, juste après le tir&nbsp;? Quelle est alors sa trajectoire dans le référentiel terrestre&nbsp;? Et dans le référentiel du pick-up&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Un ballon qui tombe tout droit</span></summary>
<div class="nt-d-body">
<p>Par rapport au sol, le ballon avance à 50&nbsp;km/h avec le pick-up, mais il est tiré vers l’arrière à 50&nbsp;km/h par rapport au pick-up&nbsp;: les deux se compensent. Dans le référentiel terrestre, le ballon sort du canon <b>sans vitesse horizontale</b>&nbsp;: il tombe <b>verticalement</b>, exactement comme si on le lâchait d’un pont, pendant que le pick-up s’éloigne.</p>
<p>Dans le référentiel du pick-up, en revanche, le ballon part vers l’arrière à 50&nbsp;km/h en tombant&nbsp;: sa trajectoire est une courbe (une parabole) qui s’éloigne du véhicule.</p>
</div>
</details>

<div class="nt-lab" id="lab-pickup">
<p class="nt-tag"><i class="fa-solid fa-truck-pickup"></i>Animation</p>
<p class="nt-lab-title">Le ballon tiré vers l’arrière</p>
<div class="nt-btns"><span class="nt-note">Observer depuis&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="pk-ref" value="sol" checked><span>le sol</span></label><label><input type="radio" name="pk-ref" value="pickup"><span>le pick-up</span></label></div></div>
<canvas role="img" aria-label="Un pick-up roule vers la droite et tire un ballon vers l’arrière ; trajectoire du ballon dans le référentiel choisi."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Lancer la scène</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La <span class="imp nt-hole">trajectoire</span> et le <span class="imp nt-hole">vecteur vitesse</span> d'un système dépendent du <span class="imp nt-hole">référentiel</span> choisi pour l'observer.</p>
</div>

## Testez-vous {.nt-h2}

<p class="nt-lead">Pour finir, un quiz qui balaie tout le chapitre&nbsp;: les questions sont mélangées à chaque essai, et chaque réponse est expliquée.</p>

<div class="nt-lab nt-quizlab" id="quiz-final">
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


  /* =================== outils de dessin du chapitre =================== */
  var VERT = '#00AB8E', ORANGE = '#FEAE00', VERT_T = '#00806A', ORANGE_T = '#A16207', ROUGE = '#E11D48', TRAJ = '#3B82F6';
  function vec(ctx, x1, y1, x2, y2, col, w, L) {   /* flèche de vecteur, tête pleine */
    var dx = x2 - x1, dy = y2 - y1, d = Math.hypot(dx, dy); if (d < 0.5) { return; }
    L = Math.min(L || 11, d * 0.6); var ux = dx / d, uy = dy / d, W2 = L * 0.45;
    ctx.save(); ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = w || 2.2; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2 - ux * L * 0.8, y2 - uy * L * 0.8); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(x2, y2); ctx.lineTo(x2 - ux * L - uy * W2, y2 - uy * L + ux * W2); ctx.lineTo(x2 - ux * L + uy * W2, y2 - uy * L - ux * W2); ctx.closePath(); ctx.fill(); ctx.restore();
  }
  function nomVec(ctx, s, x, y, col, size, ita, fond) {   /* nom de vecteur surmonté d'une petite flèche */
    size = size || 15; ctx.save(); ctx.font = (ita ? 'italic ' : '') + size + 'px Georgia, "Times New Roman", serif';
    var w = ctx.measureText(s).width, h = size;
    if (fond) { ctx.fillStyle = 'rgba(255,255,255,0.88)'; rr(ctx, x - w / 2 - 5, y - h * 1.35, w + 10, h * 1.75, 6); ctx.fill(); }
    ctx.fillStyle = col; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic'; ctx.fillText(s, x, y);
    ctx.restore(); vec(ctx, x - w / 2 - 1, y - h * 0.95, x + w / 2 + 3, y - h * 0.95, col, 1.1, 5);
  }
  function croix(ctx, x, y, col, s) { s = s || 4.5; ctx.save(); ctx.strokeStyle = col || ROUGE; ctx.lineWidth = 1.6; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(x - s, y - s); ctx.lineTo(x + s, y + s); ctx.moveTo(x + s, y - s); ctx.lineTo(x - s, y + s); ctx.stroke(); ctx.restore(); }
  function papier(ctx, x0, y0, W, H, u) {   /* papier quadrillé */
    ctx.fillStyle = '#FFFFFF'; ctx.fillRect(x0, y0, W, H); ctx.strokeStyle = '#E3EAF3'; ctx.lineWidth = 1;
    for (var x = x0; x <= x0 + W + 0.5; x += u) { ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x, y0 + H); ctx.stroke(); }
    for (var y = y0; y <= y0 + H + 0.5; y += u) { ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x0 + W, y); ctx.stroke(); }
  }
  function balle(ctx, x, y, r, alpha) {
    ctx.save(); ctx.globalAlpha = alpha === undefined ? 1 : alpha; var g = ctx.createRadialGradient(x - r * 0.35, y - r * 0.35, r * 0.1, x, y, r);
    g.addColorStop(0, '#BFDBFE'); g.addColorStop(1, '#2563EB'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.fill(); ctx.restore();
  }
  function indice(i) { return String(i).split('').map(function (c) { return String.fromCharCode(8320 + +c); }).join(''); }
  function vitTxt(v) { return fmt(Math.abs(v), Math.abs(v) < 10 && Math.abs(v) % 1 ? 1 : 0) + '\u00A0m/s'; }
  (function () {   /* roulement de tambour */
    var b = $(document, '.nt-drum'); if (!b) { return; }
    var son = null; b.addEventListener('click', function () { try { if (!son) { son = new Audio('https://presentationssite.github.io/audio/drumroll.mp3'); } son.currentTime = 0; var p = son.play(); if (p && p.catch) { p.catch(function () {}); } } catch (e) {} });
  })();

  /* =================== 1. Assis dans le train : qui bouge ? =================== */
  (function () {
    var root = document.getElementById('lab-trains'); if (!root) { return; }
    var cvF = $(root, '.nt-fen'), msg = $(root, '.nt-msg'), zone = $(root, '.nt-sits'), bGo = $(root, '[data-act="go"]'), bV = $(root, '[data-act="verif"]');
    var TF = 12, DT = 0.01, NS = Math.round(TF / DT) + 1, LW = 20, LT = 3 * LW, t = 0, run = false, vu = false, cF, cards = [], phaseMsg = -1;
    function s2(x) { return x * x; }
    function w(t) {   /* vitesse de l'autre train par rapport au vôtre (m/s ; > 0 vers la droite) : départs et arrêts en douceur */
      if (t < 1) { return 0; } if (t < 5) { return -6 * s2(Math.sin(Math.PI * (t - 1) / 4)); }
      if (t < 6.5) { return 0; } if (t < 8.5) { return 4 * s2(Math.sin(Math.PI * (t - 6.5) / 4)); } return 4;
    }
    function integre(f) { var x = [0], v0 = f(0); for (var i = 1; i < NS; i++) { var v1 = f(i * DT); x.push(x[i - 1] + (v0 + v1) / 2 * DT); v0 = v1; } return x; }
    var R = integre(w), VO = integre(function (t) { return t < 1 ? 0 : (t < 3 ? w(t) : -6); }), VM = integre(function (t) { return t < 1 ? 0 : (t < 3 ? -w(t) : 6); });
    var SIT = [   /* abscisses (m) de l'arrière gauche de chaque train dans le référentiel terrestre : [autre train, votre train] */
      { ok: true, txt: 'Le train rouge démarre vers la gauche. Votre train (le bleu) démarre à son tour dans le même sens, le rattrape, puis le double.', pos: function (i) { return [VO[i], VO[i] - R[i]]; },
        exp: 'Tant que votre train roule moins vite que le rouge, celui-ci s\u2019éloigne vers la gauche&nbsp;; à vitesses égales, il paraît arrêté&nbsp;; quand vous allez plus vite, il paraît reculer vers la droite.' },
      { ok: true, txt: 'Le train rouge reste à quai. Votre train (le bleu) avance vers la droite, s\u2019arrête, puis repart vers la gauche.', pos: function (i) { return [0, -R[i]]; },
        exp: 'Quand votre train avance vers la droite, vous voyez le train rouge glisser vers la gauche&nbsp;; quand il repart vers la gauche, le rouge paraît glisser vers la droite.' },
      { ok: true, txt: 'Votre train (le bleu) démarre vers la droite. Le train rouge démarre à son tour vers la droite, rattrape le bleu, puis le double.', pos: function (i) { return [VM[i] + R[i], VM[i]]; },
        exp: 'Tant que le rouge roule moins vite que vous, il paraît glisser vers la gauche&nbsp;; à vitesses égales, il paraît arrêté&nbsp;; quand il va plus vite que vous, il glisse vers la droite.' },
      { ok: false, txt: 'Votre train (le bleu) reste à quai. Le train rouge avance vers la gauche, puis s\u2019arrête définitivement.', pos: function (i) { return [R[Math.min(i, Math.round(5 / DT))], 0]; },
        exp: 'Après son arrêt, le train rouge ne bougerait plus&nbsp;: vous ne le verriez pas repartir vers la droite.' },
      { ok: false, txt: 'Le train rouge reste à quai. Votre train (le bleu) avance vers la gauche, s\u2019arrête, puis repart vers la droite.', pos: function (i) { return [0, R[i]]; },
        exp: 'Si votre train avançait d\u2019abord vers la gauche, vous verriez le train rouge glisser d\u2019abord vers la droite&nbsp;: l\u2019ordre serait inversé.' },
      { ok: false, txt: 'Les deux trains démarrent en même temps vers la gauche et roulent côte à côte, toujours à la même vitesse.', pos: function (i) { return [VO[i], VO[i]]; },
        exp: 'Les deux trains garderaient la même position l\u2019un par rapport à l\u2019autre&nbsp;: par la fenêtre, le train rouge paraîtrait immobile du début à la fin.' }
    ];
    var MIN = 1e9, MAX = -1e9;   /* même échelle pour toutes les vues de dessus */
    SIT.forEach(function (s) { var a = 1e9, b = -1e9; for (var i = 0; i < NS; i += 5) { var p = s.pos(i); a = Math.min(a, p[0], p[1]); b = Math.max(b, p[0], p[1]); } s.a = a; s.b = b + LT; MAX = Math.max(MAX, s.b - s.a); });
    var SPAN = MAX + 24;
    function idx() { return Math.max(0, Math.min(NS - 1, Math.round(t / DT))); }
    var LIV = { autre: { band: '#E11D48', porte: '#BE123C' }, moi: { band: '#2563EB', porte: '#1D4ED8' } };
    function autreTrain(ctx, wx, wy, ww, wh, r) {   /* l'autre train, 3 voitures de 20 m : on voit la portion qui fait face à votre place */
      var k = ww / 8, cx = wx + ww / 2;
      for (var c = 0; c < 3; c++) {
        var X = cx + (r + c * LW - LT / 2) * k, top = wy - 10, bas = wy + wh + 10;
        var gb = ctx.createLinearGradient(0, top, 0, bas); gb.addColorStop(0, '#FFFFFF'); gb.addColorStop(1, '#E2E8F0'); ctx.fillStyle = gb; ctx.fillRect(X, top, LW * k, bas - top);
        ctx.fillStyle = LIV.autre.band; ctx.fillRect(X, wy + wh * 0.68, LW * k, wh * 0.09); ctx.fillStyle = '#FDA4AF'; ctx.fillRect(X, wy + wh * 0.8, LW * k, wh * 0.022);
        [1.0, 17.6].forEach(function (d) { ctx.fillStyle = LIV.autre.porte; rr(ctx, X + d * k, wy + wh * 0.03, 1.4 * k, wh * 1.2, 6); ctx.fill(); ctx.fillStyle = '#334155'; rr(ctx, X + (d + 0.3) * k, wy + wh * 0.1, 0.8 * k, wh * 0.38, 5); ctx.fill(); ctx.fillStyle = 'rgba(255,255,255,0.35)'; ctx.fillRect(X + (d + 0.68) * k, wy + wh * 0.55, 0.04 * k, wh * 0.4); });
        for (var f = 0; f < 4; f++) { var fx = X + (3.4 + f * 3.55) * k, gw = ctx.createLinearGradient(0, wy + wh * 0.1, 0, wy + wh * 0.56); gw.addColorStop(0, '#475569'); gw.addColorStop(1, '#1E293B'); ctx.fillStyle = gw; rr(ctx, fx, wy + wh * 0.1, 2.6 * k, wh * 0.46, 10); ctx.fill(); ctx.fillStyle = 'rgba(255,255,255,0.12)'; ctx.fillRect(fx + 0.3 * k, wy + wh * 0.13, 0.25 * k, wh * 0.38); }
        ctx.fillStyle = '#94A3B8'; ctx.font = (0.45 * k) + 'px ' + FONT; ctx.textAlign = 'center'; ctx.fillText('voiture ' + (c + 1), X + 10 * k, wy + wh * 0.94);
        ctx.fillStyle = '#1E293B'; ctx.fillRect(X + LW * k - 0.35 * k, top, 0.35 * k, bas - top);   /* soufflet entre deux voitures : il masque tout l'arrière-plan */
        for (var b = 0; b < 6; b++) { ctx.fillStyle = b % 2 ? '#334155' : '#0F172A'; ctx.fillRect(X + LW * k - 0.35 * k + b * 0.06 * k, top, 0.03 * k, bas - top); }
      }
    }
    function siege(ctx, x0, sol, u, d) {   /* siège de train vu de profil (u : hauteur du siège) ; d = 1 : dossier à gauche, tourné vers la droite */
      ctx.save(); ctx.translate(x0, sol); ctx.scale(d, 1); ctx.lineJoin = 'round';
      ctx.fillStyle = 'rgba(15,23,42,0.2)'; ctx.beginPath(); ctx.ellipse(0.22 * u, 0, 0.3 * u, 0.018 * u, 0, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = '#1F2937'; ctx.beginPath(); ctx.moveTo(0.1 * u, -0.31 * u); ctx.lineTo(0.38 * u, -0.31 * u); ctx.lineTo(0.42 * u, 0); ctx.lineTo(0.06 * u, 0); ctx.closePath(); ctx.fill();   /* pied */
      ctx.fillStyle = '#E2E8F0'; rr(ctx, 0.16 * u, -0.22 * u, 0.15 * u, 0.12 * u, 0.02 * u); ctx.fill();   /* ajour du pied */
      var gs = ctx.createLinearGradient(-0.06 * u, 0, 0.2 * u, 0); gs.addColorStop(0, '#111827'); gs.addColorStop(1, '#1E293B'); ctx.fillStyle = gs;   /* coque */
      ctx.beginPath(); ctx.moveTo(0.46 * u, -0.3 * u); ctx.lineTo(0.12 * u, -0.29 * u); ctx.quadraticCurveTo(-0.01 * u, -0.3 * u, -0.02 * u, -0.45 * u); ctx.lineTo(-0.08 * u, -0.93 * u); ctx.quadraticCurveTo(-0.07 * u, -0.99 * u, -0.02 * u, -0.99 * u); ctx.lineTo(0.03 * u, -0.95 * u); ctx.lineTo(0.12 * u, -0.38 * u); ctx.lineTo(0.47 * u, -0.37 * u); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(0.44 * u, -0.296 * u); ctx.lineTo(0.12 * u, -0.287 * u); ctx.quadraticCurveTo(0.0, -0.29 * u, -0.01 * u, -0.45 * u); ctx.lineTo(-0.065 * u, -0.92 * u); ctx.stroke();   /* liseré clair de la coque */
      ctx.save(); ctx.beginPath();   /* garniture rembourrée du dossier, galbée, en deux tons comme sur la photo */
      ctx.moveTo(0.12 * u, -0.38 * u); ctx.lineTo(0.03 * u, -0.95 * u); ctx.quadraticCurveTo(0.09 * u, -0.93 * u, 0.1 * u, -0.8 * u); ctx.quadraticCurveTo(0.1 * u, -0.62 * u, 0.15 * u, -0.5 * u); ctx.quadraticCurveTo(0.17 * u, -0.42 * u, 0.12 * u, -0.38 * u); ctx.closePath(); ctx.clip();
      var gn = ctx.createLinearGradient(0, 0, 0.16 * u, 0); gn.addColorStop(0, '#22325A'); gn.addColorStop(1, '#34477A'); ctx.fillStyle = gn; ctx.fillRect(-0.1 * u, -u, 0.4 * u, 0.7 * u);
      var gg = ctx.createLinearGradient(0, 0, 0.12 * u, 0); gg.addColorStop(0, '#8E99AB'); gg.addColorStop(1, '#B4BDCB'); ctx.fillStyle = gg;
      ctx.beginPath(); ctx.moveTo(-0.1 * u, -u); ctx.lineTo(0.2 * u, -u); ctx.lineTo(0.2 * u, -0.69 * u); ctx.quadraticCurveTo(0.11 * u, -0.66 * u, 0.07 * u, -0.72 * u); ctx.quadraticCurveTo(0.04 * u, -0.77 * u, -0.1 * u, -0.73 * u); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,0.15)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(0.07 * u, -0.86 * u); ctx.quadraticCurveTo(0.075 * u, -0.6 * u, 0.12 * u, -0.45 * u); ctx.stroke();
      ctx.restore();
      var gh = ctx.createLinearGradient(0, -1.04 * u, 0, -0.82 * u); gh.addColorStop(0, '#C7CDD6'); gh.addColorStop(1, '#9CA3AF'); ctx.fillStyle = gh;   /* appui-tête rembourré */
      ctx.beginPath(); ctx.moveTo(-0.03 * u, -1.02 * u); ctx.quadraticCurveTo(0.1 * u, -1.06 * u, 0.13 * u, -0.95 * u); ctx.quadraticCurveTo(0.14 * u, -0.85 * u, 0.06 * u, -0.82 * u); ctx.lineTo(-0.01 * u, -0.83 * u); ctx.closePath(); ctx.fill();
      var gc = ctx.createLinearGradient(0, -0.45 * u, 0, -0.33 * u); gc.addColorStop(0, '#34477A'); gc.addColorStop(1, '#22325A'); ctx.fillStyle = gc;   /* assise courte et épaisse */
      ctx.beginPath(); ctx.moveTo(0.09 * u, -0.37 * u); ctx.lineTo(0.1 * u, -0.43 * u); ctx.quadraticCurveTo(0.11 * u, -0.455 * u, 0.15 * u, -0.455 * u); ctx.lineTo(0.43 * u, -0.45 * u); ctx.quadraticCurveTo(0.5 * u, -0.445 * u, 0.5 * u, -0.4 * u); ctx.quadraticCurveTo(0.5 * u, -0.355 * u, 0.44 * u, -0.35 * u); ctx.lineTo(0.12 * u, -0.35 * u); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,0.18)'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(0.16 * u, -0.44 * u); ctx.lineTo(0.43 * u, -0.437 * u); ctx.stroke();
      ctx.fillStyle = '#1E2A4A'; rr(ctx, 0.05 * u, -0.6 * u, 0.3 * u, 0.04 * u, 0.02 * u); ctx.fill();   /* accoudoir */
      ctx.fillStyle = '#334155'; ctx.beginPath(); ctx.arc(0.33 * u, -0.58 * u, 0.022 * u, 0, 2 * Math.PI); ctx.fill();
      ctx.restore();
    }
    function drawF(o) {   /* vue depuis votre place, au milieu de votre train : seul l'autre train est visible */
      var ctx = o.ctx, W = o.W, H = o.H, i = idx(), r = R[i], sol = H * 0.94;
      ctx.clearRect(0, 0, W, H);
      var g = ctx.createLinearGradient(0, 0, 0, sol); g.addColorStop(0, '#F8FAFC'); g.addColorStop(1, '#E2E8F0'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, sol);   /* paroi */
      ctx.strokeStyle = 'rgba(148,163,184,0.25)'; ctx.lineWidth = 1; for (var p = W * 0.1; p < W; p += W * 0.2) { ctx.beginPath(); ctx.moveTo(p, H * 0.12); ctx.lineTo(p, sol); ctx.stroke(); }   /* joints des panneaux */
      var gp = ctx.createLinearGradient(0, 0, 0, H * 0.06); gp.addColorStop(0, '#CBD5E1'); gp.addColorStop(1, '#E2E8F0'); ctx.fillStyle = gp; ctx.fillRect(0, 0, W, H * 0.06);   /* plafond et éclairage */
      ctx.fillStyle = '#FFFBEB'; rr(ctx, W * 0.08, H * 0.018, W * 0.84, H * 0.022, 4); ctx.fill(); ctx.fillStyle = 'rgba(253,230,138,0.25)'; ctx.fillRect(W * 0.06, H * 0.04, W * 0.88, H * 0.05);
      ctx.fillStyle = 'rgba(15,23,42,0.08)'; ctx.fillRect(0, H * 0.105, W, H * 0.035); ctx.fillStyle = '#94A3B8'; rr(ctx, 0, H * 0.095, W, H * 0.014, 3); ctx.fill(); ctx.fillStyle = '#CBD5E1'; rr(ctx, 0, H * 0.09, W, H * 0.008, 2); ctx.fill();   /* porte-bagages */
      var wx = W * 0.22, wy = H * 0.19, ww = W * 0.56, wh = H * 0.46;
      ctx.save(); ctx.shadowColor = 'rgba(15,23,42,0.22)'; ctx.shadowBlur = 16; ctx.shadowOffsetY = 5; ctx.fillStyle = '#E5E7EB'; rr(ctx, wx - 14, wy - 14, ww + 28, wh + 28, 30); ctx.fill(); ctx.restore();   /* encadrement */
      var gf = ctx.createLinearGradient(0, wy - 14, 0, wy + wh + 14); gf.addColorStop(0, '#F1F5F9'); gf.addColorStop(1, '#CBD5E1'); ctx.fillStyle = gf; rr(ctx, wx - 8, wy - 8, ww + 16, wh + 16, 25); ctx.fill();
      ctx.save(); rr(ctx, wx, wy, ww, wh, 20); ctx.clip();
      autreTrain(ctx, wx, wy, ww, wh, r);
      var ref = ctx.createLinearGradient(wx, wy, wx + ww, wy + wh); ref.addColorStop(0, 'rgba(255,255,255,0.3)'); ref.addColorStop(0.3, 'rgba(255,255,255,0)'); ref.addColorStop(0.75, 'rgba(255,255,255,0)'); ref.addColorStop(1, 'rgba(255,255,255,0.14)'); ctx.fillStyle = ref; ctx.fillRect(wx, wy, ww, wh);
      var store = ctx.createLinearGradient(0, wy, 0, wy + wh * 0.09); store.addColorStop(0, '#E7DCC6'); store.addColorStop(1, '#D6C6A5'); ctx.fillStyle = store; ctx.fillRect(wx, wy, ww, wh * 0.08);   /* store enroulé */
      ctx.fillStyle = '#B8A27A'; ctx.fillRect(wx, wy + wh * 0.08, ww, 2); ctx.fillStyle = '#94A3B8'; rr(ctx, wx + ww / 2 - 14, wy + wh * 0.08, 28, 6, 3); ctx.fill();
      ctx.restore(); ctx.strokeStyle = 'rgba(100,116,139,0.6)'; ctx.lineWidth = 1.5; rr(ctx, wx, wy, ww, wh, 20); ctx.stroke();
      ctx.fillStyle = '#CBD5E1'; ctx.fillRect(0, H * 0.73, W, 2);   /* lisse sous la fenêtre */
      var gfl = ctx.createLinearGradient(0, sol, 0, H); gfl.addColorStop(0, '#475569'); gfl.addColorStop(1, '#1E293B'); ctx.fillStyle = gfl; ctx.fillRect(0, sol, W, H - sol);   /* sol de la voiture */
      var u = Math.min(sol - H * 0.22, W * 0.42), yt = sol - 0.62 * u;   /* table à pied central, entre les deux sièges */
      ctx.fillStyle = 'rgba(15,23,42,0.15)'; ctx.beginPath(); ctx.ellipse(W / 2, sol, W * 0.05, 0.015 * u, 0, 0, 2 * Math.PI); ctx.fill();
      var gpi = ctx.createLinearGradient(W / 2 - 0.03 * u, 0, W / 2 + 0.03 * u, 0); gpi.addColorStop(0, '#374151'); gpi.addColorStop(0.5, '#6B7280'); gpi.addColorStop(1, '#374151'); ctx.fillStyle = gpi; ctx.fillRect(W / 2 - 0.028 * u, yt, 0.056 * u, sol - yt);
      ctx.fillStyle = '#4B5563'; rr(ctx, W / 2 - 0.07 * u, sol - 0.012 * u, 0.14 * u, 0.012 * u, 2); ctx.fill();
      var gt = ctx.createLinearGradient(0, yt - 0.03 * u, 0, yt); gt.addColorStop(0, '#E9D8B8'); gt.addColorStop(1, '#C8AC84'); ctx.fillStyle = gt; rr(ctx, W / 2 - 0.26 * u, yt - 0.03 * u, 0.52 * u, 0.03 * u, 0.012 * u); ctx.fill();
      ctx.fillStyle = '#374151'; ctx.fillRect(W / 2 - 0.25 * u, yt, 0.5 * u, 0.008 * u);
      var lx = W / 2 + 0.1 * u, ly = yt - 0.03 * u;   /* petite lampe, comme sur la photo */
      ctx.fillStyle = '#F59E0B'; ctx.beginPath(); ctx.moveTo(lx - 0.012 * u, ly); ctx.lineTo(lx - 0.008 * u, ly - 0.07 * u); ctx.lineTo(lx + 0.008 * u, ly - 0.07 * u); ctx.lineTo(lx + 0.012 * u, ly); ctx.closePath(); ctx.fill();
      var gl = ctx.createRadialGradient(lx, ly - 0.085 * u, 1, lx, ly - 0.085 * u, 0.09 * u); gl.addColorStop(0, 'rgba(254,243,199,0.9)'); gl.addColorStop(1, 'rgba(254,243,199,0)'); ctx.fillStyle = gl; ctx.beginPath(); ctx.arc(lx, ly - 0.085 * u, 0.09 * u, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = '#FBBF24'; ctx.beginPath(); ctx.ellipse(lx, ly - 0.09 * u, 0.04 * u, 0.025 * u, 0, Math.PI, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#FEF3C7'; ctx.beginPath(); ctx.ellipse(lx, ly - 0.09 * u, 0.04 * u, 0.018 * u, 0, 0, Math.PI); ctx.fill();
      siege(ctx, W / 2 - 0.84 * u, sol, u, 1); siege(ctx, W / 2 + 0.84 * u, sol, u, -1);
      var vg = ctx.createRadialGradient(W / 2, H * 0.45, Math.min(W, H) * 0.35, W / 2, H * 0.45, Math.max(W, H) * 0.75); vg.addColorStop(0, 'rgba(15,23,42,0)'); vg.addColorStop(1, 'rgba(15,23,42,0.18)'); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);   /* vignettage léger */
      pill(ctx, W < 520 ? 'votre fenêtre' : 'votre fenêtre, au milieu de votre train', W < 520 ? 8 : W / 2, H * 0.155, { size: W < 520 ? 10 : 11, col: NAVY, stroke: GRID2, align: W < 520 ? 'left' : 'center' });
      if (run || t > 0) { pill(ctx, 't = ' + fmt(t, 1) + ' s', W - 8, H * 0.155, { size: W < 520 ? 10 : 11, col: SLATE, align: 'right', stroke: GRID2 }); }
    }
    function drawC(card) {   /* une situation vue de dessus, dans le référentiel terrestre ; même échelle pour toutes */
      var o = card.c, ctx = o.ctx, W = o.W, H = o.H, s = card.s, i = idx(), p = s.pos(i), y1 = H * 0.36, y2 = H * 0.68, k = (W - 16) / SPAN, x0 = (s.a + s.b) / 2 - SPAN / 2, X = function (x) { return 8 + (x - x0) * k; };
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#F0FDF4'; ctx.fillRect(0, 0, W, H);
      for (var a = Math.floor(x0 / 12) * 12; a < x0 + SPAN + 12; a += 12) { ctx.fillStyle = '#4ADE80'; ctx.beginPath(); ctx.arc(X(a), H * 0.1, 4, 0, 2 * Math.PI); ctx.fill(); ctx.beginPath(); ctx.arc(X(a + 6), H * 0.93, 4, 0, 2 * Math.PI); ctx.fill(); }
      [y1, y2].forEach(function (y) { ctx.fillStyle = '#E7E5E4'; ctx.fillRect(0, y - 9, W, 18); ctx.strokeStyle = '#A8A29E'; ctx.lineWidth = 0.8; [-5, 5].forEach(function (d) { ctx.beginPath(); ctx.moveTo(0, y + d); ctx.lineTo(W, y + d); ctx.stroke(); }); });
      function tr(x, y, liv, moi) {
        for (var c = 0; c < 3; c++) { var xx = X(x + c * LW); ctx.fillStyle = '#F8FAFC'; ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 0.8; rr(ctx, xx + 0.5, y - 6, LW * k - 1, 12, 3); ctx.fill(); ctx.stroke(); ctx.fillStyle = liv.band; ctx.fillRect(xx + 1.5, y + 2.5, LW * k - 3, 2.2); ctx.fillStyle = liv.porte; ctx.fillRect(xx + 1 * k, y - 6, Math.max(1.5, 1.4 * k), 12); ctx.fillRect(xx + 17.6 * k, y - 6, Math.max(1.5, 1.4 * k), 12); }
        if (moi) { var xm = X(x + LT / 2); ctx.fillStyle = '#1D4ED8'; ctx.beginPath(); ctx.arc(xm, y - 1, 3.2, 0, 2 * Math.PI); ctx.fill(); pill(ctx, 'vous', xm, y + 17, { size: 10, col: '#1D4ED8' }); }
      }
      tr(p[0], y1, LIV.autre, false); tr(p[1], y2, LIV.moi, true);
      var q = s.pos(Math.min(NS - 1, i + 10)), v = [(q[0] - p[0]) / 0.1, (q[1] - p[1]) / 0.1];
      [[v[0], y1 - 16, p[0]], [v[1], y2 - 16, p[1]]].forEach(function (z) { if (Math.abs(z[0]) > 0.3) { var xc = X(z[2] + LT / 2); vec(ctx, xc - z[0] * 1.6, z[1], xc + z[0] * 1.6, z[1], '#475569', 1.8, 7); } });
    }
    function drawAll() { drawF(cF); cards.forEach(drawC); }
    function suivi() {   /* commentaire pendant l'observation */
      var ph = t < 1 ? 0 : (t < 5 ? 1 : (t < 6.5 ? 2 : 3)); if (ph === phaseMsg) { return; } phaseMsg = ph;
      msg.textContent = ['L\u2019autre train est immobile…', 'Il glisse vers la gauche…', '… il s\u2019arrête…', '… et repart vers la droite.'][ph];
    }
    SIT = shuffle(SIT);
    SIT.forEach(function (s) {
      var d = document.createElement('div'); d.className = 'nt-sit';
      d.innerHTML = '<canvas role="img" aria-label="Les deux trains vus de dessus dans le référentiel terrestre"></canvas><p>' + s.txt + '</p><button type="button" class="nt-btn" aria-pressed="false"><i class="fa-regular fa-square"></i>&nbsp; compatible</button><p class="nt-sit-exp" hidden></p>';
      zone.appendChild(d);
      var card = { s: s, d: d }; card.c = Canvas($(d, 'canvas'), function () { return 96; }, function () { if (card.c) { drawC(card); } }); drawC(card);
      var b = $(d, 'button'); b.addEventListener('click', function () { var on = b.getAttribute('aria-pressed') !== 'true'; b.setAttribute('aria-pressed', String(on)); b.innerHTML = '<i class="fa-regular fa-' + (on ? 'square-check' : 'square') + '"></i>&nbsp; compatible'; d.classList.remove('ok', 'ko'); $(d, '.nt-sit-exp').hidden = true; });
      cards.push(card);
    });
    var loop = Loop(root, function (dt) { if (!run) { return false; } t = Math.min(TF, t + dt); if (!vu) { suivi(); } if (t >= TF) { run = false; bGo.disabled = false; fin(); } drawAll(); return run; });
    function fin() {
      if (!vu) { vu = true; zone.hidden = false; bV.hidden = false; cards.forEach(function (c) { c.c.size(); }); }
      msg.innerHTML = 'Vous avez vu l\u2019autre train glisser vers la gauche, s\u2019arrêter, puis glisser vers la droite. Mais que s\u2019est-il passé <b>par rapport au sol</b>&nbsp;? Voici six situations vues de dessus, dans le référentiel terrestre (les points verts sont des arbres, votre train est celui du bas). Cochez celles qui sont compatibles avec votre observation, puis vérifiez. «&nbsp;Rejouer&nbsp;» anime la fenêtre et les situations ensemble.';
    }
    cF = Canvas(cvF, function (W) { return Math.round(Math.min(380, W * (W < 520 ? 0.78 : 0.6))); }, drawF);
    bGo.addEventListener('click', function () { t = 0; phaseMsg = -1; if (RM) { t = TF; fin(); drawAll(); return; } run = true; bGo.disabled = true; bGo.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Rejouer'; loop.kick(); });
    bV.addEventListener('click', function () {
      var bons = 0; cards.forEach(function (c) { var on = $(c.d, 'button').getAttribute('aria-pressed') === 'true', ok = on === c.s.ok; if (ok) { bons++; } c.d.classList.toggle('ok', ok); c.d.classList.toggle('ko', !ok); var e = $(c.d, '.nt-sit-exp'); e.hidden = false; e.innerHTML = (c.s.ok ? '<b>Compatible.</b> ' : '<b>Pas compatible.</b> ') + c.s.exp; });
      msg.innerHTML = (bons === cards.length ? '<b>Parfait&nbsp;!</b> ' : bons + '&nbsp;réponse' + (bons > 1 ? 's' : '') + ' juste' + (bons > 1 ? 's' : '') + ' sur ' + cards.length + '. ') + 'Les trois situations compatibles, très différentes vues du sol, donnent <b>exactement la même image</b> par la fenêtre&nbsp;: depuis votre place, on observe seulement le mouvement de l\u2019autre train <b>par rapport au vôtre</b>. Sans voir le sol, impossible de savoir qui bouge vraiment.';
    });
    drawAll();
  })();

  /* =================== 2. Le parachutiste =================== */
  (function () {
    var root = document.getElementById('lab-parach'); if (!root) { return; }
    var bS = $(root, '[data-act="saut"]'), bO = $(root, '[data-act="ouvre"]'), msg = $(root, '.nt-msg');
    var VC = 55, t = 0, run = false, ouvert = -1, zp = 3000, zc = 3000, vp = VC, cnv;
    var NUAGES = [[0.2, 2850], [0.75, 2700], [0.35, 2520], [0.8, 2350], [0.15, 2180], [0.6, 2000], [0.3, 1820], [0.7, 1650]];
    function perso(ctx, x, y, col, para) {   /* sauteur : position de chute libre, ou suspendu sous sa voile */
      ctx.save(); ctx.lineCap = 'round'; ctx.lineJoin = 'round';
      if (para) {
        ctx.strokeStyle = 'rgba(71,85,105,0.7)'; ctx.lineWidth = 0.7; [-15, -6, 6, 15].forEach(function (d) { ctx.beginPath(); ctx.moveTo(x + d, y - 27); ctx.lineTo(x + (d < 0 ? -2 : 2), y - 9); ctx.stroke(); });
        var gv = ctx.createLinearGradient(x - 18, 0, x + 18, 0); gv.addColorStop(0, '#F97316'); gv.addColorStop(0.5, '#FDBA74'); gv.addColorStop(1, '#F97316');
        ctx.fillStyle = gv; ctx.beginPath(); ctx.moveTo(x - 19, y - 26); ctx.quadraticCurveTo(x, y - 40, x + 19, y - 26); ctx.lineTo(x + 18, y - 23); ctx.quadraticCurveTo(x, y - 33, x - 18, y - 23); ctx.closePath(); ctx.fill();
        ctx.strokeStyle = 'rgba(255,255,255,0.8)'; ctx.lineWidth = 0.8; [-10, 0, 10].forEach(function (d) { ctx.beginPath(); ctx.moveTo(x + d, y - 33 + Math.abs(d) * 0.3); ctx.lineTo(x + d, y - 27 + Math.abs(d) * 0.25); ctx.stroke(); });
        ctx.strokeStyle = col; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(x, y - 6); ctx.lineTo(x, y + 2); ctx.moveTo(x, y + 2); ctx.lineTo(x - 2.5, y + 9); ctx.moveTo(x, y + 2); ctx.lineTo(x + 2.5, y + 9); ctx.moveTo(x, y - 4); ctx.lineTo(x - 3, y - 9); ctx.moveTo(x, y - 4); ctx.lineTo(x + 3, y - 9); ctx.stroke();
        ctx.fillStyle = '#1E293B'; ctx.beginPath(); ctx.arc(x, y - 9, 2.8, 0, 2 * Math.PI); ctx.fill();
      } else {
        ctx.strokeStyle = col; ctx.lineWidth = 3.2; ctx.beginPath(); ctx.moveTo(x - 7, y); ctx.lineTo(x + 6, y); ctx.moveTo(x - 3, y); ctx.lineTo(x - 8, y - 6); ctx.moveTo(x + 2, y); ctx.lineTo(x + 7, y - 6); ctx.moveTo(x - 7, y); ctx.lineTo(x - 12, y - 4); ctx.moveTo(x + 6, y); ctx.lineTo(x + 11, y - 5); ctx.stroke();
        ctx.fillStyle = '#1E293B'; ctx.beginPath(); ctx.arc(x + 9, y - 1, 2.8, 0, 2 * Math.PI); ctx.fill();
      }
      ctx.restore();
    }
    function nuage(ctx, x, y) {
      var g = ctx.createLinearGradient(0, y - 14, 0, y + 9); g.addColorStop(0, 'rgba(255,255,255,0.98)'); g.addColorStop(1, 'rgba(226,232,240,0.9)'); ctx.fillStyle = g;
      ctx.beginPath(); ctx.ellipse(x, y, 30, 9, 0, 0, 2 * Math.PI); ctx.ellipse(x - 10, y - 5, 14, 9, 0, 0, 2 * Math.PI); ctx.ellipse(x + 10, y - 7, 16, 11, 0, 0, 2 * Math.PI); ctx.fill();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, gap = 12, pw = (W - gap) / 2; ctx.clearRect(0, 0, W, H);
      [0, 1].forEach(function (k) {
        var x0 = k * (pw + gap); ctx.save(); rr(ctx, x0, 0, pw, H, 10); ctx.clip();
        var g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#38BDF8'); g.addColorStop(0.55, '#7DD3FC'); g.addColorStop(1, '#E0F2FE'); ctx.fillStyle = g; ctx.fillRect(x0, 0, pw, H);
        var cxp = x0 + pw * 0.4, cxc = x0 + pw * 0.62;
        if (k === 0) {   /* référentiel terrestre : fenêtre fixe de 3050 m à 2300 m */
          var Y = function (z) { return 30 + (3050 - z) / 750 * (H - 60); };
          NUAGES.forEach(function (n) { nuage(ctx, x0 + n[0] * pw, Y(n[1])); });
          ctx.fillStyle = 'rgba(255,255,255,0.85)'; ctx.fillRect(x0 + pw - 4, 0, 1.5, H); for (var z = 3000; z >= 2300; z -= 250) { var yy = Y(z); ctx.fillRect(x0 + pw - 10, yy, 8, 1.5); pill(ctx, z + ' m', x0 + pw - 13, yy, { size: 10, col: '#0C4A6E', align: 'right', bg: 'rgba(255,255,255,0.75)' }); }
          perso(ctx, cxp, Y(zp), '#EA580C', ouvert >= 0); perso(ctx, cxc, Y(zc), '#7C3AED', false);
          if (t > 0) { vec(ctx, cxp - 20, Y(zp) - 4, cxp - 20, Y(zp) - 4 + vp * 1.1, ORANGE, 2.2, 9); vec(ctx, cxc + 20, Y(zc) - 4, cxc + 20, Y(zc) - 4 + VC * 1.1, ORANGE, 2.2, 9); }
          pill(ctx, W < 520 ? 'sol' : 'référentiel terrestre', x0 + 6, 14, { size: W < 520 ? 10.5 : 11.5, col: NAVY, align: 'left', stroke: GRID2 });
        } else {   /* référentiel du caméraman : l'image qu'il filme ; on ne le voit pas, et le parachutiste, tout proche, paraît grand */
          var Yc = function (z) { return H * 0.6 + (zc - z) * 1.3; }, gx = x0 + pw * 0.5;
          NUAGES.forEach(function (n) { var y = H * 0.55 + (zc - n[1]) * 0.9; if (y > -20 && y < H + 20) { nuage(ctx, x0 + n[0] * pw, y); } });
          var yp = Yc(zp);
          ctx.save(); ctx.translate(gx, yp); ctx.scale(2.2, 2.2); perso(ctx, 0, 0, '#EA580C', ouvert >= 0); ctx.restore();
          var vr = VC - vp; if (vr > 0.5) { vec(ctx, gx - 42, yp - 10, gx - 42, yp - 10 - vr * 1.6, ORANGE, 2.6, 11); }
          else if (t > 0) { pill(ctx, 'immobile sur l\u2019image', gx, yp + 30, { size: 10.5, col: '#EA580C' }); }
          ctx.strokeStyle = 'rgba(255,255,255,0.9)'; ctx.lineWidth = 2.5; var m = 12, l = 18;   /* coins du viseur */
          [[x0 + m, m + 22, 1, 1], [x0 + pw - m, m + 22, -1, 1], [x0 + m, H - m, 1, -1], [x0 + pw - m, H - m, -1, -1]].forEach(function (c) { ctx.beginPath(); ctx.moveTo(c[0], c[1] + c[3] * l); ctx.lineTo(c[0], c[1]); ctx.lineTo(c[0] + c[2] * l, c[1]); ctx.stroke(); });
          if (run) { pill(ctx, '\u25CF REC', x0 + pw - 14, 44, { size: 10.5, col: '#DC2626', align: 'right', bg: 'rgba(15,23,42,0.65)' }); }
          pill(ctx, W < 520 ? 'caméraman' : 'référentiel du caméraman', x0 + 6, 14, { size: W < 520 ? 10.5 : 11.5, col: NAVY, align: 'left', stroke: GRID2 });
        }
        ctx.restore();
      });
    }
    function step(dt) {
      if (!run) { return false; } t += dt;
      if (ouvert >= 0) { vp = 6 + (VC - 6) * Math.exp(-(t - ouvert) / 0.9); }
      zp -= vp * dt; zc -= VC * dt;
      if (t > 13) { run = false; bS.disabled = false; }
      if (ouvert >= 0 && t - ouvert > 2.5 && msg.getAttribute('data-f') !== '1') { msg.setAttribute('data-f', '1'); msg.innerHTML = 'Dans le référentiel terrestre (à gauche), le parachutiste <b>descend toujours</b>, mais beaucoup moins vite&nbsp;: ' + vitTxt(vp) + '. Dans le référentiel du caméraman (à droite), il <b>remonte</b>&nbsp;!'; }
      draw(cnv); return run;
    }
    var loop = Loop(root, step);
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 300 : 340; }, draw);
    function reset() { t = 0; run = false; ouvert = -1; zp = zc = 3000; vp = VC; bS.disabled = false; bO.disabled = true; msg.removeAttribute('data-f'); msg.textContent = 'Les deux sauteurs tombent ensemble. Ouvrez le parachute quand vous voulez.'; draw(cnv); }
    bS.addEventListener('click', function () { reset(); run = true; bS.disabled = true; bO.disabled = false; msg.textContent = 'Chute libre&nbsp;: les deux sauteurs tombent côte à côte, à environ 200\u00A0km/h.'.replace('&nbsp;', '\u00A0'); loop.kick(); });
    bO.addEventListener('click', function () { if (!run || ouvert >= 0) { return; } ouvert = t; bO.disabled = true; msg.textContent = 'Le parachute s\u2019ouvre…'; });
    $(root, '[data-act="reset"]').addEventListener('click', reset);
    reset();
  })();

  /* =================== 3. Le bateau et le radeau =================== */
  (function () {
    var root = document.getElementById('lab-radeau'); if (!root) { return; }
    var bP = $(root, '[data-act="play"]'), msg = $(root, '.nt-msg');
    var U = 3, WB = 12, t = 0, run = false, ref = 'terre', cnv, DT = 0.05;
    function xb(t) { return t <= 0.5 ? -(WB - U) * t : -(WB - U) * 0.5 + (WB + U) * (t - 0.5); }
    function hm(t) { var m = Math.round(t * 60); return Math.floor(m / 60) + '\u00A0h\u00A0' + String(m % 60).padStart(2, '0'); }
    function bateau(t, o, X, ym, lane) {   /* position à l'écran du bateau, avec un demi-tour en arc de cercle */
      var x = X(xb(t) - (ref === 'eau' ? U * t : 0)), y = ym - lane;
      if (t > 0.5 - DT && t < 0.5 + DT) { var f = Math.PI * (t - 0.5 + DT) / (2 * DT); y = ym - lane * Math.cos(f); x -= lane * 1.1 * Math.sin(f); }
      else if (t >= 0.5 + DT) { y = ym + lane; }
      return [x, y];
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, off = ref === 'eau' ? U * t : 0, kx = (W - 40) / 11.5, X = function (x) { return 20 + (x - off + 7) * kx; };
      var y0 = H * 0.24, y1 = H * 0.8, ym = (y0 + y1) / 2 - 4, lane = (y1 - y0) * 0.16;
      ctx.clearRect(0, 0, W, H);
      var gr = ctx.createLinearGradient(0, 0, 0, H); gr.addColorStop(0, '#BBF7D0'); gr.addColorStop(1, '#86EFAC'); ctx.fillStyle = gr; ctx.fillRect(0, 0, W, H);
      var eau = ctx.createLinearGradient(0, y0, 0, y1); eau.addColorStop(0, '#7DD3FC'); eau.addColorStop(0.5, '#38BDF8'); eau.addColorStop(1, '#7DD3FC'); ctx.fillStyle = eau;
      ctx.beginPath(); ctx.moveTo(0, y0); for (var xx = 0; xx <= W; xx += 10) { ctx.lineTo(xx, y0 + 2.5 * Math.sin((xx + off * kx) / 23)); } for (xx = W; xx >= 0; xx -= 10) { ctx.lineTo(xx, y1 + 2.5 * Math.sin((xx + off * kx) / 19 + 1)); } ctx.closePath(); ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,0.55)'; ctx.lineWidth = 1.3;
      for (var k = -20; k < 30; k++) { var xw = X(k * 0.55 + U * t * 1.0), yy = y0 + 14 + ((k * 7) % 6 + 6) % 6 * (y1 - y0 - 28) / 5; if (xw > -20 && xw < W + 20) { ctx.beginPath(); ctx.moveTo(xw, yy); ctx.quadraticCurveTo(xw + 7, yy - 3, xw + 14, yy); ctx.stroke(); } }
      for (var a = -10; a <= 10; a += 0.8) {   /* arbres et roseaux sur les berges */
        var xa = X(a); if (xa < -20 || xa > W + 20) { continue; }
        var top = y0 - 16 - ((a * 10) % 3 + 3) % 3 * 3; ctx.fillStyle = '#16A34A'; ctx.beginPath(); ctx.arc(xa, top, 9, 0, 2 * Math.PI); ctx.arc(xa + 7, top + 4, 7, 0, 2 * Math.PI); ctx.fill();
        ctx.fillStyle = '#15803D'; ctx.beginPath(); ctx.arc(xa + 0.4 * kx, y1 + 13, 6, 0, 2 * Math.PI); ctx.fill();
      }
      for (var km = -7; km <= 7; km++) { var xk = X(km); if (xk < -10 || xk > W + 10) { continue; } ctx.fillStyle = '#FFFFFF'; rr(ctx, xk - 15, y1 + 25, 30, 15, 4); ctx.fill(); txt(ctx, km + '\u00A0km', xk, y1 + 32.5, { size: 10, col: SLATE }); }
      [[0, '1er croisement'], [3, '2e croisement']].forEach(function (m) { var xm = X(m[0]); ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = 'rgba(30,41,59,0.45)'; ctx.beginPath(); ctx.moveTo(xm, y0 + 4); ctx.lineTo(xm, y1 - 4); ctx.stroke(); ctx.restore(); pill(ctx, m[1], xm, y0 + 12, { size: 10, col: SLATE, bg: 'rgba(255,255,255,0.8)' }); });
      if (t > 0) {   /* trajectoire du bateau dans le référentiel choisi */
        ctx.save(); ctx.strokeStyle = 'rgba(255,255,255,0.95)'; ctx.lineWidth = 2.2; ctx.setLineDash([7, 5]); ctx.beginPath();
        for (var i = 0; i <= 200; i++) { var ti = t * i / 200, p = bateau(ti, o, function (x) { return 20 + (x + 7) * kx; }, ym, lane); if (i) { ctx.lineTo(p[0], p[1]); } else { ctx.moveTo(p[0], p[1]); } }
        ctx.stroke(); ctx.restore();
      }
      var xR = X(U * t), yR = ym + lane * 0.1;   /* radeau */
      ctx.fillStyle = '#A16207'; rr(ctx, xR - 13, yR - 9, 26, 18, 3); ctx.fill(); ctx.strokeStyle = '#713F12'; ctx.lineWidth = 1; for (var pl = -9; pl <= 9; pl += 4.5) { ctx.beginPath(); ctx.moveTo(xR + pl, yR - 9); ctx.lineTo(xR + pl, yR + 9); ctx.stroke(); }
      ctx.strokeStyle = '#1E293B'; ctx.beginPath(); ctx.moveTo(xR, yR); ctx.lineTo(xR, yR - 20); ctx.stroke(); ctx.fillStyle = '#E11D48'; ctx.beginPath(); ctx.moveTo(xR, yR - 20); ctx.lineTo(xR + 10, yR - 16); ctx.lineTo(xR, yR - 12); ctx.fill();
      var pb = bateau(t, o, function (x) { return 20 + (x + 7) * kx; }, ym, lane), pb2 = bateau(Math.min(1, t + 0.004), o, function (x) { return 20 + (x + 7) * kx; }, ym, lane), pb0 = bateau(Math.max(0, t - 0.004), o, function (x) { return 20 + (x + 7) * kx; }, ym, lane);
      var ang = Math.atan2(pb2[1] - pb0[1], pb2[0] - pb0[0]); if (t === 0) { ang = Math.PI; }
      ctx.save(); ctx.translate(pb[0], pb[1]); ctx.rotate(ang);
      if (run) { ctx.strokeStyle = 'rgba(255,255,255,0.8)'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(-12, 0); ctx.lineTo(-34, -9); ctx.moveTo(-12, 0); ctx.lineTo(-34, 9); ctx.stroke(); }
      ctx.fillStyle = '#FFFFFF'; ctx.strokeStyle = '#1E3A8A'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(17, 0); ctx.quadraticCurveTo(8, -8, -12, -7); ctx.lineTo(-12, 7); ctx.quadraticCurveTo(8, 8, 17, 0); ctx.closePath(); ctx.fill(); ctx.stroke();
      ctx.fillStyle = '#1D4ED8'; rr(ctx, -6, -4, 9, 8, 2); ctx.fill(); ctx.restore();
      vec(ctx, W - 92, y1 - 12, W - 30, y1 - 12, '#1E3A8A', 1.6, 8); txt(ctx, 'courant', W - 61, y1 - 22, { size: 10.5, col: '#1E3A8A' });
      pill(ctx, 't = ' + hm(t), 10, 14, { size: 12, col: NAVY, align: 'left', stroke: GRID2 });
      pill(ctx, ref === 'eau' ? 'référentiel de l\u2019eau (radeau immobile)' : 'référentiel terrestre (berges immobiles)', W - 10, 14, { size: W < 520 ? 10 : 11.5, col: NAVY, align: 'right', stroke: GRID2 });
    }
    function step(dt) {
      if (!run) { return false; } var t0 = t; t = Math.min(1, t + dt / 8);
      if (t0 < 0.5 && t >= 0.5) { msg.textContent = 'Demi-tour, une demi-heure après le premier croisement.'; }
      if (t >= 1) { run = false; bP.disabled = false; msg.innerHTML = ref === 'eau' ? 'Dans le référentiel de l\u2019eau, le radeau ne bouge pas&nbsp;: le bateau s\u2019est éloigné pendant 30&nbsp;min, puis est revenu à la même vitesse en 30&nbsp;min. Le deuxième croisement a lieu <b>1&nbsp;heure</b> après le premier.' : 'Deuxième croisement, 1&nbsp;heure après le premier, 3&nbsp;km plus loin&nbsp;: le radeau, porté par le courant, a parcouru 3&nbsp;km en 1&nbsp;h. Pour le comprendre facilement, regardez la scène depuis le radeau.'; }
      draw(cnv); return run;
    }
    var loop = Loop(root, step);
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 220 : 250; }, draw);
    function reset() { t = 0; run = false; bP.disabled = false; draw(cnv); }
    bP.addEventListener('click', function () { if (t >= 1) { reset(); } run = true; bP.disabled = true; msg.textContent = 'Le bateau remonte le courant…'; loop.kick(); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { reset(); msg.textContent = 'Essayez d\u2019abord de résoudre l\u2019énigme… puis observez la scène depuis le radeau.'; });
    $$(root, 'input[name="rd-ref"]').forEach(function (r) { r.addEventListener('change', function () { ref = r.value; draw(cnv); }); });
    reset();
  })();

  /* =================== 4. Translation, rotation, marteau lancé =================== */
  (function () {
    var root = document.getElementById('lab-types'); if (!root) { return; }
    var chkC = $(root, '[data-in="chrono"]'), chkT = $(root, '[data-in="traces"]'), msg = $(root, '.nt-msg');
    var mode = 'trans', t = 0, TT = 4, run = false, cnv;
    var PTS = [[-0.42, 0, '#2563EB'], [0.3, 0, ROUGE], [0.62, -0.17, VERT]];   /* bout du manche, centre de masse G, bout de la tête (repère du marteau, G n'est pas au milieu) */
    var MSG = {
      trans: 'Translation rectiligne&nbsp;: le marteau garde toujours la même orientation. Les trois points décrivent des segments de droite <b>identiques</b>, simplement décalés.',
      circ: 'Translation circulaire&nbsp;: le marteau reste toujours horizontal, comme la nacelle d\u2019une grande roue. Les trois points décrivent des cercles <b>identiques</b>, décalés les uns des autres&nbsp;: c\u2019est bien une translation.',
      rot: 'Rotation autour du bout du manche, qui reste fixe&nbsp;: les autres points décrivent des cercles <b>de rayons différents</b>, tous centrés sur l\u2019axe de rotation.',
      lancer: 'Marteau lancé&nbsp;: le centre de masse G (en rouge) décrit une simple courbe en cloche, tandis que les autres points tournent autour de lui et décrivent des trajectoires compliquées.'
    };
    var FIT = {};
    function cadre(o) {   /* mise à l'échelle pour que tout le mouvement (marteau compris) tienne dans le cadre */
      var key = mode + o.W + 'x' + o.H; if (FIT.key === key) { return FIT; }
      var mnx = 1e9, mny = 1e9, mxx = -1e9, mxy = -1e9, l = L0(o);
      for (var i = 0; i <= 160; i++) { var st = etat0(TT * i / 160, o), c = Math.cos(st[2]), s = Math.sin(st[2]);
        [[-0.45, 0], [0.64, -0.2], [0.64, 0.2], [0.5, -0.2], [0.5, 0.2]].forEach(function (p) { var x = st[0] + (p[0] - 0.3) * l * c - p[1] * l * s, y = st[1] + (p[0] - 0.3) * l * s + p[1] * l * c; mnx = Math.min(mnx, x); mxx = Math.max(mxx, x); mny = Math.min(mny, y); mxy = Math.max(mxy, y); }); }
      var f = Math.min(1, (o.W - 30) / (mxx - mnx), (o.H - 30) / (mxy - mny));
      FIT = { key: key, f: f, bx: (mnx + mxx) / 2, by: (mny + mxy) / 2 }; return FIT;
    }
    function etat(t, o) { var st = etat0(t, o), F = cadre(o); return [o.W / 2 + (st[0] - F.bx) * F.f, o.H / 2 + (st[1] - F.by) * F.f, st[2]]; }
    function etat0(t, o) {   /* position du centre de masse et angle du marteau à l'instant t (avant mise à l'échelle) */
      var W = o.W, H = o.H, u = t / TT;
      if (mode === 'trans') { return [W * 0.22 + u * W * 0.5, H * 0.68 - u * H * 0.32, -0.35]; }
      if (mode === 'circ') { var a = Math.PI / 2 - 2 * Math.PI * u; return [W / 2 + H * 0.3 * Math.cos(a), H * 0.5 + H * 0.3 * Math.sin(a), 0]; }
      if (mode === 'rot') { var th = -2 * Math.PI * u * 0.92, d = 0.72 * L0(o); return [W / 2 + d * Math.cos(th), H * 0.5 + d * Math.sin(th), th]; }
      var x = W * 0.14 + u * W * 0.72, y = H * 0.78 - H * 0.5 * 4 * u * (1 - u); return [x, y, -0.3 - 2 * Math.PI * 1.6 * u];
    }
    function L0(o) { return Math.min(o.W, o.H) * 0.42; }
    function L(o) { return L0(o) * cadre(o).f; }
    function pt(st, p, o) { var c = Math.cos(st[2]), s = Math.sin(st[2]), l = L(o); return [st[0] + (p[0] - 0.3) * l * c - p[1] * l * s, st[1] + (p[0] - 0.3) * l * s + p[1] * l * c]; }
    function marteau(ctx, st, o, alpha) {
      var l = L(o), c = Math.cos(st[2]), s = Math.sin(st[2]);
      ctx.save(); ctx.globalAlpha = alpha; ctx.translate(st[0], st[1]); ctx.rotate(st[2]); ctx.translate(-0.3 * l, 0);
      ctx.fillStyle = '#D6B38A'; ctx.strokeStyle = '#92673A'; ctx.lineWidth = 1; rr(ctx, -0.45 * l, -0.035 * l, 1.03 * l, 0.07 * l, 0.03 * l); ctx.fill(); ctx.stroke();
      var g = ctx.createLinearGradient(0, -0.2 * l, 0, 0.2 * l); g.addColorStop(0, '#CBD5E1'); g.addColorStop(1, '#64748B'); ctx.fillStyle = g; ctx.strokeStyle = '#475569';
      rr(ctx, 0.5 * l, -0.19 * l, 0.14 * l, 0.38 * l, 0.03 * l); ctx.fill(); ctx.stroke(); ctx.restore();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k, N = 9; ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#F8FAFC'; ctx.fillRect(0, 0, W, H);
      if (mode === 'rot') { var piv = pt(etat(0, o), PTS[0], o); ctx.fillStyle = '#334155'; ctx.beginPath(); ctx.arc(piv[0], piv[1], 4, 0, 2 * Math.PI); ctx.fill(); pill(ctx, 'axe de rotation', piv[0] + 8, piv[1] + 16, { size: 10.5, col: SLATE, align: 'left' }); }
      if (chkC.checked) { for (k = 0; k <= N; k++) { var tk = TT * k / N; if (tk <= t + 1e-6) { marteau(ctx, etat(tk, o), o, 0.22); } } }
      if (chkT.checked) {
        PTS.forEach(function (p) {
          ctx.save(); ctx.strokeStyle = p[2]; ctx.lineWidth = 1.6; ctx.setLineDash([5, 4]); ctx.beginPath();
          for (var i = 0; i <= 200; i++) { var ti = Math.min(t, TT * i / 200), q = pt(etat(ti, o), p, o); if (i) { ctx.lineTo(q[0], q[1]); } else { ctx.moveTo(q[0], q[1]); } if (ti >= t) { break; } }
          ctx.stroke(); ctx.restore();
        });
      }
      var st = etat(t, o); marteau(ctx, st, o, 1);
      [['bout du manche', '#2563EB'], ['centre de masse G', ROUGE], ['bout de la tête', VERT]].forEach(function (l, i) { pill(ctx, '\u25CF ' + l[0], 10, 16 + i * 22, { size: 11, col: l[1], align: 'left', stroke: GRID2 }); });
      PTS.forEach(function (p, i) { var q = pt(st, p, o); ctx.fillStyle = '#FFFFFF'; ctx.beginPath(); ctx.arc(q[0], q[1], 4.6, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = p[2]; ctx.beginPath(); ctx.arc(q[0], q[1], 3.4, 0, 2 * Math.PI); ctx.fill(); if (i === 1) { txt(ctx, 'G', q[0] + 9, q[1] - 9, { size: 13, serif: true, col: ROUGE }); } });
    }
    var loop = Loop(root, function (dt) { if (!run) { return false; } t = Math.min(TT, t + dt); if (t >= TT) { run = false; } draw(cnv); return run; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 260 : 300; }, draw);
    function lance() { msg.innerHTML = MSG[mode]; if (RM) { t = TT; draw(cnv); return; } t = 0; run = true; loop.kick(); }
    $$(root, 'input[name="ty-m"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; lance(); }); });
    [chkC, chkT].forEach(function (c) { c.addEventListener('change', function () { draw(cnv); }); });
    $(root, '[data-act="replay"]').addEventListener('click', lance);
    msg.innerHTML = MSG[mode]; t = TT; draw(cnv);
    if ('IntersectionObserver' in window) { var vu = false; new IntersectionObserver(function (es) { if (es[0].isIntersecting && !vu) { vu = true; lance(); } }).observe(root); }
  })();

  /* =================== 5. Direction, sens, norme =================== */
  (function () {
    var root = document.getElementById('lab-vecteur'); if (!root) { return; }
    var cmp = $(root, '.nt-cmp'), chkD = $(root, '[data-in="dir"]'), chkN = $(root, '[data-in="norme"]'), cv = $(root, 'canvas');
    var V = [{ a: [2, 6], b: [6, 3], col: '#2563EB', nom: 'AB', n: ['A', 'B'] }, { a: [9, 8], b: [14, 5], col: '#DB2777', nom: 'CD', n: ['C', 'D'] }], u = 30, cnv, drag = null;
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; u = W < 520 ? 22 : 30; ctx.clearRect(0, 0, W, H); papier(ctx, 0, 0, W, H, u);
      V.forEach(function (v) {
        var ax = v.a[0] * u, ay = v.a[1] * u, bx = v.b[0] * u, by = v.b[1] * u, dx = bx - ax, dy = by - ay, d = Math.hypot(dx, dy) || 1;
        if (chkD.checked) { ctx.save(); ctx.strokeStyle = v.col; ctx.globalAlpha = 0.35; ctx.setLineDash([6, 5]); ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(ax - dx / d * 2000, ay - dy / d * 2000); ctx.lineTo(ax + dx / d * 2000, ay + dy / d * 2000); ctx.stroke(); ctx.restore(); }
        vec(ctx, ax, ay, bx, by, v.col, 2.6, 13);
        [[ax, ay], [bx, by]].forEach(function (p, i) { ctx.fillStyle = '#FFFFFF'; ctx.strokeStyle = v.col; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(p[0], p[1], 6, 0, 2 * Math.PI); ctx.fill(); ctx.stroke(); txt(ctx, v.n[i], p[0] + (i ? 10 : -10) * (dx >= 0 ? 1 : -1), p[1] + (i ? -10 : 12), { size: 14, serif: true, col: v.col }); });
        var nx = -dy / d, ny = dx / d, mx = (ax + bx) / 2 + nx * 18, my = (ay + by) / 2 + ny * 18;
        nomVec(ctx, v.nom, mx, my + 5, v.col, 15, false, true);
        if (chkN.checked) { pill(ctx, 'norme\u00A0: ' + fmt(Math.hypot(v.b[0] - v.a[0], v.b[1] - v.a[1]), 1) + ' carreaux', (ax + bx) / 2 - nx * 20, (ay + by) / 2 - ny * 20, { size: 11, col: v.col, stroke: GRID2 }); }
      });
    }
    function compare() {
      var a = [V[0].b[0] - V[0].a[0], V[0].b[1] - V[0].a[1]], b = [V[1].b[0] - V[1].a[0], V[1].b[1] - V[1].a[1]], cr = a[0] * b[1] - a[1] * b[0], sc = a[0] * b[0] + a[1] * b[1];
      var na = Math.hypot(a[0], a[1]), nb = Math.hypot(b[0], b[1]), dir = Math.abs(cr) < 1e-9, sens = dir && sc > 0, norme = Math.abs(na - nb) < 1e-9;
      function c(x) { return x ? '<span class="oui">oui</span>' : '<span class="non">non</span>'; }
      var concl = dir && sens && norme ? '<b>Les deux vecteurs sont égaux&nbsp;!</b>' : (dir && !sens && norme ? '<b>Vecteurs opposés</b>&nbsp;: même direction, même norme, mais sens contraires.' : 'Les deux vecteurs ne sont pas égaux.');
      cmp.innerHTML = '<span>Même direction&nbsp;?</span>' + c(dir) + '<span>Même sens&nbsp;?</span>' + (dir ? c(sens) : '<span>sans objet (directions différentes)</span>') + '<span>Même norme&nbsp;?</span>' + c(norme) + '<span style="grid-column: 1 / -1; text-align:center; margin-top:0.3em;">' + concl + '</span>';
    }
    cnv = Canvas(cv, function (W) { var uu = W < 520 ? 22 : 30; return 10 * uu; }, draw);
    function pos(e) { var r = cv.getBoundingClientRect(); return [(e.clientX - r.left) / u, (e.clientY - r.top) / u]; }
    cv.addEventListener('pointerdown', function (e) {
      var p = pos(e), best = null, bd = 0.9;
      V.forEach(function (v) { ['a', 'b'].forEach(function (k) { var d = Math.hypot(v[k][0] - p[0], v[k][1] - p[1]); if (d < bd) { bd = d; best = [v, k]; } }); });
      if (best) { drag = best; cv.setPointerCapture(e.pointerId); }
    });
    cv.addEventListener('pointermove', function (e) {
      if (!drag) { return; } var p = pos(e), mx = Math.floor(cnv.W / u), my = Math.floor(cnv.H / u);
      var q = [Math.max(1, Math.min(mx - 1, Math.round(p[0]))), Math.max(1, Math.min(my - 1, Math.round(p[1])))], v = drag[0], o = drag[1] === 'a' ? 'b' : 'a';
      if (q[0] === v[o][0] && q[1] === v[o][1]) { return; }
      v[drag[1]] = q; draw(cnv); compare();
    });
    cv.addEventListener('pointerup', function () { drag = null; });
    $(root, '[data-act="egaux"]').addEventListener('click', function () { V[0].a = [2, 6]; V[0].b = [6, 3]; V[1].a = [9, 8]; V[1].b = [13, 5]; draw(cnv); compare(); });
    $(root, '[data-act="opp"]').addEventListener('click', function () { V[0].a = [2, 6]; V[0].b = [6, 3]; V[1].a = [14, 4]; V[1].b = [10, 7]; draw(cnv); compare(); });
    [chkD, chkN].forEach(function (c) { c.addEventListener('change', function () { draw(cnv); }); });
    compare();
  })();

  /* =================== 6. Construction pas à pas =================== */
  (function () {
    var root = document.getElementById('lab-constr'); if (!root) { return; }
    var et = $(root, '.nt-etape'), pts = $(root, '.nt-pts'), bP = $(root, '[data-act="prec"]'), bS = $(root, '[data-act="suiv"]');
    var k = 0, a = 1, cnv, IM = 3;   /* M = position n° 3, M' = position n° 4 */
    var P = []; (function () {   /* positions en cm sur le document, MM' = 4,0 cm exactement */
      for (var i = 0; i < 7; i++) { var s = i / 6; P.push([1.4 + 22.5 * s, 7.6 - 5.6 * Math.sin(Math.PI * (0.12 + 0.86 * s)) - 0.4 * s]); }
      var d = Math.hypot(P[IM + 1][0] - P[IM][0], P[IM + 1][1] - P[IM][1]), f = 4.0 / d, c = P[IM];
      P = P.map(function (p) { return [c[0] + (p[0] - c[0]) * f, c[1] + (p[1] - c[1]) * f]; });
      var mx = Math.min.apply(null, P.map(function (p) { return p[0]; })); P = P.map(function (p) { return [p[0] - mx + 1.2, p[1]]; });
    })();
    var M = P[IM], Mp = P[IM + 1], ang = Math.atan2(Mp[1] - M[1], Mp[0] - M[0]), LV = 32 / 6;
    var E = [
      ['La chronophotographie', 'Une balle est photographiée toutes les <b>$\\Delta t$ = 0,50&nbsp;s</b>. Sur le document, <b>1&nbsp;cm représente 4&nbsp;m</b> dans la réalité&nbsp;: c\u2019est l\u2019échelle des distances.'],
      ['On choisit le point M et le suivant M\u2032', 'On veut le vecteur vitesse au point M. On repère la position suivante, M\u2032, photographiée $\\Delta t$ = 0,50&nbsp;s plus tard.'],
      ['On trace le vecteur déplacement', 'On trace la flèche <span class="nt-dep">$\\overrightarrow{\\mathrm{MM\'}}$</span>, qui part de M et pointe vers M\u2032.'],
      ['On mesure MM\u2032 sur le document', 'On place le zéro de la règle sur M et on lit la longueur de la flèche&nbsp;: <b>MM\u2032 = 4,0&nbsp;cm</b> sur le document.'],
      ['On convertit avec l\u2019échelle des distances', 'Puisque 1&nbsp;cm représente 4&nbsp;m&nbsp;: <span class="nt-calc-l">MM\u2032 = 4,0 × 4 = <b>16&nbsp;m</b></span> dans la réalité.'],
      ['On calcule la vitesse', '<span class="nt-calc-l">$v = \\dfrac{\\mathrm{MM\'}}{\\Delta t} = \\dfrac{\\pu{16 m}}{\\pu{0,50 s}} = \\pu{32 m*s-1}$</span>'],
      ['On choisit une échelle pour les vitesses', 'Pour dessiner une vitesse, il faut une seconde échelle&nbsp;: <b>1&nbsp;cm pour 6&nbsp;m·s⁻¹</b>. La flèche mesurera donc <span class="nt-calc-l">32&nbsp;/&nbsp;6 ≈ <b>5,3&nbsp;cm</b></span>'],
      ['On trace le vecteur vitesse à partir de M', 'On aligne la règle sur la direction de <span class="nt-dep">$\\overrightarrow{\\mathrm{MM\'}}$</span>, zéro sur M, et on trace une flèche de 5,3&nbsp;cm dans le même sens&nbsp;: c\u2019est <span class="nt-vit">$\\vec{v}_{\\mathrm{M}}$</span>.'],
      ['Bilan', '<span class="nt-vit">$\\vec{v}_{\\mathrm{M}}$</span> a la même direction et le même sens que <span class="nt-dep">$\\overrightarrow{\\mathrm{MM\'}}$</span>, mais une longueur fixée par l\u2019échelle des vitesses. Ici, elle dépasse M\u2032&nbsp;: c\u2019est normal, les deux flèches ne représentent pas la même grandeur.']
    ];
    function cadre(W) {   /* zone du document affichée : tout, ou seulement autour de M sur les petits écrans */
      var vis = W < 560 ? P.slice(IM - 1, IM + 3) : P, end = [M[0] + Math.cos(ang) * LV, M[1] + Math.sin(ang) * LV];
      var xs = vis.map(function (p) { return p[0]; }).concat([end[0]]), ys = vis.map(function (p) { return p[1]; }).concat([end[1]]);
      var ox = Math.min.apply(null, xs) - 1.1, oy = Math.min(Math.min.apply(null, ys) - (W < 560 ? 2.2 : 1.6), 0), wx = Math.max.apply(null, xs) - ox + 1.1, hy = Math.max.apply(null, ys) - oy + 1.6;
      if (W >= 560) { oy = 0; hy = 9.4; }
      var u = Math.min(44, (W - 16) / wx); return { ox: ox, oy: oy, u: u, h: hy * u + 16 };
    }
    function U(o) { return cadre(o.W).u; }
    function regle(ctx, x, y, th, lcm, u, al) {   /* règle graduée, zéro en (x, y), le long de l'angle th */
      ctx.save(); ctx.globalAlpha = al; ctx.translate(x, y); ctx.rotate(th);
      ctx.fillStyle = 'rgba(224,242,254,0.88)'; ctx.strokeStyle = '#7DD3FC'; ctx.lineWidth = 1; rr(ctx, -0.5 * u, 0, (lcm + 1) * u, 1.25 * u, 4); ctx.fill(); ctx.stroke();
      ctx.strokeStyle = '#0C4A6E'; ctx.fillStyle = '#0C4A6E';
      for (var mm = 0; mm <= lcm * 10; mm++) { var xx = mm / 10 * u, h = mm % 10 === 0 ? 0.42 * u : (mm % 5 === 0 ? 0.28 * u : 0.17 * u); ctx.lineWidth = mm % 10 ? 0.6 : 1; ctx.beginPath(); ctx.moveTo(xx, 0); ctx.lineTo(xx, h); ctx.stroke(); if (mm % 10 === 0) { ctx.font = Math.max(8, u * 0.32) + 'px ' + FONT; ctx.textAlign = 'center'; ctx.fillText(String(mm / 10), xx, 0.78 * u); } }
      ctx.restore();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, cd = cadre(W), u = cd.u, X = function (p) { return 8 + (p[0] - cd.ox) * u; }, Y = function (p) { return 8 + (p[1] - cd.oy) * u; }, e = a * a * (3 - 2 * a);
      ctx.clearRect(0, 0, W, H); papier(ctx, 0, 0, W, H, u);
      ctx.save(); ctx.strokeStyle = TRAJ; ctx.globalAlpha = 0.6; ctx.setLineDash([4, 4]); ctx.lineWidth = 1; ctx.beginPath(); P.forEach(function (p, i) { if (i) { ctx.lineTo(X(p), Y(p)); } else { ctx.moveTo(X(p), Y(p)); } }); ctx.stroke(); ctx.restore();
      P.forEach(function (p, i) { balle(ctx, X(p), Y(p), 0.42 * u, k >= 1 && i !== IM && i !== IM + 1 ? 0.35 : 0.85); croix(ctx, X(p), Y(p), ROUGE, 0.2 * u); });
      if (k >= 1) {
        [[M, 'M', -1], [Mp, 'M\u2032', 1]].forEach(function (q) { ctx.save(); ctx.strokeStyle = NAVY; ctx.lineWidth = 1.4; ctx.globalAlpha = k === 1 ? e : 1; ctx.beginPath(); ctx.arc(X(q[0]), Y(q[0]), 0.62 * u, 0, 2 * Math.PI); ctx.stroke(); ctx.restore(); txt(ctx, q[1], X(q[0]) + q[2] * 0.2 * u, Y(q[0]) - 0.95 * u, { size: Math.max(13, u * 0.55), serif: true, col: NAVY }); });
      }
      if (k >= 2) { var g = k === 2 ? e : 1; vec(ctx, X(M), Y(M), X(M) + (X(Mp) - X(M)) * g, Y(M) + (Y(Mp) - Y(M)) * g, VERT, 2.4, 12); if (g > 0.95) { var nx = -Math.sin(ang), ny = Math.cos(ang); nomVec(ctx, 'MM\u2032', (X(M) + X(Mp)) / 2 - nx * 0.75 * u, (Y(M) + Y(Mp)) / 2 - ny * 0.75 * u + 5, VERT_T, 14, false, true); } }
      if (k === 3 || k === 7) { var off = (1 - e) * 2.5 * u; regle(ctx, X(M) - Math.sin(ang) * off, Y(M) + Math.cos(ang) * off, ang, k === 3 ? 6 : 7, u, k === 3 ? Math.min(1, 0.2 + e) : Math.min(1, 0.2 + e)); }
      if (k === 3 && e > 0.95) { pill(ctx, 'MM\u2032 = 4,0 cm', X(Mp) + 0.6 * u, Y(Mp) + 1.9 * u, { size: 12, col: '#0C4A6E', align: 'left', stroke: '#7DD3FC' }); }
      if (k >= 4 && k <= 6) { pill(ctx, 'MM\u2032 = 4,0 cm \u2194 16 m', X(Mp) + 0.6 * u, Y(Mp) + 1.2 * u, { size: 12, col: VERT_T, align: 'left', stroke: '#A7F3D0' }); }
      if (k >= 5) { pill(ctx, 'v = 32 m·s⁻¹', 6, H - 12, { size: W < 520 ? 10.5 : 12.5, col: ORANGE_T, align: 'left', stroke: '#FDE68A' }); }
      if (k >= 7) { var gv = k === 7 ? Math.max(0, (e - 0.35) / 0.65) : 1, L = LV * u * gv; if (gv > 0) { vec(ctx, X(M), Y(M), X(M) + Math.cos(ang) * L, Y(M) + Math.sin(ang) * L, ORANGE, 3, 13); } if (gv > 0.95) { nomVec(ctx, 'v', X(M) + Math.cos(ang) * L * 0.55 - Math.sin(ang) * 0.85 * u, Y(M) + Math.sin(ang) * L * 0.55 + Math.cos(ang) * 0.85 * u + 8, ORANGE_T, 16, true, true); } }
      var pt = W < 520, fs = pt ? 10 : 11.5;
      pill(ctx, (pt ? 'distances' : 'échelle des distances') + '\u00A0: 1 cm \u2194 4 m', 6, 12, { size: fs, col: NAVY, align: 'left', stroke: GRID2 });
      pill(ctx, '\u0394t = 0,50 s', W - 6, 12, { size: fs, col: NAVY, align: 'right', stroke: GRID2 });
      if (k >= 6) { pill(ctx, (pt ? 'vitesses' : 'échelle des vitesses') + '\u00A0: 1 cm \u2194 6 m·s⁻¹', pt ? W - 6 : 6, pt ? H - 12 : 34, { size: fs, col: ORANGE_T, align: pt ? 'right' : 'left', stroke: '#FDE68A' }); }
    }
    var loop = Loop(root, function (dt) { a = Math.min(1, a + dt / 1.1); draw(cnv); return a < 1; });
    cnv = Canvas($(root, 'canvas'), function (W) { return Math.round(cadre(W).h); }, draw);
    function maj() {
      et.innerHTML = '<b class="t">Étape ' + (k + 1) + ' sur ' + E.length + '&nbsp;: ' + E[k][0] + '</b>' + E[k][1]; typeset(et);
      pts.innerHTML = E.map(function (_, i) { return '<i class="' + (i < k ? 'fait' : (i === k ? 'cur' : '')) + '" data-k="' + i + '"></i>'; }).join('');
      bP.disabled = k === 0; bS.disabled = k === E.length - 1;
      a = RM ? 1 : 0; if (RM) { draw(cnv); } else { loop.kick(); }
    }
    bP.addEventListener('click', function () { if (k > 0) { k--; a = 1; maj(); a = 1; draw(cnv); } });
    bS.addEventListener('click', function () { if (k < E.length - 1) { k++; maj(); } });
    pts.addEventListener('click', function (e) { var i = e.target.getAttribute('data-k'); if (i !== null) { k = +i; maj(); } });
    maj();
  })();

  /* =================== 7. Entraînement : tracer un vecteur vitesse =================== */
  (function () {
    var root = document.getElementById('tr-vecteur'); if (!root) { return; }
    var cv = $(root, 'canvas'), qEl = $(root, '.nt-tr-q'), data = $(root, '.nt-data'), z1 = $(root, '[data-etape="1"]'), z2 = $(root, '[data-etape="2"]'), inV = $(root, '#trv-v');
    var P = null, et = 1, tip = null, montre = false, okV = false, cnv, u = 30, drag = false;
    var COMBOS = [[0.04, 0.05], [0.04, 0.1], [0.1, 0.1], [0.1, 0.2], [0.2, 0.5], [0.5, 2], [0.5, 1], [0.2, 1], [1, 5]];   /* [Δt en s, échelle des distances en m/cm] */
    function gen() {
      var c = pick(COMBOS), dt = c[0], ed = c[1], type = pick(['droite', 'courbe', 'courbe', 'acc', 'ral']), n = 6, pts = [[1.5 + Math.random() * 2, 2.5 + Math.random() * 4]];
      var th = (Math.random() - 0.5) * 0.9, dth = type === 'courbe' ? (Math.random() < 0.5 ? -1 : 1) * (0.22 + Math.random() * 0.12) : 0, L0 = 2.2 + Math.random() * 0.8, Ls = [];
      for (var i = 0; i < n - 1; i++) {
        var L = type === 'acc' ? L0 * 0.7 + 0.35 * i : (type === 'ral' ? L0 * 1.15 - 0.3 * i : L0); L = Math.round(L * 10) / 10; Ls.push(L);
        var p = pts[pts.length - 1]; pts.push([p[0] + L * Math.cos(th), p[1] + L * Math.sin(th)]); th += dth;
      }
      var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; }), mx = Math.min.apply(null, xs), my = Math.min.apply(null, ys), My = Math.max.apply(null, ys);
      pts = pts.map(function (p) { return [p[0] - mx + 1.5, p[1] - my + 1.5 + Math.max(0, (7 - (My - my)) / 2)]; });
      var i0 = 1 + Math.floor(Math.random() * (n - 3)), L1 = Ls[i0], v = L1 * ed / dt;
      var ev = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20].filter(function (e) { var l = v / e; return l >= 2.2 && l <= 5.5; });
      return { pts: pts, i: i0, L: L1, dt: dt, ed: ed, v: v, ev: ev.length ? ev[0] : 1, lv: v / (ev.length ? ev[0] : 1) };
    }
    function n2(x) { return fmt(x, x < 0.1 ? 3 : (x < 1 ? 2 : (x < 10 ? 1 : 0))); }
    function nz(x) { return String(x).replace('.', ','); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; u = Math.min(32, (W - 4) / 20); ctx.clearRect(0, 0, W, H); papier(ctx, 0, 0, W, H, u); if (!P) { return; }
      var X = function (p) { return p[0] * u; }, Y = function (p) { return p[1] * u; }, M = P.pts[P.i], Mp = P.pts[P.i + 1];
      ctx.save(); ctx.strokeStyle = TRAJ; ctx.globalAlpha = 0.6; ctx.setLineDash([4, 4]); ctx.beginPath(); P.pts.forEach(function (p, i) { if (i) { ctx.lineTo(X(p), Y(p)); } else { ctx.moveTo(X(p), Y(p)); } }); ctx.stroke(); ctx.restore();
      P.pts.forEach(function (p, i) { croix(ctx, X(p), Y(p), ROUGE, 0.17 * u); txt(ctx, 'M' + String.fromCharCode(8320 + i), X(p) - 0.1 * u, Y(p) + 0.55 * u, { size: Math.max(11, u * 0.38), serif: true, col: i === P.i || i === P.i + 1 ? NAVY : '#94A3B8' }); });
      vec(ctx, X(M), Y(M), X(Mp), Y(Mp), VERT, 2, 10);
      var ang = Math.atan2(Mp[1] - M[1], Mp[0] - M[0]);
      if (montre) { ctx.save(); ctx.globalAlpha = 0.55; ctx.setLineDash([6, 4]); vec(ctx, X(M), Y(M), X(M) + Math.cos(ang) * P.lv * u, Y(M) + Math.sin(ang) * P.lv * u, '#D99A00', 2.4, 12); ctx.restore(); pill(ctx, 'attendu\u00A0: ' + fmt(P.lv, 1) + ' cm', X(M) + Math.cos(ang) * P.lv * u, Y(M) + Math.sin(ang) * P.lv * u - 0.7 * u, { size: 11, col: '#D99A00', stroke: '#FDE68A' }); }
      if (et === 2 && tip) {
        vec(ctx, X(M), Y(M), tip[0] * u, tip[1] * u, ORANGE, 2.8, 13);
        ctx.fillStyle = '#FFFFFF'; ctx.strokeStyle = ORANGE; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(tip[0] * u, tip[1] * u, 7, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
        pill(ctx, fmt(Math.hypot(tip[0] - M[0], tip[1] - M[1]), 1) + ' cm', tip[0] * u + 12, tip[1] * u - 12, { size: 11.5, col: ORANGE_T, align: 'left', stroke: '#FDE68A' });
      }
    }
    var S = Serie(root, 5, {
      show: function () {
        P = gen(); et = 1; montre = false; okV = false; tip = null; z1.hidden = false; z2.hidden = true; inV.value = ''; $(root, '[data-act="check-v"]').disabled = false; $(root, '[data-act="check-f"]').disabled = false;
        var a = 'M' + String.fromCharCode(8320 + P.i), b = 'M' + String.fromCharCode(8320 + P.i + 1);
        qEl.innerHTML = 'Tracez le vecteur vitesse au point <b>' + a + '</b>. Calculez d\u2019abord sa valeur.';
        data.innerHTML = '<span>\u0394<i>t</i> = ' + n2(P.dt) + '&nbsp;s</span><span>distances&nbsp;: 1&nbsp;cm \u2194 ' + nz(P.ed) + '&nbsp;m</span><span>' + a + b + ' = ' + fmt(P.L, 1) + '&nbsp;cm sur le document</span><span>vitesses&nbsp;: 1&nbsp;cm \u2194 ' + nz(P.ev) + '&nbsp;m/s</span><span>1 carreau = 1&nbsp;cm</span>';
        draw(cnv);
      },
      bilan: function (g, t0) { P = null; qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;5</span><br>' + t0; data.innerHTML = ''; z1.hidden = true; z2.hidden = true; draw(cnv); }
    });
    function calcul() { var a = 'M' + String.fromCharCode(8320 + P.i), b = 'M' + String.fromCharCode(8320 + P.i + 1); return a + b + ' = ' + fmt(P.L, 1) + ' × ' + nz(P.ed) + ' = ' + n2(P.L * P.ed) + '&nbsp;m, puis <i>v</i> = ' + n2(P.L * P.ed) + '&nbsp;/&nbsp;' + n2(P.dt) + ' = <b>' + n2(P.v) + '&nbsp;m/s</b>'; }
    $(root, '[data-act="check-v"]').addEventListener('click', function () {
      if (et !== 1 || S.fini) { return; } var x = num(inV.value); if (isNaN(x)) { S.say('Entrez une vitesse en m/s.'); return; }
      okV = Math.abs(x - P.v) <= 0.03 * P.v; et = 2; z1.hidden = true; z2.hidden = false;
      var M = P.pts[P.i]; tip = [M[0] + 1.2, M[1] - 1.2]; draw(cnv);
      S.say((okV ? '<b>Bonne valeur.</b> ' : '<b>Pas tout à fait&nbsp;:</b> ') + calcul() + '. Avec l\u2019échelle des vitesses, la flèche doit mesurer ' + n2(P.v) + '&nbsp;/&nbsp;' + nz(P.ev) + ' \u2248 ' + fmt(P.lv, 1) + '&nbsp;cm. Tracez-la&nbsp;!');
    });
    $(root, '[data-act="check-f"]').addEventListener('click', function () {
      if (et !== 2 || S.answered) { return; }
      var M = P.pts[P.i], Mp = P.pts[P.i + 1], a1 = Math.atan2(Mp[1] - M[1], Mp[0] - M[0]), a2 = Math.atan2(tip[1] - M[1], tip[0] - M[0]), dA = Math.abs(((a2 - a1) * 180 / Math.PI + 540) % 360 - 180), Lt = Math.hypot(tip[0] - M[0], tip[1] - M[1]);
      var okD = dA <= 7, okL = Math.abs(Lt - P.lv) <= Math.max(0.25, 0.07 * P.lv), h = [];
      if (!okD) { h.push(dA > 150 ? 'la flèche est dans le mauvais sens' : 'la direction n\u2019est pas celle du vecteur déplacement (écart de ' + Math.round(dA) + '°)'); }
      if (!okL) { h.push('la longueur est de ' + fmt(Lt, 1) + '&nbsp;cm au lieu de ' + fmt(P.lv, 1) + '&nbsp;cm'); }
      montre = true; $(root, '[data-act="check-f"]').disabled = true; draw(cnv);
      var ok = okV && okD && okL;
      S.answer(ok, (okD && okL ? 'Votre flèche a la bonne direction, le bon sens et la bonne longueur' + (okV ? '.' : ', mais la valeur de la vitesse était fausse.') : 'Attention&nbsp;: ' + h.join(' et ') + '.') + ' Le vecteur attendu est en pointillés&nbsp;: même direction et même sens que le vecteur déplacement, longueur ' + fmt(P.lv, 1) + '&nbsp;cm.', ok ? null : (okD && okL ? '<b>Tracé juste.</b> ' : null));
    });
    function pos(e) { var r = cv.getBoundingClientRect(); return [(e.clientX - r.left) / u, (e.clientY - r.top) / u]; }
    cv.addEventListener('pointerdown', function (e) { if (et !== 2 || S.answered) { return; } drag = true; tip = pos(e); cv.setPointerCapture(e.pointerId); draw(cnv); });
    cv.addEventListener('pointermove', function (e) { if (drag) { tip = pos(e); draw(cnv); } });
    cv.addEventListener('pointerup', function () { drag = false; });
    cv.setAttribute('tabindex', '0');
    cv.addEventListener('keydown', function (e) { if (et !== 2 || !tip || S.answered) { return; } var d = { ArrowLeft: [-0.1, 0], ArrowRight: [0.1, 0], ArrowUp: [0, -0.1], ArrowDown: [0, 0.1] }[e.key]; if (d) { e.preventDefault(); tip = [tip[0] + d[0], tip[1] + d[1]]; draw(cnv); } });
    cnv = Canvas(cv, function (W) { var uu = Math.min(32, (W - 4) / 20); return Math.round(uu * 10.5); }, draw);
    S.start();
  })();

  /* =================== 8. Rapprocher M' de M =================== */
  (function () {
    var root = document.getElementById('lab-inst'); if (!root) { return; }
    var inD = $(root, '[data-in="dt"]'), inT = $(root, '[data-in="tm"]'), chk = $(root, '[data-in="tan"]'), msg = $(root, '.nt-msg');
    var TM = 0.9, dt = 3.2, cnv, anim = false, sc = 1;
    function setT() { TM = 0.2 + 6 * (+inT.value) / 100; $(root, '.out-t').textContent = fmt(TM, 1) + '\u00A0s'; }
    function r(t, o) { var s = o.W / 760; return [o.W * 0.1 + s * (60 * t - 62 * Math.sin(1.2 * t)), o.H * 0.55 + s * (-62 + 62 * Math.cos(1.2 * t)) * 1.0 + s * 30 * Math.sin(0.4 * t)]; }
    function dr(t, o) { var s = o.W / 760; return [s * (60 - 74.4 * Math.cos(1.2 * t)), s * (-74.4 * Math.sin(1.2 * t) + 12 * Math.cos(0.4 * t))]; }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k = 1.0; ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      ctx.save(); ctx.strokeStyle = TRAJ; ctx.globalAlpha = 0.7; ctx.setLineDash([5, 5]); ctx.lineWidth = 1.3; ctx.beginPath();
      for (var i = 0; i <= 300; i++) { var p = r(i / 300 * 9.8, o); if (i) { ctx.lineTo(p[0], p[1]); } else { ctx.moveTo(p[0], p[1]); } } ctx.stroke(); ctx.restore();
      var M = r(TM, o), Mp = r(TM + dt, o), v = dr(TM, o), vm = [(Mp[0] - M[0]) / dt, (Mp[1] - M[1]) / dt];
      if (chk.checked) { var nv = Math.hypot(v[0], v[1]); ctx.save(); ctx.strokeStyle = '#94A3B8'; ctx.setLineDash([3, 4]); ctx.beginPath(); ctx.moveTo(M[0] - v[0] / nv * 400, M[1] - v[1] / nv * 400); ctx.lineTo(M[0] + v[0] / nv * 400, M[1] + v[1] / nv * 400); ctx.stroke(); ctx.restore(); pill(ctx, 'tangente en M', M[0] + v[0] / nv * 150 + 14, M[1] + v[1] / nv * 150, { size: 11, col: SLATE, align: 'left' }); }
      vec(ctx, M[0], M[1], Mp[0], Mp[1], VERT, 2.2, 11);
      vec(ctx, M[0], M[1], M[0] + vm[0] * k, M[1] + vm[1] * k, ORANGE, 3, 13);
      croix(ctx, M[0], M[1], NAVY, 5); croix(ctx, Mp[0], Mp[1], NAVY, 5);
      txt(ctx, 'M', M[0] - 14, M[1] + 14, { size: 16, serif: true, col: NAVY }); txt(ctx, 'M\u2032', Mp[0] + 14, Mp[1] + 12, { size: 16, serif: true, col: NAVY });
      var tvx = M[0] + vm[0] * k, tvy = M[1] + vm[1] * k, nn = Math.hypot(vm[0], vm[1]) || 1, lx = tvx + vm[0] / nn * 20, ly = tvy + vm[1] / nn * 20 + 6;   /* étiquette au-delà de la pointe : elle ne cache jamais la flèche */
      nomVec(ctx, 'v', lx - 6, ly, ORANGE_T, 15, true, true); txt(ctx, 'moy', lx + 1, ly + 3, { size: 9.5, col: ORANGE_T, align: 'left' });
      var f = 0.025 / (o.W / 760), vmn = Math.hypot(vm[0], vm[1]) * f, vn = Math.hypot(v[0], v[1]) * f;
      pill(ctx, '\u0394t = ' + fmt(dt, dt < 0.1 ? 2 : 1) + ' s\u2003\u2003v\u2098\u2092\u1d67 = ' + fmt(vmn, 2) + ' m/s', 10, 16, { size: 12, col: NAVY, align: 'left', stroke: GRID2 });
      if (dt < 0.15) { pill(ctx, 'vitesse en M\u00A0: ' + fmt(vn, 2) + ' m/s', 10, 42, { size: 12, col: ORANGE_T, align: 'left', stroke: '#FDE68A' }); }
    }
    function fromSlider() { var s = +inD.value / 100; dt = 0.02 * Math.pow(3.2 / 0.02, s); }
    function texte() {
      $(root, '.out-dt').textContent = fmt(dt, dt < 0.1 ? 2 : 1) + '\u00A0s';
      msg.innerHTML = dt > 1.5 ? 'M\u2032 est loin de M&nbsp;: le vecteur vitesse moyenne pointe vers M\u2032, dans une direction qui n\u2019a pas grand-chose à voir avec le mouvement en M.' :
        (dt > 0.15 ? 'En rapprochant M\u2032 de M, le vecteur vitesse moyenne tourne et se rapproche de la direction de la trajectoire en M.' : 'M\u2032 est tout près de M&nbsp;: le vecteur vitesse moyenne ne change presque plus. Il est <b>tangent à la trajectoire</b> en M et orienté dans le sens du mouvement&nbsp;: c\u2019est le <b>vecteur vitesse en M</b>.');
    }
    var t0 = 0, loop = Loop(root, function (d) { if (!anim) { return false; } t0 += d; var s = Math.max(0, 1 - t0 / 4); inD.value = Math.round(s * 100); fromSlider(); texte(); draw(cnv); if (s <= 0) { anim = false; } return anim; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 250 : 300; }, draw);
    inD.addEventListener('input', function () { anim = false; fromSlider(); texte(); draw(cnv); });
    inT.addEventListener('input', function () { setT(); draw(cnv); });
    chk.addEventListener('change', function () { draw(cnv); });
    $(root, '[data-act="anim"]').addEventListener('click', function () { if (RM) { inD.value = 0; fromSlider(); texte(); draw(cnv); return; } t0 = 0; anim = true; loop.kick(); });
    setT(); fromSlider(); texte(); draw(cnv);
  })();

  /* =================== 9. Lire une chronophotographie =================== */
  var NPOS = { ru: 9, ra: 9, rr: 9, cu: 12, pa: 10 };
  function posCont(mode, u, W, H) {   /* position (px) au « temps » u, compté en nombre d'intervalles \u0394t ; la balle continue après la dernière photo */
    var N = NPOS[mode], sol = H * 0.62;
    if (mode === 'ru') { return [W * 0.08 + u * W * 0.1, sol]; }
    if (mode === 'ra') { return [W * 0.06 + W * (0.025 * u + 0.0095 * u * u), sol]; }
    if (mode === 'rr') {   /* ralentit, puis s'arrête */
      var fin = W * 0.06 + W * (0.025 * 8 + 0.0095 * 64), j = N - 1 - u;
      if (j >= 0) { return [fin - W * (0.025 * j + 0.0095 * j * j), sol]; }
      var e = Math.min(-j, 0.025 / 0.019); return [fin + W * (0.025 * e - 0.0095 * e * e), sol];
    }
    if (mode === 'cu') { var R = Math.min(W, H) * 0.34, a = -Math.PI / 2 + 2 * Math.PI * u / N; return [W / 2 + R * Math.cos(a), H / 2 + R * Math.sin(a)]; }
    var s = u / (N - 1), gy = H * 0.86;   /* ballon lancé, puis petits rebonds */
    if (s <= 1) { return [W * 0.08 + s * W * 0.84, gy - H * 0.7 * 4 * s * (1 - s)]; }
    var r = s - 1, b = 0.32; var x = W * 0.92 + r * W * 0.84 * 0.6, y = r < b ? gy - H * 0.7 * 0.18 * 4 * (r / b) * (1 - r / b) : gy;
    return [x, y];
  }
  function positions(mode, W, H) { var P = []; for (var i = 0; i < NPOS[mode]; i++) { P.push(posCont(mode, i, W, H)); } return P; }
  (function () {
    var root = document.getElementById('lab-chrono'); if (!root) { return; }
    var chk = $(root, '[data-in="vec"]'), msg = $(root, '.nt-msg'), mode = 'ru', t = 99, run = false, cnv, DTP = 0.38;
    var MSG = {
      ru: 'Positions <b>également espacées</b> sur une droite&nbsp;: mouvement <b>rectiligne uniforme</b>. Les vecteurs vitesse sont tous identiques&nbsp;: le vecteur vitesse est constant.',
      ra: 'Positions <b>de plus en plus espacées</b>&nbsp;: mouvement <b>rectiligne accéléré</b>. Les vecteurs vitesse gardent la même direction et le même sens, mais s\u2019allongent.',
      rr: 'Positions <b>de plus en plus rapprochées</b>&nbsp;: mouvement <b>rectiligne ralenti</b>. Les vecteurs vitesse raccourcissent, jusqu\u2019à l\u2019arrêt.',
      cu: 'Positions également espacées sur un cercle&nbsp;: mouvement <b>circulaire uniforme</b>. Les vecteurs vitesse ont tous la même longueur, mais leur <b>direction change</b> sans cesse&nbsp;: le vecteur vitesse n\u2019est pas constant.',
      pa: 'Ballon lancé&nbsp;: trajectoire courbe (une parabole). Les vecteurs vitesse changent de direction, et leur longueur diminue pendant la montée puis augmente pendant la descente.'
    };
    function decor(ctx, W, H) {
      var g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#F8FAFC'); g.addColorStop(1, '#EEF2F7'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      if (mode === 'ru' || mode === 'ra' || mode === 'rr') { ctx.fillStyle = '#CBD5E1'; ctx.fillRect(0, H * 0.62 + 11, W, 4); ctx.fillStyle = '#E2E8F0'; ctx.fillRect(0, H * 0.62 + 15, W, H); }
      if (mode === 'pa') { ctx.fillStyle = '#BBF7D0'; ctx.fillRect(0, H * 0.86 + 10, W, H); ctx.fillStyle = '#86EFAC'; ctx.fillRect(0, H * 0.86 + 10, W, 3); }
      if (mode === 'cu') { ctx.fillStyle = '#475569'; ctx.beginPath(); ctx.arc(W / 2, H / 2, 4, 0, 2 * Math.PI); ctx.fill(); ctx.save(); ctx.setLineDash([3, 5]); ctx.strokeStyle = '#CBD5E1'; ctx.beginPath(); ctx.arc(W / 2, H / 2, Math.min(W, H) * 0.34, 0, 2 * Math.PI); ctx.stroke(); ctx.restore(); }
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, N = NPOS[mode], u = t / DTP, n = Math.min(N, Math.floor(u + 1e-6) + 1), r = mode === 'pa' ? 11 : 10;
      ctx.clearRect(0, 0, W, H); decor(ctx, W, H);
      var P = positions(mode, W, H);
      for (var i = 0; i < n; i++) { balle(ctx, P[i][0], P[i][1], r, 0.28); croix(ctx, P[i][0], P[i][1], ROUGE, 4.5); txt(ctx, 'M' + indice(i), P[i][0], P[i][1] + (mode === 'cu' && P[i][1] < H / 2 ? -18 : 20), { size: 11, serif: true, col: '#94A3B8' }); }
      if (chk.checked) {
        for (i = 0; i < n; i++) { var Q = i < N - 1 ? P[i + 1] : posCont(mode, N, W, H); if (i === N - 1 && mode !== 'cu') { continue; } if (i < n - 1 || u >= N - 1) { vec(ctx, P[i][0], P[i][1], P[i][0] + (Q[0] - P[i][0]) * 0.85, P[i][1] + (Q[1] - P[i][1]) * 0.85, ORANGE, 2.2, 10); } }
      }
      if (run) {
        var b = posCont(mode, u, W, H), al = u > N - 1 ? Math.max(0, 1 - (u - (N - 1)) / 2.6) : 1;
        if (mode === 'cu') { ctx.strokeStyle = 'rgba(71,85,105,0.5)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(W / 2, H / 2); ctx.lineTo(b[0], b[1]); ctx.stroke(); }
        balle(ctx, b[0], b[1], r, al);
        var f = u - Math.floor(u); if (u <= N - 1 + 1e-6 && f < 0.15) { var al2 = 0.5 * (1 - f / 0.15); var gf = ctx.createRadialGradient(b[0], b[1], 2, b[0], b[1], 60); gf.addColorStop(0, 'rgba(253,224,71,' + al2.toFixed(2) + ')'); gf.addColorStop(1, 'rgba(253,224,71,0)'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H); }
      }
      pill(ctx, 'une photo toutes les \u0394t', W - 10, 16, { size: 11, col: SLATE, align: 'right', stroke: GRID2 });
    }
    var loop = Loop(root, function (dt) { if (!run) { return false; } t += dt; var N = NPOS[mode]; if (t / DTP > N - 1 + 2.6) { run = false; msg.innerHTML = MSG[mode]; } draw(cnv); return run; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 230 : 270; }, draw);
    function lance() { msg.textContent = 'Clic… clic… clic…'; if (RM) { t = 99; run = false; msg.innerHTML = MSG[mode]; draw(cnv); return; } t = 0; run = true; loop.kick(); }
    $$(root, 'input[name="ch-m"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; lance(); }); });
    $(root, '[data-act="replay"]').addEventListener('click', lance);
    chk.addEventListener('change', function () { draw(cnv); });
    msg.innerHTML = MSG[mode]; draw(cnv);
  })();

  /* =================== quiz à choix =================== */
  function Quiz(root, BANQUE, nb, fabrique) {
    var qEl = $(root, '.nt-ql-q'), bx = $(root, '.nt-ql-btns'), Q = [];
    var S = Serie(root, nb, {
      init: function () { Q = fabrique ? fabrique() : shuffle(BANQUE.slice()).slice(0, nb); },
      show: function (k) {
        var q = Q[k], ordre = q[3] ? q[1].map(function (_, i) { return i; }) : shuffle(q[1].map(function (_, i) { return i; })); qEl.innerHTML = q[0]; bx.innerHTML = ''; bx.hidden = false;
        ordre.forEach(function (i) {
          var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn nt-choix'; b.innerHTML = q[1][i]; b.setAttribute('data-i', i);
          b.addEventListener('click', function () {
            if (S.answered) { return; } var ok = i === (q[4] || 0);
            b.classList.add(ok ? 'nt-choix-ok' : 'nt-choix-ko'); if (!ok) { $(bx, '[data-i="' + (q[4] || 0) + '"]').classList.add('nt-choix-ok'); }
            S.answer(ok, q[2], ok ? null : '<b>Non.</b> ');
          });
          bx.appendChild(b);
        });
        typeset(qEl); typeset(bx);   /* les réponses peuvent contenir des formules */
      },
      bilan: function (g) { qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;' + nb + '</span><br>' + (g / nb >= 0.85 ? 'Excellent&nbsp;!' : 'Relisez les explications des questions manquées, puis recommencez&nbsp;: les questions seront mélangées.'); bx.innerHTML = ''; bx.hidden = true; }
    });
    S.start();
  }
  function chronoSVG(mode, vecs) {   /* petite chronophotographie en SVG pour les questions */
    var W = 420, H = mode === 'cu' || mode === 'pa' ? 200 : 110, P = positions(mode, W, H), h = '';
    P.forEach(function (p, i) {
      h += "<path d='M" + (p[0] - 4.5) + ',' + (p[1] - 4.5) + ' L' + (p[0] + 4.5) + ',' + (p[1] + 4.5) + ' M' + (p[0] + 4.5) + ',' + (p[1] - 4.5) + ' L' + (p[0] - 4.5) + ',' + (p[1] + 4.5) + "' stroke='#E11D48' stroke-width='1.6' stroke-linecap='round'/>";
      if (vecs && i < P.length - 1 && i % 2 === 0) { var Q = P[i + 1], x2 = p[0] + (Q[0] - p[0]) * 0.85, y2 = p[1] + (Q[1] - p[1]) * 0.85, d = Math.hypot(x2 - p[0], y2 - p[1]), ux = (x2 - p[0]) / d, uy = (y2 - p[1]) / d; h += "<line x1='" + p[0] + "' y1='" + p[1] + "' x2='" + (x2 - ux * 7).toFixed(1) + "' y2='" + (y2 - uy * 7).toFixed(1) + "' stroke='#D97706' stroke-width='2.2' stroke-linecap='round'/><polygon points='" + x2.toFixed(1) + ',' + y2.toFixed(1) + ' ' + (x2 - ux * 9 - uy * 4).toFixed(1) + ',' + (y2 - uy * 9 + ux * 4).toFixed(1) + ' ' + (x2 - ux * 9 + uy * 4).toFixed(1) + ',' + (y2 - uy * 9 - ux * 4).toFixed(1) + "' fill='#D97706'/>"; }
    });
    h += "<text x='" + P[0][0] + "' y='" + (P[0][1] + (mode === 'cu' ? -12 : 20)) + "' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, sans-serif'>départ</text>";
    return "<svg class='nt-qsvg' viewBox='0 0 " + W + ' ' + H + "' width='" + W + "' role='img' aria-label='chronophotographie'>" + h + '</svg>';
  }
  (function () {
    var root = document.getElementById('quiz-chrono'); if (!root) { return; }
    var NOMS = ['rectiligne uniforme', 'rectiligne accéléré', 'rectiligne ralenti', 'circulaire uniforme'], MODES = ['ru', 'ra', 'rr', 'cu'];
    function fab() {
      var L = [];
      MODES.forEach(function (m, k) { L.push(['Les positions sont enregistrées à intervalles de temps égaux. Ce mouvement est…' + chronoSVG(m, false), NOMS, ['Positions également espacées sur une droite&nbsp;: la vitesse est constante.', 'Les positions sont de plus en plus espacées&nbsp;: le mobile parcourt de plus en plus de distance pendant chaque \u0394t, il accélère.', 'Les positions sont de plus en plus rapprochées&nbsp;: le mobile ralentit.', 'Positions également espacées sur un cercle&nbsp;: mouvement circulaire uniforme.'][k], true, k]); });
      L.push(['Sur cette chronophotographie, la norme du vecteur vitesse…' + chronoSVG('ra', true), ['augmente', 'diminue', 'reste constante'], 'Les flèches s\u2019allongent&nbsp;: la vitesse augmente.', true, 0]);
      L.push(['Sur cette chronophotographie, la norme du vecteur vitesse…' + chronoSVG('rr', true), ['augmente', 'diminue', 'reste constante'], 'Les flèches raccourcissent&nbsp;: la vitesse diminue.', true, 1]);
      L.push(['Dans ce mouvement circulaire uniforme, le vecteur vitesse…' + chronoSVG('cu', true), ['change de direction mais garde la même norme', 'est constant', 'change de norme mais garde la même direction'], 'La norme est constante (mouvement uniforme), mais la direction change sans cesse&nbsp;: le vecteur vitesse n\u2019est pas constant.', false, 0]);
      L.push(['Pour ce ballon lancé, la norme du vecteur vitesse…' + chronoSVG('pa', true), ['diminue pendant la montée puis augmente', 'reste constante', 'augmente pendant la montée puis diminue'], 'Les positions se rapprochent pendant la montée et s\u2019écartent pendant la descente&nbsp;: le ballon ralentit en montant et accélère en redescendant.', false, 0]);
      return shuffle(L).slice(0, 6);
    }
    Quiz(root, null, 6, fab);
  })();

  /* =================== 10. Trampoline sur une remorque =================== */
  function decorCampagne(ctx, W, H, sol, sx, cam, k, nuages) {   /* ciel, nuages, champ et arbres (sx : abscisse à l'écran d'une position en m) */
    var g = ctx.createLinearGradient(0, 0, 0, sol); g.addColorStop(0, '#7DD3FC'); g.addColorStop(1, '#E0F2FE'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, sol);
    nuages.forEach(function (n) { var x = ((sx(n[0]) - sx(0)) * 0.25 + n[0] * k) % (W + 200); x = (x + W + 200) % (W + 200) - 100; ctx.fillStyle = 'rgba(255,255,255,0.9)'; ctx.beginPath(); ctx.ellipse(x, n[1] * H, 34, 11, 0, 0, 2 * Math.PI); ctx.ellipse(x + 18, n[1] * H - 7, 18, 10, 0, 0, 2 * Math.PI); ctx.fill(); });
    ctx.fillStyle = '#A7F3D0'; ctx.beginPath(); ctx.moveTo(0, sol); for (var x = 0; x <= W; x += 20) { ctx.lineTo(x, sol - 14 - 8 * Math.sin((x - (sx(0) * 0.5)) / 90)); } ctx.lineTo(W, sol); ctx.fill();
    for (var a = Math.floor((cam - 40) / 8) * 8; a < cam + W / k + 40; a += 8) { var xa = sx(a); if (xa > -30 && xa < W + 30) { ctx.fillStyle = '#92400E'; ctx.fillRect(xa - 2, sol - 30, 4, 30); ctx.fillStyle = '#22C55E'; ctx.beginPath(); ctx.arc(xa, sol - 38, 14, 0, 2 * Math.PI); ctx.arc(xa - 9, sol - 30, 9, 0, 2 * Math.PI); ctx.arc(xa + 9, sol - 30, 9, 0, 2 * Math.PI); ctx.fill(); } }
    var gs = ctx.createLinearGradient(0, sol, 0, H); gs.addColorStop(0, '#D6C29A'); gs.addColorStop(1, '#BFA672'); ctx.fillStyle = gs; ctx.fillRect(0, sol, W, H - sol);
    ctx.fillStyle = 'rgba(120,90,40,0.35)'; for (var p = Math.floor((cam - 20) / 2.5) * 2.5; p < cam + W / k + 20; p += 2.5) { var xp = sx(p); if (xp > -20 && xp < W + 20) { ctx.fillRect(xp, sol + 9, 16, 2.5); } }
  }
  (function () {
    var root = document.getElementById('lab-tramp'); if (!root) { return; }
    var chk = $(root, '[data-in="comp"]'), msg = $(root, '.nt-msg');
    var G = 10, HM = 1.6, V0 = 8, LT = 1.9, NU = [[3, 0.12], [14, 0.22], [27, 0.1], [40, 0.18]];
    var ref = 'tracteur', S, trace, cnv, run = true, camSol = 0;
    function init() { S = { t: 0, X: 0, V: 2.2, A: 0, bx: 0, by: HM, u: 2.2, vy: V0, etat: 'air', fin: 0 }; trace = []; }
    function step(dt) {
      if (!run) { return false; } dt = Math.min(dt, 0.04); S.t += dt;
      S.V = Math.max(0, Math.min(7, S.V + S.A * dt)); if (S.V === 0 || S.V === 7) { S.A = 0; } S.X += S.V * dt;
      if (S.etat === 'air') {
        S.bx += S.u * dt; S.vy -= G * dt; S.by += S.vy * dt;
        var dessus = Math.abs(S.bx - S.X) < LT;
        if (S.vy < 0 && dessus && S.by <= HM && S.by > HM - 0.6) { S.by = HM; S.vy = V0; }   /* rebond sur la toile : la vitesse horizontale de la balle ne change pas */
        else if (S.by <= 0) { S.by = 0; S.vy = -S.vy * 0.45; S.u *= 0.7; if (Math.abs(S.vy) < 1) { S.etat = 'sol'; } if (!S.fin) { S.fin = 1; texte(); } }
      } else { S.u *= Math.pow(0.15, dt); S.bx += S.u * dt; S.by = 0; }
      var arr = S.X + 4.4 - 0.25;   /* la balle ne traverse pas le tracteur : elle rebondit sur l'arrière */
      if (S.bx > arr && S.bx < S.X + 7.2 && S.by < 2.9) { S.bx = arr; S.u = Math.min(S.u, S.V) - 0.3 * Math.abs(S.u - S.V); }
      trace.push([S.bx, S.by, S.X, S.t]); while (trace.length && S.t - trace[0][3] > 1.7) { trace.shift(); }   /* on ne garde que le dernier rebond */
      if (S.t > 60) { run = false; }
      draw(cnv); return run;
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k = H / 9.5, sol = H - 34, cam = ref === 'tracteur' ? S.X : camSol, cx = W * (ref === 'tracteur' ? 0.36 : 0.1);   /* référentiel sol : caméra fixe, le tracteur finit par sortir à droite */
      function sx(x) { return cx + (x - cam) * k; }
      function sy(h) { return sol - h * k; }
      ctx.clearRect(0, 0, W, H); decorCampagne(ctx, W, H, sol, sx, cam, k, NU);
      var xt = sx(S.X), yM = sy(HM);
      ctx.fillStyle = 'rgba(15,23,42,0.18)'; ctx.beginPath(); ctx.ellipse(xt + 2.5 * k, sol + 3, 5.6 * k, 0.17 * k, 0, 0, 2 * Math.PI); ctx.fill();
      var gp = ctx.createLinearGradient(0, sy(1.05), 0, sy(0.75)); gp.addColorStop(0, '#78716C'); gp.addColorStop(1, '#44403C'); ctx.fillStyle = gp; rr(ctx, xt - 2.3 * k, sy(1.05), 4.6 * k, 0.3 * k, 3); ctx.fill();
      [-1.5, 1.5].forEach(function (d) { ctx.fillStyle = '#1F2937'; ctx.beginPath(); ctx.arc(xt + d * k, sol - 0.38 * k, 0.38 * k, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#9CA3AF'; ctx.beginPath(); ctx.arc(xt + d * k, sol - 0.38 * k, 0.15 * k, 0, 2 * Math.PI); ctx.fill(); });
      ctx.strokeStyle = '#334155'; ctx.lineWidth = 3; [-LT, LT].forEach(function (d) { ctx.beginPath(); ctx.moveTo(xt + d * k, sy(1.05)); ctx.lineTo(xt + d * k, yM); ctx.stroke(); });
      var enf = S.etat === 'air' && S.vy > 0 && S.by - HM < 0.3 && Math.abs(S.bx - S.X) < LT ? (0.3 - (S.by - HM)) * 0.5 : 0;
      ctx.strokeStyle = '#0F172A'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(xt - LT * k, yM); ctx.quadraticCurveTo(Math.max(xt - LT * k, Math.min(xt + LT * k, sx(S.bx))), yM + enf * k * 2, xt + LT * k, yM); ctx.stroke();
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1; for (var sp = -1.7; sp <= 1.71; sp += 0.34) { ctx.beginPath(); ctx.moveTo(xt + sp * k, yM + 1); ctx.lineTo(xt + sp * k, yM + 0.12 * k); ctx.stroke(); }
      var tx = xt + 4.6 * k;   /* tracteur, attelé par une longue barre */
      ctx.strokeStyle = '#334155'; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.moveTo(xt + 2.3 * k, sy(0.9)); ctx.lineTo(tx + 0.1 * k, sy(0.9)); ctx.stroke();
      var gt = ctx.createLinearGradient(0, sy(2.9), 0, sy(0.7)); gt.addColorStop(0, '#22C55E'); gt.addColorStop(1, '#15803D'); ctx.fillStyle = gt;
      rr(ctx, tx, sy(1.75), 2.5 * k, 1.0 * k, 6); ctx.fill(); rr(ctx, tx + 0.15 * k, sy(2.95), 1.15 * k, 1.3 * k, 6); ctx.fill();
      ctx.fillStyle = '#E0F2FE'; rr(ctx, tx + 0.3 * k, sy(2.8), 0.85 * k, 0.65 * k, 3); ctx.fill(); ctx.fillStyle = 'rgba(255,255,255,0.6)'; ctx.fillRect(tx + 0.35 * k, sy(2.75), 0.15 * k, 0.5 * k);
      ctx.fillStyle = '#334155'; ctx.fillRect(tx + 2.0 * k, sy(2.5), 0.13 * k, 0.75 * k); ctx.fillStyle = '#FBBF24'; ctx.fillRect(tx + 2.38 * k, sy(1.55), 0.12 * k, 0.2 * k);
      [[tx + 0.65 * k, 0.78 * k], [tx + 2.1 * k, 0.46 * k]].forEach(function (wl) { ctx.fillStyle = '#111827'; ctx.beginPath(); ctx.arc(wl[0], sol - wl[1], wl[1], 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#DC2626'; ctx.beginPath(); ctx.arc(wl[0], sol - wl[1], wl[1] * 0.55, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#FCA5A5'; ctx.beginPath(); ctx.arc(wl[0], sol - wl[1], wl[1] * 0.18, 0, 2 * Math.PI); ctx.fill(); });
      ctx.save(); ctx.strokeStyle = TRAJ; ctx.lineWidth = 2.2; ctx.lineCap = 'round'; ctx.setLineDash([0.1, 6]); ctx.beginPath();   /* trajectoire en pointillés */
      trace.forEach(function (q, i) { var xq = ref === 'tracteur' ? sx(q[0] - q[2] + S.X) : sx(q[0]), yq = sy(q[1]) - 0.25 * k; if (i) { ctx.lineTo(xq, yq); } else { ctx.moveTo(xq, yq); } }); ctx.stroke(); ctx.restore();
      var rb = 0.25 * k, bxs = sx(S.bx), bys = sy(S.by) - rb;
      ctx.fillStyle = 'rgba(15,23,42,0.2)'; ctx.beginPath(); ctx.ellipse(bxs, (Math.abs(S.bx - S.X) < LT && S.by >= HM - 0.1 ? yM : sol) + 2, rb, rb * 0.3, 0, 0, 2 * Math.PI); ctx.fill();
      var gb = ctx.createRadialGradient(bxs - rb * 0.35, bys - rb * 0.35, rb * 0.1, bxs, bys, rb); gb.addColorStop(0, '#FDBA74'); gb.addColorStop(1, '#EA580C'); ctx.fillStyle = gb; ctx.beginPath(); ctx.arc(bxs, bys, rb, 0, 2 * Math.PI); ctx.fill();
      var vx = S.u - (ref === 'tracteur' ? S.V : 0), vyy = S.etat === 'air' ? S.vy : 0, f = 14, x0 = bxs, y0 = bys;
      if (Math.hypot(vx, vyy) > 0.15) { vec(ctx, x0, y0, x0 + vx * f, y0 - vyy * f, ORANGE, 2.8, 12); }
      if (chk.checked && S.etat === 'air') { ctx.save(); ctx.setLineDash([4, 3]); if (Math.abs(vx) > 0.05) { vec(ctx, x0, y0, x0 + vx * f, y0, '#E0A400', 1.4, 8); } if (Math.abs(vyy) > 0.05) { vec(ctx, x0, y0, x0, y0 - vyy * f, '#E0A400', 1.4, 8); } ctx.restore(); }
      pill(ctx, 'référentiel ' + (ref === 'sol' ? 'terrestre' : 'du tracteur'), 10, 16, { size: 12, col: NAVY, align: 'left', stroke: GRID2 });
      pill(ctx, 'tracteur\u00A0: ' + fmt(S.V * 3.6, 0) + ' km/h' + (S.A > 0 ? ' (accélère)' : (S.A < 0 ? ' (freine)' : '')), W < 520 ? 10 : W - 10, W < 520 ? 42 : 16, { size: 12, col: '#166534', align: W < 520 ? 'left' : 'right', stroke: '#BBF7D0' });
    }
    function texte() {
      if (S.fin) { msg.innerHTML = 'La balle a raté le trampoline&nbsp;! En l\u2019air, elle a gardé la vitesse horizontale qu\u2019elle avait au dernier rebond, alors que le tracteur ' + (S.A > 0 || S.V > 2.3 ? 'accélérait' : 'freinait') + '&nbsp;: elle n\u2019est plus restée au-dessus du trampoline. Dans le référentiel du tracteur, elle a dérivé ' + (S.V > 2.3 ? 'vers l\u2019arrière' : 'vers l\u2019avant') + '.'; return; }
      msg.innerHTML = ref === 'tracteur' ? 'Dans le référentiel du tracteur, la balle monte et descend <b>à la verticale</b>&nbsp;: sa vitesse n\u2019a pas de partie horizontale. Que se passe-t-il si le tracteur accélère ou freine pendant que la balle est en l\u2019air&nbsp;?' : 'Dans le référentiel terrestre, la balle avance avec la remorque&nbsp;: sa trajectoire est une suite d\u2019<b>arches</b>, et sa vitesse a une partie horizontale constante, égale à celle du tracteur.';
    }
    var loop = Loop(root, step);
    init(); cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 270 : 310; }, draw);
    $$(root, 'input[name="tp-ref"]').forEach(function (r) { r.addEventListener('change', function () { ref = r.value; if (ref === 'sol') { camSol = S.X; } trace = []; texte(); draw(cnv); }); });
    $(root, '[data-act="acc"]').addEventListener('click', function () { S.A = 2.5; run = true; loop.kick(); });
    $(root, '[data-act="frein"]').addEventListener('click', function () { S.A = -2.5; run = true; loop.kick(); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { init(); camSol = 0; run = !RM; texte(); draw(cnv); loop.kick(); });
    chk.addEventListener('change', function () { draw(cnv); });
    if (RM) { run = false; }
    texte(); draw(cnv); if (run) { loop.kick(); }
  })();

  /* =================== 10 b. Le ballon tiré vers l'arrière d'un pick-up =================== */
  (function () {
    var root = document.getElementById('lab-pickup'); if (!root) { return; }
    var bG = $(root, '[data-act="go"]'), msg = $(root, '.nt-msg');
    var V = 13.9, G = 9.8, RAL = 0.28, LC = 3.2, AX = 1.75, BACK = 5.0, ref = 'sol', t = 0, tir = 0.6, run = false, cnv, NU = [[2, 0.12], [16, 0.2], [30, 0.1]];
    var tsort = tir + (LC - 0.2) / V;   /* le ballon parcourt tout le canon à 50 km/h par rapport au pick-up */
    function xp(t) { return 0.86 + V * t; }   /* avant du pick-up (m), référentiel terrestre : le ballon sort au milieu de la scène */
    function fond(t) { return xp(t) - 1.0; }   /* fond du canon (côté cabine) */
    function ballon(t) {   /* position du centre du ballon (m) dans le référentiel terrestre */
      var xb = fond(tir) - 0.2;
      if (t < tir) { return [fond(t) - 0.2, AX]; }
      if (t < tsort) { return [xb, AX]; }   /* dans le canon : immobile par rapport au sol, c'est le canon qui glisse ! */
      var tt = t - tsort, h0 = AX, tc = Math.sqrt(2 * (h0 - 0.22) / G);
      if (tt < tc) { return [xb, h0 - 0.5 * G * tt * tt]; }
      tt -= tc; var v = G * tc * 0.6;
      while (v > 0.4) { var d = 2 * v / G; if (tt < d) { return [xb, 0.22 + v * tt - 0.5 * G * tt * tt]; } tt -= d; v *= 0.6; }
      return [xb, 0.22];
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k = W / 24, sol = H - 40, cam = ref === 'pickup' ? xp(t) - 17 : -4;
      function sx(x) { return (x - cam) * k; }
      function sy(h) { return sol - h * k; }
      ctx.clearRect(0, 0, W, H); decorCampagne(ctx, W, H, sol, sx, cam, k, NU);
      var gr = ctx.createLinearGradient(0, sol, 0, sol + 16); gr.addColorStop(0, '#4B5563'); gr.addColorStop(1, '#374151'); ctx.fillStyle = gr; ctx.fillRect(0, sol, W, 16);
      ctx.fillStyle = '#F8FAFC'; for (var r = Math.floor(cam / 4) * 4; r < cam + W / k + 4; r += 4) { ctx.fillRect(sx(r), sol + 7, 1.6 * k, 2); }
      if (t >= tir) {   /* trajectoire du ballon, en pointillés */
        ctx.save(); ctx.strokeStyle = TRAJ; ctx.lineWidth = 2.2; ctx.lineCap = 'round'; ctx.setLineDash([0.1, 6]); ctx.beginPath();
        for (var i = 0; i <= 160; i++) { var ti = tir + (t - tir) * i / 160, b = ballon(ti), x = ref === 'sol' ? sx(b[0]) : sx(b[0] - xp(ti) + xp(t)); if (i) { ctx.lineTo(x, sy(b[1])); } else { ctx.moveTo(x, sy(b[1])); } }
        ctx.stroke(); ctx.restore();
      }
      var xf = sx(xp(t));   /* pick-up */
      ctx.fillStyle = 'rgba(15,23,42,0.22)'; ctx.beginPath(); ctx.ellipse(xf - 2.6 * k, sol + 2, 3.0 * k, 0.15 * k, 0, 0, 2 * Math.PI); ctx.fill();
      var gc = ctx.createLinearGradient(0, sy(2.2), 0, sy(0.4)); gc.addColorStop(0, '#3B82F6'); gc.addColorStop(1, '#1D4ED8'); ctx.fillStyle = gc;
      rr(ctx, xf - BACK * k, sy(1.25), BACK * k, 0.85 * k, 6); ctx.fill();
      ctx.beginPath(); ctx.moveTo(xf - 2.2 * k, sy(1.2)); ctx.lineTo(xf - 2.0 * k, sy(2.1)); ctx.lineTo(xf - 0.9 * k, sy(2.1)); ctx.lineTo(xf - 0.25 * k, sy(1.3)); ctx.lineTo(xf, sy(1.2)); ctx.closePath(); ctx.fill();
      ctx.fillStyle = '#DBEAFE'; ctx.beginPath(); ctx.moveTo(xf - 1.85 * k, sy(1.35)); ctx.lineTo(xf - 1.75 * k, sy(1.95)); ctx.lineTo(xf - 1.0 * k, sy(1.95)); ctx.lineTo(xf - 0.5 * k, sy(1.35)); ctx.closePath(); ctx.fill();
      ctx.fillStyle = '#FDE68A'; ctx.fillRect(xf - 0.12 * k, sy(1.0), 0.12 * k, 0.15 * k); ctx.fillStyle = '#F87171'; ctx.fillRect(xf - BACK * k, sy(1.05), 0.1 * k, 0.18 * k);
      [xf - 4.1 * k, xf - 1.0 * k].forEach(function (wx) { ctx.fillStyle = '#111827'; ctx.beginPath(); ctx.arc(wx, sol - 0.42 * k, 0.42 * k, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#CBD5E1'; ctx.beginPath(); ctx.arc(wx, sol - 0.42 * k, 0.2 * k, 0, 2 * Math.PI); ctx.fill(); });
      var cxR = xf - 1.0 * k, cxL = cxR - LC * k, ry = sy(AX), rc = 0.32 * k;   /* canon horizontal, embouchure vers l'arrière */
      ctx.fillStyle = '#475569'; ctx.fillRect(cxL + 0.9 * k, sy(1.25) - 0.02 * k, 0.25 * k, (sy(1.25) - ry) * -1 + 0.02 * k); ctx.fillRect(cxR - 0.6 * k, ry, 0.25 * k, sy(1.25) - ry);
      var b = ballon(t), bx = ref === 'sol' ? sx(b[0]) : sx(b[0] - xp(t) + xp(t)), byy = sy(b[1]), rb = 0.24 * k;
      var gtb = ctx.createLinearGradient(0, ry - rc, 0, ry + rc); gtb.addColorStop(0, '#94A3B8'); gtb.addColorStop(0.45, '#E2E8F0'); gtb.addColorStop(1, '#64748B');
      ctx.fillStyle = gtb; rr(ctx, cxL, ry - rc, LC * k, 2 * rc, rc * 0.4); ctx.fill();
      ctx.fillStyle = 'rgba(15,23,42,0.55)'; rr(ctx, cxL + 0.08 * k, ry - rc * 0.72, LC * k - 0.16 * k, 1.44 * rc, rc * 0.5); ctx.fill();   /* intérieur du tube, vu en coupe */
      var rbm = 0.24, xbRel = t < tir ? -1.2 : Math.max(-1.0 - LC, -1.2 - V * (t - tir)), xpRel = Math.max(-1.0 - LC + 0.12, xbRel + rbm);   /* positions le long du canon, par rapport à l'avant du pick-up (m) */
      var xPis = xf + xpRel * k;   /* paroi mobile (piston) : elle pousse le ballon à 50 km/h, puis s'arrête près de l'embouchure */
      ctx.fillStyle = '#CBD5E1'; ctx.fillRect(xPis, ry - 0.05 * k, cxR - xPis, 0.1 * k);
      var gpi = ctx.createLinearGradient(xPis, 0, xPis + 0.14 * k, 0); gpi.addColorStop(0, '#F59E0B'); gpi.addColorStop(1, '#FCD34D'); ctx.fillStyle = gpi; rr(ctx, xPis, ry - rc * 0.7, 0.14 * k, 1.4 * rc, 2); ctx.fill();
      if (t < tsort) { ballDraw(bx, byy, rb); }
      ctx.fillStyle = '#334155'; rr(ctx, cxL - 0.12 * k, ry - rc * 1.15, 0.22 * k, 2.3 * rc, 3); ctx.fill(); rr(ctx, cxR - 0.1 * k, ry - rc * 1.1, 0.2 * k, 2.2 * rc, 3); ctx.fill();
      if (t >= tsort) { ballDraw(bx, byy, rb); }
      function ballDraw(x, y, r) { var g = ctx.createRadialGradient(x - r * 0.35, y - r * 0.35, r * 0.1, x, y, r); g.addColorStop(0, '#FFFFFF'); g.addColorStop(1, '#CBD5E1'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#1E293B'; ctx.lineWidth = 1; ctx.stroke(); ctx.fillStyle = '#1E293B'; ctx.beginPath(); ctx.arc(x, y, r * 0.35, 0, 2 * Math.PI); ctx.fill(); }
      var f = 0.13 * k, vp = ref === 'sol' ? V : 0, yv = sy(2.75);
      if (vp) { vec(ctx, xf - 3 * k, yv, xf - 3 * k + vp * f, yv, VERT, 2.6, 11); pill(ctx, 'pick-up\u00A0: 50 km/h', Math.max(70, Math.min(W - 70, xf - 3 * k + vp * f / 2)), yv - 0.55 * k, { size: 11, col: VERT_T, stroke: '#99F6E4' }); }
      else { pill(ctx, 'pick-up\u00A0: immobile', xf - 3 * k, yv, { size: 11, col: VERT_T, stroke: '#99F6E4' }); }
      if (t >= tir) {
        var bb = ballon(t), b2 = ballon(t + 0.002), vbx = (b2[0] - bb[0]) / 0.002 - (ref === 'pickup' ? V : 0), vby = (b2[1] - bb[1]) / 0.002;
        if (Math.hypot(vbx, vby) > 0.3) { vec(ctx, bx, byy, bx + vbx * f, byy - vby * f, ORANGE, 2.8, 11); }
        if (ref === 'sol' && t < tsort + 0.25) { pill(ctx, 'ballon\u00A0: vitesse horizontale nulle', bx, byy - 1.2 * k, { size: 11, col: ORANGE_T, stroke: '#FDE68A' }); }
        if (ref === 'pickup' && t < tsort + 0.25) { pill(ctx, 'ballon\u00A0: 50 km/h vers l\u2019arrière', bx, byy - 1.2 * k, { size: 11, col: ORANGE_T, stroke: '#FDE68A' }); }
      }
      pill(ctx, 'référentiel ' + (ref === 'sol' ? 'terrestre' : 'du pick-up'), 10, 16, { size: 12, col: NAVY, align: 'left', stroke: GRID2 });
      pill(ctx, 'ralenti', W - 10, 16, { size: 11, col: SLATE, align: 'right', stroke: GRID2 });
    }
    function step(dt) { if (!run) { return false; } var t0 = t; t += dt * RAL; if (t0 < tir && t >= tir) { msg.innerHTML = 'Tir&nbsp;! Le ballon parcourt le canon à 50&nbsp;km/h vers l\u2019arrière… ' + (ref === 'sol' ? 'mais, vu du sol, il ne bouge pas&nbsp;: c\u2019est le canon qui glisse autour de lui.' : 'et sort par l\u2019embouchure.'); } if (t > 2.9) { run = false; bG.disabled = false; fin(); } draw(cnv); return run; }
    function fin() { msg.innerHTML = ref === 'sol' ? 'Dans le référentiel terrestre, le ballon n\u2019a <b>aucune vitesse horizontale</b>, même dans le canon&nbsp;: il en sort et tombe <b>verticalement</b>, puis rebondit sur place, tandis que le pick-up continue sa route.' : 'Dans le référentiel du pick-up, le ballon parcourt le canon puis part vers l\u2019arrière à 50&nbsp;km/h tout en tombant&nbsp;: sa trajectoire est une <b>courbe</b> qui s\u2019éloigne du véhicule.'; }
    var loop = Loop(root, step);
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 240 : 290; }, draw);
    bG.addEventListener('click', function () { t = 0; if (RM) { t = 2.9; fin(); draw(cnv); return; } run = true; bG.disabled = true; msg.textContent = 'Le pick-up roule à 50\u00A0km/h, le ballon au fond du canon…'; loop.kick(); });
    $$(root, 'input[name="pk-ref"]').forEach(function (r) { r.addEventListener('change', function () { ref = r.value; if (!run && t >= 2.9) { fin(); } draw(cnv); }); });
    msg.textContent = 'Lancez la scène, puis comparez les deux points de vue.'; draw(cnv);
  })();

  /* =================== 11. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    Quiz(root, [
      ['Un passager est assis dans un train qui roule. Dans quel référentiel est-il immobile&nbsp;?', ['le référentiel du train', 'le référentiel terrestre', 'aucun'], 'Il ne bouge pas par rapport au train. Par rapport au sol, il avance à la vitesse du train.'],
      ['Que faut-il préciser pour décrire un mouvement sans ambiguïté&nbsp;?', ['le référentiel', 'la masse du système', 'la couleur du système'], 'Le mouvement est relatif&nbsp;: sa description dépend du référentiel.'],
      ['Dans un mouvement de translation…', ['tous les points du système ont des trajectoires identiques', 'tous les points décrivent des cercles de même centre', 'le système tourne sur lui-même'], 'En translation, le système ne tourne pas&nbsp;: toutes ses trajectoires sont superposables.'],
      ['En réduisant un système à un point, on perd l\u2019information sur…', ['sa rotation', 'sa trajectoire', 'sa vitesse'], 'Un point ne peut pas tourner sur lui-même&nbsp;: on perd la rotation (et la forme du système).'],
      ['Le vecteur vitesse moyenne entre M et M\u2032 a…', ['la même direction et le même sens que le vecteur déplacement MM\u2032', 'une direction perpendiculaire à MM\u2032', 'le sens opposé à MM\u2032'], 'Il vaut le vecteur déplacement divisé par la durée \u0394t&nbsp;: même direction, même sens.'],
      ['Un point parcourt MM\u2032 = 6&nbsp;m en \u0394t = 2&nbsp;s. Quelle est la norme du vecteur vitesse moyenne&nbsp;?', ['3&nbsp;m/s', '12&nbsp;m/s', '8&nbsp;m/s'], 'v = MM\u2032 / \u0394t = 6 / 2 = 3&nbsp;m/s.'],
      ['Avec l\u2019échelle 1&nbsp;cm \u2194 5&nbsp;m/s, quelle longueur de flèche pour une vitesse de 20&nbsp;m/s&nbsp;?', ['4&nbsp;cm', '100&nbsp;cm', '0,25&nbsp;cm'], '20 / 5 = 4&nbsp;cm.'],
      ['Le vecteur vitesse en un point M de la trajectoire est…', ['tangent à la trajectoire, dans le sens du mouvement', 'perpendiculaire à la trajectoire', 'toujours dirigé vers le centre de la trajectoire'], 'C\u2019est la limite du vecteur vitesse moyenne quand M\u2032 se rapproche de M.'],
      ['Sur une chronophotographie, les positions sont de plus en plus espacées. Le mouvement est…', ['accéléré', 'ralenti', 'uniforme'], 'Pendant chaque \u0394t, le mobile parcourt une distance de plus en plus grande&nbsp;: sa vitesse augmente.'],
      ['Dans un mouvement rectiligne uniforme, le vecteur vitesse…', ['est constant', 'change de direction', 'change de norme'], 'Même direction (la droite), même sens et même norme à tout instant.'],
      ['Dans un mouvement circulaire uniforme, le vecteur vitesse…', ['n\u2019est pas constant, car sa direction change', 'est constant', 'est nul'], 'Sa norme est constante, mais sa direction change en permanence.'],
      ['Un rebondeur saute sur une remorque qui avance à vitesse constante. Dans le référentiel de la remorque, sa trajectoire est…', ['un segment vertical', 'une suite d\u2019arches', 'un cercle'], 'Dans le référentiel de la remorque, il monte et descend à la verticale&nbsp;; ce sont les arches qu\u2019on voit depuis le sol.']
    ], 12);
  })();

})();
</script>
