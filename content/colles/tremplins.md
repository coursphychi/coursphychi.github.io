---
title: "Tremplins"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
hidden: true
---




# Course de tremplins

Deux balles dévalent chacune un tremplin différent dont les points de départ et d'arrivée ont même altitude&nbsp;:

![tremplins](/tremplins.png)



Les différentes coordonnées sont données ci-dessous. <br>Les deux balles sont supposées ponctuelles et on prendra g = 9.8 m.s<sup>-2</sup>. <br>La boule jaune suit la ligne brisée ABC et la boule rouge suit ADEC.

![ccordtremplins](/coordtremplins.png)



Questions préliminaires :

1. Qulle balle atterrit le plus loin&nbsp;?
2. Quelle balle parcourt le moins de distance&nbsp;?
3. Quelle balle arrive la première en C&nbsp;?

Vérification par simulation :

{{< runpython lang="vpython" mode="output"  width="800" file="tremplins.py" autorun="true">}}
{{< /runpython >}}

Résolution :

4. Déterminer la durée mise pour chacune des balles pour atteindre le sol (y = -4). Confirmez-vous les valeurs de la simulation&nbsp;? Commenter.

[Vidéo de Bruce Yeany sur des tremplins ressemblants](http://www.youtube.com/watch?v=88NZStgiIt0).

<br>

## Petits suppléments : brachistochrone et tautochrone

Vous pouvez modifier sur le programme ci-dessous la courbe que suit la balle entre deux points fixes. <br>Vous pouvez tenter par exemple de construire le chemin le plus court ou envoyer directement la balle le plus bas possible, là où la vitesse est plus grande. 

Que remarquez-vous sur les temps de parcours obtenus par rapport au temps de parcours sur la courbe initiale&nbsp;?

Cette courbe est une cycloïde et s'appelle la **brachistochrone**.

{{< runpython lang="vpython" mode="output" fit="native" file="brachi.py" autorun="true" />}}

Une autre cycloïde intéressante, la **tautochrone**.

Changez la position initiale de la balle verte sur la courbe, que remarquez-vous&nbsp;?


{{< runpython lang="vpython" mode="output"  width="800" fit="native" file="tautochrone.py" autorun="true">}}
{{< /runpython >}}

[Petite vidéo de Bruce Yeany](https://www.youtube.com/watch?v=QL6HkOukxLA) donnant l'intuition pour comprendre la propriété de cette courbe.



**Python :**

Et pour finir, [un lien](https://scipython.com/blog/the-brachistochrone-problem/) vers un programme Python permettant de tracer la brachistochrone (utilisation de tableaux `numpy`, utilisation de la librairie `scipy` pour trouver une racine via la méthode de Newton et pour intégrer via `quad`, et utilisation de `matplotlib` pour tracer).