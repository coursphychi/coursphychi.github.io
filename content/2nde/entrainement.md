---
title: "Entraînement maths"
date: 2021-03-06T14:23:56+01:00
weight : 14
draft: false
---

<style>
ul {
  text-align: left;
}
table {
  border-collapse: collapse;
  border: 0;
}
td, th {
  border-collapse: collapse;
  text-align: center;
  vertical-align: middle;
}

/* Propriétés générales */
.btn {
  --c1: #E55D87;   /* couleurs par défaut si on oublie btn1/2/3 */
  --c2: #5FC3E4;

  display: block !important;
  width: fit-content !important;     /* largeur = contenu + padding */
  margin: 10px auto !important;      /* auto à gauche et à droite → centré */
  padding: 15px 45px !important;
  text-align: center !important;
  text-transform: uppercase !important;
  text-decoration: none !important;
  color: #fff !important;

  background-image: linear-gradient(to right, var(--c1) 0%, var(--c2) 51%, var(--c1) 100%) !important;
  background-size: 200% auto !important;
  background-position: left center !important;
  background-repeat: no-repeat !important;

  border: none !important;
  border-radius: 10px !important;
  box-shadow: 0 0 20px #aaa !important;
  cursor: pointer !important;
  transition: background-position 0.5s, box-shadow 0.15s, transform 0.15s !important;
}

.btn:visited,
.btn:hover {
  color: #fff !important;
  text-decoration: none !important;
}

.btn:hover {
  background-position: right center !important;
}

.btn:active {
  box-shadow: 0 0 6px #666 !important;
  transform: translateY(2px) !important;
}

.btn:focus-visible {
  outline: 3px solid var(--c2) !important;
  outline-offset: 3px !important;
}

/* Couleurs uniquement */
.btn1 { --c1: #E55D87; --c2: #5FC3E4; }  
.btn2 { --c1: #1A2980; --c2: #26D0CE; }
.btn3 { --c1: #fe8c00; --c2: #f83600; } 

/* ============================================================
   NOTICES DE RAPPEL (préfixe nt-)
   Les cadres prennent la teinte de la notice qui les contient.
   ------------------------------------------------------------
   À AJUSTER : --nt-accent = couleur du bandeau haut de la notice,
               --nt-soft   = couleur de fond de la notice.
   Valeurs par défaut : celles de hugo-theme-learn.
   Adaptez les sélecteurs .notices.tip… au nom de classe que
   génère votre shortcode notice pour le type "tip".
   ============================================================ */
:root {
  --nt-accent: #6AB0DE;   /* notice "note" */
  --nt-soft:   #E7F2FA;
}
.notices.tip, .notice.tip, .notice-tip {
  --nt-accent: #5CB85C;   /* notice "tip" */
  --nt-soft:   #E6F9E6;
}

/* Nuances dérivées, recalculées dans chaque composant
   (une variable dérivée déclarée sur :root ne suivrait pas la notice) */
.nt-box, .nt-card, .nt-units, ol.nt-steps, .nt-ladder, .og-wrap, .og-pill, details.nt-more {
  --nt-fill:   color-mix(in srgb, var(--nt-accent) 20%, var(--nt-soft));  /* fond des cadres : un peu plus foncé que la notice */
  --nt-fill-2: color-mix(in srgb, var(--nt-accent) 35%, var(--nt-soft));  /* fond plus marqué (en-têtes) */
  --nt-line:   var(--nt-accent);                                          /* bords : teinte du bandeau */
  --nt-ink:    color-mix(in srgb, var(--nt-accent) 55%, #000);            /* titres, pastilles : version foncée */
}

/* Couleurs « sémantiques », indépendantes de la notice */
:root {
  --nt-warn: #D9534F;  --nt-warn-ink: #A9302A;   /* pièges, règle */
  --nt-up:   #E8590C;                            /* multiples */
  --nt-ok:   #15803D;                            /* chiffres significatifs */
}

.nt-lead { font-size: 1.05em; line-height: 1.6; }
.nt-subtitle { font-weight: 700; margin: 1.4em 0 0.4em !important; }
.nt-note, .nt-caption { font-size: 0.9em; opacity: 0.85; margin-top: 0.3em !important; }
.nt-scroll { overflow-x: auto; margin: 0.6em 0 1em; -webkit-overflow-scrolling: touch; }

/* --- Échelle des préfixes --- */
.nt-ladder {
  width: 100%; min-width: 520px; margin: 0 !important;
  border-collapse: separate !important; border-spacing: 0 3px !important;
  font-variant-numeric: tabular-nums;
}
.nt-ladder th {
  background: none !important; border: 0 !important;
  padding: 4px 10px !important; font-size: 0.85em; font-weight: 600; opacity: 0.7;
}
.nt-ladder td { background: var(--row-bg) !important; border: 0 !important; padding: 6px 10px !important; }
.nt-ladder tr > td:first-child {
  border-left: 6px solid var(--row-c) !important; border-radius: 6px 0 0 6px;
  text-align: left; font-weight: 700;
}
.nt-ladder tr > td:last-child { border-radius: 0 6px 6px 0; }
.nt-ladder .sym { color: var(--row-c); font-weight: 800; font-size: 1.15em; }
.nt-ladder .lu { font-size: 0.85em; font-style: italic; opacity: 0.8; }
.nt-ladder tr.up   { --row-c: var(--nt-up);  --row-bg: color-mix(in srgb, var(--nt-up) 12%, var(--nt-soft)); }
.nt-ladder tr.down { --row-c: var(--nt-ink); --row-bg: var(--nt-fill); }
.nt-ladder tr.base { --row-c: #888;          --row-bg: color-mix(in srgb, #888 15%, var(--nt-soft)); }
.nt-ladder tr.minor > td:first-child { font-weight: 400; font-style: italic; }
.nt-ladder tr.minor > td { padding-top: 3px !important; padding-bottom: 3px !important; font-size: 0.92em; }
.nt-ladder tr.nt-zone > td,
.nt-ladder tr.nt-zone > td:first-child {
  background: none !important; border-left: 0 !important;
  text-align: left; font-weight: 700; font-size: 0.9em; font-style: normal;
  padding: 10px 4px 2px !important; color: var(--row-c);
}

/* --- Tableau de conversion --- */
.nt-units { margin: 0 auto !important; border-collapse: collapse !important; font-variant-numeric: tabular-nums; }
.nt-units th, .nt-units td { min-width: 3.2em; padding: 6px 10px !important; border: 1px solid var(--nt-line) !important; }
.nt-units th { background: var(--nt-fill) !important; color: var(--nt-ink); }
.nt-units td { font-size: 1.15em; font-weight: 700; background: none !important; }
.nt-units .nt-u0 { background: var(--nt-fill-2) !important; }

/* --- Encadrés --- */
.nt-box {
  border-left: 5px solid var(--bx-line); background: var(--bx-bg);
  border-radius: 0 8px 8px 0; padding: 0.6em 1em; margin: 1em 0;
}
.nt-box p { margin: 0.35em 0 !important; }
.nt-box-title { font-weight: 700; color: var(--bx-ink); }
.nt-box-title i { margin-right: 0.4em; }
.nt-method { --bx-line: var(--nt-line); --bx-bg: var(--nt-fill);   --bx-ink: var(--nt-ink); }
.nt-know   { --bx-line: var(--nt-ink);  --bx-bg: var(--nt-fill-2); --bx-ink: var(--nt-ink);
             border-top: 1px solid var(--nt-line); border-right: 1px solid var(--nt-line); border-bottom: 1px solid var(--nt-line); }
.nt-trap   { --bx-line: var(--nt-warn); --bx-bg: color-mix(in srgb, var(--nt-warn) 12%, var(--nt-soft)); --bx-ink: var(--nt-warn-ink); }
ul.nt-facts { list-style: none !important; padding-left: 0 !important; margin: 0.3em 0 !important; }
ul.nt-facts li { padding: 0.25em 0; }
ul.nt-facts li::before { content: "▸"; color: var(--bx-ink); margin-right: 0.5em; }

/* --- Cartes aires / volumes --- */
.nt-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; margin: 0.8em 0; }
.nt-card {
  border: 1px solid var(--nt-line); border-top: 4px solid var(--nt-ink);
  background: var(--nt-fill); border-radius: 8px; padding: 0.5em 0.9em; overflow-x: auto;
}
.nt-card-title { font-weight: 700; margin: 0.2em 0 0.4em !important; color: var(--nt-ink); }
.nt-card-title i { margin-right: 0.4em; }

/* --- Chiffres significatifs --- */
.nt-cs { width: 100%; min-width: 440px; margin: 0 !important; border-collapse: collapse !important; }
.nt-cs th {
  background: none !important; border: 0 !important;
  border-bottom: 2px solid rgba(128, 128, 128, 0.45) !important;
  font-size: 0.85em; opacity: 0.75; padding: 4px 8px !important;
}
.nt-cs td {
  background: none !important; border: 0 !important;
  border-bottom: 1px solid rgba(128, 128, 128, 0.2) !important; padding: 7px 8px !important;
}
.nt-cs td:last-child { text-align: left; font-size: 0.9em; opacity: 0.85; }
.nt-num { font-size: 1.2em; font-variant-numeric: tabular-nums; letter-spacing: 0.03em; white-space: nowrap; }
.cs-y { color: var(--nt-ok); font-weight: 700; background: rgba(21, 128, 61, 0.12); border-radius: 3px; padding: 0 2px; }
.cs-n { color: #9a9a9a; }
.nt-badge {
  display: inline-block; min-width: 1.8em; padding: 1px 8px; border-radius: 999px;
  background: var(--nt-ok); color: #fff; font-weight: 700; font-size: 0.85em; text-align: center;
}
.nt-badge-min { background: var(--nt-warn); }

/* --- Règle encadrée --- */
.nt-rule {
  max-width: 34em; margin: 1.2em auto; text-align: center;
  border: 3px solid var(--nt-warn); border-radius: 10px; padding: 0.6em 1.2em;
  background: color-mix(in srgb, var(--nt-warn) 10%, var(--nt-soft));
}
.nt-rule p { margin: 0.3em 0 !important; }
.nt-rule-head { font-weight: 700; color: var(--nt-warn-ink); font-size: 0.9em; }
.nt-rule-body { font-size: 1.1em; font-weight: 700; color: var(--nt-warn-ink); }
.nt-rule-why { font-size: 0.9em; font-style: italic; opacity: 0.85; }

/* --- Étapes d'un exemple guidé --- */
ol.nt-steps { counter-reset: ntstep; list-style: none !important; padding-left: 0 !important; margin: 0.8em 0 1em 1em !important; }
ol.nt-steps > li {
  counter-increment: ntstep; position: relative;
  padding: 0 0 0.9em 1.8em; border-left: 2px dashed var(--nt-line);
}
ol.nt-steps > li:last-child { border-left-color: transparent; padding-bottom: 0; }
ol.nt-steps > li::before {
  content: counter(ntstep); position: absolute; left: -1em; top: 0;
  width: 2em; height: 2em; line-height: 2em; border-radius: 50%;
  background: var(--nt-ink); color: #fff; font-weight: 700; text-align: center;
}
ol.nt-steps p { margin: 0.3em 0 !important; }
.nt-step-title { font-weight: 700; }
.nt-result {
  display: inline-block; max-width: 100%; overflow-x: auto; padding: 0.2em 0.9em;
  border: 2px solid var(--nt-ok); border-radius: 6px; background: rgba(21, 128, 61, 0.08);
}
.nt-draft {
  font-family: "Courier New", monospace; padding: 0 0.4em; border-radius: 4px;
  border: 1px dashed rgba(128, 128, 128, 0.6); background: rgba(128, 128, 128, 0.08);
}
ol.nt-steps kbd {
  font-size: 0.85em; padding: 0 0.4em; border: 1px solid rgba(128, 128, 128, 0.5);
  border-bottom-width: 2px; border-radius: 4px;
}

/* --- Ordres de grandeur : barres de seuil --- */
.og-wrap { max-width: 36em; margin: 0.8em auto 1.4em; }
.og-caption { text-align: center; font-size: 0.85em; opacity: 0.7; margin: 0 0 0.3em !important; }
.og-bar { position: relative; display: flex; border-radius: 8px; overflow: hidden; font-size: 0.88em; text-align: center; line-height: 1.4; }
.og-lo, .og-hi { padding: 0.5em 0.4em; color: #fff; }
.og-lo { flex: 4; background: var(--nt-ink); }                                /* de 1 à 5 : 4 unités */
.og-hi { flex: 5; background: linear-gradient(to right, #f83600, #fe8c00); }  /* de 5 à 10 : 5 unités */
.og-bar.og-log .og-lo, .og-bar.og-log .og-hi { flex: 1; }                     /* échelle log : √10 au milieu */
.og-mark { position: absolute; top: 0; bottom: 0; border-left: 2px dashed rgba(255, 255, 255, 0.9); }
.og-ticks { position: relative; height: 1.5em; font-weight: 700; font-size: 0.9em; }
.og-ticks span { position: absolute; top: 0.15em; transform: translateX(-50%); white-space: nowrap; }
.og-ticks .og-t0  { left: 0; transform: none; }
.og-ticks .og-t10 { left: auto; right: 0; transform: none; }
.og-pill { display: inline-block; padding: 0.1em 0.7em; border-radius: 999px; font-weight: 700; }
.og-pill-lo { background: var(--nt-fill); border: 1.5px solid var(--nt-ink); }
.og-pill-hi { background: rgba(254, 140, 0, 0.14); border: 1.5px solid var(--nt-up); }

/* --- Encadré escamotable « pour les curieux » --- */
details.nt-more { margin: 1.2em 0; border: 1.5px solid var(--nt-line); border-radius: 8px; background: var(--nt-fill); }
details.nt-more > summary {
  cursor: pointer; padding: 0.55em 1em; font-weight: 700; color: var(--nt-ink);
  list-style: none; border-radius: 8px;
}
details.nt-more > summary::-webkit-details-marker { display: none; }
details.nt-more > summary::before { content: "▸"; display: inline-block; margin-right: 0.6em; transition: transform 0.2s; }
details.nt-more[open] > summary::before { transform: rotate(90deg); }
details.nt-more[open] > summary { border-bottom: 1px solid var(--nt-line); border-radius: 8px 8px 0 0; }
details.nt-more > summary:focus-visible { outline: 3px solid var(--nt-ink); outline-offset: 2px; }
.nt-more-body { padding: 0.4em 1em 0.8em; }
.nt-more-body p { margin: 0.5em 0 !important; }
@media (prefers-reduced-motion: reduce) { details.nt-more > summary::before { transition: none; } }
</style>

<h1 style="overflow-x:auto;">Automatismes</h1>

Les quiz ci-dessous visent à vérifier ou installer certains automatismes très utiles (voire indispensable) en physique-chimie.

## Jouer avec les relations

<!--<div style="position:relative;margin-left:auto;margin-right:auto;width:100%;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/bandeaurel.png" style="box-shadow:none;background:none;border-radius:3px;">
</div>-->

Les lois consistent en des formules littérales mettant en jeu plusieurs grandeurs (comme $F=G\frac{m_a\times m_B}{d^2}$) et souvent, on se retrouve à vouloir isoler l'une de ces grandeurs ($m_A$ par exemple). Il est donc vital de s'aguerrir dans cet exercice et le quiz suivant permet de tester votre agilité.

Le premier quiz utilise de simples lettres pour que l'on puisse se concentrer sur les manipulations algébriques&nbsp;:

<br>

<a class="btn btn1" href="/quiz-relations.html">Quiz avec lettres simples</a>

<br>

La cible idéale à atteindre est un score de 10/10 en environ une minute.

<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1.5em;">
<img src="/gifyoda.gif" style="box-shadow:none;background:none;border-radius:10px;">
</div>

Lorsqu'on commence à s'aguerrir, on peut passer à ce quiz de même complexité algébrique mais qui utilise cette fois de véritables relations de physique-chimie (ce qui peut rendre les notations beaucoup plus lourdes et donc moins faciles à manipuler mentalement).

<br>

<a class="btn btn2" href="/quiz-relations.html?mode=physique">Quiz avec des vraies relations</a>




## Calculs numériques et écriture d'un résultat

<!--<div style="position:relative;margin-left:auto;margin-right:auto;width:100%;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/bandeaunum.png" style="box-shadow:none;background:none;border-radius:3px;">
</div>-->

Une fois qu'on a déterminé la bonne formule littérale pour la grandeur cherchée, on calcule (on dit qu'on fait l'application numérique). 

Plusieurs difficultés se dressent alors&nbsp;: 
<ul style="margin-top:-0.5em; margin-bottom:1em;">
<li>les mesures doivent être <b>converties</b> pour que les unités «&nbsp;se parlent&nbsp;»,</li>
</ul>

{{%notice type="note" title="Rappels sur les conversions" collapse="true" round="true"%}}

<p class="nt-lead">Un préfixe n'est qu'un <b>facteur multiplicatif</b> collé devant l'unité&nbsp;: «&nbsp;kilo&nbsp;» veut dire «&nbsp;×&nbsp;10<sup>3</sup>&nbsp;», «&nbsp;milli&nbsp;» veut dire «&nbsp;×&nbsp;10<sup>−3</sup>&nbsp;». Convertir, c'est donc <b>remplacer le préfixe par sa puissance de 10</b>.</p>

<div class="nt-scroll">
<table class="nt-ladder">
<thead><tr><th>Préfixe</th><th>Symbole</th><th>Facteur</th><th>Se lit</th><th>Exemple</th></tr></thead>
<tbody>
<tr class="up nt-zone"><td colspan="5"><i class="fa-solid fa-arrow-up"></i>&nbsp; Multiples&nbsp;: unités plus grandes</td></tr>
<tr class="up"><td>péta</td><td class="sym">P</td><td>$10^{15}$</td><td class="lu">million de milliards</td><td>$\pu{1 PV} = \pu{1E15 V}$</td></tr>
<tr class="up"><td>téra</td><td class="sym">T</td><td>$10^{12}$</td><td class="lu">mille milliards</td><td>$\pu{1 Ts} = \pu{1E12 s}$</td></tr>
<tr class="up"><td>giga</td><td class="sym">G</td><td>$10^{9}$</td><td class="lu">milliard</td><td>$\pu{1 GW} = \pu{1E9 W}$</td></tr>
<tr class="up"><td>méga</td><td class="sym">M</td><td>$10^{6}$</td><td class="lu">million</td><td>$\pu{1 MJ} = \pu{1E6 J}$</td></tr>
<tr class="up"><td>kilo</td><td class="sym">k</td><td>$10^{3}$</td><td class="lu">mille</td><td>$\pu{1 kg} = \pu{1E3 g}$</td></tr>
<tr class="up minor"><td>hecto</td><td class="sym">h</td><td>$10^{2}$</td><td class="lu">cent</td><td>$\pu{1 hL} = \pu{1E2 L}$</td></tr>
<tr class="up minor"><td>déca</td><td class="sym">da</td><td>$10^{1}$</td><td class="lu">dix</td><td>$\pu{1 dam} = \pu{1E1 m}$</td></tr>
<tr class="base"><td>(aucun)</td><td class="sym">–</td><td>$10^{0} = 1$</td><td class="lu">un</td><td>unité sans préfixe&nbsp;: m, g, L, s…</td></tr>
<tr class="down minor"><td>déci</td><td class="sym">d</td><td>$10^{-1}$</td><td class="lu">dixième</td><td>$\pu{1 dL} = \pu{1E-1 L}$</td></tr>
<tr class="down minor"><td>centi</td><td class="sym">c</td><td>$10^{-2}$</td><td class="lu">centième</td><td>$\pu{1 cm} = \pu{1E-2 m}$</td></tr>
<tr class="down"><td>milli</td><td class="sym">m</td><td>$10^{-3}$</td><td class="lu">millième</td><td>$\pu{1 ms} = \pu{1E-3 s}$</td></tr>
<tr class="down"><td>micro</td><td class="sym">µ</td><td>$10^{-6}$</td><td class="lu">millionième</td><td>$1\,$µ$\mathrm{W} = \pu{1E-6 W}$</td></tr>
<tr class="down"><td>nano</td><td class="sym">n</td><td>$10^{-9}$</td><td class="lu">milliardième</td><td>$\pu{1 ng} = \pu{1E-9 g}$</td></tr>
<tr class="down"><td>pico</td><td class="sym">p</td><td>$10^{-12}$</td><td class="lu">millième de milliardième</td><td>$\pu{1 pJ} = \pu{1E-12 J}$</td></tr>
<tr class="down"><td>femto</td><td class="sym">f</td><td>$10^{-15}$</td><td class="lu">millionième de milliardième</td><td>$\pu{1 fm} = \pu{1E-15 m}$</td></tr>
<tr class="down nt-zone"><td colspan="5"><i class="fa-solid fa-arrow-down"></i>&nbsp; Sous-multiples&nbsp;: unités plus petites</td></tr>
</tbody>
</table>
</div>

<p class="nt-note">Les préfixes en gras vont de mille en mille (puissances de 10 multiples de 3)&nbsp;: ce sont les plus utilisés en sciences. Hecto, déca, déci et centi, en italique, servent surtout dans la vie courante (hL, cL, cm…).</p>

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-lightbulb"></i>La méthode&nbsp;: remplacer le préfixe</p>
<p>$\pu{4,7 km} = 4{,}7\times 10^{3}\ \mathrm{m} = \pu{4,7E3 m}$</p>
<p>$\pu{250 mL} = 250\times 10^{-3}\ \mathrm{L} = \pu{0,250 L}$</p>
<p>Dans l'autre sens, on fait apparaître la puissance de 10 du préfixe voulu&nbsp;:<br>$\pu{5,8E-7 m} = 580\times 10^{-9}\ \mathrm{m} = \pu{580 nm}$</p>
</div>

<p class="nt-subtitle">Le tableau de conversion des litres</p>

<div class="nt-scroll">
<table class="nt-units">
<thead><tr><th>hL</th><th>daL</th><th class="nt-u0">L</th><th>dL</th><th>cL</th><th>mL</th></tr></thead>
<tbody><tr><td></td><td></td><td class="nt-u0">1</td><td>0</td><td>0</td><td>0</td></tr></tbody>
</table>
</div>

<p class="nt-caption" style="text-align:center;">Chaque colonne vers la droite correspond à un facteur 10. On lit&nbsp;: $\pu{1 L = 10 dL = 100 cL = 1000 mL}$, et de même $\pu{1 hL = 100 L}$.</p>

<p class="nt-subtitle">Aires et volumes&nbsp;: attention aux exposants</p>

<div class="nt-grid">
<div class="nt-card">
<p class="nt-card-title"><i class="fa-regular fa-square"></i>Aires&nbsp;: on élève au carré</p>
<p>$\begin{aligned}\pu{1 dm2} &= \pu{1 dm}\times\pu{1 dm}\\ &= \pu{10^2 mm}\times\pu{10^2 mm}\\ &= \left(10^2\right)^2\ \pu{mm2}\\ &= \pu{1E4 mm2}\end{aligned}$</p>
</div>
<div class="nt-card">
<p class="nt-card-title"><i class="fa-solid fa-cube"></i>Volumes&nbsp;: on élève au cube</p>
<p>$\begin{aligned}\pu{1 dm3} &= \pu{1 dm}\times\pu{1 dm}\times\pu{1 dm}\\ &= \pu{10^2 mm}\times\pu{10^2 mm}\times\pu{10^2 mm}\\ &= \left(10^2\right)^3\ \pu{mm3}\\ &= \pu{1E6 mm3}\end{aligned}$</p>
</div>
</div>

<p class="nt-note">L'idée&nbsp;: entre dm et mm, les longueurs sont multipliées par $10^2$. Une aire étant une longueur × une longueur, elle est multipliée par $\left(10^2\right)^2$&nbsp;; un volume (longueur × longueur × longueur) par $\left(10^2\right)^3$.</p>

<div class="nt-box nt-trap">
<p class="nt-box-title"><i class="fa-solid fa-triangle-exclamation"></i>Piège classique</p>
<p>$\pu{1 m2}$ ne vaut pas $\pu{100 cm2}$&nbsp;! Le facteur $10^2$ des longueurs doit être élevé au carré&nbsp;: $\pu{1 m2} = \left(10^2\right)^2\ \pu{cm2} = \pu{1E4 cm2}$.</p>
</div>

<div class="nt-box nt-know">
<p class="nt-box-title"><i class="fa-solid fa-thumbtack"></i>À savoir par cœur</p>
<ul class="nt-facts">
<li>$\pu{1 L} = \pu{1 dm3}$, et donc (en divisant par 1000) $\pu{1 mL} = \pu{1 cm3}$.</li>
<li>Un <b>are</b> est l'aire d'un carré de $\pu{10 m}$ de côté&nbsp;: $\pu{1 a} = \pu{10 m}\times\pu{10 m} = \pu{1E2 m2}$.</li>
<li>Un <b>hectare</b> vaut 100 ares, soit un carré de $\pu{100 m}$ de côté&nbsp;: $\pu{1 ha} = \pu{100 m}\times\pu{100 m} = \pu{1E4 m2}$.</li>
</ul>
</div>

{{%/notice%}}

<ul>
<li>le nombre de <b>chiffres significatifs</b> doit témoigner fidèlement de la précision des mesures,</li>
</ul>

{{%notice type="note" title="Règle pour les chiffres significatifs" collapse="true" round="true"%}}

<p class="nt-lead">Écrire $\pu{3,50 kg}$ plutôt que $\pu{3,5 kg}$ n'est pas un détail&nbsp;: le zéro final affirme que la masse est connue au centième de kilogramme près. Le nombre de chiffres significatifs <b>raconte la précision</b> de la mesure.</p>

<div class="nt-box nt-method">
<p class="nt-box-title"><i class="fa-solid fa-magnifying-glass"></i>Comment les compter</p>
<p>On compte tous les chiffres à partir du <b>premier chiffre non nul</b> en partant de la gauche. Les zéros de gauche ne comptent pas (ils ne servent qu'à placer la virgule)&nbsp;; ceux du milieu et de droite comptent.</p>
<p><span class="cs-y">vert</span>&nbsp;: compte &nbsp;&nbsp;&nbsp; <span class="cs-n">gris</span>&nbsp;: ne compte pas</p>
</div>

<div class="nt-scroll">
<table class="nt-cs">
<thead><tr><th>Nombre</th><th>Chiffres significatifs</th><th>À retenir</th></tr></thead>
<tbody>
<tr><td class="nt-num"><span class="cs-n">0,000</span><span class="cs-y">123000</span></td><td><span class="nt-badge">6</span></td><td>les zéros de droite comptent</td></tr>
<tr><td class="nt-num"><span class="cs-y">3,50</span></td><td><span class="nt-badge">3</span></td><td>précis au centième près</td></tr>
<tr><td class="nt-num"><span class="cs-n">0,00</span><span class="cs-y">87</span></td><td><span class="nt-badge">2</span></td><td>les zéros de gauche ne comptent pas</td></tr>
<tr><td class="nt-num"><span class="cs-y">205</span></td><td><span class="nt-badge">3</span></td><td>un zéro «&nbsp;coincé&nbsp;» entre deux chiffres compte</td></tr>
<tr><td class="nt-num"><span class="cs-y">1,20</span><span class="cs-n">&nbsp;×&nbsp;10<sup>3</sup></span></td><td><span class="nt-badge">3</span></td><td>la puissance de 10 ne compte pas</td></tr>
</tbody>
</table>
</div>

<div class="nt-rule">
<p class="nt-rule-head"><i class="fa-solid fa-scale-balanced"></i>&nbsp; Calcul ne contenant que des multiplications et des divisions</p>
<p class="nt-rule-body">On garde dans le résultat autant de chiffres significatifs que la mesure qui en contient le moins.</p>
<p class="nt-rule-why">Un calcul ne peut pas être plus précis que sa donnée la moins précise&nbsp;: c'est le maillon faible qui décide.</p>
</div>

<p class="nt-subtitle">Exemple guidé&nbsp;: une énergie cinétique</p>

<ol class="nt-steps">
<li>
<p class="nt-step-title">Repérer la précision des données</p>
<p>$m = \pu{3,50 kg}$ &nbsp;<span class="nt-badge">3</span> &nbsp;&nbsp;&nbsp; $v = \pu{2,3 m*s-1}$ &nbsp;<span class="nt-badge nt-badge-min">2</span></p>
<p>C'est la vitesse, la moins précise, qui impose <b>2 chiffres significatifs</b> au résultat.</p>
</li>
<li>
<p class="nt-step-title">Calculer sans arrondir en cours de route</p>
<p>On tape le calcul d'une seule traite. La calculatrice affiche <span class="nt-draft">9,2575</span>&nbsp;: cette valeur reste au brouillon, elle ne s'écrit pas sur la copie.</p>
<p class="nt-note">Si le calcul se fait en plusieurs étapes, on réutilise les résultats intermédiaires non arrondis (touche <kbd>Ans</kbd> ou mémoire de la calculatrice) au lieu de retaper des valeurs arrondies&nbsp;: chaque arrondi ajoute une petite erreur, et ces erreurs s'accumulent.</p>
</li>
<li>
<p class="nt-step-title">Écrire le résultat arrondi sur la copie</p>
<p><span class="nt-result">$E_c = \tfrac 12\, m\times v^2 = \tfrac 12 \times 3{,}50\times 2{,}3^2 = \pu{9,3 J}$</span></p>
</li>
</ol>

<div class="nt-box nt-trap">
<p class="nt-box-title"><i class="fa-solid fa-bomb"></i>Attention au facteur ½</p>
<p>Le $2$ de $\frac 12$ n'est pas une mesure mais un coefficient mathématique exact. Son nombre de chiffres significatifs est infini (c'est $2{,}00000\ldots$)&nbsp;: il ne limite jamais la précision du résultat.</p>
</div>

{{< youtube-plus id="KOvHirpl7vk" ratio="16x9" width="100%" shadow=true rounded=true >}}
{{%/notice%}}

<ul>
<li>et pour que le résultat soit le plus lisible possible, on utilise la <b>notation scientifique</b>.
</li>
</ul>

{{%notice type="note" title="Vidéos sur la notation scientifique et les ordres de grandeur" collapse="true" round="true"%}}

{{< youtube-plus id="bBT1hOYQPnY" ratio="4x3" width="100%" shadow=true rounded=true >}}

{{< youtube-plus id="PtftD6sU-Sc" ratio="16x9" width="100%" shadow=true rounded=true >}}

{{%/notice%}}


Le quiz ci-dessous permet de s'auto-diagnostiquer et de s'entraîner pour améliorer sa maîtrise. Le test se concentre sur&nbsp;: 
<ul style="margin-top:-0.5em; margin-bottom:1em;">
<li>les puissances de 10 et les ordres de grandeur,</li>
</ul>

{{%notice type="tip"  title="Définition des ordres de grandeur en physique" round="true" collapse="true"%}}

<p class="nt-lead">L'ordre de grandeur d'un nombre est une puissance de 10 qui en donne une idée «&nbsp;à la louche&nbsp;». Il permet de comparer d'un coup d'œil des grandeurs très différentes, de la taille d'un atome à celle d'une galaxie.</p>

<p class="nt-subtitle">La méthode</p>

<ol class="nt-steps">
<li>
<p class="nt-step-title">Écrire le nombre en notation scientifique</p>
<p>$a\times 10^{n}$, avec $1 \leqslant a < 10$ et $n$ entier.</p>
</li>
<li>
<p class="nt-step-title">Comparer $a$ à 5</p>
<p>Si $a < 5$, l'ordre de grandeur est $10^{n}$. Si $a \geqslant 5$, c'est la puissance suivante&nbsp;: $10^{n+1}$.</p>
</li>
</ol>

<div class="og-wrap">
<p class="og-caption">valeur de $a$</p>
<div class="og-bar">
<div class="og-lo">$1 \leqslant a < 5$<br>ordre de grandeur&nbsp;: $10^{n}$</div>
<div class="og-hi">$5 \leqslant a < 10$<br>ordre de grandeur&nbsp;: $10^{n+1}$</div>
</div>
<div class="og-ticks"><span class="og-t0">1</span><span style="left:44.44%;">5</span><span class="og-t10">10</span></div>
</div>

<p class="nt-subtitle">Exemples</p>

<div class="nt-scroll">
<table class="nt-cs">
<thead><tr><th>Nombre</th><th>Notation scientifique</th><th>Comparaison</th><th>Ordre de grandeur</th></tr></thead>
<tbody>
<tr><td class="nt-num">$499$</td><td>$4{,}99\times 10^{2}$</td><td>$4{,}99 < 5$</td><td><span class="og-pill og-pill-lo">$10^{2}$</span></td></tr>
<tr><td class="nt-num">$500$</td><td>$5{,}00\times 10^{2}$</td><td>$5{,}00 \geqslant 5$</td><td><span class="og-pill og-pill-hi">$10^{3}$</span></td></tr>
<tr><td class="nt-num">$0{,}0087$</td><td>$8{,}7\times 10^{-3}$</td><td>$8{,}7 \geqslant 5$</td><td><span class="og-pill og-pill-hi">$10^{-2}$</span></td></tr>
<tr><td class="nt-num">$\pu{6371 km}$<br><span class="nt-note">rayon de la Terre</span></td><td>$\pu{6,371E6 m}$</td><td>$6{,}371 \geqslant 5$</td><td><span class="og-pill og-pill-hi">$\pu{1E7 m}$</span></td></tr>
</tbody>
</table>
</div>

<div class="nt-box nt-trap">
<p class="nt-box-title"><i class="fa-solid fa-triangle-exclamation"></i>Avec les puissances négatives</p>
<p>«&nbsp;La puissance suivante&nbsp;» de $10^{-3}$ est $10^{-2}$ (car $-3+1=-2$), et non $10^{-4}$. On monte toujours vers le plus grand.</p>
</div>

<details class="nt-more">
<summary><i class="fa-solid fa-ruler-horizontal"></i>&nbsp; Pour les curieux&nbsp;: pourquoi les physiciens choisissent plutôt le seuil $\sqrt{10}\approx 3{,}16$</summary>
<div class="nt-more-body">
<p>Le seuil 5 est une <b>convention</b>&nbsp;: elle est pratique, mais elle ne correspond pas tout à fait à l'idée de «&nbsp;puissance de 10 la plus proche&nbsp;» telle qu'un physicien la conçoit.</p>
<p><b>Comparer avec des rapports, pas avec des différences</b><br>
Quand on dit que deux grandeurs diffèrent de deux ordres de grandeur, on veut dire que l'une est environ 100 fois plus grande que l'autre. On raisonne en «&nbsp;combien de fois plus&nbsp;», pas en «&nbsp;combien de plus&nbsp;». Prenons 400&nbsp;: il est 4 fois plus grand que 100, mais seulement 2,5 fois plus petit que 1000. En ce sens, 400 est plus proche de $10^3$ que de $10^2$&nbsp;!</p>
<p><b>Le milieu «&nbsp;multiplicatif&nbsp;»</b><br>
Cherchons le nombre $m$ situé à égale distance de 1 et de 10 dans ce sens-là&nbsp;: il faut multiplier par le même facteur pour passer de 1 à $m$ que pour passer de $m$ à 10.</p>
<p style="text-align:center;">$\dfrac{m}{1} = \dfrac{10}{m} \iff m^2 = 10 \iff m = \sqrt{10} \approx 3{,}16 \quad (\text{car } m > 0)$</p>
<p><b>Ce que ça donne sur une échelle logarithmique</b><br>
Sur une échelle où chaque facteur 10 occupe la même longueur (comme l'axe d'un graphique semi-logarithmique), $\sqrt{10}$ tombe pile au milieu, et 5 se retrouve nettement au-delà&nbsp;:</p>
<div class="og-wrap">
<div class="og-bar og-log">
<div class="og-lo">$a < \sqrt{10}$<br>$\to 10^{n}$</div>
<div class="og-hi">$a \geqslant \sqrt{10}$<br>$\to 10^{n+1}$</div>
<span class="og-mark" style="left:69.9%;"></span>
</div>
<div class="og-ticks"><span class="og-t0">1</span><span style="left:30.1%;">2</span><span style="left:50%;">$\sqrt{10}$</span><span style="left:69.9%;">5</span><span class="og-t10">10</span></div>
<p class="og-caption">valeur de $a$ sur une échelle logarithmique (pointillés&nbsp;: le seuil 5)</p>
</div>
<p><b>Lien avec le logarithme décimal</b> (celui du pH, en terminale). Cette convention revient à arrondir $\log x$ à l'entier le plus proche&nbsp;: l'ordre de grandeur de $x$ est $10^{k}$, où $k$ est l'entier le plus proche de $\log x$. Par exemple, $\log 400 \approx 2{,}60$, dont l'entier le plus proche est 3&nbsp;: l'ordre de grandeur est $10^3$.</p>
<p><b>En pratique.</b> Les deux conventions ne diffèrent que lorsque $a$ est compris entre $3{,}16$ et $5$, ce qui ne change pas grand-chose pour une estimation. Dans ce cours et dans les quiz, on utilise le seuil 5.</p>
</div>
</details>

{{%/notice%}}


<ul>
<li>les conversions,</li>
<li>et la notation scientifique.</li>
</ul>



<br>

<a class="btn btn3" href="/quiz-automatismes.html">Diagnostic + entraînement</a>

<br>
