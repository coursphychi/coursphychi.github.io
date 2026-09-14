---
title: "Conduction thermique"
date: 2021-03-06T14:23:56+01:00
weight : 6
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


# Conduction thermique


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tsti/conduction"> Cours </a></p>

<br>

## Rappels

<details>
<summary><a>Les 3 modes de <span style="font-weight:bold">transferts thermiques</span> sont&nbsp;:</a></summary>
<blockquote>
<ul>
<li><details>
<summary><a>la <span style="font-weight:bold">conduction</span>&nbsp;:</a></summary>
<p>
agitation moléculaire qui se transmet de proche en proche dans un matériau.
</p>
</details></li>

<li><details>
<summary><a>la <span style="font-weight:bold">convection</span>&nbsp;:</a></summary>
<p>
mouvement d'ensemble de la matière dans un fluide type air ou eau.
</p>
</details></li>

<li><details>
<summary><a>le <span style="font-weight:bold">rayonnement</span>&nbsp;:</a></summary>
<p>
transfert à distance, même dans le vide, par des ondes électromagnétiques ayant un spectre de type corps noir.<br>
C'est comme ça que le soleil nous chauffe.
</details></li>

</ul>
</blockquote>
</details>

<br>

<details>
<summary><a>Questions :</a></summary>
<ol>
    
<li><details>
<summary>Quel <a>mode de transfert thermique</a> est-il illustré dans cette expérience&nbsp;? Et quel serait l'effet de changer le métal de la tige&nbsp;?
<p style="text-align:center">
<iframe width="420" height="240"
src="https://www.youtube.com/embed/LxJoLeeqk88" allow="fullscreen;">
</iframe>
</p>

</summary>
<blockquote>
<p>
La conduction. Le transfert thermique de proche en proche sera d'autant plus rapide que la conductivité thermique du métal est élevée.
<p style="text-align:center">
<iframe width="420" height="240"
src="https://www.youtube.com/embed/RHQ17S72ON4" allow="fullscreen;">
</iframe>
</p>

</p>
</blockquote>
</details>
</li>
    
<li><details>
<summary>Quel <a>mode de transfert</a> est illustré par cette vidéo ?
<p style="text-align:center">
<video src="/convection.mp4" width="20%" type="video/mp4" autoplay="true" loop="true"  preload="auto" controls muted></video>
</p>
</summary>
<blockquote>
<p>
La convection (l'air chaud monte sous l'effet de la gravité)
<img src="/flammespace.png">
</p>
</blockquote>
</details>
</li>

<li><details>
<summary><a>Qu'est-ce que c'est&nbsp;?</a> Expliquer leurs formes, le matériau utilisé et leur orientation&nbsp;?
<p style="text-align:center">
<img src="/heatsinks.png">
</p>
</summary>
<blockquote>
<p>
Souvent en aluminium car bonne conductivité thermique, leur forme vise à maximiser la surface d'échange et l'orientation permet à l'air chaud de s'élever par convection et donc d'être remplacé.
</p>
</blockquote>
</details>
</li>

<li><details>
<summary>Pourquoi <a>un glaçon</a> fond-il moins vite dans de l'eau salée que dans de l'eau douce&nbsp;?
</summary>
<blockquote>
<p>
L'eau salée est plus dense que l'eau douce issue de la fusion du glaçon et cette eau froide reste alors en haut, au contact du glaçon plutôt que s'homogénéiser avec le reste de l'eau par convection. 
</p>
</blockquote>
</details>
</li>
<br>
<li><details>
<summary>Qu'ont en commun les meilleurs <a>isolants thermiques</a>&nbsp;?
<img src="/differentesconductivites.png">
</summary>
<blockquote>
<p>
Ils emprisonnent de l'air. Et dans le cas de l'aerogel, les cavités sont si petites (de l'ordre du nm) que la conduction y est plus difficile que dans l'air libre (et la convection est bien sûr complètement absente).
</p>
<p style="text-align:center">
<iframe width="420" height="240"
src="https://www.youtube.com/embed/AeJ9q45PfD0" allow="fullscreen;">
</iframe>
</p>
</blockquote>
</details>
</li>

<li><details>
<summary><a>Comment expliquer</a> ce qu'on voit dans cette vidéo&nbsp;?<br>
<p style="text-align:center">
<iframe width="420" height="315"
src="https://www.youtube.com/embed/Pp9Yax8UNoM" allow="fullscreen;">
</iframe>
</p>
</summary>
<blockquote>
<p>
Dans ce matériau très isolant, le flux thermique dû à la conduction thermique du centre vers les bords (en particulier les coins) n'arrive pas à compenser le flux thermique radiatif sortant. Résultat : les coins se refroidissent rapidement ($\approx\pu{35 ^\circ C}$) malgré que le centre soit encore à plus de ($\pu{1200 ^\circ C}$)&nbsp;!
</p>
</blockquote>
</details>
</li>

</ol>
</details>

<br>

## Savoir et savoir faire

{{%notice coeur%}}
<input type="checkbox"> Définir un **flux thermique** et le calculer.<br><br>
<input type="checkbox"> Savoir comment le flux thermique évolue en fonction de l'écart de température et de la résistance thermique.<br><br>
<input type="checkbox"> Calculer la valeur de la **résistance thermique** d’une paroi à partir de son épaisseur et de la conductivité thermique du matériau.<br><br>
<input type="checkbox"> Calculer la résistance thermique d’une paroi composée de plusieurs couches de matériaux différents.
{{%/notice%}}


{{%notice piege%}}
La résistance thermique telle que définie dans la présentation est en réalité la **résistance thermique surfacique**.<br>
La vraie résistance thermique est définie par $R_{th}=\frac{e}{S \lambda}$ et s'exprime en $\pu{K * W-1}$.<br>
Avec cette définition, on a $\Phi = \frac{\Delta \theta}{R_{th}}$.<br>
Cependant, le programme semble préférer la résistance thermique surfacique tout en l'appelant "résistance thermique", ce qui peut prêter à confusion, mais cela semble aussi être l'usage dans le secteur du bâtiment.<br>
Moralité, faites très attention aux unités et sachez que les deux définitions existent.
{{%/notice%}}



{{%notice note%}}

Pour **mesurer une résistance thermique**, on utilise un appareil capable de mesurer le **flux thermique**.<br>
Lorsqu'on dispose d'un échantillon, on peut utiliser un appareil un peu encombrant constitué de deux plaques métalliques dont l'une est reliée à une résistance électrique.<br>
Le matériau dont on cherche à mesurer la résistance thermique est placé entre deux plaques métalliques.<br>
La plaque du bas est au contact d’une source froide dont la température n’est pas réglable tandis que la plaque du haut est au contact d’une résistance électrique qui joue le rôle de la source chaude.<br>
L’appareil mesure la tension et l’intensité de la résistance ainsi que les températures des deux plaques une fois le régime permanent atteint.<br>
La puissance électrique de la résistance constituant la source chaude est égale au flux thermique traversant le matériau testé.
<br><br>
Mais pour mesurer la résistance thermique d'une paroi sur site, on ne peut pas utiliser cet apapreil. On se tourne alors vers des **fluxmètres thermiques** beaucoup moins encombrant constitués d'une seule plaque.<br>
On place la plaque contre la paroi (à l'intérieur ou à l'extérieur) pour mesurer le flux entrant ou sortant et on mesure préciséments la température de chaque côté de la paroi. Le principe est que le flux qui sort ou entre dans une paroi est aussi le flux qui la traverse (en régime permanent).<br>
Pour des mesures officielles, [une norme existe](https://pure.tudelft.nl/ws/portalfiles/portal/51444610/1_s2.0_S0378778818314282_main.pdf).
{{%/notice %}}


<br>

## Documents


- [**Activité : amélioration de l'isolation d'une maison par l'extérieur** (issue du manuel Nathan)](/act-conduct.pdf)<br>
- [**Stockage d'une carotte de glace** (extrait sujet 2021 candidat libre remplacement)](/exo-paroi-glace.pdf)
- [**Exercice course de glaçons**](/conduction-1.pdf)
- [**Exercice salle de classe**](/conduction-2.pdf)
- [**Exercice igloo**](/conduction-4.pdf)


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

Le flux thermique se mesure&nbsp;:

- [x] en W
- [ ] en J
- [ ] en  K


##

Si on double la surface d'une paroi, le flux thermique à travers cette paroi&nbsp;:

- [x] est multiplié par 2
- [ ] est divisé par 2
- [ ] reste inchangé



##

Si on augmente la résistance thermique d'une paroi, le flux thermique à travers cette paroi&nbsp;:


- [x] diminue
- [ ] augmente
- [ ] ne change pas



##

Si l'écart de température entre l'intérieur et l'extérieur est divisé par 2, le flux thermique à travers la paroi&nbsp;:


- [ ] est multiplié par 2
- [ ] reste inchangé
- [x] est divisé par 2


##

La résistance thermique d'une paroi homogène&nbsp;:

- [x] dépend du matériau constituant la paroi
- [x] augmente avec l'épaisseur de la paroi
- [ ] augmente avec la surface de la paroi


##

Lorsqu'un matériau isolant se tasse, sa résistance thermique&nbsp;:

- [x] diminue
- [ ] augmente
- [ ] ne varie pas

##

20 cm d'épaisseur d'un matériau ayant une conductivité thermique de $\pu{1,0 W*m-1*K-1}$ a une résistance thermique de&nbsp;:

- [ ] $\pu{0,05 m2*K*W-1}$
- [x] $\pu{0,20 m2*K*W-1}$
- [ ] $\pu{20 m2*K*W-1}$

##

On ajoute à une paroi dont la résistance thermique mesure $\pu{2,0 m2*K*W-1}$, un matériau isolant dont la résistance thermique mesure $\pu{4,0 m2*K*W-1}$. La nouvelle résistance thermique de la paroi vaut&nbsp;:

- [ ] $\pu{8,0 m2*K*W-1}$
- [x] $\pu{6,0 m2*K*W-1}$
- [ ] $\pu{3,0 m2*K*W-1}$


##

Un ordre de grandeur de la résistance thermique de 20 cm d'épaisseur d'un matériau isolant est&nbsp;:

- [ ] $\pu{5E2 m2*K*W-1}$
- [x] $\pu{5 m2*K*W-1}$
- [ ] $\pu{0,05 m2*K*W-1}$

> [valeurs usuelles](https://presentationssite.github.io/tsti/conduction/#/1/4)

##

Pour une épaisseur usuelle, on peut négliger la résistance thermique des matériaux suivant devant celle de 20 cm de parpaing&nbsp;:

- [ ] de la paille en botte
- [x] du carrelage
- [ ] du polystyrène expansé

> [valeurs usuelles](https://presentationssite.github.io/tsti/conduction/#/1/4)

{{< /quizdown >}}

