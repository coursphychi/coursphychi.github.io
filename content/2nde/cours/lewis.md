+++
title = "Configuration électronique, ions et molécules"
draft = false
hidden = true
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
/* couleurs des sous-couches et des blocs */
.nt-s { color: #B45309; } .nt-p { color: #047857; }
.nt-cfg { font-family: Georgia, "Times New Roman", serif; white-space: nowrap; }
.nt-cfg sup { font-size: 0.68em; }
.nt-cfg .nt-coeur { color: #94A3B8; }
.nt-cfg .nt-val { color: var(--blue); font-weight: 700; }
/* remplissage du cortège */
.nt-remp-out { text-align: center; margin: 0.6em 0 0.2em !important; }
.nt-remp-out .nt-el { font-size: 1.15em; font-weight: 700; color: var(--navy); }
.nt-remp-out .nt-cfg { font-size: 1.45em; }
/* tableau périodique interactif */
.nt-tp-grid { display: grid; grid-template-columns: 1.6em repeat(2, minmax(0, 1fr)) minmax(0, 0.55fr) repeat(6, minmax(0, 1fr)); gap: 4px; max-width: 760px; margin: 0.6em auto 0.4em; }
.nt-tp-h { font-size: 0.7em; color: var(--slate); text-align: center; align-self: end; }
.nt-tp-n { font-size: 0.7em; color: var(--slate); display: flex; align-items: center; justify-content: center; }
.nt-tp-gap { border-left: 1px dashed #CBD5E1; border-right: 1px dashed #CBD5E1; display: flex; align-items: center; justify-content: center; font-size: 0.62em; color: #94A3B8; text-align: center; }
.nt-tp-cell { position: relative; min-height: 4.6em; padding: 1.1em 0.15em 0.3em; border: 1px solid #CBD5E1; border-radius: 8px; background: #FFFFFF; cursor: pointer; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.15em; font: inherit; color: var(--ink); transition: transform .12s, box-shadow .12s, background .2s; }
.nt-tp-cell:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15); }
.nt-tp-cell:focus-visible { outline: 3px solid var(--blue-lt); outline-offset: 1px; }
.nt-tp-cell.nt-on { box-shadow: 0 0 0 2.5px var(--blue); }
.nt-tp-cell .z { position: absolute; top: 0.2em; left: 0.35em; font-size: 0.62em; color: #64748B; }
.nt-tp-cell .sym { font-family: Georgia, "Times New Roman", serif; font-size: 1.3em; line-height: 1; }
.nt-tp-cell .sub { font-size: 0.68em; line-height: 1.3; text-align: center; }
.nt-tp-cell .sub .nt-cfg { white-space: normal; }
.nt-tp-row.nt-tp-dim { opacity: 0.35; }
.nt-tp-cell .sym-mini { position: absolute; top: 0.25em; right: 0.45em; font-size: 0.72em; color: #64748B; font-family: Georgia, "Times New Roman", serif; }
.nt-tp-cell .ion { font-family: Georgia, "Times New Roman", serif; font-size: 1.5em; line-height: 1; color: var(--navy); margin-top: 0.15em; }
.nt-tp-cell .ion .chg { font-size: 0.52em; vertical-align: 0.8em; margin-left: 0.06em; }
.nt-tp-cell.nt-sans .sym { color: #94A3B8; }
@media (max-width: 560px) { .nt-tp-cell .ion { font-size: 1.15em; } .nt-tp-cell .sym-mini { display: none; } }
.nt-tp-cell .nt-mini { display: block; width: 3.6em; height: 3.6em; margin: -0.5em auto -0.4em; }
@media (max-width: 560px) { .nt-tp-cell .nt-mini { width: 2.6em; height: 2.6em; } }
@media (prefers-reduced-motion: reduce) { .nt-tp-cell { transition: none; } .nt-tp-cell:hover { transform: none; } }
.nt-tp-cell .sub.mob, .nt-tp-h .sm { display: none; }
@media (max-width: 560px) { .nt-tp-cell { min-height: 3.2em; padding-top: 0.9em; } .nt-tp-cell .sub.long, .nt-tp-h .lg { display: none; } .nt-tp-cell .sub.mob, .nt-tp-h .sm { display: inline; } .nt-tp-cell .sym { font-size: 1.1em; } }
.nt-tp-leg { display: flex; flex-wrap: wrap; gap: 0.4em 1em; justify-content: center; font-size: 0.82em; margin: 0.3em 0; }
.nt-tp-leg span { display: inline-flex; align-items: center; gap: 0.35em; }
.nt-tp-leg i { width: 0.95em; height: 0.95em; border-radius: 3px; border: 1px solid rgba(15, 23, 42, 0.2); }
.nt-tp-info { display: grid; grid-template-columns: auto 1fr; gap: 0.4em 1em; align-items: center; max-width: 640px; margin: 0.6em auto 0; padding: 0.7em 1em; border-radius: 12px; background: var(--slate-bg); border: 1px solid var(--line); }
.nt-tp-info p { margin: 0.2em 0 !important; line-height: 1.5; font-size: 0.93em; }
.nt-tp-info .nt-tp-titre { font-weight: 700; color: var(--navy); font-size: 1.05em; }
.nt-tp-info svg { width: 110px; height: 110px; }
@media (max-width: 520px) { .nt-tp-info { grid-template-columns: 1fr; justify-items: center; } }
/* schémas de Lewis */
.nt-lw { display: block; margin: 0.5em auto; max-width: 100%; height: auto; overflow: visible; }
.nt-lw .lw-b line, .nt-lw .lw-lp, .nt-lw .lw-at { transition: stroke .2s, fill .2s, opacity .2s; }
.nt-lw.lw-col .lw-b line { stroke: #D97706; }
.nt-lw.lw-col .lw-lp { stroke: #0284C7; }
.nt-lw .lw-at { cursor: pointer; }
.nt-lw .lw-at:focus { outline: none; }
.nt-lw .lw-at:focus-visible { outline: 2px solid var(--blue-lt); }
.nt-lewis svg.nt-lw { width: 340px; }
.nt-lw.lw-focus .lw-b line, .nt-lw.lw-focus .lw-lp, .nt-lw.lw-focus .lw-at { opacity: 0.25; }
.nt-lw.lw-focus .lw-sel, .nt-lw.lw-focus .lw-sel line { opacity: 1 !important; stroke-width: 2.6; }
.nt-lw.lw-focus text.lw-sel { font-weight: 700; fill: var(--blue); }
.nt-lw-leg { display: flex; justify-content: center; gap: 1.2em; font-size: 0.85em; flex-wrap: wrap; }
.nt-lw-leg b { font-weight: 600; }
.nt-cand { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin: 0.6em 0; }
@media (max-width: 560px) { .nt-cand { grid-template-columns: 1fr; } }
.nt-cand button { display: flex; flex-direction: column; align-items: center; justify-content: flex-start; border: 1.5px solid var(--line); border-radius: 12px; background: #FFFFFF; padding: 0.4em 0.4em 0.6em; cursor: pointer; font: inherit; color: var(--ink); transition: box-shadow .15s, border-color .15s; }
.nt-cand button:hover { box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15); }
.nt-cand button.ok { border-color: #16A34A; background: #F0FDF4; }
.nt-cand button.ko { border-color: #E11D48; background: #FFF1F2; }
.nt-cand button .nt-lw { margin: 0.2em auto; }
.nt-cand .nt-cand-t { font-weight: 700; color: var(--navy); font-size: 0.9em; }
.nt-lw text.lw-bad { fill: #E11D48; font-weight: 700; }
.nt-lw text.lw-good { fill: #16A34A; font-weight: 700; }
.nt-lab .nt-msg.nt-ion-msg { font-size: 1.04em; line-height: 1.85; color: var(--ink); max-width: 640px; margin: 0.9em auto 0 !important; padding: 0.7em 1.1em; border-radius: 12px; background: var(--slate-bg); border: 1px solid var(--line); }
.nt-ion-msg .nt-cfg { font-size: 1.12em; }
.nt-orb { display: block; width: 100%; margin: 0.6em 0 0.2em; }
.nt-picker { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.35em; margin: 0.4em 0; }
.nt-picker .nt-btn { font-family: Georgia, "Times New Roman", serif; font-weight: 600; min-width: 2.8em; }
.nt-picker .nt-btn[aria-pressed="true"] { background: var(--blue); color: #fff; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Pourquoi le sodium et le potassium réagissent-ils de la même façon avec l'eau&nbsp;? Pourquoi l'hélium, le néon ou l'argon ne réagissent-ils presque avec rien&nbsp;? Pourquoi l'oxygène forme-t-il deux liaisons et le carbone quatre&nbsp;? Toutes ces questions trouvent leur réponse dans la façon dont les <b>électrons</b> se répartissent autour du noyau.</p>

## Cortège électronique {.nt-h2}

### Couches et sous-couches {.nt-h3}

<p>L'atome de noyau $\ce{_ZX}$ possède $Z$ électrons.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Les $Z$ électrons d'un atome forment le <span class="imp nt-hole">cortège électronique</span>. Ils se répartissent en <span class="imp nt-hole">couches</span> concentriques autour du noyau, numérotées par le <span class="imp nt-hole">nombre quantique principal</span> $n$ ($n = 1$, $2$, $3$…).</p>
<p>Ces couches sont elles-mêmes divisées en <span class="imp nt-hole">sous-couches</span> notées $\text{s}$, $\text{p}$, $\text{d}$ et $\text{f}$.</p>
</div>

<p>En seconde, on se limite aux 18&nbsp;premiers éléments ($Z \leqslant 18$)&nbsp;: seules les sous-couches $\text{s}$ et $\text{p}$ sont alors occupées. La couche $n = 1$ ne contient qu'une sous-couche, notée $1\text{s}$&nbsp;; les couches $n = 2$ et $n = 3$ contiennent chacune une sous-couche $\text{s}$ et une sous-couche $\text{p}$ (la couche $n = 3$ contient aussi une sous-couche $3\text{d}$, qui n'est pas utilisée pour $Z \leqslant 18$).</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Une sous-couche <span class="imp nt-hole">s</span> est saturée lorsqu'elle contient <span class="imp nt-hole">2&nbsp;électrons</span>.</p>
<p>Une sous-couche <span class="imp nt-hole">p</span> est saturée lorsqu'elle contient <span class="imp nt-hole">6&nbsp;électrons</span>.</p>
<p>Pour obtenir la configuration la plus stable (dite à l'<b>état fondamental</b>), les sous-couches se remplissent dans l'ordre&nbsp;:</p>
<p class="nt-big"><span class="imp nt-hole">$1\text{s} \rightarrow 2\text{s} \rightarrow 2\text{p} \rightarrow 3\text{s} \rightarrow 3\text{p}$</span></p>
</div>

<div class="nt-lab" id="lab-remp">
<p class="nt-tag"><i class="fa-solid fa-atom"></i>Animation</p>
<p class="nt-lab-title">Remplir le cortège électronique, électron par électron</p>
<canvas role="img" aria-label="À gauche, l'atome avec son noyau et ses couches ; à droite, les sous-couches dans l'ordre de remplissage, avec leurs places libres et occupées."></canvas>
<p class="nt-remp-out" aria-live="polite"></p>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="moins"><i class="fa-solid fa-minus"></i>&nbsp; Retirer un électron</button><button type="button" class="nt-btn nt-btn-main" data-act="plus"><i class="fa-solid fa-plus"></i>&nbsp; Ajouter un électron</button></div>
<div class="nt-ctrls"><label class="nt-ctrl">Numéro atomique&nbsp;: <b class="out-z"></b><input type="range" min="1" max="18" step="1" value="6" data-in="z"></label></div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="val"> Montrer les électrons de valence</label></div>
</div>
<p class="nt-cap">Chaque électron ajouté prend la première place libre, dans l'ordre 1s, 2s, 2p, 3s, 3p&nbsp;: une sous-couche n'est entamée que lorsque la précédente est pleine.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les électrons tournent-ils vraiment sur des cercles&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Non&nbsp;: le dessin en cercles concentriques est une image commode, héritée du modèle de Bohr (1913). En mécanique quantique, un électron n'a pas de trajectoire&nbsp;; on sait seulement calculer où il a le plus de chances de se trouver. Une couche correspond à une zone où les électrons sont, en moyenne, à peu près à la même distance du noyau, et d'autant plus loin que $n$ est grand. Les sous-couches $\text{s}$ et $\text{p}$ correspondent à des zones de présence de formes différentes (sphérique pour $\text{s}$, en haltères pour $\text{p}$).</p>
<canvas class="nt-orb" role="img" aria-label="Zones de présence de l'électron de l'atome d'hydrogène pour les orbitales 1s, 2s, 2p et 3d, vues en coupe : une sphère pour 1s, une sphère entourée d'une couronne pour 2s, deux lobes pour 2p, deux lobes et un anneau pour 3d."></canvas>
<p class="nt-cap">Zones de présence de l'électron de l'atome d'hydrogène, vues en coupe et à la même échelle (calculées avec l'équation de Schrödinger). Plus la couleur est intense, plus l'électron a de chances de s'y trouver. Les deux couleurs distinguent des parties de l'orbitale de «&nbsp;signes&nbsp;» opposés, une notion qui dépasse le lycée.</p>
<p>L'ordre de remplissage ne suit d'ailleurs pas toujours l'ordre des couches&nbsp;: à partir de $Z = 19$ (potassium), la sous-couche $4\text{s}$ se remplit avant la $3\text{d}$.</p>
</div>
</details>

### Configuration électronique {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp nt-hole">configuration électronique</span> d'un atome est la répartition de ses électrons dans les différentes <span class="imp nt-hole">couches</span> et <span class="imp nt-hole">sous-couches</span>.</p>
</div>

<p>On l'écrit en indiquant chaque sous-couche occupée, avec en exposant son nombre d'électrons.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>La configuration électronique de l'atome de sodium (numéro atomique $Z = 11$) à l'état fondamental est $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^1$&nbsp;: 2 + 2 + 6 + 1 = 11 électrons. Cette configuration permet de retrouver la position de l'élément sodium dans le tableau périodique&nbsp;: il se situe dans la <b>3<sup>e</sup>&nbsp;période</b> et la <b>1<sup>re</sup>&nbsp;colonne du bloc s</b>, et par conséquent dans la <b>1<sup>re</sup>&nbsp;colonne du tableau</b>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Donner la configuration électronique du carbone ($Z = 6$), puis celle de l'aluminium ($Z = 13$).</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Remplir dans l'ordre jusqu'à avoir placé tous les électrons</span></summary>
<div class="nt-d-body">
<p>Carbone, 6&nbsp;électrons&nbsp;: 2 dans $1\text{s}$, 2 dans $2\text{s}$, il en reste 2 pour $2\text{p}$, d'où $1\text{s}^2\,2\text{s}^2\,2\text{p}^2$.</p>
<p>Aluminium, 13&nbsp;électrons&nbsp;: $1\text{s}^2\,2\text{s}^2\,2\text{p}^6$ en contient déjà 10&nbsp;; il en reste 3, dont 2 dans $3\text{s}$ et 1 dans $3\text{p}$, d'où $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^1$.</p>
<p>Pour vérifier, on additionne les exposants&nbsp;: on doit retrouver $Z$.</p>
</div>
</details>

<div class="nt-lab nt-trainer" id="tr-config">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Écrire une configuration électronique</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<div class="nt-qvis" aria-live="polite"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-ans"><span class="nt-champ"><label for="trc-rep">Configuration&nbsp;:</label><input id="trc-rep" class="nt-large" type="text" autocomplete="off" spellcheck="false" placeholder="par exemple 1s2 2s2…"></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
<p class="nt-center nt-note nt-tr-prev" aria-live="polite"></p>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>
<p class="nt-cap">Tapez les exposants comme des chiffres ordinaires, par exemple <code>1s2 2s2 2p3</code>&nbsp;: l'aperçu les affiche en exposant.</p>

### Configuration électronique et tableau périodique {.nt-h3}

<p>On obtient ainsi les configurations électroniques des 18&nbsp;premiers éléments. Cliquez sur un élément pour l'examiner en détail.</p>

<div class="nt-lab nt-tp" id="tp-config" data-modes="config,blocs">
<p class="nt-tag"><i class="fa-solid fa-table-cells"></i>Tableau interactif</p>
<p class="nt-lab-title">Configurations électroniques des 18 premiers éléments</p>
<div class="nt-tp-zone"></div>
</div>

<p>Selon la sous-couche en cours de remplissage, $\text{s}$ ou $\text{p}$, on fait apparaître deux <span class="imp">blocs</span> dans ce début de tableau périodique (mode «&nbsp;Blocs&nbsp;» ci-dessus). L'hélium, de configuration $1\text{s}^2$, appartient au bloc $\text{s}$, mais il est placé à droite, avec les autres gaz nobles (nous verrons pourquoi plus bas).</p>

<p>Si l'on étend au tableau entier, on voit apparaître les deux autres blocs, associés aux sous-couches $\text{d}$ et $\text{f}$.</p>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 686 410' role='img' aria-label="Tableau périodique complet des 118 éléments, coloré selon les blocs s, p, d et f ; les 18 premiers éléments sont entourés."><text x='47' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>1</text><text x='83' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>2</text><text x='119' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>3</text><text x='155' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>4</text><text x='191' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>5</text><text x='227' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>6</text><text x='263' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>7</text><text x='299' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>8</text><text x='335' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>9</text><text x='371' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>10</text><text x='407' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>11</text><text x='443' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>12</text><text x='479' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>13</text><text x='515' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>14</text><text x='551' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>15</text><text x='587' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>16</text><text x='623' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>17</text><text x='659' y='26' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>18</text><text x='20' y='54.5' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>1</text><text x='20' y='90.5' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>2</text><text x='20' y='126.5' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>3</text><text x='20' y='162.5' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>4</text><text x='20' y='198.5' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>5</text><text x='20' y='234.5' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>6</text><text x='20' y='270.5' font-size='10' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>7</text><rect x='30' y='34' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='33' y='43' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>1</text><text x='47' y='57' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>H</text><rect x='642' y='34' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='645' y='43' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>2</text><text x='659' y='57' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>He</text><rect x='30' y='70' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='33' y='79' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>3</text><text x='47' y='93' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Li</text><rect x='66' y='70' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='69' y='79' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>4</text><text x='83' y='93' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Be</text><rect x='462' y='70' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='79' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>5</text><text x='479' y='93' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>B</text><rect x='498' y='70' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='79' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>6</text><text x='515' y='93' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>C</text><rect x='534' y='70' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='79' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>7</text><text x='551' y='93' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>N</text><rect x='570' y='70' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='79' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>8</text><text x='587' y='93' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>O</text><rect x='606' y='70' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='609' y='79' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>9</text><text x='623' y='93' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>F</text><rect x='642' y='70' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='645' y='79' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>10</text><text x='659' y='93' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ne</text><rect x='30' y='106' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='33' y='115' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>11</text><text x='47' y='129' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Na</text><rect x='66' y='106' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='69' y='115' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>12</text><text x='83' y='129' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Mg</text><rect x='462' y='106' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='115' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>13</text><text x='479' y='129' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Al</text><rect x='498' y='106' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='115' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>14</text><text x='515' y='129' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Si</text><rect x='534' y='106' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='115' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>15</text><text x='551' y='129' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>P</text><rect x='570' y='106' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='115' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>16</text><text x='587' y='129' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>S</text><rect x='606' y='106' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='609' y='115' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>17</text><text x='623' y='129' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cl</text><rect x='642' y='106' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='645' y='115' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>18</text><text x='659' y='129' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ar</text><rect x='30' y='142' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='33' y='151' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>19</text><text x='47' y='165' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>K</text><rect x='66' y='142' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='69' y='151' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>20</text><text x='83' y='165' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ca</text><rect x='102' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='105' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>21</text><text x='119' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Sc</text><rect x='138' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='141' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>22</text><text x='155' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ti</text><rect x='174' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='177' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>23</text><text x='191' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>V</text><rect x='210' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='213' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>24</text><text x='227' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cr</text><rect x='246' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='249' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>25</text><text x='263' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Mn</text><rect x='282' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='285' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>26</text><text x='299' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Fe</text><rect x='318' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='321' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>27</text><text x='335' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Co</text><rect x='354' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='357' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>28</text><text x='371' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ni</text><rect x='390' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='393' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>29</text><text x='407' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cu</text><rect x='426' y='142' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='429' y='151' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>30</text><text x='443' y='165' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Zn</text><rect x='462' y='142' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='151' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>31</text><text x='479' y='165' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ga</text><rect x='498' y='142' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='151' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>32</text><text x='515' y='165' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ge</text><rect x='534' y='142' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='151' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>33</text><text x='551' y='165' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>As</text><rect x='570' y='142' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='151' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>34</text><text x='587' y='165' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Se</text><rect x='606' y='142' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='609' y='151' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>35</text><text x='623' y='165' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Br</text><rect x='642' y='142' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='645' y='151' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>36</text><text x='659' y='165' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Kr</text><rect x='30' y='178' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='33' y='187' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>37</text><text x='47' y='201' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Rb</text><rect x='66' y='178' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='69' y='187' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>38</text><text x='83' y='201' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Sr</text><rect x='102' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='105' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>39</text><text x='119' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Y</text><rect x='138' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='141' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>40</text><text x='155' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Zr</text><rect x='174' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='177' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>41</text><text x='191' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Nb</text><rect x='210' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='213' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>42</text><text x='227' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Mo</text><rect x='246' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='249' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>43</text><text x='263' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Tc</text><rect x='282' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='285' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>44</text><text x='299' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ru</text><rect x='318' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='321' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>45</text><text x='335' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Rh</text><rect x='354' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='357' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>46</text><text x='371' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Pd</text><rect x='390' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='393' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>47</text><text x='407' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ag</text><rect x='426' y='178' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='429' y='187' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>48</text><text x='443' y='201' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cd</text><rect x='462' y='178' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='187' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>49</text><text x='479' y='201' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>In</text><rect x='498' y='178' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='187' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>50</text><text x='515' y='201' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Sn</text><rect x='534' y='178' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='187' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>51</text><text x='551' y='201' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Sb</text><rect x='570' y='178' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='187' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>52</text><text x='587' y='201' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Te</text><rect x='606' y='178' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='609' y='187' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>53</text><text x='623' y='201' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>I</text><rect x='642' y='178' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='645' y='187' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>54</text><text x='659' y='201' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Xe</text><rect x='30' y='214' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='33' y='223' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>55</text><text x='47' y='237' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cs</text><rect x='66' y='214' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='69' y='223' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>56</text><text x='83' y='237' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ba</text><rect x='102' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='105' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>57</text><text x='119' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>La</text><rect x='138' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='141' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>58</text><text x='155' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ce</text><rect x='174' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='177' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>59</text><text x='191' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Pr</text><rect x='210' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='213' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>60</text><text x='227' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Nd</text><rect x='246' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='249' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>61</text><text x='263' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Pm</text><rect x='282' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='285' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>62</text><text x='299' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Sm</text><rect x='318' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='321' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>63</text><text x='335' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Eu</text><rect x='354' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='357' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>64</text><text x='371' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Gd</text><rect x='390' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='393' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>65</text><text x='407' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Tb</text><rect x='426' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='429' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>66</text><text x='443' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Dy</text><rect x='462' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>67</text><text x='479' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ho</text><rect x='498' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>68</text><text x='515' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Er</text><rect x='534' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>69</text><text x='551' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Tm</text><rect x='570' y='300' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='309' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>70</text><text x='587' y='323' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Yb</text><rect x='102' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='105' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>71</text><text x='119' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Lu</text><rect x='138' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='141' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>72</text><text x='155' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Hf</text><rect x='174' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='177' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>73</text><text x='191' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ta</text><rect x='210' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='213' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>74</text><text x='227' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>W</text><rect x='246' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='249' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>75</text><text x='263' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Re</text><rect x='282' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='285' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>76</text><text x='299' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Os</text><rect x='318' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='321' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>77</text><text x='335' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ir</text><rect x='354' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='357' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>78</text><text x='371' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Pt</text><rect x='390' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='393' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>79</text><text x='407' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Au</text><rect x='426' y='214' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='429' y='223' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>80</text><text x='443' y='237' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Hg</text><rect x='462' y='214' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='223' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>81</text><text x='479' y='237' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Tl</text><rect x='498' y='214' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='223' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>82</text><text x='515' y='237' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Pb</text><rect x='534' y='214' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='223' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>83</text><text x='551' y='237' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Bi</text><rect x='570' y='214' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='223' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>84</text><text x='587' y='237' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Po</text><rect x='606' y='214' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='609' y='223' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>85</text><text x='623' y='237' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>At</text><rect x='642' y='214' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='645' y='223' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>86</text><text x='659' y='237' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Rn</text><rect x='30' y='250' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='33' y='259' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>87</text><text x='47' y='273' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Fr</text><rect x='66' y='250' width='34' height='34' rx='4' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.35' stroke-width='0.8'/><text x='69' y='259' font-size='7' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>88</text><text x='83' y='273' font-size='12.5' text-anchor='middle' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ra</text><rect x='102' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='105' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>89</text><text x='119' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ac</text><rect x='138' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='141' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>90</text><text x='155' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Th</text><rect x='174' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='177' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>91</text><text x='191' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Pa</text><rect x='210' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='213' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>92</text><text x='227' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>U</text><rect x='246' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='249' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>93</text><text x='263' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Np</text><rect x='282' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='285' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>94</text><text x='299' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Pu</text><rect x='318' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='321' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>95</text><text x='335' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Am</text><rect x='354' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='357' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>96</text><text x='371' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cm</text><rect x='390' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='393' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>97</text><text x='407' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Bk</text><rect x='426' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='429' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>98</text><text x='443' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cf</text><rect x='462' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>99</text><text x='479' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Es</text><rect x='498' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>100</text><text x='515' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Fm</text><rect x='534' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>101</text><text x='551' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Md</text><rect x='570' y='336' width='34' height='34' rx='4' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='345' font-size='7' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>102</text><text x='587' y='359' font-size='12.5' text-anchor='middle' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>No</text><rect x='102' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='105' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>103</text><text x='119' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Lr</text><rect x='138' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='141' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>104</text><text x='155' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Rf</text><rect x='174' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='177' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>105</text><text x='191' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Db</text><rect x='210' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='213' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>106</text><text x='227' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Sg</text><rect x='246' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='249' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>107</text><text x='263' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Bh</text><rect x='282' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='285' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>108</text><text x='299' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Hs</text><rect x='318' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='321' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>109</text><text x='335' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Mt</text><rect x='354' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='357' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>110</text><text x='371' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ds</text><rect x='390' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='393' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>111</text><text x='407' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Rg</text><rect x='426' y='250' width='34' height='34' rx='4' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.35' stroke-width='0.8'/><text x='429' y='259' font-size='7' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>112</text><text x='443' y='273' font-size='12.5' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Cn</text><rect x='462' y='250' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='465' y='259' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>113</text><text x='479' y='273' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Nh</text><rect x='498' y='250' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='501' y='259' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>114</text><text x='515' y='273' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Fl</text><rect x='534' y='250' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='537' y='259' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>115</text><text x='551' y='273' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Mc</text><rect x='570' y='250' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='573' y='259' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>116</text><text x='587' y='273' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Lv</text><rect x='606' y='250' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='609' y='259' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>117</text><text x='623' y='273' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Ts</text><rect x='642' y='250' width='34' height='34' rx='4' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.35' stroke-width='0.8'/><text x='645' y='259' font-size='7' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>118</text><text x='659' y='273' font-size='12.5' text-anchor='middle' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>Og</text><path d='M27,31 H103 V67 H459 V31 H679 V143 H27 Z' fill='none' stroke='#1E293B' stroke-width='1.3' stroke-dasharray='5 3'/><rect x='30' y='385' width='16' height='16' rx='3' fill='#FEF3C7' stroke='#B45309' stroke-opacity='0.5'/><text x='52' y='397' font-size='12' fill='#B45309' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>bloc s</text><rect x='130' y='385' width='16' height='16' rx='3' fill='#D1FAE5' stroke='#047857' stroke-opacity='0.5'/><text x='152' y='397' font-size='12' fill='#047857' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>bloc p</text><rect x='230' y='385' width='16' height='16' rx='3' fill='#E0F2FE' stroke='#0369A1' stroke-opacity='0.5'/><text x='252' y='397' font-size='12' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>bloc d</text><rect x='330' y='385' width='16' height='16' rx='3' fill='#FCE7F3' stroke='#BE185D' stroke-opacity='0.5'/><text x='352' y='397' font-size='12' fill='#BE185D' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>bloc f</text><path d='M440,393 h22' stroke='#1E293B' stroke-width='1.3' stroke-dasharray='5 3'/><text x='468' y='397' font-size='12' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>les 18 premiers éléments</text></svg></div>
<p class="nt-cap">Le tableau périodique complet (118 éléments), coloré selon les blocs. Le bloc $\text{f}$ est placé sous le tableau pour qu'il ne soit pas trop large.</p>

### Électrons de valence {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Les <span class="imp nt-hole">électrons de valence</span> sont les électrons appartenant à la couche de nombre quantique principal $n$ <span class="imp nt-hole">le plus élevé</span>, ainsi que les électrons appartenant à des sous-couches partiellement remplies.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<p>L'atome de sodium a un électron de valence à l'état fondamental, l'électron appartenant à la sous-couche $3\text{s}$&nbsp;: $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,{\color{#2A6BC4}{3\text{s}^1}}$.</p>
<p>L'atome de soufre ($Z = 16$) en a six, ceux des sous-couches $3\text{s}$ et $3\text{p}$&nbsp;: $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,{\color{#2A6BC4}{3\text{s}^2\,3\text{p}^4}}$.</p>
</div>

<p>Les électrons de valence sont ainsi les électrons les plus périphériques. C'est à travers eux qu'un atome interagit avec d'autres entités&nbsp;: ils sont donc responsables de ses <b>propriétés chimiques</b>. Les autres électrons, plus proches du noyau, sont appelés <b>électrons de cœur</b>.</p>

<div class="nt-lab nt-tp" id="tp-valence" data-modes="valence,familles">
<p class="nt-tag"><i class="fa-solid fa-table-cells"></i>Tableau interactif</p>
<p class="nt-lab-title">Électrons de valence et familles chimiques</p>
<div class="nt-tp-zone"></div>
</div>

<p>Cela explique la «&nbsp;périodicité&nbsp;» du tableau périodique&nbsp;: sont placés dans une même colonne des éléments ayant la même configuration électronique de leurs <span class="imp">électrons de valence</span> (au numéro de la couche près).</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp nt-hole">famille chimique</span> est un ensemble d'éléments chimiques appartenant à une <span class="imp nt-hole">même colonne</span> du tableau périodique et partageant des <span class="imp nt-hole">propriétés chimiques et physiques similaires</span>.</p>
<p>La similarité des propriétés observées à l'échelle macroscopique est associée, à l'échelle microscopique, à l'identité des configurations électroniques de valence des atomes isolés de ces éléments.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple&nbsp;: la famille des alcalins</p>
<p>Le lithium, le sodium, le potassium, etc. ont en commun une configuration électronique fondamentale de l'atome isolé du type $n\text{s}^1$. Ils constituent la famille des <b>alcalins</b> (ou métaux alcalins), placés dans la 1<sup>re</sup>&nbsp;colonne. L'hydrogène, bien que placé dans cette colonne, n'en fait pas partie&nbsp;: c'est un gaz, aux propriétés très différentes.</p>
<ul class="nt-facts">
<li><b>Des métaux étonnants</b>&nbsp;: ils sont si mous qu'on les coupe au couteau, et si légers que le lithium, le sodium et le potassium flottent sur l'eau. Brillants quand on vient de les couper, ils se ternissent en quelques secondes à l'air.</li>
<li><b>Très réactifs</b>&nbsp;: on les conserve dans l'huile, à l'abri de l'air et de l'humidité. Au contact de l'eau, ils réagissent vivement en dégageant un gaz inflammable, le dihydrogène, et la réaction est de plus en plus violente quand on descend dans la colonne.</li>
<li><b>Jamais purs dans la nature</b>&nbsp;: on les trouve sous forme d'ions, par exemple dans le sel de cuisine (chlorure de sodium) ou dans les engrais (sels de potassium).</li>
<li><b>Des flammes colorées</b>&nbsp;: ils colorent les flammes en rouge (lithium), en jaune-orangé (sodium, la couleur des anciens lampadaires) ou en violet (potassium), ce qu'on utilise dans les feux d'artifice.</li>
<li><b>Utiles au quotidien</b>&nbsp;: le lithium est au cœur des batteries des téléphones et des voitures électriques&nbsp;; les ions sodium et potassium sont indispensables au fonctionnement de nos nerfs et de nos muscles.</li>
</ul>
</div>


{{< youtube-plus id="uixxJtJPVXk" ratio="4x3" width="500" shadow=true rounded=true >}}

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple&nbsp;: la famille des halogènes</p>
<p>L'avant-dernière colonne, la 17<sup>e</sup>, juste avant la 18<sup>e</sup> des gaz nobles, correspond à la famille des <b>halogènes</b> (fluor, chlore, brome, iode…), de configuration de valence $n\text{s}^2\,n\text{p}^5$. Leur nom vient du grec et signifie «&nbsp;qui forme des sels&nbsp;».</p>
<ul class="nt-facts">
<li><b>Des aspects très variés</b>&nbsp;: le fluor est un gaz jaune pâle, le chlore un gaz jaune-vert, le brome l'un des rares liquides parmi les éléments (rouge-brun), et l'iode un solide gris-noir qui donne des vapeurs violettes. Ils existent sous forme de molécules à deux atomes&nbsp;: $\ce{F2}$, $\ce{Cl2}$, $\ce{Br2}$, $\ce{I2}$.</li>
<li><b>Très réactifs et dangereux</b>&nbsp;: ils sont toxiques et irritants&nbsp;; le fluor est même l'élément le plus réactif de tous. Le dichlore a malheureusement servi d'arme chimique pendant la Première Guerre mondiale.</li>
<li><b>Jamais purs dans la nature</b>&nbsp;: on les trouve sous forme d'ions, comme l'ion chlorure dans le sel de cuisine et dans l'eau de mer.</li>
<li><b>Utiles au quotidien</b>&nbsp;: le chlore désinfecte l'eau du robinet et des piscines (c'est aussi le principe de l'eau de Javel), l'iode sert d'antiseptique pour les plaies, et les fluorures protègent les dents contre les caries dans les dentifrices.</li>
</ul>
</div>

{{< youtube-plus id="u2ogMUDBaf4" ratio="4x3" width="500" shadow=true rounded=true >}}


<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>La grande réactivité de ces deux familles s'explique par la proximité des gaz nobles, comme nous allons le voir dans la suite&nbsp;: les alcalins n'ont qu'un électron de plus que le gaz noble qui les précède, et il ne manque qu'un électron aux halogènes pour avoir la configuration du gaz noble qui les suit.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: écriture condensée</p>
<p>On peut condenser l'écriture d'une configuration électronique en écrivant seulement la configuration des électrons de valence, précédée du symbole, entre crochets, de l'élément ayant la configuration des électrons de cœur. Il s'agit toujours de l'élément de la dernière colonne (la famille des <span class="imp">gaz nobles</span>) qui précède.</p>
<p>Exemple&nbsp;: le soufre $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^4$ s'écrit $[\text{Ne}]\,3\text{s}^2\,3\text{p}^4$, car $1\text{s}^2\,2\text{s}^2\,2\text{p}^6$ est la configuration du néon.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Les <span class="imp nt-hole">lignes</span> du tableau périodique, appelées <span class="imp nt-hole">périodes</span>, correspondent au $n$ <span class="imp nt-hole">le plus élevé</span> parmi les sous-couches remplies ou en cours de remplissage.</p>
</div>

<div class="nt-lab nt-tp" id="tp-periodes" data-modes="condensee,periodes">
<p class="nt-tag"><i class="fa-solid fa-table-cells"></i>Tableau interactif</p>
<p class="nt-lab-title">Écriture condensée et périodes</p>
<div class="nt-tp-zone"></div>
</div>

<p>Une période commence ainsi toujours par un élément de configuration de valence $n\text{s}^1$ (le premier élément de la colonne des alcalins) et se termine par un gaz noble, dont toutes les sous-couches de valence sont pleines.</p>

### Trouver la place d'un élément {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour trouver l'emplacement d'un élément dans le tableau périodique ($Z \leqslant 18$) à partir de la configuration de ses électrons de valence&nbsp;:</p>
<ul class="nt-facts">
<li>le nombre <span class="imp nt-hole">$n$</span> de la couche de valence donne la <span class="imp nt-hole">ligne</span> (la période)&nbsp;;</li>
<li>si la configuration de valence est <span class="imp nt-hole">$n\text{s}^1$</span>, l'élément est dans la <span class="imp nt-hole">1<sup>re</sup>&nbsp;colonne</span>&nbsp;;</li>
<li>si elle est <span class="imp nt-hole">$n\text{s}^2$</span>, il est dans la <span class="imp nt-hole">2<sup>e</sup>&nbsp;colonne</span>, sauf si $n = 1$&nbsp;: c'est l'hélium, dans la 18<sup>e</sup>&nbsp;colonne&nbsp;;</li>
<li>si elle est <span class="imp nt-hole">$n\text{s}^2\,n\text{p}^i$</span>, le numéro de la colonne est <span class="imp nt-hole">$12 + i$</span>.</li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Placer l'élément dont la configuration électronique des électrons de valence est $2\text{s}^2$, puis celui dont la configuration de valence est $3\text{s}^2\,3\text{p}^4$.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Une ligne, une colonne</span></summary>
<div class="nt-d-body">
<p>$2\text{s}^2$&nbsp;: $n = 2$, donc 2<sup>e</sup>&nbsp;ligne&nbsp;; $\text{s}^{\textcolor{#D97706}{2}}$, donc ${\color{#D97706}{2}}$<sup>e</sup>&nbsp;colonne. C'est le béryllium ($1\text{s}^2\,2\text{s}^2$, $Z = 4$).</p>
<p>$3\text{s}^2\,3\text{p}^4$&nbsp;: $n = 3$, donc 3<sup>e</sup>&nbsp;ligne&nbsp;; $\text{p}^{\textcolor{#D97706}{4}}$, donc $12 + {\color{#D97706}{4}} = 16$<sup>e</sup>&nbsp;colonne. C'est le soufre ($Z = 16$).</p>
</div>
</details>

<div class="nt-lab nt-trainer" id="tr-place">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">De la configuration à la case, et réciproquement</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard nt-qcard-w">
<div class="nt-qvis" aria-live="polite"></div>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tp-zone"></div>
<div class="nt-tr-ans" hidden><span class="nt-champ"><label for="trp-rep">Valence&nbsp;:</label><input id="trp-rep" class="nt-large" type="text" autocomplete="off" spellcheck="false" placeholder="par exemple 2s2…"></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
<p class="nt-center nt-note nt-tr-prev" aria-live="polite"></p>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>

## Vers la stabilité {.nt-h2}

### La stabilité des gaz nobles {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Les configurations électroniques les plus stables sont celles des <span class="imp nt-hole">gaz nobles</span>, de la 18<sup>e</sup> et dernière colonne&nbsp;: leur couche de valence est <span class="imp nt-hole">saturée</span> (remplie).</p>
</div>

<div class="nt-lab nt-tp" id="tp-nobles" data-modes="nobles">
<p class="nt-tag"><i class="fa-solid fa-table-cells"></i>Tableau interactif</p>
<p class="nt-lab-title">Les gaz nobles et leur couche de valence pleine</p>
<div class="nt-tp-zone"></div>
</div>

<p>C'est d'ailleurs ce qui explique la position décalée de l'hélium&nbsp;: sa couche $n = 1$ saturée lui confère une grande stabilité, qui l'apparente aux autres gaz nobles. Les gaz nobles (hélium, néon, argon…) ne réagissent pratiquement avec aucune autre espèce chimique&nbsp;: on les trouve dans l'air sous forme d'atomes isolés.</p>

<p>Les autres atomes ont tendance à évoluer vers une configuration électronique plus stable, celle du gaz noble le plus proche d'eux dans le tableau périodique. Comment&nbsp;?</p>
<ul class="nt-facts">
<li>en perdant ou en gagnant des électrons, pour devenir des <span class="imp">ions monoatomiques</span>&nbsp;;</li>
<li>en mettant en commun des électrons avec d'autres atomes, par la formation de <span class="imp">liaisons covalentes</span>, et bâtir ainsi des édifices polyatomiques, les <span class="imp">molécules</span>.</li>
</ul>

### Formation d'ions monoatomiques {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Quels éléments vont avoir tendance à gagner des électrons, ceux qui précèdent ou ceux qui suivent les gaz nobles&nbsp;? Quel type d'ions formeront-ils&nbsp;?</p>
<p>Et quels éléments vont avoir tendance à perdre des électrons&nbsp;? Pour former quel type d'ions&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Le chemin le plus court vers le gaz noble</span></summary>
<div class="nt-d-body">
<p>Les éléments qui <b>précèdent</b> un gaz noble (colonnes 16 et 17) n'ont besoin que de 2 ou 1&nbsp;électron(s) de plus pour atteindre sa configuration&nbsp;: ils ont tendance à <b>gagner</b> des électrons et à former des ions chargés négativement, des <b>anions</b>. Le chlore donne ainsi l'ion chlorure $\ce{Cl-}$, qui a la configuration de l'argon.</p>
<p>Les éléments qui <b>suivent</b> un gaz noble (colonnes 1 et 2, ainsi que l'aluminium dans la colonne 13) n'ont que 1, 2 ou 3&nbsp;électron(s) de valence&nbsp;: en les perdant, ils retrouvent la configuration du gaz noble précédent. Ils ont tendance à <b>perdre</b> des électrons et à former des ions chargés positivement, des <b>cations</b>. Le sodium donne ainsi l'ion sodium $\ce{Na+}$, qui a la configuration du néon.</p>
</div>
</details>

<div class="nt-lab" id="lab-ion">
<p class="nt-tag"><i class="fa-solid fa-atom"></i>Animation</p>
<p class="nt-lab-title">De l'atome à l'ion</p>
<div class="nt-picker" role="group" aria-label="Choix de l'élément"></div>
<canvas role="img" aria-label="Un atome avec ses couches d'électrons, qui perd ou gagne des électrons pour former un ion."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="ion"><i class="fa-solid fa-wand-magic-sparkles"></i>&nbsp; Former l'ion</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Revenir à l'atome</button></div>
<p class="nt-msg nt-ion-msg" aria-live="polite"></p>
</div>

<div class="nt-lab nt-tp" id="tp-ions" data-modes="ions">
<p class="nt-tag"><i class="fa-solid fa-table-cells"></i>Tableau interactif</p>
<p class="nt-lab-title">Les ions monoatomiques courants</p>
<div class="nt-tp-zone"></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La charge d'un ion monoatomique courant se déduit de la position de l'élément dans le tableau périodique&nbsp;:</p>
<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>colonne</th><th>1</th><th>2</th><th>16</th><th>17</th></tr></thead>
<tbody><tr><td>ion formé</td><td>$\ce{X+}$</td><td>$\ce{X^2+}$</td><td>$\ce{X^2-}$</td><td>$\ce{X-}$</td></tr></tbody>
</table></div>
<p>Ions à connaître&nbsp;: <span class="imp nt-hole">$\ce{H+}$</span> ion hydrogène, <span class="imp nt-hole">$\ce{Na+}$</span> ion sodium, <span class="imp nt-hole">$\ce{K+}$</span> ion potassium, <span class="imp nt-hole">$\ce{Ca^2+}$</span> ion calcium, <span class="imp nt-hole">$\ce{Mg^2+}$</span> ion magnésium, <span class="imp nt-hole">$\ce{Cl-}$</span> ion chlorure, <span class="imp nt-hole">$\ce{F-}$</span> ion fluorure.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarques</p>
<p>Les cations portent le nom de l'élément (ion sodium, ion calcium…)&nbsp;; les anions monoatomiques prennent la terminaison <b>-ure</b> (ion chlorure, ion fluorure, ion sulfure&nbsp;$\ce{S^2-}$), sauf l'oxygène, qui donne l'ion <b>oxyde</b>&nbsp;$\ce{O^2-}$.</p>
<p>L'ion hydrogène $\ce{H+}$ est un cas à part&nbsp;: en perdant son unique électron, l'atome d'hydrogène ne garde que son noyau, un simple proton, sans aucun électron.</p>
<p>Le potassium ($Z = 19$) et le calcium ($Z = 20$) suivent l'argon&nbsp;: leurs ions $\ce{K+}$ et $\ce{Ca^2+}$ ont la configuration de l'argon. L'aluminium, dans la colonne 13, forme aussi un ion courant, $\ce{Al^3+}$, en perdant ses 3&nbsp;électrons de valence.</p>
</div>

<div class="nt-lab nt-quizlab" id="quiz-ions">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Nommer les ions, écrire leur formule</p>
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

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>L'ion $\ce{X^2-}$ a pour configuration électronique $1\text{s}^2\,2\text{s}^2\,2\text{p}^6$. Déterminer le nom et le symbole de cet ion grâce au tableau périodique.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Retirer les électrons gagnés</span></summary>
<div class="nt-d-body">
<p>L'ion possède $2 + 2 + 6 = 10$&nbsp;électrons. Un anion doublement chargé a 2&nbsp;électrons de plus que l'atome&nbsp;: l'atome $\ce{X}$ possède donc 8&nbsp;électrons, d'où $Z = 8$&nbsp;: c'est l'oxygène. Il s'agit de l'ion oxyde $\ce{O^2-}$, qui a la configuration électronique du néon.</p>
</div>
</details>

### La formation de liaisons covalentes {.nt-h3}

<p>Deuxième façon d'acquérir la configuration électronique du gaz noble le plus proche&nbsp;: mettre des électrons en commun.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Si deux atomes mettent en commun chacun un de leurs électrons de valence, ils forment une <span class="imp nt-hole">liaison covalente</span>&nbsp;: les deux électrons mis en commun forment un <span class="imp nt-hole">doublet liant</span>, qui appartient aux deux atomes à la fois.</p>
</div>

<p>Résultat&nbsp;: chaque atome compte désormais dans son entourage l'électron apporté par l'autre, en plus du sien. Tout se passe comme si chacun des deux atomes avait gagné un électron sur sa couche de valence, alors qu'aucun électron n'a quitté l'autre atome&nbsp;: les deux électrons sont partagés.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Quels éléments vont le plus avoir tendance à former des liaisons covalentes&nbsp;? Ceux qui précèdent ou ceux qui suivent les gaz nobles&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Ceux à qui il manque des électrons</span></summary>
<div class="nt-d-body">
<p>Une liaison covalente fait «&nbsp;gagner&nbsp;» un électron à chacun des deux atomes liés. Elle profite donc aux éléments à qui il <b>manque</b> des électrons pour atteindre la configuration du gaz noble suivant, c'est-à-dire ceux qui <b>précèdent</b> les gaz nobles (colonnes 14 à 17), ainsi qu'à l'hydrogène, à qui il manque un électron pour avoir la configuration de l'hélium.</p>
<p>Le nombre de liaisons qu'un atome forme est égal au nombre d'électrons qui lui manquent&nbsp;: 4 pour le carbone (colonne 14), 3 pour l'azote, 2 pour l'oxygène, 1 pour le chlore et pour l'hydrogène.</p>
</div>
</details>

<div class="nt-lab nt-tp" id="tp-liaisons" data-modes="liaisons">
<p class="nt-tag"><i class="fa-solid fa-table-cells"></i>Tableau interactif</p>
<p class="nt-lab-title">Nombre de liaisons covalentes formées</p>
<div class="nt-tp-zone"></div>
</div>

### Schéma de Lewis d'une molécule {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Dans le <span class="imp nt-hole">schéma de Lewis</span> d'une molécule, on représente tous les <span class="imp nt-hole">électrons de valence</span> de tous les atomes qui la constituent. Ces électrons s'organisent&nbsp;:</p>
<ul class="nt-facts">
<li>en <span class="imp nt-hole">doublets liants</span>, appartenant aux deux atomes liés&nbsp;: ils représentent les liaisons covalentes&nbsp;;</li>
<li>en <span class="imp nt-hole">doublets non liants</span>, appartenant uniquement à l'atome sur lequel ils sont situés.</li>
</ul>
<p>Chaque doublet, liant ou non liant, est représenté par un trait et contient <b>2&nbsp;électrons</b>.</p>
</div>

<p>Vérifions, sur le schéma de Lewis ci-dessous, qu'on retrouve bien tous les électrons de valence apportés par les 6&nbsp;atomes.</p>

<div class="nt-lab nt-lewis" id="lab-lewis1">
<p class="nt-tag"><i class="fa-solid fa-diagram-project"></i>Schéma interactif</p>
<p class="nt-lab-title">Une molécule à six atomes&nbsp;: $\ce{CH3FO}$</p>
<svg class='nt-lw' viewBox='0 0 242 188' width='242' role='img' aria-label="Schéma de Lewis de la molécule de formule brute CH3FO : le carbone est lié au fluor, à deux hydrogènes et à l'oxygène, lui-même lié à un hydrogène ; le fluor porte trois doublets non liants, l'oxygène deux."><g class='lw-b' data-a='F' data-b='C' data-o='1'><line x1='52.4' y1='94.0' x2='81.6' y2='94.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='H1' data-o='1'><line x1='94.0' y1='81.6' x2='94.0' y2='52.4' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='H2' data-o='1'><line x1='94.0' y1='106.4' x2='94.0' y2='135.6' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O' data-o='1'><line x1='106.4' y1='94.0' x2='135.6' y2='94.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='O' data-b='H3' data-o='1'><line x1='160.4' y1='94.0' x2='189.6' y2='94.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><text class='lw-at' data-at='F' x='40.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>F</text><line class='lw-lp' data-at='F' x1='46.0' y1='110.0' x2='34.0' y2='110.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='F' x1='24.0' y1='100.0' x2='24.0' y2='88.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='F' x1='34.0' y1='78.0' x2='46.0' y2='78.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='C' x='94.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>C</text><text class='lw-at' data-at='H1' x='94.0' y='47.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text><text class='lw-at' data-at='H2' x='94.0' y='155.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text><text class='lw-at' data-at='O' x='148.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>O</text><line class='lw-lp' data-at='O' x1='154.0' y1='110.0' x2='142.0' y2='110.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='O' x1='142.0' y1='78.0' x2='154.0' y2='78.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='H3' x='202.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text></svg>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="colorer"><i class="fa-solid fa-palette"></i>&nbsp; Colorer les doublets</button></div>
<p class="nt-msg" aria-live="polite">Cliquez sur un atome pour voir les doublets qui l'entourent.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<ol class="nt-steps">
<li><p>Donner la configuration électronique de chaque élément et repérer ses électrons de valence.</p></li>
<li><p>Quel est le nombre d'électrons de valence apportés par les atomes de cette molécule&nbsp;?</p></li>
<li><p>Chaque doublet, liant ou non liant, représente deux électrons. Combien d'électrons sont représentés dans ce schéma de Lewis&nbsp;? Le compte est-il bon&nbsp;?</p></li>
</ol>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">20 électrons de valence, 10 doublets</span></summary>
<div class="nt-d-body">
<p>Configurations électroniques (électrons de valence en couleur)&nbsp;:</p>
<ul class="nt-facts">
<li>H&nbsp;: ${\color{#2A6BC4}{1\text{s}^1}}$, soit 1 électron de valence&nbsp;;</li>
<li>C&nbsp;: $1\text{s}^2\,{\color{#2A6BC4}{2\text{s}^2\,2\text{p}^2}}$, soit 4&nbsp;;</li>
<li>O&nbsp;: $1\text{s}^2\,{\color{#2A6BC4}{2\text{s}^2\,2\text{p}^4}}$, soit 6&nbsp;;</li>
<li>F&nbsp;: $1\text{s}^2\,{\color{#2A6BC4}{2\text{s}^2\,2\text{p}^5}}$, soit 7.</li>
</ul>
<p>Cela fait $3 \times 1 + 4 + 6 + 7 = 20$&nbsp;électrons de valence.</p>
<p>Le schéma comporte 5&nbsp;doublets liants et 5&nbsp;doublets non liants, soit 10&nbsp;doublets et donc $10 \times 2 = 20$&nbsp;électrons. Le compte est bon.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Reprendre les questions précédentes en remplaçant l'atome de fluor F par un atome de chlore Cl, l'atome de carbone C par un atome de silicium Si et l'atome d'oxygène O par un atome de soufre S.</p>
</div>

<div class="nt-lab nt-lewis" id="lab-lewis2">
<p class="nt-tag"><i class="fa-solid fa-diagram-project"></i>Schéma interactif</p>
<p class="nt-lab-title">Même famille, même schéma&nbsp;: $\ce{ClH3SSi}$</p>
<svg class='nt-lw' viewBox='0 0 242 188' width='242' role='img' aria-label="Schéma de Lewis de la molécule de formule brute ClH3SSi : le silicium est lié au chlore, à deux hydrogènes et au soufre, lui-même lié à un hydrogène ; le chlore porte trois doublets non liants, le soufre deux."><g class='lw-b' data-a='F' data-b='C' data-o='1'><line x1='52.4' y1='94.0' x2='81.6' y2='94.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='H1' data-o='1'><line x1='94.0' y1='81.6' x2='94.0' y2='52.4' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='H2' data-o='1'><line x1='94.0' y1='106.4' x2='94.0' y2='135.6' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O' data-o='1'><line x1='106.4' y1='94.0' x2='135.6' y2='94.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='O' data-b='H3' data-o='1'><line x1='160.4' y1='94.0' x2='189.6' y2='94.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><text class='lw-at' data-at='F' x='40.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>Cl</text><line class='lw-lp' data-at='F' x1='46.0' y1='110.0' x2='34.0' y2='110.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='F' x1='24.0' y1='100.0' x2='24.0' y2='88.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='F' x1='34.0' y1='78.0' x2='46.0' y2='78.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='C' x='94.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>Si</text><text class='lw-at' data-at='H1' x='94.0' y='47.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text><text class='lw-at' data-at='H2' x='94.0' y='155.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text><text class='lw-at' data-at='O' x='148.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>S</text><line class='lw-lp' data-at='O' x1='154.0' y1='110.0' x2='142.0' y2='110.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='O' x1='142.0' y1='78.0' x2='154.0' y2='78.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='H3' x='202.0' y='101.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text></svg>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="colorer"><i class="fa-solid fa-palette"></i>&nbsp; Colorer les doublets</button></div>
<p class="nt-msg" aria-live="polite">Cliquez sur un atome pour voir les doublets qui l'entourent.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Mêmes colonnes, mêmes électrons de valence</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li>Si ($Z = 14$)&nbsp;: $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,{\color{#2A6BC4}{3\text{s}^2\,3\text{p}^2}}$, soit 4 électrons de valence, comme le carbone&nbsp;;</li>
<li>S ($Z = 16$)&nbsp;: $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,{\color{#2A6BC4}{3\text{s}^2\,3\text{p}^4}}$, soit 6, comme l'oxygène&nbsp;;</li>
<li>Cl ($Z = 17$)&nbsp;: $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,{\color{#2A6BC4}{3\text{s}^2\,3\text{p}^5}}$, soit 7, comme le fluor.</li>
</ul>
<p>On retrouve $3 \times 1 + 4 + 6 + 7 = 20$&nbsp;électrons de valence, et le même schéma de Lewis, à 10 doublets. Ce n'est pas un hasard&nbsp;: Si, S et Cl sont dans les mêmes colonnes que C, O et F, ils ont la même configuration de valence (avec $n = 3$ au lieu de $n = 2$), donc le même nombre d'électrons de valence, et ils forment le même nombre de liaisons.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>À part l'hydrogène, de combien de doublets doit être entouré un atome dans un schéma de Lewis pour se retrouver avec le même nombre d'électrons de valence que le gaz noble qui le suit dans le tableau périodique (ce qui lui confère un gain de stabilité)&nbsp;?</p>
<p>Et pour l'hydrogène, combien en faut-il&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Quatre doublets, ou un seul pour l'hydrogène</span></summary>
<div class="nt-d-body">
<p>Les gaz nobles qui suivent les éléments des périodes 2 et 3 (le néon et l'argon) ont 8&nbsp;électrons de valence&nbsp;: un atome doit donc être entouré de <b>4&nbsp;doublets</b>, liants ou non liants.</p>
<p>L'hydrogène est suivi de l'hélium, qui n'a que 2&nbsp;électrons&nbsp;: il lui faut <b>un seul doublet</b>, et ce sera toujours un doublet liant (l'hydrogène forme une seule liaison).</p>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Dans le schéma de Lewis d'une molécule stable, chaque atome (sauf l'hydrogène) est entouré de <span class="imp nt-hole">4&nbsp;doublets</span>, soit 8&nbsp;électrons comme le gaz noble qui le suit&nbsp;; l'hydrogène est entouré d'<span class="imp nt-hole">un seul doublet liant</span>, soit 2&nbsp;électrons comme l'hélium.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple&nbsp;: l'acide méthanoïque</p>
<p>L'acide méthanoïque, de formule $\ce{HCOOH}$, est utilisé par les abeilles, les fourmis et les orties pour se défendre (c'est lui qui pique).</p>
<p>Combien d'électrons de valence sont apportés par ses 5&nbsp;atomes&nbsp;? $2 \times 1$ pour les hydrogènes, $4$ pour le carbone et $2 \times 6$ pour les oxygènes&nbsp;: cela fait 18&nbsp;électrons, soit <b>9&nbsp;doublets</b>. Avec ces 9&nbsp;doublets, on peut envisager différents édifices.</p>
</div>

<div class="nt-lab" id="lab-cand">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>À vous de choisir</p>
<p class="nt-lab-title">Quel schéma de Lewis la nature choisit-elle&nbsp;?</p>
<p class="nt-center nt-note">Ces trois schémas utilisent tous les 9&nbsp;doublets. Choisissez celui qui confère un gain de stabilité à chacun des atomes.</p>
<div class="nt-cand"><button type="button" data-c="A"><span class="nt-cand-t">Schéma A</span><svg class='nt-lw' viewBox='0 0 188 220' width='188' role='img' aria-label="Schéma A"><g class='lw-b' data-a='H1' data-b='C' data-o='1'><line x1='52.4' y1='86.8' x2='81.6' y2='86.8' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O1' data-o='2'><line x1='97.8' y1='74.6' x2='112.4' y2='49.3' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line x1='102.6' y1='77.4' x2='117.2' y2='52.1' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O2' data-o='2'><line x1='102.6' y1='96.1' x2='117.2' y2='121.4' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line x1='97.8' y1='98.9' x2='112.4' y2='124.2' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='O2' data-b='H2' data-o='1'><line x1='127.2' y1='144.3' x2='141.8' y2='169.6' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><text class='lw-at' data-at='H1' x='40.0' y='94.0' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text><text class='lw-at' data-at='C' x='94.0' y='94.0' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>C</text><text class='lw-at' data-at='O1' x='121.0' y='47.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>O</text><line class='lw-lp' data-at='O1' x1='107.8' y1='29.1' x2='118.2' y2='23.1' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='O1' x1='137.0' y1='34.0' x2='137.0' y2='46.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='O2' x='121.0' y='140.7' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>O</text><line class='lw-lp' data-at='O2' x1='110.1' y1='146.7' x2='104.1' y2='136.3' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='H2' x='148.0' y='187.5' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text></svg></button><button type="button" data-c="B"><span class="nt-cand-t">Schéma B</span><svg class='nt-lw' viewBox='0 0 188 220' width='188' role='img' aria-label="Schéma B"><g class='lw-b' data-a='H1' data-b='C' data-o='2'><line x1='52.4' y1='84.0' x2='81.6' y2='84.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line x1='52.4' y1='89.6' x2='81.6' y2='89.6' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O1' data-o='1'><line x1='100.2' y1='76.0' x2='114.8' y2='50.7' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O2' data-o='1'><line x1='100.2' y1='97.5' x2='114.8' y2='122.8' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='O2' data-b='H2' data-o='1'><line x1='127.2' y1='144.3' x2='141.8' y2='169.6' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><text class='lw-at' data-at='H1' x='40.0' y='94.0' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text><text class='lw-at' data-at='C' x='94.0' y='94.0' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>C</text><text class='lw-at' data-at='O1' x='121.0' y='47.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>O</text><line class='lw-lp' data-at='O1' x1='104.1' y1='37.2' x2='110.1' y2='26.8' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='O1' x1='123.8' y1='23.1' x2='134.2' y2='29.1' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='O1' x1='137.9' y1='42.8' x2='131.9' y2='53.2' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='O2' x='121.0' y='140.7' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>O</text><line class='lw-lp' data-at='O2' x1='110.1' y1='146.7' x2='104.1' y2='136.3' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='H2' x='148.0' y='187.5' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text></svg></button><button type="button" data-c="C"><span class="nt-cand-t">Schéma C</span><svg class='nt-lw' viewBox='0 0 188 220' width='188' role='img' aria-label="Schéma C"><g class='lw-b' data-a='H1' data-b='C' data-o='1'><line x1='52.4' y1='86.8' x2='81.6' y2='86.8' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O1' data-o='2'><line x1='97.8' y1='74.6' x2='112.4' y2='49.3' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line x1='102.6' y1='77.4' x2='117.2' y2='52.1' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='C' data-b='O2' data-o='1'><line x1='100.2' y1='97.5' x2='114.8' y2='122.8' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><g class='lw-b' data-a='O2' data-b='H2' data-o='1'><line x1='127.2' y1='144.3' x2='141.8' y2='169.6' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/></g><text class='lw-at' data-at='H1' x='40.0' y='94.0' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text><text class='lw-at' data-at='C' x='94.0' y='94.0' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>C</text><text class='lw-at' data-at='O1' x='121.0' y='47.2' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>O</text><line class='lw-lp' data-at='O1' x1='107.8' y1='29.1' x2='118.2' y2='23.1' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='O1' x1='137.0' y1='34.0' x2='137.0' y2='46.0' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='O2' x='121.0' y='140.7' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>O</text><line class='lw-lp' data-at='O2' x1='110.1' y1='146.7' x2='104.1' y2='136.3' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><line class='lw-lp' data-at='O2' x1='131.9' y1='120.3' x2='137.9' y2='130.7' stroke='#1E293B' stroke-width='1.6' stroke-linecap='round'/><text class='lw-at' data-at='H2' x='148.0' y='187.5' font-size='20' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>H</text></svg></button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### Énergie de liaison {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp nt-hole">énergie de la liaison</span> entre deux atomes dans une molécule correspond à l'<span class="imp nt-hole">énergie nécessaire pour rompre cette liaison</span>.</p>
</div>

<p>Plus cette énergie est grande, plus la liaison est solide&nbsp;: c'est une autre façon de dire que la molécule est plus stable que les atomes séparés. Inversement, lorsqu'une liaison se forme, la même quantité d'énergie est libérée.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Quelques énergies de liaison</span></summary>
<div class="nt-d-body">
<p>Les énergies de liaison sont généralement données pour une mole de liaisons, c'est-à-dire environ $6{,}0 \times 10^{23}$ liaisons identiques (la mole sera étudiée dans le chapitre sur la quantité de matière).</p>
<div class="nt-svgbox"><svg class='nt-svg nt-svg-m' viewBox='0 0 640 338' role='img' aria-label="Énergies de liaison en kilojoules par mole : Cl–Cl 242, C–C 348, C–H 413, H–H 436, O–H 463, O=O 498, C=C 614, C=O 743, C≡C 839, N≡N 945."><line x1='70.0' y1='10' x2='70.0' y2='294' stroke='#E2E8F0' stroke-width='1'/><text x='70.0' y='308' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>0</text><line x1='174.0' y1='10' x2='174.0' y2='294' stroke='#E2E8F0' stroke-width='1'/><text x='174.0' y='308' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>200</text><line x1='278.0' y1='10' x2='278.0' y2='294' stroke='#E2E8F0' stroke-width='1'/><text x='278.0' y='308' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>400</text><line x1='382.0' y1='10' x2='382.0' y2='294' stroke='#E2E8F0' stroke-width='1'/><text x='382.0' y='308' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>600</text><line x1='486.0' y1='10' x2='486.0' y2='294' stroke='#E2E8F0' stroke-width='1'/><text x='486.0' y='308' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>800</text><line x1='590.0' y1='10' x2='590.0' y2='294' stroke='#E2E8F0' stroke-width='1'/><text x='590.0' y='308' font-size='11' text-anchor='middle' fill='#64748B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>1000</text><text x='62' y='28.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>Cl–Cl</text><rect x='70' y='14' width='125.8' height='20' rx='4' fill='#60A5FA'/><text x='201.8' y='28.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>242</text><text x='62' y='56.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>C–C</text><rect x='70' y='42' width='181.0' height='20' rx='4' fill='#60A5FA'/><text x='257.0' y='56.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>348</text><text x='62' y='84.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>C–H</text><rect x='70' y='70' width='214.8' height='20' rx='4' fill='#60A5FA'/><text x='290.8' y='84.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>413</text><text x='62' y='112.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>H–H</text><rect x='70' y='98' width='226.7' height='20' rx='4' fill='#60A5FA'/><text x='302.7' y='112.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>436</text><text x='62' y='140.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>O–H</text><rect x='70' y='126' width='240.8' height='20' rx='4' fill='#60A5FA'/><text x='316.8' y='140.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>463</text><text x='62' y='168.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>O=O</text><rect x='70' y='154' width='259.0' height='20' rx='4' fill='#2563EB'/><text x='335.0' y='168.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>498</text><text x='62' y='196.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>C=C</text><rect x='70' y='182' width='319.3' height='20' rx='4' fill='#2563EB'/><text x='395.3' y='196.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>614</text><text x='62' y='224.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>C=O</text><rect x='70' y='210' width='386.4' height='20' rx='4' fill='#2563EB'/><text x='462.4' y='224.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>743</text><text x='62' y='252.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>C≡C</text><rect x='70' y='238' width='436.3' height='20' rx='4' fill='#1E3A8A'/><text x='512.3' y='252.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>839</text><text x='62' y='280.4' font-size='13' text-anchor='end' fill='#1E293B' font-family='Georgia, serif'>N≡N</text><rect x='70' y='266' width='491.4' height='20' rx='4' fill='#1E3A8A'/><text x='567.4' y='280.4' font-size='12' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>945</text><rect x='70' y='317' width='14' height='14' rx='3' fill='#60A5FA'/><text x='90' y='328' font-size='12' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>liaison simple</text><rect x='210' y='317' width='14' height='14' rx='3' fill='#2563EB'/><text x='230' y='328' font-size='12' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>double</text><rect x='350' y='317' width='14' height='14' rx='3' fill='#1E3A8A'/><text x='370' y='328' font-size='12' fill='#1E293B' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>triple</text><text x='590.0' y='328' font-size='11' text-anchor='end' fill='#64748B' font-style='italic' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>kJ/mol</text></svg></div>
<p class="nt-cap">Énergies moyennes de quelques liaisons, en kilojoules par mole de liaisons.</p>
<p>Une double liaison est plus solide qu'une simple, et une triple plus solide encore&nbsp;: la triple liaison du diazote $\ce{N#N}$ est l'une des plus fortes qui soient, ce qui explique que le diazote de l'air soit si peu réactif.</p>
</div>
</details>

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


  /* =================== données sur les éléments =================== */
  var EL = [null, ['H', 'hydrogène'], ['He', 'hélium'], ['Li', 'lithium'], ['Be', 'béryllium'], ['B', 'bore'], ['C', 'carbone'], ['N', 'azote'], ['O', 'oxygène'], ['F', 'fluor'], ['Ne', 'néon'],
    ['Na', 'sodium'], ['Mg', 'magnésium'], ['Al', 'aluminium'], ['Si', 'silicium'], ['P', 'phosphore'], ['S', 'soufre'], ['Cl', 'chlore'], ['Ar', 'argon'], ['K', 'potassium'], ['Ca', 'calcium']];
  var ORDRE = [['1s', 1, 's', 2], ['2s', 2, 's', 2], ['2p', 2, 'p', 6], ['3s', 3, 's', 2], ['3p', 3, 'p', 6], ['4s', 4, 's', 2]];
  var COUL = { s: '#D97706', p: '#059669' };
  var GAZ = { 2: 'He', 10: 'Ne', 18: 'Ar' };
  function config(ne) {   /* [[nom, n, type, nombre d'électrons], …] à l'état fondamental */
    var out = [], r = ne;
    for (var i = 0; i < ORDRE.length && r > 0; i++) { var k = Math.min(ORDRE[i][3], r); out.push([ORDRE[i][0], ORDRE[i][1], ORDRE[i][2], k]); r -= k; }
    return out;
  }
  function nmax(cf) { return cf.length ? cf[cf.length - 1][1] : 0; }
  function nval(Z) { var cf = config(Z), m = nmax(cf), s = 0; cf.forEach(function (c) { if (c[1] === m) { s += c[3]; } }); return s; }
  function position(Z) {   /* [période, colonne] */
    var cf = config(Z), last = cf[cf.length - 1], per = last[1];
    if (Z === 2) { return [1, 18]; }
    return [per, last[2] === 's' ? last[3] : 12 + last[3]];
  }
  function bloc(Z) { var cf = config(Z); return cf[cf.length - 1][2]; }
  function sup(k) { return '<sup>' + k + '</sup>'; }
  function cfgHTML(cf, opt) {   /* opt.val : électrons de valence en couleur ; opt.condense : [gaz noble] ; opt.couleur : sous-couches colorées */
    opt = opt || {}; var m = nmax(cf), h = '', i0 = 0;
    if (opt.condense) {
      var tot = 0, best = 0, bi = -1;
      for (var i = 0; i < cf.length; i++) { tot += cf[i][3]; if (GAZ[tot] && i < cf.length - 1) { best = tot; bi = i; } }
      if (bi >= 0) { h += '[' + GAZ[best] + ']\u2009'; i0 = bi + 1; }
    }
    for (var j = i0; j < cf.length; j++) {
      var c = cf[j], t = c[0] + sup(c[3]), cls = opt.val ? (c[1] === m ? 'nt-val' : 'nt-coeur') : (opt.couleur ? 'nt-' + c[2] : '');
      h += (j > i0 ? '\u2009' : '') + (cls ? '<span class="' + cls + '">' + t + '</span>' : t);
    }
    return '<span class="nt-cfg">' + h + '</span>';
  }
  function famille(Z) {
    var col = position(Z)[1];
    if (Z === 1) { return ['hydrogène', '#94A3B8']; }
    return { 1: ['alcalins', '#F43F5E'], 2: ['alcalino-terreux', '#F59E0B'], 13: ['famille du bore', '#A3E635'], 14: ['famille du carbone', '#2DD4BF'], 15: ['famille de l\u2019azote', '#38BDF8'], 16: ['famille de l\u2019oxygène', '#818CF8'], 17: ['halogènes', '#22C55E'], 18: ['gaz nobles', '#C084FC'] }[col];
  }
  var ION = { 1: ['H<sup>+</sup>', 1, 'ion hydrogène'], 3: ['Li<sup>+</sup>', 1, 'ion lithium'], 4: ['Be<sup>2+</sup>', 2, 'ion béryllium'], 8: ['O<sup>2\u2212</sup>', -2, 'ion oxyde'], 9: ['F<sup>\u2212</sup>', -1, 'ion fluorure'],
    11: ['Na<sup>+</sup>', 1, 'ion sodium'], 12: ['Mg<sup>2+</sup>', 2, 'ion magnésium'], 13: ['Al<sup>3+</sup>', 3, 'ion aluminium'], 16: ['S<sup>2\u2212</sup>', -2, 'ion sulfure'], 17: ['Cl<sup>\u2212</sup>', -1, 'ion chlorure'],
    19: ['K<sup>+</sup>', 1, 'ion potassium'], 20: ['Ca<sup>2+</sup>', 2, 'ion calcium'] };
  var LIAIS = { 1: 1, 6: 4, 7: 3, 8: 2, 9: 1, 14: 4, 15: 3, 16: 2, 17: 1, 2: 0, 10: 0, 18: 0 };
  function parseCfg(s) {   /* « 1s2 2s2 2p3 » ou « 1s² 2s²… » ou « 1s^2… » → [[nom, k], …] ou null */
    var SUP = { '\u2070': '0', '\u00B9': '1', '\u00B2': '2', '\u00B3': '3', '\u2074': '4', '\u2075': '5', '\u2076': '6', '\u2077': '7', '\u2078': '8', '\u2079': '9' };
    s = String(s).replace(/[\u2070\u00B9\u00B2\u00B3\u2074-\u2079]/g, function (c) { return SUP[c]; }).replace(/[\s,;.\^]/g, '').toLowerCase();
    if (!s) { return null; }
    var re = /([1-4])([sp])(\d)/g, out = [], m, pos = 0;
    while ((m = re.exec(s)) !== null) { if (m.index !== pos) { return null; } out.push([m[1] + m[2], parseInt(m[3], 10)]); pos = re.lastIndex; }
    return pos === s.length ? out : null;
  }
  function parseHTML(p) { return '<span class="nt-cfg">' + p.map(function (c) { return c[0] + sup(c[1]); }).join('\u2009') + '</span>'; }
  function verifCfg(p, ne, valSeule) {   /* compare une configuration saisie à celle attendue ; renvoie [vrai/faux, explication] */
    var att = config(ne);
    if (valSeule) { var m = nmax(att); att = att.filter(function (c) { return c[1] === m; }); }
    var sat = { s: 2, p: 6 }, tot = 0, i;
    for (i = 0; i < p.length; i++) { if (p[i][1] > sat[p[i][0].charAt(1)]) { return [false, 'La sous-couche ' + p[i][0] + ' ne peut pas contenir ' + p[i][1] + ' électrons&nbsp;: une sous-couche ' + p[i][0].charAt(1) + ' est saturée à ' + sat[p[i][0].charAt(1)] + ' électrons.']; } tot += p[i][1]; }
    var ok = p.length === att.length && p.every(function (c, k) { return c[0] === att[k][0] && c[1] === att[k][3]; });
    if (ok) { return [true, '']; }
    var nomsAtt = att.map(function (c) { return c[0]; }).join(' '), nomsP = p.map(function (c) { return c[0]; }).join(' ');
    var totAtt = 0; att.forEach(function (c) { totAtt += c[3]; });
    if (tot !== totAtt) { return [false, 'Il faut placer ' + totAtt + ' électron' + (totAtt > 1 ? 's' : '') + (valSeule ? ' de valence' : '') + ', et votre configuration en contient ' + tot + '.']; }
    if (nomsP !== nomsAtt) { return [false, 'L\u2019ordre ou le choix des sous-couches ne convient pas&nbsp;: on remplit dans l\u2019ordre 1s, 2s, 2p, 3s, 3p, et on ne commence une sous-couche que lorsque la précédente est pleine.']; }
    return [false, 'Une sous-couche est commencée alors que la précédente n\u2019est pas pleine.'];
  }

  /* =================== dessin d'un atome (couches concentriques) =================== */
  function positionsElectrons(cf, cx, cy, rayons) {   /* électrons répartis régulièrement sur leur couche, en commençant en haut */
    var parCouche = {}, out = [];
    cf.forEach(function (c) { for (var k = 0; k < c[3]; k++) { (parCouche[c[1]] = parCouche[c[1]] || []).push(c[2]); } });
    Object.keys(parCouche).forEach(function (n) {
      var L = parCouche[n], r = rayons[n - 1];
      L.forEach(function (t, i) { var a = -Math.PI / 2 + 2 * Math.PI * i / L.length + (n % 2 ? 0 : Math.PI / L.length); out.push({ x: cx + r * Math.cos(a), y: cy + r * Math.sin(a), n: +n, t: t }); });
    });
    return out;
  }
  function dessineAtome(ctx, cx, cy, rayons, Z, cf, o) {
    o = o || {}; var nc = o.couches || rayons.length, m = nmax(cf), k;
    for (k = 1; k <= nc; k++) {
      var occ = cf.some(function (c) { return c[1] === k; }), val = o.val && k === m;
      ctx.save(); ctx.strokeStyle = val ? BLUE : (occ ? '#94A3B8' : '#CBD5E1'); ctx.lineWidth = val ? 2.2 : 1.1; if (!occ) { ctx.setLineDash([3, 4]); }
      ctx.beginPath(); ctx.arc(cx, cy, rayons[k - 1], 0, 2 * Math.PI); ctx.stroke(); ctx.restore();
    }
    var rn = Math.max(9, rayons[0] * 0.42), g = ctx.createRadialGradient(cx - rn * 0.3, cy - rn * 0.3, 1, cx, cy, rn);
    g.addColorStop(0, '#FDA4AF'); g.addColorStop(1, '#E11D48'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, rn, 0, 2 * Math.PI); ctx.fill();
    txt(ctx, '+' + Z, cx, cy + 0.5, { size: Math.max(9, rn * 0.75), col: '#FFFFFF' });
    var P = o.pos || positionsElectrons(cf, cx, cy, rayons), re = o.re || 4.6;
    if (o.labels) {   /* étiquettes des couches, placées là où il n'y a pas d'électron */
      for (k = 1; k <= nc; k++) {
        var cand = [35, 55, 15, 145, 125, 165, -20, -160], best = cand[0];
        for (var c = 0; c < cand.length; c++) {
          var a = cand[c] * Math.PI / 180, lx = cx + rayons[k - 1] * Math.cos(a), ly = cy + rayons[k - 1] * Math.sin(a);
          if (P.every(function (e) { return Math.hypot(e.x - lx, e.y - ly) > 22; })) { best = cand[c]; break; }
        }
        var ab = best * Math.PI / 180, isval = o.val && k === m;
        pill(ctx, 'n = ' + k, cx + rayons[k - 1] * Math.cos(ab), cy + rayons[k - 1] * Math.sin(ab), { size: 10.5, col: isval ? BLUE : SLATE, stroke: '#E2E8F0' });
      }
    }
    P.forEach(function (e, i) {
      var sc = o.echelle ? o.echelle(i) : 1, al = o.opacite ? o.opacite(i) : 1; if (sc <= 0 || al <= 0) { return; }
      ctx.save(); ctx.globalAlpha = al;
      if (o.val && e.n === m) { ctx.fillStyle = 'rgba(42,107,196,0.18)'; ctx.beginPath(); ctx.arc(e.x, e.y, re * 2 * sc, 0, 2 * Math.PI); ctx.fill(); }
      ctx.fillStyle = COUL[e.t]; ctx.beginPath(); ctx.arc(e.x, e.y, re * sc, 0, 2 * Math.PI); ctx.fill(); ctx.restore();
    });
  }
  function atomeSVG(Z, ne) {   /* petit dessin d'atome pour les fiches du tableau */
    var cf = config(ne === undefined ? Z : ne), m = nmax(cf), R = [17, 31, 45, 51], c = 55, h = '';
    for (var k = 1; k <= Math.max(1, m); k++) { h += "<circle cx='55' cy='55' r='" + R[k - 1] + "' fill='none' stroke='" + (k === m ? BLUE : '#94A3B8') + "' stroke-width='" + (k === m ? 1.6 : 1) + "'/>"; }
    h += "<circle cx='55' cy='55' r='8' fill='#E11D48'/><text x='55' y='58' font-size='8' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif'>+" + Z + "</text>";
    positionsElectrons(cf, c, c, R).forEach(function (e) { h += "<circle cx='" + e.x.toFixed(1) + "' cy='" + e.y.toFixed(1) + "' r='3.2' fill='" + COUL[e.t] + "'/>"; });
    return "<svg viewBox='0 0 110 110' role='img' aria-label='Atome : noyau et électrons répartis en couches'>" + h + '</svg>';
  }

  /* =================== 1. Remplir le cortège =================== */
  (function () {
    var root = document.getElementById('lab-remp'); if (!root) { return; }
    var inZ = $(root, '[data-in="z"]'), outZ = $(root, '.out-z'), chk = $(root, '[data-in="val"]'), out = $(root, '.nt-remp-out');
    var Z = 6, anim = -1, ta = 0, cnv;
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, cf = config(Z), etroit = W < 560; ctx.clearRect(0, 0, W, H);
      var ax = etroit ? W / 2 : W * 0.26, ay = etroit ? 118 : H / 2, R = etroit ? Math.min(W * 0.4, 104) : Math.min(W * 0.22, H * 0.4);
      var ray = [R * 0.36, R * 0.68, R];
      function ech(i) { return i === anim ? Math.min(1, ta / 0.3) : 1; }
      dessineAtome(ctx, ax, ay, ray, Z, cf, { val: chk.checked, labels: true, echelle: ech, re: Math.max(3.6, R * 0.05) });
      /* sous-couches dans l'ordre de remplissage, de bas en haut */
      var lx = etroit ? 36 : W * 0.56, ly0 = etroit ? H - 22 : H - 36, dy = etroit ? 34 : 44, slot = etroit ? 17 : 21, rs = etroit ? 6 : 7.2, rang = 0;
      var ys = [ly0, ly0 - dy * 1.25, ly0 - dy * 2.1, ly0 - dy * 3.35, ly0 - dy * 4.2];
      arrow(ctx, lx - 14, ys[0] + 6, lx - 14, ys[4] - 6, '#94A3B8', false, 6);
      ctx.save(); ctx.translate(lx - 22, (ys[0] + ys[4]) / 2); ctx.rotate(-Math.PI / 2); txt(ctx, 'ordre de remplissage', 0, 0, { size: 10.5, col: SLATE }); ctx.restore();
      var reste = Z;
      ORDRE.slice(0, 5).forEach(function (s, i) {
        var y = ys[i], k = Math.max(0, Math.min(s[3], reste)), part = k > 0 && k < s[3]; reste -= k;
        txt(ctx, s[0], lx + 14, y, { size: 16, serif: true, col: k ? COUL[s[2]] : '#94A3B8' });
        for (var j = 0; j < s[3]; j++) {
          var x = lx + 38 + j * slot, plein = j < k, idx = rang + j;
          ctx.strokeStyle = plein ? COUL[s[2]] : '#CBD5E1'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.arc(x, y, rs, 0, 2 * Math.PI); ctx.stroke();
          if (plein) { var sc = ech(idx); ctx.fillStyle = COUL[s[2]]; ctx.beginPath(); ctx.arc(x, y, rs * 0.62 * sc, 0, 2 * Math.PI); ctx.fill(); }
        }
        txt(ctx, k + '/' + s[3] + (k === s[3] ? ' : saturée' : (part ? ' : en cours' : '')), lx + 38 + s[3] * slot + 4, y, { size: 11, col: k === s[3] ? COUL[s[2]] : SLATE, align: 'left' });
        rang += s[3];
      });
    }
    function maj() {
      inZ.value = Z; outZ.textContent = Z;
      out.innerHTML = '<span class="nt-el">' + EL[Z][1].charAt(0).toUpperCase() + EL[Z][1].slice(1) + ' (' + EL[Z][0] + ')</span>, ' + Z + '&nbsp;électron' + (Z > 1 ? 's' : '') + '<br>' + cfgHTML(config(Z), chk.checked ? { val: true } : { couleur: true }) +
        (chk.checked ? '<br><span class="nt-note">' + nval(Z) + '&nbsp;électron' + (nval(Z) > 1 ? 's' : '') + ' de valence (couche n&nbsp;=&nbsp;' + nmax(config(Z)) + ')</span>' : '');
      draw(cnv);
    }
    var loop = Loop(root, function (dt) { ta += dt; draw(cnv); if (ta > 0.3) { anim = -1; return false; } return true; });
    function change(z) { var nz = Math.max(1, Math.min(18, z)); if (nz === Z) { return; } anim = nz > Z && !RM ? nz - 1 : -1; Z = nz; ta = 0; maj(); if (anim >= 0) { loop.kick(); } }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 430 : 300; }, draw);
    $(root, '[data-act="plus"]').addEventListener('click', function () { change(Z + 1); });
    $(root, '[data-act="moins"]').addEventListener('click', function () { change(Z - 1); });
    inZ.addEventListener('input', function () { change(parseInt(inZ.value, 10)); });
    chk.addEventListener('change', maj);
    maj();
  })();

  /* =================== 1 b. Quelques orbitales (pour aller plus loin) =================== */
  (function () {
    var cv = $(document, 'canvas.nt-orb'); if (!cv) { return; }
    var det = cv.closest('details'), cnv = null;
    var ORB = [
      ['1s', 'une sphère', 'sphère', function (x, z, r) { return Math.exp(-r); }],
      ['2s', 'une sphère et une couronne', 'sphère + couronne', function (x, z, r) { return (2 - r) * Math.exp(-r / 2); }],
      ['2p', 'deux lobes', '2 lobes', function (x, z, r) { return z * Math.exp(-r / 2); }],
      ['3d', 'deux lobes et un anneau', '2 lobes + anneau', function (x, z, r) { return (3 * z * z - r * r) * Math.exp(-r / 3); }]
    ];
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, dpr = window.devicePixelRatio || 1, cols = W < 560 ? 2 : 4, gap = 14, p = Math.floor((W - gap * (cols - 1)) / cols), L = 22;
      ctx.clearRect(0, 0, W, H);
      ORB.forEach(function (orb, k) {
        var c = k % cols, r0 = Math.floor(k / cols), x0 = c * (p + gap), y0 = r0 * (p + 46), n = Math.round(p * dpr), img = ctx.createImageData(n, n), val = new Float32Array(n * n), mx = 0, i, j;
        for (j = 0; j < n; j++) { for (i = 0; i < n; i++) {
          var x = (i / (n - 1) * 2 - 1) * L, z = -(j / (n - 1) * 2 - 1) * L, r = Math.hypot(x, z), v = orb[3](x, z, r); val[j * n + i] = v; if (v * v > mx) { mx = v * v; }
        } }
        for (i = 0; i < n * n; i++) {
          var v2 = val[i], s = Math.pow(v2 * v2 / mx, 0.3), col = v2 >= 0 ? [37, 99, 235] : [217, 119, 6];
          img.data[4 * i] = 255 + (col[0] - 255) * s; img.data[4 * i + 1] = 255 + (col[1] - 255) * s; img.data[4 * i + 2] = 255 + (col[2] - 255) * s; img.data[4 * i + 3] = 255;
        }
        ctx.putImageData(img, Math.round(x0 * dpr), Math.round(y0 * dpr));
        ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 1; rr(ctx, x0 + 0.5, y0 + 0.5, p - 1, p - 1, 6); ctx.stroke();
        ctx.fillStyle = '#E11D48'; ctx.beginPath(); ctx.arc(x0 + p / 2, y0 + p / 2, 2.2, 0, 2 * Math.PI); ctx.fill();
        txt(ctx, orb[0], x0 + p / 2, y0 + p + 15, { size: 15, serif: true, col: NAVY });
        txt(ctx, cols === 4 ? orb[1] : orb[2], x0 + p / 2, y0 + p + 33, { size: 11.5, col: SLATE });
      });
    }
    function ouvre() { if (!cnv) { cnv = Canvas(cv, function (W) { var cols = W < 560 ? 2 : 4, p = Math.floor((W - 14 * (cols - 1)) / cols); return (p + 46) * (4 / cols); }, draw); } else { cnv.size(); } }
    if (det) { det.addEventListener('toggle', function () { if (det.open) { ouvre(); } }); if (det.open) { ouvre(); } } else { ouvre(); }
  })();

  /* =================== 2. Entraînement : écrire une configuration =================== */
  (function () {
    var root = document.getElementById('tr-config'); if (!root) { return; }
    var vis = $(root, '.nt-qvis'), qEl = $(root, '.nt-tr-q'), inp = $(root, 'input[type="text"]'), bC = $(root, '[data-act="check"]'), prev = $(root, '.nt-tr-prev'), zone = $(root, '.nt-tr-ans');
    var IONS = [[11, 1], [12, 2], [13, 3], [9, -1], [8, -2], [17, -1], [16, -2], [19, 1], [20, 2], [3, 1]];
    var Q = [], cur = null;
    function charge(q) { return q === 1 ? '+' : (q === -1 ? '\u2212' : (q > 0 ? q + '+' : -q + '\u2212')); }
    function gen() {
      var zs = shuffle([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]).slice(0, 4), io = shuffle(IONS.slice()).slice(0, 2), L = [];
      zs.forEach(function (z) { L.push({ z: z, q: 0 }); }); io.forEach(function (x) { L.push({ z: x[0], q: x[1] }); });
      return shuffle(L);
    }
    var S = Serie(root, 6, {
      init: function () { Q = gen(); },
      show: function (k) {
        cur = Q[k]; var ne = cur.z - cur.q; cur.ne = ne;
        if (cur.q === 0) { vis.innerHTML = EL[cur.z][0] + '&nbsp;<span style="font-size:0.5em">(<i>Z</i>&nbsp;=&nbsp;' + cur.z + ')</span>'; qEl.innerHTML = 'Écrire la configuration électronique de l\u2019atome de ' + EL[cur.z][1] + ' à l\u2019état fondamental.'; }
        else { vis.innerHTML = EL[cur.z][0] + '<sup style="font-size:0.55em">' + charge(cur.q) + '</sup>&nbsp;<span style="font-size:0.5em">(<i>Z</i>&nbsp;=&nbsp;' + cur.z + ')</span>'; qEl.innerHTML = 'Écrire la configuration électronique de l\u2019' + ION[cur.z][2] + ' ' + ION[cur.z][0] + '.'; }
        inp.value = ''; prev.innerHTML = ''; zone.hidden = false; bC.disabled = false;
      },
      bilan: function (g, t0) { vis.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;6</span>'; qEl.innerHTML = t0; zone.hidden = true; prev.innerHTML = ''; }
    });
    inp.addEventListener('input', function () { var p = parseCfg(inp.value); prev.innerHTML = inp.value.trim() ? (p ? 'Aperçu&nbsp;: ' + parseHTML(p) : 'Écriture non reconnue&nbsp;: séparez les sous-couches, par exemple <code>1s2 2s2 2p3</code>.') : ''; });
    function check() {
      if (S.answered || S.fini) { return; }
      var p = parseCfg(inp.value); if (!p) { S.say('Écriture non reconnue&nbsp;: tapez par exemple <code>1s2 2s2 2p3</code>.'); return; }
      var v = verifCfg(p, cur.ne, false), h = '';
      if (cur.q !== 0) { h += 'L\u2019' + ION[cur.z][2] + ' ' + ION[cur.z][0] + ' a ' + (cur.q > 0 ? cur.q + '&nbsp;électron' + (cur.q > 1 ? 's' : '') + ' de moins' : (-cur.q) + '&nbsp;électron' + (cur.q < -1 ? 's' : '') + ' de plus') + ' que l\u2019atome (<i>Z</i>&nbsp;=&nbsp;' + cur.z + ')&nbsp;: il possède ' + cur.ne + '&nbsp;électrons. '; }
      else { h += 'L\u2019atome possède <i>Z</i>&nbsp;=&nbsp;' + cur.z + '&nbsp;électrons. '; }
      h += 'Configuration attendue&nbsp;: ' + cfgHTML(config(cur.ne), { couleur: true }) + '.';
      if (cur.q !== 0 && GAZ[cur.ne]) { h += ' C\u2019est la configuration ' + (GAZ[cur.ne] === 'He' ? 'de l\u2019hélium' : (GAZ[cur.ne] === 'Ne' ? 'du néon' : 'de l\u2019argon')) + '&nbsp;!'; }
      bC.disabled = true; S.answer(v[0], (v[0] ? '' : v[1] + ' ') + h);
    }
    bC.addEventListener('click', check); inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { check(); } });
    S.start();
  })();

  /* =================== 3. Tableau périodique interactif =================== */
  var COLS = [1, 2, 0, 13, 14, 15, 16, 17, 18];   /* 0 : colonnes 3 à 12, non utilisées ici */
  function zDe(per, col) { for (var z = 1; z <= 18; z++) { var p = position(z); if (p[0] === per && p[1] === col) { return z; } } return 0; }
  function clair(hex, a) { return 'color-mix(in srgb, ' + hex + ' ' + Math.round(a * 100) + '%, #FFFFFF)'; }
  function lewisMini(z) {   /* symbole de l'atome avec ses liaisons (orange) et ses doublets non liants (bleu) */
    var L = LIAIS[z], DIR = { 4: [[0, 90, 180, 270], []], 3: [[0, 90, 180], [270]], 2: [[45, 135], [225, 315]], 1: [[0], z === 1 ? [] : [90, 180, 270]] }[L], h = '';
    DIR[0].forEach(function (a) { var r = a * Math.PI / 180; h += "<line x1='" + (24 + 10 * Math.cos(r)).toFixed(1) + "' y1='" + (24 + 10 * Math.sin(r)).toFixed(1) + "' x2='" + (24 + 21 * Math.cos(r)).toFixed(1) + "' y2='" + (24 + 21 * Math.sin(r)).toFixed(1) + "' stroke='#D97706' stroke-width='2' stroke-linecap='round'/>"; });
    DIR[1].forEach(function (a) { var r = a * Math.PI / 180, cx = 24 + 12 * Math.cos(r), cy = 24 + 12 * Math.sin(r), tx = -Math.sin(r) * 4.5, ty = Math.cos(r) * 4.5; h += "<line x1='" + (cx - tx).toFixed(1) + "' y1='" + (cy - ty).toFixed(1) + "' x2='" + (cx + tx).toFixed(1) + "' y2='" + (cy + ty).toFixed(1) + "' stroke='#0284C7' stroke-width='2' stroke-linecap='round'/>"; });
    h += "<text x='24' y='29.5' font-size='15' text-anchor='middle' fill='currentColor' font-family='Georgia, \"Times New Roman\", serif'>" + EL[z][0] + "</text>";
    return "<svg class='nt-mini' viewBox='0 0 48 48' aria-hidden='true'>" + h + "</svg>";
  }
  var MODES = {
    config: { nom: 'Configurations', sub: function (z) { return [cfgHTML(config(z), { couleur: true }), true]; }, leg: '<span><b class="nt-s">s</b>&nbsp;électrons des sous-couches s</span><span><b class="nt-p">p</b>&nbsp;électrons des sous-couches p</span>' },
    blocs: { nom: 'Blocs', sub: function (z) { return ['bloc ' + bloc(z), true]; }, bg: function (z) { return bloc(z) === 's' ? '#FEF3C7' : '#D1FAE5'; }, leg: '<span><i style="background:#FEF3C7"></i>bloc s (sous-couche s en cours de remplissage)</span><span><i style="background:#D1FAE5"></i>bloc p</span>' },
    valence: { nom: 'Électrons de valence', sub: function (z) { return [cfgHTML(config(z), { val: true }), true, nval(z) + '&nbsp;e<sup>\u2212</sup>']; }, leg: '<span><b style="color:var(--blue)">en bleu</b>&nbsp;: électrons de valence</span><span><b style="color:#94A3B8">en gris</b>&nbsp;: électrons de cœur</span>' },
    familles: { nom: 'Familles', sub: function (z) { return ['', false]; }, bg: function (z) { return clair(famille(z)[1], 0.3); },
      leg: [[1, 'hydrogène'], [3, 'alcalins'], [4, 'alcalino-terreux'], [5, 'famille du bore'], [6, 'famille du carbone'], [7, 'famille de l\u2019azote'], [8, 'famille de l\u2019oxygène'], [9, 'halogènes'], [10, 'gaz nobles']].map(function (x) { return '<span><i style="background:' + clair(famille(x[0])[1], 0.3) + '"></i>' + x[1] + '</span>'; }).join('') },
    condensee: { nom: 'Écriture condensée', sub: function (z) { return [cfgHTML(config(z), { condense: true, val: true }), true]; }, leg: '<span>[He], [Ne]&nbsp;: électrons de cœur, ceux du gaz noble qui précède</span>' },
    periodes: { nom: 'Périodes', sub: function (z) { return [cfgHTML(config(z), { val: true }), true, 'n&nbsp;=&nbsp;' + position(z)[0]]; }, bg: function (z) { return ['#E0F2FE', '#FEF9C3', '#DCFCE7'][position(z)[0] - 1]; },
      leg: '<span><i style="background:#E0F2FE"></i>période 1&nbsp;: n&nbsp;=&nbsp;1</span><span><i style="background:#FEF9C3"></i>période 2&nbsp;: n&nbsp;=&nbsp;2</span><span><i style="background:#DCFCE7"></i>période 3&nbsp;: n&nbsp;=&nbsp;3</span>' },
    nobles: { nom: 'Gaz nobles', sub: function (z) { return position(z)[1] === 18 ? [cfgHTML(config(z), { val: true }), true, 'saturée'] : ['', false]; }, bg: function (z) { return position(z)[1] === 18 ? '#F3E8FF' : '#FFFFFF'; }, dim: function (z) { return position(z)[1] !== 18; },
      leg: '<span><i style="background:#F3E8FF"></i>gaz nobles&nbsp;: couche de valence saturée (2 ou 8 électrons de valence)</span>' },
    ions: { nom: 'Ions', sub: function (z) { var I = ION[z]; return [I ? '<b>' + I[0] + '</b>' : '\u2014', false]; }, bg: function (z) { var I = ION[z]; return !I ? '#FFFFFF' : (I[1] > 0 ? (I[3] ? '#FFF1F2' : '#FFE4E6') : (I[3] ? '#EFF6FF' : '#DBEAFE')); },
      leg: '<span><i style="background:#FFE4E6"></i>cation (électrons perdus)</span><span><i style="background:#DBEAFE"></i>anion (électrons gagnés)</span><span><b style="color:#94A3B8">symbole en gris</b>&nbsp;: pas d\u2019ion monoatomique courant</span>' },
    liaisons: { nom: 'Liaisons', sub: function (z) { var L = LIAIS[z]; if (L === undefined) { return ['', false, z === 5 ? '\u2014' : 'ions']; } return [L ? lewisMini(z) : '', false, L + '&nbsp;liaison' + (L > 1 ? 's' : '')]; }, bg: function (z) { var L = LIAIS[z]; return L === undefined ? '#F8FAFC' : ['#F1F5F9', '#FCE7F3', '#FAE8FF', '#EDE9FE', '#E0E7FF'][L]; },
      leg: '<span><i style="background:#E0E7FF"></i>4 liaisons</span><span><i style="background:#EDE9FE"></i>3</span><span><i style="background:#FAE8FF"></i>2</span><span><i style="background:#FCE7F3"></i>1</span><span><i style="background:#F1F5F9"></i>0 (gaz nobles)</span><span><i style="background:#F8FAFC"></i>métaux (forment surtout des ions) et bore</span><span><b style="color:#D97706">\u2014</b>&nbsp;liaison, <b style="color:#0284C7">\u2014</b>&nbsp;doublet non liant</span>' },
    vide: { nom: '', sub: function () { return ['', false]; } }
  };
  function nomGazDe(ne) { return GAZ[ne] === 'He' ? 'de l\u2019hélium' : (GAZ[ne] === 'Ne' ? 'du néon' : 'de l\u2019argon'); }
  function fiche(z, mode) {   /* texte détaillé sur un élément ; ions et liaisons ne sont détaillés que dans le tableau correspondant */
    var cf = config(z), p = position(z), f = famille(z), I = ION[z], L = LIAIS[z], v = nval(z), h = '', noble = p[1] === 18;
    h += '<p class="nt-tp-titre">' + EL[z][1].charAt(0).toUpperCase() + EL[z][1].slice(1) + ' (' + EL[z][0] + '), <i>Z</i>&nbsp;=&nbsp;' + z + '</p>';
    h += '<p>Configuration&nbsp;: ' + cfgHTML(cf, { val: true }) + (z > 2 ? ', soit ' + cfgHTML(cf, { condense: true }) : '') + '</p>';
    h += '<p>' + v + '&nbsp;électron' + (v > 1 ? 's' : '') + ' de valence, sur la couche n&nbsp;=&nbsp;' + nmax(cf) + '.</p>';
    h += '<p>Période ' + p[0] + ', colonne ' + p[1] + ' (bloc ' + bloc(z) + ')&nbsp;; famille&nbsp;: ' + f[0] + '.</p>';
    if (mode === 'ions') {
      if (noble) { h += '<p>Couche de valence saturée&nbsp;: déjà très stable, il ne forme pas d\u2019ion.</p>'; }
      else if (I) { var ne = z - I[1]; h += '<p>Ion courant&nbsp;: <b>' + I[0] + '</b> (' + I[2] + '), obtenu en ' + (I[1] > 0 ? 'perdant ' + I[1] : 'gagnant ' + (-I[1])) + '&nbsp;électron' + (Math.abs(I[1]) > 1 ? 's' : '') + (GAZ[ne] ? '&nbsp;: il a alors la configuration ' + nomGazDe(ne) : (ne === 0 ? '&nbsp;: il ne reste que le noyau' : '')) + '.</p>'; }
      else { h += '<p>Pas d\u2019ion monoatomique courant&nbsp;: il forme plutôt des liaisons covalentes.</p>'; }
    } else if (mode === 'liaisons') {
      if (noble) { h += '<p>Couche de valence saturée&nbsp;: déjà très stable, il ne forme pas de liaison.</p>'; }
      else if (z === 5) { h += '<p>Le bore forme 3&nbsp;liaisons, mais ne s\u2019entoure alors que de 6&nbsp;électrons&nbsp;: il échappe à la règle des 4&nbsp;doublets (hors programme).</p>'; }
      else if (L !== undefined) { h += '<p>Forme <b>' + L + '&nbsp;liaison' + (L > 1 ? 's' : '') + ' covalente' + (L > 1 ? 's' : '') + '</b>&nbsp;: il lui manque ' + L + '&nbsp;électron' + (L > 1 ? 's' : '') + ' pour atteindre la configuration ' + (z === 1 ? 'de l\u2019hélium' : (z <= 10 ? 'du néon' : 'de l\u2019argon')) + '.</p>'; }
      else { h += '<p>Il forme plutôt des ions que des liaisons covalentes.</p>'; }
    } else if (noble) { h += '<p>Couche de valence saturée.</p>'; }
    return h;
  }
  function Tableau(zone, opt) {
    opt = opt || {}; var modes = opt.modes || ['config'], mode = modes[0], cells = {}, sel = 0, T = {};
    var h = '';
    if (modes.length > 1) { h += '<div class="nt-btns"><div class="nt-seg" role="radiogroup">' + modes.map(function (m, i) { return '<label><input type="radio" name="tp-' + Math.random().toString(36).slice(2) + '" value="' + m + '"' + (i ? '' : ' checked') + '><span>' + MODES[m].nom + '</span></label>'; }).join('').replace(/name="tp-[^"]+"/g, 'name="tp-' + (zone.id || Math.random().toString(36).slice(2)) + '"') + '</div></div>'; }
    h += '<div class="nt-tp-grid"><span></span>' + COLS.map(function (c) { return '<span class="nt-tp-h">' + (c ? c : '<span class="lg">3 à 12</span><span class="sm">\u2026</span>') + '</span>'; }).join('');
    for (var per = 1; per <= 3; per++) {
      h += '<span class="nt-tp-n">' + per + '</span>';
      COLS.forEach(function (c) {
        if (!c) { h += per === 1 ? '<span></span>' : '<span class="nt-tp-gap"></span>'; return; }
        var z = zDe(per, c); h += z ? '<button type="button" class="nt-tp-cell" data-z="' + z + '"></button>' : '<span></span>';
      });
    }
    h += '</div><div class="nt-tp-leg"></div>' + (opt.info === false ? '' : '<div class="nt-tp-info" aria-live="polite"><div></div><div><p>Cliquez sur un élément pour l\u2019examiner.</p></div></div>');
    zone.innerHTML = h;
    var leg = $(zone, '.nt-tp-leg'), info = $(zone, '.nt-tp-info');
    $$(zone, '.nt-tp-cell').forEach(function (b) { cells[b.getAttribute('data-z')] = b; b.addEventListener('click', function () { var z = +b.getAttribute('data-z'); if (opt.onPick) { opt.onPick(z, b); } else { T.select(z); } }); });
    T.render = function () {
      var M = MODES[mode];
      Object.keys(cells).forEach(function (z) {
        z = +z; var b = cells[z], s = M.sub(z), vide = mode === 'vide';
        var dans = s[0] && s[0].indexOf('nt-mini') >= 0;
        if (mode === 'ions') {
          var I = ION[z];
          b.innerHTML = '<span class="z">' + z + '</span>' + (I ? '<span class="sym-mini">' + EL[z][0] + '</span><span class="ion">' + I[0].replace(/<sup>([^<]*)<\/sup>/, '<span class="chg">$1</span>') + '</span>' : '<span class="sym">' + EL[z][0] + '</span>');
          b.classList.toggle('nt-sans', !I); b.style.background = M.bg(z); b.style.opacity = '';
          b.setAttribute('aria-label', EL[z][1] + (I ? ', ion ' + I[2] : ', pas d\u2019ion courant')); return;
        }
        b.classList.remove('nt-sans');
        b.innerHTML = vide ? '' : '<span class="z">' + z + '</span>' + (dans ? '' : '<span class="sym">' + EL[z][0] + '</span>') + (s[0] ? (dans ? s[0] : '<span class="sub' + (s[1] ? ' long' : '') + '">' + s[0] + '</span>') : '') + (s[2] ? '<span class="sub court">' + s[2] + '</span>' : '') + (s[3] ? '<span class="sub mob">' + s[3] + '</span>' : '');
        b.style.background = M.bg ? M.bg(z) : ''; b.style.opacity = M.dim && M.dim(z) ? 0.4 : '';
        b.setAttribute('aria-label', vide ? 'case de la période ' + position(z)[0] + ', colonne ' + position(z)[1] : EL[z][1] + ', Z = ' + z);
      });
      leg.innerHTML = M.leg || '';
    };
    T.select = function (z) {
      sel = z; Object.keys(cells).forEach(function (k) { cells[k].classList.toggle('nt-on', +k === z); });
      if (info) { info.firstChild.innerHTML = atomeSVG(z); info.lastChild.innerHTML = fiche(z, mode); }
    };
    T.mark = function (z, style) { var b = cells[z]; if (b) { b.style.boxShadow = style || ''; } };
    T.clear = function () { Object.keys(cells).forEach(function (k) { cells[k].style.boxShadow = ''; cells[k].classList.remove('nt-on'); }); };
    T.setMode = function (m) { mode = m; T.render(); if (sel) { T.select(sel); } };
    $$(zone, '.nt-seg input').forEach(function (r) { r.addEventListener('change', function () { T.setMode(r.value); }); });
    T.render(); if (opt.select) { T.select(opt.select); }
    return T;
  }
  $$(document, '.nt-tp').forEach(function (lab) {
    var modes = (lab.getAttribute('data-modes') || 'config').split(','), first = { nobles: 10, ions: 11, liaisons: 6, valence: 16, condensee: 16, periodes: 16 }[modes[0]];
    Tableau($(lab, '.nt-tp-zone'), { modes: modes, select: first });
  });

  /* =================== 4. Entraînement : de la configuration à la case =================== */
  (function () {
    var root = document.getElementById('tr-place'); if (!root) { return; }
    var vis = $(root, '.nt-qvis'), qEl = $(root, '.nt-tr-q'), zone = $(root, '.nt-tr-ans'), inp = $(root, 'input[type="text"]'), bC = $(root, '[data-act="check"]'), prev = $(root, '.nt-tr-prev'), tz = $(root, '.nt-tp-zone');
    var Q = [], cur = null, T = Tableau(tz, { modes: ['vide'], info: false, onPick: function (z) { pick(z); } });
    function regle(z) {
      var cf = config(z), m = nmax(cf), last = cf[cf.length - 1], p = position(z), h = 'n&nbsp;=&nbsp;' + m + '&nbsp;: ' + m + '<sup>e</sup>&nbsp;ligne&nbsp;; ';
      if (z === 2) { h += '1s<sup>2</sup>&nbsp;: c\u2019est l\u2019hélium, placé dans la 18<sup>e</sup>&nbsp;colonne avec les gaz nobles.'; }
      else if (last[2] === 's') { h += 's<sup>' + last[3] + '</sup>&nbsp;: ' + last[3] + '<sup>' + (last[3] === 1 ? 're' : 'e') + '</sup>&nbsp;colonne.'; }
      else { h += 'p<sup>' + last[3] + '</sup>&nbsp;: 12&nbsp;+&nbsp;' + last[3] + '&nbsp;=&nbsp;' + p[1] + '<sup>e</sup>&nbsp;colonne.'; }
      return h + ' C\u2019est ' + (/^[aeéèiouyh]/i.test(EL[z][1]) ? 'l\u2019' : 'le ') + EL[z][1] + ' (' + EL[z][0] + ').';
    }
    function valHTML(z) { var cf = config(z), m = nmax(cf); return cfgHTML(cf.filter(function (c) { return c[1] === m; })); }
    var S = Serie(root, 6, {
      init: function () { var zs = shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]).slice(0, 6); Q = zs.map(function (z, i) { return { z: z, type: i % 2 ? 'B' : 'A' }; }); shuffle(Q); },
      show: function (k) {
        cur = Q[k]; T.clear(); inp.value = ''; prev.innerHTML = ''; tz.hidden = false;
        if (cur.type === 'A') { vis.innerHTML = valHTML(cur.z); qEl.innerHTML = 'Les électrons de valence d\u2019un élément ont cette configuration. Cliquez sur sa case.'; zone.hidden = true; }
        else { vis.innerHTML = '?'; qEl.innerHTML = 'Quelle est la configuration des électrons de valence de l\u2019élément de la case entourée&nbsp;?'; zone.hidden = false; bC.disabled = false; T.mark(cur.z, '0 0 0 3px #2A6BC4'); }
      },
      bilan: function (g, t0) { vis.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;6</span>'; qEl.innerHTML = t0; zone.hidden = true; tz.hidden = true; prev.innerHTML = ''; }
    });
    function pick(z) {
      if (!cur || cur.type !== 'A' || S.answered || S.fini) { return; }
      var ok = z === cur.z; T.mark(z, '0 0 0 3px ' + (ok ? '#16A34A' : '#E11D48')); if (!ok) { T.mark(cur.z, '0 0 0 3px #16A34A'); }
      S.answer(ok, regle(cur.z));
    }
    inp.addEventListener('input', function () { var p = parseCfg(inp.value); prev.innerHTML = inp.value.trim() ? (p ? 'Aperçu&nbsp;: ' + parseHTML(p) : 'Écriture non reconnue&nbsp;: par exemple <code>3s2 3p4</code>.') : ''; });
    function check() {
      if (!cur || cur.type !== 'B' || S.answered || S.fini) { return; }
      var p = parseCfg(inp.value); if (!p) { S.say('Écriture non reconnue&nbsp;: tapez par exemple <code>3s2 3p4</code>.'); return; }
      var v = verifCfg(p, cur.z, true), complet = verifCfg(p, cur.z, false)[0];
      var h = 'Électrons de valence&nbsp;: ' + valHTML(cur.z) + '. En effet, ' + regle(cur.z).replace(/ C\u2019est .*$/, '') + ' L\u2019élément est ' + (/^[aeéèiouyh]/i.test(EL[cur.z][1]) ? 'l\u2019' : 'le ') + EL[cur.z][1] + '.';
      if (complet) { h = 'Votre configuration est juste, mais c\u2019est la configuration complète&nbsp;: on ne demandait que les électrons de valence, ' + valHTML(cur.z) + '.'; }
      bC.disabled = true; S.answer(v[0] || complet, (v[0] ? '' : (complet ? '' : v[1] + ' ')) + h, complet ? '<b>D\u2019accord.</b> ' : null);
    }
    bC.addEventListener('click', check); inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { check(); } });
    S.start();
  })();

  /* =================== 5. De l'atome à l'ion =================== */
  (function () {
    var root = document.getElementById('lab-ion'); if (!root) { return; }
    var pk = $(root, '.nt-picker'), msg = $(root, '.nt-msg'), bI = $(root, '[data-act="ion"]');
    var LISTE = [1, 3, 11, 19, 12, 20, 13, 8, 16, 9, 17], Z = 11, phase = 0, t = 0, cnv;
    function formule(q) { return EL[Z][0] + (q === 0 ? '' : (q === 1 ? '\u207A' : (q === -1 ? '\u207B' : ['', '', '\u00B2', '\u00B3'][Math.abs(q)] + (q > 0 ? '\u207A' : '\u207B')))); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, I = ION[Z], q = I[1], ne = Z - q; ctx.clearRect(0, 0, W, H);
      var bg = ctx.createRadialGradient(W / 2, H / 2, 10, W / 2, H / 2, Math.max(W, H) * 0.7); bg.addColorStop(0, '#FFFFFF'); bg.addColorStop(1, '#EEF2F7'); ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
      var cx = W / 2, cy = H / 2 + 8, R = Math.min(H * 0.37, W * 0.3), cf0 = config(Z), cf1 = config(ne), N = Math.max(nmax(cf0), 1);
      var ray = []; for (var k = 1; k <= 4; k++) { ray.push(R * (0.32 + 0.68 * (k - 1) / Math.max(1, N - 1))); }
      if (N === 1) { ray[0] = R * 0.55; }
      var u = phase === 0 ? 0 : Math.min(1, t / 1.2), e = u * u * (3 - 2 * u), re = Math.max(4.2, R * 0.045);
      if (q > 0) {   /* cation : les électrons de valence s'éloignent et disparaissent */
        var P = positionsElectrons(cf0, cx, cy, ray), n0 = P.length;
        if (phase === 2) { dessineAtome(ctx, cx, cy, ray, Z, cf1, { couches: nmax(cf1) || 1, re: re }); }
        else {
          var P2 = P.map(function (p, i) { if (i < n0 - q) { return p; } var f = 1 + 0.6 * e; return { x: cx + (p.x - cx) * f, y: cy + (p.y - cy) * f, n: p.n, t: p.t }; });
          dessineAtome(ctx, cx, cy, ray, Z, cf0, { couches: N, pos: P2, re: re, opacite: function (i) { return i < n0 - q ? 1 : 1 - e; } });
        }
      } else {   /* anion : des électrons arrivent de l'extérieur */
        var F = positionsElectrons(cf1, cx, cy, ray), m0 = F.length + q, A = F.map(function (p, i) { if (i < m0 || phase === 2) { return p; } var sx = W + 20, sy = cy + (i - m0 - 0.5) * 50; return { x: sx + (p.x - sx) * e, y: sy + (p.y - sy) * e, n: p.n, t: p.t }; });
        dessineAtome(ctx, cx, cy, ray, Z, phase === 0 ? cf0 : cf1, { couches: N, pos: phase === 0 ? positionsElectrons(cf0, cx, cy, ray) : A, re: re });
      }
      /* compteurs et formule */
      var nel = phase === 2 ? ne : Z, fin = phase === 2;
      pill(ctx, Z + '\u00A0proton' + (Z > 1 ? 's' : ''), 12, 20, { size: 12.5, col: '#BE123C', bg: '#FFE4E6', align: 'left' });
      pill(ctx, nel + '\u00A0électron' + (nel > 1 ? 's' : ''), 12, 46, { size: 12.5, col: '#1D4ED8', bg: '#DBEAFE', align: 'left' });
      var col = fin ? (q > 0 ? '#BE123C' : '#1D4ED8') : NAVY;
      pill(ctx, formule(fin ? q : 0), W - 12, 26, { size: 24, serif: true, col: col, bg: '#FFFFFF', stroke: fin ? col : GRID2, align: 'right' });
      txt(ctx, fin ? (q > 0 ? 'cation' : 'anion') : 'atome', W - 12, 56, { size: 11.5, col: SLATE, align: 'right' });
    }
    function texte() {
      var I = ION[Z], q = I[1], ne = Z - q, cf0 = config(Z), cf1 = config(ne), nm = EL[Z][1], art = /^[aeéèiouyh]/i.test(nm) ? 'd\u2019' : 'de ';
      if (phase === 0) { msg.innerHTML = '<b>Atome ' + art + nm + '</b><br>' + Z + '&nbsp;électron' + (Z > 1 ? 's' : '') + '&nbsp;: ' + cfgHTML(cf0, { val: true }) + ', dont ' + nval(Z) + '&nbsp;électron' + (nval(Z) > 1 ? 's' : '') + ' de valence.<br>Comment atteindre la configuration d\u2019un gaz noble&nbsp;?'; return; }
      if (phase === 1) { msg.innerHTML = q > 0 ? 'L\u2019atome perd ' + (q > 1 ? 'ses ' + q + '&nbsp;électrons' : 'son électron') + ' de valence…' : 'L\u2019atome gagne ' + (-q) + '&nbsp;électron' + (q < -1 ? 's' : '') + '…'; return; }
      var h = '<b>' + I[2].charAt(0).toUpperCase() + I[2].slice(1) + ' ' + I[0] + '</b><br>';
      h += ne ? ne + '&nbsp;électron' + (ne > 1 ? 's' : '') + '&nbsp;: ' + cfgHTML(cf1, { couleur: true }) + ', la configuration ' + nomGazDe(ne) + '.<br>' : 'Plus aucun électron&nbsp;: il ne reste que le noyau, un simple proton.<br>';
      h += 'Charge&nbsp;: ' + Z + '&nbsp;proton' + (Z > 1 ? 's' : '') + ' \u2212 ' + ne + '&nbsp;électron' + (ne > 1 ? 's' : '') + ' = ' + (q > 0 ? '+' : '\u2212') + Math.abs(q) + '&nbsp;charge' + (Math.abs(q) > 1 ? 's' : '') + ' élémentaire' + (Math.abs(q) > 1 ? 's' : '') + '.';
      msg.innerHTML = h;
    }
    var loop = Loop(root, function (dt) { t += dt; if (phase === 1 && t >= 1.2) { phase = 2; texte(); } draw(cnv); return phase === 1; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 280 : 320; }, draw);
    LISTE.forEach(function (z) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn'; b.textContent = EL[z][0]; b.setAttribute('aria-label', EL[z][1]); b.setAttribute('aria-pressed', String(z === Z));
      b.addEventListener('click', function () { Z = z; phase = 0; bI.disabled = false; $$(pk, 'button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); texte(); draw(cnv); });
      pk.appendChild(b);
    });
    bI.addEventListener('click', function () { if (phase !== 0) { return; } if (RM) { phase = 2; bI.disabled = true; texte(); draw(cnv); return; } phase = 1; t = 0; bI.disabled = true; texte(); loop.kick(); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { phase = 0; bI.disabled = false; texte(); draw(cnv); });
    texte(); draw(cnv);
  })();

  /* =================== quiz à choix (ions, puis quiz final) =================== */
  function Quiz(root, BANQUE, nb) {
    var qEl = $(root, '.nt-ql-q'), bx = $(root, '.nt-ql-btns'), Q = [];
    var S = Serie(root, nb, {
      init: function () { Q = shuffle(BANQUE.slice()).slice(0, nb); },
      show: function (k) {
        var q = Q[k], ordre = shuffle(q[1].map(function (_, i) { return i; })); qEl.innerHTML = q[0]; bx.innerHTML = ''; bx.hidden = false;
        ordre.forEach(function (i) {
          var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn nt-choix'; b.innerHTML = q[1][i]; b.setAttribute('data-i', i);
          b.addEventListener('click', function () {
            if (S.answered) { return; } var ok = i === 0;
            b.classList.add(ok ? 'nt-choix-ok' : 'nt-choix-ko'); if (!ok) { $(bx, '[data-i="0"]').classList.add('nt-choix-ok'); }
            S.answer(ok, q[2], ok ? null : '<b>Non.</b> ');
          });
          bx.appendChild(b);
        });
        typeset(bx);   /* les réponses peuvent contenir des formules */
      },
      bilan: function (g, t0) { qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;' + nb + '</span><br>' + (g / nb >= 0.85 ? 'Excellent&nbsp;!' : 'Relisez les explications des questions manquées, puis recommencez&nbsp;: les questions seront mélangées.'); bx.innerHTML = ''; bx.hidden = true; }
    });
    S.start();
  }
  (function () {   /* la bonne réponse est toujours la première de la liste ; l'ordre affiché est mélangé */
    var root = document.getElementById('quiz-ions'); if (!root) { return; }
    var M = '\u2212';
    Quiz(root, [
      ['Quelle est la formule de l\u2019ion sodium&nbsp;?', ['Na<sup>+</sup>', 'Na<sup>' + M + '</sup>', 'Na<sup>2+</sup>', 'So<sup>+</sup>'], 'Le sodium (colonne 1) perd son unique électron de valence&nbsp;: Na<sup>+</sup>.'],
      ['Quelle est la formule de l\u2019ion chlorure&nbsp;?', ['Cl<sup>' + M + '</sup>', 'Cl<sup>+</sup>', 'Cl<sup>2' + M + '</sup>', 'Cl<sub>2</sub>'], 'Le chlore (colonne 17) gagne un électron pour avoir la configuration de l\u2019argon&nbsp;: Cl<sup>' + M + '</sup>.'],
      ['Quelle est la formule de l\u2019ion calcium&nbsp;?', ['Ca<sup>2+</sup>', 'Ca<sup>+</sup>', 'Ca<sup>2' + M + '</sup>', 'C<sup>2+</sup>'], 'Le calcium est dans la colonne 2&nbsp;: il perd ses 2 électrons de valence, Ca<sup>2+</sup>.'],
      ['Quelle est la formule de l\u2019ion magnésium&nbsp;?', ['Mg<sup>2+</sup>', 'Mg<sup>+</sup>', 'Mn<sup>2+</sup>', 'Mg<sup>2' + M + '</sup>'], 'Le magnésium (colonne 2) perd 2 électrons&nbsp;: Mg<sup>2+</sup>, de configuration celle du néon.'],
      ['Quelle est la formule de l\u2019ion fluorure&nbsp;?', ['F<sup>' + M + '</sup>', 'F<sup>+</sup>', 'Fl<sup>' + M + '</sup>', 'F<sup>2' + M + '</sup>'], 'Le fluor (colonne 17) gagne un électron&nbsp;: F<sup>' + M + '</sup>, de configuration celle du néon.'],
      ['Quelle est la formule de l\u2019ion potassium&nbsp;?', ['K<sup>+</sup>', 'P<sup>+</sup>', 'K<sup>2+</sup>', 'K<sup>' + M + '</sup>'], 'Le potassium, de symbole K, est un alcalin (colonne 1)&nbsp;: K<sup>+</sup>.'],
      ['Quelle est la formule de l\u2019ion hydrogène&nbsp;?', ['H<sup>+</sup>', 'H<sup>' + M + '</sup>', 'H<sub>2</sub>', 'He<sup>+</sup>'], 'L\u2019atome d\u2019hydrogène perd son unique électron&nbsp;: H<sup>+</sup>, un simple proton.'],
      ['Comment s\u2019appelle l\u2019ion Cl<sup>' + M + '</sup>&nbsp;?', ['ion chlorure', 'ion chlore', 'ion chlorate'], 'Les anions monoatomiques prennent la terminaison -ure&nbsp;: ion chlorure.'],
      ['Comment s\u2019appelle l\u2019ion K<sup>+</sup>&nbsp;?', ['ion potassium', 'ion phosphore', 'ion krypton'], 'K est le symbole du potassium (du latin <i>kalium</i>)&nbsp;: ion potassium.'],
      ['Comment s\u2019appelle l\u2019ion F<sup>' + M + '</sup>&nbsp;?', ['ion fluorure', 'ion fluor', 'ion fer'], 'Les anions monoatomiques prennent la terminaison -ure&nbsp;: ion fluorure.'],
      ['Le lithium est dans la 1<sup>re</sup>&nbsp;colonne. Quel ion forme-t-il&nbsp;?', ['Li<sup>+</sup>', 'Li<sup>' + M + '</sup>', 'Li<sup>2+</sup>'], 'Configuration 1s<sup>2</sup>&nbsp;2s<sup>1</sup>&nbsp;: en perdant son électron de valence, il prend la configuration de l\u2019hélium.'],
      ['Le soufre est dans la 16<sup>e</sup>&nbsp;colonne. Quel ion forme-t-il&nbsp;?', ['S<sup>2' + M + '</sup>', 'S<sup>2+</sup>', 'S<sup>6+</sup>'], 'Il lui manque 2 électrons pour avoir la configuration de l\u2019argon&nbsp;: S<sup>2' + M + '</sup>, l\u2019ion sulfure.'],
      ['L\u2019aluminium est dans la 13<sup>e</sup>&nbsp;colonne. Quel ion forme-t-il&nbsp;?', ['Al<sup>3+</sup>', 'Al<sup>3' + M + '</sup>', 'Al<sup>+</sup>'], 'Il perd ses 3 électrons de valence (3s<sup>2</sup>&nbsp;3p<sup>1</sup>) et prend la configuration du néon&nbsp;: Al<sup>3+</sup>.'],
      ['Combien d\u2019électrons possède l\u2019ion Mg<sup>2+</sup> (<i>Z</i>&nbsp;=&nbsp;12)&nbsp;?', ['10', '12', '14'], 'Il a perdu 2 électrons&nbsp;: 12 \u2212 2 = 10 électrons, comme le néon.']
    ], 10);
  })();

  /* =================== 6. Schémas de Lewis interactifs =================== */
  var NOMS_AT = { H: 'hydrogène', C: 'carbone', O: 'oxygène', F: 'fluor', Si: 'silicium', S: 'soufre', Cl: 'chlore' };
  var GAZ_AT = { H: 'l\u2019hélium (2 électrons)', C: 'le néon', O: 'le néon', F: 'le néon', Si: 'l\u2019argon', S: 'l\u2019argon', Cl: 'l\u2019argon' };
  function bilanAtome(svg, k) {
    var nb = 0, nl = 0;
    $$(svg, '.lw-b').forEach(function (g) { if (g.getAttribute('data-a') === k || g.getAttribute('data-b') === k) { nb += +g.getAttribute('data-o'); } });
    $$(svg, '.lw-lp').forEach(function (l) { if (l.getAttribute('data-at') === k) { nl++; } });
    return [nb, nl];
  }
  function deNom(nm) { return (/^[aeéèiouyh]/i.test(nm) ? 'd\u2019' : 'de ') + nm; }
  function deDoublets(n) { return n + '&nbsp;doublet' + (n > 1 ? 's' : ''); }
  $$(document, '.nt-lewis').forEach(function (root) {
    var svg = $(root, 'svg.nt-lw'), msg = $(root, '.nt-msg'), bCol = $(root, '[data-act="colorer"]'), choisi = null;
    function efface() { svg.classList.remove('lw-focus'); $$(svg, '.lw-sel').forEach(function (e) { e.classList.remove('lw-sel'); }); }
    function choisit(k) {
      efface(); if (choisi === k) { choisi = null; msg.textContent = 'Cliquez sur un atome pour voir les doublets qui l\u2019entourent.'; return; }
      choisi = k; svg.classList.add('lw-focus');
      var t = $(svg, 'text[data-at="' + k + '"]'), el = t.textContent; t.classList.add('lw-sel');
      $$(svg, '.lw-b').forEach(function (g) { if (g.getAttribute('data-a') === k || g.getAttribute('data-b') === k) { g.classList.add('lw-sel'); } });
      $$(svg, '.lw-lp').forEach(function (l) { if (l.getAttribute('data-at') === k) { l.classList.add('lw-sel'); } });
      var b = bilanAtome(svg, k), tot = b[0] + b[1];
      msg.innerHTML = 'Autour de cet atome ' + deNom(NOMS_AT[el]) + '&nbsp;: ' + deDoublets(b[0]) + ' liant' + (b[0] > 1 ? 's' : '') + (b[1] ? ' et ' + deDoublets(b[1]) + ' non liant' + (b[1] > 1 ? 's' : '') : '') + ', soit ' + deDoublets(tot) + ' et ' + 2 * tot + '&nbsp;électrons, comme ' + GAZ_AT[el] + '.';
    }
    $$(svg, '.lw-at').forEach(function (t) {
      var k = t.getAttribute('data-at'); t.setAttribute('tabindex', '0'); t.setAttribute('role', 'button'); t.setAttribute('aria-label', 'atome ' + deNom(NOMS_AT[t.textContent]));
      t.addEventListener('click', function () { choisit(k); });
      t.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); choisit(k); } });
    });
    bCol.addEventListener('click', function () {
      efface(); choisi = null; var on = svg.classList.toggle('lw-col'), nb = 0, nl = $$(svg, '.lw-lp').length;
      $$(svg, '.lw-b').forEach(function (g) { nb += +g.getAttribute('data-o'); });
      bCol.setAttribute('aria-pressed', String(on));
      if (on) { msg.innerHTML = '<b style="color:#B45309">' + nb + '&nbsp;doublets liants</b> et <b style="color:#0369A1">' + nl + '&nbsp;doublets non liants</b>&nbsp;: ' + (nb + nl) + '&nbsp;doublets, soit ' + 2 * (nb + nl) + '&nbsp;électrons.'; }
      else { msg.textContent = 'Cliquez sur un atome pour voir les doublets qui l\u2019entourent.'; }
    });
  });

  /* =================== 7. Choisir le bon schéma de Lewis =================== */
  (function () {
    var root = document.getElementById('lab-cand'); if (!root) { return; }
    var msg = $(root, '.nt-msg');
    $$(root, '.nt-cand button').forEach(function (bt) {
      bt.addEventListener('click', function () {
        var svg = $(bt, 'svg'), fautes = [], ok = true;
        $$(svg, '.lw-at').forEach(function (t) {
          var k = t.getAttribute('data-at'), el = t.textContent, b = bilanAtome(svg, k), tot = b[0] + b[1], bon = el === 'H' ? (tot === 1 && b[1] === 0) : tot === 4;
          t.classList.toggle('lw-good', bon); t.classList.toggle('lw-bad', !bon);
          if (!bon) { ok = false; fautes.push('l\u2019atome ' + deNom(NOMS_AT[el]) + ' entouré de ' + deDoublets(tot) + ' (' + 2 * tot + '&nbsp;électrons)'); }
        });
        bt.classList.toggle('ok', ok); bt.classList.toggle('ko', !ok);
        msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko');
        msg.innerHTML = ok ? '<b>Bravo&nbsp;!</b> Dans le schéma ' + bt.getAttribute('data-c') + ', le carbone et les deux oxygènes sont entourés de 4&nbsp;doublets, et chaque hydrogène d\u2019un seul doublet liant&nbsp;: chaque atome a la configuration du gaz noble qui le suit. C\u2019est le schéma de l\u2019acide méthanoïque, H\u2013COOH.'
          : '<b>Non.</b> Dans le schéma ' + bt.getAttribute('data-c') + ', il y a ' + fautes.join(', et ') + '&nbsp;: on attend 4&nbsp;doublets autour de C et de O, et 1 seul autour de H.';
      });
    });
  })();

  /* =================== 8. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    function c(s) { return '<span class="nt-cfg">' + s.replace(/(\d)([sp])(\d)/g, '$1$2<sup>$3</sup>') + '</span>'; }
    Quiz(root, [
      ['Combien d\u2019électrons une sous-couche p peut-elle contenir au maximum&nbsp;?', ['6', '2', '8'], 'Une sous-couche s est saturée à 2&nbsp;électrons, une sous-couche p à 6.'],
      ['Quelle est la configuration électronique de l\u2019azote (<i>Z</i>&nbsp;=&nbsp;7)&nbsp;?', [c('1s2 2s2 2p3'), c('1s2 2s5'), c('1s2 2p5')], '7 électrons&nbsp;: 2 dans 1s, 2 dans 2s, les 3 restants dans 2p.'],
      ['Dans quel ordre les sous-couches se remplissent-elles&nbsp;?', ['1s, 2s, 2p, 3s, 3p', '1s, 2p, 2s, 3s, 3p', '1s, 2s, 3s, 2p, 3p'], 'On remplit 1s, puis 2s, puis 2p, puis 3s, puis 3p.'],
      ['Combien le soufre (' + c('1s2 2s2 2p6 3s2 3p4') + ') a-t-il d\u2019électrons de valence&nbsp;?', ['6', '4', '16'], 'Ce sont les électrons de la couche n&nbsp;=&nbsp;3&nbsp;: 2 + 4 = 6.'],
      ['Où se trouve l\u2019élément de configuration de valence ' + c('3s2 3p5') + '&nbsp;?', ['période 3, colonne 17', 'période 5, colonne 3', 'période 3, colonne 15'], 'n&nbsp;=&nbsp;3 donne la ligne, et 12&nbsp;+&nbsp;5 = 17 la colonne&nbsp;: c\u2019est le chlore.'],
      ['Les éléments d\u2019une même colonne…', ['ont la même configuration de valence (au n près) et des propriétés chimiques semblables', 'ont le même nombre d\u2019électrons', 'ont le même nombre de couches'], 'Ils forment une famille chimique&nbsp;: même configuration de valence, propriétés semblables.'],
      ['Pourquoi les gaz nobles sont-ils très peu réactifs&nbsp;?', ['Leur couche de valence est saturée.', 'Ce sont des gaz.', 'Ils n\u2019ont pas d\u2019électrons.'], 'Leur couche de valence est pleine&nbsp;: c\u2019est la configuration électronique la plus stable.'],
      ['Quel ion forme le magnésium (colonne 2)&nbsp;?', ['Mg<sup>2+</sup>', 'Mg<sup>+</sup>', 'Mg<sup>2\u2212</sup>'], 'Il perd ses 2 électrons de valence et prend la configuration du néon.'],
      ['Comment s\u2019appelle l\u2019ion Cl<sup>\u2212</sup>&nbsp;?', ['ion chlorure', 'ion chlore', 'ion chlorate'], 'Les anions monoatomiques prennent la terminaison -ure.'],
      ['De combien de doublets un atome d\u2019oxygène est-il entouré dans un schéma de Lewis&nbsp;?', ['4', '2', '6'], '4 doublets (liants ou non liants), soit 8 électrons, comme le néon.'],
      ['Combien de liaisons covalentes l\u2019azote forme-t-il habituellement&nbsp;?', ['3', '1', '5'], 'Il a 5 électrons de valence&nbsp;: il lui en manque 3 pour en avoir 8, d\u2019où 3 liaisons.'],
      ['Dans un schéma de Lewis, un atome d\u2019hydrogène est entouré de…', ['un seul doublet liant', '4 doublets', 'un doublet non liant'], 'Un doublet, soit 2 électrons comme l\u2019hélium, et c\u2019est toujours un doublet liant.'],
      ['L\u2019énergie de liaison est…', ['l\u2019énergie nécessaire pour rompre la liaison', 'l\u2019énergie de la molécule entière', 'l\u2019énergie d\u2019un électron de valence'], 'C\u2019est l\u2019énergie qu\u2019il faut fournir pour séparer les deux atomes liés.']
    ], 12);
  })();

})();
</script>
