---
title: "Oscillateur"
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


# Simulation d'un oscillateur mécanique


{{< runpython lang="vpython" mode="toggle" default="code" width="700" file="oscillateur.py" >}}
{{< /runpython >}}


*Oscillateur amorti par frottement fluide :* 

1. Modifier la valeur du coefficient de frottement fluide pour se placer dans le régime apériodique critique.

*Oscillateur amorti par frottement solide :* 

2. Faire les modifications nécessaires pour étudier un oscillateur amorti par frottement solide plutôt que par frottement fluide.

3. Analyser les graphes obtenus.

4. Déterminer la variation entre deux élongations maximales consécutives du ressort et vérifier sur le graphe.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
<a href="http://res-nlp.univ-lemans.fr/NLP_C_M01_G04/co/Contenu_52.html#:~:text=Pour%20un%20frottement%20solide%20la,de%20l%27oscillateur%20sans%20frottement.">Approche dynamique et énergétique</a>
</blockquote>
</details>