---
title: "EEPROM"
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





# Écriture sur mémoire EEPROM


<div style="position:relative;margin-left:auto;margin-right:auto;width:600px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/eprom.png" style="box-shadow:none;background:none;">
</div>

D’après la notice de cette mémoire EEPROM, une information ne peut être écrite que si le potentiel électrique sur l’une des broches passe de 5V à 0V pendant un délai compris entre 100 et 1000 ns.

On souhaite pouvoir enclencher l’écriture sur la mémoire grâce à un bouton pressoir. 

1. Pourquoi le bouton seul ne peut pas suffire aux vues des spécifications&nbsp;?

<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/schemaeeprom.png" style="box-shadow:none;background:none;">
</div>

2. Montrer que le circuit ci-dessus permet de les respecter. On considèrera que la bascule de 0 à 1 de la broche se fait quand le potentiel dépasse 3,8V.

3. À quoi sert la résistance de 100&nbsp;Ω&nbsp;?

4. Représenter $u_c(t)$ au moment de l’appui sur l’interrupteur et au moment du relâchement.

<br>

<div style="position:relative;margin-left:auto;margin-right:auto;width:fit-content;max-width:100%;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/BA12Z7gQ4P0?si=_Ym4Yg4Gd528PVTx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius:10px;"></iframe>
</div>
