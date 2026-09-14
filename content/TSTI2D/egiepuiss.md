---
title: "Énergie/Puissance"
date: 2021-03-06T14:23:56+01:00
weight : 5
draft: false
---

# Énergie / Puissance


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tsti/egie"> Cours </a></p>

<br>

## Rappels

La <b>variation d'énergie</b> $\Delta E$ (en J) d'un système pendant $\Delta t$ (en s) est donnée par&nbsp;:
<br>
<div style="display: flex;justify-content: center;">
<div style = "border:solid red 3px;width:max-content;padding: 10px 10px 7px 10px;">
$\displaystyle \Delta E = P\times \Delta t$
</div></div>

où $P$ (en W) est la <b>puissance moyenne</b> reçue ou fournie par le système pendant $\Delta t$.

Et on obtient par conséquent la puissance moyenne $P$ délivrée ou reçue pendant $\Delta t$ grâce à&nbsp;:
<br>
<div style="display: flex;justify-content: center;">
<div style = "border:solid blue 3px;width:max-content;padding: 10px 10px 10px 10px;">
$\displaystyle P = \frac{\Delta E}{\Delta t}$
</div></div>


Conversion à connaître et à savoir redémontrer&nbsp;:
<div style="display: flex;justify-content: center;">
<div style = "border:solid green 3px;width:max-content;padding: 10px 10px 10px 10px;">
$\pu{1 kWh = 3,6 MJ}$
</div></div>

Définition du <b>rendement</b> (noté $r$ ou $\eta$)&nbsp;:<br>
Ratio de la puissance utile  $P_{utile}$  par rapport à la puissance fournie ou absorbée $P_{fournie}$.<br>
On peut aussi définir le rendement à partir des énergies (utile et fournie).

<div style="display: flex;justify-content: center;">
<div style = "border:solid #CB297B 3px;width:max-content;padding: 10px 10px 10px 10px;">
$\displaystyle \eta = \frac{P_{utile}}{P_{fournie}} = \frac{E_{utile}}{E_{fournie}}$
</div></div>


<br>

## Savoir et savoir faire


{{%notice coeur%}}
<input type="checkbox"> Déterminer une **puissance instantanée** à partir d'une courbe d'énergie.<br><br>
<input type="checkbox"> Déterminer une **énergie** à partir d'une courbe de puissance.<br><br>
<input type="checkbox"> Calculer un **rendement**.
{{%/notice%}}

<br>

## TP Python

[**Lien vers le notebook Colab**](https://colab.research.google.com/drive/1Spnaf9eOirMYTT5JxFcRUcGbLXnR0nuJ?usp=sharing) contenant les consignes et les codes à compléter (il faut se connecter à un compte google pour pouvoir exécuter le code).

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

Une ampolue à LED d'une puissance de $\pu{4,0 W}$ reste allumée pendant $\pu{12 h}$. L'énergie consommée vaut&nbsp;:

- [x] $\pu{1,7E5 J}$
- [x] $\pu{48 Wh}$  
- [ ] $\pu{48 J}$


##

L'énergie consommée par un dispositif est modélisée par la fonction $e(t)=E_M(1+\sin(\omega t))$ où $E_M$ est une constante. La puissance instantanée est alors donnée par&nbsp;:

- [x] $p(t)=E_M\omega\cos(\omega t)$
- [ ] $p(t)=E_M(1+\cos(\omega t))$  
- [ ] $p(t)=E_M\cos(\omega t)$



##

On a enregistré l'évolution de l'énergie fournie par un système électromécanique au cours du temps&nbsp;:

![](/tabenergie.png)

La valeur de la puissance moyenne sur un intervalle de 1 minute vaut&nbsp;:


- [x] $\pu{2,0 W}$
- [ ] $\pu{120 W}$
- [ ] $\pu{582 W}$



##

On a enregistré l'évolution de l'énergie fournie par un système électromécanique au cours du temps&nbsp;:

![](/tabenergie.png)

Pour l'intervalle de temps [50 s ; 60 s], la puissance est égale à&nbsp;:


- [ ] $\pu{55 W}$
- [ ] $\pu{120 W}$
- [x] $\pu{0 W}$


##

On a enregistré l'évolution de l'énergie fournie par un système électromécanique au cours du temps&nbsp;:

![](/tabenergie.png)

La puissance est maximale&nbsp;:

- [x] pour l'intervalle [0 s ; 10 s]
- [ ] pour l'intervalle [10 s ; 20 s]
- [ ] pour l'intervalle [20 s ; 30 s]


##

Une éolienne en mer absorbe une puissance moyenne de $\pu{5,0 MW}$ et fournit une puissance électrique moyenne de $\pu{2,0 MW}$. Son rendement vaut&nbsp;:

- [x] 40%
- [x] 0,40
- [ ] 2,5%

##

Pour une vitesse du vent de $\pu{10 m*s-1}$, une éolienne domestique a un rendement de 34%.<br>
Si la puissance absorbée vaut $\pu{5,0 kW}$, la puissance utile est égale à&nbsp;:

- [ ] $\pu{150 kW}$
- [x] $\pu{1,7 kW}$
- [ ] $\pu{0,15 kW}$


{{< /quizdown >}}

