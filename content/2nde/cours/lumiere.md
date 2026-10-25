+++
title = "Lumière"
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

<p class="nt-lead">Comment la lumière se propage-t-elle, et à quelle vitesse&nbsp;? De quoi la lumière blanche est-elle faite&nbsp;? Pourquoi un bâton plongé dans l'eau paraît-il cassé&nbsp;? Ce chapitre étudie la propagation de la lumière, sa décomposition en couleurs, les spectres, qui révèlent la composition chimique des étoiles, et les lois qui régissent la réflexion et la réfraction.</p>

## Propagation de la lumière {.nt-h2}

### La propagation rectiligne {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Dans un milieu transparent et <b>homogène</b> (qui a partout les mêmes propriétés), la lumière se propage <span class="imp nt-hole">en ligne droite</span>. On modélise son trajet par un <b>rayon lumineux</b>&nbsp;: une droite, orientée par une flèche dans le sens de propagation.</p>
</div>

<p>Les rayons de soleil qui percent les nuages, le faisceau d'un phare dans la brume, les rais de lumière dans un grenier poussiéreux&nbsp;: tous dessinent des lignes droites. Pourtant, ce n'est pas la lumière elle-même que l'on voit&nbsp;!</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Dans une pièce dont l'air est parfaitement pur, peut-on voir le faisceau d'un laser, sur le côté&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Non&nbsp;: on ne voit que la lumière qui entre dans l'œil</span></summary>
<div class="nt-d-body">
<p>Pour voir quelque chose, il faut que de la lumière qui en provient entre dans notre œil. La lumière du laser file en ligne droite&nbsp;: elle ne vient pas vers nous, et on ne voit rien. Dans les photos de rayons lumineux, ce sont les <b>poussières</b> ou les <b>gouttelettes d'eau</b>, éclairées par le faisceau, qui renvoient un peu de lumière dans toutes les directions&nbsp;: on dit qu'elles la <b>diffusent</b>. On ne voit pas le faisceau, on voit les poussières éclairées.</p>
</div>
</details>

<div class="nt-lab" id="lab-faisceau">
<p class="nt-tag"><i class="fa-solid fa-wand-magic-sparkles"></i>Animation</p>
<p class="nt-lab-title">Rendre visible un faisceau laser</p>
<canvas role="img" aria-label="Un laser traverse une pièce ; le faisceau n'est visible qu'aux endroits où des poussières ou des gouttelettes le diffusent vers l'œil."></canvas>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="fx-m" value="pur" checked><span>Air pur</span></label><label><input type="radio" name="fx-m" value="poussiere"><span>Un peu de poussière</span></label><label><input type="radio" name="fx-m" value="brume"><span>Brume (eau pulvérisée)</span></label></div></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### La vitesse de la lumière {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Dans le vide, et presque exactement dans l'air, la lumière se propage à la vitesse (ou <b>célérité</b>)&nbsp;:</p>
<p style="text-align:center">$c = \pu{3,00E8 m*s-1}$, soit environ 300&nbsp;000&nbsp;km par seconde.</p>
</div>

<p>C'est environ <b>un million de fois</b> plus rapide que le son dans l'air (340&nbsp;m·s<sup>−1</sup>). La lumière fait le tour de la Terre en environ 0,13&nbsp;s, et met environ 8&nbsp;minutes pour nous parvenir du Soleil.</p>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>qui se déplace&nbsp;?</th><th>vitesse (m·s<sup>−1</sup>)</th><th>soit</th></tr></thead>
<tbody>
<tr><td>un piéton</td><td>$\pu{1,4}$</td><td>5&nbsp;km·h<sup>−1</sup></td></tr>
<tr><td>un TGV</td><td>$\pu{8,3E1}$</td><td>300&nbsp;km·h<sup>−1</sup></td></tr>
<tr><td>le son dans l'air</td><td>$\pu{3,4E2}$</td><td>1&nbsp;200&nbsp;km·h<sup>−1</sup></td></tr>
<tr><td>la Station spatiale internationale</td><td>$\pu{7,7E3}$</td><td>28&nbsp;000&nbsp;km·h<sup>−1</sup></td></tr>
<tr><td>la Terre autour du Soleil</td><td>$\pu{3,0E4}$</td><td>107&nbsp;000&nbsp;km·h<sup>−1</sup></td></tr>
<tr><td>la lumière dans le vide</td><td>$\pu{3,00E8}$</td><td>1&nbsp;milliard de km·h<sup>−1</sup></td></tr>
</tbody>
</table></div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>La vitesse de la lumière dans le vide est l'une des constantes fondamentales de la physique. Depuis 1983, sa valeur est <b>fixée</b>&nbsp;: $c = \pu{299792458 m*s-1}$ exactement, et c'est elle qui sert à définir le mètre&nbsp;: la distance parcourue par la lumière dans le vide en $\dfrac{1}{\pu{299792458}}$ de seconde.</p>
</div>

<p>Dans les autres milieux transparents, la lumière va <b>moins vite</b> que dans le vide&nbsp;: environ 225&nbsp;000&nbsp;km·s<sup>−1</sup> dans l'eau, 200&nbsp;000&nbsp;km·s<sup>−1</sup> dans le verre, et seulement 124&nbsp;000&nbsp;km·s<sup>−1</sup> dans le diamant. Nous verrons que c'est ce changement de vitesse qui explique la réfraction.</p>

<div class="nt-lab" id="lab-course">
<p class="nt-tag"><i class="fa-solid fa-flag-checkered"></i>Animation</p>
<p class="nt-lab-title">La lumière fait la course</p>
<canvas role="img" aria-label="Cinq impulsions lumineuses partent en même temps dans le vide, l'air, l'eau, le verre et le diamant ; celle du vide arrive la première, celle du diamant la dernière."></canvas>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Départ&nbsp;!</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Comment a-t-on mesuré la vitesse de la lumière&nbsp;?</span></summary>
<div class="nt-d-body">
<p>En 1849, Hippolyte Fizeau envoie un faisceau de lumière à travers les dents d'une roue tournante, vers un miroir placé à 8,6&nbsp;km, sur la colline de Montmartre. La lumière revient par le même chemin. Si la roue a tourné juste assez, pendant l'aller-retour, pour qu'une dent remplace le creux par lequel la lumière était passée, la lumière est bloquée&nbsp;: l'observateur ne voit plus rien. Connaissant la vitesse de rotation de la roue, on en déduit la durée de l'aller-retour, et donc la vitesse de la lumière.</p>
<div class="nt-lab" id="lab-fizeau">
<p class="nt-tag"><i class="fa-solid fa-gear"></i>Animation</p>
<p class="nt-lab-title">La roue dentée de Fizeau</p>
<canvas role="img" aria-label="Une roue dentée tourne devant une source de lumière ; la lumière fait l'aller-retour jusqu'à un miroir lointain ; selon la vitesse de rotation, elle revient par un creux ou heurte une dent."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Vitesse de rotation de la roue&nbsp;: <b class="out-f"></b><input type="range" min="0" max="30" step="0.1" value="4" data-in="f"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>
<p>Fizeau trouva ainsi environ 315&nbsp;000&nbsp;km·s<sup>−1</sup>, à 5&nbsp;% près de la valeur actuelle. En 1862, Léon Foucault, avec un miroir tournant, obtint 298&nbsp;000&nbsp;km·s<sup>−1</sup>. Ces mesures ont été affinées jusqu'à ce que, en 1983, on décide de fixer la valeur de $c$.</p>
</div>
</details>

## Lumière blanche, lumières colorées {.nt-h2}

### La dispersion de la lumière blanche {.nt-h3}

<p>En 1666, Isaac Newton fait passer un rayon de soleil à travers un prisme de verre&nbsp;: sur le mur apparaît une bande colorée, du rouge au violet, avec toutes les couleurs de l'arc-en-ciel.</p>

<div class="nt-lab" id="lab-prisme">
<p class="nt-tag"><i class="fa-solid fa-rainbow"></i>Animation</p>
<p class="nt-lab-title">Un prisme sur le trajet de la lumière</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="pr-s" value="blanc" checked><span>Lumière blanche</span></label><label><input type="radio" name="pr-s" value="rouge"><span>Laser rouge</span></label><label><input type="radio" name="pr-s" value="vert"><span>Laser vert</span></label></div></div>
<canvas role="img" aria-label="Un faisceau de lumière traverse un prisme ; la lumière blanche est décomposée en un éventail de couleurs sur un écran, alors que la lumière d'un laser est déviée sans être décomposée."></canvas>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<ul class="nt-facts">
<li>Le prisme <span class="imp nt-hole">disperse</span> la lumière blanche&nbsp;: il la décompose en ses différentes composantes colorées. La figure obtenue est le <span class="imp nt-hole">spectre</span> de la lumière blanche.</li>
<li>Une lumière composée de plusieurs radiations, comme la lumière blanche, est dite <span class="imp nt-hole">polychromatique</span>. Une lumière composée d'une seule radiation, comme celle d'un laser, est dite <span class="imp nt-hole">monochromatique</span>&nbsp;: un prisme la dévie, mais ne la décompose pas.</li>
<li>Une radiation monochromatique est caractérisée par sa <span class="imp nt-hole">longueur d'onde</span> $\lambda$ (lettre grecque lambda) dans le vide ou dans l'air, exprimée le plus souvent en nanomètres&nbsp;: $\pu{1 nm} = \pu{1E-9 m}$.</li>
</ul>
</div>

<p>L'œil humain perçoit les radiations dont la longueur d'onde est comprise entre <b>400&nbsp;nm</b> (violet) et <b>800&nbsp;nm</b> (rouge) environ&nbsp;: c'est le domaine du <b>visible</b>. Au-delà s'étendent l'infrarouge et, en deçà, l'ultraviolet, invisibles pour nous.</p>

<div class="nt-lab" id="lab-visible">
<p class="nt-tag"><i class="fa-solid fa-palette"></i>Animation</p>
<p class="nt-lab-title">Le spectre de la lumière blanche</p>
<canvas role="img" aria-label="Le spectre de la lumière blanche, du violet à 400 nanomètres au rouge à 800 nanomètres, avec un curseur qui indique la couleur de chaque longueur d'onde."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Longueur d'onde&nbsp;: <b class="out-l"></b><input type="range" min="380" max="800" step="1" value="550" data-in="l"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Toutes les couleurs que nous pouvons percevoir sont-elles présentes dans le spectre de la lumière blanche&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Non&nbsp;: le magenta, par exemple, n'y est pas</span></summary>
<div class="nt-d-body">
<p>Le magenta (un rose violacé), le blanc, le gris ou le marron n'apparaissent nulle part dans le spectre&nbsp;: ce ne sont pas des couleurs de radiations monochromatiques. Notre œil les perçoit quand il reçoit un <b>mélange</b> de radiations&nbsp;: le magenta, par exemple, quand il reçoit à la fois du rouge et du bleu, sans vert.</p>
</div>
</details>

### Les spectres d'émission {.nt-h3}

<p>On analyse la lumière d'une source avec un <b>spectroscope</b>&nbsp;: un instrument qui la disperse, avec un prisme ou un <b>réseau</b> (une plaque gravée de milliers de traits très fins), pour en observer le spectre. Selon la source, on obtient deux sortes de spectres d'émission.</p>

<h4 class="nt-h4">Les spectres continus d'origine thermique</h4>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Un corps <b>chaud</b> et dense (le filament d'une lampe, la lave, une étoile…) émet un spectre <span class="imp nt-hole">continu</span>&nbsp;: toutes les couleurs y sont présentes, sans interruption. Quand sa température augmente, le corps émet plus de lumière, et son spectre <span class="imp nt-hole">s'enrichit vers le violet</span>&nbsp;: sa couleur passe du rouge sombre à l'orange, puis au blanc, puis au blanc bleuté.</p>
</div>

<div class="nt-lab" id="lab-thermique">
<p class="nt-tag"><i class="fa-solid fa-fire"></i>Animation</p>
<p class="nt-lab-title">Chauffer un corps de plus en plus</p>
<canvas role="img" aria-label="Un morceau de métal chauffé, dont la couleur change avec la température, et son spectre continu, qui s'étend progressivement vers le violet."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Température&nbsp;: <b class="out-t"></b><input type="range" min="800" max="12000" step="100" value="1500" data-in="t"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<h4 class="nt-h4">Les spectres de raies d'émission</h4>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Un <b>gaz</b> chauffé, ou traversé par une décharge électrique (comme dans les lampes spectrales ou les enseignes au néon), émet un spectre de <span class="imp nt-hole">raies</span>&nbsp;: quelques radiations seulement, qui apparaissent comme des raies colorées sur un fond noir.</p>
<p>Les longueurs d'onde de ces raies sont <span class="imp nt-hole">caractéristiques</span> de l'élément chimique qui les émet&nbsp;: c'est sa «&nbsp;signature&nbsp;», comme un code-barres.</p>
</div>

<div class="nt-lab" id="lab-raies">
<p class="nt-tag"><i class="fa-solid fa-barcode"></i>Animation</p>
<p class="nt-lab-title">Spectres de raies&nbsp;: émission et absorption</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="ra-e" value="H" checked><span>hydrogène</span></label><label><input type="radio" name="ra-e" value="He"><span>hélium</span></label><label><input type="radio" name="ra-e" value="Na"><span>sodium</span></label><label><input type="radio" name="ra-e" value="Hg"><span>mercure</span></label><label><input type="radio" name="ra-e" value="Ne"><span>néon</span></label></div></div>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="ra-m" value="em" checked><span>Émission (gaz chaud)</span></label><label><input type="radio" name="ra-m" value="ab"><span>Absorption (gaz froid éclairé en lumière blanche)</span></label></div></div>
<canvas role="img" aria-label="Le dispositif qui produit le spectre, et le spectre de raies de l'élément choisi, en émission ou en absorption ; les raies sont aux mêmes longueurs d'onde dans les deux cas."></canvas>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-fire-flame-curved"></i>Remarque&nbsp;: les flammes jaune-orangé</p>
<p>Le spectre du sodium est dominé par une raie jaune très intense, vers 589&nbsp;nm. Or le sel (le chlorure de sodium) est partout autour de nous, en particulier au bord de la mer, dans les embruns&nbsp;: dans une flamme, le sodium émet sa raie jaune, qui colore la flamme en jaune-orangé. C'est aussi la couleur des anciens lampadaires «&nbsp;au sodium&nbsp;» des routes.</p>
</div>

### Les spectres de raies d'absorption {.nt-h3}

<p>Que se passe-t-il si l'on éclaire un gaz froid avec de la lumière blanche&nbsp;? Le gaz <b>absorbe</b> certaines radiations&nbsp;: dans le spectre continu de la lumière qui l'a traversé, il manque quelques couleurs, qui apparaissent comme des <b>raies noires</b>. C'est un spectre de raies d'absorption. Essayez-le dans l'animation précédente, en mode «&nbsp;Absorption&nbsp;».</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Un gaz <b>absorbe</b> exactement les radiations qu'il est capable d'<b>émettre</b>&nbsp;: les raies noires de son spectre d'absorption sont aux <span class="imp nt-hole">mêmes longueurs d'onde</span> que les raies colorées de son spectre d'émission. Les deux spectres sont complémentaires, et permettent tous deux d'identifier l'élément.</p>
</div>

<p>C'est ainsi que l'on connaît la composition des étoiles, sans jamais y être allé. La lumière émise par la surface très chaude du Soleil (un spectre continu) traverse son atmosphère, plus froide, qui absorbe certaines radiations&nbsp;: le spectre du Soleil est parsemé de raies noires, découvertes par Joseph von Fraunhofer en 1814. En les comparant aux spectres des éléments connus au laboratoire, on y a reconnu l'hydrogène, le sodium, le magnésium, le fer, le calcium… et même un élément alors inconnu sur Terre, baptisé <b>hélium</b>, d'après le nom grec du Soleil, <i>hélios</i>.</p>

<div class="nt-lab" id="lab-soleil">
<p class="nt-tag"><i class="fa-solid fa-sun"></i>Animation</p>
<p class="nt-lab-title">Lire le spectre du Soleil</p>
<canvas role="img" aria-label="Le spectre du Soleil, avec ses raies noires d'absorption ; en dessous, les spectres d'émission de quelques éléments ; on cherche lesquels ont des raies aux mêmes longueurs d'onde."></canvas>
<div class="nt-btns"><span class="nt-note">Superposer le spectre d'émission&nbsp;:</span><div class="nt-seg" role="radiogroup"><label><input type="radio" name="so-e" value="" checked><span>aucun</span></label><label><input type="radio" name="so-e" value="H"><span>hydrogène</span></label><label><input type="radio" name="so-e" value="Na"><span>sodium</span></label><label><input type="radio" name="so-e" value="Mg"><span>magnésium</span></label><label><input type="radio" name="so-e" value="Hg"><span>mercure</span></label></div></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

## Réflexion et réfraction {.nt-h2}

### Le vocabulaire {.nt-h3}

<p>Quand la lumière arrive à la surface de séparation entre deux milieux transparents, comme l'air et l'eau, une partie est <b>réfléchie</b> (elle «&nbsp;rebondit&nbsp;» et reste dans le premier milieu), et une partie est <b>transmise</b> dans le second milieu, en changeant de direction&nbsp;: c'est la <b>réfraction</b>.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<ul class="nt-facts">
<li>Le <span class="imp nt-hole">rayon incident</span> arrive sur la surface de séparation au <b>point d'incidence</b> I&nbsp;; le <span class="imp nt-hole">rayon réfléchi</span> repart dans le premier milieu&nbsp;; le <span class="imp nt-hole">rayon réfracté</span> traverse vers le second milieu.</li>
<li>La <span class="imp nt-hole">normale</span> est la droite perpendiculaire à la surface de séparation, passant par le point d'incidence.</li>
<li>Les angles d'incidence $i_1$, de réflexion $r$ et de réfraction $i_2$ sont mesurés <b>entre la normale et le rayon</b> (et non entre la surface et le rayon&nbsp;!).</li>
</ul>
</div>

### L'indice optique {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp nt-hole">indice optique</span> (ou indice de réfraction) $n$ d'un milieu transparent est le rapport entre la vitesse de la lumière dans le vide, $c$, et sa vitesse $v$ dans ce milieu&nbsp;:</p>
<p style="text-align:center">$n = \dfrac{c}{v}$</p>
<p>C'est un nombre <b>sans unité</b>. Comme la lumière ne va jamais plus vite que dans le vide, $n \geq 1$.</p>
</div>

<div class="nt-scroll"><table class="nt-t">
<thead><tr><th>milieu</th><th>vide</th><th>air</th><th>eau</th><th>verre</th><th>diamant</th></tr></thead>
<tbody><tr><td>indice optique $n$</td><td>1 (exactement)</td><td>1,0003 ≈ 1,00</td><td>1,33</td><td>1,5 environ</td><td>2,42</td></tr></tbody>
</table></div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>À quelle vitesse la lumière se propage-t-elle dans un verre d'indice $n = 1,50$&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Deux cent mille kilomètres par seconde</span></summary>
<div class="nt-d-body">
<p>$n = \dfrac{c}{v}$ donc $v = \dfrac{c}{n} = \dfrac{\pu{3,00E8 m*s-1}}{1,50} = \pu{2,00E8 m*s-1}$, soit 200&nbsp;000&nbsp;km·s<sup>−1</sup>.</p>
</div>
</details>

### Les lois de Snell-Descartes {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: loi de la réflexion</p>
<p>Le rayon réfléchi est dans le plan formé par le rayon incident et la normale (le <b>plan d'incidence</b>), et l'angle de réflexion est égal à l'angle d'incidence.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$r = i_1$</p>
<div class="nt-f-units"><span>$i_1$&nbsp;: angle d'incidence</span><span>$r$&nbsp;: angle de réflexion</span><span>angles mesurés à partir de la <b>normale</b></span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir&nbsp;: loi de la réfraction</p>
<p>Le rayon réfracté est lui aussi dans le plan d'incidence, et les angles d'incidence et de réfraction sont liés aux indices optiques des deux milieux.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Formule</p>
<p class="nt-f-math">$n_1 \times \sin(i_1) = n_2 \times \sin(i_2)$</p>
<div class="nt-f-units"><span>$n_1$&nbsp;: indice du milieu d'incidence (sans unité)</span><span>$n_2$&nbsp;: indice du milieu de réfraction (sans unité)</span><span>$i_1$, $i_2$&nbsp;: angles d'incidence et de réfraction, mesurés à partir de la <b>normale</b></span></div>
</div>

<div class="nt-lab" id="lab-snell">
<p class="nt-tag"><i class="fa-solid fa-arrows-split-up-and-left"></i>Animation</p>
<p class="nt-lab-title">Réflexion et réfraction à la surface de séparation</p>
<div class="nt-milieux">
<div class="nt-mil"><span class="nt-mil-l">Milieu 1, en haut</span><div class="nt-seg nt-seg-mil" role="radiogroup" data-g="m1"></div></div>
<div class="nt-mil"><span class="nt-mil-l">Milieu 2, en bas</span><div class="nt-seg nt-seg-mil" role="radiogroup" data-g="m2"></div></div>
</div>
<div class="nt-ctrls"><label class="nt-ctrl">Angle d'incidence $i_1$&nbsp;: <b class="out-i"></b><input type="range" min="0" max="89" step="1" value="40" data-in="i"></label></div>
<canvas role="img" aria-label="Un rayon laser arrive sur la surface de séparation entre deux milieux ; on voit le rayon réfléchi, le rayon réfracté, la normale et les trois angles. On peut orienter le laser en le faisant glisser."></canvas>
<p class="nt-note nt-center">Faites glisser le laser, ou utilisez le curseur.</p>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Quand la lumière passe dans un milieu d'indice <b>plus grand</b> ($n_2 > n_1$), le rayon réfracté se <span class="imp nt-hole">rapproche de la normale</span>&nbsp;: $i_2 < i_1$.</li>
<li>Quand elle passe dans un milieu d'indice <b>plus petit</b> ($n_2 < n_1$), il <span class="imp nt-hole">s'éloigne de la normale</span>&nbsp;: $i_2 > i_1$.</li>
<li>Il n'y a réfraction (changement de direction) que si les deux milieux ont des indices <b>différents</b>. Un objet en verre plongé dans un liquide de même indice devient invisible&nbsp;!</li>
<li>Un rayon qui arrive perpendiculairement à la surface ($i_1 = 0$) n'est pas dévié.</li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Un rayon lumineux passe de l'air ($n_1 = 1,00$) dans l'eau ($n_2 = 1,33$) avec un angle d'incidence $i_1 = 50°$. Calculer l'angle de réfraction.</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Environ 35°</span></summary>
<div class="nt-d-body">
<p>D'après la loi de la réfraction, $\sin(i_2) = \dfrac{n_1 \times \sin(i_1)}{n_2} = \dfrac{1,00 \times \sin(50°)}{1,33} \approx 0,576$. On en déduit l'angle avec la fonction réciproque du sinus (touche $\sin^{-1}$, ou «&nbsp;arcsin&nbsp;», de la calculatrice, en mode degrés)&nbsp;: $i_2 = \sin^{-1}(0,576) \approx 35°$. Le rayon se rapproche bien de la normale, puisque l'eau a un indice plus grand que l'air.</p>
</div>
</details>

<div class="nt-lab nt-quizlab" id="tr-indice">
<p class="nt-tag"><i class="fa-solid fa-dumbbell"></i>Entraînement</p>
<p class="nt-lab-title">Lire un schéma de réfraction et trouver l'indice</p>
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

<div class="nt-lab" id="lab-mesures">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Expérience simulée</p>
<p class="nt-lab-title">Tester la loi de la réfraction et mesurer un indice</p>
<p>Un rayon laser entre dans un demi-cylindre de plexiglas par sa face plane, en son centre&nbsp;: il ressort ensuite par la face courbe sans être dévié. On mesure l'angle de réfraction pour plusieurs angles d'incidence.</p>
<canvas role="img" aria-label="Un demi-cylindre de plexiglas sur un rapporteur, traversé par un rayon laser ; à droite, le tableau des mesures et le graphique de sin(i1) en fonction de sin(i2)."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Angle d'incidence&nbsp;: <b class="out-i"></b><input type="range" min="0" max="80" step="5" value="30" data-in="i"></label></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="mesure"><i class="fa-solid fa-ruler"></i>&nbsp; Mesurer $i_2$</button><button type="button" class="nt-btn" data-act="droite" disabled><i class="fa-solid fa-chart-line"></i>&nbsp; Tracer la droite</button><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Nouveau bloc</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<h4 class="nt-h4">Le bâton cassé et la pièce qui apparaît</h4>

<p>Plongé dans l'eau, un bâton paraît cassé à la surface, et une pièce posée au fond d'un bol paraît plus proche de la surface qu'elle ne l'est. C'est encore la réfraction&nbsp;: les rayons qui sortent de l'eau s'éloignent de la normale, et notre cerveau, qui suppose que la lumière se propage en ligne droite, situe l'objet dans le prolongement des rayons qu'il reçoit.</p>

<div class="nt-lab" id="lab-piece">
<p class="nt-tag"><i class="fa-solid fa-coins"></i>Animation</p>
<p class="nt-lab-title">L'expérience de la pièce</p>
<canvas role="img" aria-label="Une pièce au fond d'un bol, cachée par le bord pour l'observateur ; quand on verse de l'eau, les rayons issus de la pièce sont déviés à la surface et atteignent l'œil : la pièce apparaît, plus haut qu'elle n'est."></canvas>
<div class="nt-ctrls"><label class="nt-ctrl">Hauteur d'eau&nbsp;: <b class="out-h"></b><input type="range" min="0" max="100" step="1" value="0" data-in="h"></label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### La dispersion expliquée {.nt-h3}

<p>Nous pouvons maintenant expliquer le prisme de Newton. L'indice optique d'un milieu transparent dépend légèrement de la longueur d'onde&nbsp;: dans le verre, il vaut par exemple 1,51 pour le rouge et 1,53 pour le violet. D'après la loi de la réfraction, les radiations de couleurs différentes sont donc déviées d'angles légèrement différents. Le prisme, avec ses deux réfractions successives, accentue l'écart&nbsp;: les couleurs se séparent.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La <span class="imp nt-hole">dispersion</span> de la lumière blanche par un prisme s'explique par la réfraction&nbsp;: l'indice optique du verre dépend de la longueur d'onde, donc chaque radiation est déviée d'un angle différent. Le <b>violet</b> est le plus dévié, le <b>rouge</b> le moins.</p>
</div>

<p>L'arc-en-ciel s'explique de la même façon&nbsp;: la lumière du Soleil est réfractée en entrant dans les gouttes de pluie, réfléchie au fond de la goutte, puis réfractée en ressortant&nbsp;; chaque couleur ressort dans une direction un peu différente.</p>

### La réflexion totale {.nt-h3}

<p>Quand la lumière passe d'un milieu d'indice $n_1$ à un milieu d'indice <b>plus petit</b> $n_2$ (de l'eau vers l'air, par exemple), le rayon réfracté s'éloigne de la normale&nbsp;: $i_2 > i_1$. Si l'on augmente l'angle d'incidence, l'angle de réfraction finit par atteindre 90°&nbsp;: le rayon réfracté rase la surface. Au-delà, il n'y a plus de rayon réfracté&nbsp;: <b>toute</b> la lumière est réfléchie.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>L'<span class="imp nt-hole">angle critique</span> (ou angle limite) $i_\text{c}$ est l'angle d'incidence pour lequel l'angle de réfraction vaut 90°. Pour un angle d'incidence supérieur à $i_\text{c}$, il y a <span class="imp nt-hole">réflexion totale</span>&nbsp;: toute la lumière est réfléchie, dans le premier milieu. Ce phénomène n'est possible que si la lumière va vers un milieu d'indice plus petit&nbsp;: $n_2 < n_1$.</p>
</div>

<p>D'après la loi de la réfraction, avec $i_2 = 90°$ et $\sin(90°) = 1$&nbsp;:</p>

<p style="text-align:center">$n_1 \times \sin(i_\text{c}) = n_2 \times 1$ &nbsp; donc &nbsp; $\sin(i_\text{c}) = \dfrac{n_2}{n_1}$ &nbsp; et &nbsp; $i_\text{c} = \sin^{-1}\left(\dfrac{n_2}{n_1}\right)$</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Calculer l'angle critique pour une interface eau-air ($n_\text{eau} = 1,33$), puis pour une interface verre-air ($n_\text{verre} = 1,50$).</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">49° et 42°</span></summary>
<div class="nt-d-body">
<p>Eau-air&nbsp;: $i_\text{c} = \sin^{-1}\left(\dfrac{1,00}{1,33}\right) \approx 49°$. Verre-air&nbsp;: $i_\text{c} = \sin^{-1}\left(\dfrac{1,00}{1,50}\right) \approx 42°$. Pour le diamant ($n = 2,42$), l'angle critique ne vaut que 24°.</p>
<p>Pour le vérifier, reprenez l'animation de la réfraction avec de l'eau en haut et de l'air en bas, et augmentez l'angle d'incidence.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Un nageur, sous l'eau, regarde vers la surface. Que voit-il&nbsp;?</p>
</div>
<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-comment-dots"></i>Réponse</span><span class="nt-sum">Le ciel dans un cercle, un miroir tout autour</span></summary>
<div class="nt-d-body">
<p>Seuls les rayons qui arrivent à son œil en faisant un angle de moins de 49° avec la verticale viennent de l'extérieur&nbsp;: il voit tout le ciel, et tout le paysage, rassemblés dans un cercle au-dessus de lui (c'est la «&nbsp;fenêtre de Snell&nbsp;»). Au-delà de 49°, la surface se comporte comme un miroir parfait&nbsp;: il y voit le reflet du fond de l'eau.</p>
</div>
</details>

<h4 class="nt-h4">Les fibres optiques</h4>

<p>Une fibre optique est un fil de verre très pur, plus fin qu'un cheveu&nbsp;: un <b>cœur</b> entouré d'une <b>gaine</b> d'indice un peu plus faible. La lumière qui entre dans le cœur rencontre la gaine sous un grand angle d'incidence, supérieur à l'angle critique&nbsp;: elle subit une réflexion totale, puis une autre, et encore une autre… Elle reste ainsi piégée dans le cœur, même quand la fibre est courbée, et peut parcourir des dizaines de kilomètres avec très peu de pertes.</p>

<div class="nt-lab" id="lab-fibre">
<p class="nt-tag"><i class="fa-solid fa-network-wired"></i>Animation</p>
<p class="nt-lab-title">La lumière piégée dans une fibre optique</p>
<canvas role="img" aria-label="Une fibre optique, cœur et gaine, dans laquelle un rayon lumineux se propage par réflexions totales successives ; si l'angle d'entrée est trop grand, le rayon s'échappe."></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Angle d'entrée du rayon&nbsp;: <b class="out-a"></b><input type="range" min="0" max="60" step="1" value="45" data-in="a"></label>
<label class="nt-ctrl">Courbure de la fibre&nbsp;: <b class="out-c"></b><input type="range" min="0" max="100" step="1" value="35" data-in="c"></label>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>Presque toutes nos communications (Internet, téléphone, télévision) voyagent ainsi, sous forme d'impulsions lumineuses, dans des millions de kilomètres de fibres, jusque sous les océans. Les endoscopes, qui permettent aux médecins de voir l'intérieur du corps, utilisent aussi des faisceaux de fibres.</p>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-gem"></i>D'autres applications</p>
<ul class="nt-facts">
<li><b>Les pierres précieuses</b> sont taillées pour que la lumière qui y entre subisse des réflexions totales sur les facettes arrière et ressorte vers l'avant&nbsp;: elles brillent. Plus l'indice est grand, plus l'angle critique est petit, plus il y a de réflexions totales&nbsp;: d'où l'éclat exceptionnel du diamant.</li>
<li><b>Les catadioptres</b> des vélos renvoient la lumière des phares vers leur source, par réflexions totales dans de petits coins de plastique.</li>
</ul>
</div>

### Les mirages {.nt-h3}

<p>Par une journée chaude, la route semble couverte de flaques d'eau, dans lesquelles se reflètent le ciel et les voitures&nbsp;; elles disparaissent quand on s'approche. Ce n'est pas une illusion de l'esprit&nbsp;: c'est un véritable phénomène optique, que l'on peut photographier.</p>

<p>L'air chaud est moins dense que l'air froid, et son indice optique est un peu plus faible (de quelques cent-millièmes&nbsp;!). Au-dessus d'une route surchauffée, l'air est d'autant plus chaud qu'on est près du sol&nbsp;: l'indice <b>diminue en descendant</b>. Un rayon venu du ciel, qui descend en oblique, traverse des couches d'indice de plus en plus faible&nbsp;: à chaque passage, il s'éloigne un peu plus de la normale, se courbe progressivement… et finit par remonter, par réflexion totale sur une couche d'air chaud. Notre œil le reçoit d'en bas&nbsp;: nous voyons le ciel <b>sous</b> l'horizon, à l'endroit où devrait être la route. Le cerveau interprète ce morceau de ciel comme une flaque qui le reflète.</p>

<div class="nt-lab" id="lab-mirage">
<p class="nt-tag"><i class="fa-solid fa-road"></i>Animation</p>
<p class="nt-lab-title">Comment naissent les mirages</p>
<div class="nt-btns"><div class="nt-seg" role="radiogroup"><label><input type="radio" name="mi-t" value="chaud" checked><span>Route surchauffée (mirage inférieur)</span></label><label><input type="radio" name="mi-t" value="froid"><span>Mer froide (mirage supérieur)</span></label></div><label class="nt-check"><input type="checkbox" data-in="couches" checked> Montrer les couches d'air</label></div>
<canvas role="img" aria-label="Des couches d'air d'indices différents au-dessus du sol ; un rayon lumineux s'y courbe progressivement avant d'atteindre l'œil, qui voit l'objet dans le prolongement du rayon reçu, à un endroit où il n'est pas."></canvas>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p>Au-dessus d'une mer froide, c'est l'inverse&nbsp;: l'air est plus froid, donc d'indice plus grand, près de la surface. Les rayons se courbent vers le bas, et les bateaux ou les côtes lointaines peuvent apparaître <b>au-dessus</b> de l'horizon, parfois renversés ou étirés en hautes falaises&nbsp;: c'est le mirage supérieur, ou <i>fata morgana</i>.</p>


## Testez-vous {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-final">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur la lumière</p>
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

  var ETOILES = (function () { var s = 7, a = []; function r() { s = (s * 16807) % 2147483647; return s / 2147483647; } for (var i = 0; i < 120; i++) { a.push([r(), r(), 0.3 + 0.7 * r()]); } return a; })();   /* ciel étoilé, toujours le même */

  /* ---------- couleur d'une radiation monochromatique (approximation usuelle de Bruton) ---------- */
  function rvb(l, a) {
    var r = 0, g = 0, b = 0, f;
    if (l < 380 || l > 780) { return 'rgba(0,0,0,0)'; }
    if (l < 440) { r = -(l - 440) / 60; b = 1; } else if (l < 490) { g = (l - 440) / 50; b = 1; } else if (l < 510) { g = 1; b = -(l - 510) / 20; } else if (l < 580) { r = (l - 510) / 70; g = 1; } else if (l < 645) { r = 1; g = -(l - 645) / 65; } else { r = 1; }
    f = l < 420 ? 0.3 + 0.7 * (l - 380) / 40 : (l > 700 ? 0.3 + 0.7 * (780 - l) / 80 : 1);   /* l'œil est moins sensible aux extrémités */
    function c(x) { return Math.round(255 * Math.pow(x * f, 0.8)); }
    return 'rgba(' + c(r) + ',' + c(g) + ',' + c(b) + ',' + (a === undefined ? 1 : a) + ')';
  }
  function rvbK(l, k) {   /* couleur opaque, assombrie d'un facteur k (au lieu d'une transparence, qui laisse des raccords) */
    var c = rvb(l).match(/[\d.]+/g).map(Number); return 'rgb(' + Math.round(c[0] * k) + ',' + Math.round(c[1] * k) + ',' + Math.round(c[2] * k) + ')';
  }
  function nomCouleur(l) { return l < 425 ? 'violet' : l < 490 ? 'bleu' : l < 505 ? 'bleu-vert' : l < 570 ? 'vert' : l < 590 ? 'jaune' : l < 625 ? 'orange' : l <= 780 ? 'rouge' : ''; }
  var RAIES = {   /* longueurs d'onde (nm) et intensités relatives des principales raies visibles */
    H: [[410.2, 0.5], [434.0, 0.6], [486.1, 0.85], [656.3, 1]],
    He: [[447.1, 0.6], [471.3, 0.35], [492.2, 0.4], [501.6, 0.7], [587.6, 1], [667.8, 0.7], [706.5, 0.5]],
    Na: [[498.3, 0.15], [568.8, 0.2], [589.0, 1], [589.6, 1], [616.0, 0.2]],
    Hg: [[404.7, 0.6], [435.8, 1], [546.1, 1], [577.0, 0.7], [579.1, 0.7]],
    Ne: [[540.1, 0.35], [585.2, 0.8], [588.2, 0.5], [594.5, 0.6], [603.0, 0.5], [607.4, 0.6], [614.3, 0.8], [626.6, 0.6], [633.4, 0.7], [640.2, 1], [650.7, 0.7], [659.9, 0.5], [692.9, 0.6], [703.2, 0.8], [724.5, 0.4]],
    Mg: [[470.3, 0.4], [516.7, 0.8], [517.3, 0.9], [518.4, 1], [552.8, 0.6]]
  };
  var NOMS = { H: 'hydrogène', He: 'hélium', Na: 'sodium', Hg: 'mercure', Ne: 'néon', Mg: 'magnésium' };
  function bandeSpectre(ctx, x, y, w, h, l0, l1, mode, raies, opts) {   /* mode : 'continu', 'emission' ou 'absorption' */
    opts = opts || {}; var X = function (l) { return x + (l - l0) / (l1 - l0) * w; };
    ctx.save(); rr(ctx, x, y, w, h, 6); ctx.clip();
    ctx.fillStyle = '#05070D'; ctx.fillRect(x, y, w, h);
    if (mode !== 'emission') { var gr = ctx.createLinearGradient(x, 0, x + w, 0); for (var l = l0; l <= l1 + 0.1; l += 3) { gr.addColorStop(Math.min(1, (l - l0) / (l1 - l0)), rvbK(l, opts.lum ? opts.lum(l) : 1)); } ctx.fillStyle = gr; ctx.fillRect(x, y, w, h); }   /* un seul dégradé : pas de raccords entre bandes */
    (raies || []).forEach(function (r) { var xl = X(r[0]); if (mode === 'emission') { var g = ctx.createLinearGradient(xl - 3, 0, xl + 3, 0); g.addColorStop(0, rvb(r[0], 0)); g.addColorStop(0.5, rvb(r[0], Math.min(1, 0.35 + 0.65 * r[1]))); g.addColorStop(1, rvb(r[0], 0)); ctx.fillStyle = g; ctx.fillRect(xl - 3, y, 6, h); } else { ctx.fillStyle = 'rgba(5,7,13,' + (0.08 + 0.92 * Math.pow(r[1], 1.6)) + ')'; ctx.fillRect(xl - 1.2, y, 2.4, h); } });   /* les raies faibles restent discrètes */
    ctx.restore();
    if (opts.axe) { ctx.fillStyle = SLATE; for (var g2 = Math.ceil(l0 / 50) * 50; g2 <= l1; g2 += 50) { ctx.fillRect(X(g2), y + h, 1, 5); txt(ctx, String(g2), X(g2), y + h + 13, { size: 9.5, col: SLATE }); } txt(ctx, 'λ (nm)', x + w, y + h + 26, { size: 10, col: SLATE, align: 'right' }); }
  }

  /* =================== 1. Rendre visible un faisceau laser =================== */
  (function () {
    var root = document.getElementById('lab-faisceau'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), mode = 'pur', t = 0, cnv, P = [];
    for (var i = 0; i < 260; i++) { P.push([Math.random(), Math.random(), Math.random() * 6.28, 0.4 + Math.random() * 0.6]); }
    for (var q = 0; q < 26; q++) { P[q][1] = 0.4 + Math.random() * 0.1; }   /* quelques poussières passent près du faisceau */
    var TXT = { pur: 'Dans un air parfaitement pur, on ne voit que le point rouge sur le mur, là où la lumière est renvoyée vers nous. Le faisceau lui-même reste invisible&nbsp;: sa lumière file droit vers le mur, sans venir vers notre œil.', poussiere: 'Les grains de poussière qui traversent le faisceau renvoient un peu de lumière dans toutes les directions, et donc vers notre œil&nbsp;: on voit des points briller le long d\u2019une ligne droite.', brume: 'Les innombrables gouttelettes d\u2019eau diffusent la lumière tout le long du faisceau&nbsp;: on «&nbsp;voit&nbsp;» la ligne droite suivie par la lumière… mais ce sont les gouttelettes éclairées que l\u2019on voit.' };
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, sol = H - 34, yl = H * 0.46, x0 = 96, x1 = W - 54, dens = mode === 'pur' ? 0 : (mode === 'poussiere' ? 70 : 260);
      ctx.clearRect(0, 0, W, H);
      var gm = ctx.createLinearGradient(0, 0, 0, sol); gm.addColorStop(0, '#111827'); gm.addColorStop(1, '#1F2937'); ctx.fillStyle = gm; ctx.fillRect(0, 0, W, sol);   /* pièce sombre */
      var gs = ctx.createLinearGradient(0, sol, 0, H); gs.addColorStop(0, '#374151'); gs.addColorStop(1, '#111827'); ctx.fillStyle = gs; ctx.fillRect(0, sol, W, H - sol);
      ctx.strokeStyle = 'rgba(255,255,255,0.05)'; for (var k = -6; k < 14; k++) { ctx.beginPath(); ctx.moveTo(W / 2 + k * 40, sol); ctx.lineTo(W / 2 + k * 90, H); ctx.stroke(); }   /* lames du parquet, en perspective */
      var gw = ctx.createLinearGradient(x1, 0, W, 0); gw.addColorStop(0, '#4B5563'); gw.addColorStop(1, '#374151'); ctx.fillStyle = gw; ctx.fillRect(x1, 0, W - x1, sol);   /* mur du fond */
      if (mode === 'brume') { var gb = ctx.createLinearGradient(0, yl - 14, 0, yl + 14); gb.addColorStop(0, 'rgba(239,68,68,0)'); gb.addColorStop(0.5, 'rgba(252,165,165,0.75)'); gb.addColorStop(1, 'rgba(239,68,68,0)'); ctx.fillStyle = gb; ctx.fillRect(x0, yl - 14, x1 - x0, 28); ctx.fillStyle = 'rgba(203,213,225,0.06)'; ctx.fillRect(0, 0, x1, sol); }
      P.slice(0, dens).forEach(function (p) { var px = x0 - 40 + ((p[0] + t * 0.006 * p[3]) % 1) * (x1 - x0 + 40), py = 14 + ((p[1] + Math.sin(t * 0.4 + p[2]) * 0.012 + 1) % 1) * (sol - 28), dist = Math.abs(py - yl), pres = dist < 4 && px > x0;
        if (pres) { var gl = ctx.createRadialGradient(px, py, 0, px, py, 9); gl.addColorStop(0, 'rgba(254,226,226,1)'); gl.addColorStop(0.3, 'rgba(248,113,113,0.8)'); gl.addColorStop(1, 'rgba(248,113,113,0)'); ctx.fillStyle = gl; ctx.beginPath(); ctx.arc(px, py, 9, 0, 2 * Math.PI); ctx.fill(); }
        else { ctx.fillStyle = 'rgba(203,213,225,' + (mode === 'brume' ? 0.12 : 0.22) + ')'; ctx.beginPath(); ctx.arc(px, py, mode === 'brume' ? 1.3 : 1, 0, 2 * Math.PI); ctx.fill(); } });
      var gp = ctx.createRadialGradient(x1, yl, 0, x1, yl, 26); gp.addColorStop(0, '#FFFFFF'); gp.addColorStop(0.15, '#FCA5A5'); gp.addColorStop(0.4, 'rgba(239,68,68,0.45)'); gp.addColorStop(1, 'rgba(239,68,68,0)'); ctx.fillStyle = gp; ctx.beginPath(); ctx.arc(x1, yl, 26, 0, 2 * Math.PI); ctx.fill();   /* la tache rouge sur le mur, qui renvoie la lumière vers nous */
      ctx.fillStyle = '#4B5563'; rr(ctx, 26, yl + 10, 10, sol - yl - 10, 3); ctx.fill(); ctx.fillStyle = '#6B7280'; rr(ctx, 12, sol - 6, 38, 6, 3); ctx.fill();   /* support */
      var gl2 = ctx.createLinearGradient(0, yl - 13, 0, yl + 13); gl2.addColorStop(0, '#9CA3AF'); gl2.addColorStop(0.5, '#E5E7EB'); gl2.addColorStop(1, '#6B7280'); ctx.fillStyle = gl2; rr(ctx, 10, yl - 13, 80, 26, 8); ctx.fill();   /* corps du laser */
      ctx.fillStyle = '#1F2937'; rr(ctx, 84, yl - 8, 12, 16, 3); ctx.fill(); ctx.fillStyle = '#EF4444'; ctx.beginPath(); ctx.arc(30, yl - 13, 4, Math.PI, 0); ctx.fill();
      var ga = ctx.createRadialGradient(96, yl, 0, 96, yl, 10); ga.addColorStop(0, '#FFFFFF'); ga.addColorStop(0.4, '#F87171'); ga.addColorStop(1, 'rgba(239,68,68,0)'); ctx.fillStyle = ga; ctx.beginPath(); ctx.arc(96, yl, 10, 0, 2 * Math.PI); ctx.fill();
      txt(ctx, 'laser', 50, yl + 28, { size: 10.5, col: '#CBD5E1' });
      if (mode === 'pur') { ctx.save(); ctx.setLineDash([3, 7]); ctx.strokeStyle = 'rgba(203,213,225,0.35)'; ctx.beginPath(); ctx.moveTo(x0, yl); ctx.lineTo(x1, yl); ctx.stroke(); ctx.restore(); pill(ctx, 'trajet de la lumière (invisible)', (x0 + x1) / 2, yl - 24, { size: 10.5, col: '#CBD5E1', bg: 'rgba(15,23,42,0.75)' }); }
    }
    var loop = Loop(root, function (dt) { t += dt; draw(cnv); return mode !== 'pur'; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 210 : 250; }, draw);
    $$(root, 'input[name="fx-m"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; msg.innerHTML = TXT[mode]; draw(cnv); if (!RM && mode !== 'pur') { loop.kick(); } }); });
    msg.innerHTML = TXT.pur; draw(cnv);
  })();

  /* =================== 2. La lumière fait la course =================== */
  (function () {
    var root = document.getElementById('lab-course'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), t = -1, cnv, M = [['vide', 1.0], ['air', 1.0003], ['eau', 1.33], ['verre', 1.5], ['diamant', 2.42]];
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, x0 = 90, x1 = W - 20, lh = (H - 30) / M.length;
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#0F172A'; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = 'rgba(255,255,255,0.6)'; ctx.setLineDash([4, 4]); ctx.beginPath(); ctx.moveTo(x1, 6); ctx.lineTo(x1, H - 6); ctx.stroke(); ctx.setLineDash([]);
      M.forEach(function (m, i) {
        var y = 16 + (i + 0.5) * lh, d = t < 0 ? 0 : Math.min(1, t / m[1]), xp = x0 + d * (x1 - x0);
        txt(ctx, m[0], x0 - 12, y, { size: 12, col: '#E2E8F0', align: 'right' }); txt(ctx, 'n = ' + String(m[1] === 1.0003 ? '1,0003' : fmt(m[1], 2)), x0 - 12, y + 14, { size: 9.5, col: '#94A3B8', align: 'right' });
        ctx.fillStyle = 'rgba(255,255,255,0.05)'; ctx.fillRect(x0, y - 10, x1 - x0, 20);
        var g = ctx.createLinearGradient(xp - 60, 0, xp, 0); g.addColorStop(0, 'rgba(253,224,71,0)'); g.addColorStop(1, 'rgba(253,224,71,0.9)'); ctx.fillStyle = g; ctx.fillRect(Math.max(x0, xp - 60), y - 4, Math.min(60, xp - x0), 8);
        ctx.fillStyle = '#FEF9C3'; ctx.beginPath(); ctx.arc(xp, y, 5, 0, 2 * Math.PI); ctx.fill();
        if (d >= 1) { pill(ctx, fmt(Math.round(299792 / m[1] / 1000) * 1000, 0) + ' km·s⁻¹', x1 - 10, y - 16, { size: 10, col: '#FDE68A', bg: 'rgba(15,23,42,0.8)', align: 'right' }); }
      });
    }
    var loop = Loop(root, function (dt) { if (t < 0) { return false; } t += dt / 2.2; draw(cnv); if (t > 2.5) { msg.innerHTML = 'Dans le vide et dans l\u2019air, la lumière arrive presque ensemble (l\u2019écart est invisible à cette échelle). Dans l\u2019eau, elle va 1,33 fois moins vite&nbsp;; dans le diamant, 2,42 fois moins vite. Le rapport entre la vitesse dans le vide et la vitesse dans le milieu est l\u2019<b>indice optique</b> du milieu (voir la partie&nbsp;3).'; return false; } return true; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 230 : 250; }, draw);
    $(root, '[data-act="go"]').addEventListener('click', function () { t = 0; msg.textContent = 'Toutes les impulsions partent en même temps…'; if (RM) { t = 2.6; draw(cnv); return; } loop.kick(); });
    msg.textContent = 'Cinq impulsions lumineuses vont partir en même temps, dans cinq milieux différents.'; draw(cnv);
  })();

  /* =================== 3. La roue dentée de Fizeau =================== */
  (function () {
    var root = document.getElementById('lab-fizeau'); if (!root) { return; }
    var inF = $(root, '[data-in="f"]'), msg = $(root, '.nt-msg'), cnv, ang = 0, N = 720, D = 8633, C = 2.998e8, NV = 24;   /* 720 dents ; 8,633 km ; on n'en dessine que 24, pour la lisibilité */
    function retour(f) { var s = f * 2 * D / C * N, d = Math.abs(s - Math.round(s)); return Math.max(0, 1 - 2 * d); }   /* fraction de lumière qui repasse : la roue a tourné de s périodes de dents pendant l'aller-retour ; nulle pour une demi-période (creux et dents de même largeur) */
    function dentee(ctx, x, y, R, n, a, prof) {   /* roue dentée vue de face : n dents (créneaux) de profondeur prof */
      ctx.beginPath(); for (var k = 0; k < n; k++) { var a0 = a + k * 2 * Math.PI / n, a1 = a0 + Math.PI / n; ctx.arc(x, y, R, a0, a1); ctx.arc(x, y, R - prof, a1, a1 + Math.PI / n); } ctx.closePath();
      var g = ctx.createRadialGradient(x - R * 0.3, y - R * 0.3, R * 0.1, x, y, R); g.addColorStop(0, '#E2E8F0'); g.addColorStop(1, '#64748B'); ctx.fillStyle = g; ctx.fill(); ctx.strokeStyle = '#334155'; ctx.lineWidth = 1; ctx.stroke();
      ctx.fillStyle = '#475569'; ctx.beginPath(); ctx.arc(x, y, R * 0.16, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = 'rgba(51,65,85,0.5)'; ctx.lineWidth = 2; for (var r = 0; r < 6; r++) { var b = a + r * Math.PI / 3; ctx.beginPath(); ctx.moveTo(x + R * 0.18 * Math.cos(b), y + R * 0.18 * Math.sin(b)); ctx.lineTo(x + (R - prof - 4) * Math.cos(b), y + (R - prof - 4) * Math.sin(b)); ctx.stroke(); }
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, f = +inF.value, b = retour(f), two = W >= 600, hs = two ? H * 0.64 : H * 0.58, sol = hs - 26, yb = hs * 0.36, cx = Math.min(210, W * 0.42), R = Math.min(60, hs * 0.26, W * 0.13), cy = yb + R - 5, xm = W - 40, ox = Math.min(64, W * 0.14);
      ctx.clearRect(0, 0, W, H); var gc = ctx.createLinearGradient(0, 0, 0, H); gc.addColorStop(0, '#020617'); gc.addColorStop(1, '#1E1B4B'); ctx.fillStyle = gc; ctx.fillRect(0, 0, W, H);   /* nuit étoilée de 1849 */
      ETOILES.slice(0, 70).forEach(function (e2) { ctx.fillStyle = 'rgba(255,255,255,' + e2[2] * 0.7 + ')'; ctx.fillRect(e2[0] * W, e2[1] * sol * 0.6, 1.2, 1.2); });
      ctx.fillStyle = '#0F172A'; ctx.beginPath(); ctx.moveTo(0, sol); ctx.quadraticCurveTo(W * 0.15, sol - 22, W * 0.35, sol - 8); ctx.quadraticCurveTo(W * 0.6, sol + 4, W * 0.78, sol - 26); ctx.quadraticCurveTo(W * 0.9, sol - 46, W, sol - 36); ctx.lineTo(W, hs); ctx.lineTo(0, hs); ctx.fill();   /* collines de Suresnes et de Montmartre */
      txt(ctx, 'Suresnes', W * 0.1, sol + 12, { size: 10, col: '#64748B' }); txt(ctx, 'Montmartre', W * 0.86, sol + 12, { size: 10, col: '#64748B' });
      var gA = ctx.createLinearGradient(0, yb - 3, 0, yb + 3); gA.addColorStop(0, 'rgba(253,224,71,0)'); gA.addColorStop(0.5, 'rgba(253,224,71,0.95)'); gA.addColorStop(1, 'rgba(253,224,71,0)'); ctx.fillStyle = gA; ctx.fillRect(ox + 24, yb - 3, xm - ox - 23, 6);   /* faisceau aller, jusqu'au miroir */
      ctx.fillStyle = 'rgba(253,224,71,' + (0.08 + 0.3 * b) + ')'; ctx.fillRect(ox - 14, yb - 5, 38, 10);   /* faisceau retour, vers l'œil */
      ctx.save(); ctx.globalAlpha = 0.95; dentee(ctx, cx, cy, R, NV, ang, R * 0.18); ctx.restore();
      var gl = ctx.createRadialGradient(cx, yb, 0, cx, yb, 9); gl.addColorStop(0, 'rgba(255,255,255,0.9)'); gl.addColorStop(1, 'rgba(253,224,71,0)'); ctx.fillStyle = gl; ctx.beginPath(); ctx.arc(cx, yb, 9, 0, 2 * Math.PI); ctx.fill();
      var gmr = ctx.createLinearGradient(xm, 0, xm + 8, 0); gmr.addColorStop(0, '#F8FAFC'); gmr.addColorStop(1, '#94A3B8'); ctx.fillStyle = gmr; ctx.fillRect(xm, yb - 24, 8, 48); ctx.fillStyle = '#475569'; ctx.fillRect(xm + 3, yb + 24, 3, sol - yb - 40); txt(ctx, 'miroir', xm + 4, yb - 32, { size: 10.5, col: '#CBD5E1' });
      txt(ctx, '\u2190 8,6 km, ici très raccourcis \u2192', (cx + R + xm) / 2, yb - 14, { size: 10.5, col: '#94A3B8' });
      ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(ox + 12, yb - 16); ctx.lineTo(ox + 30, yb + 16); ctx.stroke();   /* lame semi-réfléchissante */
      ctx.fillStyle = '#FEF3C7'; ctx.beginPath(); ctx.arc(ox + 21, sol - 14, 7, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = 'rgba(253,224,71,0.6)'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(ox + 21, sol - 21); ctx.lineTo(ox + 21, yb + 6); ctx.stroke(); txt(ctx, 'source', ox + 21, sol + 2, { size: 10, col: '#CBD5E1' });
      ctx.fillStyle = '#F8FAFC'; ctx.beginPath(); ctx.ellipse(ox - 26, yb, 12, 7.5, 0, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#1E3A8A'; ctx.beginPath(); ctx.arc(ox - 23, yb, 4.5, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#0F172A'; ctx.beginPath(); ctx.arc(ox - 23, yb, 2, 0, 2 * Math.PI); ctx.fill();   /* œil de l'observateur */
      ctx.fillStyle = '#0B1120'; ctx.fillRect(0, hs, W, H - hs); ctx.fillStyle = 'rgba(148,163,184,0.3)'; ctx.fillRect(0, hs, W, 1);   /* bandeau du bas : ce que l'on mesure */
      var vx = two ? W * 0.16 : W * 0.25, vy = hs + (H - hs) / 2 - 6, vr = Math.min(44, (H - hs) / 2 - 20);   /* ce que voit l'observateur, dans sa lunette */
      ctx.save(); ctx.beginPath(); ctx.arc(vx, vy, vr, 0, 2 * Math.PI); ctx.fillStyle = '#000'; ctx.fill(); ctx.clip(); var gv = ctx.createRadialGradient(vx, vy, 0, vx, vy, vr * 0.7); gv.addColorStop(0, 'rgba(255,250,220,' + b + ')'); gv.addColorStop(0.35, 'rgba(253,224,71,' + (0.85 * b) + ')'); gv.addColorStop(1, 'rgba(253,224,71,0)'); ctx.fillStyle = gv; ctx.fillRect(vx - vr, vy - vr, 2 * vr, 2 * vr); ctx.restore();
      ctx.strokeStyle = '#64748B'; ctx.lineWidth = 5; ctx.beginPath(); ctx.arc(vx, vy, vr + 2, 0, 2 * Math.PI); ctx.stroke(); txt(ctx, 'dans la lunette\u00A0: ' + Math.round(100 * b) + '\u00A0%', vx, vy + vr + 16, { size: 10.5, col: '#E2E8F0' });
      var gx = two ? W * 0.4 : W * 0.5, gw = two ? W * 0.52 : W * 0.44, gy = hs + 22, gh = H - hs - 56, X = function (v) { return gx + v / 30 * gw; }, Y = function (v) { return gy + gh - v * gh; };   /* luminosité en fonction de la vitesse de rotation */
      ctx.strokeStyle = 'rgba(148,163,184,0.5)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(gx, gy); ctx.lineTo(gx, gy + gh); ctx.lineTo(gx + gw, gy + gh); ctx.stroke();
      ctx.strokeStyle = '#FDE047'; ctx.lineWidth = 2; ctx.beginPath(); for (var k = 0; k <= 300; k++) { var fv = 30 * k / 300; if (k) { ctx.lineTo(X(fv), Y(retour(fv))); } else { ctx.moveTo(X(fv), Y(retour(fv))); } } ctx.stroke();
      ctx.fillStyle = '#F8FAFC'; ctx.beginPath(); ctx.arc(X(f), Y(b), 4.5, 0, 2 * Math.PI); ctx.fill();
      [0, 10, 20, 30].forEach(function (v) { txt(ctx, String(v), X(v), gy + gh + 11, { size: 9.5, col: '#94A3B8' }); }); txt(ctx, 'tours par seconde', gx + gw, gy + gh + 22, { size: 9.5, col: '#94A3B8', align: 'right' }); txt(ctx, 'lumière revenue', gx - 28, gy - 8, { size: 9.5, col: '#94A3B8', align: 'left' });
    }
    function texte() { var f = +inF.value, b = retour(f); $(root, '.out-f').textContent = fmt(f, 1) + '\u00A0tours par seconde'; msg.innerHTML = b < 0.05 ? '<b>Extinction&nbsp;!</b> Pendant l\u2019aller-retour de la lumière, la roue a tourné d\u2019une demi-dent&nbsp;: la lumière revient sur une dent. Durée de l\u2019aller-retour&nbsp;: $\\Delta t = \\dfrac{1}{2 \\times 720 \\times f} \\approx \\pu{5,8E-5 s}$, d\u2019où $c = \\dfrac{2 \\times \\pu{8633 m}}{\\Delta t} \\approx \\pu{3,0E8 m*s-1}$.' : 'La lumière revenue est en partie arrêtée par les dents&nbsp;: l\u2019observateur en reçoit ' + Math.round(100 * b) + '&nbsp;%. Plus la roue tourne vite, plus elle a tourné pendant l\u2019aller-retour de la lumière, et plus elle masque le faisceau de retour. Cherchez la première extinction.'; typeset(msg); }
    var loop = Loop(root, function (dt) { ang += dt * 2 * Math.PI * (+inF.value) / 12; draw(cnv); return true; });   /* rotation affichée très ralentie (12 fois), pour rester lisible */
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 600 ? 420 : 380; }, draw);
    var det = root.closest('details'); if (det) { det.addEventListener('toggle', function () { if (det.open) { cnv.size(); } }); }
    inF.addEventListener('input', function () { texte(); draw(cnv); });
    texte(); draw(cnv); if (!RM) { loop.kick(); }
  })();

  /* =================== 4. Un prisme sur le trajet de la lumière =================== */
  (function () {
    var root = document.getElementById('lab-prisme'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), src = 'blanc', cnv;
    function nVerre(l) { return 1.47 + 30000 / (l * l); }   /* loi de Cauchy, avec une dispersion exagérée pour que l'éventail soit bien visible */
    function refr(d, nrm, n1, n2) {   /* direction réfractée (vecteurs unitaires 2D), ou null si réflexion totale */
      var c = -(nrm[0] * d[0] + nrm[1] * d[1]), r = n1 / n2, k = 1 - r * r * (1 - c * c); if (k < 0) { return null; }
      return [r * d[0] + (r * c - Math.sqrt(k)) * nrm[0], r * d[1] + (r * c - Math.sqrt(k)) * nrm[1]];
    }
    function inter(p, d, a, b) { var ex = b[0] - a[0], ey = b[1] - a[1], den = d[0] * ey - d[1] * ex; if (Math.abs(den) < 1e-9) { return null; } var t = ((a[0] - p[0]) * ey - (a[1] - p[1]) * ex) / den, u = ((a[0] - p[0]) * d[1] - (a[1] - p[1]) * d[0]) / den; return t > 0 && u >= 0 && u <= 1 ? [p[0] + d[0] * t, p[1] + d[1] * t] : null; }
    var rad0 = 0.62;
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, s = Math.min(W / 640, H / 300), cx = W * 0.33, cy = H * 0.5, L = 140 * s;
      var A = [cx, cy - L * 0.87], B = [cx - L / 2, cy + L * 0.0], Cc = [cx + L / 2, cy];   /* prisme équilatéral, sommet en haut */
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#0B1120'; ctx.fillRect(0, 0, W, H);
      var ex = W - 30; ctx.fillStyle = '#F8FAFC'; ctx.fillRect(ex, 20, 8, H - 40); txt(ctx, 'écran', ex + 4, H - 8, { size: 10, col: '#CBD5E1' });
      var d0 = [Math.cos(rad0), -Math.sin(rad0)], M0 = [(A[0] + B[0]) / 2, (A[1] + B[1]) / 2 + L * 0.05], P0 = [20, M0[1] - (M0[0] - 20) * Math.tan(-rad0)];   /* incidence choisie près du minimum de déviation */
      var LS = src === 'blanc' ? (function () { var a = []; for (var l = 400; l <= 700; l += 6) { a.push(l); } return a; })() : [src === 'rouge' ? 650 : 532];
      var I1 = inter(P0, d0, B, A);
      ctx.strokeStyle = src === 'blanc' ? '#FFFFFF' : rvb(LS[0]); ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(P0[0], P0[1]); ctx.lineTo(I1[0], I1[1]); ctx.stroke();
      ctx.save(); ctx.globalCompositeOperation = 'lighter';
      LS.forEach(function (l) {
        var n = nVerre(l), nAB = [-(A[1] - B[1]), A[0] - B[0]], m1 = Math.hypot(nAB[0], nAB[1]); nAB = [nAB[0] / m1, nAB[1] / m1]; if (nAB[0] * d0[0] + nAB[1] * d0[1] > 0) { nAB = [-nAB[0], -nAB[1]]; }
        var d1 = refr(d0, nAB, 1, n), I2 = inter([I1[0] + d1[0] * 0.01, I1[1] + d1[1] * 0.01], d1, A, Cc); if (!I2) { return; }
        var nAC = [A[1] - Cc[1], -(A[0] - Cc[0])], m2 = Math.hypot(nAC[0], nAC[1]); nAC = [nAC[0] / m2, nAC[1] / m2]; if (nAC[0] * d1[0] + nAC[1] * d1[1] > 0) { nAC = [-nAC[0], -nAC[1]]; }
        var d2 = refr(d1, nAC, n, 1); if (!d2) { return; } var tf = (ex - I2[0]) / d2[0], F = [ex, I2[1] + d2[1] * tf];
        var al = src === 'blanc' ? 0.22 : 1; ctx.strokeStyle = rvb(l, al); ctx.lineWidth = src === 'blanc' ? 2.5 : 3;
        ctx.beginPath(); ctx.moveTo(I1[0], I1[1]); ctx.lineTo(I2[0], I2[1]); ctx.lineTo(F[0], F[1]); ctx.stroke();
        ctx.fillStyle = rvb(l, src === 'blanc' ? 0.9 : 1); ctx.fillRect(ex, F[1] - 2, 8, 4);
      });
      ctx.restore();
      ctx.fillStyle = 'rgba(186,230,253,0.18)'; ctx.strokeStyle = 'rgba(186,230,253,0.8)'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(A[0], A[1]); ctx.lineTo(B[0], B[1]); ctx.lineTo(Cc[0], Cc[1]); ctx.closePath(); ctx.fill(); ctx.stroke();
      txt(ctx, 'prisme en verre', cx, cy + 16, { size: 10.5, col: '#BAE6FD' }); if (src === 'blanc') { txt(ctx, '(écart entre les couleurs exagéré)', W / 2, H - 10, { size: 10, col: '#64748B' }); }
    }
    var TXT = { blanc: 'La lumière blanche est <b>dispersée</b>&nbsp;: elle ressort du prisme en un éventail de couleurs, du rouge (le moins dévié) au violet (le plus dévié). La lumière blanche est polychromatique.', rouge: 'La lumière du laser rouge est déviée par le prisme, mais elle n\u2019est pas décomposée&nbsp;: elle ne contient qu\u2019une seule radiation, de longueur d\u2019onde 650&nbsp;nm. Elle est monochromatique.', vert: 'Le laser vert (532&nbsp;nm) est un peu plus dévié que le rouge, mais lui non plus n\u2019est pas décomposé&nbsp;: il est monochromatique.' };
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 230 : 300; }, draw);
    $$(root, 'input[name="pr-s"]').forEach(function (r) { r.addEventListener('change', function () { src = r.value; msg.innerHTML = TXT[src]; draw(cnv); }); });
    msg.innerHTML = TXT.blanc; draw(cnv);
  })();

  /* =================== 5. Le spectre de la lumière blanche =================== */
  (function () {
    var root = document.getElementById('lab-visible'); if (!root) { return; }
    var inL = $(root, '[data-in="l"]'), msg = $(root, '.nt-msg'), cnv;
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, x = 20, w = W - 40, y = 34, h = 54, l = +inL.value, X = function (v) { return x + (v - 380) / 420 * w; };
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      bandeSpectre(ctx, x, y, w, h, 380, 800, 'continu', [], { axe: true });
      pill(ctx, 'ultraviolet \u2190', x, 14, { size: 10.5, col: '#6D28D9', align: 'left', stroke: '#DDD6FE' }); pill(ctx, '\u2192 infrarouge', x + w, 14, { size: 10.5, col: '#B91C1C', align: 'right', stroke: '#FECACA' });
      var xl = X(l); ctx.strokeStyle = '#0F172A'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(xl, y - 6); ctx.lineTo(xl, y + h + 6); ctx.stroke();
      ctx.fillStyle = rvb(l); ctx.strokeStyle = '#CBD5E1'; rr(ctx, W / 2 - 60, y + h + 40, 120, 40, 10); ctx.fill(); ctx.stroke();
      txt(ctx, l + ' nm', W / 2, y + h + 92, { size: 13, col: NAVY, bold: true });
    }
    function texte() { var l = +inL.value; $(root, '.out-l').textContent = l + '\u00A0nm'; msg.innerHTML = l < 400 ? 'Vers 380&nbsp;nm, on atteint la limite de la vision&nbsp;: au-delà, l\u2019ultraviolet est invisible.' : (l > 780 ? 'Au-delà de 780&nbsp;nm environ, l\u2019infrarouge est invisible pour nous.' : 'Une radiation de ' + l + '&nbsp;nm est perçue comme <b>' + nomCouleur(l) + '</b>.'); }
    cnv = Canvas($(root, 'canvas'), function () { return 200; }, draw);
    inL.addEventListener('input', function () { texte(); draw(cnv); });
    texte(); draw(cnv);
  })();

  /* =================== 6. Chauffer un corps de plus en plus =================== */
  (function () {
    var root = document.getElementById('lab-thermique'); if (!root) { return; }
    var inT = $(root, '[data-in="t"]'), msg = $(root, '.nt-msg'), cnv;
    function planck(l, T) { var x = l * 1e-9; return 1 / (Math.pow(x, 5) * (Math.exp(0.014388 / (x * T)) - 1)); }   /* loi de Planck, à un facteur près */
    function lueur(T) {   /* couleur perçue d'un corps à la température T (approximation de Tanner Helland) */
      var t = T / 100, r, g, b;
      r = t <= 66 ? 255 : 329.7 * Math.pow(t - 60, -0.1332); g = t <= 66 ? 99.47 * Math.log(t) - 161.12 : 288.12 * Math.pow(t - 60, -0.0755); b = t >= 66 ? 255 : (t <= 19 ? 0 : 138.52 * Math.log(t - 10) - 305.04);
      function c(v) { return Math.max(0, Math.min(255, Math.round(v))); } return [c(r), c(g), c(b)];
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, T = +inT.value, two = W >= 560, ref = planck(550, 6500), Pm = 0, l;
      for (l = 380; l <= 780; l += 5) { Pm = Math.max(Pm, planck(l, T)); }
      var lum = Math.min(1, Math.pow(Pm / ref, 0.16)), coul = lueur(T), aff = Math.min(1, Math.max(0.08, (T - 700) / 1300));   /* brillance globale (échelle compressée, comme la perception) */
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#0B1120'; ctx.fillRect(0, 0, W, H);
      var bx = two ? 90 : W / 2, by = two ? H / 2 : 58, br = two ? 50 : 34;
      var g = ctx.createRadialGradient(bx, by, br * 0.2, bx, by, br * 2.2); g.addColorStop(0, 'rgba(' + coul.join(',') + ',' + (0.55 * aff) + ')'); g.addColorStop(1, 'rgba(' + coul.join(',') + ',0)'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(bx, by, br * 2.2, 0, 2 * Math.PI); ctx.fill();
      var gb = ctx.createRadialGradient(bx - br * 0.3, by - br * 0.3, 2, bx, by, br); gb.addColorStop(0, 'rgba(' + coul.map(function (v) { return Math.round(v * aff + 40 * (1 - aff)); }).join(',') + ',1)'); gb.addColorStop(1, 'rgba(' + coul.map(function (v) { return Math.round(v * aff * 0.7 + 30 * (1 - aff)); }).join(',') + ',1)');
      ctx.fillStyle = gb; rr(ctx, bx - br, by - br * 0.55, 2 * br, 1.1 * br, br * 0.25); ctx.fill();   /* lingot de métal chauffé */
      txt(ctx, fmt(T, 0) + ' K', bx, by + br * 0.55 + 18, { size: 12, col: '#E2E8F0', bold: true }); txt(ctx, '≈ ' + fmt(T - 273, 0) + ' °C', bx, by + br * 0.55 + 33, { size: 10.5, col: '#94A3B8' });
      var sx = two ? 210 : 20, sw = W - sx - 20, sy = two ? 30 : 140, sh = two ? 46 : 36;
      bandeSpectre(ctx, sx, sy, sw, sh, 380, 780, 'continu', [], { axe: true, lum: function (x) { return Math.min(1, planck(x, T) / Pm) * lum; } });
      txt(ctx, 'spectre de la lumière émise', sx, sy - 10, { size: 11, col: '#CBD5E1', align: 'left' });
      var gy = sy + sh + 34, gh = H - gy - 14; if (gh > 40) {   /* intensité de chaque radiation (même échelle pour toutes les températures) */
        ctx.strokeStyle = 'rgba(148,163,184,0.4)'; ctx.beginPath(); ctx.moveTo(sx, gy); ctx.lineTo(sx, gy + gh); ctx.lineTo(sx + sw, gy + gh); ctx.stroke();
        ctx.beginPath(); for (l = 380; l <= 780; l += 4) { var px = sx + (l - 380) / 400 * sw, py = gy + gh - planck(l, T) / Pm * gh * 0.92; if (l === 380) { ctx.moveTo(px, py); } else { ctx.lineTo(px, py); } } ctx.strokeStyle = '#FDE68A'; ctx.lineWidth = 2.2; ctx.stroke();
        txt(ctx, 'intensité relative de chaque couleur', sx + 4, gy + 8, { size: 10, col: '#94A3B8', align: 'left' });
      }
    }
    function texte() { var T = +inT.value; $(root, '.out-t').textContent = fmt(T, 0) + '\u00A0K'; msg.innerHTML = T < 1100 ? 'Vers 1&nbsp;000&nbsp;K (700&nbsp;°C), le métal rougeoie à peine&nbsp;: il émet surtout dans l\u2019infrarouge, et un peu de rouge.' : (T < 2500 ? 'Le corps est rouge-orangé&nbsp;: son spectre contient surtout du rouge et du jaune, très peu de bleu.' : (T < 4500 ? 'À la température d\u2019un filament de lampe (environ 3&nbsp;000&nbsp;K), la lumière est jaune-orangé.' : (T < 7500 ? 'À la température de la surface du Soleil (environ 5&nbsp;800&nbsp;K), le spectre est complet&nbsp;: la lumière est blanche.' : 'Encore plus chaud, comme les étoiles bleues (plus de 10&nbsp;000&nbsp;K)&nbsp;: le spectre est riche en violet et en bleu, la lumière est blanc bleuté.'))) + ' Le kelvin (K) est l\u2019unité de température absolue&nbsp;: $T(\\text{K}) \\approx \\theta(°\\text{C}) + 273$.'; typeset(msg); }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 300 : 230; }, draw);
    inT.addEventListener('input', function () { texte(); draw(cnv); });
    texte(); draw(cnv);
  })();

  /* =================== 7. Spectres de raies : émission et absorption =================== */
  (function () {
    var root = document.getElementById('lab-raies'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), el = 'H', mode = 'em', cnv;
    function teinte(al) { var r = 0, g = 0, b = 0; RAIES[el].forEach(function (q) { var c = rvb(q[0]).match(/[\d.]+/g).map(Number); r += c[0] * q[1]; g += c[1] * q[1]; b += c[2] * q[1]; }); var m = Math.max(r, g, b) / 255 || 1; return 'rgba(' + Math.round(r / m) + ',' + Math.round(g / m) + ',' + Math.round(b / m) + ',' + al + ')'; }   /* couleur d'ensemble de la lampe */
    function tubeV(ctx, x, y0, y1, w) {   /* tube à décharge vertical, lumineux, avec ses deux électrodes */
      var h = y1 - y0, g = ctx.createRadialGradient(x, (y0 + y1) / 2, 2, x, (y0 + y1) / 2, h * 0.75); g.addColorStop(0, teinte(0.45)); g.addColorStop(1, teinte(0)); ctx.fillStyle = g; ctx.fillRect(x - h, y0 - 20, 2 * h, h + 40);
      var gv = ctx.createLinearGradient(x - w / 2, 0, x + w / 2, 0); gv.addColorStop(0, teinte(0.95)); gv.addColorStop(0.5, 'rgba(255,255,255,0.92)'); gv.addColorStop(1, teinte(0.95));
      ctx.fillStyle = gv; rr(ctx, x - w / 2, y0, w, h, w / 2); ctx.fill(); ctx.strokeStyle = 'rgba(226,232,240,0.85)'; ctx.lineWidth = 1.3; ctx.stroke();
      ctx.strokeStyle = 'rgba(255,255,255,0.55)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x - w / 2 + 4, y0 + w * 0.6); ctx.lineTo(x - w / 2 + 4, y1 - w * 0.6); ctx.stroke();
      var gm = ctx.createLinearGradient(x - 7, 0, x + 7, 0); gm.addColorStop(0, '#64748B'); gm.addColorStop(0.5, '#E2E8F0'); gm.addColorStop(1, '#64748B'); ctx.fillStyle = gm; rr(ctx, x - 7, y0 - 12, 14, 14, 3); ctx.fill(); rr(ctx, x - 7, y1 - 2, 14, 14, 3); ctx.fill();   /* électrodes */
      return [[x, y0 - 12], [x, y1 + 12]];
    }
    function cuve(ctx, x, y, w, h) {   /* cuve de verre transparente, fermée par deux fenêtres, remplie d'un gaz froid (presque invisible) */
      ctx.fillStyle = 'rgba(186,230,253,0.07)'; ctx.fillRect(x, y, w, h);
      ctx.strokeStyle = 'rgba(203,213,225,0.75)'; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + w, y); ctx.moveTo(x, y + h); ctx.lineTo(x + w, y + h); ctx.stroke();
      [x, x + w].forEach(function (xx) { var g = ctx.createLinearGradient(xx - 3, 0, xx + 3, 0); g.addColorStop(0, 'rgba(186,230,253,0.15)'); g.addColorStop(0.5, 'rgba(224,242,254,0.55)'); g.addColorStop(1, 'rgba(186,230,253,0.15)'); ctx.fillStyle = g; ctx.fillRect(xx - 3, y - 4, 6, h + 8); });
      for (var k = 0; k < 18; k++) { ctx.fillStyle = 'rgba(203,213,225,0.35)'; ctx.beginPath(); ctx.arc(x + 8 + ((k * 37) % 100) / 100 * (w - 16), y + 5 + ((k * 61) % 100) / 100 * (h - 10), 1.1, 0, 2 * Math.PI); ctx.fill(); }
    }
    function metal(ctx, y0, y1, a, b) { var g = ctx.createLinearGradient(0, y0, 0, y1); g.addColorStop(0, a); g.addColorStop(0.45, '#E2E8F0'); g.addColorStop(1, b); return g; }
    function tubeOpt(ctx, x, y, L, r, ang, bague) {   /* tube optique métallique, d'axe incliné de ang, partant de (x, y) */
      ctx.save(); ctx.translate(x, y); ctx.rotate(ang);
      ctx.fillStyle = metal(ctx, -r, r, '#64748B', '#1E293B'); rr(ctx, 0, -r, L, 2 * r, 2); ctx.fill();
      ctx.fillStyle = metal(ctx, -r - 2, r + 2, '#A16207', '#713F12'); bague.forEach(function (u) { rr(ctx, u * L - 3, -r - 2, 6, 2 * r + 4, 1.5); ctx.fill(); });   /* bagues en laiton */
      ctx.restore();
    }
    function spectroscope(ctx, x, y) {   /* spectroscope à prisme : collimateur tourné vers la source, plateau et prisme, lunette d'observation */
      var cx = x + 34, cy = y + 4;
      ctx.fillStyle = metal(ctx, cy + 26, cy + 40, '#475569', '#0F172A'); ctx.beginPath(); ctx.ellipse(cx, cy + 36, 30, 6, 0, 0, 2 * Math.PI); ctx.fill();   /* pied */
      ctx.fillStyle = metal(ctx, 0, 1, '#475569', '#1E293B'); ctx.fillStyle = '#334155'; ctx.fillRect(cx - 4, cy + 8, 8, 28);
      tubeOpt(ctx, x - 44, y, 64, 6, 0, [0.12, 0.85]);   /* collimateur */
      ctx.fillStyle = '#0F172A'; rr(ctx, x - 52, y - 9, 10, 18, 2); ctx.fill(); ctx.fillStyle = '#F8FAFC'; ctx.fillRect(x - 48, y - 6, 1.5, 12);   /* fente d'entrée, éclairée */
      ctx.fillStyle = metal(ctx, cy - 2, cy + 10, '#64748B', '#1E293B'); ctx.beginPath(); ctx.ellipse(cx, cy + 6, 26, 6, 0, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = 'rgba(226,232,240,0.5)'; ctx.lineWidth = 1; ctx.stroke();   /* plateau */
      var gp = ctx.createLinearGradient(cx - 12, cy - 22, cx + 12, cy + 4); gp.addColorStop(0, 'rgba(224,242,254,0.85)'); gp.addColorStop(0.5, 'rgba(125,211,252,0.45)'); gp.addColorStop(1, 'rgba(224,242,254,0.75)');
      ctx.fillStyle = gp; ctx.beginPath(); ctx.moveTo(cx, cy - 22); ctx.lineTo(cx + 13, cy + 4); ctx.lineTo(cx - 13, cy + 4); ctx.closePath(); ctx.fill(); ctx.strokeStyle = 'rgba(255,255,255,0.8)'; ctx.lineWidth = 1; ctx.stroke();   /* prisme en verre */
      ctx.strokeStyle = 'rgba(255,255,255,0.9)'; ctx.beginPath(); ctx.moveTo(cx - 3, cy - 14); ctx.lineTo(cx - 8, cy); ctx.stroke();
      tubeOpt(ctx, cx + 10, cy - 8, 58, 6, -0.5, [0.1, 0.8]);   /* lunette */
      ctx.save(); ctx.translate(cx + 10, cy - 8); ctx.rotate(-0.5); ctx.fillStyle = '#0F172A'; rr(ctx, 58, -8, 9, 16, 2); ctx.fill(); ctx.restore();   /* oculaire */
      txt(ctx, 'spectroscope', cx, cy + 54, { size: 10, col: '#94A3B8' });
    }
    function fil(ctx, a, c1, c2, b) { ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 2; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.bezierCurveTo(c1[0], c1[1], c2[0], c2[1], b[0], b[1]); ctx.stroke(); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, two = W >= 600, sx = 20, sw = W - 40, top = 44, bas = 150, mid = (top + bas) / 2;
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#0B1120'); gf.addColorStop(1, '#111827'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      var lx = W * (two ? 0.4 : 0.36), spx = Math.min(lx + (two ? 130 : 86), W - 110);   /* le spectroscope tient toujours dans la largeur */
      if (mode === 'em') {
        txt(ctx, two ? 'Lampe à décharge\u00A0: ' + NOMS[el] + ' traversé par une décharge électrique' : 'Lampe à ' + NOMS[el] + ' (décharge)', W / 2, 16, { size: 11.5, col: '#F8FAFC', bold: true });
        var gx = two ? lx - 150 : 16, gy = mid - 20;   /* générateur haute tension */
        var gg = ctx.createLinearGradient(0, gy, 0, gy + 44); gg.addColorStop(0, '#334155'); gg.addColorStop(1, '#1E293B'); ctx.fillStyle = gg; rr(ctx, gx, gy, 56, 44, 6); ctx.fill(); ctx.fillStyle = '#F59E0B'; ctx.fillRect(gx + 8, gy + 8, 14, 5); txt(ctx, 'générateur', gx + 28, gy + 56, { size: 9.5, col: '#94A3B8' });
        var bp = [gx + 56, gy + 12], bm = [gx + 56, gy + 32]; ctx.fillStyle = '#EF4444'; ctx.beginPath(); ctx.arc(bp[0], bp[1], 3.5, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#E2E8F0'; ctx.beginPath(); ctx.arc(bm[0], bm[1], 3.5, 0, 2 * Math.PI); ctx.fill();   /* bornes */
        var E = tubeV(ctx, lx, top, bas, 22);
        fil(ctx, bp, [bp[0] + 40, bp[1] + 24], [E[0][0] - 10, E[0][1] - 46], E[0]);   /* fil lâche, arrivant par le haut sur l'électrode du haut */
        fil(ctx, bm, [bm[0] + 30, bm[1] + 50], [E[1][0] - 8, E[1][1] + 46], E[1]);   /* fil lâche, arrivant par le bas sur l'électrode du bas */
      } else {
        txt(ctx, two ? 'Lumière blanche traversant une cuve de ' + NOMS[el] + ' gazeux, froid' : 'Lumière blanche et ' + NOMS[el] + ' froid', W / 2, 16, { size: 11.5, col: '#F8FAFC', bold: true });
        var bx = two ? lx - 150 : 40, gl = ctx.createRadialGradient(bx, mid, 2, bx, mid, 28); gl.addColorStop(0, '#FFFFFF'); gl.addColorStop(0.4, 'rgba(254,249,195,0.9)'); gl.addColorStop(1, 'rgba(254,249,195,0)'); ctx.fillStyle = gl; ctx.beginPath(); ctx.arc(bx, mid, 28, 0, 2 * Math.PI); ctx.fill();   /* lampe à incandescence */
        ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 1.3; ctx.beginPath(); ctx.arc(bx, mid, 14, 0, 2 * Math.PI); ctx.stroke(); txt(ctx, 'lampe', bx, mid + 34, { size: 10, col: '#94A3B8' });
        var gw = ctx.createLinearGradient(bx, 0, spx, 0); gw.addColorStop(0, 'rgba(254,249,195,0.6)'); gw.addColorStop(1, 'rgba(254,249,195,0.25)'); ctx.fillStyle = gw; ctx.fillRect(bx + 15, mid - 3, spx - 36 - bx - 15, 6);
        var cw = Math.min(110, spx - bx - 90); cuve(ctx, (bx + spx - 36) / 2 - cw / 2, mid - 20, cw, 40); txt(ctx, 'cuve', (bx + spx - 36) / 2, mid + 34, { size: 10, col: '#94A3B8' });
      }
      spectroscope(ctx, spx, mid);
      var by = bas + 62, bh = two ? 56 : 44;
      txt(ctx, mode === 'em' ? 'ce qu\u2019on voit dans le spectroscope\u00A0: spectre de raies d\u2019émission' : 'ce qu\u2019on voit dans le spectroscope\u00A0: spectre de raies d\u2019absorption', sx, by - 14, { size: 11, col: '#F8FAFC', align: 'left', bold: true });
      bandeSpectre(ctx, sx, by, sw, bh, 380, 750, mode === 'em' ? 'emission' : 'absorption', RAIES[el], { axe: true });
      var cy = by + bh + 52, ch = bh * 0.5;
      txt(ctx, ('pour comparer\u00A0: le spectre ' + (mode === 'em' ? 'd\u2019absorption' : 'd\u2019émission') + ' du ' + NOMS[el]).replace('du hélium', 'de l\u2019hélium'), sx, cy - 10, { size: 10.5, col: '#94A3B8', align: 'left' });
      bandeSpectre(ctx, sx, cy, sw, ch, 380, 750, mode === 'em' ? 'absorption' : 'emission', RAIES[el], {});
      ctx.save(); ctx.setLineDash([2, 4]); ctx.strokeStyle = 'rgba(255,255,255,0.3)'; RAIES[el].filter(function (q) { return q[1] > 0.3; }).forEach(function (q) { var x = sx + (q[0] - 380) / 370 * sw; ctx.beginPath(); ctx.moveTo(x, by + bh + 22); ctx.lineTo(x, cy); ctx.stroke(); }); ctx.restore();
    }
    function texte() {
      var l = RAIES[el].filter(function (q) { return q[1] > 0.3; }).map(function (q) { return fmt(q[0], 0); });
      msg.innerHTML = (mode === 'em' ? 'Le ' + NOMS[el] + ' émet quelques radiations seulement, ' : 'Le ' + NOMS[el] + ' froid absorbe quelques radiations de la lumière blanche, ') + 'aux longueurs d\u2019onde principales&nbsp;: ' + l.join(', ') + '&nbsp;nm. ' + (el === 'Na' ? 'Le doublet jaune, à 589,0 et 589,6&nbsp;nm, domine.' : (el === 'Ne' ? 'Ses nombreuses raies rouges et orangées donnent la couleur des enseignes au néon.' : ''));
      msg.innerHTML = msg.innerHTML.replace('Le hélium', 'L\u2019hélium');
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 600 ? 360 : 380; }, draw);
    $$(root, 'input[name="ra-e"]').forEach(function (r) { r.addEventListener('change', function () { el = r.value; texte(); draw(cnv); }); });
    $$(root, 'input[name="ra-m"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; texte(); draw(cnv); }); });
    texte(); draw(cnv);
  })();

  /* =================== 8. Lire le spectre du Soleil =================== */
  (function () {
    var root = document.getElementById('lab-soleil'); if (!root) { return; }
    var msg = $(root, '.nt-msg'), el = '', cnv;
    var SOLEIL = [[393.4, 1], [396.8, 1], [410.2, 0.5], [422.7, 0.6], [430.8, 0.7], [434.0, 0.6], [438.4, 0.4], [486.1, 0.8], [495.8, 0.35], [516.7, 0.6], [517.3, 0.7], [518.4, 0.8], [527.0, 0.5], [532.8, 0.3], [589.0, 0.9], [589.6, 0.9], [656.3, 1], [686.7, 0.7]];
    var REP = { H: 'Les quatre raies de l\u2019hydrogène (410, 434, 486 et 656&nbsp;nm) correspondent à des raies noires du Soleil&nbsp;: il y a de l\u2019<b>hydrogène</b> dans l\u2019atmosphère du Soleil. C\u2019est d\u2019ailleurs son principal constituant.', Na: 'Le doublet jaune du sodium (589,0 et 589,6&nbsp;nm) correspond au doublet noir «&nbsp;D&nbsp;» du Soleil&nbsp;: il y a du <b>sodium</b>.', Mg: 'Le triplet vert du magnésium (vers 517&nbsp;nm) se retrouve dans le spectre solaire&nbsp;: il y a du <b>magnésium</b>.', Hg: 'Les raies du mercure (436, 546, 577&nbsp;nm) ne correspondent à aucune raie noire du Soleil&nbsp;: on ne détecte pas de mercure.' };
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, sx = 20, sw = W - 40, y1 = 34, h1 = 60;
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#0B1120'; ctx.fillRect(0, 0, W, H);
      txt(ctx, 'spectre de la lumière du Soleil', sx, y1 - 10, { size: 11.5, col: '#FDE68A', align: 'left', bold: true });
      bandeSpectre(ctx, sx, y1, sw, h1, 380, 750, 'absorption', SOLEIL, { axe: !el });
      if (el) {
        var y2 = y1 + h1 + 30; bandeSpectre(ctx, sx, y2, sw, 40, 380, 750, 'emission', RAIES[el], { axe: true }); txt(ctx, 'spectre d\u2019émission du ' + NOMS[el], sx, y2 - 8, { size: 11, col: '#E2E8F0', align: 'left' });
        ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = 'rgba(255,255,255,0.5)'; RAIES[el].filter(function (q) { return q[1] > 0.3; }).forEach(function (q) { var x = sx + (q[0] - 380) / 370 * sw; ctx.beginPath(); ctx.moveTo(x, y1); ctx.lineTo(x, y2 + 40); ctx.stroke(); }); ctx.restore();
      }
    }
    cnv = Canvas($(root, 'canvas'), function () { return 200; }, draw);
    $$(root, 'input[name="so-e"]').forEach(function (r) { r.addEventListener('change', function () { el = r.value; msg.innerHTML = el ? REP[el] : 'Choisissez un élément, et comparez la position de ses raies avec les raies noires du Soleil.'; draw(cnv); }); });
    msg.innerHTML = 'Choisissez un élément, et comparez la position de ses raies avec les raies noires du Soleil.'; draw(cnv);
  })();


  var INC = '#16A34A', REFL = '#DB2777', REFR = '#CA8A04';   /* rayon incident, réfléchi, réfracté */
  function deg(a) { return a * 180 / Math.PI; } function rad(a) { return a * Math.PI / 180; }
  function arcAngle(ctx, x, y, r, a0, a1, col, lab, lx, ly) { ctx.strokeStyle = col; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(x, y, r, Math.min(a0, a1), Math.max(a0, a1)); ctx.stroke(); if (lab) { txt(ctx, lab, lx, ly, { size: 12, col: col, bold: true }); } }
  function rayon(ctx, x1, y1, x2, y2, col, w, al) { ctx.save(); ctx.globalAlpha = al === undefined ? 1 : al; ctx.strokeStyle = col; ctx.lineWidth = w; ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke(); var mx = x1 + (x2 - x1) * 0.55, my = y1 + (y2 - y1) * 0.55; vec(ctx, x1 + (x2 - x1) * 0.45, y1 + (y2 - y1) * 0.45, mx, my, col, w, 11); ctx.restore(); }   /* rayon avec sa flèche au milieu */

  /* =================== 10. Réflexion et réfraction =================== */
  function faisceau(ctx, x1, y1, x2, y2, col, al) {   /* rayon lumineux en halo, avec sa flèche */
    ctx.save(); ctx.globalAlpha = al === undefined ? 1 : al; ctx.lineCap = 'round';
    ctx.strokeStyle = col; ctx.globalAlpha *= 0.25; ctx.lineWidth = 9; ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
    ctx.globalAlpha /= 0.25; ctx.lineWidth = 3.2; ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
    vec(ctx, x1 + (x2 - x1) * 0.45, y1 + (y2 - y1) * 0.45, x1 + (x2 - x1) * 0.56, y1 + (y2 - y1) * 0.56, col, 3.2, 13); ctx.restore();
  }
  function secteur(ctx, x, y, r, a0, a1, col, lab, ang) {   /* angle repéré par un secteur coloré et une étiquette */
    ctx.save(); ctx.fillStyle = col; ctx.globalAlpha = 0.16; ctx.beginPath(); ctx.moveTo(x, y); ctx.arc(x, y, r, Math.min(a0, a1), Math.max(a0, a1)); ctx.closePath(); ctx.fill(); ctx.restore();
    ctx.strokeStyle = col; ctx.lineWidth = 1.8; ctx.beginPath(); ctx.arc(x, y, r, Math.min(a0, a1), Math.max(a0, a1)); ctx.stroke();
    var am = (a0 + a1) / 2; return function () { pill(ctx, lab, x + (r + 26) * Math.cos(am), y + (r + 18) * Math.sin(am), { size: 11.5, col: col, stroke: '#E2E8F0' }); };   /* l'étiquette est dessinée plus tard, au premier plan */
  }
  (function () {
    var root = document.getElementById('lab-snell'); if (!root) { return; }
    var inI = $(root, '[data-in="i"]'), msg = $(root, '.nt-msg'), cnv, k1 = 0, k2 = 1;
    var MIL = [['air', 1.00, ['#F8FAFC', '#E0F2FE']], ['eau', 1.33, ['#7DD3FC', '#0284C7']], ['verre', 1.50, ['#99F6E4', '#14B8A6']], ['diamant', 2.42, ['#E9D5FF', '#A78BFA']]];
    $$(root, '.nt-seg-mil').forEach(function (g) { var nom = g.getAttribute('data-g'); MIL.forEach(function (m, k) { var l = document.createElement('label'); l.innerHTML = '<input type="radio" name="sn-' + nom + '" value="' + k + '"' + ((nom === 'm1' ? 0 : 1) === k ? ' checked' : '') + '><span><i class="sw" style="background:linear-gradient(135deg,' + m[2][0] + ',' + m[2][1] + ')"></i>' + m[0] + ' <small>(' + fmt(m[1], 2) + ')</small></span>'; g.appendChild(l); l.querySelector('input').addEventListener('change', function () { if (nom === 'm1') { k1 = k; } else { k2 = k; } texte(); draw(cnv); }); }); });
    function fresnel(n1, n2, i1, i2) { var c1 = Math.cos(i1), c2 = Math.cos(i2), rs = (n1 * c1 - n2 * c2) / (n1 * c1 + n2 * c2), rp = (n1 * c2 - n2 * c1) / (n1 * c2 + n2 * c1); return (rs * rs + rp * rp) / 2; }   /* part de la lumière réfléchie */
    function milieu(ctx, m, x, y, w, h, haut) {
      var g = ctx.createLinearGradient(0, y, 0, y + h); g.addColorStop(haut ? 0 : 1, m[2][0]); g.addColorStop(haut ? 1 : 0, m[2][1]); ctx.globalAlpha = m[0] === 'air' ? 1 : 0.55; ctx.fillStyle = g; ctx.fillRect(x, y, w, h); ctx.globalAlpha = 1;
      ctx.save(); ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip();
      if (m[0] === 'eau') { ctx.strokeStyle = 'rgba(255,255,255,0.35)'; ctx.lineWidth = 1.2; for (var k = 0; k < 8; k++) { var yy = y + (k + 0.5) * h / 8; ctx.beginPath(); for (var xx = x; xx <= x + w; xx += 12) { ctx.lineTo(xx, yy + Math.sin(xx / 22 + k) * 2.5); } ctx.stroke(); } }
      if (m[0] === 'verre') { ctx.strokeStyle = 'rgba(255,255,255,0.35)'; ctx.lineWidth = 10; for (var v = -h; v < w; v += 70) { ctx.beginPath(); ctx.moveTo(x + v, y + h); ctx.lineTo(x + v + h * 0.6, y); ctx.stroke(); } }
      if (m[0] === 'diamant') { ctx.strokeStyle = 'rgba(255,255,255,0.45)'; ctx.lineWidth = 1; for (var d = 0; d < 14; d++) { var px = x + ((d * 97) % 100) / 100 * w, py = y + ((d * 61) % 100) / 100 * h; ctx.beginPath(); ctx.moveTo(px - 8, py); ctx.lineTo(px + 8, py); ctx.moveTo(px, py - 8); ctx.lineTo(px, py + 8); ctx.stroke(); } }
      ctx.restore();
    }
    function laser(ctx, x, y, a) {   /* pointeur laser orienté vers le point d'incidence */
      ctx.save(); ctx.translate(x, y); ctx.rotate(a); var g = ctx.createLinearGradient(0, -9, 0, 9); g.addColorStop(0, '#94A3B8'); g.addColorStop(0.5, '#F1F5F9'); g.addColorStop(1, '#475569'); ctx.fillStyle = g; rr(ctx, -64, -9, 60, 18, 6); ctx.fill(); ctx.fillStyle = '#1E293B'; rr(ctx, -6, -6, 10, 12, 2); ctx.fill(); ctx.fillStyle = '#16A34A'; ctx.beginPath(); ctx.arc(-44, -9, 3.5, Math.PI, 0); ctx.fill(); ctx.restore();
    }
    function geo(o) { var W = o.W, H = o.H; return { Ix: W / 2, Iy: H / 2, L: Math.min(W * 0.42, H * 0.44) }; }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, G = geo(o), m1 = MIL[k1], m2 = MIL[k2], i1 = rad(+inI.value), Ix = G.Ix, Iy = G.Iy, L = G.L;
      var s = m1[1] * Math.sin(i1) / m2[1], tot = s > 1, i2 = tot ? null : Math.asin(s), R = tot ? 1 : fresnel(m1[1], m2[1], i1, i2);
      ctx.clearRect(0, 0, W, H); milieu(ctx, m1, 0, 0, W, Iy, true); milieu(ctx, m2, 0, Iy, W, H - Iy, false);
      ctx.strokeStyle = 'rgba(15,23,42,0.55)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(0, Iy); ctx.lineTo(W, Iy); ctx.stroke(); txt(ctx, 'surface de séparation', W - 8, Iy - 9, { size: 10, col: '#334155', align: 'right' });
      pill(ctx, m1[0] + ' \u00B7 n\u2081 = ' + fmt(m1[1], 2), 10, 16, { size: 11.5, col: NAVY, align: 'left', stroke: GRID2 }); pill(ctx, m2[0] + ' \u00B7 n\u2082 = ' + fmt(m2[1], 2), 10, H - 16, { size: 11.5, col: NAVY, align: 'left', stroke: GRID2 });
      ctx.save(); ctx.setLineDash([7, 6]); ctx.strokeStyle = 'rgba(15,23,42,0.6)'; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(Ix, 8); ctx.lineTo(Ix, H - 8); ctx.stroke(); ctx.restore(); pill(ctx, 'normale', Ix, 14, { size: 10, col: '#334155', stroke: GRID2 });
      var Ax = Ix - L * Math.sin(i1), Ay = Iy - L * Math.cos(i1);
      faisceau(ctx, Ax, Ay, Ix, Iy, INC, 1);
      faisceau(ctx, Ix, Iy, Ix + L * Math.sin(i1), Iy - L * Math.cos(i1), REFL, Math.max(0.3, Math.min(1, 0.3 + R * 3)));
      if (!tot) { faisceau(ctx, Ix, Iy, Ix + L * Math.sin(i2), Iy + L * Math.cos(i2), REFR, Math.max(0.4, 1 - R)); }
      laser(ctx, Ax, Ay, Math.atan2(Iy - Ay, Ix - Ax));
      var gI = ctx.createRadialGradient(Ix, Iy, 0, Ix, Iy, 12); gI.addColorStop(0, 'rgba(255,255,255,0.95)'); gI.addColorStop(1, 'rgba(255,255,255,0)'); ctx.fillStyle = gI; ctx.beginPath(); ctx.arc(Ix, Iy, 12, 0, 2 * Math.PI); ctx.fill(); txt(ctx, 'I', Ix - 12, Iy + 13, { size: 13, col: '#0F172A', bold: true, serif: true });
      var r0 = 52, etiq = []; if (i1 > 0.03) { etiq.push(secteur(ctx, Ix, Iy, r0 + 16, -Math.PI / 2, -Math.PI / 2 + i1, REFL, 'r = ' + fmt(deg(i1), 0) + '°')); etiq.push(secteur(ctx, Ix, Iy, r0, -Math.PI / 2 - i1, -Math.PI / 2, INC, 'i\u2081 = ' + fmt(deg(i1), 0) + '°')); }
      if (!tot && i2 > 0.03) { etiq.push(secteur(ctx, Ix, Iy, r0, Math.PI / 2 - i2, Math.PI / 2, REFR, 'i\u2082 = ' + fmt(deg(i2), 1) + '°')); }
      etiq.forEach(function (f) { f(); });   /* toutes les étiquettes d'angles au premier plan */
      if (tot) { pill(ctx, 'réflexion totale\u00A0: plus de rayon réfracté\u00A0!', Ix, Iy + 48, { size: 12, col: '#B91C1C', stroke: '#FECACA' }); }
      pill(ctx, '\u25CF incident', W - 10, 16, { size: 10.5, col: INC, align: 'right', stroke: GRID2 }); pill(ctx, '\u25CF réfléchi', W - 10, 38, { size: 10.5, col: REFL, align: 'right', stroke: GRID2 }); pill(ctx, '\u25CF réfracté', W - 10, 60, { size: 10.5, col: REFR, align: 'right', stroke: GRID2 });
    }
    function texte() {
      var m1 = MIL[k1], m2 = MIL[k2], i1 = +inI.value, s = m1[1] * Math.sin(rad(i1)) / m2[1], f2 = function (v, d) { return String(fmt(v, d)).replace(',', '{,}'); };
      $(root, '.out-i').textContent = i1 + '°';
      if (s > 1) { var ic = deg(Math.asin(m2[1] / m1[1])); msg.innerHTML = 'Au-delà de l\u2019angle critique $i_\\text{c} = \\sin^{-1}\\left(\\dfrac{n_2}{n_1}\\right) \\approx ' + fmt(ic, 0) + '°$, il n\u2019y a plus de rayon réfracté&nbsp;: toute la lumière est réfléchie. C\u2019est la <b>réflexion totale</b> (voir la partie «&nbsp;La réflexion totale&nbsp;»).'; }
      else { var i2 = deg(Math.asin(s)); msg.innerHTML = '$n_1 \\times \\sin(i_1) = ' + f2(m1[1], 2) + ' \\times \\sin(' + i1 + '°) \\approx ' + f2(m1[1] * Math.sin(rad(i1)), 3) + '$ et $n_2 \\times \\sin(i_2) = ' + f2(m2[1], 2) + ' \\times \\sin(' + f2(i2, 1) + '°) \\approx ' + f2(m2[1] * Math.sin(rad(i2)), 3) + '$. ' + (m1[1] === m2[1] ? 'Les deux milieux ont le même indice&nbsp;: pas de réfraction, le rayon n\u2019est pas dévié.' : (m2[1] > m1[1] ? 'Le milieu 2 a un indice plus grand&nbsp;: le rayon réfracté se <b>rapproche</b> de la normale.' : 'Le milieu 2 a un indice plus petit&nbsp;: le rayon réfracté s\u2019<b>éloigne</b> de la normale.')); }
      typeset(msg);
    }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 340 : 380; }, draw);
    inI.addEventListener('input', function () { texte(); draw(cnv); });
    cnv.cv.style.touchAction = 'none';
    cnv.cv.addEventListener('pointerdown', function (e) { function suivre(ev) { var r = cnv.cv.getBoundingClientRect(), x = ev.clientX - r.left - cnv.W / 2, y = cnv.H / 2 - (ev.clientY - r.top); if (y > 0) { inI.value = Math.round(Math.min(89, Math.abs(deg(Math.atan2(x, y))))); texte(); draw(cnv); } } suivre(e); cnv.cv.setPointerCapture(e.pointerId); cnv.cv.onpointermove = suivre; cnv.cv.onpointerup = function () { cnv.cv.onpointermove = null; }; });   /* on oriente le laser à la souris ou au doigt */
    texte(); draw(cnv);
  })();

  /* =================== 11. Tester la loi de la réfraction et mesurer un indice =================== */
  (function () {
    var root = document.getElementById('lab-mesures'); if (!root) { return; }
    var inI = $(root, '[data-in="i"]'), msg = $(root, '.nt-msg'), bD = $(root, '[data-act="droite"]'), cnv, n, M = [], fit = false;
    function nouveau() { n = 1.45 + Math.round(Math.random() * 25) / 100; M = []; fit = false; bD.disabled = true; }
    function i2De(i1) { return deg(Math.asin(Math.sin(rad(i1)) / n)); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, two = W >= 640, cx = two ? W * 0.22 : W / 2, cy = two ? H * 0.5 : 124, R = two ? Math.min(W * 0.15, H * 0.32) : 80, i1 = +inI.value, i2 = i2De(i1);
      ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#FFFFFF'; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 1; ctx.beginPath(); ctx.arc(cx, cy, R + 14, 0, 2 * Math.PI); ctx.stroke();   /* rapporteur */
      ctx.fillStyle = 'rgba(241,245,249,0.6)'; ctx.beginPath(); ctx.arc(cx, cy, R + 14, 0, 2 * Math.PI); ctx.arc(cx, cy, R + 1, 0, 2 * Math.PI, true); ctx.fill();   /* couronne du rapporteur */
      ctx.strokeStyle = '#64748B'; for (var a = 0; a < 360; a += 5) { var c = Math.sin(rad(a)), s = -Math.cos(rad(a)), l = a % 30 === 0 ? 11 : (a % 10 === 0 ? 7 : 4); ctx.lineWidth = a % 30 === 0 ? 1.4 : 0.8; ctx.beginPath(); ctx.moveTo(cx + (R + 14) * c, cy + (R + 14) * s); ctx.lineTo(cx + (R + 14 - l) * c, cy + (R + 14 - l) * s); ctx.stroke();   /* graduations tous les 5°, repérées depuis la normale */
        if (a % 30 === 0) { var v = a <= 90 ? a : (a <= 180 ? 180 - a : (a <= 270 ? a - 180 : 360 - a)); txt(ctx, v + '°', cx + (R + 26) * c, cy + (R + 26) * s, { size: 9.5, col: '#334155' }); } }
      ctx.fillStyle = 'rgba(165,243,252,0.45)'; ctx.strokeStyle = '#0891B2'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(cx - R, cy); ctx.arc(cx, cy, R, 0, Math.PI); ctx.closePath(); ctx.fill(); ctx.stroke();   /* demi-cylindre, face plane en haut */
      ctx.save(); ctx.setLineDash([5, 4]); ctx.strokeStyle = '#64748B'; ctx.beginPath(); ctx.moveTo(cx, cy - R - 14); ctx.lineTo(cx, cy + R + 14); ctx.stroke(); ctx.restore();
      rayon(ctx, cx - (R + 14) * Math.sin(rad(i1)), cy - (R + 14) * Math.cos(rad(i1)), cx, cy, '#DC2626', 2.5);
      rayon(ctx, cx, cy, cx + (R + 14) * Math.sin(rad(i2)), cy + (R + 14) * Math.cos(rad(i2)), '#DC2626', 2.5);
      txt(ctx, 'air', cx - R - 4, cy - 12, { size: 10.5, col: SLATE, align: 'left' }); txt(ctx, 'plexiglas', cx - R + 8, cy + 14, { size: 10.5, col: '#0E7490', align: 'left' });
      var tx = two ? W * 0.44 : 30, ty = two ? 22 : 246;   /* tableau des mesures (sous le montage, sur téléphone) */
      txt(ctx, 'i\u2081', tx, ty, { size: 11, col: NAVY, bold: true }); txt(ctx, 'i\u2082', tx + 44, ty, { size: 11, col: NAVY, bold: true }); txt(ctx, 'sin i\u2081', tx + 92, ty, { size: 11, col: NAVY, bold: true }); txt(ctx, 'sin i\u2082', tx + 146, ty, { size: 11, col: NAVY, bold: true });
      M.slice().sort(function (a, b) { return a[0] - b[0]; }).forEach(function (m, k) { var y = ty + 18 + k * 17; txt(ctx, m[0] + '°', tx, y, { size: 11, col: SLATE }); txt(ctx, m[1] + '°', tx + 44, y, { size: 11, col: SLATE }); txt(ctx, fmt(Math.sin(rad(m[0])), 2), tx + 92, y, { size: 11, col: SLATE }); txt(ctx, fmt(Math.sin(rad(m[1])), 2), tx + 146, y, { size: 11, col: SLATE }); });
      var gx = two ? W * 0.72 : 40, gy = two ? 24 : 360, gw = two ? W * 0.25 : W - 64, gh = two ? H - 64 : H - 400, X = function (v) { return gx + v * gw; }, Y = function (v) { return gy + gh - v * gh; };   /* graphique sin i1 = f(sin i2) */
      ctx.strokeStyle = '#E2E8F0'; for (var v = 0; v <= 1.001; v += 0.2) { ctx.beginPath(); ctx.moveTo(X(0), Y(v)); ctx.lineTo(X(1), Y(v)); ctx.stroke(); ctx.beginPath(); ctx.moveTo(X(v), Y(0)); ctx.lineTo(X(v), Y(1)); ctx.stroke(); txt(ctx, fmt(v, 1), X(v), Y(0) + 12, { size: 9.5, col: SLATE }); txt(ctx, fmt(v, 1), X(0) - 4, Y(v), { size: 9.5, col: SLATE, align: 'right' }); }
      txt(ctx, 'sin i\u2081', X(0) + 4, gy - 8, { size: 10.5, col: NAVY, align: 'left' }); txt(ctx, 'sin i\u2082', X(1), Y(0) + 26, { size: 10.5, col: NAVY, align: 'right' });
      M.forEach(function (m) { croix(ctx, X(Math.sin(rad(m[1]))), Y(Math.sin(rad(m[0]))), '#DC2626', 4.5); });
      if (fit) { var a = pente(); ctx.strokeStyle = '#2563EB'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(Math.min(1, 1 / a)), Y(Math.min(1, a))); ctx.stroke(); }
    }
    function pente() { var sxy = 0, sxx = 0; M.forEach(function (m) { var x = Math.sin(rad(m[1])), y = Math.sin(rad(m[0])); sxy += x * y; sxx += x * x; }); return sxy / sxx; }   /* droite passant par l'origine, au sens des moindres carrés */
    function texte() { $(root, '.out-i').textContent = inI.value + '°'; }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 640 ? 600 : 300; }, draw);
    inI.addEventListener('input', function () { texte(); draw(cnv); });
    $(root, '[data-act="mesure"]').addEventListener('click', function () {
      var i1 = +inI.value;   /* la mesure (0 ; 0) est une mesure comme une autre : le rayon n'est pas dévié */
      var mes = i1 === 0 ? 0 : Math.round(i2De(i1) + (Math.random() - 0.5) * 1.2);   /* mesure au degré près, avec une petite incertitude */
      M = M.filter(function (m) { return m[0] !== i1; }); M.push([i1, mes]); bD.disabled = M.length < 3;
      msg.innerHTML = 'Mesure&nbsp;: pour $i_1 = ' + i1 + '°$, on lit $i_2 \\approx ' + mes + '°$. ' + (i1 === 0 ? 'Sous incidence normale, le rayon n\u2019est pas dévié. ' : '') + (M.length < 3 ? 'Faites au moins trois mesures.' : 'Les points semblent alignés avec l\u2019origine&nbsp;: tracez la droite.'); typeset(msg); draw(cnv);
    });
    bD.addEventListener('click', function () { fit = true; draw(cnv); var a = pente(); msg.innerHTML = 'Les points sont alignés sur une droite passant par l\u2019origine&nbsp;: $\\sin(i_1)$ est proportionnel à $\\sin(i_2)$, comme le prévoit la loi de la réfraction $1{,}00 \\times \\sin(i_1) = n \\times \\sin(i_2)$. Le coefficient directeur de la droite est l\u2019indice du plexiglas&nbsp;: $n \\approx ' + String(fmt(a, 2)).replace(',', '{,}') + '$ (valeur exacte de cette simulation&nbsp;: ' + fmt(n, 2) + ').'; typeset(msg); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { nouveau(); draw(cnv); msg.textContent = 'Nouveau bloc de plexiglas, d\u2019indice inconnu. Mesurez i\u2082 pour plusieurs angles d\u2019incidence.'; });
    nouveau(); texte(); msg.textContent = 'Choisissez un angle d\u2019incidence, puis mesurez l\u2019angle de réfraction. Recommencez pour plusieurs angles.'; draw(cnv);
  })();

  /* =================== 12. L'expérience de la pièce =================== */
  (function () {
    var root = document.getElementById('lab-piece'); if (!root) { return; }
    var inH = $(root, '[data-in="h"]'), msg = $(root, '.nt-msg'), cnv, NE = 1.33, visible = false;
    function piece(ctx, x, y, al) { ctx.save(); ctx.globalAlpha = al; var g = ctx.createLinearGradient(x - 14, 0, x + 14, 0); g.addColorStop(0, '#B45309'); g.addColorStop(0.45, '#FDE68A'); g.addColorStop(1, '#B45309'); ctx.fillStyle = g; ctx.beginPath(); ctx.ellipse(x, y, 14, 4, 0, 0, 2 * Math.PI); ctx.fill(); ctx.strokeStyle = 'rgba(146,64,14,0.7)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.ellipse(x, y - 0.5, 10, 2.6, 0, 0, 2 * Math.PI); ctx.stroke(); ctx.restore(); }
    function oeilDessin(ctx, x, y, ang) {   /* œil de profil-trois-quarts, regardant dans la direction ang */
      ctx.save(); ctx.translate(x, y); ctx.rotate(ang);
      ctx.fillStyle = 'rgba(15,23,42,0.08)'; ctx.beginPath(); ctx.ellipse(-2, 2, 26, 15, 0, 0, 2 * Math.PI); ctx.fill();
      ctx.beginPath(); ctx.moveTo(-22, 0); ctx.quadraticCurveTo(0, -17, 22, 0); ctx.quadraticCurveTo(0, 15, -22, 0); ctx.closePath();   /* contour en amande */
      var gb = ctx.createRadialGradient(0, 0, 2, 0, 0, 22); gb.addColorStop(0, '#FFFFFF'); gb.addColorStop(1, '#E2E8F0'); ctx.fillStyle = gb; ctx.fill();
      ctx.save(); ctx.clip(); var gi = ctx.createRadialGradient(5, 0, 1, 5, 0, 9); gi.addColorStop(0, '#D97706'); gi.addColorStop(0.6, '#92400E'); gi.addColorStop(1, '#451A03'); ctx.fillStyle = gi; ctx.beginPath(); ctx.arc(5, 0, 9, 0, 2 * Math.PI); ctx.fill();   /* iris */
      ctx.fillStyle = '#0F172A'; ctx.beginPath(); ctx.arc(5, 0, 4, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = 'rgba(255,255,255,0.9)'; ctx.beginPath(); ctx.arc(2, -3, 2, 0, 2 * Math.PI); ctx.fill(); ctx.restore();
      ctx.strokeStyle = '#7C2D12'; ctx.lineWidth = 2.2; ctx.beginPath(); ctx.moveTo(-22, 0); ctx.quadraticCurveTo(0, -17, 22, 0); ctx.stroke();   /* paupière */
      ctx.lineWidth = 1.2; for (var k = 0; k < 5; k++) { var t = 0.2 + k * 0.15, px = -22 + 44 * t, py = -17 * 2 * t * (1 - t) * 2 * 0.5 - 0.5; ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(px + 2, py - 5); ctx.stroke(); }   /* cils */
      ctx.strokeStyle = 'rgba(124,45,18,0.35)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(-20, 3); ctx.quadraticCurveTo(0, 14, 20, 3); ctx.stroke();
      ctx.restore();
    }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, bw = Math.min(280, W * 0.56), bx = W * 0.56, table = H - 26, fond = table - 14, haut = Math.max(96, H * 0.34), prof = fond - haut, hp = (+inH.value / 100) * prof * 0.92, surf = fond - hp;
      var mur = bx - bw / 2, bord = [mur, haut], xVis = bx + bw * 0.18, pente = (xVis - mur) / prof, oeil = [mur - (haut - 30) * pente, 30], coin = [bx, fond - 3];   /* la ligne de visée qui rase le bord tombe nettement à droite de la pièce */
      ctx.clearRect(0, 0, W, H); var gm = ctx.createLinearGradient(0, 0, 0, table); gm.addColorStop(0, '#FFF7ED'); gm.addColorStop(1, '#FDE7D3'); ctx.fillStyle = gm; ctx.fillRect(0, 0, W, table);
      var gt = ctx.createLinearGradient(0, table, 0, H); gt.addColorStop(0, '#B07B4F'); gt.addColorStop(1, '#7C4A2A'); ctx.fillStyle = gt; ctx.fillRect(0, table, W, H - table);   /* table en bois */
      ctx.fillStyle = 'rgba(15,23,42,0.15)'; ctx.beginPath(); ctx.ellipse(bx, table + 3, bw * 0.6, 6, 0, 0, 2 * Math.PI); ctx.fill();
      var gi = ctx.createLinearGradient(mur, 0, mur + bw, 0); gi.addColorStop(0, '#E2E8F0'); gi.addColorStop(0.5, '#F8FAFC'); gi.addColorStop(1, '#CBD5E1'); ctx.fillStyle = gi; ctx.fillRect(mur, haut, bw, prof);   /* intérieur du bol */
      if (hp > 0) { var ge = ctx.createLinearGradient(0, surf, 0, fond); ge.addColorStop(0, 'rgba(125,211,252,0.55)'); ge.addColorStop(1, 'rgba(14,165,233,0.6)'); ctx.fillStyle = ge; ctx.fillRect(mur, surf, bw, hp); ctx.strokeStyle = 'rgba(255,255,255,0.9)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(mur, surf); ctx.lineTo(mur + bw, surf); ctx.stroke(); }
      var ok = false, P = null, a = 0;
      if (hp > 3) {   /* rayon issu de la pièce qui atteint l'œil après réfraction à la surface : point de sortie P cherché par dichotomie */
        var lo = mur, hi = coin[0];
        for (var k = 0; k < 60; k++) { var xs = (lo + hi) / 2, i2 = Math.atan2(coin[0] - xs, coin[1] - surf), sa = NE * Math.sin(i2); if (sa >= 1) { lo = xs; continue; } var aa = Math.asin(sa), xe = xs - (surf - oeil[1]) * Math.tan(aa); if (xe < oeil[0]) { lo = xs; } else { hi = xs; } }
        var xp = (lo + hi) / 2, ib = Math.atan2(coin[0] - xp, coin[1] - surf), sb = NE * Math.sin(ib);
        if (sb < 1) { a = Math.asin(sb); P = [xp, surf]; ok = surf - (xp - mur) / Math.tan(a) < haut - 1 && Math.abs(xp - (surf - oeil[1]) * Math.tan(a) - oeil[0]) < 3; }   /* le rayon doit passer au-dessus du bord */
      }
      visible = ok;
      ctx.save(); ctx.setLineDash([5, 5]); ctx.strokeStyle = 'rgba(71,85,105,0.55)'; ctx.lineWidth = 1.3; ctx.beginPath(); ctx.moveTo(oeil[0], oeil[1]); ctx.lineTo(xVis, fond); ctx.stroke(); ctx.restore();   /* ligne de visée qui rase le bord : sans eau, l'œil ne voit pas plus bas */
      if (ok) {
        var yI = surf + (coin[0] - P[0]) / Math.tan(a);
        ctx.save(); ctx.setLineDash([5, 4]); ctx.strokeStyle = 'rgba(217,119,6,0.75)'; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(P[0], P[1]); ctx.lineTo(coin[0], yI); ctx.stroke(); ctx.restore();   /* prolongement du rayon reçu par l'œil */
        piece(ctx, coin[0], yI, 0.45); pill(ctx, 'image de la pièce', coin[0] + 24, yI - 12, { size: 10.5, col: '#92400E', align: 'left', stroke: '#FDE68A' });
        ctx.save(); ctx.setLineDash([3, 4]); ctx.strokeStyle = '#475569'; ctx.beginPath(); ctx.moveTo(P[0], surf - 34); ctx.lineTo(P[0], surf + 34); ctx.stroke(); ctx.restore();
        rayon(ctx, coin[0], coin[1] - 3, P[0], P[1], '#D97706', 2); rayon(ctx, P[0], P[1], oeil[0], oeil[1], '#D97706', 2);   /* le rayon réel, en trait simple */
      }
      piece(ctx, coin[0], coin[1], 1);
      var gb = ctx.createLinearGradient(mur - 10, 0, mur + bw + 10, 0); gb.addColorStop(0, '#1D4ED8'); gb.addColorStop(0.5, '#3B82F6'); gb.addColorStop(1, '#1E40AF');   /* parois du bol, en céramique bleue */
      ctx.fillStyle = gb; ctx.fillRect(mur - 10, haut, 10, prof + 14); ctx.fillRect(mur + bw, haut, 10, prof + 14); ctx.fillRect(mur - 10, fond, bw + 20, 14);
      ctx.fillStyle = 'rgba(255,255,255,0.35)'; ctx.fillRect(mur - 7, haut + 6, 3, prof - 6); ctx.fillStyle = '#93C5FD'; rr(ctx, mur - 12, haut - 4, 14, 6, 3); ctx.fill(); rr(ctx, mur + bw - 2, haut - 4, 14, 6, 3); ctx.fill();
      oeilDessin(ctx, oeil[0], oeil[1], Math.atan2(fond - oeil[1], xVis - oeil[0]));
    }
    function maj() { var h = +inH.value; $(root, '.out-h').textContent = h + '\u00A0%'; draw(cnv); msg.innerHTML = !visible ? (h < 5 ? 'Sans eau, le bord du bol cache la pièce&nbsp;: la ligne de visée qui rase le bord (en pointillés) passe bien à droite de la pièce. Aucun rayon issu de la pièce n\u2019atteint l\u2019œil en ligne droite.' : 'Pas encore assez d\u2019eau&nbsp;: les rayons issus de la pièce, même déviés à la surface, butent encore sur le bord du bol. Continuez à verser.') : 'La pièce apparaît&nbsp;! Les rayons issus de la pièce sont déviés en sortant de l\u2019eau&nbsp;: ils s\u2019éloignent de la normale et passent au-dessus du bord. L\u2019œil voit la pièce dans le prolongement du rayon qu\u2019il reçoit&nbsp;: plus haut, et plus à gauche, qu\u2019elle n\u2019est réellement.'; }
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 300 : 340; }, function (o) { draw(o); });
    inH.addEventListener('input', maj); maj();
  })();

  /* =================== 12 b. Lire un schéma de réfraction et trouver l'indice =================== */
  (function () {
    var root = document.getElementById('tr-indice'); if (!root) { return; }
    function schema(i1, i2, piege) {   /* schéma SVG : air en haut, milieu inconnu en bas */
      var W = 360, H = 230, Ix = 180, Iy = 110, L = 100, s = '<svg class="nt-qsvg" viewBox="0 0 ' + W + ' ' + H + '" width="' + W + '" role="img" aria-label="schéma de réfraction">';
      s += '<rect width="' + W + '" height="' + Iy + '" fill="#F1F5F9"/><rect y="' + Iy + '" width="' + W + '" height="' + (H - Iy) + '" fill="#BAE6FD" opacity="0.7"/><line x1="0" y1="' + Iy + '" x2="' + W + '" y2="' + Iy + '" stroke="#475569" stroke-width="2"/>';
      s += '<text x="8" y="18" font-size="12" fill="#334155">air, n₁ = 1,00</text><text x="8" y="' + (H - 8) + '" font-size="12" fill="#0C4A6E">milieu 2, indice n₂ ?</text>';
      var a1 = rad(i1), a2 = rad(i2), Ax = Ix - L * Math.sin(a1), Ay = Iy - L * Math.cos(a1), Bx = Ix + L * Math.sin(a2), By = Iy + L * Math.cos(a2);
      s += '<line x1="' + Ax.toFixed(1) + '" y1="' + Ay.toFixed(1) + '" x2="' + Ix + '" y2="' + Iy + '" stroke="#16A34A" stroke-width="3"/><line x1="' + Ix + '" y1="' + Iy + '" x2="' + Bx.toFixed(1) + '" y2="' + By.toFixed(1) + '" stroke="#CA8A04" stroke-width="3"/>';
      function arc(r, a0, a1, col) { var x0 = Ix + r * Math.cos(a0), y0 = Iy + r * Math.sin(a0), x1 = Ix + r * Math.cos(a1), y1 = Iy + r * Math.sin(a1); return '<path d="M' + x0.toFixed(1) + ',' + y0.toFixed(1) + ' A' + r + ',' + r + ' 0 0 ' + (a1 > a0 ? 1 : 0) + ' ' + x1.toFixed(1) + ',' + y1.toFixed(1) + '" fill="none" stroke="' + col + '" stroke-width="2"/>'; }
      function lab(t, a, r, col) { return '<text x="' + (Ix + r * Math.cos(a)).toFixed(1) + '" y="' + (Iy + r * Math.sin(a) + 4).toFixed(1) + '" font-size="13" font-weight="700" text-anchor="middle" fill="' + col + '">' + t + '</text>'; }
      if (!piege) {
        s += '<line x1="' + Ix + '" y1="10" x2="' + Ix + '" y2="' + (H - 10) + '" stroke="#475569" stroke-dasharray="6 5"/>';
        s += arc(42, -Math.PI / 2 - a1, -Math.PI / 2, '#16A34A') + lab(i1 + '°', -Math.PI / 2 - a1 / 2, 62, '#15803D');
        s += arc(42, Math.PI / 2 - a2, Math.PI / 2, '#CA8A04') + lab(i2 + '°', Math.PI / 2 - a2 / 2, 62, '#A16207');
      } else {   /* piège : les angles sont repérés depuis la surface, et la normale n'est pas tracée */
        s += arc(42, Math.PI, Math.PI + (Math.PI / 2 - a1), '#16A34A') + lab((90 - i1) + '°', Math.PI + (Math.PI / 2 - a1) / 2, 62, '#15803D');
        s += arc(42, 0, Math.PI / 2 - a2, '#CA8A04') + lab((90 - i2) + '°', (Math.PI / 2 - a2) / 2, 62, '#A16207');
      }
      return s + '<circle cx="' + Ix + '" cy="' + Iy + '" r="3" fill="#0F172A"/></svg>';
    }
    function fab() {
      var Q = [], cas = shuffle([false, false, true, false, true]);
      cas.forEach(function (piege) {
        var n = pick([1.33, 1.40, 1.47, 1.50, 1.60, 1.70]), i1 = pick([35, 40, 45, 50, 55, 60, 65]), i2 = Math.round(deg(Math.asin(Math.sin(rad(i1)) / n)));
        var bon = Math.sin(rad(i1)) / Math.sin(rad(i2)), faux1 = Math.sin(rad(90 - i1)) / Math.sin(rad(90 - i2)), faux2 = Math.sin(rad(i2)) / Math.sin(rad(i1)), faux3 = i1 / i2;
        var f = function (v) { return fmt(v, 2); }, opts = [f(bon)]; [piege ? f(faux1) : f(faux3), f(faux2), piege ? f(faux3) : f(Math.sin(rad(90 - i1)) / Math.sin(rad(90 - i2)))].forEach(function (v) { if (opts.indexOf(v) < 0) { opts.push(v); } });
        Q.push(['Un rayon lumineux passe de l\u2019air dans un milieu transparent. D\u2019après le schéma, que vaut l\u2019indice optique $n_2$ de ce milieu&nbsp;?' + schema(i1, i2, piege), opts,
          (piege ? '<b>Attention&nbsp;: les angles sont mesurés depuis la surface, pas depuis la normale&nbsp;!</b> Les angles d\u2019incidence et de réfraction valent donc $i_1 = 90° - ' + (90 - i1) + '° = ' + i1 + '°$ et $i_2 = 90° - ' + (90 - i2) + '° = ' + i2 + '°$. ' : '') + 'D\u2019après la loi de la réfraction, $n_2 = \\dfrac{n_1 \\times \\sin(i_1)}{\\sin(i_2)} = \\dfrac{1{,}00 \\times \\sin(' + i1 + '°)}{\\sin(' + i2 + '°)} \\approx ' + String(f(bon)).replace(',', '{,}') + '$.']);
      });
      return Q;
    }
    Quiz(root, null, 5, fab);
  })();

  /* =================== 12 c. La lumière piégée dans une fibre optique =================== */
  (function () {
    var root = document.getElementById('lab-fibre'); if (!root) { return; }
    var inA = $(root, '[data-in="a"]'), inC = $(root, '[data-in="c"]'), msg = $(root, '.nt-msg'), cnv, t = 0, chemin = [], fuite = false, dernier = null, N1 = 1.50, N2 = 1.35, IC = Math.asin(N2 / N1);   /* angle critique cœur-gaine : 64° */
    function geo(o) { var W = o.W, H = o.H, w = Math.min(9, H * 0.03), yc = H * 0.32, Rb = 28 + (1 - +inC.value / 100) * Math.min(200, H * 0.55), Ls = Math.max(110, Math.min(W * 0.4, 380, W - Rb - 110)), tot = 64 + Ls + Rb + 24, x0 = Math.max(70, (W - tot) / 2 + 64), xA = x0 + Ls; return { W: W, H: H, w: w, yc: yc, Rb: Rb, xA: xA, x0: x0, C: [xA, yc + Rb], yEnd: H - 14 }; }   /* fibre centrée horizontalement ; cœur fin : avec la courbure initiale, un rayon dans l'axe reste piégé */   /* cœur fin : avec la courbure initiale, un rayon dans l'axe reste piégé */
    function tracer(g) {   /* lancer de rayon dans la fibre : réflexions sur les parois droites et courbes */
      var th = Math.asin(Math.sin(rad(+inA.value)) / N1), p = [g.x0, g.yc], d = [Math.cos(th), -Math.sin(th)], pts = [p.slice()], esc = null, imin = 90, lieu = '';
      for (var k = 0; k < 3000; k++) {
        var best = null;
        function essai(tt, nrm, ok) { if (tt > 1e-6 && (!best || tt < best[0]) && ok) { best = [tt, nrm]; } }
        [g.yc - g.w, g.yc + g.w].forEach(function (yy, s) { if (Math.abs(d[1]) > 1e-9) { var tt = (yy - p[1]) / d[1], x = p[0] + d[0] * tt; essai(tt, [0, s ? 1 : -1], x >= g.x0 - 1 && x <= g.xA + 6); } });   /* parois du premier tronçon droit */
        [g.C[0] + g.Rb - g.w, g.C[0] + g.Rb + g.w].forEach(function (xx, s) { if (Math.abs(d[0]) > 1e-9) { var tt = (xx - p[0]) / d[0], y = p[1] + d[1] * tt; essai(tt, [s ? 1 : -1, 0], y >= g.C[1] - 6 && y <= g.yEnd + 50); } });   /* parois du second tronçon droit */
        [g.Rb - g.w, g.Rb + g.w].forEach(function (r) { var fx = p[0] - g.C[0], fy = p[1] - g.C[1], b = fx * d[0] + fy * d[1], c = fx * fx + fy * fy - r * r, D = b * b - c; if (D < 0) { return; } [-b - Math.sqrt(D), -b + Math.sqrt(D)].forEach(function (tt) { var x = p[0] + d[0] * tt - g.C[0], y = p[1] + d[1] * tt - g.C[1], phi = Math.atan2(x, -y); essai(tt, [x / r, y / r], phi >= -0.04 && phi <= Math.PI / 2 + 0.04);   /* domaines qui se recouvrent un peu aux raccords : aucun rayon ne passe entre deux parois */ }); });   /* parois du coude */
        if (!best) { if (d[1] > 0) { var tf = (g.yEnd - p[1]) / d[1]; pts.push([p[0] + d[0] * tf, g.yEnd]); } return { pts: pts, esc: null, imin: imin }; }   /* plus aucune paroi devant : la lumière file jusqu'au bout de la fibre */
        var q = [p[0] + d[0] * best[0], p[1] + d[1] * best[0]];
        if (q[1] > g.yEnd) { var te = (g.yEnd - p[1]) / d[1]; pts.push([p[0] + d[0] * te, g.yEnd]); return { pts: pts, esc: null, imin: imin }; }   /* la lumière sort au bout de la fibre */
        pts.push(q); var nrm = best[1], cs = d[0] * nrm[0] + d[1] * nrm[1], inc = Math.acos(Math.min(1, Math.abs(cs))); imin = Math.min(imin, deg(inc)); lieu = q[0] <= g.xA + 1 ? 'dans la première partie droite' : (q[1] >= g.C[1] - 1 ? 'dans la partie verticale' : 'dans le coude');
        if (inc < IC) { var outw = cs > 0 ? nrm : [-nrm[0], -nrm[1]], c2 = Math.abs(cs), s2 = N1 / 1.0 * Math.sqrt(1 - c2 * c2), tg = [d[0] - cs * nrm[0], d[1] - cs * nrm[1]], mt = Math.hypot(tg[0], tg[1]) || 1; tg = [tg[0] / mt, tg[1] / mt]; var so = Math.min(0.999, s2), co = Math.sqrt(1 - so * so), dout = [tg[0] * so + outw[0] * co, tg[1] * so + outw[1] * co]; esc = [q, [q[0] + dout[0] * 2000, q[1] + dout[1] * 2000], deg(inc), lieu]; return { pts: pts, esc: esc, imin: imin }; }   /* la lumière sort de la fibre (réfractée vers l'air) et file jusqu'au bord du dessin */   /* incidence trop faible : la lumière s'échappe de la fibre */
        d = [d[0] - 2 * cs * nrm[0], d[1] - 2 * cs * nrm[1]]; p = q;
      }
      return { pts: pts, esc: esc, imin: imin };
    }
    function longueur(pts) { var L = 0; for (var i = 1; i < pts.length; i++) { L += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); } return L; }
    function draw(o) {
      var ctx = o.ctx, g = geo(o), W = g.W, H = g.H, R = tracer(g); chemin = R.pts.slice(); fuite = !!R.esc; dernier = R; if (R.esc) { chemin.push(R.esc[1]); }
      ctx.clearRect(0, 0, W, H); var gf = ctx.createLinearGradient(0, 0, 0, H); gf.addColorStop(0, '#0B1120'); gf.addColorStop(1, '#111827'); ctx.fillStyle = gf; ctx.fillRect(0, 0, W, H);
      function tubeF(w, col) { ctx.strokeStyle = col; ctx.lineWidth = 2 * w; ctx.lineCap = 'butt'; ctx.beginPath(); ctx.moveTo(g.x0, g.yc); ctx.lineTo(g.xA, g.yc); ctx.arc(g.C[0], g.C[1], g.Rb, -Math.PI / 2, 0); ctx.lineTo(g.C[0] + g.Rb, g.yEnd); ctx.stroke(); }
      tubeF(g.w + 12, '#334155'); tubeF(g.w + 10, '#475569'); tubeF(g.w + 6, 'rgba(148,163,184,0.55)'); tubeF(g.w, 'rgba(165,243,252,0.22)');   /* gaine protectrice, gaine optique, cœur */
      tubeF(1, 'rgba(255,255,255,0.12)');
      var L = 0, seg = []; for (var i = 1; i < chemin.length; i++) { var l = Math.hypot(chemin[i][0] - chemin[i - 1][0], chemin[i][1] - chemin[i - 1][1]); seg.push(l); L += l; }
      var s = (t * 260) % (L + 120), acc = 0, pulse = null;
      ctx.save(); ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.strokeStyle = 'rgba(248,113,113,0.22)'; ctx.lineWidth = 1.5; ctx.beginPath(); chemin.forEach(function (q, i) { if (i) { ctx.lineTo(q[0], q[1]); } else { ctx.moveTo(q[0], q[1]); } }); ctx.stroke();   /* tout le trajet, en pâle */
      ctx.strokeStyle = 'rgba(252,165,165,0.95)'; ctx.lineWidth = 2.4; ctx.shadowColor = 'rgba(248,113,113,0.9)'; ctx.shadowBlur = 8; ctx.beginPath(); ctx.moveTo(chemin[0][0], chemin[0][1]);
      for (i = 1; i < chemin.length; i++) { if (acc + seg[i - 1] >= s) { var u = (s - acc) / seg[i - 1]; pulse = [chemin[i - 1][0] + (chemin[i][0] - chemin[i - 1][0]) * u, chemin[i - 1][1] + (chemin[i][1] - chemin[i - 1][1]) * u]; ctx.lineTo(pulse[0], pulse[1]); break; } ctx.lineTo(chemin[i][0], chemin[i][1]); acc += seg[i - 1]; }
      ctx.stroke(); ctx.restore();   /* la partie déjà parcourue, en vif */
      if (pulse) { var gp = ctx.createRadialGradient(pulse[0], pulse[1], 0, pulse[0], pulse[1], 13); gp.addColorStop(0, 'rgba(255,255,255,1)'); gp.addColorStop(0.3, 'rgba(248,113,113,0.9)'); gp.addColorStop(1, 'rgba(248,113,113,0)'); ctx.fillStyle = gp; ctx.beginPath(); ctx.arc(pulse[0], pulse[1], 13, 0, 2 * Math.PI); ctx.fill(); }
      if (!fuite) { var ex = g.C[0] + g.Rb, ge = ctx.createRadialGradient(ex, g.yEnd, 0, ex, g.yEnd, 26); ge.addColorStop(0, 'rgba(254,202,202,0.8)'); ge.addColorStop(1, 'rgba(248,113,113,0)'); ctx.fillStyle = ge; ctx.beginPath(); ctx.arc(ex, g.yEnd, 26, 0, Math.PI); ctx.fill(); }   /* la lumière sort au bout de la fibre */
      else { ctx.strokeStyle = '#FDE047'; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(R.esc[0][0], R.esc[0][1], 9, 0, 2 * Math.PI); ctx.stroke();   /* l'endroit où la lumière s'échappe */
        var e0 = R.esc[0], de = [R.esc[1][0] - e0[0], R.esc[1][1] - e0[1]], me = Math.hypot(de[0], de[1]); de = [de[0] / me, de[1] / me]; var pe = [de[1], -de[0]]; if (pe[1] > 0) { pe = [-pe[0], -pe[1]]; } pill(ctx, 'la lumière s\u2019échappe\u00A0!', Math.min(W - 80, Math.max(80, e0[0] + de[0] * 80 + pe[0] * 22)), Math.min(H - 14, Math.max(14, e0[1] + de[1] * 80 + pe[1] * 22)), { size: 11, col: '#FCA5A5', bg: 'rgba(15,23,42,0.85)' }); }   /* étiquette à côté du rayon, pas dessus */
      var gl = ctx.createLinearGradient(0, -9, 0, 9); gl.addColorStop(0, '#94A3B8'); gl.addColorStop(0.5, '#F1F5F9'); gl.addColorStop(1, '#475569'); ctx.save(); ctx.translate(g.x0 - 6, g.yc); ctx.rotate(-rad(+inA.value)); ctx.fillStyle = gl; rr(ctx, -58, -9, 54, 18, 6); ctx.fill(); ctx.fillStyle = '#1E293B'; rr(ctx, -6, -5, 8, 10, 2); ctx.fill(); ctx.fillStyle = '#EF4444'; ctx.beginPath(); ctx.arc(-40, -9, 3, Math.PI, 0); ctx.fill(); ctx.restore();
      var lx = 14, ly = H - 62;   /* légende des indices */
      ctx.fillStyle = 'rgba(15,23,42,0.85)'; rr(ctx, lx, ly, 172, 54, 8); ctx.fill(); ctx.strokeStyle = 'rgba(148,163,184,0.4)'; ctx.lineWidth = 1; ctx.stroke();
      ctx.fillStyle = 'rgba(165,243,252,0.55)'; ctx.fillRect(lx + 10, ly + 10, 18, 8); txt(ctx, 'cœur\u00A0: n = 1,50', lx + 36, ly + 14, { size: 11, col: '#E2E8F0', align: 'left' });
      ctx.fillStyle = 'rgba(148,163,184,0.75)'; ctx.fillRect(lx + 10, ly + 26, 18, 8); txt(ctx, 'gaine\u00A0: n = 1,35', lx + 36, ly + 30, { size: 11, col: '#E2E8F0', align: 'left' });
      txt(ctx, 'angle critique\u00A0: 64°', lx + 10, ly + 45, { size: 10.5, col: '#94A3B8', align: 'left' });
      if (W >= 560) {   /* repères sur la fibre (la légende suffit sur téléphone) */
      var ax = Math.max(g.x0 + 40, g.xA - 150); ctx.strokeStyle = 'rgba(165,243,252,0.7)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(ax, g.yc - 2); ctx.lineTo(ax + 10, g.yc - 34); ctx.stroke(); txt(ctx, 'cœur', ax + 13, g.yc - 38, { size: 10.5, col: '#A5F3FC', align: 'left' });
      ctx.strokeStyle = 'rgba(203,213,225,0.7)'; ctx.beginPath(); ctx.moveTo(ax + 70, g.yc + g.w + 4); ctx.lineTo(ax + 80, g.yc + g.w + 34); ctx.stroke(); txt(ctx, 'gaine', ax + 83, g.yc + g.w + 38, { size: 10.5, col: '#CBD5E1', align: 'left' });
      }
    }
    function texte() {
      $(root, '.out-a').textContent = inA.value + '°'; $(root, '.out-c').textContent = (+inC.value < 30 ? 'faible' : (+inC.value < 70 ? 'moyenne' : 'forte'));
      var R = dernier; if (!R) { return; }
      msg.innerHTML = R.esc ? 'Avec cet angle d\u2019entrée, le rayon finit par rencontrer la gaine, ' + R.esc[3] + ' (cercle jaune), sous un <b>angle d\u2019incidence</b> de ' + fmt(R.esc[2], 0) + '°, mesuré par rapport à la normale à la gaine. C\u2019est moins que l\u2019angle critique (64°)&nbsp;: il n\u2019y a pas de réflexion totale, la lumière est réfractée et s\u2019échappe de la fibre. Attention à ne pas confondre l\u2019angle d\u2019entrée, réglé par le curseur, et l\u2019angle d\u2019incidence sur la gaine, qui change à chaque rebond, surtout dans le coude&nbsp;: c\u2019est pourquoi un petit changement de l\u2019angle d\u2019entrée peut suffire à faire fuir, ou à piéger, la lumière.' : 'À chaque rencontre avec la gaine, l\u2019angle d\u2019incidence (mesuré par rapport à la normale à la gaine) reste supérieur à l\u2019angle critique de 64°&nbsp;: le plus petit vaut ici ' + fmt(R.imin, 0) + '°. La lumière subit donc à chaque fois une <b>réflexion totale</b>, et reste piégée dans le cœur jusqu\u2019au bout de la fibre, même dans le coude.';
    }
    var loop = Loop(root, function (dt) { t += dt; draw(cnv); return true; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 300 : 340; }, draw);
    [inA, inC].forEach(function (i) { i.addEventListener('input', function () { draw(cnv); texte(); }); });
    draw(cnv); texte(); if (!RM) { loop.kick(); }
  })();

  /* =================== 12 d. Comment naissent les mirages =================== */
  (function () {
    var root = document.getElementById('lab-mirage'); if (!root) { return; }
    var chk = $(root, '[data-in="couches"]'), msg = $(root, '.nt-msg'), type = 'chaud', cnv, t = 0;
    var P = { chaud: [0.012, 8], froid: [0.02, 60] };   /* variation d'indice et épaisseur de la couche : très exagérées, pour que la courbure se voie */
    function n(h) { var K = P[type][0], LC = P[type][1]; return type === 'chaud' ? 1 + K * (1 - Math.exp(-h / LC)) : 1 + K * Math.exp(-h / LC); }
    function dn(h) { var K = P[type][0], LC = P[type][1]; return type === 'chaud' ? K / LC * Math.exp(-h / LC) : -K / LC * Math.exp(-h / LC); }   /* dérivée de l'indice par rapport à la hauteur */
    function rayon(x0, h0, th, xmax) {   /* intégration de la trajectoire d'un rayon (vers la droite) dans l'air stratifié */
      var x = x0, h = h0, tx = Math.cos(th), th2 = Math.sin(th), pts = [[x, h]], ds = 2;
      for (var k = 0; k < 2000 && x < xmax; k++) { var gn = dn(h), nn = n(h), c = gn * th2; tx += (-c * tx) / nn * ds; th2 += (gn - c * th2) / nn * ds; var m = Math.hypot(tx, th2); tx /= m; th2 /= m; x += tx * ds; h += th2 * ds; if (h <= 0) { pts.push([x, 0]); return pts; } if (k % 3 === 0) { pts.push([x, h]); } if (h > 400) { break; } }
      pts.push([x, h]); return pts;
    }
    function oeilM(ctx, x, y) {   /* petit œil, regardant vers la droite */
      ctx.save(); ctx.translate(x, y); ctx.beginPath(); ctx.moveTo(-11, 0); ctx.quadraticCurveTo(0, -8, 11, 0); ctx.quadraticCurveTo(0, 7, -11, 0); ctx.closePath(); ctx.fillStyle = '#FFFFFF'; ctx.fill(); ctx.save(); ctx.clip(); ctx.fillStyle = '#1D4ED8'; ctx.beginPath(); ctx.arc(3, 0, 4.5, 0, 2 * Math.PI); ctx.fill(); ctx.fillStyle = '#0F172A'; ctx.beginPath(); ctx.arc(3, 0, 2, 0, 2 * Math.PI); ctx.fill(); ctx.restore(); ctx.strokeStyle = '#7C2D12'; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(-11, 0); ctx.quadraticCurveTo(0, -8, 11, 0); ctx.stroke(); ctx.restore();
    }
    function arbre(ctx, x, Y, al) { ctx.save(); ctx.globalAlpha = al; ctx.fillStyle = '#78350F'; ctx.fillRect(x - 4, Y(42), 8, 42); var cs = [[0, 62, 22, '#166534'], [-12, 54, 15, '#15803D'], [12, 54, 15, '#15803D'], [0, 74, 14, '#22C55E']]; cs.forEach(function (c) { ctx.fillStyle = c[3]; ctx.beginPath(); ctx.arc(x + c[0], Y(c[1]), c[2], 0, 2 * Math.PI); ctx.fill(); }); ctx.restore(); }
    function bateau(ctx, x, Y, al) { ctx.save(); ctx.globalAlpha = al; ctx.fillStyle = '#1E293B'; ctx.beginPath(); ctx.moveTo(x - 26, Y(10)); ctx.lineTo(x + 26, Y(10)); ctx.lineTo(x + 18, Y(0)); ctx.lineTo(x - 18, Y(0)); ctx.fill(); ctx.fillStyle = '#B91C1C'; ctx.fillRect(x - 26, Y(10), 52, 2); ctx.fillStyle = '#475569'; ctx.fillRect(x - 1.5, Y(44), 3, 34); ctx.fillStyle = '#F8FAFC'; ctx.beginPath(); ctx.moveTo(x + 2, Y(42)); ctx.lineTo(x + 20, Y(14)); ctx.lineTo(x + 2, Y(14)); ctx.fill(); ctx.beginPath(); ctx.moveTo(x - 2, Y(38)); ctx.lineTo(x - 15, Y(14)); ctx.lineTo(x - 2, Y(14)); ctx.fill(); ctx.restore(); }
    function draw(o) {
      var ctx = o.ctx, W = o.W, H = o.H, G = H - 92, xe = 46, he = 40, xo = W - 70, D = 760, SX = function (x) { return xe + x * (xo - xe) / D; }, Y = function (h) { return G - h; }, chaud = type === 'chaud';   /* les rayons sont calculés sur une distance fixe D, puis le dessin est comprimé horizontalement : même résultat sur ordinateur et sur téléphone */
      ctx.clearRect(0, 0, W, H);
      var gc = ctx.createLinearGradient(0, 0, 0, G); gc.addColorStop(0, chaud ? '#3B82F6' : '#64748B'); gc.addColorStop(1, chaud ? '#BFDBFE' : '#CBD5E1'); ctx.fillStyle = gc; ctx.fillRect(0, 0, W, G);
      if (chaud) { var gs = ctx.createRadialGradient(W * 0.8, 30, 2, W * 0.8, 30, 40); gs.addColorStop(0, '#FFFFFF'); gs.addColorStop(0.3, 'rgba(254,240,138,0.9)'); gs.addColorStop(1, 'rgba(254,240,138,0)'); ctx.fillStyle = gs; ctx.beginPath(); ctx.arc(W * 0.8, 30, 40, 0, 2 * Math.PI); ctx.fill(); }
      ctx.fillStyle = chaud ? 'rgba(146,64,14,0.25)' : 'rgba(51,65,85,0.25)'; ctx.beginPath(); ctx.moveTo(0, G); for (var x = 0; x <= W; x += 20) { ctx.lineTo(x, G - 10 - 8 * Math.sin(x / 70) - 5 * Math.sin(x / 23)); } ctx.lineTo(W, G); ctx.fill();   /* collines lointaines */
      if (chk.checked) { for (var c = 0; c < 8; c++) { var h0 = c * 6, a = 0.3 * Math.exp(-h0 / (chaud ? 14 : 40)); ctx.fillStyle = chaud ? 'rgba(249,115,22,' + a + ')' : 'rgba(30,64,175,' + a + ')'; ctx.fillRect(0, Y(h0 + 6), W, 6); }
        ctx.strokeStyle = chaud ? 'rgba(255,255,255,0.35)' : 'rgba(255,255,255,0.2)'; ctx.lineWidth = 1; for (var w = 0; w < 4; w++) { ctx.beginPath(); for (x = 0; x <= W; x += 8) { ctx.lineTo(x, Y(3 + w * 5) + Math.sin(x / 14 + w + t * 3) * 1.5); } ctx.stroke(); } }   /* air qui ondule */
      if (chaud) { var gr = ctx.createLinearGradient(0, G, 0, H); gr.addColorStop(0, '#6B7280'); gr.addColorStop(1, '#374151'); ctx.fillStyle = gr; ctx.fillRect(0, G, W, H - G); ctx.fillStyle = '#FDE68A'; for (var b = 0; b < W; b += 52) { ctx.fillRect(b, G + 40, 26, 3); } }
      else { var gm = ctx.createLinearGradient(0, G, 0, H); gm.addColorStop(0, '#0E7490'); gm.addColorStop(1, '#164E63'); ctx.fillStyle = gm; ctx.fillRect(0, G, W, H - G); ctx.strokeStyle = 'rgba(255,255,255,0.25)'; for (var v = 0; v < 6; v++) { ctx.beginPath(); for (x = 0; x <= W; x += 10) { ctx.lineTo(x, G + 10 + v * 13 + Math.sin(x / 18 + v) * 1.5); } ctx.stroke(); } }
      var hObj = chaud ? 82 : 44, obj = chaud ? arbre : bateau;
      obj(ctx, xo, Y, 1);
      var R = [];   /* rayons tracés depuis l'œil (principe du retour inverse) : direction de départ, trajet, hauteur atteinte au niveau de l'objet */
      for (var th = -0.2; th <= 0.2; th += 0.0015) { var pts = rayon(0, he, th, D), f = pts[pts.length - 1]; if (f[0] >= D - 1 && f[1] > 0 && f[1] <= hObj) { R.push([th, pts, f[1]]); } }
      var br = [], cur = []; R.forEach(function (r) { if (cur.length > 1) { var s0 = Math.sign(cur[cur.length - 1][2] - cur[cur.length - 2][2]), s1 = Math.sign(r[2] - cur[cur.length - 1][2]); if (s0 && s1 && s0 !== s1) { br.push(cur); cur = [cur[cur.length - 1]]; } } cur.push(r); }); if (cur.length) { br.push(cur); }   /* branches : on coupe là où la hauteur atteinte change de sens */
      var directe = chaud ? br.reduce(function (m, b) { return !m || b[b.length - 1][0] > m[m.length - 1][0] ? b : m; }, null) : null;   /* vue directe : la branche qui part le plus haut */
      var RAY = '#EA580C';   /* une seule couleur pour les rayons de lumière ; les prolongements imaginés par l'œil sont dans la même couleur, en pointillés */
      var DIRECT = '#6D28D9';   /* rayons directs, de l'arbre à l'œil sans passer près du sol */
      function trace(r, col) {   /* rayon réel, de l'objet vers l'œil, avec un halo discret et une flèche */
        col = col || RAY; ctx.save(); ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.globalAlpha = 0.1; ctx.strokeStyle = col; ctx.lineWidth = 3; ctx.beginPath(); r[1].forEach(function (q, i) { if (i) { ctx.lineTo(SX(q[0]), Y(q[1])); } else { ctx.moveTo(SX(q[0]), Y(q[1])); } }); ctx.stroke(); ctx.globalAlpha = 1; ctx.lineWidth = 1.4; ctx.stroke(); ctx.restore();
        var k = Math.floor(r[1].length * 0.5), a = r[1][k + 1] || r[1][k], b = r[1][k]; vec(ctx, SX(a[0]), Y(a[1]), SX(b[0]), Y(b[1]), col, 1.4, 9);   /* la lumière va de l'objet vers l'œil */
      }
      function hApp(r) { return he + Math.tan(r[0]) * D; }   /* hauteur où l'œil croit voir le point : dans le prolongement du rayon reçu */
      function viser(b, h) {   /* direction de départ, dans une branche, du rayon qui atteint la hauteur h de l'objet */
        for (var i = 1; i < b.length; i++) { var a = b[i - 1], c = b[i]; if ((a[2] - h) * (c[2] - h) <= 0 && a[2] !== c[2]) { var th = a[0] + (c[0] - a[0]) * (h - a[2]) / (c[2] - a[2]), pts = rayon(0, he, th, D); return [th, pts, h]; } }
        return null;
      }
      var mir = br.filter(function (b) { return b !== directe && b.length >= 3; }), hs = [];
      mir.forEach(function (b) {   /* deux points de l'objet, vus à la fois directement et par le mirage */
        var lo = Math.min.apply(null, b.map(function (r) { return r[2]; })), hi = Math.max.apply(null, b.map(function (r) { return r[2]; }));
        if (directe) { lo = Math.max(lo, Math.min.apply(null, directe.map(function (r) { return r[2]; }))); hi = Math.min(hi, Math.max.apply(null, directe.map(function (r) { return r[2]; }))); }
        hs = [lo + 0.2 * (hi - lo), lo + 0.85 * (hi - lo)];
      });
      if (directe) { hs.forEach(function (h) { var r = viser(directe, h); if (r) { trace(r, DIRECT); } }); }   /* rayons directs, au second plan */
      mir.forEach(function (b) {
        var ext = [b[0], b[b.length - 1]];
        var r1 = ext[0], r2 = ext[1], B = (hApp(r2) - hApp(r1)) / (r2[2] - r1[2]), A = hApp(r1) - B * r1[2];   /* correspondance linéaire hauteur réelle -> hauteur apparente */
        var y1 = Y(Math.max(hApp(r1), hApp(r2))), y2 = Y(Math.min(hApp(r1), hApp(r2))), mg = 14, ow = 120, oh = Math.ceil(y2 - y1 + 2 * mg);
        var oc = document.createElement('canvas'), dpr = window.devicePixelRatio || 1; oc.width = Math.round(ow * dpr); oc.height = Math.round(oh * dpr); var c2 = oc.getContext('2d'); c2.setTransform(dpr, 0, 0, dpr, 0, 0);
        if (chaud) { var gh = c2.createRadialGradient(ow / 2, oh / 2, 4, ow / 2, oh / 2, ow * 0.5); gh.addColorStop(0, 'rgba(191,219,254,0.85)'); gh.addColorStop(0.6, 'rgba(191,219,254,0.45)'); gh.addColorStop(1, 'rgba(191,219,254,0)'); c2.fillStyle = gh; c2.fillRect(0, 0, ow, oh); }   /* halo de ciel : la « flaque » */
        c2.save(); c2.beginPath(); c2.rect(0, mg - 2, ow, oh - 2 * mg + 4); c2.clip(); c2.translate(ow / 2 - xo, -(y1 - mg)); c2.translate(0, G - A - B * G); c2.scale(1, B); obj(c2, xo, function (h) { return G - h; }, 0.8); c2.restore();   /* seule la partie de l'objet atteinte par ces rayons forme une image */
        for (var row = 0; row < oh; row += 2) { var dx = (chaud ? 2.6 : 1.4) * Math.sin(row / 3.2 + t * 6) + 1.2 * Math.sin(row / 7 - t * 4); ctx.drawImage(oc, 0, row * dpr, ow * dpr, 2 * dpr, xo - ow / 2 + dx, y1 - mg + row, ow, 2); }   /* l'air chaud fait onduler l'image */
        hs.forEach(function (h) { var r = viser(b, h); if (!r) { return; }
          ctx.save(); ctx.setLineDash([7, 5]); ctx.strokeStyle = '#FDBA74'; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(xe, Y(he)); ctx.lineTo(xo, Y(hApp(r))); ctx.stroke(); ctx.restore();   /* prolongement en ligne droite : là où l'œil croit voir ce point */
          trace(r); });   /* les deux rayons courbés, au premier plan, partant des mêmes points que les rayons directs */
      });
      oeilM(ctx, xe, Y(he));
    }
    var TXT = { chaud: 'Au ras de la route surchauffée, l\u2019air est très chaud, et son indice est un peu plus faible que celui de l\u2019air au-dessus. Les rayons qui descendent vers la route traversent des couches d\u2019indice de plus en plus faible&nbsp;: ils s\u2019éloignent chaque fois un peu plus de la normale, se courbent (en orange) et remontent vers l\u2019œil. L\u2019œil reçoit donc, venant d\u2019en bas, de la lumière partie de l\u2019arbre… et du ciel. Comme il suppose que la lumière se propage en ligne droite, il situe ce qu\u2019il voit dans le prolongement des rayons reçus (en pointillés)&nbsp;: une image <b>renversée</b> de l\u2019arbre, entourée de ciel, <b>sous</b> l\u2019horizon, sur la route. Le cerveau l\u2019interprète comme le reflet de l\u2019arbre dans une flaque d\u2019eau. Les rayons qui vont directement de l\u2019arbre à l\u2019œil sans s\u2019approcher du sol (en violet), presque en ligne droite, donnent, eux, l\u2019image normale de l\u2019arbre. (Dans l\u2019animation, la courbure des rayons est très exagérée.)', froid: 'Au-dessus d\u2019une mer froide, c\u2019est l\u2019inverse&nbsp;: l\u2019air le plus froid, d\u2019indice le plus grand, est près de l\u2019eau, et l\u2019indice diminue vers le haut. Les rayons qui montent se courbent vers le bas (en orange). L\u2019œil, qui prolonge en ligne droite les rayons reçus (en pointillés), voit le bateau <b>plus haut</b> qu\u2019il n\u2019est réellement, et peut même l\u2019apercevoir quand il est caché derrière l\u2019horizon. Avec certaines superpositions de couches d\u2019air, l\u2019image est en plus renversée, ou étirée en hautes falaises&nbsp;: c\u2019est la <i>fata morgana</i>.' };
    var loop = Loop(root, function (dt) { t += dt; draw(cnv); return true; });
    cnv = Canvas($(root, 'canvas'), function (W) { return W < 560 ? 300 : 340; }, draw);
    if (!RM) { loop.kick(); }
    $$(root, 'input[name="mi-t"]').forEach(function (r) { r.addEventListener('change', function () { type = r.value; msg.innerHTML = TXT[type]; draw(cnv); }); });
    chk.addEventListener('change', function () { draw(cnv); });
    msg.innerHTML = TXT.chaud; draw(cnv);
  })();

  /* =================== 13. Quiz final =================== */
  (function () {
    var root = document.getElementById('quiz-final'); if (!root) { return; }
    Quiz(root, [
      ['Dans un milieu transparent et homogène, la lumière se propage…', ['en ligne droite', 'en zigzag', 'en arc de cercle'], 'C\u2019est la propagation rectiligne de la lumière.'],
      ['La vitesse de la lumière dans le vide vaut…', ['$\\pu{3,00E8 m*s-1}$', '$\\pu{3,40E2 m*s-1}$', '$\\pu{3,00E5 m*s-1}$'], '$c = \\pu{3,00E8 m*s-1}$, soit 300&nbsp;000&nbsp;km par seconde (et non par heure&nbsp;!).'],
      ['La lumière d\u2019un laser est…', ['monochromatique', 'polychromatique', 'blanche'], 'Elle ne contient qu\u2019une seule radiation&nbsp;: un prisme la dévie sans la décomposer.'],
      ['Une radiation de longueur d\u2019onde 450&nbsp;nm est perçue…', ['bleue', 'rouge', 'invisible'], 'Le visible s\u2019étend de 400&nbsp;nm (violet) à 800&nbsp;nm (rouge)&nbsp;; 450&nbsp;nm est dans le bleu.'],
      ['Quand la température d\u2019un corps chaud augmente, son spectre…', ['s\u2019enrichit vers le violet', 's\u2019enrichit vers le rouge', 'devient un spectre de raies'], 'Un corps plus chaud émet davantage de radiations de courtes longueurs d\u2019onde.'],
      ['Un gaz de sodium froid, éclairé en lumière blanche, donne…', ['des raies noires à 589 nm', 'une raie jaune à 589 nm sur fond noir', 'un spectre continu complet'], 'Un gaz froid absorbe les radiations qu\u2019il peut émettre&nbsp;: c\u2019est un spectre de raies d\u2019absorption.'],
      ['Les angles d\u2019incidence et de réfraction sont mesurés entre le rayon et…', ['la normale', 'la surface de séparation', 'le rayon réfléchi'], 'Tous les angles sont repérés par rapport à la normale.'],
      ['La lumière passe de l\u2019air dans l\u2019eau. Le rayon réfracté…', ['se rapproche de la normale', 's\u2019éloigne de la normale', 'n\u2019est pas dévié'], 'L\u2019eau a un indice plus grand que l\u2019air&nbsp;: $i_2 < i_1$.'],
      ['Dans un milieu d\u2019indice $n = 2{,}0$, la lumière se propage à…', ['$\\pu{1,5E8 m*s-1}$', '$\\pu{6,0E8 m*s-1}$', '$\\pu{3,0E8 m*s-1}$'], '$v = \\dfrac{c}{n} = \\dfrac{\\pu{3,0E8 m*s-1}}{2,0} = \\pu{1,5E8 m*s-1}$.'],
      ['Le prisme disperse la lumière blanche parce que…', ['l\u2019indice du verre dépend de la longueur d\u2019onde', 'le verre colore la lumière', 'le prisme réfléchit chaque couleur'], 'Chaque radiation est réfractée d\u2019un angle différent&nbsp;: le violet est le plus dévié.']
    ], 10);
  })();

})();
</script>
