---
title: "Lentilles"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
hidden: true
---


<style>
 	#correc
  {
    color: #006C65;
    border-left: solid 10px #C7DDDC;
  }
 	#comm
  {
    color: #004D80;
    border-left: solid 10px #B3CAD9;
  }
 	#commsum
  {
    color: #004D80;
  }
 	#correcsum
  {
    color: #006C65;
  }

details > summary:first-of-type {
  display: list-item;    
  cursor: pointer;       
}

details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
</style>




# Lentilles minces : démos


<img src="/schemlent.png">


1. En utilisant le schéma ci-dessus, démontrer la <b>relation de conjugaison de Newton</b> pour les lentilles minces qui stipule que&nbsp;:
$$
\overline{A'F'}\cdot\overline{AF} = \overline{OF'}\cdot\overline{OF}
$$

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
Thalès dans les traingles F'OC et F'A'B'&nbsp;:
$$\frac{\overline{OF'}}{\overline{OC}}=\frac{\overline{A'F'}}{\overline{A'B'}}$$
Et comme $\overline{OC}=\overline{AB}$, on a&nbsp;:
$$
\begin{equation}
\frac{\overline{A'B'}}{\overline{AB}}=\frac{\overline{A'F'}}{\overline{OF'}}
\end{equation}
$$
Thalès dans FAB et FOD&nbsp;:
$$\frac{\overline{OF}}{\overline{OD}}=\frac{\overline{AF}}{\overline{AB}}$$
Et comme $\overline{OD}=\overline{A'B'}$, on a&nbsp;:
$$
\begin{equation}
\frac{\overline{A'B'}}{\overline{AB}}=\frac{\overline{OF}}{\overline{AF}}
\end{equation}$$
En combinant (1) et (2), on obtient&nbsp;:
$$
\begin{equation}
\overline{A'F'}\cdot\overline{AF} = \overline{OF'}\cdot\overline{OF}
\end{equation}
$$
</blockquote>
</details>


2. En introduisant le point $O$ pour décomposer les distances algébriques $\overline{AF}$ et $\overline{A'F'}$, partir de la relation de conjugaison de Newton pour obtenir celle de Descartes.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">
On écrit que $\overline{A'F'}=-\overline{OA'}+\overline{OF'}$ et que $\overline{AF}=-\overline{OA}+\overline{OF}$ et on utilise le fait que $\overline{OF}=-\overline{OF'}$.<br>
En injectant tout ça dans (3), on obtient&nbsp;:
$$
(-\overline{OA'}+\overline{OF'})(-\overline{OA}-\overline{OF'})=-(\overline{OF'})^2
$$
On développe&nbsp;:
$$
\overline{OA'}\cdot\overline{OA}+\overline{OA'}\cdot\overline{OF'}-\overline{OF'}\cdot\overline{OA}\color{red}-{(\overline{OF'})^2}\color{black}=\color{red}{-(\overline{OF'})^2}
$$
Les termes en rouge se simplifient et il ne nours reste plus qu'à diviser par le produit $\overline{OA}\cdot\overline{OA'}\cdot\overline{OF'}$ l'expression obtenue (aucune des trois distances ne doit donc être nulle)&nbsp;:
$$
\frac{1}{\overline{OF'}}+\frac{1}{\overline{OA}}-\frac{1}{\overline{OA'}}=0
$$
Et en réarrangenat, on obtient bien la relation de conjugaison de Descartes&nbsp;:
<div style="display: flex;justify-content: center;">
<div style = "border:solid red 3px;width:min-content;padding: 0px 10px 0px 10px;font-size: 18px;">
$$
\frac{1}{\overline{OA'}}-\frac{1}{\overline{OA}}=\frac{1}{\overline{OF'}}
$$
    </div></div>
</blockquote>
</details>


3. Quelle est la distance minimale entre un objet et son image&nbsp;? Si la distance entre l'objet et l'écran est plus grande, combien de positions de la lentille permettent-elles d'avoir une image nette sur l'écran&nbsp;? Les déterminer.


<div class="imp" style="display: flex; justify-content: center;">
<iframe scrolling="no" title="Objet et écran fixes" src="https://www.geogebra.org/material/iframe/id/vtRY99as/width/1117/height/875/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl/false" style="border:0px; max-width:100%; width:1117px; aspect-ratio:1117/875;"> </iframe>
</div>

