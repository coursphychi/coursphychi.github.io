---
title: "Lewis"
date: 2021-03-06T14:23:56+01:00
weight : 5
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
/* 1. Rétablir la déclaration que votre reset a écrasée */
details > summary:first-of-type {
  display: list-item;     /* remet le triangle + l’accessibilité */
  cursor: pointer;        /* optionnel : feedback visuel */
}

/* 2. Si vous aviez aussi supprimé le list-style */
details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
</style>

# De la structure à la polarité d'une entité


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/1spe/lewis"> Cours </a></p>


<div style="position: relative; max-width: 100%; margin-left: auto;margin-right: auto;">
<a href="/cm-lewis1spe.pdf"><img src="/cm-lewis1spe.png""></a>
</div>


{{%notice definition "Schéma de Lewis d’une entité chimique"%}}
Modèle de représentation de la structure électronique de valence d’entités au moyen de lettres (symbole des éléments chimiques), traits (doublets liants et doublets non liants), lacunes électroniques et charges formelles.<br><br>
<b>Charge formelle</b><br>
Charge portée par un atome après partage équitable de chaque doublet liant, la charge formelle étant obtenue par comparaison entre le nombre d’électrons de valence à l’état fondamental et celui obtenu après partage.<br><br>
<b>Lacune électronique</b><br>
Symbole signalant le défaut d’un doublet, liant ou non liant, par rapport à la structure électronique de l’atome de gaz noble qui suit l’élément dans le tableau périodique. La présence d’une lacune électronique est un signe de grande réactivité pour l’entité.
{{%/notice%}}

> Exemple :<br>
L’atome de bore présente une lacune électronique dans la molécule de formule $\ce{BH3}$ (il y est entouré de 3 doublets contre 4 pour l’atome de néon), mais pas dans l’ion de formule $\ce{BH4-}$. Le bore porte une charge formelle négative dans le second édifice car il est entouré de 4 électrons après partage alors que l’atome de bore n’a que 3 électrons de valence à l’état isolé.


{{%notice definition "Caractère polaire d’une liaison covalente"%}}
Une liaison est dite polarisée lorsque les atomes liés ont des électronégativités différentes. La probabilité de présence des électrons du doublet liant tend alors à être supérieure dans le voisinage de l’atome le plus électronégatif. Cette situation peut être représentée par l’intermédiaire de charges partielles, notées δ+ et δ-, ou par le tracé d’un vecteur moment dipolaire.
{{%/notice%}}

> Exemple :<br>
La liaison $\ce{O-H}$ dans une molécule est polarisée, l’électronégativité de l’oxygène étant supérieure à celle de l’hydrogène. Les atomes d’hydrogène d’une molécule d’eau sont porteurs d’une charge partielle positive δ+ et l’oxygène d’une charge partielle 2δ-.

{{%notice definition "Polarité d’une entité polyatomique"%}}
Une entité polyatomique est dite polaire si le barycentre des charges positives et celui des charges négatives ne sont pas confondus. Cette situation se rencontre lorsque l’édifice présente des liaisons polaires et que les moments dipolaires de ces liaisons ne s’annulent pas. La reconnaissance d’une entité polaire nécessite par conséquent la connaissance de la géométrie de l’entité.
{{%/notice%}}

> Exemple :<br>
Parmi les entités à deux liaisons covalentes, la molécule d’eau $\ce{H2O}$ est une entité polaire, mais pas celle de dioxyde de carbone $\ce{CO2}$. Parmi celles à 3 liaisons covalentes, la molécule d’ammoniac $\ce{NH3}$ est polaire, mais pas celle de borane $\ce{BH3}$.


{{<youtube yRIVOV0OIhU>}}

## Documents et autres

<div style="overflow-x: auto;">
<table>
  <tr>
<th rowspan="1">Rappels</th>
<td><a href="../../2nde/lewis"><b>Cours de seconde sur la configuration électronique</b></a></td>
</tr>
    <tr>
    <th rowspan="2">Activités</th>
  <td style="border-bottom:none"><a href="/act-gels.pdf"><b> Hydrogels </b></a></td>
  </tr>
  <tr>
  <td style="border-top:none;"><a href="/act-beer2.pdf"><b>Tabagisme passif</b> (qu.&nbsp;3)</a></td>
  </tr>
      <tr>
    <th rowspan="2">Interactivité</th>
  <td style="border-bottom:none"><a href="https://phet.colorado.edu/sims/html/molecule-shapes/latest/molecule-shapes_fr.html"><b> Géométrie des molécules </b></a></td>
  </tr>
  <tr>
  <td style="border-top:none;"><a href="https://molview.org/?cid=2519"><b>Représentation 3D de molécules </b> </a></td>
  </tr>
  <tr>
<th rowspan="1">TP</th>
<td><a href="/tp-lewis.pdf"><b>Utilisation d'un logiciel de représentation 3D</b></a></td>
</tr>
</table>
</div>

<br>

<br>

<details>
<summary  style="text-align:center;font-size:1.1rem;"><a>Deux autres vidéos pour aller plus loin&nbsp;:</a></summary>
<br>
<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{<youtube M--6_0F62pQ>}}
</div>
<br>
<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{<youtube kgGq8xXJdIk>}}
</div>
</details>

