---
title: "Slinky"
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




# La chute du Slinky

<br>
<iframe width="296" height="526" src="https://www.youtube.com/embed/k5s1cMNTmGs" title="How a slinky falls in slow motion #shorts" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="display:block;max-width:100%;position:relative;margin-left:auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);"></iframe>
<br>


1. Quel doit être le mouvement du centre de masse du slinky ?

Le code suivant modélise de manière très simplifiée le slinky en le décomposant en deux sous-systèmes&nbsp;: le premier est composé des `n_haut` premiers disques et le second des `n_bas` disques restants. Le cœur du code se situe de la ligne 48 à la ligne 59.

{{< runpython lang="vpython" mode="toggle" default="code" width="800" file="slinky.py" >}}
{{< /runpython >}}

2.  En supposant que les deux sous-systèmes sont reliés par un ressort et que le sous-système du bas est immobile, faire un bilan des forces et exprimer ces forces sur chacun des sous-systèmes.<br>
On appellera $\vec{F}\_\mathrm{bas/haut}$ la force du sous-système bas sur le sous système haut et $\vec{F}_\mathrm{haut/bas}$ celle du haut sur le bas.

3. En déduire l'accélération du sous-système du haut.

4. Expliquer le sous-bloc composé des lignes 54 à 58.

Le code suivant donne l'évolution de la position, de la vitesse et de l'accélération de chaque disque ainsi que celle du centre de masse pendant la chute.

{{< runpython lang="vpython" mode="toggle" default="code"  width="900" file="slinkygraphes.py" >}}
{{< /runpython >}}

5. Expliquer l'allure du graphe de l'accélération. Le mouvement est-il bien celui prévu à la question 1.

