---
title: "Doigts et balai"
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





# Doigts et balai

<p style="text-align:center;"><i>(extrait de l'épreuve X Physique 1 PC 2007)</i></p>

<div style="position:relative;margin:auto;width:fit-content;max-width:100%;border-radius:10px;">
<iframe src="https://pod.univ-lille.fr/video/1386-centre-de-gravite-dun-balai/?is_iframe=true" width="640" height="360" style="padding: 0; margin: 0; border:0; border-radius:10px; max-width:100%;" allowfullscreen title="Centre de gravité d'un balai" ></iframe>
</div>

<br>

Un balai est tenu horizontalement à l'équilibre entre deux doigts.

On va tenter d'expliquer ce qui se passe lorsqu'on tente de rapprocher gentiment les deux doigts.

Appelons $d(t)$ la distance qui sépare les doigts (avec $d(0)=d_0$) et $a(t)$ la distance qui sépare le doigt de gauche du centre de gravité du balai. On a initialement $a(0)=a_0<d_0/2$.

Les deux doigts se déplacent l'un vers l'autre à une vitesse constante de $v_0/2$ (on a ainsi $d(t)=d_0-v_0t$).

On suppose que le balai ne glisse au départ que sur un des deux doigts.

1.  De quel doigt s'agit-il ?

2. Montrer qu'il existe un temps $t_1$ où le balai se met à glisser sur l'autre doigt. Que vaut $d_1=d(t_1)$&nbsp;?

3. Justifier que juste après $t_1$, le balai glisse nécessairement sur les deux doigts. Décrire la phase de transition jusqu'à l'instant $t_1^\prime$ où le balai ne glisse maintenant plus sur le doigt qui glissait au départ.

4. En supposant que la phase de transition est suffisamment courte pour être négligée ($t_1\approx t'_1$)[^1], déterminer la distance $d_2=d(t\_2)$ entre les deux doigts à l'instant $t_2$ où le balai se remet à glisser sur le même doigt qu'au début. 

5. Que vaut $\frac{d(t_2)}{d(t_1)}$&nbsp;? En déduire une méthode pour déterminer le rapport $\frac{\mu_c}{\mu_s}$&nbsp;?

[^1]: Ce que la petite simulation ci-dessus semble justifier.



{{< runpython lang="vpython" mode="toggle" default="code" file="doigtbalais.py" >}}
{{< /runpython >}}
