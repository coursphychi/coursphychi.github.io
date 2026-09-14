---
title: "Acide/Base"
date: 2021-03-06T14:23:56+01:00
weight : 2
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

# Réactions chimiques acido-basiques

<br>

<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tsti/acide"> Cours </a></p>

<br>

## Expérience


<details>
<summary><a>Vidéo :</a></summary>
<blockquote>
<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{<youtube NO7V6TMQuBs>}}
</div>
</blockquote>
</details>


<br>

<details>
<summary><a>Questions :</a></summary>
<blockquote>
<ol>
<li>De quoi témoigne l'élévation de la température du ballon&nbsp;?</li>
<li>D'après le tableau suivant, que pouvez-vous dire de l'évolution du pH de la solution aqueuse une fois que l'ammoniac se dissout et réagit avec l'eau&nbsp;?
<img src="https://www.pierron.fr/media/catalog/product/m/t/mt09698.jpg"></li>
<li> Par conséquent, l'ammoniac est-il une base ou un acide ?</li>
<li>Comment expliquer le jaillisement de l'eau dans la 1<sup>re</sup> expérience et la contraction du ballon dans la 2<sup>e</sup>&nbsp;?</li>
<li>Quelle est l'équation de la réaction de l'ammoniac avec l'eau&nbsp;?</li>
</ol>
</blockquote>
</details>


<br>

## Simulation

Testez la [**simulation**](https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_all.html?locale=fr) et répondez aux questions suivantes&nbsp;:

<br>

<details>
<summary><a>Questions :</a></summary>
<blockquote>
<ol>
<li>Comment évolue le pH lorsqu'on dilue la solution&nbsp;? Vers quelle valeur tend-il&nbsp;?</li><br>
<li>Comment évolue le rapport $\displaystyle\frac{\ce{[H3O+]}}{\ce{[HO-]}}$ lorsqu'on dilue la solution&nbsp;? Vers quelle valeur tend-il&nbsp;?</li><br>
<li>Que vaut le ratio $\displaystyle \frac{\ce{[H3O+]}}{\ce{[HO-]}}$ lorsque le pH vaut 4&nbsp;? Et lorsque le pH vaut 10&nbsp;?</li><br>
<li>Que vaut le produit $\ce{[H3O+]}\times \ce{[HO-]}$ lorsque le pH vaut 3&nbsp;? Lorsqu'il vaut 7&nbsp;? Et lorsqu'il vaut 12&nbsp;?<br>Que pouvez-vous déduire sur la grandeur $K_e = \ce{[H3O+]}\times \ce{[HO-]}$ appelée produit d'autoprotolyse de l'eau&nbsp;?</li><br>
<li>Déterminer $\ce{[H3O+]}$ lorsque le pH vaut 3,5 grâce à la simulation et vérifier par le calcul. En déduire $\ce{[HO-]}$ grâce à la question précédente.</li><br>
<li>Déterminer le pH lorsque $\ce{[H3O+]}=\pu{2E-9 mol*L-1}$ grâce à la simulation. Vérifier par le calcul.</li>
</ol>
</blockquote>
</details>

<br>

## Savoir et savoir faire

![](/cm-acid.png)

{{%notice coeur%}}
<input type="checkbox"> **Identifier un acide** par sa capacité à céder un ion $\ce{H+}$, **en déduire la base conjuguée**.
<br><br>
<input type="checkbox"> **Écrire l'équation de la réaction** entre un acide et une base à partir des couples acide-base.
<br><br>
<input type="checkbox"> **Calculer un pH** à partir de $\ce{[H3O+]}$ et inversement, **calculer $\ce{[H3O+]}$** à partir d'un **pH**.
<br><br>
<input type="checkbox"> Savoir comment **évolue le pH** lors d'une **dilution**.
{{%/notice%}}

{{%notice info%}}
La précision d'une mesure au pH-mètre est d'un chiffre après la virgule (0,1 unité de pH). Conséquence : on ne note jamais un pH avec plus d'un chiffre après la virgule.<br>
⚠️ La concentration en ions oxonium $\ce{[H3O+]}$ déduite d'une mesure de pH est toujours donnée avec **2 chiffres significatifs**, même lorsque la mesure de pH en comporte 3.
{{%/notice%}}

{{%notice piege%}}
Attention à bien écrire **pH**, petit **p**, grand **H**, pour "**p**otentiel **H**ydrogène".
{{%/notice%}}

{{%notice piege%}}
Une **solution** aqueuse peut-être **acide** (**pH&nbsp;<&nbsp;7**) alors qu'une base est le soluté majoritaire dans la solution et inversement.<br>
Par exemple, l'espèce majoritaire dans une solution contenant le couple $\ce{(CH3COOH/CH3COO^-)}$ est la base $\ce{CH3COO-}$ si le pH vaut 5,5&nbsp;!<br>
Mais **ajouter un acide dans la solution fera toujours ➘ le pH** alors qu'ajouter une base le fera ➚.
{{%/notice%}}

{{%notice piege%}}
$\ce{H3O^+}$ et $\ce{H^+(aq)}$ désignent la même chose&nbsp;!<br>
Pour une réaction acidobasique dans l'eau on utilise $\ce{H3O+}$, mais pour une réation d'oxydoréduction dans l'eau, on utilise plus souvent $\ce{H^+(aq)}$. Dans ce cas, on a $\text{pH}=-\log(\ce{H^+(aq)})$.
{{%/notice%}}



<br>



## Documents

- TP :<br>
[**TP chou rouge**](/TPchourouge.pdf)

- Exos :<br>
[**Retenue d'eau** (extrait sujet 0)](/acide-exo.pdf)<br>
[**Lessive** (extrait sujet 2022 métropole)](/acide-bac.pdf)<br>
[**Analyse d'un échantillon de glace** (bac blanc - sujet 2023 Mayotte-Liban)](/exoacidebacblanc.pdf)



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

Un acide est une espèce chimique capable de céder&nbsp;:

- [x] un proton 
- [ ] un neutron  
- [ ] un électron

## 

Une base est une espèce chimique capable de capter&nbsp;:

- [x] un proton
- [x] un $\ce{H+}$
- [ ] un électron

## 

Lorsqu'on ajoute une espèce acide dans une solution, le pH&nbsp;:

- [x] diminue
- [ ] augmente
- [ ] se rapproche de 7


## 

Lors d'une réaction acido-basique, l'acide d'un couple acide/base réagit avec&nbsp;:

- [x] la base d'un autre couple
- [ ] la base du même couple
- [ ] l'acide d'un autre couple


## 

Dans le couple acide/base où $\ce{NH3OH+}$ est l'acide, la base de ce même couple a pour formule chimique&nbsp;:

- [x] $\ce{NH3O}$
- [ ] $\ce{NH3O+}$
- [ ] $\ce{NH3OH-}$



## 

Dans le couple acide/base où l'ion hydroxyde $\ce{HO-}$ est la base, l'acide de ce même couple a pour formule chimique&nbsp;:

- [x] $\ce{H2O}$
- [ ] $\ce{H3O+}$
- [ ] $\ce{O^{2-}}$



## 

L'acide du couple $\ce{(SO2,H2O/HSO3^-)}$ réagit avec la base du couple $\ce{(HNO3/NO3^-)}$. L'équation de réaction s'écrit&nbsp;:<br>


- [x] $\ce{SO2,H2O + NO3^-  \longrightarrow  HSO3^- + HNO3}$
- [ ] $\ce{SO2,H2O + HNO3 \longrightarrow  HSO3^- + NO3^-}$
- [ ] $\ce{HSO3^- + HNO3 \longrightarrow  SO2,H2O + NO3^-}$



## 

L'acide du couple $\ce{(HCO3^-/CO3^2-)}$ réagit avec l'eau qui appartient aux deux couples suivant : $\ce{(H2O/HO^-)}$ et $\ce{(H3O+/H2O)}$. L'équation de réaction s'écrit&nbsp;:<br>


- [x] $\ce{HCO3^- + H2O \longrightarrow  CO3^2- + H3O+}$
- [ ] $\ce{HCO3^- + H2O \longrightarrow  CO3^2- + HO-}$
- [ ] $\ce{HCO3^- + HO- \longrightarrow  CO3^2- + H2O}$

## 

Pour mesurer le pH d'une solution aqueuse, on peut utiliser&nbsp;:

- [x] un papier pH
- [x] un indicateur coloré de pH
- [x] un pH-mètre

## 

La relation liant le pH à la concentration molaire en ions oxonium $\ce{H3O+}$ est&nbsp;:

- [x] $\text{pH} = -\log\ce{[H3O+]}$
- [ ] $\text{pH} = 10^{-\ce{[H3O+]}}$
- [ ] $\ce{[H3O+]} = -\log \text{pH}$


## 

Le pH d'une solution de concentration molaire $\ce{[H3O+]}=\pu{10^-5 mol*L-1}$ vaut&nbsp;:

- [x] $5$
- [ ] $-5$
- [ ] $\log 5$


## 

La concentration molaire $\ce{[H3O+]}$ d'une solution de $\text{pH}= 8,4$ vaut&nbsp;:

- [x] $\pu{10^{-8,4} mol*L-1}$
- [x] $\pu{4,0*10^{-9} mol*L-1}$
- [ ] $\pu{10^{8,4} mol*L-1}$


## 

Un pH-mètre affiche 10,23, nous pouvons conserver comme résultat&nbsp;:

- [x] $10,2$
- [ ] $10,23$
- [ ] $10$


## 

La concentration molaire des ions oxonium qui correspond à cet affichage de 10,23 est&nbsp;:

- [x] inférieure à celle que l'on trouve dans l'eau pure
- [ ] supérieure à celle que l'on trouve dans l'eau pure
- [ ] sensiblement égale à celle que l'on trouve dans l'eau pure


## 

La concentration molaire des ions oxonium qui correspond à cet affichage de 10,23 doit se noter&nbsp;:

- [x] $\pu{5,9E-11 mol*L-1}$
- [ ] $\pu{5,89E-11 mol*L-1}$
- [ ] $\pu{6E-11 mol*L-1}$


## 

Lorsqu'on ajoute de l'eau distillée à une solution basique&nbsp;:

- [x] le pH diminue
- [ ] le pH augmente
- [ ] le pH reste constant

## 

Lorsqu'on ajoute de l'eau distillée à une solution acide&nbsp;:

- [ ] le pH diminue
- [x] le pH augmente
- [x] le pH se rapproche de 7

## 

Pour diluer une solution de pH très faible ou très élevé, il faut&nbsp;:

- [x] verser la solution concentrée goutte à goutte dans l'eau
- [ ] verser l'eau goutte à goutte dans la solution concentrée
- [ ] verser la solution dans l'eau ou l'inverse, ça n'a pas d'importance

> Lors du mélange, il se produit une réaction chimique très exothermique (forte libération de chaleur).<br> 
> Les premières gouttes mélangées (acide dans eau ou eau dans acide) risque de faire localement monter la température au-delà de la température de vaporisation entraînant des projections.<br>
> Dans le cas d'ajout goutte à goutte de l'eau dans l'acide, on risque de principalement projeter de l'acide.<br>
> À l'inverse, dans le cas de l'ajout d'acide dans l'eau, c'est surtout de l'eau qui rique d'être projetée.

{{< /quizdown >}}