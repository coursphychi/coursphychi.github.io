---
title: "Filet d'eau"
date: 2026-11-14T10:00:00+01:00
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



# Filet d'eau

On frotte une règle en plastique contre un pull en laine et on l'approche, à quelques centimètres, d'un mince filet d'eau qui s'écoule d'un robinet : le filet s'incurve vers la règle, de l'ordre du centimètre au bas de l'évier.

Dans de nombreux manuels, cette expérience est présentée comme la preuve que **la molécule d'eau est polaire** : les molécules, petits dipôles permanents, s'orienteraient dans le champ de la règle et seraient attirées vers les zones de champ fort. On se propose de tester quantitativement cette explication.

**Données.**

- moment dipolaire d'une molécule d'eau : $p_0 = 6{,}2\times10^{-30}\ \mathrm{C\cdot m}$ ; nombre de molécules par unité de volume : $n=3{,}3\times10^{28}\ \mathrm{m^{-3}}$ ; masse volumique : $\rho=1000\ \mathrm{kg\cdot m^{-3}}$ ;
- $k_B=1{,}38\times10^{-23}\ \mathrm{J\cdot K^{-1}}$, $T=293\ \mathrm{K}$, $\varepsilon_0=8{,}85\times10^{-12}\ \mathrm{F\cdot m^{-1}}$ ;
- à la distance $r=2\ \mathrm{cm}$ de la règle, le champ électrique vaut $E\approx10^5\ \mathrm{V\cdot m^{-1}}$ ; il varie avec la distance comme celui d'un fil chargé : $E\propto 1/r$ ;
- le filet, de rayon $a=1\ \mathrm{mm}$, est vertical. Le champ de la règle ne le touche que sur une hauteur de $5\ \mathrm{cm}$, que l'eau traverse en $\Delta t_1\approx 40\ \mathrm{ms}$ ; elle tombe ensuite en $\Delta t_2\approx 0{,}10\ \mathrm{s}$ jusqu'au fond de l'évier ;
- pour une accélération horizontale constante $a_x$ dans la zone d'interaction, puis une chute à vitesse horizontale constante, la déviation au fond est $\Delta x = a_x\mkern3mu \Delta t_1\left(\tfrac12\Delta t_1+\Delta t_2\right)$.

---

## Partie A : les dipôles s'alignent-ils ?

1. Rappeler l'énergie potentielle d'un dipôle $\overrightarrow{p}$ dans un champ $\overrightarrow{E}$. Comparer son ordre de grandeur à l'énergie d'agitation thermique $k_BT$. Qu'en déduire sur l'alignement des molécules d'eau ?

2. Un dipôle de moment $p_0$ fait l'angle $\theta$ avec le champ. Sa direction est repérée sur la sphère unité, et la probabilité d'observer un angle compris entre $\theta$ et $\theta+\mathrm{d}\theta$ est proportionnelle à $\mathrm{e}^{-U/k_BT}\sin\theta\mkern3mu \mathrm{d}\theta$. Justifier la présence du facteur $\sin\theta$. En se plaçant dans la limite $x=\frac{p_0E}{k_BT}\ll1$, montrer que
$$\langle\cos\theta\rangle\simeq\frac{x}{3}.$$
On donne $\displaystyle\int_0^\pi\cos^2\theta\mkern3mu \sin\theta\mkern3mu \mathrm{d}\theta=\frac23$.

3. En déduire le moment dipolaire moyen $\langle p\rangle$ d'une molécule puis la polarisation $P$ de l'eau (moment dipolaire par unité de volume), proportionnelle à $E$. Calculer $P$. Quelle fraction de la polarisation maximale $np_0$ cela représente-t-il ?

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">

1. $U=-\overrightarrow{p}\cdot\overrightarrow{E}=-p_0E\cos\theta$, donc $|U|\le p_0E\approx 6\times10^{-25}\ \mathrm{J}$, alors que $k_BT\approx4\times10^{-21}\ \mathrm{J}$. Le rapport vaut $x=\frac{p_0E}{k_BT}\approx 1{,}5\times10^{-4}$ : l'énergie d'alignement est environ 7000 fois plus faible que l'agitation thermique. Les molécules **ne s'alignent pas** comme des aiguilles de boussole : le champ ne fait qu'infléchir très légèrement une distribution presque isotrope.

2. Les directions possibles forment la sphère unité : l'élément d'angle solide compris entre $\theta$ et $\theta+\mathrm{d}\theta$ est $2\pi\sin\theta\mkern3mu \mathrm{d}\theta$ (il y a bien plus de directions proches de l'équateur que des pôles). Le poids de Boltzmann étant $\mathrm{e}^{x\cos\theta}$,
$$\langle\cos\theta\rangle=\frac{\int_0^\pi\cos\theta\mkern3mu \mathrm{e}^{x\cos\theta}\sin\theta\mkern3mu \mathrm{d}\theta}{\int_0^\pi\mathrm{e}^{x\cos\theta}\sin\theta\mkern3mu \mathrm{d}\theta}.$$
Pour $x\ll1$, $\mathrm{e}^{x\cos\theta}\simeq1+x\cos\theta$. Au numérateur, $\int\cos\theta\sin\theta\mkern3mu \mathrm{d}\theta=0$ (le terme d'ordre 0 disparaît par symétrie), il reste $x\cdot\frac23$. Au dénominateur, à l'ordre le plus bas, $\int\sin\theta\mkern3mu \mathrm{d}\theta=2$. D'où
$$\langle\cos\theta\rangle\simeq\frac{x\cdot\frac23}{2}=\frac x3 .$$

3. La composante moyenne du dipôle sur $\overrightarrow{E}$ est $\langle p\rangle=p_0\langle\cos\theta\rangle=\dfrac{p_0^2E}{3k_BT}$, et
$$P=n\langle p\rangle=\frac{np_0^2}{3k_BT}\mkern3mu E .$$
Numériquement, $P=\dfrac{3{,}3\times10^{28}\times(6{,}2\times10^{-30})^2\times10^5}{3\times1{,}38\times10^{-23}\times293}\approx1\times10^{-5}\ \mathrm{C\cdot m^{-2}}$, à comparer à $np_0\approx0{,}2\ \mathrm{C\cdot m^{-2}}$ : seule une molécule sur vingt mille est « utilement » alignée. On peut écrire $P=\varepsilon_0\chi E$ avec $\chi=\frac{P}{\varepsilon_0E}\approx11$.

</blockquote>
</details>

---

## Partie B : la force subie par l'eau polarisée

4. Un dipôle est formé d'une charge $-q$ en $x$ et d'une charge $+q$ en $x+d$ ($d$ petit), placé dans un champ $\overrightarrow{E}=E(x)\overrightarrow{u_x}$. Exprimer la résultante des forces et montrer qu'elle vaut $p\mkern3mu \dfrac{\mathrm{d}E}{\mathrm{d}x}$ avec $p=qd$. Que vaut-elle dans un champ uniforme ?

5. En déduire la force volumique $f$ qui s'exerce sur l'eau polarisée dans le champ de la règle (on prendra $E\propto1/r$ et $P$ parallèle à $E$). Dans quel sens est-elle dirigée ? Calculer $f$ puis l'accélération $a_{\text{dip}}$ du filet.

6. Calculer la déviation $\Delta x_{\text{dip}}$ au fond de l'évier et conclure. Que se passerait-il si l'on utilisait la valeur mesurée $\chi\approx79$, plus grande que celle trouvée à la question 3 car les molécules d'eau, liées par liaisons hydrogène, basculent en groupes ?

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">

4. $F=qE(x+d)-qE(x)\simeq qd\mkern3mu \dfrac{\mathrm{d}E}{\mathrm{d}x}=p\mkern3mu \dfrac{\mathrm{d}E}{\mathrm{d}x}$. Les deux forces sont égales et opposées en champ uniforme : la résultante est **nulle** (il reste un couple, qui fait pivoter le dipôle). Il faut un gradient de champ pour attirer un dipôle.

5. Par sommation sur les dipôles d'un volume unité, $f=P\mkern3mu \dfrac{\mathrm{d}E}{\mathrm{d}r}$ en norme. Avec $\left|\frac{\mathrm{d}E}{\mathrm{d}r}\right|=\frac Er$ et $P=\varepsilon_0\chi E$,
$$f=\frac{\varepsilon_0\chi E^2}{r}.$$
La force est dirigée vers les zones de champ fort, donc vers la règle, quel que soit le signe de la charge de la règle (elle varie comme $\frac12\mkern3mu \frac{\mathrm{d}(E^2)}{\mathrm{d}r}$). Numériquement $f=\dfrac{8{,}85\times10^{-12}\times11\times10^{10}}{0{,}02}\approx50\ \mathrm{N\cdot m^{-3}}$ et $a_{\text{dip}}=\dfrac f\rho\approx5\times10^{-2}\ \mathrm{m\cdot s^{-2}}$.

6. $\Delta x_{\text{dip}}=0{,}05\times0{,}04\times(0{,}02+0{,}10)\approx2\times10^{-4}\ \mathrm{m}=0{,}2\ \mathrm{mm}$ : cinquante fois moins que le centimètre observé. Avec $\chi=79$, on trouve $a\approx0{,}35\ \mathrm{m\cdot s^{-2}}$ et $\Delta x\approx1{,}7\ \mathrm{mm}$ : mieux, mais toujours six fois trop petit, **et c'est une surestimation**, car le champ à l'intérieur de l'eau polarisée est plus faible que le champ de la règle (champ dépolarisant des charges de surface du filet, qui divise encore par environ 40). L'hypothèse des dipôles échoue donc de plus de deux ordres de grandeur.

</blockquote>
</details>

---

## Partie C : un autre mécanisme

7. On fait passer le filet entre les armatures d'un condensateur plan chargé, où le champ est uniforme. Que prédit le modèle dipolaire ? Expérimentalement, le filet est dévié, de façon spectaculaire, vers l'une des armatures. Que peut-on en conclure sur le filet ?

8. L'eau du robinet est un conducteur ohmique de conductivité $\sigma\approx5\times10^{-2}\ \mathrm{S\cdot m^{-1}}$ et de permittivité relative $\varepsilon_r=80$. En combinant la loi d'Ohm locale, la conservation de la charge et l'équation de Maxwell-Gauss, établir l'équation d'évolution de la densité volumique de charge $\rho_e$ et en déduire un temps caractéristique $\tau_e$. Calculer sa valeur et comparer à $\Delta t_1$. Que dire du potentiel du filet, relié au robinet donc à la terre ?

9. On modélise le filet par un cylindre infini de rayon $a$, conducteur, au potentiel de la terre. Sous l'effet de la règle, il porte la charge linéique $\lambda$. À l'intérieur de l'eau, le champ du filet compense celui de la règle ; on admet qu'à la distance $r$ du filet, son champ propre est du même ordre que $E$. Calculer $\lambda$ à l'aide du théorème de Gauss, puis la force par unité de longueur $F_\ell=\lambda E$ et l'accélération $a_{\text{ion}}$ du filet (de masse linéique $\mu=\rho\pi a^2$).

10. Calculer la déviation correspondante et comparer au cas dipolaire. Proposer une expérience simple pour trancher entre les deux mécanismes autre que celle de la question 7.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">

7. Le modèle dipolaire prédit une force **nulle** (question 4), donc un filet non dévié. La déviation observée montre que le filet porte une **charge nette** : la force $q\overrightarrow{E}$ ne demande aucun gradient. Le sens de la déviation donne le signe de cette charge.

8. Avec $\overrightarrow{j}=\sigma\overrightarrow{E}$, $\operatorname{div}\overrightarrow{j}+\dfrac{\partial\rho_e}{\partial t}=0$ et $\operatorname{div}\overrightarrow{E}=\dfrac{\rho_e}{\varepsilon_r\varepsilon_0}$ :
$$\frac{\partial\rho_e}{\partial t}+\frac{\sigma}{\varepsilon_r\varepsilon_0}\rho_e=0\quad\Longrightarrow\quad\rho_e(t)=\rho_e(0)\mkern3mu \mathrm{e}^{-t/\tau_e},\qquad\tau_e=\frac{\varepsilon_r\varepsilon_0}{\sigma}.$$
Numériquement $\tau_e=\dfrac{80\times8{,}85\times10^{-12}}{5\times10^{-2}}\approx1{,}4\times10^{-8}\ \mathrm{s}$, soit $14\ \mathrm{ns}\ll\Delta t_1=40\ \mathrm{ms}$. Les charges libres se réorganisent beaucoup plus vite que le temps de traversée : à l'échelle de l'expérience, le filet est un **conducteur à l'équilibre**, équipotentiel, au potentiel de la terre (même pour de l'eau très pure, $\sigma\approx5\times10^{-6}\ \mathrm{S\cdot m^{-1}}$ donne seulement $0{,}13\ \mathrm{ms}$). Les ions positifs sont attirés vers le flanc qui fait face à la règle (si elle est négative), les ions négatifs refoulés vers le robinet : le filet s'électrise **par influence**.

9. Théorème de Gauss sur un cylindre coaxial de rayon $\rho$ et de hauteur $h$ : $2\pi\rho h\mkern3mu E_{\text{filet}}(\rho)=\dfrac{\lambda h}{\varepsilon_0}$, d'où $E_{\text{filet}}=\dfrac{\lambda}{2\pi\varepsilon_0\rho}$. En $\rho=r$, l'égalité avec $E$ donne
$$\lambda\approx2\pi\varepsilon_0Er=2\pi\times8{,}85\times10^{-12}\times10^5\times0{,}02\approx1{,}1\times10^{-7}\ \mathrm{C\cdot m^{-1}}.$$
La force par unité de longueur est $F_\ell=\lambda E\approx1{,}1\times10^{-2}\ \mathrm{N\cdot m^{-1}}$, et
$$a_{\text{ion}}=\frac{F_\ell}{\rho\pi a^2}=\frac{2\varepsilon_0rE^2}{\rho a^2}\approx3{,}5\ \mathrm{m\cdot s^{-2}}.$$

10. $\Delta x_{\text{ion}}=3{,}5\times0{,}04\times0{,}12\approx1{,}7\ \mathrm{cm}$ : **le bon ordre de grandeur**, soit environ 70 fois plus que le mécanisme dipolaire, ou 10 fois plus même avec $\chi=79$. Le rapport des deux accélérations est indépendant de $E$ : $\dfrac{a_{\text{ion}}}{a_{\text{dip}}}=\dfrac{2}{\chi}\left(\dfrac ra\right)^2\approx70$. Le facteur $(r/a)^2$ traduit la différence entre une charge nette, portée par la surface du filet et que le champ attire directement, et des dipôles neutres répartis dans tout son volume, sur lesquels le champ n'agit que par son gradient. Pour trancher : isoler électriquement le filet de la terre (robinet en plastique, ou filet tombant dans un seau isolé) ; ou, mieux, **mesurer la charge des gouttes** qui se détachent du filet à l'aide d'une coupelle de Faraday ou d'un électroscope : si elles portent une charge de signe opposé à celui de la règle, le mécanisme est bien l'influence, et non la polarité de la molécule.

</blockquote>
</details>

---

Cette expérience est détaillée, avec l'estimation du champ dépolarisant et le rôle de la charge des gouttes, dans la page [La déviation du filet d'eau](https://sciencesilencieuse.github.io/physique/electromag/filetdeau/).
