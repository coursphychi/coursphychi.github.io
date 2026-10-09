+++
title = "Équilibre chimique"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Transformation non totale&nbsp;: l'équilibre chimique {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Transformation non totale</p>
<p>Si une transformation chimique est non totale, l'avancement final est <span class="imp nt-hole">inférieur à l'avancement maximal</span>&nbsp;: $x_\mathrm{f} &lt; x_\mathrm{max}$.</p>
<p>En appelant <span class="imp">taux d'avancement final</span> le rapport $\tau=\dfrac{x_\mathrm{f}}{x_\mathrm{max}}$, cela revient à&nbsp;:</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Transformation non totale</p>
<p class="nt-f-math">$$\text{transformation non totale} \;\Leftrightarrow\; x_\mathrm{f} &lt; x_\mathrm{max} \;\Leftrightarrow\; \tau &lt; 1$$</p>
<div class="nt-f-units"><span>une transformation totale correspond à <b>$\tau = 1$</b></span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Dans l'état final d'une transformation non totale, l'ensemble des réactifs et des produits de la réaction <span class="imp nt-hole">coexistent</span>, et leurs quantités de matière <span class="imp nt-hole">n'évoluent plus</span> dans le temps.</p>
<p>C'est la caractéristique d'un état d'<span class="imp nt-hole">équilibre chimique</span>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice</p>
<p>Le fluorure d'hydrogène $\ce{HF}$ réagit avec l'eau selon la réaction d'équation&nbsp;:</p>
<p class="nt-center">$\ce{HF(aq) + H2O(l) <=> F-(aq) + H3O+(aq)}$</p>
<p>Une solution d'acide fluorhydrique est préparée en ajoutant du fluorure d'hydrogène ($n_0=\pu{1,0 mmol}$) dans de l'eau distillée pour former une solution de volume $V=\pu{1,0 L}$. Le pH de la solution vaut 3,2.</p>
<p>Calculer le taux d'avancement final $\tau$ de cette transformation et en déduire son caractère total ou non total.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li>
<p>On dresse le tableau d'avancement de la réaction&nbsp;:</p>
<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>État</th><th>Avancement</th><th>$\ce{HF}$</th><th>$\ce{H2O}$</th><th>$\ce{F-}$</th><th>$\ce{H3O+}$</th></tr></thead>
<tbody>
<tr><td>initial</td><td>$0$</td><td>$n_0$</td><td>excès</td><td>$0$</td><td>$0$</td></tr>
<tr><td>intermédiaire</td><td>$x$</td><td>$n_0-x$</td><td>excès</td><td>$x$</td><td>$x$</td></tr>
<tr><td>final</td><td>$x_\mathrm{f}$</td><td>$n_0-x_\mathrm{f}$</td><td>excès</td><td>$x_\mathrm{f}$</td><td>$x_\mathrm{f}$</td></tr>
</tbody>
</table>
</div>
</li>
<li><p>Si la réaction était totale, $\ce{HF}$ serait le réactif limitant&nbsp;: $n_0-x_\mathrm{max} = 0$, d'où $x_\mathrm{max}=n_0=\pu{1,0E-3 mol}$.</p></li>
<li><p>Le pH donne la concentration finale en ions oxonium&nbsp;: $\ce{[H3O+]}_\mathrm{f}=c°\times 10^{-\mathrm{pH}}=\pu{6,3E-4 mol*L-1}$, d'où $n_\mathrm{f}(\ce{H3O+})=\ce{[H3O+]}_\mathrm{f}\times V = \pu{6,3E-4 mol}$.</p></li>
<li><p>D'après le tableau d'avancement, cette quantité de matière finale est aussi l'avancement final&nbsp;: $x_\mathrm{f} = \pu{6,3E-4 mol}$.</p></li>
<li><p>Le taux d'avancement vaut donc $\tau = \dfrac{x_\mathrm{f}}{x_\mathrm{max}} = \dfrac{6{,}3\times10^{-4}}{1{,}0\times10^{-3}} = 63\ \%$. Comme $\tau &lt; 1$, la transformation n'est pas totale.</p></li>
</ol>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">L'acide fluorhydrique, un acide faible… mais redoutable</span></summary>
<div class="nt-d-body">
<p>Bien que ce soit un acide faible (c'est ainsi que l'on appelle un acide qui ne se dissocie pas totalement dans l'eau), l'acide fluorhydrique est extrêmement dangereux&nbsp;: il traverse la peau, et les ions fluorure s'attaquent au calcium de l'organisme, jusque dans les os. Il est aussi l'un des rares acides capables d'attaquer le verre, ce qui sert à le graver. Dans la réalité, ces processus seraient bien plus lents (et plus dangereux) que dans la série où on le voit «&nbsp;dissoudre&nbsp;» un corps.</p>
<p>Une technique funéraire voisine existe bel et bien, mais avec une base&nbsp;: l'hydrolyse alcaline, appelée «&nbsp;aquamation&nbsp;», alternative à l'inhumation et à la crémation qui émettrait moins de gaz à effet de serre. Elle sert aussi à éliminer les carcasses d'animaux malades.</p>
<p><a href="https://www.youtube.com/watch?v=hd3EAzJ_McA" target="_blank" rel="noopener">Voir l'extrait vidéo</a>.</p>
</div>
</details>

### Un équilibre dynamique {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Les deux sens de la réaction</p>
<p>L'état d'équilibre est dû à la compensation entre la réaction dans son <span class="imp nt-hole">sens direct</span>, $\ce{\text{réactifs} -> \text{produits}}$, et la réaction dans le <span class="imp nt-hole">sens indirect</span>, $\ce{\text{produits} -> \text{réactifs}}$.</p>
<p>On modélise ce double sens de la réaction par une double flèche à simple pointe&nbsp;: $\ce{\text{réactifs} <=> \text{produits}}$.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>À l'équilibre</p>
<p>La vitesse de disparition d'un réactif A dans le sens direct est égale à sa vitesse de formation dans le sens indirect. La variation globale de sa concentration est donc nulle&nbsp;:</p>
<p class="nt-center">$\dfrac{\mathrm{d}\ce{[A]}}{\mathrm{d}t}=-v_\text{direct}+v_\text{indirect}=0 \quad\Rightarrow\quad \ce{[A]}=\mathrm{cte}$</p>
</div>

<div class="nt-lab" id="lab-dyn">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Deux réactions opposées qui finissent par se compenser</p>
<p class="nt-note">Réaction modèle $\ce{A <=> B}$, avec une vitesse $k_1\ce{[A]}$ dans le sens direct et $k_2\ce{[B]}$ dans le sens indirect, en partant de A seul.</p>
<div class="nt-lab-pair">
<figure><canvas class="c1" style="height:240px; background:#fff;" aria-label="Concentrations de A et de B au cours du temps"></canvas><figcaption>Concentrations</figcaption></figure>
<figure><canvas class="c2" style="height:240px; background:#fff;" aria-label="Vitesses des réactions directe et indirecte au cours du temps"></canvas><figcaption>Vitesses des deux réactions opposées</figcaption></figure>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">$k_1$ (sens direct)&nbsp;: <b class="out-k1"></b><input type="range" data-p="k1" min="0.1" max="2" step="0.05" value="0.8"></label>
<label class="nt-ctrl">$k_2$ (sens indirect)&nbsp;: <b class="out-k2"></b><input type="range" data-p="k2" min="0.1" max="2" step="0.05" value="0.3"></label>
<label class="nt-ctrl">Date $t$&nbsp;: <b class="out-t"></b><input type="range" data-p="t" min="0" max="10" step="0.1" value="1"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$Q_r = \ce{[B]}/\ce{[A]}$ = <b class="out-q"></b></span><span>valeur finale $k_1/k_2$ = <b class="out-k"></b></span></div>
<p class="nt-note">Au début, seule la réaction directe a lieu. Puis la réaction indirecte s'accélère à mesure que B se forme&nbsp;: quand les deux vitesses sont égales, les concentrations ne varient plus. L'équilibre est atteint, mais les deux réactions continuent.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>On parle d'<span class="imp nt-hole">équilibre dynamique</span>&nbsp;: microscopiquement, les deux réactions opposées continuent à se faire, mais macroscopiquement, leurs effets se compensent.</p>
</div>

## Quotient de réaction {.nt-h2}

<p class="nt-lead">Soit une transformation modélisée par la réaction $\ce{\nu_A A + \nu_B B <=> \nu_C C + \nu_D D}$.</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Quotient de réaction</p>
<p class="nt-f-math">$$Q_r = \frac{a_\mathrm{C}^{\nu_\mathrm{C}}\times a_\mathrm{D}^{\nu_\mathrm{D}}}{a_\mathrm{A}^{\nu_\mathrm{A}}\times a_\mathrm{B}^{\nu_\mathrm{B}}}$$</p>
<div class="nt-f-units"><span>$Q_r$ est <b>sans dimension</b></span><span>produits au numérateur, réactifs au dénominateur</span></div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Activité d'une espèce</p>
<p>La grandeur $a_\mathrm{X}$ est l'<span class="imp nt-hole">activité</span> de l'espèce $\ce{X}$. C'est une grandeur sans dimension telle que&nbsp;:</p>
<ul class="nt-facts">
<li>$a_\mathrm{X}=\dfrac{\ce{[X]}}{c°}$ si $\ce{X}$ est un <b>soluté</b>, où $c°=\pu{1 mol*L-1}$ est la <span class="imp nt-hole">concentration standard</span>&nbsp;;</li>
<li>$a_\mathrm{X}=1$ pour le <b>solvant</b>&nbsp;;</li>
<li>$a_\mathrm{X}=1$ pour un <b>solide</b>.</li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Petit exercice</p>
<p>Dans $V=\pu{200 mL}$ d'eau distillée, on dissout totalement $m_1=\pu{0,30 g}$ d'iodure de potassium $\ce{KI}$ et $m_2=\pu{0,30 g}$ de nitrate de plomb $\ce{Pb(NO3)2}$. Les ions iodure et les ions plomb peuvent précipiter selon la réaction d'équation&nbsp;:</p>
<p class="nt-center">$\ce{Pb^2+(aq) + 2 I-(aq) <=> PbI2(s)}$</p>
<p>Exprimer et calculer le quotient de réaction initial $Q_{r,\mathrm{i}}$.</p>
<p class="nt-note">Données&nbsp;: $M(\ce{KI})=\pu{166 g*mol-1}$&nbsp;; $M(\ce{Pb(NO3)2})=\pu{331 g*mol-1}$.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>Équations de dissolution&nbsp;: $\ce{KI(s) ->[H2O] K+(aq) + I-(aq)}$ et $\ce{Pb(NO3)2(s) ->[H2O] Pb^2+(aq) + 2 NO3-(aq)}$.</p></li>
<li><p>Concentration initiale en ions iodure&nbsp;: $\ce{[I-]}_\mathrm{i} = C(\ce{KI}) = \dfrac{m_1/M(\ce{KI})}{V} = \dfrac{0{,}30/166}{0{,}200} = \pu{9,0E-3 mol*L-1}$.</p></li>
<li><p>Concentration initiale en ions plomb&nbsp;: $\ce{[Pb^{2+}]}_\mathrm{i} = C(\ce{Pb(NO3)2}) = \dfrac{0{,}30/331}{0{,}200} = \pu{4,5E-3 mol*L-1}$.</p>
<p class="nt-note">Attention aux coefficients de la dissolution&nbsp;: pour les ions nitrate, on aurait $\ce{[NO3-]}_\mathrm{i} = 2\times C(\ce{Pb(NO3)2})$.</p></li>
<li><p>Quotient de réaction initial (l'activité du solide vaut 1)&nbsp;:</p>
<p class="nt-center">$\begin{aligned} Q_{r,\mathrm{i}} &= \dfrac{a_\mathrm{i}(\ce{PbI2})}{a_\mathrm{i}(\mathrm{Pb^{2+}})\times {a_\mathrm{i}(\ce{I-})}^2} = \dfrac{1}{\dfrac{\ce{[Pb^{2+}]}_\mathrm{i}}{c°}\times \left(\dfrac{\ce{[I-]}_\mathrm{i}}{c°}\right)^2} \\[2mm] &= \dfrac{1}{4{,}5\times10^{-3}\times (9{,}0\times10^{-3})^2} = 2{,}7\times 10^{6} \end{aligned}$</p></li>
</ol>
</div>
</details>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>La pluie dorée</p>
<p>L'iodure de plomb, dissous à chaud, précipite en refroidissant sous forme de paillettes dorées. C'est le quotient de réaction de cette transformation qui a été calculé dans le petit exercice précédent.</p>
<p style="text-align:center;"><a href="https://www.youtube.com/shorts/nyoOhWLwN_g" target="_blank" rel="noopener"><i class="fa-brands fa-youtube"></i> Vidéo de l'expérience</a></p>
</div>


## Évolution spontanée {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Constante d'équilibre</p>
<p>Lorsqu'un système atteint l'équilibre chimique, son quotient de réaction prend une valeur indépendante de la composition initiale, appelée <span class="imp nt-hole">constante d'équilibre $K(T)$</span>.</p>
<p>$K(T)$ est sans unité et <span class="imp nt-hole">ne dépend que de la température</span>.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>À l'équilibre</p>
<p class="nt-f-math">$$Q_{r,\mathrm{eq}}=K(T)$$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Critère d'évolution spontanée</p>
<p>Un système chimique hors équilibre évolue spontanément de manière à <span class="imp nt-hole">rapprocher le quotient de réaction de la constante d'équilibre</span>.</p>
<ul class="nt-facts">
<li>Si <b style="color:#E11D48;">$Q_r &lt; K(T)$</b>, $Q_r$ doit augmenter&nbsp;: la réaction évolue spontanément dans le <span class="imp nt-hole">sens direct</span> (consommation des réactifs et formation des produits).</li>
<li>Si <b style="color:#2A6BC4;">$Q_r &gt; K(T)$</b>, $Q_r$ doit diminuer&nbsp;: la réaction évolue spontanément dans le <span class="imp nt-hole">sens indirect</span> (consommation des produits et formation des réactifs).</li>
<li>Si $Q_r = K(T)$, le système est à l'équilibre&nbsp;: sa composition n'évolue pas.</li>
</ul>
</div>

<div class="nt-lab" id="lab-sens">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Dans quel sens va évoluer le système&nbsp;?</p>
<p class="nt-note">Réaction modèle $\ce{A + B <=> C + D}$&nbsp;: choisissez la composition initiale et la constante d'équilibre.</p>
<canvas style="height:360px;" aria-label="Position du quotient de réaction initial par rapport à la constante d'équilibre, et compositions initiale et finale"></canvas>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-ctrls">
<label class="nt-ctrl">A initial&nbsp;: <b class="out-A"></b><input type="range" data-p="A" min="0" max="10" step="0.5" value="6"></label>
<label class="nt-ctrl">B initial&nbsp;: <b class="out-B"></b><input type="range" data-p="B" min="0" max="10" step="0.5" value="4"></label>
<label class="nt-ctrl">C initial&nbsp;: <b class="out-C"></b><input type="range" data-p="C" min="0" max="10" step="0.5" value="1"></label>
<label class="nt-ctrl">D initial&nbsp;: <b class="out-D"></b><input type="range" data-p="D" min="0" max="10" step="0.5" value="1"></label>
<label class="nt-ctrl">Constante d'équilibre $K$&nbsp;: <b class="out-K"></b><input type="range" data-p="K" min="-3" max="3" step="0.05" value="0.6"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$Q_{r,\mathrm{i}}$ = <b class="out-Q"></b></span></div>
<p class="nt-note">L'axe des quotients de réaction est en échelle logarithmique. Les compositions finales sont calculées en résolvant $Q_{r,\mathrm{eq}} = K$.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>La pluie dorée (le retour)</p>
<p>Pourquoi le iodure de plomb ne précipite-t-il qu'après refroidissement pour donner cette apparition spectaculaire de petits grains dorés&nbsp;?</p>
<ul style="margin-top:0em; margin-bottom:0.5em;">
<li>Constante d’équilibre de la de précipitation à 70°C&nbsp;: $K(70^\circ \mathrm{C})=1,2\cdot 10^{6}$</li>
<li>Constante d’équilibre de la de précipitation à 25°C&nbsp;: $K(25^\circ \mathrm{C})=1,6\cdot 10^{8}$</li>
</ul>
<p>On a choisi la composition initiale afin d'obtenir $Q_{r,\mathrm{i}} > K(70^\circ \mathrm{C})$. Le sens d'évolution spontanée est donc le sens indirect, celui de la dissolution du précipité. Le précipité étant initialement absent, le système est bloqué.</p>
<p>Mais comme $Q_{r,\mathrm{i}} < K(25^\circ \mathrm{C})$, il y a une température entre 70°C et 25°C où $Q_{r,\mathrm{i}}$ devient inférieur à la constante d'équilibre et donc où le sens d'évolution spontanée devient le sens direct&nbsp;; l'iodure de plomb commence alors à précipiter.</p>
</div>

## Description microscopique {.nt-h2}

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>C'est hors programme mais éclairant.</p>
</div>

<p class="nt-lead">Reprenons la réaction modèle $\ce{A + B <=> C + D}$, et observons-la à l'échelle des entités.</p>

<div class="nt-lab" id="lab-micro">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'équilibre, vu de près</p>
<canvas class="box" style="height:300px;" aria-label="Entités A, B, C et D qui s'agitent et réagissent lors de leurs chocs"></canvas>
<canvas class="graph" style="height:170px; margin-top:8px; background:#fff;" aria-label="Quotient de réaction au cours du temps, comparé à la constante d'équilibre"></canvas>
<div class="nt-read" aria-live="polite"><span><b style="color:#0284C7;">A</b>&nbsp;: <b class="out-A"></b></span><span><b style="color:#E11D48;">B</b>&nbsp;: <b class="out-B"></b></span><span><b style="color:#16A34A;">C</b>&nbsp;: <b class="out-C"></b></span><span><b style="color:#CA8A04;">D</b>&nbsp;: <b class="out-D"></b></span><span>$Q_r$ = <b class="out-Q"></b></span></div>
<div class="nt-ctrls">
<label class="nt-ctrl">Entités A au départ&nbsp;: <input type="range" data-p="A" min="0" max="150" step="10" value="100"></label>
<label class="nt-ctrl">Entités B au départ&nbsp;: <input type="range" data-p="B" min="0" max="150" step="10" value="60"></label>
<label class="nt-ctrl">Entités C au départ&nbsp;: <input type="range" data-p="C" min="0" max="150" step="10" value="0"></label>
<label class="nt-ctrl">Entités D au départ&nbsp;: <input type="range" data-p="D" min="0" max="150" step="10" value="0"></label>
<label class="nt-ctrl">Constante d'équilibre $K$&nbsp;: <b class="out-K"></b><input type="range" data-p="K" min="-1" max="1" step="0.05" value="0.3"></label>
</div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-note">Lors d'un choc entre A et B, la réaction directe a lieu avec une certaine probabilité&nbsp;; lors d'un choc entre C et D, la réaction inverse a lieu avec une autre probabilité. Le rapport de ces deux probabilités vaut $K$. Les autres chocs sont de simples rebonds. Les cercles violets signalent une réaction directe, les jaunes une réaction inverse.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Que mesurent $K$ et $Q_r$&nbsp;?</p>
<ul class="nt-facts">
<li>Lors d'un choc, si l'énergie dépasse un seuil d'activation, la réaction se fait&nbsp;; sinon, les entités rebondissent. <b>$K$ mesure combien de fois la réaction est plus probable dans le sens direct que dans le sens indirect</b>&nbsp;: pour $K=3$, un choc entre deux réactifs a 3 fois plus de chances de donner lieu à une réaction qu'un choc entre deux produits.</li>
<li><b>$Q_r$ mesure combien de fois il est plus probable, pour les produits, de se rencontrer que pour les réactifs</b>&nbsp;: pour $Q_r=3$, deux réactifs ont 3 fois moins de chances de s'entrechoquer que deux produits.</li>
</ul>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>D'où vient $Q_{r,\mathrm{eq}} = K$&nbsp;?</p>
<p>À l'équilibre, la réaction directe et la réaction inverse doivent se faire au même rythme. Donc&nbsp;:</p>
<p class="nt-center">(proba que deux réactifs se rencontrent) $\times$ (proba que les réactifs réagissent) $=$ (proba que deux produits se rencontrent) $\times$ (proba que les produits réagissent)</p>
<p>Ce qui peut se réécrire&nbsp;:</p>
<p class="nt-center">$\dfrac{\text{proba que deux produits se rencontrent}}{\text{proba que deux réactifs se rencontrent}} = \dfrac{\text{proba que les réactifs réagissent}}{\text{proba que les produits réagissent}}$</p>
<p>Le membre de gauche est $Q_r$, celui de droite est $K$&nbsp;: on retrouve $Q_{r,\mathrm{eq}} = K$.</p>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CA = '#0284C7', CB = '#E11D48', CC = '#16A34A', CD = '#CA8A04', CDIR = '#E11D48', CIND = '#2A6BC4';
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function nice(x) {   /* écriture adaptée : décimale ou puissance de 10 */
    if (!isFinite(x)) { return '\u221e'; }
    if (x === 0) { return '0'; }
    if (x >= 0.01 && x < 1000) { return fr(x, x < 1 ? 3 : (x < 10 ? 2 : 1)); }
    var n = Math.floor(Math.log10(x)), a = x / Math.pow(10, n);
    return fr(a, 1) + ' \u00d7 10<sup>' + String(n).replace('-', '\u2212') + '</sup>';
  }
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function canvasCtx(cv) {
    var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '700 12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.92)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  function frame(c, w, h, o) {
    var L = o.L || 54, R = w - (o.R || 16), T = o.T || 12, B = h - (o.B || 32);
    function X(v) { return L + (v - o.x0) / (o.x1 - o.x0) * (R - L); }
    function Y(v) { return B - (v - o.y0) / (o.y1 - o.y0) * (B - T); }
    c.strokeStyle = col('--line'); c.lineWidth = 1;
    for (var gy = o.y0; gy <= o.y1 + 1e-9; gy += o.dy) { c.beginPath(); c.moveTo(L, Y(gy)); c.lineTo(R, Y(gy)); c.stroke(); }
    c.strokeStyle = col('--ink'); c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
    c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'right';
    for (gy = o.y0; gy <= o.y1 + 1e-9; gy += o.dy) { c.fillText(fr(gy, o.ndy || 0), L - 5, Y(gy) + 4); }
    c.textAlign = 'center'; c.fillText(o.xl, (L + R) / 2, h - 4);
    c.save(); c.translate(12, (T + B) / 2); c.rotate(-Math.PI / 2); c.fillText(o.yl, 0, 0); c.restore();
    return { X: X, Y: Y, L: L, R: R, T: T, B: B };
  }
  function curve(c, F, f, x0, x1, color, w, dash) {
    c.strokeStyle = color; c.lineWidth = w || 2.4; c.setLineDash(dash || []); c.beginPath();
    for (var i = 0; i <= 200; i++) { var x = x0 + (x1 - x0) * i / 200; if (i === 0) { c.moveTo(F.X(x), F.Y(f(x))); } else { c.lineTo(F.X(x), F.Y(f(x))); } }
    c.stroke(); c.setLineDash([]);
  }
  /* ================= 1. L'équilibre dynamique (A ⇄ B) ================= */
  (function () {
    var root = document.getElementById('lab-dyn');
    if (!root) { return; }
    var c1 = $(root, 'canvas.c1'), c2 = $(root, 'canvas.c2'), rK1 = $(root, '[data-p="k1"]'), rK2 = $(root, '[data-p="k2"]'), rT = $(root, '[data-p="t"]');
    var o1 = $(root, '.out-k1'), o2 = $(root, '.out-k2'), oT = $(root, '.out-t'), oQ = $(root, '.out-q'), oK = $(root, '.out-k'), S1, S2, A0 = 1.0, TM = 10;
    function draw() {
      var k1 = +rK1.value, k2 = +rK2.value, t0 = +rT.value, s = k1 + k2, Aeq = A0 * k2 / s;
      function A(t) { return Aeq + (A0 - Aeq) * Math.exp(-s * t); }
      function Bc(t) { return A0 - A(t); }
      o1.textContent = fr(k1, 2) + ' s\u207b\u00b9'; o2.textContent = fr(k2, 2) + ' s\u207b\u00b9'; oT.textContent = fr(t0, 1) + ' s';
      oQ.innerHTML = nice(Bc(t0) / A(t0)); oK.innerHTML = nice(k1 / k2);
      var c = S1.ctx; c.clearRect(0, 0, S1.w, S1.h);
      var F = frame(c, S1.w, S1.h, { x0: 0, x1: TM, y0: 0, y1: 1, dy: 0.25, ndy: 2, xl: 'temps (s)', yl: 'concentration (mol\u00b7L\u207b\u00b9)' });
      curve(c, F, A, 0, TM, CA); curve(c, F, Bc, 0, TM, CB);
      txt(c, '[A]', F.R - 6, F.Y(A(TM)) - 8, CA, '700 13px system-ui, sans-serif', 'right'); txt(c, '[B]', F.R - 6, F.Y(Bc(TM)) - 8, CB, '700 13px system-ui, sans-serif', 'right');
      c.strokeStyle = 'rgba(30,41,59,.4)'; c.lineWidth = 1.2; c.setLineDash([4, 4]); c.beginPath(); c.moveTo(F.X(t0), F.T); c.lineTo(F.X(t0), F.B); c.stroke(); c.setLineDash([]);
      var g = S2.ctx; g.clearRect(0, 0, S2.w, S2.h);
      var vmax = Math.max(k1 * A0, 0.05) * 1.1;
      var G = frame(g, S2.w, S2.h, { x0: 0, x1: TM, y0: 0, y1: vmax, dy: vmax / 4, ndy: 2, xl: 'temps (s)', yl: 'vitesse (mol\u00b7L\u207b\u00b9\u00b7s\u207b\u00b9)' });
      curve(g, G, function (t) { return k1 * A(t); }, 0, TM, CDIR); curve(g, G, function (t) { return k2 * Bc(t); }, 0, TM, CIND);
      txt(g, 'sens direct (A \u2192 B)', G.L + 8, G.T + 14, CDIR, '700 12px system-ui, sans-serif', 'left');
      txt(g, 'sens indirect (B \u2192 A)', G.L + 8, G.T + 30, CIND, '700 12px system-ui, sans-serif', 'left');
      g.strokeStyle = 'rgba(30,41,59,.4)'; g.lineWidth = 1.2; g.setLineDash([4, 4]); g.beginPath(); g.moveTo(G.X(t0), G.T); g.lineTo(G.X(t0), G.B); g.stroke(); g.setLineDash([]);
    }
    [rK1, rK2, rT].forEach(function (r) { r.addEventListener('input', draw); });
    function setup() { S1 = canvasCtx(c1); S2 = canvasCtx(c2); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 2. Le critère d'évolution spontanée ================= */
  (function () {
    var root = document.getElementById('lab-sens');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rs = {}, ou = {}, rK = $(root, '[data-p="K"]'), oK = $(root, '.out-K'), oQ = $(root, '.out-Q'), msg = $(root, '.nt-msg'), S;
    ['A', 'B', 'C', 'D'].forEach(function (k) { rs[k] = $(root, '[data-p="' + k + '"]'); ou[k] = $(root, '.out-' + k); });
    function eqx(n, K) {   /* avancement final : (C+x)(D+x) = K (A−x)(B−x), x entre −min(C,D) et min(A,B) */
      var lo = -Math.min(n.C, n.D), hi = Math.min(n.A, n.B);
      function f(x) { return (n.C + x) * (n.D + x) - K * (n.A - x) * (n.B - x); }
      for (var i = 0; i < 80; i++) { var m = (lo + hi) / 2; if (f(m) > 0) { hi = m; } else { lo = m; } }
      return (lo + hi) / 2;
    }
    function draw() {
      var n = {}; ['A', 'B', 'C', 'D'].forEach(function (k) { n[k] = +rs[k].value; ou[k].textContent = fr(n[k], 1) + ' mmol'; });
      var K = Math.pow(10, +rK.value), num = n.C * n.D, den = n.A * n.B, Q = den === 0 ? (num === 0 ? NaN : Infinity) : num / den;
      oK.innerHTML = nice(K); oQ.innerHTML = isNaN(Q) ? 'indéterminé' : nice(Q);
      var x = (den === 0 && num === 0) ? 0 : eqx(n, K), c = S.ctx, w = S.w, h = S.h;
      c.clearRect(0, 0, w, h);
      /* axe logarithmique des quotients de réaction */
      var L = 40, R = w - 40, yA = 58;
      function X(v) { var l = Math.log10(v); l = Math.max(-4, Math.min(4, l)); return L + (l + 4) / 8 * (R - L); }
      c.strokeStyle = col('--ink'); c.lineWidth = 2; c.beginPath(); c.moveTo(L, yA); c.lineTo(R, yA); c.stroke();
      c.strokeStyle = col('--ink'); c.lineWidth = 1;
      for (var p = -4; p <= 4; p++) { var big = p % 2 === 0; c.beginPath(); c.moveTo(X(Math.pow(10, p)), yA - (big ? 6 : 3)); c.lineTo(X(Math.pow(10, p)), yA + (big ? 6 : 3)); c.stroke(); }
      for (p = -4; p <= 4; p += 2) { txt(c, '10' + ['\u207b\u2074', '', '\u207b\u00b2', '', '\u2070', '', '\u00b2', '', '\u2074'][p + 4], X(Math.pow(10, p)), yA + 30, col('--slate'), '600 11px system-ui, sans-serif'); }   /* sous la flèche */
      txt(c, 'Q\u1d63', R + 14, yA + 4, col('--ink'), 'italic 700 14px Georgia, serif');
      var xK = X(K);
      c.fillStyle = '#7C3AED'; c.beginPath(); c.moveTo(xK, yA - 6); c.lineTo(xK - 7, yA - 20); c.lineTo(xK + 7, yA - 20); c.closePath(); c.fill();
      txt(c, 'K', xK, yA - 26, '#7C3AED', 'italic 700 15px Georgia, serif');
      if (!isNaN(Q)) {
        var xQ = isFinite(Q) && Q > 0 ? X(Q) : (Q === 0 ? L : R);
        c.fillStyle = col('--ink'); c.beginPath(); c.arc(xQ, yA, 6, 0, 2 * Math.PI); c.fill();
        var dxl = Math.abs(xQ - xK) < 28 ? (xQ < xK ? -16 : 16) : 0;   /* décalée si elle tombe sur K */
        txt(c, 'Q\u1d63,\u1d62', xQ + dxl, yA - 14, col('--ink'), 'italic 700 13px Georgia, serif');
        if (Math.abs(xQ - xK) > 10) {
          var dir = xK > xQ ? 1 : -1, yArr = yA + 10, colr = dir > 0 ? CDIR : CIND;
          c.strokeStyle = colr; c.fillStyle = colr; c.lineWidth = 3; c.beginPath(); c.moveTo(xQ, yArr); c.lineTo(xK - dir * 10, yArr); c.stroke();
          c.beginPath(); c.moveTo(xK, yArr); c.lineTo(xK - dir * 12, yArr - 6); c.lineTo(xK - dir * 12, yArr + 6); c.closePath(); c.fill();
        }
      }
      /* compositions initiale et finale */
      var top = 120, bh = h - top - 40, bw = (w - 120) / 8, keys = ['A', 'B', 'C', 'D'], cols = [CA, CB, CC, CD], mx = 12;
      var fin = { A: n.A - x, B: n.B - x, C: n.C + x, D: n.D + x };
      [['état initial', n, 50], ['état final (équilibre)', fin, 50 + 4 * bw + 30]].forEach(function (blk) {
        txt(c, blk[0], blk[2] + 2 * bw - 6, top - 6, col('--slate'), '700 12px system-ui, sans-serif');
        keys.forEach(function (k, i) {
          var x0 = blk[2] + i * bw, v = Math.max(0, blk[1][k]), hh = v / mx * bh;
          c.fillStyle = '#E2E8F0'; c.fillRect(x0 + 4, top + 4, bw - 14, bh);
          c.fillStyle = cols[i]; c.fillRect(x0 + 4, top + 4 + bh - hh, bw - 14, hh);
          txt(c, k, x0 + bw / 2 - 3, top + bh + 22, cols[i], '700 14px system-ui, sans-serif');
          txt(c, fr(v, 2), x0 + bw / 2 - 3, top + bh - hh - 2, col('--ink'), '600 11px system-ui, sans-serif');
        });
      });
      if (isNaN(Q)) { msg.innerHTML = 'Sans réactifs ni produits en quantité suffisante, le quotient de réaction n\u2019est pas défini.'; }
      else if (Math.abs(Math.log10(Q) - Math.log10(K)) < 0.02) { msg.innerHTML = '<b>Q<sub>r,i</sub> = K</b> : le système est déjà à l\u2019équilibre, sa composition n\u2019évolue pas.'; }
      else if (Q < K) { msg.innerHTML = '<b style="color:' + CDIR + ';">Q<sub>r,i</sub> &lt; K</b> : le système évolue dans le <b>sens direct</b> ; les réactifs A et B sont consommés, les produits C et D formés, jusqu\u2019à ce que Q<sub>r</sub> atteigne K.'; }
      else { msg.innerHTML = '<b style="color:' + CIND + ';">Q<sub>r,i</sub> &gt; K</b> : le système évolue dans le <b>sens indirect</b> ; les produits C et D sont consommés, les réactifs A et B formés, jusqu\u2019à ce que Q<sub>r</sub> atteigne K.'; }
    }
    ['A', 'B', 'C', 'D'].forEach(function (k) { rs[k].addEventListener('input', draw); }); rK.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 3. Description microscopique ================= */
  (function () {
    var root = document.getElementById('lab-micro');
    if (!root) { return; }
    var cv = $(root, 'canvas.box'), cg = $(root, 'canvas.graph'), rs = {}, ou = {}, rK = $(root, '[data-p="K"]'), oK = $(root, '.out-K'), oQ = $(root, '.out-Q');
    var btn = $(root, '[data-act="play"]'), rst = $(root, '[data-act="reset"]'), S, SG, P = [], hist = [], t = 0, playing = !RM, visible = true, last = null, R = 4, SP = 70, fx = [];
    var COLS = { A: CA, B: CB, C: CC, D: CD };
    ['A', 'B', 'C', 'D'].forEach(function (k) { rs[k] = $(root, '[data-p="' + k + '"]'); ou[k] = $(root, '.out-' + k); });
    function spawn(type) { var a = Math.random() * 2 * Math.PI; return { x: R + Math.random() * (S.w - 2 * R), y: R + Math.random() * (S.h - 2 * R), vx: SP * Math.cos(a), vy: SP * Math.sin(a), t: type }; }
    function reset() { P = []; hist = []; t = 0; fx = []; ['A', 'B', 'C', 'D'].forEach(function (k) { for (var i = 0; i < +rs[k].value; i++) { P.push(spawn(k)); } }); }
    function counts() { var n = { A: 0, B: 0, C: 0, D: 0 }; P.forEach(function (p) { n[p.t]++; }); return n; }
    function Kv() { return Math.pow(10, +rK.value); }
    function phys(dt) {
      var w = S.w, h = S.h, K = Kv(), pf = K / (1 + K), pr = 1 / (1 + K);   /* le rapport des probabilités de réaction vaut K */
      P.forEach(function (p) {
        p.x += p.vx * dt; p.y += p.vy * dt;
        if (p.x < R) { p.x = R; p.vx = Math.abs(p.vx); } if (p.x > w - R) { p.x = w - R; p.vx = -Math.abs(p.vx); }
        if (p.y < R) { p.y = R; p.vy = Math.abs(p.vy); } if (p.y > h - R) { p.y = h - R; p.vy = -Math.abs(p.vy); }
      });
      for (var i = 0; i < P.length; i++) {
        for (var j = i + 1; j < P.length; j++) {
          var a = P[i], b = P[j], dx = b.x - a.x, dy = b.y - a.y, d2 = dx * dx + dy * dy;
          if (d2 > 4 * R * R || d2 === 0) { continue; }
          var d = Math.sqrt(d2), nx = dx / d, ny = dy / d, rv = (a.vx - b.vx) * nx + (a.vy - b.vy) * ny;
          if (rv <= 0) { continue; }
          var pair = a.t + b.t;
          if ((pair === 'AB' || pair === 'BA') && Math.random() < pf) { a.t = 'C'; b.t = 'D'; fx.push({ x: (a.x + b.x) / 2, y: (a.y + b.y) / 2, r: 0, c: '232,121,249' }); }
          else if ((pair === 'CD' || pair === 'DC') && Math.random() < pr) { a.t = 'A'; b.t = 'B'; fx.push({ x: (a.x + b.x) / 2, y: (a.y + b.y) / 2, r: 0, c: '253,224,71' }); }
          /* dans tous les cas, les deux entités s'éloignent l'une de l'autre : sinon, des produits tout juste formés
             se heurteraient de nouveau au pas suivant et pourraient redonner aussitôt les réactifs (ce qui fausserait le rapport K) */
          a.vx -= rv * nx; a.vy -= rv * ny; b.vx += rv * nx; b.vy += rv * ny;
          var ov = (2 * R - d) / 2; a.x -= nx * ov; a.y -= ny * ov; b.x += nx * ov; b.y += ny * ov;
        }
      }
    }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, n = counts(), K = Kv(), Q = (n.A * n.B) ? n.C * n.D / (n.A * n.B) : Infinity;
      c.fillStyle = '#1A0B14'; c.fillRect(0, 0, w, h);
      P.forEach(function (p) { c.fillStyle = COLS[p.t]; c.beginPath(); c.arc(p.x, p.y, R, 0, 2 * Math.PI); c.fill(); });
      fx = fx.filter(function (f) { return f.r < 26; });
      fx.forEach(function (f) { c.strokeStyle = 'rgba(' + f.c + ',' + (1 - f.r / 26) + ')'; c.lineWidth = 1.5; c.beginPath(); c.arc(f.x, f.y, f.r, 0, 2 * Math.PI); c.stroke(); f.r += 1.2; });
      oK.innerHTML = nice(K); oQ.innerHTML = nice(Q);
      ['A', 'B', 'C', 'D'].forEach(function (k) { ou[k].textContent = n[k]; });
      var g = SG.ctx, W = SG.w, H = SG.h; g.clearRect(0, 0, W, H);
      var L = 54, Rr = W - 14, T = 12, B = H - 28, tm = Math.max(20, t);
      function GX(s) { return L + s / tm * (Rr - L); }
      function GY(v) { var l = Math.max(-2, Math.min(2, Math.log10(v))); return B - (l + 2) / 4 * (B - T); }
      g.strokeStyle = col('--ink'); g.lineWidth = 1; g.beginPath(); g.moveTo(L, T); g.lineTo(L, B); g.lineTo(Rr, B); g.stroke();
      [-2, -1, 0, 1, 2].forEach(function (p) { g.fillStyle = col('--muted'); g.font = '11px system-ui, sans-serif'; g.textAlign = 'right'; g.fillText(['0,01', '0,1', '1', '10', '100'][p + 2], L - 5, GY(Math.pow(10, p)) + 4); });
      g.textAlign = 'center'; g.fillText('temps', (L + Rr) / 2, H - 6);
      g.save(); g.translate(12, (T + B) / 2); g.rotate(-Math.PI / 2); g.fillText('Q\u1d63 (échelle log.)', 0, 0); g.restore();
      g.strokeStyle = '#7C3AED'; g.setLineDash([6, 4]); g.lineWidth = 1.8; g.beginPath(); g.moveTo(L, GY(K)); g.lineTo(Rr, GY(K)); g.stroke(); g.setLineDash([]);
      txt(g, 'K', Rr - 8, GY(K) - 6, '#7C3AED', 'italic 700 14px Georgia, serif', 'right');
      g.strokeStyle = col('--ink'); g.lineWidth = 2; g.beginPath(); var started = false;
      hist.forEach(function (q) { if (!isFinite(q[1]) || q[1] <= 0) { return; } if (!started) { g.moveTo(GX(q[0]), GY(q[1])); started = true; } else { g.lineTo(GX(q[0]), GY(q[1])); } });
      g.stroke();
    }
    function step(ts) {
      var dt = last === null ? 0 : Math.min(0.04, (ts - last) / 1000); last = ts;
      if (playing && visible && S) {
        phys(dt); t += dt;
        if (!hist.length || t - hist[hist.length - 1][0] > 0.25) { var n = counts(); hist.push([t, (n.A * n.B) ? n.C * n.D / (n.A * n.B) : Infinity]); }
      }
      if (visible && S) { draw(); }
      requestAnimationFrame(step);
    }
    ['A', 'B', 'C', 'D'].forEach(function (k) { rs[k].addEventListener('change', reset); });
    rK.addEventListener('input', function () { if (S) { draw(); } });
    rst.addEventListener('click', reset);
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); SG = canvasCtx(cg); if (!P.length) { reset(); } }
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(cv); }
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
})();
</script>
