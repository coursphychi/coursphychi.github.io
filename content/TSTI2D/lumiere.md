---
title: "Lumière"
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


# Énergie transportée par la lumière


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tsti/lumiere"> Cours </a></p>

<br>

## Rappels

<details>
<summary>
<a>Lien entre la fréquence $f$ et la longueur d'onde $\lambda$&nbsp;?</a></summary>
<blockquote>
<div style="display: flex;justify-content: left;">
<div style = "border:solid red 2px;width:min-content;padding: 0px 10px 0px 10px;">
$$\lambda=\frac{c}{f}$$
</div></div>
<br>
Où $c$ est la célérité (vitesse) de la lumière<br>
$c = \pu{3,0*10^8 m*s-1}$
</blockquote>
</details>

<br>

<details>
<summary>
Étendue en longueurs d'ondes de la <a>partie <span style="font-weight:bold">visible</span></a> du spectre électromagnétique&nbsp;?</summary>
<blockquote>
<div style="position:relative;width:800px;max-width:100%;margin:auto;">
<img src="/spectrelmag.png" style="width:content"/>
</div>
</blockquote>
</details>

<br>

## Simulations

- Photons et niveaux d'énergie (spectres)&nbsp;: [**applet Geogebra**](https://www.geogebra.org/m/kMx37ken)

- Tracé d'une caractéristique&nbsp;: [**applet Geogebra**](https://www.geogebra.org/m/u27ch5v7) + [**activité**](/TP-PV.pdf)

<br>

## Savoir et savoir faire

{{%notice coeur%}}
<input type="checkbox"> Interpréter les échanges d’énergie entre la matière et la lumière à l’aide de la notion de **photon**.
<br><br>
<input type="checkbox"> Citer et exploiter la relation $ΔE = h\cdot f$ reliant une variation d’énergie à la fréquence des photons émis ou reçus.
<br><br>
<input type="checkbox"> Identifier les formes d’énergie mises en jeu dans une **conversion photovoltaïque** et une **conversion photothermique**.
<br><br>
<input type="checkbox"> Exploiter les **caractéristiques tension-courant** d’un panneau photovoltaïque pour identifier son point de fonctionnement.
<br><br>
<input type="checkbox"> Réaliser le **bilan de puissance** pour déterminer le **rendement** d’une conversion photovoltaïque et d’une conversion photothermique.
{{%/notice%}}



{{%notice piege%}}
L'**irradiance**, qui est la puissance radiative reçue par mètre carré (unité : $\pu{W*m-2}$), peut aussi être appelé **éclairement énergétique**.<br> Et la lettre pour désigner cette grandeur peut varier ! Fiez-vous à l'unité.
{{%/notice%}}


<br>

## Exercices

- [**caractéristiques et point de fonctionnement**](/exo-pv-pt-fctnmt.pdf) - <a href="/exo-pv-pt-fctnmt-corr.pdf" style="font-weight:bold;color:green">Correction</a>
- [**refuge de montagne** (extrait sujet 2022 métropole)](/exo-bac-pvthermique.pdf) - <a href="https://presentationssite.github.io/tsti/correc-lumiere" style="font-weight:bold;color:green">Correction</a>


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

La lumière est&nbsp;:

- [x] constituée de photons
- [ ] constituée de phonons
- [x] une onde électromagnétique

##

Un rayonnement gamma a pour fréquence $\pu{7,7E19 Hz}$. L'énergie du photon associé est&nbsp;:

- [x] $\Delta E = hf$
- [x] $\pu{5,1E-14 J}$
- [ ] $\displaystyle \Delta E = \frac{hc}{f}$

##

L'énergie d'un photon de 3,5 eV est égale à&nbsp;:

- [ ] $\pu{2,2E19 J}$
- [x] $\pu{5,6E-19 J}$
- [ ] $\pu{4,6E-20 J}$

> $\pu{1,0 eV}=\pu{1,6E-19 J}$

##

La longueur d'onde dans le vide d'un rayonnement associé à un photon d'énergie $\Delta E = \pu{2,34E-19 J}$ est&nbsp;:

- [ ] $\pu{85 \mu m}$
- [x] $\pu{850 nm}$
- [x] $\pu{8,50E-7 m}$

##

Un panneau solaire thermique fournit&nbsp;:

- [x] une énergie thermique
- [ ] une énergie lumineuse
- [ ] une énergie électrique


##

Le rendement d'un panneau solaire thermique est le rapport des puissances&nbsp;:


- [x] $\frac{P_{thermique}}{P_{rayonnante}}$
- [ ] $\frac{P_{rayonnante}}{P_{thermique}}$
- [ ] $\frac{P_{électrique}}{P_{rayonnante}}$



##

Une masse de $\pu{1,0 kg}$ d'eau subissant une élévation de température de $\pu{50 ^\circ C}$ reçoit une énergie thermique de&nbsp;:


- [x] $\pu{58 Wh}$
- [ ] $\pu{7,6E8 Wh}$
- [x] $\pu{2,1E5 J}$

> $c_{eau}=\pu{4,18E3 J*kg-1*^\circ C-1}$

##

On a représenté ci-dessous la caractéristique $I(U)$ d'une cellule photovoltaïque.<br><br>
![](/caractnue.png)<br><br>
Que vallent la tension en circuit ouvert $U_{co}$ et l'intensité de court-circuit $I_{cc}$&nbsp;?

- [x] $\pu{8,08 V}$ et $\pu{1,05 A}$
- [ ] $\pu{7,0 V}$ et $\pu{1,0 A}$
- [ ] les valeurs de la tension et de l'intensité au point de fonctionnement à puissance maximale.


##

![](/caractass.png)<br><br>
La caractéristique ci-dessus correspond à une association de deux cellules identiques à celle de la question précédente.<br>
Il s'agit&nbsp;:

- [x] d'une association série
- [ ] d'une association parallèle
- [ ] d'une association libre


##

On a maintenant superposé la courbe de la puissance délivrée $P(U)$ à la caractéristique.<br><br>
![](/caractpuiss.png)<br><br>
les valeurs nominales d'intensité et de tension de cette cellule sont&nbsp;:

- [x] les coordonnées du point B
- [ ] les coordonnées du point A
- [ ] $\pu{8,08 V}$ et $\pu{1,05 A}$

##

![](/caractpuiss.png)<br><br>
La puissance électrique maximale que peut fournir le panneau est&nbsp;:

- [ ] $\pu{8,5 W}$
- [x] $\pu{7,0 W}$
- [ ] $\pu{8,0 W}$
- [ ] $\pu{9,4 W}$


##

Le panneau alimente un conducteur ohmique de résistance $R = \pu{40 \Omega}$ dont on a superposé la caractéristique&nbsp;:<br>
![](/caractres.png)<br><br>
Le point de fonctionnement du circuit est&nbsp;:

- [x] le point C
- [ ] le point A
- [ ] le point B


##

![](/caractres.png)<br><br>
La puissance que la cellule délivre au dipôle ohmique est&nbsp;:

- [x] $\pu{1,6 W}$
- [ ] $\pu{9,8 W}$
- [ ] $\pu{7,0 W}$



##

![](/caractpuiss.png)<br><br>
Que vaut la résistance qui permettrait à la cellule de délivrer une puissance maximale&nbsp;:

- [ ] $\pu{0,14 \Omega}$
- [x] $\pu{7,0 \Omega}$
- [ ] $\pu{40 \Omega}$


{{< /quizdown >}}