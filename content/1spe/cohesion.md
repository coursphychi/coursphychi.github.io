---
title: "Cohésion"
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
.iframe-container {
    position: relative;
    width: 100%;
    padding-bottom: 71%;
    height: 0;
}
.iframe-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
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

<h1 style="overflow-x:auto;">Cohésion de la matière</h1>

<p style="font-size:1.5em;text-align:center;margin-top:-1.5em;">De la structure des entités à la cohésion et à la solubilité/miscibilité d’espèces chimiques</p>


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/1spe/cohesion"> Cours </a></p>


<div style="position: relative; max-width: 100%; margin-left: auto;margin-right: auto;">
<a href="/cm-cohesion.pdf"><img src="/cm-cohesion.png" "></a>
</div>



## Documents et autres

<div style="overflow-x: auto;">
<table>
<tr>
<th rowspan="2">Activité</th>
<td style="border-bottom:none;"><a href="/act-gels.pdf"><b>Hydrogels</b></a></td>
</tr>
<tr>
<td style="border-top:none;"><a href="/act-savon.pdf"><b>Savons</b></a> + <a href="/act-savon-corr.pdf"><b style="color:#FF644E;"><i class="fa-solid fa-pen-nib"></i></b></a></td>
</tr>
<tr>
<th rowspan="1">Schéma de montage / Protocole</th>
<td><a href="/protextr.pdf"><b>Extraction par solvant<br>(ou extraction liquide-liquide)</b></a></td>
</tr>
<tr>
<th rowspan="1">Manipulation</th>
<td><a href="https://culturesciences.chimie.ens.fr/thematiques/chimie-experimentale/synthese-organique/l-extraction-liquide-liquide"><b>Description de l'extraction liquide-liquide</i></b></a></td>
</tr>
<tr>
<th rowspan="1">TP</th>
<td><a href="/tp-liquideliquide.pdf"><b>Extraction par solvant</b></a></td>
</tr>    
 <tr>
  <th rowspan="4">En plus</th>
<td style="border-bottom:none;"><a href="https://www.cea.fr/multimedia/Documents/infographies/Defis-du-CEA-infographie-extraction-liquide-liquide.pdf"><b>Recyclage d'une terre rare</b> (application industrielle)</a></td>
</tr>
<tr>
<td style="border-bottom:none;border-top:none;"><a href="https://culturesciences.chimie.ens.fr/thematiques/chimie-du-vivant/les-forces-de-van-der-waals-et-le-gecko"><b>Forces de Van der Waals et le Gecko</b> (article)</a></td>
</tr>
<tr>
<td style="border-bottom:none;border-top:none;"><a href="https://youtu.be/rbKxs4-zzis"><b>Effet du sel sur une séparation de solvants</b> (vidéo)</a></td>
</tr>
<tr>
<td style="border-top:none;"><a href="https://youtu.be/VcaPh1-9XeA?si=-bNo7Y0F8lJlTd4B"><b>Tour de magie avec des polymères superabsorbants</b> (vidéo)</a></td>
</tr>
</table>
</div>

## Définitions

{{%notice definition "Cohésion dans une espèce chimique solide ou liquide"%}}
L’existence d’un volume propre pour un liquide ou un solide, à température et de pression données, est modélisée par des forces attractives entre entités, d’origine électrostatique, de courte portée et n’impliquant pas de mise en commun d’électrons : interaction entre deux ions, entre un ion et une entité polaire, entre deux entités polaires, entre deux entités polarisables.
{{%/notice%}}

> Exemple :<br>
La cohésion de cristaux de chlorure de sodium, observée à l’échelle macroscopique, peut s’expliquer par l’existence de forces attractives entre les cations $\ce{Na+}$ et les anions $\ce{Cl-}$ à l’échelle microscopique.

{{%notice definition "Polarisabilité d’une entité"%}}
La polarisabilité caractérise la capacité d’un nuage électronique à être déformé sous l’action d’un champ électrique extérieur, situation qui peut être induite par la proximité d’une autre entité, chargée ou non. En règle générale, plus un édifice est volumineux, plus il est polarisable.
{{%/notice%}}

{{%notice definition "Interaction par pont Hydrogène"%}}
Interaction d’origine électrostatique entre un atome très électronégatif, porteur de doublet non liant, et un atome d’hydrogène attaché à un autre atome très électronégatif. En pratique, cette interaction est principalement rencontrée lorsque l’atome très électronégatif est un atome de fluor, un atome d’oxygène ou un atome d’azote.
{{%/notice%}}

> Exemple :<br>
La cohésion de l’eau liquide est interprétée par l’existence d’interactions attractives entre molécules polaires et par ponts hydrogène.

<!--

<br>

<br>

<details>
<summary style="text-align:center;font-size:1.2rem;"><a>📖 BD sur la chimie 🧪</a></summary>

La BD ci-dessous est un panorama très sympa de toute la chimie. Petit défaut&nbsp;: certaines notations et représentations ne correspondent pas au programme actuel du lycée (les deux points à la place des doublets non liant par exemple), ça ne doit donc pas être considéré comme un cours&nbsp;!
<ul>
<li> le <a href="https://archive.org/details/317596081TheCartoonGuideToChemistryLarryGonickCraigCriddle/page/n50/mode/2up?view=theater"><b>chapitre 3</b></a> (p.&nbsp;45 à 66 dans la BD et <b>p.&nbsp;50 à 70</b> dans la liseuse) passe en revue les concepts des deux derniers chapitres (liaisons ioniques, liaisons covalentes et géométrie des molécules, polarité, liaisons inter-moléculaires, cohésion).</li>
<li>le <a href="https://archive.org/details/317596081TheCartoonGuideToChemistryLarryGonickCraigCriddle/page/n110/mode/2up?view=theater"><b>début du chapitre 6</b></a> (p. 105 à 108 dans la BD, <b>p. 110 à 114</b> de la liseuse) reparle des liaisons inter-moléculaires, de leur énergie et de leur origine (interaction électrostatique entre entités dipolaires ou non).</li>
<li>le <a href="https://archive.org/details/317596081TheCartoonGuideToChemistryLarryGonickCraigCriddle/page/n134/mode/2up?view=theater"><b>début du chapitre 7</b></a> (p. 129 à 132 de la BD, <b>p. 134 à 138</b> de la liseuse) est sur la solvatation.</li>
</ul>

<div class="iframe-container">
    <iframe id="myIframe" src="https://archive.org/embed/317596081TheCartoonGuideToChemistryLarryGonickCraigCriddle/page/n50/" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>
</div>

<button onclick="goFullscreen()" style="width:100%;background-color:#C2E3FD;">Pour passer en plein écran</button>

</details>

<script>
function goFullscreen() {
var iframe = document.getElementById('myIframe');
if (iframe.requestFullscreen) {
  iframe.requestFullscreen();
} else if (iframe.webkitRequestFullscreen) {
  iframe.webkitRequestFullscreen();
} else if (iframe.mozRequestFullScreen) {
  iframe.mozRequestFullScreen();
} else if (iframe.msRequestFullscreen) {
  iframe.msRequestFullscreen();
} else {
  // Si le plein écran n'est pas supporté, ouvrir le lien de l'iframe dans un nouvel onglet
  window.open(iframe.src, '_blank');
}
}

// Polyfill for older browsers
document.addEventListener('fullscreenchange', (event) => {
if (document.fullscreenElement) {
  console.log(`Element: ${document.fullscreenElement.id} entered full-screen mode.`);
} else {
  console.log('Leaving full-screen mode.');
}
});

document.addEventListener('webkitfullscreenchange', (event) => {
if (document.webkitFullscreenElement) {
  console.log(`Element: ${document.webkitFullscreenElement.id} entered full-screen mode.`);
} else {
  console.log('Leaving full-screen mode.');
}
});

document.addEventListener('mozfullscreenchange', (event) => {
if (document.mozFullScreenElement) {
  console.log(`Element: ${document.mozFullScreenElement.id} entered full-screen mode.`);
} else {
  console.log('Leaving full-screen mode.');
}
});

document.addEventListener('MSFullscreenChange', (event) => {
if (document.msFullscreenElement) {
  console.log(`Element: ${document.msFullscreenElement.id} entered full-screen mode.`);
} else {
  console.log('Leaving full-screen mode.');
}
});
</script>

-->
