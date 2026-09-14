# Fenêtres de code exécutable pour Hugo (façon Trinket)

Intègre dans ton site Hugo des fenêtres de code **Python** et **VPython (GlowScript)**
qui s'exécutent dans le navigateur — sans serveur, sans base de données, sans le
stack trinket-oss complet. Tout repose sur deux moteurs *côté client* :

- **Python** → [Skulpt](https://skulpt.org) (le moteur qu'utilisait Trinket)
- **VPython** → la chaîne [GlowScript](https://github.com/vpython/glowscript)
  (compilateur RapydScript + runtime WebGL), reproduite à partir du mécanisme
  officiel `GlowScriptOffline`.

Un shortcode `runpython` génère une `<iframe>` légère pointant vers un *player*
autonome (`player.html`) ; le code lui est transmis par `postMessage`.

---

## Arborescence

```
ton-site-hugo/
├── layouts/shortcodes/runpython.html        ← le shortcode
├── static/
│   ├── trinket/
│   │   ├── player.html                       ← le moteur d'exécution
│   │   ├── skulpt_libraries/                  ← (recommandé) Skulpt en local (voir §2)
│   │   └── glowscript_libraries/             ← À AJOUTER pour VPython (voir §3)
│   └── programmes/                           ← tes "gros" programmes .py
│       ├── rebond.py
│       └── spirale.py
└── content/exemples/demo.md                  ← page de démonstration
```

## Installation

### 1. Copier les deux fichiers de base
Copie `layouts/shortcodes/runpython.html` et `static/trinket/player.html`
dans ton projet (mêmes chemins).

### 2. Python : fonctionne tout de suite (mais auto-héberge Skulpt)
Par défaut, le player essaie d'abord une copie **locale** de Skulpt, puis
retombe sur un **CDN** en secours. Sans rien faire, ça marche tant que le CDN
est joignable.

⚠️ **Fortement recommandé** : dépose les deux fichiers de Skulpt dans
`static/trinket/skulpt_libraries/` (voir le `_LIRE_MOI.txt` qui s'y trouve) :

```
skulpt_libraries/
├── skulpt.min.js
└── skulpt-stdlib.js
```

Sinon, sur un réseau d'établissement qui bloque ou ralentit le CDN, on obtient
un long écran blanc puis « Échec du chargement : …skulpt.min.js ». En local,
le Python fonctionne même hors-ligne et derrière un proxy. Téléchargement :
les mêmes fichiers que le CDN (`…/gh/Tezumie/Skulpt-CDN@latest/…`) ou l'archive
*skulpt-dist* officielle (https://skulpt.org/using.html).

### 3. VPython : ajouter les bibliothèques GlowScript (obligatoire)
GlowScript n'a pas de CDN officiel, il faut l'auto-héberger (c'est aussi plus
robuste — l'objectif est justement de ne plus dépendre d'un service tiers).

1. Va sur https://github.com/vpython/glowscript et télécharge
   **`GlowScriptOffline3.2.zip`** (à la racine du dépôt).
2. Dézippe-le. À l'intérieur se trouve un dossier `glowscript_libraries/`.
3. Copie-le dans `static/trinket/glowscript_libraries/`.

Fichiers réellement utilisés par le player (tu peux ne garder que ceux-là) :

```
glowscript_libraries/
├── jquery.min.js
├── jquery-ui.custom.min.js
├── jquery-ui.custom.css
├── ide.css
├── RSrun.3.2.min.js
├── glow.3.2.min.js
├── RScompiler.3.2.min.js
├── Roboto_Medium_ttf_sans.js          (texte 3D)
└── NimbusRomNo9L_Med_otf_serif.js     (texte 3D)
```

> Si la version GlowScript change un jour (ex. 3.3), mets à jour `gsVersion`
> en haut de `player.html` et le nom des fichiers `*.3.x.min.js`.

#### Faire cohabiter plusieurs versions (ex. 3.1 et 3.2)

Certains programmes écrits pour une version précise ne tournent correctement
qu'avec celle-ci. Le cas classique : une animation **lancée depuis un menu ou un
bouton** (et non depuis une boucle principale) — la 3.2 a modifié la façon dont
le compilateur insère `async`/`await`, et un tel programme écrit pour la 3.1 peut
voir son compteur défiler **sans que rien ne bouge** en 3.2.

Pour faire tourner un programme dans sa version d'origine, ajoute les trois
fichiers versionnés correspondants à côté des autres, puis utilise
`version="…"` dans le shortcode. Pour la 3.1 :

```
glowscript_libraries/
├── glow.3.1.min.js
├── RScompiler.3.1.min.js
└── RSrun.3.1.min.js
```

Téléchargeables sur `https://www.glowscript.org/package/glow.3.1.min.js`
(et `RScompiler.3.1.min.js`, `RSrun.3.1.min.js`), ou sur le miroir GitHub
`https://raw.githubusercontent.com/vpython/glowscript/master/package/glow.3.1.min.js`.
Les fichiers jQuery, polices et CSS sont communs à toutes les versions.

Le shortcode devient alors :

```
{{< runpython lang="vpython" file="tris.py" version="3.1" />}}
```

Le player charge alors le compilateur et le runtime 3.1 pour cette fenêtre,
et ne réécrit pas l'en-tête en 3.2. Les autres fenêtres restent en 3.2.

### 4. (Optionnel) Auto-héberger aussi CodeMirror
En haut de `player.html`, l'objet `LIBS` centralise toutes les URLs.
**Skulpt** se gère déjà tout seul (local prioritaire + CDN de secours, voir §2).
Il reste **CodeMirror** (éditeur et addons), chargé depuis un CDN. Pour le
rendre local aussi, télécharge ces fichiers et remplace les URLs `cm…` par des
chemins locaux (ex. `static/trinket/lib/...`) :

- CodeMirror 5 : `codemirror.min.js`, `codemirror.min.css`, `mode/python/python.min.js`,
  et les addons `addon/selection/active-line.min.js`, `addon/edit/closebrackets.min.js`,
  `addon/edit/matchbrackets.min.js`.

---

## Utilisation du shortcode

### Petits codes : directement dans le shortcode
Utilise la forme **paire** avec les délimiteurs `{{</* */>}}` (et non `{{%/* */%}}`)
pour que l'indentation Python soit conservée telle quelle :

```md
{{</* runpython lang="python" mode="toggle" */>}}
for i in range(5):
    print(i)
{{</* /runpython */>}}
```

### Gros codes : depuis `static/programmes/`
Forme **auto-fermante** avec `file` :

```md
{{</* runpython lang="vpython" mode="output" file="rebond.py" */>}}
```

### Paramètres

| Paramètre | Valeurs | Défaut | Rôle |
|-----------|---------|--------|------|
| `lang`    | `python`, `vpython` | `python` | Moteur d'exécution |
| `mode`    | `toggle`, `output`  | `toggle` | `toggle` = onglets Code/Résultat ; `output` = résultat seul |
| `default` | `code`, `output`    | `code`   | En mode `toggle` : onglet affiché au départ |
| `file`    | nom de fichier      | —        | Lit le code dans `static/programmes/<file>` |
| `height`  | nombre (px)         | auto     | Hauteur de départ ; en VPython elle s'ajuste ensuite à la scène |
| `width`   | nombre (px)         | —        | Force la largeur de la fenêtre ; la scène s'y adapte et la hauteur suit (sinon la fenêtre épouse la scène) |
| `autorun` | `true`/`false`      | `false`  | **Seul** moyen de lancer l'exécution au chargement |
| `fit`     | `scale`, `native`   | `scale`  | VPython : `scale` = ajustement parfait fenêtre/scène (transform CSS) ; `native` = canvas dimensionné nativement → **souris juste même fenêtre réduite** (à utiliser pour les scènes où l'on tire des points), au prix d'un ajustement parfois un peu moins parfait |
| `version` | `3.1`, `3.2`, …     | (3.2)    | VPython : force la version de GlowScript pour ce programme. Nécessite les bibliothèques correspondantes dans `glowscript_libraries/` (voir ci-dessous). Utile pour un programme écrit pour une version précise (p. ex. animations lancées depuis un menu, qui dépendent de la 3.1) |

Les deux modes correspondent aux options d'embed de Trinket :
« Output only » et « Toggle between code and output ».

Par défaut **rien ne s'exécute automatiquement** : l'utilisateur clique sur le
bouton ▶. Mets `autorun="true"` pour lancer le code dès l'affichage.

Un bouton ■ (Arrêter) apparaît pendant l'exécution. Il stoppe le programme
(utile pour les boucles d'animation VPython) en réinitialisant la fenêtre tout
en conservant le code en cours d'édition.

### Fichiers générés (`open()` / `write()`) — Python

Comme Trinket, le player **capture les écritures de fichiers**. Si un programme
Python fait :

```python
f = open('out.csv', 'w')
f.write("{}\t{:.4f}\n".format(t, valeur))
f.close()
```

le contenu écrit apparaît sous la console dans un panneau **Fichiers générés**,
avec deux boutons **Copier** et **Télécharger** : pratique pour coller les données
directement dans un tableur ou un grapheur (Deimos, etc.), ou pour récupérer le
fichier (`.csv`…). Les `print()` restent, eux, dans la console — on peut donc
garder un affichage « joli » pour la classe **et** un fichier au format brut, dans
le même programme. La capture est en mémoire (rien n'est écrit sur le disque réel)
et concerne les modes d'écriture (`'w'`, `'a'`).

---

## Compatibilité reveal-hugo (présentations)

Le shortcode fonctionne tel quel avec reveal-hugo. La configuration est
transmise par le **hash de l'URL** de l'iframe (`player.html#<config>`),
que le player lit lui-même : aucun script parent n'est requis, ce qui évite
les problèmes classiques de reveal.js (slides Markdown où les `<script>`
ne s'exécutent pas, iframes pilotées par reveal, CSP inline).

De plus, le player écoute le message `slide:start` que reveal.js envoie aux
iframes : une fenêtre en mode `output` (re)lance donc son animation à chaque
fois qu'on arrive sur la slide, et le rendu WebGL se dimensionne correctement.

Conseils en présentation :
- Pense à fixer `height=` pour que la fenêtre tienne dans la slide.
- En mode `output`, l'animation tourne aussi tant que la slide n'est pas
  affichée ; si tu as beaucoup de fenêtres VPython, préfère `mode="toggle"`
  (lancement au clic) pour économiser le processeur.

## Notes techniques

- **VPython** : pas besoin d'écrire la ligne d'en-tête `Web VPython 3.2` ;
  le player l'ajoute automatiquement si elle est absente. La fenêtre s'ajuste
  toute seule à **l'ensemble** de la sortie GlowScript — scène 3D, **boutons,
  sliders, légendes, graphes (`graph()`)** et **sortie `print()`** — en respectant
  la disposition voulue (les `align='left'` / `align='right'` se retrouvent bien
  côte à côte si la largeur le permet).
  - **sans `width`** : chaque élément garde sa **taille déclarée** dans le code
    (`canvas(width=…, height=…)`, `graph(width=…)`) ; la fenêtre épouse ce contenu
    et n'est réduite que si elle dépasse la place disponible. Une scène seule
    s'affiche donc exactement à sa taille, centrée ;
  - **avec `width="…"`** : c'est la **largeur de mise en page** de GlowScript. Très
    utile quand une scène étroite doit côtoyer un graphe large : p. ex. une scène
    de 250 px et un graphe de 650 px tiennent côte à côte avec `width="900"`. Le
    tout est ensuite réduit si la place manque.

  Le player mesure le conteneur GlowScript et redimensionne sa propre iframe via
  `window.frameElement`, en réagissant aux ajouts tardifs (un `graph()` ou un
  `print()` de fin de programme agrandit la fenêtre automatiquement).

- **Re-lancer un programme VPython** recharge la fenêtre (en conservant le code en
  cours d'édition). C'est nécessaire : relancer pendant qu'un programme tourne
  encore corromprait l'état interne de GlowScript (erreur `L.match`). Le premier
  lancement, lui, ne recharge pas.

  Note résolution : forcer une largeur supérieure à la résolution native d'une
  scène agrandit l'image par CSS (léger flou). Pour une scène nette en grand, fixe
  la résolution dans le code, p. ex. `scene = canvas(width=800, height=500)`.
- **`input()`** en Python : géré par un champ de saisie en ligne dans la zone de
  résultat.
- **turtle** : dessine dans la zone de résultat.
- **Isolation** : chaque fenêtre vit dans son iframe, ce qui évite tout conflit
  entre les nombreuses variables globales de Skulpt/GlowScript et permet
  plusieurs fenêtres sur une même page.
- **Personnalisation visuelle** : les couleurs/rayons sont des variables CSS
  (`:root`) en haut de `player.html`.

## Limites
- Skulpt implémente Python 3 mais pas toute la bibliothèque standard (pas de
  numpy/matplotlib). Idéal pour l'algorithmique, turtle, les bases.
- GlowScript VPython n'accède qu'aux bibliothèques JavaScript (comme sur
  glowscript.org), pas aux modules Python installés.
