---
title: "Promenade"
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



# Promenade

<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/promenade.png" style="box-shadow:none;background:none;">
</div>

Alice part se promener en marchant à une vitesse de $\pu{2 km\*h-1}$.
Une heure après, Bob part avec un chien pour la rejoindre, en marchant à une vitesse de $\pu{4 km\*h-1}$. Le chien étant agité, il fait des aller-retours entre les deux, à une vitesse de $\pu{10 km*h-1}$ jusqu’à ce qu’Alice et Bob se rejoignent. 
On veut déterminer la distance  que le chien a parcouru ?

1. Superposer l'allure des courbes représentant l'abscisse sur le trajet de la promenade en fonction du temps pour Alice, Bob et le chien.

2. Appelons $D_n$ la distance séparant Alice et Bob au départ du $n$<sup>e</sup> aller-retour du chien (au moment où il repart vers Alice). 
Déterminer numériquement $\frac{D_{n+1}}{D_n}$ ainsi que la distance $d_n$ parcourue par le chien sur cet aller-retour.

3. En déduire la distance totale parcourue par le chien.

4. Comment aurait-on pu obtenir le résultat beaucoup plus rapidement ?


