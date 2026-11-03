# Consignes pour Claude

Site Hugo (thème `learn`) de cours de physique-chimie de Marc, publié depuis `main`.
Les pages de cours sont dans `content/<niveau>/cours/*.md` (`2nde`, `1spe`, `Tspe`…).

## 0. Fonctionnement

- Écrire à Marc en français.
- Commiter et pousser directement sur `main`, sauf demande contraire.
- Hugo n'est pas installé dans l'environnement cloud. Pour vérifier une animation, extraire le bloc HTML et le `<script>` de la page dans un fichier d'aperçu (avec `static/css/cours.css`) et le capturer avec Playwright, en largeur ordinateur **et** téléphone (≈ 340 px).

## 1. Objectif et principes (conversion diaporama reveal-hugo → page web)

- Les diaporamas servent à la **découverte** en classe ; la page web est la **synthèse** pour comprendre finement et réviser.
- Garder la structure et la formulation de Marc. Ne reformuler que pour corriger une erreur, mais ajouter des explications, des exemples et des précisions. Périmètre : le programme officiel et le bac ; des « Pour aller plus loin » sont bienvenus.
- **Signaler** toute erreur trouvée dans les diapositives (physique, historique, notation, signe), la corriger dans la page et l'expliquer dans la réponse.
- Les notes de présentation (`{{%note%}}`) deviennent souvent des « Pour aller plus loin » ou des réponses rédigées.
- Chaque question des diapositives reçoit une réponse rédigée, dans un repliable.
- Livrer la page complète, **testée dans un navigateur** (aucune erreur JavaScript, captures vérifiées).

## 2. Travail sur les versions de Marc

- Quand Marc fournit son fichier de travail, **repartir de lui** : comparer avec la version précédente, conserver toutes ses modifications (ajouts, suppressions, styles) et ne rien réintroduire de ce qu'il a retiré.
- Vérifier, module par module, s'il a touché au script avant de le remplacer.
- Ne pas reformater ce qui n'est pas demandé.

## 3. Structure d'une page

```
+++
title = "…"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style> … seulement les règles propres à la page … </style>

<div class="nt-quizbar"> … bouton « Mode révision » … </div>

## Titre de partie {.nt-h2}
### Sous-partie {.nt-h3}
#### Intertitre {.nt-h4}      (style .nt-h4 défini dans la page si besoin)

… contenu …

<script> … tout le JavaScript de la page, dans une IIFE … </script>
```

- Styles et scripts communs : `static/css/cours.css` et `static/js/cours.js` (la version du dépôt fait foi). Une règle utile à plusieurs pages va dans `cours.css`, pas dans le `<style>` d'une page.
- Dans un titre, écrire les accolades littérales en entités : `&#123;Terre, atmosphère&#125;`.
- Pas de ligne vide à l'intérieur d'un bloc HTML (`div`, `details`, `table`…) : Hugo repasserait en Markdown.
- Mots-clés à retrouver en mode révision : `<span class="imp nt-hole">…</span>` ; mot-clé simplement mis en valeur : `<span class="imp">…</span>`.

## 4. Les encadrés (`cours.css`)

| Rôle | Code |
|---|---|
| Définition | `<div class="nt-b nt-def">` + `<p class="nt-tag"><i class="fa-solid fa-book-open"></i>…</p>` |
| À retenir | `nt-b nt-prop` (icône `fa-star`) |
| Formule | `<div class="nt-f">` avec `nt-f-math` et `nt-f-units` |
| Attention | `nt-b nt-warn` (icône `fa-triangle-exclamation`) |
| Exemple, à savoir | `nt-b nt-ex` (icône `fa-lightbulb`) |
| Remarque, démonstration | `nt-b nt-demo-box` (icônes `fa-eye`, `fa-list-check`) |
| Question | `nt-b nt-ask` (icône `fa-circle-question`), suivie de `<details class="nt-d nt-rep">` |
| Pour aller plus loin | `<details class="nt-d nt-plus">` (icône `fa-rocket`) |
| Protocole | `nt-b nt-proto`, gestes utiles en `nt-ece` ; en **seconde**, ajouter `nt-sans-ece` (pas d'étiquette ECE) |
| Animation, quiz, entraînement | `<div class="nt-lab" id="lab-…">` (`nt-quizlab`, `nt-trainer`) |

- Démonstrations : listes `<ol class="nt-steps">`.
- Tableaux : `<div class="nt-scroll"><table class="nt-t">` (`nt-t-egal` si aucune colonne n'est une colonne d'en-tête).
- Champs de saisie compacts, unité collée : `<span class="nt-champ"><label>…</label><input type="text"><span class="nt-u">mL</span></span>` (style commun dans `cours.css` ; `class="nt-large"` sur l'`input` pour un champ de texte long).

## 5. Médias

- **Règle générale : ne pas intégrer les images des diapositives.** Marc efface la plupart de celles qui sont intégrées. On redessine en SVG ce qui est utile à la compréhension (schémas, graphiques), on remplace un graphique par une animation quand c'est pertinent, et l'on décrit ou l'on supprime une question qui reposait sur une image.
- Exception rare, à justifier : une image vraiment irremplaçable. Elle est alors hébergée sur `https://presentationssite.github.io/<fichier>`.
- Images et vidéos avec légende : `style="margin-top:0.5em; margin-bottom:0;"` sur l'image ou la vidéo.
- YouTube : `{{< youtube-plus id="…" ratio="16x9" width="500" shadow=true rounded=true >}}`, intégré directement plutôt qu'en lien. Dans un bloc HTML, pas de ligne vide autour.
- Vidéo locale ou animation eduMedia : `<div class="nt-embed"><video …></video></div>` ou `<div class="nt-embed"><iframe …></iframe></div>` (style commun dans `cours.css` ; iframe au format 5:4 par défaut, variantes `nt-169`, `nt-large`, `nt-bandeau`). GeoGebra : plutôt en lien.

## 6. LaTeX (MathJax)

- Unités avec `\pu{…}` : `\pu{6,63E-34 J*s}`, `\pu{W*m-2*K-4}`.
- Couleur : `\color` est un interrupteur. Toujours isoler : `{\color{#E11D48}{i(t)}}`, ou `\textcolor{#E11D48}{i(t)}`.
- `\Leftrightarrow` seulement pour de vraies équivalences ; « donc » pour une déduction (notamment après une dérivation). Dans un `array`, autant de colonnes déclarées que de cellules (ou `aligned`).
- Température en degrés Celsius notée θ ; T réservée aux kelvins.

## 7. Schémas et animations

- Couleurs harmonieuses, bleu dominant (en-tête du thème) ; traits fins ; étiquettes sobres. Palette : variables de `:root` dans `cours.css`.
- **Personnages** : toujours dessinés en **bonhomme fil de fer** (traits gris `#94A3B8`, tête en disque plein, pas de vêtements ni de couleur de peau), y compris quand le reste de la scène est détaillé.
- **Légendes** : le moins possible. Ne pas nommer ce qui se reconnaît (« wagon », « sol »…) ; garder seulement les étiquettes indispensables (grandeurs et appareils d'un montage, vecteurs, axes).
- Dans les dessins, pas d'effet décoratif qui n'apporte rien à la physique (par exemple une ombre sous un objet).
- **Aucun texte coupé** par un trait : décaler l'étiquette, ou la poser sur une pastille de fond.
- Sur fond sombre : texte sans halo blanc (ou halo sombre).
- Fonction d'écriture sur canvas : `save()` / `restore()` autour du halo, sinon les tracés suivants héritent de la couleur blanche (grilles invisibles).
- Électricité : moteur `circ.js` (`CI.wire`, `CI.res`, `CI.cap`, `CI.gen`, `CI.src`, `CI.pv`, `CI.pile`, `CI.npn`, `CI.ldr`, `CI.led`, `CI.therm`, `CI.meter`, `CI.inter`, `CI.inter2`, `CI.iarr`, `CI.uarr`, `CI.qty`…), inclus dans le script des pages qui l'utilisent (exemples : `content/Tspe/cours/rc.md`, `content/2nde/cours/elec.md`).
  - Fils jusqu'aux appareils, sans rectangle blanc qui jure sur fond coloré.
  - Convention récepteur ; en décharge d'un condensateur, `i` orienté vers l'armature qui porte `q`.
  - Thermistance : diagonale terminée par un petit segment à chaque bout.
- Photons : onde dont l'amplitude s'annule aux extrémités, pointe dans l'axe.
- Canvas : résolution de l'écran (`devicePixelRatio`), redessin au redimensionnement, animation suspendue hors écran, respect de « réduire les animations », mise en page adaptée au téléphone.
- Graphiques : quadrillage fin plus quadrillage principal ; constructions (tangente, asymptote, 63 %…) en pointillés ; étiquettes sur pastilles.
- Modèles physiques **vérifiés numériquement** (ordres de grandeur, conservation, valeurs calées sur les diapositives).
- Animations guidées « étape par étape » quand une démarche s'y prête (exemple : dosage par étalonnage, solution trop concentrée → extrapolation dangereuse → dilution → lecture graphique → régression).
- En cas d'erreur de l'élève : afficher la correction, et proposer un bouton (« Préparer le tube avec les bons volumes ») plutôt que de lancer l'animation automatiquement.

## 8. Quiz et entraînements

- Quiz : questions mélangées, correction expliquée, score, bilan.
- Entraînements : 6 questions tirées au hasard, valeurs aléatoires, tolérance de 2 à 3 %, correction détaillée avec le calcul.

Interface commune (mise au point pour `2nde/cours/atome.md`, puis reprise dans `melanges.md`) ; ses styles (`.nt-prog`, `.nt-qnum`, `.nt-qcard`, `.nt-qvis`, `.nt-choix`, `.nt-fb`, `.nt-big-score`) sont dans `cours.css`, et `cours.js` met en forme le bilan :

- « Question k sur N » au-dessus d'une rangée de pastilles : grise à venir, verte si juste, rouge si faux, la question en cours entourée de bleu.
- La question et les boutons de réponse dans une carte (`.nt-qcard`).
- Grands boutons arrondis (`.nt-choix`), qui se soulèvent au survol. Après la réponse, le choix fait est coloré (vert ou rouge) et, en cas d'erreur, la bonne réponse est surlignée en vert.
- La correction dans un cadre coloré (`.nt-msg.nt-fb.ok` ou `.ko`), avec une bordure à gauche.
- Pour un entraînement, l'objet de la question (une écriture de noyau, une formule…) est affiché en grand dans la carte (`.nt-qvis`).
- Le contenu des questions et des corrections ne change pas.

```html
<div class="nt-lab nt-quizlab" id="quiz-…">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">…</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next">…</button></div>
</div>
```

Côté script : tenir un tableau `res` (vrai, faux ou vide pour chaque question), redessiner les pastilles et le numéro après chaque réponse et à chaque nouvelle question ; donner aux boutons la classe `nt-choix`, puis `nt-choix-ok` ou `nt-choix-ko` ; mettre la correction dans `msg` avec la classe `nt-msg nt-fb ok` ou `ko`, et la remettre à `nt-msg` pour la question suivante. Les modules de `melanges.md` (choix communs à toutes les questions) et d'`atome.md` (choix propres à chaque question) servent de modèles.

## 9. Niveaux

- **Seconde** : pas d'étiquette ECE ; unités simples (g/L, mg/L), exposants négatifs évités en début d'année.
- **Spécialité de première et de terminale** : étiquette ECE ; préciser ce qui est fourni ou à connaître au bac (par exemple $R_\text{th} = \Delta T/\Phi$ à connaître ; loi de Newton, loi de Stefan-Boltzmann et $R_\text{th} = e/(\lambda S)$ fournies ; notice toujours fournie aux ECE).

## 10. Moteurs de dessin (archive `moteurs.zip`, hors dépôt : la demander à Marc)

| Fichier | Rôle | Utilisation |
|---|---|---|
| `circ.js` | schémas électriques en SVG | inclus dans le script de la page ; `CI.svg(largeur, hauteur, contenu, description, classe)` assemble le schéma |
| `chem.py` | formules de molécules en SVG (Python, avec RDKit) | `m = mol('CCO')`, puis `orient(m, …)` ou `tree_coords(m)` pour une chaîne en zigzag droit ; `topsvg(m)` pour la formule topologique, `semisvg(m)` pour la semi-développée ; options : couleurs de liaisons et d'atomes, numérotation (`notes`), étiquettes |
| `lewis.py` | schémas de Lewis en SVG | `lewis(atomes, liaisons)` ; doublets non liants placés comme des domaines électroniques, charges entourées |
| `chem.py` → `model3d()` | coordonnées 3D optimisées | `model3d('CCO')` renvoie atomes et liaisons, au format de la visionneuse |
| `mol3d.js` | visionneuse 3D (boules et bâtons, rotation au doigt) | dans le script de la page, en remplaçant `@@MODELS@@` par le JSON de `model3d()` ; dans la page : `<div class="nt-mol3d" data-mol="ethanol">` |

Conventions des molécules : traits fins (1 px), chaînes en zigzag droit (non penché), numérotation petite et grise, lettres des hétéroatomes petites et colorées (O rouge, N bleu…), même espacement des doubles liaisons dans tous les dessins.

## 11. Avancement

- Terminale spécialité : tous les cours sont convertis.
- Seconde : électricité, mélanges, solutions… déjà convertis ; restent de nombreux cours de seconde et de première spécialité (vérifier dans `content/` ce qui existe déjà).
