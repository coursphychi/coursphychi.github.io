---
title: "Équilibre chimique"
date: 2021-03-06T14:23:56+01:00
weight : 6
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

# Évolution spontanée d'un système chimique


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tspe/equilibre"> Cours </a></p>

<div style="position: relative; max-width: 100%; margin-left: auto;margin-right: auto;border-radius: 50px;">
<a href="/cm-equilibrechim.pdf"><img src="/cm-equilibrechim.png" style="border-radius: 50px;"></a>
</div>


## Documents 

<div style="overflow-x: auto;">
<table>
      <tr>
  <th rowspan="1">TP</th>
  <td><a href="/tp-quotienreaction.pdf"><b>Equilibre chimique</b></a> + <a href="/tp-equilibre.xlsx" target="_blank"><b style="color:#00AB8E"><i class="fa-solid fa-computer"></i></b></a> + <a href="/corrtpequ.pdf"><b style="color:#FF644E;"><i class="fa-solid fa-pen-nib"></i></b></a></td>
  </tr>
  <tr>
<th rowspan="1">Activité</th>
  <td><a href="/act-pluiedor.pdf"><b>Pluie dorée</b></a></td>
</tr>
  <tr>
<th rowspan="1">Exercice</th>
  <td><a href="/act-salicylate.pdf"><b>Ion salicylate</b><br>(dissolution, dilution, avancement, équilibre, dosage par étalonnage spectrophotométrique)</a></td>
  </tr>
</table>
</div>

<br>

## Définitions

{{%notice definition "Avancement maximal"%}}
Avancement associé à la <b style="color:#B51700;">disparition totale du réactif limitant</b>.
{{%/notice%}}

{{%notice definition "Taux d'avancement"%}}
Rapport de la valeur finale de l’avancement sur celle de l’avancement maximal&nbsp;:<br>
<b style="color:#B51700;">$$\tau=\frac{x_\mathrm{final}}{x_\mathrm{max}}$$</b>
{{%/notice%}}

{{%notice definition "Transformation totale ou non totale"%}}
Une transformation est dite <b style="color:#B51700;">totale</b> si le taux d’avancement final est égal à 1 (<b style="color:#B51700;">$\tau=1$</b>).<br>
À l’état final d’une transformation totale, au moins une des espèces chimiques présentes à l’état initial a disparu.<br><br>
S’il est inférieur à 1 (<b style="color:#B51700;">$\tau<1\Leftrightarrow x_\mathrm{final}<x_\mathrm{max}$</b>), la transformation est dite <b style="color:#B51700;">non-totale</b>.<br><br>
{{%/notice%}}

{{%notice note%}}
 Un soluté ou un gaz ne disparaissent jamais totalement d’un milieu. Ainsi, toute transformation consommant exclusivement des solutés et/ou gaz ne peut être totale. Dans certains cas, le taux d’avancement final est si proche de 1 que la transformation peut être qualifiée de quasi-totale. Une transformation chimique n’est rigoureusement totale que si une phase condensée pure (liquide pur ou solide pur) a disparu.
{{%/notice%}}

{{%notice definition "Quotient de réaction"%}}
Grandeur adimensionnée définie par la relation ci-dessous dans laquelle interviennent les activités des espèces chimiques réactives et produites apparaissant dans l’équation de la réaction et les nombres stœchiométriques qui leur sont associés, considérés ici positifs&nbsp;:
<b style="color:#B51700;">$$\displaystyle Q_r=\frac{\prod_i\left(a_{\text {produits } i}\right)^{\nu_i}}{\prod_j\left(a_{\text {réactifs } j}\right)^{\nu_j}}$$</b>
{{%/notice%}}

{{%notice info%}}
 <i class="fa fa-arrow-right"></i> L’activité d’un solvant est prise égale à 1,<br>
 <i class="fa fa-arrow-right"></i> celle d’une espèce soluté est le rapport $C_i/C°$ de sa concentration $C_i$ en quantité de matière sur la concentration standard,<br>
 <i class="fa fa-arrow-right"></i> celle d’un solide est prise égale à 1.
{{%/notice%}}

<div class="notices definition" style="--title: 'Équilibre chimique';">
  <p>
    Un système est à l’équilibre chimique s’il vérifie, à l’état final, les conditions suivantes :<br>
  <i class="fa fa-arrow-right"></i> l’ensemble des <b style="color:#B51700;">réactifs</b> et <b style="color:#B51700;">produits</b> de la réaction <b style="color:#B51700;">coexistent</b> et leurs quantités de matière <b style="color:#B51700;">n’évoluent plus</b> dans le temps</b>&nbsp;;<br>
  <i class="fa fa-arrow-right"></i> le quotient de réaction <b style="color:#B51700;">\( Q_r \)</b> prend une valeur notée <b style="color:#B51700;">\( K(T) \)</b>, indépendante de la composition initiale, appelée <b style="color:#B51700;">constante d’équilibre</b>.<br>
  </p>
</div>

{{%notice info%}}
  Pour une réaction donnée, la valeur de $K(T)$ ne dépend que de la température. Elle est par conséquent indépendante de la pression et des quantités de matière mises en œuvre.
{{%/notice%}}

{{%notice note%}}
 L’équilibre chimique est modélisé par deux réactions opposées dont les effets se compensent une fois l’équilibre chimique atteint.
{{%/notice%}}

{{%notice definition "Sens d’évolution spontanée d’un système chimique"%}}
En l’absence de générateur, le <b style="color:#B51700;">sens d’évolution spontanée</b> est celui qui modifie la valeur du quotient de réaction pour le rapprocher de la constante d’équilibre (<b style="color:#B51700;">$Qr\rightarrow K(T)$</b>).<br><br>
L’état d’<b style="color:#B51700;">équilibre final du système</b> résulte de l’une des deux situations suivantes&nbsp;:<br>
 <i class="fa fa-arrow-right"></i> l’état final est un état d’équilibre chimique caractérisé par la relation <b style="color:#B51700;">$Q_{r\,\mathrm{eq}}=K(T)$</b>, la transformation n’est <b style="color:#B51700;">pas totale</b>&nbsp;;<br>
 <i class="fa fa-arrow-right"></i> la <b style="color:#B51700;">disparition d’un réactif</b> (solide ou liquide pur) intervient avant que la valeur du quotient de réaction n’atteigne $K(T)$, la transformation est <b style="color:#B51700;">totale</b>.
{{%/notice%}}

{{%notice info%}}
En présence d’un générateur (système siège d’une électrolyse), le sens d’évolution du système peut être contrôlé par l’expérimentateur&nbsp;:<br>
le générateur impose le sens de circulation des électrons dans le circuit extérieur, et par conséquent, le sens des transferts électroniques aux électrodes.
{{%/notice%}}

