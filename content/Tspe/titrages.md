---
title: "Titrages"
date: 2021-03-06T14:23:56+01:00
weight : 3
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

# Analyser un système chimique par des méthodes chimiques

<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tspe/titrages">Cours</a></p>

<div style="position: relative; max-width: 100%; margin-left: auto;margin-right: auto;border-radius: 50px;">
<a href="/cm-tstitrages.pdf"><img src="/cm-tstitrages.png" style="border-radius: px;"></a>
</div>


## Documents et autres

<div style="overflow-x: auto;">
<table>
      <tr>
  <th rowspan="2">TP</th>
  <td style="border-bottom:none;"><a href="/tp-titrageph.pdf"><b>Titrage pH-métrique</b></a></td>
  <tr>
  <td style="border-top:none;"><a href="/tp-titrageconduct.pdf"><b>Titrage conductimétrique</b></a>&nbsp;+&nbsp;<a href="https://colab.research.google.com/drive/1xJbK97GnqoUhC7m5SpJc8cy_cQk1T7g1#scrollTo=cqhDB-OuvYN-&uniqifier=1" target="_blank" style="color:#00AB8E"><b><i class="fa-solid fa-computer"></i></b> (Monte-Carlo)</a></td>
  </tr>
  <tr>
<th rowspan="4 ">Exercices</th>
  <td style="border-bottom:none;"><a href="/act-titragets1.pdf"><b>Titrage conductimétrique et agneaux</b></a>&nbsp;+&nbsp;<a href="https://colab.research.google.com/drive/1xJbK97GnqoUhC7m5SpJc8cy_cQk1T7g1#scrollTo=cqhDB-OuvYN-&uniqifier=1" target="_blank"><b style="color:#00AB8E"><i class="fa-solid fa-computer"></i></b></a>  +  <a href="/correcagneau.pdf"><b style="color:#FF644E;"><i class="fa-solid fa-pen-nib"></i></b></a></td>
  <tr>
  <td style="border-top:none;border-bottom:none;"><a href="/act-titragets2.pdf"><b>Eau de Javel et acide</b> (partie B)</td>
  </tr>
  <tr>
  <td style="border-top:none;border-bottom:none;"><a href="/act-titragets3.pdf"><b>Acide polylactique</b> (jusqu'à B.1.)</a>  +  <a href="/correcpla.pdf"><b style="color:#FF644E;"><i class="fa-solid fa-pen-nib"></i></b></a></td>
  </tr>
    <tr>
  <td style="border-top:none;"><a href="/act-chaufferettes.pdf"><b>Chaufferette</b></a>&nbsp;+&nbsp;<a href="/correcchaufferettes.pdf"><b style="color:#FF644E;"><i class="fa-solid fa-pen-nib"></i></b></a></td>
  </tr>
  <tr>
  <th rowspan="1">Simulation</th>
  <td> <a href="https://www.hatier-clic.fr/miniliens/mie/2020/9782401061798/Simulateur_titrage_accueil/index.html"><b>Différents titrages simulés</b></a></td>
    </tr>
 <tr>
  <th rowspan="1">Révisions 1<sup>re</sup></th>
  <td> <a href="../../1spe/titrage"><b>Titrage par oxydoréduction avec suivi colorimétrique</b></a></td>
</tr>
<!--
<tr>
  <th rowspan="1 ">DS</th>
  <td><a href="/ds-titrage.pdf"><b>Chaufferette</b></a></td>
  </tr>
  -->
</table>
</div>

{{%notice tip%}}
Il faut tout connaître sur le bout des doigts (schémas de montages, méthodes de détermination de l'équivalence, rédaction de la détermination d'une concentration à l'équivalence, etc.). Tombe tout le temps au bac.<br>
En particulier, savoir écrire&nbsp;:<br>
&laquo;&nbsp;<b>À l'équivalence, le mélange est stœchiométrique</b>.<br>
On a donc&nbsp;:<br>
$\frac{n_A}{a}=\frac{n_B}{b}$<br>
$\frac{C_AV_A}{a}=\frac{C_BV_B}{b}$<br>
$\cdots$&nbsp;&raquo;
{{%/notice%}}


## Définitions

{{%notice definition "Dosage par titrage"%}}
Méthode destructive de détermination d’une quantité de matière utilisant une transformation chimique totale, en pratique, quasi-totale. La mise en œuvre de la technique nécessite l’introduction d’incréments de quantité de matière d’un réactif titrant à une solution contenant l’espèce à titrer. Le titrage est qualifié d’«&nbsp;acido-basique&nbsp;», «&nbsp;par oxydoréduction » ou «&nbsp;par précipitation&nbsp;» selon la nature de la réaction support.
{{%/notice%}}


{{%notice definition "Équivalence"%}}
Moment du titrage associé à la disparition quasi-totale de l’espèce à titrer. Cette situation correspond au moment où la quantité introduite de l’espèce titrante et celle de l’espèce titrée initiale sont dans les proportions stœchiométriques de la réaction support du titrage.<br>
La détection de l’équivalence nécessite une technique adaptée, comme la colorimétrie, la pH-métrie ou encore la conductimétrie.
{{%/notice%}}

## Quiz

{{< quizdown >}}

---
primary_color: steelblue
secondary_color: "#f2f2f2"
text_color: black
shuffle_questions: false
shuffle_answers: true

---

## Burette

On utilise toujours une burette graduée

- [x] dans un dosage par titrage
- [ ] dans un dosage par étalonnage


## Méthode destructive

L'espèce à doser est détruite

- [x] dans un dosage par titrage
- [ ] dans un dosage par étalonnage


## Réaction support

On utilise la stœchiométrie d'une réaction

- [x] dans un dosage par titrage
- [ ] dans un dosage par étalonnage


## Conductimétrie

On peut utiliser la conductimétrie

- [x] dans un dosage par titrage
- [x] dans un dosage par étalonnage

## Ajout d'eau

L'ajout d'eau distillée dans la solution à doser modifie le résultat

- [ ] dans un dosage par titrage
- [x] dans un dosage par étalonnage

## Quel titrage ?

![](/quiztitrage.png)

<br>S'agit-il du titrage

- [ ] d'un acide par un acide&nbsp;?
- [x] d'une base par un acide&nbsp;?
- [ ] d'une base par une base&nbsp;?
- [ ] d'un acide par une base&nbsp;?

{{< /quizdown >}}


