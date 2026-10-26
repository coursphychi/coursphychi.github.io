+++
title = "Lentilles"
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
.nt-milieux { display: flex; flex-wrap: wrap; gap: 0.6em 1.4em; justify-content: center; margin: 0.4em 0 0.6em; }
.nt-mil { display: flex; flex-direction: column; align-items: center; gap: 0.3em; }
.nt-mil-l { font-size: 0.85em; font-weight: 700; color: var(--navy); }
.nt-seg-mil label span { display: inline-flex; align-items: center; gap: 0.4em; }
.nt-seg-mil label span i.sw { display: inline-block; width: 0.9em; height: 0.9em; border-radius: 50%; border: 1px solid rgba(15,23,42,0.25); }
.nt-spectre { display: block; width: 100%; height: 34px; border-radius: 8px; margin: 0.5em 0; }
.nt-h4 { color: var(--navy); font-size: 1.08em; margin: 1.5em 0 0.5em; }
.nt-geant { display: block; text-align: center; font-family: Georgia, "Times New Roman", serif; font-size: clamp(1.1em, 4.2vw, 2.2em); color: #C2410C; letter-spacing: 0.04em; margin: 0.4em 0; overflow-wrap: anywhere; }
.nt-etapes-calc p { margin: 0.35em 0 !important; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Chaque point d'un arbre éclairé renvoie de la lumière dans toutes les directions. Comment, à partir de ce fouillis de rayons, obtenir une image nette de l'arbre sur un écran, sur un capteur d'appareil photo ou sur la rétine&nbsp;? Ce chapitre montre comment une lentille convergente forme des images, comment on les construit, et comment fonctionne l'œil.</p>

## Former une image {.nt-h2}

### Qu'est-ce qu'une image&nbsp;? {.nt-h3}

<p>Chaque point éclairé d'un objet, comme un arbre au soleil, diffuse de la lumière dans toutes les directions. Si l'on place un écran blanc devant l'arbre, chaque point de l'écran reçoit de la lumière venue de tous les points de l'arbre&nbsp;: les contributions se mélangent, et l'écran est simplement éclairé, sans aucune image.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Former l'<span class="imp nt-hole">image</span> d'un objet, c'est faire correspondre à chaque <b>point objet</b> un <b>point image</b>, et un seul. On appelle <span class="imp nt-hole">stigmatisme</span> la capacité d'un système optique à réaliser cette correspondance&nbsp;: un point pour un point.</p>
</div>

<p>Une image est donc faite de points, comme un tableau pointilliste de Seurat ou les pixels d'un écran. Mais un écran blanc, lui, n'émet pas de lumière&nbsp;: il faut qu'il reçoive, en chaque point image, la lumière venue <b>d'un seul</b> point de l'objet. Comment trier ainsi les rayons qui divergent depuis chaque point&nbsp;?</p>

<div class="nt-lab" id="lab-image">
<p class="nt-tag"><i class="fa-solid fa-tree"></i>Animation</p>
<p class="nt-lab-title">Un arbre, un écran… et entre les deux&nbsp;?</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="im-s" value="rien" checked><span>Rien</span></label><label><input type="radio" name="im-s" value="trou"><span>Un petit trou</span></label><label><input type="radio" name="im-s" value="lentille"><span>Une lentille convergente</span></label></div></div>
<canvas role="img" aria-label="Un arbre aux fruits rouges, un écran, et, entre les deux, rien, un petit trou ou une lentille ; à droite, ce qu'on voit sur l'écran."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl nt-trou">Diamètre du trou&nbsp;: <b class="out-d"></b><input type="range" min="1" max="10" step="1" value="2" data-in="d"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### Première solution&nbsp;: le sténopé {.nt-h3}

<p>Plaçons entre l'objet et l'écran une plaque opaque percée d'un petit trou. De chaque point objet, un seul mince pinceau de lumière passe par le trou, et atteint l'écran en un seul endroit&nbsp;: on obtient bien, à chaque point objet, un point image. L'image est <b>renversée</b>, puisque les rayons se croisent dans le trou.</p>

<p>C'est le principe du <b>sténopé</b>, ancêtre de l'appareil photo. Pendant une éclipse, les petits trous d'une passoire, ou les trous entre les feuilles d'un arbre, projettent au sol des dizaines de petits croissants de Soleil.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Quel est le défaut d'une image formée par un sténopé, et que se passe-t-il si l'on agrandit le trou pour y remédier&nbsp;? Essayez dans l'animation précédente.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Sombre, ou floue</span></summary>
<div class="nt-d-body">
<p>Avec un tout petit trou, très peu de lumière passe&nbsp;: l'image est très <b>peu lumineuse</b>. Si l'on agrandit le trou, chaque point objet éclaire sur l'écran une petite tache, et non plus un point&nbsp;: les taches se chevauchent, et l'image devient <b>floue</b>. Il faut choisir entre une image sombre et une image floue.</p>
<p>Le photographe Justin Quinnell a ainsi fabriqué un appareil photo avec une canette percée d'un trou d'épingle, tapissée de papier photographique. Orientée vers le sud, à Bristol, elle a été exposée six mois, d'un solstice à l'autre&nbsp;: on y voit la trace du Soleil, jour après jour.</p>
</div>
</details>

### Meilleure solution&nbsp;: la lentille convergente {.nt-h3}

<p>Une <b>lentille convergente</b> fait converger les rayons qui la traversent. Bien placée, elle envoie <b>tous</b> les rayons issus d'un point objet qui la traversent vers un même point image. On retrouve la correspondance «&nbsp;un point pour un point&nbsp;», mais avec beaucoup plus de lumière&nbsp;: la luminosité de l'image est multipliée par le rapport entre la surface de la lentille et celle du petit trou.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Une lentille convergente fait correspondre à chaque point objet un point image, vers lequel convergent <span class="imp nt-hole">tous les rayons</span> issus du point objet qui traversent la lentille. Elle forme ainsi une image à la fois <b>nette</b> et <b>lumineuse</b>.</p>
</div>

## La lentille mince convergente {.nt-h2}

### Modélisation {.nt-h3}

<p>Une lentille est un morceau de verre (ou de plastique) transparent, limité par deux faces courbes. Une lentille <b>convergente</b> a les bords plus minces que le centre. Elle dévie la lumière par deux réfractions successives, à l'entrée et à la sortie. Quand elle est mince, on peut ignorer son épaisseur&nbsp;: on la représente par un segment terminé par deux pointes de flèche tournées vers l'extérieur.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<ul class="nt-facts">
<li>Le <span class="imp nt-hole">centre optique</span> O est le centre de la lentille.</li>
<li>L'<span class="imp nt-hole">axe optique</span> est la droite perpendiculaire à la lentille qui passe par O. On l'oriente dans le sens de propagation de la lumière, en général de la gauche vers la droite.</li>
<li>Pour un objet AB, perpendiculaire à l'axe optique, on note A le point de l'objet situé sur l'axe et B l'autre extrémité. Leurs images sont notées A' et B' (lire «&nbsp;A prime&nbsp;» et «&nbsp;B prime&nbsp;»).</li>
</ul>
</div>

<div class="nt-lab" id="lab-schema">
<p class="nt-tag"><i class="fa-solid fa-magnifying-glass"></i>Animation</p>
<p class="nt-lab-title">De la lentille réelle au modèle</p>
<canvas role="img" aria-label="Une lentille réelle en verre, puis son symbole : un segment vertical avec deux pointes de flèche vers l'extérieur, l'axe optique et le centre optique O."></canvas>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="sc-m" value="reel" checked><span>Lentille réelle</span></label><label><input type="radio" name="sc-m" value="modele"><span>Modèle</span></label></div></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### Les foyers et la distance focale {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: le foyer image</p>
<p>Les rayons qui arrivent sur la lentille <b>parallèlement à l'axe optique</b> en ressortent tous en passant par un même point de l'axe, situé après la lentille&nbsp;: le <span class="imp nt-hole">foyer image</span>, noté F'.</p>
</div>

<p>La lumière peut parcourir un même chemin dans un sens ou dans l'autre&nbsp;: c'est le <b>principe du retour inverse de la lumière</b> (comme un film que l'on passerait à l'envers). Des rayons qui partent du foyer image et traversent la lentille vers la gauche en ressortent donc parallèles à l'axe. En retournant la figure, on obtient un second point remarquable, symétrique de F' par rapport à O.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: le foyer objet</p>
<p>Les rayons qui passent par le <span class="imp nt-hole">foyer objet</span> F, situé avant la lentille, en ressortent <b>parallèles à l'axe optique</b>. F et F' sont symétriques par rapport au centre optique O.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp nt-hole">distance focale</span> $f'$ d'une lentille convergente est la distance entre son centre optique et son foyer image&nbsp;: $f' = \text{OF}'$. Elle s'exprime en mètres. Plus elle est petite, plus la lentille est convergente.</p>
</div>

<div class="nt-lab" id="lab-foyers">
<p class="nt-tag"><i class="fa-solid fa-bullseye"></i>Animation</p>
<p class="nt-lab-title">Les foyers d'une lentille convergente</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="fo-m" value="image" checked><span>Rayons parallèles à l'axe</span></label><label><input type="radio" name="fo-m" value="objet"><span>Rayons issus de F</span></label><label><input type="radio" name="fo-m" value="oblique"><span>Rayons parallèles, inclinés</span></label></div></div>
<canvas role="img" aria-label="Une lentille convergente, son axe optique, ses foyers F et F' ; selon le choix, un faisceau parallèle converge en F', un faisceau issu de F ressort parallèle, ou un faisceau incliné converge en un point du plan focal."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Distance focale&nbsp;: <b class="out-f"></b><input type="range" min="3" max="12" step="0.5" value="6" data-in="f"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Le Soleil est si loin que ses rayons nous parviennent pratiquement parallèles entre eux. Où se forme l'image du Soleil donnée par une lentille convergente, et pourquoi peut-on enflammer une feuille de papier avec une loupe&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Au foyer image&nbsp;: d'où son nom</span></summary>
<div class="nt-d-body">
<p>Les rayons du Soleil qui traversent la lentille convergent au foyer image&nbsp;: l'image du Soleil est une toute petite tache lumineuse, dans le plan qui passe par F'. Toute l'énergie lumineuse reçue par la lentille y est concentrée sur une très petite surface, qui s'échauffe fortement&nbsp;: le papier peut s'enflammer. C'est ce qui justifie le nom de <b>foyer</b> (du latin <i>focus</i>, le feu).</p>
<p>Plus généralement, l'image d'un objet très éloigné (on dit «&nbsp;à l'infini&nbsp;») se forme au foyer image&nbsp;; à l'inverse, un objet placé au foyer objet a son image à l'infini.</p>
</div>
</details>

## Construire l'image d'un objet {.nt-h2}

### Les trois rayons particuliers {.nt-h3}

<p>Pour trouver l'image B' d'un point objet B, il suffit de tracer <b>deux</b> rayons issus de B, dont on connaît le trajet après la lentille&nbsp;: B' est à leur intersection. Les propriétés du centre optique et des foyers fournissent trois rayons faciles à tracer.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: les trois rayons particuliers</p>
<ol class="nt-steps">
<li style="--c:#DC2626"><p>Un rayon qui passe par le <span class="imp nt-hole">centre optique</span> O n'est <b>pas dévié</b>.</p></li>
<li style="--c:#0891B2"><p>Un rayon qui arrive <span class="imp nt-hole">parallèle à l'axe optique</span> ressort en passant par le <b>foyer image</b> F'.</p></li>
<li style="--c:#7C3AED"><p>Un rayon qui passe par le <span class="imp nt-hole">foyer objet</span> F ressort <b>parallèle à l'axe optique</b>.</p></li>
</ol>
<p>L'image A' de A se trouve sur l'axe optique, à la verticale de B'&nbsp;: l'image A'B' est, elle aussi, perpendiculaire à l'axe.</p>
</div>

<div class="nt-lab" id="lab-construction">
<p class="nt-tag"><i class="fa-solid fa-pen-ruler"></i>Animation</p>
<p class="nt-lab-title">Construire l'image A'B'</p>
<canvas role="img" aria-label="Un objet AB devant une lentille convergente, ses foyers F et F' ; on trace les trois rayons particuliers issus de B, qui se croisent en B' ; on peut déplacer l'objet et changer sa taille."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="r1">① par O</button><button type="button" class="nt-btn" data-act="r2">② parallèle à l'axe</button><button type="button" class="nt-btn" data-act="r3">③ par F</button><button type="button" class="nt-btn" data-act="faisceau"><i class="fa-solid fa-wand-magic-sparkles"></i>&nbsp; Tout un faisceau</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-eraser"></i>&nbsp; Effacer</button></div>
<div class="nt-ctrls">
<label class="nt-ctrl">Distance de l'objet à la lentille&nbsp;: <b class="out-a"></b><input type="range" min="2" max="30" step="0.5" value="15" data-in="a"></label>
<label class="nt-ctrl">Distance focale&nbsp;: <b class="out-f"></b><input type="range" min="3" max="10" step="0.5" value="6" data-in="f"></label>
</div>
<p class="nt-note nt-center">Faites glisser le point B pour déplacer l'objet.</p>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Les trois rayons particuliers n'ont rien de spécial, sinon d'être faciles à tracer&nbsp;! Une fois B' trouvé, on sait que <b>tous</b> les rayons issus de B qui traversent la lentille passent par B'&nbsp;: essayez le bouton «&nbsp;Tout un faisceau&nbsp;». La convergence d'un faisceau parallèle vers F' n'est d'ailleurs qu'un cas particulier de cette règle, quand le point objet est à l'infini.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode&nbsp;: construire l'image à l'échelle</p>
<ol class="nt-steps">
<li><p>Choisir une échelle, puis tracer l'axe optique, la lentille, les foyers F et F' (à la distance $f'$ de O, de part et d'autre), et l'objet AB.</p></li>
<li><p>Tracer deux des trois rayons particuliers issus de B, en les fléchant&nbsp;; leur intersection est B'.</p></li>
<li><p>Tracer A'B', perpendiculaire à l'axe optique, avec A' sur l'axe.</p></li>
<li><p>Mesurer sur le schéma, et convertir avec l'échelle, la position de l'image ($\text{OA}'$) et sa taille ($\text{A}'\text{B}'$)&nbsp;; noter son sens (droite ou renversée).</p></li>
</ol>
</div>

### Le grandissement {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp nt-hole">grandissement</span> $\gamma$ (lettre grecque gamma) est le rapport entre la taille de l'image et celle de l'objet. Il n'a <b>pas d'unité</b>.</p>
<ul class="nt-facts">
<li>Si $\gamma > 1$, l'image est plus grande que l'objet&nbsp;: on dit qu'elle est <span class="imp nt-hole">agrandie</span>.</li>
<li>Si $\gamma < 1$, elle est plus petite que l'objet&nbsp;: on dit qu'elle est <span class="imp nt-hole">réduite</span>.</li>
</ul>
</div>

<p>Sur le schéma, les triangles OAB et OA'B' forment une configuration «&nbsp;papillon&nbsp;»&nbsp;: les droites (AB) et (A'B') sont parallèles (toutes deux perpendiculaires à l'axe), et les droites (AA') et (BB') se coupent en O. D'après le théorème de Thalès, les longueurs des côtés correspondants sont proportionnelles.</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$\gamma = \dfrac{\text{A}'\text{B}'}{\text{AB}} = \dfrac{\text{OA}'}{\text{OA}}$</p>
<div class="nt-f-units"><span>$\text{AB}$, $\text{A}'\text{B}'$&nbsp;: tailles de l'objet et de l'image</span><span>$\text{OA}$, $\text{OA}'$&nbsp;: distances de l'objet et de l'image à la lentille</span><span>toutes les longueurs dans la <b>même unité</b></span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On précise toujours, en plus du grandissement, le <b>sens</b> de l'image&nbsp;: droite ou renversée. Plus tard (en première), on utilisera des longueurs comptées avec un signe, et le grandissement sera négatif pour une image renversée.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Un objet AB de 2,0&nbsp;cm est placé à 15&nbsp;cm d'une lentille convergente. Son image se forme à 10&nbsp;cm de la lentille, de l'autre côté. Calculer le grandissement et la taille de l'image.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">γ ≈ 0,67 et A'B' ≈ 1,3 cm</span></summary>
<div class="nt-d-body">
<p>$\gamma = \dfrac{\text{OA}'}{\text{OA}} = \dfrac{\pu{10 cm}}{\pu{15 cm}} \approx 0,67$, donc $\text{A}'\text{B}' = \gamma \times \text{AB} \approx 0,67 \times \pu{2,0 cm} \approx \pu{1,3 cm}$. L'image est réduite ($\gamma < 1$) et renversée (elle est de l'autre côté de l'axe).</p>
</div>
</details>

<div class="nt-lab nt-quizlab" id="tr-image">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Exploiter une construction</p>
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

### La nature de l'image dépend de la position de l'objet {.nt-h3}

<p>En déplaçant l'objet dans l'animation de construction, on constate que l'image change de position, de taille, et même de nature.</p>

<div class="nt-scroll"><table class="nt-t nt-t-egal">
<thead><tr><th>position de l'objet</th><th>image</th><th>exemple</th></tr></thead>
<tbody>
<tr><td>très loin («&nbsp;à l'infini&nbsp;»)</td><td>dans le plan du foyer image F', très petite</td><td>image du Soleil</td></tr>
<tr><td>avant F, loin de la lentille (au-delà de $2f'$)</td><td><b>réelle</b>, renversée, réduite</td><td>œil, appareil photo</td></tr>
<tr><td>avant F, près de F (entre $2f'$ et $f'$)</td><td><b>réelle</b>, renversée, agrandie</td><td>projecteur de cinéma</td></tr>
<tr><td>sur F</td><td>à l'infini</td><td>phare, lampe torche</td></tr>
<tr><td>entre F et la lentille</td><td><b>virtuelle</b>, droite, agrandie</td><td>loupe</td></tr>
</tbody>
</table></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour qu'une lentille convergente donne d'un objet une <span class="imp nt-hole">image réelle</span>, que l'on peut recueillir sur un écran, l'objet doit être placé <b>avant le foyer objet</b> F. L'image est alors renversée, et située après le foyer image F'.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La loupe et l'image virtuelle</span></summary>
<div class="nt-d-body">
<p>Quand l'objet est entre le foyer objet et la lentille, les rayons issus de B ressortent de la lentille en <b>divergeant</b>&nbsp;: ils ne se croisent nulle part, et aucune image ne peut être recueillie sur un écran. Pourtant, si l'on regarde à travers la lentille, on voit une image droite et agrandie&nbsp;: c'est le principe de la <b>loupe</b>.</p>
<p>Les rayons qui sortent de la lentille semblent provenir d'un point B', situé du même côté que l'objet&nbsp;: c'est le point où se croisent leurs <b>prolongements</b>, vers l'arrière. Aucun rayon ne passe réellement par B'&nbsp;: c'est une illusion, du même type que les mirages. On dit que l'image est <b>virtuelle</b>. Placez l'objet entre F et O dans l'animation de construction pour la voir.</p>
</div>
</details>

## Quelques questions {.nt-h2}

### L'image a-t-elle besoin de l'écran&nbsp;? {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Si l'on approche ou éloigne un peu l'écran, observe-t-on encore l'image nette&nbsp;? Et l'image a-t-elle besoin de l'écran pour se former&nbsp;?</p>
</div>

<div class="nt-lab" id="lab-ecran">
<p class="nt-tag"><i class="fa-solid fa-display"></i>Animation</p>
<p class="nt-lab-title">L'écran, la lentille et l'image</p>
<canvas role="img" aria-label="Une flèche lumineuse, une lentille convergente et un écran que l'on déplace ; à droite, ce qu'on voit sur l'écran : une image nette seulement quand l'écran est à l'endroit où les rayons se croisent ; on peut aussi cacher une partie de la lentille."></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Position de l'écran&nbsp;: <b class="out-e"></b><input type="range" min="-100" max="100" step="1" value="40" data-in="e"></label>
<label class="nt-ctrl">Partie cachée de la lentille&nbsp;: <b class="out-c"></b><input type="range" min="0" max="90" step="1" value="0" data-in="c"></label>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>L'image se forme là où les rayons se croisent, et <b>seulement là</b>. Ailleurs, l'écran intercepte des rayons qui convergent vers les points images, ou qui en divergent&nbsp;: chaque point objet donne une petite tache, et l'image est <b>floue</b>. Faire la <b>mise au point</b>, c'est placer l'écran (ou le capteur) à l'endroit de l'image.</li>
<li>L'écran ne sert qu'à <b>diffuser</b> la lumière vers nos yeux&nbsp;: l'image existe sans lui. On peut d'ailleurs la voir sans écran, en regardant vers la lentille depuis un peu plus loin que l'image.</li>
</ul>
</div>

### Que se passe-t-il si l'on cache une partie de la lentille&nbsp;? {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Si l'on cache la moitié de la lentille, une partie de l'image disparaît-elle&nbsp;? Faites une prédiction, puis vérifiez avec le second curseur de l'animation.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Non&nbsp;: l'image est complète, mais moins lumineuse</span></summary>
<div class="nt-d-body">
<p>L'image reste entière&nbsp;! Chaque point image est formé par des rayons qui ont traversé <b>toute</b> la lentille. Tant qu'il reste une partie de la lentille, des rayons issus de chaque point objet la traversent et convergent vers le point image correspondant&nbsp;: l'image se forme, mais elle reçoit moins de lumière, et elle est moins lumineuse.</p>
</div>
</details>

## L'œil {.nt-h2}

### L'œil réel {.nt-h3}

<p>L'œil est, lui aussi, un système optique qui forme des images. La lumière y entre par la <b>cornée</b>, membrane transparente et bombée, traverse la <b>pupille</b>, ouverture au centre de l'<b>iris</b> (la partie colorée de l'œil), puis le <b>cristallin</b>, une lentille souple. Elle forme une image sur la <b>rétine</b>, qui tapisse le fond de l'œil et contient des cellules sensibles à la lumière. Le <b>nerf optique</b> transmet les signaux au cerveau.</p>

<div class="nt-lab" id="lab-oeilreel">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Schéma</p>
<p class="nt-lab-title">Coupe de l'œil humain</p>
<canvas role="img" aria-label="Coupe de l'œil humain : cornée, iris, pupille, cristallin, humeur aqueuse, humeur vitrée, rétine, nerf optique ; en survolant ou en touchant une partie, son rôle s'affiche."></canvas>
<p class="nt-msg" aria-live="polite"></p>
</div>

### Le modèle de l'œil réduit {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: le modèle de l'œil réduit</p>
<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>œil réel</th><th>modèle de l'œil réduit</th><th>rôle</th></tr></thead>
<tbody>
<tr><td>iris (et pupille)</td><td>diaphragme</td><td>règle la quantité de lumière qui entre</td></tr>
<tr><td>cornée et cristallin</td><td>lentille mince convergente</td><td>forment l'image</td></tr>
<tr><td>rétine</td><td>écran</td><td>reçoit l'image</td></tr>
</tbody>
</table></div>
<p>L'image formée sur la rétine est <b>réelle</b> et <b>renversée</b>&nbsp;: c'est le cerveau qui la «&nbsp;redresse&nbsp;».</p>
</div>

<p>La cornée assure l'essentiel de la convergence&nbsp;; le cristallin, lui, permet d'ajuster finement la distance focale. Contrairement à l'appareil photo, qui fait la mise au point en déplaçant l'objectif par rapport au capteur, l'œil ne peut pas changer la distance entre sa lentille et sa rétine (environ 17&nbsp;mm dans le modèle)&nbsp;: c'est la <b>distance focale</b> qui varie.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Pour un œil normal (on dit <b>emmétrope</b>), au repos, l'image d'un objet très éloigné se forme exactement sur la rétine. Quand l'objet se rapproche, son image recule derrière la rétine&nbsp;: des muscles bombent alors le cristallin, ce qui diminue sa distance focale et ramène l'image sur la rétine. C'est l'<span class="imp nt-hole">accommodation</span>.</p>
</div>

<div class="nt-lab" id="lab-oeil">
<p class="nt-tag"><i class="fa-solid fa-glasses"></i>Animation</p>
<p class="nt-lab-title">Le modèle de l'œil réduit</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="oe-t" value="normal" checked><span>Œil normal</span></label><label><input type="radio" name="oe-t" value="myope"><span>Œil myope</span></label><label><input type="radio" name="oe-t" value="hyper"><span>Œil hypermétrope</span></label></div><label class="nt-check"><input type="checkbox" data-in="acc" checked> Accommodation</label><label class="nt-check"><input type="checkbox" data-in="verre"> Verre correcteur</label></div>
<canvas role="img" aria-label="Le modèle de l'œil réduit : un diaphragme, une lentille convergente et un écran (la rétine) ; les rayons issus d'un point objet convergent sur la rétine, ou avant, ou après, selon la distance de l'objet, l'accommodation et le type d'œil."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Distance de l'objet&nbsp;: <b class="out-d"></b><input type="range" min="0" max="100" step="1" value="100" data-in="d"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les défauts de l'œil et leur correction</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>La myopie.</b> L'œil est trop convergent (cornée trop courbée, cristallin trop puissant) ou trop long&nbsp;: l'image d'un objet éloigné se forme <b>avant</b> la rétine, et le myope voit flou de loin. On la corrige avec des verres <b>divergents</b>, qui font converger les rayons plus loin.</li>
<li><b>L'hypermétropie.</b> L'œil n'est pas assez convergent, ou trop court&nbsp;: l'image d'un objet éloigné se forme <b>après</b> la rétine. L'hypermétrope doit accommoder même pour voir de loin, et n'y parvient plus de près. On la corrige avec des verres <b>convergents</b>.</li>
<li><b>La presbytie.</b> Avec l'âge (à partir de 40 ans environ), le cristallin durcit et l'accommodation devient insuffisante&nbsp;: on voit mal de près. On la corrige aussi avec des verres convergents.</li>
<li><b>L'astigmatisme.</b> La cornée ou le cristallin n'ont plus la même courbure dans toutes les directions&nbsp;: les rayons qui arrivent selon deux directions différentes ne convergent pas au même endroit. L'image d'un point n'est plus un point, mais une petite tache allongée&nbsp;: l'œil a perdu son <b>stigmatisme</b>, d'où le nom. On le corrige avec des verres de forme particulière.</li>
</ul>
<p>Testez la myopie et l'hypermétropie dans l'animation précédente, avec et sans verre correcteur.</p>
</div>
</details>

## Testez-vous {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-final">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur les lentilles et l'œil</p>
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

  /* ---------- outils communs du chapitre ---------- */
  var VERT = '#16A34A', ROSE = '#DB2777', BLEU_L = '#2563EB';
  function lentille(ctx, x, y, h, col) {   /* symbole de la lentille mince convergente : segment et deux pointes vers l'extérieur */
    ctx.strokeStyle = col || BLEU_L; ctx.fillStyle = col || BLEU_L; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.moveTo(x, y - h); ctx.lineTo(x, y + h); ctx.stroke();
    [[-1, y - h], [1, y + h]].forEach(function (s) { var yy = s[1], d = s[0]; ctx.beginPath(); ctx.moveTo(x, yy); ctx.lineTo(x - 8, yy - d * 11); ctx.lineTo(x + 8, yy - d * 11); ctx.closePath(); ctx.fill(); });
  }
  function fleche(ctx, x, y0, y1, col, w, tir) {   /* objet ou image : flèche verticale de (x, y0) à (x, y1) */
    ctx.save(); if (tir) { ctx.setLineDash(tir); } ctx.strokeStyle = col; ctx.lineWidth = w || 3; ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x, y1); ctx.stroke(); ctx.restore();
    var s = y1 < y0 ? 1 : -1; ctx.fillStyle = col; ctx.beginPath(); ctx.moveTo(x, y1); ctx.lineTo(x - 6, y1 + s * 11); ctx.lineTo(x + 6, y1 + s * 11); ctx.closePath(); ctx.fill();
  }
  function point(ctx, x, y, col, lab, dx, dy) { ctx.fillStyle = col; ctx.beginPath(); ctx.arc(x, y, 3.5, 0, 2 * Math.PI); ctx.fill(); if (lab) { txt(ctx, lab, x + (dx || 0), y + (dy === undefined ? 16 : dy), { size: 13, col: col, bold: true, serif: true }); } }
  function arbre(ctx, x, sol, h, al, fruits) {   /* arbre de dessin animé, aux fruits rouges ; renvoie la position des fruits */
    ctx.save(); ctx.globalAlpha = al === undefined ? 1 : al;
    var gt = ctx.createLinearGradient(x - h * 0.06, 0, x + h * 0.06, 0); gt.addColorStop(0, '#9A3412'); gt.addColorStop(1, '#EA580C'); ctx.fillStyle = gt; ctx.beginPath(); ctx.moveTo(x - h * 0.06, sol); ctx.lineTo(x - h * 0.035, sol - h * 0.5); ctx.lineTo(x + h * 0.035, sol - h * 0.5); ctx.lineTo(x + h * 0.06, sol); ctx.closePath(); ctx.fill();
    var cy = sol - h * 0.68, R = h * 0.3, gc = ctx.createRadialGradient(x - R * 0.3, cy - R * 0.4, R * 0.1, x, cy, R * 1.3); gc.addColorStop(0, '#BEF264'); gc.addColorStop(1, '#4D7C0F'); ctx.fillStyle = gc;
    [[0, 0, 1], [-0.55, 0.2, 0.62], [0.55, 0.2, 0.62], [-0.3, -0.45, 0.6], [0.32, -0.42, 0.62]].forEach(function (b) { ctx.beginPath(); ctx.arc(x + b[0] * R, cy + b[1] * R, b[2] * R, 0, 2 * Math.PI); ctx.fill(); });
    var F = (fruits || [[0, -0.7], [-0.55, 0.05], [0.5, 0.3], [0.05, 0.45]]).map(function (f) { return [x + f[0] * R, cy + f[1] * R]; });
    F.forEach(function (p) { ctx.fillStyle = '#DC2626'; ctx.beginPath(); ctx.arc(p[0], p[1], Math.max(2.5, h * 0.035), 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = 'rgba(255,255,255,0.7)'; ctx.beginPath(); ctx.arc(p[0] - 1, p[1] - 1, Math.max(1, h * 0.012), 0, 2 * Math.PI); ctx.fill(); });
    ctx.restore(); return F;
  }
  function flouDisque(ctx, x, y, w, h, r, dessin) {   /* dessine dessin(c2, w, h) dans le cadre (x, y, w, h), flouté par un disque de rayon r (moyenne exacte de copies décalées) */
    var m = Math.ceil(r) + 2, dpr = window.devicePixelRatio || 1, oc = document.createElement('canvas'); oc.width = Math.round((w + 2 * m) * dpr); oc.height = Math.round((h + 2 * m) * dpr);
    var c2 = oc.getContext('2d'); c2.setTransform(dpr, 0, 0, dpr, 0, 0); c2.translate(m, m); dessin(c2, w, h);
    ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip();
    var n = r < 0.6 ? 1 : Math.min(90, 12 + Math.round(r * 3));
    for (var i = 0; i < n; i++) { var a = i * 2.39996, q = n === 1 ? 0 : r * Math.sqrt((i + 0.5) / n); ctx.globalAlpha = 1 / (i + 1); ctx.drawImage(oc, x - m + q * Math.cos(a), y - m + q * Math.sin(a), w + 2 * m, h + 2 * m); }   /* moyenne glissante : chaque copie pèse autant que les autres */
    ctx.restore();
  }

  /* =================== 1. Un arbre, un écran… et entre les deux ? =================== */
  (function () {
    var root = document.getElementById('lab-image'); if (!root) { return; }
    var inD = $(root, '[data-in="d"]'), msg = $(root, '.nt-msg'), mode = 'rien', cnv, ctrl = $(root, '.nt-trou');
    var COUL = ['#DC2626', '#F59E0B', '#7C3AED'];   /* trois fruits suivis, de couleurs différentes */
    function scene(c2, w, h, hor, base, ech, inv) {   /* paysage vu sur l'écran : ciel, herbe, arbre ; inv : image renversée */
      c2.save(); if (inv) { c2.translate(w, h); c2.scale(-1, -1); }   /* image renversée : tournée d'un demi-tour */
      var g = c2.createLinearGradient(0, -20, 0, hor); g.addColorStop(0, '#93C5FD'); g.addColorStop(1, '#E0F2FE'); c2.fillStyle = g; c2.fillRect(-40, -40, w + 80, hor + 40);
      var gh = c2.createLinearGradient(0, hor, 0, h + 40); gh.addColorStop(0, '#84CC16'); gh.addColorStop(1, '#4D7C0F'); c2.fillStyle = gh; c2.fillRect(-40, hor, w + 80, h - hor + 40);   /* le ciel et l'herbe couvrent tout l'écran */
      arbre(c2, w / 2, base, ech, 1, [[0, -0.75], [-0.55, 0.0], [0.45, 0.4]]); c2.restore();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, two = W >= 620, hs = two ? H : H * 0.6, sol = hs - 26, ht = two ? hs * 0.62 : hs * 0.5, xt = Math.max(two ? W * 0.1 : W * 0.12, ht * 0.33 + 6), xb = two ? W * 0.36 : W * 0.5, xs = two ? W * 0.58 : W * 0.88, yb = sol - ht * 0.55, d = +inD.value;
      var sTop = sol - hs * 0.86, hh = d * hs * 0.006, lh = hs * 0.24;   /* haut de l'écran ; demi-hauteur du trou ; demi-hauteur de la lentille */
      ctx.clearRect(0, 0, W, H); var g = ctx.createLinearGradient(0, 0, 0, sol); g.addColorStop(0, '#93C5FD'); g.addColorStop(1, '#E0F2FE'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, sol); ctx.fillStyle = '#65A30D'; ctx.fillRect(0, sol, W, hs - sol);
      var Fr = arbre(ctx, xt, sol, ht, 1, [[0, -0.75], [-0.55, 0.0], [0.45, 0.4]]);
      var m = (xs - xb) / (xb - xt), Pi = Fr.map(function (p) { return [xs, yb + (yb - p[1]) * m]; });   /* points images (trou ou lentille) */
      function surEcran(p, yo) { return p[1] + (yo - p[1]) * (xs - p[0]) / (xb - p[0]); }   /* où arrive, sur l'écran, le rayon issu de p passant par (xb, yo) */
      ctx.save(); ctx.beginPath(); ctx.rect(0, 0, xs, hs); ctx.clip();
      Fr.forEach(function (p, k) {
        var col = COUL[k];
        if (mode === 'rien') { ctx.strokeStyle = col; ctx.globalAlpha = 0.8; ctx.lineWidth = 1.1; for (var j2 = 0; j2 < 9; j2++) { var ye = sTop + 6 + j2 * (sol - sTop - 12) / 8; ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(xs, ye); ctx.stroke(); } ctx.globalAlpha = 1; return; }
        var y1 = mode === 'trou' ? yb - hh : yb - lh, y2 = mode === 'trou' ? yb + hh : yb + lh, e1 = mode === 'trou' ? surEcran(p, y1) : Pi[k][1], e2 = mode === 'trou' ? surEcran(p, y2) : Pi[k][1];
        ctx.fillStyle = col; ctx.globalAlpha = mode === 'trou' ? 0.28 : 0.2; ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(xb, y1); ctx.lineTo(xs, e1); ctx.lineTo(xs, e2); ctx.lineTo(xb, y2); ctx.closePath(); ctx.fill();   /* pinceau de lumière, jusqu'aux rayons extrêmes */
        ctx.globalAlpha = 0.9; ctx.strokeStyle = col; ctx.lineWidth = 1.2; [[y1, e1], [y2, e2]].forEach(function (r) { ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(xb, r[0]); ctx.lineTo(xs, r[1]); ctx.stroke(); }); ctx.globalAlpha = 1;
        ctx.fillStyle = col; ctx.fillRect(xs - 2, Math.min(e1, e2) - 1, 4, Math.abs(e2 - e1) + 2);   /* la tache sur l'écran */
      });
      ctx.restore();
      Fr.forEach(function (p, k) { ctx.fillStyle = COUL[k]; ctx.beginPath(); ctx.arc(p[0], p[1], 5, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = 1.5; ctx.stroke(); });
      if (mode === 'trou') { ctx.fillStyle = '#334155'; ctx.fillRect(xb - 4, sTop, 8, yb - hh - sTop); ctx.fillRect(xb - 4, yb + hh, 8, sol - yb - hh); }
      if (mode === 'lentille') { var gl = ctx.createLinearGradient(xb - 9, 0, xb + 9, 0); gl.addColorStop(0, 'rgba(186,230,253,0.5)'); gl.addColorStop(0.5, 'rgba(255,255,255,0.85)'); gl.addColorStop(1, 'rgba(186,230,253,0.5)'); ctx.fillStyle = gl; ctx.beginPath(); ctx.moveTo(xb, yb - lh); ctx.quadraticCurveTo(xb + 18, yb, xb, yb + lh); ctx.quadraticCurveTo(xb - 18, yb, xb, yb - lh); ctx.fill(); ctx.strokeStyle = 'rgba(14,116,144,0.6)'; ctx.lineWidth = 1; ctx.stroke(); }
      ctx.fillStyle = '#F8FAFC'; ctx.fillRect(xs, sTop, 6, sol - sTop); ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1; ctx.strokeRect(xs, sTop, 6, sol - sTop); txt(ctx, 'écran', xs + 3, sol + 12, { size: 10, col: '#1E293B' });
      /* ce que l'on voit sur l'écran, de face : l'écran correspond à la hauteur [sTop, sol] du dessin de côté */
      var px = two ? W * 0.66 : 20, py = two ? 24 : hs + 16, pw = two ? W * 0.31 : W - 40, ph = two ? H - 48 : H - hs - 30, k = ph / (sol - sTop);
      txt(ctx, 'sur l\u2019écran', px + pw / 2, py - 10, { size: 11, col: '#1E293B', bold: true });
      if (mode === 'rien') { var gg = ctx.createRadialGradient(px + pw / 2, py + ph / 2, 4, px + pw / 2, py + ph / 2, pw * 0.8); gg.addColorStop(0, '#FAFAF5'); gg.addColorStop(1, '#E7E5DF'); ctx.fillStyle = gg; ctx.fillRect(px, py, pw, ph); }
      else {
        var hor = (yb - sTop) * k, base = (yb + (yb - sol) * m - sTop) * k, ech = ht * m * k, tache = mode === 'trou' ? (2 * hh * (xs - xt) / (xb - xt)) * k / 2 : 0, lum = mode === 'lentille' ? 1 : Math.min(1, 0.1 + d * d * 0.011);   /* horizon à la hauteur du trou ; rayon des taches ; luminosité */
        flouDisque(ctx, px, py, pw, ph, tache, function (c2, w, h) { scene(c2, w, h, h - hor, h - base, ech, true); });
        ctx.fillStyle = 'rgba(15,23,42,' + (0.85 * (1 - lum)) + ')'; ctx.fillRect(px, py, pw, ph);   /* image sombre si peu de lumière passe */
      }
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.5; ctx.strokeRect(px, py, pw, ph);
    }
    var TXT = { rien: 'Chaque point de l\u2019écran reçoit de la lumière venue de <b>tous</b> les points de l\u2019arbre&nbsp;: les contributions se mélangent, et l\u2019écran est uniformément éclairé. Aucune image&nbsp;!', trou: '', lentille: 'Tous les rayons issus d\u2019un point de l\u2019arbre qui traversent la lentille convergent vers un même point de l\u2019écran&nbsp;: l\u2019image est nette, lumineuse et renversée.' };
    function texte() { var d = +inD.value; $(root, '.out-d').textContent = d + '\u00A0mm'; ctrl.style.display = mode === 'trou' ? '' : 'none'; msg.innerHTML = mode === 'trou' ? (d <= 2 ? 'À travers le petit trou, un seul mince pinceau de lumière passe de chaque point de l\u2019arbre&nbsp;: à chaque point objet correspond un point image. L\u2019image est nette et renversée… mais très sombre.' : (d <= 5 ? 'Avec un trou plus large, l\u2019image est plus lumineuse, mais chaque point de l\u2019arbre donne une petite tache&nbsp;: elle devient floue.' : 'Avec un grand trou, l\u2019image est lumineuse mais très floue&nbsp;: les taches se chevauchent. Avec un sténopé, il faut choisir entre une image sombre et une image floue.')) : TXT[mode]; }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 620 ? 470 : 300; }, draw);
    $$(root, 'input[name="im-s"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; texte(); draw(cnv); }); });
    inD.addEventListener('input', function () { texte(); draw(cnv); });
    texte(); draw(cnv);
  })();

  /* =================== 2. De la lentille réelle au modèle =================== */
  (function () {
    var root = document.getElementById('lab-schema'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), mode = 'reel', cnv;
    function refr(d, nrm, n1, n2) { var c = -(nrm[0] * d[0] + nrm[1] * d[1]); if (c < 0) { nrm = [-nrm[0], -nrm[1]]; c = -c; } var r = n1 / n2, k = 1 - r * r * (1 - c * c); if (k < 0) { return null; } return [r * d[0] + (r * c - Math.sqrt(k)) * nrm[0], r * d[1] + (r * c - Math.sqrt(k)) * nrm[1]]; }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, cx = W / 2, cy = H / 2, h = Math.min(90, H * 0.36), R = h * 2.2, e = h * 0.5;   /* lentille biconvexe : deux arcs de rayon R, épaisseur e au centre */
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#0B1120'); gf.addColorStop(1, '#172554'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      ctx.save(); ctx.setLineDash([8, 6]); ctx.strokeStyle = 'rgba(203,213,225,0.6)'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(16, cy); ctx.lineTo(W - 16, cy); ctx.stroke(); ctx.restore(); txt(ctx, 'axe optique', W - 18, cy + 14, { size: 10.5, col: '#CBD5E1', align: 'right' });
      var C1 = [cx - e / 2 + R, cy], C2 = [cx + e / 2 - R, cy];   /* centres des deux faces */
      if (mode === 'reel') {
        ctx.save(); ctx.beginPath(); ctx.arc(C1[0], C1[1], R, Math.PI - Math.asin(h / R), Math.PI + Math.asin(h / R)); ctx.arc(C2[0], C2[1], R, -Math.asin(h / R), Math.asin(h / R)); ctx.closePath();
        var gl = ctx.createLinearGradient(cx - e, 0, cx + e, 0); gl.addColorStop(0, 'rgba(186,230,253,0.35)'); gl.addColorStop(0.5, 'rgba(240,249,255,0.75)'); gl.addColorStop(1, 'rgba(186,230,253,0.35)'); ctx.fillStyle = gl; ctx.fill(); ctx.strokeStyle = 'rgba(224,242,254,0.9)'; ctx.lineWidth = 1.5; ctx.stroke(); ctx.restore();
        for (var k = -3; k <= 3; k++) { if (!k) { continue; } var y0 = cy + k * h * 0.26, d = [1, 0], p = [20, y0];   /* rayons parallèles : deux réfractions, à l'entrée et à la sortie */
          var xi = C1[0] - Math.sqrt(R * R - (y0 - cy) * (y0 - cy)), n1 = [(xi - C1[0]) / R, (y0 - cy) / R], d1 = refr(d, n1, 1, 1.5); if (!d1) { continue; }
          var fx = xi - C2[0], fy = y0 - C2[1], b = fx * d1[0] + fy * d1[1], c = fx * fx + fy * fy - R * R, t2 = -b + Math.sqrt(b * b - c), q = [xi + d1[0] * t2, y0 + d1[1] * t2], n2 = [(q[0] - C2[0]) / R, (q[1] - C2[1]) / R], d2 = refr(d1, n2, 1.5, 1); if (!d2) { continue; }
          var L = (W - 20 - q[0]) / d2[0]; ctx.strokeStyle = '#F87171'; ctx.lineWidth = 1.8; ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(xi, y0); ctx.lineTo(q[0], q[1]); ctx.lineTo(q[0] + d2[0] * L, q[1] + d2[1] * L); ctx.stroke(); }
        txt(ctx, 'lentille en verre', cx, cy - h - 16, { size: 11, col: '#E0F2FE' });
      } else {
        for (var k2 = -3; k2 <= 3; k2++) { if (!k2) { continue; } var y2 = cy + k2 * h * 0.26, fp = W * 0.28, X = W - 20, s = (cy - y2) / fp; ctx.strokeStyle = '#F87171'; ctx.lineWidth = 1.8; ctx.beginPath(); ctx.moveTo(20, y2); ctx.lineTo(cx, y2); ctx.lineTo(X, y2 + s * (X - cx)); ctx.stroke(); }   /* même déviation, mais d'un seul coup, dans le plan de la lentille */
        lentille(ctx, cx, cy, h, '#93C5FD'); point(ctx, cx, cy, '#FDE68A', 'O', -10, 16); txt(ctx, 'lentille mince (symbole)', cx, cy - h - 18, { size: 11, col: '#E0F2FE' });
      }
    }
    var TXT = { reel: 'Une lentille convergente a les bords plus minces que le centre. Chaque rayon est dévié deux fois, en entrant dans le verre puis en en sortant&nbsp;: c\u2019est la réfraction, étudiée au chapitre précédent.', modele: 'Pour une lentille mince, on ignore l\u2019épaisseur&nbsp;: on représente la lentille par ce symbole, et on fait comme si chaque rayon était dévié d\u2019un seul coup, en traversant le plan de la lentille. Le centre optique O est l\u2019intersection de la lentille et de l\u2019axe optique.' };
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 220 : 250; }, draw);
    $$(root, 'input[name="sc-m"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; msg.innerHTML = TXT[mode]; draw(cnv); }); });
    msg.innerHTML = TXT.reel; draw(cnv);
  })();

  /* =================== 3. Les foyers d'une lentille convergente =================== */
  (function () {
    var root = document.getElementById('lab-foyers'); if (!root) { return; }
    var inF = $(root, '[data-in="f"]'), msg = $(root, '.nt-msg'), mode = 'image', cnv;
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, cx = W / 2, cy = H / 2, u = Math.min(W / 30, 22), f = +inF.value * u, h = H * 0.38;
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#0B1120'); gf.addColorStop(1, '#172554'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      ctx.save(); ctx.setLineDash([8, 6]); ctx.strokeStyle = 'rgba(203,213,225,0.55)'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(10, cy); ctx.lineTo(W - 10, cy); ctx.stroke(); ctx.restore();
      if (mode === 'oblique') { ctx.save(); ctx.setLineDash([4, 5]); ctx.strokeStyle = 'rgba(253,230,138,0.45)'; ctx.beginPath(); ctx.moveTo(cx + f, 14); ctx.lineTo(cx + f, H - 14); ctx.stroke(); ctx.restore(); txt(ctx, 'plan focal image', cx + f + 6, 22, { size: 10, col: '#FDE68A', align: 'left' }); }
      ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.strokeStyle = 'rgba(248,113,113,0.85)'; ctx.lineWidth = 1.6;
      for (var k = -5; k <= 5; k++) {
        var y = cy + k * h * 0.17;
        if (mode === 'image') { var s = (cy - y) / f; ctx.beginPath(); ctx.moveTo(14, y); ctx.lineTo(cx, y); ctx.lineTo(W - 14, y + s * (W - 14 - cx)); ctx.stroke(); }
        else if (mode === 'objet') { if (Math.abs(y - cy) > h) { continue; } ctx.beginPath(); ctx.moveTo(cx - f, cy); ctx.lineTo(cx, y); ctx.lineTo(W - 14, y); ctx.stroke(); }   /* les rayons partent de F lui-même */
        else { var a = 0.22, yF = cy - Math.tan(a) * f, yl = y, xs = 14, ys = yl + Math.tan(a) * (cx - xs); ctx.beginPath(); ctx.moveTo(xs, ys); ctx.lineTo(cx, yl); var sx = (yF - yl) / f; ctx.lineTo(W - 14, yl + sx * (W - 14 - cx)); ctx.stroke(); }
      }
      ctx.restore();
      lentille(ctx, cx, cy, h + 8, '#93C5FD');
      point(ctx, cx - f, cy, '#FDE68A', 'F', 0, 18); point(ctx, cx + f, cy, '#FDE68A', 'F\u2032', 0, 18); point(ctx, cx, cy, '#E0F2FE', 'O', -10, 18);
      ctx.strokeStyle = '#FDE68A'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(cx, cy + 32); ctx.lineTo(cx + f, cy + 32); ctx.stroke(); vec(ctx, cx + 8, cy + 32, cx, cy + 32, '#FDE68A', 1.2, 7); vec(ctx, cx + f - 8, cy + 32, cx + f, cy + 32, '#FDE68A', 1.2, 7); txt(ctx, 'f\u2032', cx + f / 2, cy + 44, { size: 13, col: '#FDE68A', bold: true, serif: true });
      if (mode === 'oblique') { var yF2 = cy - Math.tan(0.22) * f; ctx.fillStyle = '#FDE68A'; ctx.beginPath(); ctx.arc(cx + f, yF2, 4.5, 0, 2 * Math.PI); ctx.fill(); }
    }
    var TXT = { image: 'Les rayons parallèles à l\u2019axe optique convergent tous vers un même point de l\u2019axe&nbsp;: le <b>foyer image</b> F\u2032. Diminuez la distance focale&nbsp;: la lentille est plus convergente, F\u2032 se rapproche.', objet: 'Les rayons issus du <b>foyer objet</b> F ressortent tous parallèles à l\u2019axe optique&nbsp;: c\u2019est le trajet précédent parcouru à l\u2019envers (principe du retour inverse de la lumière). F et F\u2032 sont symétriques par rapport à O.', oblique: 'Des rayons parallèles entre eux mais inclinés convergent aussi en un même point, situé dans le plan perpendiculaire à l\u2019axe qui passe par F\u2032 (le plan focal image). C\u2019est le cas des rayons venant d\u2019une étoile qui n\u2019est pas dans l\u2019axe.' };
    function texte() { $(root, '.out-f').textContent = fmt(+inF.value, 1) + '\u00A0cm'; msg.innerHTML = TXT[mode]; }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 260 : 300; }, draw);
    $$(root, 'input[name="fo-m"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; texte(); draw(cnv); }); });
    inF.addEventListener('input', function () { texte(); draw(cnv); });
    texte(); draw(cnv);
  })();

  var C1R = '#DC2626', C2R = '#0891B2', C3R = '#7C3AED';   /* rouge, bleu canard, violet : bien distincts */   /* couleurs des trois rayons particuliers */

  /* =================== 4. Construire l'image A'B' =================== */
  (function () {
    var root = document.getElementById('lab-construction'); if (!root) { return; }
    var inA = $(root, '[data-in="a"]'), inF = $(root, '[data-in="f"]'), msg = $(root, '.nt-msg'), cnv, R = { r1: false, r2: false, r3: false, faisceau: false }, hB = 3;
    function geo(o) { var W = o.W, H = o.H, a = +inA.value, f = +inF.value, ap = Math.abs(a - f) < 1e-6 ? 40 : a * f / (a - f), droite = Math.min(40, Math.max(f, ap > 0 ? ap : 0) + 3), gauche = Math.max(a, ap < 0 ? -ap : 0) + 2.5, vmax = Math.max(hB, Math.min(12, Math.abs(hB * ap / a))) + 1.5, u = Math.min((W - 20) / (gauche + droite), H * 0.46 / vmax, 26), cx = 10 + gauche * u, cy = H * 0.5; return {   /* … et en hauteur aussi */   /* l'échelle s'adapte pour que l'objet et l'image tiennent dans le dessin */ W: W, H: H, cx: cx, cy: cy, u: u, X: function (v) { return cx + v * u; }, Y: function (v) { return cy - v * u; } }; }
    function img() { var a = +inA.value, f = +inF.value; if (Math.abs(a - f) < 1e-6) { return null; } var ap = a * f / (a - f); return { a: a, f: f, ap: ap, g: ap / a, hp: -hB * ap / a }; }   /* ap > 0 : image réelle, après la lentille ; ap < 0 : image virtuelle, du côté de l'objet */
    function seg(ctx, G, x1, y1, x2, y2, col, w, dash) { ctx.save(); if (dash) { ctx.setLineDash(dash); } ctx.strokeStyle = col; ctx.lineWidth = w || 2; ctx.beginPath(); ctx.moveTo(G.X(x1), G.Y(y1)); ctx.lineTo(G.X(x2), G.Y(y2)); ctx.stroke(); ctx.restore(); }
    function prolong(x1, y1, x2, y2, xm) { return [xm, y1 + (y2 - y1) * (xm - x1) / (x2 - x1)]; }
    function draw(o) {
      var ctx = o.ctx, G = geo(o), W = G.W, H = G.H, I = img(), a = +inA.value, f = +inF.value, xmin = -(G.cx - 10) / G.u, xmax = (W - G.cx - 10) / G.u, ymax = (G.cy - 8) / G.u, ETQ = [], FIXE = [];
      function etiq(t, x, y, col) { ETQ.push({ t: t, x: x, y: y, col: col }); }   /* les étiquettes sont placées à la fin, en évitant les chevauchements */
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = '#EEF2F7'; ctx.lineWidth = 1; for (var gx = Math.ceil(xmin); gx <= xmax; gx++) { ctx.beginPath(); ctx.moveTo(G.X(gx), 0); ctx.lineTo(G.X(gx), H); ctx.stroke(); } for (var gy = -Math.floor(ymax); gy <= ymax; gy++) { ctx.beginPath(); ctx.moveTo(0, G.Y(gy)); ctx.lineTo(W, G.Y(gy)); ctx.stroke(); }   /* quadrillage : 1 carreau = 1 cm */
      seg(ctx, G, xmin, 0, xmax - 0.3, 0, '#64748B', 1.3, [8, 6]); vec(ctx, W - 22, G.cy, W - 8, G.cy, '#64748B', 1.3, 10);   /* axe optique, orienté */
      txt(ctx, 'axe optique', W - 8, G.cy - 10, { size: 10.5, col: '#475569', align: 'right' });
      var hl = Math.min(ymax - 0.5, 7); lentille(ctx, G.X(0), G.Y(0), hl * G.u, BLEU_L);
      var xB = -a, yB = hB, virtuel = I && I.ap < 0;
      function rayon(pts, col, virt, fl) {
        for (var i = 1; i < pts.length; i++) { seg(ctx, G, pts[i - 1][0], pts[i - 1][1], pts[i][0], pts[i][1], col, 2);
          if (fl) { var a0 = pts[i - 1], a1 = pts[i], apres = a0[0] >= -1e-9, dx = a1[0] - a0[0], dy = a1[1] - a0[1], t0 = apres ? Math.min(0.5, f * 0.5 / Math.max(0.1, dx)) : 0.5, mx = a0[0] + dx * t0, my = a0[1] + dy * t0, L = Math.hypot(dx, dy) || 1; vec(ctx, G.X(mx - dx / L * 0.4), G.Y(my - dy / L * 0.4), G.X(mx + dx / L * 0.4), G.Y(my + dy / L * 0.4), col, 2, 10); } }   /* après la lentille, la flèche est à mi-chemin du foyer : elle ne cache pas F' */
        if (virt) { seg(ctx, G, virt[0][0], virt[0][1], virt[1][0], virt[1][1], col, 1.4, [5, 4]); }
      }
      if (R.faisceau && I) { for (var k = -6; k <= 6; k++) { var yl = k * hl / 6.5, out; if (I.ap > 0) { out = prolong(0, yl, I.ap, I.hp, xmax); } else { out = prolong(I.ap, I.hp, 0, yl, xmax); } ctx.globalAlpha = 0.35; rayon([[xB, yB], [0, yl], out], '#0EA5E9', virtuel ? [[0, yl], [I.ap, I.hp]] : null); ctx.globalAlpha = 1; } }
      if (R.r1) { var e1 = prolong(xB, yB, 0, 0, xmax); rayon([[xB, yB], [0, 0], e1], C1R, virtuel ? [[0, 0], [I.ap, I.hp]] : null, true); }   /* ① par O, non dévié */
      if (R.r2) { var e2 = prolong(0, yB, f, 0, xmax); rayon([[xB, yB], [0, yB], e2], C2R, virtuel ? [[0, yB], [I.ap, I.hp]] : null, true); }   /* ② parallèle à l'axe, puis par F' */
      if (R.r3 && Math.abs(a - f) > 0.05) { var yL = yB * f / (f - a), e3 = [xmax, yL]; if (Math.abs(yL) < ymax + 4) {
        if (a < f) { seg(ctx, G, -f, 0, xB, yB, C3R, 1.4, [5, 4]); }   /* image virtuelle : la droite du rayon passe par F, en pointillés entre F et B */
        rayon([[xB, yB], [0, yL], e3], C3R, virtuel ? [[0, yL], [I.ap, yL]] : null, true); } }   /* ③ par F, puis parallèle à l'axe */
      fleche(ctx, G.X(xB), G.Y(0), G.Y(yB), VERT, 3); point(ctx, G.X(xB), G.Y(yB), VERT);
      ctx.fillStyle = 'rgba(22,163,74,0.18)'; ctx.beginPath(); ctx.arc(G.X(xB), G.Y(yB), 13, 0, 2 * Math.PI); ctx.fill();   /* poignée */
      etiq('B', G.X(xB), G.Y(yB) - 16, VERT); etiq('A', G.X(xB), G.cy + 16, VERT);
      var montre = R.r1 + R.r2 + R.r3 >= 2 || R.faisceau;
      if (I && montre) { var xi = I.ap, yi = I.hp; if (xi > xmin && xi < xmax && Math.abs(yi) < ymax + 1) { fleche(ctx, G.X(xi), G.Y(0), G.Y(yi), ROSE, 3, virtuel ? [5, 4] : null); point(ctx, G.X(xi), G.Y(yi), ROSE);
        etiq('B\u2032', G.X(xi), G.Y(yi) + (yi < 0 ? 18 : -16), ROSE); FIXE.push({ t: 'A\u2032', x: G.X(xi), y: G.cy + (yi < 0 ? -12 : 16), col: ROSE }); } }   /* B' sous le point (image réelle, renversée), au-dessus si l'image est virtuelle */
      point(ctx, G.X(-f), G.cy, '#0F172A'); point(ctx, G.X(f), G.cy, '#0F172A'); point(ctx, G.X(0), G.cy, '#0F172A');   /* foyers et centre optique, au premier plan */
      etiq('F', G.X(-f), G.cy + 16, '#0F172A'); etiq('F\u2032', G.X(f), G.cy + 16, '#0F172A'); etiq('O', G.X(0) - 10, G.cy + 16, '#0F172A');
      var pris = [{ x: W - 40, y: G.cy - 10, w: 66 }];   /* placement des étiquettes (la place du nom de l'axe est réservée) : on décale verticalement celles qui en chevauchent une autre */
      ETQ.forEach(function (e) {
        var w = 9 * e.t.length + 8, h = 16, y = e.y, essais = [0, 14, -14, 28, -28];
        for (var k = 0; k < essais.length; k++) { var yy = e.y + essais[k], bloque = pris.some(function (b) { return Math.abs(b.x - e.x) < (b.w + w) / 2 && Math.abs(b.y - yy) < h; }); if (!bloque) { y = yy; break; } }
        pris.push({ x: e.x, y: y, w: w });
        txt(ctx, e.t, e.x, y, { size: 13, col: e.col, bold: true, serif: true });
      });
      FIXE.forEach(function (e) { txt(ctx, e.t, e.x, e.y, { size: 13, col: e.col, bold: true, serif: true }); });   /* A' : à sa place, au premier plan, sans être déplacée */
    }
    function texte() {
      var I = img(), a = +inA.value, f = +inF.value, montre = R.r1 + R.r2 + R.r3 >= 2 || R.faisceau;
      $(root, '.out-a').textContent = fmt(a, 1) + '\u00A0cm'; $(root, '.out-f').textContent = fmt(f, 1) + '\u00A0cm';
      if (!montre) { msg.innerHTML = 'Tracez au moins deux des trois rayons particuliers issus de B&nbsp;: leur intersection donne B\u2032.'; return; }
      if (!I) { msg.innerHTML = 'L\u2019objet est sur le foyer objet&nbsp;: les rayons issus de B ressortent parallèles entre eux. Ils ne se croisent pas&nbsp;: l\u2019image est rejetée à l\u2019infini.'; return; }
      var t = I.ap > 0 ? ('Image <b>réelle</b>, <b>renversée</b>, ' + (I.g > 1.02 ? '<b>agrandie</b>' : (I.g < 0.98 ? '<b>réduite</b>' : 'de même taille que l\u2019objet')) + ', à $\\text{OA}\u2032 \\approx ' + String(fmt(I.ap, 1)).replace(',', '{,}') + '\\ \\text{cm}$ de la lentille. Grandissement&nbsp;: $\\gamma = \\dfrac{\\text{OA}\u2032}{\\text{OA}} \\approx ' + String(fmt(I.g, 2)).replace(',', '{,}') + '$.' + (I.ap > 30 ? ' L\u2019image est très loin, hors du dessin.' : ''))
        : ('L\u2019objet est entre F et la lentille&nbsp;: les rayons ressortent en divergeant et ne se croisent pas. Leurs <b>prolongements</b> (en pointillés) se croisent en B\u2032&nbsp;: l\u2019image est <b>virtuelle</b>, droite et agrandie ($\\gamma \\approx ' + String(fmt(-I.g, 2)).replace(',', '{,}') + '$). C\u2019est le principe de la loupe.');
      msg.innerHTML = t; typeset(msg);
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 300 : 380; }, draw);
    function maj() { texte(); draw(cnv); }
    ['r1', 'r2', 'r3', 'faisceau'].forEach(function (k) { var b = $(root, '[data-act="' + k + '"]'); b.addEventListener('click', function () { R[k] = !R[k]; b.classList.toggle('nt-btn-main', R[k]); maj(); }); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { ['r1', 'r2', 'r3', 'faisceau'].forEach(function (k) { R[k] = false; $(root, '[data-act="' + k + '"]').classList.remove('nt-btn-main'); }); maj(); });
    [inA, inF].forEach(function (i) { i.addEventListener('input', maj); });
    cnv.cv.style.touchAction = 'none';
    cnv.cv.addEventListener('pointerdown', function (e) {   /* on déplace l'objet en faisant glisser B */
      var G = geo(cnv), r = cnv.cv.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top; if (Math.hypot(x - G.X(-inA.value), y - G.Y(hB)) > 28) { return; }
      cnv.cv.setPointerCapture(e.pointerId);
      cnv.cv.onpointermove = function (ev) { var rr2 = cnv.cv.getBoundingClientRect(), xv = (ev.clientX - rr2.left - G.cx) / G.u, yv = (G.cy - (ev.clientY - rr2.top)) / G.u; inA.value = Math.max(2, Math.min(30, Math.round(-xv * 2) / 2)); hB = Math.max(1, Math.min(6, Math.round(yv * 2) / 2)); maj(); };
      cnv.cv.onpointerup = function () { cnv.cv.onpointermove = null; };
    });
    maj();
  })();

  /* =================== 5. Entraînement : exploiter une construction =================== */
  (function () {
    var root = document.getElementById('tr-image'); if (!root) { return; }
    var CAS = [[3, 2, 6], [4, 2, 4], [6, 2, 3], [6, 3, 6], [12, 3, 4], [8, 4, 8], [12, 4, 6]];   /* OA, f', OA' (en carreaux) : valeurs entières */
    function svgFl(x, y, ang, col, t) { t = t || 9; var a1 = ang + 2.7, a2 = ang - 2.7; return '<polygon points="' + x.toFixed(1) + ',' + y.toFixed(1) + ' ' + (x + t * Math.cos(a1)).toFixed(1) + ',' + (y + t * Math.sin(a1)).toFixed(1) + ' ' + (x + t * Math.cos(a2)).toFixed(1) + ',' + (y + t * Math.sin(a2)).toFixed(1) + '" fill="' + col + '"/>'; }   /* pointe de flèche en (x, y), dans la direction ang */
    function svgRayon(P, col) {   /* rayon en plusieurs segments, avec une flèche au milieu de chacun */
      var s = '<polyline points="' + P.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" fill="none" stroke="' + col + '" stroke-width="1.8"/>';
      for (var i = 1; i < P.length; i++) { var mx = (P[i - 1][0] + P[i][0]) / 2, my = (P[i - 1][1] + P[i][1]) / 2; s += svgFl(mx + 4 * Math.cos(Math.atan2(P[i][1] - P[i - 1][1], P[i][0] - P[i - 1][0])), my + 4 * Math.sin(Math.atan2(P[i][1] - P[i - 1][1], P[i][0] - P[i - 1][0])), Math.atan2(P[i][1] - P[i - 1][1], P[i][0] - P[i - 1][0]), col, 8); }
      return s;
    }
    function schema(a, f, ap, h, o) {
      var c = 24, hp = h * ap / a, R = Math.ceil(Math.max(h, hp)) + 2, xmin = -a - 2, xmax = ap + 3, W = (xmax - xmin) * c, Hh = 2 * R * c, cx = -xmin * c, cy = R * c, X = function (v) { return cx + v * c; }, Y = function (v) { return cy - v * c; };   /* l'axe et la lentille tombent sur des lignes du quadrillage */
      var s = '<svg class="nt-qsvg" viewBox="0 0 ' + W + ' ' + Hh + '" width="' + Math.min(W, 460) + '" role="img" aria-label="construction de l\u2019image">';
      for (var i = 0; i <= W / c; i++) { s += '<line x1="' + i * c + '" y1="0" x2="' + i * c + '" y2="' + Hh + '" stroke="#E2E8F0"/>'; } for (var k = 0; k <= Hh / c; k++) { s += '<line x1="0" y1="' + k * c + '" x2="' + W + '" y2="' + k * c + '" stroke="#E2E8F0"/>'; }
      s += '<line x1="2" y1="' + cy + '" x2="' + (W - 4) + '" y2="' + cy + '" stroke="#64748B" stroke-dasharray="6 4"/>' + svgFl(W - 2, cy, 0, '#64748B', 10);   /* axe optique, orienté */
      var hl = (R - 0.6) * c; s += '<line x1="' + cx + '" y1="' + (cy - hl) + '" x2="' + cx + '" y2="' + (cy + hl) + '" stroke="#2563EB" stroke-width="2.5"/>' + svgFl(cx, cy - hl, -Math.PI / 2, '#2563EB', 11) + svgFl(cx, cy + hl, Math.PI / 2, '#2563EB', 11);   /* lentille convergente */
      if (o.rayons) { s += svgRayon([[X(-a), Y(h)], [X(0), Y(0)], [X(ap), Y(-hp)], [X(ap + 2), Y(-hp - 2 * hp / ap)]], '#DC2626') + svgRayon([[X(-a), Y(h)], [X(0), Y(h)], [X(ap), Y(-hp)], [X(ap + 2), Y(-hp - 2 * (h + hp) / ap)]], '#0891B2'); }
      s += '<circle cx="' + cx + '" cy="' + cy + '" r="3" fill="#0F172A"/><text x="' + (cx - 10) + '" y="' + (cy + 15) + '" font-size="12" font-weight="700" fill="#0F172A">O</text>';
      if (o.foyers) { [[X(-f), 'F'], [X(f), 'F\u2032']].forEach(function (q) { s += '<circle cx="' + q[0] + '" cy="' + cy + '" r="3" fill="#0F172A"/><text x="' + q[0] + '" y="' + (cy + 15) + '" font-size="12" font-weight="700" text-anchor="middle" fill="#0F172A">' + q[1] + '</text>'; }); }
      s += '<line x1="' + X(-a) + '" y1="' + cy + '" x2="' + X(-a) + '" y2="' + (Y(h) + 6) + '" stroke="#16A34A" stroke-width="3"/>' + svgFl(X(-a), Y(h), -Math.PI / 2, '#16A34A', 10) + '<text x="' + (X(-a) - 12) + '" y="' + (Y(h) + 4) + '" font-size="12" font-weight="700" fill="#16A34A">B</text><text x="' + X(-a) + '" y="' + (cy + 15) + '" font-size="12" font-weight="700" text-anchor="middle" fill="#16A34A">A</text>';
      if (o.rayons) { s += '<line x1="' + X(ap) + '" y1="' + cy + '" x2="' + X(ap) + '" y2="' + (Y(-hp) - 6) + '" stroke="#DB2777" stroke-width="3"/>' + svgFl(X(ap), Y(-hp), Math.PI / 2, '#DB2777', 10) + '<text x="' + X(ap) + '" y="' + (Y(-hp) + 18) + '" font-size="12" font-weight="700" text-anchor="middle" fill="#DB2777">B\u2032</text><text x="' + X(ap) + '" y="' + (cy - 7) + '" font-size="12" font-weight="700" text-anchor="middle" fill="#DB2777">A\u2032</text>'; }
      return s + '</svg><span class="nt-note">Échelle&nbsp;: 1 carreau = ' + o.echelle + '.</span>';
    }
    function cm(v) { return fmt(v, Math.abs(v - Math.round(v)) < 1e-9 ? 0 : (Math.abs(v * 10 - Math.round(v * 10)) < 1e-9 ? 1 : 2)) + ' cm'; }
    function uniq(t) { return t.filter(function (v, i) { return t.indexOf(v) === i; }); }
    function fab() {
      var Q = [], L = shuffle(CAS.slice());
      [0, 1, 2, 3, 4, 5].forEach(function (typ, k) {
        var cs = L[k % L.length], a = cs[0], f = cs[1], ap = cs[2], h = a >= ap ? 2 : 1, hp = h * ap / a, g = ap / a;
        if (typ === 0) { var e0 = pick([1, 2]), un0 = e0 === 1 ? '1 cm' : '2 cm'; Q.push(['Sur ce schéma, les foyers ne sont pas indiqués. Quelle est la distance focale de la lentille&nbsp;?' + schema(a, f, ap, h, { rayons: true, foyers: false, echelle: un0 }), uniq([cm(f * e0), cm(ap * e0), cm((ap - f) * e0 || f * e0 + 1)]), 'Le rayon qui arrive parallèlement à l\u2019axe (en bleu) ressort en passant par le foyer image F\u2032&nbsp;: il coupe l\u2019axe à ' + f + '&nbsp;carreaux de O. Avec l\u2019échelle, $f\u2032 = ' + f + ' \\times ' + e0 + '\\ \\text{cm} = ' + (f * e0) + '\\ \\text{cm}$.']); }
        else if (typ === 1) { Q.push(['À quelle distance de la lentille se forme l\u2019image&nbsp;?' + schema(a, f, ap, h, { rayons: true, foyers: true, echelle: '0,5 cm' }), uniq([cm(ap * 0.5), cm(ap), cm((ap - f) * 0.5)]), 'On compte ' + ap + '&nbsp;carreaux entre O et A\u2032 (et non entre F\u2032 et A\u2032). Avec l\u2019échelle&nbsp;: $\\text{OA}\u2032 = ' + ap + ' \\times 0{,}5\\ \\text{cm} = ' + String(fmt(ap * 0.5, 1)).replace(',', '{,}') + '\\ \\text{cm}$.']); }
        else if (typ === 2) { Q.push(['Quel est le grandissement&nbsp;?' + schema(a, f, ap, h, { rayons: true, foyers: true, echelle: '1 cm' }), uniq([fmt(g, 2), fmt(1 / g, 2), fmt(ap / f, 2)]), '$\\gamma = \\dfrac{\\text{OA}\u2032}{\\text{OA}} = \\dfrac{' + ap + '}{' + a + '} \\approx ' + String(fmt(g, 2)).replace(',', '{,}') + '$ (on peut aussi faire le rapport des tailles&nbsp;: $\\dfrac{\\text{A}\u2032\\text{B}\u2032}{\\text{AB}}$).']); }
        else if (typ === 3) { Q.push(['Quelle est la taille réelle de l\u2019image&nbsp;?' + schema(a, f, ap, h, { rayons: true, foyers: true, echelle: '2 cm' }), uniq([cm(hp * 2), cm(hp), cm(h * 2)]), 'L\u2019image mesure ' + fmt(hp, hp % 1 ? 1 : 0) + '&nbsp;carreau' + (hp > 1 ? 'x' : '') + ' sur le schéma, soit $\\text{A}\u2032\\text{B}\u2032 = ' + String(fmt(hp * 2, hp % 1 ? 1 : 0)).replace(',', '{,}') + '\\ \\text{cm}$ avec l\u2019échelle (1 carreau = 2 cm).']); }
        else if (typ === 4) { var bon = g > 1.01 ? 'réelle, renversée et agrandie' : (g < 0.99 ? 'réelle, renversée et réduite' : 'réelle, renversée, de même taille'); Q.push(['Comment est l\u2019image&nbsp;?' + schema(a, f, ap, h, { rayons: true, foyers: true, echelle: '1 cm' }), uniq([bon, g > 1.01 ? 'réelle, renversée et réduite' : 'réelle, renversée et agrandie', g > 1.01 ? 'virtuelle, droite et agrandie' : 'réelle, droite et réduite']), 'Les rayons se croisent réellement en B\u2032&nbsp;: l\u2019image est réelle. Elle est de l\u2019autre côté de l\u2019axe&nbsp;: renversée. ' + (g > 1.01 ? 'Elle est plus grande que l\u2019objet&nbsp;: agrandie ($\\gamma > 1$).' : (g < 0.99 ? 'Elle est plus petite que l\u2019objet&nbsp;: réduite ($\\gamma < 1$).' : 'Elle a la même taille que l\u2019objet ($\\gamma = 1$)&nbsp;: l\u2019objet est à $2f\u2032$ de la lentille.'))]); }
        else { var Hm = pick([1.5, 1.6, 1.8]), D = pick([2, 3, 4]), v = pick([3.5, 4, 5]), r = Hm * 100 * v / (D * 100); Q.push(['Un appareil photo photographie une personne de ' + fmt(Hm, 2) + '&nbsp;m, située à ' + fmt(D, 1) + '&nbsp;m de l\u2019objectif. L\u2019image se forme sur le capteur, à ' + fmt(v, 1) + '&nbsp;cm de l\u2019objectif. Quelle est la taille de l\u2019image&nbsp;?', uniq([cm(r), cm(r * 100), fmt(Hm * D / v * 100, 0) + ' cm', cm(r * 10)]).slice(0, 3), 'Les distances doivent être dans la même unité&nbsp;: $\\gamma = \\dfrac{\\text{OA}\u2032}{\\text{OA}} = \\dfrac{' + String(fmt(v, 1)).replace(',', '{,}') + '\\ \\text{cm}}{' + D * 100 + '\\ \\text{cm}} \\approx ' + String(fmt(v / (D * 100), 4)).replace(',', '{,}') + '$, donc $\\text{A}\u2032\\text{B}\u2032 = \\gamma \\times \\text{AB} \\approx ' + String(fmt(r, 2)).replace(',', '{,}') + '\\ \\text{cm}$. L\u2019image est très réduite.']); }
      });
      return Q;
    }
    Quiz(root, null, 6, fab);
  })();

  /* =================== 6. L'écran, la lentille et l'image =================== */
  (function () {
    var root = document.getElementById('lab-ecran'); if (!root) { return; }
    var inE = $(root, '[data-in="e"]'), inC = $(root, '[data-in="c"]'), msg = $(root, '.nt-msg'), cnv;
    function lettreF(ctx, x, y, s, col) { ctx.fillStyle = col; ctx.beginPath(); ctx.rect(x - s * 0.3, y - s, s * 0.22, 2 * s); ctx.rect(x - s * 0.08, y - s, s * 0.48, s * 0.24); ctx.rect(x - s * 0.08, y - s * 0.12, s * 0.28, s * 0.22); ctx.fill(); }   /* barres juxtaposées, sans recouvrement : la lettre est uniforme */
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, two = W >= 620, hs = two ? H : H * 0.56, cy = hs * 0.46, rail = hs - 30, x0 = 44, xl = two ? W * 0.25 : W * 0.36, a = xl - x0, f = a * 0.4, ap = a * f / (a - f), xi = xl + ap, span = Math.min(ap * 0.55, (two ? W * 0.62 : W - 16) - xi), xs = xi + (+inE.value / 100) * span, hl = hs * 0.3, cache = +inC.value / 100, hB = hs * 0.15, hBp = -hB * ap / a;
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#0B1120'); gf.addColorStop(1, '#111827'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      var xm = two ? W * 0.64 : W - 6, gr = ctx.createLinearGradient(0, rail, 0, rail + 12); gr.addColorStop(0, '#94A3B8'); gr.addColorStop(1, '#334155'); ctx.fillStyle = gr; rr(ctx, 8, rail, xm - 14, 12, 3); ctx.fill();   /* banc d'optique */
      ctx.fillStyle = 'rgba(15,23,42,0.8)'; for (var g = 14; g < xm - 10; g += 10) { ctx.fillRect(g, rail + 1, 1, g % 50 < 10 ? 6 : 3); }
      function support(x, y) { ctx.fillStyle = '#475569'; ctx.fillRect(x - 2, y, 4, rail - y); ctx.fillStyle = '#64748B'; rr(ctx, x - 10, rail - 4, 20, 6, 2); ctx.fill(); }
      ctx.save(); ctx.setLineDash([7, 6]); ctx.strokeStyle = 'rgba(203,213,225,0.35)'; ctx.beginPath(); ctx.moveTo(8, cy); ctx.lineTo(xm - 8, cy); ctx.stroke(); ctx.restore();
      var hautVisible = cy - hl + 2 * hl * cache;   /* la partie haute de la lentille est cachée */
      [[cy - hB, cy - hBp, '253,224,71'], [cy, cy, '251,146,60']].forEach(function (P) {   /* pinceaux issus de B (jaune) et de A (orange), limités à la partie visible de la lentille */
        var yh = Math.max(hautVisible, cy - hl), yb2 = cy + hl; if (yh >= yb2) { return; }
        var t = (xs - xl) / (xi - xl), e1 = yh + (P[1] - yh) * t, e2 = yb2 + (P[1] - yb2) * t;
        ctx.fillStyle = 'rgba(' + P[2] + ',0.16)'; ctx.beginPath(); ctx.moveTo(x0, P[0]); ctx.lineTo(xl, yh); ctx.lineTo(xs, e1); ctx.lineTo(xs, e2); ctx.lineTo(xl, yb2); ctx.closePath(); ctx.fill();
        ctx.strokeStyle = 'rgba(' + P[2] + ',0.9)'; ctx.lineWidth = 1.3; [[yh, e1], [yb2, e2]].forEach(function (r) { ctx.beginPath(); ctx.moveTo(x0, P[0]); ctx.lineTo(xl, r[0]); ctx.lineTo(xs, r[1]); ctx.stroke(); });
      });
      support(x0, cy + 18); var gb = ctx.createLinearGradient(x0 - 16, 0, x0 + 4, 0); gb.addColorStop(0, '#334155'); gb.addColorStop(1, '#64748B'); ctx.fillStyle = gb; rr(ctx, x0 - 22, cy - hB - 12, 22, hB + 30, 4); ctx.fill();   /* lanterne */
      ctx.fillStyle = '#FDE047'; ctx.shadowColor = 'rgba(253,224,71,0.8)'; ctx.shadowBlur = 10; ctx.fillRect(x0 - 2, cy - hB, 4, hB); ctx.shadowBlur = 0; txt(ctx, 'objet', 6, cy + 30, { size: 10, col: '#CBD5E1', align: 'left' });
      support(xl, cy + hl + 8); lentille(ctx, xl, cy, hl + 6, '#93C5FD');
      if (cache > 0) { var gc = ctx.createLinearGradient(xl - 10, 0, xl + 10, 0); gc.addColorStop(0, '#0F172A'); gc.addColorStop(0.5, '#334155'); gc.addColorStop(1, '#0F172A'); ctx.fillStyle = gc; rr(ctx, xl - 9, cy - hl - 10, 18, 2 * hl * cache + 10, 3); ctx.fill(); ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1; ctx.stroke(); txt(ctx, 'cache', xl + 14, cy - hl - 2, { size: 10, col: '#94A3B8', align: 'left' }); }
      ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = 'rgba(244,114,182,0.7)'; ctx.beginPath(); ctx.moveTo(xi, cy - hl); ctx.lineTo(xi, cy + hl); ctx.stroke(); ctx.restore(); txt(ctx, 'image', xi, cy + hl + 10, { size: 10, col: '#F9A8D4' });
      support(xs, cy + hl + 10); var gs = ctx.createLinearGradient(xs - 3, 0, xs + 4, 0); gs.addColorStop(0, '#CBD5E1'); gs.addColorStop(1, '#F8FAFC'); ctx.fillStyle = gs; rr(ctx, xs - 3, cy - hl - 10, 7, 2 * hl + 22, 2); ctx.fill(); txt(ctx, 'écran', xs, cy - hl - 20, { size: 10, col: '#E2E8F0' });
      /* ce qu'on voit sur l'écran : chaque point de l'objet donne un disque, de rayon proportionnel à l'écart entre l'écran et l'image */
      var px = two ? W * 0.67 : 20, py = two ? 30 : hs + 16, pw = two ? W * 0.3 : W - 40, ph = two ? H - 56 : H - hs - 28, blur = Math.abs(xs - xi) / (xi - xl) * hl * (1 - cache), lum = 1 - cache, dy = (xs - xi) / (xi - xl) * hl * cache;   /* rayon des disques ; décalage du centre des disques quand on cache le haut */
      txt(ctx, 'sur l\u2019écran', px + pw / 2, py - 12, { size: 11, col: '#E2E8F0', bold: true });
      var c0 = [30, 41, 59], c1 = [253, 240, 150], cF = 'rgb(' + c0.map(function (v, i) { return Math.round(v + (c1[i] - v) * lum); }).join(',') + ')';   /* couleur opaque de la lettre, d'autant plus sombre qu'il passe moins de lumière */
      ctx.save(); rr(ctx, px, py, pw, ph, 8); ctx.clip();
      flouDisque(ctx, px, py, pw, ph, Math.min(ph * 0.4, blur * 0.8), function (c2, w, h) { var gp = c2.createRadialGradient(w / 2, h / 2, 10, w / 2, h / 2, Math.max(w, h) * 0.75); gp.addColorStop(0, '#334155'); gp.addColorStop(1, '#1E293B'); c2.fillStyle = gp; c2.fillRect(-60, -60, w + 120, h + 120); c2.translate(w / 2, h / 2 + dy * 0.6); c2.rotate(Math.PI); lettreF(c2, 0, 0, h * 0.28, cF); });   /* image de la lettre F, renversée (tournée d'un demi-tour) */
      ctx.restore(); ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.5; rr(ctx, px, py, pw, ph, 8); ctx.stroke();
    }
    function texte() {
      var e = +inE.value, c = +inC.value; $(root, '.out-e').textContent = e === 0 ? 'sur l\u2019image' : (e < 0 ? 'trop près de la lentille' : 'trop loin de la lentille'); $(root, '.out-c').textContent = c + '\u00A0%';
      msg.innerHTML = (Math.abs(e) < 4 ? 'L\u2019écran est à l\u2019endroit où les rayons se croisent&nbsp;: l\u2019image est <b>nette</b> (et renversée).' : 'L\u2019écran n\u2019est pas à l\u2019endroit de l\u2019image&nbsp;: il intercepte des rayons qui ' + (e < 0 ? 'convergent vers' : 'divergent depuis') + ' les points images. Chaque point de l\u2019objet donne une tache&nbsp;: l\u2019image est <b>floue</b>.') + (c > 0 ? ' Avec ' + c + '&nbsp;% de la lentille caché' + (c > 1 ? 's' : '') + ', l\u2019image est toujours <b>complète</b>, mais moins lumineuse.' : '');
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 620 ? 430 : 280; }, draw);
    [inE, inC].forEach(function (i) { i.addEventListener('input', function () { texte(); draw(cnv); }); });
    texte(); draw(cnv);
  })();

  /* =================== 7. Coupe de l'œil humain =================== */
  (function () {
    var root = document.getElementById('lab-oeilreel'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), cnv, sel = -1, ZONES = [];
    var P = [   /* nom, rôle, position relative de la cible (par rapport au centre, en rayons), position de l'étiquette */
      ['cornée', 'Membrane transparente et bombée, à l\u2019avant de l\u2019œil&nbsp;: c\u2019est elle qui fait l\u2019essentiel de la convergence de la lumière.', [-1.045, -0.24], [-1.5, -0.95]],   /* sur l'arc de la cornée */
      ['iris', 'Partie colorée de l\u2019œil. Ses muscles agrandissent ou rétrécissent la pupille, pour régler la quantité de lumière qui entre&nbsp;: c\u2019est un diaphragme.', [-0.78, -0.42], [-0.95, -1.25]],
      ['pupille', 'Ouverture au centre de l\u2019iris, par laquelle la lumière entre dans l\u2019œil. Elle paraît noire, car presque aucune lumière n\u2019en ressort.', [-0.8, -0.155], [-1.8, -0.42]],
      ['cristallin', 'Lentille souple et transparente. Des muscles la bombent plus ou moins, pour ajuster la distance focale de l\u2019œil&nbsp;: c\u2019est l\u2019accommodation.', [-0.58, 0.18], [-0.75, 1.25]],
      ['humeur aqueuse', 'Liquide transparent entre la cornée et le cristallin.', [-0.93, 0.25], [-1.6, 0.85]],
      ['humeur vitrée', 'Gel transparent qui remplit l\u2019œil et lui donne sa forme.', [0.1, 0.3], [0.2, 1.3]],
      ['rétine', 'Fine membrane qui tapisse le fond de l\u2019œil, couverte de millions de cellules sensibles à la lumière (cônes et bâtonnets)&nbsp;: c\u2019est l\u2019écran sur lequel se forme l\u2019image.', [0.846, -0.308], [1.15, -1.05]],   /* sur la rétine (rayon 0,9 R) */
      ['nerf optique', 'Il transmet au cerveau les signaux produits par la rétine.', [1.25, 0.08], [1.55, 0.7]]
    ];
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, cx = W * 0.5, cy = H * 0.5, R = Math.min(W * 0.26, H * 0.36);
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#0F172A'); gf.addColorStop(1, '#1E3A8A'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      ctx.fillStyle = '#FDE68A'; ctx.beginPath(); ctx.moveTo(cx + R * 0.9, cy - R * 0.12); ctx.quadraticCurveTo(cx + R * 1.5, cy - R * 0.1, cx + R * 1.75, cy - R * 0.02); ctx.lineTo(cx + R * 1.75, cy + R * 0.2); ctx.quadraticCurveTo(cx + R * 1.5, cy + R * 0.15, cx + R * 0.9, cy + R * 0.16); ctx.fill();   /* nerf optique */
      var gs = ctx.createRadialGradient(cx - R * 0.2, cy - R * 0.3, R * 0.2, cx, cy, R * 1.05); gs.addColorStop(0, '#FFFFFF'); gs.addColorStop(1, '#E2E8F0'); ctx.fillStyle = gs; ctx.beginPath(); ctx.arc(cx, cy, R, 0, 2 * Math.PI); ctx.fill();   /* sclérotique (blanc de l'œil) */
      var gv = ctx.createRadialGradient(cx - R * 0.2, cy, R * 0.1, cx, cy, R * 0.9); gv.addColorStop(0, '#1E3A8A'); gv.addColorStop(1, '#172554'); ctx.fillStyle = gv; ctx.beginPath(); ctx.arc(cx, cy, R * 0.9, 0, 2 * Math.PI); ctx.fill();   /* humeur vitrée, sombre pour bien voir les rayons */
      ctx.strokeStyle = '#F97316'; ctx.lineWidth = 4; ctx.beginPath(); ctx.arc(cx, cy, R * 0.9, -Math.PI * 0.62, Math.PI * 0.62); ctx.stroke();   /* rétine */
      ctx.fillStyle = 'rgba(30,64,175,0.75)'; ctx.beginPath(); ctx.arc(cx - R * 0.55, cy, R * 0.55, Math.PI * 0.68, Math.PI * 1.32); ctx.closePath(); ctx.fill();   /* humeur aqueuse */
      ctx.strokeStyle = '#38BDF8'; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(cx - R * 0.55, cy, R * 0.55, Math.PI * 0.68, Math.PI * 1.32); ctx.stroke();   /* cornée */
      ctx.strokeStyle = '#7C2D12'; ctx.lineWidth = 6; ctx.beginPath(); ctx.moveTo(cx - R * 0.78, cy - R * 0.62); ctx.lineTo(cx - R * 0.78, cy - R * 0.17); ctx.moveTo(cx - R * 0.78, cy + R * 0.17); ctx.lineTo(cx - R * 0.78, cy + R * 0.62); ctx.stroke();   /* iris, et la pupille entre ses deux parties */
      var gc = ctx.createLinearGradient(cx - R * 0.72, 0, cx - R * 0.44, 0); gc.addColorStop(0, 'rgba(255,255,255,0.95)'); gc.addColorStop(1, 'rgba(191,219,254,0.95)'); ctx.fillStyle = gc; ctx.beginPath(); ctx.ellipse(cx - R * 0.58, cy, R * 0.13, R * 0.42, 0, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = '#60A5FA'; ctx.lineWidth = 1.5; ctx.stroke();   /* cristallin */
      ctx.save(); ctx.globalAlpha = 0.9; ctx.strokeStyle = '#FDE047'; ctx.lineWidth = 1.6; [-0.12, 0.12].forEach(function (s) { ctx.beginPath(); ctx.moveTo(6, cy + s * R); ctx.lineTo(cx - R * 0.6, cy + s * R); ctx.lineTo(cx + R * 0.9, cy - s * R * 0.4); ctx.stroke(); vec(ctx, cx - R * 1.95, cy + s * R, cx - R * 1.8, cy + s * R, '#FDE047', 1.6, 9); }); ctx.restore();   /* lumière qui arrive de loin devant l'œil */
      ZONES = [];
      P.forEach(function (p, k) {
        var tx = cx + p[2][0] * R, ty = cy + p[2][1] * R, lx = Math.max(46, Math.min(W - 46, cx + p[3][0] * R)), ly = Math.max(14, Math.min(H - 12, cy + p[3][1] * R)), on = k === sel;
        ctx.strokeStyle = on ? '#FDE047' : 'rgba(226,232,240,0.7)'; ctx.lineWidth = on ? 2 : 1; ctx.beginPath(); ctx.moveTo(tx, ty); ctx.lineTo(lx, ly); ctx.stroke(); ctx.fillStyle = on ? '#FDE047' : '#E2E8F0'; ctx.beginPath(); ctx.arc(tx, ty, 3, 0, 2 * Math.PI); ctx.fill();
        pill(ctx, p[0], lx, ly, { size: 11, col: on ? '#0F172A' : '#0F172A', bg: on ? '#FDE047' : 'rgba(255,255,255,0.92)' });
        ZONES.push([lx - 48, ly - 12, 96, 24, k], [tx - 14, ty - 14, 28, 28, k]);
      });
    }
    function choisir(k) { sel = k; draw(cnv); msg.innerHTML = k < 0 ? 'Touchez ou survolez une étiquette pour connaître le rôle de chaque partie de l\u2019œil.' : '<b>' + P[k][0].charAt(0).toUpperCase() + P[k][0].slice(1) + '.</b> ' + P[k][1]; }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 300 : 340; }, draw);
    function viser(e) { var r = cnv.cv.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top, k = -1; ZONES.forEach(function (z) { if (x >= z[0] && x <= z[0] + z[2] && y >= z[1] && y <= z[1] + z[3]) { k = z[4]; } }); return k; }
    cnv.cv.addEventListener('pointermove', function (e) { var k = viser(e); if (k >= 0 && k !== sel) { choisir(k); } });
    cnv.cv.addEventListener('pointerdown', function (e) { var k = viser(e); if (k >= 0) { choisir(k); } });
    choisir(-1);
  })();

  /* =================== 8. Le modèle de l'œil réduit =================== */
  (function () {
    var root = document.getElementById('lab-oeil'); if (!root) { return; }
    var inD = $(root, '[data-in="d"]'), cAcc = $(root, '[data-in="acc"]'), cVer = $(root, '[data-in="verre"]'), msg = $(root, '.nt-msg'), type = 'normal', cnv;
    var L = 0.017, P0 = 1 / L, AMP = 4, DEF = { normal: 0, myope: 3, hyper: -2 }, VER = { normal: 0, myope: -3, hyper: 2 };   /* œil réduit : rétine à 17 mm ; puissance au repos 58,8 δ ; amplitude d'accommodation 4 δ */
    function dist() { var k = +inD.value; return k >= 100 ? Infinity : 0.1 * Math.pow(10, k / 100 * 2.3); }   /* de 10 cm à environ 20 m, puis l'infini */
    function etat() {
      var d = dist(), inv = isFinite(d) ? 1 / d : 0, Prepos = P0 + DEF[type], Pv = cVer.checked ? VER[type] : 0, Pbesoin = P0 + inv - Pv, P = Prepos;
      if (cAcc.checked) { P = Math.max(Prepos, Math.min(Prepos + AMP, Pbesoin)); }   /* l'œil accommode autant qu'il le peut */
      var Ptot = P + Pv, v = 1 / (Ptot - inv);   /* distance lentille-image (m) */
      return { d: d, P: P, Prepos: Prepos, v: v, net: Math.abs(v - L) < 0.00012, acc: P - Prepos };
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, E = etat(), two = W >= 620, hs = two ? H : H * 0.62, cy = hs / 2, xl = two ? W * 0.3 : W * 0.34, xr = two ? W * 0.66 : W - 26, s = (xr - xl) / L, ap = hs * 0.15;   /* échelle réelle : s pixels par mètre */
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#0B1120'); gf.addColorStop(1, '#172554'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      var ge = ctx.createRadialGradient((xl + xr) / 2, cy, 10, (xl + xr) / 2, cy, (xr - xl) * 0.75); ge.addColorStop(0, 'rgba(30,64,175,0.35)'); ge.addColorStop(1, 'rgba(30,64,175,0.05)'); ctx.fillStyle = ge; ctx.beginPath(); ctx.ellipse((xl + xr) / 2 + 4, cy, (xr - xl) * 0.6, hs * 0.42, 0, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = 'rgba(148,163,184,0.35)'; ctx.lineWidth = 1.5; ctx.stroke();   /* silhouette du globe oculaire */
      ctx.save(); ctx.setLineDash([7, 6]); ctx.strokeStyle = 'rgba(203,213,225,0.35)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(6, cy); ctx.lineTo(xr + 14, cy); ctx.stroke(); ctx.restore();
      var xv = xl + E.v * s, xo = isFinite(E.d) ? xl - E.d * s : -Infinity, Pv = cVer.checked ? VER[type] : 0, xg = xl - Math.min(60, xl * 0.4);   /* point image ; position réelle de l'objet (souvent hors du cadre) ; verre */
      ctx.save(); ctx.lineCap = 'round';
      for (var k = -3; k <= 3; k++) {
        var yl = cy + k * ap / 3, x0 = 6, y0;
        if (isFinite(E.d)) { y0 = xo >= 6 ? cy : cy + (yl - cy) * (x0 - xo) / (xl - xo); if (xo >= 6) { x0 = xo; } } else { y0 = yl; }   /* rayon issu de l'objet, à sa vraie distance */
        var t = (xr - xl) / (xv - xl), yr = yl + (cy - yl) * t;
        ctx.strokeStyle = 'rgba(253,224,71,0.18)'; ctx.lineWidth = 5; ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(xl, yl); ctx.lineTo(xr, yr); ctx.stroke();
        ctx.strokeStyle = '#FDE047'; ctx.lineWidth = 1.4; ctx.stroke();
        if (Math.abs(k) === 3) { var mx = (x0 + xl) / 2, my = y0 + (yl - y0) * (mx - x0) / (xl - x0); vec(ctx, mx - 6, my - (yl - y0) / (xl - x0) * 6, mx + 6, my + (yl - y0) / (xl - x0) * 6, '#FDE047', 1.4, 9); }
      }
      ctx.restore();
      if (isFinite(E.d) && xo >= 6) { ctx.fillStyle = '#FDE047'; ctx.beginPath(); ctx.arc(xo, cy, 5, 0, 2 * Math.PI); ctx.fill(); txt(ctx, 'objet', xo, cy - 14, { size: 10.5, col: '#FDE68A' }); }
      else { pill(ctx, isFinite(E.d) ? '\u2190 objet à ' + (E.d < 1 ? fmt(E.d * 100, 0) + ' cm' : fmt(E.d, 1) + ' m') + ', hors du cadre' : '\u2190 objet très éloigné\u00A0: rayons parallèles', 10, 18, { size: 10.5, col: '#FDE68A', bg: 'rgba(15,23,42,0.75)', align: 'left' }); }
      if (cVer.checked && type !== 'normal') { var conv = VER[type] > 0, gh = ap * 1.6; ctx.fillStyle = 'rgba(186,230,253,0.3)'; ctx.strokeStyle = '#7DD3FC'; ctx.lineWidth = 1.2; ctx.beginPath(); if (conv) { ctx.moveTo(xg, cy - gh); ctx.quadraticCurveTo(xg + 12, cy, xg, cy + gh); ctx.quadraticCurveTo(xg - 12, cy, xg, cy - gh); } else { ctx.moveTo(xg - 7, cy - gh); ctx.lineTo(xg + 7, cy - gh); ctx.quadraticCurveTo(xg, cy, xg + 7, cy + gh); ctx.lineTo(xg - 7, cy + gh); ctx.quadraticCurveTo(xg, cy, xg - 7, cy - gh); } ctx.fill(); ctx.stroke(); txt(ctx, 'verre ' + (conv ? 'convergent' : 'divergent'), xg, cy + gh + 14, { size: 10, col: '#7DD3FC' }); }
      var gi = ctx.createLinearGradient(0, cy - hs * 0.36, 0, cy + hs * 0.36); gi.addColorStop(0, '#92400E'); gi.addColorStop(0.5, '#B45309'); gi.addColorStop(1, '#92400E'); ctx.fillStyle = gi; rr(ctx, xl - 11, cy - hs * 0.34, 6, hs * 0.34 - ap - 3, 2); ctx.fill(); rr(ctx, xl - 11, cy + ap + 3, 6, hs * 0.34 - ap - 3, 2); ctx.fill();   /* diaphragme (iris) */
      pill(ctx, 'diaphragme (iris)', xl - 8, cy - hs * 0.34 - 12, { size: 10, col: '#FDBA74', bg: 'rgba(15,23,42,0.7)' });
      var bomb = 0.35 + E.acc / AMP * 0.6, lh = ap * 1.45, gl = ctx.createLinearGradient(xl - 10, 0, xl + 10, 0); gl.addColorStop(0, 'rgba(186,230,253,0.55)'); gl.addColorStop(0.5, 'rgba(255,255,255,0.9)'); gl.addColorStop(1, 'rgba(186,230,253,0.55)');
      ctx.fillStyle = gl; ctx.beginPath(); ctx.moveTo(xl, cy - lh); ctx.quadraticCurveTo(xl + lh * bomb, cy, xl, cy + lh); ctx.quadraticCurveTo(xl - lh * bomb, cy, xl, cy - lh); ctx.fill(); ctx.strokeStyle = '#93C5FD'; ctx.lineWidth = 1.2; ctx.stroke();   /* lentille, plus bombée quand l'œil accommode */
      pill(ctx, 'lentille (cornée + cristallin)', xl, cy + lh + 16, { size: 10, col: '#BFDBFE', bg: 'rgba(15,23,42,0.7)' });
      ctx.strokeStyle = '#F97316'; ctx.lineWidth = 4; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(xr, cy - hs * 0.32); ctx.lineTo(xr, cy + hs * 0.32); ctx.stroke(); ctx.lineCap = 'butt'; pill(ctx, 'rétine (écran)', Math.min(xr, W - 50), cy - hs * 0.32 - 12, { size: 10, col: '#FDBA74', bg: 'rgba(15,23,42,0.7)' });
      ctx.strokeStyle = 'rgba(203,213,225,0.6)'; ctx.lineWidth = 1; var yd = cy + hs * 0.4; ctx.beginPath(); ctx.moveTo(xl, yd); ctx.lineTo(xr, yd); ctx.stroke(); vec(ctx, xl + 10, yd, xl, yd, 'rgba(203,213,225,0.8)', 1, 7); vec(ctx, xr - 10, yd, xr, yd, 'rgba(203,213,225,0.8)', 1, 7); txt(ctx, '17 mm', (xl + xr) / 2, yd + 12, { size: 10, col: '#CBD5E1' });
      if (xv > xl && xv < W - 4) { var gp = ctx.createRadialGradient(xv, cy, 0, xv, cy, 10); gp.addColorStop(0, E.net ? 'rgba(134,239,172,1)' : 'rgba(249,168,212,1)'); gp.addColorStop(1, 'rgba(0,0,0,0)'); ctx.fillStyle = gp; ctx.beginPath(); ctx.arc(xv, cy, 10, 0, 2 * Math.PI); ctx.fill(); txt(ctx, 'image', xv, cy - 14, { size: 10, col: E.net ? '#86EFAC' : '#F9A8D4' }); }
      if (two) pill(ctx, 'distance focale\u00A0: ' + fmt(1000 / (E.P + Pv), 1) + ' mm', (xl + xr) / 2 + 30, 18, { size: 10.5, col: '#E2E8F0', bg: 'rgba(15,23,42,0.75)' });
      var tache = Math.abs(xr - xv) / Math.max(1, xv - xl) * ap * 2;   /* ce que perçoit l'œil */
      var px = two ? W * 0.74 : 20, py = two ? 34 : hs + 16, pw = two ? W * 0.23 : W - 40, ph = two ? H - 68 : H - hs - 28;
      txt(ctx, 'ce que l\u2019on voit', px + pw / 2, py - 12, { size: 11, col: '#E2E8F0', bold: true });
      ctx.save(); rr(ctx, px, py, pw, ph, 10); ctx.clip();
      flouDisque(ctx, px, py, pw, ph, Math.min(ph * 0.25, tache * 0.9), function (c2, w, h) { c2.fillStyle = '#F8FAFC'; c2.fillRect(-60, -60, w + 120, h + 120); c2.font = 'bold ' + Math.round(h * 0.28) + 'px ' + FONT; c2.fillStyle = '#0F172A'; c2.textAlign = 'center'; c2.textBaseline = 'middle'; c2.fillText('E F P', w / 2, h * 0.38); c2.font = 'bold ' + Math.round(h * 0.15) + 'px ' + FONT; c2.fillText('T O Z', w / 2, h * 0.7); });
      ctx.restore(); ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.5; rr(ctx, px, py, pw, ph, 10); ctx.stroke();
    }
    function texte() {
      var E = etat(), d = E.d, nom = { normal: 'normal', myope: 'myope', hyper: 'hypermétrope' }[type];
      $(root, '.out-d').textContent = isFinite(d) ? (d < 1 ? fmt(d * 100, 0) + '\u00A0cm' : fmt(d, 1) + '\u00A0m') : 'très loin («\u00A0l\u2019infini\u00A0»)';
      var t = E.net ? 'L\u2019image se forme sur la rétine&nbsp;: la vision est <b>nette</b>.' : (E.v < L ? 'L\u2019image se forme <b>avant</b> la rétine&nbsp;: la vision est floue.' : 'L\u2019image se forme <b>après</b> la rétine&nbsp;: la vision est floue.');
      if (cAcc.checked && E.acc > 0.05) { t += ' L\u2019œil accommode&nbsp;: le cristallin se bombe' + (E.acc >= AMP - 0.01 ? ', au maximum de ses possibilités' : '') + '.'; }
      if (!cAcc.checked && isFinite(d) && type === 'normal' && !E.net) { t += ' Sans accommodation, un œil normal ne voit net que les objets éloignés.'; }
      if (type === 'myope' && !cVer.checked) { t += ' Œil myope&nbsp;: trop convergent, il voit flou de loin (et accommoder ne fait qu\u2019aggraver les choses), mais net de près.'; }
      if (type === 'hyper' && !cVer.checked) { t += ' Œil hypermétrope&nbsp;: pas assez convergent, il doit accommoder même pour voir de loin, et n\u2019y parvient plus de près.'; }
      if (cVer.checked && type !== 'normal') { t += ' Le verre ' + (type === 'myope' ? 'divergent' : 'convergent') + ' corrige le défaut.'; }
      var Pv2 = cVer.checked ? VER[type] : 0; t += ' (Distance focale de l\u2019œil' + (Pv2 ? ' et de son verre' : '') + '&nbsp;: ' + fmt(1000 / (E.P + Pv2), 1) + '&nbsp;mm.)';
      msg.innerHTML = t;
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 620 ? 420 : 300; }, draw);
    function maj() { texte(); draw(cnv); }
    $$(root, 'input[name="oe-t"]').forEach(function (r) { r.addEventListener('change', function () { type = r.value; maj(); }); });
    [inD, cAcc, cVer].forEach(function (i) { i.addEventListener(i === inD ? 'input' : 'change', maj); });
    maj();
  })();

  /* =================== 9. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    Quiz(root, [
      ['Former l\u2019image d\u2019un objet, c\u2019est…', ['associer un point image à chaque point objet', 'éclairer un écran avec l\u2019objet', 'agrandir l\u2019objet'], 'Un système stigmatique fait correspondre un point image à chaque point objet.'],
      ['Pourquoi l\u2019image d\u2019un sténopé est-elle peu lumineuse&nbsp;?', ['un seul mince pinceau de lumière passe de chaque point objet', 'le trou absorbe la lumière', 'l\u2019image est virtuelle'], 'Le petit trou ne laisse passer qu\u2019une infime partie de la lumière issue de chaque point.'],
      ['Un rayon parallèle à l\u2019axe optique ressort de la lentille en passant par…', ['le foyer image F\u2032', 'le foyer objet F', 'le centre optique O'], 'C\u2019est la définition du foyer image.'],
      ['Un rayon qui passe par le centre optique O…', ['n\u2019est pas dévié', 'ressort parallèle à l\u2019axe', 'passe par F\u2032'], 'C\u2019est le premier des trois rayons particuliers.'],
      ['La distance focale d\u2019une lentille convergente est la distance…', ['entre O et F\u2032', 'entre F et F\u2032', 'entre l\u2019objet et l\u2019image'], '$f\u2032 = \\text{OF}\u2032$.'],
      ['Un objet de 3,0 cm donne une image de 1,5 cm. Le grandissement vaut…', ['0,50', '2,0', '1,5'], '$\\gamma = \\dfrac{\\text{A}\u2032\\text{B}\u2032}{\\text{AB}} = \\dfrac{1{,}5}{3{,}0} = 0{,}50$.'],
      ['Pour obtenir une image réelle avec une lentille convergente, l\u2019objet doit être…', ['avant le foyer objet F', 'entre F et la lentille', 'au foyer objet F'], 'Entre F et la lentille, l\u2019image est virtuelle&nbsp;; sur F, elle est à l\u2019infini.'],
      ['Si l\u2019on cache la moitié de la lentille, l\u2019image…', ['reste entière, mais moins lumineuse', 'perd sa moitié', 'disparaît'], 'Chaque point image est formé par des rayons passés par toute la lentille.'],
      ['Dans le modèle de l\u2019œil réduit, la rétine joue le rôle…', ['de l\u2019écran', 'de la lentille', 'du diaphragme'], 'L\u2019image se forme sur la rétine.'],
      ['Quand un objet se rapproche, l\u2019œil accommode en…', ['bombant le cristallin pour diminuer sa distance focale', 'éloignant la rétine', 'fermant la pupille'], 'La distance lentille-rétine est fixe&nbsp;: c\u2019est la distance focale qui diminue.']
    ], 10);
  })();

})();
</script>
