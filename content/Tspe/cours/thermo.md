+++
title = "Thermodynamique"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-ql-q { font-size: 1.05em; text-align: center; margin: 0.5em 0 0.7em !important; min-height: 1.6em; }
.nt-ql-btns { display: flex; flex-wrap: wrap; gap: 0.45em; justify-content: center; }
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
.nt-lab .nt-msg { margin-top: 1em !important; }
.nt-lab [hidden] { display: none !important; }
.nt-tr-ans { display: flex; align-items: center; justify-content: center; gap: 0.5em; flex-wrap: wrap; margin: 0.6em 0; }
.nt-champ { display: inline-flex; align-items: center; gap: 0.35em; white-space: nowrap; margin: 0 0.7em; }
.nt-champ label { display: inline; margin: 0; font-weight: 600; }
.nt-champ input[type="text"] { width: 5.5em !important; min-width: 0; margin: 0; padding: 0.25em 0.5em; text-align: right; font: inherit; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-champ .nt-u { color: var(--slate); }
.nt-figs { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8em; margin: 1em 0; }
.nt-figs figure { margin: 0; text-align: center; }
.nt-figs img, .nt-figs video { width: 100%; border-radius: 10px; }
.nt-figs figcaption { font-size: 0.88em; color: var(--muted); }
.nt-embed { position: relative; width: 100%; max-width: 760px; margin: 1em auto; aspect-ratio: 5 / 4; }
.nt-embed iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 10px; }
.nt-embed.nt-large { max-width: 900px; aspect-ratio: 16 / 10; }
.nt-embed.nt-bandeau { aspect-ratio: 16 / 8; }
.nt-h4 { font-size: 1.08em; font-weight: 700; color: var(--ink, #0F172A); margin: 1.6em 0 0.5em; padding-left: 0.6em; border-left: 4px solid #F97316; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">La thermodynamique est une branche de la physique développée au XIX<sup>e</sup> siècle, avec l'essor des machines à vapeur. Elle s'intéresse aux <b>conversions d'énergie</b> en lien avec la <b>température</b>&nbsp;: comment chauffer, refroidir, isoler, et finalement comprendre le climat de notre planète.</p>

## Le modèle du gaz parfait {.nt-h2}

<p class="nt-lead">L'état gazeux est <span class="imp nt-hole">dispersé</span> et <span class="imp nt-hole">désordonné</span>. À l'échelle microscopique, les entités qui le composent sont éloignées les unes des autres et ont un mouvement aléatoire incessant. Pour le décrire parfaitement, il faudrait connaître la masse, la position et la vitesse de chacune des milliards de milliards d'entités…</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Trois grandeurs macroscopiques</p>
<p>À l'échelle macroscopique, trois grandeurs <span class="imp nt-hole">intensives</span> (qui ne dépendent pas de la taille du système) suffisent à «&nbsp;moyenner&nbsp;» le chaos microscopique&nbsp;:</p>
<ul class="nt-facts">
<li>la <span class="imp">masse volumique</span> $\rho$, qui dit combien les entités sont serrées en moyenne&nbsp;;</li>
<li>la <span class="imp">pression</span> $P$, qui traduit la force moyenne par unité de surface due aux <span class="imp nt-hole">chocs</span> incessants des entités sur les parois&nbsp;;</li>
<li>la <span class="imp">température</span> $T$, qui mesure l'énergie cinétique moyenne des entités, c'est-à-dire leur <span class="imp nt-hole">agitation</span>.</li>
</ul>
</div>

<div class="nt-lab" id="lab-gaz">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Un gaz parfait vu de près</p>
<canvas style="height:270px;" aria-label="Des particules de gaz s'agitent dans une enceinte fermée par un piston ; un manomètre indique la pression"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Température&nbsp;: <b class="out-T"></b><input type="range" data-p="T" min="150" max="700" step="5" value="300"></label>
<label class="nt-ctrl">Volume&nbsp;: <b class="out-V"></b><input type="range" data-p="V" min="0.6" max="2" step="0.05" value="1"></label>
<label class="nt-ctrl">Quantité de matière&nbsp;: <b class="out-n"></b><input type="range" data-p="n" min="0.01" max="0.06" step="0.002" value="0.04"></label>
</div>
<div class="nt-read" aria-live="polite"><span>pression&nbsp;: <b class="out-P"></b></span></div>
<p class="nt-note">Chauffer le gaz agite davantage les particules&nbsp;: les chocs sont plus fréquents et plus violents, la pression augmente. Réduire le volume ou ajouter du gaz rend aussi les chocs plus fréquents. La pression affichée est calculée par la loi des gaz parfaits.</p>
</div>


<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Loi des gaz parfaits</p>
<p>Ces trois grandeurs sont liées par la <span class="imp nt-hole">loi des gaz parfaits</span>, $P = \dfrac{R}{M}\,\rho\, T$, où $M$ est la masse molaire du gaz. On lui préfère généralement la forme qui fait intervenir la quantité de matière $n$ et le volume $V$&nbsp;:</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi des gaz parfaits</p>
<p class="nt-f-math">$$PV = nRT$$</p>
<div class="nt-f-units"><span>$P$ en <b>Pa</b></span><span>$V$ en <b>m³</b></span><span>$n$ en <b>mol</b></span><span>$T$ en <b>K</b></span><span>$R$ = 8,314&nbsp;$\pu{Pa*m3*K-1*mol-1}$</span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Une pression est aussi une énergie par unité de volume&nbsp;: $\pu{1 Pa} = \pu{1 N*m-2} = \pu{1 J*m-3}$. La constante des gaz parfaits s'exprime donc aussi en $\pu{J*K-1*mol-1}$.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention aux unités</p>
<ul class="nt-facts">
<li>Le volume en <b>m³</b>&nbsp;: 1&nbsp;L = 10<sup>−3</sup>&nbsp;m³.</li>
<li>La température en <b>kelvins</b>&nbsp;: $T(\text{K}) = \theta(°\text{C}) + 273{,}15$. Quand la température est exprimée en degrés Celsius, l'usage est de la noter $\theta$ (thêta) plutôt que $T$, lettre réservée à la température absolue, en kelvins.</li>
<li>La pression en <b>pascals</b>&nbsp;: 1&nbsp;bar = 10<sup>5</sup>&nbsp;Pa, 1&nbsp;hPa = 100&nbsp;Pa.</li>
</ul>
</div>

<div class="nt-lab nt-trainer" id="lab-pv">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Entraînement</p>
<p class="nt-lab-title">Utiliser la loi des gaz parfaits</p>
<p class="nt-ql-q nt-tr-q"></p>
<div class="nt-tr-zone"><div class="nt-tr-ans"><span class="nt-champ"><label for="pv-rep">Réponse&nbsp;:</label><input id="pv-rep" type="text" inputmode="decimal"><span class="nt-u nt-tr-unit"></span></span><button type="button" class="nt-btn" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Valider</button></div></div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

### Les limites du modèle {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Le modèle du gaz parfait</p>
<p>Dans le modèle du <span class="imp">gaz parfait</span>, on néglige&nbsp;:</p>
<ul class="nt-facts">
<li>la <span class="imp nt-hole">taille des entités</span> devant la distance qui les sépare&nbsp;;</li>
<li>leurs <span class="imp nt-hole">interactions</span>.</li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Quand ces approximations deviennent-elles problématiques&nbsp;? Qu'en déduire pour l'air, dans les conditions ordinaires de température et de pression&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li>À <b>haute pression</b>, les entités sont si serrées que leur volume propre n'est plus négligeable.</li>
<li>À <b>basse température</b>, leur énergie cinétique devient du même ordre de grandeur que leur énergie d'interaction&nbsp;: le gaz est proche de se liquéfier.</li>
</ul>
<p>Le modèle du gaz parfait convient donc pour une pression pas trop grande ($P \lesssim 10$&nbsp;bar = 1&nbsp;MPa) et une température très supérieure à la température de liquéfaction du gaz. L'air se liquéfie vers −190&nbsp;°C sous 1&nbsp;bar&nbsp;: dans les conditions ordinaires, c'est un très bon gaz parfait.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Température et agitation moléculaire</span></summary>
<div class="nt-d-body">
<p>Pour un gaz parfait monoatomique, l'énergie cinétique moyenne d'une entité est directement proportionnelle à la température absolue&nbsp;: $\langle E_c \rangle = \dfrac{3}{2}\, k_B T$, où $k_B = \pu{1,38E-23 J*K-1}$ est la constante de Boltzmann. C'est ce qui donne un sens physique au zéro absolu&nbsp;: à $T$ = 0&nbsp;K, l'agitation thermique cesse.</p>
<p>La constante des gaz parfaits n'est autre que la constante de Boltzmann rapportée à une mole&nbsp;: $R = N_A\, k_B$. Dans l'air, à 20&nbsp;°C, les molécules de diazote filent en moyenne à environ 500&nbsp;m/s.</p>
</div>
</details>

## L'énergie interne {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp">énergie interne</span> $U$ d'un système est la somme des énergies <span class="imp nt-hole">cinétiques</span> (liées à l'agitation) et <span class="imp nt-hole">potentielles</span> (liées aux interactions) de l'ensemble des entités qui le composent, à l'échelle microscopique.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La variation d'énergie interne d'un <span class="imp nt-hole">système incompressible</span> (solide ou liquide) est proportionnelle à sa variation de température. Le coefficient de proportionnalité est la <span class="imp nt-hole">capacité thermique</span> $C$ du système. Pour caractériser un matériau indépendamment de sa masse, on utilise sa <span class="imp nt-hole">capacité thermique massique</span> $c$, avec $C = mc$.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Capacité thermique</p>
<p class="nt-f-math">$$\Delta U = C\,\Delta T$$</p>
<div class="nt-f-units"><span>$\Delta U$ en <b>J</b></span><span>$\Delta T$ en <b>K</b></span><span>$C$ en <b>$\pu{J*K-1}$</b></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Capacité thermique massique</p>
<p class="nt-f-math">$$\Delta U = m\,c\,\Delta T$$</p>
<div class="nt-f-units"><span>$m$ en <b>kg</b></span><span>$c$ en <b>$\pu{J*K-1*kg-1}$</b></span></div>
</div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Une variation de température a la même valeur en kelvins et en degrés Celsius&nbsp;: une hausse de 10&nbsp;°C est une hausse de 10&nbsp;K.</p>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Matériau</th><th>Capacité thermique massique ($\pu{J*kg-1*K-1}$)</th></tr></thead>
<tbody>
<tr><td>eau liquide</td><td>4&nbsp;185</td></tr>
<tr><td>glace (à 0&nbsp;°C)</td><td>2&nbsp;100</td></tr>
<tr><td>huile végétale</td><td>2&nbsp;000</td></tr>
<tr><td>aluminium</td><td>897</td></tr>
<tr><td>brique</td><td>840</td></tr>
<tr><td>acier</td><td>450 à 500</td></tr>
</tbody>
</table>
</div>

<div class="nt-lab" id="lab-cap">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Même énergie, températures différentes</p>
<canvas style="height:300px;" aria-label="Température de 1 kg de différents matériaux, chauffés avec la même puissance de 1 kW"></canvas>
<div class="nt-read" aria-live="polite"><span>durée de chauffage&nbsp;: <b class="out-t"></b></span><span>énergie reçue par chacun&nbsp;: <b class="out-Q"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-fire"></i>&nbsp; Chauffer</button></div>
<p class="nt-note">Chaque échantillon a une masse de 1&nbsp;kg, part de 20&nbsp;°C et reçoit la même puissance, 1&nbsp;kW. On a $\Delta T = \dfrac{Q}{mc}$&nbsp;: plus la capacité thermique est grande, plus la température monte lentement.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Plus la capacité thermique d'un corps est grande, plus il est facile ou difficile de modifier sa température&nbsp;? Pourquoi les régions côtières ont-elles des hivers plus doux et des étés moins chauds que l'intérieur des terres&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Plus la capacité thermique est grande, plus il est <b>difficile</b> de modifier sa température&nbsp;: il faut beaucoup d'énergie pour la faire varier. L'eau, avec sa très grande capacité thermique, joue le rôle de régulateur&nbsp;: l'océan se réchauffe lentement en été et se refroidit lentement en hiver, ce qui adoucit le climat des côtes.</p>
</div>
</details>

## Le premier principe de la thermodynamique {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Énergie totale</p>
<p>L'<span class="imp">énergie totale</span> d'un système est la somme de son <span class="imp nt-hole">énergie mécanique</span> et de son <span class="imp nt-hole">énergie interne</span>&nbsp;: $E_\text{tot} = E_m + U$.</p>
</div>

<p class="nt-lead">L'énergie d'un système <b>fermé</b> (qui n'échange pas de matière avec l'extérieur) peut varier par échange d'énergie avec l'extérieur, sous deux formes&nbsp;:</p>
<ul class="nt-facts">
<li>le <span class="imp nt-hole">travail</span> $W$ des forces non conservatives (forces de pression, travail électrique…)&nbsp;;</li>
<li>le <span class="imp nt-hole">transfert thermique</span> $Q$.</li>
</ul>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Premier principe de la thermodynamique</p>
<p class="nt-f-math">$$\Delta E_\text{tot} = W + Q$$</p>
<div class="nt-f-units"><span>pour un système <b>fermé</b>&nbsp;; toutes les grandeurs en <b>J</b></span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Système immobile</p>
<p>Si le système est <span class="imp nt-hole">immobile</span> (au repos macroscopique), son énergie mécanique est constante&nbsp;: $\Delta E_\text{tot} = \cancel{\Delta E_m} + \Delta U$, et le premier principe s'écrit</p>
<p class="nt-center">$\Delta U = W + Q$</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Un raccourci à manier avec précaution&nbsp;: $Q = C\,\Delta T$</p>
<p>On rencontre souvent, pour un système incompressible, la formule $Q = C\,\Delta T$. Elle est pratique, mais conceptuellement fausse en tant que définition de $Q$&nbsp;:</p>
<ul class="nt-facts">
<li>$C\,\Delta T$ renseigne sur la <b>variation d'énergie interne</b> du système&nbsp;: $\Delta U = C\,\Delta T$. C'est ce qui change <b>à l'intérieur</b> du système.</li>
<li>$Q$ est un <b>transfert</b>&nbsp;: c'est ce que le système <b>échange</b> avec l'extérieur.</li>
</ul>
<p>Le lien entre les deux, c'est le premier principe&nbsp;: $\Delta U = W + Q$. Lorsque le système, immobile, ne reçoit aucun travail ($W = 0$), on a bien $\Delta U = Q$, et donc $Q = C\,\Delta T$. Le raccourci n'est valable <b>que dans ce cas</b>.</p>
<p>Contre-exemple&nbsp;: de l'eau chauffée par une résistance électrique plongée dedans. Pour le système {eau + résistance}, l'énergie entre sous forme de <b>travail électrique</b>&nbsp;: $W > 0$, alors que $Q$ est nul (ou même négatif, à cause des pertes vers l'air). La température monte pourtant&nbsp;: $\Delta U = C\,\Delta T > 0$ n'est pas égal à $Q$.</p>
<p class="nt-note">Ce raccourci est toléré, voire utilisé dans certains sujets du baccalauréat, comme s'il s'agissait d'une formule pour $Q$. Mieux vaut pourtant écrire les deux étapes, $\Delta U = C\,\Delta T$ puis $\Delta U = Q$ (car $W = 0$)&nbsp;: c'est plus juste, et cela garde clair le message du premier principe, qui distingue ce qui varie dans le système de ce qu'il échange.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Convention de signe</p>
<p>Les transferts d'énergie sont comptés <span class="imp nt-hole">positivement</span> lorsqu'ils <b>entrent</b> dans le système (de l'extérieur vers le système), et <span class="imp nt-hole">négativement</span> lorsqu'ils en <b>sortent</b>. Un système <b>isolé</b> n'échange ni matière ni énergie&nbsp;: $W = Q = 0$, et son énergie totale se conserve.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple&nbsp;: la bouilloire électrique</p>
<ul class="nt-facts">
<li>Système {résistance chauffante}&nbsp;: le travail électrique $W$ reçu est positif&nbsp;; le transfert thermique $Q$ cédé à l'eau est négatif.</li>
<li>Système {eau}&nbsp;: il n'y a plus de travail, mais deux transferts thermiques&nbsp;: $Q_r$ reçu de la résistance, positif, et $Q_e$ cédé à l'air extérieur, négatif.</li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Rien n'empêche que tous les transferts soient positifs, ou tous négatifs. Trouver un exemple.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir des exemples</span></summary>
<div class="nt-d-body">
<p>Un gaz dans une seringue que l'on comprime (W &gt; 0) tout en la plongeant dans de l'eau chaude (Q &gt; 0)&nbsp;: tous les transferts sont positifs. À l'inverse, un gaz chaud qui se détend en repoussant un piston (W &lt; 0) tout en refroidissant au contact de l'air (Q &lt; 0)&nbsp;: tous sont négatifs.</p>
</div>
</details>

<div class="nt-lab nt-quizlab" id="quiz-signes">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Le signe des transferts d'énergie</p>
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

## Les modes de transfert thermique {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Il existe trois modes de transfert thermique&nbsp;: la <span class="imp nt-hole">conduction</span>, la <span class="imp nt-hole">convection</span> et le <span class="imp nt-hole">rayonnement</span>.</p>
</div>

<div class="nt-lab" id="lab-modes">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Trois façons de transférer de l'énergie</p>
<div class="nt-ctrl">
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="tmode" value="cond" checked><span>conduction</span></label>
<label><input type="radio" name="tmode" value="conv"><span>convection</span></label>
<label><input type="radio" name="tmode" value="ray"><span>rayonnement</span></label>
</div>
</div>
<canvas style="height:280px;" aria-label="Les trois modes de transfert thermique vus à l'échelle microscopique"></canvas>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### La conduction {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un transfert thermique par <span class="imp">conduction</span> est dû à la <span class="imp nt-hole">diffusion de l'agitation thermique</span> dans la matière. Il a lieu <span class="imp nt-hole">de proche en proche</span>, <b>sans déplacement macroscopique de matière</b>&nbsp;: l'agitation des entités est communiquée de l'une à l'autre.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Aérogel de silice, polystyrène expansé, laine de roche, laine de verre, liège expansé, ouate de cellulose… Qu'ont en commun les meilleurs isolants thermiques&nbsp;?</p>
</div>

<div style="position:relative;margin-left:auto;margin-right:auto;width:300px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Aerogel_matches.jpg" style="box-shadow:none;background:none;border-radius:5px;">
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Ils emprisonnent tous de l'<b>air</b>, dans des pores, des bulles ou entre des fibres. Un gaz conduit très mal la chaleur, car ses entités sont éloignées les unes des autres. Et comme l'air est bloqué dans de minuscules cavités, il ne peut pas non plus transporter la chaleur par convection.</p>
</div>
</details>


### La convection {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un transfert thermique par <span class="imp">convection</span> ne peut avoir lieu que dans un <span class="imp nt-hole">fluide</span>. Il correspond à un <span class="imp nt-hole">mouvement macroscopique de matière</span>&nbsp;: le fluide est animé d'un mouvement d'ensemble.</p>
</div>

<div class="nt-figs" style="grid-template-columns: minmax(200px, 340px); justify-content: center;">
<figure><video src="https://coursphychi.github.io/convection.mp4" autoplay loop muted playsinline preload="metadata"></video></figure>
</div>


<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Comment expliquer ce mouvement d'ensemble du fluide&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Le fluide chauffé se dilate&nbsp;: il devient moins dense que le fluide froid qui l'entoure. Il s'élève alors sous l'effet de la poussée d'Archimède, et il est remplacé par du fluide plus froid, qui à son tour se réchauffe et monte. Une circulation s'installe.</p>
</div>
</details>



<div class="nt-figs" style="grid-template-columns: minmax(240px, 800px); justify-content: center;">
<figure><img src="https://coursphychi.github.io/heatsinks.png" alt="Des pièces métalliques munies de nombreuses ailettes" loading="lazy" style="margin-top:0;margin-bottom:0;"></figure>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Qu'est-ce que c'est&nbsp;? Discuter le matériau, la forme et l'orientation de ces objets.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Ce sont des <b>dissipateurs thermiques</b> (on dit aussi, paradoxalement, des radiateurs), qui évacuent la chaleur d'un processeur ou d'un composant électronique.</p>
<ul class="nt-facts">
<li><b>Le matériau</b>&nbsp;: un métal bon conducteur (aluminium, cuivre), pour conduire rapidement la chaleur du composant jusqu'aux ailettes.</li>
<li><b>La forme</b>&nbsp;: de nombreuses ailettes fines, pour augmenter la surface d'échange avec l'air.</li>
<li><b>L'orientation</b>&nbsp;: des ailettes verticales, pour que l'air réchauffé puisse monter librement entre elles (convection naturelle).</li>
</ul>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Petite énigme</p>
<p>Pourquoi un glaçon fond-il moins vite dans de l'eau salée que dans de l'eau douce&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>C'est une question de convection. En fondant, le glaçon libère de l'eau douce et froide.</p>
<ul class="nt-facts">
<li>Dans l'<b>eau douce</b>, cette eau froide est plus dense que l'eau tiède qui l'entoure&nbsp;: elle coule au fond et est remplacée par de l'eau tiède, qui continue de faire fondre le glaçon.</li>
<li>Dans l'<b>eau salée</b>, l'eau de fonte, douce, est moins dense que l'eau salée&nbsp;: elle reste en surface, autour du glaçon, et forme une couche froide qui l'isole. La convection est bloquée, et le glaçon fond surtout par conduction, beaucoup plus lente.</li>
</ul>
</div>
</details>

### Le rayonnement {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le transfert thermique par <span class="imp">rayonnement</span> est le seul à pouvoir se faire dans le <span class="imp nt-hole">vide</span>. Il correspond à l'<span class="imp nt-hole">émission ou l'absorption d'ondes électromagnétiques</span>.</p>
</div>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 520px); justify-content: center;">
<figure><img src="https://upload.wikimedia.org/wikipedia/commons/f/f8/RescueFoil.jpg" alt="Une couverture de survie dorée et argentée" loading="lazy" style="margin-top:0em;margin-bottom:0em;"></figure>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Comment fonctionne une couverture de survie&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>C'est une fine feuille de plastique recouverte d'une couche métallique (de l'aluminium) très réfléchissante. Elle <b>renvoie le rayonnement</b> au lieu de le laisser passer&nbsp;: elle limite les échanges par rayonnement. Elle limite aussi les pertes par convection en bloquant l'air autour du corps. Elle a été développée par la NASA dans les années 1960, pour l'isolation des engins spatiaux.</p>
<p>Ses deux faces sont métallisées&nbsp;; la face dorée est simplement recouverte d'un vernis coloré. La face <b>argentée</b>, nue, réfléchit un peu mieux le rayonnement&nbsp;: on la tourne vers ce que l'on veut renvoyer.</p>
<ul class="nt-facts">
<li><b>Contre le froid</b> (hypothermie)&nbsp;: face argentée <b>vers le corps</b>, pour renvoyer vers lui l'infrarouge qu'il émet&nbsp;; la face dorée, à l'extérieur, rend en outre la victime plus visible pour les secours.</li>
<li><b>Contre la chaleur</b> (coup de chaleur, insolation)&nbsp;: face argentée <b>vers l'extérieur</b>, pour réfléchir le rayonnement solaire.</li>
</ul>
<p class="nt-note">L'écart entre les deux faces reste modeste&nbsp;: l'essentiel de l'effet vient de la couche métallique, et du fait que la couverture entoure bien le corps.</p>
</div>
</details>

{{< youtube-plus id="Pp9Yax8UNoM" ratio="4x3" width="700" shadow=true rounded=true >}}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Comment expliquer ce que l'on voit dans cette vidéo&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Ce matériau est un excellent isolant&nbsp;: la conduction de la chaleur, du centre vers les bords, est très faible. Elle ne parvient pas à compenser les pertes par rayonnement, qui se font par toute la surface. Résultat&nbsp;: les coins et les bords refroidissent très vite, jusqu'à pouvoir être tenus à la main (vers 35&nbsp;°C), alors que le centre est encore à plus de 1&nbsp;200&nbsp;°C&nbsp;!</p>
</div>
</details>

<div class="nt-lab nt-quizlab" id="quiz-modes">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Quel mode de transfert thermique&nbsp;?</p>
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

## Le flux thermique {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp">flux thermique</span> $\Phi$ est la <span class="imp nt-hole">puissance</span> qui traverse une surface au cours d'un transfert thermique&nbsp;: c'est l'énergie thermique $Q$ transférée par unité de temps.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Flux thermique</p>
<p class="nt-f-math">$$\Phi = \frac{Q}{\Delta t}$$</p>
<div class="nt-f-units"><span>$Q$ en <b>J</b></span><span>$\Delta t$ en <b>s</b></span><span>$\Phi$ en <b>W</b></span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Comme le transfert thermique $Q$ et le travail $W$, le flux thermique $\Phi$ est compté positivement s'il entre dans le système, et négativement s'il en sort.</p>
</div>

## La résistance thermique {.nt-h2}

<svg class='nt-svg nt-svg-m' viewBox='0 0 520 230' role='img' aria-label="Un flux thermique traverse une paroi de résistance thermique Rth, de la face chaude à la température Tc vers la face froide à la température Tf"><defs><linearGradient id='gPar' x1='0' x2='1'><stop offset='0' stop-color='#FCA5A5'/><stop offset='1' stop-color='#93C5FD'/></linearGradient><linearGradient id='gFlu' x1='0' x2='1'><stop offset='0' stop-color='#DC2626'/><stop offset='1' stop-color='#F97316'/></linearGradient><clipPath id='cSortie'><rect x='336' y='0' width='200' height='230'/></clipPath></defs><path d='M40,108 L420,108 L420,90 L470,120 L420,150 L420,132 L40,132 Z' fill='url(#gFlu)' fill-opacity='.9'/><rect x='200' y='40' width='110' height='160' fill='url(#gPar)' fill-opacity='.78' stroke='#64748B'/><path d='M310,40 L360,20 L360,180 L310,200 Z' fill='#BFDBFE' fill-opacity='.8' stroke='#64748B'/><path d='M200,40 L250,20 L360,20 L310,40 Z' fill='#E2E8F0' stroke='#64748B'/><ellipse cx='336' cy='120' rx='5' ry='13' fill='#EA580C' fill-opacity='.55'/><path d='M40,108 L420,108 L420,90 L470,120 L420,150 L420,132 L40,132 Z' fill='url(#gFlu)' fill-opacity='.95' clip-path='url(#cSortie)'/><text x='255' y='70' font-size='17' text-anchor='middle' fill='#1E293B' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>R</tspan><tspan font-size='11' dy='4'>th</tspan></text><text x='70' y='88' font-size='18' text-anchor='middle' fill='#DC2626' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>T</tspan><tspan font-size='12' dy='4'>c</tspan></text><text x='70' y='160' font-size='12' text-anchor='middle' fill='#B91C1C' font-family='system-ui, sans-serif'>côté chaud</text><text x='405' y='80' font-size='18' text-anchor='middle' fill='#2563EB' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>T</tspan><tspan font-size='12' dy='4'>f</tspan></text><text x='405' y='178' font-size='12' text-anchor='middle' fill='#1D4ED8' font-family='system-ui, sans-serif'>côté froid</text><text x='445' y='126' font-size='18' text-anchor='middle' fill='#fff' font-family='Georgia, serif' font-weight='700'>Φ</text></svg>

<p class="nt-lead">À travers un milieu limité par deux surfaces aux températures $T_c$ et $T_f$ (avec $T_c > T_f$), le flux thermique par conduction ou convection va toujours de la surface <b>chaude</b> vers la surface <b>froide</b>.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">résistance thermique</span> $R_\text{th}$ traduit l'aptitude d'un milieu à <span class="imp nt-hole">s'opposer au passage du flux thermique</span>&nbsp;:</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Résistance thermique</p>
<p class="nt-f-math">$$R_\text{th} = \frac{\Delta T}{\Phi} = \frac{T_c - T_f}{\Phi}$$</p>
<div class="nt-f-units"><span>$\Delta T$ en <b>K</b></span><span>$\Phi$ en <b>W</b></span><span>$R_\text{th}$ en <b>$\pu{K*W-1}$</b></span></div>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Analogie électrique</p>
<p>Cette relation a la même forme que la loi d'Ohm, $U = RI$&nbsp;:</p>
<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Thermique</th><th>Électricité</th></tr></thead>
<tbody>
<tr><td>résistance thermique $R_\text{th}$</td><td>résistance électrique $R$</td></tr>
<tr><td>flux thermique $\Phi$</td><td>intensité $I$</td></tr>
<tr><td>écart de température $\Delta T$</td><td>tension $U$</td></tr>
</tbody>
</table>
</div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pour un même écart de température, plus la résistance thermique du milieu est grande, plus le flux thermique est grand ou faible&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Plus <b>faible</b>&nbsp;: $\Phi = \dfrac{\Delta T}{R_\text{th}}$. Un bon isolant a une grande résistance thermique.</p>
</div>
</details>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Conduction à travers une paroi plane</p>
<p class="nt-f-math">$$R_\text{th cond} = \frac{e}{\lambda S}$$</p>
<div class="nt-f-units"><span>$e$, l'épaisseur, en <b>m</b></span><span>$S$ en <b>m²</b></span><span>$\lambda$, la conductivité thermique, en <b>$\pu{W*m-1*K-1}$</b></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Contact avec un fluide (conducto-convectif)</p>
<p class="nt-f-math">$$R_\text{th cv} = \frac{1}{hS}$$</p>
<div class="nt-f-units"><span>$h$, le coefficient d'échange, en <b>$\pu{W*m-2*K-1}$</b></span></div>
</div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Les expressions de $R_\text{th cond}$ et de $R_\text{th cv}$ sont toujours fournies. Il faut en revanche savoir que des résistances thermiques <span class="imp nt-hole">en série s'additionnent</span>, comme des résistances électriques.</p>
</div>

<div class="nt-lab" id="lab-mur">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Isoler un mur&nbsp;: des résistances thermiques en série</p>
<div class="nt-ctrl">Isolant&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="iso" value="laine" checked><span>laine de verre</span></label>
<label><input type="radio" name="iso" value="poly"><span>polystyrène</span></label>
<label><input type="radio" name="iso" value="liege"><span>liège</span></label>
</div>
</div>
<canvas style="height:330px;" aria-label="Coupe d'un mur multicouche, avec le profil de température et le flux thermique qui le traverse"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Épaisseur d'isolant&nbsp;: <b class="out-e"></b><input type="range" data-p="e" min="0" max="300" step="10" value="100"></label>
<label class="nt-ctrl">Température extérieure&nbsp;: <b class="out-Te"></b><input type="range" data-p="Te" min="-10" max="15" step="1" value="0"></label>
</div>
<div class="nt-read" aria-live="polite"><span>R<sub>th</sub> totale&nbsp;: <b class="out-R"></b></span><span>flux thermique&nbsp;: <b class="out-F"></b></span></div>
<p class="nt-note">Mur de 10&nbsp;m², pièce à 19&nbsp;°C. De l'intérieur vers l'extérieur&nbsp;: air intérieur ($h$ = 8&nbsp;$\pu{W*m-2*K-1}$), plâtre (13&nbsp;mm), isolant, parpaing (20&nbsp;cm), air extérieur ($h$ = 25&nbsp;$\pu{W*m-2*K-1}$). La température chute dans chaque couche proportionnellement à sa résistance&nbsp;: presque toute la chute se fait dans l'isolant. Retirez l'isolant pour voir l'effet sur le flux&nbsp;!</p>
</div>

## Évolution temporelle de la température {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Loi phénoménologique de Newton</p>
<p>La <span class="imp">loi de Newton</span> (ou loi du refroidissement de Newton) modélise le transfert thermique par conduction et convection entre un système et le milieu extérieur. Le flux thermique reçu par le système est <span class="imp nt-hole">proportionnel à l'écart de température</span> entre le milieu extérieur et le système&nbsp;:</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi de Newton</p>
<p class="nt-f-math">$$\Phi = hS\left(T_\text{ext} - T\right)$$</p>
<div class="nt-f-units"><span>$T$, la température du système</span><span>$S$, la surface d'échange, en <b>m²</b></span><span>$h$ en <b>$\pu{W*m-2*K-1}$</b></span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarques</p>
<ul class="nt-facts">
<li>Cette formule, ou une formule semblable, est toujours fournie. Elle revient à utiliser la résistance conducto-convective $R_\text{th cv} = \dfrac{1}{hS}$.</li>
<li>Un système dont la température peut être considérée comme constante (parce qu'il est très grand, par exemple) est appelé un <span class="imp nt-hole">thermostat</span>. On considère très souvent le milieu extérieur comme un thermostat&nbsp;: $T_\text{ext}$ = constante.</li>
</ul>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Démonstration&nbsp;: l'équation différentielle</p>
<p>On étudie un système incompressible, immobile, qui ne reçoit aucun travail, en contact avec un thermostat. Bilan d'énergie entre les instants $t$ et $t + \Delta t$&nbsp;:</p>
<ol class="nt-steps">
<li><p>Premier principe&nbsp;: $\cancel{\Delta E_m} + \Delta U = \cancel{W} + Q$.<br>
Donc ${\color{#017100} \Delta U} = {\color{#B51700} Q}$.</p></li>
<li><p>Système incompressible&nbsp;: $\color{#017100} \Delta U = mc\,\Delta T$.</p></li>
<li><p>Transfert thermique pendant $\Delta t$&nbsp;: $\color{#B51700}Q = \Phi\,\Delta t =hS\left(T_\text{ext} - T(t)\right)\Delta t$.<br>
Où on a utilisé la loi de Newton, $\Phi=hS\left(T_\mathrm{ext}-T\right)$.</p></li>
<li><p>On égale les deux expressions et on divise par $\Delta t$&nbsp;: $mc\,\dfrac{\Delta T}{\Delta t} = hS\,T_\text{ext} - hS\,T(t)$.</p></li>
<li><p>On fait tendre $\Delta t$ vers 0&nbsp;: $\dfrac{\Delta T}{\Delta t} \to \dfrac{\mathrm{d}T}{\mathrm{d}t}$, d'où</p>
<p class="nt-center">$\dfrac{\mathrm{d}T}{\mathrm{d}t} + \dfrac{1}{\tau}\,T(t) = \dfrac{1}{\tau}\,T_\text{ext}$, avec $\tau = \dfrac{mc}{hS}$.</p></li>
</ol>
<p>On reconnaît une équation différentielle du premier ordre, à coefficients constants, avec second membre. $\tau$ est le <b>temps caractéristique</b> de l'évolution.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Solution</p>
<p class="nt-f-math">$$T(t) = \left(T_0 - T_\text{ext}\right)\mathrm{e}^{-t/\tau} + T_\text{ext}$$</p>
<div class="nt-f-units"><span>$T_0 = T(0)$, la température initiale</span><span>$\tau = \dfrac{mc}{hS}$ en <b>s</b></span></div>
</div>

<div class="nt-lab" id="lab-newton">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Une tasse de thé qui refroidit… ou qui se réchauffe</p>
<canvas style="height:300px;" aria-label="Température d'une tasse de thé en fonction du temps, avec la constante de temps et l'équilibre thermique"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Masse de thé&nbsp;: <b class="out-m"></b><input type="range" data-p="m" min="0.1" max="1" step="0.05" value="0.25"></label>
<label class="nt-ctrl">Coefficient d'échange $h$&nbsp;: <b class="out-h"></b><input type="range" data-p="h" min="4" max="40" step="1" value="10"></label>
<label class="nt-ctrl">Température initiale&nbsp;: <b class="out-T0"></b><input type="range" data-p="T0" min="2" max="95" step="1" value="85"></label>
<label class="nt-ctrl">Température ambiante&nbsp;: <b class="out-Te"></b><input type="range" data-p="Te" min="0" max="30" step="1" value="20"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$\tau = \dfrac{mc}{hS}$ = <b class="out-tau"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-preset="85,20"><i class="fa-solid fa-mug-hot"></i>&nbsp; Thé chaud</button>
<button type="button" class="nt-btn" data-preset="4,25"><i class="fa-solid fa-glass-water"></i>&nbsp; Thé glacé</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-play"></i>&nbsp; Lancer</button>
</div>
<p class="nt-note">Surface d'échange $S$ = 0,03&nbsp;m², eau ($c$ = 4&nbsp;185&nbsp;$\pu{J*kg-1*K-1}$). La tangente à l'origine coupe l'asymptote à $t = \tau$&nbsp;; à cet instant, la température a parcouru 63&nbsp;% de l'écart initial. Avec le thé glacé, la température initiale est inférieure à la température ambiante&nbsp;: le thé se réchauffe, et la même loi s'applique.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Si $T_0 < T_\text{ext}$, $T(t)$ est <span class="imp nt-hole">croissante</span>&nbsp;: le système se réchauffe. Si $T_0 > T_\text{ext}$, $T(t)$ est <span class="imp nt-hole">décroissante</span>&nbsp;: le système se refroidit.</li>
<li>Dans tous les cas, quand $t \to \infty$ (en pratique, pour $t > 5\tau$), le système atteint la température du thermostat&nbsp;: c'est l'<span class="imp nt-hole">équilibre thermique</span>.</li>
</ul>
</div>


## Bilan thermique du système &#123;Terre, atmosphère&#125; {.nt-h2}

<svg class='nt-svg nt-svg-m' viewBox='0 0 560 230' role='img' aria-label="Le système Terre et atmosphère reçoit de l'énergie du Soleil par rayonnement, transfert compté positivement, et en perd vers l'espace par rayonnement, transfert compté négativement"><defs><radialGradient id='gSol' cx='.5' cy='.5' r='.5'><stop offset='0' stop-color='#FEF9C3'/><stop offset='1' stop-color='#F59E0B'/></radialGradient><radialGradient id='gTer' cx='.4' cy='.35' r='.7'><stop offset='0' stop-color='#93C5FD'/><stop offset='1' stop-color='#1D4ED8'/></radialGradient></defs><rect width='560' height='230' rx='12' fill='#0F172A'/><circle cx='70' cy='115' r='48' fill='url(#gSol)'/><circle cx='360' cy='115' r='84' fill='rgba(147,197,253,.25)'/><circle cx='360' cy='115' r='74' fill='url(#gTer)'/><path d='M330,70 q20,-14 40,0 q16,10 6,24 q-20,8 -34,-4 z M350,130 q24,-6 30,10 q4,22 -20,26 q-18,-8 -10,-36 z' fill='#22C55E' opacity='.85'/><path d='M130,115 L250,115 L250,100 L280,120 L250,140 L250,125 L130,125 Z' fill='#F97316'/><text x='190' y='98' font-size='15' text-anchor='middle' fill='#FED7AA' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>Q</tspan> &gt; 0</text><g transform='translate(428,160) rotate(32)'><path d='M0,-6 L78,-6 L78,-18 L106,0 L78,18 L78,6 L0,6 Z' fill='#60A5FA'/></g><text x='500' y='158' font-size='15' text-anchor='middle' fill='#BFDBFE' font-family='Georgia, serif' font-weight='700'><tspan font-style='italic'>Q</tspan> &lt; 0</text><text x='70' y='190' font-size='12' text-anchor='middle' fill='#FDE68A' font-family='system-ui, sans-serif' font-weight='700'>Soleil</text><text x='360' y='222' font-size='12' text-anchor='middle' fill='#BFDBFE' font-family='system-ui, sans-serif' font-weight='700'>système {Terre, atmosphère}</text><text x='520' y='40' font-size='12' text-anchor='end' fill='#94A3B8' font-family='system-ui, sans-serif'>espace</text></svg>

<p class="nt-lead">Le système {Terre, atmosphère} <b>reçoit</b> de l'énergie par transfert thermique radiatif du Soleil, et en <b>perd</b> par transfert thermique radiatif vers l'espace. Il y a donc un flux entrant, positif, $\Phi_\text{entrant}$, et un flux sortant, négatif, $\Phi_\text{sortant}$. Plutôt que le flux total $\Phi$, on raisonne sur le <b>flux surfacique</b> $\varphi$, le flux par mètre carré.</p>

### L'albédo {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Albédo</p>
<p>Une partie du flux solaire entrant est directement renvoyée vers l'espace, par les nuages et par le sol selon sa nature. L'<span class="imp">albédo</span> $A$ est le rapport entre ce flux diffusé $\varphi_D$ et le flux entrant&nbsp;: $A = \dfrac{\varphi_D}{\varphi_\text{entrant}}$.</p>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Type de surface</th><th>Albédo</th></tr></thead>
<tbody>
<tr><td>corps noir parfait</td><td>0</td></tr>
<tr><td>surface d'un lac</td><td>0,02 à 0,04</td></tr>
<tr><td>forêt de conifères</td><td>0,05 à 0,15</td></tr>
<tr><td>surface de la mer</td><td>0,05 à 0,15</td></tr>
<tr><td>forêt de feuillus</td><td>0,15 à 0,20</td></tr>
<tr><td>cultures</td><td>0,15 à 0,25</td></tr>
<tr><td>sable léger et sec</td><td>0,25 à 0,45</td></tr>
<tr><td>calcaire</td><td>0,40 environ</td></tr>
<tr><td>nuage</td><td>0,50 à 0,80</td></tr>
<tr><td>glace</td><td>0,60 environ</td></tr>
<tr><td>neige tassée</td><td>0,40 à 0,70</td></tr>
<tr><td>neige fraîche</td><td>0,75 à 0,90</td></tr>
<tr><td>miroir parfait</td><td>1</td></tr>
</tbody>
</table>
</div>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 520px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/albedofeuille.jpeg" alt="Une feuille morte posée sur de la glace a creusé sa forme en faisant fondre la glace sous elle" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>une feuille sombre, d'albédo faible, absorbe davantage le rayonnement solaire que la glace qui l'entoure&nbsp;: elle s'échauffe et s'y enfonce</figcaption></figure>
</div>

<p class="nt-lead">Grâce à sa couverture nuageuse, l'albédo de la Terre est relativement élevé, de l'ordre de 30&nbsp;%, quand celui de la Lune ne vaut que 7&nbsp;%. La carte animée suivante, réalisée à partir des données du projet CERES de la NASA, montre le rayonnement solaire directement renvoyé vers l'espace.</p>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 760px); justify-content: center;">
<figure><video src="https://upload.wikimedia.org/wikipedia/commons/transcoded/b/b9/NPP_Ceres_Shortwave_Radiation.ogv/NPP_Ceres_Shortwave_Radiation.ogv.1080p.vp9.webm" autoplay loop muted playsinline preload="metadata"></video></figure>
</div>

### Le rayonnement de la Terre et l'effet de serre {.nt-h3}

<p class="nt-lead">Ce rayonnement réfléchi ne représente qu'une partie du flux sortant&nbsp;: il en manque beaucoup pour équilibrer le flux solaire entrant, $\varphi_\text{entrant} = \pu{340,4 W*m-2}$. D'où vient le reste&nbsp;? Du rayonnement de la Terre elle-même&nbsp;!</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Loi de Stefan-Boltzmann</p>
<p>Tout corps à la température $T$ émet un rayonnement électromagnétique, dont le flux thermique surfacique vaut $\varphi = \sigma T^4$.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Au bac, la loi de Stefan-Boltzmann sera toujours donnée.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi de Stefan-Boltzmann</p>
<p class="nt-f-math">$$\varphi = \sigma T^4$$</p>
<div class="nt-f-units"><span>$\varphi$ en <b>$\pu{W*m-2}$</b></span><span>$T$ en <b>K</b></span><span>$\sigma = \pu{5,67E-8 W*m-2*K-4}$, la constante de Stefan-Boltzmann</span></div>
</div>

<div class="nt-embed nt-large"><iframe src="https://presentationssite.github.io/spectre_corps_noir.html" title="Spectre du rayonnement d'un corps noir selon sa température" loading="lazy"></iframe></div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>L'effet de serre</p>
<p>Le Soleil rayonne surtout dans le visible, alors que la Terre émet dans l'<span class="imp nt-hole">infrarouge</span>, autour de 10&nbsp;µm. Or certains gaz de l'atmosphère ($\ce{CO2}$, $\ce{H2O}$, $\ce{CH4}$…) absorbent l'infrarouge (voir la spectroscopie infrarouge). Ce rayonnement absorbé est réémis dans toutes les directions, donc pour moitié vers la surface.</p>
<p>Il est alors plus difficile pour la Terre d'évacuer son énergie&nbsp;: c'est l'<span class="imp nt-hole">effet de serre</span>. La surface se réchauffe jusqu'à ce que le flux sortant redevienne suffisant pour équilibrer le flux entrant.</p>
</div>

#### Le réchauffement climatique {.nt-h4}

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Un équilibre déplacé</p>
<p>L'augmentation de la concentration des gaz à effet de serre dans l'atmosphère déplace à nouveau l'équilibre. Le déséquilibre $\varphi_\text{entrant} > \varphi_\text{sortant}$ entraîne une hausse de la température de surface, qui augmente à son tour $\varphi_\text{sortant}$, jusqu'au retour à l'équilibre. Le déséquilibre par rapport à l'année de référence préindustrielle (1750) est appelé <span class="imp nt-hole">forçage radiatif</span>&nbsp;: il dépasse aujourd'hui $\pu{3,0 W*m-2}$.</p>
</div>


<p class="nt-center"><a href="https://climatechangetracker.org/global-warming" target="_blank" rel="noopener"><i class="fa-solid fa-gauge-high"></i>&nbsp; Tableau de bord interactif du réchauffement climatique</a></p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Une tendance de fond, des fluctuations naturelles</span></summary>
<div class="nt-d-body">
<p>Le forçage radiatif dû aux gaz à effet de serre augmente régulièrement, au rythme de nos émissions. Mais le déséquilibre énergétique que l'on mesure n'augmente pas de façon parfaitement régulière&nbsp;: il est soumis à une <b>variabilité naturelle</b>, d'une année à l'autre.</p>
<ul class="nt-facts">
<li><b>El Niño et La Niña.</b> Ces phénomènes du Pacifique tropical font alterner, tous les 2 à 7 ans environ, des phases où l'océan libère de la chaleur vers l'atmosphère (El Niño&nbsp;: les températures de surface montent nettement, comme en 1998, 2016 ou 2023-2024) et des phases où il en stocke davantage (La Niña). Ces échanges d'énergie entre l'océan et l'atmosphère font fluctuer la température mondiale et le déséquilibre mesuré, autour de la tendance de fond.</li>
<li><b>Les grandes éruptions volcaniques.</b> Elles peuvent produire un forçage <b>négatif</b>. En juin 1991, l'éruption du Pinatubo, aux Philippines, a injecté environ 15 à 20 millions de tonnes de dioxyde de soufre dans la stratosphère. Les fines gouttelettes de sulfates qui s'y sont formées ont réfléchi une partie du rayonnement solaire, augmentant l'albédo terrestre&nbsp;: le forçage a atteint environ $\pu{-3 W*m-2}$, et la température mondiale a baissé d'environ 0,5&nbsp;°C en 1992. L'effet a disparu en deux ou trois ans, le temps que les aérosols retombent.</li>
</ul>
<p class="nt-note">C'est pourquoi on étudie le climat sur des moyennes de plusieurs décennies&nbsp;: une année froide ne remet pas en cause la tendance, pas plus qu'une année record ne la prouve à elle seule.</p>
</div>
</details>

#### Le bilan radiatif complet {.nt-h4}

<p class="nt-lead">Depuis 2000, les satellites du programme CERES de la NASA mesurent en continu les flux qui entrent dans le système {Terre, atmosphère} et qui en sortent. En moyenne, sur environ $\pu{341 W*m-2}$ de rayonnement solaire reçu, environ $\pu{102 W*m-2}$ sont réfléchis (albédo voisin de 0,30), et environ $\pu{239 W*m-2}$ sont réémis vers l'espace sous forme d'infrarouge. La différence, de l'ordre de $\pu{1 W*m-2}$, est le déséquilibre qui réchauffe la planète, surtout ses océans.</p>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 760px); justify-content: center;">
<figure><video src="https://presentationssite.github.io/ceres.mp4" autoplay loop muted playsinline preload="metadata" style="margin-top:0.5em; margin-bottom:0;"></video><figcaption>les flux radiatifs de la Terre observés par les satellites CERES</figcaption></figure>
</div>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 860px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/bilanradiatif.png" alt="Le bilan radiatif moyen de la Terre : flux solaire incident, réfléchi, absorbé, et rayonnement infrarouge émis par la surface et par l'atmosphère, en W par mètre carré" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>le bilan radiatif moyen de la Terre (en $\pu{W*m-2}$)</figcaption></figure>
</div>

### Un modèle simple&nbsp;: l'atmosphère à une couche {.nt-h3}

<p class="nt-lead">On peut faire un bilan radiatif simplifié en modélisant l'atmosphère par une seule couche, qui absorbe une proportion $\alpha$ du rayonnement infrarouge $\varphi_E$ émis par la Terre. On note $\varphi_S$ le flux solaire entrant.</p>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 620px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/bilanrad.png" alt="Le modèle à une couche : le flux solaire, la part réfléchie par l'albédo, le rayonnement de la Terre, la part qui traverse l'atmosphère et celle qu'elle réémet vers l'espace et vers le sol" loading="lazy" style="margin-top:0.5em; margin-bottom:0;"><figcaption>le modèle de l'atmosphère à une couche</figcaption></figure>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Démonstration&nbsp;: la température d'équilibre</p>
<ol class="nt-steps">
<li><p>D'après le schéma, le flux sortant vers l'espace vaut&nbsp;: $\varphi_\text{sortant} = A\,\varphi_S + (1 - \alpha)\,\varphi_E + \dfrac{\alpha}{2}\,\varphi_E$.</p></li>
<li><p>À l'équilibre, $\varphi_\text{sortant} = \varphi_\text{entrant} = \varphi_S$, d'où $\varphi_E = \dfrac{2(1 - A)}{2 - \alpha}\,\varphi_S$.</p></li>
<li><p>Avec la loi de Stefan-Boltzmann, $\varphi_E = \sigma T^4$&nbsp;:</p>
<p class="nt-center">$T_\text{eq} = \left(\dfrac{2(1 - A)}{\sigma\,(2 - \alpha)}\,\varphi_S\right)^{1/4}$</p></li>
</ol>
</div>

<div class="nt-lab" id="lab-terre">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Albédo, effet de serre et température de la Terre</p>
<canvas style="height:330px;" aria-label="Les flux radiatifs du modèle à une couche, avec des flèches de largeur proportionnelle au flux, et la température de surface obtenue"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Albédo $A$&nbsp;: <b class="out-A"></b><input type="range" data-p="A" min="0" max="0.9" step="0.01" value="0.3"></label>
<label class="nt-ctrl">Absorption de l'infrarouge par l'atmosphère $\alpha$&nbsp;: <b class="out-al"></b><input type="range" data-p="al" min="0" max="1" step="0.01" value="0.8"></label>
</div>
<div class="nt-read" aria-live="polite"><span>température d'équilibre de la surface&nbsp;: <b class="out-T"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-preset="0.30,0.80">Terre actuelle</button>
<button type="button" class="nt-btn" data-preset="0.30,0">sans effet de serre</button>
<button type="button" class="nt-btn" data-preset="0.60,0.80">Terre couverte de glace</button>
</div>
<p class="nt-note">Les largeurs des flèches sont proportionnelles aux flux (en $\pu{W*m-2}$). Actuellement, $\alpha$ vaut environ 0,80 et $A$ environ 0,30, ce qui donne une température moyenne de surface d'environ 16&nbsp;°C. Sans effet de serre, elle serait d'environ −18&nbsp;°C.</p>
</div>


<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function nb(x, sig) { if (x === 0) { return '0'; } var a = Math.abs(x), d = Math.max(0, (sig || 3) - 1 - Math.floor(Math.log10(a))); var s = x.toFixed(Math.min(d, 6)), p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, '\u202f'); return p.join(',').replace('-', '\u2212'); }   /* espaces des milliers dans la partie entière seulement */
  function canvasCtx(cv) {
    var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function num(s) { return parseFloat(String(s).replace(',', '.').replace(/\s/g, '')); }
  function bilanTxt(r) { return r === 1 ? 'Parfait&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;!' : (r >= 0.5 ? 'C\u2019est un bon début&nbsp;: relisez les cas manqués.' : 'Relisez le cours, puis recommencez.')); }
  /* texte avec halo blanc ; le style de tracé est rétabli ensuite (sinon les lignes suivantes deviendraient blanches) */
  function txt(c, s, x, y, color, font, align) { c.save(); c.font = font || '12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round'; c.lineWidth = 4; c.strokeStyle = 'rgba(255,255,255,.92)'; c.strokeText(s, x, y); c.fillStyle = color; c.fillText(s, x, y); c.restore(); }
  function rr(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
  function watch(cv, cb) { if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }).observe(cv); } else { cb(true); } }
  /* couleur d'une température (bleu froid → rouge chaud), u entre 0 et 1 */
  function chaud(u) { u = Math.max(0, Math.min(1, u)); var a = [[37, 99, 235], [147, 197, 253], [253, 230, 138], [249, 115, 22], [220, 38, 38]], k = u * 4, i = Math.min(3, Math.floor(k)), f = k - i; return 'rgb(' + [0, 1, 2].map(function (j) { return Math.round(a[i][j] + (a[i + 1][j] - a[i][j]) * f); }).join(',') + ')'; }
  function axes(c, L, R, T, B, xs, ys, xl, yl) {
    xs.forEach(function (v) { c.strokeStyle = '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(v[0], T); c.lineTo(v[0], B); c.stroke(); txt(c, v[1], v[0], B + 15, '#475569', '11px system-ui, sans-serif'); });
    ys.forEach(function (v) { c.strokeStyle = '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(L, v[0]); c.lineTo(R, v[0]); c.stroke(); txt(c, v[1], L - 6, v[0] + 4, '#475569', '11px system-ui, sans-serif', 'right'); });
    c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
    txt(c, xl, R - 30, B + 29, '#475569', '11px system-ui, sans-serif');
    c.save(); c.translate(L - 38, (T + B) / 2); c.rotate(-Math.PI / 2); txt(c, yl, 0, 0, '#475569', '11px system-ui, sans-serif'); c.restore();
  }
  /* ================= Quiz génériques ================= */
  var QUIZ = {
    'quiz-signes': [
      ['Système {résistance chauffante d\u2019une bouilloire}. Le travail électrique W reçu du secteur est…', ['positif', 'négatif', 'nul'], 0, 'L\u2019énergie électrique <b>entre</b> dans la résistance&nbsp;: W &gt; 0.'],
      ['Système {résistance chauffante d\u2019une bouilloire}. Le transfert thermique Q vers l\u2019eau est…', ['positif', 'négatif', 'nul'], 1, 'L\u2019énergie <b>sort</b> de la résistance vers l\u2019eau&nbsp;: Q &lt; 0.'],
      ['Système {eau de la bouilloire}. Le transfert thermique Q<sub>r</sub> reçu de la résistance est…', ['positif', 'négatif'], 0, 'L\u2019eau reçoit de l\u2019énergie de la résistance&nbsp;: Q<sub>r</sub> &gt; 0.'],
      ['Système {eau de la bouilloire}. Le transfert thermique Q<sub>e</sub> avec l\u2019air de la cuisine, plus froid, est…', ['positif', 'négatif'], 1, 'L\u2019eau chaude cède de l\u2019énergie à l\u2019air plus froid&nbsp;: Q<sub>e</sub> &lt; 0.'],
      ['Système {canette sortie du réfrigérateur, posée sur la table}. Le transfert thermique Q avec l\u2019air ambiant est…', ['positif', 'négatif'], 0, 'L\u2019air ambiant, plus chaud, cède de l\u2019énergie à la canette&nbsp;: Q &gt; 0, et sa température augmente.'],
      ['Système {gaz d\u2019une pompe à vélo} qu\u2019on comprime vite. Le travail W des forces de pression est…', ['positif', 'négatif'], 0, 'L\u2019opérateur fournit de l\u2019énergie au gaz en le comprimant&nbsp;: W &gt; 0 (et le gaz s\u2019échauffe).'],
      ['Un système immobile reçoit W = 200 J et cède 50 J par transfert thermique. Sa variation d\u2019énergie interne vaut…', ['250 J', '150 J', '\u2212150 J'], 1, 'Premier principe&nbsp;: \u0394U = W + Q = 200 + (\u221250) = 150&nbsp;J.']
    ],
    'quiz-modes': [
      ['On se brûle en touchant la poignée métallique d\u2019une casserole chaude.', 0, 'L\u2019agitation thermique se transmet de proche en proche dans le métal&nbsp;: conduction.'],
      ['L\u2019air chaud d\u2019un radiateur monte vers le plafond, puis redescend refroidi le long des murs.', 1, 'C\u2019est un mouvement d\u2019ensemble du fluide&nbsp;: convection.'],
      ['On sent la chaleur d\u2019un feu de cheminée sur son visage, à deux mètres.', 2, 'L\u2019air entre le feu et le visage n\u2019est presque pas chauffé&nbsp;: c\u2019est le rayonnement infrarouge du feu.'],
      ['L\u2019énergie du Soleil nous parvient à travers le vide spatial.', 2, 'Seul le rayonnement peut se propager dans le vide.'],
      ['Dans une casserole d\u2019eau chauffée par le bas, l\u2019eau chaude du fond monte et l\u2019eau froide de la surface descend.', 1, 'Mouvement d\u2019ensemble du liquide&nbsp;: convection.'],
      ['Un glaçon fond dans la main.', 0, 'Contact direct entre la main et le glaçon&nbsp;: conduction.'],
      ['Une caméra thermique «&nbsp;voit&nbsp;» les personnes dans le noir.', 2, 'Tout corps chaud émet un rayonnement infrarouge, que la caméra détecte.'],
      ['Le vent refroidit la peau plus vite que l\u2019air immobile à la même température.', 1, 'L\u2019air en mouvement renouvelle sans cesse l\u2019air réchauffé au contact de la peau&nbsp;: convection (forcée).']
    ]
  };
  var MODES = ['conduction', 'convection', 'rayonnement'];
  $$(document, '.nt-quizlab').forEach(function (root) {
    var D = QUIZ[root.id]; if (!D) { return; }
    var qEl = $(root, '.nt-ql-q'), bx = $(root, '.nt-ql-btns'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), next = $(root, '[data-act="next"]'), lbl = next.innerHTML;
    var order = [], k = 0, good = 0, answered = false, fini = false;
    function show() {
      answered = false; var q = D[order[k]], choix = typeof q[1] === 'number' ? MODES : q[1], bon = typeof q[1] === 'number' ? q[1] : q[2], ex = typeof q[1] === 'number' ? q[2] : q[3];
      qEl.innerHTML = q[0]; msg.textContent = ''; bx.innerHTML = '';
      choix.forEach(function (cTxt, i) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn'; b.innerHTML = cTxt;
        b.addEventListener('click', function () {
          if (answered) { return; } answered = true;
          if (i === bon) { good++; b.classList.add('nt-btn-main'); msg.innerHTML = '<span style="color:#16A34A;">Bravo&nbsp;!</span> ' + ex; }
          else { b.style.borderColor = '#E11D48'; b.style.color = '#E11D48'; msg.innerHTML = '<span style="color:#E11D48;">Non.</span> ' + ex; }
          sc.textContent = good + ' / ' + (k + 1);
        });
        bx.appendChild(b);
      });
      next.innerHTML = k === order.length - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lbl;
    }
    function start() { order = shuffle(D.map(function (_, i) { return i; })); k = 0; good = 0; fini = false; bx.hidden = false; sc.textContent = '0 / 0'; show(); }
    next.addEventListener('click', function () {
      if (fini) { start(); return; }
      if (!answered) { msg.textContent = 'Choisissez d\u2019abord une réponse.'; return; }
      k++;
      if (k >= order.length) { fini = true; bx.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + order.length + '</span> ' + bilanTxt(good / order.length); msg.textContent = ''; next.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; return; }
      show();
    });
    start();
  });
  /* ================= Le gaz parfait vu de près ================= */
  (function () {
    var root = document.getElementById('lab-gaz');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rT = $(root, '[data-p="T"]'), rV = $(root, '[data-p="V"]'), rN = $(root, '[data-p="n"]'), oT = $(root, '.out-T'), oV = $(root, '.out-V'), oN = $(root, '.out-n'), oP = $(root, '.out-P'), S, visible = true, last = null;
    var R = 8.314, P = [], chocs = [], pm = null;
    function maxwell() { var a = 0; for (var i = 0; i < 3; i++) { var u = Math.sqrt(-2 * Math.log(Math.random() + 1e-9)) * Math.cos(2 * Math.PI * Math.random()); a += u * u; } return Math.sqrt(a / 3); }   /* vitesse relative, distribution de type Maxwell */
    function ajuster() { var n = Math.round(+rN.value * 3000); while (P.length < n) { P.push({ x: Math.random(), y: Math.random(), a: Math.random() * 2 * Math.PI, f: maxwell() }); } P.length = n; }
    function draw(dt) {
      if (!S) { return; }
      var T = +rT.value, V = +rV.value, n = +rN.value, Pa = n * R * T / (V / 1000);
      oT.textContent = Math.round(T) + ' K'; oV.textContent = fr(V, 2) + ' L'; oN.textContent = fr(n * 1000, 0) + ' mmol'; oP.textContent = nb(Pa / 1000, 3) + ' kPa';
      ajuster();
      var c = S.ctx, w = S.w, h = S.h, Wmax = Math.min(w * 0.55, 420), x0 = 24, y0 = 26, bh = h - 86, bw = Wmax * V / 2, v = 75 * Math.sqrt(T / 300), uT = (T - 150) / 550;
      c.clearRect(0, 0, w, h);
      /* plaque chauffante, dont la couleur suit la température */
      var py = y0 + bh + 12;
      rr(c, x0 - 8, py, Wmax + 16, 14, 4); c.fillStyle = '#CBD5E1'; c.fill();
      var gp = c.createLinearGradient(0, py, 0, py + 6); gp.addColorStop(0, chaud(uT)); gp.addColorStop(1, 'rgba(255,255,255,0)'); c.fillStyle = gp; c.fillRect(x0 - 4, py, Wmax + 8, 5);
      txt(c, 'source thermique', x0 + Wmax / 2, py + 30, '#64748B', '600 10.5px system-ui, sans-serif');
      /* cylindre en verre */
      var gv = c.createLinearGradient(0, y0, 0, y0 + bh); gv.addColorStop(0, '#F8FAFC'); gv.addColorStop(0.5, '#EEF2F7'); gv.addColorStop(1, '#F8FAFC');
      c.fillStyle = gv; c.fillRect(x0, y0, bw, bh);
      /* particules : rebonds élastiques, traînée selon la vitesse, couleur selon la vitesse individuelle */
      P.forEach(function (p) {
        var sp = v * p.f * dt, nx = p.x + Math.cos(p.a) * sp / bw, ny = p.y + Math.sin(p.a) * sp / bh, hit = null;
        if (nx < 0) { p.a = Math.PI - p.a; nx = 0; hit = [x0, y0 + p.y * bh]; } else if (nx > 1) { p.a = Math.PI - p.a; nx = 1; hit = [x0 + bw, y0 + p.y * bh]; }
        if (ny < 0) { p.a = -p.a; ny = 0; hit = [x0 + p.x * bw, y0]; } else if (ny > 1) { p.a = -p.a; ny = 1; hit = [x0 + p.x * bw, y0 + bh]; }
        if (hit && chocs.length < 90) { chocs.push({ x: hit[0], y: hit[1], t: 0 }); }
        p.x = nx; p.y = ny;
        var X = x0 + 4 + p.x * (bw - 8), Y = y0 + 4 + p.y * (bh - 8), col = chaud(Math.min(1, 0.12 + uT * 0.75 * p.f));
        c.strokeStyle = col; c.globalAlpha = 0.35; c.lineWidth = 2.2; c.beginPath(); c.moveTo(X, Y); c.lineTo(X - Math.cos(p.a) * v * p.f * 0.06, Y - Math.sin(p.a) * v * p.f * 0.06); c.stroke(); c.globalAlpha = 1;
        c.fillStyle = col; c.beginPath(); c.arc(X, Y, 3.6, 0, 2 * Math.PI); c.fill();
        c.fillStyle = 'rgba(255,255,255,.55)'; c.beginPath(); c.arc(X - 1.1, Y - 1.1, 1.2, 0, 2 * Math.PI); c.fill();
      });
      /* éclats des chocs sur les parois : c'est l'origine microscopique de la pression */
      chocs = chocs.filter(function (k) { k.t += dt; return k.t < 0.25; });
      chocs.forEach(function (k) { c.strokeStyle = 'rgba(220,38,38,' + (0.6 * (1 - k.t / 0.25)) + ')'; c.lineWidth = 1.5; c.beginPath(); c.arc(k.x, k.y, 3 + 14 * k.t, 0, 2 * Math.PI); c.stroke(); });
      /* parois, piston, tige et poignée */
      c.strokeStyle = '#475569'; c.lineWidth = 3; c.lineCap = 'round'; c.beginPath(); c.moveTo(x0 + bw + 2, y0); c.lineTo(x0, y0); c.lineTo(x0, y0 + bh); c.lineTo(x0 + bw + 2, y0 + bh); c.stroke();
      c.strokeStyle = 'rgba(71,85,105,.35)'; c.lineWidth = 1.5; c.beginPath(); c.moveTo(x0 + bw + 2, y0); c.lineTo(x0 + Wmax + 30, y0); c.moveTo(x0 + bw + 2, y0 + bh); c.lineTo(x0 + Wmax + 30, y0 + bh); c.stroke();
      var gpi = c.createLinearGradient(x0 + bw, 0, x0 + bw + 14, 0); gpi.addColorStop(0, '#94A3B8'); gpi.addColorStop(0.5, '#E2E8F0'); gpi.addColorStop(1, '#64748B');
      c.fillStyle = gpi; rr(c, x0 + bw, y0 - 2, 14, bh + 4, 3); c.fill();
      c.fillStyle = '#94A3B8'; c.fillRect(x0 + bw + 14, y0 + bh / 2 - 4, 54, 8);
      c.fillStyle = '#334155'; rr(c, x0 + bw + 66, y0 + bh / 2 - 16, 12, 32, 4); c.fill();
      /* manomètre, relié au haut du cylindre */
      var gx = w - 74, gy = y0 + 66, rg = 54, pmax = 400e3, a0 = 0.75 * Math.PI, a1 = 2.25 * Math.PI, ang = a0 + (a1 - a0) * Math.min(1, Pa / pmax);
      pm = pm === null ? ang : pm + (ang - pm) * Math.min(1, dt * 6);
      c.strokeStyle = '#94A3B8'; c.lineWidth = 3; c.lineJoin = 'round'; c.beginPath(); c.moveTo(x0 + 30, y0); c.arcTo(x0 + 30, y0 - 14, x0 + 44, y0 - 14, 8); c.arcTo(gx, y0 - 14, gx, gy - rg, 8); c.lineTo(gx, gy - rg); c.stroke();   /* tuyau : monte, longe le haut, puis descend droit jusqu'au cadran */
      c.fillStyle = '#64748B'; rr(c, gx - 6, gy - rg - 7, 12, 8, 2); c.fill();   /* raccord */
      var gf = c.createRadialGradient(gx - 12, gy - 14, 6, gx, gy, rg); gf.addColorStop(0, '#FFFFFF'); gf.addColorStop(1, '#E2E8F0');
      c.fillStyle = gf; c.beginPath(); c.arc(gx, gy, rg, 0, 2 * Math.PI); c.fill(); c.strokeStyle = '#334155'; c.lineWidth = 4; c.stroke();
      [['#22C55E', 0, 0.5], ['#F59E0B', 0.5, 0.75], ['#EF4444', 0.75, 1]].forEach(function (z) { c.strokeStyle = z[0]; c.lineWidth = 5; c.beginPath(); c.arc(gx, gy, rg - 8, a0 + (a1 - a0) * z[1], a0 + (a1 - a0) * z[2]); c.stroke(); });
      for (var k = 0; k <= 8; k++) { var a = a0 + (a1 - a0) * k / 8; c.strokeStyle = '#334155'; c.lineWidth = k % 2 ? 1 : 2; c.beginPath(); c.moveTo(gx + (rg - 13) * Math.cos(a), gy + (rg - 13) * Math.sin(a)); c.lineTo(gx + (rg - (k % 2 ? 17 : 20)) * Math.cos(a), gy + (rg - (k % 2 ? 17 : 20)) * Math.sin(a)); c.stroke(); if (k % 2 === 0) { txt(c, String(k * 50), gx + (rg - 30) * Math.cos(a), gy + (rg - 30) * Math.sin(a) + 4, '#334155', '600 9.5px system-ui, sans-serif'); } }
      c.save(); c.translate(gx, gy); c.rotate(pm); c.fillStyle = '#DC2626'; c.beginPath(); c.moveTo(-6, -2.5); c.lineTo(rg - 16, 0); c.lineTo(-6, 2.5); c.closePath(); c.fill(); c.restore();
      c.fillStyle = '#1E293B'; c.beginPath(); c.arc(gx, gy, 4.5, 0, 2 * Math.PI); c.fill();
      txt(c, 'kPa', gx, gy + 26, '#475569', '600 10px system-ui, sans-serif'); txt(c, 'manomètre', gx, gy + rg + 18, '#475569', '600 11px system-ui, sans-serif');
    }
    function loop(ts) { var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; if (visible) { draw(RM ? dt * 0.4 : dt); } requestAnimationFrame(loop); }
    [rT, rV, rN].forEach(function (r) { r.addEventListener('input', function () { draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    watch(cv, function (v) { visible = v; });
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Entraînement : la loi des gaz parfaits ================= */
  (function () {
    var root = document.getElementById('lab-pv');
    if (!root) { return; }
    var qEl = $(root, '.nt-tr-q'), inp = $(root, 'input[type="text"]'), uEl = $(root, '.nt-tr-unit'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), bV = $(root, '[data-act="check"]'), bN = $(root, '[data-act="next"]'), lblN = bN.innerHTML;
    var R = 8.314, NQ = 6, n = 0, good = 0, cur, done = false, fini = false;
    var G = [
      function () {   /* pression d'un gaz dans un récipient */
        var VL = pick([0.5, 1, 2, 5, 10, 20]), th = pick([0, 20, 25, 37, 80, 100]), nn = pick([0.01, 0.02, 0.05, 0.1, 0.2, 0.5]), T = th + 273.15, P = nn * R * T / (VL / 1000);
        return { q: nb(nn, 2) + '&nbsp;mol de gaz sont enfermées dans un récipient de ' + nb(VL, 2) + '&nbsp;L, à ' + th + '&nbsp;°C. Calculer la pression du gaz, en <b>kPa</b>.', rep: P / 1000, unit: 'kPa',
          expl: 'Conversions&nbsp;: V = ' + nb(VL, 2) + '&nbsp;L = ' + nb(VL / 1000, 2) + '&nbsp;m³ et T = ' + th + ' + 273,15 = ' + fr(T, 2) + '&nbsp;K. Puis P = nRT / V = ' + nb(nn, 2) + ' × 8,314 × ' + fr(T, 2) + ' / ' + nb(VL / 1000, 2) + ' ≈ ' + nb(P, 3) + '&nbsp;Pa, soit ' + nb(P / 1000, 3) + '&nbsp;kPa.' };
      },
      function () {   /* quantité de matière d'air dans une pièce ou un ballon */
        var V = pick([[0.002, '2,0 L'], [0.005, '5,0 L'], [30, '30 m³'], [50, '50 m³']]), th = pick([15, 20, 25]), Pb = pick([1.0, 1.013, 2.0]), T = th + 273.15, nn = Pb * 1e5 * V[0] / (R * T);
        return { q: 'Quelle quantité de matière d\u2019air contient un volume de ' + V[1] + ', à ' + th + '&nbsp;°C et sous ' + fr(Pb, Pb === 1.013 ? 3 : 1) + '&nbsp;bar&nbsp;? Réponse en <b>mol</b>.', rep: nn, unit: 'mol',
          expl: 'Conversions&nbsp;: P = ' + fr(Pb, Pb === 1.013 ? 3 : 1) + '&nbsp;bar = ' + nb(Pb * 1e5, 4) + '&nbsp;Pa (1&nbsp;bar = 10<sup>5</sup>&nbsp;Pa), V = ' + nb(V[0], 2) + '&nbsp;m³ et T = ' + fr(T, 2) + '&nbsp;K. Puis n = PV / (RT) ≈ ' + nb(nn, 3) + '&nbsp;mol.' };
      },
      function () {   /* volume molaire */
        var th = pick([0, 20, 25]), T = th + 273.15, Vm = R * T / 101325 * 1000;
        return { q: 'Calculer le volume occupé par une mole de gaz parfait à ' + th + '&nbsp;°C, sous la pression atmosphérique normale (1&nbsp;013&nbsp;hPa). Réponse en <b>L</b>.', rep: Vm, unit: 'L',
          expl: 'V = nRT / P = 1 × 8,314 × ' + fr(T, 2) + ' / 101&nbsp;325 ≈ ' + nb(Vm / 1000, 3) + '&nbsp;m³, soit ' + nb(Vm, 3) + '&nbsp;L. C\u2019est le volume molaire&nbsp;: il ne dépend pas de la nature du gaz&nbsp;!' };
      },
      function () {   /* température d'un gaz */
        var VL = pick([1, 2, 10]), nn = pick([0.05, 0.1, 0.5]), PkPa = pick([120, 150, 200, 250]), T = PkPa * 1000 * VL / 1000 / (nn * R);
        return { q: 'Un récipient de ' + VL + '&nbsp;L contient ' + nb(nn, 2) + '&nbsp;mol de gaz, à la pression de ' + PkPa + '&nbsp;kPa. Quelle est sa température, en <b>K</b>&nbsp;?', rep: T, unit: 'K',
          expl: 'T = PV / (nR) = ' + PkPa + '&nbsp;000 × ' + nb(VL / 1000, 2) + ' / (' + nb(nn, 2) + ' × 8,314) ≈ ' + nb(T, 3) + '&nbsp;K, soit ' + nb(T - 273.15, 3) + '&nbsp;°C.' };
      },
      function () {   /* transformation à quantité de matière constante */
        var P1 = pick([100, 150, 200]), T1 = pick([280, 290, 300]), T2 = pick([320, 330, 350, 360]), V = pick([1, 2]), P2 = P1 * T2 / T1;
        return { q: 'Un pneu (volume constant) contient de l\u2019air à ' + P1 + '&nbsp;kPa et ' + T1 + '&nbsp;K. Après un long trajet, l\u2019air est à ' + T2 + '&nbsp;K. Quelle est sa nouvelle pression, en <b>kPa</b>&nbsp;?', rep: P2, unit: 'kPa',
          expl: 'n, R et V sont constants, donc P / T = nR / V est constant&nbsp;: P<sub>2</sub> = P<sub>1</sub> × T<sub>2</sub> / T<sub>1</sub> = ' + P1 + ' × ' + T2 + ' / ' + T1 + ' ≈ ' + nb(P2, 3) + '&nbsp;kPa. Inutile de connaître n ou V&nbsp;!' };
      }
    ];
    function nouveau() { cur = pick(G)(); qEl.innerHTML = cur.q; uEl.textContent = cur.unit; inp.value = ''; msg.textContent = ''; done = false; bV.disabled = false; inp.disabled = false; bN.innerHTML = n === NQ - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lblN; }
    function start() { n = 0; good = 0; fini = false; sc.textContent = '0 / 0'; $(root, '.nt-tr-zone').hidden = false; nouveau(); }
    bV.addEventListener('click', function () {
      if (done || fini) { return; }
      var v = num(inp.value); if (isNaN(v)) { msg.textContent = 'Entrez une valeur numérique.'; return; }
      var ok = Math.abs(v - cur.rep) <= Math.abs(cur.rep) * 0.02; done = true; n++; if (ok) { good++; }
      bV.disabled = true; inp.disabled = true; sc.textContent = good + ' / ' + n;
      msg.innerHTML = (ok ? '<span style="color:#16A34A;">Bravo&nbsp;!</span> ' : '<span style="color:#E11D48;">Non</span>&nbsp;: la réponse est ' + nb(cur.rep, 3) + '&nbsp;' + cur.unit + '. ') + cur.expl;
    });
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { bV.click(); } });
    bN.addEventListener('click', function () {
      if (fini) { start(); return; }
      if (!done) { msg.textContent = 'Validez d\u2019abord votre réponse.'; return; }
      if (n >= NQ) { fini = true; $(root, '.nt-tr-zone').hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + NQ + '</span> ' + bilanTxt(good / NQ); msg.textContent = ''; bN.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; return; }
      nouveau();
    });
    start();
  })();
  /* ================= Capacité thermique : chauffer 1 kg de différents matériaux ================= */
  (function () {
    var root = document.getElementById('lab-cap');
    if (!root) { return; }
    var cv = $(root, 'canvas'), btn = $(root, '[data-act="play"]'), oT = $(root, '.out-t'), oQ = $(root, '.out-Q'), S, t = 0, run = false, last = null;
    var MAT = [['eau liquide', 4185, '#3B82F6'], ['huile', 2000, '#EAB308'], ['aluminium', 897, '#94A3B8'], ['brique', 840, '#C2410C'], ['acier', 475, '#475569']], PW = 1000, TMAX = 60, T0 = 20;
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, L = 52, R = w - 16, T = 14, B = h - 34, Q = PW * t;
      function X(i) { return L + (i + 0.5) * (R - L) / MAT.length; }
      function Y(th) { return B - (th - T0) / 130 * (B - T); }
      c.clearRect(0, 0, w, h);
      var ys = []; for (var th = 20; th <= 150; th += 20) { ys.push([Y(th), th + ' °C']); }
      ys.forEach(function (v) { c.strokeStyle = '#E2E8F0'; c.lineWidth = 1; c.beginPath(); c.moveTo(L, v[0]); c.lineTo(R, v[0]); c.stroke(); txt(c, v[1], L - 6, v[0] + 4, '#475569', '11px system-ui, sans-serif', 'right'); });
      MAT.forEach(function (m, i) {
        var dT = Q / (1 * m[1]), th = T0 + dT, x = X(i), bw = Math.min(46, (R - L) / MAT.length * 0.5), yb = Y(Math.min(th, 150));
        rr(c, x - bw / 2, T, bw, B - T, 6); c.fillStyle = '#F1F5F9'; c.fill();
        var g = c.createLinearGradient(0, B, 0, yb); g.addColorStop(0, chaud(0.25)); g.addColorStop(1, chaud(0.25 + (th - T0) / 170));
        c.fillStyle = g; c.fillRect(x - bw / 2, yb, bw, B - yb);
        txt(c, fr(th, 1) + ' °C', x, Math.max(T + 12, yb - 6), '#1E293B', '700 11.5px system-ui, sans-serif');
        txt(c, m[0], x, B + 15, m[2], '700 11px system-ui, sans-serif'); txt(c, m[1] + ' J/(kg·K)', x, B + 28, '#64748B', '10px system-ui, sans-serif');
      });
      oT.textContent = fr(t, 1) + ' s'; oQ.textContent = nb(Q / 1000, 3) + ' kJ';
    }
    function loop(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (run) { t = Math.min(TMAX, t + dt * 6); if (t >= TMAX) { run = false; btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; } draw(); }
      requestAnimationFrame(loop);
    }
    btn.addEventListener('click', function () {
      if (t >= TMAX) { t = 0; draw(); }
      run = !run; btn.innerHTML = run ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-fire"></i>&nbsp; Chauffer';
    });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Les trois modes de transfert thermique ================= */
  (function () {
    var root = document.getElementById('lab-modes');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), S, visible = true, last = null, tps = 0, mode = 'cond';
    var NC = 16, NR = 5, E = [], conv = [], cible = 0, etoiles = [];
    var TXT = { cond: '<b>Conduction</b>&nbsp;: la flamme agite les atomes du bout de la barre. Chaque atome communique son agitation à ses voisins, <b>de proche en proche</b>, sans que la matière se déplace.',
                conv: '<b>Convection</b>&nbsp;: l\u2019eau chauffée au fond se dilate, devient moins dense et monte (poussée d\u2019Archimède)&nbsp;; refroidie en surface, elle redescend le long des parois. C\u2019est un <b>mouvement d\u2019ensemble</b> du fluide.',
                ray: '<b>Rayonnement</b>&nbsp;: le corps chaud émet des ondes électromagnétiques (infrarouge, lumière) qui traversent <b>le vide</b> et sont absorbées par l\u2019objet, qui s\u2019échauffe.' };
    function init() {
      E = []; for (var i = 0; i < NC; i++) { E.push(0.05); }
      conv = []; for (var k = 0; k < 170; k++) { conv.push({ x: Math.random(), y: Math.random(), T: 0.3 + Math.random() * 0.2, px: null, py: null }); }
      etoiles = []; for (var s = 0; s < 70; s++) { etoiles.push([Math.random(), Math.random(), Math.random()]); }
      cible = 0; tps = 0; msg.innerHTML = TXT[mode];
    }
    /* flamme complète, avec son halo ; (x, y) : base de la flamme ; s : échelle */
    function flamme(c, x, y, s) {
      var t = tps * 9, hal = c.createRadialGradient(x, y - 22 * s, 2, x, y - 22 * s, 34 * s);
      hal.addColorStop(0, 'rgba(251,146,60,.35)'); hal.addColorStop(1, 'rgba(251,146,60,0)'); c.fillStyle = hal; c.beginPath(); c.arc(x, y - 22 * s, 34 * s, 0, 2 * Math.PI); c.fill();
      var g1 = c.createLinearGradient(0, y, 0, y - 44 * s); g1.addColorStop(0, '#EA580C'); g1.addColorStop(1, 'rgba(251,146,60,.85)');
      c.fillStyle = g1; c.beginPath(); c.moveTo(x - 11 * s, y); c.bezierCurveTo(x - 15 * s, y - 16 * s, x - 6 * s, y - 30 * s, x + 2.5 * Math.sin(t) * s, y - 46 * s); c.bezierCurveTo(x + 7 * s, y - 30 * s, x + 15 * s, y - 16 * s, x + 11 * s, y); c.closePath(); c.fill();
      var g2 = c.createLinearGradient(0, y, 0, y - 26 * s); g2.addColorStop(0, '#3B82F6'); g2.addColorStop(0.35, '#FDE047'); g2.addColorStop(1, 'rgba(254,240,138,.9)');
      c.fillStyle = g2; c.beginPath(); c.moveTo(x - 5.5 * s, y); c.bezierCurveTo(x - 7 * s, y - 9 * s, x - 3 * s, y - 17 * s, x + 1.2 * Math.sin(t + 1) * s, y - 27 * s); c.bezierCurveTo(x + 3 * s, y - 17 * s, x + 7 * s, y - 9 * s, x + 5.5 * s, y); c.closePath(); c.fill();
    }
    function bunsen(c, x, y) {   /* bec Bunsen : (x, y) = haut du tube */
      var g = c.createLinearGradient(x - 7, 0, x + 7, 0); g.addColorStop(0, '#64748B'); g.addColorStop(0.5, '#CBD5E1'); g.addColorStop(1, '#64748B');
      c.fillStyle = g; c.fillRect(x - 6, y, 12, 44); c.fillStyle = '#475569'; rr(c, x - 22, y + 44, 44, 9, 3); c.fill(); c.fillStyle = '#334155'; c.fillRect(x - 8, y + 20, 16, 6);
    }
    function draw(dt) {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h; c.clearRect(0, 0, w, h); tps += dt;
      if (mode === 'cond') {
        for (var it = 0; it < 4; it++) { var Dt = dt / 4, nE = E.slice(); nE[0] = 1; for (var i = 1; i < NC; i++) { var r = i < NC - 1 ? E[i + 1] : E[i]; nE[i] = E[i] + 2.2 * Dt * (E[i - 1] - 2 * E[i] + r); } E = nE; }
        var bx0 = 70, bx1 = w - 30, dx = (bx1 - bx0) / (NC - 1), by = 40, bh = (NR - 1) * 22;
        var gb = c.createLinearGradient(0, by - 18, 0, by + bh + 18); gb.addColorStop(0, '#F1F5F9'); gb.addColorStop(1, '#E2E8F0');
        rr(c, bx0 - 18, by - 18, bx1 - bx0 + 36, bh + 36, 10); c.fillStyle = gb; c.fill(); c.strokeStyle = '#CBD5E1'; c.lineWidth = 1; c.stroke();
        for (var j = 0; j < NR; j++) { for (var i2 = 0; i2 < NC; i2++) {
          var a = 7 * Math.sqrt(E[i2]), x = bx0 + i2 * dx + a * Math.sin(tps * 23 + i2 * 1.7 + j * 2.9), y = by + j * 22 + a * Math.cos(tps * 19 + i2 * 2.3 + j * 1.1);
          var ga = c.createRadialGradient(x - 2, y - 2, 1, x, y, 7); ga.addColorStop(0, '#fff'); ga.addColorStop(0.35, chaud(E[i2])); ga.addColorStop(1, chaud(E[i2]));
          c.fillStyle = ga; c.beginPath(); c.arc(x, y, 6.5, 0, 2 * Math.PI); c.fill();
        } }
        /* bec Bunsen sous le bout gauche : flamme entière visible */
        var fx = bx0 + 6, fy = by + bh + 18 + 52;
        flamme(c, fx, fy, 1.15); bunsen(c, fx, fy);
        txt(c, 'barre métallique : chaque bille est un atome', (bx0 + bx1) / 2 + 30, by + bh + 46, '#475569', '600 11px system-ui, sans-serif');
        txt(c, 'atomes agités', bx0 + 40, by - 24, '#B91C1C', '600 10.5px system-ui, sans-serif'); txt(c, 'atomes peu agités', bx1 - 40, by - 24, '#1D4ED8', '600 10.5px system-ui, sans-serif');
      } else if (mode === 'conv') {
        var x0 = Math.max(30, w / 2 - 220), x1 = Math.min(w - 30, w / 2 + 220), y0 = 34, y1 = h - 58, W = x1 - x0, H = y1 - y0;
        /* plaque chauffante sous le bécher */
        rr(c, x0 - 14, y1 + 6, W + 28, 18, 5); c.fillStyle = '#CBD5E1'; c.fill();
        var gp = c.createRadialGradient((x0 + x1) / 2, y1 + 8, 4, (x0 + x1) / 2, y1 + 8, W * 0.35); gp.addColorStop(0, 'rgba(239,68,68,.95)'); gp.addColorStop(1, 'rgba(239,68,68,0)'); c.fillStyle = gp; c.fillRect(x0, y1 + 6, W, 8);
        txt(c, 'plaque chauffante', (x0 + x1) / 2, h - 10, '#B91C1C', '600 11px system-ui, sans-serif');
        /* eau : légèrement plus chaude au fond */
        var ge = c.createLinearGradient(0, y0, 0, y1); ge.addColorStop(0, 'rgba(191,219,254,.75)'); ge.addColorStop(1, 'rgba(254,215,170,.6)'); c.fillStyle = ge; c.fillRect(x0 + 2, y0 + 8, W - 4, H - 8);
        /* sens de circulation : deux rouleaux */
        c.strokeStyle = 'rgba(100,116,139,.35)'; c.lineWidth = 2;
        [[0.25, 1], [0.75, -1]].forEach(function (rl) { var cx = x0 + rl[0] * W, cy = y0 + H / 2 + 4, rx = W * 0.17, ry = H * 0.32; for (var q = 0; q < 4; q++) { var a1 = q * Math.PI / 2 + 0.25, a2 = a1 + 1.1; c.beginPath(); c.ellipse(cx, cy, rx, ry, 0, Math.min(a1, a2), Math.max(a1, a2)); c.stroke(); var ae = rl[1] > 0 ? a1 : a2, ex = cx + rx * Math.cos(ae), ey = cy + ry * Math.sin(ae), tx = -rx * Math.sin(ae) * -rl[1], ty = ry * Math.cos(ae) * -rl[1], L = Math.hypot(tx, ty); tx /= L; ty /= L; c.fillStyle = 'rgba(100,116,139,.45)'; c.beginPath(); c.moveTo(ex + tx * 7, ey + ty * 7); c.lineTo(ex - ty * 4, ey + tx * 4); c.lineTo(ex + ty * 4, ey - tx * 4); c.closePath(); c.fill(); } });
        conv.forEach(function (p) {
          var u = -Math.PI * Math.sin(2 * Math.PI * p.x) * Math.cos(Math.PI * p.y), v = 2 * Math.PI * Math.cos(2 * Math.PI * p.x) * Math.sin(Math.PI * p.y);
          var ox = x0 + p.x * W, oy = y0 + 8 + p.y * (H - 10);
          p.x = Math.min(0.99, Math.max(0.01, p.x + u * dt * 0.06)); p.y = Math.min(0.99, Math.max(0.01, p.y + v * dt * 0.06));
          if (p.y > 0.85 && Math.abs(p.x - 0.5) < 0.3) { p.T = Math.min(1, p.T + dt * 0.8); } if (p.y < 0.15) { p.T = Math.max(0.1, p.T - dt * 0.6); }
          var X = x0 + p.x * W, Y = y0 + 8 + p.y * (H - 10);
          c.strokeStyle = chaud(p.T); c.globalAlpha = 0.4; c.lineWidth = 2; c.beginPath(); c.moveTo(X, Y); c.lineTo(X + (X - ox) * -6, Y + (Y - oy) * -6); c.stroke(); c.globalAlpha = 1;
          c.fillStyle = chaud(p.T); c.beginPath(); c.arc(X, Y, 3.8, 0, 2 * Math.PI); c.fill();
        });
        /* bécher en verre */
        c.strokeStyle = '#64748B'; c.lineWidth = 2.5; c.lineJoin = 'round'; c.beginPath(); c.moveTo(x0 - 8, y0 - 8); c.quadraticCurveTo(x0 - 1, y0 - 4, x0, y0 + 6); c.lineTo(x0, y1 - 6); c.quadraticCurveTo(x0, y1, x0 + 6, y1); c.lineTo(x1 - 6, y1); c.quadraticCurveTo(x1, y1, x1, y1 - 6); c.lineTo(x1, y0); c.stroke();
        txt(c, 'en surface, l\u2019eau refroidit', (x0 + x1) / 2, y0 - 4, '#1D4ED8', '600 11px system-ui, sans-serif');
      } else {
        /* espace : le vide, quelques étoiles */
        var gsp = c.createLinearGradient(0, 0, w, 0); gsp.addColorStop(0, '#1E1B4B'); gsp.addColorStop(1, '#0F172A'); c.fillStyle = gsp; rr(c, 0, 0, w, h, 10); c.fill();
        etoiles.forEach(function (e) { c.fillStyle = 'rgba(255,255,255,' + (0.3 + 0.5 * Math.abs(Math.sin(tps * 1.5 + e[2] * 9))) + ')'; c.fillRect(e[0] * w, e[1] * h, 1.6, 1.6); });
        var sx = 80, sy = h / 2, ox = w - 90;
        cible = Math.min(1, cible + dt * 0.07);
        var hal = c.createRadialGradient(sx, sy, 20, sx, sy, 90); hal.addColorStop(0, 'rgba(253,224,71,.45)'); hal.addColorStop(1, 'rgba(253,224,71,0)'); c.fillStyle = hal; c.beginPath(); c.arc(sx, sy, 90, 0, 2 * Math.PI); c.fill();
        var gs = c.createRadialGradient(sx - 10, sy - 10, 4, sx, sy, 42); gs.addColorStop(0, '#FEF9C3'); gs.addColorStop(0.6, '#FBBF24'); gs.addColorStop(1, '#F97316'); c.fillStyle = gs; c.beginPath(); c.arc(sx, sy, 40, 0, 2 * Math.PI); c.fill();
        c.save(); c.font = '700 11.5px system-ui, sans-serif'; c.textAlign = 'center'; c.fillStyle = '#FDE68A'; c.fillText('corps chaud', sx, sy + 66); c.restore();   /* sans halo blanc, sur fond sombre */
        for (var q2 = 0; q2 < 7; q2++) {   /* trains d'ondes, avec une pointe de flèche */
          var ph = ((tps * 0.32 + q2 / 7) % 1), xc = sx + 58 + ph * (ox - sx - 100), dy = ((q2 * 3) % 5 - 2) * 18, al = 0.95 - 0.35 * ph, col = q2 % 2 ? '251,146,60' : '248,113,113';
          c.strokeStyle = 'rgba(' + col + ',' + al + ')'; c.lineWidth = 2.2; c.beginPath();
          for (var s2 = -26; s2 <= 26; s2 += 1.5) { var xx = xc + s2, yy = sy + dy + 7 * Math.sin(s2 / 3.2 - tps * 9) * Math.exp(-s2 * s2 / 340); if (s2 === -26) { c.moveTo(xx, yy); } else { c.lineTo(xx, yy); } }
          c.stroke(); c.fillStyle = 'rgba(' + col + ',' + al + ')'; c.beginPath(); c.moveTo(xc + 34, sy + dy); c.lineTo(xc + 26, sy + dy - 4); c.lineTo(xc + 26, sy + dy + 4); c.closePath(); c.fill();
        }
        /* objet qui absorbe et s'échauffe, avec son thermomètre */
        var go = c.createLinearGradient(ox - 24, 0, ox + 24, 0); go.addColorStop(0, chaud(0.1 + 0.75 * cible)); go.addColorStop(1, chaud(0.05 + 0.6 * cible)); c.fillStyle = go; rr(c, ox - 24, sy - 44, 48, 88, 10); c.fill(); c.strokeStyle = 'rgba(255,255,255,.6)'; c.lineWidth = 1.5; c.stroke();
        var tx0 = ox + 44; c.fillStyle = 'rgba(255,255,255,.85)'; rr(c, tx0 - 5, sy - 44, 10, 80, 5); c.fill(); c.beginPath(); c.arc(tx0, sy + 42, 9, 0, 2 * Math.PI); c.fill();
        c.fillStyle = '#EF4444'; c.beginPath(); c.arc(tx0, sy + 42, 6, 0, 2 * Math.PI); c.fill(); c.fillRect(tx0 - 2.5, sy + 34 - 70 * (0.15 + 0.8 * cible), 5, 70 * (0.15 + 0.8 * cible) + 2);
        c.save(); c.font = '700 11.5px system-ui, sans-serif'; c.textAlign = 'center'; c.fillStyle = '#E2E8F0'; c.fillText('objet', ox, sy + 66); c.restore();
        c.save(); c.font = '600 11px system-ui, sans-serif'; c.textAlign = 'center'; c.fillStyle = '#94A3B8'; c.fillText('le vide : aucune matière entre les deux', (sx + ox) / 2, 22); c.restore();
      }
    }
    function loop(ts) { var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts; if (visible) { draw(RM ? dt * 0.4 : dt); } requestAnimationFrame(loop); }
    $$(root, 'input[name="tmode"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; init(); }); });
    $(root, '[data-act="reset"]').addEventListener('click', init);
    function setup() { S = canvasCtx(cv); draw(0); }
    watch(cv, function (v) { visible = v; });
    init(); setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Un mur, plusieurs couches : résistances thermiques en série ================= */
  (function () {
    var root = document.getElementById('lab-mur');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rE = $(root, '[data-p="e"]'), rTe = $(root, '[data-p="Te"]'), oE = $(root, '.out-e'), oTe = $(root, '.out-Te'), oR = $(root, '.out-R'), oF = $(root, '.out-F'), S;
    var Ssurf = 10, Ti = 19, ISO = { laine: ['laine de verre', 0.035, '#FDE68A'], poly: ['polystyrène expansé', 0.038, '#E9D5FF'], liege: ['liège expansé', 0.040, '#D6BCA0'] }, iso = 'laine';
    function couches() {
      var e = +rE.value / 1000, L = [
        { n: 'air intérieur', cv: true, h: 8, col: '#FEE2E2' },
        { n: 'plâtre', e: 0.013, l: 0.25, col: '#F1F5F9' },
        { n: ISO[iso][0], e: e, l: ISO[iso][1], col: ISO[iso][2] },
        { n: 'parpaing', e: 0.20, l: 1.1, col: '#CBD5E1' },
        { n: 'air extérieur', cv: true, h: 25, col: '#DBEAFE' }];
      L.forEach(function (c) { c.R = c.cv ? 1 / (c.h * Ssurf) : (c.e > 0 ? c.e / (c.l * Ssurf) : 0); });
      return L;
    }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, Te = +rTe.value, L = couches(), Rt = L.reduce(function (s, x) { return s + x.R; }, 0), Phi = (Ti - Te) / Rt;   /* h : hauteur du dessin */
      oE.textContent = rE.value + ' mm'; oTe.textContent = fr(Te, 0).replace('\u2212', '\u2212') + ' °C';
      oR.textContent = nb(Rt, 3) + ' K/W'; oF.textContent = nb(Phi, 3) + ' W';
      c.clearRect(0, 0, w, h);
      /* coupe du mur : épaisseurs à l'échelle (les couches d'air ont une largeur conventionnelle) */
      var x0 = 30, x1 = w - 30, y0 = 30, y1 = h - 96, airW = 50, tot = L.filter(function (x) { return !x.cv; }).reduce(function (s, x) { return s + x.e; }, 0), k = (x1 - x0 - 2 * airW) / Math.max(0.3, tot), xs = [x0], x = x0;
      L.forEach(function (cc) { var wd = cc.cv ? airW : cc.e * k; cc.x0 = x; cc.x1 = x + wd; x += wd; });
      L.forEach(function (cc) { c.fillStyle = cc.col; c.fillRect(cc.x0, y0, cc.x1 - cc.x0, y1 - y0); if (!cc.cv && cc.x1 - cc.x0 > 2) { c.strokeStyle = '#94A3B8'; c.lineWidth = 1; c.strokeRect(cc.x0, y0, cc.x1 - cc.x0, y1 - y0); } });
      /* profil de température : chute de température proportionnelle à la résistance de chaque couche (comme U = R I) */
      function Y(T) { return y0 + 10 + (Ti - T) / (Ti - Math.min(-10, Te)) * (y1 - y0 - 30); }
      var T = Ti, pts = [[L[0].x0, Ti]];
      L.forEach(function (cc) { T -= Phi * cc.R; pts.push([cc.x1, T]); });
      c.strokeStyle = '#DC2626'; c.lineWidth = 2.6; c.beginPath(); pts.forEach(function (p, i) { if (i === 0) { c.moveTo(p[0], Y(p[1])); } else { c.lineTo(p[0], Y(p[1])); } }); c.stroke();
      var lastX = -1e9;   /* températures aux interfaces : on n'écrit que celles qui ne se chevauchent pas */
      pts.forEach(function (p, i) { if (i > 0 && i < pts.length - 1) { c.fillStyle = '#DC2626'; c.beginPath(); c.arc(p[0], Y(p[1]), 3.5, 0, 2 * Math.PI); c.fill(); if (p[0] - lastX > 56 && p[0] > L[0].x0 + 66 && p[0] < L[4].x1 - 40) { txt(c, fr(p[1], 1) + ' °C', p[0], Y(p[1]) - 8, '#B91C1C', '700 10.5px system-ui, sans-serif'); lastX = p[0]; } } });
      txt(c, Ti + ' °C', L[0].x0 + 4, Y(Ti) - 8, '#B91C1C', '700 11px system-ui, sans-serif', 'left'); txt(c, fr(Te, 0) + ' °C', L[4].x1 - 4, Y(Te) - 8, '#1D4ED8', '700 11px system-ui, sans-serif', 'right');
      /* flèche du flux */
      var fy = y1 - 22, fw = Math.max(3, Math.min(26, Phi / 15));
      c.fillStyle = 'rgba(234,88,12,.85)'; c.beginPath(); c.moveTo(x0 + 10, fy - fw / 2); c.lineTo(x1 - 26, fy - fw / 2); c.lineTo(x1 - 26, fy - fw / 2 - 6); c.lineTo(x1 - 8, fy); c.lineTo(x1 - 26, fy + fw / 2 + 6); c.lineTo(x1 - 26, fy + fw / 2); c.lineTo(x0 + 10, fy + fw / 2); c.closePath(); c.fill();
      txt(c, '\u03a6 = ' + nb(Phi, 3) + ' W', (x0 + x1) / 2, fy - fw / 2 - 8, '#C2410C', '700 12px system-ui, sans-serif');
      /* résistances de chaque couche */
      var rang = 0;   /* noms des couches : les couches étroites sont écrites en alternance sur deux lignes */
      L.forEach(function (cc) { var xm = (cc.x0 + cc.x1) / 2, large = cc.x1 - cc.x0 > 70, dy = large ? 0 : (rang++ % 2) * 28; if (cc.x1 - cc.x0 > 2) { txt(c, cc.n, xm, y1 + 16 + dy, '#334155', '600 10.5px system-ui, sans-serif'); txt(c, nb(cc.R, 2) + ' K/W', xm, y1 + 29 + dy, '#64748B', '10px system-ui, sans-serif'); } });
      txt(c, 'R\u209c\u2095 totale = somme des résistances = ' + nb(Rt, 3) + ' K/W', (x0 + x1) / 2, h - 10, '#0F172A', '700 12px system-ui, sans-serif');
    }
    [rE, rTe].forEach(function (r) { r.addEventListener('input', draw); });
    $$(root, 'input[name="iso"]').forEach(function (r) { r.addEventListener('change', function () { iso = r.value; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= Refroidissement d'une tasse de thé : loi de Newton ================= */
  (function () {
    var root = document.getElementById('lab-newton');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rM = $(root, '[data-p="m"]'), rH = $(root, '[data-p="h"]'), rT0 = $(root, '[data-p="T0"]'), rTe = $(root, '[data-p="Te"]'), oM = $(root, '.out-m'), oH = $(root, '.out-h'), oT0 = $(root, '.out-T0'), oTe = $(root, '.out-Te'), oTau = $(root, '.out-tau'), btn = $(root, '[data-act="play"]'), S, t = 0, run = false, last = null;
    var C = 4185, Ssurf = 0.03;
    function draw() {
      var m = +rM.value, hh = +rH.value, T0 = +rT0.value, Te = +rTe.value, tau = m * C / (hh * Ssurf), tmax = 5.5 * tau;
      oM.textContent = Math.round(m * 1000) + ' g'; oH.textContent = hh + ' W/(m²·K)'; oT0.textContent = T0 + ' °C'; oTe.textContent = Te + ' °C'; oTau.textContent = nb(tau / 60, 3) + ' min';
      var c = S.ctx, w = S.w, h = S.h, L = 52, R = w - 110, T = 16, B = h - 36, Tlo = Math.min(T0, Te) - 5, Thi = Math.max(T0, Te) + 5;
      function X(s) { return L + s / tmax * (R - L); }
      function Y(th) { return B - (th - Tlo) / (Thi - Tlo) * (B - T); }
      function Tt(s) { return (T0 - Te) * Math.exp(-s / tau) + Te; }
      c.clearRect(0, 0, w, h);
      var xs = [], ys = [], st = tmax / 60 > 50 ? 30 : (tmax / 60 > 20 ? 10 : 5);
      for (var mn = 0; mn * 60 <= tmax; mn += st) { xs.push([X(mn * 60), String(mn)]); }
      for (var th = Math.ceil(Tlo / 10) * 10; th <= Thi; th += 10) { ys.push([Y(th), String(th)]); }
      axes(c, L, R, T, B, xs, ys, 't (min) \u2192', 'T (°C) \u2192');
      /* température extérieure, tangente à l'origine, τ et 5τ */
      c.setLineDash([5, 4]); c.strokeStyle = '#2563EB'; c.lineWidth = 1.4; c.beginPath(); c.moveTo(L, Y(Te)); c.lineTo(R, Y(Te)); c.stroke();
      c.strokeStyle = '#94A3B8'; c.beginPath(); c.moveTo(X(0), Y(T0)); c.lineTo(X(tau), Y(Te)); c.stroke();
      c.strokeStyle = '#7C3AED'; c.beginPath(); c.moveTo(X(tau), B); c.lineTo(X(tau), Y(Tt(tau))); c.lineTo(L, Y(Tt(tau))); c.stroke();
      c.strokeStyle = '#059669'; c.beginPath(); c.moveTo(X(5 * tau), T); c.lineTo(X(5 * tau), B); c.stroke(); c.setLineDash([]);
      txt(c, 'T\u2091\u2093\u209c', R + 6, Y(Te) + 4, '#2563EB', '700 12px system-ui, sans-serif', 'left');
      txt(c, '\u03c4', X(tau) + 9, B - 8, '#7C3AED', '700 14px Georgia, serif', 'left'); txt(c, '5\u03c4', X(5 * tau) + 4, T + 12, '#059669', '700 12px Georgia, serif', 'left');
      txt(c, '63 % de l\u2019écart', X(tau) + 6, Y(Tt(tau)) - 8, '#7C3AED', '600 10.5px system-ui, sans-serif', 'left');
      c.strokeStyle = '#DC2626'; c.lineWidth = 2.6; c.beginPath();
      for (var k = 0; k <= 200; k++) { var s = tmax * k / 200; if (k === 0) { c.moveTo(X(s), Y(Tt(s))); } else { c.lineTo(X(s), Y(Tt(s))); } }
      c.stroke();
      var tn = Math.min(t, tmax); c.fillStyle = '#DC2626'; c.beginPath(); c.arc(X(tn), Y(Tt(tn)), 6, 0, 2 * Math.PI); c.fill();
      /* tasse dont la couleur suit la température */
      var cx = w - 52, cy = h / 2 + 10, Tc = Tt(tn);
      if (T0 >= Te) {   /* thé chaud : une tasse */
        c.fillStyle = chaud((Tc - 0) / 100); rr(c, cx - 26, cy - 30, 52, 60, 10); c.fill(); c.strokeStyle = '#334155'; c.lineWidth = 2; c.stroke();
        c.beginPath(); c.arc(cx + 28, cy, 12, -Math.PI / 2, Math.PI / 2); c.stroke();
      } else {   /* thé glacé : un verre, des glaçons tant qu'il est froid, de la buée sur la paroi */
        c.fillStyle = 'rgba(234,179,8,.55)'; c.beginPath(); c.moveTo(cx - 24, cy - 24); c.lineTo(cx - 19, cy + 32); c.lineTo(cx + 19, cy + 32); c.lineTo(cx + 24, cy - 24); c.closePath(); c.fill();
        if (Tc < 10) { c.fillStyle = 'rgba(255,255,255,.8)'; c.strokeStyle = 'rgba(148,163,184,.9)'; c.lineWidth = 1; [[-14, -20], [2, -16], [-6, -4]].forEach(function (g2) { rr(c, cx + g2[0], cy + g2[1], 13, 12, 3); c.fill(); c.stroke(); }); }
        if (Tc < Te - 3) { c.fillStyle = 'rgba(255,255,255,.75)'; for (var d = 0; d < 9; d++) { c.beginPath(); c.arc(cx - 20 + (d * 7) % 40, cy - 10 + (d * 13) % 38, 1.6, 0, 2 * Math.PI); c.fill(); } }
        c.strokeStyle = '#334155'; c.lineWidth = 2; c.beginPath(); c.moveTo(cx - 26, cy - 34); c.lineTo(cx - 20, cy + 34); c.lineTo(cx + 20, cy + 34); c.lineTo(cx + 26, cy - 34); c.stroke();
      }
      if (T0 >= Te && Tc > 45) { c.strokeStyle = 'rgba(148,163,184,.7)'; c.lineWidth = 2; for (var v = 0; v < 3; v++) { var vx = cx - 12 + v * 12; c.beginPath(); c.moveTo(vx, cy - 36); c.bezierCurveTo(vx - 6, cy - 46, vx + 6, cy - 54, vx, cy - 64 - 3 * Math.sin(tn / tau * 20 + v)); c.stroke(); } }
      txt(c, fr(Tc, 1) + ' °C', cx, cy + 50, '#1E293B', '700 12px system-ui, sans-serif'); txt(c, 't = ' + nb(tn / 60, 3) + ' min', cx, cy + 65, '#64748B', '11px system-ui, sans-serif');
    }
    function loop(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (run) { var tau = +rM.value * C / (+rH.value * Ssurf); t += dt * tau / 2.2; if (t >= 5.5 * tau) { t = 5.5 * tau; run = false; btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; } draw(); }
      requestAnimationFrame(loop);
    }
    btn.addEventListener('click', function () { var tau = +rM.value * C / (+rH.value * Ssurf); if (t >= 5.5 * tau) { t = 0; } run = !run; btn.innerHTML = run ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lancer'; });
    [rM, rH, rT0, rTe].forEach(function (r) { r.addEventListener('input', function () { t = 0; run = false; btn.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Lancer'; draw(); }); });
    $$(root, '[data-preset]').forEach(function (b) { b.addEventListener('click', function () { var v = b.getAttribute('data-preset').split(','); rT0.value = v[0]; rTe.value = v[1]; t = 0; run = true; btn.innerHTML = '<i class="fa-solid fa-pause"></i>&nbsp; Pause'; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup); requestAnimationFrame(loop);
  })();
  /* ================= Bilan radiatif de la Terre : modèle à une couche ================= */
  (function () {
    var root = document.getElementById('lab-terre');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rA = $(root, '[data-p="A"]'), rAl = $(root, '[data-p="al"]'), oA = $(root, '.out-A'), oAl = $(root, '.out-al'), oT = $(root, '.out-T'), S, etoiles = [];
    var PHI = 340.4, SIG = 5.67e-8;
    for (var e = 0; e < 90; e++) { etoiles.push([Math.random(), Math.random() * 0.6, 0.4 + Math.random() * 0.6]); }
    function pastille(c, s2, x, y, col, align) {   /* étiquette dans une pastille sombre, lisible sur le ciel */
      c.save(); c.font = '700 11.5px system-ui, sans-serif'; var lw = c.measureText(s2).width + 14, xx = align === 'left' ? x : (align === 'right' ? x - lw : x - lw / 2);
      xx = Math.max(4, Math.min(S.w - lw - 4, xx));
      c.fillStyle = 'rgba(15,23,42,.78)'; rr(c, xx, y - 13, lw, 19, 9); c.fill(); c.strokeStyle = col; c.lineWidth = 1.2; c.stroke();
      c.fillStyle = col; c.textAlign = 'left'; c.fillText(s2, xx + 7, y + 1); c.restore();
    }
    function fleche(c, x1, y1, x2, y2, wd, c1, c2) {
      if (wd < 0.6) { return; }
      var dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L, hw = Math.max(wd, 2.5) / 2, hl = 10 + wd * 0.45, hw2 = hw + 5 + wd * 0.15;
      var g = c.createLinearGradient(x1, y1, x2, y2); g.addColorStop(0, c1); g.addColorStop(1, c2);
      c.fillStyle = g; c.beginPath();
      c.moveTo(x1 - uy * hw, y1 + ux * hw); c.lineTo(x2 - ux * hl - uy * hw, y2 - uy * hl + ux * hw); c.lineTo(x2 - ux * hl - uy * hw2, y2 - uy * hl + ux * hw2); c.lineTo(x2, y2);
      c.lineTo(x2 - ux * hl + uy * hw2, y2 - uy * hl - ux * hw2); c.lineTo(x2 - ux * hl + uy * hw, y2 - uy * hl - ux * hw); c.lineTo(x1 + uy * hw, y1 - ux * hw); c.closePath(); c.fill();
    }
    function draw() {
      var A = +rA.value, al = +rAl.value, phE = 2 * (1 - A) / (2 - al) * PHI, T = Math.pow(phE / SIG, 0.25), Tr = Math.round(T);
      oA.textContent = fr(A, 2); oAl.textContent = fr(al, 2); oT.innerHTML = Tr + '&nbsp;K, soit ' + fr(Tr - 273, 0) + '&nbsp;°C';
      var c = S.ctx, w = S.w, h = S.h, k = 0.075;
      /* ciel étoilé et Soleil */
      var sky = c.createLinearGradient(0, 0, 0, h); sky.addColorStop(0, '#020617'); sky.addColorStop(1, '#1E3A8A'); c.fillStyle = sky; c.fillRect(0, 0, w, h);
      etoiles.forEach(function (st) { c.fillStyle = 'rgba(255,255,255,' + (0.25 + 0.5 * st[2]) + ')'; c.fillRect(st[0] * w, st[1] * h, 1.5, 1.5); });
      var sx = 26, sy = 22, hs = c.createRadialGradient(sx, sy, 6, sx, sy, 70); hs.addColorStop(0, 'rgba(254,240,138,.9)'); hs.addColorStop(0.35, 'rgba(250,204,21,.45)'); hs.addColorStop(1, 'rgba(250,204,21,0)'); c.fillStyle = hs; c.beginPath(); c.arc(sx, sy, 70, 0, 2 * Math.PI); c.fill();
      /* Terre (vue en courbe) et atmosphère, qui suit la courbure */
      var R = w * 1.6, cx = w / 2, cy = h - 64 + R;
      function ysurf(x) { return cy - Math.sqrt(R * R - (x - cx) * (x - cx)); }
      var ga = c.createRadialGradient(cx, cy, R, cx, cy, R + 120); ga.addColorStop(0, 'rgba(147,197,253,' + (0.15 + 0.5 * al) + ')'); ga.addColorStop(1, 'rgba(147,197,253,0)');
      c.fillStyle = ga; c.beginPath(); c.arc(cx, cy, R + 120, Math.PI, 2 * Math.PI); c.fill();
      c.strokeStyle = 'rgba(191,219,254,' + (0.25 + 0.5 * al) + ')'; c.lineWidth = 1; c.setLineDash([4, 5]); c.beginPath(); c.arc(cx, cy, R + 70, Math.PI * 1.02, Math.PI * 1.98); c.stroke(); c.setLineDash([]);
      var gt = c.createRadialGradient(cx, cy - R, 10, cx, cy - R, w * 0.8); gt.addColorStop(0, chaud(Math.max(0, (T - 230) / 95))); gt.addColorStop(0.45, '#15803D'); gt.addColorStop(1, '#1E3A8A');
      c.fillStyle = gt; c.beginPath(); c.arc(cx, cy, R, Math.PI, 2 * Math.PI); c.fill();
      function yatm(x, d) { return cy - Math.sqrt((R + d) * (R + d) - (x - cx) * (x - cx)); }
      var xa = (w * 0.33 + w * 0.58) / 2 + 12;   /* légende de l'atmosphère, dans l'espace libre entre les flèches */
      c.save(); c.font = '600 10.5px system-ui, sans-serif'; c.textAlign = 'center'; c.fillStyle = 'rgba(191,219,254,.95)'; c.fillText('atmosphère : absorbe', xa, yatm(xa, 70) - 22); c.fillText('une part \u03b1 de l\u2019infrarouge', xa, yatm(xa, 70) - 8); c.restore();
      /* flux : largeur des flèches proportionnelle au flux */
      var x1 = w * 0.17, x2 = w * 0.33, x3 = w * 0.58, x4 = w * 0.82;
      fleche(c, x1 - 40, 14, x1 + 10, ysurf(x1 + 10) - 2, PHI * k, 'rgba(254,240,138,.95)', 'rgba(250,204,21,.95)');
      fleche(c, x1 + 32, ysurf(x1 + 32) - 4, x2, 14, A * PHI * k, 'rgba(250,204,21,.85)', 'rgba(254,249,195,.95)');
      fleche(c, x3, ysurf(x3) - 3, x3, yatm(x3, 70) + 4, phE * k, 'rgba(239,68,68,.95)', 'rgba(248,113,113,.95)');
      fleche(c, x3, yatm(x3, 70) - 4, x3, 14, phE * (1 - al) * k, 'rgba(248,113,113,.95)', 'rgba(254,202,202,.95)');
      fleche(c, x4, yatm(x4, 70) - 4, x4, 14, phE * al / 2 * k, 'rgba(249,115,22,.95)', 'rgba(254,215,170,.95)');
      fleche(c, x4, yatm(x4, 70) + 4, x4, ysurf(x4) - 3, phE * al / 2 * k, 'rgba(249,115,22,.95)', 'rgba(251,146,60,.95)');
      pastille(c, '\u03c6\u209b = ' + nb(PHI, 4) + ' W/m²', x1 + 18, 40, '#FDE047', 'left');
      pastille(c, 'A\u03c6\u209b = ' + Math.round(A * PHI), x2 + 12, 64, '#FEF9C3', 'left');
      pastille(c, '\u03c6\u2091 = ' + Math.round(phE), x3 + phE * k / 2 + 8, (ysurf(x3) + yatm(x3, 70)) / 2 + 4, '#FCA5A5', 'left');
      if (phE * (1 - al) >= 1) { pastille(c, '(1\u2212\u03b1)\u03c6\u2091 = ' + Math.round(phE * (1 - al)), x3 + Math.max(phE * (1 - al) * k, 3) / 2 + 8, 70, '#FECACA', 'left'); }   /* deux hauteurs différentes : pas de chevauchement */
      if (phE * al / 2 >= 1) { pastille(c, '\u03b1\u03c6\u2091/2 = ' + Math.round(phE * al / 2), x4 + phE * al / 2 * k / 2 + 8, 34, '#FED7AA', 'left');
        pastille(c, 'vers le sol : ' + Math.round(phE * al / 2), x4 - phE * al / 2 * k / 2 - 8, (yatm(x4, 70) + ysurf(x4)) / 2 + 4, '#FDBA74', 'right'); }
      /* température de surface */
      c.save(); c.font = '800 13.5px system-ui, sans-serif'; var lab = 'température de surface : ' + Tr + ' K (' + fr(Tr - 273, 0) + ' °C)', lw = c.measureText(lab).width + 22;
      c.fillStyle = 'rgba(255,255,255,.92)'; rr(c, cx - lw / 2, h - 34, lw, 26, 13); c.fill(); c.fillStyle = Tr > 280 ? '#B91C1C' : (Tr > 265 ? '#B45309' : '#1D4ED8'); c.textAlign = 'center'; c.fillText(lab, cx, h - 16); c.restore();
    }
    [rA, rAl].forEach(function (r) { r.addEventListener('input', draw); });
    $$(root, '[data-preset]').forEach(function (b) { b.addEventListener('click', function () { var v = b.getAttribute('data-preset').split(','); rA.value = v[0]; rAl.value = v[1]; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
})();
</script>
