---
title: "Respiration"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
hidden: true
---


<style>
 	#correc
  {
    color: #006C65;
    border-left: solid 10px #C7DDDC;
  }
 	#comm
  {
    color: #004D80;
    border-left: solid 10px #B3CAD9;
  }
 	#commsum
  {
    color: #004D80;
  }
 	#correcsum
  {
    color: #006C65;
  }

details > summary:first-of-type {
  display: list-item;    
  cursor: pointer;       
}

details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
</style>



# La respiration

La respiration permet d'illustrer le premier principe de la thermodynamique sur un exemple qui nous est tous assez familier (j'espère).

<div style="position:relative;margin-left:auto;margin-right:auto;width:350px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/poumon.jpg" style="box-shadow:none;background:none;">
</div>


On va supposer l'air comme étant un gaz parfait diatomique. Dans ces conditions, l'énergie interne de $n$ moles d'air vaut $U=\frac{5}{2}nRT$.

On ne considère dans la suite que les variations relatives du volume des poumons $\Rightarrow$ le volume $V$ avant inspiration (= après expiration) est pris comme égal à zéro. <br>De même, seules les pressions relatives nous intéressent $\Rightarrow$ la pression $P$  avant inspiration (= après expiration) est prise comme égale à zéro.

Une modélisation de $V(P)$ à partir de mesures expérimentales (réalisées grâce à un cathéter œsophagien  pour $P$ et un pléthysmographe pour $V$) donne :
- pour l'inspiration : $V=A_I\left(1-e^{-k_IP}\right)$
- pour l'expiration : $V=A_E\left(1-e^{-k_EP}\right)$

Avec $A_I=3,57\text{ L}$, $k_I=0,964.10^{-3}\text{ Pa}^{-1}$, $A_E=3,35\text{ L}$, $k_E=1,644.10^{-3}\text{ Pa}^{-1}$.

$A$ est la capacité pulmonaire maximale et $k$ est un coefficient de compressibilité.<br>
$A_E<A_I$ car en fin d'expiration, des alvéoles se referment, s'affaissent, leurs parois se collant sous l'action de la tension superficielle (et ce malgré la production de surfactants par les poumons équivalents à ceux qu'on trouve dans le savon pour abaisser cette énergie de surface... Sans eux, c'est tout le poumon qui s'affaisserait). Et c'est aussi pourquoi $k_I>k_E$ ; à l'inspiration, il faut vaincre la tension de surface pour recruter à nouveau les alvéoles refermées.  

<img src="/courberespi1.png" width="800">

1. Déterminer la fonctions $P_I(V)$ à l'inspiration et la fonction $P_E(V)$ à l'expiration. 

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$P_I(V)= \frac{1}{k_I}\ln\left(\frac{A_I}{A_I-V}\right)$<br>
$P_F(V)= \frac{1}{k_E}\ln\left(\frac{A_E}{A_E-V}\right)$
</details>

2. En utilisant la librairie `matplotlib`, tracer l'évolution de $P_I(V)$ et $P_E(V)$ pour $V$ allant de $3.3$ à $V_{max}$ (que vaut $V_{max}$ ?).<br>
Il faudra compléter le code sur [ce notebook](https://colab.research.google.com/drive/1qfLD3k038dye43zN2wihIWzB-JHyRsXK?usp=sharing) (une connexion à un compte google est nécessaire).

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">import matplotlib.pyplot as plt
<br>
A_I, A_E = 3.57, 3.35
k_I, k_E = 0.964, 1.644
<br>
def P_I(V): return 1/k_I*(np.log(A_I/(A_I-V)))
def P_E(V): return 1/k_E*(np.log(A_E/(A_E-V)))
<br>
Vmax = min(A_I,A_E)
V = np.linspace(3.3,Vmax-1E-5,100)
<br>
plt.figure(figsize=(10,8),dpi=150)
plt.plot(V,P_I(V),c = "red", label="inspiration")
plt.plot(V,P_E(V),c = "blue",label="expiration")
plt.xlabel("Volume V (L)")
plt.ylabel("Pression P (kPa)")
plt.legend()
plt.show()
</code>
</pre>
<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/respicorrec.png" style="box-shadow:none;background:none;">
</div>
</blockquote>
</details>

3. Déterminer numériquement les valeurs finales de volume $V_f$ et de pression $P_f$ en fin d'inspiration / début d'expiration en utilisant la fonction `brentq` de la librairie `scipy.optimize` dont la signature est donnée ci-dessous.<br>
S'inspirer du tracé obtenu à la question 2. pour déterminer des valeurs de `a` et `b` adéquates.

```python
def brentq(func, a, b):
    """
    brentq(func, a, b) -> float
    ---------------------------
    Trouve une racine de l’équation func(x) = 0 dans l’intervalle fermé
    [a, b] grâce à l’algorithme de Brent (combinaison bisection, sécante et
    interpolation quadratique).

    Conditions préalables
    ---------------------
    - func(a) et func(b) doivent avoir des signes opposés strictement :
      func(a) * func(b) < 0.  
    - L’intervalle est supposé borné et fini.

    Paramètres
    ----------
    func : callable
        Fonction continue sur [a, b] à annuler.
        Signature attendue : y = func(x) (scalaire en entrée et en sortie).
    a, b : float
        Bornes gauche (`a`) et droite (`b`) de l’intervalle de recherche
        contenant exactement une racine (changement de signe garanti).

    Retour
    ------
    xr : float
        Approximation de la racine telle que  
        abs(func(xr)) < 2 × 10⁻¹² (tolérance par défaut interne).
```



<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">from scipy.optimize import brentq
<br>
def diff(V): return P_I(V)-P_E(V)
<br>
V_f = brentq(diff,3.30,3.33)
P_f = P_I(V_f)
print(f"V_f = {V_f:.2f} L")
print(f"P_f = {P_f:.2f} kPa")
</code>
</pre>
<code>V_f = 3.31 L</code><br>
<code>P_f = 2.73 kPa</code>
</blockquote>
</details>



4. Lorsque la respiration n'est pas forcée, les muscles respiratoires ne travaillent que pendant l'inspiration (l'élasticité des poumons suffit pour l'expiration). Calculer ce travail numériquement grâce à la fonction d'intégration `quad ` de la librairie `scipy.integrate` dont la signature est donnée ci-dessous.

```python
def quad(func, a, b):
    """
    quad(func, a, b) -> (float, float)
    ----------------------------------
    Calcule l’intégrale définie de func(x) sur l’intervalle [a, b] au moyen
    de la méthode adaptative de quadrature de Gauss–Kronrod (algorithme
    QAG de QUADPACK).

    Usage minimal (sans options) :
        >>> I, err = quad(f, 0, 1)

    Paramètres
    ----------
    func : callable
        Fonction réelle de variable réelle.  
        Signature attendue : y = func(x), où x est un flottant et y également.
    a, b : float
        Bornes d’intégration avec a < b.

    Retour
    ------
    I : float
        Approximation de l’intégrale ∫ₐᵇ func(x) dx.
    err : float
        Estimation absolue de l’erreur sur `I`
        (≈ précision effective de la valeur retournée).
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">from scipy.integrate import quad
W = quad(P_I, 0, V_f)[0]
print(f"W = {W:.2f} J")</code>
</pre>
<code>W = 2.73 J</code>
</blockquote>
</details>

5. Montrer qu'on a $W= -A_IP_f+P_fV_f+\frac{1}{k_I}V_f$<br>
*aide : on pourra utiliser $dV=A_Ik_Ie^{-k_IP}dP$ puis intégrer par partie.*<br>
Calculer le résultat à l'aide de Python.<br>Quelle proportion du métabolisme d'un humain moyen (≈ 10 MJ par jour) la respiration représente-t-elle ?


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">

<div style="overflow-x:auto;">
$$
\begin{aligned} W&=-W_I &\text{le travail musculaire s'oppose au travail des forces de pression} \\
&=-\int_0^{V_f}-PdV \\ 
& =\int_0^{P_f}PA_I k_I e^{-k_I P}dP &\text{en utilisant }dV=A_Ik_Ie^{-k_IP}dP \\
& =A_Ik_I\left[\frac{-P}{k_I}e^{-k_I P}\right]_0^{P_f}-A_Ik_I\int_0^{P_f}\frac{-1}{k_I} e^{-k_I P}dP &\text{intégration par partie}  \\
& =A_Ik_I\left[\frac{-P}{k_I}e^{-k_I P}\right]_0^{P_f}-A_Ik_I\left[\frac{1}{k_I^2}e^{-k_I P}\right]_0^{P_f} & \\ 
& =-A_I P_f e^{-k_I P_f}-\frac{A_I}{k_I}e^{-k_I P_f}+\frac{A_I}{k_I} \\
& =-A_IP_f+P_fV_f+\frac{V_f}{k_I}&\text{car }A_Ie^{-k_IP_f}=A_I-V_f \end{aligned}
$$
</div>
<pre><code class="language-python">W = -A_I*P_f + P_f*V_f + V_f/k_I
print(f"W = {W:.2f} J")
prop = 15*24*60*W/10e6*100 # pour 15 inspirations par minute
print(f"proportion du métabolisme : {prop:.2f} %")
</code>
</pre>
<code>W = 2.73 J</code><br>
<code>proportion du métabolisme : 0.59 %</code>
</blockquote>
</details>

6. Montrer que le transfert thermique $Q_I$ fourni à l'air lors d'une inspiration peut s'écrire $Q_I=\frac{7}{2}P_fV_f-A_I P_f +\frac{1}{k_I}V_f$.<br>Donner sa valeur.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$\Delta U_I = W_I + Q_I \Rightarrow Q_I = \Delta U_I - W_I$
<br>
$\begin{aligned}
Q_I &= \frac{5}{2}(P_fV_f - 0)-\int_0^{V_f} -P dV\\
&= \frac{5}{2}(P_fV_f - 0)-A_IP_f+P_fV_f+\frac{V_f}{k_I}\\
&=\frac{7}{2}P_fV_f-A_I P_f +\frac{V_f}{k_I}
\end{aligned}$
<br>
<pre><code class="language-python">Q_I = 7/2*P_f*V_f - A_I*P_f+V_f/k_I # calcul explicite
print(f"Q_I = {Q_I:.1f} J") 
Q_I = 5/2*P_f*V_f + W # calcul implicite
print(f"Q_I = {Q_I:.1f} J") 
</code>
</pre>

<code>Q_I = 25.3 J</code><br>
<code>Q_I = 25.3 J</code>
</blockquote>
</details>

7. Calculer numériquement le transfert thermique $Q$ lors d'un cycle respiratoire complet puis la puissance thermique libérée. Commenter son signe. Comparer à la puissance thermique perdue par un corps humain dans les conditions de vie courante, au repos, de l'ordre de 100 W.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">V = np.linspace(0,Vf,100)
plt.figure(figsize=(9,6),dpi=150)
plt.plot(V,P_I(V),c = "red", label="inspiration")
plt.plot(V,P_E(V),c = "blue",label="expiration")
plt.xlabel("Volume V (L)")
plt.ylabel("Pression P (kPa)")
plt.legend()
plt.fill_between(V, P_I(V), P_E(V), color = "yellow", alpha = 0.2)
plt.show()
</code>
</pre>
<div style="position:relative;margin-left:auto;margin-right:auto;width:700px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/courberespi2.png" style="box-shadow:none;background:none;">
</div>
<pre><code class="language-python">Q = quad(diff, 0, V_f)[0]
print(f"Q = {Q:.3f} J")
Plib = Q/4 # en prenant 4 s pour un cycle respiratoire (15 respirations par minute)
print(f"Plib = {Plib:.3f} W")
</code>
</pre>
<code>Q = 0.821 J</code><br>
<code>Plib = 0.205 W</code>

Sur le cycle, on a $W<0$ et $Q>0$, l'air reçoit de la chaleur.<br>
Seule une toute petite partie des 100 W perdue par le corps humain sert à chauffer l'air.


</blockquote>
</details>