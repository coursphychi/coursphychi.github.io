+++
title = "Changements d'état"
draft = false
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
/* chapitre inertie */
details.nt-d.nt-rep { --c: var(--emerald); --bg: var(--emerald-bg); --c-ink: #065F46; }   /* réponses : même style que les exemples */
.nt-duo { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 1em auto; max-width: 560px; }
.nt-carte { display: flex; flex-direction: column; align-items: center; gap: 0.2em; padding: 0.8em 0.6em; border-radius: 16px; text-align: center; font-size: 0.95em; }
.nt-carte-s { background: linear-gradient(180deg, #FEF3C7, #FFFBEB); border: 1.5px solid #FCD34D; } .nt-carte-t { background: linear-gradient(180deg, #DBEAFE, #EFF6FF); border: 1.5px solid #93C5FD; }
.nt-carte .nt-emo { font-size: 2.6em; line-height: 1.1; } .nt-carte b { color: var(--navy); }
.nt-m { color: #2563EB; font-weight: 700; } .nt-depl { color: #059669; font-weight: 700; }
.nt-checklist { list-style: none; padding-left: 0.2em; margin: 0.4em 0; }
.nt-checklist li { margin: 0.35em 0; color: #9A3412; } .nt-checklist label { display: flex; gap: 0.6em; align-items: flex-start; cursor: pointer; }
.nt-checklist input { margin-top: 0.35em; accent-color: #EA580C; width: 1.05em; height: 1.05em; flex: none; }
.nt-predi { margin: 0.6em auto; max-width: 640px; padding: 0.6em 0.9em; border-radius: 12px; background: #FFF7ED; border: 1.5px dashed #FDBA74; text-align: center; }
.nt-predi p { margin: 0 0 0.4em !important; font-weight: 600; color: #9A3412; }
.nt-predi .nt-btn[aria-pressed="true"] { background: #EA580C; border-color: #EA580C; color: #fff; }
.nt-predi.fait { background: #F8FAFC; border-color: var(--line); } .nt-predi.fait p { color: var(--ink); }
.nt-predi .nt-btn:disabled { opacity: 0.45; cursor: default; }
.nt-predi-res { display: flex; gap: 0.8em; align-items: center; max-width: 640px; margin: 0.8em auto 0.2em; padding: 0.75em 1em; border-radius: 14px; font-size: 1.02em; }
.nt-predi-res > i { font-size: 2em; flex: none; } .nt-predi-res div { display: flex; flex-direction: column; gap: 0.15em; } .nt-predi-res b { font-size: 1.12em; }
.nt-predi-res.ok { background: #DCFCE7; border: 2px solid #22C55E; color: #14532D; } .nt-predi-res.ok > i { color: #16A34A; }
.nt-predi-res.ko { background: #FFE4E6; border: 2px solid #F43F5E; color: #881337; } .nt-predi-res.ko > i { color: #E11D48; }
.nt-piege { margin: 0.6em auto 0.2em; max-width: 680px; }
.nt-dirs { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 1em 0; }
@media (max-width: 560px) { .nt-dirs { grid-template-columns: 1fr; } }
.nt-dir { display: flex; flex-direction: column; gap: 0.45em; padding: 0.9em 1em; border-radius: 16px; font-size: 0.95em; line-height: 1.5; }
.nt-dir > b { font-size: 1.05em; } .nt-dir span:not(.nt-dir-res)::before { content: "→ "; font-weight: 700; }
.nt-dir-h { background: linear-gradient(180deg, #ECFDF5, #F8FFFC); border: 1.5px solid #6EE7B7; } .nt-dir-h > b, .nt-dir-h b { color: #047857; }
.nt-dir-v { background: linear-gradient(180deg, #FFF1F2, #FFFAFA); border: 1.5px solid #FDA4AF; } .nt-dir-v > b, .nt-dir-v b { color: #BE123C; }
.nt-dir-res { margin-top: auto; align-self: center; padding: 0.3em 0.9em; border-radius: 999px; font-weight: 700; font-size: 0.92em; text-align: center; }
.nt-dir-h .nt-dir-res { background: #047857; color: #fff; } .nt-dir-v .nt-dir-res { background: #BE123C; color: #fff; }
.nt-cadre-def { display: inline-block; padding: 0.45em 1.4em; border-radius: 18px; background: linear-gradient(135deg, #3F2E9E, #6B5BD2); box-shadow: 0 2px 8px rgba(63,46,158,0.35); color: #FFFFFF; }   /* même style que l'étiquette « Définition » */
.nt-cadre { display: inline-block; padding: 0.35em 1.1em; border-radius: 14px; background: #FFFFFF; border: 2px solid #93C5FD; box-shadow: 0 3px 10px rgba(30,78,156,0.12); }
p:has(> mjx-container) { overflow-x: auto; overflow-y: hidden; }   /* une formule trop longue défile sur téléphone au lieu d'élargir la page */
p.nt-big { overflow-x: auto; overflow-y: hidden; max-width: 100%; }
mjx-container[display="true"] { overflow-x: auto; overflow-y: hidden; max-width: 100%; padding: 2px 0; }
.nt-principe { position: relative; margin: 1.4em 0; padding: 1em 1.3em; border-radius: 14px; border: 3px solid #FF42A1; background: linear-gradient(180deg, #FFF0F7, #FFFFFF); }
.nt-principe .nt-tag { color: #DB2777; }
.nt-force { color: #B42318; font-weight: 700; } .nt-v { color: #C98A00; font-weight: 700; } .nt-dv { color: #6D28D9; font-weight: 700; }
.nt-barre { text-decoration: line-through; text-decoration-thickness: 2px; }
.nt-equiv { display: grid; grid-template-columns: auto auto auto; gap: 0.3em 0.8em; justify-content: center; align-items: center; font-size: 1.1em; margin: 0.6em 0; }
.nt-chips { display: flex; flex-wrap: wrap; gap: 0.45em; justify-content: center; margin: 0.6em 0; }
.nt-chip { border: 1.5px solid var(--line); border-radius: 999px; padding: 0.3em 0.8em; background: #fff; cursor: pointer; font: inherit; font-size: 0.92em; color: var(--ink); }
.nt-chip[aria-pressed="true"] { background: var(--blue); border-color: var(--blue); color: #fff; }
.nt-chip.ok { border-color: #16A34A; background: #DCFCE7; color: #14532D; } .nt-chip.ko { border-color: #E11D48; background: #FFE4E6; color: #881337; }
.nt-types { display: flex; flex-direction: column; gap: 0.5em; align-items: center; margin: 0.6em 0; }
.nt-types .nt-ty { display: flex; gap: 0.7em; align-items: center; flex-wrap: wrap; justify-content: center; padding: 0.35em 0.7em; border-radius: 12px; background: #F8FAFC; border: 1px solid var(--line); }
.nt-types .nt-ty b { min-width: 5.5em; text-align: right; color: var(--navy); }
.nt-types .nt-ty.ok { border-color: #86EFAC; background: #F0FDF4; } .nt-types .nt-ty.ko { border-color: #FDA4AF; background: #FFF1F2; }
.nt-c-f { margin-top: 0.8em; }
.nt-qsvg { display: block; margin: 0.3em auto; max-width: 100%; height: auto; }
details.nt-d pre { overflow-x: auto; margin: 0.6em 0 !important; padding: 0.7em 1em; border-radius: 8px; background: #0F172A; color: #E2E8F0; font-size: 0.85em; line-height: 1.5; }
/* chapitre quantité de matière */
.nt-eq { display: block; width: fit-content; margin: 0.8em auto; padding: 0.5em 1.4em; border-radius: 14px; background: linear-gradient(135deg, #FFF1F2, #FFE4E6); border: 2px solid #FDA4AF; font-size: 1.05em; text-align: center; }
.nt-endo { color: #1D4ED8; font-weight: 700; } .nt-exo { color: #DC2626; font-weight: 700; }
.nt-video { margin: 1em auto; max-width: 640px; } .nt-video video { width: 100%; border-radius: 14px; box-shadow: 0 6px 20px rgba(15,23,42,0.18); }
.nt-h4 { color: var(--navy); font-size: 1.08em; margin: 1.5em 0 0.5em; }
.nt-geant { display: block; text-align: center; font-family: Georgia, "Times New Roman", serif; font-size: clamp(1.1em, 4.2vw, 2.2em); color: #C2410C; letter-spacing: 0.04em; margin: 0.4em 0; overflow-wrap: anywhere; }
.nt-etapes-calc p { margin: 0.35em 0 !important; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Un glaçon qui fond, la buée sur une vitre, la neige carbonique qui «&nbsp;fume&nbsp;»… Une même espèce chimique peut exister sous trois états&nbsp;: solide, liquide ou gazeux. Ce chapitre décrit les passages d'un état à l'autre, ce qui se passe à l'échelle des molécules, et l'énergie qu'ils mettent en jeu.</p>

## Les changements d'état {.nt-h2}

### Trois états, six changements d'état {.nt-h3}

<p>Une espèce chimique peut se trouver à l'état <span class="imp">solide</span>, <span class="imp">liquide</span> ou <span class="imp">gazeux</span>. Le passage d'un état à un autre est un <span class="imp">changement d'état</span>&nbsp;: c'est une <b>transformation <span class="imp">physique</span></b>, car l'espèce chimique reste la même. Chaque changement d'état porte un nom.</p>

<div class="nt-lab" id="lab-triangle">
<p class="nt-tag"><i class="fa-solid fa-diagram-project"></i>Animation</p>
<p class="nt-lab-title">Les changements d'état</p>
<canvas role="img" aria-label="Les trois états, solide, liquide et gaz, reliés par six flèches, une par changement d'état ; un clic sur une flèche affiche son nom et un exemple."></canvas>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="noms" checked> Afficher les noms</label><label class="nt-check"><input type="checkbox" data-in="energie"> Colorer selon l'énergie (voir partie 3)</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Les six changements d'état</p>
<ul class="nt-facts">
<li><b>fusion</b>&nbsp;: solide → liquide&nbsp;; <b>solidification</b>&nbsp;: liquide → solide&nbsp;;</li>
<li><b>vaporisation</b>&nbsp;: liquide → gaz&nbsp;; <b>liquéfaction</b>&nbsp;: gaz → liquide&nbsp;;</li>
<li><b>sublimation</b>&nbsp;: solide → gaz&nbsp;; <b>condensation</b>&nbsp;: gaz → solide.</li>
</ul>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention au mot «&nbsp;condensation&nbsp;»</p>
<p>Le passage de l'état gazeux à l'état solide, la condensation, porte plusieurs noms&nbsp;: condensation, condensation solide, sublimation inverse, déposition, désublimation.</p>
<p>Dans le langage courant, le mot <b>condensation</b> ne désigne pas la même chose qu'en physique&nbsp;: on parle communément de condensation pour le passage de l'état gazeux à l'état <b>liquide</b>, comme la rosée du matin ou la buée sur une vitre. En physique, c'est une <b>liquéfaction</b>.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Évaporation ou ébullition&nbsp;?</p>
<p>La vaporisation peut prendre la forme d'une <b>évaporation</b>, qui se produit à la surface du liquide, ou d'une <b>ébullition</b>, qui se produit dans tout le liquide, avec formation de bulles de vapeur.</p>
<p>Seule l'ébullition se fait à température fixe (pour un corps pur)&nbsp;: on parle alors de <b>température d'ébullition</b>. L'évaporation, elle, se produit à toute température&nbsp;: une flaque d'eau sèche même en hiver.</p>
</div>



<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>La sublimation et la condensation sont plus rares à notre échelle. Le diiode, par exemple, se sublime quand on le chauffe doucement, en dégageant des vapeurs violettes, qui se condensent en cristaux sur une paroi froide&nbsp;:</p>
{{< youtube-plus id="jX9pskbKSw0" ratio="16x9" width="384" shadow=true rounded=true >}}
<p>On peut citer aussi la neige carbonique (dioxyde de carbone solide) qui se sublime en formant un nuage... d'eau. La température du $\ce{CO_2 (g)}$ libéré est très basse&nbsp;: -79°C. À son contact, la vapeur d'eau de l'air se liquéfie, voire se solidifie, formant une brume.
<iframe style="display: block; margin: 1rem auto; border-radius:10px;box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2), 0 4px 6px -4px rgba(0, 0, 0, 0.1);" width="384" height="216" frameborder="0" loading="lazy" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; web-share" allowfullscreen src="https://commons.wikimedia.org/wiki/File:Dry_ice_sublimation_march_29_2021.webm?embedplayer=true" ></iframe>
</div>



### L'équation d'un changement d'état {.nt-h3}

<p>On modélise un changement d'état par une équation, où l'on précise l'état de l'espèce chimique entre parenthèses&nbsp;: <b>(s)</b> pour solide, <b>($\ell$)</b> pour liquide, <b>(g)</b> pour gazeux.</p>

<div class="nt-f">
<p class="nt-f-math"><span>espèce chimique <b>(état 1)</b> $\longrightarrow$ espèce chimique <b>(état 2)</b></span>
</div>

<div class="nt-b nt-warn">
<p><b>L'espèce chimique est la même des deux côtés de la flèche</b>&nbsp;: seul son état change.</p>
</div>


<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemples</p>
<p>Écrire l'équation de la sublimation du dioxyde de carbone $\ce{CO2}$, puis celle de la liquéfaction du méthane $\ce{CH4}$.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Deux équations</span></summary>
<div class="nt-d-body">
<p>Sublimation (solide → gaz)&nbsp;: $\ce{CO2 (s) -> CO2 (g)}$. C'est ce qui se passe avec la «&nbsp;neige carbonique&nbsp;», qui ne fond pas mais disparaît en «&nbsp;fumant&nbsp;».</p>
<p>Liquéfaction (gaz → liquide)&nbsp;: $\ce{CH4 (g) -> CH4 (\ell)}$. Le méthane est ainsi transporté par bateau sous forme liquide, à $-162$&nbsp;°C.</p>
</div>
</details>

<div class="nt-lab nt-quizlab" id="tr-equation">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Nommer et écrire un changement d'état</p>
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

## Modélisation microscopique {.nt-h2}

<p>À l'échelle microscopique, les trois états se distinguent par la disposition et le mouvement des entités (atomes, molécules ou ions), et par l'intensité des liaisons qui les retiennent les unes aux autres.</p>

<div class="nt-lab" id="lab-etats">
<p class="nt-tag"><i class="fa-solid fa-atom"></i>Animation</p>
<p class="nt-lab-title">Les trois états, vus de très près</p>
<canvas role="img" aria-label="Trois récipients : à l'état solide, les molécules sont serrées et rangées, et vibrent sur place ; à l'état liquide, elles sont serrées mais en désordre et glissent les unes sur les autres ; à l'état gazeux, elles sont éloignées et se déplacent rapidement dans tout le récipient."></canvas>
<p class="nt-msg" aria-live="polite">Observez la disposition des molécules et leur mouvement dans chaque état.</p>
</div>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th></th><th>solide</th><th>liquide</th><th>gaz</th></tr></thead>
<tbody>
<tr><td>disposition</td><td><span class="imp nt-hole">compact</span> et <span class="imp nt-hole">ordonné</span></td><td><span class="imp nt-hole">compact</span> et <span class="imp nt-hole">désordonné</span></td><td><span class="imp nt-hole">dispersé</span> et <span class="imp nt-hole">désordonné</span></td></tr>
<tr><td>mouvement</td><td>les entités vibrent autour de positions fixes</td><td>les entités glissent les unes sur les autres</td><td>les entités se déplacent librement, très vite</td></tr>
<tr><td>liaisons entre entités</td><td>énergie de liaison <b>grande</b></td><td>énergie de liaison <b>grande</b>, mais moins que dans le solide</td><td>énergie de liaison <b>faible</b></td></tr>
</tbody>
</table></div>

### Fusion ou dissolution&nbsp;? {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Est-ce que le sucre <b>fond</b> dans le café&nbsp;?</p>
<p class="nt-note">Indice&nbsp;: la température de fusion du saccharose (le sucre de table) est d'environ 186&nbsp;°C, d'après la base de données <a href="https://pubchem.ncbi.nlm.nih.gov/compound/5988">PubChem</a>.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Non&nbsp;: il se dissout</span></summary>
<div class="nt-d-body">
<p>Un café est à moins de 100&nbsp;°C, bien en dessous de la température de fusion du sucre&nbsp;: le sucre ne peut pas fondre. Il se <b>dissout</b>&nbsp;: ses molécules se dispersent parmi les molécules d'eau. Ce n'est pas un changement d'état.</p>
</div>
</details>

<div class="nt-lab" id="lab-dissol">
<p class="nt-tag"><i class="fa-solid fa-cubes-stacked"></i>Animation</p>
<p class="nt-lab-title">Ne pas confondre fusion et dissolution</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="fd" value="fusion" checked><span>Fusion</span></label><label><input type="radio" name="fd" value="dissolution"><span>Dissolution</span></label></div><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Lancer</button></div>
<canvas role="img" aria-label="Fusion : le cristal de sucre, chauffé, devient du sucre liquide, sans eau. Dissolution : les molécules de sucre se dispersent parmi les molécules d'eau."></canvas>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>À ne pas confondre</p>
<p>Lors d'une <b>fusion</b>, une seule espèce chimique passe de l'état solide à l'état liquide&nbsp;: $\ce{C12H22O11 (s) -> C12H22O11 (\ell)}$. Lors d'une <b>dissolution</b>, une espèce chimique se disperse dans un liquide, le solvant&nbsp;; on note (aq) une espèce dissoute dans l'eau&nbsp;: $\ce{C12H22O11 (s) -> C12H22O11 (aq)}$.</p>
</div>

## Transferts thermiques et changements d'état {.nt-h2}

### Chauffer de la glace {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-flask"></i>Expérience</p>
<p>On chauffe 1,0&nbsp;kg d'eau glacée, sortie d'un congélateur à $-18$&nbsp;°C, dans un four à micro-ondes qui fournit à l'eau une puissance $P = \pu{800 W}$. On mesure la température $T$ de l'eau au cours du temps $t$.</p>
<p>À quoi va ressembler la courbe $T = f(t)$&nbsp;?</p>
</div>

<div class="nt-lab" id="lab-chauffe">
<p class="nt-tag"><i class="fa-solid fa-temperature-arrow-up"></i>Animation</p>
<p class="nt-lab-title">Chauffer un kilogramme de glace</p>
<canvas role="img" aria-label="À gauche, l'échantillon d'eau dans le four, à l'état solide, liquide ou gazeux ; à droite, la courbe de la température en fonction du temps, avec deux paliers."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Chauffer</button><button type="button" class="nt-btn" data-act="pause" disabled><i class="fa-solid fa-pause"></i>&nbsp; Pause</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pendant un changement d'état d'un corps pur, la température <span class="imp nt-hole">reste constante</span>, même si l'on continue à fournir de l'énergie&nbsp;: cette énergie sert à changer d'état. <b>Il faut fournir de l'énergie</b> pour faire passer une espèce chimique vers un état moins condensé (fusion, vaporisation, sublimation).</p>
</div>

### Changements d'état endothermiques et exothermiques {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pourquoi a-t-on généralement froid en sortant de la mer ou de la douche&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">L'eau s'évapore… en prenant de l'énergie</span></summary>
<div class="nt-d-body">
<p>L'eau qui couvre la peau s'évapore. Or le passage de l'eau de l'état liquide à l'état gazeux nécessite de l'énergie, que l'eau prend à son environnement, et en particulier à la peau&nbsp;: celle-ci se refroidit. On dit que ce changement d'état est <span class="nt-endo">endothermique</span>.</p>
<p>Le même phénomène permet de rafraîchir une boisson en l'entourant d'un linge mouillé, laissé au soleil ou au vent&nbsp;: en s'évaporant, l'eau du linge prend de l'énergie à la boisson.</p>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Un changement d'état est <span class="imp nt-hole">endothermique</span> s'il nécessite de l'énergie&nbsp;: il en prend à son environnement, qui se refroidit. C'est le cas de la <b>fusion</b>, de la <b>vaporisation</b> et de la <b>sublimation</b>.</p>
<p>Un changement d'état est <span class="imp nt-hole">exothermique</span> s'il libère de l'énergie&nbsp;: il en cède à son environnement, qui se réchauffe. C'est le cas de la <b>solidification</b>, de la <b>liquéfaction</b> et de la <b>condensation</b>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Qu'ont en commun les trois changements d'état endothermiques&nbsp;? Voyez-vous une explication microscopique&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Libérer les entités demande de l'énergie</span></summary>
<div class="nt-d-body">
<p>Ils correspondent tous au passage vers un état <b>moins lié</b>, où les énergies de liaison entre entités sont plus faibles. Or il faut fournir de l'énergie pour rompre, au moins en partie, les liaisons qui retiennent les entités les unes aux autres.</p>
<p>À l'inverse, lors d'une liquéfaction, d'une solidification ou d'une condensation, des liaisons se forment entre les entités&nbsp;: de l'énergie est <b>libérée</b>. Ces changements d'état sont <span class="nt-exo">exothermiques</span>.</p>
</div>
</details>

<p>Reprenez l'animation du début du chapitre, en cochant «&nbsp;Colorer selon l'énergie&nbsp;»&nbsp;: les flèches qui montent vers un état moins lié sont endothermiques, celles qui descendent sont exothermiques.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La chaudière à condensation</span></summary>
<div class="nt-d-body">
<p>Dans une chaudière classique, les fumées chaudes contiennent de la vapeur d'eau, qui s'échappe par la cheminée. Une chaudière à condensation refroidit ces fumées au contact de l'eau froide du circuit de chauffage&nbsp;: la vapeur d'eau s'y liquéfie, et l'énergie libérée par cette liquéfaction, exothermique, préchauffe l'eau du circuit. Le rendement de la chaudière est ainsi amélioré.</p>
<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 700 290' role='img' aria-label="Chaudière classique : les fumées chaudes, chargées de vapeur d'eau, s'échappent par la cheminée. Chaudière à condensation : l'eau froide du circuit passe dans les fumées, la vapeur d'eau s'y liquéfie et lui cède de l'énergie ; l'eau liquide est évacuée."><defs><linearGradient id='corps-c' x1='0' x2='1'><stop offset='0' stop-color='#E2E8F0'/><stop offset='1' stop-color='#CBD5E1'/></linearGradient><linearGradient id='chaud-c' x1='0' x2='0' y1='0' y2='1'><stop offset='0' stop-color='#FCA5A5'/><stop offset='1' stop-color='#FEF2F2'/></linearGradient></defs><text x='160' y='22' font-size='14' text-anchor='middle' fill='#0F172A' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-weight='700'>chaudière classique</text><rect x='80' y='60' width='160' height='190' rx='14' fill='url(#corps-c)' stroke='#64748B' stroke-width='2'/><rect x='92' y='72' width='136' height='150' rx='8' fill='url(#chaud-c)'/><rect x='145' y='34' width='30' height='28' fill='#94A3B8'/><path d='M112,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M112,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M131,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M131,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M150,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M150,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M169,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M169,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M188,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M188,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M207,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M207,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><text x='160' y='268' font-size='11' text-anchor='middle' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>brûleur (combustible)</text><path d='M60,120 L110,120 L110,150 L140,150 L140,110 L170,110 L170,150 L200,150 L200,110 L260,110' fill='none' stroke='#DC2626' stroke-width='5' stroke-linejoin='round'/><text x='264' y='104' font-size='11' fill='#B91C1C' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>eau chaude</text><text x='480' y='22' font-size='14' text-anchor='middle' fill='#0F172A' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-weight='700'>chaudière à condensation</text><rect x='400' y='60' width='160' height='190' rx='14' fill='url(#corps-c)' stroke='#64748B' stroke-width='2'/><rect x='412' y='72' width='136' height='150' rx='8' fill='url(#chaud-c)'/><rect x='465' y='34' width='30' height='28' fill='#94A3B8'/><path d='M432,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M432,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M451,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M451,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M470,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M470,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M489,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M489,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M508,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M508,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><path d='M527,214 q-6,-10 0,-20 q6,10 0,20 Z' fill='#3B82F6'/><path d='M527,214 q-3,-6 0,-11 q3,5 0,11 Z' fill='#BFDBFE'/><text x='480' y='268' font-size='11' text-anchor='middle' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>brûleur (combustible)</text><path d='M380,120 L430,120 L430,150 L460,150 L460,110 L490,110 L490,150 L520,150 L520,110 L580,110' fill='none' stroke='#DC2626' stroke-width='5' stroke-linejoin='round'/><text x='584' y='104' font-size='11' fill='#B91C1C' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>eau chaude</text><path d='M160,34 q-8,-10 0,-18 q8,-8 0,-16' fill='none' stroke='#94A3B8' stroke-width='3'/><circle cx='150' cy='14' r='2.6' fill='#93C5FD'/><circle cx='170' cy='8' r='2.6' fill='#93C5FD'/><circle cx='158' cy='26' r='2.6' fill='#93C5FD'/><text x='182' y='42' font-size='11' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>fumées chaudes</text><text x='182' y='55' font-size='11' fill='#2563EB' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>+ vapeur d'eau perdue</text><text x='20' y='134' font-size='11' fill='#2563EB' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>eau froide</text><path d='M340,96 L420,96 L420,80 L460,80 L460,96 L480,96' fill='none' stroke='#2563EB' stroke-width='5' stroke-linejoin='round'/><text x='340' y='90' font-size='11' fill='#2563EB' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>eau froide</text><circle cx='430' cy='90' r='2.6' fill='#2563EB'/><circle cx='446' cy='93' r='2.6' fill='#2563EB'/><circle cx='438' cy='102' r='2.6' fill='#2563EB'/><circle cx='452' cy='104' r='2.6' fill='#2563EB'/><circle cx='426' cy='110' r='2.6' fill='#2563EB'/><path d='M560,230 L600,230 L600,262' fill='none' stroke='#2563EB' stroke-width='3'/><path d='M596,256 L600,264 L604,256' fill='#2563EB'/><text x='608' y='262' font-size='11' fill='#2563EB' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>évacuation de</text><text x='608' y='276' font-size='11' fill='#2563EB' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>l'eau liquéfiée</text><path d='M480,34 q-8,-10 0,-18 q8,-8 0,-16' fill='none' stroke='#CBD5E1' stroke-width='3'/><text x='502' y='42' font-size='11' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>fumées refroidies,</text><text x='502' y='55' font-size='11' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>presque sans vapeur</text><text x='570' y='150' font-size='10.5' fill='#1D4ED8' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>la vapeur d'eau</text><text x='570' y='163' font-size='10.5' fill='#1D4ED8' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>se liquéfie et cède</text><text x='570' y='176' font-size='10.5' fill='#1D4ED8' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>de l'énergie à l'eau</text></svg></div>
<p class="nt-note">Ici encore, «&nbsp;condensation&nbsp;» est employé au sens courant&nbsp;: en physique, le passage de la vapeur d'eau à l'eau liquide est une liquéfaction.</p>
</div>
</details>


<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les bouillottes «&nbsp;magiques&nbsp;»</span></summary>
<div class="nt-d-body">
<p>Dans une chaudière classique, les fumées chaudes contiennent de la vapeur d'eau, qui s'échappe par la cheminée. Une chaudière à condensation refroidit ces fumées au contact de l'eau froide du circuit de chauffage&nbsp;: la vapeur d'eau s'y liquéfie, et l'énergie libérée par cette liquéfaction, exothermique, préchauffe l'eau du circuit. Le rendement de la chaudière est ainsi amélioré.</p>
<p>Ces bouillottes contiennent de l'acétate de sodium liquide, à température ambiante, alors que sa température de solidification est de 58&nbsp;°C&nbsp;: il est dans un état instable, dit <b>surfondu</b>. En pliant la petite pastille métallique, on déclenche sa solidification, qui se propage dans toute la bouillotte. Cette solidification est exothermique&nbsp;: la bouillotte chauffe, jusqu'à environ 50&nbsp;°C. Pour la «&nbsp;recharger&nbsp;», on la plonge dans l'eau bouillante, ce qui fait fondre l'acétate de sodium.</p>
</details>





## Énergie massique de changement d'état {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp nt-hole">énergie massique de changement d'état</span> $L$ d'une espèce chimique est l'énergie absorbée (si elle est positive) ou cédée (si elle est négative) lorsque <b>1&nbsp;kg</b> de cette espèce change d'état. Elle s'exprime en <span class="imp nt-hole">$\pu{J*kg-1}$</span>.</p>
</div>

<p>Un changement d'état et son inverse mettent en jeu la même énergie, au signe près&nbsp;:</p>

<div class="nt-f">
<p class="nt-f-math"><span>$L_{\text{état 1}\to\text{état 2}}$ $=$ <b>$-$</b>$L_{\text{état 2}\to\text{état 1}}$</span>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-ul"></i>Explicitement</p>
<ul class="nt-facts">
<li><b>$L_\text{vaporisation} = -L_\text{liquéfaction}$</b></li>
<li><b>$L_\text{sublimation} = -L_\text{condensation}$</b></li>
<li><b>$L_\text{fusion} = -L_\text{solidification}$</b></li>
</ul>
</div>


<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pour l'eau, $L_\text{fus} = \pu{334 kJ*kg-1}$ et $L_\text{vap} = \pu{2265 kJ*kg-1}$. Que vaut l'énergie massique de solidification de l'eau&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">L'opposé de l'énergie massique de fusion</span></summary>
<div class="nt-d-body">
<p>La solidification est l'inverse de la fusion&nbsp;: $L_\text{sol} = -L_\text{fus} = \pu{-334 kJ*kg-1}$. Le signe négatif traduit que la solidification libère de l'énergie&nbsp;: elle est exothermique.</p>
</div>
</details>

<p>Si un échantillon de masse $m$ change d'état, l'énergie thermique échangée est proportionnelle à sa masse&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$Q = m \times L$</p>
<div class="nt-f-units"><span>$Q$&nbsp;: énergie thermique reçue par l'espèce en <b>J</b> (négative si elle est cédée)</span><span>$m$&nbsp;: masse en <b>kg</b></span><span>$L$&nbsp;: énergie massique de changement d'état en <b>J·kg<sup>−1</sup></b></span></div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Que vaut l'énergie thermique $Q$ échangée lorsque 500&nbsp;g de fer fondu se solidifient à 1&nbsp;538&nbsp;°C&nbsp;?</p>
<p>Donnée&nbsp;: énergie massique de fusion du fer, $L_\text{fus} = \pu{247 kJ*kg-1}$.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Environ −124 kJ</span></summary>
<div class="nt-d-body">
<p>$Q = m \times L_\text{sol} = m \times (-L_\text{fus}) = \pu{0,500 kg} \times (\pu{-247 kJ*kg-1}) \approx \pu{-124 kJ}$.</p>
<p>Le signe négatif indique que le fer <b>cède</b> cette énergie à son environnement&nbsp;: la solidification est exothermique.</p>
</div>
</details>

<div class="nt-lab nt-trainer" id="tr-q">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Calculer l'énergie échangée lors d'un changement d'état</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-ans"><span class="nt-champ"><label for="trq-x">$Q$&nbsp;=</label><input id="trq-x" type="text" inputmode="decimal" autocomplete="off"><span class="nt-u">kJ</span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>

## Testez-vous {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-final">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur les changements d'état</p>
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
  function vitTxt(v) { return fmt(Math.abs(v), Math.abs(v) < 10 && Math.abs(v) % 1 ? 1 : 0) + '\u00A0m·s⁻¹'; }
  function decorCampagne(ctx, W, H, sol, sx, cam, k, nuages) {   /* ciel, nuages, champ et arbres (sx : abscisse à l'écran d'une position en m) */
    var g = ctx.createLinearGradient(0, 0, 0, sol); g.addColorStop(0, '#7DD3FC'); g.addColorStop(1, '#E0F2FE'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, sol);
    nuages.forEach(function (n) { var x = ((sx(n[0]) - sx(0)) * 0.25 + n[0] * k) % (W + 200); x = (x + W + 200) % (W + 200) - 100; ctx.fillStyle = 'rgba(255,255,255,0.9)'; ctx.beginPath(); ctx.ellipse(x, n[1] * H, 34, 11, 0, 0, 2 * Math.PI); ctx.ellipse(x + 18, n[1] * H - 7, 18, 10, 0, 0, 2 * Math.PI); ctx.fill(); });
    ctx.fillStyle = '#A7F3D0'; ctx.beginPath(); ctx.moveTo(0, sol); for (var x = 0; x <= W; x += 20) { ctx.lineTo(x, sol - 14 - 8 * Math.sin((x - (sx(0) * 0.5)) / 90)); } ctx.lineTo(W, sol); ctx.fill();
    for (var a = Math.floor((cam - 40) / 8) * 8; a < cam + W / k + 40; a += 8) { var xa = sx(a); if (xa > -30 && xa < W + 30) { ctx.fillStyle = '#92400E'; ctx.fillRect(xa - 2, sol - 30, 4, 30); ctx.fillStyle = '#22C55E'; ctx.beginPath(); ctx.arc(xa, sol - 38, 14, 0, 2 * Math.PI); ctx.arc(xa - 9, sol - 30, 9, 0, 2 * Math.PI); ctx.arc(xa + 9, sol - 30, 9, 0, 2 * Math.PI); ctx.fill(); } }
    var gs = ctx.createLinearGradient(0, sol, 0, H); gs.addColorStop(0, '#D6C29A'); gs.addColorStop(1, '#BFA672'); ctx.fillStyle = gs; ctx.fillRect(0, sol, W, H - sol);
    ctx.fillStyle = 'rgba(120,90,40,0.35)'; for (var p = Math.floor((cam - 20) / 2.5) * 2.5; p < cam + W / k + 20; p += 2.5) { var xp = sx(p); if (xp > -20 && xp < W + 20) { ctx.fillRect(xp, sol + 9, 16, 2.5); } }
  }  var FORCE = '#E5484D', FORCE_T = '#B42318', DV = '#7C3AED', DV_T = '#6D28D9';
  function ciel(ctx, W, H) { var g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#0B1026'); g.addColorStop(1, '#1E293B'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); for (var i = 0; i < 60; i++) { var x = (i * 97.3) % W, y = (i * 53.7) % H; ctx.fillStyle = 'rgba(255,255,255,' + (0.3 + (i % 5) / 8) + ')'; ctx.fillRect(x, y, 1.5, 1.5); } }
  function Prediction(root, avant, question, choix, bon, quand) {   /* « prédire avant d'observer » : boutons de choix, puis bilan après l'observation */
    var d = document.createElement('div'), P = { choix: -1 }; d.className = 'nt-predi';
    d.innerHTML = '<p><i class="fa-solid fa-lightbulb"></i>&nbsp; Avant d\u2019observer, faites une prédiction&nbsp;: ' + question + '</p><div class="nt-btns"></div>';
    var bx = d.querySelector('.nt-btns');
    choix.forEach(function (c, i) { var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn'; b.textContent = c; b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () { if (P.choix >= 0) { return; } P.choix = i; $$(bx, 'button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); x.disabled = x !== b; }); d.classList.add('fait'); if (quand) { quand(i); } }); bx.appendChild(b); });   /* une seule prédiction, définitive */
    avant.parentNode.insertBefore(d, avant);
    P.el = d;
    var res = document.createElement('div'); res.className = 'nt-predi-res'; res.hidden = true; var m = root.querySelector('.nt-msg'); m.parentNode.insertBefore(res, m.nextSibling);   /* verdict, séparé de l'explication et placé dessous */
    P.montrer = function () { if (P.choix < 0 || P.vu) { return; } P.vu = true; var ok = P.choix === bon; res.className = 'nt-predi-res ' + (ok ? 'ok' : 'ko'); res.innerHTML = '<i class="fa-solid fa-' + (ok ? 'circle-check' : 'circle-xmark') + '"></i><div><b>' + (ok ? 'Prédiction confirmée&nbsp;!' : 'Prédiction infirmée') + '</b><span>Vous aviez prédit&nbsp;: «&nbsp;' + choix[P.choix] + '&nbsp;»' + (ok ? '' : '. La bonne réponse&nbsp;: «&nbsp;' + choix[bon] + '&nbsp;».') + '</span></div>'; res.hidden = false; };
    P.cacher = function () {};   /* le verdict, une fois donné, reste affiché */
    P.bilan = function () { if (P.choix < 0) { return ''; } return P.choix === bon ? '<b>Votre prédiction («&nbsp;' + choix[P.choix] + '&nbsp;») était juste&nbsp;!</b>' : '<b>Vous aviez prédit «&nbsp;' + choix[P.choix] + '&nbsp;»</b>&nbsp;: ce n\u2019est pas ce qu\u2019on observe.'; };
    return P;
  }
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

  var ENDO = '#2563EB', EXO = '#DC2626', NEUTRE = '#64748B';
  function molEau(ctx, x, y, r, a) {   /* molécule d'eau : oxygène rouge, deux hydrogènes blancs à 104,5° */
    ctx.save(); ctx.translate(x, y); ctx.rotate(a);
    [-0.912, 0.912].forEach(function (d) { ctx.fillStyle = '#F8FAFC'; ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 0.6; ctx.beginPath(); ctx.arc(Math.sin(d) * r * 1.05, Math.cos(d) * r * 1.05, r * 0.6, 0, 2 * Math.PI); ctx.fill(); ctx.stroke(); });
    var g = ctx.createRadialGradient(-r * 0.3, -r * 0.3, 0.5, 0, 0, r); g.addColorStop(0, '#FCA5A5'); g.addColorStop(1, '#B91C1C'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(0, 0, r, 0, 2 * Math.PI); ctx.fill();
    ctx.restore();
  }

  function becher(ctx, x, y, w, h, avant) {   /* bécher en verre : avant = true pour le fond, false pour les reflets et le contour (dessinés par-dessus le contenu) */
    if (avant) { ctx.fillStyle = 'rgba(224,242,254,0.35)'; rr(ctx, x, y, w, h, 8); ctx.fill(); ctx.fillStyle = 'rgba(15,23,42,0.10)'; ctx.beginPath(); ctx.ellipse(x + w / 2, y + h + 4, w * 0.52, 5, 0, 0, 2 * Math.PI); ctx.fill(); return; }
    ctx.strokeStyle = '#64748B'; ctx.lineWidth = 2.2; ctx.lineJoin = 'round'; ctx.beginPath(); ctx.moveTo(x - 7, y - 4); ctx.quadraticCurveTo(x, y - 2, x, y + 6); ctx.lineTo(x, y + h - 8); ctx.quadraticCurveTo(x, y + h, x + 8, y + h); ctx.lineTo(x + w - 8, y + h); ctx.quadraticCurveTo(x + w, y + h, x + w, y + h - 8); ctx.lineTo(x + w, y); ctx.stroke();   /* bec verseur à gauche */
    ctx.strokeStyle = 'rgba(100,116,139,0.55)'; ctx.lineWidth = 1; for (var g = 1; g <= 4; g++) { var gy = y + h - g * h / 5; ctx.beginPath(); ctx.moveTo(x + w - 4, gy); ctx.lineTo(x + w - (g % 2 ? 12 : 18), gy); ctx.stroke(); }
    ctx.strokeStyle = 'rgba(255,255,255,0.85)'; ctx.lineWidth = 3; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(x + 6, y + 12); ctx.lineTo(x + 6, y + h - 14); ctx.stroke(); ctx.lineCap = 'butt';
  }
  function sucre(ctx, x, y, s, a) {   /* molécule de saccharose stylisée : un cycle à six sommets relié à un cycle à cinq sommets */
    ctx.save(); ctx.translate(x, y); ctx.rotate(a); ctx.fillStyle = '#FEF3C7'; ctx.strokeStyle = '#B45309'; ctx.lineWidth = Math.max(1, s * 0.16); ctx.lineJoin = 'round';
    ctx.beginPath(); for (var i = 0; i < 6; i++) { var an = Math.PI / 6 + i * Math.PI / 3; ctx.lineTo(-s * 0.95 + s * 0.8 * Math.cos(an), s * 0.8 * Math.sin(an)); } ctx.closePath(); ctx.fill(); ctx.stroke();
    ctx.beginPath(); for (i = 0; i < 5; i++) { an = Math.PI + i * 2 * Math.PI / 5; ctx.lineTo(s * 1.0 + s * 0.7 * Math.cos(an), s * 0.7 * Math.sin(an)); } ctx.closePath(); ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#DC2626'; ctx.beginPath(); ctx.arc(-s * 0.1 + s * 0.12, 0, s * 0.18, 0, 2 * Math.PI); ctx.fill();   /* l'atome d'oxygène qui relie les deux cycles */
    ctx.restore();
  }
  function icone(ctx, k, x, y, s) {   /* glaçon, goutte ou nuage */
    ctx.save(); ctx.translate(x, y);
    if (k === 's') { ctx.fillStyle = '#E0F2FE'; ctx.strokeStyle = '#0EA5E9'; ctx.lineWidth = 1.4; rr(ctx, -s, -s, 2 * s, 2 * s, s * 0.35); ctx.fill(); ctx.stroke(); ctx.strokeStyle = 'rgba(255,255,255,0.95)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(-s * 0.5, -s * 0.55); ctx.lineTo(s * 0.2, -s * 0.55); ctx.stroke(); }
    else if (k === 'l') { var g = ctx.createLinearGradient(0, -s, 0, s); g.addColorStop(0, '#7DD3FC'); g.addColorStop(1, '#0284C7'); ctx.fillStyle = g; ctx.beginPath(); ctx.moveTo(0, -s * 1.15); ctx.bezierCurveTo(s * 0.4, -s * 0.5, s, 0, s * 0.85, s * 0.4); ctx.arc(0, s * 0.35, s * 0.85, 0.05, Math.PI - 0.05); ctx.bezierCurveTo(-s, 0, -s * 0.4, -s * 0.5, 0, -s * 1.15); ctx.fill(); }
    else { ctx.fillStyle = '#CBD5E1'; ctx.beginPath(); ctx.arc(-s * 0.55, s * 0.2, s * 0.55, 0, 2 * Math.PI); ctx.arc(s * 0.1, -s * 0.15, s * 0.72, 0, 2 * Math.PI); ctx.arc(s * 0.72, s * 0.22, s * 0.5, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#E2E8F0'; ctx.beginPath(); ctx.arc(s * 0.05, -s * 0.25, s * 0.42, 0, 2 * Math.PI); ctx.fill(); }
    ctx.restore();
  }

  /* =================== 1. Le triangle des changements d'état =================== */
  (function () {
    var root = document.getElementById('lab-triangle'); if (!root) { return; }
    var chkN = $(root, '[data-in="noms"]'), chkE = $(root, '[data-in="energie"]'), msg = $(root, '.nt-msg'), sel = -1, survol = -1, cnv, CH = [];
    var ETATS = { g: ['Gaz', '#EA580C'], l: ['Liquide', '#1D4ED8'], s: ['Solide', '#0E7490'] };
    var T = [   /* départ, arrivée, nom, endothermique ?, exemple, équation */
      ['s', 'l', 'fusion', true, 'un glaçon qui fond', '\\ce{H2O (s) -> H2O (\\ell)}'],
      ['l', 's', 'solidification', false, 'l\u2019eau qui gèle dans le bac à glaçons', '\\ce{H2O (\\ell) -> H2O (s)}'],
      ['l', 'g', 'vaporisation', true, 'l\u2019eau qui bout, ou une flaque qui sèche', '\\ce{H2O (\\ell) -> H2O (g)}'],
      ['g', 'l', 'liquéfaction', false, 'la buée sur une vitre froide, la rosée du matin', '\\ce{H2O (g) -> H2O (\\ell)}'],
      ['s', 'g', 'sublimation', true, 'la «&nbsp;neige carbonique&nbsp;» qui disparaît en fumant', '\\ce{CO2 (s) -> CO2 (g)}'],
      ['g', 's', 'condensation', false, 'le givre qui se forme sur une vitre en hiver', '\\ce{H2O (g) -> H2O (s)}']
    ];
    function pos(o) { var W = o.W, H = o.H, m = Math.min(W - (W < 560 ? 104 : 140), H * 1.3); return { g: [W / 2 - m * 0.38, 40], l: [W / 2 + m * 0.4, H * 0.5], s: [W / 2 - m * 0.38, H - 40] }; }
    function courbe(o, i) {   /* chaque flèche est un arc ; les deux flèches d'une même paire passent de part et d'autre */
      var P = pos(o), t = T[i], a = P[t[0]], b = P[t[1]], mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1], d = Math.hypot(dx, dy), nx = -dy / d, ny = dx / d, c = [mx + nx * 40, my + ny * 40];
      var pts = []; for (var k = 0; k <= 40; k++) { var u = 0.16 + 0.68 * k / 40; pts.push([(1 - u) * (1 - u) * a[0] + 2 * u * (1 - u) * c[0] + u * u * b[0], (1 - u) * (1 - u) * a[1] + 2 * u * (1 - u) * c[1] + u * u * b[1]]); }
      return pts;
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, P = pos(o); ctx.clearRect(0, 0, W, H); var gf = ctx.createRadialGradient(W / 2, H / 2, 20, W / 2, H / 2, Math.max(W, H) * 0.7); gf.addColorStop(0, '#FFFFFF'); gf.addColorStop(1, '#EEF2F7'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      CH = T.map(function (_, i) { return courbe(o, i); });
      T.forEach(function (t, i) {
        var pts = CH[i], col = chkE.checked ? (t[3] ? ENDO : EXO) : NEUTRE, act = i === sel || i === survol;
        ctx.strokeStyle = col; ctx.lineWidth = act ? 4.5 : 2.6; ctx.globalAlpha = sel >= 0 && !act ? 0.45 : 1; ctx.beginPath(); pts.forEach(function (p, k) { if (k) { ctx.lineTo(p[0], p[1]); } else { ctx.moveTo(p[0], p[1]); } }); ctx.stroke();
        var p1 = pts[pts.length - 2], p2 = pts[pts.length - 1]; vec(ctx, p1[0], p1[1], p2[0], p2[1], col, act ? 4.5 : 2.6, act ? 15 : 12);
        ctx.globalAlpha = 1;
      });
      if (chkN.checked) { T.forEach(function (t, i) { var pts = CH[i], col = chkE.checked ? (t[3] ? ENDO : EXO) : NEUTRE, Pp = pos(o), A = Pp[t[0]], B2 = Pp[t[1]], pm = pts[20], ox = pm[0] - (A[0] + B2[0]) / 2, oy = pm[1] - (A[1] + B2[1]) / 2, dd = Math.hypot(ox, oy) || 1, ex = Math.abs(ox / dd) > 0.5 ? (W < 560 ? 30 : 46) : 22, lx = Math.min(W - 46, Math.max(46, pm[0] + ox / dd * ex)), dx = 0, dy = 0, d = 1;   /* étiquette décalée vers l'extérieur de la paire de flèches */ ctx.globalAlpha = sel >= 0 && i !== sel && i !== survol ? 0.5 : 1; pill(ctx, t[2], lx, pm[1] + oy / dd * 14, { size: W < 560 ? 10.5 : 11.5, col: col, stroke: '#E2E8F0' }); ctx.globalAlpha = 1; }); }   /* étiquettes par-dessus les flèches, dans le cadre */
      Object.keys(ETATS).forEach(function (k) { var p = P[k], e = ETATS[k], g = ctx.createLinearGradient(p[0], p[1] - 20, p[0], p[1] + 20); g.addColorStop(0, e[1]); g.addColorStop(1, '#1E293B'); ctx.fillStyle = g; var nw = W < 560 ? 92 : 118, nh = 40; ctx.save(); ctx.shadowColor = 'rgba(15,23,42,0.25)'; ctx.shadowBlur = 10; ctx.shadowOffsetY = 3; ctx.fillStyle = '#FFFFFF'; rr(ctx, p[0] - nw / 2, p[1] - nh / 2, nw, nh, 20); ctx.fill(); ctx.restore(); ctx.strokeStyle = e[1]; ctx.lineWidth = 2.5; rr(ctx, p[0] - nw / 2, p[1] - nh / 2, nw, nh, 20); ctx.stroke(); icone(ctx, k, p[0] - nw / 2 + 20, p[1], 9); txt(ctx, e[0], p[0] + 12, p[1], { size: W < 560 ? 13 : 14.5, col: e[1], bold: true }); });   /* nœud : pastille blanche, icône et nom */
      if (chkE.checked) { pill(ctx, '\u25CF endothermique', W - 8, 14, { size: 11, col: ENDO, align: 'right', stroke: '#BFDBFE' }); pill(ctx, '\u25CF exothermique', W - 8, 36, { size: 11, col: EXO, align: 'right', stroke: '#FECACA' }); }
    }
    function proche(e) { var r = cnv.cv.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top, best = -1, bd = 22; CH.forEach(function (pts, i) { pts.forEach(function (p) { var d = Math.hypot(p[0] - x, p[1] - y); if (d < bd) { bd = d; best = i; } }); }); return best; }
    function texte() {
      if (sel < 0) { msg.textContent = 'Cliquez sur une flèche pour découvrir le changement d\u2019état correspondant.'; return; }
      var t = T[sel]; msg.innerHTML = '<b>' + t[2].charAt(0).toUpperCase() + t[2].slice(1) + '</b>&nbsp;: passage de l\u2019état ' + ETATS[t[0]][0].toLowerCase() + ' à l\u2019état ' + ETATS[t[1]][0].toLowerCase() + '. Exemple&nbsp;: ' + t[4] + ', $' + t[5] + '$.' + (chkE.checked ? ' Ce changement d\u2019état est <span class="' + (t[3] ? 'nt-endo">endothermique' : 'nt-exo">exothermique') + '</span>.' : '');
      typeset(msg);
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 330 : 360; }, draw);
    cnv.cv.addEventListener('click', function (e) { var i = proche(e); if (i >= 0) { sel = i; texte(); draw(cnv); } });
    cnv.cv.addEventListener('mousemove', function (e) { var i = proche(e); if (i !== survol) { survol = i; cnv.cv.style.cursor = i >= 0 ? 'pointer' : 'default'; draw(cnv); } });
    [chkN, chkE].forEach(function (c) { c.addEventListener('change', function () { texte(); draw(cnv); }); });
    texte(); draw(cnv);
  })();

  /* =================== 2. Entraînement : nommer et écrire un changement d'état =================== */
  (function () {
    var root = document.getElementById('tr-equation'); if (!root) { return; }
    var NOM = { sl: 'fusion', ls: 'solidification', lg: 'vaporisation', gl: 'liquéfaction', sg: 'sublimation', gs: 'condensation' }, ET = { s: 'solide', l: 'liquide', g: 'gazeux' }, NOT = { s: '(s)', l: '(\\ell)', g: '(g)' };
    var ESP = [['l\u2019eau', 'H2O'], ['le dioxyde de carbone', 'CO2'], ['le méthane', 'CH4'], ['le diiode', 'I2'], ['le fer', 'Fe'], ['l\u2019éthanol', 'C2H6O']];
    function eq(f, a, b) { return '$\\ce{' + f + ' ' + NOT[a] + ' -> ' + f + ' ' + NOT[b] + '}$'; }
    function fab() {
      var Q = [], cles = shuffle(Object.keys(NOM));
      cles.slice(0, 3).forEach(function (c) { var faux = shuffle(Object.keys(NOM).filter(function (x) { return x !== c; })).slice(0, 3); Q.push(['Comment s\u2019appelle le passage de l\u2019état ' + ET[c[0]] + ' à l\u2019état ' + ET[c[1]] + '&nbsp;?', [NOM[c]].concat(faux.map(function (x) { return NOM[x]; })), 'Le passage de l\u2019état ' + ET[c[0]] + ' à l\u2019état ' + ET[c[1]] + ' est une ' + NOM[c] + '.']); });
      cles.slice(3).forEach(function (c) { var e = pick(ESP), autre = pick(ESP.filter(function (x) { return x !== e; })), tiers = 'slg'.replace(c[0], '').replace(c[1], '');
        Q.push(['Quelle équation modélise la ' + NOM[c] + ' de ' + e[0] + '&nbsp;?', [eq(e[1], c[0], c[1]), eq(e[1], c[1], c[0]), eq(e[1], c[0], tiers), '$\\ce{' + e[1] + ' ' + NOT[c[0]] + ' -> ' + autre[1] + ' ' + NOT[c[1]] + '}$'], 'La ' + NOM[c] + ' est le passage de l\u2019état ' + ET[c[0]] + ' à l\u2019état ' + ET[c[1]] + '&nbsp;; l\u2019espèce chimique reste la même des deux côtés de la flèche.']); });
      return shuffle(Q);
    }
    Quiz(root, null, 6, fab);
  })();

  /* =================== 3. Les trois états, vus de très près =================== */
  (function () {
    var root = document.getElementById('lab-etats'); if (!root) { return; }
    var cnv, t = 0, P = { s: [], l: [], g: [] }, init = false;
    function boites(o) { var W = o.W, H = o.H, n = 3, gap = W < 560 ? 16 : 26, w = (W - gap * (n + 1)) / n, h = H - 66; return ['s', 'l', 'g'].map(function (k, i) { return { k: k, x: gap + i * (w + gap), y: 36, w: w, h: h }; }); }
    function prepare(o) {
      var B = boites(o), r = Math.min(9, B[0].w / 22); P = { s: [], l: [], g: [], r: r };
      var bs = B[0], cols = Math.floor((bs.w - 10) / (3 * r)), rows = 5; for (var i = 0; i < rows; i++) { for (var j = 0; j < cols; j++) { P.s.push({ x0: bs.x + 8 + 1.5 * r + j * 3 * r, y0: bs.y + bs.h - 6 - 1.5 * r - i * 3 * r, ph: Math.random() * 6, a: 0.3 }); } }
      var bl = B[1], nl = P.s.length; for (i = 0; i < nl; i++) { P.l.push({ x: bl.x + 10 + Math.random() * (bl.w - 20), y: bl.y + bl.h - 8 - Math.random() * rows * 3 * r * 0.95, vx: (Math.random() - 0.5) * 20, vy: (Math.random() - 0.5) * 20, a: Math.random() * 6 }); }
      var bg = B[2]; for (i = 0; i < 9; i++) { var an = Math.random() * 6.28; P.g.push({ x: bg.x + 15 + Math.random() * (bg.w - 30), y: bg.y + 15 + Math.random() * (bg.h - 30), vx: Math.cos(an) * 110, vy: Math.sin(an) * 110, a: Math.random() * 6, w: (Math.random() - 0.5) * 6 }); }
      init = true;
    }
    function pas(o, dt) {
      var B = boites(o), r = P.r, bl = B[1], bg = B[2], top = bl.y + bl.h - 8 - 5 * 3 * r * 0.95;
      P.l.forEach(function (p, i) {   /* liquide : agitation, répulsion entre voisines, et une « surface » qui retient les molécules en bas */
        p.vx += (Math.random() - 0.5) * 400 * dt; p.vy += (Math.random() - 0.5) * 400 * dt + 60 * dt;
        P.l.forEach(function (q, j) { if (j <= i) { return; } var dx = q.x - p.x, dy = q.y - p.y, d = Math.hypot(dx, dy) || 1; if (d < 2.6 * r) { var f = (2.6 * r - d) * 18 * dt; p.vx -= dx / d * f; p.vy -= dy / d * f; q.vx += dx / d * f; q.vy += dy / d * f; } });
        p.vx *= 0.9; p.vy *= 0.9; p.x += p.vx * dt; p.y += p.vy * dt; p.a += p.vx * 0.01;
        if (p.x < bl.x + 8 + r) { p.x = bl.x + 8 + r; p.vx = Math.abs(p.vx); } if (p.x > bl.x + bl.w - 8 - r) { p.x = bl.x + bl.w - 8 - r; p.vx = -Math.abs(p.vx); }
        if (p.y > bl.y + bl.h - 6 - r) { p.y = bl.y + bl.h - 6 - r; p.vy = -Math.abs(p.vy); } if (p.y < top) { p.vy += (top - p.y) * 20 * dt; }
      });
      P.g.forEach(function (p) { p.x += p.vx * dt; p.y += p.vy * dt; p.a += p.w * dt;   /* gaz : mouvement rectiligne rapide, rebonds sur les parois */
        if (p.x < bg.x + 8 + r) { p.x = bg.x + 8 + r; p.vx = Math.abs(p.vx); } if (p.x > bg.x + bg.w - 8 - r) { p.x = bg.x + bg.w - 8 - r; p.vx = -Math.abs(p.vx); }
        if (p.y < bg.y + 8 + r) { p.y = bg.y + 8 + r; p.vy = Math.abs(p.vy); } if (p.y > bg.y + bg.h - 6 - r) { p.y = bg.y + bg.h - 6 - r; p.vy = -Math.abs(p.vy); } });
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; if (!init) { prepare(o); } var B = boites(o), r = P.r;
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#FFFFFF'); gf.addColorStop(1, '#EEF2F7'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      var COL = ['#0E7490', '#1D4ED8', '#EA580C'];
      B.forEach(function (b, i) {
        if (i < 2) { becher(ctx, b.x, b.y, b.w, b.h, true); } else { ctx.fillStyle = 'rgba(224,242,254,0.35)'; rr(ctx, b.x, b.y, b.w, b.h, 10); ctx.fill(); }
        pill(ctx, ['solide', 'liquide', 'gaz'][i], b.x + b.w / 2, 13, { size: 12.5, col: COL[i], stroke: '#E2E8F0' }); icone(ctx, ['s', 'l', 'g'][i], b.x + b.w / 2 - (W < 560 ? 30 : 38), 13, 6);
      });
      P.s.forEach(function (p) { molEau(ctx, p.x0 + Math.sin(t * 9 + p.ph) * r * 0.18, p.y0 + Math.cos(t * 11 + p.ph) * r * 0.18, r * 0.62, p.a + Math.sin(t * 7 + p.ph) * 0.2); });
      P.l.forEach(function (p) { molEau(ctx, p.x, p.y, r * 0.62, p.a); });
      P.g.forEach(function (p) { ctx.strokeStyle = 'rgba(234,88,12,0.18)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(p.x - p.vx * 0.06, p.y - p.vy * 0.06); ctx.stroke(); molEau(ctx, p.x, p.y, r * 0.62, p.a); });   /* petite traînée : les molécules de gaz vont vite */
      B.forEach(function (b, i) {
        if (i < 2) { becher(ctx, b.x, b.y, b.w, b.h, false); } else { ctx.strokeStyle = '#64748B'; ctx.lineWidth = 2.2; rr(ctx, b.x, b.y, b.w, b.h, 10); ctx.stroke(); ctx.fillStyle = '#94A3B8'; rr(ctx, b.x - 4, b.y - 6, b.w + 8, 8, 4); ctx.fill(); ctx.strokeStyle = 'rgba(255,255,255,0.85)'; ctx.lineWidth = 3; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(b.x + 7, b.y + 14); ctx.lineTo(b.x + 7, b.y + b.h - 14); ctx.stroke(); ctx.lineCap = 'butt'; }   /* le gaz est dans un récipient fermé */
        var lg = [['compact', 'et ordonné'], ['compact', 'et désordonné'], ['dispersé', 'et désordonné']][i]; if (W < 560) { txt(ctx, lg[0], b.x + b.w / 2, b.y + b.h + 14, { size: 10, col: SLATE }); txt(ctx, lg[1], b.x + b.w / 2, b.y + b.h + 26, { size: 10, col: SLATE }); } else { txt(ctx, lg[0] + ' ' + lg[1], b.x + b.w / 2, b.y + b.h + 18, { size: 11.5, col: SLATE }); }
      });
    }
    var loop = Loop(root, function (dt) { dt = Math.min(dt, 0.04); t += dt; pas(cnv, dt); draw(cnv); return true; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 220 : 260; }, function (o) { init = false; draw(o); });
    draw(cnv); if (!RM) { loop.kick(); }
  })();

  /* =================== 4. Fusion ou dissolution =================== */
  (function () {
    var root = document.getElementById('lab-dissol'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), mode = 'fusion', t = 0, run = false, cnv, S = [], E = [];
    function prep(o) {
      var W = o.W, H = o.H, bw = Math.min(200, W * 0.46), bx = W / 2 - bw / 2, by = 44, bh = H - 104; S = []; E = [];
      for (var i = 0; i < 4; i++) { for (var j = 0; j < 5; j++) { S.push({ x0: bx + bw / 2 - 2 * 27 + j * 27, y0: by + bh - 14 - i * 17, x1: 0, y1: 0, a1: (Math.random() - 0.5) * 3 }); } }   /* cristal : molécules alignées et toutes orientées pareil */
      var places = shuffle(S.map(function (_, n) { return n; })); S.forEach(function (s, n) { var q = places[n], c = q % 7, rg = Math.floor(q / 7); if (mode === 'fusion') { s.x1 = bx + 18 + c * (bw - 36) / 6 + (Math.random() - 0.5) * 8; s.y1 = by + bh - 14 - rg * 16 + (Math.random() - 0.5) * 6; } else { s.x1 = bx + 20 + Math.random() * (bw - 40); s.y1 = by + 30 + Math.random() * (bh - 48); } });   /* liquide : serré mais en désordre ; dissous : dispersé dans l'eau */
      if (mode === 'dissolution') { for (var k = 0; k < 70; k++) { E.push({ x: bx + 12 + Math.random() * (bw - 24), y: by + 22 + Math.random() * (bh - 34), a: Math.random() * 6 }); } }
      return { bx: bx, by: by, bw: bw, bh: bh };
    }
    var G = null;
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H; if (!G) { G = prep(o); } var e = Math.min(1, t / 3), u = e * e * (3 - 2 * e), b = G;
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#FFFFFF'); gf.addColorStop(1, '#EEF2F7'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      ctx.fillStyle = '#CBD5E1'; ctx.fillRect(0, b.by + b.bh + 26, W, H - b.by - b.bh - 26);   /* paillasse */
      if (mode === 'fusion') {   /* plaque chauffante */
        var chaud = run || t >= 3; ctx.fillStyle = '#334155'; rr(ctx, b.bx - 24, b.by + b.bh + 4, b.bw + 48, 22, 6); ctx.fill();
        var gp = ctx.createLinearGradient(0, b.by + b.bh + 2, 0, b.by + b.bh + 8); gp.addColorStop(0, chaud ? '#F97316' : '#94A3B8'); gp.addColorStop(1, chaud ? '#DC2626' : '#64748B'); ctx.fillStyle = gp; rr(ctx, b.bx - 14, b.by + b.bh + 1, b.bw + 28, 7, 3); ctx.fill();
        ctx.fillStyle = chaud ? '#F87171' : '#64748B'; ctx.beginPath(); ctx.arc(b.bx + b.bw + 8, b.by + b.bh + 16, 4, 0, 2 * Math.PI); ctx.fill();
      } else { ctx.fillStyle = '#E2E8F0'; rr(ctx, b.bx - 24, b.by + b.bh + 4, b.bw + 48, 22, 6); ctx.fill(); }
      becher(ctx, b.bx, b.by, b.bw, b.bh, true);
      if (mode === 'dissolution') { var gw = ctx.createLinearGradient(0, b.by + 16, 0, b.by + b.bh); gw.addColorStop(0, 'rgba(186,230,253,0.55)'); gw.addColorStop(1, 'rgba(125,211,252,0.55)'); ctx.fillStyle = gw; rr(ctx, b.bx + 1, b.by + 16, b.bw - 2, b.bh - 17, 7); ctx.fill(); ctx.strokeStyle = 'rgba(56,189,248,0.8)'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(b.bx + 2, b.by + 16); ctx.lineTo(b.bx + b.bw - 2, b.by + 16); ctx.stroke(); }
      E.forEach(function (w) { molEau(ctx, w.x + Math.sin(t * 3 + w.a) * 2, w.y + Math.cos(t * 2.6 + w.a) * 2, 4.2, w.a + t); });
      S.forEach(function (s) { var x = s.x0 + (s.x1 - s.x0) * u + (u > 0 ? Math.sin(t * 4 + s.a1) * 2 * u : 0), y = s.y0 + (s.y1 - s.y0) * u; sucre(ctx, x, y, 6.5, s.a1 * u); });
      becher(ctx, b.bx, b.by, b.bw, b.bh, false);
      pill(ctx, mode === 'fusion' ? 'sucre seul, chauffé au-delà de 186 °C' : 'sucre dans l\u2019eau, à température ambiante', W / 2, 16, { size: 12, col: NAVY, stroke: '#E2E8F0' });
      var ly = H - 14; sucre(ctx, 22, ly - (mode === 'dissolution' ? 22 : 0), 5, 0); txt(ctx, 'molécule de sucre', 34, ly - (mode === 'dissolution' ? 22 : 0), { size: 11, col: '#92400E', align: 'left' });
      if (mode === 'dissolution') { molEau(ctx, 20, ly, 4.2, 0); txt(ctx, 'molécule d\u2019eau', 34, ly, { size: 11, col: '#B91C1C', align: 'left' }); }
    }
    function texte() { msg.innerHTML = t < 3 ? (mode === 'fusion' ? 'Le cristal de sucre est seul dans le récipient&nbsp;; on le chauffe.' : 'Le cristal de sucre est plongé dans l\u2019eau.') : (mode === 'fusion' ? '<b>Fusion</b>&nbsp;: les molécules de sucre ne sont plus rangées, mais restent serrées entre elles&nbsp;: c\u2019est du sucre liquide, sans eau. $\\ce{C12H22O11 (s) -> C12H22O11 (\\ell)}$' : '<b>Dissolution</b>&nbsp;: les molécules de sucre se dispersent parmi les molécules d\u2019eau, qui les entourent&nbsp;: le sucre est dissous. $\\ce{C12H22O11 (s) -> C12H22O11 (aq)}$'); typeset(msg); }
    var loop = Loop(root, function (dt) { if (!run) { return false; } t += dt; if (t >= 3.2) { run = false; texte(); } draw(cnv); return run || t < 3.2; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 270 : 300; }, function (o) { G = prep(o); draw(o); });
    $(root, '[data-act="go"]').addEventListener('click', function () { G = prep(cnv); t = 0; run = true; texte(); if (RM) { t = 3.2; run = false; texte(); draw(cnv); return; } loop.kick(); });
    $$(root, 'input[name="fd"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; t = 0; run = false; G = prep(cnv); texte(); draw(cnv); }); });
    texte(); draw(cnv);
  })();

  /* =================== 5. Chauffer un kilogramme de glace =================== */
  (function () {
    var root = document.getElementById('lab-chauffe'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), bG = $(root, '[data-act="go"]'), bP = $(root, '[data-act="pause"]'), t = 0, run = false, cnv, ACC = 240;   /* accélération : 1 s affichée = 4 min */
    var P = 800, M = 1, T0 = -18, CG = 2100, CE = 4180, CV = 2010, LF = 334e3, LV = 2265e3, TMAX = 130;
    var t1 = M * CG * (0 - T0) / P, t2 = t1 + M * LF / P, t3 = t2 + M * CE * 100 / P, t4 = t3 + M * LV / P, t5 = t4 + M * CV * (TMAX - 100) / P;
    function etat(t) {   /* température (°C), fraction liquide, fraction gaz */
      if (t < t1) { return [T0 + P * t / (M * CG), 0, 0]; } if (t < t2) { return [0, (t - t1) / (t2 - t1), 0]; } if (t < t3) { return [P * (t - t2) / (M * CE), 1, 0]; }
      if (t < t4) { var fg = (t - t3) / (t4 - t3); return [100, 1 - fg, fg]; } return [100 + P * (Math.min(t, t5) - t4) / (M * CV), 0, 1];
    }
    var ZONES = [[0, t1, 'solide', '#DCFCE7'], [t1, t2, 'solide + liquide', '#D1FAE5'], [t2, t3, 'liquide', '#DBEAFE'], [t3, t4, 'liquide + gaz', '#E0F2FE'], [t4, t5, 'gaz', '#FEF3C7']];
    function four(ctx, x, y, w, h, e) {   /* four à micro-ondes, avec un bécher sur le plateau */
      ctx.save(); ctx.shadowColor = 'rgba(15,23,42,0.25)'; ctx.shadowBlur = 12; ctx.shadowOffsetY = 4; var gb = ctx.createLinearGradient(x, y, x, y + h); gb.addColorStop(0, '#F1F5F9'); gb.addColorStop(1, '#CBD5E1'); ctx.fillStyle = gb; rr(ctx, x, y, w, h, 12); ctx.fill(); ctx.restore();
      var wx = x + 10, wy = y + 10, ww = w * 0.7, wh = h - 20;
      var gi = ctx.createRadialGradient(wx + ww / 2, wy + wh / 2, 5, wx + ww / 2, wy + wh / 2, ww * 0.7); gi.addColorStop(0, run ? '#FEF3C7' : '#334155'); gi.addColorStop(1, run ? '#F59E0B' : '#0F172A'); ctx.fillStyle = gi; rr(ctx, wx, wy, ww, wh, 8); ctx.fill();   /* intérieur éclairé quand le four chauffe */
      var cx = wx + ww / 2, base = wy + wh - 14, bw = ww * 0.5, bh = wh * 0.62;
      ctx.fillStyle = 'rgba(203,213,225,0.9)'; ctx.beginPath(); ctx.ellipse(cx, base + 4, ww * 0.38, 5, 0, 0, 2 * Math.PI); ctx.fill();   /* plateau tournant */
      var fl = e[1], fg = e[2], fs = Math.max(0, 1 - fl - fg), hw = bh * 0.5 * fl;
      ctx.fillStyle = 'rgba(224,242,254,0.35)'; ctx.fillRect(cx - bw / 2, base - bh, bw, bh);
      if (hw > 0.5) { var gw2 = ctx.createLinearGradient(0, base - hw, 0, base); gw2.addColorStop(0, 'rgba(125,211,252,0.9)'); gw2.addColorStop(1, 'rgba(2,132,199,0.9)'); ctx.fillStyle = gw2; ctx.fillRect(cx - bw / 2 + 1, base - hw, bw - 2, hw); }
      if (fs > 0.01) { for (var i = 0; i < 6; i++) { var sz = 15 * Math.max(0.3, Math.sqrt(fs)), gx = cx - bw * 0.28 + (i % 3) * bw * 0.28, gy = base - sz / 2 - 2 - Math.floor(i / 3) * (sz + 2) - (fl > 0 ? Math.min(hw * 0.3, 6) : 0); ctx.fillStyle = 'rgba(240,249,255,0.96)'; ctx.strokeStyle = '#38BDF8'; ctx.lineWidth = 1; rr(ctx, gx - sz / 2, gy - sz / 2, sz, sz, 3); ctx.fill(); ctx.stroke(); ctx.strokeStyle = 'rgba(255,255,255,0.95)'; ctx.beginPath(); ctx.moveTo(gx - sz * 0.25, gy - sz * 0.25); ctx.lineTo(gx + sz * 0.1, gy - sz * 0.25); ctx.stroke(); } }   /* glaçons qui rétrécissent en fondant */
      if (fg > 0 && fg < 1) { for (var k = 0; k < 7; k++) { var by = base - ((t * 40 + k * 13) % Math.max(10, hw)); ctx.strokeStyle = 'rgba(255,255,255,0.95)'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.arc(cx - bw * 0.35 + k * bw * 0.11, by, 2.4, 0, 2 * Math.PI); ctx.stroke(); } }
      if (fg > 0) { for (var v = 0; v < 5; v++) { var vy = base - bh - 4 - ((t * 0.4 + v * 9) % 30); ctx.fillStyle = 'rgba(248,250,252,' + (0.5 * fg * (1 - ((t * 0.4 + v * 9) % 30) / 30)).toFixed(2) + ')'; ctx.beginPath(); ctx.ellipse(cx - 12 + v * 6 + Math.sin(t * 0.05 + v) * 5, vy, 9, 5, 0, 0, 2 * Math.PI); ctx.fill(); } }   /* vapeur qui s'élève */
      ctx.strokeStyle = '#E2E8F0'; ctx.lineWidth = 1.8; ctx.beginPath(); ctx.moveTo(cx - bw / 2, base - bh); ctx.lineTo(cx - bw / 2, base); ctx.lineTo(cx + bw / 2, base); ctx.lineTo(cx + bw / 2, base - bh); ctx.stroke();
      ctx.fillStyle = 'rgba(255,255,255,0.10)'; ctx.beginPath(); ctx.moveTo(wx, wy); ctx.lineTo(wx + ww * 0.45, wy); ctx.lineTo(wx + ww * 0.2, wy + wh); ctx.lineTo(wx, wy + wh); ctx.fill();   /* reflet sur la vitre */
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 3; rr(ctx, wx, wy, ww, wh, 8); ctx.stroke();
      var px = x + w * 0.78, pw = w * 0.17; ctx.fillStyle = '#0F172A'; rr(ctx, px, y + 14, pw, 18, 4); ctx.fill(); ctx.fillStyle = '#4ADE80'; ctx.font = 'bold 11px ' + FONT; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(Math.floor(t / 60) + ':' + String(Math.floor(t % 60)).padStart(2, '0'), px + pw / 2, y + 23);
      for (var bb = 0; bb < 6; bb++) { ctx.fillStyle = bb === 5 ? (run ? '#22C55E' : '#94A3B8') : '#E2E8F0'; ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1; rr(ctx, px + (bb % 2) * pw * 0.52, y + 42 + Math.floor(bb / 2) * 16, pw * 0.46, 11, 3); ctx.fill(); ctx.stroke(); }
      ctx.fillStyle = '#64748B'; rr(ctx, px + pw * 0.15, y + h - 26, pw * 0.7, 6, 3); ctx.fill();   /* poignée */
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, two = W >= 600, e = etat(t);
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#FFFFFF'); gf.addColorStop(1, '#F1F5F9'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      var fw = two ? W * 0.31 : W * 0.66, fh = two ? H * 0.58 : H * 0.34, fx = two ? 14 : (W - fw) / 2, fy = two ? H * 0.16 : 10; four(ctx, fx, fy, fw, fh, e);
      pill(ctx, '\uD83C\uDF21 ' + fmt(e[0], 0) + ' °C', fx + fw / 2, fy + fh + 22, { size: 14, col: '#B91C1C', stroke: '#FECACA' });
      var gx = two ? W * 0.41 : 46, gy = two ? 24 : fh + 56, gw = two ? W * 0.56 : W - 60, gh = two ? H - 60 : H - fh - 92, X = function (s) { return gx + s / t5 * gw; }, Y = function (T) { return gy + gh - (T + 30) / 170 * gh; };
      ctx.fillStyle = '#FFFFFF'; ctx.fillRect(gx, gy, gw, gh);
      ZONES.forEach(function (z) { if (t > z[0]) { ctx.fillStyle = z[3]; ctx.fillRect(X(z[0]), gy, X(Math.min(t, z[1])) - X(z[0]), gh); if (t > z[1] || z[2] === 'gaz') { ctx.save(); ctx.translate((X(z[0]) + X(Math.min(t, z[1]))) / 2, gy + gh - 8); ctx.rotate(-Math.PI / 2); txt(ctx, z[2], 0, 0, { size: 10.5, col: SLATE, align: 'left' }); ctx.restore(); } } });
      ctx.strokeStyle = 'rgba(148,163,184,0.35)'; ctx.lineWidth = 1; [-20, 0, 20, 40, 60, 80, 100, 120].forEach(function (T) { ctx.beginPath(); ctx.moveTo(gx, Y(T)); ctx.lineTo(gx + gw, Y(T)); ctx.stroke(); txt(ctx, String(T), gx - 6, Y(T), { size: 10, col: SLATE, align: 'right' }); });
      for (var m = 0; m <= t5 / 60; m += (two ? 10 : 20)) { txt(ctx, m + ' min', X(m * 60), gy + gh + 13, { size: 10, col: SLATE }); }
      ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(gx, gy - 4); ctx.lineTo(gx, gy + gh); ctx.lineTo(gx + gw + 4, gy + gh); ctx.stroke(); txt(ctx, 'T (°C)', gx + 4, gy - 10, { size: 11, col: NAVY, align: 'left' });
      ctx.save(); ctx.lineJoin = 'round'; ctx.strokeStyle = 'rgba(220,38,38,0.25)'; ctx.lineWidth = 7; ctx.beginPath(); for (var i = 0; i <= 300; i++) { var s = Math.min(t, t5) * i / 300, T = etat(s)[0]; if (i) { ctx.lineTo(X(s), Y(T)); } else { ctx.moveTo(X(s), Y(T)); } } ctx.stroke(); ctx.strokeStyle = '#DC2626'; ctx.lineWidth = 2.8; ctx.stroke(); ctx.restore();
      if (t > t2) { pill(ctx, 'fusion à 0 °C', X((t1 + t2) / 2), Y(0) - 14, { size: 10.5, col: '#0E7490', stroke: '#A5F3FC' }); }
      if (t > t3 + (t4 - t3) * 0.15) { pill(ctx, 'ébullition à 100 °C', X(t3 + (Math.min(t, t4) - t3) / 2), Y(100) - 14, { size: 10.5, col: '#1D4ED8', stroke: '#BFDBFE' }); }
      if (t > 0) { ctx.fillStyle = '#FFFFFF'; ctx.strokeStyle = '#DC2626'; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.arc(X(Math.min(t, t5)), Y(e[0]), 5, 0, 2 * Math.PI); ctx.fill(); ctx.stroke(); }
      var Ek = P * Math.min(t, t5) / 1000, Emax = P * t5 / 1000, ex = gx + gw - 150, ey = gy + 8;   /* jauge de l'énergie reçue */
      ctx.fillStyle = 'rgba(255,255,255,0.9)'; rr(ctx, ex - 6, ey - 4, 152, 34, 8); ctx.fill(); ctx.strokeStyle = GRID2; ctx.lineWidth = 1; ctx.stroke();
      txt(ctx, 'énergie reçue\u00A0: ' + fmt(Ek, 0) + ' kJ', ex, ey + 6, { size: 10.5, col: NAVY, align: 'left' }); ctx.fillStyle = '#E2E8F0'; rr(ctx, ex, ey + 15, 140, 7, 3.5); ctx.fill(); var gE = ctx.createLinearGradient(ex, 0, ex + 140, 0); gE.addColorStop(0, '#FBBF24'); gE.addColorStop(1, '#DC2626'); ctx.fillStyle = gE; rr(ctx, ex, ey + 15, Math.max(4, 140 * Ek / Emax), 7, 3.5); ctx.fill();
    }
    function phase() { return t < t1 ? 0 : t < t2 ? 1 : t < t3 ? 2 : t < t4 ? 3 : 4; }
    var TXT = ['La glace se réchauffe&nbsp;: sa température monte vite.', '<b>Palier de fusion</b>&nbsp;: la glace fond, la température reste à 0&nbsp;°C, bien que le four continue de chauffer&nbsp;! L\u2019énergie reçue sert à faire fondre la glace.', 'L\u2019eau liquide se réchauffe, de 0&nbsp;°C à 100&nbsp;°C.', '<b>Palier d\u2019ébullition</b>&nbsp;: l\u2019eau bout à 100&nbsp;°C. Ce palier est près de sept fois plus long que celui de la fusion&nbsp;: vaporiser l\u2019eau demande beaucoup plus d\u2019énergie que la faire fondre.', 'Toute l\u2019eau est vaporisée&nbsp;: la vapeur se réchauffe à son tour.'];
    var der = -1;
    var loop = Loop(root, function (dt) { if (!run) { return false; } t = Math.min(t5, t + dt * ACC); var ph = phase(); if (ph !== der) { der = ph; msg.innerHTML = TXT[ph]; } if (t >= t5) { run = false; bG.disabled = true; bP.disabled = true; pred.montrer(); msg.innerHTML = 'La courbe présente deux <b>paliers</b>, aux températures de changement d\u2019état&nbsp;: 0&nbsp;°C pour la fusion, 100&nbsp;°C pour l\u2019ébullition. Durée totale&nbsp;: environ ' + Math.round(t5 / 60) + '&nbsp;minutes.'; } draw(cnv); return run; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 600 ? 520 : 330; }, draw);
    var pred = Prediction(root, $(root, 'canvas'), 'à quoi va ressembler la courbe $T = f(t)$&nbsp;?', ['une droite qui monte régulièrement', 'une courbe qui monte, avec des paliers horizontaux', 'une courbe qui monte de plus en plus vite'], 1, function () { bG.disabled = false; });
    bG.disabled = true;
    bG.addEventListener('click', function () { if (t >= t5) { return; } run = true; bP.disabled = false; bG.disabled = true; if (RM) { t = t5; run = false; draw(cnv); pred.montrer(); return; } loop.kick(); });
    bP.addEventListener('click', function () { run = false; bP.disabled = true; bG.disabled = false; });
    $(root, '[data-act="reset"]').addEventListener('click', function () { run = false; t = 0; der = -1; bG.disabled = pred.choix < 0; bP.disabled = true; msg.textContent = 'Faites votre prédiction, puis lancez le chauffage.'; draw(cnv); });
    msg.textContent = 'Faites votre prédiction, puis lancez le chauffage.'; draw(cnv);
  })();

  /* =================== 6. Entraînement : Q = m × L =================== */
  (function () {
    var root = document.getElementById('tr-q'); if (!root) { return; }
    var qEl = $(root, '.nt-tr-q'), inp = $(root, '#trq-x'), P = null;
    var E = [['d\u2019eau', 334, 2265, 0, 100], ['d\u2019éthanol', 108, 855, -114, 78], ['de fer', 247, null, 1538, null], ['d\u2019aluminium', 397, null, 660, null], ['de plomb', 23, null, 327, null]];
    var CH = [['fond', 'fusion', 1, 1], ['se solidifie', 'fusion', -1, 1], ['se vaporise', 'vaporisation', 1, 2], ['se liquéfie', 'vaporisation', -1, 2]];
    function gen() { var e = pick(E), c = pick(CH.filter(function (x) { return e[x[3]] !== null; })), m = pick([0.2, 0.25, 0.5, 0.75, 1.5, 2, 3]); var L = e[c[3]]; return { e: e, c: c, m: m, L: L, Q: c[2] * m * L }; }
    var S = Serie(root, 5, {
      show: function () { P = gen(); var Tc = P.c[3] === 1 ? P.e[3] : P.e[4], g = P.m < 1 ? fmt(P.m * 1000, 0) + '&nbsp;g' : fmt(P.m, P.m % 1 ? 1 : 0) + '&nbsp;kg'; qEl.innerHTML = 'Une masse de ' + g + ' ' + P.e[0] + ' ' + P.c[0] + ' à ' + Tc + '&nbsp;°C. Que vaut l\u2019énergie thermique $Q$ reçue par l\u2019espèce (négative si elle est cédée)&nbsp;?<br><span class="nt-note">Donnée&nbsp;: énergie massique de ' + P.c[1] + '&nbsp;: $L_\\text{' + (P.c[3] === 1 ? 'fus' : 'vap') + '} = \\pu{' + P.L + ' kJ*kg-1}$.</span>'; inp.value = ''; $(root, '[data-act="check"]').disabled = false; typeset(qEl); },
      bilan: function (g, t0) { qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;5</span><br>' + t0; }
    });
    $(root, '[data-act="check"]').addEventListener('click', function () {
      if (S.answered || S.fini) { return; } var x = num(inp.value); if (isNaN(x)) { S.say('Entrez une valeur numérique, en kJ.'); return; }
      var ok = Math.abs(x - P.Q) <= 0.02 * Math.abs(P.Q) + 0.5, signe = Math.abs(x + P.Q) <= 0.02 * Math.abs(P.Q) + 0.5 && !ok; $(root, '[data-act="check"]').disabled = true;
      S.answer(ok, '$Q = m \\times L = ' + (P.c[2] < 0 ? '\\pu{' + String(P.m).replace('.', ',') + ' kg} \\times (\\pu{-' + P.L + ' kJ*kg-1})' : '\\pu{' + String(P.m).replace('.', ',') + ' kg} \\times \\pu{' + P.L + ' kJ*kg-1}') + ' \\approx \\pu{' + fmt(P.Q, Math.abs(P.Q) < 100 ? 1 : 0).replace(/\s/g, ' ') + ' kJ}$' + (P.c[2] < 0 ? '&nbsp;: le changement d\u2019état est exothermique, l\u2019énergie est cédée.' : '&nbsp;: le changement d\u2019état est endothermique, l\u2019énergie est reçue.'), ok ? null : (signe ? '<b>Attention au signe&nbsp;!</b> ' : '<b>Non.</b> ')); typeset($(root, '.nt-msg'));
    });
    S.start();
  })();

  /* =================== 7. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    Quiz(root, [
      ['Le passage de l\u2019état solide à l\u2019état gazeux s\u2019appelle…', ['la sublimation', 'la condensation', 'la vaporisation'], 'La sublimation est le passage direct de l\u2019état solide à l\u2019état gazeux.'],
      ['La buée qui se forme sur une vitre froide est, en physique, une…', ['liquéfaction', 'condensation', 'solidification'], 'La vapeur d\u2019eau passe à l\u2019état liquide&nbsp;: c\u2019est une liquéfaction, même si l\u2019on parle couramment de «&nbsp;condensation&nbsp;».'],
      ['Lors d\u2019un changement d\u2019état, l\u2019espèce chimique…', ['reste la même', 'devient une autre espèce', 'disparaît en partie'], 'Un changement d\u2019état est une transformation physique&nbsp;: seul l\u2019état change.'],
      ['À l\u2019état liquide, les entités sont…', ['proches les unes des autres et en désordre', 'éloignées et en désordre', 'proches et rangées'], 'Le liquide est un état compact et désordonné.'],
      ['Pendant la fusion de la glace, si l\u2019on continue de chauffer, la température…', ['reste à 0 °C', 'augmente régulièrement', 'diminue'], 'Tant que la glace fond, l\u2019énergie reçue sert au changement d\u2019état&nbsp;: la température reste constante.'],
      ['Lequel de ces changements d\u2019état est exothermique&nbsp;?', ['la solidification', 'la fusion', 'la vaporisation'], 'La solidification libère de l\u2019énergie&nbsp;: elle est exothermique.'],
      ['Le sucre dans le café…', ['se dissout', 'fond', 'se sublime'], 'La température du café est bien trop basse pour faire fondre le sucre (environ 186&nbsp;°C)&nbsp;: il se dissout dans l\u2019eau.'],
      ['L\u2019énergie massique de fusion de l\u2019eau vaut $\\pu{334 kJ*kg-1}$. Pour faire fondre 2,0&nbsp;kg de glace, il faut…', ['668 kJ', '167 kJ', '336 kJ'], '$Q = m \\times L_\\text{fus} = \\pu{2,0 kg} \\times \\pu{334 kJ*kg-1} = \\pu{668 kJ}$.']
    ], 8);
  })();

})();
</script>
