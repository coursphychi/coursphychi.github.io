+++
title = "Réaction chimique"
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
.nt-eq-w { text-align: center; margin: 0.9em 0; }
.nt-eq { display: inline-block; margin: 0; padding: 0.5em 1.4em; border-radius: 14px; background: linear-gradient(135deg, #FFF1F2, #FFE4E6); border: 2px solid #FDA4AF; font-size: 1.05em; text-align: center; }
.nt-endo { color: #1D4ED8; font-weight: 700; } .nt-exo { color: #DC2626; font-weight: 700; }
.nt-video { margin: 1em auto; max-width: 640px; } .nt-video video { width: 100%; border-radius: 14px; box-shadow: 0 6px 20px rgba(15,23,42,0.18); }
.nt-aj-eq { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.35em 0.5em; font-size: 1.12em; margin: 0.8em 0; }
.nt-aj-t { display: inline-flex; align-items: center; gap: 0.15em; }
.nt-aj-c { display: inline-flex; flex-direction: column; align-items: center; line-height: 1; }
.nt-aj-c b { color: #DB2777; font-size: 1.15em; min-width: 1.2em; text-align: center; }
.nt-aj-c button { border: 1px solid var(--line); background: #FFFFFF; color: var(--navy); border-radius: 6px; font-size: 0.62em; padding: 0.1em 0.45em; cursor: pointer; }
.nt-aj-c button:hover { background: #FCE7F3; border-color: #F9A8D4; }
.nt-aj-plus, .nt-aj-fl { color: #64748B; }
.nt-aj-tab { margin: 0.4em auto; font-size: 0.95em; } .nt-aj-tab tr.ok td { color: #15803D; } .nt-aj-tab tr.ko td { color: #B91C1C; }
.nt-ctrl-inline { display: inline-flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.3em; max-width: 100%; }
.nt-ctrl-inline select { margin-left: 0.4em; padding: 0.35em 0.6em; border-radius: 10px; border: 1.5px solid var(--line); background: #FFFFFF; font: inherit; color: var(--navy); max-width: 100%; }
.nt-aj-t { flex-direction: column; } .nt-aj-tl { display: inline-flex; align-items: center; gap: 0.15em; } .nt-aj-mol { display: block; margin: 0.2em auto 0; }
.nt-h4 { color: var(--navy); font-size: 1.08em; margin: 1.5em 0 0.5em; }
.nt-geant { display: block; text-align: center; font-family: Georgia, "Times New Roman", serif; font-size: clamp(1.1em, 4.2vw, 2.2em); color: #C2410C; letter-spacing: 0.04em; margin: 0.4em 0; overflow-wrap: anywhere; }
.nt-etapes-calc p { margin: 0.35em 0 !important; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Le vinaigre qui mousse au contact du bicarbonate, le gaz qui brûle dans une gazinière, le métal qui disparaît dans un acide… Au cours d'une transformation chimique, des espèces chimiques disparaissent et d'autres apparaissent. Ce chapitre montre comment la modéliser par une <b>réaction chimique</b>, comment écrire et ajuster son <b>équation</b>, comment prévoir quel réactif sera épuisé le premier, et quels effets thermiques l'accompagnent.</p>

## Transformation chimique et réaction chimique {.nt-h2}

### Reconnaître une transformation chimique {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp nt-hole">transformation chimique</span> est une transformation au cours de laquelle des espèces chimiques sont <span class="imp nt-hole">consommées</span> et d'autres sont <span class="imp nt-hole">produites</span>.</p>
</div>

<p>Contrairement à une transformation physique (changement d'état, dissolution…), où les espèces chimiques restent les mêmes, une transformation chimique fait apparaître de <b>nouvelles espèces</b>. Plusieurs indices permettent de la repérer&nbsp;:</p>

<ul class="nt-facts">
<li>un changement de couleur&nbsp;;</li>
<li>l'apparition ou la disparition d'un solide&nbsp;;</li>
<li>un dégagement gazeux&nbsp;;</li>
<li>un dégagement ou une absorption d'énergie thermique (le milieu chauffe ou refroidit)&nbsp;;</li>
<li>l'apparition d'une odeur, la modification de l'acidité…</li>
</ul>

<p>Pour confirmer qu'une nouvelle espèce est apparue, on l'identifie par un <b>test chimique</b>. Rappel des tests des gaz courants&nbsp;:</p>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>gaz</th><th>test</th><th>résultat positif</th></tr></thead>
<tbody>
<tr><td>dioxyde de carbone $\ce{CO2}$</td><td>on fait barboter le gaz dans l'eau de chaux</td><td>l'eau de chaux se trouble</td></tr>
<tr><td>dihydrogène $\ce{H2}$</td><td>on approche une flamme de l'ouverture du tube</td><td>une légère détonation («&nbsp;aboiement&nbsp;»)</td></tr>
<tr><td>dioxygène $\ce{O2}$</td><td>on introduit une bûchette incandescente</td><td>la bûchette se rallume</td></tr>
<tr><td>ion cuivre $\ce{Cu^2+}$</td><td>on ajoute quelques gouttes de soude (solution d'hydroxyde de sodium)</td><td>un précipité bleu se forme</td></tr>
<tr><td>ion argent $\ce{Ag+}$</td><td>on ajoute quelques gouttes d'une solution contenant des ions chlorure (eau salée)</td><td>un précipité blanc se forme, qui noircit à la lumière</td></tr>
</tbody>
</table></div>

### Système chimique, réactifs et produits {.nt-h3}

<p>Pour décrire une transformation chimique, on étudie un <b>système chimique</b>&nbsp;: l'ensemble des espèces chimiques présentes dans le récipient. On décrit sa composition (la nature et la quantité de matière de chaque espèce) dans l'<b>état initial</b>, avant la transformation, et dans l'<b>état final</b>, quand elle est terminée.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<ul class="nt-facts">
<li>Les <span class="imp nt-hole">réactifs</span> sont les espèces chimiques dont la quantité de matière <b>diminue</b> au cours de la transformation.</li>
<li>Les <span class="imp nt-hole">produits</span> sont les espèces chimiques dont la quantité de matière <b>augmente</b>.</li>
<li>Une <span class="imp nt-hole">espèce spectatrice</span> est présente dans le système, mais sa quantité de matière <b>ne varie pas</b>&nbsp;: elle ne participe pas à la transformation.</li>
</ul>
</div>

<p>On les distingue en comparant l'état initial et l'état final&nbsp;: c'est un travail d'enquête, d'abord qualitatif (quelles espèces ont disparu, lesquelles sont apparues&nbsp;?), puis quantitatif (dans quelles proportions&nbsp;?). La partie 2.3 en donne un exemple complet. Les espèces spectatrices sont souvent le solvant (l'eau) et les ions qui accompagnent les espèces qui réagissent.</p>

<div class="nt-lab nt-quizlab" id="tr-especes">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Réactif, produit ou espèce spectatrice&nbsp;?</p>
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

### La réaction chimique et son équation {.nt-h3}

<p>Une transformation chimique réelle est souvent complexe. On la <b>modélise</b> par une <span class="imp">réaction chimique</span>, qui ne retient que l'essentiel&nbsp;: quels réactifs disparaissent, quels produits apparaissent, et dans quelles proportions. On l'écrit sous la forme d'une <span class="imp">équation de réaction</span>&nbsp;:</p>

<div class="nt-eq-w"><span class="nt-eq">réactifs $\longrightarrow$ produits</span></div>

<p>Par exemple, pour le magnésium dans l'acide chlorhydrique&nbsp;:</p>

$$\ce{Mg (s) + {\color{#DB2777}2} H3O+ (aq) -> Mg^2+ (aq) + H2 (g) + {\color{#DB2777}2} H2O (\ell)}$$

<ul class="nt-facts">
<li>Les réactifs sont à gauche de la flèche, les produits à droite. On précise l'état de chaque espèce&nbsp;: (s), ($\ell$), (g), ou (aq) pour une espèce dissoute dans l'eau.</li>
<li>Les espèces spectatrices (ici les ions chlorure $\ce{Cl-}$) <b>n'apparaissent pas</b> dans l'équation.</li>
<li>Les nombres placés devant les formules sont les <span class="imp">coefficients stœchiométriques</span>. Le coefficient 1 n'est pas écrit.</li>
</ul>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Une équation est un bilan macroscopique</p>
<p>L'équation de réaction ne décrit pas ce qui se passe à l'échelle des atomes&nbsp;: c'est un <b>bilan</b>, établi à partir de quantités de matière mesurées à notre échelle. On ne dit donc pas «&nbsp;un atome de magnésium réagit avec deux ions oxonium&nbsp;», mais «&nbsp;<b>une mole</b> de magnésium réagit avec <b>deux moles</b> d'ions oxonium&nbsp;».</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: ajuster une équation</p>
<p>Au cours d'une réaction chimique, les atomes ne sont ni créés ni détruits&nbsp;: ils se réarrangent. Une équation de réaction doit donc respecter deux lois de conservation&nbsp;:</p>
<ul class="nt-facts">
<li>la <span class="imp nt-hole">conservation des éléments</span>&nbsp;: chaque élément est présent en même nombre dans les réactifs et dans les produits&nbsp;;</li>
<li>la <span class="imp nt-hole">conservation de la charge</span>&nbsp;: la charge électrique totale est la même dans les réactifs et dans les produits.</li>
</ul>
<p><b>Ajuster</b> une équation, c'est choisir les coefficients stœchiométriques, les plus petits entiers possibles, pour que ces deux lois soient respectées.</p>
</div>

<p>Vérifions sur l'exemple du magnésium&nbsp;:</p>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th></th><th>réactifs</th><th>produits</th></tr></thead>
<tbody>
<tr><td>magnésium Mg</td><td>1</td><td>1</td></tr>
<tr><td>hydrogène H</td><td>$2 \times 3 = 6$</td><td>$2 + 2 \times 2 = 6$</td></tr>
<tr><td>oxygène O</td><td>$2 \times 1 = 2$</td><td>$2 \times 1 = 2$</td></tr>
<tr><td>charge</td><td>$2 \times (+1) = +2$</td><td>$+2$</td></tr>
</tbody>
</table></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode&nbsp;: ajuster une équation</p>
<ol class="nt-steps">
<li><p>Écrire les formules des réactifs et des produits, sans jamais les modifier.</p></li>
<li><p>Ajuster un élément après l'autre, en commençant par ceux qui n'apparaissent que dans une espèce de chaque côté, et en gardant pour la fin les éléments présents seuls (comme $\ce{O2}$ ou $\ce{H2}$).</p></li>
<li><p>Vérifier la conservation de chaque élément, puis celle de la charge. Si un coefficient est fractionnaire, multiplier tous les coefficients pour obtenir des entiers.</p></li>
</ol>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Erreur classique</p>
<p>On ne modifie <b>jamais</b> les indices d'une formule pour ajuster une équation&nbsp;: $\ce{H2O}$ et $\ce{H2O2}$ sont deux espèces chimiques différentes&nbsp;! On ne joue que sur les coefficients placés devant les formules.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>En solution aqueuse, l'ion hydrogène $\ce{H+ (aq)}$ n'existe pas seul&nbsp;: il est toujours lié à une molécule d'eau, sous forme d'ion oxonium $\ce{H3O+ (aq)}$. Les deux écritures sont utilisées pour simplifier ou préciser les équations.</p>
</div>

<p>Pour vérifier qu'une équation est ajustée, il est commode de compter les atomes de chaque élément. L'outil ci-dessous dessine pour cela les entités en relief, en autant d'exemplaires que l'indique chaque coefficient.</p>

<div class="nt-lab" id="lab-ajuster">
<p class="nt-tag"><i class="fa-solid fa-scale-balanced"></i>Entraînement</p>
<p class="nt-lab-title">Ajuster une équation de réaction</p>
<div class="nt-btns"><label class="nt-ctrl-inline">Équation&nbsp;: <select data-in="eq"></select></label></div>
<div class="nt-ajust" aria-live="polite"></div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="sol"><i class="fa-solid fa-eye"></i>&nbsp; Voir la solution</button><button type="button" class="nt-btn" data-act="suivante"><i class="fa-solid fa-forward"></i>&nbsp; Équation suivante</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p class="nt-note">Ce dessin ne sert qu'à compter les atomes&nbsp;: il ne représente pas le déroulement de la réaction. Les entités ne se rencontrent presque jamais ainsi, par petits groupes, à l'échelle microscopique&nbsp;; l'équation est un bilan à l'échelle macroscopique. Pour les solides ioniques ($\ce{CaCO3}$, $\ce{Fe2O3}$), on a dessiné un «&nbsp;motif&nbsp;» du cristal, qui en compte des milliards de milliards.</p>

## Stœchiométrie et réactif limitant {.nt-h2}

### Lire une équation de réaction {.nt-h3}

<p>Les coefficients stœchiométriques indiquent dans quelles <b>proportions</b> les réactifs sont consommés et les produits formés. L'équation</p>

$$\ce{CH4 (g) + 2 O2 (g) -> CO2 (g) + 2 H2O (g)}$$

<p>se lit ainsi&nbsp;: <b>une</b> mole de méthane réagit avec <b>deux</b> moles de dioxygène pour former <b>une</b> mole de dioxyde de carbone et <b>deux</b> moles d'eau. Ces proportions restent vraies pour n'importe quelle quantité&nbsp;: 3&nbsp;mol de méthane réagissent avec 6&nbsp;mol de dioxygène, 0,5&nbsp;mol avec 1&nbsp;mol… Les quantités de matière consommées et formées sont <b>proportionnelles</b> aux coefficients stœchiométriques.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Des réactifs sont introduits dans les <span class="imp nt-hole">proportions stœchiométriques</span> lorsque leurs quantités de matière initiales sont dans le même rapport que leurs coefficients stœchiométriques. Pour une réaction $a\,\text{A} + b\,\text{B} \longrightarrow \ldots$, cela s'écrit&nbsp;:</p>
<p style="text-align:center">$\dfrac{n_\text{A,i}}{a} = \dfrac{n_\text{B,i}}{b}$</p>
</div>

### Le réactif limitant {.nt-h3}

<p>Dans une transformation <b>totale</b>, la transformation s'arrête dès qu'un des réactifs est entièrement consommé&nbsp;: il ne peut plus réagir, faute de partenaire.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp nt-hole">réactif limitant</span> est le réactif qui est <b>entièrement consommé</b> à la fin d'une transformation totale&nbsp;: c'est lui qui arrête la transformation. Les autres réactifs, encore présents dans l'état final, sont dits <b>en excès</b>.</p>
<p>Si les réactifs sont introduits dans les proportions stœchiométriques, ils sont tous entièrement consommés&nbsp;: ils sont tous limitants.</p>
</div>

<div class="nt-lab" id="lab-limitant">
<p class="nt-tag"><i class="fa-solid fa-chart-column"></i>Animation</p>
<p class="nt-lab-title">Qui sera épuisé le premier&nbsp;?</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="lim-r" value="ch4" checked><span>Combustion du méthane</span></label><label><input type="radio" name="lim-r" value="nh3"><span>Synthèse de l'ammoniac</span></label><label><input type="radio" name="lim-r" value="cu"><span>Cuivre et ions argent</span></label></div></div>
<p class="nt-center nt-lim-eq"></p>
<div class="nt-ctrls">
<label class="nt-ctrl"><span class="nt-lim-l1"></span>&nbsp;: <b class="out-a"></b><input type="range" min="0" max="6" step="0.5" value="3" data-in="a"></label>
<label class="nt-ctrl"><span class="nt-lim-l2"></span>&nbsp;: <b class="out-b"></b><input type="range" min="0" max="9" step="0.5" value="4" data-in="b"></label>
</div>
<canvas role="img" aria-label="Les quantités de matière de chaque espèce, représentées par des piles de blocs d'une mole ; au cours de la transformation, les réactifs diminuent et les produits augmentent, dans les proportions de l'équation, jusqu'à l'épuisement d'un réactif."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Lancer la transformation</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>On peut déterminer le réactif limitant de deux façons.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode 1&nbsp;: à partir de l'état final</p>
<p>On identifie les espèces chimiques présentes dans l'état final (par un test, un indicateur coloré, l'observation d'un solide restant…). Le réactif qui a <b>totalement disparu</b> est le réactif limitant.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode 2&nbsp;: à partir des quantités initiales</p>
<p>Pour une réaction $a\,\text{A} + b\,\text{B} \longrightarrow \ldots$, on compare les quotients $\dfrac{n_\text{A,i}}{a}$ et $\dfrac{n_\text{B,i}}{b}$&nbsp;: le réactif limitant est celui qui a le <b>plus petit quotient</b>. Si les deux quotients sont égaux, les réactifs sont dans les proportions stœchiométriques.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>On mélange 1,0&nbsp;mol de méthane et 1,5&nbsp;mol de dioxygène. Quel est le réactif limitant de la combustion $\ce{CH4 + 2 O2 -> CO2 + 2 H2O}$&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Le dioxygène</span></summary>
<div class="nt-d-body">
<p>$\dfrac{n_{\ce{CH4},\text{i}}}{1} = \pu{1,0 mol}$ et $\dfrac{n_{\ce{O2},\text{i}}}{2} = \pu{0,75 mol}$. Le plus petit quotient est celui du dioxygène&nbsp;: c'est le réactif limitant.</p>
<p>Autrement dit&nbsp;: pour brûler 1,0&nbsp;mol de méthane, il faudrait 2,0&nbsp;mol de dioxygène. On n'en a que 1,5&nbsp;mol&nbsp;: le dioxygène sera épuisé avant le méthane.</p>
</div>
</details>

<div class="nt-lab nt-quizlab" id="tr-limitant">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Trouver le réactif limitant</p>
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

### Exemple&nbsp;: du cuivre dans une solution de nitrate d'argent {.nt-h3}

<p>Voici, sur un exemple, toute la démarche qui mène des observations à l'équation de réaction.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-flask"></i>Expérience</p>
<p>On plonge un morceau de cuivre $\ce{Cu (s)}$ dans 50&nbsp;mL d'une solution incolore de nitrate d'argent, qui contient des ions argent $\ce{Ag+ (aq)}$ et des ions nitrate $\ce{NO3- (aq)}$. On réalise trois transformations, avec la même solution et trois masses de cuivre&nbsp;: 0,23&nbsp;g, 0,43&nbsp;g et 3,0&nbsp;g.</p>
</div>

<div class="nt-lab" id="lab-enquete">
<p class="nt-tag"><i class="fa-solid fa-magnifying-glass"></i>Animation</p>
<p class="nt-lab-title">L'enquête&nbsp;: que s'est-il passé dans les béchers&nbsp;?</p>
<canvas role="img" aria-label="Trois béchers de nitrate d'argent dans lesquels on plonge 0,23 g, 0,43 g et 3,0 g de cuivre ; à l'état final, la solution est bleutée et un solide gris brillant est apparu ; on peut ensuite réaliser des tests d'identification dans des tubes à essai."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Plonger le cuivre</button><button type="button" class="nt-btn" data-act="soude" disabled><i class="fa-solid fa-vial"></i>&nbsp; Test à la soude</button><button type="button" class="nt-btn" data-act="chlorure" disabled><i class="fa-solid fa-vial"></i>&nbsp; Test aux ions chlorure</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Étape 1&nbsp;: quelles espèces sont présentes dans l'état final&nbsp;?</p>
<p>Interprétez la couleur bleue, le solide gris brillant, et les résultats des deux tests.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Des ions cuivre et de l'argent sont apparus</span></summary>
<div class="nt-d-body">
<p>La couleur bleue est due aux <b>ions cuivre</b> $\ce{Cu^2+ (aq)}$, ce que confirme le précipité bleu obtenu avec la soude. Le solide gris brillant est de l'<b>argent</b> $\ce{Ag (s)}$. Le test aux ions chlorure montre qu'il reste des ions argent dans les béchers 1 et 2, mais plus dans le bécher 3.</p>
<div class="nt-scroll"><table class="nt-t">
<thead><tr><th></th><th>bécher 1 (0,23&nbsp;g)</th><th>bécher 2 (0,43&nbsp;g)</th><th>bécher 3 (3,0&nbsp;g)</th></tr></thead>
<tbody>
<tr><td>état final</td><td>eau, ions nitrate, ions argent, ions cuivre, argent</td><td>eau, ions nitrate, ions argent, ions cuivre, argent</td><td>eau, ions nitrate, ions cuivre, argent, <b>cuivre</b></td></tr>
</tbody>
</table></div>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Étape 2&nbsp;: réactifs, produits ou espèces spectatrices&nbsp;?</p>
<p>On sait aussi que la quantité d'ions argent diminue dans les trois béchers. Classez les espèces chimiques.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Deux réactifs, deux produits, deux espèces spectatrices</span></summary>
<div class="nt-d-body">
<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>réactifs</th><th>produits</th><th>espèces spectatrices</th></tr></thead>
<tbody><tr><td>cuivre $\ce{Cu (s)}$, ions argent $\ce{Ag+ (aq)}$</td><td>ions cuivre $\ce{Cu^2+ (aq)}$, argent $\ce{Ag (s)}$</td><td>eau, ions nitrate $\ce{NO3- (aq)}$</td></tr></tbody>
</table></div>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Étape 3&nbsp;: quel est le réactif limitant de chaque transformation&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Le cuivre, puis les ions argent</span></summary>
<div class="nt-d-body">
<p>Dans les béchers 1 et 2, le cuivre a entièrement disparu, alors qu'il reste des ions argent&nbsp;: le <b>cuivre</b> est le réactif limitant. Dans le bécher 3, il reste du cuivre, mais plus d'ions argent&nbsp;: ce sont les <b>ions argent</b> qui sont limitants.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Étape 4&nbsp;: dans quelles proportions&nbsp;?</p>
<p>Dans le bécher 1, les 0,23&nbsp;g de cuivre ont réagi, et une pesée montre qu'il s'est formé 0,76&nbsp;g d'argent. Comparez les quantités de matière de cuivre consommé et d'argent formé.</p>
<p>Données&nbsp;: masse d'un atome de cuivre&nbsp;: $\pu{1,1E-22 g}$&nbsp;; masse d'un atome d'argent&nbsp;: $\pu{1,8E-22 g}$.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Deux fois plus d'argent formé que de cuivre consommé</span></summary>
<div class="nt-d-body">
<p>$n_\text{Cu consommé} = \dfrac{\pu{0,23 g}}{\pu{1,1E-22 g} \times \pu{6,02E23 mol-1}} \approx \pu{3,5 mmol}$ et $n_\text{Ag formé} = \dfrac{\pu{0,76 g}}{\pu{1,8E-22 g} \times \pu{6,02E23 mol-1}} \approx \pu{7,0 mmol}$.</p>
<p>On constate que $n_\text{Ag formé} = 2 \times n_\text{Cu consommé}$&nbsp;: <b>une mole</b> de cuivre consommée produit <b>deux moles</b> d'argent.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Étape 5&nbsp;: l'équation de la réaction</p>
<p>Écrivez l'équation de la réaction qui modélise les trois transformations, sans les espèces spectatrices.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Une équation pour trois transformations</span></summary>
<div class="nt-d-body">
$$\ce{Cu (s) + 2 Ag+ (aq) -> Cu^2+ (aq) + 2 Ag (s)}$$
<p>Le coefficient 2 devant l'argent traduit la proportion trouvée à l'étape 4. Pour conserver l'élément argent, il faut aussi 2 devant les ions argent. La charge est conservée&nbsp;: $2 \times (+1) = +2$ de chaque côté.</p>
</div>
</details>

### D'autres exemples {.nt-h3}


<h4 class="nt-h4">Le bicarbonate de soude dans le vinaigre</h4>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-flask"></i>Expérience</p>
<p>Dans six erlenmeyers contenant chacun 100&nbsp;mL de vinaigre (une solution d'acide éthanoïque $\ce{CH3COOH}$ à 5&nbsp;% en masse), on verse des masses croissantes d'hydrogénocarbonate de sodium $\ce{NaHCO3}$ (le bicarbonate de soude)&nbsp;: 2,0&nbsp;g, 4,0&nbsp;g… jusqu'à 12,0&nbsp;g. Un ballon de baudruche, fixé sur chaque erlenmeyer, recueille le gaz produit.</p>
</div>


<p>Le gaz produit trouble l'eau de chaux&nbsp;: c'est du dioxyde de carbone. Les solutions 1 à 3 sont de moins en moins acides, et les solutions 4 à 6 ne sont plus acides du tout. La transformation est modélisée par la réaction d'équation&nbsp;:</p>

$$\ce{NaHCO3 (s) + CH3COOH (aq) -> CO2 (g) + Na+ (aq) + CH3COO- (aq) + H2O (\ell)}$$

<div class="nt-lab" id="lab-ballons1">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Animation</p>
<p class="nt-lab-title">Six ballons, deux réactifs limitants</p>
<canvas role="img" aria-label="Six erlenmeyers surmontés de ballons de plus en plus gonflés, jusqu'au quatrième ; les trois derniers ont la même taille. Sous chacun, les quantités de matière des réactifs, et le réactif limitant."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Verser le bicarbonate</button><label class="nt-check"><input type="checkbox" data-in="qte" checked> Quantités de matière</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-calculator"></i>Calcul</span><span class="nt-sum">Les quantités de matière des réactifs</span></summary>
<div class="nt-d-body">
<p><b>Données&nbsp;:</b> masse d'une entité $\ce{NaHCO3}$&nbsp;: $\pu{1,4E-22 g}$&nbsp;; masse d'une molécule $\ce{CH3COOH}$&nbsp;: $\pu{1,0E-22 g}$&nbsp;; la masse volumique du vinaigre est proche de celle de l'eau.</p>
<p><b>Hydrogénocarbonate de sodium</b>, pour 2,0&nbsp;g&nbsp;: $N = \dfrac{\pu{2,0 g}}{\pu{1,4E-22 g}} \approx \pu{1,4E22}$ entités, soit $n = \dfrac{\pu{1,4E22}}{\pu{6,02E23 mol-1}} \approx \pu{24 mmol}$. De même, on trouve 47, 71, 95, 120 et 140&nbsp;mmol pour 4,0&nbsp;g, 6,0&nbsp;g, 8,0&nbsp;g, 10,0&nbsp;g et 12,0&nbsp;g.</p>
<p><b>Acide éthanoïque</b>&nbsp;: 100&nbsp;mL de vinaigre ont une masse d'environ 100&nbsp;g, dont 5&nbsp;% d'acide éthanoïque, soit 5,0&nbsp;g. Cela représente $N = \dfrac{\pu{5,0 g}}{\pu{1,0E-22 g}} = \pu{5,0E22}$ molécules, soit $n \approx \pu{83 mmol}$.</p>
<p>Les coefficients stœchiométriques valant tous 1, le réactif limitant est celui qui a la plus petite quantité de matière&nbsp;: le bicarbonate dans les erlenmeyers 1 à 3, l'acide éthanoïque dans les erlenmeyers 4 à 6. On retrouve ce que montrent les ballons&nbsp;: la quantité de dioxyde de carbone formée est égale à la quantité de matière du réactif limitant.</p>
</div>
</details>

<h4 class="nt-h4">Le magnésium dans l'acide chlorhydrique</h4>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-flask"></i>Expérience</p>
<p>Dans quatre erlenmeyers contenant chacun 100&nbsp;mmol d'ions oxonium $\ce{H3O+}$ (de l'acide chlorhydrique), on verse 13, 25, 50 et 100&nbsp;mmol de magnésium en poudre. On ajoute quelques gouttes de bleu de bromothymol (BBT), un indicateur coloré <b>jaune</b> en présence d'ions oxonium et <b>vert ou bleu</b> sinon. Le gaz recueilli dans les ballons est du dihydrogène.</p>
</div>


<div class="nt-lab" id="lab-ballons2">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Animation</p>
<p class="nt-lab-title">Le BBT désigne le réactif limitant</p>
<canvas role="img" aria-label="Quatre erlenmeyers : les deux premiers restent jaunes et sans magnésium, le troisième devient vert, sans magnésium, le quatrième devient vert et garde du magnésium au fond."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Verser le magnésium</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>À partir de l'état final de chaque erlenmeyer, déterminer le réactif limitant. Que dire de l'erlenmeyer&nbsp;3&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Le magnésium, puis l'ion oxonium… et les deux à la fois</span></summary>
<div class="nt-d-body">
<p>Dans les erlenmeyers 1 et 2, le BBT reste jaune&nbsp;: il reste des ions oxonium, et il n'y a plus de magnésium. Le magnésium est limitant. Dans l'erlenmeyer 4, le BBT est vert et il reste du magnésium&nbsp;: l'ion oxonium est limitant.</p>
<p>Dans l'erlenmeyer 3, il ne reste ni magnésium ni ions oxonium&nbsp;: les deux réactifs ont été entièrement consommés, ils sont tous les deux limitants. Ils ont été introduits dans les <b>proportions stœchiométriques</b>&nbsp;: $\dfrac{\pu{50 mmol}}{1} = \dfrac{\pu{100 mmol}}{2}$.</p>
<p>Les ballons contiennent 13, 25, 50 et 50&nbsp;mmol de dihydrogène&nbsp;: autant que de magnésium consommé, et deux fois moins que d'ions oxonium consommés. C'est ce que traduisent les coefficients de l'équation $\ce{Mg (s) + 2 H3O+ (aq) -> Mg^2+ (aq) + H2 (g) + 2 H2O (\ell)}$. Les ions chlorure, eux, sont restés en même quantité&nbsp;: ce sont des espèces spectatrices.</p>
</div>
</details>

## Effets thermiques des transformations {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Une transformation est <span class="imp nt-hole">exothermique</span> si elle <b>libère</b> de l'énergie thermique&nbsp;: elle réchauffe son environnement.</p>
<p>Une transformation est <span class="imp nt-hole">endothermique</span> si elle <b>prend</b> de l'énergie thermique à son environnement&nbsp;: elle le refroidit.</p>
<p>Si la température ne varie pas au cours de la transformation, celle-ci est dite <span class="imp nt-hole">athermique</span>.</p>
</div>

<div class="nt-scroll"><table class="nt-t nt-t-egal">
<thead><tr><th>transformations chimiques exothermiques</th><th>transformations chimiques endothermiques</th></tr></thead>
<tbody>
<tr><td>les combustions (gaz de la gazinière, bois, essence…)</td><td>la réaction du bicarbonate de soude avec le vinaigre</td></tr>
<tr><td>la réaction d'un métal (magnésium, zinc…) avec un acide</td><td>la photosynthèse, qui consomme l'énergie de la lumière</td></tr>
<tr><td>la réaction entre un acide et une base (acide chlorhydrique et soude)</td><td>la décomposition du calcaire en chaux, dans les fours à chaux</td></tr>
<tr><td>l'oxydation de la poudre de fer dans les chaufferettes jetables</td><td>la réaction de l'acide citrique avec le bicarbonate, dans les comprimés effervescents</td></tr>
</tbody>
</table></div>

<p>Plus la quantité de réactif limitant est grande, plus la quantité de produits formés est grande… et plus l'énergie libérée ou absorbée est grande&nbsp;: <b>la variation de température est d'autant plus grande que la quantité de réactif limitant est grande</b>.</p>

<div class="nt-lab" id="lab-thermo">
<p class="nt-tag"><i class="fa-solid fa-temperature-half"></i>Animation</p>
<p class="nt-lab-title">Suivre la température d'une transformation</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="th-r" value="mg" checked><span>Magnésium + acide chlorhydrique</span></label><label><input type="radio" name="th-r" value="bic"><span>Bicarbonate + vinaigre</span></label></div></div>
<div class="nt-ctrls"><label class="nt-ctrl"><span class="nt-th-l"></span>&nbsp;: <b class="out-m"></b><input type="range" min="1" max="5" step="1" value="2" data-in="m"></label></div>
<canvas role="img" aria-label="Un thermomètre plongé dans le mélange et la courbe de la température au cours du temps, pour différentes masses de réactif limitant."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Mélanger</button><button type="button" class="nt-btn" data-act="clear"><i class="fa-solid fa-eraser"></i>&nbsp; Effacer les courbes</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Les transformations physiques aussi</p>
<p>Les effets thermiques ne sont pas réservés aux transformations chimiques&nbsp;: les changements d'état (voir le chapitre correspondant) et les dissolutions peuvent aussi être exothermiques ou endothermiques. La dissolution du nitrate d'ammonium dans l'eau, par exemple, est très endothermique&nbsp;: elle est utilisée dans les poches de froid instantané. Celle de l'hydroxyde de sodium est au contraire très exothermique.</p>
</div>



## Testez-vous {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-final">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur la réaction chimique</p>
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
        typeset(bx);   /* les réponses peuvent contenir des formules */
        typeset(qEl);
      },
      bilan: function (g) { qEl.innerHTML = '<span class="nt-big-score">' + g + '&nbsp;/&nbsp;' + nb + '</span><br>' + (g / nb >= 0.85 ? 'Excellent&nbsp;!' : 'Relisez les explications des questions manquées, puis recommencez&nbsp;: les questions seront mélangées.'); bx.innerHTML = ''; bx.hidden = true; }
    });
    S.start();
  }
  function becher(ctx, x, y, w, h, avant) {   /* bécher en verre : avant = true pour le fond, false pour les reflets et le contour (dessinés par-dessus le contenu) */
    if (avant) { ctx.fillStyle = 'rgba(224,242,254,0.35)'; rr(ctx, x, y, w, h, 8); ctx.fill(); ctx.fillStyle = 'rgba(15,23,42,0.10)'; ctx.beginPath(); ctx.ellipse(x + w / 2, y + h + 4, w * 0.52, 5, 0, 0, 2 * Math.PI); ctx.fill(); return; }
    ctx.strokeStyle = '#64748B'; ctx.lineWidth = 2.2; ctx.lineJoin = 'round'; ctx.beginPath(); ctx.moveTo(x - 7, y - 4); ctx.quadraticCurveTo(x, y - 2, x, y + 6); ctx.lineTo(x, y + h - 8); ctx.quadraticCurveTo(x, y + h, x + 8, y + h); ctx.lineTo(x + w - 8, y + h); ctx.quadraticCurveTo(x + w, y + h, x + w, y + h - 8); ctx.lineTo(x + w, y); ctx.stroke();   /* bec verseur à gauche */
    ctx.strokeStyle = 'rgba(100,116,139,0.55)'; ctx.lineWidth = 1; for (var g = 1; g <= 4; g++) { var gy = y + h - g * h / 5; ctx.beginPath(); ctx.moveTo(x + w - 4, gy); ctx.lineTo(x + w - (g % 2 ? 12 : 18), gy); ctx.stroke(); }
    ctx.strokeStyle = 'rgba(255,255,255,0.85)'; ctx.lineWidth = 3; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(x + 6, y + 12); ctx.lineTo(x + 6, y + h - 14); ctx.stroke(); ctx.lineCap = 'butt';
  }

  /* ---------- modèles moléculaires compacts, en relief (seulement pour compter les atomes) ---------- */
  var ATC = { H: ['#F8FAFC', '#94A3B8', 0.55], C: ['#475569', '#0F172A', 0.8], O: ['#F87171', '#991B1B', 0.75], N: ['#60A5FA', '#1E3A8A', 0.75], Zn: ['#A5B4FC', '#4338CA', 1.0], Li: ['#D8B4FE', '#7E22CE', 1.0], Al: ['#E2E8F0', '#64748B', 1.05], Fe: ['#FDBA74', '#9A3412', 1.0], Ca: ['#86EFAC', '#15803D', 1.1] };
  var GEO = {   /* élément, x, y, z (en Å environ) ; q : charge ; ion : rayon réduit pour les cations */
    'C': [['C', 0, 0, 0]], 'O2': [['O', -0.6, 0, 0], ['O', 0.6, 0, 0]], 'CO2': [['O', -1.16, 0, 0], ['C', 0, 0, 0.05], ['O', 1.16, 0, 0]],
    'H2O': [['O', 0, 0, 0], ['H', -0.76, 0.59, 0.15], ['H', 0.76, 0.59, 0.15]], 'H2': [['H', -0.37, 0, 0], ['H', 0.37, 0, 0]], 'N2': [['N', -0.55, 0, 0], ['N', 0.55, 0, 0]],
    'CH4': [['C', 0, 0, 0], ['H', 0.63, 0.63, 0.63], ['H', -0.63, -0.63, 0.63], ['H', -0.63, 0.63, -0.63], ['H', 0.63, -0.63, -0.63]],
    'NH3': [['N', 0, -0.1, 0], ['H', 0, 0.3, 0.94], ['H', 0.81, 0.3, -0.47], ['H', -0.81, 0.3, -0.47]],
    'H3O+': [['O', 0, 0, 0], ['H', 0, -0.95, 0.25], ['H', 0.82, 0.47, 0.25], ['H', -0.82, 0.47, 0.25]], 'HO-': [['O', 0, 0, 0], ['H', 0.95, 0, 0.1]],
    'C3H8': [['C', -1.27, 0.4, 0], ['C', 0, -0.4, 0], ['C', 1.27, 0.4, 0], ['H', -2.15, -0.25, 0], ['H', -1.3, 1.05, 0.88], ['H', -1.3, 1.05, -0.88], ['H', 0, -1.05, 0.88], ['H', 0, -1.05, -0.88], ['H', 2.15, -0.25, 0], ['H', 1.3, 1.05, 0.88], ['H', 1.3, 1.05, -0.88]],
    'C4H10': [['C', -1.9, 0.4, 0], ['C', -0.64, -0.4, 0], ['C', 0.64, 0.4, 0], ['C', 1.9, -0.4, 0], ['H', -2.8, -0.25, 0], ['H', -1.9, 1.05, 0.88], ['H', -1.9, 1.05, -0.88], ['H', -0.64, -1.05, 0.88], ['H', -0.64, -1.05, -0.88], ['H', 0.64, 1.05, 0.88], ['H', 0.64, 1.05, -0.88], ['H', 2.8, 0.25, 0], ['H', 1.9, -1.05, 0.88], ['H', 1.9, -1.05, -0.88]],
    'C2H6O': [['C', -1.2, 0.3, 0], ['C', 0.1, -0.45, 0], ['O', 1.2, 0.4, 0], ['H', 1.95, -0.15, 0], ['H', -2.05, -0.35, 0], ['H', -1.25, 0.95, 0.88], ['H', -1.25, 0.95, -0.88], ['H', 0.12, -1.1, 0.88], ['H', 0.12, -1.1, -0.88]],
    'CaCO3': [['Ca', -1.75, 0, 0], ['C', 0.9, 0, 0], ['O', 0.9, -1.22, 0], ['O', 1.95, 0.62, 0], ['O', -0.15, 0.62, 0]],
    'Fe2O3': [['Fe', -0.95, -0.35, 0], ['Fe', 0.95, -0.35, 0], ['O', 0, -0.95, 0.4], ['O', -1.8, 0.55, 0], ['O', 1.8, 0.55, 0]],
    'Zn': [['Zn', 0, 0, 0]], 'Li': [['Li', 0, 0, 0]], 'Al': [['Al', 0, 0, 0]], 'Fe': [['Fe', 0, 0, 0]], 'H+': [['H', 0, 0, 0]],
    'Zn^2+': [['Zn', 0, 0, 0, 0.7]], 'Li+': [['Li', 0, 0, 0, 0.65]], 'Al^3+': [['Al', 0, 0, 0, 0.6]], 'Ca^2+': [['Ca', 0, 0, 0, 0.8]]
  };
  var CHG = { 'H+': '+', 'Zn^2+': '2+', 'Li+': '+', 'Al^3+': '3+', 'Ca^2+': '2+', 'H3O+': '+', 'HO-': '\u2212' };
  function modele(ctx, cle, x, y, s) {   /* dessine l'entité centrée en (x, y), s : pixels par Å ; les atomes du fond d'abord */
    var at = GEO[cle].slice().sort(function (a, b) { return a[3] - b[3]; });
    at.forEach(function (a) { var c = ATC[a[0]], r = (a[4] || c[2]) * s * (1 + a[3] * 0.06), px = x + a[1] * s, py = y + a[2] * s;
      var g = ctx.createRadialGradient(px - r * 0.38, py - r * 0.4, r * 0.08, px, py, r); g.addColorStop(0, '#FFFFFF'); g.addColorStop(0.3, c[0]); g.addColorStop(1, c[1]);
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(px, py, r, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = 'rgba(15,23,42,0.25)'; ctx.lineWidth = 0.8; ctx.stroke(); });
    if (CHG[cle]) { var ext = 0; GEO[cle].forEach(function (a) { ext = Math.max(ext, Math.abs(a[1]) + (a[4] || ATC[a[0]][2])); }); ctx.font = 'bold ' + Math.round(s * 0.75) + 'px ' + FONT; ctx.fillStyle = '#BE185D'; ctx.textAlign = 'left'; ctx.textBaseline = 'middle'; ctx.fillText(CHG[cle], x + ext * s * 0.85, y - s * 0.9); }
  }
  function etendue(cle) { var w = 0, h = 0; GEO[cle].forEach(function (a) { var r = a[4] || ATC[a[0]][2]; w = Math.max(w, Math.abs(a[1]) + r); h = Math.max(h, Math.abs(a[2]) + r); }); return [2 * w + (CHG[cle] ? 0.9 : 0), 2 * h]; }

  /* =================== 2. Entraînement : réactif, produit ou espèce spectatrice ? =================== */
  (function () {
    var root = document.getElementById('tr-especes'); if (!root) { return; }
    var T = [   /* transformation, [espèce, n initial, n final (mmol)] */
      ['On verse de la soude (ions sodium $\\ce{Na+}$ et ions hydroxyde $\\ce{HO-}$) dans de l\u2019acide chlorhydrique (ions oxonium $\\ce{H3O+}$ et ions chlorure $\\ce{Cl-}$).', [['H3O+', 50, 10], ['Cl-', 50, 50], ['Na+', 40, 40], ['HO-', 40, 0], ['H2O', 5000, 5080]]],
      ['On fait brûler du méthane $\\ce{CH4}$ dans l\u2019air (dioxygène $\\ce{O2}$ et diazote $\\ce{N2}$).', [['CH4', 10, 0], ['O2', 42, 22], ['N2', 160, 160], ['CO2', 0, 10], ['H2O', 0, 20]]],
      ['On plonge un clou en fer $\\ce{Fe}$ dans une solution de sulfate de cuivre (ions cuivre $\\ce{Cu^2+}$ et ions sulfate $\\ce{SO4^2-}$).', [['Fe', 90, 70], ['Cu^2+', 20, 0], ['SO4^2-', 20, 20], ['Fe^2+', 0, 20], ['Cu', 0, 20]]],
      ['On verse du magnésium $\\ce{Mg}$ dans de l\u2019acide chlorhydrique.', [['Mg', 25, 0], ['H3O+', 100, 50], ['Cl-', 100, 100], ['Mg^2+', 0, 25], ['H2', 0, 25]]]
    ];
    function role(e) { return e[2] < e[1] ? 0 : (e[2] > e[1] ? 1 : 2); }
    var R = ['un réactif', 'un produit', 'une espèce spectatrice'];
    function fab() {
      var Q = []; shuffle(T.slice()).forEach(function (tr) { shuffle(tr[1].slice()).slice(0, 2).forEach(function (e) {
        var tab = '<div class="nt-scroll"><table class="nt-t" style="margin:0.6em auto;font-size:0.92em"><thead><tr><th>espèce</th><th>état initial</th><th>état final</th></tr></thead><tbody>' + tr[1].map(function (x) { return '<tr' + (x === e ? ' style="background:#FEF3C7"' : '') + '><td>$\\ce{' + x[0] + '}$</td><td>' + fmt(x[1], 0) + '&nbsp;mmol</td><td>' + fmt(x[2], 0) + '&nbsp;mmol</td></tr>'; }).join('') + '</tbody></table></div>';
        var r = role(e); Q.push([tr[0] + tab + 'Dans cette transformation, $\\ce{' + e[0] + '}$ est…', [R[r]].concat(R.filter(function (_, k) { return k !== r; })), r === 0 ? 'Sa quantité de matière diminue&nbsp;: c\u2019est un réactif.' : (r === 1 ? 'Sa quantité de matière augmente&nbsp;: c\u2019est un produit.' : 'Sa quantité de matière ne varie pas&nbsp;: elle ne participe pas à la transformation, c\u2019est une espèce spectatrice. Elle n\u2019apparaît pas dans l\u2019équation de la réaction.')]);
      }); });
      return shuffle(Q).slice(0, 6);
    }
    Quiz(root, null, 6, fab);
  })();

  /* =================== 3. Ajuster une équation de réaction =================== */
  (function () {
    var root = document.getElementById('lab-ajuster'); if (!root) { return; }
    var sel = $(root, '[data-in="eq"]'), zone = $(root, '.nt-ajust'), msg = $(root, '.nt-msg'), cur = 0, co = [];
    function F(f, el, q) { return { f: f, el: el, q: q || 0, g: f.replace(/\s*\(.*$/, '') }; }   /* formule (mhchem), composition, charge ; g : clé du modèle */
    var EQ = [
      ['🐣 Combustion du carbone', [F('C (s)', { C: 1 }), F('O2 (g)', { O: 2 })], [F('CO2 (g)', { C: 1, O: 2 })], [1, 1, 1]],
      ['🐣 Combustion du méthane', [F('CH4 (g)', { C: 1, H: 4 }), F('O2 (g)', { O: 2 })], [F('CO2 (g)', { C: 1, O: 2 }), F('H2O (g)', { H: 2, O: 1 })], [1, 2, 1, 2]],
      ['🐣 Corrosion du zinc par un acide', [F('Zn (s)', { Zn: 1 }), F('H+ (aq)', { H: 1 }, 1)], [F('Zn^2+ (aq)', { Zn: 1 }, 2), F('H2 (g)', { H: 2 })], [1, 2, 1, 1]],
      ['🐣 Synthèse de l\u2019ammoniac', [F('N2 (g)', { N: 2 }), F('H2 (g)', { H: 2 })], [F('NH3 (g)', { N: 1, H: 3 })], [1, 3, 2]],
      ['🐥 Combustion du propane', [F('C3H8 (g)', { C: 3, H: 8 }), F('O2 (g)', { O: 2 })], [F('CO2 (g)', { C: 1, O: 2 }), F('H2O (g)', { H: 2, O: 1 })], [1, 5, 3, 4]],
      ['🐥 Corrosion du lithium par un acide', [F('Li (s)', { Li: 1 }), F('H+ (aq)', { H: 1 }, 1)], [F('Li+ (aq)', { Li: 1 }, 1), F('H2 (g)', { H: 2 })], [2, 2, 2, 1]],
      ['🐥 Action d\u2019un acide sur le calcaire', [F('CaCO3 (s)', { Ca: 1, C: 1, O: 3 }), F('H+ (aq)', { H: 1 }, 1)], [F('Ca^2+ (aq)', { Ca: 1 }, 2), F('CO2 (g)', { C: 1, O: 2 }), F('H2O (\\ell)', { H: 2, O: 1 })], [1, 2, 1, 1, 1]],
      ['🐥 Acide chlorhydrique et soude', [F('H3O+ (aq)', { H: 3, O: 1 }, 1), F('HO- (aq)', { H: 1, O: 1 }, -1)], [F('H2O (\\ell)', { H: 2, O: 1 })], [1, 1, 2]],
      ['🐓 Combustion de l\u2019éthanol', [F('C2H6O (\\ell)', { C: 2, H: 6, O: 1 }), F('O2 (g)', { O: 2 })], [F('CO2 (g)', { C: 1, O: 2 }), F('H2O (g)', { H: 2, O: 1 })], [1, 3, 2, 3]],
      ['🐓 Combustion du butane', [F('C4H10 (g)', { C: 4, H: 10 }), F('O2 (g)', { O: 2 })], [F('CO2 (g)', { C: 1, O: 2 }), F('H2O (g)', { H: 2, O: 1 })], [2, 13, 8, 10]],
      ['🐓 Corrosion de l\u2019aluminium par un acide', [F('Al (s)', { Al: 1 }), F('H+ (aq)', { H: 1 }, 1)], [F('Al^3+ (aq)', { Al: 1 }, 3), F('H2 (g)', { H: 2 })], [2, 6, 2, 3]],
      ['🐓 Formation de la rouille', [F('Fe (s)', { Fe: 1 }), F('O2 (g)', { O: 2 })], [F('Fe2O3 (s)', { Fe: 2, O: 3 })], [4, 3, 2]]
    ];
    EQ.forEach(function (e, k) { var op = document.createElement('option'); op.value = k; op.textContent = e[0]; sel.appendChild(op); });
    function especes() { var e = EQ[cur]; return e[1].concat(e[2]); }
    function bilan() {   /* nombre d'atomes de chaque élément et charge, de chaque côté */
      var e = EQ[cur], n = e[1].length, G = {}, D = {}, qg = 0, qd = 0;
      especes().forEach(function (s, k) { var c = co[k], T = k < n ? G : D; Object.keys(s.el).forEach(function (x) { T[x] = (T[x] || 0) + c * s.el[x]; }); if (k < n) { qg += c * s.q; } else { qd += c * s.q; } });
      var els = []; especes().forEach(function (s) { Object.keys(s.el).forEach(function (x) { if (els.indexOf(x) < 0) { els.push(x); } }); });
      return { els: els, G: G, D: D, qg: qg, qd: qd, charge: e[1].concat(e[2]).some(function (s) { return s.q; }) };
    }
    function pgcd(a, b) { return b ? pgcd(b, a % b) : a; }
    function rendu() {
      var e = EQ[cur], n = e[1].length, h = '<div class="nt-aj-eq">';
      especes().forEach(function (s, k) {
        if (k === n) { h += '<span class="nt-aj-fl">$\\longrightarrow$</span>'; } else if (k) { h += '<span class="nt-aj-plus">+</span>'; }
        h += '<span class="nt-aj-t"><span class="nt-aj-tl"><span class="nt-aj-c"><button type="button" data-k="' + k + '" data-d="1" aria-label="augmenter">\u25B2</button><b>' + co[k] + '</b><button type="button" data-k="' + k + '" data-d="-1" aria-label="diminuer">\u25BC</button></span>$\\ce{' + s.f + '}$</span><canvas class="nt-aj-mol" data-k="' + k + '"></canvas></span>';
      });
      h += '</div>';
      var B = bilan(), ok = true;
      h += '<div class="nt-scroll"><table class="nt-t nt-aj-tab"><thead><tr><th></th><th>réactifs</th><th>produits</th><th></th></tr></thead><tbody>';
      B.els.forEach(function (x) { var a = B.G[x] || 0, b = B.D[x] || 0, bon = a === b; ok = ok && bon; h += '<tr class="' + (bon ? 'ok' : 'ko') + '"><td>' + x + '</td><td>' + a + '</td><td>' + b + '</td><td>' + (bon ? '\u2714' : '\u2718') + '</td></tr>'; });
      if (B.charge) { var bq = B.qg === B.qd; ok = ok && bq; var fq = function (q) { return q > 0 ? '+' + q : (q < 0 ? '\u2212' + (-q) : '0'); }; h += '<tr class="' + (bq ? 'ok' : 'ko') + '"><td>charge</td><td>' + fq(B.qg) + '</td><td>' + fq(B.qd) + '</td><td>' + (bq ? '\u2714' : '\u2718') + '</td></tr>'; }
      h += '</tbody></table></div>';
      zone.innerHTML = h; typeset(zone);
      var S0 = Math.min(13, Math.min.apply(null, especes().map(function (sp) { return 58 / Math.max(etendue(sp.g)[0], 2.2); })));   /* même échelle pour toutes les entités de l'équation : un atome a partout la même taille */
      $$(zone, 'canvas.nt-aj-mol').forEach(function (cv) {   /* les entités en relief, autant que l'indique le coefficient */
        var k = +cv.getAttribute('data-k'), cle = especes()[k].g, ex = etendue(cle), s = S0, par = ex[0] * s > 40 ? 2 : 3, n = co[k], cw = ex[0] * s + 6, ch = ex[1] * s + 6, nl = Math.ceil(n / par), W = Math.max(cw * Math.min(n, par), 40), Hc = ch * nl, dpr = window.devicePixelRatio || 1;
        cv.width = Math.round(W * dpr); cv.height = Math.round(Hc * dpr); cv.style.width = W + 'px'; cv.style.height = Hc + 'px'; var c = cv.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0);
        for (var i = 0; i < n; i++) { var li = Math.floor(i / par), nn = Math.min(par, n - li * par), x0 = (W - nn * cw) / 2 + (i % par + 0.5) * cw; modele(c, cle, x0, (li + 0.5) * ch, s); }
      });
      var g = co.reduce(function (a, b) { return pgcd(a, b); });
      msg.innerHTML = ok ? (g === 1 ? '<b>Bravo&nbsp;!</b> L\u2019équation est ajustée&nbsp;: tous les éléments' + (B.charge ? ' et la charge' : '') + ' sont conservés.' : 'Les éléments sont bien conservés, mais on peut simplifier&nbsp;: tous les coefficients sont divisibles par ' + g + '.') : 'Ajustez les coefficients avec les flèches&nbsp;: le tableau indique, pour chaque élément, s\u2019il est conservé.';
      msg.className = 'nt-msg' + (ok && g === 1 ? ' ok' : '');
      $$(zone, 'button').forEach(function (b) { b.addEventListener('click', function () { var k = +b.getAttribute('data-k'); co[k] = Math.max(1, Math.min(20, co[k] + +b.getAttribute('data-d'))); rendu(); }); });
    }
    function charge(k) { cur = k; sel.value = k; co = especes().map(function () { return 1; }); rendu(); }
    sel.addEventListener('change', function () { charge(+sel.value); });
    $(root, '[data-act="sol"]').addEventListener('click', function () { co = EQ[cur][3].slice(); rendu(); });
    $(root, '[data-act="suivante"]').addEventListener('click', function () { charge((cur + 1) % EQ.length); });
    charge(0);
  })();

  /* =================== 4. Entraînement : trouver le réactif limitant =================== */
  (function () {
    var root = document.getElementById('tr-limitant'); if (!root) { return; }
    var R = [   /* équation, A, a, B, b */
      ['CH4 (g) + 2 O2 (g) -> CO2 (g) + 2 H2O (g)', 'le méthane', 1, 'le dioxygène', 2, 'de méthane', 'de dioxygène'],
      ['C3H8 (g) + 5 O2 (g) -> 3 CO2 (g) + 4 H2O (g)', 'le propane', 1, 'le dioxygène', 5, 'de propane', 'de dioxygène'],
      ['2 H2 (g) + O2 (g) -> 2 H2O (\\ell)', 'le dihydrogène', 2, 'le dioxygène', 1, 'de dihydrogène', 'de dioxygène'],
      ['N2 (g) + 3 H2 (g) -> 2 NH3 (g)', 'le diazote', 1, 'le dihydrogène', 3, 'de diazote', 'de dihydrogène'],
      ['2 Al (s) + 6 H+ (aq) -> 2 Al^3+ (aq) + 3 H2 (g)', 'l\u2019aluminium', 2, 'l\u2019ion hydrogène', 6, 'd\u2019aluminium', 'd\u2019ions hydrogène'],
      ['Mg (s) + 2 H3O+ (aq) -> Mg^2+ (aq) + H2 (g) + 2 H2O (\\ell)', 'le magnésium', 1, 'l\u2019ion oxonium', 2, 'de magnésium', 'd\u2019ions oxonium']
    ];
    function fab() {
      var Q = [], cas = shuffle([0, 0, 1, 1, 2, 0]);
      cas.forEach(function (c, i) {
        var r = R[i % R.length], k = pick([1, 2, 3, 4, 5]), nA, nB;
        if (c === 2) { nA = r[2] * k; nB = r[4] * k; } else if (c === 0) { nA = r[2] * k; nB = r[4] * k + pick([1, 2, r[4]]); } else { nA = r[2] * k + pick([1, 2, r[2]]); nB = r[4] * k; }   /* c : 0 → A limitant, 1 → B limitant, 2 → proportions stœchiométriques */
        var qa = nA / r[2], qb = nB / r[4], bon = qa < qb ? 0 : (qb < qa ? 1 : 2), opts = [r[1], r[3], 'les deux&nbsp;: proportions stœchiométriques'];
        Q.push(['On mélange ' + fmt(nA, 0) + '&nbsp;mol ' + r[5] + ' et ' + fmt(nB, 0) + '&nbsp;mol ' + r[6] + '. Réaction&nbsp;: $\\ce{' + r[0] + '}$. Le réactif limitant est…', [opts[bon]].concat(opts.filter(function (_, j) { return j !== bon; })),
          '$\\dfrac{n_\\text{A}}{a} = \\dfrac{' + nA + '}{' + r[2] + '} = ' + String(fmt(qa, qa % 1 ? 2 : 0)).replace(',', '{,}') + '$ et $\\dfrac{n_\\text{B}}{b} = \\dfrac{' + nB + '}{' + r[4] + '} = ' + String(fmt(qb, qb % 1 ? 2 : 0)).replace(',', '{,}') + '$&nbsp;: ' + (bon === 2 ? 'les quotients sont égaux, les réactifs sont dans les proportions stœchiométriques.' : 'le plus petit quotient désigne le réactif limitant, ' + opts[bon] + '.')]);
      });
      return Q;
    }
    Quiz(root, null, 6, fab);
  })();

  /* =================== 5. Qui sera épuisé le premier ? (stocks de matière, échelle macroscopique) =================== */
  (function () {
    var root = document.getElementById('lab-limitant'); if (!root) { return; }
    var inA = $(root, '[data-in="a"]'), inB = $(root, '[data-in="b"]'), msg = $(root, '.nt-msg'), cnv, rx = 'ch4', x = 0, run = false;
    var RX = {   /* espèces : nom, coefficient, couleur ; R : réactifs, P : produits */
      ch4: { eq: '$\\ce{CH4 (g) + 2 O2 (g) -> CO2 (g) + 2 H2O (g)}$', R: [['méthane', 1, '#64748B'], ['dioxygène', 2, '#EF4444']], P: [['dioxyde de carbone', 1, '#334155'], ['eau', 2, '#38BDF8']] },
      nh3: { eq: '$\\ce{N2 (g) + 3 H2 (g) -> 2 NH3 (g)}$', R: [['diazote', 1, '#3B82F6'], ['dihydrogène', 3, '#CBD5E1']], P: [['ammoniac', 2, '#8B5CF6']] },
      cu: { eq: '$\\ce{Cu (s) + 2 Ag+ (aq) -> Cu^2+ (aq) + 2 Ag (s)}$', R: [['cuivre', 1, '#C2410C'], ['ions argent', 2, '#94A3B8']], P: [['ions cuivre', 1, '#0EA5E9'], ['argent', 2, '#CBD5E1']] }
    };
    function xmax() { var r = RX[rx]; return Math.min(+inA.value / r.R[0][1], +inB.value / r.R[1][1]); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, r = RX[rx], a = +inA.value, b = +inB.value, esp = r.R.concat(r.P), n = esp.length, base = H - 56, top = 34, u = (base - top) / 10, cw = Math.min(110, (W - 56) / (n + 0.6)), gx = Math.max(48, (W - cw * n - cw * 0.6) / 2), etroit = W < 560;
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = '#E2E8F0'; ctx.lineWidth = 1; for (var m = 0; m <= 10; m += 2) { ctx.beginPath(); ctx.moveTo(gx - 4, base - m * u); ctx.lineTo(gx + cw * (n + 0.6), base - m * u); ctx.stroke(); txt(ctx, m + ' mol', gx - 8, base - m * u, { size: 10, col: SLATE, align: 'right' }); }
      esp.forEach(function (s, i) {
        var reac = i < r.R.length, q = reac ? (i ? b : a) - s[1] * x : s[1] * x, xc = gx + cw * (i + (reac ? 0.5 : 1.1)), bw = cw * 0.62;
        for (var k = 0; k < Math.ceil(q - 1e-9); k++) { var hb = Math.min(1, q - k) * u; ctx.fillStyle = s[2]; rr(ctx, xc - bw / 2, base - k * u - hb, bw, hb - 1.5, 3); ctx.fill(); }   /* une pile de blocs d'une mole */
        if (reac) { var q0 = i ? b : a; ctx.save(); ctx.setLineDash([3, 3]); ctx.strokeStyle = '#94A3B8'; ctx.strokeRect(xc - bw / 2, base - q0 * u, bw, q0 * u); ctx.restore(); }   /* quantité initiale, en pointillés */
        var mots = s[0].split(' '); if (etroit && mots.length > 1) { txt(ctx, mots[0], xc, base + 12, { size: 9.5, col: NAVY }); txt(ctx, mots.slice(1).join(' '), xc, base + 23, { size: 9.5, col: NAVY }); } else { txt(ctx, s[0], xc, base + 14, { size: etroit ? 9.5 : 11, col: NAVY }); } txt(ctx, fmt(q, q % 1 ? 1 : 0) + ' mol', xc, base + (etroit ? 36 : 29), { size: 11, col: reac && q < 1e-9 && x > 0 ? '#B91C1C' : SLATE, bold: reac && q < 1e-9 && x > 0 });
        if (reac && q < 1e-9 && x > 0 && x >= xmax() - 1e-9) { pill(ctx, 'épuisé', xc, base - 14, { size: 11, col: '#B91C1C', stroke: '#FECACA' }); }
      });
      var xs = gx + cw * (r.R.length + 0.3); vec(ctx, xs - 12, base - 5 * u, xs + 12, base - 5 * u, '#94A3B8', 2, 8);
      pill(ctx, 'réactifs', gx + cw * r.R.length / 2, 14, { size: 11, col: '#B91C1C', stroke: '#FECACA' }); pill(ctx, 'produits', gx + cw * (r.R.length + 0.6 + r.P.length / 2), 14, { size: 11, col: '#15803D', stroke: '#BBF7D0' });
    }
    function texte() {
      var r = RX[rx]; $(root, '.nt-lim-eq').innerHTML = r.eq; typeset($(root, '.nt-lim-eq'));
      $(root, '.nt-lim-l1').textContent = 'Quantité initiale de ' + r.R[0][0]; $(root, '.nt-lim-l2').textContent = 'Quantité initiale de ' + r.R[1][0];
      $(root, '.out-a').textContent = fmt(+inA.value, +inA.value % 1 ? 1 : 0) + '\u00A0mol'; $(root, '.out-b').textContent = fmt(+inB.value, +inB.value % 1 ? 1 : 0) + '\u00A0mol';
    }
    function fin() {
      var r = RX[rx], a = +inA.value, b = +inB.value, qa = a / r.R[0][1], qb = b / r.R[1][1];
      if (a === 0 || b === 0) { msg.innerHTML = 'Il manque un des deux réactifs&nbsp;: aucune transformation ne peut se produire.'; return; }
      var ra = a - r.R[0][1] * x, rb = b - r.R[1][1] * x;
      msg.innerHTML = 'Les quantités ont varié dans les proportions de l\u2019équation&nbsp;: ' + r.R[1][1] + '&nbsp;mol de ' + r.R[1][0] + ' consommées pour ' + r.R[0][1] + '&nbsp;mol de ' + r.R[0][0] + '. ' + (qa === qb ? 'Les deux réactifs sont épuisés en même temps&nbsp;: ils étaient dans les <b>proportions stœchiométriques</b>.' : 'Le réactif limitant est le <b>' + (qa < qb ? r.R[0][0] : r.R[1][0]) + '</b>&nbsp;; il reste ' + fmt(qa < qb ? rb : ra, (qa < qb ? rb : ra) % 1 ? 1 : 0) + '&nbsp;mol de ' + (qa < qb ? r.R[1][0] : r.R[0][0]) + ', en excès.') + ' Vérification&nbsp;: $\\dfrac{n_\\text{A,i}}{a} = ' + String(fmt(qa, qa % 1 ? 2 : 0)).replace(',', '{,}') + '$ et $\\dfrac{n_\\text{B,i}}{b} = ' + String(fmt(qb, qb % 1 ? 2 : 0)).replace(',', '{,}') + '$.';
      typeset(msg);
    }
    var loop = Loop(root, function (dt) { if (!run) { return false; } x = Math.min(xmax(), x + dt * Math.max(0.6, xmax() / 2.5)); if (x >= xmax()) { run = false; fin(); } draw(cnv); return run; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 290 : 300; }, draw);
    function maj() { run = false; x = 0; texte(); draw(cnv); msg.textContent = 'Choisissez les quantités initiales de réactifs (1 bloc = 1 mol), puis lancez la transformation.'; }
    [inA, inB].forEach(function (i) { i.addEventListener('input', maj); });
    $$(root, 'input[name="lim-r"]').forEach(function (q) { q.addEventListener('change', function () { rx = q.value; maj(); }); });
    $(root, '[data-act="go"]').addEventListener('click', function () { x = 0; run = true; msg.textContent = 'Les réactifs sont consommés et les produits formés, dans les proportions de l\u2019équation…'; if (RM || xmax() === 0) { x = xmax(); run = false; draw(cnv); fin(); return; } loop.kick(); });
    maj();
  })();

  /* =================== 5 b. L'enquête : du cuivre dans le nitrate d'argent =================== */
  (function () {
    var root = document.getElementById('lab-enquete'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), bS = $(root, '[data-act="soude"]'), bC = $(root, '[data-act="chlorure"]'), t = -1, test = null, cnv;
    var B = [   /* masse de cuivre (g), cuivre restant, ions argent restants, intensité du bleu */
      [0.23, false, true, 0.25], [0.43, false, true, 0.45], [3.0, true, false, 0.95]];
    function fil(ctx, x, y, w, couv, al) {   /* morceau de cuivre, éventuellement recouvert d'argent */
      ctx.save(); ctx.globalAlpha = al; ctx.lineCap = 'round'; ctx.strokeStyle = '#C2410C'; ctx.lineWidth = 6; ctx.beginPath(); ctx.moveTo(x - w / 2, y); ctx.bezierCurveTo(x - w / 6, y - 10, x + w / 6, y + 8, x + w / 2, y - 2); ctx.stroke();
      ctx.strokeStyle = '#FDBA74'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(x - w / 2 + 2, y - 2); ctx.bezierCurveTo(x - w / 6, y - 12, x + w / 6, y + 6, x + w / 2 - 2, y - 4); ctx.stroke(); ctx.restore();
      if (couv > 0) { cristaux(ctx, x, y - 4, w * 0.9, 18 * couv, 14); }
    }
    function cristaux(ctx, x, y, w, h, n) {   /* argent : petites aiguilles grises et brillantes */
      for (var i = 0; i < n; i++) { var cx = x - w / 2 + (i + 0.5) * w / n, l = h * (0.5 + 0.5 * Math.abs(Math.sin(i * 2.3))), a = -Math.PI / 2 + Math.sin(i * 1.7) * 0.6;
        ctx.strokeStyle = i % 3 ? '#94A3B8' : '#F1F5F9'; ctx.lineWidth = 2.2; ctx.beginPath(); ctx.moveTo(cx, y); ctx.lineTo(cx + Math.cos(a) * l, y + Math.sin(a) * l); ctx.stroke(); ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(cx + Math.cos(a) * l * 0.5, y + Math.sin(a) * l * 0.5); ctx.lineTo(cx + Math.cos(a + 0.8) * l * 0.8, y + Math.sin(a + 0.8) * l * 0.8); ctx.stroke(); if (i % 4 === 0) { ctx.fillStyle = '#FFFFFF'; ctx.beginPath(); ctx.arc(cx + Math.cos(a) * l, y + Math.sin(a) * l, 1.6, 0, 2 * Math.PI); ctx.fill(); } }   /* reflets */
    }
    function tube(ctx, x, y, h, liq, prec) {   /* tube à essai : liq = couleur de la solution ; prec = couleur du précipité (ou null) */
      var w = 18; ctx.fillStyle = liq; ctx.beginPath(); ctx.moveTo(x - w / 2, y + h * 0.45); ctx.lineTo(x - w / 2, y + h - w / 2); ctx.arc(x, y + h - w / 2, w / 2, Math.PI, 0, true); ctx.lineTo(x + w / 2, y + h * 0.45); ctx.closePath(); ctx.fill();
      if (prec) { ctx.fillStyle = prec; ctx.beginPath(); ctx.moveTo(x - w / 2, y + h * 0.78); ctx.lineTo(x - w / 2, y + h - w / 2); ctx.arc(x, y + h - w / 2, w / 2, Math.PI, 0, true); ctx.lineTo(x + w / 2, y + h * 0.78); ctx.closePath(); ctx.fill(); for (var k = 0; k < 7; k++) { ctx.beginPath(); ctx.arc(x - 6 + (k * 5) % 13, y + h * 0.62 + (k * 7) % 12, 1.6, 0, 2 * Math.PI); ctx.fill(); } }
      ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(x - w / 2, y); ctx.lineTo(x - w / 2, y + h - w / 2); ctx.arc(x, y + h - w / 2, w / 2, Math.PI, 0, true); ctx.lineTo(x + w / 2, y); ctx.stroke();
      ctx.strokeStyle = 'rgba(255,255,255,0.9)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x - w / 2 + 3, y + 6); ctx.lineTo(x - w / 2 + 3, y + h - 12); ctx.stroke();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, cw = W / 3, bw = Math.min(150, cw * 0.66), bh = bw * 0.82, th = Math.min(70, bw * 0.55), tubes = !!test;
      var bloc = 52 + bh + 26 + (tubes ? th + 46 : 0), by = (H - bloc) / 2 + 52;   /* tout le contenu est centré verticalement */
      var e = t < 0 ? 0 : Math.min(1, t / 2.5), plonge = t < 0 ? 0 : Math.min(1, t / 0.5), es = t < 0.5 ? 0 : Math.min(1, (t - 0.5) / 2), ess = es * es * (3 - 2 * es);
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#F8FAFC'); gf.addColorStop(1, '#E2E8F0'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      var yb = by + bh + 4, gt = ctx.createLinearGradient(0, yb, 0, yb + 12); gt.addColorStop(0, '#D6B98C'); gt.addColorStop(1, '#A47E50'); ctx.fillStyle = gt; ctx.fillRect(0, yb, W, 10);   /* paillasse */
      B.forEach(function (b, i) {
        var x = (i + 0.5) * cw, bx = x - bw / 2, fw = bw * (i === 2 ? 0.66 : 0.34 + 0.14 * i), surf = by + bh * 0.28;
        ctx.fillStyle = 'rgba(15,23,42,0.12)'; ctx.beginPath(); ctx.ellipse(x, yb + 1, bw * 0.55, 4, 0, 0, 2 * Math.PI); ctx.fill();
        becher(ctx, bx, by, bw, bh, true);
        var a = b[3] * ess, gl = ctx.createLinearGradient(0, surf, 0, by + bh); gl.addColorStop(0, 'rgba(' + Math.round(236 - 170 * a) + ',' + Math.round(246 - 70 * a) + ',' + Math.round(255 - 20 * a) + ',0.8)'); gl.addColorStop(1, 'rgba(' + Math.round(224 - 190 * a) + ',' + Math.round(242 - 110 * a) + ',' + Math.round(254 - 40 * a) + ',0.85)');
        ctx.fillStyle = gl; rr(ctx, bx + 1, surf, bw - 2, by + bh - surf - 1, 7); ctx.fill(); ctx.strokeStyle = 'rgba(255,255,255,0.8)'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(bx + 3, surf); ctx.lineTo(bx + bw - 3, surf); ctx.stroke();   /* la solution bleuit à mesure que les ions cuivre apparaissent */
        var yf = (by - 16) + (by + bh - 12 - (by - 16)) * plonge;   /* le cuivre descend dans le bécher */
        if (b[1] || ess < 1) { fil(ctx, x, yf, fw, b[1] ? ess : 0, b[1] ? 1 : 1 - ess); }
        if (!b[1] && ess > 0) { ctx.save(); ctx.globalAlpha = ess; cristaux(ctx, x, by + bh - 5, bw * (0.32 + 0.12 * i), 15 * (0.6 + 0.3 * i), 10 + i * 4); ctx.restore(); }   /* l'argent formé, au fond */
        becher(ctx, bx, by, bw, bh, false);
        pill(ctx, 'bécher ' + (i + 1), x, by - 42, { size: 11.5, col: NAVY, stroke: GRID2 });
        txt(ctx, fmt(b[0], b[0] % 1 ? 2 : 1) + ' g de cuivre', x, yb + 22, { size: 11, col: '#9A3412' });
        if (tubes) {   /* tube à essai prélevé dans le bécher, posé dans un portoir */
          var pos = test === 'soude', prec = pos ? 'rgba(56,189,248,0.95)' : (b[2] ? 'rgba(255,255,255,0.98)' : null), ty = yb + 34;
          tube(ctx, x, ty, th, 'rgba(186,230,253,0.6)', prec);
          ctx.fillStyle = '#A16207'; rr(ctx, x - 22, ty + th * 0.55, 44, 7, 3); ctx.fill();
          pill(ctx, prec ? (pos ? 'précipité bleu' : 'précipité blanc') : 'pas de précipité', x, ty + th + 14, { size: 10.5, col: prec ? (pos ? '#0369A1' : '#334155') : '#B91C1C', stroke: '#E2E8F0' });
        }
      });
    }
    var loop = Loop(root, function (dt) { if (t < 0 || t >= 2.5) { return false; } t += dt; if (t >= 2.5) { t = 2.5; bS.disabled = false; bC.disabled = false; msg.innerHTML = 'État final&nbsp;: la solution a bleui, et un solide gris brillant est apparu. Dans les béchers 1 et 2, le cuivre a disparu&nbsp;; dans le bécher 3, il est en partie recouvert du solide gris. Réalisez maintenant les tests d\u2019identification.'; } draw(cnv); return t < 2.5; });
    cnv = Canvas($(root, 'canvas'), function (W) { var bw = Math.min(150, W / 3 * 0.66); return Math.round(52 + bw * 0.82 + 26 + Math.min(70, bw * 0.55) + 46 + 24); }, draw);   /* juste la place qu'il faut, tubes compris */
    $(root, '[data-act="go"]').addEventListener('click', function () { if (t >= 0) { return; } t = 0; test = null; msg.textContent = 'Le cuivre est plongé dans les solutions…'; if (RM) { t = 2.5; bS.disabled = false; bC.disabled = false; draw(cnv); return; } loop.kick(); });
    bS.addEventListener('click', function () { test = 'soude'; draw(cnv); msg.innerHTML = 'Test à la soude&nbsp;: un précipité bleu se forme dans les trois tubes. Les trois solutions contiennent des <b>ions cuivre</b> $\\ce{Cu^2+}$, responsables de la couleur bleue.'; typeset(msg); });
    bC.addEventListener('click', function () { test = 'chlorure'; draw(cnv); msg.innerHTML = 'Test aux ions chlorure&nbsp;: un précipité blanc se forme dans les tubes 1 et 2, mais pas dans le tube 3. Il reste des <b>ions argent</b> $\\ce{Ag+}$ dans les béchers 1 et 2, plus dans le bécher 3.'; typeset(msg); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { t = -1; test = null; bS.disabled = true; bC.disabled = true; msg.textContent = 'État initial\u00A0: trois béchers contenant la même solution incolore de nitrate d\u2019argent, et trois masses de cuivre.'; draw(cnv); });
    msg.textContent = 'État initial\u00A0: trois béchers contenant la même solution incolore de nitrate d\u2019argent, et trois masses de cuivre.'; draw(cnv);
  })();

  /* =================== 6. Les ballons (bicarbonate + vinaigre ; magnésium + acide) =================== */
  function erlen(ctx, x, base, w, h, liq, couleur) {   /* erlenmeyer : x centre, base = bas ; liq = hauteur de liquide (fraction) */
    var col = w * 0.24, hc = h * 0.25, pts = [[x - col / 2, base - h], [x - col / 2, base - h + hc], [x - w / 2, base - 8], [x - w / 2 + 8, base], [x + w / 2 - 8, base], [x + w / 2, base - 8], [x + col / 2, base - h + hc], [x + col / 2, base - h]];
    ctx.save(); ctx.beginPath(); pts.forEach(function (p, i) { if (i) { ctx.lineTo(p[0], p[1]); } else { ctx.moveTo(p[0], p[1]); } }); ctx.closePath(); ctx.fillStyle = 'rgba(224,242,254,0.35)'; ctx.fill(); ctx.clip();
    ctx.fillStyle = couleur; ctx.fillRect(x - w / 2, base - h * liq, w, h * liq); ctx.restore();
    ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.8; ctx.beginPath(); pts.forEach(function (p, i) { if (i) { ctx.lineTo(p[0], p[1]); } else { ctx.moveTo(p[0], p[1]); } }); ctx.stroke();
    ctx.strokeStyle = 'rgba(255,255,255,0.85)'; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.moveTo(x - col / 2 + 3, base - h + 6); ctx.lineTo(x - col / 2 + 3, base - h + hc); ctx.lineTo(x - w / 2 + 9, base - 14); ctx.stroke();
  }
  function ballon(ctx, x, y, r, col) {   /* ballon de baudruche posé sur le col, en y */
    if (r < 2) { return; } var g = ctx.createRadialGradient(x - r * 0.35, y - r * 1.3, r * 0.1, x, y - r, r * 1.1); g.addColorStop(0, '#FFFFFF'); g.addColorStop(0.25, col[0]); g.addColorStop(1, col[1]);
    ctx.fillStyle = g; ctx.beginPath(); ctx.moveTo(x - 6, y); ctx.bezierCurveTo(x - r * 1.1, y - r * 0.4, x - r * 1.05, y - r * 2.1, x, y - r * 2.05); ctx.bezierCurveTo(x + r * 1.05, y - r * 2.1, x + r * 1.1, y - r * 0.4, x + 6, y); ctx.closePath(); ctx.fill();
    ctx.fillStyle = col[1]; rr(ctx, x - 7, y - 3, 14, 7, 3); ctx.fill();
  }
  function tas(ctx, x, base, w, n, col, graine) {   /* n grains de poudre en tas, au fond de l'erlenmeyer, disposés au hasard (mais toujours de la même façon) */
    var s = graine * 97 + 13; function alea() { s = (s * 16807) % 2147483647; return s / 2147483647; }
    var demi = w * 0.36, h0 = Math.min(w * 0.32, 2.2 * Math.sqrt(n));
    for (var i = 0; i < n; i++) {
      var u = (alea() + alea() + alea()) / 3 * 2 - 1, gx = x + u * demi, hmax = h0 * (1 - Math.abs(u)), gy = base - 3 - Math.pow(alea(), 0.7) * hmax, r = 1.6 + alea() * 1.4;
      ctx.fillStyle = col[0]; ctx.beginPath(); ctx.ellipse(gx, gy, r * 1.25, r, alea() * 3, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = col[1]; ctx.lineWidth = 0.6; ctx.stroke();
    }
  }
  function experience(id, D) {
    var root = document.getElementById(id); if (!root) { return; }
    var msg = $(root, '.nt-msg'), chk = $(root, '[data-in="qte"]'), t = -1, run = false, cnv;
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, n = D.n.length, lignes = W < 560 && n > 4 ? 2 : 1, parL = Math.ceil(n / lignes), cw = W / parL, hl = H / lignes, w = Math.min(70, cw * 0.62), h = w * 1.15, qte = !chk || chk.checked, e = t < 0 ? 0 : Math.min(1, t / 2.5), es = 1 - Math.pow(1 - e, 3);
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#FFFFFF'); gf.addColorStop(1, '#EEF2F7'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      D.n.forEach(function (q, i) {
        var li = Math.floor(i / parL), x = (i % parL + 0.5) * cw, base = (li + 1) * hl - (qte ? 50 : 26), rmax = Math.min(cw * 0.42, (base - li * hl - h - 18) / 2.15), r = rmax * Math.cbrt(D.gaz(q) / D.gmax) * es, fs = cw < 130 ? 9 : 10.5;
        ctx.fillStyle = '#CBD5E1'; ctx.fillRect(x - cw / 2, base, cw, 3);
        erlen(ctx, x, base, w, h, 0.42, e > 0 ? D.couleurFin(q, es) : D.couleurIni);
        tas(ctx, x, base, w, Math.round(0.75 * (D.reste(q) > 0 ? D.reste(q) : 0) + 0.75 * (q[0] - Math.max(0, D.reste(q))) * (1 - es)) * (t < 0 ? 0 : 1), D.solide, i);   /* poudre au fond : tout le solide versé au début, puis seulement l'excès */
        ballon(ctx, x, base - h, r, D.ballon);
        if (r > 14) { txt(ctx, fmt(D.gaz(q), 0) + ' mmol', x, base - h - r * 1.05, { size: Math.min(11, r * 0.4), col: '#FFFFFF', bold: true }); }
        txt(ctx, D.etiq(q), x, base + 13, { size: fs, col: NAVY });
        if (qte) { var lim = D.limitant(q); [[D.nomA + '\u00A0: ' + q[0], lim !== 1], [D.nomB + '\u00A0: ' + q[1], lim !== 0]].forEach(function (l, k2) { txt(ctx, l[0] + (cw < 130 ? '' : ' mmol'), x, base + 28 + k2 * 13, { size: fs - 0.5, col: e >= 1 && l[1] ? '#BE185D' : SLATE, bold: e >= 1 && l[1] }); }); }
      });
      if (e >= 1 && qte) { pill(ctx, 'en rose\u00A0: le ou les réactifs limitants' + (W < 560 ? ' (en mmol)' : ''), W - 8, 12, { size: 10, col: '#BE185D', align: 'right', stroke: '#FBCFE8' }); }
    }
    var loop = Loop(root, function (dt) { if (!run) { return false; } t += dt; if (t >= 2.5) { run = false; msg.innerHTML = D.bilan; typeset(msg); } draw(cnv); return run; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 && D.n.length > 4 ? 560 : (W < 560 ? 320 : 330); }, draw);
    $(root, '[data-act="go"]').addEventListener('click', function () { t = 0; run = true; msg.textContent = D.pendant; if (RM) { t = 2.5; run = false; draw(cnv); msg.innerHTML = D.bilan; typeset(msg); return; } loop.kick(); });
    if (chk) { chk.addEventListener('change', function () { draw(cnv); }); }
    msg.textContent = D.avant; draw(cnv);
  }
  experience('lab-ballons1', {
    n: [[24, 83], [47, 83], [71, 83], [95, 83], [120, 83], [140, 83]], nomA: 'NaHCO\u2083', nomB: 'CH\u2083COOH', gmax: 83,
    gaz: function (q) { return Math.min(q[0], q[1]); }, reste: function (q) { return q[0] - q[1]; }, limitant: function (q) { return q[0] < q[1] ? 0 : (q[1] < q[0] ? 1 : 2); },
    etiq: function (q) { return fmt([2, 4, 6, 8, 10, 12][[24, 47, 71, 95, 120, 140].indexOf(q[0])], 1) + ' g'; },
    couleurIni: 'rgba(125,211,252,0.55)', couleurFin: function () { return 'rgba(125,211,252,0.55)'; }, solide: ['#FFFFFF', '#94A3B8'], ballon: ['#F87171', '#B91C1C'],
    avant: 'Chaque erlenmeyer contient 100\u00A0mL de vinaigre, soit 83\u00A0mmol d\u2019acide éthanoïque. Versez le bicarbonate…',
    pendant: 'Effervescence\u00A0: le dioxyde de carbone gonfle les ballons…',
    bilan: 'Dans les erlenmeyers 1 à 3, tout le bicarbonate a disparu&nbsp;: il est <b>limitant</b>, et la quantité de dioxyde de carbone formée lui est égale. À partir du 4<sup>e</sup>, il reste du bicarbonate au fond&nbsp;: c\u2019est l\u2019<b>acide éthanoïque</b> qui est limitant, et les ballons cessent de grossir (83&nbsp;mmol de gaz).'
  });
  experience('lab-ballons2', {
    n: [[13, 100], [25, 100], [50, 100], [100, 100]], nomA: 'Mg', nomB: 'H\u2083O\u207A', gmax: 50,
    gaz: function (q) { return Math.min(q[0], q[1] / 2); }, reste: function (q) { return q[0] - q[1] / 2; }, limitant: function (q) { return q[0] < q[1] / 2 ? 0 : (q[1] / 2 < q[0] ? 1 : 2); },
    etiq: function (q) { return 'n° ' + ([13, 25, 50, 100].indexOf(q[0]) + 1); },
    couleurIni: 'rgba(250,204,21,0.6)', couleurFin: function (q, es) { var reste = q[1] - 2 * Math.min(q[0], q[1] / 2); return reste > 0 ? 'rgba(250,204,21,0.6)' : 'rgba(' + Math.round(250 - 216 * es) + ',' + Math.round(204 - 7 * es) + ',' + Math.round(21 + 73 * es) + ',0.6)'; }, solide: ['#94A3B8', '#475569'], ballon: ['#60A5FA', '#1D4ED8'],
    avant: 'Chaque erlenmeyer contient 100\u00A0mmol d\u2019ions oxonium et quelques gouttes de BBT, jaune en milieu acide. Versez le magnésium…',
    pendant: 'Le magnésium réagit, le dihydrogène gonfle les ballons…',
    bilan: 'Erlenmeyers 1 et 2&nbsp;: le BBT reste jaune (il reste des ions oxonium) et tout le magnésium a disparu&nbsp;: le <b>magnésium</b> est limitant. Erlenmeyer 4&nbsp;: le BBT devient vert et il reste du magnésium&nbsp;: l\u2019<b>ion oxonium</b> est limitant. Erlenmeyer 3&nbsp;: plus de magnésium et plus d\u2019ions oxonium&nbsp;: les réactifs étaient dans les <b>proportions stœchiométriques</b>.'
  });

  /* =================== 7. Suivre la température d'une transformation =================== */
  (function () {
    var root = document.getElementById('lab-thermo'); if (!root) { return; }
    var inM = $(root, '[data-in="m"]'), msg = $(root, '.nt-msg'), rx = 'mg', t = 0, run = false, cnv, COURBES = [];
    var RX = {   /* masse du réactif limitant (g) par cran, masse d'une mole (g), énergie par mole (J, négative si libérée) */
      mg: { lab: 'Masse de magnésium', pas: 0.1, M: 24.3, dH: -467e3, col: '#DC2626', nom: 'magnésium' },
      bic: { lab: 'Masse de bicarbonate', pas: 1.0, M: 84, dH: 31e3, col: '#2563EB', nom: 'bicarbonate' }
    };
    var T0 = 20, TMAX = 240, TAU = 6, FUITE = 600;   /* température initiale (°C), durée observée (s), durée de la réaction, refroidissement lent vers l'ambiante */
    function dT(m) { var r = RX[rx]; return -r.dH * (m / r.M) / (100 * 4.18); }   /* 100 g de solution ; énergie échangée = n × énergie par mole */
    function T(c, s) { return T0 + c.d * (1 - Math.exp(-s / TAU)) * Math.exp(-s / FUITE); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, two = W >= 600, gx = two ? 150 : 46, gy = 20, gw = W - gx - 20, gh = H - 58, lo = rx === 'mg' ? 15 : 13, hi = rx === 'mg' ? 50 : 22;
      var X = function (s) { return gx + s / TMAX * gw; }, Y = function (v) { return gy + gh - (v - lo) / (hi - lo) * gh; };
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = '#E2E8F0'; ctx.lineWidth = 1; for (var v = Math.ceil(lo / 5) * 5; v <= hi; v += (rx === 'mg' ? 5 : 1)) { ctx.beginPath(); ctx.moveTo(gx, Y(v)); ctx.lineTo(gx + gw, Y(v)); ctx.stroke(); txt(ctx, v + ' °C', gx - 6, Y(v), { size: 10, col: SLATE, align: 'right' }); }
      for (var s = 0; s <= TMAX; s += 60) { txt(ctx, s + ' s', X(s), gy + gh + 14, { size: 10, col: SLATE }); }
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.3; ctx.beginPath(); ctx.moveTo(gx, gy); ctx.lineTo(gx, gy + gh); ctx.lineTo(gx + gw, gy + gh); ctx.stroke();
      COURBES.forEach(function (c, i) { var fin = c === COURBES[COURBES.length - 1] && run ? t : TMAX; ctx.strokeStyle = RX[rx].col; ctx.globalAlpha = 0.35 + 0.65 * (i + 1) / COURBES.length; ctx.lineWidth = 2.4; ctx.beginPath(); for (var k = 0; k <= 160; k++) { var s2 = fin * k / 160; if (k) { ctx.lineTo(X(s2), Y(T(c, s2))); } else { ctx.moveTo(X(s2), Y(T(c, s2))); } } ctx.stroke(); ctx.globalAlpha = 1;
        if (!run || c !== COURBES[COURBES.length - 1]) { var sm = TAU * 4; pill(ctx, fmt(c.m, rx === 'mg' ? 1 : 0) + ' g', X(sm) + 8, Y(T(c, sm)) + (c.d > 0 ? -10 : 10), { size: 10.5, col: RX[rx].col, align: 'left', stroke: '#E2E8F0' }); } });
      if (two) {   /* thermomètre */
        var c0 = COURBES[COURBES.length - 1], Tc = c0 ? T(c0, run ? t : TMAX) : T0, tx = 70, ty0 = 30, th = H - 90, fr = Math.max(0, Math.min(1, (Tc - lo) / (hi - lo)));
        ctx.fillStyle = '#F1F5F9'; ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.5; rr(ctx, tx - 9, ty0, 18, th, 9); ctx.fill(); ctx.stroke(); ctx.beginPath(); ctx.arc(tx, ty0 + th + 8, 15, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
        ctx.fillStyle = '#EF4444'; ctx.beginPath(); ctx.arc(tx, ty0 + th + 8, 11, 0, 2 * Math.PI); ctx.fill(); rr(ctx, tx - 4.5, ty0 + th - fr * (th - 10), 9, fr * (th - 10) + 12, 4.5); ctx.fill();
        pill(ctx, fmt(Tc, 1) + ' °C', tx, ty0 - 12 + 6, { size: 12, col: '#B91C1C', stroke: '#FECACA' });
      }
    }
    function texte() { var r = RX[rx]; $(root, '.nt-th-l').textContent = r.lab; $(root, '.out-m').textContent = fmt(+inM.value * r.pas, rx === 'mg' ? 1 : 0) + '\u00A0g'; }
    var loop = Loop(root, function (dt) { if (!run) { return false; } t += dt * 40; if (t >= TMAX) { t = TMAX; run = false; var c = COURBES[COURBES.length - 1]; msg.innerHTML = 'La température a ' + (c.d > 0 ? '<b>augmenté</b> d\u2019environ ' + fmt(c.d, 1) + '&nbsp;°C&nbsp;: la transformation est <b>exothermique</b>.' : '<b>diminué</b> d\u2019environ ' + fmt(-c.d, 1) + '&nbsp;°C&nbsp;: la transformation est <b>endothermique</b>.') + ' Recommencez avec une autre masse&nbsp;: plus il y a de réactif limitant, plus la variation de température est grande. (Ensuite, le mélange revient lentement à la température ambiante.)'; } draw(cnv); return run; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 600 ? 260 : 300; }, draw);
    inM.addEventListener('input', texte);
    $$(root, 'input[name="th-r"]').forEach(function (q) { q.addEventListener('change', function () { rx = q.value; COURBES = []; run = false; texte(); draw(cnv); msg.textContent = rx === 'mg' ? '100\u00A0mL d\u2019acide chlorhydrique (en excès) et du magnésium, le réactif limitant.' : '100\u00A0mL de vinaigre (en excès) et du bicarbonate de soude, le réactif limitant.'; }); });
    $(root, '[data-act="go"]').addEventListener('click', function () { var m = +inM.value * RX[rx].pas; COURBES.push({ m: m, d: dT(m) }); if (COURBES.length > 5) { COURBES.shift(); } t = 0; run = true; msg.textContent = 'On mélange, et on relève la température…'; if (RM) { t = TMAX; run = false; draw(cnv); return; } loop.kick(); });
    $(root, '[data-act="clear"]').addEventListener('click', function () { COURBES = []; run = false; draw(cnv); });
    texte(); msg.textContent = '100\u00A0mL d\u2019acide chlorhydrique (en excès) et du magnésium, le réactif limitant. Choisissez une masse et mélangez.'; draw(cnv);
  })();

  /* =================== 8. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    Quiz(root, [
      ['Au cours d\u2019une transformation chimique, la quantité de matière d\u2019un réactif…', ['diminue', 'augmente', 'reste constante'], 'Les réactifs sont consommés&nbsp;: leur quantité de matière diminue.'],
      ['Une espèce spectatrice…', ['est présente mais ne réagit pas', 'est un produit de la réaction', 'est entièrement consommée'], 'Sa quantité de matière ne varie pas, et elle n\u2019apparaît pas dans l\u2019équation.'],
      ['Quelle équation est correctement ajustée&nbsp;?', ['$\\ce{2 H2 + O2 -> 2 H2O}$', '$\\ce{H2 + O2 -> H2O}$', '$\\ce{H2 + O2 -> H2O2}$'], 'Il faut autant d\u2019atomes d\u2019hydrogène (4) et d\u2019oxygène (2) de chaque côté. $\\ce{H2O2}$ (l\u2019eau oxygénée) est une autre espèce chimique&nbsp;: on ne change jamais une formule.'],
      ['Dans $\\ce{Zn + 2 H+ -> Zn^2+ + H2}$, la charge totale des réactifs vaut…', ['+2', '+1', '0'], '$2 \\times (+1) = +2$, comme celle des produits&nbsp;: la charge est conservée.'],
      ['Pour $\\ce{N2 + 3 H2 -> 2 NH3}$, on mélange 2&nbsp;mol de diazote et 3&nbsp;mol de dihydrogène. Le réactif limitant est…', ['le dihydrogène', 'le diazote', 'aucun : proportions stœchiométriques'], '$\\dfrac{2}{1} = 2$ pour le diazote, $\\dfrac{3}{3} = 1$ pour le dihydrogène&nbsp;: le plus petit quotient désigne le dihydrogène.'],
      ['Le réactif limitant est…', ['entièrement consommé à la fin de la transformation', 'celui qui a la plus petite masse', 'celui qui a le plus petit coefficient'], 'C\u2019est le réactif épuisé le premier&nbsp;: ce n\u2019est pas forcément celui qui a la plus petite masse, ni la plus petite quantité de matière&nbsp;!'],
      ['Une transformation qui refroidit son environnement est…', ['endothermique', 'exothermique', 'athermique'], 'Elle prend de l\u2019énergie thermique à son environnement&nbsp;: elle est endothermique.'],
      ['Si l\u2019on double la quantité de réactif limitant d\u2019une transformation exothermique, l\u2019élévation de température…', ['est environ doublée', 'est la même', 'est divisée par deux'], 'L\u2019énergie libérée est proportionnelle à la quantité de réactif limitant consommé.'],
      ['Lequel de ces exemples est une transformation chimique exothermique&nbsp;?', ['la combustion du gaz de ville', 'la fusion de la glace', 'la réaction du bicarbonate avec le vinaigre'], 'Les combustions libèrent de l\u2019énergie. La fusion est une transformation physique, et la réaction du bicarbonate avec le vinaigre est endothermique.']
    ], 9);
  })();

})();
</script>
