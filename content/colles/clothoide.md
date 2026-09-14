---
title: "Clothoïde"
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





# Clothoïde

Pour opérer un virage, on choisit d'abord de connecter deux sections de rails rectilignes (en orange) de directions différentes par un arc de cercle (bleu).

<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/viragetrain.png" style="box-shadow:none;background:none;">
</div>

1. Tracer l'évolution de l'accélération d'un point $\mathrm{M}$ suivant les rails à vitesse constante sur le trajet entre $\mathrm{I}$ et $\mathrm{F}$.

2. Ce raccordement est-il une bonne idée ?

Plutôt qu'un arc de cercle, on va relier les deux portions rectilignes par des morceaux de clothoïdes[^1]. Cette courbe a pour particularité que son rayon de courbure croit linéairement avec l'abscisse curviligne sur la courbe.<br>
Supposons qu'un point $\mathrm{M}$ suive une clothoïde à vitesse constante $v=\pu{1,0 m*s-1}$. On peut alors paramétrer la courbe avec le temps $t$. Plaçons l'origine en $\mathrm{M}(t=0)$. Le rayon de courbure $R(t)$ en $\mathrm{M}(t)$ vaut alors $\frac{1}{R(t)}=kt$ où $k$ est une constante positive. 

3. Esquisser l'allure d'une clothoïde.

4. Dans un repère de Frenet, écrire l'accélération tangentielle et normale du point M.

5. Reprendre les questions 1 et 2 avec un tronçon de raccordement fait à partir de deux tronçons de clothoïdes symétriques par rapport à l'axe ($\Delta$). L'origine de la première clothoïde est en O et celle de la deuxième en B. 

<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/clothoapex.png" style="box-shadow:none;background:none;">
</div>

On veut maintenant tracer un tronçon de clothoïde et pour cela, il faut trouver son équation.

6. En appelant $\theta$ l'angle que fait le vecteur tangent $\vec{u}_T(t)$ au point $\mathrm{M}(t)$ de la courbe avec l'axe $\mathrm{O}x$, montrer que :
$$\theta(t)=\frac 12 k v t^2$$

7. En déduire que l'équation de la clothoïde est donnée par :
$$
\begin{cases}
v\int_0^t \cos\left(\frac 12 kv u^2\right)\mathrm{d}u\\\\
v\int_0^t \sin\left(\frac 12 kv u^2\right)\mathrm{d}u
\end{cases}
$$

8. En utilisant la méthode des rectangles, représenter graphiquement un tronçon de clothoïde pout $t$ allant de 0 à 5&nbsp;s sur Python en complétant le code suivant.

```python
import numpy as np
import matplotlib.pyplot as plt

def integrale(f,a,b):
    #################
    ## À COMPLÉTER ##
    #################

v = 1
k = 2
t = np.linspace(0,5,500)

def c(x):
    return v * np.cos(1/2 * k * v * x**2)

def s(x):
    return v * np.sin(1/2 * k * v * x**2)

def C(x):
    return integrale(c,0,x)

def S(x):
    return integrale(s,0,x)

plt.figure(figsize=(6, 6),dpi=150)
plt.plot(C(t),S(t))
plt.show()
```

[Correction pour le code](https://colab.research.google.com/drive/1YviDpj3-evww1ciq8ikosMoHxv8UAMOu?usp=sharing)

[^1]: Clotho est la benjamine des trois Moires, celle qui tisse le fil de la vie (ça a donné l'anglais clothe)&nbsp;; les deux autres tirent (Lachésis) et découpent (Atropos) dans la mythologie grecque antique.
On appelle aussi la clothoïde spirale de Cornu ou d'Euler ou de Fresnel...