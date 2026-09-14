+++
title = "Cours de physique-chimie"
date = 2021-03-06T14:20:50+01:00
weight = 0
chapter = true
+++

<style>
body {
background-color:#101010;
}
td {
text-align:center;
}
a {
font-size:1.5em;
color: white;
font-weight: lighter;
}

/* Reset global pour ce lien spécifique */
a.alarm-link {
  display: inline-block !important; /* Indispensable pour que le 'transform' survive au thème */
  color: #aaa !important; /* Verrouille la couleur face aux styles de liens du thème */
  text-decoration: none !important;
  background: none !important;
  box-shadow: none !important;
  border: none !important;
  line-height: 1;
  
  /* Paramètres d'animation */
  transform-origin: center center;
  transition: transform 160ms ease !important;
}

/* Neutralisation des pseudo-éléments (effets de soulignement, flèches, etc.) */
a.alarm-link::before,
a.alarm-link::after {
  display: none !important;
  content: none !important;
}

/* Comportement au survol et au clic */
a.alarm-link:hover,
a.alarm-link:active {
  transform: scale(1.25) !important; /* Force l'animation */
  background: none !important; /* Empêche le thème d'ajouter un fond au survol */
  /* color: #888 !important; Optionnel : foncer légèrement l'icône au survol */
}

/* Accessibilité (Navigation au clavier) */
a.alarm-link:focus-visible {
  outline: 2px solid currentColor !important;
  outline-offset: 4px !important;
  border-radius: 8px !important;
}
/* On s'assure que le lien englobe bien l'icône */
a.alarm-link {
  display: inline-block !important;
  padding: 5px; /* Donne un peu de "matière" à survoler */
}

/* L'animation est appliquée à l'enfant (i ou svg) lors du survol du parent (a) */
a.alarm-link i,
a.alarm-link svg {
  display: inline-block !important;
  transform-origin: center center;
  transition: transform 160ms ease !important;
}

a.alarm-link:hover i,
a.alarm-link:hover svg {
  transform: scale(1.25) !important;
}
</style>


# <span style="color:white">Cours de physique-chimie</span>


![](/lentgrav.jpg)



<div style="overflow-x: auto;">
<table>
  <tr>
    <td><a href = "/2nde" >2NDE</a></td>  <td><a href = "/1spe" >1SPÉ</a></td><td><a href = "/tspe">TSPÉ</a></td>
  </tr>
  <tr>
<td><a href = "/1sti2d"> 1STI2D </a></td>  <td><a href = "/tsti2d"> TSTI2D </a></td><td><a href = "/colles">Colles</a></td>
  </tr>
    <tr>
  <td><a href = "/1es"> 1ES </a></td>  <td><a href = "/tes" >TES</a></td><td><a href = "https://sciencesilencieuse.github.io" >MORE</a></td>
  </tr>
</table>
</div>

<br>

<p>
<a class="alarm-link" href="/minuteur.html" aria-label="Minuteur">
  <i class="fa-solid fa-stopwatch" aria-hidden="true"></i>
</a>
</p>

<p style="color:#929292">Pour toute question : 
    <a id="email-link" href="mailto:" style="font-size:1em;"></a>
</p>

<script type="text/javascript">
    var part1 = "cordier.sc.phy";
    var part2 = "gmail";
    var part3 = "com";
    var email = part1 + "@" + part2 + "." + part3;

    // Mettre à jour le lien
    var link = document.getElementById("email-link");
    link.href = "mailto:" + email;
    link.textContent = email;
</script>