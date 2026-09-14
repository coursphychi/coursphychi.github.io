---
title: "Réfraction"
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





# Réfraction



<video width="700" poster="/carreaux.poster.webp" controls style="display:block; max-width: 100%; position:relative;margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
  <source src="https://presentationssite.github.io/carreaux.mp4" type="video/mp4">
</video>

>Le champ de l'image fait 7 carreaux de largeur en dehors de l'eau mais seulement 5 sous l'eau. L'exercice vise dans un premier temps à expliquer cette observation puis à déterminer la distance entre le mur et la caméra.

1. Observerait-on la même chose en immergeant sa tête sous l'eau, les yeux ouverts ? Et avec un masque ?

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
Les carreaux ne nous apparaitraient pas plus grands si on ouvrait les yeux sous l'eau. Par contre, ils nous apparaîtraient flous car les rayons de lumière sont moins réfractés lors de leur passage de l'eau au corps vitré (le milieu contenu dans l'œil d'indice optique 1,336). C'est comme si on était devenu très hypermétrope.
    <img src="/aireauoeil.png">
Avec un masque ou des lunettes, on observerait la même chose que la caméra de la vidéo car c'est bien la couche d'air supplémentaire qui crée la réfraction responsable de l'agrandissement de l'image.
</blockquote>
</details>


2. Schématiser la situation lorsque la caméra est dans l'eau en représentant les rayons lumineux, les angles et en faisant apparaître les paramètres nécessaires.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
<img src="/schemacollerefr.png">
</blockquote>
</details>

On cherche maintenant à déterminer la distance $D$ entre la caméra et le mur.

3. Écrire la relation liant $\theta$, $c$ et $D$.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
$$\tan\theta = \frac{3,5\times c}{D}$$
</blockquote>
</details>


4. Écrire la relation liant $\theta_r$, $h$, $d$, $c$ et $D$.


<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
$$\begin{aligned}
(D-d)\tan\theta_r + h &= 2,5\times c\\
\tan\theta_r &= \frac{2,5\times c-h}{D-d}
\end{aligned}$$
</blockquote>
</details>


5. Quelles approximations peut-on faire ?


<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
$$d\ll D \;\text{  et  }\;h\ll 2,5c$$
La relation précédente devient alors :
$$
\tan\theta_r = \frac{2,5\times c}{D}
$$
</blockquote>
</details>

6. Utiliser la relation de la question 3 et Snell-Descartes pour remplacer $\theta_r$ dans la relation de la question 4 (dans sa version simplifiée).

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
$$\begin{aligned}
n_{air} \sin\theta &= n_{eau}\sin\theta_r\\
\Rightarrow \theta_r &= \sin^{-1}\left(\frac{n_{air}}{n_{eau}}\sin\theta\right)
\end{aligned}$$
Et en utilisant la relation de la question 3 :
$$\theta_r = \sin^{-1}\left(\frac{n_{air}}{n_{eau}}\sin\left(\tan^{-1}\left(\frac{3,5\times c}{D}\right)\right)\right)$$
$$\tan\theta_r = \frac{2,5c}{D}$$
devient donc :
$$\tan \left(\sin^{-1}\left(\frac{n_{air}}{n_{eau}}\sin\left(\tan^{-1}\left(\frac{3,5\times c}{D}\right)\right)\right)\right)= \frac{2,5\times c}{D}$$
</blockquote>
</details>


7. Utiliser Python pour trouver graphiquement une approximation de la solution.


<a href="https://colab.research.google.com/drive/1QD9yHmXzN25woSPemtNbuOeXNxK5frL3?usp=sharing">Lien vers notebook Colab</a>


8. Reschématiser la situation en prenant en compte les approximations faites à la question 4.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
<img src="/schemacollerefrsimpl.png">
</blockquote>
</details>

9. En utilisant les deux triangles, déterminer algébriquement $D$ en fonction de $c$, $n_{eau}$ et $n_{air}$ (partir de Snell-Descartes et utiliser la trigonométrie et Pythagore).

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
<img src="/schemacollerefrcorr.png">
$$
\begin{aligned}
n_{air} \sin\theta &= n_{eau}\sin\theta_r\\
n_{air} \frac{3,5c}{\sqrt{D^2+(3,5c)^2}} &= n_{eau} \frac{2,5c}{\sqrt{D^2+(2,5c)^2}}\\
\Rightarrow n_{air}^2 \frac{(3,5c)^2}{D^2+(3,5c)^2} &= n_{eau}^2 \frac{(2,5c)^2}{D^2+(2,5c)^2}
\end{aligned}
$$
D'où
<div style="display: flex;justify-content: center;">
<div style = "border:solid red 3px;width:min-content;padding: 0px 10px 0px 10px;font-size: 18px;">
$$D = 2,5 \times 3,5 \times c  \times \sqrt{\frac{ n_{eau}^2-n_{air}^2}{(3,5 \times  n_{air})^2 - (2,5 \times n_{eau})^2}}$$
</div></div>
Pour $\pu{c = 5,0 cm}$, on trouve $\pu{D = 35 cm}$.
</blockquote>
</details>


---

<video width="700" poster="/perchemoite.poster.webp" controls style="display:block;max-width: 100%;position:relative;margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
  <source src="https://presentationssite.github.io/perchemoite.mp4" type="video/mp4">
</video>

<br>

<video width="700" poster="/casse.poster.webp" controls style="display:block;max-width: 100%;position:relative;margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
  <source src="https://presentationssite.github.io/casse.mp4" type="video/mp4">
</video>