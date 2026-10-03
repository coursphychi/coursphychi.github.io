---
title: "Entraînement maths"
date: 2021-03-06T14:23:56+01:00
weight : 14
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

/* Propriétés générales */
.btn {
  --c1: #E55D87;   /* couleurs par défaut si on oublie btn1/2/3 */
  --c2: #5FC3E4;

  display: block !important;
  width: fit-content !important;     /* largeur = contenu + padding */
  margin: 10px auto !important;      /* auto à gauche et à droite → centré */
  padding: 15px 45px !important;
  text-align: center !important;
  text-transform: uppercase !important;
  text-decoration: none !important;
  color: #fff !important;

  background-image: linear-gradient(to right, var(--c1) 0%, var(--c2) 51%, var(--c1) 100%) !important;
  background-size: 200% auto !important;
  background-position: left center !important;
  background-repeat: no-repeat !important;

  border: none !important;
  border-radius: 10px !important;
  box-shadow: 0 0 20px #aaa !important;
  cursor: pointer !important;
  transition: background-position 0.5s, box-shadow 0.15s, transform 0.15s !important;
}

.btn:visited,
.btn:hover {
  color: #fff !important;
  text-decoration: none !important;
}

.btn:hover {
  background-position: right center !important;
}

.btn:active {
  box-shadow: 0 0 6px #666 !important;
  transform: translateY(2px) !important;
}

.btn:focus-visible {
  outline: 3px solid var(--c2) !important;
  outline-offset: 3px !important;
}

/* Couleurs uniquement */
.btn1 { --c1: #E55D87; --c2: #5FC3E4; }  
.btn2 { --c1: #1A2980; --c2: #26D0CE; }
.btn3 { --c1: #fe8c00; --c2: #f83600; } 
</style>

<h1 style="overflow-x:auto;">Automatismes</h1>

Les quiz ci-dessous visent à vérifier ou installer certains automatismes très utiles (voire indispensable) en physique-chimie.

## Jouer avec les relations

<!--<div style="position:relative;margin-left:auto;margin-right:auto;width:100%;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/bandeaurel.png" style="box-shadow:none;background:none;border-radius:3px;">
</div>-->

Les lois consistent en des formules littérales mettant en jeu plusieurs grandeurs (comme $F=G\frac{m_a\times m_B}{d^2}$) et souvent, on se retrouve à vouloir isoler l'une de ces grandeurs ($m_A$ par exemple). Il est donc vital de s'aguerrir dans cet exercice et le quiz suivant permet de tester votre agilité.

Le premier quiz utilise de simples lettres pour que l'on puisse se concentrer sur les manipulations algébriques&nbsp;:

<br>

<a class="btn btn1" href="/quiz-relations.html">Quiz avec lettres simples</a>

<br>

La cible idéale à atteindre est un score de 10/10 en environ une minute.

<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1.5em;">
<img src="/gifyoda.gif" style="box-shadow:none;background:none;border-radius:10px;">
</div>

Lorsqu'on commence à s'aguerrir, on peut passer à ce quiz de même complexité algébrique mais qui utilise cette fois de vraies relations de physique-chimie (ce qui peut rendre les notations beaucoup plus lourdes).

<br>

<a class="btn btn2" href="/quiz-relations.html?mode=physique">Quiz avec des vraies relations</a>




## Calculs numériques et écriture d'un résultat

<!--<div style="position:relative;margin-left:auto;margin-right:auto;width:100%;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/bandeaunum.png" style="box-shadow:none;background:none;border-radius:3px;">
</div>-->

Une fois qu'on a déterminé la bonne formule littérale pour la grandeur cherchée, on calcule (on dit qu'on fait l'application numérique). 

Plusieurs difficultés se dressent alors&nbsp;: 
<ul style="margin-top:-0.5em; margin-bottom:1em;">
<li>les grandeurs doivent être converties pour que les unités «&nbsp;se parlent&nbsp;»,</li>
<li>la précision des mesures doit être retranscrites dans le nombre de chiffres significatifs,</li>
<li>et pour que le résultat soit le plus lisible possible, on utilise la notation scientifique.</li>
</ul>  

Le quiz ci-dessous permet de s'auto-diagnostiquer et de s'entraîner pour améliorer sa maîtrise. Le test se concentre sur&nbsp;: 
<ul style="margin-top:-0.5em; margin-bottom:1em;">
<li>les puissances de 10 et les ordres de grandeur,</li>
<li>les conversions,</li>
<li>et la notation scientifique</li>
</ul>

{{%notice type="tip"  title="Ordre de grandeur en physique" round="true"%}}
En physique, l'ordre de grandeur d'un nombre est la puissance de 10 la plus proche de ce nombre.

Exemples&nbsp;:
<ul style="margin-top:-0.5em; margin-bottom:0em;">
<li>l'ordre de grandeur de 499 est 10<sup>2</sup></li>
<li>l'ordre de grandeur de 500 est 10<sup>3</sup></li>
<li>l'ordre de grandeur de 0,0087 est 10<sup>-2</sup></li>
</ul>
{{%/notice%}}

<br>

<a class="btn btn3" href="/quiz-automatismes.html">Diagnostic + entraînement</a>

<br>

{{%notice type="note" title="Vidéos sur la notation scientifique, les ordres de grandeur et les chiffres significatifs" collapse="true" round="true"%}}

{{< youtube-plus id="bBT1hOYQPnY" ratio="4x3" width="100%" shadow=true rounded=true >}}

{{< youtube-plus id="PtftD6sU-Sc" ratio="16x9" width="100%" shadow=true rounded=true >}}

{{< youtube-plus id="KOvHirpl7vk" ratio="16x9" width="100%" shadow=true rounded=true >}}
{{%/notice%}}

