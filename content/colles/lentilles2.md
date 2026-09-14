---
title: "Lentilles"
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





# Lentilles minces : modéliser le flou


L'objectif de cet exercice est de reproduire par traitement d'image, à l'aide d'un programme Python, ce qu'on verrait sur un écran situé derrière une lentille convergente pour différentes positions de l'écran&nbsp;; on fournit au programme un fichier image et des paramètres (le diamètre de la lentille $D$, sa distance focale $f'$, la distance lentille-objet $\overline{OA}$, la distance lentille-écran $\overline{OE}$, la taille de l'objet $\overline{AB}$), et il produit une image correspondant à ce qu'on verrait sur l'écran. 

1. Pourquoi la figure sur l'écran est-elle floue lorsque la distance entre la lentille et l'écran est différente de $\overline{OA'}$&nbsp;? Faire un schéma pour illustrer.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
<img src="/schemlentflou.png">
À un point objet ne correspond plus sur l'écran un point image mais une tâche de diamètre $d$.
</blockquote>
</details>

2. Déterminer $\overline{OA'}$ et $\overline{A\'B'}$ en fonction de $\overline{OA}$, $f'$ et $\overline{AB}$.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
$\displaystyle \overline{OA'} = \frac{\overline{OA}\cdot f'}{\overline{OA}+f'}$<br>
$\displaystyle \overline{A'B'} = \overline{AB}\times\frac{\overline{OA'}}{\overline{OA}}$
</blockquote>
</details>

3. Déterminer la hauteur $H$ de la figure sur l'écran ainsi que le diamètre d'une tâche $d$ en fonction de $D$, $f'$, $\overline{OA'}$, $\overline{OE}$ et $\overline{A'B'}$.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">

<ul>
<li>$\displaystyle d = D\times\frac{|\overline{OE}-\overline{OA'}|}{\overline{OA'}}$</li>
<li>Le schéma nous montre que $H-A'B'$ est proportionnel à $|\overline{OE}-\overline{OA'}|$ $\Rightarrow$ $\displaystyle \frac{H-A'B'}{|\overline{OE}-\overline{OA'}|} = cste$.<br>
Et comme lorsque $\overline{OE}=0$, $H=D$, on a :<br>
$\displaystyle \frac{H-A'B'}{|\overline{OE}-\overline{OA'}|} = \frac{D-A'B'}{|0-\overline{OA'}|}$<br>
On en déduit que $\displaystyle H = A'B'+\frac{D-A'B'}{\overline{OA'}}\times |\overline{OE}-\overline{OA'}|$
</li>
</ul>

</blockquote>
</details>


Le programme Python est déjà écrit à l'exception de la fonction centrale qui contient la physique du problème&nbsp;:

```python
def calcule_taille(D:float, fprime:float, OA:float, OE:float, AB:float) -> tuple:
    """
    Entrées:
        D: diamètre de la lentille (en m)
        fprime: 0 distance focale de la lentille (en m)
        OA: distance lentille-objet (en m)
        OE: distance lentille-écran (en m)
        AB: taille objet (en m)
    Sorties:
        tuple (H,d) avec:
        H: hauteur de la figure sur l'écran (en m)
        d: diamètre des tâches sur l'écran (en m)
    """
    # CODE À COMPLÉTER
```

3. Se rendre sur [ce notebook Colab](https://colab.research.google.com/drive/1mf8qHa3ZdkZ43RzJWAAmXbzfzaQTYaPO?usp=sharing) et compléter la fonction.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
Exemple de solution :

```python
def calcule_taille(D, fprime, OA, OE, AB):
    OAprime = fprime * OA / (fprime + OA)
    d = (abs(OE - OAprime) / OAprime * D)
    AprimeBprime = AB * OAprime / OA
    H = abs(AprimeBprime) + (D - abs(AprimeBprime)) / OAprime * (abs(OE - OAprime))
    return H, d
```
                    
</blockquote>
</details>






