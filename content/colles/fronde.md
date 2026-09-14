---
title: "Fronde"
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



# Fronde

--- 

## Dynamique

Une fronde est constituée par une pierre de masse $m$ reliée à un point fixe O par l'intermédiaire d'un fil de longueurs $\ell$ et de masse négligeable. 

Depuis sa position d’équilibre, on donne à la masse une vitesse initiale $\overrightarrow{v_0}$ horizontale.


1. Écrire le PFD dans un repère polaire pour une position de la masse repérée par l’angle définie depuis la direction initiale du fil.

2. Intégrer la projection du PFD suivant  en multipliant chaque membre par $\dot{\theta}$. En déduire une expression pour $\dot{\theta}^2$.

3. Injecter cette expression dans la composante radiale du PFD afin d’obtenir une expression pour la tension $T$  en fonction de $\theta$.

4. En déduire la vitesse minimale $v_0$ pour que la pierre parcours un cercle.

5. La vitesse initiale $v_0$ étant inférieure à la valeur limite trouvée ci-dessus, calculer l'angle que fait le fil avec la verticale lorsqu’il cesse d’être tendu ? Quel est le mouvement ultérieur de la masse m ?


<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
<div style="position:relative;margin-left:auto;margin-right:auto;width:700px;max-width:100%;margin-bottom:-40px;margin-top:-40px;">
<a href="/correcfronde.pdf"><img src="/correcfronde.png" style="box-shadow:none;background:none;"></a>
</div>
</blockquote>
</details>

---

## Énergétique


On remplace la question 2 par :

2. Utiliser le théorème de l’énergie cinétique pour exprimer $\dot{\theta}^2$ en fonction de $\theta$.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
Le TEC s'écrit :
<div id="grosseformule">
$$
\displaystyle
\begin{array}{rcll}
E_{cB}-E_{cA}&=&\sum W_{AB}(\overrightarrow{F})&\text{en appelant A le point de départ et B le point repéré par }\theta\\\\
\frac{1}{2}m(\ell\dot{\theta})^2-\frac{1}{2}m\ell v_0^2 &=& W_{AB}(\overrightarrow{P}) &\text{car la tension de la corde ne travaille pas}\\\\
\frac{1}{2}m(\ell\dot{\theta})^2-\frac{1}{2}m v_0^2 &=& \int_A^B \overrightarrow{P}\cdot \overrightarrow{dOM} &\\\\
\frac{1}{2}m(\ell\dot{\theta})^2-\frac{1}{2}m v_0^2 &=& -\int_{z_A}^{z_B} mgdz &\text{avec un axe z vertical dirigé vers le haut}\\\\
\frac{1}{2}m(\ell\dot{\theta})^2-\frac{1}{2}m v_0^2 &=& -mg\ell(1-\cos (\theta)) &\\\\
\end{array}
$$
</div>
<div id="grosseformule">
$$
\Rightarrow \dot{\theta}^2= \frac{v_0^2}{\ell^2}-\frac{2g}{\ell}\left(1-\cos(\theta)\right)
$$
</div>
</blockquote>
</details>

---

6. Vérifier sur la simulation ci-dessous qu'on obtient bien les comportements attendus en modifiant la valeur à la ligne 22.

{{< runpython lang="vpython" mode="toggle" default="code" width="800" file="fronde.py" >}}
{{< /runpython >}}


