+++
title = "Le Soleil"
date = 2021-03-06T14:20:50+01:00
weight = 2
chapter = false
page_css = "css/soleil-accueil.css"
+++

<!--
  Page d'accueil du chapitre « Le Soleil », sur le modèle de la présentation (presentationssite.github.io/1es/soleil).
  Style : static/css/soleil-accueil.css, chargé uniquement sur cette page (paramètre page_css) et
  limité aux éléments situés sous le conteneur .sol-accueil.
-->

<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<filter id="sol-o1" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB"><feMorphology in="SourceAlpha" operator="dilate" radius="1.3" result="d"/><feMorphology in="SourceAlpha" operator="erode" radius="1.3" result="e"/><feComposite in="d" in2="e" operator="out" result="ring"/><feFlood flood-color="#ffb938"/><feComposite in2="ring" operator="in"/></filter>
<filter id="sol-o2" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB"><feMorphology in="SourceAlpha" operator="dilate" radius="1.3" result="d"/><feMorphology in="SourceAlpha" operator="erode" radius="1.3" result="e"/><feComposite in="d" in2="e" operator="out" result="ring"/><feFlood flood-color="#5cc8ff"/><feComposite in2="ring" operator="in"/></filter>
<filter id="sol-o3" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB"><feMorphology in="SourceAlpha" operator="dilate" radius="1.3" result="d"/><feMorphology in="SourceAlpha" operator="erode" radius="1.3" result="e"/><feComposite in="d" in2="e" operator="out" result="ring"/><feFlood flood-color="#b69cff"/><feComposite in2="ring" operator="in"/></filter>
</svg>

<div class="sol-accueil">

<header class="sol-hero">
<div class="sol-eclipse"></div>
<h1>Le Soleil, notre source d'énergie</h1>
<p class="sol-sub">Rayonnement, couleur des étoiles et bilan radiatif de la Terre</p>
<nav class="sol-actions">
<a class="sol-btn sol-btn-main" href="https://presentationssite.github.io/1es/soleil"><i class="fas fa-play"></i> Présentation<small>animations interactives et QCM</small></a>
<a class="sol-btn" href="/recapsoleil.pdf"><i class="fas fa-file-pdf"></i> Récap</a>
</nav>
</header>

<figure class="sol-photo">
<img src="/systsolech.png" alt="Le Soleil et les planètes du système solaire, à l'échelle">
</figure>

<section class="sol-part sol-p1">
<h2><span class="num">01</span>Rayonnement solaire</h2>
<div class="sol-media">
{{< youtube-plus id="MWUEh0xqtB4" ratio="16x9" >}}
</div>
</section>

<section class="sol-part sol-p2">
<h2><span class="num">02</span>Bilan radiatif terrestre</h2>

<div class="sol-media">
<video controls>
  <source src="/inclinaison.mp4" type="video/mp4">
</video>
</div>

<p class="sol-note"><i class="fas fa-globe-europe"></i> <a href="https://www.geogebra.org/m/ezzzm95w">Applet Geogebra</a> pour visualiser l'origine géométrique des lignes imaginaires que sont les tropiques et cercles polaires en lien avec les solstices et les équinoxes&nbsp;:</p>

<div class="sol-media">
<a href="https://www.geogebra.org/m/ezzzm95w">
<img src="/solsticegeogebra.png" alt="Applet GeoGebra : solstices et équinoxes">
</a>
</div>

<p class="sol-note"><i class="fas fa-video"></i> Vidéo filmée à Pune, en Inde, le 13 Mai 2023 (source&nbsp;: <a href="https://x.com/i/status/1657420559335182336">संकेत</a>) + <a href="https://alokm.com/zsd.html">tracking du zéro shadow day</a> + <a href="https://www.skymarvels.com/infopages/vids/Earth%20-%20Sub-solar%20Point%20001.htm">tracking du point subsolaire</a>&nbsp;:</p>

<div class="sol-media">
<video width="800" controls>
  <source src="/noshadow.mp4" type="video/mp4">
</video>
</div>

<div class="sol-media sol-xkcd">
<img src="https://www.explainxkcd.com/wiki/images/5/56/solar_panel_placement_2x.png" alt="xkcd : Solar Panel Placement">
</div>
</section>

<section class="sol-part sol-p3">
<h2><span class="num">03</span>Documents</h2>
<ul class="sol-docs">
<li><a href="/act-temp-etoile.pdf"><i class="fas fa-file-pdf"></i><span>Activité température et couleur des étoiles</span></a></li>
<li><a href="/act-dist-temp.pdf"><i class="fas fa-file-pdf"></i><span>Activité température et distance au Soleil</span></a></li>
<li><a href="/act-hauteur.pdf"><i class="fas fa-file-pdf"></i><span>Activité latitude et "hauteur" du Soleil</span></a></li>
<li><a href="/act-albedo.pdf"><i class="fas fa-file-pdf"></i><span>Activité température et albédo</span></a></li>
<li><a href="/act-bilanrad.pdf"><i class="fas fa-file-pdf"></i><span>Activité bilan radiatif</span></a><a class="sol-corr" href="/act-bilanrad-corr.pdf"><i class="fas fa-check-circle"></i> correction</a></li>
<!-- <li><a href="/correcevalsol.pdf">Correction DS</a></li> -->
</ul>
</section>

</div>
