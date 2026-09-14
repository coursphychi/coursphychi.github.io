---
title: "Analyse dimensionnelle"
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





# Analyse dimensionnelle

## Écoulement du verre d’un vitrail

<div style="position:relative;margin-left:auto;margin-right:auto;width:600px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/vitrail.png" style="box-shadow:none;background:none;border-radius:10px;">
</div>

On entend parfois que l’écoulement du verre des vitraux des cathédrales sous leur propre poids explique pourquoi on observe sur certains de ces vitraux que le bas est plus épais que le haut.

Déterminer par analyse dimensionnelle un temps typique pour cet écoulement à partir des deux grandeurs suivantes&nbsp;:
<ul style="margin-top:-0.5em; margin-bottom:-0.5em;">
 <li>la viscosité dynamique $\eta$  (pour le verre $\eta\approx\pu{e20 Pa*s}$),</li>
 <li>la grandeur $A$ (avec $A = \rho g H$ où $\rho$ est la masse volumique, $g$ la pesanteur et $H$ la hauteur du vitrail).</li>
 </ul> 
 
Conclure : s’agit-il d’un mythe ou est-ce vraisemblable ? 

Rq : pour comparaison, la viscosité de l’eau liquide vaut environ $\pu{e-3 Pa\*s}$, celle du miel $\pu{10 Pa\*s}$ 
et celle du plomb $\pu{e-10 Pa*s}$.

<br>


## Rayon d’un cratère d’impact météoritique

<div style="position:relative;margin-left:auto;margin-right:auto;width:600px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/crateres.png" style="box-shadow:none;background:none;border-radius:10px;">
</div>


1. Proposer une loi donnant le rayon  du cratère créé par l’impact d’un météorite en fonction de l’énergie cinétique $E_c$ du météorite, de la masse volumique $\rho$ du sol et de la pesanteur $g$. 

2. En déduire approximativement le ratio des masses des météorites ayant créés les deux cratères lunaires fléchés sur l’image ci-dessus en supposant qu’ils avaient la même vitesse.

3. Et quel serait le ratio des vitesses s’ils avaient la même masse&nbsp;?

4. En supposant un coefficient de proportionnalité proche de 1 dans la loi trouvée, donner l’ordre de grandeur de la vitesse d’une météorite d’1 kg créant un cratère de 10 m de rayon. Cette vitesse vous apparait-elle raisonnable&nbsp;? Comparez-la à la vitesse de la Terre autour du Soleil.

<br>

## Ondes de surface

Lorsqu’on perturbe la surface d’un lac (en y jetant un objet par exemple), deux types de régimes d’onde peuvent être créés en fonction de la taille de l’objet.

### Ondes capillaires 

Si l’objet est petit, on obtient des ondes dites capillaires dont la célérité dépend de la tension superficielle du fluide.

1. Retrouver par analyse dimensionnelle une relation donnant la célérité $c$ de ces ondes en fonction de la longueur d’onde $\lambda$, de la tension superficielle de l'eau $\gamma$ (force par unité de longueur), et de la masse volumique de l'eau $\rho$.

### Ondes de gravité

 Si l’objet est plus gros, on passe au régime des ondes de gravité dont la célérité $c$ ne dépend plus que de la longueur d’onde $\lambda$ et de la pesanteur $g$. 
 
 2. Déterminer cette relation.
 
 <div style="position:relative;margin-left:auto;margin-right:auto;width:400px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/capillaire.png" style="box-shadow:none;background:none;">
</div>
 
 3. D’après cette image, a-t-on lancé un gros ou un petit objet&nbsp;?
 
 <br>
 
## Bulles de savon


 <div style="position:relative;margin-left:auto;margin-right:auto;width:600px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Jean-Baptiste_Siméon_Chardin_022.jpg/1238px-Jean-Baptiste_Siméon_Chardin_022.jpg?20150210150300" style="box-shadow:none;background:none;">
</div>

 
 Faut-il souffler plus fort pour avoir des bulles plus grosses&nbsp;?
 
 1. Établir une relation liant le rayon $R$ d’une bulle de savon à la tension superficielle $\gamma$  de la bulle (la tension superficielle est une force par unité de longueur), la masse volumique $\rho$ de l’air et la vitesse $v$ du souffle.

2. Répondre à la question posée en introduction.
 
 <br>
 
## Éolienne

 <div style="position:relative;margin-left:auto;margin-right:auto;width:350px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Éolienne-tripale-st-caradec-22.gif?20241217103647" style="box-shadow:none;background:none;border-radius:10px;">
</div>


1. Proposer une loi donnant la puissance maximale $P$ qu’une éolienne peut extraire du vent en fonction de l’aire $A$ balayée par les pales, de la vitesse $v$ du vent , et de la masse volumique de l’air $\rho$.

2. Sachant que le coefficient de proportionnalité vaut $1/2$, donnée une application numérique de la puissance maximale recueillie pour un vent de 36 km/h et des pales de 60 m.

