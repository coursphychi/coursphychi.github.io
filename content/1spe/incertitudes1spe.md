---
title: "Incertitudes"
date: 2021-03-06T14:23:56+01:00
weight : 19
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

# Incertitudes

---

## Les chiffres significatifs


{{<youtube KOvHirpl7vk>}}

<br>

<div style="border:solid 5px #FFBBBB;border-radius:10px;background-color:#FADEDE;padding:0.1em 0.5em 0.1em 0.5em;">
<ul>
<li>Si multiplications et/ou divisions de mesures&nbsp;:<br>
le résultat ne doit pas avoir plus de chiffres significatifs que la mesure qui en possède le moins.<br>
ex&nbsp;: $\frac{5,23\times2,728}{0,032}=\pu{4,5E2}$
</li>
<br>
<li>Si addition et/ou soustractions de mesures&nbsp;:<br>
le résultat ne doit pas avoir plus de décimales que la mesure qui en comporte le moins.<br>
ex&nbsp;: $5,23 +2,7 - 0,03 = 7,9$
</li>
</ul>

</div>

---


## Le cours sur les incertitudes

<div style="overflow-x: auto;border:solid 0px #FFBBBB;border-radius:10px;">
<table>
<tr>
<th style="background-color:#599DFF;">{{<youtube R6ogbpcuyH8>}}</th>
</tr>
</table>
</div>


---

<p style="text-align:center">
<a href="https://presentationssite.github.io/1spe/calculette/#/" style="font-weight:bold;">Tutoriels calculette</a><br>sur l'utilisation de la partie tableur afin de calculer la moyenne d'une série de valeurs et son écart-type expérimental $\sigma_{exp}$.
</p>

---

<div style="overflow-x: auto;">
<table>
<tr>
<th rowspan="1">Activités</th>
<td><a href="/ecritureresultat.pdf"><b>Écriture d'un résultat</b></a>  +  <a href="/ecritureresultatcorr.pdf"><b style="color:#FF644E;"><i class="fa-solid fa-pen-nib"></i></b></a> </td>
</tr>
<tr>
<th rowspan="1">TP</th>
<td><a href="/tp-tpsreac.pdf" target="_blank"><b>Temps de réaction</b></a></td>
</tr>
</table>
</div>


---

## Pour aller plus loin



{{%notice tip%}}

La vidéo suivante explique l'intérêt de répéter les mesures.

{{%/notice%}}

{{<youtube g5kIh7sjPwQ>}}


{{%notice tip%}}

La vidéo suivante permet d'en savoir plus sur le lien entre incertitude-type et niveau de confiance&nbsp;: quelle est la probabilité que la valeur de référence soit dans l'intervalle $[x-\mathrm{u},x+\mathrm{u}]$&nbsp;?

{{%/notice%}}

{{<youtube k1y9h7c3yDo>}}


{{%notice tip%}}

La vidéo suivante permet d'en savoir plus sur la formule de l'écart-type expérimental (en particulier l'étrange présence du $n-1$).

{{%/notice%}}


{{<youtube bEDXykqj6o4>}}

{{%notice tip%}}

Pourquoi faut-il diviser la demi-étendue par $\sqrt{3}$ pour obtenir l'incertitude-type lors d'une évaluation de type B&nbsp;?&nbsp;

{{%/notice%}}

<details>
<summary id="correcsum">
Démonstration mathématique&nbsp;:
</summary>
<blockquote id="correc">
On modélise notre mesure par une variable aléatoire continue $X$ répartie uniformément sur $[\mu -a,\mu + a]$ où $\mu = E(X)$ est la valeur centrale (la valeur lue sur l'appareil).<br>
<br>
Il faut définir sa fonction de densité de probabilité $f(x)$.<br>
<ul style="margin-top:0.5em;margin-bottom:0.5em;">
<li>Puisque la probabilité est uniforme, $f(x)$ est une constante sur l'intervalle $[-a, a]$  et vaut $0$ en dehors.</li>
<li>La somme de toutes les probabilités doit valoir $1$. <br>Graphiquement, l'aire sous la courbe (un rectangle de largeur $2a$ et de hauteur constante) doit être égale à $1$.</li>
</ul>
Si la largeur est $2a$, alors la hauteur (la constante) doit être $\frac{1}{2a}$ pour que l'aire soit $2a \times \frac{1}{2a} = 1$.<br>
<br>
On a donc notre fonction de densité&nbsp;:
$$f(x) = \frac{1}{2a} \quad \text{pour } x \in [-a, a]$$ 
$$f(x) = 0 \quad \text{ailleurs}$$
L'incertitude-type $u(x)$ que l'on cherche correspond mathématiquement à l'écart-type $\sigma$ de cette distribution.<br>
Et l'écart-type est la racine carrée de la variance $V(X)$.<br>
On repart de la définition générale de la variance&nbsp;:<br>
$$V(X) = \int_{-\infty}^{+\infty} (x - E(X))^2 f(x) dx$$
Ce qui donne ici&nbsp;:<br>
$$
\begin{aligned}
V(X) &= \int_{\mu - a}^{\mu + a} (x - \mu)^2 \left(\frac{1}{2a}\right) dx\\\\
&=\frac{1}{2a} \int_{\mu - a}^{\mu + a} (x - \mu)^2 dx
\end{aligned}
$$
Or, la primitive de $u'u^n$ est $\frac{u^{n+1}}{n+1}$.<br>
Ici, en posant $u(x) = x - \mu$, on a $u'(x) = 1$. L'expression sous l'intégrale est donc exactement de la forme $u'u^2$.<br>
La primitive de $(x - \mu)^2$ est donc $\frac{(x - \mu)^3}{3}$.<br>
<br>
On évalue&nbsp;:<br>
$$
\begin{aligned}
V(X) &= \frac{1}{2a} \left[ \frac{(x - \mu)^3}{3} \right]_{\mu - a}^{\mu + a}\\\\
&= \frac{1}{2a} \left( \frac{((\mu + a) - \mu)^3}{3} - \frac{((\mu - a) - \mu)^3}{3} \right)\\\\
&= \frac{1}{2a} \left( \frac{a^3}{3} - \frac{(-a)^3}{3} \right)\\\\
&= \frac{a^2}{3}
\end{aligned}
$$
D'où&nbsp;:<br>
$$u = \sqrt{V(X)} = \frac{a}{\sqrt{3}}$$

</blockquote>
</details>