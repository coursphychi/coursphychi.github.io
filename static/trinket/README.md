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
│   │   ├── pyhost.js                         ← Python (Pyodide) partagé par les fenêtres d'une page
│   │   ├── skulpt_libraries/                  ← (recommandé) Skulpt en local (voir §2)
│   │   └── glowscript_libraries/             ← À AJOUTER pour VPython (voir §3)
│   └── programmes/                           ← tes "gros" programmes .py
│       ├── rebond.py
│       ├── spirale.py
│       └── oscillateur.py                    ← exemple numpy + matplotlib (pyodide)
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
| `lang`    | `python`, `vpython`, `pyodide` | `python` | Moteur d'exécution : `python` = Skulpt (léger, instantané) ; `vpython` = GlowScript (3D) ; `pyodide` = vrai CPython avec numpy, matplotlib… (voir « Python scientifique ») |
| `mode`    | `toggle`, `output`  | `toggle` | `toggle` = onglets Code/Résultat ; `output` = résultat seul |
| `default` | `code`, `output`    | `code`   | En mode `toggle` : onglet affiché au départ |
| `file`    | nom de fichier      | —        | Lit le code dans `static/programmes/<file>` |
| `height`  | nombre (px) ou `auto` | selon `lang` | Hauteur de la fenêtre. `auto` (mode `toggle`) : la fenêtre affiche **toutes les lignes du code**, sans défilement, et suit les modifications (lignes ajoutées ou supprimées). Sur l'onglet Résultat la hauteur est conservée et la console défile. En mode `output`, `auto` revient à la hauteur par défaut. En VPython, la hauteur s'ajuste ensuite à la scène |
| `width`   | nombre (px)         | —        | Force la largeur de la fenêtre ; la scène s'y adapte et la hauteur suit (sinon la fenêtre épouse la scène) |
| `packages` | liste (`pint, uncertainties`) | — | `pyodide` : paquets PyPI **en Python pur** à installer pour cette fenêtre (seaborn n'en a pas besoin, voir ci-dessous) |
| `data`    | liste de fichiers | — | Fichiers de données (CSV, TXT…) placés dans `static/programmes/`, lisibles par le programme sous leur nom seul (voir « Fichiers de données ») — `python` et `pyodide` |
| `upload`  | `true` ou extensions (`.csv,.txt`) | — | L'élève importe ses propres fichiers (bouton ou glisser-déposer), lisibles par le programme — `python` et `pyodide` (voir « Fichiers importés par l'élève ») |
| `theme`   | `light`, `dark`, `auto` | `light` (ou défaut du site) | Thème de la fenêtre. `auto` suit le réglage clair/sombre du système de l'élève, en direct. Défaut pour tout le site : `[params] runpython_theme = "dark"` dans `hugo.toml` |
| `autorun` | `true`/`false`      | `false`  | **Seul** moyen de lancer l'exécution au chargement |
| `fit`     | `scale`, `native`   | `scale`  | VPython : `scale` = ajustement parfait fenêtre/scène (transform CSS) ; `native` = canvas dimensionné nativement → **souris juste même fenêtre réduite** (à utiliser pour les scènes où l'on tire des points), au prix d'un ajustement parfois un peu moins parfait |
| `version` | `3.1`, `3.2`, …     | (3.2)    | VPython : force la version de GlowScript pour ce programme. Nécessite les bibliothèques correspondantes dans `glowscript_libraries/` (voir ci-dessous). Utile pour un programme écrit pour une version précise (p. ex. animations lancées depuis un menu, qui dépendent de la 3.1) |

Les deux modes correspondent aux options d'embed de Trinket :
« Output only » et « Toggle between code and output ».

Par défaut **rien ne s'exécute automatiquement** : l'utilisateur clique sur le
bouton ▶. Mets `autorun="true"` pour lancer le code dès l'affichage.

**Hauteur adaptée à la sortie** (`python` et `pyodide`) : sur l'onglet
Résultat, la fenêtre épouse la sortie — graphe, texte, erreurs, fichiers
générés : elle s'agrandit ou rétrécit, entre 100 px et 90 % de la hauteur
de l'écran (au-delà, la console défile ; réglable via `OUT_MAX_FRACTION`
dans `player.html`). Pendant l'exécution elle ne fait que grandir ;
l'ajustement exact a lieu quand le programme se termine. De retour sur
l'onglet Code, elle reprend sa hauteur d'origine (ou celle du code avec
`height="auto"`). VPython garde son ajustement à la scène ; en présentation
reveal.js, l'ajustement est désactivé (une diapositive a une taille fixe).

**Largeur adaptée au graphe** (`python` et `pyodide`) : quand la sortie
contient un graphe (figure matplotlib, dessin turtle), la fenêtre se
resserre à la largeur utile — la plus grande entre le graphe, la plus longue
ligne de texte (un tableau pandas n'est pas coupé) et la barre d'outils — et
se centre dans la page. Elle ne dépasse jamais la place disponible ni
`width` s'il est déclaré (un graphe plus large est alors réduit). Sans
graphe, et de retour sur l'onglet Code, elle reprend sa largeur d'origine.

Un bouton ■ (Arrêter) apparaît pendant l'exécution. Il stoppe le programme
(utile pour les boucles d'animation VPython) en réinitialisant la fenêtre tout
en conservant le code en cours d'édition.

### Dans une notice (ou tout shortcode qui rend son contenu en Markdown)

```
{{< notice tip "Essaie toi-même" >}}
Modifie la valeur de `k` puis relance.
{{< runpython lang="pyodide" height="auto" >}}
import numpy as np
k = 3
print(np.arange(k))
{{< /runpython >}}
{{< /notice >}}
```

Ça fonctionne avec `{{< notice >}}` comme avec `{{% notice %}}` (testé sous
Hugo 0.123 et 0.147). La sortie de `runpython` ne contient volontairement
**aucune ligne vide** : une notice qui rend son contenu avec
`.Page.RenderString` le fait passer par Goldmark, et une ligne vide y
terminerait le bloc HTML (la suite du script serait réécrite en Markdown).
Si tu modifies `runpython.html`, garde cette contrainte — elle vaut pour tout
shortcode destiné à être imbriqué dans une notice.

### Python scientifique (`lang="pyodide"`) : numpy, matplotlib…

```
{{< runpython lang="pyodide" height="600" file="oscillateur.py" />}}
```

Ce moteur exécute le **vrai Python** (CPython compilé en WebAssembly, projet
[Pyodide](https://pyodide.org)), avec les bibliothèques scientifiques : numpy,
matplotlib, scipy, sympy, pandas… **Rien à installer** : Pyodide est chargé
depuis le CDN jsDelivr, en **version épinglée** (`LIBS.pyodide` en haut de
`player.html`).

- **Paquets automatiques** : les `import` du programme sont détectés et les
  bibliothèques correspondantes téléchargées à la demande.
- **Paquets hors Pyodide (seaborn…)** : Pyodide ne fournit qu'une liste fixe
  de paquets. Les paquets PyPI écrits en **Python pur** peuvent s'y ajouter
  (via `micropip`) :
  - **seaborn** s'installe tout seul dès que le code fait `import seaborn` ;
    il figure dans la liste blanche `LIBS.pypiAuto` en haut de `player.html`
    (testé : seaborn 0.13.2 + pandas 3.0 + matplotlib 3.10) ;
  - pour un autre paquet, ajoute `packages="pint"` au shortcode, ou ajoute-le
    à `LIBS.pypiAuto` pour tout le site.
  
  Liste blanche **volontaire** : le player n'installe pas n'importe quel nom
  tapé dans l'éditeur, car une faute de frappe (`import numpi`) pourrait
  installer un paquet malveillant homonyme publié sur PyPI. Les paquets avec
  du code compilé (C, Fortran…) absents de Pyodide ne peuvent pas s'installer.
- **Graphes** : `plt.show()` insère la figure dans la console, à sa place parmi
  les `print()`. Une figure créée sans `plt.show()` est affichée à la fin.
- **Erreurs** : traceback réduit au seul programme de l'élève, ligne fautive
  marquée d'un point rouge (comme en `python`).
- **Fichiers** : les fichiers texte écrits apparaissent dans « Fichiers générés ».
- **Variables** : chaque exécution repart de zéro.

**Une seule installation par page.** Toutes les fenêtres `pyodide` d'une
même page partagent **une seule instance** de Python : la première qui en a
besoin la démarre (avec ses bibliothèques), les suivantes la réutilisent
aussitôt — numpy, matplotlib ou seaborn ne sont installés qu'une fois.
L'instance est hébergée par la page elle-même (via `pyhost.js`, à déployer
avec `player.html`), pas par une fenêtre : recharger une fenêtre (bouton ■)
ne la perd pas. Chaque exécution garde ses propres variables et ses propres
fichiers. Les exécutions passent **une à la fois** : une fenêtre lancée
pendant qu'une autre tourne affiche « En attente… » quelques instants. Si la
page n'est pas accessible (fenêtre ouverte seule, autre domaine), chaque
fenêtre retombe sur sa propre instance.

Skulpt (`python`) et GlowScript (`vpython`) restent propres à chaque
fenêtre : ils sont légers (et mis en cache par le navigateur), et VPython a
besoin d'un état neuf à chaque exécution.

Ce qu'il faut savoir :

- **Poids** : ~10 Mo pour Python au premier lancement, puis quelques Mo par
  bibliothèque (numpy + matplotlib : ~20–30 Mo au total). Tout est ensuite en
  cache : les lancements suivants sont rapides. Réserve donc `pyodide` aux
  programmes qui en ont besoin ; `python` (Skulpt) reste le bon choix pour
  l'algorithmique.
- **`input()`** passe par une boîte de dialogue du navigateur (pas de saisie
  dans la console comme en `python`).
- **Programme très long** : l'onglet est occupé pendant le calcul ; le bouton ■
  n'agit qu'entre deux calculs (ou pendant les téléchargements).
- **Graphes statiques** : pas d'animation (`plt.pause`, `FuncAnimation`) ni de
  zoom interactif — une image par figure.
- **Hauteur** : prévois `height="560"` ou plus pour qu'un graphe tienne sans
  défilement.
- **CSP** : si ton site impose une Content-Security-Policy, autorise
  `cdn.jsdelivr.net` (en `script-src` et `connect-src`), et pour les paquets
  PyPI `pypi.org` et `files.pythonhosted.org` (en `connect-src`).

### Fichiers de données (`data=`) — CSV, TXT…

```
{{< runpython data="chute.csv" file="analyse.py" />}}
{{< runpython lang="pyodide" data="tp3/mesures.csv, tp3/etalon.csv" >}}…{{< /runpython >}}
```

- Les fichiers sont cherchés dans `static/programmes/` (sous-dossiers permis),
  séparés par des virgules. Le programme les voit sous leur **nom seul** :
  `data="tp3/mesures.csv"` → `open("mesures.csv")`.
- Hugo les lit au build et les transmet avec le code : rien à télécharger à
  l'exécution, ça marche aussi en reveal.js et dans une notice. Un fichier
  introuvable **arrête le build** avec le nom de la page et la ligne ; au-delà
  de ~300 ko, un avertissement signale que la page s'alourdit.
- `python` (Skulpt) : `open()`, itération ligne à ligne, `read()`,
  `readline()`, `readlines()`, `seek()`/`tell()`, modes `"r"`, `"w"`, `"a"`,
  et `FileNotFoundError` si le fichier n'existe pas (pas de module `csv` :
  on découpe avec `ligne.split(";")`).
- `pyodide` : vrai système de fichiers — `pandas.read_csv`, `numpy.loadtxt`,
  module `csv`…
- À chaque exécution, les données repartent de leur état d'origine. Un
  fichier de données modifié par le programme apparaît dans « Fichiers
  générés » ; non modifié, il n'y figure pas.
- Pas de données pour `vpython` (GlowScript n'a pas de système de fichiers).

### Thème sombre (`theme=`)

```
{{< runpython theme="dark" >}}…{{< /runpython >}}     ← toujours sombre
{{< runpython theme="auto" >}}…{{< /runpython >}}     ← suit le système de l'élève
```

Pour tout le site, dans `hugo.toml` (un `theme=` sur une fenêtre reste prioritaire) :

```toml
[params]
  runpython_theme = "dark"
```

Tout passe en sombre : barre, onglets, éditeur (thème `tkdark` intégré,
couleurs inspirées de One Dark), console, messages, fichiers. Contrastes
vérifiés au critère WCAG AA (texte ≥ 4,5:1). Le thème est appliqué avant le
premier affichage : pas de flash blanc au chargement. Les figures matplotlib
gardent leur fond blanc, posées comme une carte ; les scènes VPython ont déjà
leur propre fond. Pour ajuster une couleur, modifier les variables du bloc
`html.tk-dark` en haut de `player.html`.

### Fichiers importés par l'élève (`upload=`)

```
{{< runpython upload="true" >}}…{{< /runpython >}}
{{< runpython lang="pyodide" upload=".csv,.txt" >}}…{{< /runpython >}}
```

Un bouton d'import apparaît dans la barre ; on peut aussi **glisser** un ou
plusieurs fichiers sur la fenêtre. Chaque fichier importé s'affiche en
étiquette sous la barre (nom, taille, × pour le retirer) et se lit par son
nom : `open("mesures.csv")`, `pandas.read_csv("mesures.csv")`.

- **CSV d'Excel** : souvent encodé en Windows-1252 (et parfois en UTF-16 ou
  UTF-8 avec BOM). Le player détecte l'encodage et convertit en UTF-8, et
  normalise les fins de ligne Windows : les accents et `readline()`
  fonctionnent sans précaution. La virgule décimale reste à traiter dans le
  programme (`float(v.replace(",", "."))`).
- **Fichiers binaires** (image, xlsx…) : acceptés en `pyodide` seulement,
  tels quels. `upload="true"` accepte `.csv .tsv .txt .dat .json` en
  `python`, tout type en `pyodide` ; une liste d'extensions restreint le choix.
- 5 Mo maximum par fichier. Rien n'est envoyé sur Internet : tout reste dans
  le navigateur de l'élève.
- Les fichiers importés restent disponibles le temps de la session de
  l'onglet (ils survivent au bouton ■ et au rechargement de la page). Un
  fichier importé remplace un fichier `data=` de même nom.
- Pas d'import pour `vpython`.

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
  numpy/matplotlib). Idéal pour l'algorithmique, turtle, les bases. Pour
  numpy/matplotlib, utiliser `lang="pyodide"`.
- GlowScript VPython n'accède qu'aux bibliothèques JavaScript (comme sur
  glowscript.org), pas aux modules Python installés.
