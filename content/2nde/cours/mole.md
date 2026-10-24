+++
title = "Quantité de matière"
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
.nt-geant { display: block; text-align: center; font-family: Georgia, "Times New Roman", serif; font-size: clamp(1.1em, 4.2vw, 2.2em); color: #C2410C; letter-spacing: 0.04em; margin: 0.4em 0; overflow-wrap: anywhere; }
.nt-etapes-calc p { margin: 0.35em 0 !important; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Combien y a-t-il de molécules d'eau dans un verre&nbsp;? Des milliards de milliards… beaucoup trop pour les compter une à une. Pour dénombrer les atomes et les molécules, les chimistes les comptent par paquets géants&nbsp;: des <b>moles</b>. Ce chapitre présente cette unité et la grandeur qui l'utilise, la <b>quantité de matière</b>.</p>

## La quantité de matière {.nt-h2}

### Compter par paquets {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Vous connaissez la masse d'un sac d'huîtres et la masse d'une huître. Comment savoir combien de <b>douzaines</b> d'huîtres contient le sac, sans les compter&nbsp;?</p>
</div>

<div class="nt-lab" id="lab-huitres">
<p class="nt-tag"><i class="fa-solid fa-scale-balanced"></i>Animation</p>
<p class="nt-lab-title">Compter des huîtres… en les pesant</p>
<canvas role="img" aria-label="Un sac d'huîtres sur une balance ; les huîtres sont ensuite rangées par douzaines."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Masse du sac&nbsp;: <b class="out-m"></b><input type="range" min="1.8" max="7.2" step="0.9" value="3.6" data-in="m"></label></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Compter par douzaines</button></div>
<div class="nt-b nt-demo-box nt-etapes-calc" aria-live="polite"></div>
</div>

<p>Une <span class="imp">mole</span>, c'est comme une douzaine&nbsp;: c'est une <b>unité de comptage</b>, un paquet d'objets. Mais dans une mole, il y a beaucoup, beaucoup plus que 12 éléments… il y en a 602 mille milliards de milliards&nbsp;! Plus précisément, il y en a exactement&nbsp;:</p>

<p class="nt-geant">602&#8239;214&#8239;076&#8239;000&#8239;000&#8239;000&#8239;000&#8239;000</p>

<p>soit $\pu{6,02214076E23}$, que l'on arrondit le plus souvent à $\pu{6,02E23}$.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pourquoi avoir choisi un nombre aussi étrange&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Pour qu'une mole de nucléons pèse un gramme</span></summary>
<div class="nt-d-body">
<p>Un nucléon (proton ou neutron) a une masse d'environ $\pu{1,67E-24 g}$. Pour obtenir un gramme de nucléons, il en faut donc environ $\dfrac{\pu{1 g}}{\pu{1,67E-24 g}} \approx \pu{6,0E23}$&nbsp;: c'est justement le nombre d'éléments dans une mole. Ainsi, <b>une mole de nucléons pèse environ un gramme</b>, et une mole d'atomes de carbone 12 (12&nbsp;nucléons) pèse environ 12&nbsp;g.</p>
</div>
</details>

### Du microscopique au macroscopique {.nt-h3}

<p>La mole est l'unité de comptage adaptée pour dénombrer des entités microscopiques (atomes, molécules, ions) dans un échantillon macroscopique, c'est-à-dire à notre échelle.</p>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-m' viewBox='0 0 640 250' role='img' aria-label="De l'échelle microscopique (quelques molécules d'eau orientées dans tous les sens) à l'échelle macroscopique (18 g d'eau dans un verre) : on multiplie par 6,02 fois 10 puissance 23, le nombre d'entités dans une mole."><defs><radialGradient id='micro-e' cx='0.4' cy='0.35'><stop offset='0' stop-color='#F0F9FF'/><stop offset='1' stop-color='#7DD3FC'/></radialGradient><radialGradient id='macro-e' cx='0.4' cy='0.35'><stop offset='0' stop-color='#FFF7ED'/><stop offset='1' stop-color='#FDBA74'/></radialGradient><radialGradient id='o-e' cx='0.35' cy='0.3'><stop offset='0' stop-color='#FCA5A5'/><stop offset='1' stop-color='#B91C1C'/></radialGradient><radialGradient id='h-e' cx='0.35' cy='0.3'><stop offset='0' stop-color='#FFFFFF'/><stop offset='1' stop-color='#CBD5E1'/></radialGradient><linearGradient id='fl-e' x1='0' x2='1'><stop offset='0' stop-color='#38BDF8'/><stop offset='1' stop-color='#F97316'/></linearGradient><linearGradient id='eau-e' x1='0' x2='0' y1='0' y2='1'><stop offset='0' stop-color='#7DD3FC'/><stop offset='1' stop-color='#0284C7'/></linearGradient><linearGradient id='verre-e' x1='0' x2='1'><stop offset='0' stop-color='rgba(255,255,255,0.85)'/><stop offset='0.25' stop-color='rgba(255,255,255,0.25)'/><stop offset='0.75' stop-color='rgba(255,255,255,0.1)'/><stop offset='1' stop-color='rgba(255,255,255,0.6)'/></linearGradient><clipPath id='disque-e'><circle cx='110' cy='110' r='88'/></clipPath></defs><circle cx='110' cy='110' r='88' fill='url(#micro-e)'/><g clip-path='url(#disque-e)'><g transform='translate(72,74) rotate(20)'><circle cx='8.7' cy='6.7' r='6.0' fill='url(#h-e)'/><circle cx='-8.7' cy='6.7' r='6.0' fill='url(#h-e)'/><circle cx='0' cy='0' r='10.0' fill='url(#o-e)'/></g><g transform='translate(128,66) rotate(-65)'><circle cx='8.3' cy='6.4' r='5.7' fill='url(#h-e)'/><circle cx='-8.3' cy='6.4' r='5.7' fill='url(#h-e)'/><circle cx='0' cy='0' r='9.5' fill='url(#o-e)'/></g><g transform='translate(160,112) rotate(140)'><circle cx='7.8' cy='6.1' r='5.4' fill='url(#h-e)'/><circle cx='-7.8' cy='6.1' r='5.4' fill='url(#h-e)'/><circle cx='0' cy='0' r='9.0' fill='url(#o-e)'/></g><g transform='translate(98,120) rotate(95)'><circle cx='9.1' cy='7.1' r='6.3' fill='url(#h-e)'/><circle cx='-9.1' cy='7.1' r='6.3' fill='url(#h-e)'/><circle cx='0' cy='0' r='10.5' fill='url(#o-e)'/></g><g transform='translate(60,140) rotate(-150)'><circle cx='7.8' cy='6.1' r='5.4' fill='url(#h-e)'/><circle cx='-7.8' cy='6.1' r='5.4' fill='url(#h-e)'/><circle cx='0' cy='0' r='9.0' fill='url(#o-e)'/></g><g transform='translate(132,158) rotate(35)'><circle cx='8.3' cy='6.4' r='5.7' fill='url(#h-e)'/><circle cx='-8.3' cy='6.4' r='5.7' fill='url(#h-e)'/><circle cx='0' cy='0' r='9.5' fill='url(#o-e)'/></g><g transform='translate(110,32) rotate(200)'><circle cx='7.0' cy='5.4' r='4.8' fill='url(#h-e)'/><circle cx='-7.0' cy='5.4' r='4.8' fill='url(#h-e)'/><circle cx='0' cy='0' r='8.0' fill='url(#o-e)'/></g><g transform='translate(178,70) rotate(-20)'><circle cx='7.0' cy='5.4' r='4.8' fill='url(#h-e)'/><circle cx='-7.0' cy='5.4' r='4.8' fill='url(#h-e)'/><circle cx='0' cy='0' r='8.0' fill='url(#o-e)'/></g><g transform='translate(40,100) rotate(70)'><circle cx='7.0' cy='5.4' r='4.8' fill='url(#h-e)'/><circle cx='-7.0' cy='5.4' r='4.8' fill='url(#h-e)'/><circle cx='0' cy='0' r='8.0' fill='url(#o-e)'/></g></g><text x='110' y='222' font-size='15' text-anchor='middle' fill='#0369A1' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-weight='700'>échelle microscopique</text><text x='110' y='240' font-size='12' text-anchor='middle' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>quelques molécules d'eau</text><path d='M214,92 L392,92 L392,72 L438,110 L392,148 L392,128 L214,128 Z' fill='url(#fl-e)'/><text x='306' y='117' font-size='17' text-anchor='middle' fill='#FFFFFF' font-family='Georgia, "Times New Roman", serif' font-weight='700'>× 6,02 × 10²³</text><text x='306' y='168' font-size='12.5' text-anchor='middle' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>une mole d'entités</text><circle cx='530' cy='110' r='88' fill='url(#macro-e)'/><ellipse cx='530' cy='176' rx='30' ry='5' fill='rgba(15,23,42,0.15)'/><path d='M496,58 L564,58 L556,166 Q555,174 546,174 L514,174 Q505,174 504,166 Z' fill='rgba(224,242,254,0.55)' stroke='#64748B' stroke-width='1.6'/><path d='M500,104 L560,104 L555,164 Q554,170 546,170 L514,170 Q506,170 505,164 Z' fill='url(#eau-e)' opacity='0.9'/><ellipse cx='530' cy='104' rx='30' ry='4.5' fill='#BAE6FD' stroke='#38BDF8' stroke-width='1'/><path d='M496,58 L564,58 L556,166 Q555,174 546,174 L514,174 Q505,174 504,166 Z' fill='url(#verre-e)'/><ellipse cx='530' cy='58' rx='34' ry='6' fill='none' stroke='#64748B' stroke-width='1.6'/><path d='M505,70 L510,160' stroke='rgba(255,255,255,0.9)' stroke-width='4' stroke-linecap='round'/><path d='M554,72 L551,110' stroke='rgba(255,255,255,0.6)' stroke-width='2.5' stroke-linecap='round'/><text x='530' y='222' font-size='15' text-anchor='middle' fill='#C2410C' font-family='system-ui, -apple-system, Segoe UI, sans-serif' font-weight='700'>échelle macroscopique</text><text x='530' y='240' font-size='12' text-anchor='middle' fill='#475569' font-family='system-ui, -apple-system, Segoe UI, sans-serif'>18 g d'eau, à notre échelle</text></svg></div>

<div class="nt-lab" id="lab-unemole">
<p class="nt-tag"><i class="fa-solid fa-flask"></i>Animation</p>
<p class="nt-lab-title">À quoi ressemble une mole de…</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="um" value="eau" checked><span>eau</span></label><label><input type="radio" name="um" value="al"><span>aluminium</span></label><label><input type="radio" name="um" value="cu"><span>cuivre</span></label><label><input type="radio" name="um" value="sel"><span>sel</span></label><label><input type="radio" name="um" value="sucre"><span>sucre</span></label><label><input type="radio" name="um" value="he"><span>hélium</span></label></div></div>
<canvas role="img" aria-label="Une mole de l'espèce choisie, représentée à côté d'un verre d'eau pour comparer les tailles, avec sa masse."></canvas>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>Une mole d'entités contient toujours le même <b>nombre</b> d'entités, mais n'a pas toujours la même <b>masse</b>, ni le même volume&nbsp;: tout dépend de la masse de chaque entité.</p>

### Quantité de matière et constante d'Avogadro {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>La <span class="imp nt-hole">quantité de matière</span> $n$ d'une espèce chimique dans un échantillon est le <span class="imp nt-hole">nombre de moles</span> d'entités (atomes, molécules, ions) de cette espèce qu'il contient. Elle s'exprime en <span class="imp nt-hole">mole</span>, de symbole <span class="imp nt-hole">mol</span>.</p>
<p>Le nombre d'entités par mole est la <span class="imp nt-hole">constante d'Avogadro</span>&nbsp;: $N_\text{A} = \pu{6,02E23 mol-1}$, en hommage au physicien et chimiste italien Amedeo Avogadro (1776-1856).</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$n = \dfrac{N}{N_\text{A}}$</p>
<div class="nt-f-units"><span>$n$&nbsp;: quantité de matière en <b>mol</b></span><span>$N$&nbsp;: nombre d'entités (sans unité)</span><span>$N_\text{A}$&nbsp;: constante d'Avogadro en <b>mol<sup>−1</sup></b></span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On dit parfois «&nbsp;nombre d'Avogadro&nbsp;» pour le nombre sans unité $\pu{6,02E23}$, et «&nbsp;constante d'Avogadro&nbsp;» pour $N_\text{A} = \pu{6,02E23 mol-1}$, le nombre d'entités <b>par mole</b>. C'est cette constante qui intervient dans les calculs.</p>
</div>

## Calculer une quantité de matière {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode</p>
<p>Pour déterminer la quantité de matière d'une espèce dans un échantillon de masse $m$&nbsp;:</p>
<ol class="nt-steps">
<li><p>Déterminer la masse $m_\text{entité}$ d'<b>une</b> entité (atome, molécule…), par exemple à partir du nombre de nucléons qu'elle contient.</p></li>
<li><p>En déduire le <b>nombre d'entités</b>&nbsp;:<br>
$N = \dfrac{m}{m_\text{entité}}$ (avec $m$ et $m_\text{entité}$ dans la même unité).</p></li>
<li><p>En déduire la <b>quantité de matière</b>&nbsp;:<br>
$n = \dfrac{N}{N_\text{A}}$.</p></li>
</ol>
</div>

<p>C'est exactement le raisonnement des huîtres&nbsp;: la masse d'une huître, puis le nombre d'huîtres, puis le nombre de douzaines.</p>

### Une bouteille d'eau pure {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 1</p>
<p>Combien y a-t-il de moles de molécules d'eau dans un litre d'eau pure (de masse 1,0&nbsp;kg)&nbsp;?</p>
<p><b>Données&nbsp;:</b></p>
<ul class="nt-facts">
<li>la molécule d'eau $\ce{H2O}$ est formée d'un atome d'oxygène et de deux atomes d'hydrogène&nbsp;;</li>
<li>écriture conventionnelle des deux noyaux&nbsp;: $\ce{^1_1H}$ et $\ce{^{16}_8O}$&nbsp;;</li>
<li>masse d'un nucléon&nbsp;: $m_\text{nucléon} \approx \pu{1,7E-27 kg}$.</li>
</ul>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Environ 53 moles</span></summary>
<div class="nt-d-body">
<p><b>Masse d'une molécule&nbsp;:</b><br>
En négligeant la masse des électrons, une molécule d'eau contient $2 \times 1 + 16 = 18$ nucléons&nbsp;: $m_{\ce{H2O}} \approx 18 \times \pu{1,7E-27 kg} \approx \pu{3,1E-26 kg}$.</p>
<p><b>Nombre de molécules&nbsp;:</b><br>
$N = \dfrac{\pu{1,0 kg}}{\pu{3,1E-26 kg}} \approx \pu{3,2E25}$ molécules.</p>
<p><b>Quantité de matière&nbsp;:</b><br>
$n = \dfrac{N}{N_\text{A}} = \dfrac{\pu{3,2E25}}{\pu{6,02E23 mol-1}} \approx \pu{53 mol}$</p>
<p>La valeur précise est d'environ $\pu{55,5 mol}$&nbsp;: l'écart vient surtout de l'arrondi de la masse du nucléon ($\pu{1,67E-27 kg}$ plutôt que $\pu{1,7E-27 kg}$).</p>
</div>
</details>

### L'air de la salle de classe {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 2</p>
<p>Déterminer les quantités de matière de dioxygène et de diazote dans l'air de la salle de cours.</p>
<p><b>Données&nbsp;:</b></p>
<ul class="nt-facts">
<li>masse volumique de l'air&nbsp;: $\rho_\text{air} = \pu{1,2 kg*m-3}$&nbsp;;</li>
<li>masse d'une molécule de dioxygène&nbsp;: $m_{\ce{O2}} = \pu{5,3E-26 kg}$&nbsp;;</li>
<li>masse d'une molécule de diazote&nbsp;: $m_{\ce{N2}} = \pu{4,7E-26 kg}$&nbsp;;</li>
<li>composition massique de l'air&nbsp;: 76&nbsp;% de diazote et 23&nbsp;% de dioxygène (le reste est surtout de l'argon).</li>
</ul>
</div>

<div class="nt-lab" id="lab-salle">
<p class="nt-tag"><i class="fa-solid fa-school"></i>Animation</p>
<p class="nt-lab-title">Et dans votre salle&nbsp;?</p>
<canvas role="img" aria-label="Une salle de classe en perspective, dont on règle les dimensions ; le volume, la masse d'air et les quantités de matière s'affichent."></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Longueur&nbsp;: <b class="out-L"></b><input type="range" min="5" max="15" step="1" value="10" data-in="L"></label>
<label class="nt-ctrl">Largeur&nbsp;: <b class="out-l"></b><input type="range" min="4" max="10" step="1" value="5" data-in="l"></label>
<label class="nt-ctrl">Hauteur&nbsp;: <b class="out-h"></b><input type="range" min="2.5" max="4" step="0.5" value="3" data-in="h"></label>
</div>
<div class="nt-b nt-demo-box nt-etapes-calc" aria-live="polite"></div>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Détails</span><span class="nt-sum">Pour une salle de 10 m × 5 m × 3 m</span></summary>
<div class="nt-d-body">
<p><b>Volume de la salle.</b> $V = \pu{10 m} \times \pu{5 m} \times \pu{3 m} = \pu{150 m3}$.</p>
<p><b>Masse d'air&nbsp;:</b><br>
$m_\text{air} = \rho_\text{air} \times V = \pu{1,2 kg*m-3} \times \pu{150 m3} = \pu{180 kg}$.</p>
<p><b>Masses de chaque gaz&nbsp;:</b><br>
$m_{\ce{O2}} = 23\,\% \times \pu{180 kg} \approx \pu{41 kg}$ et $m_{\ce{N2}} = 76\,\% \times \pu{180 kg} \approx \pu{137 kg}$.</p>
<p><b>Nombres de molécules&nbsp;:</b><br>
$N_{\ce{O2}} = \dfrac{\pu{41 kg}}{\pu{5,3E-26 kg}} \approx \pu{7,7E26}$ et $N_{\ce{N2}} = \dfrac{\pu{137 kg}}{\pu{4,7E-26 kg}} \approx \pu{2,9E27}$.</p>
<p><b>Quantités de matière&nbsp;:</b><br>
$n_{\ce{O2}} = \dfrac{\pu{7,7E26}}{\pu{6,02E23 mol-1}} \approx \pu{1,3E3 mol}$ et $n_{\ce{N2}} = \dfrac{\pu{2,9E27}}{\pu{6,02E23 mol-1}} \approx \pu{4,8E3 mol}$.</p>
<p>Il y a donc environ <b>1&nbsp;300&nbsp;moles de dioxygène</b> et <b>4&nbsp;800&nbsp;moles de diazote</b> dans la salle&nbsp;!</p>
</div>
</details>

### Une pièce de 50 centimes {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 3</p>
<p>Déterminer les quantités de matière des différents métaux présents dans une pièce de 50&nbsp;centimes d'euro, en «&nbsp;or nordique&nbsp;».</p>
<p><b>Données&nbsp;:</b></p>
<ul class="nt-facts">
<li>composition massique de la pièce&nbsp;: 89&nbsp;% de cuivre, 5&nbsp;% d'aluminium, 5&nbsp;% de zinc et 1&nbsp;% d'étain&nbsp;;</li>
<li>masse de la pièce&nbsp;: $\pu{7,8 g}$&nbsp;;</li>
<li>masses des atomes&nbsp;: $m_{\ce{Cu}} = \pu{1,1E-22 g}$, $m_{\ce{Al}} = \pu{4,5E-23 g}$, $m_{\ce{Zn}} = \pu{1,1E-22 g}$, $m_{\ce{Sn}} = \pu{2,0E-22 g}$.</li>
</ul>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Quatre métaux, quatre calculs</span></summary>
<div class="nt-d-body">
<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>métal</th><th>masse dans la pièce</th><th>nombre d'atomes</th><th>quantité de matière</th></tr></thead>
<tbody>
<tr><td>cuivre</td><td>$89\,\% \times \pu{7,8 g} = \pu{6,9 g}$</td><td>$\dfrac{\pu{6,9 g}}{\pu{1,1E-22 g}} \approx \pu{6,3E22}$</td><td>$\pu{0,10 mol}$</td></tr>
<tr><td>aluminium</td><td>$5\,\% \times \pu{7,8 g} = \pu{0,39 g}$</td><td>$\dfrac{\pu{0,39 g}}{\pu{4,5E-23 g}} \approx \pu{8,7E21}$</td><td>$\pu{14 mmol}$</td></tr>
<tr><td>zinc</td><td>$5\,\% \times \pu{7,8 g} = \pu{0,39 g}$</td><td>$\dfrac{\pu{0,39 g}}{\pu{1,1E-22 g}} \approx \pu{3,5E21}$</td><td>$\pu{5,8 mmol}$</td></tr>
<tr><td>étain</td><td>$1\,\% \times \pu{7,8 g} = \pu{0,078 g}$</td><td>$\dfrac{\pu{0,078 g}}{\pu{2,0E-22 g}} \approx \pu{3,9E20}$</td><td>$\pu{0,65 mmol}$</td></tr>
</tbody>
</table></div>
<p>Les quantités de matière s'obtiennent en divisant chaque nombre d'atomes par $N_\text{A} = \pu{6,02E23 mol-1}$&nbsp;; on rappelle que $\pu{1 mmol} = \pu{1E-3 mol}$.</p>
</div>
</details>

<div class="nt-lab" id="lab-piece">
<p class="nt-tag"><i class="fa-solid fa-chart-column"></i>Animation</p>
<p class="nt-lab-title">Même masse, même nombre d'atomes&nbsp;?</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="pc" value="masse" checked><span>Composition en masse</span></label><label><input type="radio" name="pc" value="nombre"><span>Composition en nombre d'atomes</span></label></div></div>
<canvas role="img" aria-label="Diagramme en barres de la composition de la pièce, en masse ou en nombre d'atomes."></canvas>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-lab nt-trainer" id="tr-mole">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Calculer une quantité de matière</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-ans"><span class="nt-champ"><label for="trm-x">$n$&nbsp;=</label><input id="trm-x" type="text" inputmode="decimal" autocomplete="off" placeholder="ex. 2,5e-3"><span class="nt-u">mol</span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Divulgâchage&nbsp;: la masse molaire</span></summary>
<div class="nt-d-body">
<p>Vous verrez l'an prochain (pour ceux qui feront de la physique-chimie) que les deux étapes du calcul, $N = \dfrac{m}{m_\text{entité}}$ puis $n = \dfrac{N}{N_\text{A}}$, peuvent se résumer en un seul calcul, grâce à la <b>masse molaire</b> $M$ de l'entité&nbsp;: la masse d'une mole de cette entité, en $\pu{g*mol-1}$.</p>
<p style="text-align:center;">$n = \dfrac{m}{M}$ &nbsp; avec &nbsp; $M = N_\text{A} \times m_\text{entité}$</p>
<p>Les masses molaires sont alors toujours données.</p> 
<p>Par exemple, avec $M(\ce{H2O}) = \pu{18 g*mol-1}$, un verre de $\pu{200 mL}$ d'eau (soit $\pu{200 g}$) contient $n = \dfrac{\pu{200 g}}{\pu{18 g*mol-1}} \approx \pu{11 mol}$ de molécules d'eau.</p>
</div>
</details>

## Testez-vous {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-final">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur la quantité de matière</p>
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

  function nsci(x, d) {   /* écriture scientifique en HTML : 3,2 × 10<sup>25</sup> */
    if (x === 0) { return '0'; } var e = Math.floor(Math.log10(Math.abs(x))), m = x / Math.pow(10, e); if (Math.abs(m) >= 9.995) { m /= 10; e += 1; }
    if (e >= -2 && e <= 2) { return fmt(x, Math.max(0, (d === undefined ? 1 : d) - e)); }
    return fmt(m, d === undefined ? 1 : d) + '&nbsp;×&nbsp;10<sup>' + String(e).replace('-', '\u2212') + '</sup>';
  }

  /* =================== 1. Compter des huîtres en les pesant =================== */
  (function () {
    var root = document.getElementById('lab-huitres'); if (!root) { return; }
    var inM = $(root, '[data-in="m"]'), panneau = $(root, '.nt-etapes-calc'), MH = 75, t = -1, cnv;   /* masse d'une huître : 75 g */
    function N() { return Math.round(+inM.value * 1000 / MH); }
    function huitre(ctx, x, y, s, a) {
      ctx.save(); ctx.translate(x, y); ctx.rotate(a); var g = ctx.createLinearGradient(0, -6 * s, 0, 6 * s); g.addColorStop(0, '#E7E5E4'); g.addColorStop(1, '#78716C');
      ctx.fillStyle = g; ctx.beginPath(); ctx.moveTo(-9 * s, 0); ctx.bezierCurveTo(-8 * s, -7 * s, 6 * s, -8 * s, 10 * s, -2 * s); ctx.bezierCurveTo(9 * s, 5 * s, -4 * s, 7 * s, -9 * s, 0); ctx.fill();
      ctx.strokeStyle = 'rgba(68,64,60,0.6)'; ctx.lineWidth = 0.8; ctx.beginPath(); ctx.moveTo(-6 * s, 0); ctx.quadraticCurveTo(0, -4 * s, 7 * s, -2 * s); ctx.stroke(); ctx.restore();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, n = N(), dz = n / 12, two = W >= 560, xg = two ? W * 0.2 : W * 0.5, yb = two ? H * 0.72 : H * 0.36;
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#F8FAFC'; ctx.fillRect(0, 0, W, H);
      ctx.fillStyle = '#94A3B8'; rr(ctx, xg - 70, yb, 140, 16, 5); ctx.fill(); ctx.fillStyle = '#334155'; rr(ctx, xg - 46, yb + 16, 92, 34, 6); ctx.fill();   /* balance */
      ctx.fillStyle = '#0F172A'; rr(ctx, xg - 34, yb + 24, 68, 20, 4); ctx.fill(); txt(ctx, fmt(+inM.value, 1) + ' kg', xg, yb + 34, { size: 13, col: '#4ADE80', serif: false });
      var sh = 46 + n * 0.6, gs = ctx.createLinearGradient(xg - 40, 0, xg + 40, 0); gs.addColorStop(0, '#A16207'); gs.addColorStop(0.5, '#CA8A04'); gs.addColorStop(1, '#A16207');   /* sac de jute */
      ctx.fillStyle = gs; ctx.beginPath(); ctx.moveTo(xg - 46, yb); ctx.quadraticCurveTo(xg - 58, yb - sh * 0.6, xg - 26, yb - sh); ctx.lineTo(xg + 26, yb - sh); ctx.quadraticCurveTo(xg + 58, yb - sh * 0.6, xg + 46, yb); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#78350F'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(xg - 26, yb - sh + 6); ctx.lineTo(xg + 26, yb - sh + 6); ctx.stroke();
      for (var i = 0; i < 5; i++) { huitre(ctx, xg - 22 + i * 11, yb - sh - 2 - (i % 2) * 3, 1.0, (i - 2) * 0.3); }
      if (t >= 0) {   /* les huîtres rangées par douzaines */
        var x0 = two ? W * 0.44 : 30, y0 = two ? 30 : H * 0.62, cw = two ? (W * 0.55) / 12 : (W - 32) / 12, rh = two ? Math.min(30, (H - 50) / 8) : Math.min(22, (H * 0.36) / 8), vis = Math.min(n, Math.floor(t * 40));
        for (var k = 0; k < vis; k++) { var r = Math.floor(k / 12), c = k % 12; huitre(ctx, x0 + c * cw + cw / 2, y0 + r * rh + rh / 2, Math.min(1.15, cw / 20), ((k * 37) % 7 - 3) * 0.1); }
        for (var r2 = 0; r2 < Math.ceil(vis / 12); r2++) { txt(ctx, String(r2 + 1), x0 - 8, y0 + r2 * rh + rh / 2, { size: 11, col: '#64748B', align: 'right' }); }   /* numéro de la douzaine */
        if (vis) { txt(ctx, 'douzaines', x0 - 8, y0 - 12, { size: 10.5, col: '#64748B', align: 'left' }); }
      }
    }
    function texte() {
      var n = N(), m = +inM.value * 1000;
      panneau.innerHTML = '<p class="nt-tag"><i class="fa-solid fa-calculator"></i>Le raisonnement</p>' +
        '<p><b>1.</b> Masse d\u2019une huître&nbsp;: $m_\\text{huître} = \\pu{75 g}$.</p>' +
        '<p><b>2.</b> Nombre d\u2019huîtres&nbsp;: $N = \\dfrac{m_\\text{sac}}{m_\\text{huître}}$ <span style="white-space:nowrap">$= \\dfrac{\\pu{' + fmt(m, 0).replace(/\s/g, ' ') + ' g}}{\\pu{75 g}} = ' + n + '$.</span></p>' +
        '<p><b>3.</b> Nombre de douzaines&nbsp;: $\\dfrac{N}{12} = \\dfrac{' + n + '}{12} = ' + (n / 12) + '$ douzaines.</p>' +
        '<p>Pour des atomes, on fera exactement la même chose, avec des «&nbsp;paquets&nbsp;» de $\\pu{6,02E23}$ au lieu de 12&nbsp;: des moles.</p>';
      typeset(panneau); $(root, '.out-m').textContent = fmt(+inM.value, 1) + '\u00A0kg';
    }
    var loop = Loop(root, function (dt) { if (t < 0) { return false; } t += dt; draw(cnv); return t * 40 < N() + 2; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 420 : 300; }, draw);
    inM.addEventListener('input', function () { t = -1; texte(); draw(cnv); });
    $(root, '[data-act="go"]').addEventListener('click', function () { t = 0; if (RM) { t = 99; draw(cnv); return; } loop.kick(); });
    texte(); draw(cnv);
  })();

  /* =================== 2. À quoi ressemble une mole de… =================== */
  (function () {
    var root = document.getElementById('lab-unemole'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), cle = 'eau', cnv;
    var D = {   /* masse d'une mole (g), volume (cm³), description */
      eau: [18, 18, 'Une mole d\u2019eau&nbsp;: <b>18&nbsp;g</b>, soit 18&nbsp;mL, une grosse cuillerée. Elle contient $\\pu{6,02E23}$ molécules d\u2019eau.'],
      al: [27, 10, 'Une mole d\u2019aluminium&nbsp;: <b>27&nbsp;g</b>, par exemple une boule de papier d\u2019aluminium froissé. Le métal seul formerait un petit cube de 2,2&nbsp;cm de côté. Elle contient $\\pu{6,02E23}$ atomes d\u2019aluminium.'],
      cu: [63.5, 7.1, 'Une mole de cuivre&nbsp;: <b>63,5&nbsp;g</b>, un petit tas de billes&nbsp;: le métal seul formerait un cube de seulement 1,9&nbsp;cm de côté, car les atomes de cuivre sont lourds et serrés.'],
      sel: [58.4, 27, 'Une mole de sel (chlorure de sodium)&nbsp;: <b>58,4&nbsp;g</b>, environ deux grosses cuillerées. Elle contient $\\pu{6,02E23}$ ions sodium et autant d\u2019ions chlorure.'],
      sucre: [342, 215, 'Une mole de sucre (saccharose)&nbsp;: <b>342&nbsp;g</b>, environ 70&nbsp;morceaux&nbsp;! La molécule de saccharose, $\\ce{C12H22O11}$, contient 45&nbsp;atomes&nbsp;: elle est très lourde.'],
      he: [4, 24000, 'Une mole d\u2019hélium&nbsp;: seulement <b>4&nbsp;g</b>, mais un gros ballon de 24&nbsp;L, d\u2019environ 36&nbsp;cm de diamètre. Un gaz occupe beaucoup de place pour peu de matière.']
    };
    function verre(ctx, x, sol, hv, lv, niveau) {   /* verre de 20 cL : paroi, buvant ovale, reflets ; niveau = hauteur d'eau (px) */
      ctx.fillStyle = 'rgba(15,23,42,0.12)'; ctx.beginPath(); ctx.ellipse(x, sol, lv * 0.5, 4, 0, 0, 2 * Math.PI); ctx.fill();
      ctx.beginPath(); ctx.moveTo(x - lv / 2, sol - hv); ctx.lineTo(x + lv / 2, sol - hv); ctx.lineTo(x + lv * 0.4, sol - 3); ctx.quadraticCurveTo(x + lv * 0.4, sol, x + lv * 0.36, sol); ctx.lineTo(x - lv * 0.36, sol); ctx.quadraticCurveTo(x - lv * 0.4, sol, x - lv * 0.4, sol - 3); ctx.closePath();
      ctx.fillStyle = 'rgba(224,242,254,0.45)'; ctx.fill();
      if (niveau > 0) { ctx.save(); ctx.clip(); var ge = ctx.createLinearGradient(0, sol - niveau, 0, sol); ge.addColorStop(0, '#7DD3FC'); ge.addColorStop(1, '#0284C7'); ctx.fillStyle = ge; ctx.fillRect(x - lv, sol - niveau, 2 * lv, niveau); ctx.restore(); var wl = lv * (0.4 + 0.1 * niveau / hv); ctx.fillStyle = '#BAE6FD'; ctx.beginPath(); ctx.ellipse(x, sol - niveau, wl, 2.5, 0, 0, 2 * Math.PI); ctx.fill(); }
      ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(x - lv / 2, sol - hv); ctx.lineTo(x - lv * 0.4, sol - 3); ctx.quadraticCurveTo(x - lv * 0.4, sol, x - lv * 0.36, sol); ctx.lineTo(x + lv * 0.36, sol); ctx.quadraticCurveTo(x + lv * 0.4, sol, x + lv * 0.4, sol - 3); ctx.lineTo(x + lv / 2, sol - hv); ctx.stroke();   /* parois et fond seulement : pas de trait en travers de l'ouverture */
      ctx.beginPath(); ctx.ellipse(x, sol - hv, lv / 2, 4, 0, 0, 2 * Math.PI); ctx.stroke();
      ctx.strokeStyle = 'rgba(255,255,255,0.9)'; ctx.lineWidth = 3; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(x - lv * 0.36, sol - hv * 0.85); ctx.lineTo(x - lv * 0.3, sol - hv * 0.12); ctx.stroke(); ctx.lineCap = 'butt';
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k = cle === 'he' ? Math.min(H / 46, W / 70) : Math.min(H / 22, W / 40), sol = H - 34, d = D[cle];   /* k : pixels par cm ; le verre de référence est toujours à la même échelle que l'échantillon */
      ctx.clearRect(0, 0, W, H);
      var gm = ctx.createLinearGradient(0, 0, 0, sol); gm.addColorStop(0, '#F8FAFC'); gm.addColorStop(1, '#E2E8F0'); ctx.fillStyle = gm; ctx.fillRect(0, 0, W, sol);   /* mur carrelé du laboratoire */
      ctx.strokeStyle = 'rgba(148,163,184,0.25)'; ctx.lineWidth = 1; for (var tx = 0; tx < W; tx += 34) { ctx.beginPath(); ctx.moveTo(tx, 0); ctx.lineTo(tx, sol); ctx.stroke(); } for (var ty = sol; ty > 0; ty -= 34) { ctx.beginPath(); ctx.moveTo(0, ty); ctx.lineTo(W, ty); ctx.stroke(); }
      var gt = ctx.createLinearGradient(0, sol, 0, H); gt.addColorStop(0, '#E7D3B0'); gt.addColorStop(1, '#B08B5A'); ctx.fillStyle = gt; ctx.fillRect(0, sol, W, H - sol); ctx.fillStyle = '#8B6B43'; ctx.fillRect(0, sol, W, 2);   /* paillasse */
      var xv = W * 0.26, hv = 10 * k, lv = 7 * k;
      verre(ctx, xv, sol, hv, lv, cle === 'eau' ? 18 / 200 * hv * 1.15 : 0);
      txt(ctx, 'verre de 20 cL', xv, sol + 16, { size: 11, col: '#5B4632' });
      var xs = W * 0.64;
      if (cle === 'eau') { pill(ctx, '18 mL d\u2019eau, au fond du verre', xv + lv * 0.62, sol - hv * 0.25, { size: 11.5, col: '#0369A1', stroke: '#BAE6FD', align: 'left' }); }
      else if (cle === 'he') {   /* ballon de baudruche gonflé à l'hélium */
        var r = 18 * k, cy = sol - 2 * r - 26 - r; cy = Math.max(r + 8, cy);
        ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(xs, cy + r * 1.08); ctx.bezierCurveTo(xs + 14, cy + r * 1.4, xs - 10, sol - 20, xs + 4, sol); ctx.stroke();
        var gb = ctx.createRadialGradient(xs - r * 0.4, cy - r * 0.4, r * 0.05, xs, cy, r * 1.05); gb.addColorStop(0, '#FEF9C3'); gb.addColorStop(0.5, '#FACC15'); gb.addColorStop(1, '#CA8A04'); ctx.fillStyle = gb;
        ctx.beginPath(); ctx.ellipse(xs, cy, r * 0.95, r * 1.05, 0, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#CA8A04'; ctx.beginPath(); ctx.moveTo(xs - 5, cy + r * 1.08); ctx.lineTo(xs + 5, cy + r * 1.08); ctx.lineTo(xs, cy + r * 1.02); ctx.fill();
        ctx.fillStyle = 'rgba(255,255,255,0.55)'; ctx.beginPath(); ctx.ellipse(xs - r * 0.42, cy - r * 0.45, r * 0.16, r * 0.28, -0.5, 0, 2 * Math.PI); ctx.fill();
        pill(ctx, '24 L', xs, cy, { size: 13, col: '#854D0E', bg: 'rgba(255,255,255,0.75)' });
      }
      else if (cle === 'sucre') {   /* 70 morceaux de sucre empilés en pyramide : 13 + 12 + 11 + 10 + 9 + 8 + 7 */
        var c = Math.min(1.5 * k, (W * 0.62) / 13.5);
        ctx.fillStyle = 'rgba(15,23,42,0.12)'; ctx.beginPath(); ctx.ellipse(xs, sol, 6.8 * c, 5, 0, 0, 2 * Math.PI); ctx.fill();
        for (var row = 0; row < 7; row++) { var nr = 13 - row; for (var col = 0; col < nr; col++) {
          var x = xs - nr * c / 2 + col * c, y = sol - (row + 1) * c * 0.94, gs = ctx.createLinearGradient(x, y, x + c, y + c); gs.addColorStop(0, '#FFFFFF'); gs.addColorStop(1, '#E2E8F0');
          ctx.fillStyle = gs; ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 0.8; rr(ctx, x + 0.5, y, c * 0.95, c * 0.92, 2); ctx.fill(); ctx.stroke();
          ctx.fillStyle = 'rgba(148,163,184,0.35)'; ctx.fillRect(x + c * 0.2, y + c * 0.25, 1.4, 1.4); ctx.fillRect(x + c * 0.6, y + c * 0.55, 1.4, 1.4);
        } }
      }
      else if (cle === 'sel') {   /* tas de sel dans une coupelle */
        var rs = 3.6 * k; ctx.fillStyle = '#94A3B8'; ctx.beginPath(); ctx.ellipse(xs, sol - 4, rs * 1.6, 6, 0, 0, 2 * Math.PI); ctx.fill();
        var gsel = ctx.createLinearGradient(0, sol - rs * 1.2, 0, sol); gsel.addColorStop(0, '#FFFFFF'); gsel.addColorStop(1, '#E2E8F0'); ctx.fillStyle = gsel; ctx.beginPath(); ctx.moveTo(xs - rs * 1.4, sol - 6); ctx.quadraticCurveTo(xs - rs * 0.4, sol - rs * 1.25, xs, sol - rs * 1.2); ctx.quadraticCurveTo(xs + rs * 0.5, sol - rs * 1.2, xs + rs * 1.4, sol - 6); ctx.fill();
        ctx.fillStyle = 'rgba(148,163,184,0.7)'; for (var q = 0; q < 60; q++) { var u = ((q * 37) % 100) / 100 - 0.5, hmax = rs * 1.15 * (1 - 4 * u * u); ctx.fillRect(xs + u * rs * 2.6, sol - 8 - ((q * 53) % 100) / 100 * Math.max(0, hmax - 6), 1.6, 1.6); }
      }
      else if (cle === 'al') {   /* boule de papier d'aluminium froissé */
        var ra = 2.6 * k, cya = sol - ra; var ga = ctx.createRadialGradient(xs - ra * 0.4, cya - ra * 0.4, 1, xs, cya, ra); ga.addColorStop(0, '#FFFFFF'); ga.addColorStop(0.6, '#CBD5E1'); ga.addColorStop(1, '#64748B'); ctx.fillStyle = ga;
        ctx.beginPath(); for (var i = 0; i <= 24; i++) { var an = i / 24 * 2 * Math.PI, rr2 = ra * (0.9 + 0.1 * Math.sin(i * 2.7)); if (i) { ctx.lineTo(xs + rr2 * Math.cos(an), cya + rr2 * Math.sin(an)); } else { ctx.moveTo(xs + rr2 * Math.cos(an), cya + rr2 * Math.sin(an)); } } ctx.closePath(); ctx.fill();
        ctx.strokeStyle = 'rgba(71,85,105,0.5)'; ctx.lineWidth = 1; for (var f = 0; f < 9; f++) { var a1 = f * 0.7, a2 = a1 + 1.1; ctx.beginPath(); ctx.moveTo(xs + ra * 0.7 * Math.cos(a1), cya + ra * 0.7 * Math.sin(a1)); ctx.lineTo(xs + ra * 0.3 * Math.cos(a2), cya + ra * 0.3 * Math.sin(a2)); ctx.stroke(); }
      }
      else {   /* billes de cuivre en petit tas */
        var rb = 0.28 * k, nb = 0; for (var lvl = 0; lvl < 6; lvl++) { for (var bi = 0; bi < 9 - lvl * 1.5; bi++) { var bxx = xs - (9 - lvl * 1.5) * rb + bi * 2 * rb + lvl * rb * 0.5 + rb, byy = sol - rb - lvl * rb * 1.7; var gc = ctx.createRadialGradient(bxx - rb * 0.35, byy - rb * 0.35, 0.5, bxx, byy, rb); gc.addColorStop(0, '#FED7AA'); gc.addColorStop(0.5, '#EA580C'); gc.addColorStop(1, '#7C2D12'); ctx.fillStyle = gc; ctx.beginPath(); ctx.arc(bxx, byy, rb, 0, 2 * Math.PI); ctx.fill(); nb++; } }
      }
      pill(ctx, '1 mol = ' + fmt(d[0], d[0] % 1 ? 1 : 0) + ' g', xs, 22, { size: 14, col: '#C2410C', stroke: '#FED7AA' });
      var xr = W - 26; ctx.fillStyle = '#FEF3C7'; ctx.strokeStyle = '#CA8A04'; ctx.lineWidth = 1; ctx.fillRect(xr - 8, sol - 10 * k, 16, 10 * k); ctx.strokeRect(xr - 8, sol - 10 * k, 16, 10 * k);   /* règle de 10 cm */
      ctx.fillStyle = '#854D0E'; for (var cm = 0; cm <= 10; cm++) { ctx.fillRect(xr - 8, sol - cm * k, cm % 5 ? 5 : 9, 1); } txt(ctx, '10 cm', xr - 12, sol - 10 * k - 8, { size: 10, col: '#854D0E', align: 'right' });
    }
    function texte() { msg.innerHTML = D[cle][2]; typeset(msg); }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 280 : 340; }, draw);
    $$(root, 'input[name="um"]').forEach(function (r) { r.addEventListener('change', function () { cle = r.value; texte(); draw(cnv); }); });
    texte(); draw(cnv);
  })();

  /* =================== 3. L'air de la salle =================== */
  (function () {
    var root = document.getElementById('lab-salle'); if (!root) { return; }
    var inL = $(root, '[data-in="L"]'), inl = $(root, '[data-in="l"]'), inh = $(root, '[data-in="h"]'), panneau = $(root, '.nt-etapes-calc'), cnv, NA = 6.02e23;
    var MOL = []; for (var q = 0; q < 70; q++) { MOL.push([((q * 0.6180339) % 1), ((q * 0.4142135 * 3.1) % 1), ((q * 0.7320508 * 1.7) % 1), q % 5 === 0, ((q * 47) % 360) * Math.PI / 180]); }   /* positions fixes des molécules dessinées */
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, L = +inL.value, l = +inl.value, h = +inh.value, k = Math.min((W - 110) / (L + l * 0.6), (H - 64) / (h + l * 0.45)), ox = W / 2 - (L + l * 0.6) * k / 2 - 10, oy = H - 34;   /* perspective cavalière : la salle remplit le cadre */
      function P(x, y, z) { return [ox + x * k + z * k * 0.6, oy - y * k - z * k * 0.45]; }
      function poly(pts, fill, stroke) { ctx.beginPath(); pts.forEach(function (p, i) { var q = P(p[0], p[1], p[2]); if (i) { ctx.lineTo(q[0], q[1]); } else { ctx.moveTo(q[0], q[1]); } }); ctx.closePath(); if (fill) { ctx.fillStyle = fill; ctx.fill(); } if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 1; ctx.stroke(); } }
      ctx.clearRect(0, 0, W, H); var gb = ctx.createLinearGradient(0, 0, 0, H); gb.addColorStop(0, '#F8FAFC'); gb.addColorStop(1, '#EEF2F7'); ctx.fillStyle = gb; ctx.fillRect(0, 0, W, H);
      poly([[0, 0, 0], [L, 0, 0], [L, 0, l], [0, 0, l]], '#D9B98A');   /* parquet */
      ctx.strokeStyle = 'rgba(120,80,40,0.25)'; for (var z = 0.5; z < l; z += 0.5) { var a = P(0, 0, z), b = P(L, 0, z); ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.stroke(); }
      var gw = ctx.createLinearGradient(0, P(0, h, l)[1], 0, P(0, 0, l)[1]); gw.addColorStop(0, '#F1F5F9'); gw.addColorStop(1, '#E2E8F0'); poly([[0, 0, l], [L, 0, l], [L, h, l], [0, h, l]], gw);   /* mur du fond */
      poly([[0, 0, 0], [0, 0, l], [0, h, l], [0, h, 0]], '#E7ECF3');   /* mur de gauche, avec une fenêtre */
      poly([[0, h * 0.35, l * 0.25], [0, h * 0.35, l * 0.75], [0, h * 0.85, l * 0.75], [0, h * 0.85, l * 0.25]], '#BAE6FD', '#94A3B8');
      var w1 = P(0, h * 0.6, l * 0.25), w2 = P(0, h * 0.6, l * 0.75); ctx.strokeStyle = '#94A3B8'; ctx.beginPath(); ctx.moveTo(w1[0], w1[1]); ctx.lineTo(w2[0], w2[1]); ctx.stroke();
      poly([[L * 0.3, h * 0.3, l], [L * 0.7, h * 0.3, l], [L * 0.7, h * 0.8, l], [L * 0.3, h * 0.8, l]], '#14532D', '#A16207');   /* tableau */
      var tb = P(L * 0.34, h * 0.65, l); ctx.fillStyle = 'rgba(255,255,255,0.75)'; ctx.font = Math.max(9, k * 0.38) + 'px ' + FONT; ctx.textAlign = 'left'; ctx.fillText('n = N / Nᴀ', tb[0], tb[1]);
      for (var i = 0; i < Math.floor((L - 1) / 2.5); i++) { for (var jj = 0; jj < Math.floor((l - 1) / 1.8); jj++) {   /* tables et chaises */
        var x0 = 1 + i * 2.5, z0 = 0.9 + jj * 1.8;
        poly([[x0, 0.75, z0], [x0 + 1.3, 0.75, z0], [x0 + 1.3, 0.75, z0 + 0.6], [x0, 0.75, z0 + 0.6]], '#B45309');
        [[x0 + 0.05, z0 + 0.05], [x0 + 1.25, z0 + 0.05]].forEach(function (pp) { var a1 = P(pp[0], 0, pp[1]), b1 = P(pp[0], 0.75, pp[1]); ctx.strokeStyle = '#78350F'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(a1[0], a1[1]); ctx.lineTo(b1[0], b1[1]); ctx.stroke(); });
        poly([[x0 + 0.35, 0.45, z0 - 0.45], [x0 + 0.85, 0.45, z0 - 0.45], [x0 + 0.85, 0.45, z0 - 0.05], [x0 + 0.35, 0.45, z0 - 0.05]], '#2563EB');
      } }
      MOL.forEach(function (m) { var q = P(m[0] * L, 0.2 + m[1] * (h - 0.4), m[2] * l), c = m[3] ? '#EF4444' : '#3B82F6', d = Math.max(1.6, k * 0.07); ctx.fillStyle = c; ctx.globalAlpha = 0.65; ctx.beginPath(); ctx.arc(q[0] - d * Math.cos(m[4]), q[1] - d * Math.sin(m[4]), d, 0, 2 * Math.PI); ctx.arc(q[0] + d * Math.cos(m[4]), q[1] + d * Math.sin(m[4]), d, 0, 2 * Math.PI); ctx.fill(); ctx.globalAlpha = 1; });   /* molécules de l'air (très agrandies !) */
      ctx.save(); ctx.strokeStyle = 'rgba(15,23,42,0.45)'; ctx.setLineDash([4, 4]); [[[L, 0, 0], [L, h, 0]], [[0, h, 0], [L, h, 0]], [[L, h, 0], [L, h, l]], [[0, 0, 0], [0, h, 0]], [[L, 0, 0], [L, 0, l]]].forEach(function (sg) { var a1 = P.apply(null, sg[0]), b1 = P.apply(null, sg[1]); ctx.beginPath(); ctx.moveTo(a1[0], a1[1]); ctx.lineTo(b1[0], b1[1]); ctx.stroke(); }); ctx.restore();
      function cote(p1, p2, lab, dx, dy) { var a1 = P.apply(null, p1), b1 = P.apply(null, p2); a1 = [a1[0] + dx, a1[1] + dy]; b1 = [b1[0] + dx, b1[1] + dy]; vec(ctx, (a1[0] + b1[0]) / 2, (a1[1] + b1[1]) / 2, a1[0], a1[1], '#475569', 1.2, 7); vec(ctx, (a1[0] + b1[0]) / 2, (a1[1] + b1[1]) / 2, b1[0], b1[1], '#475569', 1.2, 7); pill(ctx, lab, (a1[0] + b1[0]) / 2, (a1[1] + b1[1]) / 2, { size: 11.5, col: NAVY, stroke: GRID2 }); }
      cote([0, 0, 0], [L, 0, 0], fmt(L, 0) + ' m', 0, 16); cote([L, 0, 0], [L, h, 0], fmt(h, 1) + ' m', 18, 0); cote([L, 0, 0], [L, 0, l], fmt(l, 0) + ' m', 22, 8);
      pill(ctx, '\u25CF dioxygène', 10, 14, { size: 10.5, col: '#DC2626', align: 'left', stroke: GRID2 }); pill(ctx, '\u25CF diazote', 98, 14, { size: 10.5, col: '#2563EB', align: 'left', stroke: GRID2 }); pill(ctx, 'molécules très agrandies\u00A0!', W - 10, 14, { size: 10, col: SLATE, align: 'right', stroke: GRID2 });
    }
    function texte() {
      var L = +inL.value, l = +inl.value, h = +inh.value, V = L * l * h, m = 1.2 * V, mo = 0.23 * m, mn = 0.76 * m, No = mo / 5.3e-26, Nn = mn / 4.7e-26;
      $(root, '.out-L').textContent = fmt(L, 0) + '\u00A0m'; $(root, '.out-l').textContent = fmt(l, 0) + '\u00A0m'; $(root, '.out-h').textContent = fmt(h, 1) + '\u00A0m';
      panneau.innerHTML = '<p class="nt-tag"><i class="fa-solid fa-calculator"></i>Le calcul pour cette salle</p>' +
        '<p><b>Volume&nbsp;:</b> $V = ' + fmt(L, 0) + ' \\times ' + fmt(l, 0) + ' \\times ' + String(fmt(h, 1)).replace(',', '{,}') + ' = \\pu{' + fmt(V, V % 1 ? 1 : 0).replace(/\s/g, ' ') + ' m3}$</p>' +
        '<p><b>Masse d\u2019air&nbsp;:</b> $m = \\rho_\\text{air} \\times V \\approx \\pu{' + fmt(m, 0).replace(/\s/g, ' ') + ' kg}$, dont $\\pu{' + fmt(mo, 0) + ' kg}$ de dioxygène et $\\pu{' + fmt(mn, 0) + ' kg}$ de diazote.</p>' +
        '<p><b>Nombres de molécules&nbsp;:</b> ' + nsci(No, 1) + ' molécules de dioxygène et ' + nsci(Nn, 1) + ' molécules de diazote.</p>' +
        '<p><b>Quantités de matière&nbsp;:</b> $n_{\\ce{O2}} \\approx$ <b>' + nsci(No / NA, 1) + '&nbsp;mol</b> et $n_{\\ce{N2}} \\approx$ <b>' + nsci(Nn / NA, 1) + '&nbsp;mol</b>.</p>';
      typeset(panneau);
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 230 : 280; }, draw);
    [inL, inl, inh].forEach(function (i) { i.addEventListener('input', function () { texte(); draw(cnv); }); });
    texte(); draw(cnv);
  })();

  /* =================== 4. Même masse, même nombre d'atomes ? =================== */
  (function () {
    var root = document.getElementById('lab-piece'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), mode = 'masse', a = 1, cnv;
    var M = [['cuivre', 89, 6.3e22, '#C2410C'], ['aluminium', 5, 8.7e21, '#94A3B8'], ['zinc', 5, 3.5e21, '#64748B'], ['étain', 1, 3.9e20, '#475569']], TOT = 6.3e22 + 8.7e21 + 3.5e21 + 3.9e20;
    function pc(i, md) { return md === 'masse' ? M[i][1] : M[i][2] / TOT * 100; }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, x0 = 60, y0 = 26, hh = H - 70, w = W - x0 - 20, bw = Math.min(90, w / 6), e = a * a * (3 - 2 * a), autre = mode === 'masse' ? 'nombre' : 'masse';
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = '#E2E8F0'; for (var p = 0; p <= 100; p += 20) { var y = y0 + hh - p / 100 * hh; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x0 + w, y); ctx.stroke(); txt(ctx, p + ' %', x0 - 8, y, { size: 10.5, col: SLATE, align: 'right' }); }
      M.forEach(function (m, i) {
        var v = pc(i, autre) + (pc(i, mode) - pc(i, autre)) * e, xc = x0 + (i + 0.5) * w / 4, hb = v / 100 * hh, g = ctx.createLinearGradient(0, y0 + hh - hb, 0, y0 + hh); g.addColorStop(0, m[3]); g.addColorStop(1, '#1E293B');
        ctx.fillStyle = g; rr(ctx, xc - bw / 2, y0 + hh - hb, bw, Math.max(hb, 1), 6); ctx.fill();
        pill(ctx, fmt(v, v < 50 ? 1 : 0) + ' %', xc, y0 + hh - hb - 14, { size: 11.5, col: NAVY, stroke: GRID2 }); txt(ctx, m[0], xc, y0 + hh + 16, { size: 12, col: NAVY });
      });
      if (mode === 'nombre' && a >= 1) { var xa = x0 + 1.5 * w / 4, xz = x0 + 2.5 * w / 4; pill(ctx, 'même masse, mais 2,5 fois plus d\u2019atomes d\u2019aluminium\u00A0!', (xa + xz) / 2, y0 + 8, { size: 11.5, col: '#B91C1C', stroke: '#FECACA' }); }
    }
    function texte() { msg.innerHTML = mode === 'masse' ? 'En masse, l\u2019aluminium et le zinc représentent chacun 5&nbsp;% de la pièce. Passez à la composition en nombre d\u2019atomes&nbsp;!' : 'En nombre d\u2019atomes, l\u2019aluminium représente 11,5&nbsp;% des atomes de la pièce, et le zinc seulement 4,6&nbsp;%&nbsp;: un atome d\u2019aluminium est environ 2,5 fois plus léger qu\u2019un atome de zinc, donc pour la même masse, il y en a 2,5 fois plus.'; }
    var loop = Loop(root, function (dt) { a = Math.min(1, a + dt / 0.9); draw(cnv); return a < 1; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 240 : 280; }, draw);
    $$(root, 'input[name="pc"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; a = RM ? 1 : 0; texte(); if (RM) { draw(cnv); } else { loop.kick(); } }); });
    texte(); draw(cnv);
  })();

  /* =================== 5. Entraînement : calculer une quantité de matière =================== */
  (function () {
    var root = document.getElementById('tr-mole'); if (!root) { return; }
    var qEl = $(root, '.nt-tr-q'), inp = $(root, '#trm-x'), P = null, NA = 6.02e23;
    var E = [   /* échantillon, masse (g), entité, masse de l'entité (g) */
      ['une pépite d\u2019or', [1.5, 2.5, 4.0], 'atomes d\u2019or', 3.27e-22],
      ['un clou en fer', [3.0, 5.6, 8.0], 'atomes de fer', 9.27e-23],
      ['un diamant (carbone pur)', [0.2, 0.5, 1.0], 'atomes de carbone', 1.99e-23],
      ['une gorgée d\u2019eau', [15, 20, 30], 'molécules d\u2019eau', 2.99e-23],
      ['un morceau de sucre', [4.5, 5.0, 6.0], 'molécules de saccharose', 5.68e-22],
      ['une canette en aluminium', [12, 15, 16], 'atomes d\u2019aluminium', 4.48e-23],
      ['un bloc de glace carbonique', [44, 88, 132], 'molécules de dioxyde de carbone', 7.31e-23]
    ];
    function gen() { var e = pick(E), m = pick(e[1]); return { e: e, m: m, N: m / e[3], n: m / e[3] / NA }; }
    var S = Serie(root, 5, {
      show: function () { P = gen(); qEl.innerHTML = 'Quelle est la quantité de matière de ' + P.e[2] + ' dans ' + P.e[0] + ' de ' + fmt(P.m, P.m % 1 ? 1 : 0) + '&nbsp;g&nbsp;? <br><span class="nt-note">Masse d\u2019une entité&nbsp;: ' + nsci(P.e[3], 2) + '&nbsp;g&nbsp;; $N_\\text{A} = \\pu{6,02E23 mol-1}$.</span>'; inp.value = ''; $(root, '[data-act="check"]').disabled = false; typeset(qEl); },
      bilan: function (g, t0) { qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;5</span><br>' + t0; }
    });
    $(root, '[data-act="check"]').addEventListener('click', function () {
      if (S.answered || S.fini) { return; } var x = num(String(inp.value).replace(/\s*[x×]\s*10\^?/, 'e')); if (isNaN(x)) { S.say('Entrez une valeur numérique (par exemple 2,5e-3 pour 2,5 × 10⁻³).'); return; }
      var ok = Math.abs(x - P.n) <= 0.03 * P.n; $(root, '[data-act="check"]').disabled = true;
      S.answer(ok, '$N = \\dfrac{m}{m_\\text{entité}} = $ ' + nsci(P.N, 2) + ' entités, puis $n = \\dfrac{N}{N_\\text{A}} \\approx$ <b>' + nsci(P.n, 2) + '&nbsp;mol</b>.', ok ? null : '<b>Non.</b> '); typeset($(root, '.nt-msg'));
    });
    S.start();
  })();

  /* =================== 6. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    Quiz(root, [
      ['Une mole d\u2019entités contient…', ['$\\pu{6,02E23}$ entités', '12 entités', '$\\pu{6,02E-23}$ entités'], 'C\u2019est la constante d\u2019Avogadro&nbsp;: $\\pu{6,02E23}$ entités par mole.'],
      ['Le symbole de l\u2019unité de quantité de matière est…', ['mol', 'M', 'mo'], 'L\u2019unité est la mole, de symbole mol.'],
      ['Une mole de cuivre et une mole d\u2019aluminium contiennent…', ['le même nombre d\u2019atomes', 'la même masse', 'le même volume'], 'Une mole contient toujours le même nombre d\u2019entités&nbsp;; mais les masses et les volumes diffèrent.'],
      ['Un échantillon contient $\\pu{1,2E24}$ molécules. Sa quantité de matière vaut environ…', ['2,0 mol', '0,50 mol', '$\\pu{7,2E47}$ mol'], '$n = \\dfrac{N}{N_\\text{A}} = \\dfrac{\\pu{1,2E24}}{\\pu{6,02E23 mol-1}} \\approx \\pu{2,0 mol}$.'],
      ['Pour calculer le nombre d\u2019entités dans un échantillon de masse $m$, on calcule…', ['$N = \\dfrac{m}{m_\\text{entité}}$', '$N = m \\times m_\\text{entité}$', '$N = \\dfrac{m_\\text{entité}}{m}$'], 'On divise la masse de l\u2019échantillon par la masse d\u2019une entité, comme pour les huîtres.'],
      ['Une molécule d\u2019eau contient 18 nucléons. Sa masse vaut environ…', ['$\\pu{3,0E-26 kg}$', '$\\pu{1,7E-27 kg}$', '$\\pu{18 kg}$'], '$18 \\times \\pu{1,67E-27 kg} \\approx \\pu{3,0E-26 kg}$&nbsp;: la masse des électrons est négligeable.'],
      ['Même masse d\u2019aluminium et de zinc&nbsp;: lequel contient le plus d\u2019atomes&nbsp;?', ['l\u2019aluminium, car ses atomes sont plus légers', 'le zinc, car ses atomes sont plus lourds', 'aucun, il y en a autant'], 'Pour une même masse, plus les atomes sont légers, plus ils sont nombreux.'],
      ['Une mole de nucléons a une masse d\u2019environ…', ['1 g', '1 kg', '6 g'], 'C\u2019est l\u2019idée qui a guidé le choix du nombre d\u2019Avogadro&nbsp;: $\\pu{6,02E23} \\times \\pu{1,67E-24 g} \\approx \\pu{1 g}$.']
    ], 8);
  })();

})();
</script>
