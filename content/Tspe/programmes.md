---
title: "Programmes"
date: 2021-03-06T14:23:56+01:00
weight : 40
hidden: true
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
</style>

# Programmes

Ensemble des codes python rencontrés (dans les TP, activités, exercices, etc.) rangés par chapitre.


## Titrages

### Exercice «&nbsp;[titrage agneaux](/act-titragets1.pdf)&nbsp;»

Code du sujet&nbsp;:

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
# Simulation du titrage dont la réaction support est de la forme
# a A + b B -> c C + H2O
# a, b, c et d sont les coefficients stoechiométriques
from matplotlib import pyplot as plt

a = # nombre stoechiométrique de l'espèce à titrer A COMPLETER
b = # nombre stoechiométrique de l'espèce titrante A COMPLETER
c = # nombre stoechiométrique du produit de la réaction A COMPLETER
Ca = 0.14  # concentration de la solution à titrer (mol/L)
Va = 10.0  # volume de la solution à titrer (mL)
Cb = 0.10  # concentration de la solution titrante (mol/L)
Veq = # Calcul du volume à l’équivalence (mL) A COMPLETER
pasVb = 0.1

nA, nB, nC, nS_A, nS_B = [], [], [], [], []
v = [i/10 for i in range(250)]
for Vb in v:
    if Vb < Veq:
        nA.append(Ca*Va - Cb*Vb*a/b)
        # A COMPLETER AVEC LE CALCUL DE nB
        nC.append(c/b*Cb*Vb)
        nS_A.append(Ca*Va)
        nS_B.append(Cb*Vb)
    else:
        nA.append(0)
        nB.append(Cb*Vb - Cb*Veq)
        nC.append(c/b*Cb*Veq)
        nS_A.append(Ca*Va)
        nS_B.append(Cb*Vb)

# Code ajouté pour réaliser le tracer
plt.plot(v,nA,label=r"$n_A(V)$")
plt.plot(v,nB,label=r"$n_B(V)$")
plt.plot(v,nC,label=r"$n_C(V)$")
plt.xlabel("Volume versé de solution titrante (mL)")
plt.ylabel("Quantité de matière (mmol)")
plt.legend()
plt.show()
{{< /runpython >}}


{{%notice type="tip" collapse="true" round="true"%}}
Code utilisé pour tracer la figure de l'énoncé comprenant l'ensemble des graphes&nbsp;:

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
# Simulation du titrage dont la réaction support est de la forme
# a A + b B -> c C + H2O
# a, b, c et d sont les coefficients stoechiométriques
from matplotlib import pyplot as plt

a = 1
b = 1
c = 1
Ca = 0.14  # concentration de la solution à titrer (mol/L)
Va = 10.0  # volume de la solution à titrer (mL)
Cb = 0.10  # concentration de la solution titrante (mol/L)
Veq =  Ca*Va/Cb # Calcul du volume à l’équivalence (mL) A COMPLETER
pasVb = 0.1

nA, nB, nC, nS_A, nS_B = [], [], [], [], []
v = [i/10 for i in range(250)]
for Vb in v:
    if Vb < Veq:
        nA.append(Ca*Va - Cb*Vb*a/b)
        nB.append(0)
        nC.append(c/b*Cb*Vb)
        nS_A.append(Ca*Va)
        nS_B.append(Cb*Vb)
    else:
        nA.append(0)
        nB.append(Cb*Vb - Cb*Veq)
        nC.append(c/b*Cb*Veq)
        nS_A.append(Ca*Va)
        nS_B.append(Cb*Vb)

# Tracé des graphes
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.flatten()

# Taille des labels et des axes
label_fontsize = 16
axis_fontsize = 12

# Figure 1 : nB en fonction de v
axes[0].plot(v, nB, color='green', label="figure 1")
axes[0].set_xlabel("Volume versé de solution titrante (mL)", fontsize=label_fontsize)
axes[0].set_ylabel("Quantité de matière (mmol)", fontsize=label_fontsize)
axes[0].tick_params(axis='both', labelsize=axis_fontsize)
axes[0].legend(fontsize=label_fontsize)
axes[0].grid(True)

# Figure 2 : nS_A en fonction de v
axes[1].plot(v, nS_A, color='black', label="figure 2")
axes[1].set_xlabel("Volume versé de solution titrante (mL)", fontsize=label_fontsize)
axes[1].set_ylabel("Quantité de matière (mmol)", fontsize=label_fontsize)
axes[1].tick_params(axis='both', labelsize=axis_fontsize)
axes[1].legend(fontsize=label_fontsize)
axes[1].grid(True)

# Figure 3 : nC en fonction de v
axes[2].plot(v, nC, color='blue', label="figure 3")
axes[2].set_xlabel("Volume versé de solution titrante (mL)", fontsize=label_fontsize)
axes[2].set_ylabel("Quantité de matière (mmol)", fontsize=label_fontsize)
axes[2].tick_params(axis='both', labelsize=axis_fontsize)
axes[2].legend(fontsize=label_fontsize)
axes[2].grid(True)

# Figure 4 : nS_B en fonction de v
axes[3].plot(v, nS_B, color='black', label="figure 4")
axes[3].set_xlabel("Volume versé de solution titrante (mL)", fontsize=label_fontsize)
axes[3].set_ylabel("Quantité de matière (mmol)", fontsize=label_fontsize)
axes[3].tick_params(axis='both', labelsize=axis_fontsize)
axes[3].legend(fontsize=label_fontsize)
axes[3].grid(True)

# Figure 5 : nA en fonction de v
axes[4].plot(v, nA, color='red', label="figure 5")
axes[4].set_xlabel("Volume versé de solution titrante (mL)", fontsize=label_fontsize)
axes[4].set_ylabel("Quantité de matière (mmol)", fontsize=label_fontsize)
axes[4].tick_params(axis='both', labelsize=axis_fontsize)
axes[4].legend(fontsize=label_fontsize)
axes[4].grid(True)

# Supprime le graphique vide (en bas à droite)
fig.delaxes(axes[5])

# Ajuste les espaces entre les sous-graphiques
plt.tight_layout()
plt.savefig("act-titrage.png",
            transparent=True,
            bbox_inches='tight',
            pad_inches=0,
            dpi=300)
plt.show()
{{< /runpython >}}

{{%/notice%}}


### TP [titrage conductimétrique](/tp-titrageconduct.pdf)

Code du TP titrage conductimétrique d'un déboucheur.<br>
Le but du code est de montrer que la formule de propagation des erreurs (détermination de type B d'une incertitude-type) donne bien la même réponse qu'une simulation Monte-Carlo.

Dans la simulation Monte-Carlo, on tire au hasard chaque valeur expérimentale en respectant l'incertitude-type indiquée pour cette grandeur puis on calcule la grandeur composée (ici la concentration du déboucheur `CB`).<br>
On recommence l'opération 500\,000 fois et on calcule ensuite l'écart-type expérimental des valeurs de `CB` obtenues (et on trace aussi un histogramme de ces valeurs).<br>
L'écart-type, estimation de l'incertitude-type sur `CB`, est ensuite comparée au résultat donné par la formule de propagation des erreurs.

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Renvoie une valeur aléatoire de la variable L[0] d'incertitude-type L[1]
def Alea(L):
    tirage = np.random.normal()  # Tirage entre -♾️ et +♾️ (loi normale)
    return L[0] + L[1] * tirage

# Grandeurs mesurées et leurs incertitudes-type
Vf = (1000.0e-3, 0.4e-3  )
Vp = (2.00e-3  , 0.010e-3)
CA = (1.00e-2  , 0.01e-2 )
VB = (10.00e-3 , 0.04e-3 )
VE = (         , 0.1e-3  ) # À COMPLÉTER

# Méthode de Monte Carlo pour obtenir l'incertitude-type sur CB:
################################################################

L_CB = [] # Liste des concentration CB obtenues
N_iterations = 500000

for j in range(N_iterations):
    Alea_CB = Alea(Vf)/Alea(Vp)*Alea(CA)*Alea(VE)/Alea(VB) # Calcul d'un CB aléatoire
    L_CB.append(Alea_CB)

u_CB = np.std(L_CB, ddof=1) # calcule l'écart-type expérimental des CB obtenues

################################################################

# Histogramme avec Seaborn
sns.set_theme()
sns.set_context("talk")
plt.figure(figsize=(6,4),dpi=200)
sns.set_context("paper")
sns.histplot(L_CB, kde=False, bins=50)
plt.xlabel('C_B')
plt.ylabel('Effectif')
plt.title(f'Pour {N_iterations} iterations')
plt.tight_layout()
#plt.savefig("histo.png",transparent=True,bbox_inches='tight',pad_inches=0,dpi=300)
plt.show()

# Vérification par la formule :
#### À VOUS D'ÉCRIRE LES FORMULES ####
#### Aide : la valeur de Vf est donnée par Vf[0] et son incertitude par Vf[1]
CB =
UCB =

# Affichage des résultats
print(f"Concentration en hydroxyde de sodium du déboucheur : C_B = {CB :.3E} mol/L")
print(f"Incertitude-type à partir de la méthode de Monte-Carlo : u(C_B) = {u_CB:.1E} mol/L")
print(f"Incertitude-type à partir de la formule de propagation : u(C_B) = {UCB:.1E} mol/L")
{{< /runpython >}}

{{% notice type="correction" collapse="true" round="true" %}}
<pre><code class="python">CB = Vf[0]/Vp[0]*CA[0]*VE[0]/VB[0]
UCB = CB*np.sqrt((Vf[1]/Vf[0])**2+(Vp[1]/Vp[0])**2+(CA[1]/CA[0])**2+(VB[1]/VB[0])**2+(VE[1]/VE[0])**2)
</code></pre>
{{%/notice%}}



---




## Cinétique chimique 

### Activité «&nbsp;[Dégradation d'un produit de contraste](/act-cinet.pdf)&nbsp;»

Ajustement de l'évolution de la concentration par une exponentielle décroissante dont on détermine les paramètres idéaux&nbsp;:

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
from scipy.optimize import curve_fit

# Données
temps = np.array([0,10,20,30,40,50,60,70,80,90,100,110])
Iopamidol = np.array([10.0,7.74,6.22,5.24,4.36,3.67,2.98,2.43,1.99,1.66,1.39,1.11])

def	func(x, a, b):
    return a * np.exp(-b*x)            # modèle de notre fonction

# modélisation des données expérimentale par notre fonction
popt, pcov = curve_fit(func, temps, Iopamidol, bounds=(0, [15, 0.1]))

# Récupération des valeurs et incertitudes
a, b = popt
a_err = np.sqrt(pcov[0,0])
b_err = np.sqrt(pcov[1,1])

# Fonction pour déterminer le nombre de décimales en fonction de l'écart-type
def ecriture_resultat(valeur, ecarttype):
    # Obtenir le nombre de décimales pour l'incertitude (2 chiffres significatifs)
    ecarttype_str = f"{ecarttype:.2e}"
    decimales = -int(np.floor(np.log10(ecarttype)))  # position de la première décimale significative
    decimales += 1 # pour garder 2 chiffres significatifs sur l'écart-type

    # Formater la valeur avec le bon nombre de décimales
    valeur_str = f"{valeur:.{max(0, decimales)}f}"
    ecarttype_str = f"{ecarttype:.{max(0, decimales)}f}"

    return f"{valeur_str} ± {ecarttype_str}"

# Affichage des résultats
print(f"a = {ecriture_resultat(a, a_err)}")
print(f"b = {ecriture_resultat(b, b_err)}")
{{< /runpython >}}


Tracé de l'évolution temporelle de la concentration et de sa modélisation&nbsp;:

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

# Données
temps = np.array([0,10,20,30,40,50,60,70,80,90,100,110])
Iopamidol = np.array([10.0,7.74,6.22,5.24,4.36,3.67,2.98,2.43,1.99,1.66,1.39,1.11])

def	func(x, a, b):
    return a * np.exp(-b*x)            # modèle de notre fonction

# modélisation des données expérimentale par notre fonction
popt, pcov = curve_fit(func, temps, Iopamidol, bounds=(0, [15, 0.1]))

# Récupération des valeurs et incertitudes
a, b = popt
a_err = np.sqrt(pcov[0,0])
b_err = np.sqrt(pcov[1,1])

t_fit = np.linspace(temps.min(), temps.max(), 400)
y_fit = func(t_fit, a, b)

plt.figure(figsize=(12, 6),dpi=150)
plt.plot(temps, Iopamidol, 'o', label="Données expérimentales")      # points
plt.plot(t_fit, y_fit, 'r--', label="Ajustement : $a e^{-bt}$")      # courbe rouge pointillée

plt.xlabel("Temps (s)")
plt.ylabel("Concentration (μmol/L)")
plt.title("Iopamidol : données + ajustement exponentiel")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
{{< /runpython >}}


Au lieu d'ajuster les points expérimentaux par une fonction exponentielle, on aurait pu prendre le logarithme des concentrations et réaliser un ajustement linéaire&nbsp;:
 
 
 {{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

# Données
temps = np.array([0,10,20,30,40,50,60,70,80,90,100,110])
Iopamidol = np.array([10.0,7.74,6.22,5.24,4.36,3.67,2.98,2.43,1.99,1.66,1.39,1.11])

# On prends le logarithme de chaque concentration
logIop = np.log(Iopamidol)

def	lin(x, a, b):
    return a * x + b            # modèle affine

# modélisation des données expérimentale par notre fonction
popt, pcov = curve_fit(lin, temps, logIop)

a, b = popt
a_err = np.sqrt(pcov[0,0])
b_err = np.sqrt(pcov[1,1])

# Fonction pour déterminer le nombre de décimales en fonction de l'écart-type
def ecriture_resultat(valeur, ecarttype):
    # Obtenir le nombre de décimales pour l'incertitude (2 chiffres significatifs)
    ecarttype_str = f"{ecarttype:.2e}"
    decimales = -int(np.floor(np.log10(ecarttype)))  # position de la première décimale significative
    decimales += 1 # pour garder 2 chiffres significatifs sur l'écart-type

    # Formater la valeur avec le bon nombre de décimales
    valeur_str = f"{valeur:.{max(0, decimales)}f}"
    ecarttype_str = f"{ecarttype:.{max(0, decimales)}f}"

    return f"{valeur_str} ± {ecarttype_str}"

# Affichage des résultats
print(f"a = {ecriture_resultat(a, a_err)}")
print(f"b = {ecriture_resultat(b, b_err)}")

# Tracer
t_fit = np.linspace(temps.min(), temps.max(), 400)
y_fit = lin(t_fit, a, b)

plt.figure(figsize=(12, 6),dpi=150)
plt.plot(temps, logIop, 'o', label=r"Données expérimentales")                # logarithme des données
plt.plot(t_fit, y_fit, 'r--', label=fr"Ajustement : ${a:.2e} t + {b:.2e}$")  # courbe rouge pointillée

plt.xlabel("Temps (s)")
plt.ylabel(r"$\ln(\mathrm{[Iop]}(t))$")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
{{< /runpython >}}

On peut aussi tracer l'évolution temporelle de la vitesse de disparition, mais pour cela, il faut calculer numériquement la dérivée temporelle de la concentration.

{{%notice type="info" title="Rappel dérivée numérique" round="true" %}}
Soit une grandeur $x$ variant en fonction du temps.<br>
Supposons que l'on ait une liste `X` de N valeurs de $x$ correspondant à N valeurs temporelles enregistrées dans une liste `T`.

Une liste de N-1 valeurs approximant numériquement la **dérivée** de $x$ par rapport au temps s'obtient grâce à la boucle suivante&nbsp;:

<pre style="margin-top:-0.5em;margin-bottom:-0.5em;">
<code class="python" style="border-radius:5px;">derX = []
for i in range(N-1):
    derX.append((X[i+1]-X[i])/(T[i+1]-T[i]))</code></pre>

Ce n'est rien d'autre que l'approximation $\frac{\mathrm d x}{\mathrm d t}\approx \frac{\Delta x}{\Delta t}=\frac{x(t+\Delta t)-x(t)}{\Delta t}$.

Exemple :
{{< runpython lang="pyodide" height="auto" theme="dark">}}
import numpy as np
import matplotlib.pyplot as plt

N = 1000
T = np.linspace(-5,5,N)
X = T**2 - 5

derX = []
for i in range(N-1):
    derX.append((X[i+1]-X[i])/(T[i+1]-T[i]))

plt.plot(T, X, label = "X")
plt.plot(T[:-1], derX, label="dérivée de X")
plt.legend()
plt.grid()
{{< /runpython >}}
{{%/notice%}}

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
from matplotlib import pyplot as plt

# Données
temps = np.array([0,10,20,30,40,50,60,70,80,90,100,110])
Iopamidol = np.array([10.0,7.74,6.22,5.24,4.36,3.67,2.98,2.43,1.99,1.66,1.39,1.11])

# Construction de la vitesse volumique de disparition à partir de la dérivée de la concentration
vd = []
for i in range(len(temps)-1):
    vd.append(-(Iopamidol[i+1]-Iopamidol[i])/(temps[i+1]-temps[i]))

plt.figure(figsize=(12, 6),dpi=150)
plt.plot(temps[:-1],vd,'--o', label=r"$v_{d,\mathrm{[Iop]}}(t)$")
plt.xlabel("temps (s)")
plt.ylabel("vitesse de disparition (μmmol/L/s)")
plt.legend()
{{< /runpython >}}

<br>

---

## Piles

### Exercice «&nbsp;[pile zinc-air](/act-pilezincair.pdf)&nbsp;»

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import matplotlib.pyplot as plt

# Paramètres (valeurs moyennes et incertitudes-type)
a_mean = 1.09    # mA
a_std  = 0.03    # mA
b_mean = 13.2    # mA
b_std  = 0.9     # mA
I_exp_mean = 31.7  # mA
I_exp_std  = 0.2   # mA

# Nombre de tirages Monte-Carlo
N = 100_000

# Génération des échantillons aléatoires selon des lois normales
a_samples = np.random.normal(a_mean, a_std, N)
#a_samples = np.random.uniform(a_mean-a_std, a_mean+a_std, N)
b_samples = np.random.normal(b_mean, b_std, N)
#b_samples = np.random.uniform(b_mean-b_std, b_mean+b_std, N)
I_exp_samples = np.random.normal(I_exp_mean, I_exp_std, N)
#I_exp_samples = np.random.uniform(I_exp_mean-I_exp_std, I_exp_mean+I_exp_std, N)

# Calcul de x_O2 pour chaque échantillon
xO2_samples = (I_exp_samples - b_samples) / a_samples

# Calcul des statistiques sur la distribution obtenue
xO2_mean = np.mean(xO2_samples)
xO2_std = np.std(xO2_samples, ddof=1)  # ddof=1 pour un estimateur sans biais

# Affichage des résultats
print(f"Estimation de x_O2 : {xO2_mean}")
print(f"Incertitude-type sur x_O2 : {xO2_std}")

# Optionnel : affichage graphique de la distribution
plt.hist(xO2_samples, bins=30, density=False, alpha=0.6, color='g')
plt.title("Pour 100 000 itérations")
plt.xlabel("pourcentage de dioxygène")
plt.ylabel("effectifs")
plt.savefig("histo.png",transparent=True,bbox_inches='tight',pad_inches=0,dpi=300)
plt.show()
{{< /runpython >}}

{{%notice type="note" title="Remarque :" round="true" collapse="true" %}}
Dans le vrai sujet (sujet 0 2021), l'incertitude-type est de 0,42. Plutôt bizarre car incohérent avec la formule de propagation des incertitudes :
$x_\mathrm{O_2}=\frac{I_\mathrm{exp}-b}{a}$<br>
$\begin{aligned}
\Rightarrow \frac{u(x_\mathrm{O_2})}{x_\mathrm{O_2}}&=\sqrt{\left(\frac{u(I_\mathrm{exp}-b)}{I_\mathrm{exp}-b}\right)^2+\left(\frac{u(a)}{a}\right)^2}\\\\
&=\sqrt{\left(\frac{\sqrt{u(I_\mathrm{exp})^2+u(b)^2}}{I_\mathrm{exp}-b}\right)^2+\left(\frac{u(a)}{a}\right)^2}
\end{aligned}$
<br>
Ça donne :<br>
$
\begin{aligned}
u(x_\mathrm{O_2})&=\frac{31,7 - 13,2}{1,09}\times\sqrt{\left(\frac{\sqrt{0,2^2 + 0,9^2}}{31,7 - 13,2}\right)^2 + \left(\frac{0,03}{1,09}\right)^2}\\\\
&=0,97 \text{ mA}
\end{aligned}
$

Ou en utilisant Python&nbsp;:

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np

# Paramètres (valeurs moyennes et incertitudes-type)
a_mean = 1.09      # mA
a_std  = 0.03      # mA
b_mean = 13.2      # mA
b_std  = 0.9       # mA
I_exp_mean = 31.7  # mA
I_exp_std  = 0.2   # mA

incert_type_xO2 = (I_exp_mean-b_mean)/a_mean*np.sqrt((np.sqrt(I_exp_std**2+b_std**2)/(I_exp_mean-b_mean))**2+(a_std/a_mean)**2)
print(f"incertitude-type sur le pourcentage en dioxygène obtenue par le calcul : {incert_type_xO2:.2f} mA")
{{< /runpython >}}

{{%/notice%}}

<br>

---

## Constante d'acidité $K_a$

### Activité «&nbsp;[Taux d'avancement](/act-kapython.pdf)&nbsp;»

Compléter le code de la fonction `final` permettant de retourner à la fois le taux d'avancement et le pH à l'équilibre.<br>
<u>Rq</u> : on obtient la racine carrée grâce à `np.sqrt()` et le logarithme décimal grâce à `np.log10()`.


{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

liste_pKa = [-1.8, -1.2, 1.2, 3.8, 4.8, 9.2]
C = np.linspace(0, 0.01, 2000)

# définition de la fonction final (à compléter)
def final(a,b,c):
    if a == 0:
        return ..., ... # tau , pH (pour C = 0 puisque a = C)
    Delta = ...
    tau = ... # seule solution positive
    pH = ...
    return tau, pH

# Styles noir et blanc
sns.set_theme()
styles = [
    {"ls": "-",  "marker": "x"},     # ligne continue
    {"ls": "--", "marker": "v"},     # tirets
    {"ls": "-.", "marker": None},    # tiret‑point
    {"ls": ":",  "marker": None},    # pointillés
    {"ls": "-",  "marker": "o"},     # continue + cercles
    {"ls": "--", "marker": "s"},     # tirets + carrés
]

# ---------- Figure 1 : τ(C) ----------
plt.figure(figsize=(12, 6), dpi=150)
for idx, pKa in enumerate(liste_pKa):
    b = 10 ** (-pKa)
    tau_vals = [final(c, b, -b)[0] for c in C]
    st = styles[idx]
    plt.plot(C, tau_vals,
             label=f"pKa = {pKa}",
             linestyle=st["ls"],
             marker=st["marker"],
             markevery=150,
             markersize=5)
plt.xlabel("Concentration (mol/L)")
plt.ylabel(r"$\tau$ d'avancement")
plt.legend(title="Courbes")
plt.tight_layout()
plt.show()

# ---------- Figure 2 : pH(C) ----------
plt.figure(figsize=(12, 6), dpi=150)
for idx, pKa in enumerate(liste_pKa):
    b = 10 ** (-pKa)
    pH_vals = [final(c, b, -b)[1] for c in C]
    st = styles[idx]
    plt.plot(C, pH_vals,
             label=f"pKa = {pKa}",
             linestyle=st["ls"],
             marker=st["marker"],
             markevery=150,
             markersize=5)
plt.xlabel("Concentration (mol/L)")
plt.ylabel("pH")
plt.legend()
plt.tight_layout()
plt.show()
{{< /runpython >}}

{{%notice type="tip" title="Bizarrerie" round="true"%}}
Pourquoi le pH dépasse-t-il 7 pour les petites concentrations de l'acide de pKa élevé&nbsp;?<br>
C'est dû à notre modèle incomplet.<br>
On a négligé l'autoprotolyse de l'eau. La prendre en compte transforme l'équation en un polynôme de degré 3.<br>
La condition d'électroneutralité permet d'écrire&nbsp;:</br>
$[\mathrm H^+] = [\mathrm A^-] + [\mathrm{OH}^-]$ et avec $[\mathrm{OH}^-] = \frac{K_w}{[\mathrm{H_3O^+}]}$, et on obtient alors&nbsp;:<br>
$x^{3}+K_a\\,x^{2}-\bigl(K_w+K_a\\,C\bigr)\\,x-K_a\\,K_w = 0$ où $x=[\mathrm H_3O^+]$.<br>
La seule racine positive permet d'obtenir le pH et il est bien acide ($<7$) cette fois-ci.
{{%/notice%}}


### Activité «&nbsp;[Diagramme de distribution](/act-diagdistrib.pdf)&nbsp;»

Compléter le code de la fonction `pAH`. La fonction doit retourner la valeur de la proportion de la forme acide donnée à la question 3.

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pH = np.linspace(0,14,1000)
pKa = 4.8

# Fonction pAH
def pAH(pH,pKa):
    return ... # code à compléter

# Tracé
sns.set_theme()
plt.figure(figsize=(12, 6), dpi=300)
plt.plot(pH,pAH(pH,pKa),':', c='#EE220C', label='acide')
plt.plot(pH,1-pAH(pH,pKa),':', c='#0076BA', label='base')
plt.xlabel('pH')
plt.ylabel('proportions')
plt.legend()
plt.tight_layout()
{{< /runpython >}}

<br>

---

## Décrire un mouvement

### TP mouvement

Pour importer les tableaux `regressi` dans le programme ci-dessous, utiliser le bouton d'import sur la droite de la barre supérieure. 

{{< runpython lang="pyodide" height="auto"  upload="true" theme="dark" >}}
# #####
# IMPORTATION DES MODULES
# #####
from math import sqrt
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

# Import des tableaux x,y,t produits par Regressi
from pointage import x,y,t

# Initialisation des tableaux vx, vy, ax, ay
vx = []
vy = []
ax = []
ay = []
a = []

# nombres d'éléments pointés
n = len(x)

# #####
# Calcul des composantes x et y de la vitesse par la méthode centrée
# #####

for i in range(1,n-1):
    # pour chaque mesure i, on ajoute au tableau vx la coordonnée de v suivant x, puis de même pour vy
    vx.append((x[i+1]-x[i-1])/(t[i+1]-t[i-1]))
    vy.append((y[i+1]-y[i-1])/(t[i+1]-t[i-1]))

# #####
# On retire les premiers et derniers éléments aux listes x, y et t pour que les éléments de vx et vy leur correspondent
# #####

t = t[1:-1]
x = x[1:-1]
y = y[1:-1]

# on met à jour n par le nombre d'éléments calculés dans vx
n = len(vx)

# #####
# Calcul des composantes x et y de l'accélération par la méthode centrée
# #####

########################
# TRAVAIL À RÉALISER 1 #
########################






# #####
# Calcul de la norme de l'accélération en chaque position
# #####

########################
# TRAVAIL À RÉALISER 2 #
########################

# Pour calculer une racine carrée, vous pouvez utiliser la fonction sqrt().





# #####
# On retire à nouveau les extrémités où a n'est pas calculée
# #####

t = t[1:-1]
x = x[1:-1]
y = y[1:-1]
vx = vx[1:-1]
vy = vy[1:-1]

# dernière mise-à-jour du nombre d'éléments
n = len(ax)

echelle = 1/40 # permet d'ajuster la taille des vecteurs

# Positions des extrémités des vecteurs :
finAx = []
finAy = []
for i in range(n):
    finAx.append(x[i] + ax[i]*echelle)
    finAy.append(y[i] + ay[i]*echelle)

# Tracés :
plt.figure(figsize=(6, 6),dpi=150)
# Positions
plt.scatter(x, y, zorder=2)
# Vecteurs accélération
a = plt.quiver(x, y, ax, ay, units = "dots", color = "#1DB100", scale = 0.1)
plt.quiverkey(a, 0.9, 0.85, 10, label=r"$10\ \mathrm{m \cdot s^{-2}}$", coordinates = "axes")
plt.title('Représentation des positions de la balle et des vecteurs accélérations')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')
#plt.xlim(0,3)
plt.show()
{{< /runpython >}}

### Mouvement circulaire uniforme

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
from math import sqrt, cos, sin, pi
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

R = 5
n = 20
v = 10 # m/s

x = [R * cos(2*pi*i/n) for i in range(n)]
y = [R * sin(2*pi*i/n) for i in range(n)]

vx = [- v * sin(2*pi*i/n) for i in range(n)]
vy = [v * cos(2*pi*i/n) for i in range(n)]

ax = [-v**2 / R * cos(2*pi*i/n) for i in range(n)]
ay = [-v**2 / R * sin(2*pi*i/n) for i in range(n)]

plt.figure(figsize=(6, 6),dpi=200)
plt.scatter(x, y, zorder=2)
v = plt.quiver(x, y, vx, vy, units = "dots", color = "#FEAE00", scale = 0.05)
a = plt.quiver(x, y, ax, ay, units = "dots", color = "#1DB100", scale = 0.1)
plt.quiverkey(v, 0.9, 0.9, 5, label=r"$5\; \mathrm{m \cdot s^{-1}}$", coordinates = "axes")
plt.quiverkey(a, 0.9, 0.05, 10, label=r"$10\; \mathrm{m \cdot s^{-2}}$", coordinates = "axes")
plt.margins(0.2)
{{< /runpython >}}


{{< runpython lang="vpython" height="auto" theme="dark" >}}
Web VPython 3.2

scene.width, scene.height = 500,500
scene.background = vec(2,61,96)/255
v = 2
R = 10
a = v**2/R

M = sphere(pos=vec(R,0,0),vit=vec(0,v,0),color=vec(0,162,255)/255,radius=0.5,emissive=True)
O = sphere(pos=vec(0,0,0),radius=0.2)
c = curve(pos=[O.pos,M.pos],radius=0.02)
v_fleche = arrow(pos=M.pos, axis=hat(cross(vec(0,0,1),M.pos))*v, color=vec(254,174,0)/255, round=True)
a_fleche = arrow(pos=M.pos, axis=-M.pos*a, color=vec(29,177,0)/255, round=True, shaftwidth=0.2, emissive=True)

dt = 1e-4
t = 0

while(True):
    
    rate(10/dt)
    a_vec = -a*hat(M.pos)
    M.vit = M.vit + a_vec*dt
    M.pos = M.pos + M.vit*dt
    c.modify(1, pos=M.pos)
    v_fleche.pos = M.pos
    v_fleche.axis = hat(cross(vec(0,0,1),M.pos))*v
    a_fleche.pos = M.pos
    a_fleche.axis = -M.pos*a
    t += dt
{{< /runpython >}}

### Exercice «&nbsp;[clothoïde et échangeur routier](/act-tspemvt2.pdf)&nbsp;»

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
# début du programme
from math import *
# -----Coordonnées des positions du véhicule-----
t=[0.00, 1.50, 3.00, 4.50, 6.00, 7.50, 9.00, 10.5, 12.0, 13.5, 15.0]
x=[0.00, 0.0624, 0.4818, 1.625, 3.849, 7.500, 12.91, 20.37, 30.11, 42.25, 56.80]
y=[0.00, 20.00, 39.99, 59.96, 79.83, 99.49, 118.7, 137.3, 154.7, 170.6, 184.3]
vx = [ ]
vy = [ ]
dt = 1.50 # durée entre deux positions successives
for i in range(0, len(t)-1) :
    vx.append((x[i+1]-x[i])/dt)
    vy.append((y[i+1]-y[i])/dt)
t.pop(0) # supprime t[0] et décale liste t pour coïncider avec l'accélération
ax = [ ]
ay = [ ]
a = [ ]
for i in range(0, len(t)-1) :
    ax.append((vx[i+1]-vx[i])/dt)
    ay.append((vx[i+1]-vx[i])/dt)
    a.append(sqrt(ax[i]**2+ay[i]**2)) # norme du vecteur accélération
print(t)
print(a)
{{< /runpython >}}

<br>

---

## Champ uniforme

### Chute libre (vecteurs accélération)

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

g = 9.8
n = 15
v0 = 30 # m/s
alpha = 60 #°
h = 5
tf = v0*np.sin(alpha*np.pi/180)/g + np.sqrt((v0*np.sin(alpha*np.pi/180))**2 + 2*h*g)/g
t = np.linspace(0,tf,n)

x = v0*np.cos(alpha*np.pi/180)*t
y = -1/2*g*t**2 + v0*np.sin(alpha*np.pi/180)*t + h

vx = v0*np.cos(alpha*np.pi/180)
vy = -g*t + v0*np.sin(alpha*np.pi/180)

ax = [0]*n
ay = [-g]*n

plt.figure(figsize=(12, 7),dpi=150)
plt.scatter(x, y, zorder=2)
v = plt.quiver(x, y, vx, vy, units = "dots", color = "#FEAE00", scale = 0.1)
a = plt.quiver(x, y, ax, ay, units = "dots", color = "#1DB100", scale = 0.05)
plt.quiverkey(v, 0.9, 0.9, 20, label=r"$20\; \mathrm{m \cdot s^{-1}}$", coordinates = "axes")
plt.quiverkey(a, 0.9, 0.8, 10, label=r"$10\; \mathrm{m \cdot s^{-2}}$", coordinates = "axes")
#plt.ylim(-5,13)
#plt.xlim(-2,25)
plt.axis('equal')
plt.show()
{{< /runpython >}}

{{< runpython lang="vpython" height="auto" theme="dark" >}}
Web VPython 3.2

scene.width, scene.height = 800,600
scene.background = vec(2,61,96)/255

h = 0
M0 = vec(0,h,0)
v = 20
alpha = pi/3
g = vec(0,-9.81,0)
scene.center = vec(sin(2*alpha)*v**2/(2*mag(g)),v**2*sin(alpha)**2/(4*mag(g)),0)
scene.range = max(sin(2*alpha)*v**2/(mag(g))/2.5,v**2/(2*mag(g)))

v0 = vec(v*cos(alpha),v*sin(alpha),0)
M = sphere(pos=M0, vit=v0, color=vec(0,162,255)/255, radius=0.5, emissive=True, make_trail=False)

v_fleche = arrow(pos=M.pos, axis=v0/3, color=vec(254,174,0)/255, round=True, shaftwidth=0.2)
a_fleche = arrow(pos=M.pos, axis=g/2, color=vec(29,177,0)/255, round=True, shaftwidth=0.2)

dt = 1e-4
t = 0

while(M.pos.y >= 0):
    
    rate(1/dt)
    M.vit = M.vit + g*dt
    M.pos = M.pos + M.vit*dt
    v_fleche.pos = M.pos
    v_fleche.axis = M.vit/3
    a_fleche.pos = M.pos
    t += dt
{{< /runpython >}}

### Chute libre (énergie)

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

v0 = 5 # m/s
h = 2
alpha = 60 # °
C = 0.8 # Coefficient de restitution lors d'un rebond
m = 0.200 # kg
f = 0.02 # coefficient de frottement
z = h
g = 9.8

vx = v0 * np.cos(alpha/180*np.pi)
vz = v0 * np.sin(alpha/180*np.pi)
Vx = [vx]
Vz = [vz]

x = 0
z = h
X = [x]
Z = [z]

t = 0
dt = 1e-4
T = [0]

########################################################
### La boucle while qui suit est hors programme      ###
### Elle permet de garnir les listes Vx,Vz,X,Z et T  ###
### en tenant compte des frottements et d'un coef de ###
### restitution au rebond grâce à la méthode d'Euler ###
########################################################

while t < 5:
    vx += - dt * f * (vx**2 + vz**2) * vx / np.sqrt((vx**2 + vz**2))
    vz += dt * ( - f * (vx**2 + vz**2) * vz / np.sqrt(vx**2 + vz**2)  - g )
    Vx.append(vx)
    Vz.append(vz)
    x += dt * vx
    z += dt * vz
    if z < 0:
        z = 0
        vz = -vz * C**0.5
    X.append(x)
    Z.append(z)
    t += dt
    T.append(t)

plt.figure(figsize=(12, 7),dpi=150)

##################################################
### À PARTIR DE LÀ, IL FAUT COMPRENDRE LE CODE ###
##################################################

Ec = []
Ep = []
Em = []

for i in range(len(Vx)):
    Ec.append(1/2 * m * (Vx[i]**2 + Vz[i]**2))
    Ep.append(m * g * Z[i])
    Em.append(Ec[i] + Ep[i])

plt.plot(T,Ec,label=r"$E_c$")
plt.plot(T,Ep,label=r"$E_p$")
plt.plot(T,Em,label=r"$E_m$")
plt.xlabel("temps (s)")
plt.ylabel("énergie (J)")
plt.legend()
plt.show()
{{< /runpython >}}

### Activité «&nbsp;[LINAC](/linac.pdf)&nbsp;»

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
from math import sqrt

e = 1.60E-19
m = 1.67E-27
d = 0.100
U = 2.00E6
T = 1/25.0E6
E = 0

def calcul_vs(v_e):
    return sqrt( 2 * e * U / m + v_e**2)

def calcul_taille_tube(v_e,v_s):
    t_cavité = d / (v_e + (v_s - v_e) / 2) # tire partie de l'augmentation linéaire de la vitesse
    return (T/2 - t_cavité) * v_s # le temps passé dans le tube est T/2- t_cavité

L = 0
v0 = 0
for i in range(24): # le 25e tube peut être aussi court que l'on veut
    E = E + U
    print(f"Énergie atteinte après la cavité {i+1} : {E:.2E} eV")
    v1 = calcul_vs(v0)
    l = calcul_taille_tube(v0,v1)
    print(f"Longueur du tube {i+1} : {l:.2E} m\n")
    L = L + d + l # Longueur totale
    ### À COMPLÉTER

L = L + d # On ajoute la dernière cavité
print(f"Énergie atteinte après la dernière cavité : {E+U:.2E} eV\n")
print(f"Longueur totale parcourue : L = {L:.2E} m")
{{< /runpython >}}

<br>

---

## Kepler

### Test de la deuxième loi

On va tester la deuxième loi de Kepler en suivant sur plusieurs jours la position de Mercure, planète à l'orbite la plus elliptique du système solaire.

{{%notice type="tip" round="true" title="Protocole"%}}
Pour récupérer un tableau de données des positions de Mercure dans le référentiel héliocentrique pour 17 positions séparées de 5 jours&nbsp;:
<ul style="margin-top:-0.5em; margin-bottom:1em;">
<li>se rendre sur le <a href="https://ssp.imcce.fr/forms/ephemeris" target="_blank">site d'éphémérides de l'Observatoire de Paris</a>&nbsp;;</li>
<li>dans "corps du système solaire", choisir Mercure&nbsp;;</li>
<li>dans "époque", choisir la date d'aujourd'hui, nombres de dates : 17, pas de calcul : 5 jours&nbsp;;</li>
<li>dans "système de coordonnées", pour le centre du repère : héliocentre, et pour coordonnées (dernier truc), choisir cartésiennes (ne pas modifier le reste)&nbsp;;</li>
<li>cliquer sur "calculer"&nbsp;;</li>
<li>enfin, en haut à droite du tableau créé, exporter en "comma-separated values (csv)".</li>
</ul>
{{%/notice%}}

Il faut alors enregistrer le fichier de données sous le nom "`ephemerides.csv`".

Vous pouvez télécharger le programme `mercure.py` en cliquant [ici](https://coursphychi.github.io/mercure.py) (ou sur l'icône ordi de la page du cours). Il faudra ensuite que vous placiez le fichier `ephemeride.csv` dans le même dossier que le programme `mercure.py`.

En exécutant le programme `mercure.py`, on peut alors constater que la deuxième loi de Kepler est plutôt très bien vérifiée pour l'orbite de Mercure.

{{< runpython lang="pyodide" height="auto" upload="true" theme="dark" >}}
# =============================================
# TEST DE LA DEUXIÈME LOI DE KEPLER SUR MERCURE
# =============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Charger les données -------------------------------------------------
FILENAME = "ephemerides.csv"           # le fichier doit être dans le même dossier
df = pd.read_csv(FILENAME, sep=';')    # données exportées avec des « ; »

# On récupère la date et la position x, y (en unités astronomiques = UA)
dates_iso = df['Date (undefined)']
x = df['px (au)'].values
y = df['py (au)'].values

# Pour un affichage plus compact des dates : 1/3/25
def format_date(iso):
    ymd = iso.split('T')[0]              # "2025-03-01"
    y, m, d = map(int, ymd.split('-'))
    return f"{d}/{m}/{str(y)[-2:]}"      # "1/3/25"
dates = [format_date(s) for s in dates_iso]

# 2) Calcul des aires en UA² --------------------------------------------
areas = []
for i in range(len(x)-1):
    # Formule de l’aire d’un triangle (produit vectoriel 2D)
    area = 0.5 * abs(x[i]*y[i+1] - y[i]*x[i+1])
    areas.append(area)

# 3) Tracé ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 7),dpi=250)
ax.set_aspect('equal')
ax.axis('off')

couleurs = ['#0076BA', '#FF42A1']     # bleu puis rose
alpha  = 0.4                          # transparence

# Secteurs colorés
for i in range(len(x)-1):
    ax.fill((0,x[i],x[i+1]),(0,y[i],y[i+1]), color=couleurs[i % 2], alpha=alpha, edgecolor='none')
    # Rayon pointillé vers la position i
    ax.plot([0, x[i]], [0, y[i]], ls='--', lw=0.7, c='grey')

# Dernier rayon
ax.plot([0, x[-1]], [0, y[-1]], ls='--', lw=0.7, c='grey', alpha=0.7)

# Positions et dates (décalage léger pour ne pas coller le point)
ax.scatter(x, y, s=45, c='#00A2FF', zorder=3)
for xi, yi, t in zip(x, y, dates):
    r = np.hypot(xi, yi)
    ax.text(xi*1.05, yi*1.05, t, fontsize=6, ha='center', va='center')

# Soleil
ax.scatter(0, 0, s=120, c='#FFD932', zorder=4)

plt.show()

# 4) Affichage des aires --------------------------------------------------
print("Aires balayées entre positions successives (UA²) :")
for d1, d2, a in zip(dates[:-1], dates[1:], areas):
    print(f"{d1} → {d2} : {a:.4e}")
print(f"\nMoyenne des aires = {np.mean(areas):.4e} UA²")
print(f"incertitude-type = {np.std(areas,ddof=1)/np.sqrt(len(areas)):.1e}  UA²")
{{< /runpython >}}

### Test de la troisième loi

Le code se trouve dans l'activité «&nbsp;[découverte des lois de Kepler](/act-kepler.pdf)&nbsp;»

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
### ENTRER LES VALEURS OBTENUS DANS LES LISTES SUIVANTES
Hauteurs = [hauteur en km, hauteur en km, hauteur en km, ...]
Périodes = [(heures,minutes),(heures,minutes),(heures,minutes),...]

### CONVERSION DES HAUTEURS EN RAYON DE L'ORBITE (EN m)
RT = 6.378E6 # rayon de la terre en m
R = [] # Liste vide qui devra contenir les rayons des orbites en m
for h in Hauteurs:
    R.append(.......)

### CONVERSION DES PÉRIODES EN s
T = []
for (heures,minutes) in Périodes:
    T.append(...)

### POUR CHAQUE COUPLE (R,T), ON SOUHAITE CALCULER ET AFFICHER LE QUOTIENT T²/R³
for i in range(len(R)):
    quotient = ........
    print(quotient)
{{< /runpython >}}

<br>

---

## Diffraction et interférences

### Somme de deux signaux sinusoïdaux déphasés

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import matplotlib.pyplot as plt

f = 200 # Hz
T = 1/f

# Valeurs de t
t = np.linspace(0, 5*T, 1000) # 1000 points entre 0 et 5T

# Signal 1 échantillonné sur les valeurs de t
s1 = np.sin(2*np.pi * f * t)

Δφ = 3*np.pi/4 # déphasage

# Signal 2 échantillonné sur les valeurs de t
s2 = np.sin(2*np.pi * f * t + Δφ)

# Tracés
plt.figure(figsize=(12, 6), dpi=150)
plt.plot(t,s1,ls="-.",label=r"signal $s_1(t)$")
plt.plot(t,s2,ls="--",label=r"signal $s_2(t)$")
plt.plot(t,s1+s2,lw=2,label=r"signal $s_1(t)+s_2(t)$")

plt.xlabel("t (s)")
plt.ylabel("Amplitude")
plt.title(f"Somme de deux signaux sinusoïdaux déphasés")
plt.grid("True")
plt.legend()
plt.show()
{{< /runpython >}}

Appliquons cela à l'activité sur la [réduction active de bruit des écouteurs](/act-rab.pdf).

Le circuit de l'écouteur émet un anti-bruit en opposition de phase avec le bruit. Mais l'électronique met une durée $\tau$ à traiter le signal : l'anti-bruit part en retard.

Un retard $\tau$ sur un signal de période $T$ ajoute un déphasage $2 \pi \times \tau/T$.<br>
La phase à l'origine de l'anti-bruit vaut donc&nbsp;:

$$\phi = -\left(\pi + 2 \pi \frac{\tau}{T}\right)$$

<ul style="margin-top:-0.5em; margin-bottom:1em;">
<li>$\pi$ : l'opposition de phase voulue</li>
<li>$2 \pi \tau/T$ : le défaut dû au retard de l'électronique</li>
<li>signe moins : un retard se traduit par un déphasage en arrière</li>
</ul>

Autrement dit, l'anti-bruit est exactement le bruit inversé et retardé de tau.

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Paramètre à modifier
# ------------------------------------------------------------------
f = 600            # fréquence du bruit (Hz)

# ------------------------------------------------------------------
# Donnée de l'activité
# ------------------------------------------------------------------
tau = 45e-6        # retard de l'électronique (s) : hypothèse du document 3

# ------------------------------------------------------------------
# Calculs
# ------------------------------------------------------------------
T = 1 / f                                   # période (s)
phi = -(np.pi + 2 * np.pi * tau / T)        # phase à l'origine de l'anti-bruit (rad)

t = np.linspace(0, 3 * T, 1000)             # instants sur trois périodes (s)

bruit = np.cos(2 * np.pi * f * t)           # amplitude choisie égale à 1
anti_bruit = np.cos(2 * np.pi * f * t + phi)
somme = bruit + anti_bruit                  # ce que reçoit le tympan

# amplitude de la somme, lue directement sur la courbe
amplitude_somme = np.max(np.abs(somme))

# atténuation : l'amplitude du bruit seul vaut 1
A = -20 * np.log10(amplitude_somme)

# ------------------------------------------------------------------
# Affichage des résultats
# ------------------------------------------------------------------
print("f =", f, "Hz")
print("T =", round(T * 1000, 3), "ms")
print("tau / T =", round(tau / T, 4))
print("écart à l'opposition de phase :",
      round(np.degrees(2 * np.pi * tau / T), 1), "degrés")
print("amplitude de la somme :", round(amplitude_somme, 3))
print("atténuation A =", round(A, 1), "dB")

# ------------------------------------------------------------------
# Tracé
# ------------------------------------------------------------------
plt.figure(figsize=(9, 4.5))

plt.plot(t * 1000, bruit, color="tab:blue", label="bruit")
plt.plot(t * 1000, anti_bruit, color="tab:orange", linestyle="--",
         label="anti-bruit")
plt.plot(t * 1000, somme, color="black", linewidth=2.5,
         label="somme reçue par le tympan")

plt.axhline(0, color="grey", linewidth=0.8)

# échelle verticale FIXE : on peut comparer les courbes d'une fréquence à l'autre
plt.ylim(-2.2, 2.2)

plt.xlabel("t (ms)")
plt.ylabel("pression (unité arbitraire)")
plt.title("f = " + str(f) + " Hz      τ = " + str(round(tau * 1e6)) + " µs"
          + "      τ/T = " + str(round(tau / T, 3))
          + "      A = " + str(round(A, 1)) + " dB")
plt.legend(loc="upper right")
plt.grid(alpha=0.3)
plt.show()
{{< /runpython >}}

### Exercice «&nbsp;[trombone de Koenig](/act-konig.pdf)&nbsp;»

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
from statistics import mean

D = [4.35e-2, 8.7e-2, 13.1e-2, 17.4e-2, 21.6e-2]   # décalage en mètre de la partie mobile du trombone
k = [1, 2, 3, 4, 5]                                # nombre de décalage permettant l’obtention d’interférences constructives
f = 4032
v = []

for i in range(len(k)):                            # i prend les valeurs successives 0,1,2,3,4
    vi = 2 * f * D[i] / k[i]
    v.append(vi)

vson = round(mean(v))                              # permet de calculer la moyenne vson des grandeurs contenues dans la liste v

print("La vitesse moyenne du son dans le trombone est", vson, "m/s")

Lambda = ...
print("La longueur d'onde de l’onde acoustique dans le trombone est", Lambda, "m")
{{< /runpython >}}

### Scarabé

{{< runpython lang="pyodide" height="auto" theme="dark" >}}
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

# Simulation de 5000 longueurs choisies aléatoirement dans les intervalles de mesure
Nsim = 5000
echelle = rd.uniform(2.6, 2.7, Nsim)   # intervalle de mesure de la barre de l'échelle en cm
d_mes = rd.uniform(1.7, 1.9, Nsim)     # intervalle de mesure de la distance d en cm

# Calcul de l'épaisseur e en nm
e = d_mes*1000/(9*echelle)

# Calcul de la moyenne (en nm) et de l'incertitude-type (en nm) sur l'épaisseur e
e_moy = np.average(e)
u_e = np.std(e, ddof=1)

# Tracé graphique de l'histogramme et affichage des résultats
plt.hist(e, bins="rice", color="grey")
print("INCERTITUDE-TYPE : u(e) =", u_e, " en nm")
print("VALEUR MOYENNE : e_moyen =", e_moy, " en nm")
{{< /runpython >}}
