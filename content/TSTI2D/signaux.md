---
title: "Signaux"
date: 2021-03-06T14:23:56+01:00
weight : 9
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

# Signaux


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tsti/signaux"> Cours </a></p>

<br>

## Rappels

Un **signal** est une quantité qui dépend du temps.<br>
Mathématiquement, un signal est modélisé par une fonction $t\mapsto f(t)$ qui à chaque instant $t\in \mathbb{R}$ associe une valeur $f(t)$.
<details>
<summary>
Qu'est-ce qu'un <a><b>signal périodique</b></a>&nbsp;?</summary>
<blockquote>
Un signal périodique est un signal qui se répète à l'identique dans le temps.<br>
La durée d'une répétition est appelée période et est notée $T$ (unité de base : la seconde).<br>
Mathématiquement, on dit qu’une fonction $f:\mathbb{R}\rightarrow\mathbb{R}$ est périodique de période $T>0$ lorsque la relation $f(t+T)=f(t)$ est satisfaite pour tout $t\in\mathbb{R}$.
<div style="position:relative;width:700px;max-width:100%;margin:auto;">
<img src="https://images.math.cnrs.fr/freeze/img/png/periodic.png" >
</div>
</blockquote>
</details>

<br>
<details>
<summary>
Qu'est-ce que la <b><a>fréquence</a></b> d'un signal périodique&nbsp;?</summary>
<blockquote>
La fréquence, notée $f$, est le nombre de fois que le signal se répète par unité de temps.<br>
Unité de base : le hertz $\pu{Hz}$<br>
$\pu{1 Hz}= \pu{1 s-1}$.<br>
<span style="font-weight:bold">La fréquence est l'inverse de la période</span>.
<div style="display: flex;justify-content: left;">
<div style = "border:solid red 2px;width:min-content;padding: 0px 8px 0px 10px;">
$$f=\frac{1}{T}$$
</div></div>
</blockquote>
</details>

<br>

## Manipulation d'un spectre


<p style="text-align:left;">
<a href="https://www.geogebra.org/m/s4jhpvt2" style="font-weight:bold;">Appliquette geogebra</a>
</p>

<br>



## Savoir et savoir faire

{{%notice coeur%}}
<input type="checkbox"> Savoir qu'un **signal périodique** quelconque peut être **décomposé** en une **somme** d’un **signal continu** (composante continue) et de **signaux sinusoïdaux** (**les harmoniques**).
<br><br>
<input type="checkbox"> Savoir identifier la **fréquence du fondamental** (harmonique de rang 1) d’un signal périodique.
<br><br>
<input type="checkbox"> Déterminer la **valeur absolue de la composante continue** à partir du **spectre d’amplitude** d’un signal.
<br><br>
<input type="checkbox"> Déterminer l’**amplitude** et la **fréquence** du **fondamental** et des **harmoniques** présents à partir du **spectre d’amplitude** d’un signal.
<br><br>
<input type="checkbox"> Déterminer le **rang d’un harmonique** à partir de sa fréquence et de la fréquence du signal.
<br><br>
<input type="checkbox"> Déterminer l’**intervalle de fréquence nécessaire** pour **transmettre** un signal comportant un ensemble d’harmoniques choisis.
{{%/notice%}}


{{%notice note%}}
Un [super cours un peu poussé](https://images.math.cnrs.fr/freeze/Analyse-frequentielle-du-signal.html) pour ceux que le sujet intéresse et qui voudraient creuser.
{{%/notice%}}

<br>

## Exercices

- [**Spectre d'amplitude** (extrait sujet zéro)](/suj0harm.pdf)
- [**Transmission du signal** (un peu plus loin dans l'exo précédent)](/suj0transm.pdf)
- [**Antenne et bande passante** (extrait sujet 2022 métropole remplacement)](/exobacsontalkiewalkie.pdf)
- [**Radiotelescope + Canal 16**](/exo-signaux.pdf)


<br>

## Quiz

{{< quizdown >}}

---
primary_color: steelblue
secondary_color: "#f2f2f2"
text_color: black
shuffle_questions: false

---

##

![](/quiz3signaux.png)<br>

Parmi les trois signaux, y en a t-il un qui n'est pas périodique&nbsp;?

- [x] aucun des trois
- [ ] le signal (a)
- [ ] le signal (b)
- [ ] le signal (c)

##

![](/quiz3signaux.png)<br>

Parmi les trois signaux, y en a t-il un qui n'a pas de composante continue&nbsp;?

- [ ] le signal (a)
- [ ] le signal (b)
- [x] le signal (c)
- [ ] aucun des trois

##

![](/quiz3signaux.png)<br>

Que peut-on dire de la période de ces trois signaux&nbsp;?

- [ ] ils ont tous une période différente
- [x] ils ont tous la même période
- [ ] seuls les signaux (a) et (c) ont la même période


##

![](/quiz3signaux.png)<br>

Que peut-on dire de la fréquence du fondamental de ces trois signaux&nbsp;?

- [ ] ils en ont tous une différente
- [x] ils ont tous la même
- [ ] seuls les signaux (a) et (c) ont la même

##

![](/quizspectrea.png)<br>

Ci-dessus, le spectre d'amplitude du signal&nbsp;(a).<br><br>

La fréquence du fondamental du signal&nbsp;(a) vaut&nbsp;:

- [ ] 0 Hz
- [x] 160 Hz
- [ ] 320 Hz

##

![](/quizspectrea.png)<br>

L'amplitude de l'harmonique de rang 2 du signal&nbsp;(a) vaut&nbsp;:

- [ ] 0,5 V
- [x] 1 V
- [ ] 2 V


##

![](/quiz3signaux.png)<br>

Quel est le spectre d'amplitude du signal&nbsp;(b)&nbsp;?


- [x] ![](/quizspb2.png)
- [ ] ![](/quizspb1.png)
- [ ] ![](/quizspb3.png)



##

![](/quiz3signaux.png)<br>

Quel est le spectre d'amplitude du signal&nbsp;(c)&nbsp;?


- [x] ![](/quizspc2.png)
- [ ] ![](/quizspc1.png)
- [ ] ![](/quizspc3.png)



##

Enregistrement d'un signal et son spectre&nbsp;:<br>
![](/quizsignsp.png)<br>

La fréquence du signal vaut&nbsp;?

- [x] 10 Hz
- [ ] 50 Hz
- [ ] 100 Hz


##

Enregistrement d'un signal et son spectre&nbsp;:<br>
![](/quizsignsp.png)<br>

Le rang de la dernière harmonique du signal est&nbsp;:

- [ ] 10
- [ ] 6
- [x] 13


##

Enregistrement d'un spectre d'amplitude d'un signal obtenu par modulation de fréquence&nbsp;:<br>
![](/quizspfm.png)<br>

Que peut-on dire du signal&nbsp;?

- [ ] il est sinusoïdal
- [x] il n'est pas audible par l'oreille humaine
- [ ] il possède une composante continue


##

![](/quizspfm.png)<br><br>
Pour transmettre correctement ce signal, on aura besoin d'une bande passante d'au moins&nbsp;:

- [x] 10 kHz de largeur
- [ ]  5 kHz de largeur
- [ ] 20 kHz de largeur
- [ ] 50 kHz de largeur


##

Les ondes utilisées dans les télécommunications sont&nbsp;:

- [x] des ondes radios
- [x] des ondes lumineuses
- [x] des ondes infrarouges

##

Les ondes radios sont les ondes électromagnétiques ayant&nbsp;:

- [ ] les fréquences les plus élevées
- [x] les longueurs d'onde les plus élevées
- [x] les fréquences les plus faibles


##

Un rayonnement de longueur d'onde $\lambda= \pu{1300 nm}$ correspond à un rayonnement&nbsp;:

- [ ] radio
- [x] infrarouge
- [ ] visible

##

La transmission d'une onde radio nécessite&nbsp;:

- [x] une antenne émettrice et une antenne réceptrice
- [ ] une fibre optique
- [ ] un milieu matériel obligatoirement


##

Plus la fréquence de l'onde radio est faible,

- [x] plus la dimension de l'antenne doit être élevée
- [ ] plus la dimension de l'antenne doit être faible
- [ ] cela ne joue pas sur la dimension de l'antenne


##

La dimension de l'antenne est en théorie&nbsp;:

- [x] du même ordre de grandeur que la longueur d'onde de l'onde radio à laquelle elle est sensible
- [ ] beaucoup plus grande que la longueur d'onde de l'onde radio à laquelle elle est sensible
- [ ] inversement proportionnelle à la longueur d'onde de l'onde radio à laquelle elle est sensible

##

Une fibre optique transporte,

- [x] la lumière
- [ ] une onde radio
- [ ] la lumière et une onde radio

##

![](/signalam.png)
Ce signal est modulé en&nbsp;:

- [x] amplitude
- [ ] fréquence
- [ ] phase

##

La porteuse est un signal&nbsp;:

- [x] de haute fréquence
- [ ] de basse fréquence
- [ ] de fréquence audible


##

Le signal modulant est&nbsp;:

- [x] de basse fréquence
- [x] le signal à transmettre
- [ ] de haute fréquence

##

Comment peut-on transmettre différents signaux dans un même milieu&nbsp;?

- [x] Grâce à des porteuses de fréquence différente suffisamment éloignées les unes des autres
- [x] Grâce à la transposition en fréquence
- [ ] En ayant un câble différent par signal.


{{< /quizdown >}}