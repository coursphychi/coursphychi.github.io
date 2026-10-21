+++
title = "Décollage d'Ariane et Python"
draft = false
hidden = true
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Cette activité présente un exemple d'exploitation des données d'un pointage vidéo en Python à partir du décollage d'une fusée Ariane&nbsp;5. Vous pouvez exécuter et modifier librement chaque fenêtre de code directement dans la page&nbsp;: seule la boucle de calcul de la vitesse présentée plus loin est exigible.</p>

## Vidéo du décollage et acquisition {.nt-h2}

<div style="position:relative; width:100%; max-width:760px; margin:1.2em auto; aspect-ratio:16/9; border-radius:12px; overflow:hidden; box-shadow:0 6px 22px rgba(30,41,59,0.12);">
  <iframe src="https://www.youtube-nocookie.com/embed/0QFr5W3Lgrw" title="Décollage d'Ariane 5" style="position:absolute; inset:0; width:100%; height:100%; border:0;" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<p>Le pointage vidéo a été réalisé de façon similaire à un TP de pointage classique. Les données fournies par le logiciel (repérages temporels $t$ et altitudes $y$ de la fusée) ont été enregistrées dans un fichier de données nommé <code>arianelaunch.csv</code>.</p>

## Importation du fichier CSV {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-table"></i>Fichier CSV et bibliothèque <code>pandas</code></p>
<p>Un fichier <span class="imp nt-hole">CSV</span> (<i>Comma-Separated Values</i>) est un fichier texte contenant un tableau de valeurs séparées par un caractère délimiteur (souvent un point-virgule <code>;</code> en français). En Python, la bibliothèque <b><code>pandas</code></b> permet d'importer et de manipuler très facilement ces tableaux de mesures.</p>
</div>

<p>Cliquez sur <b>▶ Exécuter</b> dans la fenêtre ci-dessous pour importer le fichier <code>arianelaunch.csv</code>, afficher le tableau de mesures, puis extraire les colonnes sous forme de deux listes Python <code>temps</code> et <code>altitude</code>&nbsp;:</p>

{{< runpython lang="pyodide" height="auto" >}}
import pandas as pd
from pyodide.http import open_url

# Lecture du fichier CSV depuis le serveur (séparateur ';' et virgule décimale ',')
url = "https://coursphychi.github.io/arianelaunch.csv"
tableau = pd.read_csv(open_url(url), sep=';', decimal=',')

# On renomme les colonnes pour simplifier leur écriture dans la suite du code
tableau.rename(columns={'temps (s)': 'temps', 'altitude (m)': 'altitude'}, inplace=True)

print("--- Tableau des 28 mesures pointées ---")
print(tableau.to_string())

# Conversion des deux colonnes en listes Python classiques
temps = list(tableau['temps'])
altitude = list(tableau['altitude'])

print("\nListe temps =", temps)
print("Liste altitude =", altitude)
{{< /runpython >}}

## Calcul des vitesses en Python {.nt-h2}

<p class="nt-lead">Pour déterminer la valeur de la vitesse verticale $v(t_i)$ de la fusée à chaque instant $t_i$, on calcule le quotient de la distance parcourue entre les instants $t_i$ et $t_{i+1}$ par la durée écoulée&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vitesse verticale à l'instant $t_i$</p>
<p class="nt-f-math">$$v(t_i) = \dfrac{y(t_{i+1}) - y(t_i)}{t_{i+1} - t_i}$$</p>
<div class="nt-f-units"><span>$v(t_i)$ en <b>m/s</b></span><span>$y(t_{i+1}),\, y(t_i)$ en <b>m</b></span><span>$t_{i+1},\, t_i$ en <b>s</b></span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-code"></i>Construction de la liste des vitesses</p>
<p>Pour construire automatiquement la liste <code>vitesse</code> à partir des listes <code>temps</code> et <code>altitude</code>&nbsp;:</p>
<ul class="nt-facts">
<li><code>vitesse = []</code> crée au départ une <span class="imp nt-hole">liste vide</span>&nbsp;;</li>
<li><code>len(temps)</code> renvoie le nombre total d'éléments de la liste <code>temps</code> (ici $28$ mesures)&nbsp;;</li>
<li><code>for i in range(len(temps) - 1):</code> fait varier l'indice <code>i</code> de <code>0</code> jusqu'à <code>26</code> (soit $27$ calculs), car le calcul en <code>i</code> utilise le point suivant d'indice <span class="imp nt-hole"><code>i + 1</code></span>&nbsp;;</li>
<li><code>vitesse.append(...)</code> <span class="imp nt-hole">ajoute</span> à la fin de la liste <code>vitesse</code> la nouvelle valeur calculée à chaque tour de boucle.</li>
</ul>
</div>

<p>Exécutez le programme ci-dessous (moteur instantané) pour observer le calcul de la liste <code>vitesse</code>&nbsp;:</p>

{{< runpython height="auto" >}}
temps = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4]
altitude = [0.0, 0.06, -0.04, 0.06, -0.04, 0.12, 1.01, 1.96, 3.35, 4.62, 6.39, 8.47, 10.69, 12.97, 16.13, 19.42, 23.09, 26.76, 30.93, 35.24, 39.92, 44.85, 49.85, 55.42, 61.3, 67.5, 74.33, 81.48]

# --- CE CODE EST À COMPRENDRE ---
vitesse = []
for i in range(len(temps) - 1):
    v = (altitude[i+1] - altitude[i]) / (temps[i+1] - temps[i])
    vitesse.append(round(v, 2))

print("Liste des vitesses (en m/s) :")
print(vitesse)
{{< /runpython >}}

<details class="nt-d">
<summary><span class="nt-tag"><i class="fa-solid fa-table-list"></i>Tableau complet</span><span class="nt-sum">Afficher le tableau récapitulatif (temps, altitude, vitesse)</span></summary>
<div class="nt-d-body">
<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Indice <code>i</code></th><th><code>temps</code> (s)</th><th><code>altitude</code> (m)</th><th><code>vitesse</code> (m/s)</th></tr></thead>
<tbody>
<tr><td>0</td><td>0,0</td><td>0,00</td><td>0,30</td></tr>
<tr><td>1</td><td>0,2</td><td>0,06</td><td>−0,50</td></tr>
<tr><td>2</td><td>0,4</td><td>−0,04</td><td>0,50</td></tr>
<tr><td>3</td><td>0,6</td><td>0,06</td><td>−0,50</td></tr>
<tr><td>4</td><td>0,8</td><td>−0,04</td><td>0,80</td></tr>
<tr><td>5</td><td>1,0</td><td>0,12</td><td>4,45</td></tr>
<tr><td>6</td><td>1,2</td><td>1,01</td><td>4,75</td></tr>
<tr><td>7</td><td>1,4</td><td>1,96</td><td>6,95</td></tr>
<tr><td>8</td><td>1,6</td><td>3,35</td><td>6,35</td></tr>
<tr><td>9</td><td>1,8</td><td>4,62</td><td>8,85</td></tr>
<tr><td>10</td><td>2,0</td><td>6,39</td><td>10,40</td></tr>
<tr><td>11</td><td>2,2</td><td>8,47</td><td>11,10</td></tr>
<tr><td>12</td><td>2,4</td><td>10,69</td><td>11,40</td></tr>
<tr><td>13</td><td>2,6</td><td>12,97</td><td>15,80</td></tr>
<tr><td>14</td><td>2,8</td><td>16,13</td><td>16,45</td></tr>
<tr><td>15</td><td>3,0</td><td>19,42</td><td>18,35</td></tr>
<tr><td>16</td><td>3,2</td><td>23,09</td><td>18,35</td></tr>
<tr><td>17</td><td>3,4</td><td>26,76</td><td>20,85</td></tr>
<tr><td>18</td><td>3,6</td><td>30,93</td><td>21,55</td></tr>
<tr><td>19</td><td>3,8</td><td>35,24</td><td>23,40</td></tr>
<tr><td>20</td><td>4,0</td><td>39,92</td><td>24,65</td></tr>
<tr><td>21</td><td>4,2</td><td>44,85</td><td>25,00</td></tr>
<tr><td>22</td><td>4,4</td><td>49,85</td><td>27,85</td></tr>
<tr><td>23</td><td>4,6</td><td>55,42</td><td>29,40</td></tr>
<tr><td>24</td><td>4,8</td><td>61,30</td><td>31,00</td></tr>
<tr><td>25</td><td>5,0</td><td>67,50</td><td>34,15</td></tr>
<tr><td>26</td><td>5,2</td><td>74,33</td><td>35,75</td></tr>
<tr><td>27</td><td>5,4</td><td>81,48</td><td><code>NaN</code> (non défini)</td></tr>
</tbody>
</table>
</div>
</div>
</details>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-circle-info"></i>Remarque&nbsp;:</p>
<p>Lorsqu'on intègre la liste <code>vitesse</code> (qui compte $27$ valeurs) dans le tableau de $28$ lignes avec <code>pandas</code>, la dernière ligne ($t = \pu{5,4 s}$) affiche <b><code>NaN</code></b> (<i>Not a Number</i>). En effet, aucune vitesse ne peut être calculée pour la toute dernière position pointée, puisque la formule nécessite de connaître la position <i>suivante</i> $y(t_{i+1})$, qui n'existe pas&nbsp;!</p>
</div>

## Représentations graphiques interactives {.nt-h2}

<p class="nt-lead">Exécutez les deux fenêtres ci-dessous pour tracer les graphiques interactifs de l'<b>altitude</b> puis de la <b>vitesse</b> en fonction du temps. Vous pouvez passer la souris sur chaque point du graphique pour lire directement ses coordonnées.</p>

### Graphique de l'altitude en fonction du temps {.nt-h3}

{{< runpython lang="pyodide" height="auto" >}}
import pandas as pd
import plotly.graph_objects as go
from pyodide.http import open_url

url = "https://coursphychi.github.io/arianelaunch.csv"
tableau = pd.read_csv(open_url(url), sep=';', decimal=',')
tableau.rename(columns={'temps (s)': 'temps', 'altitude (m)': 'altitude'}, inplace=True)

fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=tableau['temps'],
    y=tableau['altitude'],
    mode='markers',
    hovertemplate='temps = %{x:.1f} s<br>altitude = %{y:.2f} m',
    name='',
    marker=dict(size=10, color='#00A2FF', symbol='circle-dot', line=dict(color='#004D80', width=0.5))
))
fig1.update_xaxes(title_text='Temps (s)')
fig1.update_yaxes(title_text='Altitude (m)')
fig1.update_layout(title_text="Altitude de la fusée en fonction du temps", title_x=0.5, height=520)
fig1.show()
{{< /runpython >}}

### Graphique de la vitesse en fonction du temps {.nt-h3}

{{< runpython lang="pyodide" height="auto" >}}
import pandas as pd
import plotly.graph_objects as go
from pyodide.http import open_url

url = "https://coursphychi.github.io/arianelaunch.csv"
tableau = pd.read_csv(open_url(url), sep=';', decimal=',')
tableau.rename(columns={'temps (s)': 'temps', 'altitude (m)': 'altitude'}, inplace=True)

temps = list(tableau['temps'])
altitude = list(tableau['altitude'])

vitesse = []
for i in range(len(temps) - 1):
    vitesse.append((altitude[i+1] - altitude[i]) / (temps[i+1] - temps[i]))

tableau["vitesse"] = pd.Series(vitesse, index=tableau.index[:-1])

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=tableau['temps'],
    y=tableau['vitesse'],
    mode='markers',
    hovertemplate='temps = %{x:.1f} s<br>vitesse = %{y:.2f} m/s',
    name='',
    marker=dict(size=10, color='#FFD932', symbol='x-dot', line=dict(color='red', width=0.5))
))
fig2.update_xaxes(title_text='Temps (s)')
fig2.update_yaxes(title_text='Vitesse (m/s)')
fig2.update_layout(title_text="Vitesse de la fusée en fonction du temps", title_x=0.5, height=520)
fig2.show()
{{< /runpython >}}

## Exploitation physique des résultats {.nt-h2}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<ol class="nt-steps">
<li><p>Vérifiez «&nbsp;à la main&nbsp;» le calcul réalisé par Python pour déterminer la vitesse atteinte à $t = \pu{3,0 s}$ (les graphiques étant interactifs, vous pouvez lire les altitudes et vérifier la valeur de la vitesse en survolant les points correspondants).</p></li>
<li><p>Convertir cette vitesse en km/h.</p></li>
<li><p>En supposant que le mouvement est purement vertical, comment peut-on qualifier le mouvement de la fusée après $t = \pu{1,0 s}$&nbsp;?</p></li>
<li><p>En combien de temps la fusée atteindra-t-elle la vitesse du son ($v_\text{son} = \pu{340 m/s}$) si sa vitesse continue d'augmenter au même rythme&nbsp;?</p></li>
</ol>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution détaillée des 4 questions</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p><b>Calcul de la vitesse à $t_{15} = \pu{3,0 s}$&nbsp;:</b><br>
Sur le tableau ou le premier graphique, on relève les altitudes aux instants $t_{15} = \pu{3,0 s}$ et $t_{16} = \pu{3,2 s}$&nbsp;:<br>
$$y(\pu{3,0 s}) = \pu{19,42 m} \quad\text{et}\quad y(\pu{3,2 s}) = \pu{23,09 m}$$
En appliquant la relation du cours&nbsp;:
$$v(\pu{3,0 s}) = \dfrac{y(\pu{3,2 s}) - y(\pu{3,0 s})}{3{,}2 - 3{,}0} = \dfrac{23{,}09 - 19{,}42}{0{,}2} = \dfrac{3{,}67}{0{,}2} = \pu{18,35 m/s}$$
On retrouve exactement la valeur $\pu{18,35 m/s}$ indiquée sur le second graphique.</p></li>
<li><p><b>Conversion en $\pu{km/h}$&nbsp;:</b><br>
Pour convertir des m/s en km/h, on multiplie par $3{,}6$&nbsp;:
$$v(\pu{3,0 s}) = 18{,}35 \times 3{,}6 \approx \pu{66,1 km/h}$$
</p></li>
<li><p><b>Description du mouvement&nbsp;:</b><br>
Entre $t = \pu{0,0 s}$ et $t = \pu{1,0 s}$, la fusée est encore immobile sur son pas de tir (les infimes variations de $\pm\pu{0,06 m}$ sont dues à l'imprécision du pointage manuel à la souris).<br>
Après le décollage ($t \geqslant \pu{1,0 s}$), la trajectoire est une droite verticale et la valeur de la vitesse augmente au cours du temps&nbsp;: le mouvement de la fusée est donc <span class="imp nt-hole">rectiligne accéléré</span>.</p></li>
<li><p><b>Durée pour atteindre la vitesse du son ($v_\text{son} = \pu{340 m*s-1}$)&nbsp;:</b><br>
Sur le second graphique, à partir du décollage effectif à $t_0 = \pu{1,0 s}$, les points $(t, v)$ sont sensiblement alignés sur une droite&nbsp;: la vitesse augmente de façon quasi proportionnelle à la durée écoulée depuis le décollage.<br>
<ul>
<li>Entre $t_0 = \pu{1,0 s}$ ($v \approx \pu{0 m/s}$) et $t = \pu{5,2 s}$ ($v = \pu{35,75 m/s}$), soit pendant une durée $\Delta t = 5{,}2 - 1{,}0 = \pu{4,2 s}$, la vitesse augmente d'environ $\pu{35,75 m*s-1}$, ce qui correspond à un gain moyen de vitesse (accélération) de&nbsp;:
$$a = \dfrac{\Delta v}{\Delta t} = \dfrac{35{,}75}{4{,}2} \approx \pu{8,5 m*s-1}\text{ par seconde (soit }\pu{8,5 m*s-2}\text{)}$$</li>
<li>Pour atteindre $v_\text{son} = \pu{340 m/s}$ à ce rythme à partir du décollage, il faudra une durée&nbsp;:
$$\Delta t_\text{son} = \dfrac{340}{8{,}5} \approx \pu{40 s}\quad\text{(soit à l'instant }t \approx \pu{41 s}\text{ de la vidéo)}$$</li>
</ul>
</p></li>
</ol>
<p class="nt-note">En réalité, comme la fusée consomme son carburant, sa masse diminue fortement au cours de l'ascension&nbsp;: son accélération augmente donc encore plus vite, et Ariane&nbsp;5 franchit le mur du son (Mach&nbsp;1) au bout d'environ $45\text{ à }50\text{ s}$ de vol malgré l'augmentation des frottements de l'air.</p>
</div>
</details>