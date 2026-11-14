---
title: "Filet d'eau (électrostatique)"
date: 2026-11-14T10:00:00+01:00
weight : 1
draft: false
hidden: true
---

<!--
Version « électrostatique seule » de la colle Filet d'eau.
Retirés par rapport à la version complète : le facteur de Boltzmann et l'alignement thermique des dipôles
(physique statistique), la loi d'Ohm locale et le temps de relaxation de Maxwell (conduction).
Ajoutés : champ du fil par le théorème de Gauss, champ dépolarisant par superposition de deux cylindres chargés,
condensateur filet-règle (capacité linéique).
-->

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
h1
{
overflow-x:auto;
}
</style>



<h1>Filet d'eau (électrostatique)</h1>

On frotte une règle en plastique contre un pull en laine et on l'approche, à quelques centimètres, d'un mince filet d'eau qui s'écoule d'un robinet : le filet s'incurve vers la règle, de l'ordre du centimètre au bas de l'évier.

Dans de nombreux manuels, cette expérience est présentée comme la preuve que **la molécule d'eau est polaire** : l'eau, polarisée par le champ de la règle, serait attirée vers les zones de champ fort. On se propose de tester quantitativement cette explication, puis de la comparer à une autre.

**Données.**

- $\varepsilon_0=8{,}85\times10^{-12}\ \mathrm{F\cdot m^{-1}}$ ; masse volumique de l'eau : $\rho=1000\ \mathrm{kg\cdot m^{-3}}$ ; permittivité relative de l'eau : $\varepsilon_r=80$ ;
- la règle est assimilée à un fil rectiligne infini, horizontal, uniformément chargé ; à la distance $r=2\ \mathrm{cm}$ de son axe, le champ vaut $E\approx10^5\ \mathrm{V\cdot m^{-1}}$ ;
- le filet, vertical, a un rayon $a=1\ \mathrm{mm}$. Le champ de la règle ne le touche que sur une hauteur de $5\ \mathrm{cm}$, que l'eau traverse en $\Delta t_1\approx 40\ \mathrm{ms}$ ; elle tombe ensuite en $\Delta t_2\approx 0{,}10\ \mathrm{s}$ jusqu'au fond de l'évier ;
- pour une accélération horizontale constante $a_x$ dans la zone d'interaction, puis une chute à vitesse horizontale constante, la déviation au fond est $\Delta x = a_x\mkern3mu \Delta t_1\left(\tfrac12\Delta t_1+\Delta t_2\right)$.

---

## Partie A : l'hypothèse de l'eau polarisée

1. Montrer par le théorème de Gauss que le champ de la règle, à la distance $r$ de son axe, s'écrit $E(r)=\dfrac{\Lambda}{2\pi\varepsilon_0r}$, où $\Lambda$ est la charge linéique. En déduire $\left|\dfrac{\mathrm{d}E}{\mathrm{d}r}\right|$ en fonction de $E$ et $r$, puis calculer $\Lambda$.

2. Un dipôle est formé d'une charge $-q$ en $x$ et d'une charge $+q$ en $x+d$ ($d$ petit), placé dans un champ $\overrightarrow{E}=E(x)\overrightarrow{u_x}$. Montrer que la résultante des forces vaut $p\mkern3mu \dfrac{\mathrm{d}E}{\mathrm{d}x}$ avec $p=qd$. Que vaut-elle dans un champ uniforme ?

3. L'eau, polarisée, porte un moment dipolaire par unité de volume $\overrightarrow{P}$, parallèle à $\overrightarrow{E}$. En déduire la force volumique $f$ exercée dans le champ de la règle. On suppose dans un premier temps que le champ à l'intérieur de l'eau est égal à celui de la règle, de sorte que $P=\varepsilon_0(\varepsilon_r-1)E$. Calculer $f$, l'accélération $a_{\text{dip}}$ du filet et la déviation $\Delta x$ au fond de l'évier. Comparer à l'observation.

4. En réalité, le champ à l'intérieur du filet n'est pas $\overrightarrow{E}$, mais $\overrightarrow{E_{\text{int}}}=\overrightarrow{E}+\overrightarrow{E_{\text{dép}}}$, où $\overrightarrow{E_{\text{dép}}}$ est le champ créé par les charges de polarisation du filet lui-même.
    - a) Un cylindre infini d'axe $Oz$ et de rayon $a$ porte la densité volumique de charge uniforme $+\rho_0$. Montrer par le théorème de Gauss que le champ en un point intérieur $M$ vaut $\dfrac{\rho_0}{2\varepsilon_0}\overrightarrow{OM}$, où $O$ est le projeté de $M$ sur l'axe.
    - b) Un filet polarisé transversalement, avec la polarisation uniforme $\overrightarrow{P}$, équivaut à deux cylindres de charges volumiques $+\rho_0$ et $-\rho_0$, légèrement décalés de $\overrightarrow{\delta}$ avec $\overrightarrow{P}=\rho_0\overrightarrow{\delta}$. En déduire $\overrightarrow{E_{\text{dép}}}$.
    - c) Avec $\overrightarrow{P}=\varepsilon_0(\varepsilon_r-1)\overrightarrow{E_{\text{int}}}$, exprimer $E_{\text{int}}$ en fonction de $E$, puis corriger la déviation de la question 3. Conclure.

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">

1. Par symétrie, le champ est radial et ne dépend que de $r$. Gauss sur un cylindre coaxial de rayon $r$ et de longueur $h$ : $2\pi rh\mkern3mu E(r)=\dfrac{\Lambda h}{\varepsilon_0}$, donc $E(r)=\dfrac{\Lambda}{2\pi\varepsilon_0r}\propto\dfrac1r$. Ainsi $\dfrac{\mathrm{d}E}{\mathrm{d}r}=-\dfrac Er$, de norme $\dfrac Er$. Numériquement, $\Lambda=2\pi\varepsilon_0Er\approx1{,}1\times10^{-7}\ \mathrm{C\cdot m^{-1}}$.

2. $F=qE(x+d)-qE(x)\simeq qd\mkern3mu \dfrac{\mathrm{d}E}{\mathrm{d}x}=p\mkern3mu \dfrac{\mathrm{d}E}{\mathrm{d}x}$. En champ uniforme, les deux forces sont égales et opposées : la résultante est **nulle** (il reste un couple, qui fait pivoter le dipôle). Il faut un gradient de champ pour attirer un dipôle.

3. Par sommation sur un volume unité, $f=P\left|\dfrac{\mathrm{d}E}{\mathrm{d}r}\right|=\dfrac{PE}{r}$, dirigée vers les zones de champ fort, donc vers la règle, quel que soit le signe de sa charge ($P$ et $E$ changent de signe ensemble : la force varie comme $\frac12\mkern3mu \frac{\mathrm{d}(E^2)}{\mathrm{d}r}$). Avec $P=\varepsilon_0(\varepsilon_r-1)E$,<br>
$\displaystyle f=\frac{\varepsilon_0(\varepsilon_r-1)E^2}{r}=\frac{8{,}85\times10^{-12}\times79\times10^{10}}{0{,}02}\approx3{,}5\times10^{2}\ \mathrm{N\cdot m^{-3}},\qquad a_{\text{dip}}=\frac f\rho\approx0{,}35\ \mathrm{m\cdot s^{-2}}.$

Puis $\Delta x=0{,}35\times0{,}04\times(0{,}02+0{,}10)\approx1{,}7\ \mathrm{mm}$, six fois moins que le centimètre observé, et c'est déjà une **surestimation**.

4. a) Gauss sur un cylindre coaxial de rayon $\rho<a$ et de longueur $h$ : $2\pi\rho h\mkern3mu E=\dfrac{\rho_0\mkern3mu \pi\rho^2h}{\varepsilon_0}$, d'où $\overrightarrow{E}=\dfrac{\rho_0}{2\varepsilon_0}\overrightarrow{OM}$ (le facteur $\frac12$ vient du rapport de la surface du disque $\pi\rho^2$ à son périmètre $2\pi\rho$).

   b) Soit $O_+$ et $O_-$ les axes des deux cylindres, avec $\overrightarrow{O_-O_+}=\overrightarrow{\delta}$. Par superposition,<br>
   $\displaystyle \overrightarrow{E_{\text{dép}}}=\frac{\rho_0}{2\varepsilon_0}\overrightarrow{O_+M}-\frac{\rho_0}{2\varepsilon_0}\overrightarrow{O_-M}=\frac{\rho_0}{2\varepsilon_0}\overrightarrow{O_+O_-}=-\frac{\rho_0\overrightarrow{\delta}}{2\varepsilon_0}=-\frac{\overrightarrow{P}}{2\varepsilon_0}.$
   
   Le champ dépolarisant est **uniforme** dans le filet et **opposé** à $\overrightarrow{P}$ : les charges de polarisation écrantent le champ appliqué.

   c) On a $\overrightarrow{E_{\text{int}}}=\overrightarrow{E}-\dfrac{\overrightarrow{P}}{2\varepsilon_0}=\overrightarrow{E}-\dfrac{\varepsilon_r-1}{2}\overrightarrow{E_{\text{int}}}$, soit
   $$\overrightarrow{E_{\text{int}}}=\frac{2}{\varepsilon_r+1}\overrightarrow{E}\approx\frac{\overrightarrow{E}}{40},\qquad\overrightarrow{P}=2\varepsilon_0\frac{\varepsilon_r-1}{\varepsilon_r+1}\overrightarrow{E}.$$
   La polarisation est donc $\dfrac{\varepsilon_r+1}{2}\approx40$ fois plus faible que dans le calcul naïf : $a_{\text{dip}}\approx9\times10^{-3}\ \mathrm{m\cdot s^{-2}}$ et $\Delta x\approx40\ \mathrm{\mu m}$, **deux cents fois** moins que le centimètre observé. L'hypothèse de la polarisation de l'eau doit être abandonnée.

</blockquote>
</details>

---

## Partie B : un filet chargé

5. On fait passer le filet entre les armatures d'un condensateur plan chargé, où le champ est uniforme. Que prédit l'hypothèse de l'eau polarisée ? Expérimentalement, le filet est dévié, de façon spectaculaire, vers l'une des armatures. Que peut-on en conclure sur le filet ?

6. L'eau du robinet est conductrice, et le filet est relié à la terre par la tuyauterie. On admet qu'à l'échelle de l'expérience il est à l'équilibre électrostatique, donc **équipotentiel**, au potentiel $V=0$ de la terre. La règle est portée au potentiel $V_0\approx6\ \mathrm{kV}$. Pour que le filet reste au potentiel nul, des charges s'y accumulent : la charge linéique $\lambda$, de signe opposé à celle de la règle (électrisation par influence).
    - a) Exprimer le champ créé par le filet à la distance $\rho>a$ de son axe. En déduire la tension entre le filet et la règle, et la capacité linéique $C_\ell$ du système (on assimile la règle, à la distance $r\gg a$, à une armature).
    - b) Calculer $\lambda$, puis vérifier que le champ propre du filet à la distance $r$ est cohérent avec la valeur $E\approx10^5\ \mathrm{V\cdot m^{-1}}$ donnée.

7. En déduire la force par unité de longueur exercée par la règle sur le filet, puis l'accélération $a_{\text{ion}}$ et la déviation $\Delta x_{\text{ion}}$. Comparer à $\Delta x_{\text{dip}}$ de la question 4 et à l'observation. Le rapport $\dfrac{a_{\text{ion}}}{a_{\text{dip}}}$ dépend-il de $E$ ?

8. Proposer une expérience, autre que celle de la question 5, pour confirmer que le filet est bien chargé. Quel signe observe-t-on pour la charge des gouttes qui se détachent du filet, si la règle est chargée négativement ?

<details>
<summary id="correcsum">
Correction</summary>
<blockquote id="correc">

5. Le modèle de l'eau polarisée prédit une force **nulle** en champ uniforme (question 2), donc un filet non dévié. La déviation observée montre que le filet porte une **charge nette** : la force $q\overrightarrow{E}$ ne demande aucun gradient. Le sens de la déviation donne le signe de cette charge.

6. a) Gauss sur un cylindre coaxial de rayon $\rho$ et de longueur $h$ : $E_{\text{filet}}(\rho)=\dfrac{\lambda}{2\pi\varepsilon_0\rho}$. La tension entre le filet ($\rho=a$) et la règle ($\rho\approx r$) est

   $\displaystyle |V_0|=\int_a^rE_{\text{filet}}(\rho)\mkern3mu \mathrm{d}\rho=\frac{|\lambda|}{2\pi\varepsilon_0}\ln\frac ra,\qquad\text{donc}\qquad C_\ell=\frac{|\lambda|}{|V_0|}=\frac{2\pi\varepsilon_0}{\ln(r/a)}.$

   b) $\ln(r/a)=\ln20\approx3{,}0$, donc $C_\ell\approx1{,}9\times10^{-11}\ \mathrm{F\cdot m^{-1}}$ et $|\lambda|=C_\ell|V_0|\approx1{,}1\times10^{-7}\ \mathrm{C\cdot m^{-1}}$. Le champ propre du filet à la distance $r$ vaut $\dfrac{|\lambda|}{2\pi\varepsilon_0r}\approx\dfrac{1{,}1\times10^{-7}}{5{,}6\times10^{-11}\times0{,}02}\approx1\times10^{5}\ \mathrm{V\cdot m^{-1}}$ : c'est bien l'ordre de grandeur du champ de la règle, dont il compense l'effet à l'intérieur de l'eau. Le modèle est cohérent. On retrouve d'ailleurs $|\lambda|\approx2\pi\varepsilon_0Er$, c'est-à-dire la charge linéique $\Lambda$ de la règle de la question 1.

7. $F_\ell=|\lambda|E\approx1{,}1\times10^{-2}\ \mathrm{N\cdot m^{-1}}$. La masse linéique du filet est $\mu=\rho\pi a^2\approx3{,}1\times10^{-3}\ \mathrm{kg\cdot m^{-1}}$, donc<br>
   $\displaystyle a_{\text{ion}}=\frac{F_\ell}{\mu}=\frac{2\varepsilon_0rE^2}{\rho a^2}\approx3{,}5\ \mathrm{m\cdot s^{-2}},\qquad\Delta x_{\text{ion}}=3{,}5\times0{,}04\times0{,}12\approx1{,}7\ \mathrm{cm}.$
   
   C'est **le bon ordre de grandeur**, environ 400 fois la déviation dipolaire corrigée de la question 4. Le rapport des accélérations est, avec $a_{\text{dip}}=\dfrac{2\varepsilon_0}{\rho r}\dfrac{\varepsilon_r-1}{\varepsilon_r+1}E^2$ :
   $$\frac{a_{\text{ion}}}{a_{\text{dip}}}=\frac{\varepsilon_r+1}{\varepsilon_r-1}\left(\frac ra\right)^2\approx400,$$
   **indépendant de $E$** : les deux forces varient comme $E^2$, on ne peut donc pas les départager en changeant l'intensité du champ. Le facteur $(r/a)^2$ traduit la différence entre une charge nette, que le champ attire directement, et des dipôles neutres, sur lesquels il n'agit que par son gradient.

8. On peut isoler électriquement le filet de la terre (robinet en plastique, filet tombant dans un seau isolé) : sans possibilité d'écoulement des charges vers la terre, le filet ne peut plus s'électriser par influence et la déviation disparaît (ou s'affaiblit fortement). Plus directement, on **mesure la charge des gouttes** qui se détachent du filet, à l'aide d'une coupelle de Faraday reliée à un électroscope ou à un électromètre (influence totale). Les charges libres du filet sont celles de signe opposé à la règle : pour une règle chargée négativement, la règle attire les ions positifs vers le filet, et les gouttes emportent une charge **positive**.

</blockquote>
</details>

---

Cette expérience est détaillée, avec l'estimation du champ dépolarisant et le rôle de la charge des gouttes, dans la page [La déviation du filet d'eau](https://sciencesilencieuse.github.io/physique/electromag/filetdeau/).
