---
title: "Son"
date: 2021-03-06T14:23:56+01:00
weight : 11
draft: false
---

<style>
ul {
  text-align: left;
}
table {
  border-collapse: collapse;
  border: 0;
}
td, th {
  border-collapse: collapse;
  text-align: center;
  vertical-align: middle;
}
</style>

# Signal sonore


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/2nde/son"> Cours </a></p>


[![](/cm-son.png)](/cm-son.pdf)



## Documents et autre

<div style="overflow-x: auto;">
<table>
<tr>
<th rowspan="3">Exercices</th>
<td style="border-bottom:none;"><a href="/exovitson.pdf"><b>Mesure historique de la vitesse du son dans l'eau</b></a></td>
</tr>
<tr>
<td style="border-top:none;border-bottom:none;"><a href="/exosonar.pdf"><b>Sonar</b></a> + <a href="/exosonar-corr.pdf"><b style="color:#FFA601;">correction</b></a></td>
</tr>
<tr>
<td style="border-top:none;"><a href="/exotessiture.pdf"><b>Tessiture</b></a> + <a href="https://www.desmos.com/calculator/jo42kizxcc"><b style="color:#00AB8E;">graphique</b></a></td>
</tr>
<tr>
<th rowspan="2">TP</th>
<td style="border-bottom:none;"><a href="/tpvitson2nde.pdf"><b>Mesure de la vitesse du son</b></a></td>
</tr>
<tr>
<td style="border-top:none;"><a href="/tpmusic.pdf"><b>Analyse d'un son musical</b></a></td>
</tr>
<tr>
<th rowspan="1">Webapp</th>
<td><a href="https://www.compadre.org/osp/pwa/soundanalyzer/"><b>Obtention d'un oscillogramme depuis le son du micro</b></a></td>
</tr>
</table>
</div>

<br>

## Quiz

{{< quizdown >}}

---
primary_color: steelblue
secondary_color: "#f2f2f2"
text_color: black
shuffle_questions: false

---

## Son

Un signal sonore est créé&nbsp;:

- [x] quand un objet se met à vibrer dans un milieu matériel
- [ ] uniquement s'il y a une caisse de résonance
> Elle ne sert qu'à amplifier le son
- [ ] seulement si on l'entend


## Propagation

Lorsqu'un signal sonore se propage&nbsp;:

- [ ] les molécules ou les atomes du milieu se déplacent de l'émetteur du son jusqu'aux oreilles
- [x] les molécules ou les atomes du milieu oscillent sur place

## Milieu

- [x] Le son se déplace plus vite dans l'eau que dans l'air
- [ ] Le son se déplace plus vite dans le vide que dans l'air
- [ ] Le son se déplace plus vite dans l'eau que dans l'acier

## Hauteur

La hauteur d'un son&nbsp;:

- [ ]  est liée à l'intensité de ce son
- [ ]  est liée à la vitesse du son
- [x]  est liée à la fréquence du son

## Hauteur et vitesse

Un ultrason se déplace plus vite qu'un son audible.

- [x] faux
- [ ] vrai

## Fréquence

La période est&nbsp;:

- [x] inversement proportionnelle à la fréquence
- [ ] proportionnelle à la fréquence
- [ ] sans lien avec la fréquence

## Unité 

L'unité de la fréquence, le hertz (Hz), est équivalent à&nbsp;:

- [x] $\pu{s-1}$
- [ ] $\pu{m*s-1}$
- [ ] $\pu{s*m-1}$

## Intensité sonore

Lorsque l'amplitude du signal sonore double, l'intensité sonore&nbsp;:

- [x] double
- [ ] ne varie pas
- [ ] augmente de 3 dB
- [ ] est divisée par deux

## Niveau sonore

Lorsque l'amplitude du signal sonore double, le niveau sonore&nbsp;:

- [ ] double
- [ ] ne varie pas
- [x] augmente de 3 dB
- [ ] est divisée par deux

## Tympan 

Une onde sonore produit une succession locale de surpressions/dépressions dans le milieu de propagation. Au niveau de l'oreille, cette variation de la pression acoustique met en mouvement la membrane du tympan.<br><br>
Au seuil d'audibilité correspondant au niveau sonore de $\pu{0 dB}$, la surpression est de $20 \text{ μPa}$ (le tympan ne bouge alors que de quelques nanomètres) alors qu'au seuil de douleur ($\pu{120 dB}$), la surpression est de $\pu{20 Pa}$. L'intensité sonore étant proportionnelle au carré de la pression acoustique, combien de fois est-elle plus grande au seuil de douleur qu'au seuil d'audibilité&nbsp;?

- [x] mille milliards
- [x] $10^{12}$
- [ ] $120$
- [ ] un million
- [ ] $10^7$

## Spectre sonore

Le domaine des sons audibles pour l'Homme s'étend de&nbsp;:

- [x] de $\pu{20 Hz}$ à $\pu{20 kHz}$
- [ ] de $\pu{0 Hz}$ à $\pu{20 Hz}$
- [ ] de $\pu{20 Hz}$ à $\pu{20 MHz}$

## Sons différents

Deux signaux de même fréquence, de même amplitude mais de formes différentes se distinguent par&nbsp;:

- [x] leur timbre
- [ ] leur hauteur
- [ ] leur niveau sonore

## Formule

Connaissant la vitesse $v_{son}$ du son dans un milieu, comment peut-on calculer la distance $d$ parcourue entre un émetteur et un récepteur si on a mesuré la durée $\Delta t$ entre l'émission et la réception&nbsp;?

- [x] $d=v_{son}\times \Delta t$
- [ ] $d=\frac{\Delta t}{v_{son}}$
- [ ] $d=\frac{v_{son}}{\Delta t}$

## Concert

Un concert de rock se tient dans un stade. Il y a des enceintes près de la scène et d'autres à $d=\pu{102 m}$ pour les spectateurs les plus éloignés.<br><br>

Le signal électrique dans les câbles se déplaçant beaucoup plus vite que le son, il faut retarder artificiellement le signal des enceintes du fond pour que le son qu'elles émettent se superpose bien à celui émis par la scène.<br><br>

De quelle valeur doit être le délai&nbsp;?

> Dans l'air : $v_{son} = \pu{340 m*s-1}$

- [x] $\pu{300 ms}$
- [x] $\pu{0,300 s}$
- [ ] $\pu{3,5 s}$
- [ ] $\pu{35 ms}$

## Feu d'artifice

Léo-Paul regarde depuis le port de la Pelle à Marsilly le feu d'artifice du 14 juillet de Saint-Martin de Ré. Combien de temps met le son d'une explosion à lui parvenir&nbsp;?

> Dans l'air : $v_{son} = \pu{340 m*s-1}$<br>
[Google Earth](https://earth.google.com/web/)

- [x] $\pu{47 s}$
- [ ] $\pu{47 ms}$
- [ ] $\pu{21 s}$
- [ ] $\pu{21 ms}$

{{< /quizdown >}}


