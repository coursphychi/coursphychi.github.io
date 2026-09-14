---
title: "Puissance électrique"
date: 2021-03-06T14:23:56+01:00
weight : 8
draft: false
---

<style>
details summary { 
	cursor:pointer;
	color: #006C65;
}

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

# Puissance en régime sinusoïdal


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tsti/puisselec"> Cours </a></p>

<br>

## Rappels

<details>
<summary>En régime alternatif, que mesurent le voltmètre et l'ampèremètre en mode continu (DC ou ⎓)&nbsp;?</summary>
<blockquote>
La tension et l'intensité <span style="font-weight:bold">moyenne</span>.
</blockquote>
</details>

<br>

<details>
<summary>Et en mode alternatif (AC ou ∿), que mesurent-ils&nbsp;?</summary>
<blockquote>
La tension et l'intensité <span style="font-weight:bold">efficace</span>.
</blockquote>
</details>

<br>

<details>
<summary>Comment obtient-on $U_{eff}$ à partir de $U_{max}$ en <span style="font-weight:bold">régime sinusoïdal</span>&nbsp;?</summary>
<blockquote>
<div style="display: flex;justify-content: left;">
<div style = "border:solid red 2px;width:min-content;padding: 0px 10px 0px 10px;">
$$U_{eff}=\frac{U_{max}}{\sqrt{2}}$$
</div></div>
</blockquote>
</details>

<br>

## Savoir et savoir faire

{{%notice coeur%}}
<input type="checkbox"> Savoir définir la **puissance apparente** $S$.
<br><br>
<input type="checkbox"> Savoir que la **puissance apparente** est une **grandeur de dimensionnement** d'une installation ou d'un équipement électrique.
<br><br>
<input type="checkbox"> Savoir définir la **puissance active** $P$.
<br><br>
<input type="checkbox"> Calculer le **facteur de puissance** $k=P/S$ d'un récepteur en régime sinusoïdal.
{{%/notice%}}

<br>

## TP

- [**TP facteur de puissance**](/tpfactpuiss.pdf)<br>

Comment calculer numériquement la valeur de la puissance active d’un système à partir des évolutions temporelles de la tension et de l’intensité du courant&nbsp;?<br>
[**Lien vers l'exercice sur Colab**](https://colab.research.google.com/drive/1dnu9TQhB5rtaSxEl4LWKIe76ZJp0BzTU?usp=sharing) (il faut vous connecter à un compte Google pour pouvoir exécuter le code).



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

La relation qui permet de calculer la puissance active consommée par un dipôle est&nbsp;:

- [x] $P = kUI$
- [ ] $P = UI$
- [ ] $P = UI/k$

##

La relation qui permet de calculer la puissance apparente consommée par un dipôle est&nbsp;:

- [ ] $S = kUI$
- [x] $S = UI$
- [ ] $S = UI/k$

##

La relation qui permet de calculer le facteur de puissance est&nbsp;:

- [x] $k = P/S$
- [ ] $k = S/P$
- [ ] $k = PS$

##

Dans les relations donnant la puissance active $P$ et la puissance efficace $S$, les valeurs de la tension et de l'intensité sont&nbsp;:

- [x] les valeurs efficaces
- [ ] les valeurs moyennes
- [ ] les valeurs maximales



##

Une résistance soumise à une tension efficace de $\pu{45 V}$ et parcourue par une intensité efficace de $\pu{8,3 A}$ dissipe une puissance de&nbsp;:


- [x] $\pu{3,7E2 W}$
- [ ] $\pu{5,4 W}$
- [ ] $\pu{0,18 W}$



##

Un dipôle purement capacitif ou inductif&nbsp;:


- [ ] consomme de la puissance active
- [ ] ne fonctionne pas en régime sinusoïdal
- [x] ne consomme pas de puissance active


##

Pour un dipôle, on a&nbsp;:<br>
tension aux bornes (en V) : $u(t)=110\sqrt{2}\cos(314t)$<br>
intensité du courant (en A) : $i(t)=8\sqrt{2}\cos(314t-1,25)$<br>

- [x] la tension efficace aux bornes de ce dipôle vaut 110 V
- [ ] la tension efficace aux bornes de ce dipôle vaut 156 V
- [ ] la tension efficace aux bornes de ce dipôle vaut 8 V


##

Pour un dipôle, on a&nbsp;:<br>
tension aux bornes (en V) : $u(t)=110\sqrt{2}\cos(314t)$<br>
intensité du courant (en A) : $i(t)=8\sqrt{2}\cos(314t-1,25)$<br>
<br>
Pour ce dipôle, l'intensité efficace vaut&nbsp;:

- [x] 8 A
- [ ] 11 A
- [ ] 110 A

##

Que vaut la puissance efficace&nbsp;:

- [ ] $S = \pu{1760 VA}$
- [x] $S = \pu{880 VA}$
- [ ] $S = \pu{440 VA}$

##

On a représenté ci-dessous la puissance instantanée $p(t)$&nbsp;:
![](/puissactivequiz.png)
La puissance active consommée par le dipôle vaut&nbsp;:

- [x] $P = \pu{0,28 kW}$
- [ ] $P = \pu{1,16 kW}$
- [ ] $P = \pu{400 W}$


##

Le facteur de puissance vaut alors&nbsp;:

- [x] $k = 0,32$
- [ ] $k = 3,1$
- [ ] $k = 0,64$


##

Un dipôle qui absorbe une puissance active de $\pu{2,3 kW}$ et une puissance apparente de $\pu{3,5 kVA}$ a un facteur de puissance égal à&nbsp;:

- [ ] 1,5
- [x] 0,66
- [ ] 0,34


##

Pour mesurer une puissance active, on utilise&nbsp;:

- [ ] un voltmètre et un ampèremètre
- [x] un wattmètre
- [ ] un ohmmètre

##

Pour mesurer une puissance apparente, on utilise&nbsp;:

- [x] un voltmètre et un ampèremètre
- [ ] un wattmètre
- [ ] un ohmmètre

{{< /quizdown >}}