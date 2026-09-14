---
title: "Pression"
date: 2021-03-06T14:23:56+01:00
weight : 16
draft: false
---

<style>
details summary { cursor:pointer; }

details summary::-webkit-details-marker { display:none; } /* WebKit */
details summary { list-style:none; }                      /* Firefox */

/* triangle personnalisé AVANT le texte */
details summary::before {
  content:"▸";
  display:inline-block;
  margin-right:0.4em;
  font-size:0.8em;
  transition:transform .2s ease;
}

details[open] > summary::before {
  transform:rotate(90deg);
}
</style>


# Pression et statique des fluides


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tsti/pression"> Cours </a></p>



[![](/cmpression.png)](/cmpression.pdf)


<br>


## Savoir et savoir faire


{{%notice coeur%}}
<input type="checkbox"> Définir la **pression exercée sur une surface** à partir de la **résultante des forces pressantes** appliquées.<br><br>
<input type="checkbox"> Distinguer la **pression absolue** de la **pression relative**.<br><br>
<input type="checkbox"> Citer et exploiter le **principe fondamental de
l'hydrostatique**.<br>
{{%/notice%}}


{{%notice piege%}}
Le principe fondamental de l'hydrostatique peut s'écrire différemment suivant l'orientation des axes (parle-t-on de la hauteur ou de la profondeur ?) et suivant si on considère les élévations $z$ ou leur écart $\Delta z = z_2-z_1 = h$.<br>
$\uparrow$ Ainsi, avec un axe dirigé vers le haut, $z_2$ est au-dessus de $z_1$. Et on a&nbsp;:<br>
$P_1 + \rho g z_1 = P_2 + \rho g z_2$<br>
$\Rightarrow P_2 - P_1 = -\rho g (z_2-z_1) \Leftrightarrow \Delta P = -\rho g h$ (**plus on est haut, plus la pression diminue**).<br>
$\downarrow$ Si l'axe vertical est vers le bas, $h$ désignant alors la profondeur ($z_2$ en dessous de $z_1$ pour un $h=\Delta z >0$) et $\Delta P = P_2-P_1$ désigne maintenant l'élévation de pression en fonction de la profondeur. On a alors&nbsp;:<br>
$\Delta P = \rho g h$ (**plus on est profond, plus la pression augmente**).
{{%/notice%}}


<br>

## TP

- [**Principe fondamental de l'hydrostatique**](/tppression.pdf)
- [**Simulation expérience**](https://www.geogebra.org/m/dgyzejbh)


<br>

## Activités

- [**Canalisations**](/canalisations.pdf)
- [**Exercice Nautile**](/actnautile.pdf)
- [**Densimètre et fontaine de Héron**](/collehydrostatique.pdf)

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube -Zq_fmPz9IU >}}
</div>

[**Très chouette explication (+ une autre fontaine)**](https://genuineideas.com/ArticlesIndex/halitefountain.html)

-  [**Un évier à base de pailles**](/collefaucet.pdf)

<video width="400" controls style="display:block;max-width:100%;position:relative;margin-left:auto;margin-right: auto; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
  <source src="/faucet.mp4" type="video/mp4">
</video>



