+++
title = "Cours"
date = 2021-03-06T14:20:50+01:00
weight = 1
chapter = false
hidden = true
+++

<style>
/* ============================================================
   PAGE DE COURS (préfixe nt-) — même système que la page Entraînement
   ------------------------------------------------------------
   --nt-accent / --nt-soft : teinte des cadres (bandeau et fond
   des notices « note » de hugo-theme-learn par défaut).
   ============================================================ */
:root {
  --nt-accent: #6AB0DE;
  --nt-soft:   #E7F2FA;
  /* couleurs « sémantiques » */
  --nt-warn: #D9534F;  --nt-warn-ink: #A9302A;
  --nt-up:   #E8590C;
  --nt-ok:   #15803D;
  /* identité des diaporamas : le saumon #FF968D, foncé pour le texte sur fond clair */
  --imp-line: #FF968D;
  --imp:      #C7392D;
  /* hauteur / intensité / timbre (versions lisibles sur fond clair des couleurs des diapos) */
  --c-haut:   #2B8A3E;
  --c-int:    #C27C0E;
  --c-timbre: #1971C2;
}
.nt-box, .nt-card, ol.nt-steps, .nt-feat, details.nt-more, .nt-svg, .nt-lab, .nt-quizbar, .nt-essentiel, .nt-cs {
  --nt-fill:   color-mix(in srgb, var(--nt-accent) 20%, var(--nt-soft));
  --nt-fill-2: color-mix(in srgb, var(--nt-accent) 35%, var(--nt-soft));
  --nt-line:   var(--nt-accent);
  --nt-ink:    color-mix(in srgb, var(--nt-accent) 55%, #000);
}

/* --- Texte --- */
.imp { font-weight: 700; color: var(--imp); }
.nt-lead { font-size: 1.08em; line-height: 1.65; }
.nt-note, .nt-caption { font-size: 0.9em; opacity: 0.85; }
.nt-center { text-align: center; }
.nt-scroll { overflow-x: auto; margin: 0.6em 0 1em; -webkit-overflow-scrolling: touch; }

/* --- Encadrés --- */
.nt-box {
  border-left: 5px solid var(--bx-line); background: var(--bx-bg);
  border-radius: 0 8px 8px 0; padding: 0.6em 1.1em; margin: 1.1em 0;
}
.nt-box p { margin: 0.4em 0 !important; }
.nt-box-title { font-weight: 700; color: var(--bx-ink); }
.nt-box-title i { margin-right: 0.45em; }
.nt-method { --bx-line: var(--nt-line); --bx-bg: var(--nt-fill);   --bx-ink: var(--nt-ink); }
.nt-know   { --bx-line: var(--nt-ink);  --bx-bg: var(--nt-fill-2); --bx-ink: var(--nt-ink);
             border-top: 1px solid var(--nt-line); border-right: 1px solid var(--nt-line); border-bottom: 1px solid var(--nt-line); }
.nt-trap   { --bx-line: var(--nt-warn); --bx-bg: color-mix(in srgb, var(--nt-warn) 10%, #fff); --bx-ink: var(--nt-warn-ink); }
.nt-ask    { --bx-line: var(--nt-up);   --bx-bg: color-mix(in srgb, var(--nt-up) 9%, #fff);    --bx-ink: #B5470A; }
ul.nt-facts { list-style: none !important; padding-left: 0 !important; margin: 0.3em 0 !important; }
ul.nt-facts li { position: relative; padding: 0.25em 0 0.25em 1.2em; }
ul.nt-facts li::before { content: "▸"; color: var(--bx-ink, var(--nt-ink)); position: absolute; left: 0; }

/* --- Formules encadrées (signature des diaporamas) --- */
.nt-formula {
  width: fit-content; max-width: 100%; overflow-x: auto; margin: 1em auto; padding: 0.2em 2.2em;
  border: 4px solid var(--imp-line); border-radius: 10px;
  background: color-mix(in srgb, var(--imp-line) 8%, #fff); font-size: 1.15em;
}
.nt-formula p { margin: 0.3em 0 !important; }

/* --- Cartes et grilles --- */
.nt-grid  { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin: 1em 0; align-items: start; }
.nt-grid3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin: 1em 0; }
.nt-card {
  border: 1px solid var(--nt-line); border-top: 4px solid var(--nt-ink);
  background: var(--nt-fill); border-radius: 8px; padding: 0.5em 1em; overflow-x: auto;
}
.nt-card p { margin: 0.4em 0 !important; }
.nt-card-title { font-weight: 700; color: var(--nt-ink); }
.nt-card-title i { margin-right: 0.45em; }

/* --- Hauteur / intensité / timbre --- */
.nt-feat {
  border: 1px solid color-mix(in srgb, var(--f) 45%, #fff); border-top: 5px solid var(--f);
  border-radius: 8px; padding: 0.6em 0.9em; background: color-mix(in srgb, var(--f) 7%, #fff);
}
.nt-feat p { margin: 0.3em 0 !important; }
.nt-feat-title { font-weight: 800; font-size: 1.1em; color: var(--f); }
.nt-feat-key { font-weight: 700; color: var(--f); }
.nt-wave { display: block; width: 100%; height: auto; margin: 0.3em 0; }

/* --- Unités --- */
ul.nt-units-list { list-style: none !important; padding: 0 !important; margin: 0.6em auto !important; width: fit-content; }
ul.nt-units-list li { margin: 0.3em 0; }
ul.nt-units-list li::before { content: "▸"; color: var(--imp-line); margin-right: 0.5em; }

/* --- Figures, vidéos, intégrations --- */
.nt-fig { margin: 1.2em auto; text-align: center; }
.nt-fig img, .nt-fig video {
  display: block; max-width: 100%; height: auto; margin: 0 auto;
  border-radius: 10px; box-shadow: 0 2px 14px rgba(0, 0, 0, 0.15);
}
.nt-fig-dark img { background: #191919; }
.nt-fig figcaption { font-size: 0.88em; opacity: 0.8; margin-top: 0.6em; line-height: 1.45; max-width: 46em; margin-left: auto; margin-right: auto; }
.nt-svg { display: block; width: 100%; height: auto; max-width: 760px; margin: 0.8em auto; color: inherit; }
.nt-embed { position: relative; width: 100%; max-width: 820px; margin: 1.2em auto; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 14px rgba(0, 0, 0, 0.15); }
.nt-embed iframe { display: block; width: 100%; height: 100%; border: 0; }
.nt-embed-ggb { aspect-ratio: 4 / 3; }
.nt-embed-edu { aspect-ratio: 5 / 4; max-width: 700px; }

/* --- Tableaux --- */
.nt-cs { width: 100%; min-width: 420px; margin: 0 !important; border-collapse: collapse !important; }
.nt-cs th {
  background: var(--nt-fill) !important; border: 0 !important; color: var(--nt-ink);
  border-bottom: 2px solid var(--nt-line) !important; font-size: 0.88em; padding: 6px 8px !important;
}
.nt-cs td {
  background: none !important; border: 0 !important; text-align: center;
  border-bottom: 1px solid rgba(128, 128, 128, 0.2) !important; padding: 7px 8px !important;
}
.nt-pill { display: inline-block; padding: 0.05em 0.7em; border-radius: 999px; font-weight: 700; background: color-mix(in srgb, var(--imp-line) 18%, #fff); border: 1.5px solid var(--imp-line); }
.nt-pill-down { background: color-mix(in srgb, var(--nt-warn) 10%, #fff); border-color: var(--nt-warn); }

/* --- Escamotables --- */
details.nt-more { margin: 1.2em 0; border: 1.5px solid var(--nt-line); border-radius: 8px; background: var(--nt-fill); }
details.nt-more > summary { cursor: pointer; padding: 0.55em 1em; font-weight: 700; color: var(--nt-ink); list-style: none; border-radius: 8px; }
details.nt-more > summary::-webkit-details-marker { display: none; }
details.nt-more > summary::before { content: "▸"; display: inline-block; margin-right: 0.6em; transition: transform 0.2s; }
details.nt-more[open] > summary::before { transform: rotate(90deg); }
details.nt-more[open] > summary { border-bottom: 1px solid var(--nt-line); border-radius: 8px 8px 0 0; }
details.nt-more > summary:focus-visible { outline: 3px solid var(--nt-ink); outline-offset: 2px; }
.nt-more-body { padding: 0.4em 1.1em 0.8em; overflow-x: auto; }
.nt-more-body p { margin: 0.5em 0 !important; }
@media (prefers-reduced-motion: reduce) { details.nt-more > summary::before { transition: none; } }

/* --- Mode révision : mots-clés masqués --- */
.nt-quizbar {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.6em 1em; margin: 1em 0 1.6em;
  padding: 0.6em 1em; border-radius: 10px; background: var(--nt-fill); border: 1px dashed var(--nt-line);
}
.nt-quizbar p { margin: 0 !important; flex: 1 1 18em; font-size: 0.92em; }
.nt-quiz-toggle {
  border: 0; border-radius: 999px; padding: 0.45em 1.2em; cursor: pointer; font-weight: 700;
  color: #fff; background: var(--nt-ink); transition: transform 0.15s;
}
.nt-quiz-toggle[aria-pressed="true"] { background: var(--imp); }
.nt-quiz-toggle:active { transform: translateY(1px); }
.nt-quiz-toggle:focus-visible { outline: 3px solid var(--nt-line); outline-offset: 2px; }
body.nt-quiz .nt-hole:not(.nt-shown) {
  filter: blur(7px); opacity: 0.55; cursor: pointer; user-select: none;
  background: color-mix(in srgb, var(--imp-line) 30%, transparent); border-radius: 4px;
}
body.nt-quiz .nt-hole { transition: filter 0.25s, opacity 0.25s; }
body.nt-quiz .nt-hole:focus-visible { outline: 2px solid var(--imp); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { body.nt-quiz .nt-hole { transition: none; } }

/* --- Étapes --- */
ol.nt-steps { counter-reset: ntstep; list-style: none !important; padding-left: 0 !important; margin: 0.8em 0 1em 1em !important; }
ol.nt-steps > li { counter-increment: ntstep; position: relative; padding: 0 0 0.9em 1.8em; border-left: 2px dashed var(--nt-line); }
ol.nt-steps > li:last-child { border-left-color: transparent; padding-bottom: 0; }
ol.nt-steps > li::before {
  content: counter(ntstep); position: absolute; left: -1em; top: 0;
  width: 2em; height: 2em; line-height: 2em; border-radius: 50%;
  background: var(--nt-ink); color: #fff; font-weight: 700; text-align: center;
}
ol.nt-steps p { margin: 0.3em 0 !important; }

/* --- Convertisseur interactif --- */
.nt-lab { border: 2px solid var(--nt-line); border-radius: 12px; padding: 0.8em 1.2em 1em; margin: 1.4em 0; background: var(--nt-fill); }
.nt-lab p { margin: 0.4em 0 !important; }
.nt-lab-title { font-weight: 700; color: var(--nt-ink); }
.nt-lab-title i { margin-right: 0.45em; }
.nt-lab input[type="range"] { width: 100%; accent-color: var(--imp); margin: 0.6em 0 0.2em; }
.nt-lab-out { display: flex; flex-wrap: wrap; gap: 0.6em 2em; justify-content: center; font-size: 1.15em; margin: 0.5em 0; }
.nt-lab-out b { color: var(--imp); }
.nt-lab-bar { position: relative; height: 12px; border-radius: 6px; background: linear-gradient(to right, #40c057, #fab005 50%, #fd7e14 75%, #e03131); margin: 0.6em 0 0.3em; }
.nt-lab-cursor { position: absolute; top: -5px; width: 4px; height: 22px; margin-left: -2px; border-radius: 2px; background: currentColor; transition: left 0.3s; }
.nt-lab-btns { display: flex; flex-wrap: wrap; gap: 0.5em; justify-content: center; margin-top: 0.7em; }
.nt-lab-btns button {
  border: 1.5px solid var(--nt-ink); background: #fff; color: var(--nt-ink); border-radius: 999px;
  padding: 0.3em 0.9em; cursor: pointer; font-weight: 600; font-size: 0.92em;
}
.nt-lab-btns button:hover { background: var(--nt-fill-2); }
.nt-lab-btns button:focus-visible { outline: 3px solid var(--nt-line); outline-offset: 2px; }
.nt-lab-msg { text-align: center; font-size: 0.92em; min-height: 1.4em; }

/* --- L'essentiel --- */
.nt-essentiel { border: 3px solid var(--imp-line); border-radius: 12px; padding: 0.8em 1.3em; margin: 2em 0 1em; background: color-mix(in srgb, var(--imp-line) 6%, #fff); }
.nt-essentiel-title { font-weight: 800; font-size: 1.15em; color: var(--imp); margin: 0.2em 0 0.6em !important; }
.nt-essentiel-title i { margin-right: 0.45em; }
.nt-essentiel .nt-grid { margin: 0.4em 0; }
.nt-essentiel .nt-grid > div { background: #fff; border-radius: 8px; padding: 0.4em 0.8em; border: 1px solid color-mix(in srgb, var(--imp-line) 50%, #fff); }
.nt-essentiel .nt-grid p { margin: 0.3em 0 !important; }
</style>

# Intensité sonore

<div class="nt-quizbar">
<button type="button" class="nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés <span class="imp">surlignés</span>&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Rappels

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-water"></i>Une onde</p>
<p>Une onde est caractérisée par <span class="imp nt-hole">un transport d'énergie et d'information sans transport de matière</span>.</p>
</div>

<div class="nt-grid">
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-cubes"></i>Une onde mécanique</p>
<p>L'onde sonore est une onde <span class="imp nt-hole">mécanique</span> car elle nécessite un <span class="imp nt-hole">milieu matériel</span> pour se propager.</p>
<p class="nt-note">Conséquence&nbsp;: le son ne se propage pas dans le vide.</p>
</div>
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-arrows-left-right"></i>Une onde longitudinale</p>
<p>L'onde sonore est une onde <span class="imp nt-hole">longitudinale</span> car la perturbation se fait <span class="imp nt-hole">dans la même direction</span> que sa propagation.</p>
</div>
</div>

<figure class="nt-fig nt-fig-dark">
<img src="/animsonrond.gif" alt="Animation de la propagation d'une onde sonore" loading="lazy">
<figcaption>Propagation d'une onde sonore&nbsp;: le milieu subit une succession de compressions et de dilatations dans la direction de propagation.</figcaption>
</figure>

<p class="nt-lead">Un son musical est un signal <span class="imp nt-hole">périodique</span> caractérisé par&nbsp;:</p>

<div class="nt-grid3">
<div class="nt-feat" style="--f: var(--c-haut);">
<p class="nt-feat-title"><i class="fa-solid fa-music"></i>&nbsp; sa hauteur</p>
<p>liée à <span class="nt-feat-key nt-hole">la fréquence</span> du signal</p>
<svg class="nt-wave" viewBox="0 0 200 70" role="img" aria-label="Deux signaux de même amplitude ; le signal coloré a une fréquence double"><line x1="0" y1="35" x2="200" y2="35" stroke="currentColor" stroke-opacity=".2"/><polyline points="0.0,35.0 1.0,34.1 2.0,33.2 3.0,32.4 4.0,31.5 5.0,30.7 6.0,29.8 7.0,29.0 8.0,28.3 9.0,27.5 10.0,26.8 11.0,26.1 12.0,25.4 13.0,24.8 14.0,24.2 15.0,23.7 16.0,23.2 17.0,22.7 18.0,22.3 19.0,22.0 20.0,21.7 21.0,21.4 22.0,21.2 23.0,21.1 24.0,21.0 25.0,21.0 26.0,21.0 27.0,21.1 28.0,21.2 29.0,21.4 30.0,21.7 31.0,22.0 32.0,22.3 33.0,22.7 34.0,23.2 35.0,23.7 36.0,24.2 37.0,24.8 38.0,25.4 39.0,26.1 40.0,26.8 41.0,27.5 42.0,28.3 43.0,29.0 44.0,29.8 45.0,30.7 46.0,31.5 47.0,32.4 48.0,33.2 49.0,34.1 50.0,35.0 51.0,35.9 52.0,36.8 53.0,37.6 54.0,38.5 55.0,39.3 56.0,40.2 57.0,41.0 58.0,41.7 59.0,42.5 60.0,43.2 61.0,43.9 62.0,44.6 63.0,45.2 64.0,45.8 65.0,46.3 66.0,46.8 67.0,47.3 68.0,47.7 69.0,48.0 70.0,48.3 71.0,48.6 72.0,48.8 73.0,48.9 74.0,49.0 75.0,49.0 76.0,49.0 77.0,48.9 78.0,48.8 79.0,48.6 80.0,48.3 81.0,48.0 82.0,47.7 83.0,47.3 84.0,46.8 85.0,46.3 86.0,45.8 87.0,45.2 88.0,44.6 89.0,43.9 90.0,43.2 91.0,42.5 92.0,41.7 93.0,41.0 94.0,40.2 95.0,39.3 96.0,38.5 97.0,37.6 98.0,36.8 99.0,35.9 100.0,35.0 101.0,34.1 102.0,33.2 103.0,32.4 104.0,31.5 105.0,30.7 106.0,29.8 107.0,29.0 108.0,28.3 109.0,27.5 110.0,26.8 111.0,26.1 112.0,25.4 113.0,24.8 114.0,24.2 115.0,23.7 116.0,23.2 117.0,22.7 118.0,22.3 119.0,22.0 120.0,21.7 121.0,21.4 122.0,21.2 123.0,21.1 124.0,21.0 125.0,21.0 126.0,21.0 127.0,21.1 128.0,21.2 129.0,21.4 130.0,21.7 131.0,22.0 132.0,22.3 133.0,22.7 134.0,23.2 135.0,23.7 136.0,24.2 137.0,24.8 138.0,25.4 139.0,26.1 140.0,26.8 141.0,27.5 142.0,28.3 143.0,29.0 144.0,29.8 145.0,30.7 146.0,31.5 147.0,32.4 148.0,33.2 149.0,34.1 150.0,35.0 151.0,35.9 152.0,36.8 153.0,37.6 154.0,38.5 155.0,39.3 156.0,40.2 157.0,41.0 158.0,41.7 159.0,42.5 160.0,43.2 161.0,43.9 162.0,44.6 163.0,45.2 164.0,45.8 165.0,46.3 166.0,46.8 167.0,47.3 168.0,47.7 169.0,48.0 170.0,48.3 171.0,48.6 172.0,48.8 173.0,48.9 174.0,49.0 175.0,49.0 176.0,49.0 177.0,48.9 178.0,48.8 179.0,48.6 180.0,48.3 181.0,48.0 182.0,47.7 183.0,47.3 184.0,46.8 185.0,46.3 186.0,45.8 187.0,45.2 188.0,44.6 189.0,43.9 190.0,43.2 191.0,42.5 192.0,41.7 193.0,41.0 194.0,40.2 195.0,39.3 196.0,38.5 197.0,37.6 198.0,36.8 199.0,35.9 200.0,35.0" fill="none" stroke="#9a9a9a" stroke-width="1.5" stroke-dasharray="4 3"/><polyline points="0.0,35.0 1.0,33.2 2.0,31.5 3.0,29.8 4.0,28.3 5.0,26.8 6.0,25.4 7.0,24.2 8.0,23.2 9.0,22.3 10.0,21.7 11.0,21.2 12.0,21.0 13.0,21.0 14.0,21.2 15.0,21.7 16.0,22.3 17.0,23.2 18.0,24.2 19.0,25.4 20.0,26.8 21.0,28.3 22.0,29.8 23.0,31.5 24.0,33.2 25.0,35.0 26.0,36.8 27.0,38.5 28.0,40.2 29.0,41.7 30.0,43.2 31.0,44.6 32.0,45.8 33.0,46.8 34.0,47.7 35.0,48.3 36.0,48.8 37.0,49.0 38.0,49.0 39.0,48.8 40.0,48.3 41.0,47.7 42.0,46.8 43.0,45.8 44.0,44.6 45.0,43.2 46.0,41.7 47.0,40.2 48.0,38.5 49.0,36.8 50.0,35.0 51.0,33.2 52.0,31.5 53.0,29.8 54.0,28.3 55.0,26.8 56.0,25.4 57.0,24.2 58.0,23.2 59.0,22.3 60.0,21.7 61.0,21.2 62.0,21.0 63.0,21.0 64.0,21.2 65.0,21.7 66.0,22.3 67.0,23.2 68.0,24.2 69.0,25.4 70.0,26.8 71.0,28.3 72.0,29.8 73.0,31.5 74.0,33.2 75.0,35.0 76.0,36.8 77.0,38.5 78.0,40.2 79.0,41.7 80.0,43.2 81.0,44.6 82.0,45.8 83.0,46.8 84.0,47.7 85.0,48.3 86.0,48.8 87.0,49.0 88.0,49.0 89.0,48.8 90.0,48.3 91.0,47.7 92.0,46.8 93.0,45.8 94.0,44.6 95.0,43.2 96.0,41.7 97.0,40.2 98.0,38.5 99.0,36.8 100.0,35.0 101.0,33.2 102.0,31.5 103.0,29.8 104.0,28.3 105.0,26.8 106.0,25.4 107.0,24.2 108.0,23.2 109.0,22.3 110.0,21.7 111.0,21.2 112.0,21.0 113.0,21.0 114.0,21.2 115.0,21.7 116.0,22.3 117.0,23.2 118.0,24.2 119.0,25.4 120.0,26.8 121.0,28.3 122.0,29.8 123.0,31.5 124.0,33.2 125.0,35.0 126.0,36.8 127.0,38.5 128.0,40.2 129.0,41.7 130.0,43.2 131.0,44.6 132.0,45.8 133.0,46.8 134.0,47.7 135.0,48.3 136.0,48.8 137.0,49.0 138.0,49.0 139.0,48.8 140.0,48.3 141.0,47.7 142.0,46.8 143.0,45.8 144.0,44.6 145.0,43.2 146.0,41.7 147.0,40.2 148.0,38.5 149.0,36.8 150.0,35.0 151.0,33.2 152.0,31.5 153.0,29.8 154.0,28.3 155.0,26.8 156.0,25.4 157.0,24.2 158.0,23.2 159.0,22.3 160.0,21.7 161.0,21.2 162.0,21.0 163.0,21.0 164.0,21.2 165.0,21.7 166.0,22.3 167.0,23.2 168.0,24.2 169.0,25.4 170.0,26.8 171.0,28.3 172.0,29.8 173.0,31.5 174.0,33.2 175.0,35.0 176.0,36.8 177.0,38.5 178.0,40.2 179.0,41.7 180.0,43.2 181.0,44.6 182.0,45.8 183.0,46.8 184.0,47.7 185.0,48.3 186.0,48.8 187.0,49.0 188.0,49.0 189.0,48.8 190.0,48.3 191.0,47.7 192.0,46.8 193.0,45.8 194.0,44.6 195.0,43.2 196.0,41.7 197.0,40.2 198.0,38.5 199.0,36.8 200.0,35.0" fill="none" stroke="var(--c-haut)" stroke-width="2.5"/></svg>
<p class="nt-note">Fréquence doublée&nbsp;: le son est plus aigu.</p>
</div>
<div class="nt-feat" style="--f: var(--c-int);">
<p class="nt-feat-title"><i class="fa-solid fa-volume-high"></i>&nbsp; son intensité</p>
<p>liée à <span class="nt-feat-key nt-hole">l'amplitude</span> du signal</p>
<svg class="nt-wave" viewBox="0 0 200 70" role="img" aria-label="Deux signaux de même fréquence ; le signal coloré a une amplitude plus grande"><line x1="0" y1="35" x2="200" y2="35" stroke="currentColor" stroke-opacity=".2"/><polyline points="0.0,35.0 1.0,34.3 2.0,33.6 3.0,32.9 4.0,32.3 5.0,31.6 6.0,31.0 7.0,30.3 8.0,29.7 9.0,29.1 10.0,28.5 11.0,28.0 12.0,27.5 13.0,27.0 14.0,26.5 15.0,26.1 16.0,25.7 17.0,25.4 18.0,25.0 19.0,24.8 20.0,24.5 21.0,24.3 22.0,24.2 23.0,24.1 24.0,24.0 25.0,24.0 26.0,24.0 27.0,24.1 28.0,24.2 29.0,24.3 30.0,24.5 31.0,24.8 32.0,25.0 33.0,25.4 34.0,25.7 35.0,26.1 36.0,26.5 37.0,27.0 38.0,27.5 39.0,28.0 40.0,28.5 41.0,29.1 42.0,29.7 43.0,30.3 44.0,31.0 45.0,31.6 46.0,32.3 47.0,32.9 48.0,33.6 49.0,34.3 50.0,35.0 51.0,35.7 52.0,36.4 53.0,37.1 54.0,37.7 55.0,38.4 56.0,39.0 57.0,39.7 58.0,40.3 59.0,40.9 60.0,41.5 61.0,42.0 62.0,42.5 63.0,43.0 64.0,43.5 65.0,43.9 66.0,44.3 67.0,44.6 68.0,45.0 69.0,45.2 70.0,45.5 71.0,45.7 72.0,45.8 73.0,45.9 74.0,46.0 75.0,46.0 76.0,46.0 77.0,45.9 78.0,45.8 79.0,45.7 80.0,45.5 81.0,45.2 82.0,45.0 83.0,44.6 84.0,44.3 85.0,43.9 86.0,43.5 87.0,43.0 88.0,42.5 89.0,42.0 90.0,41.5 91.0,40.9 92.0,40.3 93.0,39.7 94.0,39.0 95.0,38.4 96.0,37.7 97.0,37.1 98.0,36.4 99.0,35.7 100.0,35.0 101.0,34.3 102.0,33.6 103.0,32.9 104.0,32.3 105.0,31.6 106.0,31.0 107.0,30.3 108.0,29.7 109.0,29.1 110.0,28.5 111.0,28.0 112.0,27.5 113.0,27.0 114.0,26.5 115.0,26.1 116.0,25.7 117.0,25.4 118.0,25.0 119.0,24.8 120.0,24.5 121.0,24.3 122.0,24.2 123.0,24.1 124.0,24.0 125.0,24.0 126.0,24.0 127.0,24.1 128.0,24.2 129.0,24.3 130.0,24.5 131.0,24.8 132.0,25.0 133.0,25.4 134.0,25.7 135.0,26.1 136.0,26.5 137.0,27.0 138.0,27.5 139.0,28.0 140.0,28.5 141.0,29.1 142.0,29.7 143.0,30.3 144.0,31.0 145.0,31.6 146.0,32.3 147.0,32.9 148.0,33.6 149.0,34.3 150.0,35.0 151.0,35.7 152.0,36.4 153.0,37.1 154.0,37.7 155.0,38.4 156.0,39.0 157.0,39.7 158.0,40.3 159.0,40.9 160.0,41.5 161.0,42.0 162.0,42.5 163.0,43.0 164.0,43.5 165.0,43.9 166.0,44.3 167.0,44.6 168.0,45.0 169.0,45.2 170.0,45.5 171.0,45.7 172.0,45.8 173.0,45.9 174.0,46.0 175.0,46.0 176.0,46.0 177.0,45.9 178.0,45.8 179.0,45.7 180.0,45.5 181.0,45.2 182.0,45.0 183.0,44.6 184.0,44.3 185.0,43.9 186.0,43.5 187.0,43.0 188.0,42.5 189.0,42.0 190.0,41.5 191.0,40.9 192.0,40.3 193.0,39.7 194.0,39.0 195.0,38.4 196.0,37.7 197.0,37.1 198.0,36.4 199.0,35.7 200.0,35.0" fill="none" stroke="#9a9a9a" stroke-width="1.5" stroke-dasharray="4 3"/><polyline points="0.0,35.0 1.0,33.2 2.0,31.5 3.0,29.8 4.0,28.0 5.0,26.3 6.0,24.7 7.0,23.1 8.0,21.5 9.0,20.0 10.0,18.5 11.0,17.2 12.0,15.8 13.0,14.6 14.0,13.4 15.0,12.3 16.0,11.4 17.0,10.5 18.0,9.7 19.0,9.0 20.0,8.4 21.0,7.9 22.0,7.5 23.0,7.2 24.0,7.1 25.0,7.0 26.0,7.1 27.0,7.2 28.0,7.5 29.0,7.9 30.0,8.4 31.0,9.0 32.0,9.7 33.0,10.5 34.0,11.4 35.0,12.3 36.0,13.4 37.0,14.6 38.0,15.8 39.0,17.2 40.0,18.5 41.0,20.0 42.0,21.5 43.0,23.1 44.0,24.7 45.0,26.3 46.0,28.0 47.0,29.8 48.0,31.5 49.0,33.2 50.0,35.0 51.0,36.8 52.0,38.5 53.0,40.2 54.0,42.0 55.0,43.7 56.0,45.3 57.0,46.9 58.0,48.5 59.0,50.0 60.0,51.5 61.0,52.8 62.0,54.2 63.0,55.4 64.0,56.6 65.0,57.7 66.0,58.6 67.0,59.5 68.0,60.3 69.0,61.0 70.0,61.6 71.0,62.1 72.0,62.5 73.0,62.8 74.0,62.9 75.0,63.0 76.0,62.9 77.0,62.8 78.0,62.5 79.0,62.1 80.0,61.6 81.0,61.0 82.0,60.3 83.0,59.5 84.0,58.6 85.0,57.7 86.0,56.6 87.0,55.4 88.0,54.2 89.0,52.8 90.0,51.5 91.0,50.0 92.0,48.5 93.0,46.9 94.0,45.3 95.0,43.7 96.0,42.0 97.0,40.2 98.0,38.5 99.0,36.8 100.0,35.0 101.0,33.2 102.0,31.5 103.0,29.8 104.0,28.0 105.0,26.3 106.0,24.7 107.0,23.1 108.0,21.5 109.0,20.0 110.0,18.5 111.0,17.2 112.0,15.8 113.0,14.6 114.0,13.4 115.0,12.3 116.0,11.4 117.0,10.5 118.0,9.7 119.0,9.0 120.0,8.4 121.0,7.9 122.0,7.5 123.0,7.2 124.0,7.1 125.0,7.0 126.0,7.1 127.0,7.2 128.0,7.5 129.0,7.9 130.0,8.4 131.0,9.0 132.0,9.7 133.0,10.5 134.0,11.4 135.0,12.3 136.0,13.4 137.0,14.6 138.0,15.8 139.0,17.2 140.0,18.5 141.0,20.0 142.0,21.5 143.0,23.1 144.0,24.7 145.0,26.3 146.0,28.0 147.0,29.8 148.0,31.5 149.0,33.2 150.0,35.0 151.0,36.8 152.0,38.5 153.0,40.2 154.0,42.0 155.0,43.7 156.0,45.3 157.0,46.9 158.0,48.5 159.0,50.0 160.0,51.5 161.0,52.8 162.0,54.2 163.0,55.4 164.0,56.6 165.0,57.7 166.0,58.6 167.0,59.5 168.0,60.3 169.0,61.0 170.0,61.6 171.0,62.1 172.0,62.5 173.0,62.8 174.0,62.9 175.0,63.0 176.0,62.9 177.0,62.8 178.0,62.5 179.0,62.1 180.0,61.6 181.0,61.0 182.0,60.3 183.0,59.5 184.0,58.6 185.0,57.7 186.0,56.6 187.0,55.4 188.0,54.2 189.0,52.8 190.0,51.5 191.0,50.0 192.0,48.5 193.0,46.9 194.0,45.3 195.0,43.7 196.0,42.0 197.0,40.2 198.0,38.5 199.0,36.8 200.0,35.0" fill="none" stroke="var(--c-int)" stroke-width="2.5"/></svg>
<p class="nt-note">Amplitude plus grande&nbsp;: le son est plus fort.</p>
</div>
<div class="nt-feat" style="--f: var(--c-timbre);">
<p class="nt-feat-title"><i class="fa-solid fa-guitar"></i>&nbsp; son timbre</p>
<p>lié au <span class="nt-feat-key nt-hole">spectre</span> du signal</p>
<svg class="nt-wave" viewBox="0 0 200 70" role="img" aria-label="Deux signaux de même période ; le signal coloré a une forme plus complexe"><line x1="0" y1="35" x2="200" y2="35" stroke="currentColor" stroke-opacity=".2"/><polyline points="0.0,35.0 1.0,33.7 2.0,32.5 3.0,31.3 4.0,30.0 5.0,28.8 6.0,27.6 7.0,26.5 8.0,25.4 9.0,24.3 10.0,23.2 11.0,22.3 12.0,21.3 13.0,20.4 14.0,19.6 15.0,18.8 16.0,18.1 17.0,17.5 18.0,16.9 19.0,16.4 20.0,16.0 21.0,15.6 22.0,15.4 23.0,15.2 24.0,15.0 25.0,15.0 26.0,15.0 27.0,15.2 28.0,15.4 29.0,15.6 30.0,16.0 31.0,16.4 32.0,16.9 33.0,17.5 34.0,18.1 35.0,18.8 36.0,19.6 37.0,20.4 38.0,21.3 39.0,22.3 40.0,23.2 41.0,24.3 42.0,25.4 43.0,26.5 44.0,27.6 45.0,28.8 46.0,30.0 47.0,31.3 48.0,32.5 49.0,33.7 50.0,35.0 51.0,36.3 52.0,37.5 53.0,38.7 54.0,40.0 55.0,41.2 56.0,42.4 57.0,43.5 58.0,44.6 59.0,45.7 60.0,46.8 61.0,47.7 62.0,48.7 63.0,49.6 64.0,50.4 65.0,51.2 66.0,51.9 67.0,52.5 68.0,53.1 69.0,53.6 70.0,54.0 71.0,54.4 72.0,54.6 73.0,54.8 74.0,55.0 75.0,55.0 76.0,55.0 77.0,54.8 78.0,54.6 79.0,54.4 80.0,54.0 81.0,53.6 82.0,53.1 83.0,52.5 84.0,51.9 85.0,51.2 86.0,50.4 87.0,49.6 88.0,48.7 89.0,47.7 90.0,46.8 91.0,45.7 92.0,44.6 93.0,43.5 94.0,42.4 95.0,41.2 96.0,40.0 97.0,38.7 98.0,37.5 99.0,36.3 100.0,35.0 101.0,33.7 102.0,32.5 103.0,31.3 104.0,30.0 105.0,28.8 106.0,27.6 107.0,26.5 108.0,25.4 109.0,24.3 110.0,23.2 111.0,22.3 112.0,21.3 113.0,20.4 114.0,19.6 115.0,18.8 116.0,18.1 117.0,17.5 118.0,16.9 119.0,16.4 120.0,16.0 121.0,15.6 122.0,15.4 123.0,15.2 124.0,15.0 125.0,15.0 126.0,15.0 127.0,15.2 128.0,15.4 129.0,15.6 130.0,16.0 131.0,16.4 132.0,16.9 133.0,17.5 134.0,18.1 135.0,18.8 136.0,19.6 137.0,20.4 138.0,21.3 139.0,22.3 140.0,23.2 141.0,24.3 142.0,25.4 143.0,26.5 144.0,27.6 145.0,28.8 146.0,30.0 147.0,31.3 148.0,32.5 149.0,33.7 150.0,35.0 151.0,36.3 152.0,37.5 153.0,38.7 154.0,40.0 155.0,41.2 156.0,42.4 157.0,43.5 158.0,44.6 159.0,45.7 160.0,46.8 161.0,47.7 162.0,48.7 163.0,49.6 164.0,50.4 165.0,51.2 166.0,51.9 167.0,52.5 168.0,53.1 169.0,53.6 170.0,54.0 171.0,54.4 172.0,54.6 173.0,54.8 174.0,55.0 175.0,55.0 176.0,55.0 177.0,54.8 178.0,54.6 179.0,54.4 180.0,54.0 181.0,53.6 182.0,53.1 183.0,52.5 184.0,51.9 185.0,51.2 186.0,50.4 187.0,49.6 188.0,48.7 189.0,47.7 190.0,46.8 191.0,45.7 192.0,44.6 193.0,43.5 194.0,42.4 195.0,41.2 196.0,40.0 197.0,38.7 198.0,37.5 199.0,36.3 200.0,35.0" fill="none" stroke="#9a9a9a" stroke-width="1.5" stroke-dasharray="4 3"/><polyline points="0.0,25.4 1.0,23.4 2.0,21.7 3.0,20.2 4.0,19.0 5.0,18.2 6.0,17.6 7.0,17.3 8.0,17.3 9.0,17.5 10.0,18.0 11.0,18.6 12.0,19.3 13.0,20.1 14.0,21.0 15.0,21.9 16.0,22.8 17.0,23.6 18.0,24.4 19.0,25.0 20.0,25.6 21.0,26.0 22.0,26.3 23.0,26.5 24.0,26.6 25.0,26.6 26.0,26.5 27.0,26.3 28.0,26.1 29.0,25.9 30.0,25.7 31.0,25.5 32.0,25.4 33.0,25.3 34.0,25.4 35.0,25.5 36.0,25.8 37.0,26.2 38.0,26.7 39.0,27.2 40.0,27.9 41.0,28.6 42.0,29.4 43.0,30.3 44.0,31.1 45.0,31.9 46.0,32.7 47.0,33.5 48.0,34.2 49.0,34.7 50.0,35.2 51.0,35.6 52.0,35.9 53.0,36.1 54.0,36.2 55.0,36.3 56.0,36.3 57.0,36.2 58.0,36.2 59.0,36.2 60.0,36.2 61.0,36.3 62.0,36.5 63.0,36.9 64.0,37.4 65.0,38.0 66.0,38.9 67.0,39.9 68.0,41.1 69.0,42.4 70.0,44.0 71.0,45.6 72.0,47.3 73.0,49.1 74.0,51.0 75.0,52.8 76.0,54.5 77.0,56.1 78.0,57.6 79.0,58.9 80.0,59.9 81.0,60.6 82.0,61.1 83.0,61.2 84.0,60.9 85.0,60.3 86.0,59.3 87.0,58.0 88.0,56.4 89.0,54.4 90.0,52.2 91.0,49.7 92.0,47.1 93.0,44.3 94.0,41.4 95.0,38.5 96.0,35.7 97.0,32.9 98.0,30.2 99.0,27.7 100.0,25.4 101.0,23.4 102.0,21.7 103.0,20.2 104.0,19.0 105.0,18.2 106.0,17.6 107.0,17.3 108.0,17.3 109.0,17.5 110.0,18.0 111.0,18.6 112.0,19.3 113.0,20.1 114.0,21.0 115.0,21.9 116.0,22.8 117.0,23.6 118.0,24.4 119.0,25.0 120.0,25.6 121.0,26.0 122.0,26.3 123.0,26.5 124.0,26.6 125.0,26.6 126.0,26.5 127.0,26.3 128.0,26.1 129.0,25.9 130.0,25.7 131.0,25.5 132.0,25.4 133.0,25.3 134.0,25.4 135.0,25.5 136.0,25.8 137.0,26.2 138.0,26.7 139.0,27.2 140.0,27.9 141.0,28.6 142.0,29.4 143.0,30.3 144.0,31.1 145.0,31.9 146.0,32.7 147.0,33.5 148.0,34.2 149.0,34.7 150.0,35.2 151.0,35.6 152.0,35.9 153.0,36.1 154.0,36.2 155.0,36.3 156.0,36.3 157.0,36.2 158.0,36.2 159.0,36.2 160.0,36.2 161.0,36.3 162.0,36.5 163.0,36.9 164.0,37.4 165.0,38.0 166.0,38.9 167.0,39.9 168.0,41.1 169.0,42.4 170.0,44.0 171.0,45.6 172.0,47.3 173.0,49.1 174.0,51.0 175.0,52.8 176.0,54.5 177.0,56.1 178.0,57.6 179.0,58.9 180.0,59.9 181.0,60.6 182.0,61.1 183.0,61.2 184.0,60.9 185.0,60.3 186.0,59.3 187.0,58.0 188.0,56.4 189.0,54.4 190.0,52.2 191.0,49.7 192.0,47.1 193.0,44.3 194.0,41.4 195.0,38.5 196.0,35.7 197.0,32.9 198.0,30.2 199.0,27.7 200.0,25.4" fill="none" stroke="var(--c-timbre)" stroke-width="2.5"/></svg>
<p class="nt-note">Même période, forme différente&nbsp;: même note, autre instrument.</p>
</div>
</div>

<p class="nt-note nt-center">En pointillés gris&nbsp;: le signal de référence.</p>

## Intensité sonore

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-book"></i>Définition</p>
<p>L'<span class="imp">intensité sonore $I$</span> (ou intensité acoustique) est la <span class="imp">puissance $P$</span> transportée par l'onde sonore <span class="imp">par unité de surface</span>.</p>
</div>

<div class="nt-grid">
<div>
<div class="nt-formula">$$I=\frac{P}{S}$$</div>
<ul class="nt-units-list">
<li>$P$ en <span class="imp nt-hole">$\pu{W}$</span></li>
<li>$S$ en <span class="imp nt-hole">$\pu{m2}$</span></li>
<li>$I$ en <span class="imp nt-hole">$\pu{W*m-2}$</span></li>
</ul>
</div>
<div>
<svg class="nt-svg" viewBox="0 0 420 170" role="img" aria-label="La puissance sonore traverse une surface S perpendiculaire à la direction de propagation"><defs><marker id="arrS" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="var(--nt-ink)"/></marker></defs><polygon points="230,22 280,46 280,152 230,128" fill="var(--nt-fill-2)" stroke="var(--nt-ink)" stroke-width="2"/><line x1="30" y1="45" x2="244" y2="45" stroke="var(--nt-ink)" stroke-width="2" marker-end="url(#arrS)" opacity=".85"/><line x1="30" y1="70" x2="248" y2="70" stroke="var(--nt-ink)" stroke-width="2" marker-end="url(#arrS)" opacity=".85"/><line x1="30" y1="95" x2="248" y2="95" stroke="var(--nt-ink)" stroke-width="2" marker-end="url(#arrS)" opacity=".85"/><line x1="30" y1="120" x2="244" y2="120" stroke="var(--nt-ink)" stroke-width="2" marker-end="url(#arrS)" opacity=".85"/><text x="292" y="98" font-size="22" font-weight="700" fill="var(--nt-ink)" font-style="italic">S</text><text x="30" y="30" font-size="13" fill="currentColor">puissance <tspan font-style="italic" font-weight="700">P</tspan> transportée</text><text x="30" y="150" font-size="12" fill="currentColor" opacity=".75">direction de propagation →</text><text x="315" y="122" font-size="12" fill="var(--imp)">surface</text><text x="315" y="137" font-size="12" fill="var(--imp)">perpendiculaire</text><text x="315" y="152" font-size="12" fill="var(--imp)">à la propagation</text></svg>
<p class="nt-center">La surface doit être perpendiculaire à la direction de propagation.</p>
</div>
</div>

<figure class="nt-fig">
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d1/RIAN_archive_38689_Defending_the_Moscow_sky.jpg" alt="Soldats soviétiques utilisant un détecteur acoustique d'avions à quatre grands pavillons, Moscou, 1941" loading="lazy">
<figcaption>«&nbsp;Défendre le ciel de Moscou&nbsp;» (1941). Avant l'invention du radar, des soldats soviétiques écoutaient l'arrivée des bombardiers allemands avec ces grands pavillons acoustiques. Le son recueilli était conduit par des tubes jusqu'aux écouteurs du technicien. Une paire de pavillons horizontale permettait de repérer la direction de l'avion, la paire verticale son altitude. <i>Photo&nbsp;: RIA Novosti, Wikimedia Commons.</i></figcaption>
</figure>

<div class="nt-box nt-ask">
<p class="nt-box-title"><i class="fa-solid fa-circle-question"></i>Pourquoi des pavillons aussi grands&nbsp;?</p>
<p>Un pavillon recueille la puissance sonore sur une grande surface puis la canalise vers la toute petite surface de l'écouteur. La même puissance $P$ traverse alors une surface $S$ bien plus petite&nbsp;: d'après $I = P/S$, l'intensité sonore à l'oreille est beaucoup plus grande.</p>
</div>

<figure class="nt-fig">
<img src="/trompettesint.png" alt="Illustration de l'additivité de l'intensité sonore avec des trompettes" loading="lazy">
</figure>

<div class="nt-box nt-know">
<p class="nt-box-title"><i class="fa-solid fa-plus"></i>L'intensité sonore est additive</p>
<p>S'il y a 2 ou 10 fois plus de sources sonores (de même puissance), l'intensité (à la même distance) est multipliée par 2 ou 10.</p>
</div>

<p class="nt-lead">Mais notre sensation auditive ne semble pas, elle, proportionnelle au nombre de sources. C'est cette non proportionnalité qui permet d'avoir une plage de sensibilité si étendue&nbsp;:</p>

<div class="nt-grid">
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-ear-listen"></i>Seuil d'audibilité</p>
<p>Le seuil d'audibilité à $\pu{1 kHz}$, appelé <span class="imp">intensité sonore de référence $I_0$</span>, vaut $\pu{1,0E-12 W*m-2}$.</p>
</div>
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-bolt"></i>Seuil de douleur</p>
<p>Le seuil de douleur est de l'ordre de $\pu{1 W*m-2}$.</p>
</div>
</div>

<p class="nt-lead nt-center">Il y a un facteur <span class="imp">mille milliards</span> entre les deux 🤯</p>

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-ruler"></i>Pour se représenter ce facteur $10^{12}$</p>
<p>Si le seuil d'audibilité correspondait à une longueur de $\pu{1 mm}$, le seuil de douleur correspondrait à $10^{12}\ \pu{mm} = \pu{1E6 km}$, soit environ 2,6 fois la distance Terre-Lune.</p>
</div>

<details class="nt-more">
<summary><i class="fa-solid fa-flask"></i>&nbsp; Pour les curieux&nbsp;: d'où vient la valeur de $I_0$&nbsp;?</summary>
<div class="nt-more-body">
<p>Les sonomètres mesurent en réalité la <b>pression acoustique</b>, c'est-à-dire la petite surpression $p$ créée par l'onde (en pascals). Pour une onde plane dans l'air, l'intensité est reliée à la valeur efficace $p_{\text{eff}}$ de cette surpression par&nbsp;:</p>
<p class="nt-center">$I = \dfrac{p_{\text{eff}}^2}{\rho\, c}$</p>
<p>où $\rho \approx \pu{1,2 kg*m-3}$ est la masse volumique de l'air et $c \approx \pu{343 m*s-1}$ la célérité du son (à $20\,^\circ\mathrm{C}$), soit $\rho\, c \approx \pu{415 kg*m-2*s-1}$.</p>
<p>Le seuil d'audition correspond à $p_{\text{eff}} = \pu{2E-5 Pa}$, d'où $I_0 = \dfrac{\left(2\times 10^{-5}\right)^2}{415} \approx \pu{1,0E-12 W*m-2}$. Notre oreille détecte donc des variations de pression environ 5 milliards de fois plus petites que la pression atmosphérique&nbsp;!</p>
</div>
</details>

<div class="nt-box nt-know">
<p class="nt-box-title"><i class="fa-solid fa-chart-line"></i>Notre sensibilité est <span class="nt-hole">logarithmique</span></p>
<p>On peut par exemple mesurer que l'intensité du son émis par quelqu'un qui parle fort est environ 10&nbsp;000 fois plus grande que celle d'une personne qui chuchote à la même distance&nbsp;!</p>
<p>On n'a pourtant pas la sensation d'un son 10&nbsp;000 fois plus fort…</p>
</div>

## Point mathématique

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-square-root-variable"></i>Le logarithme décimal</p>
<p>$\log$ est la fonction logarithme décimal (logarithme en base 10), définie sur $]0\,;+\infty[$&nbsp;:</p>
<p class="nt-center">$\log(x) = \dfrac{\ln(x)}{\ln(10)}$</p>
<p>On a ainsi $\log(10)=$ <span class="imp nt-hole">$1$</span>.</p>
</div>

<div class="nt-grid">
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-calculator"></i>Règles de calcul</p>
<p>Les règles de calcul de $\log$ sont les mêmes que celles de $\ln$&nbsp;:</p>
<ul class="nt-facts">
<li>$\log(1)=$ <span class="imp nt-hole">$0$</span></li>
<li>$\log(a{\color{#C7392D}\times} b)=$ <span class="nt-hole">$\log(a){\color{#C7392D}+}\log(b)$</span></li>
<li>$\log(a{\color{#C7392D}\,/\,}b)=$ <span class="nt-hole">$\log(a){\color{#C7392D}-}\log(b)$</span></li>
<li>$\log(a^{\color{#C7392D}n})=$ <span class="nt-hole">${\color{#C7392D}n}\log(a)$</span></li>
</ul>
<p class="nt-note">pour $a > 0$, $b > 0$ et $n$ réel.</p>
</div>
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-arrow-right-arrow-left"></i>Fonction réciproque</p>
<p>La fonction réciproque du logarithme décimal est la fonction <span class="imp nt-hole">$10^x$</span>.</p>
<p>Ainsi, si $\log(x)=b$, alors $x=$ <span class="imp nt-hole">$10^b$</span>.</p>
</div>
</div>

<div class="nt-box nt-know">
<p class="nt-box-title"><i class="fa-solid fa-lightbulb"></i>L'idée à retenir</p>
<p>Le boulot de la fonction $\log$ est de fournir l'exposant d'un nombre écrit sous la forme d'une puissance de 10. Exemples&nbsp;:</p>
<ul class="nt-facts">
<li>$\log(10^{\color{#C7392D} 7}) =$ <span class="imp nt-hole">$7$</span></li>
<li>$\log(0{,}01) = \log(10^{\color{#C7392D}-2}) =$ <span class="imp nt-hole">$-2$</span></li>
<li>$\log(2) \approx \log(10^{\color{#C7392D}0{,}3}) \approx$ <span class="imp nt-hole">$0{,}3$</span></li>
</ul>
</div>

<svg class="nt-svg" viewBox="0 0 680 170" role="img" aria-label="Règle logarithmique : chaque multiplication par 10 de x ajoute 1 à log(x)"><text x="20" y="66" font-size="15" font-weight="700" fill="currentColor" font-style="italic">x</text><text x="20" y="114" font-size="15" font-weight="700" fill="var(--imp)">log(x)</text><line x1="80" y1="85" x2="650" y2="85" stroke="currentColor" stroke-width="2"/><line x1="100.0" y1="77" x2="100.0" y2="93" stroke="currentColor" stroke-width="2"/><text x="100.0" y="66" font-size="14" text-anchor="middle" fill="currentColor">0,01</text><text x="100.0" y="114" font-size="14" text-anchor="middle" fill="var(--imp)" font-weight="700">−2</text><line x1="206.0" y1="77" x2="206.0" y2="93" stroke="currentColor" stroke-width="2"/><text x="206.0" y="66" font-size="14" text-anchor="middle" fill="currentColor">0,1</text><text x="206.0" y="114" font-size="14" text-anchor="middle" fill="var(--imp)" font-weight="700">−1</text><line x1="312.0" y1="77" x2="312.0" y2="93" stroke="currentColor" stroke-width="2"/><text x="312.0" y="66" font-size="14" text-anchor="middle" fill="currentColor">1</text><text x="312.0" y="114" font-size="14" text-anchor="middle" fill="var(--imp)" font-weight="700">0</text><line x1="343.9" y1="77" x2="343.9" y2="93" stroke="var(--imp)" stroke-width="2"/><text x="343.9" y="66" font-size="14" text-anchor="middle" fill="var(--imp)">2</text><text x="343.9" y="114" font-size="14" text-anchor="middle" fill="var(--imp)" font-weight="700">0,3</text><line x1="418.0" y1="77" x2="418.0" y2="93" stroke="currentColor" stroke-width="2"/><text x="418.0" y="66" font-size="14" text-anchor="middle" fill="currentColor">10</text><text x="418.0" y="114" font-size="14" text-anchor="middle" fill="var(--imp)" font-weight="700">1</text><line x1="524.0" y1="77" x2="524.0" y2="93" stroke="currentColor" stroke-width="2"/><text x="524.0" y="66" font-size="14" text-anchor="middle" fill="currentColor">100</text><text x="524.0" y="114" font-size="14" text-anchor="middle" fill="var(--imp)" font-weight="700">2</text><line x1="630.0" y1="77" x2="630.0" y2="93" stroke="currentColor" stroke-width="2"/><text x="630.0" y="66" font-size="14" text-anchor="middle" fill="currentColor">1 000</text><text x="630.0" y="114" font-size="14" text-anchor="middle" fill="var(--imp)" font-weight="700">3</text><path d="M312,48 Q365.0,18 418,48" fill="none" stroke="var(--nt-ink)" stroke-width="1.5"/><text x="365.0" y="26" font-size="13" text-anchor="middle" fill="var(--nt-ink)" font-weight="700">× 10</text><path d="M312,122 Q365.0,152 418,122" fill="none" stroke="var(--imp)" stroke-width="1.5"/><text x="365.0" y="160" font-size="13" text-anchor="middle" fill="var(--imp)" font-weight="700">+ 1</text></svg>

<p class="nt-caption nt-center">Sur cette règle, chaque multiplication de $x$ par 10 ajoute 1 à $\log(x)$&nbsp;: le logarithme transforme les multiplications en additions.</p>

## Niveau d'intensité sonore

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-book"></i>Définition</p>
<p>Le <span class="imp">niveau d'intensité sonore $L$</span> (pour «&nbsp;Level&nbsp;») se mesure en <span class="imp">décibels (dB)</span> et est donné par la relation&nbsp;:</p>
<div class="nt-formula">$$L=10\log\left(\frac{I}{I_0}\right)$$</div>
<p class="nt-center">$I_0=\pu{1,0E-12 W*m-2}$ est l'<span class="imp">intensité sonore de référence</span>.</p>
</div>

<svg class="nt-svg" viewBox="0 0 760 240" role="img" aria-label="Correspondance entre intensité sonore en watts par mètre carré et niveau sonore en décibels, avec quelques repères"><defs><linearGradient id="gradDB" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#40c057"/><stop offset=".5" stop-color="#fab005"/><stop offset=".75" stop-color="#fd7e14"/><stop offset="1" stop-color="#e03131"/></linearGradient></defs><text x="385" y="22" font-size="13" text-anchor="middle" fill="var(--nt-ink)" font-weight="700">Intensité sonore I (en W·m⁻²) : chaque graduation multiplie I par 10</text><rect x="60" y="104" width="650" height="14" rx="7" fill="url(#gradDB)"/><line x1="60" y1="98" x2="60" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="60" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−12</tspan></text><text x="60" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">0</text><line x1="110" y1="98" x2="110" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="110" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−11</tspan></text><text x="110" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">10</text><line x1="160" y1="98" x2="160" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="160" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−10</tspan></text><text x="160" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">20</text><line x1="210" y1="98" x2="210" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="210" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−9</tspan></text><text x="210" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">30</text><line x1="260" y1="98" x2="260" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="260" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−8</tspan></text><text x="260" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">40</text><line x1="310" y1="98" x2="310" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="310" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−7</tspan></text><text x="310" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">50</text><line x1="360" y1="98" x2="360" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="360" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−6</tspan></text><text x="360" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">60</text><line x1="410" y1="98" x2="410" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="410" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−5</tspan></text><text x="410" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">70</text><line x1="460" y1="98" x2="460" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="460" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−4</tspan></text><text x="460" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">80</text><line x1="510" y1="98" x2="510" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="510" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−3</tspan></text><text x="510" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">90</text><line x1="560" y1="98" x2="560" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="560" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−2</tspan></text><text x="560" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">100</text><line x1="610" y1="98" x2="610" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="610" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10<tspan dy="-7" font-size="9">−1</tspan></text><text x="610" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">110</text><line x1="660" y1="98" x2="660" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="660" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">1</text><text x="660" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">120</text><line x1="710" y1="98" x2="710" y2="124" stroke="currentColor" stroke-width="1.2"/><text x="710" y="88" font-size="12" text-anchor="middle" fill="var(--nt-ink)">10</text><text x="710" y="142" font-size="12" text-anchor="middle" fill="var(--imp)" font-weight="700">130</text><path d="M55,100 L65,100 L60,108 z" fill="currentColor"/><line x1="60" y1="149" x2="60" y2="160" stroke="currentColor" stroke-opacity=".45" stroke-dasharray="2 2"/><text x="58" y="172" font-size="12" text-anchor="start" fill="currentColor">seuil d'audibilité</text><path d="M205,100 L215,100 L210,108 z" fill="currentColor"/><line x1="210" y1="149" x2="210" y2="184" stroke="currentColor" stroke-opacity=".45" stroke-dasharray="2 2"/><text x="210" y="196" font-size="12" text-anchor="middle" fill="currentColor">chuchotement</text><path d="M355,100 L365,100 L360,108 z" fill="currentColor"/><line x1="360" y1="149" x2="360" y2="160" stroke="currentColor" stroke-opacity=".45" stroke-dasharray="2 2"/><text x="360" y="172" font-size="12" text-anchor="middle" fill="currentColor">conversation</text><path d="M405,100 L415,100 L410,108 z" fill="currentColor"/><line x1="410" y1="149" x2="410" y2="184" stroke="currentColor" stroke-opacity=".45" stroke-dasharray="2 2"/><text x="410" y="196" font-size="12" text-anchor="middle" fill="currentColor">voix forte</text><path d="M655,100 L665,100 L660,108 z" fill="currentColor"/><line x1="660" y1="149" x2="660" y2="160" stroke="currentColor" stroke-opacity=".45" stroke-dasharray="2 2"/><text x="662" y="172" font-size="12" text-anchor="end" fill="currentColor">seuil de douleur</text><text x="385" y="230" font-size="13" text-anchor="middle" fill="var(--imp)" font-weight="700">Niveau sonore L (en dB) : chaque graduation ajoute 10 dB</text></svg>

<p class="nt-caption nt-center">Une échelle en décibels «&nbsp;comprime&nbsp;» les douze puissances de 10 qui séparent le seuil d'audibilité du seuil de douleur en une échelle de 0 à 120&nbsp;dB.</p>

<figure class="nt-fig">
<img src="/trompettesdb.png" alt="Illustration : doubler le nombre de trompettes ajoute 3 dB" loading="lazy">
</figure>

<div class="nt-box nt-know">
<p class="nt-box-title"><i class="fa-solid fa-thumbtack"></i>À retenir</p>
<p>Doubler l'intensité acoustique revient à <span class="imp nt-hole">ajouter 3 dB</span> au niveau sonore et multiplier l'intensité par 10 <span class="imp nt-hole">ajoute 10 dB</span>.</p>
</div>

<div class="nt-scroll">
<table class="nt-cs">
<thead><tr><th>Nombre de sources<br>de même intensité</th><th>Intensité sonore</th><th>Niveau sonore</th></tr></thead>
<tbody>
<tr><td>1</td><td>$I_t$</td><td>$L_t$</td></tr>
<tr><td>2</td><td>$2\,I_t$</td><td><span class="nt-pill">$L_t + \pu{3 dB}$</span></td></tr>
<tr><td>4</td><td>$4\,I_t$</td><td><span class="nt-pill">$L_t + \pu{6 dB}$</span></td></tr>
<tr><td>8</td><td>$8\,I_t$</td><td><span class="nt-pill">$L_t + \pu{9 dB}$</span></td></tr>
<tr><td>10</td><td>$10\,I_t$</td><td><span class="nt-pill">$L_t + \pu{10 dB}$</span></td></tr>
<tr><td>100</td><td>$100\,I_t$</td><td><span class="nt-pill">$L_t + \pu{20 dB}$</span></td></tr>
</tbody>
</table>
</div>

<p class="nt-caption nt-center">Multiplier les intensités revient à additionner des décibels&nbsp;: c'est la règle $\log(a\times b)=\log(a)+\log(b)$ en action.</p>

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-pen-nib"></i>Preuve</p>
<p>Si ${\color{#2B8A3E}I_t}$ est l'intensité sonore d'une trompette, pour 2 trompettes, on a&nbsp;: ${\color{#D98400}I} = 2\times {\color{#2B8A3E}I_t}$.</p>
<p>Appelons ${\color{#2B8A3E}L_t}$ le niveau sonore d'une trompette et cherchons le niveau sonore ${\color{#D98400}L}$ des 2 trompettes&nbsp;:</p>
<div class="nt-scroll">$$\begin{aligned}{\color{#D98400}L} &= 10\times \log\left(\frac{\color{#D98400}I}{I_0}\right)\\ &= 10\times \log\left(\frac{2\times {\color{#2B8A3E}I_t}}{I_0}\right)\\ &= 10\times \log\left(2\times\frac{\color{#2B8A3E}I_t}{I_0}\right)\\ &= 10\times\left(\log(2) + \log\left(\frac{\color{#2B8A3E}I_t}{I_0}\right)\right)\\ &= 10\times \log\left(\frac{\color{#2B8A3E}I_t}{I_0}\right) + {\color{#C2255C}10\times\log(2)}\\ &= {\color{#2B8A3E}L_t} + {\color{#C2255C}\pu{3 dB}}\end{aligned}$$</div>
<p class="nt-note">car $10\times\log(2) \approx 10 \times 0{,}30 = \pu{3,0 dB}$.</p>
</div>

<figure class="nt-fig">
<video controls loop playsinline preload="metadata" src="/trompettedbfort.mp4"></video>
</figure>

<figure class="nt-fig">
<img src="/echelleidb.png" alt="Échelle des niveaux sonores de sons de la vie courante" loading="lazy">
</figure>

<div class="nt-embed nt-embed-edu">
<iframe src="https://www.edumedia.com/media/frame/fr/155/?auth=51a8d1c53ced40fce13e3b1dccd9e62d/27824" title="Animation eduMedia sur le niveau sonore" loading="lazy" allowfullscreen></iframe>
</div>

<details class="nt-more">
<summary><i class="fa-solid fa-ear-listen"></i>&nbsp; Le saviez-vous&nbsp;? Les décibels de l'audiogramme</summary>
<div class="nt-more-body">
<p>Pour les tests audiométriques qui mesurent le degré de perte auditive, on utilise le dB HL (pour <i>hearing level</i>). Le dB HL tient compte de la variation de sensibilité de l'oreille humaine en fonction de la fréquence (donc de la hauteur des sons)&nbsp;: pour chaque fréquence testée, 0&nbsp;dB HL correspond à l'intensité minimale perçue en moyenne par les personnes normo-entendantes.</p>
</div>
</details>

<p class="nt-lead">Comment obtenir l'intensité sonore $I$ à partir du niveau d'intensité sonore $L$&nbsp;?</p>

<div class="nt-formula">$$I=I_0\times 10^{\frac{L}{10}}$$</div>

<details class="nt-more">
<summary><i class="fa-solid fa-pen-nib"></i>&nbsp; Voir la démonstration</summary>
<div class="nt-more-body">
<ol class="nt-steps">
<li><p>On isole le logarithme&nbsp;: $L = 10\log\left(\dfrac{I}{I_0}\right) \iff \dfrac{L}{10} = \log\left(\dfrac{I}{I_0}\right)$.</p></li>
<li><p>On applique la fonction réciproque $10^x$ aux deux membres&nbsp;: $\dfrac{I}{I_0} = 10^{\frac{L}{10}}$.</p></li>
<li><p>On multiplie par $I_0$&nbsp;: $I = I_0\times 10^{\frac{L}{10}}$.</p></li>
</ol>
</div>
</details>

<div class="nt-lab" id="nt-lab-db">
<p class="nt-lab-title"><i class="fa-solid fa-sliders"></i>À vous de jouer&nbsp;: le convertisseur décibels ↔ intensité</p>
<label for="nt-lab-L" class="nt-note">Faites varier le niveau sonore, ou utilisez les boutons pour voir l'effet du nombre de sources et de la distance.</label>
<input type="range" id="nt-lab-L" min="0" max="130" step="0.01" value="60">
<div class="nt-lab-bar" aria-hidden="true"><div class="nt-lab-cursor"></div></div>
<div class="nt-lab-out" aria-live="polite">
<span>$L$ = <b class="nt-lab-L">60 dB</b></span>
<span>$I$ = <b class="nt-lab-I">1,0 × 10<sup>−6</sup> W·m<sup>−2</sup></b></span>
</div>
<p class="nt-lab-msg"></p>
<div class="nt-lab-btns">
<button type="button" data-k="2">× 2 sources</button>
<button type="button" data-k="10">× 10 sources</button>
<button type="button" data-k="0.25">distance × 2</button>
<button type="button" data-k="0.01">distance × 10</button>
</div>
</div>

## Atténuation

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-arrow-trend-down"></i>Définition</p>
<p>L'<span class="imp">atténuation</span> (en dB) mesure la diminution du niveau d'intensité sonore&nbsp;: $A = L_{\text{avant}} - L_{\text{après}}$.</p>
<p>Il y a deux types d'atténuation&nbsp;: l'atténuation <span class="imp nt-hole">géométrique</span> et l'atténuation <span class="imp nt-hole">par absorption</span>.</p>
</div>

### Atténuation géométrique

<p class="nt-lead">Elle est due à l'<span class="imp">éloignement</span> entre la source et l'observateur.</p>

<p>En effet, <span class="imp">plus la source est éloignée</span> et <span class="imp">plus la surface</span> sur laquelle la puissance sonore se répartit <span class="imp nt-hole">est grande</span> et donc <span class="imp">plus l'intensité sonore</span> <span class="imp nt-hole">est faible</span>.</p>

<p>Si la source est omnidirectionnelle (même intensité sonore dans toutes les directions), alors l'intensité sonore à une distance $d$ de la source se répartit sur <span class="nt-hole" style="font-weight:700;color:var(--c-int);">une sphère de rayon $d$</span> centrée sur la source. On a donc&nbsp;:</p>

<div class="nt-formula">$$I=\frac{P}{\color{#C27C0E}4\pi d^2}$$</div>

<svg class="nt-svg" viewBox="0 0 520 350" role="img" aria-label="La même puissance se répartit sur 1, 4 puis 9 carrés quand la distance passe de d à 2d puis 3d"><line x1="40" y1="175" x2="449.5" y2="50.8" stroke="currentColor" stroke-opacity=".35" stroke-dasharray="4 3"/><line x1="40" y1="175" x2="350.5" y2="119.2" stroke="currentColor" stroke-opacity=".35" stroke-dasharray="4 3"/><line x1="40" y1="175" x2="449.5" y2="230.8" stroke="currentColor" stroke-opacity=".35" stroke-dasharray="4 3"/><line x1="40" y1="175" x2="350.5" y2="299.2" stroke="currentColor" stroke-opacity=".35" stroke-dasharray="4 3"/><polygon points="143.5,216.4 143.5,156.4 176.5,133.6 176.5,193.6" fill="var(--nt-fill)" fill-opacity=".85" stroke="var(--nt-ink)" stroke-width="1.6"/><polygon points="143.5,216.4 143.5,156.4 176.5,133.6 176.5,193.6" fill="#fab005" fill-opacity=".75"/><text x="148.5" y="238.4" font-size="14" font-weight="700" fill="currentColor" font-style="italic">d</text><text x="148.5" y="254.4" font-size="12" fill="var(--imp)" font-weight="700">1 carré</text><polygon points="247.0,257.8 247.0,137.8 313.0,92.2 313.0,212.2" fill="var(--nt-fill)" fill-opacity=".85" stroke="var(--nt-ink)" stroke-width="1.6"/><polygon points="247.0,257.8 247.0,197.8 280.0,175.0 280.0,235.0" fill="#fab005" fill-opacity=".75"/><line x1="247.0" y1="197.8" x2="313.0" y2="152.2" stroke="var(--nt-ink)" stroke-width="1"/><line x1="280.0" y1="235.0" x2="280.0" y2="115.0" stroke="var(--nt-ink)" stroke-width="1"/><text x="252.0" y="279.8" font-size="14" font-weight="700" fill="currentColor" font-style="italic">2d</text><text x="252.0" y="295.8" font-size="12" fill="var(--imp)" font-weight="700">4 carrés</text><polygon points="350.5,299.2 350.5,119.2 449.5,50.8 449.5,230.8" fill="var(--nt-fill)" fill-opacity=".85" stroke="var(--nt-ink)" stroke-width="1.6"/><polygon points="350.5,299.2 350.5,239.2 383.5,216.4 383.5,276.4" fill="#fab005" fill-opacity=".75"/><line x1="350.5" y1="239.2" x2="449.5" y2="170.8" stroke="var(--nt-ink)" stroke-width="1"/><line x1="383.5" y1="276.4" x2="383.5" y2="96.4" stroke="var(--nt-ink)" stroke-width="1"/><line x1="350.5" y1="179.2" x2="449.5" y2="110.8" stroke="var(--nt-ink)" stroke-width="1"/><line x1="416.5" y1="253.6" x2="416.5" y2="73.6" stroke="var(--nt-ink)" stroke-width="1"/><text x="355.5" y="321.2" font-size="14" font-weight="700" fill="currentColor" font-style="italic">3d</text><text x="355.5" y="337.2" font-size="12" fill="var(--imp)" font-weight="700">9 carrés</text><circle cx="40" cy="175" r="7" fill="var(--imp)"/><text x="34" y="161" font-size="12" fill="currentColor">source</text></svg>

<p class="nt-caption nt-center">La même puissance traverse 1 carré à la distance $d$, 4 carrés à $2d$, 9 carrés à $3d$&nbsp;: chaque carré (en jaune) reçoit 4 fois, puis 9 fois moins de puissance.</p>

<div class="nt-embed nt-embed-ggb">
<iframe src="https://www.geogebra.org/material/iframe/id/fbyk36y6" title="Applet GeoGebra : atténuation géométrique" loading="lazy" allowfullscreen></iframe>
</div>

<div class="nt-box nt-know">
<p class="nt-box-title"><i class="fa-solid fa-flag-checkered"></i>Conclusion</p>
<p>L'intensité sonore varie <span class="imp nt-hole">inversement proportionnellement au carré de la distance à la source</span>.</p>
</div>

<p class="nt-lead">Conséquences&nbsp;:</p>

<div class="nt-grid">
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-xmark"></i>Doubler la distance</p>
<p><span class="imp">Doubler la distance</span> divise l'intensité sonore par <span class="imp nt-hole">4</span>, ce qui correspond à une <span class="imp">atténuation de</span> <span class="imp nt-hole">6 dB</span> du niveau sonore.</p>
<p class="nt-center">$d\rightarrow 2d\Rightarrow I\rightarrow I/4 \Leftrightarrow L\rightarrow L-6$</p>
</div>
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-xmark"></i>Multiplier la distance par 10</p>
<p><span class="imp">Multiplier par 10 la distance</span> divise l'intensité sonore par <span class="imp nt-hole">100</span>, ce qui correspond à une <span class="imp">atténuation de</span> <span class="imp nt-hole">20 dB</span> du niveau sonore.</p>
<p class="nt-center">$d\rightarrow 10d\Rightarrow I\rightarrow I/100 \Leftrightarrow L\rightarrow L-20$</p>
</div>
</div>

<details class="nt-more">
<summary><i class="fa-solid fa-pen-nib"></i>&nbsp; D'où viennent ces 6 dB et ces 20 dB&nbsp;?</summary>
<div class="nt-more-body">
<p>Si l'intensité est divisée par 4, le niveau sonore devient $L' = 10\log\left(\dfrac{I/4}{I_0}\right) = 10\log\left(\dfrac{I}{I_0}\right) - 10\log(4) = L - 10\log(4)$.</p>
<p>Or $10\log(4) = 10\log(2^2) = 20\log(2) \approx 20\times 0{,}30 = 6$&nbsp;: on perd environ $\pu{6 dB}$.</p>
<p>De même, si l'intensité est divisée par 100, on perd $10\log(100) = 10\times 2 = \pu{20 dB}$.</p>
</div>
</details>

### Atténuation par absorption

<p class="nt-lead">Le niveau d'intensité sonore d'une onde sonore rencontrant un obstacle est atténué car une partie de son <span class="imp">énergie est absorbée</span> par le milieu matériel composant l'obstacle.</p>

<p>La proportion d'énergie absorbée dépend du <span class="imp nt-hole">matériau</span> composant l'obstacle et de <span class="imp nt-hole">l'épaisseur</span> de celui-ci.</p>

<figure class="nt-fig">
<img src="/abstransm.png" alt="Schéma : absorption et transmission d'une onde sonore par un obstacle" loading="lazy">
<figcaption>Remarque&nbsp;: une partie de l'onde est aussi réfléchie par l'obstacle, mais les exercices de terminale négligent généralement cette réflexion.</figcaption>
</figure>

<figure class="nt-fig">
<img src="/bouchons.png" alt="Bouchons d'oreille en mousse et bouchons moulés" loading="lazy">
</figure>

<div class="nt-box nt-ask">
<p class="nt-box-title"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pourquoi les bouchons moulés sont-ils plus adaptés à des musiciens&nbsp;?</p>
</div>

<details class="nt-more">
<summary><i class="fa-solid fa-key"></i>&nbsp; Élément de réponse</summary>
<div class="nt-more-body">
<p>Les bouchons en mousse modifient le timbre, puisqu'ils n'atténuent pas toutes les fréquences de la même façon&nbsp;: les harmoniques (les fréquences élevées du spectre) disparaissent. Et de toute façon, ils atténuent trop. Les bouchons moulés pour musiciens atténuent à peu près de la même façon toutes les fréquences&nbsp;: le son est moins fort, mais son timbre est préservé.</p>
</div>
</details>

<figure class="nt-fig">
<video controls playsinline preload="metadata" src="/anechoique.mp4"></video>
<figcaption>Une chambre anéchoïque&nbsp;: ses parois absorbent presque totalement les ondes sonores.</figcaption>
</figure>

<details class="nt-more">
<summary><i class="fa-solid fa-flask"></i>&nbsp; Pour aller plus loin&nbsp;: le temps de réverbération</summary>
<div class="nt-more-body">
<p>Le temps de réverbération d'une salle est la durée au bout de laquelle le niveau sonore a diminué de $\pu{60 dB}$ après l'arrêt de la source. En pratique, une telle baisse est difficile à mesurer&nbsp;: si l'on suppose que le niveau décroît de façon linéaire, on mesure la durée nécessaire pour perdre $\pu{20 dB}$ ou $\pu{30 dB}$, puis on la multiplie respectivement par 3 ou par 2.</p>
</div>
</details>

<div class="nt-essentiel">
<p class="nt-essentiel-title"><i class="fa-solid fa-star"></i>L'essentiel</p>
<div class="nt-grid">
<div><p><b>Intensité sonore</b></p><p>$I=\dfrac{P}{S}$ en $\pu{W*m-2}$</p></div>
<div><p><b>Niveau sonore</b></p><p>$L=10\log\left(\dfrac{I}{I_0}\right)$ en dB</p><p>$I=I_0\times 10^{\frac{L}{10}}$</p></div>
<div><p><b>Additivité</b></p><p>$I \times 2 \Rightarrow L + \pu{3 dB}$</p><p>$I \times 10 \Rightarrow L + \pu{10 dB}$</p></div>
<div><p><b>Atténuation géométrique</b></p><p>$I=\dfrac{P}{4\pi d^2}$</p><p>$d \times 2 \Rightarrow L - \pu{6 dB}$</p><p>$d \times 10 \Rightarrow L - \pu{20 dB}$</p></div>
</div>
</div>

<script>
(function () {
  /* ----- Mode révision ----- */
  var btn = document.querySelector('.nt-quiz-toggle');
  var holes = Array.prototype.slice.call(document.querySelectorAll('.nt-hole'));
  function reveal(h) {
    if (document.body.classList.contains('nt-quiz')) { h.classList.toggle('nt-shown'); }
  }
  holes.forEach(function (h) {
    h.addEventListener('click', function () { reveal(h); });
    h.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); reveal(h); }
    });
  });
  if (btn) {
    btn.addEventListener('click', function () {
      var on = document.body.classList.toggle('nt-quiz');
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      holes.forEach(function (h) {
        h.classList.remove('nt-shown');
        if (on) { h.setAttribute('tabindex', '0'); h.setAttribute('role', 'button'); }
        else { h.removeAttribute('tabindex'); h.removeAttribute('role'); }
      });
    });
  }
  /* ----- Convertisseur dB / intensité ----- */
  var lab = document.getElementById('nt-lab-db');
  if (!lab) { return; }
  var range = document.getElementById('nt-lab-L');
  var outL = lab.querySelector('.nt-lab-L');
  var outI = lab.querySelector('.nt-lab-I');
  var msg = lab.querySelector('.nt-lab-msg');
  var cursor = lab.querySelector('.nt-lab-cursor');
  var marks = [[0, "le seuil d'audibilité"], [30, 'un chuchotement'], [60, 'une conversation'], [70, 'une voix forte'], [120, 'le seuil de douleur']];
  function sup(n) { return String(n).replace('-', '−'); }
  function show(L, note) {
    var e = L / 10 - 12;
    var n = Math.floor(e + 1e-9);
    var a = Math.pow(10, e - n);
    var aTxt = a.toFixed(1);
    if (aTxt === '10.0') { aTxt = '1.0'; n += 1; }
    outL.textContent = Math.round(L) + ' dB';
    outI.innerHTML = aTxt.replace('.', ',') + ' × 10<sup>' + sup(n) + '</sup> W·m<sup>−2</sup>';
    cursor.style.left = (L / 130 * 100) + '%';
    var best = marks[0];
    marks.forEach(function (m) { if (Math.abs(m[0] - L) < Math.abs(best[0] - L)) { best = m; } });
    var near = 'Repère le plus proche : ' + best[1] + ' (≈ ' + best[0] + ' dB).';
    msg.textContent = note ? note + ' ' + near : near;
  }
  range.addEventListener('input', function () { show(parseFloat(range.value)); });
  Array.prototype.forEach.call(lab.querySelectorAll('button[data-k]'), function (b) {
    b.addEventListener('click', function () {
      var k = parseFloat(b.getAttribute('data-k'));
      var dL = 10 * Math.log10(k);
      var L = parseFloat(range.value) + dL;
      var note = b.textContent + ' : ' + (k > 1 ? 'intensité × ' + k : 'intensité ÷ ' + Math.round(1 / k)) + ', soit ' + (dL > 0 ? '+ ' : '− ') + Math.abs(dL).toFixed(0) + ' dB.';
      if (L > 130 || L < 0) {
        L = Math.min(130, Math.max(0, L));
        note += ' (On sort de l\u2019échelle 0–130 dB.)';
      }
      range.value = L;
      show(L, note);
    });
  });
  show(parseFloat(range.value));
})();
</script>
