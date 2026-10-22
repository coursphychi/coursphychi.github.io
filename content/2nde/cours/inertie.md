+++
title = "Principe d'inertie"
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
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Pourquoi un objet lâché dans la station spatiale flotte-t-il en ligne droite, alors que sur Terre il tombe&nbsp;? Pourquoi faut-il pousser une voiture pour la faire démarrer, mais aussi pour l’arrêter&nbsp;? Ce chapitre présente la loi qui relie le mouvement d’un système aux actions qu’il subit&nbsp;: le <b>principe d’inertie</b>, puis la façon de modéliser ces actions par des <b>forces</b>.</p>

## Le principe d'inertie {.nt-h2}

### Une observation dans la station spatiale {.nt-h3}

<p>Observons ce qui arrive à tout objet lâché dans la Station spatiale internationale (ISS), qu'on le lâche sans vitesse ou en lui donnant une petite impulsion. Comment décrire le mouvement de ces objets, en les assimilant à des points matériels&nbsp;?</p>

<div class="nt-lab" id="lab-iss">
<p class="nt-tag"><i class="fa-solid fa-satellite"></i>Animation</p>
<p class="nt-lab-title">Des objets lâchés dans l'ISS</p>
<canvas role="img" aria-label="Coupe d'un module de la station spatiale, dans l'espace ; quelques objets partent du centre avec de petites vitesses, et l'on suit leurs positions successives."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="lancer"><i class="fa-solid fa-play"></i>&nbsp; Lâcher les objets</button><label class="nt-check"><input type="checkbox" data-in="chrono" checked> Chronophotographie</label><label class="nt-check"><input type="checkbox" data-in="vec" checked> Vecteurs vitesse</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Que peut-on dire du mouvement d'un objet lâché ou lancé dans la station, tant qu'il ne touche rien&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Il garde sa vitesse</span></summary>
<div class="nt-d-body">
<p>Dans le référentiel de la station, un objet lâché sans vitesse reste <b>immobile</b>, et un objet lancé se déplace en <b>ligne droite</b>, avec des positions également espacées sur la chronophotographie&nbsp;: son mouvement est <b>rectiligne uniforme</b>. Son vecteur vitesse reste le même&nbsp;: même direction, même sens, même norme. Il ne changerait que si quelque chose agissait sur l'objet, par exemple s'il venait heurter une paroi.</p>
</div>
</details>

### Énoncé du principe {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: le principe d'inertie</p>
<p>Tout système persévère dans son état de <span class="imp nt-hole">repos</span> ou de <span class="imp nt-hole">mouvement rectiligne uniforme</span>, à moins qu'il ne soit contraint, par des <span class="imp nt-hole">actions</span> s'exerçant sur lui, à changer cet état.</p>
</div>

<p>C'est une <b>équivalence</b> (une propriété «&nbsp;si et seulement si&nbsp;»), qu'on peut réexprimer ainsi&nbsp;:</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: une autre formulation</p>
<p>Si <span class="nt-force">aucune action non compensée</span> ne s'exerce sur un système, alors son <span class="nt-v">vecteur vitesse</span> <span class="imp nt-hole">reste constant</span>.</p>
<p>Et inversement, si le <span class="nt-v">vecteur vitesse</span> d'un système reste constant, alors <span class="nt-force">aucune action non compensée</span> ne s'exerce sur lui.</p>
</div>

<p>«&nbsp;Non compensée&nbsp;» signifie que les actions qui s'exercent sur le système ne s'annulent pas les unes les autres. Une action compensée par une autre n'a pas d'effet sur le mouvement. Schématiquement&nbsp;:</p>

<div class="nt-equiv">
<span class="nt-force nt-barre">action</span><span>$\Leftrightarrow$</span><span class="nt-v">$\vec{v} = \overrightarrow{\text{cste}}$</span>
</div>

<p>La <b>contraposée</b> du principe d'inertie est tout aussi utile&nbsp;:</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: la contraposée</p>
<p>Si le <span class="nt-v">vecteur vitesse</span> d'un système <span class="imp nt-hole">n'est pas constant</span>, alors il y a <span class="nt-force">au moins une action non compensée</span> qui s'exerce sur lui.</p>
<p>Et inversement, s'il y a une <span class="nt-force">action non compensée</span>, alors le <span class="nt-v">vecteur vitesse</span> du système n'est pas constant.</p>
</div>

<div class="nt-equiv">
<span class="nt-v">$\vec{v} \neq \overrightarrow{\text{cste}}$</span><span>$\Leftrightarrow$</span><span class="nt-force">action</span>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Le vecteur vitesse n'est pas constant dès que l'une de ses trois caractéristiques change&nbsp;: sa <b>norme</b> (le système accélère ou ralentit), mais aussi sa <b>direction</b> (le système tourne), même à vitesse constante. Un mouvement circulaire uniforme n'est donc pas un mouvement «&nbsp;sans action&nbsp;».</p>
</div>

<div class="nt-lab nt-quizlab" id="quiz-logique">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Que peut-on conclure&nbsp;?</p>
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

### Et sur Terre&nbsp;? {.nt-h3}

<p>Sur Terre, un objet lâché tombe&nbsp;: son vecteur vitesse n'est pas constant, il subit une action, celle de la Terre. Mais cette action est <b>verticale</b>. Dans la direction horizontale, si l'on néglige l'action de l'air, rien n'agit sur lui&nbsp;: le principe d'inertie s'applique alors à cette seule direction, et l'objet <b>conserve sa vitesse horizontale</b>. Nous détaillerons ce raisonnement dans la partie 3, une fois les forces introduites.</p>

<div class="nt-lab" id="lab-velo">
<p class="nt-tag"><i class="fa-solid fa-bicycle"></i>Animation</p>
<p class="nt-lab-title">Une balle lâchée depuis un vélo</p>
<div class="nt-btns"><span class="nt-note">Observer depuis&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="vl-ref" value="sol" checked><span>le sol</span></label><label><input type="radio" name="vl-ref" value="velo"><span>le vélo</span></label></div></div>
<canvas role="img" aria-label="Un cycliste roule à vitesse constante et lâche une balle de tennis au milieu de la scène ; on suit sa chute dans le référentiel choisi."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="inertie" checked> Principe d'inertie</label><label class="nt-check"><input type="checkbox" data-in="traj" checked> Trajectoire</label><label class="nt-check"><input type="checkbox" data-in="ralenti"> Ralenti</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Première approche</p>
<p>Le principe d'inertie peut s'appliquer à une seule direction&nbsp;: un objet qui ne subit que l'action de la Terre, verticale, ne subit aucune action horizontale et conserve donc sa vitesse horizontale. Nous y reviendrons en détail dans la partie 3.</p>
</div>

### Un principe valable dans certains référentiels seulement {.nt-h3}

<p>Revenons dans la station spatiale. Régulièrement, l'ISS allume ses moteurs pour remonter un peu son orbite&nbsp;: c'est un <i>reboost</i>. Que deviennent les objets qui flottent à l'intérieur&nbsp;?</p>

<div class="nt-lab" id="lab-boost">
<p class="nt-tag"><i class="fa-solid fa-rocket"></i>Animation</p>
<p class="nt-lab-title">Les moteurs de la station s'allument</p>
<div class="nt-btns"><span class="nt-note">Observer depuis&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="bs-ref" value="station" checked><span>la station</span></label><label><input type="radio" name="bs-ref" value="etoiles"><span>les étoiles</span></label></div></div>
<canvas role="img" aria-label="Coupe d'un module de la station avec un astronaute et des objets qui flottent ; les moteurs s'allument et la station accélère."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="boost"><i class="fa-solid fa-fire"></i>&nbsp; Allumer les moteurs</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>Dans le référentiel de la station, pendant la poussée des moteurs, les objets se mettent en mouvement vers l'arrière alors que rien n'agit sur eux&nbsp;: le principe d'inertie <b>n'y est plus vérifié</b>. Observée depuis les étoiles, la scène redevient simple&nbsp;: ce sont les objets qui gardent leur vitesse, et la station qui accélère autour d'eux.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le principe d'inertie n'est valable que dans certains référentiels, appelés <span class="imp nt-hole">référentiels galiléens</span>. Pour les mouvements de courte durée à la surface de la Terre, le <span class="imp nt-hole">référentiel terrestre</span> est une très bonne approximation d'un référentiel galiléen.</p>
</div>

<p>On a déjà rencontré cet effet dans le chapitre sur le mouvement&nbsp;: dans un train qui démarre, un objet posé sur une tablette très glissante semblerait partir vers l'arrière sans que rien ne le pousse. Le référentiel du train qui accélère n'est pas galiléen.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Et si la Terre s'arrêtait soudain de tourner&nbsp;?</span></summary>
<div class="nt-d-body">
<p>La Terre fait un tour sur elle-même en 24&nbsp;heures environ. Un point de l'équateur parcourt donc le périmètre de la Terre, environ $\pu{40 000 km}$, en 24&nbsp;h&nbsp;: sa vitesse vaut à peu près $\dfrac{\pu{40 000 km}}{\pu{24 h}} \approx \pu{1 670 km*h-1}$, soit $\pu{465 m*s-1}$, environ 1,4 fois la vitesse du son dans l'air ($\pu{340 m*s-1}$).</p>
<p>Cette vitesse diminue quand on s'éloigne de l'équateur, car le cercle parcouru en 24&nbsp;h est de plus en plus petit&nbsp;: elle passe sous la vitesse du son vers 43° de latitude (à peu près celle de Marseille ou de Toulouse), vaut encore environ $\pu{1 150 km*h-1}$ au centre de la France, et devient nulle aux pôles.</p>
<p>Si le sol s'arrêtait brusquement, tout ce qui n'y est pas solidement attaché (l'air, l'eau des océans, les personnes, les voitures…) conserverait cette vitesse, en vertu du principe d'inertie&nbsp;: des vents supersoniques sur une grande partie du globe, des vagues gigantesques, et tous les objets projetés vers l'est. Rassurez-vous&nbsp;: aucun phénomène connu ne peut arrêter la rotation de la Terre aussi brutalement.</p>
</div>
</details>

## Actions et forces {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Une <span class="imp nt-hole">action</span> est ce qui permet à un système de modifier le mouvement d'un autre système (ou de le déformer).</p>
<p>On modélise une action par une <span class="imp nt-hole">force</span>, représentée par un <span class="imp nt-hole">vecteur</span>&nbsp;: sa direction et son sens sont ceux de l'action (la Terre attire vers le bas, une corde tire le long de la corde…), et sa norme est l'intensité de la force, qui s'exprime en <span class="imp nt-hole">newton (N)</span>.</p>
</div>

<p>On note $\overrightarrow{F}_{\text{A}\to\text{B}}$ la force qui modélise l'action du système A sur le système B.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-apple-whole"></i>Ordre de grandeur</p>
<p>Un newton, c'est à peu près la force qu'il faut pour tenir une petite pomme de 100&nbsp;g dans la main&nbsp;: c'est son poids. Soulever un sac de 10&nbsp;kg demande environ 100&nbsp;N, et un élève de 60&nbsp;kg pèse environ 600&nbsp;N.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Une force n'est pas forcément dans le sens du mouvement&nbsp;! Un parachutiste qui descend à vitesse constante subit son poids, vers le bas, et l'action de l'air, vers le haut. C'est la <b>somme</b> des forces qui renseigne sur la variation du mouvement&nbsp;: ici, elle est nulle, et le vecteur vitesse reste constant.</p>
</div>

### Le diagramme objet-interaction {.nt-h3}

<p>Pour savoir ce qui agit sur un système, on fait l'inventaire des objets en interaction avec lui dans un <span class="imp">diagramme objet-interaction</span> (DOI)&nbsp;:</p>

<ul class="nt-facts">
<li>le système étudié est placé au centre, entouré d'un cercle rose&nbsp;;</li>
<li>chaque objet qui agit sur lui est relié au système par une double flèche&nbsp;: <b>en trait plein</b> pour une action de <b>contact</b> (le sol, l'air, un fil…), <b>en pointillés</b> pour une action <b>à distance</b> (la Terre, un aimant…).</li>
</ul>

<p>On assimile ensuite le système à un <span class="imp">point matériel</span>, un point qui concentre toute sa masse, et on représente chaque action par un vecteur force partant de ce point.</p>

<div class="nt-lab" id="lab-doi">
<p class="nt-tag"><i class="fa-solid fa-diagram-project"></i>Animation pas à pas</p>
<p class="nt-lab-title">Du DOI aux forces</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="doi-ex" value="para" checked><span>Parachutiste</span></label><label><input type="radio" name="doi-ex" value="seau"><span>Seau posé</span></label><label><input type="radio" name="doi-ex" value="balle"><span>Balle au bout d'un fil</span></label><label><input type="radio" name="doi-ex" value="moto"><span>Moto qui accélère</span></label><label><input type="radio" name="doi-ex" value="ballon"><span>Ballon après le lancer</span></label></div></div>
<p class="nt-note nt-center nt-doi-q"></p>
<div class="nt-chips"></div>
<div class="nt-types" hidden></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="valider"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
<canvas class="nt-c-doi" role="img" aria-label="Diagramme objet-interaction : le système au centre, relié par des doubles flèches aux objets qui agissent sur lui."></canvas>
<p class="nt-msg nt-msg-doi" aria-live="polite"></p>
<div class="nt-piege" hidden></div>
<div class="nt-forces" hidden>
<canvas class="nt-c-f" role="img" aria-label="Le système modélisé par un point matériel, avec les vecteurs forces et leur somme."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="decomp" hidden><i class="fa-solid fa-arrows-split-up-and-left"></i>&nbsp; Décomposer la force du sol</button><button type="button" class="nt-btn nt-btn-main" data-act="anim" hidden><i class="fa-solid fa-play"></i>&nbsp; Animer le mouvement de la balle</button></div>
<p class="nt-msg nt-msg-f" aria-live="polite"></p>
</div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: le principe d'inertie avec les forces</p>
<p>Dire que les actions qui s'exercent sur un système se compensent, c'est dire que la <span class="imp nt-hole">somme des forces</span> qui s'exercent sur lui est <span class="imp nt-hole">nulle</span>. Le principe d'inertie s'écrit alors&nbsp;:</p>
<p class="nt-big">${\color{#9A3412}\sum \overrightarrow{F} = \vec{0} \quad \Leftrightarrow \quad \vec{v} = \overrightarrow{\text{cste}}}$</p>
<p>et sa contraposée&nbsp;: ${\color{#9A3412}\sum \overrightarrow{F} \neq \vec{0} \Leftrightarrow \vec{v} \neq \overrightarrow{\text{cste}}}$.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode&nbsp;: exploiter le principe d'inertie</p>
<ol class="nt-steps">
<li><p>Préciser le <b>système</b> étudié et le <b>référentiel</b> (en général le référentiel terrestre).</p></li>
<li><p>Faire l'inventaire des actions dans un <b>DOI</b>.</p></li>
<li><p>Modéliser chaque action par une <b>force</b>, représentée à partir du point matériel.</p></li>
<li><p><b>Conclure</b>, dans un sens ou dans l'autre&nbsp;: si l'on connaît les forces, on en déduit la nature du mouvement&nbsp;; si l'on connaît le mouvement, on en déduit si les forces se compensent ou non.</p></li>
</ol>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Une voiture roule sur une route horizontale et rectiligne, à vitesse constante. Que peut-on dire des forces qui s'exercent sur elle&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse rédigée</span><span class="nt-sum">La méthode, étape par étape</span></summary>
<div class="nt-d-body">
<p><b>Système et référentiel&nbsp;:</b><br>
Le système est la voiture, étudiée dans le référentiel terrestre.</p>
<p><b>DOI&nbsp;:</b><br>
La voiture est en interaction avec la Terre (action à distance), la route et l'air (actions de contact).</p>
<p><b>Forces&nbsp;:</b><br>
Elle subit son poids $\overrightarrow{P}$, vertical vers le bas, la force de la route, qui se compose de la réaction du support (verticale, vers le haut) et de la force de propulsion (horizontale, vers l'avant), et les frottements de l'air (horizontaux, vers l'arrière).</p>
<p><b>Invocation du principe d'inertie&nbsp;:</b><br>
D'après l'énoncé, le <b>mouvement</b> de la voiture est <b>rectiligne uniforme</b> (le vecteur vitesse est constant). <b>D'après le principe d'inertie, la somme des forces doit être nulle</b>. 
<p><b>Conclusion&nbsp;:</b><br>
Les forces verticales et horizontales se compensent alors deux à deux.<br>
La réaction du support compense donc le poids, et la force de propulsion compense les frottements de l'air.</p>
</div>
</details>

### Le poids {.nt-h3}

<p>Le <span class="imp">poids</span> $\overrightarrow{P}$ modélise l'action de la Terre sur un système situé à sa surface. Il est <span class="imp nt-hole">vertical</span>, orienté <span class="imp nt-hole">vers le bas</span>, et sa valeur est donnée par&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$P = m \times g$</p>
<div class="nt-f-units"><span>$P$&nbsp;: poids en <b>N</b></span><span>$m$&nbsp;: masse du système en <b>kg</b></span><span>$g$&nbsp;: intensité de la pesanteur en <b>N·kg<sup>−1</sup></b> (c'est-à-dire N/kg)&nbsp;; sur Terre, $g = \pu{9,8 N*kg-1}$</span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On écrit aussi $g = \pu{9,8 m*s-2}$&nbsp;: les deux unités sont équivalentes, car $\pu{1 N} = \pu{1 kg*m*s-2}$. Il ne faut pas confondre la <b>masse</b> (en kg), qui ne dépend pas du lieu, et le <b>poids</b> (en N), qui en dépend&nbsp;: sur la Lune, où $g = \pu{1,6 N*kg-1}$, un astronaute de même masse pèse six fois moins lourd.</p>
</div>

<div class="nt-lab nt-trainer" id="tr-poids">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Masse et poids</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-ans"><span class="nt-champ"><label for="trp-x" class="nt-trp-l"></label><input id="trp-x" type="text" inputmode="decimal" autocomplete="off"><span class="nt-u nt-trp-u"></span></span><button type="button" class="nt-btn nt-btn-main" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="next">Question suivante</button></div>
</div>

## Le principe d'inertie dans la vie de tous les jours {.nt-h2}

<p>Pas besoin de vivre dans l'ISS pour observer les effets du principe d'inertie. L'exemple le plus simple&nbsp;: un objet au repos a tendance à rester au repos si rien ne le met en mouvement.</p>

<p>Sur Terre, deux obstacles empêchent cependant d'observer les beaux mouvements rectilignes uniformes de la station&nbsp;:</p>
<ul class="nt-facts">
<li><b>Les frottements</b> freinent l'objet en mouvement. Il y en avait aussi dans l'ISS, ceux de l'air, mais ils sont beaucoup plus faibles que ceux d'un support solide. Leur effet dépend de la durée d'observation (partie 3.1).</li>
<li><b>Le poids</b> agit toujours… à moins qu'une autre force ne le compense, comme la réaction d'un support horizontal. Et même quand il n'est pas compensé, il n'agit que verticalement&nbsp;: le principe d'inertie s'applique encore horizontalement (partie 3.2).</li>
</ul>

### Frottements et échelle de temps {.nt-h3}

<p>Si l'on diminue fortement les frottements, sur de la glace ou sur un coussin d'air, le principe d'inertie est plutôt bien illustré&nbsp;: le mouvement se conserve… du moins pendant un certain temps.</p>

<div class="nt-lab" id="lab-palet">
<p class="nt-tag"><i class="fa-solid fa-hockey-puck"></i>Animation</p>
<p class="nt-lab-title">Un palet lancé sur différentes surfaces</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="pl-s" value="air" checked><span>Coussin d'air</span></label><label><input type="radio" name="pl-s" value="glace"><span>Glace</span></label><label><input type="radio" name="pl-s" value="parquet"><span>Parquet</span></label><label><input type="radio" name="pl-s" value="moquette"><span>Moquette</span></label></div></div>
<canvas role="img" aria-label="Vue de dessus d'un palet lancé sur une piste ; chronophotographie de ses positions successives."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="lancer"><i class="fa-solid fa-play"></i>&nbsp; Lancer le palet</button><span class="nt-note">Durée d'observation&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="pl-d" value="court" checked><span>courte (0,6 s)</span></label><label><input type="radio" name="pl-d" value="long"><span>longue (6 s)</span></label></div></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>L'<span class="imp nt-hole">échelle de temps</span> de l'observation est primordiale&nbsp;: sur une durée très courte, on observe facilement des mouvements presque rectilignes uniformes, alors que sur des durées plus longues, les frottements finissent toujours par modifier le mouvement.</p>
</div>

### La vitesse horizontale se conserve {.nt-h3}

<p>Dans la partie 1, la balle lâchée depuis un vélo nous a montré qu'un objet qui ne subit que l'action de la Terre conserve sa vitesse horizontale. Maintenant que nous savons modéliser les actions par des forces, détaillons ce raisonnement.</p>

<p>Un objet lancé ne suit pas une ligne droite&nbsp;: il retombe, car son poids n'est compensé par rien. Le principe d'inertie semble ne plus servir à rien… Pourtant, il continue de s'appliquer, à condition de regarder le mouvement <b>direction par direction</b>&nbsp;:</p>

<div class="nt-dirs">
<div class="nt-dir nt-dir-h"><b><i class="fa-solid fa-arrows-left-right"></i>&nbsp; Horizontalement</b><span>Le poids est vertical&nbsp;: il ne tire ni vers l'avant, ni vers l'arrière.</span><span>Si l'on néglige les frottements de l'air, <b>aucune action horizontale</b> ne s'exerce.</span><span>D'après le principe d'inertie, la <b>vitesse horizontale reste constante</b>.</span><span class="nt-dir-res">mouvement horizontal uniforme</span></div>
<div class="nt-dir nt-dir-v"><b><i class="fa-solid fa-arrows-up-down"></i>&nbsp; Verticalement</b><span>Le poids, vertical et vers le bas, n'est compensé par rien.</span><span>Une <b>action non compensée</b> s'exerce.</span><span>D'après la contraposée du principe d'inertie, la <b>vitesse verticale change</b>&nbsp;: elle diminue à la montée, puis augmente à la descente.</span><span class="nt-dir-res">montée ralentie, puis chute accélérée</span></div>
</div>

<p>Pour «&nbsp;voir&nbsp;» la vitesse horizontale, il suffit de regarder l'ombre de l'objet sur le sol, quand le Soleil est haut dans le ciel&nbsp;: elle ne garde que le mouvement horizontal. Lors d'une chandelle au rugby, l'ombre du ballon avance à vitesse constante, alors que le ballon monte puis redescend.</p>

<div class="nt-lab" id="lab-rugby">
<p class="nt-tag"><i class="fa-solid fa-football"></i>Animation</p>
<p class="nt-lab-title">La chandelle au rugby</p>
<canvas role="img" aria-label="Un joueur tape une chandelle ; le ballon monte puis redescend, et son ombre avance sur le sol à vitesse constante ; à gauche, la projection verticale du ballon."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Taper la chandelle</button><label class="nt-check"><input type="checkbox" data-in="chrono" checked> Chronophotographie</label><label class="nt-check"><input type="checkbox" data-in="comp" checked> Décomposer la vitesse</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>C'est exactement ce qui se passait pour la <b>balle lâchée depuis le vélo</b>&nbsp;: elle conservait la vitesse horizontale du cycliste, et tombait donc à côté de lui. C'est aussi ce qu'on a vu dans le chapitre sur le mouvement, avec la balle qui rebondit sur une remorque tirée par un tracteur&nbsp;: tant que le tracteur roule à vitesse constante, la balle retombe toujours sur le trampoline… mais s'il accélère ou freine pendant qu'elle est en l'air, elle garde sa vitesse horizontale et le rate&nbsp;!</p>

<div class="nt-lab" id="lab-tramp">
<p class="nt-tag"><i class="fa-solid fa-tractor"></i>Animation</p>
<p class="nt-lab-title">Une balle qui rebondit sur une remorque</p>
<div class="nt-btns"><span class="nt-note">Observer depuis&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="tp-ref" value="tracteur" checked><span>le tracteur</span></label><label><input type="radio" name="tp-ref" value="sol"><span>le sol</span></label></div></div>
<canvas role="img" aria-label="Une balle rebondit sur un trampoline tiré par un tracteur ; trajectoire en pointillés et vecteur vitesse de la balle."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="acc"><i class="fa-solid fa-gauge-high"></i>&nbsp; Accélérer</button><button type="button" class="nt-btn" data-act="frein"><i class="fa-solid fa-hand"></i>&nbsp; Freiner</button><button type="button" class="nt-btn nt-btn-main" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-in="comp" checked> Décomposer la vitesse</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Un objet soumis uniquement à son poids (frottements négligés) <span class="imp nt-hole">conserve sa vitesse horizontale</span>, tandis que sa vitesse verticale varie. C'est la conséquence la plus courante du principe d'inertie dans la vie de tous les jours&nbsp;: ballons, projectiles, sauts, objets lâchés depuis un véhicule…</p>
</div>

## Le principe des actions réciproques {.nt-h2}

<p>Une action va toujours dans les deux sens&nbsp;: quand on pousse un mur, le mur nous repousse.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: le principe des actions réciproques (troisième loi de Newton)</p>
<p>Si un système A agit sur un système B, alors le système B agit sur le système A avec une action <span class="imp nt-hole">exactement opposée</span>&nbsp;: même direction, même intensité, mais sens contraire.</p>
<p class="nt-big">${\color{#9A3412}\overrightarrow{F}_{\text{A}\to\text{B}} = -\overrightarrow{F}_{\text{B}\to\text{A}}}$</p>
</div>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-l' viewBox='0 0 700 250' role='img' aria-label="Un petit ourson pousse une voiture ; la force de l'ourson sur la voiture et celle de la voiture sur l'ourson ont même direction, même intensité et des sens opposés."><defs><linearGradient id='caisse-o' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#F8FAFC'/><stop offset='0.55' stop-color='#E2E8F0'/><stop offset='1' stop-color='#CBD5E1'/></linearGradient><linearGradient id='vitre-o' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#475569'/><stop offset='1' stop-color='#1E293B'/></linearGradient></defs><rect x='0' y='214' width='700' height='3' fill='#A8A29E'/><ellipse cx='470' cy='215' rx='200' ry='6' fill='rgba(15,23,42,0.14)'/><ellipse cx='204' cy='215' rx='24' ry='4' fill='rgba(15,23,42,0.12)'/><g fill='#F9A8D4'><circle cx='196' cy='144' r='19'/><circle cx='182' cy='128' r='7'/><circle cx='210' cy='128' r='7'/><ellipse cx='200' cy='184' rx='19' ry='24'/><rect x='186' y='198' width='10' height='16' rx='5'/><rect x='204' y='198' width='10' height='16' rx='5'/><path d='M206,168 L246,147 L250,155 L210,176 Z'/></g><g fill='#BE185D'><circle cx='182' cy='128' r='3.5'/><circle cx='210' cy='128' r='3.5'/></g><ellipse cx='204' cy='149' rx='7' ry='5' fill='#FCE7F3'/><g fill='#831843'><circle cx='191' cy='140' r='2.3'/><circle cx='204' cy='140' r='2.3'/><ellipse cx='206' cy='148' rx='3' ry='2.2'/></g><path d='M250,186 L250,150 Q251,134 266,131 L318,126 L366,86 Q372,80 384,79 L500,77 Q520,77 536,86 L598,124 L660,132 Q684,136 688,156 L690,180 Q690,188 682,190 L640,190 A40,40 0 0 0 562,190 L376,190 A40,40 0 0 0 298,190 Z' fill='url(#caisse-o)' stroke='#64748B' stroke-width='2' stroke-linejoin='round'/><path d='M334,124 L376,90 Q380,87 388,87 L452,86 L452,124 Z' fill='url(#vitre-o)'/><path d='M462,124 L462,86 L498,86 Q512,86 522,92 L578,124 Z' fill='url(#vitre-o)'/><path d='M346,118 L372,96' stroke='rgba(255,255,255,0.35)' stroke-width='4' stroke-linecap='round'/><path d='M262,150 L680,150' stroke='#94A3B8' stroke-width='1.2'/><path d='M457,126 L457,186' stroke='#94A3B8' stroke-width='1.2'/><path d='M572,128 Q576,160 566,186' stroke='#94A3B8' stroke-width='1.2' fill='none'/><rect x='428' y='138' width='18' height='4' rx='2' fill='#94A3B8'/><rect x='534' y='138' width='18' height='4' rx='2' fill='#94A3B8'/><path d='M584,122 L596,118 L600,127 L588,128 Z' fill='#64748B'/><path d='M250,140 L262,140 L262,160 L250,160 Z' fill='#DC2626'/><path d='M660,140 Q676,141 684,150 L664,152 Z' fill='#FDE68A' stroke='#CA8A04' stroke-width='1'/><path d='M298,190 A39,39 0 0 1 376,190 Z' fill='#475569'/><path d='M562,190 A39,39 0 0 1 640,190 Z' fill='#475569'/><circle cx='337' cy='181' r='33' fill='#111827'/><circle cx='337' cy='181' r='19' fill='#CBD5E1'/><circle cx='337' cy='181' r='19' fill='none' stroke='#94A3B8' stroke-width='3' stroke-dasharray='6 6'/><circle cx='337' cy='181' r='5' fill='#475569'/><circle cx='601' cy='181' r='33' fill='#111827'/><circle cx='601' cy='181' r='19' fill='#CBD5E1'/><circle cx='601' cy='181' r='19' fill='none' stroke='#94A3B8' stroke-width='3' stroke-dasharray='6 6'/><circle cx='601' cy='181' r='5' fill='#475569'/><line x1='250.0' y1='151.0' x2='348.0' y2='151.0' stroke='#E5484D' stroke-width='3.2' stroke-linecap='round'/><polygon points='360.0,151.0 345.0,158.0 345.0,144.0' fill='#E5484D'/><text x='367.0' y='157' font-size='17' fill='#B42318' font-family='Georgia, "Times New Roman", serif' font-style='italic'>F<tspan font-size='11' dy='5' font-style='normal'>ourson→voiture</tspan></text><line x1='367.5' y1='141.4' x2='376.5' y2='141.4' stroke='#B42318' stroke-width='1.2' stroke-linecap='round'/><polygon points='380.5,141.4 375.5,143.8 375.5,139.0' fill='#B42318'/><line x1='250.0' y1='151.0' x2='152.0' y2='151.0' stroke='#E5484D' stroke-width='3.2' stroke-linecap='round'/><polygon points='140.0,151.0 155.0,144.0 155.0,158.0' fill='#E5484D'/><text x='42.3' y='157' font-size='17' fill='#B42318' font-family='Georgia, "Times New Roman", serif' font-style='italic'>F<tspan font-size='11' dy='5' font-style='normal'>voiture→ourson</tspan></text><line x1='42.8' y1='141.4' x2='51.8' y2='141.4' stroke='#B42318' stroke-width='1.2' stroke-linecap='round'/><polygon points='55.8,141.4 50.8,143.8 50.8,139.0' fill='#B42318'/><circle cx='250' cy='151' r='3.5' fill='#1E293B'/></svg></div>
<p class="nt-cap">L'ourson pousse la voiture, et la voiture pousse l'ourson&nbsp;: les deux forces ont la même intensité. Elles ne se compensent pas pour autant, car elles s'exercent sur deux systèmes différents.</p>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention à ne pas confondre</p>
<p>Deux forces <b>réciproques</b> modélisent les deux sens d'une même interaction&nbsp;: elles s'exercent sur <b>deux systèmes différents</b>, et ne peuvent donc jamais se compenser. Deux forces qui <b>se compensent</b> s'exercent au contraire sur <b>le même système</b>, et proviennent de deux interactions différentes.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<p>Un livre posé sur une table est soumis à deux forces : la force de la Terre sur le livre (poids) et la force de la table sur le livre (réaction du support). Ces deux forces se compensent d'après le principe d'inertie.

La force du livre sur la Terre, réciproque à celle de la Terre sur le livre, n'agit pas sur le livre (elle agit sur la Terre) et ne participe donc pas au bilan des forces sur le livre.</p>
</div>


<div class="nt-lab nt-quizlab" id="quiz-reciproque">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Réciproques ou compensées&nbsp;?</p>
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

<div class="nt-lab" id="lab-pousse">
<p class="nt-tag"><i class="fa-solid fa-user-astronaut"></i>Animation</p>
<p class="nt-lab-title">Un astronaute pousse un objet</p>
<div class="nt-btns"><span class="nt-note">L'astronaute (100&nbsp;kg avec sa combinaison) pousse&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="ps-m" value="0.06" checked><span>une balle (60 g)</span></label><label><input type="radio" name="ps-m" value="10"><span>un sac (10 kg)</span></label><label><input type="radio" name="ps-m" value="100"><span>un collègue (100 kg)</span></label><label><input type="radio" name="ps-m" value="400"><span>une caisse (400 kg)</span></label></div></div>
<canvas role="img" aria-label="Un astronaute flottant pousse un objet ; pendant la poussée, deux forces opposées de même intensité ; ensuite, les deux s'éloignent."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="pousser"><i class="fa-solid fa-hand"></i>&nbsp; Pousser</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>Appliquer la même force à des objets de masses différentes n'a pas le même effet&nbsp;: pousser un vélo ou pousser un camion ne donne pas le même résultat. Plus la masse est grande, plus la vitesse acquise est petite.</p>

### La Terre bouge-t-elle quand on saute&nbsp;? {.nt-h3}

<p>La Terre agit sur nous autant que nous agissons sur elle. Pourquoi alors ne bouge-t-elle pas quand on saute&nbsp;? En fait… elle bouge&nbsp;! Mais il est raisonnable de supposer que les déplacements du sauteur et de la Terre sont <b>inversement proportionnels</b> à leurs masses&nbsp;: plus la masse est grande, plus le «&nbsp;saut&nbsp;» est petit.</p>


<div class="nt-duo">
<div class="nt-carte nt-carte-s"><span class="nt-emo">🧑</span><b>Le sauteur</b><span>masse&nbsp;: <span class="nt-m">60&nbsp;kg</span></span><span>il s'élève de <span class="nt-depl">50&nbsp;cm</span></span></div>
<div class="nt-carte nt-carte-t"><span class="nt-emo">🌍</span><b>La Terre</b><span>masse&nbsp;: <span class="nt-m">6&nbsp;×&nbsp;10<sup>24</sup>&nbsp;kg</span></span><span>elle recule de… <span class="nt-depl">?</span></span></div>
</div>

<p>«&nbsp;Inversement proportionnel&nbsp;» signifie que le rapport des déplacements est l'inverse du rapport des masses&nbsp;:</p>
<p class="nt-big">$\dfrac{{\color{#059669}d_\text{Terre}}}{{\color{#059669}d_\text{sauteur}}} = \dfrac{{\color{#2563EB}m_\text{sauteur}}}{{\color{#2563EB}M_\text{Terre}}}$</p>
<p style="text-align:center;">d'où&nbsp;: ${\color{#059669}d_\text{Terre}} = \pu{0,5 m} \times \dfrac{\pu{60 kg}}{\pu{6E24 kg}} = {\color{#059669}\pu{5E-24 m}}$.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-ruler"></i>Pour se faire une idée</p>
<p>Un atome mesure environ $\pu{1E-10 m}$, et le noyau d'un atome environ $\pu{1E-15 m}$. Le recul de la Terre, $\pu{5E-24 m}$, est donc <b>un milliard de fois plus petit que le noyau d'un atome</b>&nbsp;!</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-people-group"></i>Défi</p>
<p>Et si les 8&nbsp;milliards d'humains, de 70&nbsp;kg en moyenne, sautaient tous ensemble, au même instant, de 50&nbsp;cm&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Toujours aussi ridicule</span></summary>
<div class="nt-d-body">
<p>La masse totale des sauteurs vaut $\pu{8E9} \times \pu{70 kg} \approx \pu{6E11 kg}$, d'où ${\color{#059669}d_\text{Terre}} = \pu{0,5 m} \times \dfrac{\pu{6E11 kg}}{\pu{6E24 kg}} = {\color{#059669}\pu{5E-14 m}}$.</p>
<p>C'est quelques dizaines de fois la taille d'un proton&nbsp;: aucun instrument ne pourrait le détecter. Et quand tout le monde retombe, la Terre revient exactement à sa place&nbsp;!</p>
</div>
</details>

## Force d'interaction gravitationnelle et poids {.nt-h2}

<p>La Terre attire la Lune, et la Lune attire la Terre. D'après le principe des actions réciproques, ces deux forces ont exactement la <b>même intensité</b>, même si la Terre est 81 fois plus massive que la Lune.</p>

<div class="nt-lab" id="lab-grav">
<p class="nt-tag"><i class="fa-solid fa-magnet"></i>Animation</p>
<p class="nt-lab-title">De quoi dépend l'attraction gravitationnelle&nbsp;?</p>
<canvas role="img" aria-label="Deux boules A et B, de masses réglables en tonnes, séparées d'une distance réglable, avec les deux forces d'attraction, toujours de même longueur."></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Masse de A&nbsp;: <b class="out-ma"></b><input type="range" min="1" max="4" step="1" value="1" data-in="ma"></label>
<label class="nt-ctrl">Masse de B&nbsp;: <b class="out-mb"></b><input type="range" min="1" max="4" step="1" value="1" data-in="mb"></label>
<label class="nt-ctrl">Distance AB&nbsp;: <b class="out-d"></b><input type="range" min="2" max="4" step="0.5" value="2" data-in="d"></label>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Loi de la gravitation universelle</p>
<p>La force d'attraction gravitationnelle exercée par un système A de masse $m_\text{A}$ sur un système B de masse $m_\text{B}$, leurs centres étant séparés d'une distance AB, s'écrit&nbsp;:</p>
<p class="nt-big"><span class="nt-cadre-def">${\color{#FFFFFF}\overrightarrow{F}_{\text{A}\to\text{B}} = {\color{#99F6E4}-}\,G\,\dfrac{m_\text{A} \times m_\text{B}}{\text{AB}^2}\,{\color{#99F6E4}\vec{u}_{\text{AB}}}}$</span></p>
<ul class="nt-facts">
<li>$G = \pu{6,67E-11 N*m2*kg-2}$ est la <span class="imp nt-hole">constante de gravitation universelle</span>&nbsp;;</li>
<li>$m_\text{A}$ et $m_\text{B}$ s'expriment en kg, et la distance AB en m&nbsp;;</li>
<li><span style="color:#0D9488">$\vec{u}_{\text{AB}}$</span> est un vecteur unitaire (de norme 1), de direction (AB), orienté de A vers B. Le signe «&nbsp;<span style="color:#0D9488">$-$</span>&nbsp;» indique que la force subie par B est dirigée vers A&nbsp;: c'est une <b>attraction</b>.</li>
</ul>
</div>

<div class="nt-svgbox"><svg class='nt-svg nt-svg-m' viewBox='0 0 640 140' role='img' aria-label="Les points A et B ; le vecteur unitaire u AB part de A vers B ; la force exercée par A sur B part de B et pointe vers A."><line x1='70' y1='90' x2='560' y2='90' stroke='#94A3B8' stroke-width='1.2' stroke-dasharray='5 5'/><path d='M62,82 L78,98 M78,82 L62,98' stroke='#1E293B' stroke-width='2.4' stroke-linecap='round'/><text x='70' y='122' font-size='18' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>A</text><path d='M552,82 L568,98 M568,82 L552,98' stroke='#1E293B' stroke-width='2.4' stroke-linecap='round'/><text x='560' y='122' font-size='18' text-anchor='middle' fill='#1E293B' font-family='Georgia, "Times New Roman", serif'>B</text><line x1='70.0' y1='90.0' x2='130.4' y2='90.0' stroke='#0D9488' stroke-width='2.6' stroke-linecap='round'/><polygon points='140.0,90.0 128.0,95.5 128.0,84.5' fill='#0D9488'/><text x='106' y='76' font-size='17' text-anchor='middle' fill='#0D9488' font-family='Georgia, "Times New Roman", serif' font-style='italic'>u<tspan font-size='11' dy='5' font-style='normal'>AB</tspan></text><line x1='98.0' y1='59.0' x2='112.0' y2='59.0' stroke='#0D9488' stroke-width='1.2' stroke-linecap='round'/><polygon points='116.0,59.0 111.0,61.4 111.0,56.6' fill='#0D9488'/><line x1='560.0' y1='90.0' x2='401.2' y2='90.0' stroke='#E5484D' stroke-width='3' stroke-linecap='round'/><polygon points='390.0,90.0 404.0,83.5 404.0,96.5' fill='#E5484D'/><text x='460.5' y='76' font-size='17' fill='#B42318' font-family='Georgia, "Times New Roman", serif' font-style='italic'>F<tspan font-size='11' dy='5' font-style='normal'>A→B</tspan></text><line x1='461.0' y1='60.4' x2='470.1' y2='60.4' stroke='#B42318' stroke-width='1.2' stroke-linecap='round'/><polygon points='474.1,60.4 469.1,62.8 469.1,58.0' fill='#B42318'/></svg></div>

<p>Pour calculer l'intensité de la force, on laisse de côté le signe «&nbsp;$-$&nbsp;» et le vecteur unitaire&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$F_{\text{A}\to\text{B}} = G\,\dfrac{m_\text{A} \times m_\text{B}}{\text{AB}^2}$</p>
<div class="nt-f-units"><span>$F_{\text{A}\to\text{B}} = F_{\text{B}\to\text{A}}$&nbsp;: intensité de la force en <b>N</b></span><span>$m_\text{A}$, $m_\text{B}$&nbsp;: masses en <b>kg</b></span><span>AB&nbsp;: distance en <b>m</b></span><span>$G = \pu{6,67E-11}$&nbsp;<b>N·m<sup>2</sup>·kg<sup>−2</sup></b></span></div>
</div>

<p>L'intensité est proportionnelle à chacune des deux masses, et inversement proportionnelle au <b>carré</b> de la distance&nbsp;: si l'on double la distance, la force est divisée par 4.</p>

### Retrouver le poids {.nt-h3}

<p>Appliquons cette loi à un objet de masse $m$ posé à la surface de la Terre, de masse $M_\text{T}$ et de rayon $R_\text{T}$&nbsp;: la distance entre leurs centres vaut $R_\text{T}$.</p>

$$F_{\text{Terre}\to\text{objet}} = G\\,\dfrac{m \times M_\text{T}}{R_\text{T}^2} = m \times {\color{#2563EB}G\\,\dfrac{M_\text{T}}{R_\text{T}^2}} = m \times {\color{#2563EB}g}$$

<p>C'est la formule du poids&nbsp;! Avec $M_\text{T} = \pu{5,97E24 kg}$ et $R_\text{T} = \pu{6,37E6 m}$&nbsp;:</p>

$${\color{#2563EB}g} = \pu{6,67E-11 N * m2 * kg-2} \times \dfrac{\pu{5,97E24 kg}}{\left(\pu{6,37E6 m}\right)^2} \approx {\color{#2563EB}\pu{9,81 N*kg-1}}$$

<p>On retrouve bien l'intensité de la pesanteur terrestre.</p>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>En toute rigueur, le poids et l'attraction gravitationnelle de la Terre diffèrent très légèrement, à cause de la rotation de la Terre, mais on les confond en seconde.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Que vaut l'intensité de la pesanteur $g$ à bord de l'ISS, qui tourne à environ 400&nbsp;km d'altitude&nbsp;?</p>
</div>

<div class="nt-lab" id="lab-alt">
<p class="nt-tag"><i class="fa-solid fa-chart-line"></i>Animation</p>
<p class="nt-lab-title">L'intensité de la pesanteur en fonction de l'altitude</p>
<canvas role="img" aria-label="Courbe de l'intensité de la pesanteur en fonction de l'altitude, avec quelques repères : avion, ISS, satellites GPS, satellites géostationnaires."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Altitude&nbsp;: <b class="out-h"></b><input type="range" min="0" max="1000" step="1" value="0" data-in="h"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Presque autant qu'au sol&nbsp;!</span></summary>
<div class="nt-d-body">
<p>À 400&nbsp;km d'altitude, la distance au centre de la Terre vaut $R_\text{T} + \pu{400 km} = \pu{6,77E6 m}$, d'où $g = G\,\dfrac{M_\text{T}}{(\pu{6,77E6 m})^2} \approx \pu{8,7 N*kg-1}$, soit environ 89&nbsp;% de sa valeur au sol.</p>
<p>Les astronautes ne flottent donc pas parce qu'il n'y aurait «&nbsp;plus de pesanteur&nbsp;»&nbsp;! Ils flottent parce que la station et tout ce qu'elle contient <b>tombent ensemble</b> vers la Terre, en permanence, sous l'effet de leur seul poids&nbsp;: ils sont en <b>chute libre</b> (voir la partie 5.2). La station va si vite horizontalement (environ $\pu{28 000 km*h-1}$) qu'en tombant, elle «&nbsp;rate&nbsp;» sans cesse la Terre et tourne autour.</p>
</div>
</details>

<p>Comment la station peut-elle tomber sans jamais s'écraser&nbsp;? Newton l'avait déjà compris, avec une expérience de pensée&nbsp;: un canon, placé au sommet d'une montagne immense, tire des boulets horizontalement, de plus en plus vite.</p>

<div class="nt-lab" id="lab-canon">
<p class="nt-tag"><i class="fa-solid fa-earth-europe"></i>Animation</p>
<p class="nt-lab-title">Le canon de Newton</p>
<canvas role="img" aria-label="La Terre et un canon au sommet d'une tour de 400 km ; selon la vitesse de tir, le boulet retombe sur Terre ou tourne autour."></canvas>
<div class="nt-btns"><span class="nt-note">Vitesse de tir&nbsp;:</span><button type="button" class="nt-btn" data-v="3">3 km·s⁻¹</button><button type="button" class="nt-btn" data-v="6">6 km·s⁻¹</button><button type="button" class="nt-btn nt-btn-main" data-v="7.67">7,7 km·s⁻¹</button><button type="button" class="nt-btn" data-v="8.5">8,5 km·s⁻¹</button><button type="button" class="nt-btn" data-act="effacer"><i class="fa-solid fa-eraser"></i>&nbsp; Effacer</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### La chute libre {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On parle de <span class="imp nt-hole">chute libre</span> lorsqu'un système n'est soumis qu'à son <span class="imp nt-hole">poids</span>.</p>
</div>

<div class="nt-lab" id="lab-chute">
<p class="nt-tag"><i class="fa-solid fa-feather"></i>Animation</p>
<p class="nt-lab-title">Une boule de bowling et une plume lâchées ensemble</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="ch-air" value="air" checked><span>Dans l'air</span></label><label><input type="radio" name="ch-air" value="vide"><span>Dans le vide</span></label></div></div>
<canvas role="img" aria-label="Une boule de bowling et une plume lâchées ensemble ; chronophotographie de leurs chutes, dans l'air ou dans le vide."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="lacher"><i class="fa-solid fa-play"></i>&nbsp; Lâcher</button><label class="nt-check"><input type="checkbox" data-in="chrono" checked> Chronophotographie</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le mouvement d'un objet en chute libre lâché sans vitesse est <span class="imp nt-hole">accéléré vers le bas</span>, et il <span class="imp nt-hole">ne dépend pas de la masse</span> de l'objet.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">De Galilée à Einstein&nbsp;: la chute libre, mouvement «&nbsp;naturel&nbsp;»</span></summary>
<div class="nt-d-body">
<p>Pendant près de deux mille ans, on a pensé, avec Aristote, que les corps lourds tombaient plus vite que les corps légers. Au début du XVII<sup>e</sup> siècle, <b>Galilée</b> montre qu'il n'en est rien&nbsp;: si l'on pouvait supprimer l'air, tous les corps tomberaient de la même façon. L'astronaute David Scott l'a vérifié sur la Lune en 1971, en lâchant ensemble un marteau et une plume, et l'expérience a été refaite dans une immense chambre à vide de la NASA avec une boule de bowling et des plumes&nbsp;: elles touchent le sol au même instant.</p>
<p>Cette propriété étonnante est au cœur de la relativité générale d'<b>Einstein</b>. Imaginez-vous enfermé dans un ascenseur dont le câble casse&nbsp;: vous, l'ascenseur et tous les objets qu'il contient tombez exactement de la même façon. Un objet lâché reste donc immobile par rapport à vous, comme dans l'ISS. Depuis l'intérieur, rien ne permet de distinguer cette chute libre d'un voyage dans l'espace, loin de toute planète&nbsp;: c'est le <b>principe d'équivalence</b> (Einstein en parlait comme de «&nbsp;l'idée la plus heureuse de sa vie&nbsp;»).</p>
<p>Pour Einstein, la chute libre est donc le mouvement le plus «&nbsp;naturel&nbsp;» qui soit&nbsp;: c'est le référentiel de l'ascenseur qui tombe, ou de l'ISS, qui ressemble le plus à un référentiel galiléen. Celui qui ressent quelque chose de particulier, c'est vous, debout sur le sol, que le sol empêche de tomber&nbsp;!</p>
</div>
</details>

## Force et variation de vitesse {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp nt-hole">vecteur variation de vitesse</span> entre deux instants voisins, où le système passe en M puis en M', est&nbsp;:</p>
<p class="nt-big">${\color{#6D28D9}{\overrightarrow{\Delta v}}} = {\color{#C98A00}{\vec{v}_{\mathrm{M'}}}} - {\color{#C98A00}{\vec{v}_{\mathrm{M}}}}$</p>
</div>

<p>Soustraire $\vec{v}_\mathrm{M}$, c'est ajouter le vecteur opposé. En pratique, on trace les deux vecteurs vitesse <b>à partir du même point</b>&nbsp;: $\overrightarrow{\Delta v}$ est alors la flèche qui va de l'extrémité de $\vec{v}_\mathrm{M}$ à l'extrémité de $\vec{v}_{\mathrm{M'}}$.</p>

<p>D'après la contraposée du principe d'inertie, si $\overrightarrow{\Delta v} \neq \vec{0}$, alors la somme des forces qui s'exercent sur le système n'est pas nulle. On peut aller plus loin&nbsp;:</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La somme des forces qui s'exercent sur un système a la <span class="imp nt-hole">même direction</span> et le <span class="imp nt-hole">même sens</span> que le vecteur variation de vitesse $\overrightarrow{\Delta v}$ entre deux instants voisins.</p>
</div>

<div class="nt-lab" id="lab-dv">
<p class="nt-tag"><i class="fa-solid fa-pen-ruler"></i>Animation pas à pas</p>
<p class="nt-lab-title">Construire le vecteur variation de vitesse</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="dv-m" value="chute" checked><span>Chute libre (balle lancée)</span></label><label><input type="radio" name="dv-m" value="cercle"><span>Mouvement circulaire uniforme</span></label></div></div>
<canvas role="img" aria-label="Chronophotographie avec deux vecteurs vitesse successifs, ramenés au même point, et le vecteur variation de vitesse qui en résulte."></canvas>
<div class="nt-steps-nav"><button type="button" class="nt-btn" data-act="prec"><i class="fa-solid fa-chevron-left"></i>&nbsp; Étape précédente</button><span class="nt-pts" aria-hidden="true"></span><button type="button" class="nt-btn nt-btn-main" data-act="suiv">Étape suivante&nbsp; <i class="fa-solid fa-chevron-right"></i></button></div>
<div class="nt-etape" aria-live="polite"></div>
</div>

<p>En chute libre, $\overrightarrow{\Delta v}$ est vertical et vers le bas, comme le poids, seule force qui s'exerce. Pour le mouvement circulaire uniforme, $\overrightarrow{\Delta v}$ est dirigé vers le centre du cercle&nbsp;: la somme des forces aussi (pour une balle qui tourne au bout d'un fil, c'est le fil qui tire vers le centre).</p>

<div class="nt-lab nt-quizlab" id="quiz-dv">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Du vecteur variation de vitesse à la somme des forces</p>
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
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Vecteurs vitesse et variation de vitesse en Python</span></summary>
<div class="nt-d-body">
<p>Ce programme simule la chute libre d'une balle lancée horizontalement, calcule les vecteurs vitesse et les vecteurs variation de vitesse, puis les trace. Modifiez la vitesse de lancement <code>v0</code> ou la durée <code>dt</code> et relancez&nbsp;: les vecteurs $\overrightarrow{\Delta v}$ restent tous verticaux, vers le bas, et identiques.</p>
{{< runpython lang="pyodide" height="auto" >}}
import matplotlib.pyplot as plt

# Données
g = 9.8      # intensité de la pesanteur (N·kg⁻¹)
v0 = 2.0     # vitesse de lancement horizontale (m·s⁻¹)
dt = 0.05    # durée entre deux positions (s)

# Positions successives de la balle en chute libre
t = [i * dt for i in range(9)]
x = [v0 * ti for ti in t]
y = [-0.5 * g * ti**2 for ti in t]

# Vecteurs vitesse : vx = (x[i+1] - x[i]) / dt, vy = (y[i+1] - y[i]) / dt
vx = [(x[i+1] - x[i]) / dt for i in range(len(t) - 1)]
vy = [(y[i+1] - y[i]) / dt for i in range(len(t) - 1)]

# Tracés
plt.plot(x, y, 'r+')
plt.quiver(x[:-1], y[:-1], vx, vy, color='orange',
           angles='xy', scale_units='xy', scale=10)

# Vecteurs variation de vitesse, tracés au point M(i+1)
for i in range(len(vx) - 1):
    dvx = vx[i+1] - vx[i]
    dvy = vy[i+1] - vy[i]
    plt.quiver(x[i+1], y[i+1], dvx, dvy, color='purple',
               angles='xy', scale_units='xy', scale=2)

plt.axis('equal')
plt.show()
{{< /runpython >}}
</div>
</details>

## Bilan {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-clipboard-check"></i>Je sais…</p>
<ul class="nt-checklist">
<li><label><input type="checkbox"> énoncer le principe d'inertie et sa contraposée, avec les actions ou avec les forces&nbsp;;</label></li>
<li><label><input type="checkbox"> utiliser le principe d'inertie pour déduire la nature du mouvement à partir des forces, ou l'existence de forces non compensées à partir du mouvement&nbsp;;</label></li>
<li><label><input type="checkbox"> expliquer qu'un système soumis seulement à son poids conserve sa vitesse horizontale&nbsp;;</label></li>
<li><label><input type="checkbox"> réaliser le DOI d'un système et modéliser les actions par des forces&nbsp;;</label></li>
<li><label><input type="checkbox"> calculer un poids avec $P = m \times g$, et distinguer masse et poids&nbsp;;</label></li>
<li><label><input type="checkbox"> énoncer le principe des actions réciproques et ne pas confondre forces réciproques et forces qui se compensent&nbsp;;</label></li>
<li><label><input type="checkbox"> utiliser la loi de la gravitation universelle et retrouver l'expression du poids&nbsp;;</label></li>
<li><label><input type="checkbox"> caractériser une chute libre&nbsp;;</label></li>
<li><label><input type="checkbox"> construire le vecteur variation de vitesse et en déduire la direction et le sens de la somme des forces.</label></li>
</ul>
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
        typeset(qEl);
      },
      bilan: function (g) { qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;' + nb + '</span><br>' + (g / nb >= 0.85 ? 'Excellent&nbsp;!' : 'Relisez les explications des questions manquées, puis recommencez&nbsp;: les questions seront mélangées.'); bx.innerHTML = ''; bx.hidden = true; }
    });
    S.start();
  }

  /* =================== décor : intérieur d'un module de la station =================== */
  function module(ctx, x0, y0, w, h) {
    var g = ctx.createLinearGradient(0, y0, 0, y0 + h); g.addColorStop(0, '#CBD5E1'); g.addColorStop(0.5, '#F1F5F9'); g.addColorStop(1, '#CBD5E1');
    ctx.fillStyle = g; rr(ctx, x0, y0, w, h, h * 0.18); ctx.fill();
    ctx.save(); rr(ctx, x0, y0, w, h, h * 0.18); ctx.clip();
    for (var i = 0; i < 8; i++) {   /* baies d'équipements, en haut et en bas */
      var x = x0 + 10 + i * (w - 20) / 8, ww = (w - 20) / 8 - 8;
      ctx.fillStyle = i % 3 === 0 ? '#E2E8F0' : '#D9E0EA'; rr(ctx, x, y0 + 6, ww, h * 0.16, 5); ctx.fill(); rr(ctx, x, y0 + h * 0.84 - 6, ww, h * 0.16, 5); ctx.fill();
      ctx.fillStyle = ['#94A3B8', '#60A5FA', '#FBBF24', '#94A3B8'][i % 4]; ctx.fillRect(x + 6, y0 + 14, ww * 0.3, 4); ctx.fillRect(x + ww * 0.55, y0 + h * 0.84 + 4, ww * 0.25, 4);
    }
    ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(x0 + 20, y0 + h * 0.2); ctx.lineTo(x0 + w - 20, y0 + h * 0.2); ctx.moveTo(x0 + 20, y0 + h * 0.8); ctx.lineTo(x0 + w - 20, y0 + h * 0.8); ctx.stroke();   /* mains courantes */
    ctx.restore(); ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 2; rr(ctx, x0, y0, w, h, h * 0.18); ctx.stroke();
  }
  function astronaute(ctx, x, y, s, ang) {   /* astronaute flottant (dessin original) */
    ctx.save(); ctx.translate(x, y); ctx.rotate(ang || 0); ctx.scale(s, s); ctx.lineCap = 'round';
    ctx.strokeStyle = '#334155'; ctx.lineWidth = 7; ctx.beginPath(); ctx.moveTo(-4, 14); ctx.lineTo(-12, 34); ctx.moveTo(4, 14); ctx.lineTo(14, 32); ctx.moveTo(-8, -6); ctx.lineTo(-24, 4); ctx.moveTo(8, -6); ctx.lineTo(22, -14); ctx.stroke();
    ctx.fillStyle = '#1E3A8A'; rr(ctx, -11, -12, 22, 30, 9); ctx.fill(); ctx.fillStyle = '#60A5FA'; ctx.fillRect(-11, 2, 22, 3);
    ctx.fillStyle = '#FCD9B6'; ctx.beginPath(); ctx.arc(0, -22, 9, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#7C2D12'; ctx.beginPath(); ctx.arc(0, -25, 9, Math.PI, 2 * Math.PI); ctx.fill();
    ctx.restore();
  }
  function objet(ctx, o, x, y, a) {   /* balle, stylo ou boule d'eau */
    ctx.save(); ctx.globalAlpha = a === undefined ? 1 : a;
    if (o.type === 'balle') { var g = ctx.createRadialGradient(x - 3, y - 3, 1, x, y, 9); g.addColorStop(0, '#FDE68A'); g.addColorStop(1, '#EA580C'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, 8, 0, 2 * Math.PI); ctx.fill(); }
    else if (o.type === 'eau') { var g2 = ctx.createRadialGradient(x - 3, y - 3, 1, x, y, 11); g2.addColorStop(0, 'rgba(255,255,255,0.95)'); g2.addColorStop(1, 'rgba(56,189,248,0.75)'); ctx.fillStyle = g2; ctx.beginPath(); ctx.arc(x, y, 10, 0, 2 * Math.PI); ctx.fill(); }
    else { ctx.translate(x, y); ctx.rotate(o.ang || 0); ctx.fillStyle = '#1D4ED8'; rr(ctx, -13, -2.5, 22, 5, 2); ctx.fill(); ctx.fillStyle = '#E5E7EB'; ctx.beginPath(); ctx.moveTo(9, -2.5); ctx.lineTo(14, 0); ctx.lineTo(9, 2.5); ctx.fill(); }
    ctx.restore();
  }

  var ETOILES = []; for (var ie = 0; ie < 140; ie++) { ETOILES.push([(ie * 0.6180339) % 1, (ie * 0.3819660 * 7.13) % 1, 0.4 + (ie % 7) / 9, ie % 11 === 0]); }
  function fondEspace(ctx, W, H) {
      var g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#020617'); g.addColorStop(1, '#0F172A'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      ETOILES.forEach(function (e) { ctx.fillStyle = 'rgba(255,255,255,' + e[2] + ')'; var s = e[3] ? 2.2 : 1.2; ctx.fillRect(e[0] * W, e[1] * H, s, s); });
      var R = W * 1.6, cy = H + R - H * 0.12, ga = ctx.createRadialGradient(W * 0.5, cy, R * 0.98, W * 0.5, cy, R * 1.03);   /* limbe de la Terre */
      ga.addColorStop(0, 'rgba(56,189,248,0.0)'); ga.addColorStop(0.45, 'rgba(56,189,248,0.55)'); ga.addColorStop(1, 'rgba(56,189,248,0)'); ctx.fillStyle = ga; ctx.beginPath(); ctx.arc(W * 0.5, cy, R * 1.03, 0, 2 * Math.PI); ctx.fill();
      var gt = ctx.createLinearGradient(0, H * 0.86, 0, H); gt.addColorStop(0, '#1D4ED8'); gt.addColorStop(1, '#0B3B8C'); ctx.fillStyle = gt; ctx.beginPath(); ctx.arc(W * 0.5, cy, R, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = 'rgba(255,255,255,0.25)'; [[0.2, 0.93, 60], [0.55, 0.95, 90], [0.82, 0.92, 50]].forEach(function (n) { ctx.beginPath(); ctx.ellipse(W * n[0], H * n[1], n[2], 6, 0, 0, 2 * Math.PI); ctx.fill(); });
    }
  function moduleCoupe(ctx, z, W, pan) {   /* module de la station vu en coupe ; pan = 'bords' (panneaux jusqu'aux bords du canevas) ou 'attaches' */
      var e = 9, r = z.h * 0.22;
      [-1, 1].forEach(function (d) {   /* poutre et panneaux solaires de part et d'autre du module */
        var w2 = pan === 'bords' ? Math.max(14, z.x0 - 30) : z.w * 0.09, xs = pan === 'bords' ? (d < 0 ? 6 : W - 6 - w2) : (d < 0 ? z.x0 - e - 14 - w2 : z.x0 + z.w + e + 14), xh = d < 0 ? z.x0 - e : z.x0 + z.w + e, ph = z.h * 0.42, gap = 7;
        ctx.fillStyle = '#94A3B8'; ctx.fillRect(Math.min(xh, xs + w2 / 2), z.cy - 3, Math.abs(xh - (xs + w2 / 2)), 6);
        [z.cy - gap - ph, z.cy + gap].forEach(function (y) {
          var gs = ctx.createLinearGradient(xs, y, xs + w2, y + ph); gs.addColorStop(0, '#92400E'); gs.addColorStop(0.5, '#D97706'); gs.addColorStop(1, '#B45309'); ctx.fillStyle = gs; ctx.fillRect(xs, y, w2, ph);
          ctx.strokeStyle = 'rgba(15,23,42,0.45)'; ctx.lineWidth = 1; for (var c = 1; c < 5; c++) { ctx.beginPath(); ctx.moveTo(xs, y + c * ph / 5); ctx.lineTo(xs + w2, y + c * ph / 5); ctx.stroke(); } ctx.beginPath(); ctx.moveTo(xs + w2 / 2, y); ctx.lineTo(xs + w2 / 2, y + ph); ctx.stroke();
        });
      });
      var gh = ctx.createLinearGradient(0, z.y0 - e, 0, z.y0 + z.h + e); gh.addColorStop(0, '#E2E8F0'); gh.addColorStop(0.5, '#94A3B8'); gh.addColorStop(1, '#64748B');   /* coque */
      ctx.fillStyle = gh; rr(ctx, z.x0 - e, z.y0 - e, z.w + 2 * e, z.h + 2 * e, r + e); ctx.fill();
      ctx.strokeStyle = 'rgba(15,23,42,0.25)'; ctx.lineWidth = 1; for (var b = 1; b < 6; b++) { var xb = z.x0 + b * z.w / 6; ctx.beginPath(); ctx.moveTo(xb, z.y0 - e); ctx.lineTo(xb, z.y0 - 1); ctx.moveTo(xb, z.y0 + z.h + 1); ctx.lineTo(xb, z.y0 + z.h + e); ctx.stroke(); }
      var gi = ctx.createLinearGradient(0, z.y0, 0, z.y0 + z.h); gi.addColorStop(0, '#DCE3EC'); gi.addColorStop(0.5, '#F8FAFC'); gi.addColorStop(1, '#DCE3EC');   /* intérieur */
      ctx.fillStyle = gi; rr(ctx, z.x0, z.y0, z.w, z.h, r); ctx.fill();
      ctx.save(); rr(ctx, z.x0, z.y0, z.w, z.h, r); ctx.clip();
      var n = Math.max(4, Math.round(z.w / 110));
      for (var k = 0; k < n; k++) { var x = z.x0 + 14 + k * (z.w - 28) / n, ww = (z.w - 28) / n - 8;
        ctx.fillStyle = k % 3 ? '#E2E8F0' : '#E8EDF4'; rr(ctx, x, z.y0 + 5, ww, z.h * 0.14, 5); ctx.fill(); rr(ctx, x, z.y0 + z.h * 0.86 - 5, ww, z.h * 0.14, 5); ctx.fill();
        ctx.fillStyle = ['#94A3B8', '#38BDF8', '#FBBF24', '#A3E635'][k % 4]; ctx.fillRect(x + 7, z.y0 + 12, ww * 0.28, 3); ctx.fillRect(x + ww * 0.55, z.y0 + z.h * 0.86 + 4, ww * 0.25, 3);
        ctx.fillStyle = 'rgba(15,23,42,0.08)'; ctx.fillRect(x + ww * 0.15, z.y0 + z.h * 0.86 + 12, ww * 0.6, 2); }
      ctx.strokeStyle = '#A8B3C2'; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.moveTo(z.x0 + 26, z.y0 + z.h * 0.2); ctx.lineTo(z.x0 + z.w - 26, z.y0 + z.h * 0.2); ctx.moveTo(z.x0 + 26, z.y0 + z.h * 0.8); ctx.lineTo(z.x0 + z.w - 26, z.y0 + z.h * 0.8); ctx.stroke();
      var gl = ctx.createRadialGradient(z.cx, z.cy, 10, z.cx, z.cy, z.w * 0.6); gl.addColorStop(0, 'rgba(255,255,255,0.35)'); gl.addColorStop(1, 'rgba(255,255,255,0)'); ctx.fillStyle = gl; ctx.fillRect(z.x0, z.y0, z.w, z.h);
      ctx.restore(); ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.5; rr(ctx, z.x0, z.y0, z.w, z.h, r); ctx.stroke();
    }
  function dessinObjet(ctx, ob, x, y, al) {   /* les objets : balle, stylo, boule d'eau, pomme, petit cube */
      ctx.save(); ctx.globalAlpha = al; ctx.translate(x, y);
      if (ob.type === 'balle') { var g = ctx.createRadialGradient(-3, -3, 1, 0, 0, 8); g.addColorStop(0, '#FEF3C7'); g.addColorStop(1, '#EA580C'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(0, 0, 7.5, 0, 2 * Math.PI); ctx.fill(); }
      else if (ob.type === 'eau') { var g2 = ctx.createRadialGradient(-3, -3, 1, 0, 0, 10); g2.addColorStop(0, 'rgba(255,255,255,0.95)'); g2.addColorStop(1, 'rgba(14,165,233,0.75)'); ctx.fillStyle = g2; ctx.beginPath(); ctx.arc(0, 0, 9, 0, 2 * Math.PI); ctx.fill(); }
      else if (ob.type === 'pomme') { ctx.fillStyle = '#DC2626'; ctx.beginPath(); ctx.arc(-3, 1, 6.5, 0, 2 * Math.PI); ctx.arc(3, 1, 6.5, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#78350F'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(0, -5); ctx.lineTo(1, -9); ctx.stroke(); ctx.fillStyle = '#16A34A'; ctx.beginPath(); ctx.ellipse(4, -8, 3.5, 1.8, -0.4, 0, 2 * Math.PI); ctx.fill(); }
      else if (ob.type === 'cube') { ctx.rotate(ob.ang); ctx.fillStyle = '#7C3AED'; rr(ctx, -6, -6, 12, 12, 2); ctx.fill(); ctx.fillStyle = 'rgba(255,255,255,0.35)'; ctx.fillRect(-6, -6, 12, 3); }
      else { ctx.rotate(ob.ang); ctx.fillStyle = '#1D4ED8'; rr(ctx, -12, -2.2, 20, 4.4, 2); ctx.fill(); ctx.fillStyle = '#E5E7EB'; ctx.beginPath(); ctx.moveTo(8, -2.2); ctx.lineTo(13, 0); ctx.lineTo(8, 2.2); ctx.fill(); }
      ctx.restore();
    }

  /* =================== 1. Objets lâchés dans l'ISS =================== */
  (function () {
    var root = document.getElementById('lab-iss'); if (!root) { return; }
    var chkC = $(root, '[data-in="chrono"]'), chkV = $(root, '[data-in="vec"]'), msg = $(root, '.nt-msg'), bL = $(root, '[data-act="lancer"]');
    var OBJ = [], t = 0, TF = 5, run = false, cnv, DTP = 0.5;
    function geo(o) {   /* intérieur du module (zone où les objets peuvent se déplacer) */
      var mx = Math.max(26, o.W * 0.07), my = o.H * 0.13, w = Math.min(o.W - 2 * mx, o.H * 3.2);   /* largeur plafonnée : le module garde ses proportions sur un très grand écran */
      return { x0: (o.W - w) / 2, y0: my, w: w, h: o.H * 0.6, cx: o.W / 2, cy: my + o.H * 0.3 };
    }
    function tirage() {   /* 5 objets partent du centre : un sans vitesse, les autres avec de petites vitesses aléatoires */
      var z = geo(cnv), types = shuffle(['balle', 'stylo', 'eau', 'pomme', 'cube']), a0 = Math.random() * 2 * Math.PI, L = [];
      types.forEach(function (ty, i) {
        if (i === 0) { L.push({ type: ty, vx: 0, vy: 0, ang: Math.random() * 3, w: 0 }); return; }
        var a = a0 + (i - 1) * Math.PI / 2 + (Math.random() - 0.5) * 0.9, v = 0.35 + Math.random() * 0.65;
        L.push({ type: ty, vx: v * Math.cos(a), vy: v * Math.sin(a), ang: Math.random() * 3, w: (Math.random() - 0.5) * 1.2 });
      });
      L.forEach(function (ob) {   /* chaque vitesse est réglée pour que l'objet n'atteigne pas la paroi avant la fin */
        var m = 18, n = Math.hypot(ob.vx, ob.vy); ob.x = 0; ob.y = 0; ob.rec = [[0, 0]]; if (!n) { return; }
        var tw = Math.min(ob.vx ? (z.w / 2 - m) / Math.abs(ob.vx / n) : 1e9, ob.vy ? (z.h / 2 - m) / Math.abs(ob.vy / n) : 1e9), v = tw / TF * (0.5 + 0.42 * Math.random());
        ob.vx = ob.vx / n * v; ob.vy = ob.vy / n * v;
      });
      return L;
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, z = geo(o); ctx.clearRect(0, 0, W, H); fondEspace(ctx, W, H); moduleCoupe(ctx, z, W, z.x0 > 140 ? 'attaches' : 'bords');
      var mob = OBJ.filter(function (ob) { return ob.vx || ob.vy; }), fix = OBJ.filter(function (ob) { return !ob.vx && !ob.vy; });
      mob.forEach(function (ob) {
        if (chkC.checked) { ob.rec.forEach(function (p) { dessinObjet(ctx, ob, z.cx + p[0], z.cy + p[1], 0.18); croix(ctx, z.cx + p[0], z.cy + p[1], ROUGE, 3.5); }); }
        dessinObjet(ctx, ob, z.cx + ob.x, z.cy + ob.y, 1);
      });
      if (chkV.checked) { mob.forEach(function (ob) { var x = z.cx + ob.x, y = z.cy + ob.y; vec(ctx, x, y, x + ob.vx * 1.4, y + ob.vy * 1.4, ORANGE, 2.4, 10); }); }
      fix.forEach(function (ob) { dessinObjet(ctx, ob, z.cx, z.cy, 1); if (chkC.checked) { croix(ctx, z.cx, z.cy, ROUGE, 3.5); } });   /* l'objet lâché sans vitesse, au premier plan */
      pill(ctx, 'référentiel de la station', 10, 16, { size: 11.5, col: '#E2E8F0', bg: 'rgba(15,23,42,0.6)', align: 'left' });
      if (t > 0) { pill(ctx, 't = ' + fmt(t, 1) + ' s', W - 10, 16, { size: 11.5, col: '#E2E8F0', bg: 'rgba(15,23,42,0.6)', align: 'right' }); }
    }
    function step(dt) {
      if (!run) { return false; } dt = Math.min(dt, 0.05); var t0 = t; t = Math.min(TF, t + dt);
      OBJ.forEach(function (ob) { ob.x += ob.vx * (t - t0); ob.y += ob.vy * (t - t0); ob.ang += ob.w * (t - t0); if (Math.floor(t / DTP + 1e-9) > ob.rec.length - 1) { ob.rec.push([ob.vx * DTP * ob.rec.length, ob.vy * DTP * ob.rec.length]); } });
      if (t >= TF) { run = false; bL.disabled = false; msg.innerHTML = 'Chaque objet a gardé sa vitesse de départ&nbsp;: celui lâché sans vitesse est resté immobile au centre, les autres ont avancé en <b>ligne droite</b>, avec des positions <b>également espacées</b>. Relancez pour un autre tirage.'; }
      draw(cnv); return run;
    }
    var loop = Loop(root, step);
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 280 : 360; }, draw);
    bL.addEventListener('click', function () { OBJ = tirage(); t = 0; msg.textContent = 'Les objets sont lâchés au centre du module, avec de petites vitesses (l\u2019un d\u2019eux sans vitesse)…'; if (RM) { OBJ.forEach(function (ob) { ob.x = ob.vx * TF; ob.y = ob.vy * TF; for (var j = 1; j <= TF / DTP; j++) { ob.rec.push([ob.vx * DTP * j, ob.vy * DTP * j]); } }); t = TF; draw(cnv); return; } run = true; bL.disabled = true; loop.kick(); });
    [chkC, chkV].forEach(function (c) { c.addEventListener('change', function () { draw(cnv); }); });
    OBJ = tirage(); msg.textContent = 'Cinq objets attendent au centre du module. Lâchez-les et observez leurs mouvements.'; draw(cnv);
  })();

  /* =================== 2. Que peut-on conclure ? =================== */
  (function () {
    var root = document.getElementById('quiz-logique'); if (!root) { return; }
    var C = 'Les actions qui s\u2019exercent sur lui se compensent (ou il n\u2019y en a aucune).', N = 'Au moins une action non compensée s\u2019exerce sur lui.';
    Quiz(root, [
      ['Un palet glisse sur la glace, en ligne droite et à vitesse constante. Que peut-on en conclure&nbsp;?', [C, N, 'Aucune action ne s\u2019exerce sur lui.'], 'Son vecteur vitesse est constant&nbsp;: les actions se compensent. Il y en a pourtant&nbsp;: le poids et la réaction de la glace.'],
      ['Une voiture prend un virage à 90&nbsp;km·h⁻¹ constants. Que peut-on en conclure&nbsp;?', [N, C, 'On ne peut rien conclure.'], 'La direction du vecteur vitesse change&nbsp;: il n\u2019est pas constant, même si sa norme l\u2019est.'],
      ['Une pomme tombe d\u2019un arbre, de plus en plus vite. Que peut-on en conclure&nbsp;?', [N, C, 'Aucune action ne s\u2019exerce sur elle.'], 'Sa vitesse augmente&nbsp;: une action n\u2019est pas compensée, celle de la Terre (le poids).'],
      ['Un ascenseur monte à vitesse constante. Que peut-on en conclure&nbsp;?', [C, N, 'Le câble tire plus fort que le poids.'], 'Vecteur vitesse constant&nbsp;: la traction du câble compense exactement le poids.'],
      ['Un cycliste freine en ligne droite. Que peut-on en conclure&nbsp;?', [N, C, 'On ne peut rien conclure.'], 'Sa vitesse diminue&nbsp;: au moins une action n\u2019est pas compensée.'],
      ['La Lune tourne autour de la Terre sur une orbite presque circulaire, à vitesse presque constante. Que peut-on en conclure&nbsp;?', [N, C, 'Aucune action ne s\u2019exerce sur elle.'], 'Son vecteur vitesse change de direction en permanence&nbsp;: une action n\u2019est pas compensée, l\u2019attraction de la Terre.'],
      ['Les actions qui s\u2019exercent sur un ballon immobile se compensent. Que va-t-il se passer&nbsp;?', ['Il reste immobile.', 'Il se met à rouler.', 'On ne peut rien prévoir.'], 'Principe d\u2019inertie&nbsp;: il persévère dans son état de repos.'],
      ['Une sonde spatiale file à $\\pu{17 km*s-1}$, loin de toute étoile et de toute planète, moteurs coupés. Que va-t-il se passer&nbsp;?', ['Elle continue en ligne droite à $\\pu{17 km*s-1}$.', 'Elle ralentit peu à peu jusqu\u2019à s\u2019arrêter.', 'Elle se met à tourner.'], 'Rien n\u2019agit sur elle (ou presque)&nbsp;: son vecteur vitesse reste constant, sans qu\u2019il faille de moteur pour cela.']
    ], 6);
  })();

  /* =================== 3. Une balle lâchée depuis un vélo =================== */
  (function () {
    var root = document.getElementById('lab-velo'); if (!root) { return; }
    var chkI = $(root, '[data-in="inertie"]'), chkT = $(root, '[data-in="traj"]'), chkR = $(root, '[data-in="ralenti"]'), msg = $(root, '.nt-msg');
    var V = 5, G = 9.8, HB = 1.35, ref = 'sol', S, trace, cnv, camSol = 0, NU = [[2, 0.12], [12, 0.22], [24, 0.1]];
    function init() { S = { t: 0, X: 1.5, lache: false, bx: 1.5 + 0.55, by: HB, u: 0, vy: 0, sol: false }; trace = []; camSol = 0; }
    function step(dt) {
      dt = Math.min(dt, 0.04) * (chkR.checked ? 0.2 : 0.7); S.t += dt; S.X += V * dt;
      if (!S.lache) { S.bx = S.X + 0.55; S.by = HB; if (S.bx * cnv.H / 4.2 >= cnv.W / 2) {   /* lâcher automatique au milieu de la scène (vue du sol) */ S.lache = true; S.u = chkI.checked ? V : 0; S.vy = 0; texte(); } }
      if (S.lache) {
        S.bx += S.u * dt; if (!S.sol) { S.vy -= G * dt; S.by += S.vy * dt; if (S.by <= 0.035) { if (!dit && chkI.checked) { dit = true; pred.montrer(); } S.by = 0.035; S.vy = -S.vy * 0.55; S.u *= 0.75; if (Math.abs(S.vy) < 0.6) { S.sol = true; S.vy = 0; } } } else { S.u *= Math.pow(0.3, dt); }
      }
      trace.push([S.bx, S.by, S.X, S.t, S.lache]); if (trace.length > 900) { trace.shift(); }
      draw(cnv); if (dehors(cnv)) { S.fini = true; return false; } return S.t < 30;
    }
    function dehors(o) {   /* le vélo ou la balle est-il sorti du cadre, dans le référentiel affiché ? */
      var k = o.H / 4.2, cam = ref === 'velo' ? S.X - (o.W * 0.42) / k : camSol, xv = (S.X - cam) * k, xb = (S.bx - cam) * k;
      return xv - 0.9 * k > o.W || xv + 0.9 * k < 0 || xb > o.W + 10 || xb < -10;
    }
    function velo(ctx, x, sol, k) {   /* vélo et cycliste vus de profil */
      ctx.save(); ctx.lineCap = 'round'; ctx.lineJoin = 'round'; var r = 0.34 * k, xa = x - 0.5 * k, xb = x + 0.55 * k, yw = sol - r;
      [xa, xb].forEach(function (xx) { ctx.strokeStyle = '#1F2937'; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(xx, yw, r, 0, 2 * Math.PI); ctx.stroke(); ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 1; for (var a = 0; a < 6; a++) { ctx.beginPath(); ctx.moveTo(xx, yw); ctx.lineTo(xx + r * Math.cos(a + S.X), yw + r * Math.sin(a + S.X)); ctx.stroke(); } });
      ctx.strokeStyle = '#DC2626'; ctx.lineWidth = 3.5; ctx.beginPath(); ctx.moveTo(xa, yw); ctx.lineTo(x - 0.05 * k, yw); ctx.lineTo(x - 0.2 * k, sol - 0.85 * k); ctx.lineTo(xa, yw); ctx.moveTo(x - 0.2 * k, sol - 0.85 * k); ctx.lineTo(x + 0.42 * k, sol - 0.85 * k); ctx.lineTo(x - 0.05 * k, yw); ctx.moveTo(x + 0.42 * k, sol - 0.85 * k); ctx.lineTo(xb, yw); ctx.stroke();
      ctx.strokeStyle = '#1E3A8A'; ctx.lineWidth = 5; ctx.beginPath(); ctx.moveTo(x - 0.22 * k, sol - 0.95 * k); ctx.lineTo(x - 0.05 * k, sol - 1.45 * k); ctx.stroke();   /* torse */
      ctx.strokeStyle = '#334155'; ctx.lineWidth = 4.5; var pa = S.X * 3; ctx.beginPath(); ctx.moveTo(x - 0.22 * k, sol - 0.95 * k); ctx.lineTo(x + 0.05 * k, sol - 0.6 * k + 0.08 * k * Math.sin(pa)); ctx.lineTo(x - 0.05 * k + 0.15 * k * Math.cos(pa), yw + 0.12 * k * Math.sin(pa)); ctx.stroke();
      ctx.strokeStyle = '#475569'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(x + 0.42 * k, sol - 0.85 * k); ctx.lineTo(x + 0.47 * k, sol - 1.08 * k); ctx.lineTo(x + 0.36 * k, sol - 1.12 * k); ctx.stroke();   /* potence et guidon */
      ctx.fillStyle = '#111827'; rr(ctx, x + 0.31 * k, sol - 1.15 * k, 0.1 * k, 0.06 * k, 2); ctx.fill();
      ctx.strokeStyle = '#1E3A8A'; ctx.lineWidth = 3.5; ctx.beginPath(); ctx.moveTo(x - 0.05 * k, sol - 1.38 * k); ctx.lineTo(x + 0.18 * k, sol - 1.22 * k); ctx.lineTo(x + 0.35 * k, sol - 1.12 * k); ctx.stroke();   /* bras sur le guidon */
      if (!S.lache) { ctx.beginPath(); ctx.moveTo(x - 0.05 * k, sol - 1.4 * k); ctx.lineTo(x + 0.3 * k, sol - 1.3 * k); ctx.lineTo(x + 0.5 * k, sol - HB * k + 0.05 * k); ctx.stroke(); }   /* bras tendu qui tient la balle */
      ctx.fillStyle = '#FCD9B6'; ctx.beginPath(); ctx.arc(x, sol - 1.58 * k, 0.11 * k, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#F59E0B'; ctx.beginPath(); ctx.arc(x - 0.01 * k, sol - 1.62 * k, 0.12 * k, Math.PI, 2 * Math.PI); ctx.fill();
      ctx.restore();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k = H / 4.2, sol = H - 30, cam = ref === 'velo' ? S.X - (W * 0.42) / k : camSol;
      function sx(x) { return (x - cam) * k; }
      ctx.clearRect(0, 0, W, H); decorCampagne(ctx, W, H, sol, sx, cam, k, NU);
      if (chkT.checked && trace.length > 1) {
        ctx.save(); ctx.strokeStyle = TRAJ; ctx.lineWidth = 2.2; ctx.lineCap = 'round'; ctx.setLineDash([0.1, 6]); ctx.beginPath();
        var deb = true; trace.forEach(function (q) { if (ref === 'velo' && !q[4] && S.t - q[3] > 0.6) { deb = true; return; } var x = ref === 'velo' ? sx(q[0] - q[2] + S.X) : sx(q[0]), y = sol - q[1] * k - 0.07 * k; if (deb) { ctx.moveTo(x, y); deb = false; } else { ctx.lineTo(x, y); } }); ctx.stroke(); ctx.restore();   /* vue du vélo, tant que la balle est tenue, la trace ne persiste que 0,6 s ; vue du sol, on garde toute la trajectoire */
      }
      velo(ctx, sx(S.X), sol, k);
      var bx = sx(S.bx), by = sol - S.by * k - 0.07 * k, gb = ctx.createRadialGradient(bx - 2, by - 2, 1, bx, by, 0.07 * k + 2); gb.addColorStop(0, '#ECFCCB'); gb.addColorStop(1, '#A3E635'); ctx.fillStyle = gb; ctx.beginPath(); ctx.arc(bx, by, 0.07 * k + 2, 0, 2 * Math.PI); ctx.fill();
      if (!S.sol) { var vx = (S.lache ? S.u : V) - (ref === 'velo' ? V : 0), vyb = S.lache ? S.vy : 0, f = 0.09 * k; if (Math.hypot(vx, vyb) > 0.2) { vec(ctx, bx, by, bx + vx * f, by - vyb * f, ORANGE, 2.6, 10); } }   /* vecteur vitesse de la balle, tenue ou lâchée */
      pill(ctx, 'référentiel ' + (ref === 'sol' ? 'terrestre' : 'du vélo'), 10, 16, { size: 12, col: NAVY, align: 'left', stroke: GRID2 });
      if (!chkI.checked) { pill(ctx, 'principe d\u2019inertie désactivé\u00A0!', W - 10, 16, { size: 11.5, col: '#B91C1C', align: 'right', stroke: '#FECACA' }); }
    }
    function texte() {
      if (!S.lache) { msg.textContent = 'Le cycliste roule à vitesse constante (18\u00A0km·h⁻¹) et tient une balle de tennis\u00A0: il la lâchera au milieu de la scène.'; return; }
      if (chkI.checked) { msg.innerHTML = ref === 'sol' ? 'Vue du sol, la balle garde sa vitesse horizontale&nbsp;: elle avance avec le vélo en tombant, et décrit une courbe. Elle tombe au pied du cycliste.' : 'Vue du vélo, la balle tombe <b>verticalement</b>, juste à côté du cycliste&nbsp;: horizontalement, elle avance exactement comme lui.'; }
      else { msg.innerHTML = 'Sans le principe d\u2019inertie, la balle perdrait sa vitesse horizontale dès qu\u2019on la lâche, et retomberait derrière le cycliste. <b>Ce n\u2019est pas ce qu\u2019on observe</b>&nbsp;: essayez avec un vrai vélo… et une vraie balle&nbsp;!'; }
    }
    var loop = Loop(root, step);
    init(); cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 240 : 290; }, draw);
    var pred = Prediction(root, $(root, 'canvas'), 'vue du sol, où la balle va-t-elle toucher le sol&nbsp;?', ['loin derrière le cycliste', 'à côté du cycliste', 'devant le cycliste'], 1, function () { dit = false; pred.cacher(); init(); texte(); draw(cnv); loop.kick(); }), dit = false;
    $(root, '[data-act="reset"]').addEventListener('click', function () { if (pred.choix < 0) { pred.el.querySelector('p').style.color = '#DC2626'; return; } dit = false; pred.cacher(); init(); texte(); draw(cnv); loop.kick(); });
    $$(root, 'input[name="vl-ref"]').forEach(function (r) { r.addEventListener('change', function () { ref = r.value; if (ref === 'sol') { camSol = S.X - 1.5; } texte(); draw(cnv); }); });
    [chkI, chkT].forEach(function (c) { c.addEventListener('change', function () { texte(); draw(cnv); }); });
    texte(); draw(cnv);   /* l'animation démarre après la prédiction */
  })();

  /* =================== 4. Le reboost de la station =================== */
  (function () {
    var root = document.getElementById('lab-boost'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), bB = $(root, '[data-act="boost"]');
    var A = 0.6, TB = 3, L = 14, ref = 'station', S, cnv;   /* accélération (m·s⁻²), durée de poussée (s), longueur intérieure du module (m) */
    function init() { S = { t: 0, tb: -1, X: 0, V: 0, fin: false, obj: [{ type: 'astro', x: 9, y: 0.5, v: 0, ang: -0.3 }, { type: 'balle', x: 5.5, y: 0.3, v: 0 }, { type: 'stylo', x: 12, y: 0.7, v: 0, ang: 0.6 }, { type: 'eau', x: 7.2, y: 0.74, v: 0 }, { type: 'cube', x: 3.6, y: 0.62, v: 0, ang: 0.3 }] }; }
    function step(dt) {
      dt = Math.min(dt, 0.04); S.t += dt; var a = S.tb >= 0 && S.t - S.tb < TB ? A : 0; S.V += a * dt; S.X += S.V * dt;
      S.obj.forEach(function (o) { o.x += o.v * dt; var mur = S.X + (o.type === 'astro' ? 0.9 : 0.35); if (o.x < mur) { o.x = mur; o.v = S.V; } });   /* au contact de la paroi arrière, l'objet est entraîné */
      if (S.tb >= 0 && S.t - S.tb > TB && !S.fin) { S.fin = true; pred.montrer(); msg.innerHTML = 'Moteurs coupés. Dans le référentiel de la station, les objets continuent de dériver vers l\u2019arrière, jusqu\u2019à toucher la paroi, qui les entraîne. Vue des étoiles, ils n\u2019ont pas bougé avant d\u2019être rattrapés par la paroi&nbsp;!'; }
      draw(cnv); return S.tb < 0 || S.t - S.tb < 8;
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k = W / (2.2 * L), w = L * k, h = Math.min(0.32 * w, H * 0.5), x0 = ref === 'station' ? (W - w) / 2 : W * 0.07 + S.X * k, y0 = (H - h) / 2 - H * 0.04;   /* même échelle dans les deux référentiels */
      var z = { x0: x0, y0: y0, w: w, h: h, cx: x0 + w / 2, cy: y0 + h / 2 };
      ctx.clearRect(0, 0, W, H); fondEspace(ctx, W, H);
      if (S.tb >= 0 && S.t - S.tb < TB) {   /* flamme des moteurs, à l'arrière */
        var fl = 0.75 + 0.25 * Math.sin(S.t * 37), lf = w * 0.22 * fl, gf = ctx.createLinearGradient(x0 - 9 - lf, 0, x0 - 9, 0); gf.addColorStop(0, 'rgba(251,191,36,0)'); gf.addColorStop(0.6, 'rgba(251,146,60,0.85)'); gf.addColorStop(1, 'rgba(255,247,237,0.95)');
        ctx.fillStyle = gf; ctx.beginPath(); ctx.moveTo(x0 - 9, z.cy - 7); ctx.quadraticCurveTo(x0 - 9 - lf * 0.6, z.cy - 10, x0 - 9 - lf, z.cy); ctx.quadraticCurveTo(x0 - 9 - lf * 0.6, z.cy + 10, x0 - 9, z.cy + 7); ctx.fill();
      }
      moduleCoupe(ctx, z, W, 'attaches');
      ctx.fillStyle = '#475569'; rr(ctx, x0 - 9 - 12, z.cy - 9, 12, 18, 3); ctx.fill();   /* tuyère */
      S.obj.forEach(function (ob) {
        var x = x0 + (ob.x - S.X) * k, y = y0 + h * (0.18 + 0.64 * ob.y);   /* position dans le module */
        if (ob.type === 'astro') { astronaute(ctx, x, y, Math.max(0.75, h / 150), ob.ang); } else { dessinObjet(ctx, ob, x, y, 1); }
        var vr = ob.v - (ref === 'station' ? S.V : 0); if (Math.abs(vr) > 0.05) { vec(ctx, x, y - 20, x + vr * k * 0.9, y - 20, ORANGE, 2.2, 9); }
      });
      var vs = ref === 'station' ? 0 : S.V; if (vs > 0.05) { vec(ctx, z.cx, y0 - 22, z.cx + vs * k * 0.9, y0 - 22, '#CBD5E1', 2.2, 9); pill(ctx, 'station', z.cx - 8, y0 - 22, { size: 10.5, col: '#E2E8F0', bg: 'rgba(15,23,42,0.6)', align: 'right' }); }
      pill(ctx, ref === 'station' ? 'référentiel de la station' : 'référentiel des étoiles', 10, 16, { size: 11.5, col: '#E2E8F0', bg: 'rgba(15,23,42,0.6)', align: 'left' });
      if (S.tb >= 0 && S.t - S.tb < TB) { pill(ctx, 'moteurs allumés', W - 10, 16, { size: 11.5, col: '#FDE68A', bg: 'rgba(15,23,42,0.6)', align: 'right' }); }
    }
    var loop = Loop(root, step);
    init(); cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 240 : 300; }, draw);
    var pred = Prediction(root, $(root, 'canvas'), 'quand les moteurs s\u2019allument, que font les objets qui flottent, vus depuis la station&nbsp;?', ['ils restent immobiles', 'ils partent vers l\u2019avant', 'ils partent vers l\u2019arrière'], 2, function () { bB.disabled = S.tb >= 0; });
    bB.disabled = true;
    bB.addEventListener('click', function () { if (S.tb >= 0) { return; } S.tb = S.t; bB.disabled = true; msg.innerHTML = ref === 'station' ? 'Les moteurs poussent la station… et dans son référentiel, les objets se mettent à dériver vers l\u2019arrière, sans que rien ne les touche&nbsp;!' : 'Vue des étoiles, la station accélère, et les objets restent immobiles&nbsp;: rien n\u2019agit sur eux.'; loop.kick(); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { init(); pred.cacher(); bB.disabled = pred.choix < 0; msg.textContent = 'L\u2019astronaute et les objets flottent, immobiles dans la station. Allumez les moteurs.'; draw(cnv); });
    $$(root, 'input[name="bs-ref"]').forEach(function (r) { r.addEventListener('change', function () { ref = r.value; draw(cnv); }); });
    msg.textContent = 'L\u2019astronaute et les objets flottent, immobiles dans la station. Allumez les moteurs.'; draw(cnv);
  })();

  function nomForce(ctx, idx, x, y, col, al) {   /* F avec indice et flèche au-dessus */
    ctx.save(); ctx.fillStyle = col; ctx.textBaseline = 'alphabetic'; ctx.font = 'italic 16px Georgia, "Times New Roman", serif';
    var w1 = ctx.measureText('F').width; ctx.font = '10.5px ' + FONT; var w2 = ctx.measureText(idx).width, wt = w1 + w2 + 1, x0 = al === 'right' ? x - wt : (al === 'left' ? x : x - wt / 2);
    ctx.font = 'italic 16px Georgia, "Times New Roman", serif'; ctx.textAlign = 'left'; ctx.fillText('F', x0, y); ctx.font = '10.5px ' + FONT; ctx.fillText(idx, x0 + w1 + 1, y + 4); ctx.restore();
    vec(ctx, x0, y - 15, x0 + w1 + 4, y - 15, col, 1.1, 4.5);
  }
  function sci(x, d) {   /* écriture scientifique : 5,0 × 10⁻²⁴ */
    if (x === 0) { return '0'; } var e = Math.floor(Math.log10(Math.abs(x))), m = x / Math.pow(10, e); if (Math.abs(m) >= 9.995) { m /= 10; e += 1; }
    if (e >= -2 && e <= 3) { return fmt(x, Math.max(0, 2 - e)); }
    var sup = String(e).replace('-', '\u207B').replace(/\d/g, function (c) { return '\u2070\u00B9\u00B2\u00B3\u2074\u2075\u2076\u2077\u2078\u2079'[+c]; });
    return fmt(m, d === undefined ? 1 : d) + '\u00A0×\u00A010' + sup;
  }

  /* =================== 5. Du DOI aux forces =================== */
  function terreIcone(ctx, x, y, r) {   /* la Terre vue de l'espace : océans, continents, nuages, atmosphère */
    var ga = ctx.createRadialGradient(x, y, r * 0.95, x, y, r * 1.18); ga.addColorStop(0, 'rgba(125,211,252,0.55)'); ga.addColorStop(1, 'rgba(125,211,252,0)'); ctx.fillStyle = ga; ctx.beginPath(); ctx.arc(x, y, r * 1.18, 0, 2 * Math.PI); ctx.fill();
    var go = ctx.createRadialGradient(x - r * 0.35, y - r * 0.35, r * 0.1, x, y, r); go.addColorStop(0, '#60A5FA'); go.addColorStop(0.7, '#1D4ED8'); go.addColorStop(1, '#1E3A8A');
    ctx.save(); ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.fillStyle = go; ctx.fill(); ctx.clip();
    ctx.fillStyle = '#22A355';
    ctx.beginPath(); ctx.moveTo(x - 0.15 * r, y - 0.85 * r); ctx.bezierCurveTo(x + 0.25 * r, y - 0.8 * r, x + 0.35 * r, y - 0.45 * r, x + 0.1 * r, y - 0.3 * r); ctx.bezierCurveTo(x + 0.35 * r, y - 0.1 * r, x + 0.3 * r, y + 0.35 * r, x + 0.05 * r, y + 0.7 * r); ctx.bezierCurveTo(x - 0.1 * r, y + 0.4 * r, x - 0.25 * r, y + 0.1 * r, x - 0.2 * r, y - 0.2 * r); ctx.bezierCurveTo(x - 0.45 * r, y - 0.3 * r, x - 0.45 * r, y - 0.7 * r, x - 0.15 * r, y - 0.85 * r); ctx.fill();   /* Europe et Afrique, très stylisées */
    ctx.beginPath(); ctx.ellipse(x + 0.62 * r, y - 0.45 * r, 0.3 * r, 0.2 * r, 0.3, 0, 2 * Math.PI); ctx.fill();
    ctx.fillStyle = '#A3825A'; ctx.beginPath(); ctx.ellipse(x + 0.08 * r, y - 0.05 * r, 0.14 * r, 0.1 * r, 0.4, 0, 2 * Math.PI); ctx.fill();   /* Sahara */
    ctx.strokeStyle = 'rgba(255,255,255,0.75)'; ctx.lineWidth = Math.max(1.5, r * 0.07); ctx.lineCap = 'round';
    [[-0.6, 0.35, 0.35], [0.4, 0.55, 0.3], [-0.3, -0.55, 0.25]].forEach(function (n) { ctx.beginPath(); ctx.arc(x + n[0] * r, y + n[1] * r, n[2] * r, Math.PI * 1.1, Math.PI * 1.75); ctx.stroke(); });   /* nuages */
    var gs = ctx.createRadialGradient(x - r * 0.45, y - r * 0.45, 0, x - r * 0.45, y - r * 0.45, r * 1.5); gs.addColorStop(0, 'rgba(255,255,255,0.25)'); gs.addColorStop(0.5, 'rgba(255,255,255,0)'); gs.addColorStop(1, 'rgba(15,23,42,0.35)'); ctx.fillStyle = gs; ctx.fillRect(x - r, y - r, 2 * r, 2 * r);
    ctx.restore();
  }
  function airIcone(ctx, x, y, r) {   /* l'air : un morceau de ciel, avec des filets de vent et un petit nuage */
    var g = ctx.createLinearGradient(0, y - r, 0, y + r); g.addColorStop(0, '#7DD3FC'); g.addColorStop(1, '#E0F2FE');
    ctx.save(); ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.fillStyle = g; ctx.fill(); ctx.clip();
    ctx.fillStyle = '#FFFFFF'; ctx.beginPath(); ctx.ellipse(x + 0.35 * r, y - 0.45 * r, 0.32 * r, 0.14 * r, 0, 0, 2 * Math.PI); ctx.ellipse(x + 0.2 * r, y - 0.55 * r, 0.18 * r, 0.14 * r, 0, 0, 2 * Math.PI); ctx.fill();
    ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = Math.max(2, r * 0.09); ctx.lineCap = 'round';
    [[-0.05, 0.75], [0.25, 0.6], [0.5, 0.45]].forEach(function (q) { var yy = y + q[0] * r; ctx.beginPath(); ctx.moveTo(x - q[1] * r, yy); ctx.bezierCurveTo(x - 0.2 * r, yy - 0.18 * r, x + 0.2 * r, yy + 0.12 * r, x + q[1] * r * 0.8, yy - 0.05 * r); ctx.stroke(); });
    ctx.beginPath(); ctx.arc(x + 0.55 * r, y - 0.05 * r - 0.12 * r, 0.12 * r, Math.PI * 0.5, Math.PI * 2.1); ctx.stroke();
    ctx.restore(); ctx.strokeStyle = '#38BDF8'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.stroke();
  }
  function solIcone(ctx, x, y, r) {
    ctx.save(); ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.clip();
    var g = ctx.createLinearGradient(0, y - r, 0, y + r); g.addColorStop(0, '#E0F2FE'); g.addColorStop(0.5, '#E0F2FE'); g.addColorStop(0.5, '#86EFAC'); g.addColorStop(0.58, '#22C55E'); g.addColorStop(0.58, '#A16207'); g.addColorStop(1, '#713F12'); ctx.fillStyle = g; ctx.fillRect(x - r, y - r, 2 * r, 2 * r);
    ctx.restore(); ctx.strokeStyle = '#16A34A'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.stroke();
  }
  function filIcone(ctx, x, y, r) {
    ctx.fillStyle = '#F1F5F9'; ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.5; ctx.stroke();
    ctx.fillStyle = '#64748B'; ctx.fillRect(x - 0.55 * r, y - 0.7 * r, 1.1 * r, 0.12 * r);
    ctx.strokeStyle = '#B45309'; ctx.lineWidth = Math.max(2, r * 0.08); ctx.beginPath(); ctx.moveTo(x, y - 0.6 * r); ctx.lineTo(x + 0.15 * r, y + 0.45 * r); ctx.stroke();
    ctx.fillStyle = '#FBBF24'; ctx.beginPath(); ctx.arc(x + 0.17 * r, y + 0.55 * r, 0.14 * r, 0, 2 * Math.PI); ctx.fill();
  }
  function doubleFleche(ctx, x1, y1, x2, y2, col, w, dist) {   /* double flèche, en trait plein (contact) ou en pointillés (à distance) */
    var d = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / d, uy = (y2 - y1) / d, L = Math.min(15, d * 0.16), Wd = L / 2;
    ctx.save(); ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = w; ctx.lineCap = 'round'; if (dist) { ctx.setLineDash([2, 9]); }
    ctx.beginPath(); ctx.moveTo(x1 + ux * L, y1 + uy * L); ctx.lineTo(x2 - ux * L, y2 - uy * L); ctx.stroke(); ctx.setLineDash([]);
    [[x1, y1, 1], [x2, y2, -1]].forEach(function (p) { var s = p[2]; ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(p[0] + s * (ux * L) - uy * Wd, p[1] + s * (uy * L) + ux * Wd); ctx.lineTo(p[0] + s * (ux * L) + uy * Wd, p[1] + s * (uy * L) - ux * Wd); ctx.closePath(); ctx.fill(); });
    ctx.restore();
  }
  (function () {
    var root = document.getElementById('lab-doi'); if (!root) { return; }
    var chips = $(root, '.nt-chips'), piege = $(root, '.nt-piege'), types = $(root, '.nt-types'), q = $(root, '.nt-doi-q'), m1 = $(root, '.nt-msg-doi'), m2 = $(root, '.nt-msg-f'), zf = $(root, '.nt-forces'), bV = $(root, '[data-act="valider"]'), bD = $(root, '[data-act="decomp"]');
    var ICO = { terre: [terreIcone, 'la Terre'], air: [airIcone, 'l\u2019air'], sol: [solIcone, 'le sol'], fil: [filIcone, 'le fil'] };
    var EX = {
      para: { sys: ['parachutiste', '+ parachute'], q: 'Système&nbsp;: le parachutiste et son parachute, qui descendent à vitesse constante. Quels objets agissent sur lui&nbsp;?',
        c: [['terre', 1, 'd'], ['air', 1, 'c'], ['avion', 0, 'L\u2019avion n\u2019est plus en contact avec lui.'], ['sol', 0, 'Il n\u2019a pas encore atteint le sol.'], ['soleil', 0, 'L\u2019attraction du Soleil est négligeable devant celle de la Terre.']],
        F: [['air', 0, -1.0, 'air\u2192système', 'frottements de l\u2019air'], ['terre', 0, 1.0, 'Terre\u2192système', 'poids']], bilan: 'Les deux forces ont la même intensité et des sens opposés&nbsp;: elles se compensent, leur somme est nulle. C\u2019est cohérent avec le principe d\u2019inertie&nbsp;: le parachutiste descend en ligne droite, à vitesse constante.' },
      seau: { sys: ['seau de', 'peinture'], q: 'Système&nbsp;: un seau de peinture posé sur le sol. Quels objets agissent sur lui&nbsp;?',
        c: [['terre', 1, 'd'], ['sol', 1, 'c'], ['main', 0, 'La main qui l\u2019a posé ne le touche plus.'], ['peinture', 0, 'La peinture fait partie du système.'], ['mur', 0, 'Le seau ne touche pas le mur.']],
        F: [['sol', 0, -0.9, 'sol\u2192système', 'réaction du support'], ['terre', 0, 0.9, 'Terre\u2192système', 'poids']], bilan: 'La réaction du sol compense exactement le poids&nbsp;: la somme des forces est nulle, et le seau reste immobile, comme le prévoit le principe d\u2019inertie.' },
      balle: { sys: ['balle'], q: 'Système&nbsp;: une balle accrochée à un fil, qui se balance. Quels objets agissent sur elle&nbsp;?',
        c: [['terre', 1, 'd'], ['fil', 1, 'c'], ['air', 1, 'c'], ['plafond', 0, 'Le plafond ne touche pas la balle&nbsp;: il agit sur le fil, qui agit sur la balle.'], ['main', 0, 'Plus personne ne tient la balle.']],
        F: [['fil', 0.55, -0.95, 'fil\u2192système', 'tension du fil'], ['air', -0.32, -0.12, 'air\u2192système', 'frottements'], ['terre', 0, 0.85, 'Terre\u2192système', 'poids']], bilan: 'Les forces ne se compensent pas&nbsp;: leur somme, en rouge vif, n\u2019est pas nulle. Le vecteur vitesse de la balle change donc sans cesse (sa direction comme sa norme), et c\u2019est bien ce qu\u2019on observe.' },
      moto: { sys: ['moto', '+ pilote'], q: 'Système&nbsp;: une moto et son pilote, qui accélèrent sur une route horizontale. Quels objets agissent sur le système&nbsp;?',
        c: [['terre', 1, 'd'], ['sol', 1, 'c'], ['air', 1, 'c'], ['moteur', 0, 'Le moteur fait partie du système&nbsp;: il ne peut pas le pousser tout seul&nbsp;! C\u2019est le sol, poussé vers l\u2019arrière par la roue, qui pousse la moto vers l\u2019avant.'], ['pilote', 0, 'Le pilote fait partie du système.']],
        F: [['sol', 0.75, -0.9, 'sol\u2192système', ''], ['air', -0.45, 0, 'air\u2192système', 'frottements'], ['terre', 0, 0.9, 'Terre\u2192système', 'poids']], bilan: 'Les forces ne se compensent pas&nbsp;: leur somme, en rouge vif, est dirigée vers l\u2019avant, et la moto accélère vers l\u2019avant.' }
    };
    EX.ballon = { sys: ['ballon'], q: 'Système&nbsp;: un ballon de basket qui vient de quitter les mains du joueur, et qui monte vers le panier. Quels objets agissent sur lui&nbsp;?',
      c: [['terre', 1, 'd'], ['air', 1, 'c'], ['mainj', 0, 'Le ballon a quitté la main&nbsp;: elle ne le touche plus, et n\u2019agit donc plus sur lui. Il n\u2019existe pas de «&nbsp;force du lancer&nbsp;» qui accompagnerait le ballon&nbsp;!'], ['panier', 0, 'Le ballon ne touche pas (encore) le panier.'], ['sol', 0, 'Le ballon ne touche pas le sol.']],
      F: [['air', -0.28, 0.2, 'air\u2192système', 'frottements'], ['terre', 0, 1.0, 'Terre\u2192système', 'poids']], vit: [0.75, -0.6],
      bilan: 'La somme des forces (en rouge vif) est dirigée vers le bas, un peu vers l\u2019arrière, alors que le ballon <b>monte et avance</b> (vitesse en orange)&nbsp;: une force n\u2019est pas forcément dans le sens du mouvement&nbsp;! Le ballon continue d\u2019avancer par inertie, tandis que la somme des forces modifie peu à peu son vecteur vitesse&nbsp;: il ralentit en montant, puis redescend.' };
    var NOMS = { terre: 'la Terre', air: 'l\u2019air', sol: 'le sol', fil: 'le fil', avion: 'l\u2019avion', soleil: 'le Soleil', main: 'une main', peinture: 'la peinture', mur: 'le mur', plafond: 'le plafond', moteur: 'le moteur', pilote: 'le pilote', panier: 'le panier', mainj: 'la main du joueur' };
    var PIEGES = {para: ['avion', 'L\u2019avion a largué le parachutiste&nbsp;: il ne le touche plus. Une action de contact cesse dès que le contact est rompu, même si l\u2019avion «&nbsp;a donné de la vitesse&nbsp;» au parachutiste au départ.'], seau: ['peinture', 'La peinture fait partie du système. Les actions d\u2019une partie du système sur une autre partie sont des <b>actions intérieures</b>&nbsp;: elles ne peuvent pas modifier le mouvement du système dans son ensemble, et n\u2019entrent donc <b>jamais</b> dans le bilan des forces. Seuls comptent les objets <b>extérieurs</b> au système.'], balle: ['plafond', 'Le plafond ne touche pas la balle&nbsp;: il agit sur le fil, et c\u2019est le fil qui agit sur la balle. On ne retient que les objets qui touchent le système (ou qui agissent à distance, comme la Terre).'], moto: ['moteur', 'Le moteur fait partie du système&nbsp;: c\u2019est une <b>action intérieure</b>, qui n\u2019entre pas dans le bilan des forces. Le moteur fait tourner la roue, qui pousse le sol vers l\u2019arrière&nbsp;; c\u2019est le <b>sol</b> qui, en retour, pousse la moto vers l\u2019avant.'], ballon: ['mainj', 'La main n\u2019agit sur le ballon que tant qu\u2019elle le <b>touche</b>&nbsp;: c\u2019est une action de contact, qui cesse à l\u2019instant où le ballon quitte la main. Le ballon n\u2019emporte avec lui aucune «&nbsp;force du lancer&nbsp;»&nbsp;: s\u2019il continue d\u2019avancer, c\u2019est <b>par inertie</b>.']};
    var ex = 'para', etape = 0, decomp = false, cD, cF, anim = false, tA = 0, bA = $(root, '[data-act="anim"]'), TH0 = 0.7, PER = 2.6;
    function charge() {
      var E = EX[ex]; etape = 0; decomp = false; anim = false; bA.hidden = true; piege.hidden = true; q.innerHTML = E.q; chips.innerHTML = ''; types.hidden = true; types.innerHTML = ''; bD.hidden = true; bV.hidden = false; zf.hidden = true;
      shuffle(E.c.slice()).forEach(function (c) { var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-chip'; b.textContent = NOMS[c[0]]; b.setAttribute('aria-pressed', 'false'); b.setAttribute('data-k', c[0]); b.addEventListener('click', function () { if (etape) { return; } b.setAttribute('aria-pressed', String(b.getAttribute('aria-pressed') !== 'true')); }); chips.appendChild(b); });
      m1.textContent = 'Sélectionnez les objets qui agissent sur le système, puis validez.'; m2.innerHTML = ''; drawD(cD);
    }
    function valider() {
      var E = EX[ex];
      if (etape === 0) {
        var faux = [], manque = [];
        $$(chips, '.nt-chip').forEach(function (b) { var c = E.c.filter(function (x) { return x[0] === b.getAttribute('data-k'); })[0], on = b.getAttribute('aria-pressed') === 'true';
          b.classList.toggle('ok', !!c[1]); b.classList.toggle('ko', !c[1] && on); if (on && !c[1] && c[0] !== PIEGES[ex][0]) { faux.push(c[2]); } if (!on && c[1]) { manque.push(NOMS[c[0]]); } });
        m1.innerHTML = (faux.length || manque.length ? '' : '<b>Bien vu&nbsp;!</b> ') + (manque.length ? 'Il manquait&nbsp;: ' + manque.join(', ') + '. ' : '') + faux.join(' ') + ' Pour chaque objet retenu (en vert), indiquez maintenant le type d\u2019action.';
        var pg = PIEGES[ex], tombe = $(chips, '.nt-chip[data-k="' + pg[0] + '"]').getAttribute('aria-pressed') === 'true';   /* l'erreur classique, mise en avant, que l'élève y soit tombé ou non */
        piege.className = 'nt-piege nt-b ' + (tombe ? 'nt-warn' : 'nt-demo-box'); piege.innerHTML = '<p class="nt-tag"><i class="fa-solid fa-' + (tombe ? 'triangle-exclamation' : 'shield-halved') + '"></i>' + (tombe ? 'Erreur classique&nbsp;: «&nbsp;' + NOMS[pg[0]] + '&nbsp;»' : 'Piège évité&nbsp;: «&nbsp;' + NOMS[pg[0]] + '&nbsp;»') + '</p><p>' + pg[1] + '</p>'; piege.hidden = false;
        etape = 1; types.hidden = false;
        E.c.filter(function (c) { return c[1]; }).forEach(function (c) { var d = document.createElement('div'); d.className = 'nt-ty'; d.innerHTML = '<b>' + NOMS[c[0]] + '</b><div class="nt-seg" role="radiogroup"><label><input type="radio" name="ty-' + c[0] + '" value="c"><span><i class="fa-solid fa-hand"></i>&nbsp; contact</span></label><label><input type="radio" name="ty-' + c[0] + '" value="d"><span><i class="fa-solid fa-tower-broadcast"></i>&nbsp; à distance</span></label></div>'; types.appendChild(d); });
        drawD(cD); return;
      }
      var err = [];
      E.c.filter(function (c) { return c[1]; }).forEach(function (c, i) { var r = $(types, 'input[name="ty-' + c[0] + '"]:checked'), ok = r && r.value === c[2]; if (!ok) { err.push(NOMS[c[0]] + '&nbsp;: action ' + (c[2] === 'c' ? 'de contact' : 'à distance')); } types.children[i].classList.add(ok ? 'ok' : 'ko'); $$(types, 'input[name="ty-' + c[0] + '"]').forEach(function (x) { x.checked = x.value === c[2]; x.disabled = true; }); });
      etape = 2; bV.hidden = true; bD.hidden = ex !== 'moto'; bA.hidden = ex !== 'balle'; bA.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Animer le mouvement de la balle'; zf.hidden = false; cF.size();
      m1.innerHTML = (err.length ? 'Correction&nbsp;: ' + err.join('&nbsp;; ') + '. ' : '<b>Exact&nbsp;!</b> ') + 'Voici le DOI complet&nbsp;: double flèche en trait plein pour une action de contact, en pointillés pour une action à distance.';
      m2.innerHTML = 'On modélise maintenant le système par un point matériel, et chaque action par une force. ' + E.bilan;
      drawD(cD); drawF(cF);
    }
    function drawD(o) {
      var ctx = o.ctx, W = o.W, H = o.H, E = EX[ex], cx = W / 2, cy = H / 2, ri = Math.min(34, W * 0.065), R = Math.min((W / 2 - ri - 10) / 1.15, H * 0.42), rs = Math.min(46, R * 0.36, W * 0.09);
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#F8FAFC'; ctx.fillRect(0, 0, W, H);
      var ok = E.c.filter(function (c) { return c[1]; });
      if (etape >= 1) {
        var P = ok.length === 2 ? [[-1, -0.1], [1, -0.1]] : [[-1, 0], [1, -0.55], [1, 0.55]], Rx = Math.min(W / 2 - ri - 14, R * 2.4);   /* jamais d'objet juste sous le système : il serait trop près */
        ok.forEach(function (c, i) {
          var x = cx + P[i][0] * Rx, y = cy + P[i][1] * R, d = Math.hypot(x - cx, y - cy), ux = (x - cx) / d, uy = (y - cy) / d;
          doubleFleche(ctx, cx + ux * (rs + 6), cy + uy * (rs + 6), x - ux * (ri + 6), y - uy * (ri + 6), etape >= 2 ? '#F97360' : '#CBD5E1', 4, etape >= 2 && c[2] === 'd');
          ICO[c[0]][0](ctx, x, y, ri); txt(ctx, ICO[c[0]][1], x, y + ri + 13, { size: 12, col: NAVY });
        });
      }
      var gs = ctx.createRadialGradient(cx, cy, 2, cx, cy, rs); gs.addColorStop(0, '#FFFFFF'); gs.addColorStop(1, '#FBCFE8'); ctx.fillStyle = gs; ctx.beginPath(); ctx.arc(cx, cy, rs, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#EC4899'; ctx.lineWidth = 3; ctx.stroke();
      var fs = Math.min(12, rs * 0.25); E.sys.forEach(function (l, i) { txt(ctx, l, cx, cy + (i - (E.sys.length - 1) / 2) * fs * 1.3, { size: fs, col: '#9D174D' }); });
      if (etape >= 2) { ctx.save(); ctx.lineWidth = 2; ctx.lineCap = 'round'; ctx.strokeStyle = '#F97360'; ctx.beginPath(); ctx.moveTo(14, H - 30); ctx.lineTo(44, H - 30); ctx.stroke(); ctx.setLineDash([2, 6]); ctx.beginPath(); ctx.moveTo(14, H - 12); ctx.lineTo(44, H - 12); ctx.stroke(); ctx.restore(); txt(ctx, 'contact', 50, H - 30, { size: 10.5, col: SLATE, align: 'left' }); txt(ctx, 'à distance', 50, H - 12, { size: 10.5, col: SLATE, align: 'left' }); }
    }
    function pendule(o) {   /* balle au bout d'un fil : forces à chaque instant du balancement (en unités de mg) */
      var ctx = o.ctx, W = o.W, H = o.H, Lp = H * 0.5, ox = W / 2, oy = 26, w = 2 * Math.PI / PER, th = TH0 * Math.cos(w * tA), dth = -TH0 * w * Math.sin(w * tA);
      var bx = ox + Lp * Math.sin(th), by = oy + Lp * Math.cos(th), Lf = Math.min(H * 0.22, 70);
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#F8FAFC'; ctx.fillRect(0, 0, W, H);
      ctx.fillStyle = '#64748B'; ctx.fillRect(ox - 50, oy - 10, 100, 8);
      ctx.save(); ctx.strokeStyle = 'rgba(59,130,246,0.45)'; ctx.setLineDash([4, 5]); ctx.beginPath(); ctx.arc(ox, oy, Lp, Math.PI / 2 - TH0, Math.PI / 2 + TH0); ctx.stroke(); ctx.restore();
      ctx.strokeStyle = '#B45309'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(bx, by); ctx.stroke();
      var g = ctx.createRadialGradient(bx - 4, by - 4, 1, bx, by, 11); g.addColorStop(0, '#FEF3C7'); g.addColorStop(1, '#F59E0B'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(bx, by, 10, 0, 2 * Math.PI); ctx.fill();
      var T = 3 * Math.cos(th) - 2 * Math.cos(TH0), tx = -Math.sin(th), ty = -Math.cos(th), et = [Math.cos(th), -Math.sin(th)], ka = 0.12 / (TH0 * w), Fa = [-ka * dth * et[0], -ka * dth * et[1]];   /* tension, et frottements de l'air opposés à la vitesse */
      var F = [[0, 1, 'Terre\u2192système'], [T * tx, T * ty, 'fil\u2192système'], [Fa[0], Fa[1], 'air\u2192système']], sx = 0, sy = 0;
      F.forEach(function (f, i) { sx += f[0]; sy += f[1]; if (Math.hypot(f[0], f[1]) > 0.02) { vec(ctx, bx, by, bx + f[0] * Lf, by + f[1] * Lf, FORCE, 2.4, 11); if (i < 2) { nomForce(ctx, f[2], bx + f[0] * Lf + (i === 0 ? 8 : -8), by + f[1] * Lf + (i === 0 ? 12 : -4), FORCE_T, i === 0 ? 'left' : 'right'); } } });
      var ns = Math.hypot(sx, sy); vec(ctx, bx, by, bx + sx * Lf, by + sy * Lf, '#FF1414', 4, 13); if (ns > 0.05) { pill(ctx, 'somme des forces', bx + sx * Lf + sx / ns * 14, by + sy * Lf + sy / ns * 14, { size: 10.5, col: '#B91C1C', stroke: '#FECACA', align: sx >= 0 ? 'left' : 'right' }); }
      var vx = Lp * dth * et[0], vy = Lp * dth * et[1]; if (Math.hypot(vx, vy) > 4) { vec(ctx, bx, by, bx + vx * 0.3, by + vy * 0.3, ORANGE, 2.2, 9); }
      pill(ctx, 'en orange : vitesse de la balle', 10, H - 14, { size: 10.5, col: ORANGE_T, align: 'left', stroke: '#FDE68A' });
    }
    function drawF(o) {
      if (ex === 'balle' && anim) { pendule(o); return; }
      var ctx = o.ctx, W = o.W, H = o.H, E = EX[ex], fx = W / 2, fy = H / 2, L = Math.min(H * 0.38, W * 0.26, 130), ex0 = 0.1, ey0 = 0.1, sx0 = 0, sy0 = 0;
      E.F.forEach(function (f) { sx0 += f[1]; sy0 += f[2]; ex0 = Math.max(ex0, Math.abs(f[1])); ey0 = Math.max(ey0, Math.abs(f[2])); }); ex0 = Math.max(ex0, Math.abs(sx0), E.vit ? Math.abs(E.vit[0]) : 0); ey0 = Math.max(ey0, Math.abs(sy0), E.vit ? Math.abs(E.vit[1]) : 0);
      L = Math.min(L, (H / 2 - 36) / ey0, (W / 2 - 110) / ex0);   /* toutes les flèches, et leurs étiquettes, restent dans le cadre */
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#F8FAFC'; ctx.fillRect(0, 0, W, H);
      var sx = 0, sy = 0;
      E.F.forEach(function (f) {
        sx += f[1]; sy += f[2]; var x2 = fx + f[1] * L, y2 = fy + f[2] * L;
        if (ex === 'moto' && f[0] === 'sol' && decomp) { ctx.save(); ctx.globalAlpha = 0.3; vec(ctx, fx, fy, x2, y2, FORCE, 2.6, 12); ctx.restore(); ctx.save(); ctx.setLineDash([5, 4]); vec(ctx, fx, fy, x2, fy, FORCE, 2.2, 11); vec(ctx, fx, fy, fx, y2, FORCE, 2.2, 11); ctx.restore(); txt(ctx, 'force de propulsion', (fx + x2) / 2 + 34, fy - 10, { size: 10.5, col: FORCE_T }); txt(ctx, 'réaction du support', fx - 8, y2 + 14, { size: 10.5, col: FORCE_T, align: 'right' }); }
        else { vec(ctx, fx, fy, x2, y2, FORCE, 2.6, 12); }
        var al = f[1] < -0.1 ? 'right' : 'left', lx = x2 + (f[1] < -0.1 ? -8 : 8), ly = y2 + (f[2] > 0.1 ? 14 : -4);
        if (al === 'left' && lx > W - 95) { al = 'right'; lx = x2 - 10; }   /* étiquette ramenée à l'intérieur du cadre */
        nomForce(ctx, f[3], lx, ly, FORCE_T, al); if (f[4]) { txt(ctx, '(' + f[4] + ')', lx, ly + 15, { size: 10, col: FORCE_T, align: al }); }
      });
      if (Math.hypot(sx, sy) > 0.02) { var ns = Math.hypot(sx, sy), tx = fx + sx * L, ty = fy + sy * L; vec(ctx, fx, fy, tx, ty, '#FF1414', 4, 14); if (Math.abs(sy / ns) < 0.5) { pill(ctx, 'somme des forces', tx, ty + 18, { size: 11, col: '#B91C1C', stroke: '#FECACA' }); } else { pill(ctx, 'somme des forces', tx + sx / ns * 12, ty + sy / ns * 12 + (sy > 0 ? 8 : -8), { size: 11, col: '#B91C1C', stroke: '#FECACA', align: Math.abs(sx / ns) < 0.3 ? 'center' : (sx > 0 ? 'left' : 'right') }); }   /* étiquette au bout de la flèche */ }
      else { pill(ctx, 'somme des forces nulle', W - 10, 16, { size: 11.5, col: '#B91C1C', stroke: '#FECACA', align: 'right' }); }
      if (E.vit) { vec(ctx, fx, fy, fx + E.vit[0] * L, fy + E.vit[1] * L, ORANGE, 3, 12); pill(ctx, 'vitesse', fx + E.vit[0] * L + 8, fy + E.vit[1] * L - 6, { size: 11, col: ORANGE_T, stroke: '#FDE68A', align: 'left' }); }   /* le ballon monte et avance */
      croix(ctx, fx, fy, '#1E293B', 6);
    }
    cD = Canvas($(root, '.nt-c-doi'), function (W) { return W < 520 ? 260 : 280; }, drawD);
    cF = Canvas($(root, '.nt-c-f'), function (W) { return W < 520 ? 300 : 320; }, drawF);
    bV.addEventListener('click', valider);
    var loopA = Loop(root, function (dt) { if (!anim) { return false; } tA += dt; drawF(cF); return true; });
    bA.addEventListener('click', function () {
      anim = !anim; bA.innerHTML = anim ? '<i class="fa-solid fa-stop"></i>&nbsp; Revenir au schéma fixe' : '<i class="fa-solid fa-play"></i>&nbsp; Animer le mouvement de la balle';
      m2.innerHTML = anim ? 'Au cours du balancement, le poids ne change pas, mais la tension du fil varie&nbsp;: elle est maximale au point le plus bas. La somme des forces (en rouge vif) <b>n\u2019est jamais nulle</b>&nbsp;: au point le plus bas, elle est verticale, vers le haut (vers le point d\u2019attache)&nbsp;; aux extrémités, où la balle s\u2019arrête un instant, elle est tangente à la trajectoire. Le vecteur vitesse change donc en permanence.' : 'On modélise maintenant le système par un point matériel, et chaque action par une force. ' + EX[ex].bilan;
      if (anim) { tA = 0; if (RM) { tA = PER / 4; drawF(cF); } else { loopA.kick(); } } else { drawF(cF); }
    });
    bD.addEventListener('click', function () { decomp = !decomp; bD.innerHTML = decomp ? '<i class="fa-solid fa-arrows-split-up-and-left"></i>&nbsp; Recomposer' : '<i class="fa-solid fa-arrows-split-up-and-left"></i>&nbsp; Décomposer la force du sol'; m2.innerHTML = decomp ? 'La force du sol se décompose en deux&nbsp;: une partie verticale, la <b>réaction du support</b>, qui compense le poids, et une partie horizontale, la <b>force de propulsion</b>, qui pousse la moto vers l\u2019avant et l\u2019emporte sur les frottements de l\u2019air&nbsp;: d\u2019où une somme des forces dirigée vers l\u2019avant.' : 'On modélise maintenant le système par un point matériel, et chaque action par une force. ' + EX[ex].bilan; drawF(cF); });
    $$(root, 'input[name="doi-ex"]').forEach(function (r) { r.addEventListener('change', function () { ex = r.value; charge(); }); });
    charge();
  })();

  /* =================== 6. Entraînement : masse et poids =================== */
  (function () {
    var root = document.getElementById('tr-poids'); if (!root) { return; }
    var qEl = $(root, '.nt-tr-q'), inp = $(root, '#trp-x'), lab = $(root, '.nt-trp-l'), un = $(root, '.nt-trp-u'), P = null;
    var OBJ = [['un smartphone', 0.18], ['un sac de courses', 4.5], ['un élève', 58], ['un vélo', 12], ['une pomme', 0.15], ['un astronaute équipé', 120]];
    function de(s) { return /^[aeiouyéèêh]/i.test(s) ? 'd\u2019' + s : 'de ' + s; }
    function gen(k) {
      var o = pick(OBJ), typ = ['P', 'P', 'm', 'lune', 'mars'][k % 5];
      if (typ === 'P') { return { q: 'Quel est le poids ' + de(o[0]) + ' de masse ' + fmt(o[1], o[1] < 1 ? 2 : (o[1] < 10 ? 1 : 0)) + '&nbsp;kg, sur Terre ($g = \\pu{9,8 N*kg-1}$)&nbsp;?', l: '$P$&nbsp;=', u: 'N', r: o[1] * 9.8, c: '$P = m \\times g = ' + fmt(o[1], 2).replace(/,?0+$/, '') + ' \\times 9{,}8$' }; }
      if (typ === 'm') { var Pv = Math.round(o[1] * 9.8 * 10) / 10; return { q: 'Sur Terre, le poids ' + de(o[0]) + ' vaut ' + fmt(Pv, Pv % 1 ? 1 : 0) + '&nbsp;N. Quelle est sa masse&nbsp;?', l: '$m$&nbsp;=', u: 'kg', r: Pv / 9.8, c: '$m = \\dfrac{P}{g} = \\dfrac{' + fmt(Pv, 1) + '}{9{,}8}$' }; }
      var g = typ === 'lune' ? 1.6 : 3.7, lieu = typ === 'lune' ? 'sur la Lune ($g = \\pu{1,6 N*kg-1}$)' : 'sur Mars ($g = \\pu{3,7 N*kg-1}$)';
      return { q: 'Quel serait le poids ' + de(o[0]) + ' de masse ' + fmt(o[1], o[1] < 1 ? 2 : (o[1] < 10 ? 1 : 0)) + '&nbsp;kg ' + lieu + '&nbsp;?', l: '$P$&nbsp;=', u: 'N', r: o[1] * g, c: '$P = m \\times g$, avec la valeur de $g$ du lieu' };
    }
    var S = Serie(root, 5, {
      show: function (k) { P = gen(k); qEl.innerHTML = P.q; lab.innerHTML = P.l; un.textContent = P.u; inp.value = ''; $(root, '[data-act="check"]').disabled = false; typeset(qEl); typeset(lab); },
      bilan: function (g, t0) { qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;5</span><br>' + t0; }
    });
    $(root, '[data-act="check"]').addEventListener('click', function () {
      if (S.answered || S.fini) { return; } var x = num(inp.value); if (isNaN(x)) { S.say('Entrez une valeur numérique.'); return; }
      var ok = Math.abs(x - P.r) <= 0.02 * Math.abs(P.r); $(root, '[data-act="check"]').disabled = true;
      S.answer(ok, P.c + ' $\\approx ' + String(sig(P.r, 3)).replace('.', '{,}') + '$&nbsp;' + P.u + '.', ok ? null : '<b>Non.</b> '); typeset($(root, '.nt-msg'));
    });
    S.start();
  })();

  /* =================== 7. Un palet sur différentes surfaces =================== */
  (function () {
    var root = document.getElementById('lab-palet'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), surf = 'air', duree = 'court', t = 0, run = false, cnv, V0 = 3;
    var SU = { air: [0.04, '#E0F2FE', 'coussin d\u2019air'], glace: [0.15, '#F0F9FF', 'glace'], parquet: [1.5, '#E7C99A', 'parquet'], moquette: [4, '#B8A9C9', 'moquette'] };
    function x(t) { var a = SU[surf][0], ts = V0 / a; return t < ts ? V0 * t - 0.5 * a * t * t : V0 * ts / 2; }
    function T() { return duree === 'court' ? 0.6 : 6; }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, Lm = duree === 'court' ? 2.0 : 19, k = (W - 40) / Lm, x0 = 20, y = H * 0.55, s = SU[surf];
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = s[1]; rr(ctx, 6, H * 0.18, W - 12, H * 0.74, 12); ctx.fill();
      if (surf === 'parquet') { ctx.strokeStyle = 'rgba(146,64,14,0.25)'; for (var p = 6; p < W; p += 34) { ctx.beginPath(); ctx.moveTo(p, H * 0.18); ctx.lineTo(p, H * 0.92); ctx.stroke(); } }
      if (surf === 'air') { ctx.fillStyle = 'rgba(14,116,144,0.18)'; for (var i = 0; i < 260; i++) { ctx.fillRect(10 + (i * 37) % (W - 20), H * 0.2 + (i * 53) % (H * 0.7), 2, 2); } }
      ctx.strokeStyle = 'rgba(15,23,42,0.25)'; ctx.lineWidth = 1; rr(ctx, 6, H * 0.18, W - 12, H * 0.74, 12); ctx.stroke();
      for (var m = 0; m <= Lm; m += (duree === 'court' ? 0.5 : 5)) { var xm = x0 + m * k; ctx.fillStyle = SLATE; ctx.fillRect(xm, H * 0.86, 1, 8); txt(ctx, fmt(m, duree === 'court' ? 1 : 0) + ' m', xm, H * 0.82, { size: 10, col: SLATE }); }
      var N = 10, dt = T() / N, prev = null, ecarts = [];
      for (var j = 0; j <= N; j++) { var tj = j * dt; if (tj > t + 1e-9) { break; } var xj = x0 + x(tj) * k; ctx.fillStyle = 'rgba(30,41,59,0.25)'; ctx.beginPath(); ctx.arc(xj, y, 9, 0, 2 * Math.PI); ctx.fill(); croix(ctx, xj, y, ROUGE, 3.5); if (prev !== null) { ecarts.push(x(tj) - prev); } prev = x(tj); }
      var xp = x0 + x(Math.min(t, T())) * k; ctx.fillStyle = '#111827'; ctx.beginPath(); ctx.arc(xp, y, 10, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#374151'; ctx.beginPath(); ctx.arc(xp, y, 6, 0, 2 * Math.PI); ctx.fill();
      pill(ctx, s[2] + ' · une photo toutes les ' + fmt(dt, duree === 'court' ? 2 : 1) + ' s', 10, 14, { size: 11.5, col: NAVY, align: 'left', stroke: GRID2 });
      root._ecarts = ecarts;
    }
    function bilan() {
      var e = root._ecarts || []; if (e.length < 2) { return; } var d = (e[e.length - 1] - e[0]) / e[0] * 100;
      msg.innerHTML = e[e.length - 1] < 1e-6 ? 'Sur ' + (duree === 'court' ? '0,6' : '6') + '&nbsp;s, le palet a eu le temps de <b>s\u2019arrêter</b>&nbsp;: les frottements ont modifié son mouvement.' :
        'Entre le premier et le dernier intervalle, l\u2019écart entre deux positions a diminué de <b>' + fmt(Math.abs(d), Math.abs(d) < 10 ? 1 : 0) + '&nbsp;%</b>' + (Math.abs(d) < 5 ? '&nbsp;: à l\u2019œil, le mouvement est rectiligne uniforme.' : '&nbsp;: le palet ralentit nettement.');
    }
    var loop = Loop(root, function (dt) { if (!run) { return false; } t += dt * (duree === 'court' ? 0.25 : 1); if (t >= T()) { t = T(); run = false; draw(cnv); bilan(); return false; } draw(cnv); return true; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 170 : 190; }, draw);
    function lance() { t = 0; msg.textContent = 'Le palet glisse…'; if (RM) { t = T(); draw(cnv); bilan(); return; } run = true; loop.kick(); }
    $(root, '[data-act="lancer"]').addEventListener('click', lance);
    $$(root, 'input[name="pl-s"]').forEach(function (r) { r.addEventListener('change', function () { surf = r.value; lance(); }); });
    $$(root, 'input[name="pl-d"]').forEach(function (r) { r.addEventListener('change', function () { duree = r.value; lance(); }); });
    msg.textContent = 'Choisissez une surface et une durée d\u2019observation, puis lancez le palet à 3\u00A0m·s⁻¹.'; t = 0; draw(cnv);
  })();

  /* =================== 7 b. Réciproques ou compensées ? =================== */
  (function () {
    var root = document.getElementById('quiz-reciproque'); if (!root) { return; }
    var C = 'Elles se compensent (même système)', R = 'Elles sont réciproques (même interaction)', N = 'Ni l\u2019un ni l\u2019autre';
    var BQ = [
      ['Les forces de la Terre sur le livre et de la table sur le livre…', [C, R, N], 'Elles s\u2019exercent toutes les deux sur le livre et proviennent de deux interactions différentes&nbsp;: elles se compensent, et le livre reste immobile.'],
      ['Les forces de la table sur le livre et du livre sur la table…', [R, C, N], 'Ce sont les deux sens de l\u2019interaction livre-table&nbsp;: elles sont réciproques, et s\u2019exercent sur deux systèmes différents.'],
      ['Les forces de la Terre sur le livre et du livre sur la Terre…', [R, C, N], 'Ce sont les deux sens de l\u2019interaction Terre-livre&nbsp;: elles sont réciproques. Le livre attire la Terre exactement autant que la Terre attire le livre&nbsp;!'],
      ['Les forces du livre sur la table et du livre sur la Terre…', [N, C, R], 'Elles s\u2019exercent sur deux systèmes différents (la table, la Terre) et proviennent de deux interactions différentes&nbsp;: ni réciproques, ni compensées.'],
      ['Pourquoi deux forces réciproques ne peuvent-elles jamais se compenser&nbsp;?', ['Parce qu\u2019elles s\u2019exercent sur deux systèmes différents', 'Parce qu\u2019elles n\u2019ont pas la même intensité', 'Parce qu\u2019elles ont le même sens'], 'Pour se compenser, deux forces doivent s\u2019exercer sur le même système. Deux forces réciproques agissent chacune sur un système différent.']
    ];
    Quiz(root, BQ, 5, function () { return BQ.slice(); });
  })();

  /* =================== 7 c. La chandelle au rugby =================== */
  (function () {
    var root = document.getElementById('lab-rugby'); if (!root) { return; }
    var chkC = $(root, '[data-in="chrono"]'), chkV = $(root, '[data-in="comp"]'), msg = $(root, '.nt-msg'), bG = $(root, '[data-act="go"]');
    var G = 9.8, VX = 8, VY = 14, TV = 2 * VY / G, DTP = 0.25, RAL = 0.55, t = -1, cnv, NU = [[4, 0.12], [14, 0.2], [23, 0.1]];
    function pos(t) { var q = Math.min(Math.max(t, 0), TV); return [2 + VX * q, Math.max(0, VY * q - 0.5 * G * q * q)]; }   /* abscisse et altitude du ballon (m) */
    function ballon(ctx, x, y, r, a, al) {   /* ballon de rugby : ovale, coutures et lacets */
      ctx.save(); ctx.globalAlpha = al; ctx.translate(x, y); ctx.rotate(a);
      var g = ctx.createRadialGradient(-r * 0.4, -r * 0.4, 1, 0, 0, r * 1.5); g.addColorStop(0, '#FFFFFF'); g.addColorStop(0.6, '#E5E7EB'); g.addColorStop(1, '#9CA3AF');
      ctx.fillStyle = g; ctx.beginPath(); ctx.ellipse(0, 0, r * 1.5, r, 0, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = '#1D4ED8'; ctx.lineWidth = Math.max(1, r * 0.18); ctx.beginPath(); ctx.ellipse(0, 0, r * 1.5, r * 0.45, 0, Math.PI * 1.05, Math.PI * 1.95); ctx.stroke();
      ctx.strokeStyle = '#475569'; ctx.lineWidth = 1; for (var l = -2; l <= 2; l++) { ctx.beginPath(); ctx.moveTo(l * r * 0.22, -r * 0.62); ctx.lineTo(l * r * 0.22, -r * 0.36); ctx.stroke(); }
      ctx.restore();
    }
    function joueur(ctx, px, py, k, frappe) {   /* rugbyman de profil, tourné vers la droite (pieds en (px, py)) */
      ctx.save(); ctx.lineCap = 'round'; ctx.lineJoin = 'round';
      var hanche = [px, py - 0.95 * k], pied = frappe ? [px + 0.78 * k, py - 1.15 * k] : [px + 0.32 * k, py], genou = frappe ? [px + 0.42 * k, py - 0.62 * k] : [px + 0.24 * k, py - 0.48 * k];
      function seg(a, b, c, w) { ctx.strokeStyle = c; ctx.lineWidth = w; ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.stroke(); }
      seg(hanche, [px - 0.22 * k, py - 0.48 * k], '#F2C9A0', 0.15 * k); seg([px - 0.22 * k, py - 0.48 * k], [px - 0.16 * k, py - 0.08 * k], '#B91C1C', 0.14 * k);   /* jambe d'appui : cuisse, chaussette */
      ctx.fillStyle = '#111827'; rr(ctx, px - 0.26 * k, py - 0.1 * k, 0.32 * k, 0.1 * k, 0.04 * k); ctx.fill();
      seg(hanche, genou, '#F2C9A0', 0.15 * k); seg(genou, pied, '#B91C1C', 0.14 * k);   /* jambe de frappe */
      ctx.save(); ctx.translate(pied[0], pied[1]); ctx.rotate(frappe ? -0.6 : 0); ctx.fillStyle = '#111827'; rr(ctx, -0.06 * k, -0.06 * k, 0.32 * k, 0.11 * k, 0.04 * k); ctx.fill(); ctx.restore();
      ctx.fillStyle = '#F8FAFC'; rr(ctx, px - 0.24 * k, py - 1.12 * k, 0.48 * k, 0.32 * k, 0.08 * k); ctx.fill();   /* short */
      var gm = ctx.createLinearGradient(px - 0.25 * k, 0, px + 0.25 * k, 0); gm.addColorStop(0, '#B91C1C'); gm.addColorStop(1, '#EF4444'); ctx.fillStyle = gm; rr(ctx, px - 0.26 * k, py - 1.82 * k, 0.52 * k, 0.78 * k, 0.12 * k); ctx.fill();   /* maillot */
      ctx.fillStyle = '#FFFFFF'; ctx.fillRect(px - 0.26 * k, py - 1.5 * k, 0.52 * k, 0.07 * k); ctx.font = 'bold ' + Math.round(0.22 * k) + 'px ' + FONT; ctx.textAlign = 'center'; ctx.fillText('10', px, py - 1.2 * k);
      seg([px + 0.1 * k, py - 1.7 * k], [px + 0.45 * k, py - 1.35 * k], '#B91C1C', 0.12 * k); seg([px - 0.1 * k, py - 1.7 * k], [px - 0.48 * k, py - 1.45 * k], '#B91C1C', 0.12 * k);   /* bras écartés pour l'équilibre */
      ctx.fillStyle = '#F2C9A0'; ctx.beginPath(); ctx.arc(px + 0.02 * k, py - 2.02 * k, 0.17 * k, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#3F2A1D'; ctx.beginPath(); ctx.arc(px - 0.01 * k, py - 2.08 * k, 0.17 * k, Math.PI * 0.95, Math.PI * 2.0); ctx.fill();
      ctx.restore();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, sol = H - 46, k = Math.min((W - 40) / 28, (sol - 34) / 11.5), x0 = (W - 28 * k) / 2, sx = function (x) { return x0 + x * k; }, sy = function (y) { return sol - y * k; };   /* scène centrée */
      ctx.clearRect(0, 0, W, H);
      var gs = ctx.createLinearGradient(0, 0, 0, sol); gs.addColorStop(0, '#38BDF8'); gs.addColorStop(0.7, '#BAE6FD'); gs.addColorStop(1, '#E0F2FE'); ctx.fillStyle = gs; ctx.fillRect(0, 0, W, sol);
      var gsol = ctx.createRadialGradient(W - 44, 30, 2, W - 44, 30, 40); gsol.addColorStop(0, 'rgba(254,240,138,1)'); gsol.addColorStop(0.4, 'rgba(253,224,71,0.9)'); gsol.addColorStop(1, 'rgba(253,224,71,0)'); ctx.fillStyle = gsol; ctx.beginPath(); ctx.arc(W - 44, 30, 40, 0, 2 * Math.PI); ctx.fill();   /* Soleil, haut dans le ciel */
      NU.forEach(function (n) { var cxn = x0 + n[0] * k; ctx.fillStyle = 'rgba(255,255,255,0.9)'; ctx.beginPath(); ctx.ellipse(cxn, n[1] * H, 34, 10, 0, 0, 2 * Math.PI); ctx.ellipse(cxn + 18, n[1] * H - 7, 18, 10, 0, 0, 2 * Math.PI); ctx.ellipse(cxn - 16, n[1] * H - 3, 14, 8, 0, 0, 2 * Math.PI); ctx.fill(); });
      var ht = sol - 0.065 * H;   /* tribune lointaine, discrète, avec le public */
      ctx.fillStyle = '#94A3B8'; ctx.fillRect(0, ht - 6, W, 0.065 * H + 6); ctx.fillStyle = '#CBD5E1'; ctx.fillRect(0, ht - 9, W, 3);
      for (var cx2 = 4; cx2 < W; cx2 += 6) { for (var r2 = 0; r2 < 2; r2++) { ctx.fillStyle = ['rgba(248,113,113,0.7)', 'rgba(251,191,36,0.7)', 'rgba(96,165,250,0.7)', 'rgba(248,250,252,0.8)', 'rgba(52,211,153,0.7)'][(cx2 * 7 + r2 * 13) % 5]; ctx.beginPath(); ctx.arc(cx2 + (r2 % 2) * 3, ht + 2 + r2 * 0.028 * H, 1.6, 0, 2 * Math.PI); ctx.fill(); } }
      ctx.fillStyle = '#64748B'; ctx.fillRect(0, sol - 4, W, 4);
      for (var b = 0; b < 12; b++) { ctx.fillStyle = b % 2 ? '#22C55E' : '#16A34A'; ctx.fillRect(b * W / 12, sol, W / 12 + 1, H - sol); }   /* pelouse tondue en bandes */
      ctx.fillStyle = 'rgba(255,255,255,0.85)'; [-2, 8, 18, 28].forEach(function (m) { if (sx(m) > 0 && sx(m) < W) { ctx.fillRect(sx(m) - 1, sol, 2, H - sol); } });
      var xp = sx(27.2);   /* poteaux en H */
      ctx.strokeStyle = '#F8FAFC'; ctx.lineWidth = 4; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(xp, sol); ctx.lineTo(xp, sy(9)); ctx.moveTo(xp + 12, sol - 4); ctx.lineTo(xp + 12, sy(9) - 4); ctx.moveTo(xp, sy(3)); ctx.lineTo(xp + 12, sy(3) - 4); ctx.stroke(); ctx.fillStyle = '#EF4444'; ctx.fillRect(xp - 3, sol - 0.8 * k, 18, 0.8 * k);
      var axe = sx(0.4);   /* axe vertical gradué : projection du ballon */
      ctx.strokeStyle = 'rgba(15,23,42,0.55)'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(axe, sol); ctx.lineTo(axe, sy(10.6)); ctx.stroke();
      for (var m2 = 0; m2 <= 10; m2 += 2) { ctx.fillStyle = 'rgba(15,23,42,0.6)'; ctx.fillRect(axe - 4, sy(m2), 8, 1.2); if (m2) { pill(ctx, m2 + ' m', axe - 8, sy(m2), { size: 9.5, col: '#0F172A', bg: 'rgba(255,255,255,0.75)', align: 'right' }); } }
      var tt = Math.max(t, 0);
      if (t >= 0) { ctx.save(); ctx.setLineDash([2, 5]); ctx.strokeStyle = 'rgba(15,23,42,0.35)'; ctx.lineWidth = 1.5; ctx.beginPath(); for (var i = 0; i <= 60; i++) { var ti = Math.min(tt, TV) * i / 60, q0 = pos(ti); if (i) { ctx.lineTo(sx(q0[0]), sy(q0[1]) - 0.25 * k); } else { ctx.moveTo(sx(q0[0]), sy(q0[1]) - 0.25 * k); } } ctx.stroke(); ctx.restore(); }
      if (chkC.checked && t >= 0) { for (var tj = 0; tj <= Math.min(tt, TV) + 1e-9; tj += DTP) { var q = pos(tj); ballon(ctx, sx(q[0]), sy(q[1]) - 0.25 * k, 0.2 * k, -tj * 4, 0.4); croix(ctx, sx(q[0]), sol + 10, '#F8FAFC', 4); croix(ctx, axe, sy(q[1]) - 0.25 * k, ROUGE, 4); } }
      var bq = pos(tt), bx = sx(bq[0]), by = sy(bq[1]) - 0.25 * k;
      ctx.fillStyle = 'rgba(15,23,42,' + (0.38 - Math.min(0.22, bq[1] * 0.022)).toFixed(2) + ')'; ctx.beginPath(); ctx.ellipse(bx, sol + 2, 0.32 * k, 0.08 * k, 0, 0, 2 * Math.PI); ctx.fill();   /* ombre, juste sous le ballon */
      ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = 'rgba(15,23,42,0.4)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(bx, by + 0.2 * k); ctx.lineTo(bx, sol); ctx.moveTo(bx - 0.3 * k, by); ctx.lineTo(axe, by); ctx.stroke(); ctx.restore();
      ctx.fillStyle = ROUGE; ctx.beginPath(); ctx.arc(axe, by, 4.5, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = 1.5; ctx.stroke();
      joueur(ctx, sx(1.4), sol, k, t >= 0 && t < 0.3);
      ballon(ctx, bx, by, 0.22 * k, t > 0 && t < TV ? -t * 4 : 0, 1);
      if (t > 0 && t < TV) {
        var vy = VY - G * t, f = 0.11 * k;
        if (chkV.checked) { ctx.save(); ctx.setLineDash([4, 3]); vec(ctx, bx, by, bx + VX * f, by, '#047857', 2.2, 9); if (Math.abs(vy) > 0.3) { vec(ctx, bx, by, bx, by - vy * f, '#BE123C', 2.2, 9); } ctx.restore(); }
        vec(ctx, bx, by, bx + VX * f, by - vy * f, ORANGE, 3, 12);
        vec(ctx, bx, sol + 26, bx + VX * f, sol + 26, '#047857', 2.6, 10);   /* la vitesse de l'ombre, toujours la même */
      }
      pill(ctx, 'vitesse de l\u2019ombre\u00A0: ' + (t > 0 && t < TV ? fmt(VX, 0) : '0') + ' m·s⁻¹', Math.min(W - 10, Math.max(150, bx + 0.6 * k + 140)), sol + 26, { size: 11, col: '#065F46', bg: 'rgba(255,255,255,0.92)', align: 'right' });
    }
    var loop = Loop(root, function (dt) { if (t < 0) { return false; } t += dt * RAL; if (t >= TV) { t = TV; draw(cnv); fin(); return false; } draw(cnv); return true; });
    function fin() { bG.disabled = false; msg.innerHTML = 'Sur le sol, les positions successives de l\u2019ombre (croix blanches) sont <b>également espacées</b>&nbsp;: la vitesse horizontale du ballon est restée constante, égale à 8&nbsp;m·s⁻¹. Sur l\u2019axe vertical (croix rouges), les positions se resserrent à la montée puis s\u2019écartent à la descente&nbsp;: la vitesse verticale varie, car le poids agit verticalement.'; }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 300 : 360; }, draw);
    bG.addEventListener('click', function () { t = 0; bG.disabled = true; msg.textContent = 'Le ballon s\u2019élève… regardez son ombre.'; if (RM) { t = TV; draw(cnv); fin(); return; } loop.kick(); });
    [chkC, chkV].forEach(function (c) { c.addEventListener('change', function () { draw(cnv); }); });
    msg.textContent = 'Le Soleil est haut dans le ciel\u00A0: l\u2019ombre du ballon est juste en dessous de lui. Tapez la chandelle\u00A0!'; draw(cnv);
  })();

  /* =================== 7 d. La balle sur la remorque (repris du chapitre sur le mouvement) =================== */
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
      pill(ctx, 'tracteur\u00A0: ' + fmt(S.V * 3.6, 0) + ' km·h⁻¹' + (S.A > 0 ? ' (accélère)' : (S.A < 0 ? ' (freine)' : '')), W < 520 ? 10 : W - 10, W < 520 ? 42 : 16, { size: 12, col: '#166534', align: W < 520 ? 'left' : 'right', stroke: '#BBF7D0' });
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


  /* =================== 8. Un astronaute pousse un objet =================== */
  function personne(ctx, x, y, s, o) {   /* personne flottante vue de profil, tournée vers la droite (o.dir = -1 : vers la gauche) ; (x, y) = hanches */
    o = o || {}; var d = o.dir || 1, haut = o.haut || '#1E3A8A', bas = o.bas || '#334155';
    ctx.save(); ctx.translate(x, y); ctx.scale(d, 1); ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    function membre(pts, col, w) { ctx.strokeStyle = col; ctx.lineWidth = w; ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]); for (var i = 1; i < pts.length; i++) { ctx.lineTo(pts[i][0], pts[i][1]); } ctx.stroke(); }
    var epaule = [3 * s, -27 * s], bras = o.mains ? o.mains.map(function (h) { return [(h[0] - x) * d, h[1] - y]; }) : null;
    function brasIK(h, col) {   /* bras en deux segments, coude calculé pour que la main atteigne le point h */
      var a = 15 * s, dx = h[0] - epaule[0], dy = h[1] - epaule[1], L = Math.min(Math.hypot(dx, dy), 2 * a - 0.01), an = Math.atan2(dy, dx), b = Math.acos(L / (2 * a)), cx = epaule[0] + a * Math.cos(an + b), cy = epaule[1] + a * Math.sin(an + b);
      var hx = epaule[0] + L * Math.cos(an), hy = epaule[1] + L * Math.sin(an);
      membre([epaule, [cx, cy], [hx, hy]], col, 5.5 * s);
      ctx.fillStyle = '#0F172A'; ctx.beginPath(); ctx.arc(hx, hy, 3.4 * s, 0, 2 * Math.PI); ctx.fill();
    }
    if (bras) { brasIK(bras[0], '#1E3A8A'); } else { membre([epaule, [9 * s, -14 * s], [17 * s, -10 * s]], '#1E3A8A', 5.5 * s); }   /* bras arrière-plan */
    membre([[-2 * s, 0], [7 * s, 14 * s], [1 * s, 30 * s]], bas, 7 * s); membre([[3 * s, 0], [12 * s, 12 * s], [9 * s, 29 * s]], bas, 7 * s);   /* jambes pliées, en apesanteur */
    ctx.fillStyle = '#E2E8F0'; rr(ctx, -4 * s, 27 * s, 12 * s, 6 * s, 3 * s); ctx.fill(); rr(ctx, 4 * s, 26 * s, 12 * s, 6 * s, 3 * s); ctx.fill();   /* chaussons */
    var gt = ctx.createLinearGradient(-9 * s, 0, 10 * s, 0); gt.addColorStop(0, haut); gt.addColorStop(1, '#3B5BDB'); ctx.fillStyle = gt;
    ctx.beginPath(); ctx.moveTo(-7 * s, 2 * s); ctx.lineTo(-8 * s, -26 * s); ctx.quadraticCurveTo(-6 * s, -33 * s, 2 * s, -33 * s); ctx.quadraticCurveTo(9 * s, -32 * s, 9 * s, -24 * s); ctx.lineTo(8 * s, 2 * s); ctx.closePath(); ctx.fill();   /* torse (polo) */
    ctx.fillStyle = '#93C5FD'; rr(ctx, -5 * s, -30 * s, 4 * s, 4 * s, 1 * s); ctx.fill();   /* écusson */
    ctx.fillStyle = '#F2C9A0'; ctx.fillRect(-1 * s, -37 * s, 5 * s, 5 * s);   /* cou */
    ctx.beginPath(); ctx.ellipse(2 * s, -44 * s, 8 * s, 9 * s, 0, 0, 2 * Math.PI); ctx.fill();   /* tête */
    ctx.fillStyle = o.cheveux || '#7C2D12'; ctx.beginPath(); ctx.ellipse(0, -48 * s, 8.5 * s, 6.5 * s, -0.2, Math.PI * 0.9, Math.PI * 2.05); ctx.fill();
    ctx.fillStyle = '#1E293B'; ctx.beginPath(); ctx.arc(6.5 * s, -45 * s, 1.1 * s, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#B45309'; ctx.lineWidth = 1 * s; ctx.beginPath(); ctx.arc(6 * s, -40.5 * s, 2 * s, 0.2, 1.4); ctx.stroke();   /* œil et sourire */
    if (bras) { brasIK(bras[1] || bras[0], '#2B4BC0'); } else { membre([epaule, [10 * s, -18 * s], [18 * s, -14 * s]], '#2B4BC0', 5.5 * s); ctx.fillStyle = '#F2C9A0'; ctx.beginPath(); ctx.arc(18 * s, -14 * s, 3 * s, 0, 2 * Math.PI); ctx.fill(); }   /* bras au premier plan */
    ctx.restore();
  }
  (function () {
    var root = document.getElementById('lab-pousse'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), bP = $(root, '[data-act="pousser"]'), M = 100, m = 0.06, U = 1.6, TP = 0.25, RAL = 0.35, t = -1, cnv, fini = false;   /* vitesse relative finale U (m·s⁻¹), durée de la poussée TP (s) */
    function vit() { return [-U * m / (M + m), U * M / (M + m)]; }   /* vitesses finales de l'astronaute et de l'objet */
    function etat(t) {   /* positions (m) et vitesses (m·s⁻¹) : accélération constante pendant la poussée, puis vitesse constante */
      var v = vit(); if (t <= 0) { return [0, 0, 0, 0]; }
      var q = Math.min(t, TP), xa = v[0] * q * q / (2 * TP), xo = v[1] * q * q / (2 * TP), f = q / TP;
      if (t > TP) { xa += v[0] * (t - TP); xo += v[1] * (t - TP); }
      return [xa, xo, v[0] * f, v[1] * f];
    }
    function largeur(s) { return m < 1 ? 11 * s : (m < 50 ? 30 * s : (m < 200 ? 30 * s : 52 * s)); }   /* encombrement de l'objet poussé, vers la droite */
    function forme(ctx, x, y, s) {   /* l'objet poussé, son bord gauche en x */
      if (m < 1) { var r = 5.5 * s, g = ctx.createRadialGradient(x + r - 2, y - 2, 1, x + r, y, r); g.addColorStop(0, '#ECFCCB'); g.addColorStop(1, '#A3E635'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x + r, y, r, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.arc(x + r - r * 0.9, y, r * 0.75, -1, 1); ctx.stroke(); ctx.beginPath(); ctx.arc(x + r + r * 0.9, y, r * 0.75, Math.PI - 1, Math.PI + 1); ctx.stroke(); return; }
      if (m < 50) {   /* sac de sport */
        var gs = ctx.createLinearGradient(0, y - 11 * s, 0, y + 11 * s); gs.addColorStop(0, '#F97316'); gs.addColorStop(1, '#C2410C'); ctx.fillStyle = gs; rr(ctx, x, y - 11 * s, 30 * s, 22 * s, 10 * s); ctx.fill();
        ctx.strokeStyle = '#7C2D12'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(x + 4 * s, y - 6 * s); ctx.lineTo(x + 26 * s, y - 6 * s); ctx.stroke(); ctx.strokeStyle = '#1F2937'; ctx.lineWidth = 2 * s; ctx.beginPath(); ctx.moveTo(x + 9 * s, y - 11 * s); ctx.quadraticCurveTo(x + 15 * s, y - 20 * s, x + 21 * s, y - 11 * s); ctx.stroke(); return;
      }
      if (m < 200) { personne(ctx, x + 9 * s, y + 14 * s, s, { haut: '#047857', cheveux: '#1F2937' }); return; }   /* le collègue, dos à l'astronaute */
      var gc = ctx.createLinearGradient(x, y - 26 * s, x + 52 * s, y + 26 * s); gc.addColorStop(0, '#F1F5F9'); gc.addColorStop(1, '#94A3B8'); ctx.fillStyle = gc; rr(ctx, x, y - 26 * s, 52 * s, 52 * s, 5 * s); ctx.fill();   /* caisse de rangement */
      ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.5; rr(ctx, x + 5 * s, y - 21 * s, 42 * s, 42 * s, 3 * s); ctx.stroke(); ctx.fillStyle = '#334155'; rr(ctx, x + 18 * s, y - 24 * s, 16 * s, 4 * s, 2 * s); ctx.fill();
      ctx.fillStyle = '#FBBF24'; ctx.fillRect(x + 8 * s, y + 8 * s, 14 * s, 6 * s); ctx.fillStyle = '#1F2937'; ctx.fillRect(x + 9 * s, y + 10 * s, 12 * s, 1.5 * s);
    }
    function geo(o) { var W = o.W, H = o.H, mx = Math.max(26, W * 0.07), wm = Math.min(W - 2 * mx, H * 3.2), z = { x0: (W - wm) / 2, y0: H * 0.13, w: wm, h: H * 0.62 };   /* largeur plafonnée : personnages et module restent à l'échelle */ z.cx = z.x0 + z.w / 2; z.cy = z.y0 + z.h / 2; z.k = z.w / 8; z.s = z.k / 55; return z; }
    function scene(o) {   /* positions à l'écran : hanches de l'astronaute, bord gauche de l'objet, mains */
      var z = geo(o), k = z.k, s = z.s, e = etat(Math.max(t, 0)), xo = z.cx + 0.1 * k + e[1] * k, yh = z.cy + 10 * s;
      var dx0 = 14 * s, ha = z.cx + 0.1 * k - dx0 - 3 * s + e[0] * k, ep = [ha + 3 * s, yh - 27 * s];
      var main = t <= TP ? [xo, z.cy] : [ep[0] + dx0 + (vit()[1] - vit()[0]) * TP / 2 * k, z.cy];   /* les mains restent sur l'objet pendant la poussée, puis gardent les bras tendus */
      return { z: z, e: e, xo: xo, ha: ha, yh: yh, main: main };
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, S = scene(o), z = S.z, k = z.k, s = z.s, cy = z.cy, xo = S.xo, e = S.e;
      ctx.clearRect(0, 0, W, H); fondEspace(ctx, W, H); moduleCoupe(ctx, z, W, z.x0 > 140 ? 'attaches' : 'bords');
      personne(ctx, S.ha, S.yh, s, { mains: [[S.main[0], S.main[1] - 3 * s], [S.main[0], S.main[1] + 3 * s]] });
      forme(ctx, xo, cy, s);
      if (t >= 0 && t <= TP) { var Fv = (M * m / (M + m)) * (U / TP), Lf = Math.min(0.9 * k, 18 + 12 * Math.log10(1 + Fv)); vec(ctx, xo + 2, cy - 30 * s, xo + 2 + Lf, cy - 30 * s, FORCE, 3, 12); vec(ctx, xo - 2, cy - 30 * s, xo - 2 - Lf, cy - 30 * s, FORCE, 3, 12); pill(ctx, 'deux forces de même intensité\u00A0: ' + sci(Fv, 1) + ' N', z.cx, z.y0 + 16, { size: 11.5, col: FORCE_T, stroke: '#FECACA' }); }
      if (t > 0) { [[S.ha, e[2], 'astronaute'], [xo + largeur(s) / 2, e[3], 'objet']].forEach(function (q) { if (Math.abs(q[1]) > 0.005) { vec(ctx, q[0], cy + 0.72 * k, q[0] + q[1] * k * 0.8, cy + 0.72 * k, ORANGE, 2.6, 10); } var gauche = q[2] === 'astronaute', xl = q[0] + (gauche ? -6 : 6); if (gauche && xl < 150) { gauche = false; xl = Math.max(z.x0 + 4, q[0] - 20); } if (!gauche && q[2] === 'objet' && xl > W - 150) { gauche = true; xl = Math.min(z.x0 + z.w - 4, q[0] + 20); } pill(ctx, q[2] + '\u00A0: ' + (Math.abs(q[1]) < 0.01 ? sci(Math.abs(q[1]), 1) : fmt(Math.abs(q[1]), 2)) + ' m·s⁻¹', xl, cy + 0.98 * k, { size: 11, col: ORANGE_T, stroke: '#FDE68A', align: gauche ? 'right' : 'left' }); }); }   /* étiquettes ramenées dans le cadre */
      pill(ctx, 'référentiel de la station', 10, 16, { size: 11.5, col: '#E2E8F0', bg: 'rgba(15,23,42,0.6)', align: 'left' });
    }
    function bute(o) {   /* arrêt avant que l'objet ou l'astronaute ne touche une paroi */
      var S = scene(o), z = S.z, s = z.s; return S.xo + largeur(s) > z.x0 + z.w - 10 || S.ha - 12 * s < z.x0 + 10;
    }
    var loop = Loop(root, function (dt) { if (t < 0 || fini) { return false; } var t0 = t; t += dt * RAL; if (bute(cnv)) { t = t0; fini = true; draw(cnv); return false; } draw(cnv); return t < TP + 12; });   /* même ralenti pendant et après la poussée */
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 260 : 320; }, draw);
    function reset() { t = -1; fini = false; bP.disabled = false; draw(cnv); msg.textContent = 'Choisissez ce que pousse l\u2019astronaute, puis poussez.'; }
    bP.addEventListener('click', function () { if (t >= 0) { return; } t = 0; bP.disabled = true; msg.innerHTML = 'Pendant la poussée, l\u2019astronaute exerce une force sur l\u2019objet, et l\u2019objet une force <b>de même intensité, de sens opposé</b> sur l\u2019astronaute&nbsp;: leurs vitesses augmentent. Dès que le contact cesse, chacun garde la vitesse acquise&nbsp;: ' + (m < 1 ? 'la balle part vite, l\u2019astronaute bouge à peine.' : (m < 100 ? 'l\u2019objet, plus léger, part plus vite que l\u2019astronaute.' : (m === 100 ? 'même masse, même vitesse&nbsp;!' : 'la caisse, plus lourde, part plus lentement que l\u2019astronaute.'))); loop.kick(); });
    $(root, '[data-act="reset"]').addEventListener('click', reset);
    $$(root, 'input[name="ps-m"]').forEach(function (r) { r.addEventListener('change', function () { m = +r.value; reset(); }); });
    reset();
  })();


  /* =================== 10. De quoi dépend l'attraction gravitationnelle ? =================== */
  (function () {
    var root = document.getElementById('lab-grav'); if (!root) { return; }
    var inA = $(root, '[data-in="ma"]'), inB = $(root, '[data-in="mb"]'), inD = $(root, '[data-in="d"]'), msg = $(root, '.nt-msg'), cnv, GG = 6.67e-11, FMAX = GG * 4e9 * 4e9 / 4e6;   /* force maximale : 4E9 kg et 4E9 kg à 2 km */
    function boule(ctx, x, y, r, c1, c2) {
      ctx.fillStyle = 'rgba(0,0,0,0.25)'; ctx.beginPath(); ctx.ellipse(x, y + r + 6, r * 0.9, r * 0.18, 0, 0, 2 * Math.PI); ctx.fill();
      var g = ctx.createRadialGradient(x - r * 0.35, y - r * 0.4, r * 0.1, x, y, r); g.addColorStop(0, c1); g.addColorStop(1, c2); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = 'rgba(255,255,255,0.35)'; ctx.beginPath(); ctx.ellipse(x - r * 0.35, y - r * 0.45, r * 0.28, r * 0.16, -0.6, 0, 2 * Math.PI); ctx.fill();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, a = +inA.value, b = +inB.value, d = +inD.value, F = GG * a * 1e9 * b * 1e9 / (d * d *1e6);
      var u = (W - Math.min(150, W * 0.16)) / 4, cx = W / 2, y = H * 0.46, xa = cx - d * u / 2, xb = cx + d * u / 2, ra = 13 + 7 * Math.cbrt(a), rb = 13 + 7 * Math.cbrt(b);
      var Lmax = u - 5, L = F / FMAX * Lmax;   /* même échelle pour toutes les forces : à 2 km avec 4E9 kg et 4E9 kg, les pointes se touchent presque ; ailleurs, elles ne peuvent pas se croiser */
      ctx.clearRect(0, 0, W, H); var g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#0B1026'); g.addColorStop(1, '#1E293B'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      ETOILES.forEach(function (e2) { ctx.fillStyle = 'rgba(255,255,255,' + e2[2] * 0.7 + ')'; ctx.fillRect(e2[0] * W, e2[1] * H, 1.2, 1.2); });
      var yd = y + Math.max(ra, rb) + 44; ctx.strokeStyle = 'rgba(203,213,225,0.7)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(xa, yd - 6); ctx.lineTo(xa, yd + 6); ctx.moveTo(xb, yd - 6); ctx.lineTo(xb, yd + 6); ctx.stroke();
      vec(ctx, cx, yd, xa + 1, yd, 'rgba(203,213,225,0.8)', 1, 7); vec(ctx, cx, yd, xb - 1, yd, 'rgba(203,213,225,0.8)', 1, 7);
      pill(ctx, 'AB = ' + fmt(d, d % 1 ? 1 : 0) + ' km', cx, yd, { size: 11.5, col: '#E2E8F0', bg: '#1E293B' });
      boule(ctx, xa, y, ra, '#FDE68A', '#D97706'); boule(ctx, xb, y, rb, '#BAE6FD', '#1D4ED8');
      [[xa, ra, 'A', a], [xb, rb, 'B', b]].forEach(function (q) { txt(ctx, q[2], q[0], y + q[1] + 18, { size: 16, serif: true, col: '#F8FAFC' }); txt(ctx, q[3] + '\u00d710\u2079\u00A0kg', q[0] + 14, y + q[1] + 18, { size: 11.5, col: '#CBD5E1', align: 'left' }); });
      if (L > 0.5) { vec(ctx, xb, y, xb - L, y, FORCE, 3, Math.min(12, L * 0.8)); vec(ctx, xa, y, xa + L, y, FORCE, 3, Math.min(12, L * 0.8)); }
      ctx.save(); ctx.fillStyle = '#F87171'; ctx.beginPath(); ctx.arc(xa, y, 2.5, 0, 2 * Math.PI); ctx.arc(xb, y, 2.5, 0, 2 * Math.PI); ctx.fill(); ctx.restore();
      var ya = L > ra + 14 ? y - 12 : y - ra - 8, yb2 = L > rb + 14 ? y - 12 : y - rb - 8; nomForce(ctx, 'B\u2192A', xa + Math.max(L, 2 * ra + 20) / 2, ya, '#FCA5A5', 'center'); nomForce(ctx, 'A\u2192B', xb - Math.max(L, 2 * rb + 20) / 2, yb2, '#FCA5A5', 'center');   /* légendes au-dessus des flèches, hors des boules */
      pill(ctx, 'F = ' + sci(F, 1) + ' N', cx, 18, { size: 13, col: '#FCA5A5', bg: 'rgba(15,23,42,0.75)' });
      $(root, '.out-ma').textContent = a + '\u00d710\u2079\u00A0kg'; $(root, '.out-mb').textContent = b + '\u00d710\u2079\u00A0kg'; $(root, '.out-d').textContent = fmt(d, d % 1 ? 1 : 0) + '\u00A0km';
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 210 : 240; }, draw);
    [inA, inB, inD].forEach(function (i) { i.addEventListener('input', function () { draw(cnv); }); });
    msg.innerHTML = 'Doublez la masse de A, puis celle de B, puis la distance&nbsp;: comment varie la force&nbsp;? Remarquez que les deux flèches ont toujours <b>la même longueur</b>, même quand les masses sont différentes.';
    draw(cnv);
  })();

  /* =================== 11. Pesanteur et altitude =================== */
  (function () {
    var root = document.getElementById('lab-alt'); if (!root) { return; }
    var inH = $(root, '[data-in="h"]'), msg = $(root, '.nt-msg'), RT = 6371, HM = 40000, cnv;
    var REP = [[400, 'ISS'], [20200, 'satellites GPS'], [35786, 'satellites géostationnaires']];
    function g(h) { return 9.81 * Math.pow(RT / (RT + h), 2); }
    function hval() { var s = +inH.value / 1000; return HM * s * s; }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, x0 = 56, y0 = 26, w = W - x0 - 24, hh = H - 70, X = function (h) { return x0 + h / HM * w; }, Y = function (v) { return y0 + hh - v / 10 * hh; }, h = hval();
      ctx.clearRect(0, 0, W, H); var bg = ctx.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#F8FAFC'); bg.addColorStop(1, '#EEF2F7'); ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = '#E2E8F0'; ctx.lineWidth = 1; for (var v = 0; v <= 10; v += 2) { ctx.beginPath(); ctx.moveTo(x0, Y(v)); ctx.lineTo(x0 + w, Y(v)); ctx.stroke(); txt(ctx, String(v), x0 - 8, Y(v), { size: 10.5, col: SLATE, align: 'right' }); }
      for (var a = 0; a <= HM; a += 10000) { ctx.beginPath(); ctx.moveTo(X(a), y0); ctx.lineTo(X(a), y0 + hh); ctx.stroke(); txt(ctx, fmt(a, 0) + ' km', X(a), y0 + hh + 14, { size: 10.5, col: SLATE }); }
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(x0, y0 - 6); ctx.lineTo(x0, y0 + hh); ctx.lineTo(x0 + w + 8, y0 + hh); ctx.stroke();
      txt(ctx, 'g (N·kg⁻¹)', x0 - 6, 10, { size: 11, col: NAVY, align: 'left' }); txt(ctx, 'altitude', x0 + w, y0 + hh + 32, { size: 11, col: NAVY, align: 'right' });
      var ga = ctx.createLinearGradient(0, y0, 0, y0 + hh); ga.addColorStop(0, 'rgba(37,99,235,0.28)'); ga.addColorStop(1, 'rgba(37,99,235,0.02)'); ctx.fillStyle = ga;
      ctx.beginPath(); ctx.moveTo(X(0), y0 + hh); for (var i = 0; i <= 300; i++) { var hi = HM * i / 300; ctx.lineTo(X(hi), Y(g(hi))); } ctx.lineTo(X(HM), y0 + hh); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#2563EB'; ctx.lineWidth = 2.6; ctx.beginPath(); for (i = 0; i <= 300; i++) { hi = HM * i / 300; if (i) { ctx.lineTo(X(hi), Y(g(hi))); } else { ctx.moveTo(X(hi), Y(g(hi))); } } ctx.stroke();
      REP.forEach(function (r, j) { var xr = X(r[0]), yr = Y(g(r[0])); ctx.fillStyle = '#FFFFFF'; ctx.strokeStyle = '#1D4ED8'; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(xr, yr, 4.5, 0, 2 * Math.PI); ctx.fill(); ctx.stroke(); pill(ctx, r[1], j === 2 ? xr - 6 : xr + 8, yr - 14, { size: 10.5, col: '#1D4ED8', align: j === 2 ? 'right' : 'left', stroke: '#BFDBFE' }); });
      ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(X(h), Y(g(h))); ctx.lineTo(X(h), y0 + hh); ctx.moveTo(X(h), Y(g(h))); ctx.lineTo(x0, Y(g(h))); ctx.stroke(); ctx.restore();
      ctx.fillStyle = ROUGE; ctx.beginPath(); ctx.arc(X(h), Y(g(h)), 6, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = 2; ctx.stroke();
    }
    function texte() { var h = hval(), gv = g(h); $(root, '.out-h').textContent = fmt(h, 0) + '\u00A0km'; msg.innerHTML = 'À ' + fmt(h, 0) + '&nbsp;km d\u2019altitude&nbsp;: $g \\approx ' + String(gv < 1 ? gv.toFixed(2) : gv.toFixed(1)).replace('.', '{,}') + '$&nbsp;N·kg⁻¹, soit ' + fmt(gv / 9.81 * 100, 0) + '&nbsp;% de sa valeur au sol.'; typeset(msg); }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 250 : 290; }, draw);
    inH.addEventListener('input', function () { texte(); draw(cnv); });
    texte(); draw(cnv);
  })();

  /* =================== 12. Boule de bowling et plume =================== */
  (function () {
    var root = document.getElementById('lab-chute'); if (!root) { return; }
    var chk = $(root, '[data-in="chrono"]'), msg = $(root, '.nt-msg'), vide = false, t = 0, run = false, cnv, HC = 3, G = 9.8, RB = 14, RF = 4, DTP = 0.1;
    function yb(t) { return Math.min(HC, 0.5 * G * t * t); }   /* chute (m) depuis le point de lâcher */
    function yp(t) { if (vide) { return yb(t); } var vt = 0.6, tau = vt / G; return Math.min(HC, vt * (t - tau * (1 - Math.exp(-t / tau)))); }   /* plume freinée par l'air */
    function decor(ctx, W, H, sol) {
      var g = ctx.createLinearGradient(0, 0, 0, H);
      if (vide) { g.addColorStop(0, '#1E293B'); g.addColorStop(1, '#334155'); } else { g.addColorStop(0, '#E0F2FE'); g.addColorStop(1, '#F8FAFC'); }
      ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      if (vide) {   /* parois métalliques de la chambre à vide */
        for (var x = 0; x < W; x += 60) { var gp = ctx.createLinearGradient(x, 0, x + 60, 0); gp.addColorStop(0, 'rgba(148,163,184,0.10)'); gp.addColorStop(0.5, 'rgba(203,213,225,0.22)'); gp.addColorStop(1, 'rgba(148,163,184,0.10)'); ctx.fillStyle = gp; ctx.fillRect(x, 0, 58, sol); }
        ctx.fillStyle = 'rgba(203,213,225,0.35)'; for (var y = 30; y < sol; y += 70) { for (var x2 = 12; x2 < W; x2 += 60) { ctx.beginPath(); ctx.arc(x2, y, 2, 0, 2 * Math.PI); ctx.fill(); } }
      } else { ctx.fillStyle = 'rgba(255,255,255,0.7)'; [[0.15, 0.2], [0.8, 0.32]].forEach(function (n) { ctx.beginPath(); ctx.ellipse(n[0] * W, n[1] * H, 36, 11, 0, 0, 2 * Math.PI); ctx.ellipse(n[0] * W + 20, n[1] * H - 7, 20, 10, 0, 0, 2 * Math.PI); ctx.fill(); }); }
      var gs = ctx.createLinearGradient(0, sol, 0, H); gs.addColorStop(0, vide ? '#64748B' : '#CBD5E1'); gs.addColorStop(1, vide ? '#475569' : '#94A3B8'); ctx.fillStyle = gs; ctx.fillRect(0, sol, W, H - sol);
      ctx.fillStyle = vide ? '#94A3B8' : '#64748B'; rr(ctx, W * 0.22, 6, W * 0.56, 10, 4); ctx.fill();   /* système de lâcher */
    }
    function plume(ctx, x, y, a, al) {
      ctx.save(); ctx.globalAlpha = al; ctx.translate(x, y); ctx.rotate(a); ctx.strokeStyle = vide ? '#E2E8F0' : '#64748B'; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(-17, 0); ctx.quadraticCurveTo(0, -2, 17, 0); ctx.stroke();
      var gp = ctx.createLinearGradient(-15, -8, 15, 6); gp.addColorStop(0, vide ? '#F8FAFC' : '#E2E8F0'); gp.addColorStop(1, vide ? '#CBD5E1' : '#94A3B8'); ctx.fillStyle = gp;
      ctx.beginPath(); ctx.moveTo(-14, 0); ctx.bezierCurveTo(-8, -10, 8, -9, 16, -1); ctx.bezierCurveTo(8, 5, -6, 6, -14, 0); ctx.fill(); ctx.restore();
    }
    function boule(ctx, x, y, al) { ctx.save(); ctx.globalAlpha = al; var g = ctx.createRadialGradient(x - 5, y - 5, 1, x, y, RB); g.addColorStop(0, '#6B7280'); g.addColorStop(1, '#0F172A'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, RB, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#E5E7EB'; [[-3, -6], [2, -7], [-1, -2]].forEach(function (q) { ctx.beginPath(); ctx.arc(x + q[0], y + q[1], 1.6, 0, 2 * Math.PI); ctx.fill(); }); ctx.restore(); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, top = 20 + RB, sol = H - 28, k = (sol - RB - top) / HC, xb = W * 0.38, xp = W * 0.62;   /* les deux objets partent avec leur bas à la même hauteur, et finissent au sol */
      ctx.clearRect(0, 0, W, H); decor(ctx, W, H, sol);
      function Yb(y) { return top + y * k; } function Yp(y) { return top + RB - RF + y * k; }
      if (chk.checked) { for (var tj = 0; tj <= t + 1e-9; tj += DTP) { if (yb(tj) < HC || tj < DTP / 2) { boule(ctx, xb, Yb(yb(tj)), 0.2); croix(ctx, xb, Yb(yb(tj)), ROUGE, 3.5); } if (vide) { plume(ctx, xp, Yp(yp(tj)), 0.2, 0.25); croix(ctx, xp, Yp(yp(tj)), ROUGE, 3.5); } else { croix(ctx, xp, Yp(yp(tj)), 'rgba(225,29,72,0.55)', 2.5); } } }
      boule(ctx, xb, Yb(yb(t)), 1); plume(ctx, xp, Yp(yp(t)), vide ? 0.15 : 0.15 + 0.45 * Math.sin(t * 5), 1);
      pill(ctx, vide ? 'chambre à vide' : 'dans l\u2019air', 10, H - 14, { size: 11.5, col: vide ? '#E2E8F0' : NAVY, bg: vide ? 'rgba(15,23,42,0.6)' : '#FFFFFF', align: 'left' });
    }
    function fin() { if (vide) { pred.montrer(); } msg.innerHTML = vide ? 'Dans le vide, la boule et la plume tombent <b>exactement ensemble</b>&nbsp;: les positions sont identiques à chaque instant, de plus en plus espacées. La chute libre ne dépend pas de la masse.' : 'Dans l\u2019air, la plume est très freinée et descend lentement, presque à vitesse constante&nbsp;: elle n\u2019est pas en chute libre. La boule, elle, n\u2019est presque pas freinée.'; }
    var loop = Loop(root, function (dt) { if (!run) { return false; } t += dt; if (yb(t) >= HC && yp(t) >= HC) { run = false; fin(); } draw(cnv); return run; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 300 : 340; }, draw);
    var bL = $(root, '[data-act="lacher"]'), pred = Prediction(root, $(root, 'canvas'), 'dans le vide, lequel des deux objets touchera le sol en premier&nbsp;?', ['la boule de bowling', 'la plume', 'les deux en même temps'], 2, function () { bL.disabled = false; }); pred.el.hidden = true;
    function go() { t = 0; pred.cacher(); msg.textContent = 'Lâcher…'; if (RM) { t = vide ? 0.79 : 5.5; draw(cnv); fin(); return; } run = true; loop.kick(); }
    $(root, '[data-act="lacher"]').addEventListener('click', go);
    $$(root, 'input[name="ch-air"]').forEach(function (r) { r.addEventListener('change', function () { vide = r.value === 'vide'; t = 0; run = false; pred.el.hidden = !vide && pred.choix < 0; bL.disabled = vide && pred.choix < 0; draw(cnv); msg.textContent = vide ? 'On a fait le vide dans une immense chambre\u00A0: lâchez les deux objets.' : 'Les deux objets sont lâchés ensemble, dans l\u2019air.'; }); });
    chk.addEventListener('change', function () { draw(cnv); });
    msg.textContent = 'Les deux objets sont lâchés ensemble, dans l\u2019air.'; draw(cnv);
  })();

  /* =================== 15. Construire le vecteur variation de vitesse =================== */
  (function () {
    var root = document.getElementById('lab-dv'); if (!root) { return; }
    var et = $(root, '.nt-etape'), pts = $(root, '.nt-pts'), bP = $(root, '[data-act="prec"]'), bS = $(root, '[data-act="suiv"]'), mode = 'chute', k = 0, a = 1, cnv;
    function P(o) {   /* positions successives (px) */
      var W = o.W, H = o.H, L = [];
      if (mode === 'chute') { for (var i = 0; i < 5; i++) { L.push([W * 0.18 + W * 0.13 * i, H * 0.78 - H * 0.3 * i + H * 0.07 * i * i]); } return L; }
      var R = Math.min(W, H) * 0.34; for (var j = 0; j < 12; j++) { var an = -Math.PI * 0.9 + 2 * Math.PI * j / 12; L.push([W / 2 + R * Math.cos(an), H / 2 + R * Math.sin(an)]); } return L;
    }
    var IM = 1;   /* M = position n°1, M' = position n°2 */
    var E = {
      chute: [
        ['La chronophotographie', 'Une balle est lancée vers le haut et vers la droite&nbsp;; elle n\u2019est soumise qu\u2019à son poids (chute libre). On s\u2019intéresse aux points M et M\u2032, deux positions successives.'],
        ['Le vecteur vitesse en M', 'Comme au chapitre précédent, <span class="nt-v">$\\vec{v}_\\mathrm{M}$</span> a la direction et le sens du déplacement de M vers la position suivante, M\u2032.'],
        ['Le vecteur vitesse en M\u2032', '<span class="nt-v">$\\vec{v}_{\\mathrm{M\'}}$</span> a la direction et le sens du déplacement de M\u2032 vers la position suivante.'],
        ['On reporte $\\vec{v}_\\mathrm{M}$ en M\u2032', 'Pour comparer les deux vecteurs, on les fait partir du même point&nbsp;: on recopie <span class="nt-v">$\\vec{v}_\\mathrm{M}$</span> (en pointillés) à partir de M\u2032, sans changer ni sa direction, ni son sens, ni sa longueur.'],
        ['On trace $\\overrightarrow{\\Delta v}$', '<span class="nt-dv">$\\overrightarrow{\\Delta v} = \\vec{v}_{\\mathrm{M\'}} - \\vec{v}_\\mathrm{M}$</span> va de l\u2019extrémité de <span class="nt-v">$\\vec{v}_\\mathrm{M}$</span> à l\u2019extrémité de <span class="nt-v">$\\vec{v}_{\\mathrm{M\'}}$</span>&nbsp;: c\u2019est ce qu\u2019il faut ajouter à $\\vec{v}_\\mathrm{M}$ pour obtenir $\\vec{v}_{\\mathrm{M\'}}$.'],
        ['On compare avec les forces', '<span class="nt-dv">$\\overrightarrow{\\Delta v}$</span> est <b>vertical, vers le bas</b>&nbsp;: exactement comme le <span class="nt-force">poids $\\overrightarrow{P}$</span>, la seule force qui s\u2019exerce sur la balle en chute libre.']
      ],
      cercle: [
        ['La chronophotographie', 'Un objet tourne sur un cercle à vitesse constante (mouvement circulaire uniforme). On s\u2019intéresse aux points M et M\u2032, deux positions successives.'],
        ['Le vecteur vitesse en M', '<span class="nt-v">$\\vec{v}_\\mathrm{M}$</span> a la direction et le sens du déplacement de M vers M\u2032.'],
        ['Le vecteur vitesse en M\u2032', '<span class="nt-v">$\\vec{v}_{\\mathrm{M\'}}$</span> a la même longueur que $\\vec{v}_\\mathrm{M}$ (le mouvement est uniforme), mais pas la même direction.'],
        ['On reporte $\\vec{v}_\\mathrm{M}$ en M\u2032', 'On recopie <span class="nt-v">$\\vec{v}_\\mathrm{M}$</span> (en pointillés) à partir de M\u2032, sans changer ni sa direction, ni son sens, ni sa longueur.'],
        ['On trace $\\overrightarrow{\\Delta v}$', '<span class="nt-dv">$\\overrightarrow{\\Delta v}$</span> va de l\u2019extrémité de <span class="nt-v">$\\vec{v}_\\mathrm{M}$</span> à l\u2019extrémité de <span class="nt-v">$\\vec{v}_{\\mathrm{M\'}}$</span>. Il n\u2019est pas nul, bien que la vitesse soit constante&nbsp;!'],
        ['On compare avec les forces', '<span class="nt-dv">$\\overrightarrow{\\Delta v}$</span> est dirigé <b>vers le centre du cercle</b>&nbsp;: la somme des forces aussi. Pour un objet qui tourne au bout d\u2019un fil, c\u2019est la force du fil, qui tire vers le centre.']
      ]
    };
    function etiq(ctx, nom, ind, x1, y1, x2, y2, col, cote) {   /* étiquette de vecteur placée à côté de la flèche, jamais dessus */
      var dx = x2 - x1, dy = y2 - y1, d = Math.hypot(dx, dy) || 1, nx = -dy / d, ny = dx / d;
      if ((cote === 'haut' && ny > 0) || (cote === 'bas' && ny < 0) || (cote === 'droite' && nx < 0)) { nx = -nx; ny = -ny; }
      var cx = (x1 + x2) / 2 + nx * 24, cy = (y1 + y2) / 2 + ny * 24;
      ctx.save(); ctx.font = 'italic 15px Georgia, serif'; var wn = ctx.measureText(nom).width, wi = ind ? 13 : 0, w = wn + wi;
      ctx.fillStyle = 'rgba(255,255,255,0.92)'; rr(ctx, cx - w / 2 - 6, cy - 18, w + 12, 27, 6); ctx.fill(); ctx.restore();
      var xn = cx - w / 2 + wn / 2; nomVec(ctx, nom, xn, cy + 4, col, 15, true, false);
      if (ind) { txt(ctx, ind, xn + wn / 2 + 1, cy + 7, { size: 9.5, serif: true, col: col, align: 'left' }); }
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, L = P(o), M = L[IM], Mp = L[IM + 1], Mpp = L[IM + 2], e = a * a * (3 - 2 * a), SV = mode === 'chute' ? 1.4 : 2.1;
      var v1 = [(Mp[0] - M[0]) * SV, (Mp[1] - M[1]) * SV], v2 = [(Mpp[0] - Mp[0]) * SV, (Mpp[1] - Mp[1]) * SV];
      ctx.clearRect(0, 0, W, H); papier(ctx, 0, 0, W, H, 24);
      if (mode === 'cercle') { ctx.save(); ctx.strokeStyle = TRAJ; ctx.globalAlpha = 0.5; ctx.setLineDash([4, 5]); ctx.beginPath(); ctx.arc(W / 2, H / 2, Math.min(W, H) * 0.34, 0, 2 * Math.PI); ctx.stroke(); ctx.restore(); ctx.fillStyle = '#334155'; ctx.beginPath(); ctx.arc(W / 2, H / 2, 3.5, 0, 2 * Math.PI); ctx.fill(); txt(ctx, 'centre', W / 2, H / 2 + 14, { size: 10.5, col: SLATE }); }
      else { ctx.save(); ctx.strokeStyle = TRAJ; ctx.globalAlpha = 0.5; ctx.setLineDash([4, 5]); ctx.beginPath(); L.forEach(function (p, i) { if (i) { ctx.lineTo(p[0], p[1]); } else { ctx.moveTo(p[0], p[1]); } }); ctx.stroke(); ctx.restore(); }
      L.forEach(function (p, i) { croix(ctx, p[0], p[1], i === IM || i === IM + 1 ? NAVY : '#E11D48', 5); });
      txt(ctx, 'M', M[0] - 12, M[1] + 16, { size: 15, serif: true, col: NAVY }); txt(ctx, 'M\u2032', Mp[0] + 2, Mp[1] + 20, { size: 15, serif: true, col: NAVY });
      if (k >= 1) { var g1 = k === 1 ? e : 1; vec(ctx, M[0], M[1], M[0] + v1[0] * g1, M[1] + v1[1] * g1, ORANGE, 2.8, 12); if (g1 > 0.95) { etiq(ctx, 'v', 'M', M[0], M[1], M[0] + v1[0], M[1] + v1[1], ORANGE_T, 'haut'); } }
      if (k >= 2) { var g2 = k === 2 ? e : 1; vec(ctx, Mp[0], Mp[1], Mp[0] + v2[0] * g2, Mp[1] + v2[1] * g2, ORANGE, 2.8, 12); if (g2 > 0.95) { etiq(ctx, 'v', 'M\u2032', Mp[0], Mp[1], Mp[0] + v2[0], Mp[1] + v2[1], ORANGE_T, 'bas');   /* sous la flèche : la pointe de v_M, au-dessus, reste visible */ } }
      if (k >= 3) { var g3 = k === 3 ? e : 1, ox = M[0] + (Mp[0] - M[0]) * g3, oy = M[1] + (Mp[1] - M[1]) * g3; ctx.save(); ctx.setLineDash([5, 4]); ctx.globalAlpha = 0.85; vec(ctx, ox, oy, ox + v1[0], oy + v1[1], ORANGE, 2, 11); ctx.restore(); }
      if (k >= 4) { var g4 = k === 4 ? e : 1, sx0 = Mp[0] + v1[0], sy0 = Mp[1] + v1[1], ex = Mp[0] + v2[0], ey = Mp[1] + v2[1]; vec(ctx, sx0, sy0, sx0 + (ex - sx0) * g4, sy0 + (ey - sy0) * g4, DV, 3, 12); if (g4 > 0.95) { etiq(ctx, '\u0394v', '', sx0, sy0, ex, ey, DV_T, 'droite'); } }
      if (k >= 5) {
        if (mode === 'chute') { var px = Mp[0], g5 = k === 5 ? e : 1; vec(ctx, px, Mp[1] + 6, px, Mp[1] + 6 + 80 * g5, FORCE, 3, 12); if (g5 > 0.95) { txt(ctx, 'P', px - 14, Mp[1] + 64, { size: 15, serif: true, col: FORCE_T }); vec(ctx, px - 19, Mp[1] + 49, px - 8, Mp[1] + 49, FORCE_T, 1.1, 4.5); } }
        else { ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = DV; ctx.globalAlpha = 0.6; ctx.beginPath(); ctx.moveTo(Mp[0], Mp[1]); ctx.lineTo(W / 2, H / 2); ctx.stroke(); ctx.restore(); }
      }
    }
    var loop = Loop(root, function (dt) { a = Math.min(1, a + dt / 1.0); draw(cnv); return a < 1; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 320 : 380; }, draw);
    function maj() {
      var L = E[mode]; et.innerHTML = '<b class="t">Étape ' + (k + 1) + ' sur ' + L.length + '&nbsp;: ' + L[k][0] + '</b>' + L[k][1]; typeset(et);
      pts.innerHTML = L.map(function (_, i) { return '<i class="' + (i < k ? 'fait' : (i === k ? 'cur' : '')) + '" data-k="' + i + '"></i>'; }).join('');
      bP.disabled = k === 0; bS.disabled = k === L.length - 1; a = RM ? 1 : 0; if (RM) { draw(cnv); } else { loop.kick(); }
    }
    bP.addEventListener('click', function () { if (k > 0) { k--; maj(); a = 1; draw(cnv); } });
    bS.addEventListener('click', function () { if (k < E[mode].length - 1) { k++; maj(); } });
    pts.addEventListener('click', function (ev) { var i = ev.target.getAttribute('data-k'); if (i !== null) { k = +i; maj(); } });
    $$(root, 'input[name="dv-m"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; k = 0; maj(); }); });
    maj();
  })();

  /* =================== 15 b. Du vecteur variation de vitesse à la somme des forces =================== */
  (function () {
    var root = document.getElementById('quiz-dv'); if (!root) { return; }
    var OPT = ['vertical, vers le bas', 'vertical, vers le haut', 'horizontal, dans le sens du mouvement', 'horizontal, dans le sens opposé au mouvement', 'dirigé vers le centre du cercle', 'nul'];
    function pts(type) {
      var P = [], i;
      if (type === 'ra') { for (i = 0; i < 5; i++) { P.push([40 + 30 * i + 9 * i * i, 105]); } }
      else if (type === 'rr') { for (i = 0; i < 5; i++) { var j2 = 4 - i; P.push([40 + 30 * 4 + 9 * 16 - 30 * j2 - 9 * j2 * j2, 105]); } }
      else if (type === 'ru') { for (i = 0; i < 5; i++) { P.push([50 + 75 * i, 105]); } }
      else if (type === 'up') { for (i = 0; i < 5; i++) { var j3 = 4 - i; P.push([210, 20 + 8 * j3 * j3 + 6 * j3]); } }   /* balle lancée vers le haut : positions de plus en plus rapprochées */
      else if (type === 'chute') { for (i = 0; i < 5; i++) { P.push([70 + 70 * i, 160 - 70 * i + 17 * i * i]); } }
      else { for (i = 0; i < 9; i++) { var a = -Math.PI * 0.95 + 2 * Math.PI * i / 10; P.push([210 + 75 * Math.cos(a), 100 + 75 * Math.sin(a)]); } }
      return P;
    }
    function svg(type) {
      var P = pts(type), h = '', M = P[1], Mp = P[2], Mpp = P[3], k = type === 'cercle' ? 1.55 : 0.62;   /* échelle des vitesses : les flèches ne joignent pas deux positions (vitesse et déplacement sont différents) */
      if (type === 'cercle') { h += "<circle cx='210' cy='100' r='75' fill='none' stroke='#3B82F6' stroke-dasharray='4 5' opacity='0.5'/><circle cx='210' cy='100' r='3' fill='#334155'/>"; }
      P.forEach(function (q, i) { var c = i === 1 || i === 2 ? '#1E3A8A' : '#E11D48'; h += "<path d='M" + (q[0] - 4.5) + ',' + (q[1] - 4.5) + ' L' + (q[0] + 4.5) + ',' + (q[1] + 4.5) + ' M' + (q[0] + 4.5) + ',' + (q[1] - 4.5) + ' L' + (q[0] - 4.5) + ',' + (q[1] + 4.5) + "' stroke='" + c + "' stroke-width='1.8' stroke-linecap='round'/>"; });
      function fl(x1, y1, x2, y2) { var d = Math.hypot(x2 - x1, y2 - y1); if (d < 1) { return ''; } var ux = (x2 - x1) / d, uy = (y2 - y1) / d; return "<line x1='" + x1 + "' y1='" + y1 + "' x2='" + (x2 - ux * 8).toFixed(1) + "' y2='" + (y2 - uy * 8).toFixed(1) + "' stroke='#FEAE00' stroke-width='2.6' stroke-linecap='round'/><polygon points='" + x2.toFixed(1) + ',' + y2.toFixed(1) + ' ' + (x2 - ux * 10 - uy * 4.5).toFixed(1) + ',' + (y2 - uy * 10 + ux * 4.5).toFixed(1) + ' ' + (x2 - ux * 10 + uy * 4.5).toFixed(1) + ',' + (y2 - uy * 10 - ux * 4.5).toFixed(1) + "' fill='#FEAE00'/>"; }
      h += fl(M[0], M[1], M[0] + (Mp[0] - M[0]) * k, M[1] + (Mp[1] - M[1]) * k) + fl(Mp[0], Mp[1], Mp[0] + (Mpp[0] - Mp[0]) * k, Mp[1] + (Mpp[1] - Mp[1]) * k);
      var lab = function (q, s, dx, dy) { return "<text x='" + (q[0] + dx) + "' y='" + (q[1] + dy) + "' font-size='14' fill='#1E3A8A' font-family='Georgia, serif'>" + s + '</text>'; };
      h += type === 'up' ? lab(M, 'M', 10, 5) + lab(Mp, 'M\u2032', 10, 5) : lab(M, 'M', -6, 20) + lab(Mp, 'M\u2032', -6, 20);
      h += "<text x='" + (P[0][0]) + "' y='" + (P[0][1] + (type === 'up' ? 18 : -10)) + "' font-size='11' fill='#64748B' text-anchor='middle' font-family='system-ui, sans-serif'>départ</text>";
      return "<svg class='nt-qsvg' viewBox='0 0 420 200' width='420' role='img' aria-label='chronophotographie avec les vecteurs vitesse en M et en M\u2032'>" + h + '</svg>';
    }
    var CAS = [
      ['ra', 2, 'Le mobile accélère en ligne droite&nbsp;: $\\vec{v}_{\\mathrm{M\'}}$ est plus long que $\\vec{v}_\\mathrm{M}$, dans la même direction. $\\overrightarrow{\\Delta v}$ est donc dans le sens du mouvement, comme la somme des forces&nbsp;: quelque chose pousse le mobile vers l\u2019avant.'],
      ['rr', 3, 'Le mobile ralentit&nbsp;: $\\vec{v}_{\\mathrm{M\'}}$ est plus court que $\\vec{v}_\\mathrm{M}$. $\\overrightarrow{\\Delta v}$ est opposé au mouvement, comme la somme des forces&nbsp;: c\u2019est un freinage.'],
      ['ru', 5, 'Positions également espacées sur une droite&nbsp;: les deux vecteurs vitesse sont égaux, $\\overrightarrow{\\Delta v} = \\vec{0}$. La somme des forces est nulle&nbsp;: les forces se compensent.'],
      ['up', 0, 'La balle monte en ralentissant&nbsp;: $\\vec{v}_{\\mathrm{M\'}}$ est plus court que $\\vec{v}_\\mathrm{M}$. $\\overrightarrow{\\Delta v}$ est vertical vers le bas, comme le poids&nbsp;: la balle monte, mais la somme des forces la tire vers le bas&nbsp;!'],
      ['chute', 0, 'En chute libre, seul le poids agit&nbsp;: $\\overrightarrow{\\Delta v}$ est vertical vers le bas, comme la somme des forces, alors même que la balle monte au début.'],
      ['cercle', 4, 'Mouvement circulaire uniforme&nbsp;: les vecteurs vitesse ont même longueur, mais pas même direction. $\\overrightarrow{\\Delta v}$, et donc la somme des forces, sont dirigés vers le centre du cercle.']
    ];
    function fab() {
      return shuffle(CAS.slice()).map(function (c) {
        var autres = shuffle(OPT.map(function (_, i) { return i; }).filter(function (i) { return i !== c[1]; })).slice(0, 3), ids = [c[1]].concat(autres);
        return ['Sur cette chronophotographie, à intervalles de temps égaux, on a tracé les vecteurs vitesse en M et en M\u2032 (avec une échelle des vitesses&nbsp;: leur longueur n\u2019est pas celle du déplacement). Le vecteur $\\overrightarrow{\\Delta v}$, et donc la somme des forces, est…' + svg(c[0]), ids.map(function (i) { return OPT[i]; }), c[2]];
      });
    }
    Quiz(root, null, 6, fab);
  })();

  /* =================== 15 c. Le canon de Newton =================== */
  (function () {
    var root = document.getElementById('lab-canon'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), GM = 398600, R = 6371, H0 = 400, ACC = 700, TR = [], cur = null, cnv;   /* km, km³·s⁻², accélération du temps */
    var COL = { 3: '#F97316', 6: '#EAB308', 7.67: '#22C55E', 8.5: '#38BDF8' };
    function tir(v) { cur = { v: v, x: 0, y: R + H0, vx: v, vy: 0, t: 0, pts: [[0, R + H0]], ang: 0, fin: false, col: COL[v] }; TR.push(cur); if (TR.length > 5) { TR.shift(); } }
    function avance(dt) {
      if (!cur || cur.fin) { return; } var h = 5, n = Math.ceil(dt * ACC / h);
      for (var i = 0; i < n; i++) {   /* intégration de Verlet : seule l'attraction de la Terre agit */
        var r = Math.hypot(cur.x, cur.y), ax = -GM * cur.x / (r * r * r), ay = -GM * cur.y / (r * r * r);
        cur.vx += ax * h / 2; cur.vy += ay * h / 2; cur.x += cur.vx * h; cur.y += cur.vy * h;
        r = Math.hypot(cur.x, cur.y); ax = -GM * cur.x / (r * r * r); ay = -GM * cur.y / (r * r * r); cur.vx += ax * h / 2; cur.vy += ay * h / 2; cur.t += h;
        var a = Math.atan2(cur.x, cur.y); if (a < 0) { a += 2 * Math.PI; } if (cur.pts.length > 3 && a < cur.ang - 3) { cur.tours = (cur.tours || 0) + 1; } cur.ang = a;
        if (r < R) { cur.fin = true; cur.sol = true; break; } if ((cur.tours || 0) >= 1) { cur.fin = true; break; }
      }
      cur.pts.push([cur.x, cur.y]);
      if (cur.fin) { fin(); }
    }
    function fin() {
      var v = cur.v;
      msg.innerHTML = v < 7 ? 'À ' + fmt(v, 0) + '&nbsp;km·s⁻¹, le boulet tombe et finit par toucher la Terre, d\u2019autant plus loin qu\u2019il est tiré vite.' :
        (v < 8 ? 'À 7,7&nbsp;km·s⁻¹, la vitesse de l\u2019ISS, le boulet tombe sans cesse… mais la surface de la Terre, qui est courbe, «&nbsp;se dérobe&nbsp;» sous lui aussi vite qu\u2019il tombe&nbsp;: il tourne en rond, en <b>chute libre permanente</b>. C\u2019est exactement ce que fait la station, et tout ce qu\u2019elle contient.' :
        'Plus vite encore, le boulet s\u2019éloigne davantage avant de revenir&nbsp;: sa trajectoire est une ellipse. Au-delà d\u2019environ 11&nbsp;km·s⁻¹, il quitterait la Terre pour toujours.');
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, k = Math.min(W, H) * 0.27 / R, cx = W / 2, cy = H * 0.36, X = function (x) { return cx + x * k; }, Y = function (y) { return cy - y * k; };
      ctx.clearRect(0, 0, W, H); var g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#020617'); g.addColorStop(1, '#0F172A'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      ETOILES.forEach(function (e) { ctx.fillStyle = 'rgba(255,255,255,' + e[2] * 0.8 + ')'; ctx.fillRect(e[0] * W, e[1] * H, 1.3, 1.3); });
      terreIcone(ctx, cx, cy, R * k);
      ctx.fillStyle = '#CBD5E1'; ctx.fillRect(cx - 1.5, Y(R + H0), 3, H0 * k); ctx.fillStyle = '#475569'; rr(ctx, cx - 7, Y(R + H0) - 5, 14, 7, 2); ctx.fill();   /* tour de 400 km et canon */
      TR.forEach(function (tr) { ctx.strokeStyle = tr.col; ctx.lineWidth = 2.6; ctx.globalAlpha = tr === cur ? 1 : 0.8; ctx.beginPath(); tr.pts.forEach(function (q, i) { if (i) { ctx.lineTo(X(q[0]), Y(q[1])); } else { ctx.moveTo(X(q[0]), Y(q[1])); } }); ctx.stroke(); ctx.globalAlpha = 1; });
      if (cur) {
        var bx = X(cur.x), by = Y(cur.y); ctx.fillStyle = '#F8FAFC'; ctx.beginPath(); ctx.arc(bx, by, 4.5, 0, 2 * Math.PI); ctx.fill();
        if (!cur.fin) { var r = Math.hypot(cur.x, cur.y); vec(ctx, bx, by, bx - cur.x / r * 30, by + cur.y / r * 30, FORCE, 2.4, 9); vec(ctx, bx, by, bx + cur.vx * 4, by - cur.vy * 4, ORANGE, 2.4, 9); }
      }
      pill(ctx, 'en rouge\u00A0: poids du boulet, toujours dirigé vers le centre de la Terre\u00A0; en orange\u00A0: sa vitesse', 10, H - 14, { size: 10.5, col: '#E2E8F0', bg: 'rgba(15,23,42,0.6)', align: 'left' });
    }
    var loop = Loop(root, function (dt) { if (!cur || cur.fin) { return false; } avance(Math.min(dt, 0.05)); draw(cnv); return !cur.fin; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 520 ? 330 : 400; }, draw);
    $$(root, '[data-v]').forEach(function (b) { b.addEventListener('click', function () { tir(+b.getAttribute('data-v')); msg.textContent = 'Feu\u00A0!'; if (RM) { while (!cur.fin) { avance(0.05); } draw(cnv); return; } loop.kick(); }); });
    $(root, '[data-act="effacer"]').addEventListener('click', function () { TR = []; cur = null; draw(cnv); msg.textContent = 'Choisissez une vitesse de tir.'; });
    msg.textContent = 'Le canon est au sommet d\u2019une tour imaginaire de 400\u00A0km, l\u2019altitude de l\u2019ISS. Choisissez une vitesse de tir.'; draw(cnv);
  })();

  /* =================== 16. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    Quiz(root, [
      ['Le principe d\u2019inertie affirme qu\u2019un système sur lequel les actions se compensent…', ['est immobile ou en mouvement rectiligne uniforme', 'est forcément immobile', 'ralentit peu à peu'], 'Il persévère dans son état&nbsp;: repos, ou mouvement rectiligne uniforme.'],
      ['Le vecteur vitesse d\u2019une voiture change de direction, à vitesse constante. Alors…', ['au moins une action non compensée s\u2019exerce sur elle', 'les actions se compensent', 'aucune action ne s\u2019exerce sur elle'], 'Contraposée du principe d\u2019inertie&nbsp;: vecteur vitesse non constant, donc action non compensée.'],
      ['Dans un DOI, l\u2019action de la Terre sur un système est représentée par…', ['une double flèche hachurée (action à distance)', 'une double flèche pleine (action de contact)', 'aucune flèche'], 'La Terre agit à distance, sans contact.'],
      ['Quel est le poids d\u2019un objet de 2&nbsp;kg sur Terre ($g = \\pu{9,8 N*kg-1}$)&nbsp;?', ['19,6 N', '2 N', '0,2 N'], '$P = m \\times g = 2 \\times 9{,}8 = \\pu{19,6 N}$.'],
      ['La masse d\u2019un astronaute sur la Lune est…', ['la même que sur Terre', 'six fois plus petite que sur Terre', 'nulle'], 'La masse ne dépend pas du lieu&nbsp;; c\u2019est le poids qui change.'],
      ['Un ourson pousse une voiture avec une force de 3&nbsp;N. La voiture pousse l\u2019ourson avec une force de…', ['3 N, de sens opposé', '0 N', 'moins de 3 N, car la voiture est plus lourde'], 'Principe des actions réciproques&nbsp;: même intensité, sens opposé.'],
      ['Si l\u2019on double la distance entre deux astres, la force d\u2019attraction gravitationnelle est…', ['divisée par 4', 'divisée par 2', 'multipliée par 2'], 'Elle est inversement proportionnelle au carré de la distance.'],
      ['La Terre attire la Lune avec une force $F$. La Lune attire la Terre avec une force…', ['de même intensité <i><b>F</b></i>', '81 fois plus petite', '81 fois plus grande'], 'Actions réciproques&nbsp;: même intensité, quelles que soient les masses.'],
      ['À bord de l\u2019ISS, à 400&nbsp;km d\u2019altitude, l\u2019intensité de la pesanteur vaut environ…', ['8,7 N·kg⁻¹', '0 N·kg⁻¹', '98 N·kg⁻¹'], 'Presque autant qu\u2019au sol&nbsp;: les astronautes flottent parce qu\u2019ils sont en chute libre avec la station.'],
      ['Dans le vide, une plume et une boule de bowling lâchées ensemble…', ['touchent le sol en même temps', 'la boule arrive bien avant', 'la plume flotte'], 'La chute libre ne dépend pas de la masse.'],
      ['En chute libre, le vecteur variation de vitesse $\\overrightarrow{\\Delta v}$ est…', ['vertical, vers le bas', 'dans le sens du mouvement', 'nul'], 'Il a la direction et le sens de la somme des forces, ici le poids.'],
      ['Une balle lâchée par un cycliste qui roule à vitesse constante tombe…', ['à côté du cycliste, qui avance avec elle', 'loin derrière le cycliste', 'devant le cycliste'], 'Elle conserve sa vitesse horizontale&nbsp;: horizontalement, elle avance comme le cycliste.']
    ], 12);
  })();

})();
</script>
