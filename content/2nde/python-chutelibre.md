+++
title = "Mouvement de chute libre d'une balle (Python)"
draft = false
hidden = "true"
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<p class="nt-lead">On souhaite modéliser et étudier à l'aide du langage Python les positions successives, les vecteurs vitesse et les variations de vitesse d'une balle lancée verticalement vers le haut.</p>

<div style="position:relative;margin-left:auto;margin-right:auto;width:400px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/lanceballepython.png" style="box-shadow:none;background:none;">
</div>


## Modélisation physique et chute libre {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition&nbsp;: chute libre</p>
<p>Un système est en <span class="imp nt-hole">chute libre</span> s'il n'est soumis qu'à <span class="imp nt-hole">son poids</span> (l'action mécanique exercée par l'air est alors négligée).</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question 1</p>
<p>Une fois que la balle a quitté la main du lanceur, faire un diagramme objet-interaction (DOI) des différents objets interagissant avec la balle, puis représenter les forces s'exerçant sur la balle (assimilée à un point matériel situé en son centre).</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir le bilan des actions mécaniques</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>Terre</b>&nbsp;: interaction à distance (gravitationnelle), modélisée par le <span class="imp">poids $\vec{P}$</span> (direction verticale, sens vers le bas).</li>
<li><b>Air</b>&nbsp;: interaction de contact avec l'air environnant, modélisée par la force de <span class="imp">frottement fluide $\vec{f}$</span> (opposée au mouvement) et la poussée d'Archimède (très faible ici).</li>
</ul>
<p class="nt-note">Attention&nbsp;: la main n'interagit plus avec la balle dès que celle-ci est lâchée&nbsp;! Il n'y a pas de «&nbsp;force de lancer&nbsp;» qui accompagnerait la balle pendant son vol.</p>
</div>
</details>

<p class="nt-lead">À partir de maintenant, on <b>néglige les frottements de l'air</b> devant le poids de la balle.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question 2</p>
<p>Sous cette hypothèse, la balle est-elle en chute libre pendant sa phase de montée&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p><b>Oui, tout à fait.</b> En physique, le terme «&nbsp;chute libre&nbsp;» ne signifie pas nécessairement que l'objet descend&nbsp;: dès que la balle a quitté la main et que l'action de l'air est négligée, la seule force qui s'exerce sur elle est son poids $\vec{P}$, aussi bien pendant la <span class="imp nt-hole">montée</span>, au sommet de la trajectoire, que pendant la <span class="imp nt-hole">descente</span>.</p>
</div>
</details>

## Listes de données et boucles en Python {.nt-h2}

### Création et affichage des listes `T` et `Y` {.nt-h3}

<p>Le programme ci-dessous calcule une liste <code>T</code> contenant $N = 12$ instants $t_i$ régulièrement espacés d'une durée $\Delta t$ (notée <code>Dt</code>), ainsi qu'une liste <code>Y</code> contenant les $N$ altitudes $y(t_i)$ correspondantes de la balle (lancée à $t = 0$ depuis une hauteur de $1\text{ m}$ avec une vitesse initiale $v_0 = \pu{5 m*s-1}$).</p>

<p>Cliquez sur le bouton <b>▶ Exécuter</b> pour afficher le contenu des deux listes&nbsp;:</p>

{{< runpython height="auto"    >}}
g = 9.8         # intensité de la pesanteur (m/s^2)
v0 = 5          # vitesse initiale (m/s)
tmax = 2*v0/g   # durée pour revenir à l'altitude initiale
N = 12          # nombre de positions étudiées

Dt = tmax/(N-2) # intervalle de temps entre deux points consécutifs (s)

T = [Dt*i for i in range(N)]            # liste des instants t_i (s)
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]  # liste des altitudes y_i (m)

print("Liste des altitudes Y :", Y)
print("Liste des instants T :", T)
{{< /runpython >}}

### Récupérer un élément dans une liste {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-code"></i>Indice d'une liste en Python</p>
<p>En Python, une <b>liste</b> est une série d'éléments séparés par des virgules et placés entre crochets <code>[ ]</code>. Les éléments sont repérés par leur position, appelée <span class="imp nt-hole">indice</span>, mais <b>la numérotation commence à 0</b> (et non à 1)&nbsp;:</p>
<ul class="nt-facts">
<li>pour récupérer le 1<sup>er</sup> élément d'une liste <code>T</code>, on écrit <code>T[0]</code>&nbsp;;</li>
<li>pour récupérer le 3<sup>e</sup> élément de la liste <code>Y</code> (l'altitude du 3<sup>e</sup> point), on écrit <code>Y[2]</code>&nbsp;;</li>
<li>plus généralement, le $i$<sup>e</sup> élément d'une liste <code>L</code> s'écrit <span class="imp nt-hole"><code>L[i-1]</code></span>&nbsp;;</li>
<li><b>astuce&nbsp;:</b> pour récupérer directement le <i>dernier</i> élément d'une liste <code>L</code>, on écrit <span class="imp nt-hole"><code>L[-1]</code></span>.</li>
</ul>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Position courante</th><th>1<sup>er</sup> élément</th><th>2<sup>e</sup> élément</th><th>3<sup>e</sup> élément</th><th>…</th><th>$i$<sup>e</sup> élément</th><th>Dernier ($N$<sup>e</sup>)</th></tr></thead>
<tbody>
<tr><td>Indice en Python</td><td><code>0</code></td><td><code>1</code></td><td><code>2</code></td><td>…</td><td><code>i - 1</code></td><td><code>N - 1</code> ou <code>-1</code></td></tr>
<tr><td>Syntaxe pour la liste <code>Y</code></td><td><code>Y[0]</code></td><td><code>Y[1]</code></td><td><code>Y[2]</code></td><td>…</td><td><code>Y[i-1]</code></td><td><code>Y[N-1]</code> ou <code>Y[-1]</code></td></tr>
</tbody>
</table>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question 3</p>
<p>Dans la fenêtre de code ci-dessous, complétez la fin du programme pour afficher le <b>7<sup>e</sup> élément</b> de la liste <code>Y</code> ainsi que son <b>dernier élément</b>.</p>
</div>

{{< runpython height="auto"    >}}
g = 9.8
v0 = 5
tmax = 2*v0/g
N = 12
Dt = tmax/(N-2)
T = [Dt*i for i in range(N)]
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]

# Écrire votre code ci-dessous pour afficher le 7e élément puis le dernier élément de Y :

{{< /runpython >}}

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir les instructions à écrire</span></summary>
<div class="nt-d-body">
<p>Le 7<sup>e</sup> élément porte l'indice <code>6</code> (car $7 - 1 = 6$)&nbsp;:</p>
<pre><code class="python">print("7e élément de Y :", Y[6])
print("Dernier élément de Y :", Y[-1])</code></pre>
<p class="nt-note">On trouve $Y[6] \approx \pu{2,22 m}$ et $Y[-1] \approx \pu{0,44 m}$.</p>
</div>
</details>

### Parcourir une liste avec `for` et tester avec `if / else` {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-repeat"></i>Boucle <code>for</code> et conditions <code>if / else</code></p>
<ul class="nt-facts">
<li><b>La boucle <code>for</code>&nbsp;:</b> l'instruction <code>for i in range(N):</code> fait varier la variable <code>i</code> (qui sert d'<u>i</u>ndice) sur tous les entiers de <code>0</code> jusqu'à <code>N - 1</code> inclus. Tout le bloc de code <b>indenté</b> (décalé vers la droite de 4 espaces) est répété pour chaque valeur de <code>i</code>.</li>
<li><b>La structure conditionnelle <code>if / else</code>&nbsp;:</b> permet d'exécuter un bloc d'instructions <i>uniquement si</i> une condition est vraie (<code>if</code>), et un autre bloc sinon (<code>else</code>).</li>
</ul>
</div>

<p>Exécutez les deux petits exemples ci-dessous pour observer le fonctionnement d'une boucle <code>for</code> qui parcourt la liste <code>Y</code>, puis d'un test de parité avec <code>if / else</code>&nbsp;:</p>

{{< runpython height="auto"    >}}
g = 9.8
v0 = 5
tmax = 2*v0/g
N = 12
Dt = tmax/(N-2)
T = [Dt*i for i in range(N)]
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]

print("--- Affichage élément par élément avec une boucle for ---")
for i in range(N):
    print(f"Point n°{i} : y = {Y[i]:.2f} m")
{{< /runpython >}}

{{< runpython height="auto"    >}}
# Exemple d'utilisation de if / else sur les entiers de 0 à 19 :
for i in range(20):
    if i % 2 == 0: # i % 2 calcule le reste de la division euclidienne de i par 2
        print(f"{i} est pair")
    else:
        print(f"{i} est impair")
{{< /runpython >}}

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-face-Grin-Beam-Sweat"></i>Comparaison</span><span class="nt-sum">Pourquoi le test automatique est bien plus élégant que la «&nbsp;version candide&nbsp;»</span></summary>
<div class="nt-d-body">
<p>Sans utiliser l'opérateur reste <code>%</code> et le bloc <code>if / else</code>, il aurait fallu tester chaque valeur à la main&nbsp;:</p>
<pre><code class="python">for i in range(20):
    if i == 0: print(f"{i} est pair")
    if i == 1: print(f"{i} est impair")
    if i == 2: print(f"{i} est pair")
    # ... et ainsi de suite jusqu'à 19 (ou 10 000 !)</code></pre>
<p>Un bon programme exprime une <b>règle générale</b> valable quel que soit le nombre de points $N$.</p>
</div>
</details>

## Évolution de l'altitude au cours du temps {.nt-h2}

<p class="nt-lead">On trace maintenant le graphique représentant l'altitude $y$ de la balle en fonction du temps $t$. Les points sont colorés en <b style="color:#4c72b0;">bleu</b> lors de la montée et en <b style="color:#dd8452;">orange</b> lors de la descente.</p>

<p>Exécutez le programme ci-dessous (le premier lancement de <code>matplotlib</code> prend quelques secondes)&nbsp;:</p>

{{< runpython lang="pyodide" height="auto"    >}}
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

# 1. Création des données
g = 9.8
v0 = 5
tmax = 2*v0/g
N = 12
Dt = tmax/(N-2)
T = [Dt*i for i in range(N)]
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]

# 2. Tracé du graphique y(t)
plt.figure(figsize=(8, 4.8), dpi=120)
plt.scatter(T[0], Y[0], c="#4c72b0")
for i in range(1, N):
    if Y[i-1] < Y[i]:
        coul = "#4c72b0"
    else:
        coul = "#dd8452"
    plt.scatter(T[i], Y[i], c=coul)

plt.title("Altitude de la balle au cours du temps")
plt.ylim([0, max(Y) + 0.2])
plt.xlim([-0.05, T[-1] + 0.1])
plt.xlabel("t (s)")
plt.ylabel("y (m)")
plt.tight_layout()
plt.show()
{{< /runpython >}}

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention à ne pas confondre</p>
<p>La courbe en cloche ci-dessus représente l'évolution de l'altitude $y$ <b>en fonction du temps $t$</b> ($y(t)$), et <b>non la trajectoire</b> de la balle dans l'espace&nbsp;! Dans la réalité, la balle monte et redescend sur une même droite verticale ($x = 0$).</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 4</p>
<p>Décrire précisément le mouvement de la balle (nature de la trajectoire et évolution de la vitesse lors des deux phases).</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 5</p>
<p>Expliquer comment le programme choisit automatiquement la couleur bleue ou orange pour chaque point $M_i$.</p>
</ol>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir les réponses aux questions 4 et 5</span></summary>
<div class="nt-d-body">
<ol class="nt-steps" start="4">
<li><p>La trajectoire est un segment de droite vertical&nbsp;: le mouvement est <span class="imp">rectiligne</span>.<br>
• <b>Phase de montée (points bleus)&nbsp;:</b> l'écart vertical parcouru pendant une même durée $\Delta t$ diminue au fur et à mesure que la balle monte. Le mouvement est <b>rectiligne ralenti</b> (ou décéléré).<br>
• <b>Phase de descente (points oranges)&nbsp;:</b> l'écart vertical parcouru pendant $\Delta t$ augmente de plus en plus. Le mouvement est <b>rectiligne accéléré</b>.</p></li>
<li><p>Pour chaque indice <code>i</code> allant de <code>1</code> à <code>N-1</code>, le test <code>if Y[i-1] &lt; Y[i]:</code> compare l'altitude du point précédent $M_{i-1}$ à celle du point actuel $M_i$&nbsp;: si l'altitude a augmenté ($y_{i-1} < y_i$), la balle monte et on choisit le bleu (<code>#4c72b0</code>)&nbsp;; sinon ($y_{i-1} \geqslant y_i$), elle redescend et on choisit l'orange (<code>#dd8452</code>).</p></li>
</ol>
</div>
</details>

## Vecteurs déplacement {.nt-h2}

<p class="nt-lead">On s'intéresse maintenant aux <b>vecteurs déplacement</b> $\overrightarrow{M_i M_{i+1}}$ reliant deux positions consécutives $M_i$ et $M_{i+1}$. Pour un mouvement vertical selon l'axe $(Oy)$, la coordonnée verticale du vecteur $\overrightarrow{M_i M_{i+1}}$ vaut simplement $y_{i+1} - y_i$.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question 6</p>
<p>Observez le bloc de calcul des vecteurs déplacement dans le programme ci-dessous, puis exécutez-le. Pourquoi a-t-on écrit <code>for i in range(N-1):</code> (soit $N-1$ éléments) plutôt que <code>for i in range(N):</code>&nbsp;?</p>
</div>

{{< runpython lang="pyodide" height="auto"   >}}
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

# 1. Données des positions
g = 9.8
v0 = 5
tmax = 2*v0/g
N = 12
Dt = tmax/(N-2)
T = [Dt*i for i in range(N)]
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]

# 2. Initialisation de la liste de N-1 éléments pour les vecteurs déplacement
MMprime = [0 for i in range(N-1)]

############ CALCUL DES VECTEURS DÉPLACEMENT #############
for i in range(N-1):
    MMprime[i] = Y[i+1] - Y[i]
##########################################################

# 3. Tracés (montée et descente séparées pour la lisibilité)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 9), dpi=120, sharey=True)
for i in range(N//2):
    coul = "#4c72b0"
    ax1.scatter(0, Y[i], c=coul, zorder=2)
    if i < N//2 - 1:
        ax1.annotate('', xy=(0, Y[i] + MMprime[i]), xytext=(0, Y[i]),
                     arrowprops=dict(facecolor='#00AB8E', edgecolor='none', width=2, headwidth=7), zorder=1)
        ax1.text(0.008, Y[i] + MMprime[i]/2 - 0.015, rf'$\overrightarrow{{M_{{{i}}}M_{{{i+1}}}}}$', fontsize=10, color='#00AB8E')
    ax1.text(-0.028, Y[i] - 0.01, rf'$M_{{{i}}}$', fontsize=10, color=coul)
ax1.set_xlim([-0.05, 0.06])
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.set_title("Montée")

for i in range(N//2 - 1, N):
    coul = '#dd8452'
    ax2.scatter(0, Y[i], c=coul, zorder=2)
    ax2.text(-0.028, Y[i] - 0.01, rf'$M_{{{i}}}$', fontsize=10, color=coul)
    if i < N - 1:
        ax2.annotate('', xy=(0, Y[i] + MMprime[i]), xytext=(0, Y[i]),
                     arrowprops=dict(facecolor='#00AB8E', edgecolor='none', width=2, headwidth=7), zorder=1)
        ax2.text(0.008, Y[i] + MMprime[i]/2 - 0.015, rf'$\overrightarrow{{M_{{{i}}}M_{{{i+1}}}}}$', fontsize=10, color='#00AB8E')
ax2.set_xlim([-0.05, 0.06])
ax2.set_xlabel('x (m)')
ax2.set_title("Descente")

plt.tight_layout()
plt.show()
{{< /runpython >}}

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir l'explication sur <code>range(N-1)</code></span></summary>
<div class="nt-d-body">
<p>Entre $N$ points ($M_0, M_1, \dots, M_{N-1}$), il n'y a que <span class="imp">$N - 1$ intervalles</span>&nbsp;: le dernier vecteur déplacement est $\overrightarrow{M_{N-2} M_{N-1}}$.<br>
D'un point de vue informatique, la formule utilise <code>Y[i+1]</code>&nbsp;: si <code>i</code> atteignait la valeur <code>N-1</code>, le programme chercherait à lire <code>Y[N]</code> qui n'existe pas, ce qui déclencherait une erreur (<code>IndexError: list index out of range</code>).</p>
</div>
</details>

## Vecteurs vitesse {.nt-h2}

<p class="nt-lead">On souhaite maintenant calculer et représenter le <b>vecteur vitesse</b> $\vec{v}_i$ en chaque point à partir du vecteur déplacement $\overrightarrow{M_i M_{i+1}}$ et de la durée $\Delta t$ entre deux positions consécutives.</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vecteur vitesse en un point $M_i$</p>
<p class="nt-f-math">$$\vec{v}_i = \dfrac{\overrightarrow{M_i M_{i+1}}}{\Delta t}$$</p>
<div class="nt-f-units"><span>$v_i$ en <b>$\pu{m*s-1}$</b></span><span>$M_i M_{i+1}$ en <b>m</b></span><span>$\Delta t$ en <b>s</b> (variable <code>Dt</code> dans le code)</span></div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 7</p>
<ol class="nt-steps">
<p>Dans la fenêtre ci-dessous, complétez la ligne <code>V[i] = ...</code> permettant de calculer la coordonnée verticale de chaque vecteur vitesse à partir de <code>MMprime[i]</code> et de <code>Dt</code>, puis exécutez le programme pour tracer les vecteurs vitesse.</p>
</div>

{{< runpython lang="pyodide" height="auto"    >}}
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

# 1. Données et vecteurs déplacement
g = 9.8
v0 = 5
tmax = 2*v0/g
N = 12
Dt = tmax/(N-2)
T = [Dt*i for i in range(N)]
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]
MMprime = [Y[i+1] - Y[i] for i in range(N-1)]

# 2. Initialisation de la liste des vecteurs vitesse :
V = [0 for i in range(N-1)]

############ PARTIE À COMPLÉTER (Question 7) ############
for i in range(N-1):
    V[i] = 0 # <-- remplacer 0 par la formule utilisant MMprime[i] et Dt
#########################################################

# 3. Positions des extrémités des vecteurs (échelle 1/15) et tracés :
echelle = 1/15
finV = [Y[i] + V[i]*echelle for i in range(N-1)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 9), dpi=120, sharey=True)
for i in range(N//2):
    coul = "#4c72b0"
    ax1.scatter(0, Y[i], c=coul, zorder=2)
    if i < N//2 - 1:
        ax1.annotate('', xy=(0, finV[i]), xytext=(0, Y[i]),
                     arrowprops=dict(facecolor='#FFD932', edgecolor='#FEAE00', width=2, headwidth=7), zorder=1)
        ax1.text(0.008, Y[i] + V[i]*echelle/2, f'{abs(V[i]):.1f} m/s', fontsize=9, color='#D97706', fontweight='bold')
    ax1.text(-0.028, Y[i] - 0.01, rf'$M_{{{i}}}$', fontsize=10, color=coul)
ax1.set_xlim([-0.05, 0.06])
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.set_title("Montée")

for i in range(N//2 - 1, N):
    coul = '#dd8452'
    ax2.scatter(0, Y[i], c=coul, zorder=2)
    ax2.text(-0.028, Y[i] - 0.01, rf'$M_{{{i}}}$', fontsize=10, color=coul)
    if i < N - 1:
        ax2.annotate('', xy=(0, finV[i]), xytext=(0, Y[i]),
                     arrowprops=dict(facecolor='#FFD932', edgecolor='#FEAE00', width=2, headwidth=7), zorder=1)
        ax2.text(0.008, Y[i] + V[i]*echelle/2, f'{abs(V[i]):.1f} m/s', fontsize=9, color='#D97706', fontweight='bold')
ax2.set_xlim([-0.05, 0.06])
ax2.set_xlabel('x (m)')
ax2.set_title("Descente")

plt.tight_layout()
plt.show()
{{< /runpython >}}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 8</p>
<p>Que remarquez-vous concernant la direction, le sens et la norme des vecteurs vitesse au cours du mouvement&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir le code de la question 7 et les observations (question 8)</span></summary>
<div class="nt-d-body">
<ol class="nt-steps" start="7">
<li><p><b>Ligne à écrire&nbsp;:</b></p>
<pre><code class="python">for i in range(N-1):
    V[i] = MMprime[i] / Dt</code></pre>
<p class="nt-note">Dans ce programme orienté vers le haut, <code>V[i]</code> est positif à la montée ($\vec{v}_i$ vers le haut) et négatif à la descente ($\vec{v}_i$ vers le bas).</p></li>
<li><p><b>Observations&nbsp;:</b><br>
• Lors de la <b>montée</b>, les vecteurs vitesse sont verticaux, dirigés vers le haut, et leur norme diminue régulièrement (de $\pu{4,5 m*s-1}$ jusqu'à $\pu{0,5 m*s-1}$ avant le sommet).<br>
• Lors de la <b>descente</b>, les vecteurs vitesse sont verticaux, dirigés vers le bas, et leur norme augmente régulièrement.<br>
• <b>Symétrie&nbsp;:</b> à une même altitude, la balle possède exactement la même valeur de vitesse à la montée et à la descente (seul le sens du vecteur change).</p></li>
</ol>
</div>
</details>

## Vecteurs variation de vitesse et lien avec les forces {.nt-h2}

<p class="nt-lead">On étudie enfin le <b>vecteur variation de vitesse</b> entre deux positions successives&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vecteur variation de vitesse</p>
<p class="nt-f-math">$$\overrightarrow{\Delta v}_i = \vec{v}_{i+1} - \vec{v}_i$$</p>
<div class="nt-f-units"><span>$\Delta v_i$ en <b>$\pu{m*s-1}$</b></span><span>Il y a $N-1$ vecteurs vitesse, donc <b>$N-2$</b> vecteurs variation de vitesse</span></div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 9</p>
<ol class="nt-steps">
<p>Dans le code ci-dessous, complétez la ligne <code>DV[i] = ...</code> en vous inspirant du calcul fait précédemment pour les déplacements, puis exécutez la cellule.</p></li>
</div>


{{< runpython lang="pyodide" height="auto"    >}}
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

# 1. Données, déplacements et vitesses
g = 9.8
v0 = 5
tmax = 2*v0/g
N = 12
Dt = tmax/(N-2)
T = [Dt*i for i in range(N)]
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]
MMprime = [Y[i+1] - Y[i] for i in range(N-1)]
V = [MMprime[i]/Dt for i in range(N-1)]

# 2. Initialisation des N-2 vecteurs "variation de vitesse" :
DV = [0 for i in range(N-2)]

############ PARTIE À COMPLÉTER (Question 9) ############
for i in range(N-2):
    DV[i] = 0 # <-- remplacer 0 par la formule utilisant la liste V
#########################################################

# 3. Positions des extrémités des vecteurs (échelle 1/10) et tracés :
echelle = 1/10
finDV = [Y[i] + DV[i]*echelle for i in range(N-2)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 9), dpi=120, sharey=True)
for i in range(N//2):
    coul = "#4c72b0"
    ax1.scatter(0, Y[i], c=coul, zorder=2)
    if i <= N//2 - 1:
        ax1.annotate('', xy=(0, finDV[i]), xytext=(0, Y[i]),
                     arrowprops=dict(color='#1DB100', width=2, headwidth=7), zorder=1)
        ax1.text(0.008, Y[i] + DV[i]*echelle/2 - 0.015, rf'$\overrightarrow{{\Delta v_{{{i}}}}}=\vec{{v}}_{{{i+1}}}-\vec{{v}}_{{{i}}}$', fontsize=9, color='#1DB100')
    ax1.text(-0.028, Y[i] - 0.01, rf'$M_{{{i}}}$', fontsize=10, color=coul)
ax1.set_xlim([-0.045, 0.085])
ax1.set_ylim([0.3, max(Y) + 0.1])
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.set_title("Montée")

for i in range(N//2 - 1, N):
    coul = '#dd8452'
    ax2.scatter(0, Y[i], c=coul, zorder=2)
    ax2.text(-0.028, Y[i] - 0.01, rf'$M_{{{i}}}$', fontsize=10, color=coul)
    if i < N - 2:
        ax2.annotate('', xy=(0, finDV[i]), xytext=(0, Y[i]),
                     arrowprops=dict(color='#1DB100', width=2, headwidth=7), zorder=1)
        ax2.text(0.008, Y[i] + DV[i]*echelle/2 - 0.015, rf'$\overrightarrow{{\Delta v_{{{i}}}}}=\vec{{v}}_{{{i+1}}}-\vec{{v}}_{{{i}}}$', fontsize=9, color='#1DB100')
ax2.set_xlim([-0.045, 0.085])
ax2.set_xlabel('x (m)')
ax2.set_title("Descente")

plt.tight_layout()
plt.show()
{{< /runpython >}}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 10</p>
<p>En utilisant la contraposée du principe d'inertie (et le lien entre variation de vitesse et forces), que pouvez-vous déduire de l'allure des vecteurs $\overrightarrow{\Delta v}_i$ tracés sur le graphique&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir le code de la question 9 et la déduction physique (question 10)</span></summary>
<div class="nt-d-body">
<ol class="nt-steps" start="9">
<li><p><b>Ligne à écrire&nbsp;:</b></p>
<pre><code class="python">for i in range(N-2):
    DV[i] = V[i+1] - V[i]</code></pre></li>
<li><p><b>Déduction à partir du principe d'inertie&nbsp;:</b><br>
• On observe que le vecteur vitesse varie ($\overrightarrow{\Delta v}_i \neq \vec{0}$)&nbsp;: d'après le principe d'inertie, les forces qui s'exercent sur la balle <b>ne se compensent pas</b>.<br>
• De plus, aussi bien pendant la montée que pendant la descente, tous les vecteurs $\overrightarrow{\Delta v}_i$ ont la <b>même direction</b> (verticale), le <b>même sens</b> (vers le bas) et la <b>même norme</b>&nbsp;: la somme des forces qui s'exercent sur la balle est donc une force constante, verticale et dirigée vers le bas. On retrouve bien les caractéristiques du seul <span class="imp">poids $\vec{P}$</span> de la balle&nbsp;!</p></li>
</ol>
</div>
</details>

### Vérification numérique des valeurs {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 11</p>
Dans la fenêtre ci-dessous, écrivez les instructions <code>print(...)</code> permettant d'afficher les listes <code>T</code>, <code>Y</code>, <code>MMprime</code>, <code>V</code> et <code>DV</code>.
</div>
<p></p>

{{< runpython height="auto"    >}}
g = 9.8
v0 = 5
tmax = 2*v0/g
N = 12
Dt = tmax/(N-2)
T = [Dt*i for i in range(N)]
Y = [v0*t - 1/2*g*t**2 + 1 for t in T]
MMprime = [Y[i+1] - Y[i] for i in range(N-1)]
V = [MMprime[i]/Dt for i in range(N-1)]
DV = [V[i+1] - V[i] for i in range(N-2)]

####### CODE POUR AFFICHER LES LISTES ########




##############################################
{{< /runpython >}}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 12</p>
<p>Que constatez-vous en observant les valeurs numériques de la liste <code>DV</code>&nbsp;?</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions 13</p>
<p>Vérifiez à la main le calcul de la norme $\|\overrightarrow{\Delta v}_2\|$ à partir des valeurs de la liste <code>V</code>.</p></li>

</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir le code d'affichage et les réponses aux questions 12 et 13</span></summary>
<div class="nt-d-body">
<ol class="nt-steps" start="11">
<li><p><b>Code d'affichage&nbsp;:</b></p>
<pre><code class="python">print("T =", T)
print("Y =", Y)
print("MMprime =", MMprime)
print("V =", V)
print("DV =", DV)</code></pre></li>
<li><p><b>Question 11&nbsp;:</b> Toutes les valeurs de la liste <code>DV</code> sont constantes et égales à $\pu{-1,0 m*s-1}$ (aux minuscules arrondis numériques près de Python, par exemple <code>-0.9999999999999996</code>). Le signe «&nbsp;$-$&nbsp;» indique que le vecteur $\overrightarrow{\Delta v}_i$ est toujours orienté vers le bas, et sa norme vaut $\|\overrightarrow{\Delta v}_i\| = \pu{1,0 m*s-1}$.</p></li>
<li><p><b>Question 12&nbsp;:</b> Par définition, $\overrightarrow{\Delta v}_2 = \vec{v}_3 - \vec{v}_2$ (soit <code>DV[2] = V[3] - V[2]</code> en Python).<br>
En lisant les 3<sup>e</sup> et 4<sup>e</sup> éléments de la liste <code>V</code>&nbsp;: $v_2 = \pu{2,5 m*s-1}$ et $v_3 = \pu{1,5 m*s-1}$ (tous deux dirigés vers le haut).<br>
Sur l'axe vertical orienté vers le haut&nbsp;: $\Delta v_2 = v_3 - v_2 = 1{,}5 - 2{,}5 = \pu{-1,0 m*s-1}$, d'où $\|\overrightarrow{\Delta v}_2\| = \pu{1,0 m*s-1}$.</p></li>
</ol>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Lors d'une <b>chute libre</b>, le système n'est soumis qu'à son <span class="imp nt-hole">poids $\vec{P}$</span> (vertical, vers le bas, de valeur constante $P = m \times g$).</li>
<li>Quelle que soit la phase du mouvement (montée ou descente), le vecteur variation de vitesse $\overrightarrow{\Delta v}$ entre deux instants séparés de $\Delta t$ a la <span class="imp nt-hole">même direction</span> et le <span class="imp nt-hole">même sens</span> que la somme des forces extérieures&nbsp;: il est donc <b>toujours vertical, dirigé vers le bas et de norme constante</b>.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi trouve-t-on exactement $\|\overrightarrow{\Delta v}\| = \pu{1,0 m*s-1}$ dans ce programme&nbsp;?</span></summary>
<div class="nt-d-body">
<p>En classe de Première et de Terminale, la deuxième loi de Newton montre que pour une chute libre pendant une durée $\Delta t$, le vecteur variation de vitesse vérifie&nbsp;:</p>
<p style="text-align:center;">$$m\,\overrightarrow{\Delta v} = \vec{P}\times \Delta t = m\,\vec{g}\times \Delta t \quad\Longleftrightarrow\quad \overrightarrow{\Delta v} = \vec{g}\times \Delta t$$</p>
<p>Dans notre programme, l'intervalle de temps vaut $\Delta t = \dfrac{t_\text{max}}{N - 2} = \dfrac{2\,v_0 / g}{10} = \dfrac{2 \times 5}{10 \times g} = \dfrac{1}{g} \approx \pu{0,102 s}$.<br>
La norme de $\overrightarrow{\Delta v}$ vaut donc $g \times \Delta t = g \times \dfrac{1}{g} = \pu{1,0 m*s-1}$&nbsp;!</p>
</div>
</details>