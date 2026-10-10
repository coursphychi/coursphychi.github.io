+++
title = "Constante d'acidité"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Autoprotolyse de l'eau {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>L'eau, un ampholyte</p>
<p>L'eau est un <span class="imp nt-hole">ampholyte</span>&nbsp;: elle appartient à deux couples acide-base, $({\color{#16A34A}\ce{H2O}}/{\color{#2A6BC4}\ce{HO-}})$ et $({\color{#E11D48}\ce{H3O+}}/{\color{#16A34A}\ce{H2O}})$.</p>
<p>L'eau peut donc réagir sur elle-même&nbsp;! C'est la réaction d'<span class="imp nt-hole">autoprotolyse de l'eau</span>&nbsp;:</p>
<p class="nt-center">$\ce{H2O(l) + H2O(l) <=> H3O+(aq) + HO-(aq)}$</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Produit ionique de l'eau</p>
<p class="nt-f-math">$$K_\mathrm{e} = \frac{\ce{[H3O+]}\times\ce{[HO-]}}{{c^°}^2}$$</p>
<div class="nt-f-units"><span>à 25&nbsp;°C, <b>$K_\mathrm{e}=1{,}0\times10^{-14}$</b></span><span>d'où <b>$\mathrm{p}K_\mathrm{e} = -\log\left(K_\mathrm{e}\right) = 14$</b></span></div>
</div>

<p class="nt-lead">Si on connaît $K_\mathrm{e}$, la concentration en ions oxonium permet de déterminer celle en ions hydroxyde, et inversement.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Le pH d'une solution à 25&nbsp;°C est mesuré à 2,3. Déterminer la concentration en ions oxonium et en ions hydroxyde.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p class="nt-center">$\ce{[H3O+]}=c°\times 10^{-\mathrm{pH}}= 10^{-2{,}3} = \pu{5,0E-3 mol*L-1}$</p>
<p class="nt-center">$\ce{[HO-]}=\dfrac{K_\mathrm{e} \times {c^°}^2}{\ce{[H3O+]}} = \dfrac{1{,}0\times10^{-14}\times 1{,}0^2}{5{,}0\times10^{-3}} = \pu{2,0E-12 mol*L-1}$</p>
</div>
</details>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Solution neutre, acide ou basique</p>
<ul class="nt-facts">
<li><b style="color:#16A34A;">Solution neutre</b>&nbsp;: par définition, $\ce{[H3O+]}=\ce{[HO-]}$. Comme $\ce{[H3O+]}\times\ce{[HO-]}=K_\mathrm{e}\,{c^°}^2$, on obtient $\ce{[H3O+]}^2 = K_\mathrm{e}\,{c^°}^2$, soit $\ce{[H3O+]} = \sqrt{K_\mathrm{e}}\times c° = \pu{1,0E-7 mol*L-1}$, ou encore $\mathrm{pH} = \frac{1}{2}\mathrm{p}K_\mathrm{e} = 7{,}0$.</li>
<li><b style="color:#E11D48;">Solution acide</b>&nbsp;: $\ce{[H3O+]} &gt; \ce{[HO-]} = \dfrac{K_\mathrm{e}\,{c^°}^2}{\ce{[H3O+]}}$, donc $\ce{[H3O+]}^2 &gt; K_\mathrm{e}\,{c^°}^2$, soit $\ce{[H3O+]} &gt; \pu{1,0E-7 mol*L-1}$ et $\mathrm{pH} &lt; 7{,}0$.</li>
<li><b style="color:#2A6BC4;">Solution basique</b>&nbsp;: $\ce{[H3O+]} &lt; \ce{[HO-]}$, donc $\ce{[H3O+]} &lt; \pu{1,0E-7 mol*L-1}$ et $\mathrm{pH} &gt; 7{,}0$.</li>
</ul>
</div>

<div class="nt-lab" id="lab-auto">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Des ions oxonium et des ions hydroxyde, à tout pH</p>
<canvas style="height:360px;" aria-label="Concentrations en ions oxonium et hydroxyde, en échelle logarithmique, selon le pH"></canvas>
<label class="nt-ctrl">pH&nbsp;: <b class="out-ph"></b><input type="range" min="0" max="14" step="0.1" value="2.3"></label>
<div class="nt-read" aria-live="polite"><span>$\ce{[H3O+]}$ = <b class="out-h"></b></span><span>$\ce{[HO-]}$ = <b class="out-o"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

## Acides forts et bases fortes {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un <span class="imp nt-hole">acide fort</span> ou une <span class="imp nt-hole">base forte</span> réagit de manière <span class="imp nt-hole">quasi totale</span> avec l'eau&nbsp;: le taux d'avancement de la réaction vaut $\tau = 1$.</p>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Acide fort</th><th>Avancement</th><th>$\ce{AH}$</th><th>$\ce{H2O}$</th><th>$\ce{A-}$</th><th>$\ce{H3O+}$</th></tr></thead>
<tbody>
<tr><td>état initial</td><td>$0$</td><td>$n = C\,V$</td><td>excès</td><td>$0$</td><td>$0$</td></tr>
<tr><td>état final</td><td>$x_\mathrm{f} = x_\mathrm{max} = n$</td><td>$0$</td><td>excès</td><td>$n$</td><td>$n$</td></tr>
</tbody>
</table>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Acide fort</p>
<p class="nt-f-math">$$\mathrm{pH}= -\log\left(\frac{C}{c°}\right)$$</p>
<div class="nt-f-units"><span>car $\ce{[H3O+]} = C$, la concentration apportée en acide</span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Base forte</p>
<p class="nt-f-math">$$\mathrm{pH}= \mathrm{p}K_\mathrm{e} + \log\left(\frac{C}{c°}\right)$$</p>
<div class="nt-f-units"><span>car $\ce{[HO-]} = C$&nbsp;; à 25&nbsp;°C, <b>$\mathrm{pH} = 14 + \log(C/c°)$</b></span></div>
</div>
</div>

<details class="nt-d">
<summary><span class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</span><span class="nt-sum">Le pH d'une base forte</span></summary>
<div class="nt-d-body">
<p>Pour une base forte, $\ce{A- + H2O -> AH + HO-}$ est totale, donc $\ce{[HO-]} = C$. Avec le produit ionique de l'eau&nbsp;:</p>
<p class="nt-center">$\ce{[H3O+]}=\dfrac{K_\mathrm{e}\,{c^°}^2}{\ce{[HO-]}}=\dfrac{K_\mathrm{e}\,{c^°}^2}{C}$</p>
<p class="nt-center">$\mathrm{pH} =-\log\left(\dfrac{\ce{[H3O+]}}{c°}\right) =-\log\left(K_\mathrm{e}\times\dfrac{c°}{C}\right) =-\log\left(K_\mathrm{e}\right)-\log\left(\dfrac{c°}{C}\right) =\mathrm{p}K_\mathrm{e} + \log\left(\dfrac{C}{c°}\right)$</p>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li>Acides forts&nbsp;: le chlorure d'hydrogène, $\ce{HCl(g) + H2O(l) -> H3O+(aq) + Cl-(aq)}$ (sa solution est l'acide chlorhydrique), et l'acide nitrique, $\ce{HNO3(l) + H2O(l) -> H3O+(aq) + NO3-(aq)}$.</li>
<li>Base forte&nbsp;: l'hydroxyde de sodium (la soude), $\ce{NaOH(s) -> Na+(aq) + HO-(aq)}$ dans l'eau.</li>
</ul>
</div>

## Acides faibles et bases faibles {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La transformation chimique entre un <span class="imp nt-hole">acide faible</span> ou une <span class="imp nt-hole">base faible</span> et l'eau <span class="imp nt-hole">n'est pas totale</span>&nbsp;: $\tau &lt; 1$.</p>
<p class="nt-center">$\ce{AH + H2O <=> A- + H3O+}$</p>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Acide faible</th><th>Avancement</th><th>$\ce{AH}$</th><th>$\ce{H2O}$</th><th>$\ce{A-}$</th><th>$\ce{H3O+}$</th></tr></thead>
<tbody>
<tr><td>état initial</td><td>$0$</td><td>$n = C\,V$</td><td>excès</td><td>$0$</td><td>$0$</td></tr>
<tr><td>état final</td><td>$x_\mathrm{f} &lt; n$</td><td>$n - x_\mathrm{f}$</td><td>excès</td><td>$x_\mathrm{f}$</td><td>$x_\mathrm{f}$</td></tr>
</tbody>
</table>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>$x_\mathrm{f} &lt; n \Rightarrow \ce{[H3O+]} &lt; C \Rightarrow \mathrm{pH} &gt; -\log\left(\dfrac{C}{c°}\right)$&nbsp;: le pH d'un acide faible dans l'eau est <span class="imp nt-hole">plus grand</span> que celui d'un acide fort de même concentration apportée.</p>
<p>De même, le pH d'une base faible dans l'eau est <span class="imp nt-hole">plus petit</span> que celui d'une base forte de même concentration apportée&nbsp;: $\ce{[HO-]}$ est plus petite, donc $\ce{[H3O+]}$ est plus grande et le pH plus petit.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li>Acide faible&nbsp;: l'acide éthanoïque (ou acide acétique), dont la forme dissoute est simplement $\ce{CH3COOH(aq)}$&nbsp;:<br>
$\ce{CH3COOH(aq) }+ \ce{H2O(l)} \ce{<=>} \ce{CH3COO-(aq)} + \ce{H3O+(aq)}$.<br>
Sa base conjuguée est l'ion éthanoate.</li>
<li>Base faible&nbsp;: l'ammoniac, dont la forme dissoute est simplement $\ce{NH3(aq)}$&nbsp;:<br>
$\ce{NH3(aq)} + \ce{H2O(l)} \ce{<=>}  \ce{NH4+(aq)} + \ce{HO-(aq)}$.<br>
Son acide conjugué est l'ion ammonium.</li>
</ul>
</div>

<div class="nt-lab" id="lab-force">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Acide fort ou acide faible&nbsp;: le rôle de la concentration</p>
<div class="nt-lab-pair">
<figure><canvas class="c1" style="height:250px; background:#fff;" aria-label="Taux d'avancement en fonction de la concentration apportée"></canvas><figcaption>Taux d'avancement $\tau$</figcaption></figure>
<figure><canvas class="c2" style="height:250px; background:#fff;" aria-label="pH en fonction de la concentration apportée"></canvas><figcaption>pH de la solution</figcaption></figure>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">$\mathrm{p}K_\mathrm{A}$ de l'acide faible&nbsp;: <b class="out-pka"></b><input type="range" data-p="pka" min="2" max="10" step="0.1" value="4.8"></label>
<label class="nt-ctrl">Concentration apportée $C$&nbsp;: <b class="out-c"></b><input type="range" data-p="c" min="-6" max="0" step="0.05" value="-2"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$\tau$ = <b class="out-tau"></b></span><span>pH (acide faible) = <b class="out-phw"></b></span><span>pH (acide fort) = <b class="out-phs"></b></span></div>
<p class="nt-note">Calcul exact, qui tient compte de l'autoprotolyse de l'eau. Remarquez qu'un acide faible réagit d'autant plus avec l'eau qu'il est dilué&nbsp;: à très faible concentration, $\tau$ s'approche de 1. Ces courbes reprennent celles de l'activité Python «&nbsp;Taux d'avancement et p$K_\mathrm{A}$&nbsp;».</p>
</div>

## Force d'un acide faible ou d'une base faible {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Constante d'acidité</p>
<p>La constante d'équilibre de la réaction d'un acide faible avec l'eau, $\ce{AH + H2O <=> A- + H3O+}$, s'appelle <span class="imp nt-hole">constante d'acidité</span> et se note $K_\mathrm{A}$. Elle caractérise un couple acide-base $(\ce{AH}/\ce{A-})$.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Constante d'acidité</p>
<p class="nt-f-math">$$K_\mathrm{A}=\frac{\ce{[A-]}_\mathrm{f}\times\ce{[H3O+]}_\mathrm{f}}{\ce{[AH]}_\mathrm{f}\times c°}$$</p>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>pK<sub>A</sub></p>
<p class="nt-f-math">$$\mathrm{p}K_\mathrm{A}=-\log\left(K_\mathrm{A}\right)$$</p>
<div class="nt-f-units"><span>des valeurs plus pratiques, généralement <b>entre 0 et 14</b></span></div>
</div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Et pour la base conjuguée&nbsp;?</p>
<p>Pour une base faible, $\ce{A- + H2O <=> AH + HO-}$, la constante d'équilibre s'écrit, en utilisant $\ce{[HO-]} = K_\mathrm{e}\,{c°}^2/\ce{[H3O+]}$&nbsp;:</p>
<p class="nt-center">$K_\mathrm{B}=\dfrac{\ce{[AH]}\times\ce{[HO-]}}{\ce{[A-]}\times c°} = \dfrac{\ce{[AH]}\times K_\mathrm{e}\,{c°}^2}{\ce{[A-]}\times c°\times\ce{[H3O+]}} = \dfrac{K_\mathrm{e}}{K_\mathrm{A}}$</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-prop" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Plus un acide faible est fort</p>
<p>Plus la réaction d'un acide faible sur l'eau est avancée&nbsp;:</p>
<ul class="nt-facts">
<li>plus $\tau$ est proche de 1&nbsp;;</li>
<li>plus $K_\mathrm{A}$ est <span class="imp nt-hole">grand</span>&nbsp;;</li>
<li>plus $\mathrm{p}K_\mathrm{A}$ est <span class="imp nt-hole">petit</span>.</li>
</ul>
</div>
<div class="nt-b nt-prop" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Plus une base faible est forte</p>
<p>Plus la réaction d'une base faible sur l'eau est avancée&nbsp;:</p>
<ul class="nt-facts">
<li>plus $\tau$ est proche de 1&nbsp;;</li>
<li>plus $K_\mathrm{B}$ est grand, donc $K_\mathrm{A}$ <span class="imp nt-hole">petit</span>&nbsp;;</li>
<li>plus $\mathrm{p}K_\mathrm{A}$ est <span class="imp nt-hole">grand</span>.</li>
</ul>
</div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Que valent $K_\mathrm{A}$ et $\mathrm{p}K_\mathrm{A}$ pour le couple $(\ce{H3O+}/\ce{H2O})$&nbsp;? Et pour le couple $(\ce{H2O}/\ce{HO-})$&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li>Pour $(\ce{H3O+}/\ce{H2O})$, la «&nbsp;réaction&nbsp;» $\ce{H3O+ + H2O <=> H2O + H3O+}$ ne change rien&nbsp;: $K_\mathrm{A} = 1$, donc $\mathrm{p}K_\mathrm{A} = 0$.</li>
<li>Pour $(\ce{H2O}/\ce{HO-})$, de même $K_\mathrm{B} = 1$, donc $K_\mathrm{A} = \dfrac{K_\mathrm{e}}{K_\mathrm{B}} = 10^{-14}$ et $\mathrm{p}K_\mathrm{A} = 14$.</li>
</ul>
</div>
</details>

<p class="nt-lead">On classe les acides et les bases sur une <b>échelle de pK<sub>A</sub></b>&nbsp;:</p>

<svg class="nt-svg nt-svg-m" viewBox="0 0 560 430" role="img" aria-label="Échelle de pKa : de bas en haut, H3O+/H2O (0), CH3COOH/CH3COO- (4,8), NH4+/NH3 (9,2), H2O/HO- (14). Les acides sont d'autant plus forts que le pKa est petit, les bases d'autant plus fortes que le pKa est grand"><defs><linearGradient id="gPka" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FCA5A5"/><stop offset=".5" stop-color="#86EFAC"/><stop offset="1" stop-color="#93C5FD"/></linearGradient></defs><rect x="262" y="67" width="36" height="328" rx="6" fill="url(#gPka)"/><line x1="280" y1="403" x2="280" y2="55" stroke="#1E293B" stroke-width="2"/><polygon points="280.0,51.0 286.0,62.0 274.0,62.0" fill="#1E293B"/><text x="280" y="45" font-size="15" text-anchor="middle" fill="#1E293B" font-weight="700">pK<tspan font-size="11" dy="4">A</tspan></text><line x1="250" y1="385" x2="310" y2="385" stroke="#1E293B" stroke-width="1.6"/><text x="238" y="390" font-size="15" text-anchor="end" fill="#E11D48" font-weight="700">H₃O⁺</text><text x="322" y="390" font-size="15" fill="#2A6BC4" font-weight="700">H₂O</text><text x="290" y="381" font-size="11" fill="#475569">0</text><line x1="250" y1="279.4" x2="310" y2="279.4" stroke="#1E293B" stroke-width="1.6"/><text x="238" y="284.4" font-size="15" text-anchor="end" fill="#E11D48" font-weight="700">CH₃COOH</text><text x="322" y="284.4" font-size="15" fill="#2A6BC4" font-weight="700">CH₃COO⁻</text><text x="290" y="275.4" font-size="11" fill="#475569">4,8</text><line x1="250" y1="182.60000000000002" x2="310" y2="182.60000000000002" stroke="#1E293B" stroke-width="1.6"/><text x="238" y="187.60000000000002" font-size="15" text-anchor="end" fill="#E11D48" font-weight="700">NH₄⁺</text><text x="322" y="187.60000000000002" font-size="15" fill="#2A6BC4" font-weight="700">NH₃</text><text x="290" y="178.60000000000002" font-size="11" fill="#475569">9,2</text><line x1="250" y1="77" x2="310" y2="77" stroke="#1E293B" stroke-width="1.6"/><text x="238" y="82" font-size="15" text-anchor="end" fill="#E11D48" font-weight="700">H₂O</text><text x="322" y="82" font-size="15" fill="#2A6BC4" font-weight="700">HO⁻</text><text x="290" y="73" font-size="11" fill="#475569">14</text><line x1="70" y1="99" x2="70" y2="363" stroke="#E11D48" stroke-width="4"/><polygon points="70.0,376.2 62.0,362.2 78.0,362.2" fill="#E11D48"/><text x="52" y="231.0" font-size="14" text-anchor="middle" fill="#E11D48" font-weight="700" transform="rotate(-90 52 231.0)">force croissante des acides</text><line x1="490" y1="363" x2="490" y2="99" stroke="#2A6BC4" stroke-width="4"/><polygon points="490.0,85.8 498.0,99.8 482.0,99.8" fill="#2A6BC4"/><text x="512" y="231.0" font-size="14" text-anchor="middle" fill="#2A6BC4" font-weight="700" transform="rotate(90 512 231.0)">force croissante des bases</text></svg>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>$\ce{NH4+}$ est-il un acide plus faible ou plus fort que $\ce{CH3COOH}$&nbsp;? $\ce{NH3}$ est-elle une base plus faible ou plus forte que $\ce{CH3COO-}$&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>$\ce{NH4+}$ ($\mathrm{p}K_\mathrm{A} = 9{,}2$) est un acide <b>plus faible</b> que $\ce{CH3COOH}$ ($\mathrm{p}K_\mathrm{A} = 4{,}8$), et $\ce{NH3}$ est une base <b>plus forte</b> que $\ce{CH3COO-}$. Plus un acide est faible, plus sa base conjuguée est forte.</p>
</div>
</details>

## Diagrammes de distribution et de prédominance {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Proportions à l'équilibre</p>
<p>La <span class="imp nt-hole">proportion à l'équilibre</span> d'un acide et celle de sa base conjuguée sont les quotients&nbsp;:</p>
<p class="nt-center">${\color{#E11D48} r_\mathrm{AH}}=\dfrac{\color{#E11D48} n_\mathrm{AH,f}}{n_\mathrm{AH,f}+n_\mathrm{A^-,f}} \qquad {\color{#2A6BC4} r_\mathrm{A^-}}=\dfrac{\color{#2A6BC4} n_\mathrm{A^-,f}}{n_\mathrm{AH,f}+n_\mathrm{A^-,f}}$</p>
<p>Dans un <span class="imp nt-hole">diagramme de distribution</span>, on superpose les courbes donnant ces proportions en fonction du pH.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Diagramme de prédominance</p>
<p>Le <span class="imp nt-hole">diagramme de prédominance</span> est une simplification du diagramme de distribution&nbsp;: on n'indique plus, sur un axe de pH, que l'espèce qui prédomine.</p>
<ul class="nt-facts">
<li>pour $\mathrm{pH} &lt; \mathrm{p}K_\mathrm{A}$, $\ce{[AH]} &gt; \ce{[A-]}$&nbsp;: l'<span class="imp nt-hole">acide</span> prédomine&nbsp;;</li>
<li>pour $\mathrm{pH} = \mathrm{p}K_\mathrm{A}$, $\ce{[AH]} = \ce{[A-]}$&nbsp;;</li>
<li>pour $\mathrm{pH} &gt; \mathrm{p}K_\mathrm{A}$, $\ce{[AH]} &lt; \ce{[A-]}$&nbsp;: la <span class="imp nt-hole">base</span> prédomine.</li>
</ul>
</div>

<details class="nt-d">
<summary><span class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</span><span class="nt-sum">D'où viennent ces règles&nbsp;?</span></summary>
<div class="nt-d-body">
<p>En prenant le logarithme de $K_\mathrm{A}$, on obtient la relation $\mathrm{pH} = \mathrm{p}K_\mathrm{A} + \log\left(\dfrac{\ce{[A-]}}{\ce{[AH]}}\right)$. Si $\mathrm{pH} &gt; \mathrm{p}K_\mathrm{A}$, le logarithme est positif, donc $\ce{[A-]} &gt; \ce{[AH]}$&nbsp;; et inversement.</p>
</div>
</details>

<div class="nt-lab" id="lab-distrib">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Du diagramme de distribution au diagramme de prédominance</p>
<canvas style="height:380px; background:#fff;" aria-label="Proportions d'un acide et de sa base conjuguée en fonction du pH, et diagramme de prédominance correspondant"></canvas>
<label class="nt-ctrl">pH&nbsp;: <b class="out-ph"></b><input type="range" min="0" max="14" step="0.1" value="6"></label>
<div class="nt-ctrl">Couple&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="couple" value="ethan" checked><span>CH₃COOH / CH₃COO⁻</span></label>
<label><input type="radio" name="couple" value="ammon"><span>NH₄⁺ / NH₃</span></label>
<label><input type="radio" name="couple" value="meth"><span>HCOOH / HCOO⁻</span></label>
<label><input type="radio" name="couple" value="bbt"><span>bleu de bromothymol</span></label>
<label><input type="radio" name="couple" value="phph"><span>phénolphtaléine</span></label>
<label><input type="radio" name="couple" value="hel"><span>hélianthine</span></label>
</div>
</div>
<div class="nt-read" aria-live="polite"><span>$r_\mathrm{AH}$ = <b class="out-ra"></b></span><span>$r_\mathrm{A^-}$ = <b class="out-rb"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>L'acide d'un couple peut très bien dominer sa base conjuguée dans une solution aqueuse basique, et réciproquement, une base peut dominer dans une solution acide&nbsp;! Par exemple, à pH = 8 (solution basique), c'est l'ion ammonium $\ce{NH4+}$, un acide, qui prédomine sur $\ce{NH3}$, car $8 &lt; 9{,}2$.</p>
</div>

## Indicateurs colorés {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Un <span class="imp nt-hole">indicateur coloré</span> est un couple acide-base dont la forme acide et la forme basique n'ont pas la même couleur.</p>
<p>Sa <span class="imp nt-hole">zone de virage</span> est la zone de pH où les formes acide et basique sont en proportions comparables&nbsp;: la couleur est alors un mélange des couleurs acide et basique. Elle se situe autour de $\mathrm{pH} = \mathrm{p}K_\mathrm{A}$ (typiquement de $\mathrm{p}K_\mathrm{A}-1$ à $\mathrm{p}K_\mathrm{A}+1$).</p>
<p class="nt-note">Essayez les trois indicateurs dans l'animation ci-dessus&nbsp;: la couleur de la solution est affichée.</p>
</div>

<svg class="nt-svg" viewBox="0 0 745 288" role="img" aria-label="Zones de virage de quelques indicateurs colorés sur une échelle de pH de 0 à 14"><text x="180" y="36" font-size="13" text-anchor="end" fill="#1E293B" font-weight="700">hélianthine</text><rect x="190.0" y="20" width="110.7" height="22" fill="#DC2626"/><rect x="300.7" y="20" width="46.4" height="22" fill="#F97316"/><rect x="347.1" y="20" width="342.9" height="22" fill="#FDE047"/><rect x="190" y="20" width="500" height="22" fill="none" stroke="#94A3B8"/><text x="300.7" y="54" font-size="10" text-anchor="middle" fill="#475569">3,1</text><text x="347.1" y="54" font-size="10" text-anchor="middle" fill="#475569">4,4</text><text x="180" y="74" font-size="13" text-anchor="end" fill="#1E293B" font-weight="700">vert de bromocrésol</text><rect x="190.0" y="58" width="135.7" height="22" fill="#FDE047"/><rect x="325.7" y="58" width="57.1" height="22" fill="#22C55E"/><rect x="382.9" y="58" width="307.1" height="22" fill="#2563EB"/><rect x="190" y="58" width="500" height="22" fill="none" stroke="#94A3B8"/><text x="325.7" y="92" font-size="10" text-anchor="middle" fill="#475569">3,8</text><text x="382.9" y="92" font-size="10" text-anchor="middle" fill="#475569">5,4</text><text x="180" y="112" font-size="13" text-anchor="end" fill="#1E293B" font-weight="700">rouge de méthyle</text><rect x="190.0" y="96" width="150.0" height="22" fill="#DC2626"/><rect x="340.0" y="96" width="71.4" height="22" fill="#F97316"/><rect x="411.4" y="96" width="278.6" height="22" fill="#FDE047"/><rect x="190" y="96" width="500" height="22" fill="none" stroke="#94A3B8"/><text x="340.0" y="130" font-size="10" text-anchor="middle" fill="#475569">4,2</text><text x="411.4" y="130" font-size="10" text-anchor="middle" fill="#475569">6,2</text><text x="180" y="150" font-size="13" text-anchor="end" fill="#1E293B" font-weight="700">bleu de bromothymol</text><rect x="190.0" y="134" width="214.3" height="22" fill="#FDE047"/><rect x="404.3" y="134" width="57.1" height="22" fill="#22C55E"/><rect x="461.4" y="134" width="228.6" height="22" fill="#2563EB"/><rect x="190" y="134" width="500" height="22" fill="none" stroke="#94A3B8"/><text x="404.3" y="168" font-size="10" text-anchor="middle" fill="#475569">6,0</text><text x="461.4" y="168" font-size="10" text-anchor="middle" fill="#475569">7,6</text><text x="180" y="188" font-size="13" text-anchor="end" fill="#1E293B" font-weight="700">phénolphtaléine</text><rect x="190.0" y="172" width="292.9" height="22" fill="#F8FAFC"/><rect x="482.9" y="172" width="64.3" height="22" fill="#F9A8D4"/><rect x="547.1" y="172" width="142.9" height="22" fill="#DB2777"/><rect x="190" y="172" width="500" height="22" fill="none" stroke="#94A3B8"/><text x="482.9" y="206" font-size="10" text-anchor="middle" fill="#475569">8,2</text><text x="547.1" y="206" font-size="10" text-anchor="middle" fill="#475569">10,0</text><text x="180" y="226" font-size="13" text-anchor="end" fill="#1E293B" font-weight="700">bleu de thymol</text><rect x="190.0" y="210" width="42.9" height="22" fill="#DC2626"/><rect x="232.9" y="210" width="57.1" height="22" fill="#F97316"/><rect x="290.0" y="210" width="185.7" height="22" fill="#FDE047"/><rect x="475.7" y="210" width="57.1" height="22" fill="#22C55E"/><rect x="532.9" y="210" width="157.1" height="22" fill="#2563EB"/><rect x="190" y="210" width="500" height="22" fill="none" stroke="#94A3B8"/><text x="232.9" y="244" font-size="10" text-anchor="middle" fill="#475569">1,2</text><text x="290.0" y="244" font-size="10" text-anchor="middle" fill="#475569">2,8</text><text x="475.7" y="244" font-size="10" text-anchor="middle" fill="#475569">8,0</text><text x="532.9" y="244" font-size="10" text-anchor="middle" fill="#475569">9,6</text><line x1="190" y1="252" x2="700" y2="252" stroke="#1E293B" stroke-width="1.6"/><polygon points="708.0,252.0 699.0,257.0 699.0,247.0" fill="#1E293B"/><line x1="190.0" y1="248" x2="190.0" y2="256" stroke="#1E293B"/><text x="190.0" y="270" font-size="11" text-anchor="middle" fill="#475569">0</text><line x1="261.4" y1="248" x2="261.4" y2="256" stroke="#1E293B"/><text x="261.4" y="270" font-size="11" text-anchor="middle" fill="#475569">2</text><line x1="332.9" y1="248" x2="332.9" y2="256" stroke="#1E293B"/><text x="332.9" y="270" font-size="11" text-anchor="middle" fill="#475569">4</text><line x1="404.3" y1="248" x2="404.3" y2="256" stroke="#1E293B"/><text x="404.3" y="270" font-size="11" text-anchor="middle" fill="#475569">6</text><line x1="475.7" y1="248" x2="475.7" y2="256" stroke="#1E293B"/><text x="475.7" y="270" font-size="11" text-anchor="middle" fill="#475569">8</text><line x1="547.1" y1="248" x2="547.1" y2="256" stroke="#1E293B"/><text x="547.1" y="270" font-size="11" text-anchor="middle" fill="#475569">10</text><line x1="618.6" y1="248" x2="618.6" y2="256" stroke="#1E293B"/><text x="618.6" y="270" font-size="11" text-anchor="middle" fill="#475569">12</text><line x1="690.0" y1="248" x2="690.0" y2="256" stroke="#1E293B"/><text x="690.0" y="270" font-size="11" text-anchor="middle" fill="#475569">14</text><text x="706" y="270" font-size="12" fill="#1E293B" font-weight="700">pH</text></svg>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Choisir un indicateur pour un titrage</p>
<p>Pour utiliser efficacement un indicateur coloré lors d'un titrage acide-base, il faut que <span class="imp nt-hole">sa zone de virage contienne le pH à l'équivalence $\mathrm{pH_E}$</span>.</p>
</div>

<div class="nt-lab" id="lab-indic">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Choisir un indicateur adapté au titrage</p>
<p class="nt-note">Titrage de 10&nbsp;mL d'acide éthanoïque ($C = \pu{0,10 mol*L-1}$) par la soude ($C_\mathrm{B} = \pu{0,10 mol*L-1}$).</p>
<canvas style="height:320px; background:#fff;" aria-label="Courbe de titrage pH-métrique et zone de virage de l'indicateur choisi"></canvas>
<div class="nt-ctrl">Indicateur&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="ind2" value="hel"><span>hélianthine</span></label>
<label><input type="radio" name="ind2" value="rm"><span>rouge de méthyle</span></label>
<label><input type="radio" name="ind2" value="bbt"><span>bleu de bromothymol</span></label>
<label><input type="radio" name="ind2" value="phph" checked><span>phénolphtaléine</span></label>
</div>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-leaf"></i>Dans la vie courante… et dans la nature</p>
<ul class="nt-facts">
<li>Les bandelettes et le papier pH contiennent un mélange d'indicateurs colorés, qui change de couleur progressivement sur toute l'échelle de pH.</li>
<li>Le jus de chou rouge contient des anthocyanes, des pigments qui passent du rouge (milieu acide) au violet, puis au bleu-vert et au jaune (milieu très basique)&nbsp;: c'est un indicateur coloré naturel.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi les hortensias sont-ils bleus en Bretagne et roses ailleurs&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Les hortensias (<i>Hydrangea macrophylla</i>) sont plutôt roses à rouges en sol calcaire, basique, et bleus à violets en sol granitique, acide. Mais contrairement à une idée reçue, ce n'est pas l'acidité elle-même qui colore les fleurs en bleu&nbsp;: c'est la présence d'<b>ions aluminium</b> $\ce{Al^{3+}}$.</p>
<ul class="nt-facts">
<li>En sol acide (granitique), l'aluminium présent dans la terre devient soluble. La plante l'absorbe, et il se lie à un pigment de la fleur (la delphinidine-3-glucoside), ce qui produit la couleur bleue.</li>
<li>En sol basique (calcaire), l'aluminium reste «&nbsp;prisonnier&nbsp;» sous forme de précipités insolubles&nbsp;: le pigment reste sous sa forme naturelle, rose.</li>
</ul>
<p>Dans un sol calcaire, le carbonate de calcium neutralise l'acidité&nbsp;: c'est un effet tampon. Dans un sol granitique, ce tampon est absent, et les pluies, naturellement un peu acides à cause du dioxyde de carbone dissous, font baisser le pH sans résistance. Pour faire bleuir un hortensia dans un jardin calcaire, il ne suffit donc pas d'acidifier le sol&nbsp;: il faut souvent apporter de l'aluminium (sulfate d'aluminium, vendu comme «&nbsp;bleuissant&nbsp;»).</p>
</div>
</details>

## Acides α-aminés {.nt-h2}

<p class="nt-lead">Les acides α-aminés sont les briques des protéines. Qu'ont-ils en commun&nbsp;? <a href="https://www.compoundchem.com/2014/09/16/aminoacids/" target="_blank" rel="noopener">Voir les 20 acides α-aminés usuels</a>.</p>

<svg class="nt-svg nt-svg-s" viewBox="0 0 420 330" role="img" aria-label="Structure d'un acide alpha-aminé : un carbone porte un groupe amine, un groupe carboxyle, un atome d'hydrogène et une chaîne latérale R"><ellipse cx="92" cy="205" rx="62" ry="38" fill="#BFDBFE" stroke="#2A6BC4" stroke-dasharray="5 4"/><path d="M262,175 C292,135 372,128 380,168 C388,208 365,232 352,262 C340,295 285,300 266,272 C250,250 245,205 262,175 Z" fill="#FECDD3" stroke="#E11D48" stroke-dasharray="5 4"/><text x="200" y="158" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">C</text><text x="95" y="213" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">H<tspan font-size="14" dy="5">2</tspan><tspan dy="-5">N</tspan></text><text x="295" y="213" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">C</text><text x="350" y="180" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">O</text><text x="287" y="270" font-size="22" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">OH</text><text x="138" y="70" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">R</text><text x="258" y="74" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="121.6" y1="191.1" x2="187.6" y2="156.5" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><line x1="212.1" y1="157.0" x2="282.9" y2="198.0" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><line x1="308.8" y1="200.8" x2="339.8" y2="182.2" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><line x1="305.2" y1="194.8" x2="336.2" y2="176.2" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><line x1="295.0" y1="219.0" x2="295.0" y2="246.0" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><polygon points="200,136 146,82 156,73" fill="#1E293B"/><line x1="205.1" y1="126.0" x2="209.2" y2="129.5" stroke="#1E293B" stroke-width="1.6"/><line x1="211.7" y1="117.2" x2="216.9" y2="121.7" stroke="#1E293B" stroke-width="1.6"/><line x1="218.3" y1="108.5" x2="224.6" y2="113.8" stroke="#1E293B" stroke-width="1.6"/><line x1="224.9" y1="99.7" x2="232.3" y2="106.0" stroke="#1E293B" stroke-width="1.6"/><line x1="231.5" y1="91.0" x2="239.9" y2="98.2" stroke="#1E293B" stroke-width="1.6"/><line x1="238.1" y1="82.2" x2="247.6" y2="90.4" stroke="#1E293B" stroke-width="1.6"/><text x="92" y="262" font-size="13" text-anchor="middle" fill="#2A6BC4" font-weight="700">groupe amine</text><text x="318" y="318" font-size="13" text-anchor="middle" fill="#E11D48" font-weight="700">groupe carboxyle</text><text x="200" y="196" font-size="12" text-anchor="middle" fill="#475569" font-style="italic">carbone α</text></svg>

<p class="nt-cap">Tous possèdent un <b style="color:#E11D48;">groupe carboxyle</b> et un <b style="color:#2A6BC4;">groupe amine</b>, portés par le même atome de carbone, le carbone α. Seule la chaîne latérale R change d'un acide aminé à l'autre.</p>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque&nbsp;: pourquoi «&nbsp;α&nbsp;»&nbsp;?</p>
<p>Le carbone qui porte le groupe amine est le premier qui suit celui du groupe carboxyle. En nomenclature officielle, on l'appellerait le carbone 2, mais la tradition a gardé une ancienne notation par lettres grecques&nbsp;: α pour le premier, β pour le deuxième, etc. Il existe des acides β- ou γ-aminés (comme le GABA, principal neurotransmetteur inhibiteur du système nerveux), mais seuls les acides α-aminés sont incorporés dans les protéines.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Deux couples acide-base</p>
<p>Les acides aminés interviennent à la fois dans le couple <b style="color:#E11D48;">acide carboxylique ($\ce{-COOH}$)</b> / <b style="color:#2A6BC4;">ion carboxylate ($\ce{-COO-}$)</b>, de constante $K_\mathrm{A1}$, et dans le couple <b style="color:#E11D48;">ion ammonium ($\ce{-NH3+}$)</b> / <b style="color:#2A6BC4;">amine ($\ce{-NH2}$)</b>, de constante $K_\mathrm{A2}$, avec $\mathrm{p}K_\mathrm{A1} &lt; \mathrm{p}K_\mathrm{A2}$.</p>
</div>

<svg class="nt-svg" viewBox="0 0 745 200" role="img" aria-label="Diagramme de prédominance d'un acide aminé : forme cationique pour pH inférieur à pKA1, zwitterion entre pKA1 et pKA2, forme anionique au-delà de pKA2"><rect x="40" y="40" width="210" height="110" fill="#FEF3C7"/><rect x="250" y="40" width="220" height="110" fill="#DCFCE7"/><rect x="470" y="40" width="220" height="110" fill="#DBEAFE"/><line x1="40" y1="160" x2="700" y2="160" stroke="#1E293B" stroke-width="1.6"/><polygon points="708.0,160.0 699.0,165.0 699.0,155.0" fill="#1E293B"/><text x="704" y="182" font-size="13" fill="#1E293B" font-weight="700">pH</text><line x1="250" y1="32" x2="250" y2="166" stroke="#1E293B" stroke-width="2"/><text x="250" y="22" font-size="14" text-anchor="middle" fill="#1E293B" font-weight="700">pK<tspan font-size="10" dy="3">A1</tspan></text><line x1="470" y1="32" x2="470" y2="166" stroke="#1E293B" stroke-width="2"/><text x="470" y="22" font-size="14" text-anchor="middle" fill="#1E293B" font-weight="700">pK<tspan font-size="10" dy="3">A2</tspan></text><text x="145.0" y="78" font-size="17" text-anchor="middle" fill="#E11D48" font-weight="700">−COOH</text><text x="145.0" y="108" font-size="17" text-anchor="middle" fill="#E11D48" font-weight="700">−NH₃⁺</text><text x="145.0" y="138" font-size="12" text-anchor="middle" fill="#475569" font-weight="700">cation</text><text x="360.0" y="78" font-size="17" text-anchor="middle" fill="#2A6BC4" font-weight="700">−COO⁻</text><text x="360.0" y="108" font-size="17" text-anchor="middle" fill="#E11D48" font-weight="700">−NH₃⁺</text><text x="360.0" y="138" font-size="12" text-anchor="middle" fill="#475569" font-weight="700">zwitterion (ampholyte)</text><text x="580.0" y="78" font-size="17" text-anchor="middle" fill="#2A6BC4" font-weight="700">−COO⁻</text><text x="580.0" y="108" font-size="17" text-anchor="middle" fill="#2A6BC4" font-weight="700">−NH₂</text><text x="580.0" y="138" font-size="12" text-anchor="middle" fill="#475569" font-weight="700">anion</text></svg>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Au pH de l'organisme (environ 7,4, entre $\mathrm{p}K_\mathrm{A1} \approx 2$ et $\mathrm{p}K_\mathrm{A2} \approx 9$), un acide aminé est sous la forme $\ce{-COO-}$ et $\ce{-NH3+}$&nbsp;: c'est un <span class="imp nt-hole">ampholyte</span>, doublement ionique. On parle de <span class="imp nt-hole">zwitterion</span>, ou d'ion dipolaire.</p>
<ul class="nt-facts">
<li>Cela garantit une excellente solubilité dans le sang et le cytoplasme, grâce aux fortes interactions ion-dipôle avec les molécules d'eau.</li>
<li>Cela permet surtout la formation de liaisons ioniques à l'intérieur de la structure tertiaire des protéines.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin (hors programme)</span><span class="nt-sum">Chiralité&nbsp;: la main gauche du vivant</span></summary>
<div class="nt-d-body">
<p><b>Carbone asymétrique.</b> À l'exception de la glycine (pour laquelle R est un atome d'hydrogène), le carbone α est lié à quatre groupes différents&nbsp;: c'est un carbone asymétrique. La molécule est alors <b>chirale</b>&nbsp;: elle n'est pas superposable à son image dans un miroir, comme une main. Deux molécules chirales images l'une de l'autre sont des <b>énantiomères</b>.</p>
<svg class="nt-svg nt-svg-m" viewBox="0 0 640 270" role="img" aria-label="Les deux énantiomères d'un acide alpha-aminé, images l'une de l'autre dans un miroir : on ne peut pas les superposer"><line x1="320" y1="20" x2="320" y2="230" stroke="#94A3B8" stroke-width="3" stroke-dasharray="8 6"/><text x="320" y="252" font-size="13" text-anchor="middle" fill="#475569" font-weight="700">miroir</text><text x="170" y="158" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">C</text><line x1="101.3" y1="184.4" x2="157.5" y2="156.3" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><text x="78" y="204" font-size="20" text-anchor="middle" fill="#2A6BC4" font-family="Georgia, 'Times New Roman', serif">H<tspan font-size="13" dy="5">2</tspan><tspan dy="-5">N</tspan></text><line x1="182.5" y1="156.3" x2="231.6" y2="180.8" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><text x="262" y="204" font-size="20" text-anchor="middle" fill="#E11D48" font-family="Georgia, 'Times New Roman', serif">COOH</text><polygon points="170,136 134.8,78.4 125.2,85.6" fill="#1E293B"/><text x="120" y="74" font-size="20" text-anchor="middle" fill="#7C3AED" font-family="Georgia, 'Times New Roman', serif">R</text><line x1="173.9" y1="127.0" x2="177.5" y2="129.6" stroke="#1E293B" stroke-width="1.5"/><line x1="179.1" y1="118.8" x2="183.8" y2="122.3" stroke="#1E293B" stroke-width="1.5"/><line x1="184.2" y1="110.7" x2="190.1" y2="115.0" stroke="#1E293B" stroke-width="1.5"/><line x1="189.4" y1="102.5" x2="196.4" y2="107.7" stroke="#1E293B" stroke-width="1.5"/><line x1="194.5" y1="94.4" x2="202.6" y2="100.4" stroke="#1E293B" stroke-width="1.5"/><line x1="199.6" y1="86.3" x2="208.9" y2="93.2" stroke="#1E293B" stroke-width="1.5"/><text x="220" y="74" font-size="20" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">H</text><text x="470" y="158" font-size="22" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">C</text><line x1="482.5" y1="156.3" x2="538.7" y2="184.4" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><text x="562" y="204" font-size="20" text-anchor="middle" fill="#2A6BC4" font-family="Georgia, 'Times New Roman', serif">NH<tspan font-size="13" dy="5">2</tspan></text><line x1="457.5" y1="156.3" x2="408.4" y2="180.8" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/><text x="378" y="204" font-size="20" text-anchor="middle" fill="#E11D48" font-family="Georgia, 'Times New Roman', serif">HOOC</text><polygon points="470,136 514.8,85.6 505.2,78.4" fill="#1E293B"/><text x="520" y="74" font-size="20" text-anchor="middle" fill="#7C3AED" font-family="Georgia, 'Times New Roman', serif">R</text><line x1="462.5" y1="129.6" x2="466.1" y2="127.0" stroke="#1E293B" stroke-width="1.5"/><line x1="456.2" y1="122.3" x2="460.9" y2="118.8" stroke="#1E293B" stroke-width="1.5"/><line x1="449.9" y1="115.0" x2="455.8" y2="110.7" stroke="#1E293B" stroke-width="1.5"/><line x1="443.6" y1="107.7" x2="450.6" y2="102.5" stroke="#1E293B" stroke-width="1.5"/><line x1="437.4" y1="100.4" x2="445.5" y2="94.4" stroke="#1E293B" stroke-width="1.5"/><line x1="431.1" y1="93.2" x2="440.4" y2="86.3" stroke="#1E293B" stroke-width="1.5"/><text x="420" y="74" font-size="20" text-anchor="middle" fill="#1E293B" font-family="Georgia, 'Times New Roman', serif">H</text><text x="170" y="252" font-size="13" text-anchor="middle" fill="#475569" font-weight="700">forme L</text><text x="470" y="252" font-size="13" text-anchor="middle" fill="#475569" font-weight="700">forme D</text></svg>
<p class="nt-cap">Le coin plein désigne une liaison dirigée vers l'avant, les hachures une liaison dirigée vers l'arrière. On a beau tourner l'une des deux molécules dans tous les sens, on ne peut pas la superposer à l'autre.</p>
<p>Dans un environnement achiral, deux énantiomères ont les mêmes propriétés (mêmes températures de changement d'état, même densité…). Mais dans un environnement chiral, ils peuvent se comporter très différemment. Par exemple, les deux énantiomères de la carvone n'ont pas la même odeur pour nos récepteurs olfactifs, eux-mêmes faits de protéines chirales&nbsp;: l'un sent la menthe verte, l'autre le carvi.</p>
<p><b>La thalidomide.</b> Ce médicament des années 1950, vendu comme mélange des deux énantiomères, était prescrit aux femmes enceintes contre les nausées. L'énantiomère (R) avait l'effet sédatif recherché, mais l'énantiomère (S) s'est révélé gravement tératogène, provoquant des malformations chez des milliers de nouveau-nés. Isoler la «&nbsp;bonne&nbsp;» forme n'aurait d'ailleurs pas suffi&nbsp;: dans l'organisme, chaque énantiomère se transforme en partie en l'autre. À l'époque, les tests portaient surtout sur la toxicité aiguë, on pensait que le placenta protégeait le fœtus, et les rongeurs utilisés pour les essais se sont révélés insensibles à cet effet. Ce drame a conduit aux règles modernes des essais cliniques, qui imposent notamment l'étude des effets sur la reproduction.</p>
<p><b>Un vivant homochiral.</b> Les acides aminés des protéines sont tous de la même «&nbsp;main&nbsp;», la forme dite L (notée S avec les règles de nommage actuelles, sauf la cystéine qui, pour une raison de priorité des atomes, est notée R). Inverser un seul acide aminé dans une protéine peut empêcher son bon repliement. À l'inverse, les sucres de l'ADN et de l'ARN sont tous de forme «&nbsp;droite&nbsp;» (D). Un léger excès de forme L a été mesuré dans des acides aminés de météorites&nbsp;; une hypothèse est que la lumière polarisée circulairement émise dans le nuage présolaire aurait détruit préférentiellement l'une des deux formes.</p>
<p><a href="https://www.youtube.com/shorts/BoPLmR98S2k" target="_blank" rel="noopener">Une courte vidéo sur la chiralité</a>.</p>
</div>
</details>

## Solutions tampons {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp nt-hole">solution tampon</span> est une solution pour laquelle un ajout modéré d'acide ou de base modifie peu le pH. De même, son pH varie peu lors d'une dilution.</p>
<p class="nt-note">Les solutions tampons du commerce (pH 4, 7 et 10, par exemple) servent à étalonner les pH-mètres.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>L'effet tampon</p>
<p>L'effet tampon consiste en l'absorption ou la libération d'ions hydrogène par les espèces présentes en solution. On le rencontre dès qu'un acide $\color{#E11D48}\ce{AH}$ et sa base conjuguée $\color{#2A6BC4}\ce{A-}$ sont présents ensemble&nbsp;: si la concentration en ions oxonium varie, l'équilibre entre $\ce{AH}$ et $\ce{A-}$ se déplace de manière à compenser cette variation.</p>
<p>L'effet tampon est <span class="imp nt-hole">maximal</span> quand $\ce{[AH]}=\ce{[A-]}$, c'est-à-dire quand <span class="imp nt-hole">$\mathrm{pH}=\mathrm{p}K_\mathrm{A}$</span>. C'est ce que confirment les courbes de titrage&nbsp;: autour de la demi-équivalence, le pH varie très peu.</p>
</div>

<div class="nt-lab" id="lab-tampon">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Eau pure ou solution tampon&nbsp;?</p>
<p class="nt-note">100&nbsp;mL d'eau pure, comparés à 100&nbsp;mL d'une solution tampon contenant 10&nbsp;mmol d'acide éthanoïque et 10&nbsp;mmol d'ion éthanoate. On y ajoute de l'acide chlorhydrique ou de la soude concentrés.</p>
<canvas style="height:300px; background:#fff;" aria-label="pH de l'eau pure et de la solution tampon en fonction de la quantité d'acide ou de base ajoutée"></canvas>
<div class="nt-btns">
<button type="button" class="nt-btn" data-add="-0.5"><i class="fa-solid fa-droplet"></i>&nbsp; + 0,5 mmol d'acide</button>
<button type="button" class="nt-btn" data-add="0.5"><i class="fa-solid fa-droplet"></i>&nbsp; + 0,5 mmol de base</button>
<button type="button" class="nt-btn" data-act="dil">Diluer 10 fois</button>
<button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button>
</div>
<div class="nt-read" aria-live="polite"><span>pH de l'eau pure&nbsp;: <b class="out-w"></b></span><span>pH de la solution tampon&nbsp;: <b class="out-t"></b></span></div>
<p class="nt-note">Une seule goutte d'acide ou de base fait varier le pH de l'eau pure de plusieurs unités, alors que celui de la solution tampon bouge à peine. Diluez&nbsp;: le pH du tampon ne change presque pas.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-heart-pulse"></i>Le sang, une solution tampon</p>
<p>C'est principalement le couple acide carbonique $\ce{H2CO3}$ / ion hydrogénocarbonate (ou bicarbonate) $\ce{HCO3-}$ qui maintient le pH du sang entre 7,35 et 7,45. En dehors de cette petite fenêtre, une acidose ou une alcalose se développe rapidement, et peut être mortelle.</p>
<p>La forme ampholyte des acides aminés renforce aussi l'effet tampon&nbsp;: un excès d'ions $\ce{H+}$ peut être absorbé par le groupe $\ce{-COO-}$, et un déficit compensé par le groupe $\ce{-NH3+}$, qui peut en libérer.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">L'alcalose des ruminants</span></summary>
<div class="nt-d-body">
<p>Les alcaloses sont fréquentes chez les ruminants, par accumulation d'ammoniac lorsque leur alimentation est trop riche en azote. L'animal gonfle (il «&nbsp;météorise&nbsp;»), puis présente des signes de malaise&nbsp;: tremblements, salivation excessive, respiration rapide. On peut la traiter en lui faisant ingérer du vinaigre, riche en acide acétique.</p>
</div>
</details>

## Application&nbsp;: le chaulage d'un lac acide {.nt-h2}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Retour sur l'exercice du chaulage</p>
<p>Pourquoi utilise-t-on du carbonate de calcium pour remonter le pH d'un lac acide, sachant que l'ion carbonate est une base faible (couple $\ce{HCO3-}/\ce{CO3^{2-}}$, $\mathrm{p}K_\mathrm{A}=10{,}3$), plutôt qu'une base forte comme l'hydroxyde de sodium&nbsp;?</p>
<p>Pour comparer, on titre un litre d'une solution à pH 5,5, représentant l'eau du lac, par une solution d'ions carbonate, puis par une solution d'ions hydroxyde, toutes deux à $\pu{2,0E-4 mol*L-1}$. Cette concentration est-elle adaptée&nbsp;?</p>
</div>

<svg class="nt-svg" viewBox="0 0 660 350" role="img" aria-label="Titrage de l'eau du lac par la soude et par le carbonate de sodium à 2,0 × 10⁻⁴ mol/L : équivalence vers 16 mL, montée du pH plus progressive avec le carbonate"><line x1="70.0" y1="30" x2="70.0" y2="300" stroke="#E2E8F0"/><text x="70.0" y="318" font-size="12" text-anchor="middle" fill="#475569">0</text><line x1="138.8" y1="30" x2="138.8" y2="300" stroke="#E2E8F0"/><text x="138.8" y="318" font-size="12" text-anchor="middle" fill="#475569">5</text><line x1="207.5" y1="30" x2="207.5" y2="300" stroke="#E2E8F0"/><text x="207.5" y="318" font-size="12" text-anchor="middle" fill="#475569">10</text><line x1="276.2" y1="30" x2="276.2" y2="300" stroke="#E2E8F0"/><text x="276.2" y="318" font-size="12" text-anchor="middle" fill="#475569">15</text><line x1="345.0" y1="30" x2="345.0" y2="300" stroke="#E2E8F0"/><text x="345.0" y="318" font-size="12" text-anchor="middle" fill="#475569">20</text><line x1="413.8" y1="30" x2="413.8" y2="300" stroke="#E2E8F0"/><text x="413.8" y="318" font-size="12" text-anchor="middle" fill="#475569">25</text><line x1="482.5" y1="30" x2="482.5" y2="300" stroke="#E2E8F0"/><text x="482.5" y="318" font-size="12" text-anchor="middle" fill="#475569">30</text><line x1="551.2" y1="30" x2="551.2" y2="300" stroke="#E2E8F0"/><text x="551.2" y="318" font-size="12" text-anchor="middle" fill="#475569">35</text><line x1="620.0" y1="30" x2="620.0" y2="300" stroke="#E2E8F0"/><text x="620.0" y="318" font-size="12" text-anchor="middle" fill="#475569">40</text><line x1="70" y1="300.0" x2="620" y2="300.0" stroke="#E2E8F0"/><text x="62" y="304.0" font-size="12" text-anchor="end" fill="#475569">5</text><line x1="70" y1="246.0" x2="620" y2="246.0" stroke="#E2E8F0"/><text x="62" y="250.0" font-size="12" text-anchor="end" fill="#475569">6</text><line x1="70" y1="192.0" x2="620" y2="192.0" stroke="#E2E8F0"/><text x="62" y="196.0" font-size="12" text-anchor="end" fill="#475569">7</text><line x1="70" y1="138.0" x2="620" y2="138.0" stroke="#E2E8F0"/><text x="62" y="142.0" font-size="12" text-anchor="end" fill="#475569">8</text><line x1="70" y1="84.0" x2="620" y2="84.0" stroke="#E2E8F0"/><text x="62" y="88.0" font-size="12" text-anchor="end" fill="#475569">9</text><line x1="70" y1="30.0" x2="620" y2="30.0" stroke="#E2E8F0"/><text x="62" y="34.0" font-size="12" text-anchor="end" fill="#475569">10</text><line x1="70" y1="30" x2="70" y2="300" stroke="#1E293B"/><line x1="70" y1="300" x2="620" y2="300" stroke="#1E293B"/><text x="345.0" y="340" font-size="13" text-anchor="middle" fill="#475569">volume de solution titrante ajoutée (mL)</text><text x="22" y="165.0" font-size="13" text-anchor="middle" fill="#475569" transform="rotate(-90 22 165.0)">pH</text><polyline points="70.0,273.0 71.4,272.9 72.8,272.7 74.1,272.6 75.5,272.4 76.9,272.3 78.2,272.1 79.6,271.9 81.0,271.8 82.4,271.6 83.8,271.5 85.1,271.3 86.5,271.1 87.9,271.0 89.2,270.8 90.6,270.7 92.0,270.5 93.4,270.3 94.8,270.2 96.1,270.0 97.5,269.8 98.9,269.6 100.2,269.5 101.6,269.3 103.0,269.1 104.4,268.9 105.8,268.8 107.1,268.6 108.5,268.4 109.9,268.2 111.2,268.0 112.6,267.8 114.0,267.7 115.4,267.5 116.8,267.3 118.1,267.1 119.5,266.9 120.9,266.7 122.2,266.5 123.6,266.3 125.0,266.1 126.4,265.9 127.8,265.7 129.1,265.5 130.5,265.3 131.9,265.1 133.2,264.9 134.6,264.7 136.0,264.5 137.4,264.2 138.8,264.0 140.1,263.8 141.5,263.6 142.9,263.4 144.2,263.1 145.6,262.9 147.0,262.7 148.4,262.4 149.8,262.2 151.1,262.0 152.5,261.7 153.9,261.5 155.2,261.2 156.6,261.0 158.0,260.8 159.4,260.5 160.8,260.2 162.1,260.0 163.5,259.7 164.9,259.5 166.2,259.2 167.6,258.9 169.0,258.7 170.4,258.4 171.8,258.1 173.1,257.8 174.5,257.5 175.9,257.3 177.2,257.0 178.6,256.7 180.0,256.4 181.4,256.1 182.8,255.8 184.1,255.5 185.5,255.1 186.9,254.8 188.2,254.5 189.6,254.2 191.0,253.8 192.4,253.5 193.8,253.2 195.1,252.8 196.5,252.5 197.9,252.1 199.2,251.8 200.6,251.4 202.0,251.0 203.4,250.6 204.8,250.3 206.1,249.9 207.5,249.5 208.9,249.1 210.2,248.7 211.6,248.2 213.0,247.8 214.4,247.4 215.8,246.9 217.1,246.5 218.5,246.0 219.9,245.6 221.2,245.1 222.6,244.6 224.0,244.1 225.4,243.6 226.8,243.1 228.1,242.6 229.5,242.0 230.9,241.5 232.3,240.9 233.6,240.3 235.0,239.8 236.4,239.2 237.8,238.5 239.1,237.9 240.5,237.2 241.9,236.6 243.3,235.9 244.6,235.2 246.0,234.4 247.4,233.7 248.8,232.9 250.1,232.1 251.5,231.3 252.9,230.4 254.2,229.6 255.6,228.6 257.0,227.7 258.4,226.7 259.8,225.7 261.1,224.6 262.5,223.5 263.9,222.4 265.2,221.2 266.6,219.9 268.0,218.6 269.4,217.2 270.8,215.7 272.1,214.2 273.5,212.6 274.9,210.9 276.2,209.2 277.6,207.3 279.0,205.4 280.4,203.4 281.8,201.3 283.1,199.1 284.5,196.8 285.9,194.6 287.2,192.3 288.6,190.0 290.0,187.7 291.4,185.4 292.8,183.2 294.1,181.1 295.5,179.1 296.9,177.1 298.2,175.3 299.6,173.5 301.0,171.8 302.4,170.2 303.8,168.6 305.1,167.2 306.5,165.8 307.9,164.5 309.2,163.2 310.6,162.0 312.0,160.8 313.4,159.7 314.8,158.6 316.1,157.6 317.5,156.6 318.9,155.7 320.2,154.7 321.6,153.9 323.0,153.0 324.4,152.2 325.8,151.4 327.1,150.6 328.5,149.9 329.9,149.1 331.2,148.4 332.6,147.7 334.0,147.1 335.4,146.4 336.8,145.8 338.1,145.2 339.5,144.5 340.9,144.0 342.2,143.4 343.6,142.8 345.0,142.3 346.4,141.7 347.8,141.2 349.1,140.7 350.5,140.2 351.9,139.7 353.2,139.2 354.6,138.8 356.0,138.3 357.4,137.8 358.8,137.4 360.1,137.0 361.5,136.5 362.9,136.1 364.2,135.7 365.6,135.3 367.0,134.9 368.4,134.5 369.8,134.1 371.1,133.7 372.5,133.4 373.9,133.0 375.2,132.6 376.6,132.3 378.0,131.9 379.4,131.6 380.8,131.2 382.1,130.9 383.5,130.6 384.9,130.2 386.2,129.9 387.6,129.6 389.0,129.3 390.4,129.0 391.8,128.7 393.1,128.4 394.5,128.1 395.9,127.8 397.2,127.5 398.6,127.2 400.0,126.9 401.4,126.6 402.8,126.3 404.1,126.1 405.5,125.8 406.9,125.5 408.2,125.3 409.6,125.0 411.0,124.7 412.4,124.5 413.8,124.2 415.1,124.0 416.5,123.7 417.9,123.5 419.2,123.3 420.6,123.0 422.0,122.8 423.4,122.5 424.8,122.3 426.1,122.1 427.5,121.8 428.9,121.6 430.2,121.4 431.6,121.2 433.0,121.0 434.4,120.7 435.8,120.5 437.1,120.3 438.5,120.1 439.9,119.9 441.2,119.7 442.6,119.5 444.0,119.3 445.4,119.1 446.8,118.9 448.1,118.7 449.5,118.5 450.9,118.3 452.3,118.1 453.6,117.9 455.0,117.7 456.4,117.5 457.8,117.3 459.1,117.1 460.5,117.0 461.9,116.8 463.3,116.6 464.6,116.4 466.0,116.2 467.4,116.1 468.8,115.9 470.1,115.7 471.5,115.5 472.9,115.4 474.3,115.2 475.6,115.0 477.0,114.9 478.4,114.7 479.8,114.5 481.1,114.4 482.5,114.2 483.9,114.0 485.3,113.9 486.6,113.7 488.0,113.6 489.4,113.4 490.8,113.2 492.1,113.1 493.5,112.9 494.9,112.8 496.2,112.6 497.6,112.5 499.0,112.3 500.4,112.2 501.8,112.0 503.1,111.9 504.5,111.7 505.9,111.6 507.2,111.4 508.6,111.3 510.0,111.2 511.4,111.0 512.8,110.9 514.1,110.7 515.5,110.6 516.9,110.5 518.2,110.3 519.6,110.2 521.0,110.1 522.4,109.9 523.8,109.8 525.1,109.6 526.5,109.5 527.9,109.4 529.2,109.3 530.6,109.1 532.0,109.0 533.4,108.9 534.8,108.7 536.1,108.6 537.5,108.5 538.9,108.4 540.2,108.2 541.6,108.1 543.0,108.0 544.4,107.9 545.8,107.7 547.1,107.6 548.5,107.5 549.9,107.4 551.2,107.2 552.6,107.1 554.0,107.0 555.4,106.9 556.8,106.8 558.1,106.7 559.5,106.5 560.9,106.4 562.2,106.3 563.6,106.2 565.0,106.1 566.4,106.0 567.8,105.9 569.1,105.7 570.5,105.6 571.9,105.5 573.2,105.4 574.6,105.3 576.0,105.2 577.4,105.1 578.8,105.0 580.1,104.9 581.5,104.8 582.9,104.7 584.2,104.5 585.6,104.4 587.0,104.3 588.4,104.2 589.8,104.1 591.1,104.0 592.5,103.9 593.9,103.8 595.2,103.7 596.6,103.6 598.0,103.5 599.4,103.4 600.8,103.3 602.1,103.2 603.5,103.1 604.9,103.0 606.2,102.9 607.6,102.8 609.0,102.7 610.4,102.6 611.8,102.5 613.1,102.4 614.5,102.3 615.9,102.2 617.3,102.1 618.6,102.0 620.0,101.9" fill="none" stroke="#2A6BC4" stroke-width="2.6"/><polyline points="70.0,273.0 71.4,272.7 72.8,272.5 74.1,272.2 75.5,271.9 76.9,271.6 78.2,271.3 79.6,271.0 81.0,270.7 82.4,270.4 83.8,270.1 85.1,269.8 86.5,269.4 87.9,269.1 89.2,268.8 90.6,268.5 92.0,268.1 93.4,267.8 94.8,267.5 96.1,267.1 97.5,266.8 98.9,266.4 100.2,266.1 101.6,265.7 103.0,265.3 104.4,265.0 105.8,264.6 107.1,264.2 108.5,263.8 109.9,263.4 111.2,263.0 112.6,262.6 114.0,262.2 115.4,261.8 116.8,261.4 118.1,261.0 119.5,260.6 120.9,260.1 122.2,259.7 123.6,259.2 125.0,258.8 126.4,258.3 127.8,257.9 129.1,257.4 130.5,256.9 131.9,256.5 133.2,256.0 134.6,255.5 136.0,255.0 137.4,254.5 138.8,254.0 140.1,253.4 141.5,252.9 142.9,252.4 144.2,251.8 145.6,251.3 147.0,250.7 148.4,250.2 149.8,249.6 151.1,249.0 152.5,248.4 153.9,247.8 155.2,247.2 156.6,246.6 158.0,246.0 159.4,245.4 160.8,244.8 162.1,244.1 163.5,243.5 164.9,242.9 166.2,242.2 167.6,241.5 169.0,240.9 170.4,240.2 171.8,239.5 173.1,238.8 174.5,238.1 175.9,237.4 177.2,236.7 178.6,236.0 180.0,235.3 181.4,234.6 182.8,233.9 184.1,233.2 185.5,232.4 186.9,231.7 188.2,231.0 189.6,230.2 191.0,229.5 192.4,228.7 193.8,228.0 195.1,227.2 196.5,226.4 197.9,225.7 199.2,224.9 200.6,224.2 202.0,223.4 203.4,222.6 204.8,221.8 206.1,221.1 207.5,220.3 208.9,219.5 210.2,218.7 211.6,217.9 213.0,217.1 214.4,216.3 215.8,215.5 217.1,214.7 218.5,213.9 219.9,213.1 221.2,212.3 222.6,211.5 224.0,210.7 225.4,209.9 226.8,209.1 228.1,208.2 229.5,207.4 230.9,206.6 232.3,205.8 233.6,204.9 235.0,204.1 236.4,203.2 237.8,202.4 239.1,201.5 240.5,200.7 241.9,199.8 243.3,198.9 244.6,198.0 246.0,197.2 247.4,196.3 248.8,195.4 250.1,194.5 251.5,193.6 252.9,192.7 254.2,191.7 255.6,190.8 257.0,189.9 258.4,189.0 259.8,188.0 261.1,187.1 262.5,186.1 263.9,185.2 265.2,184.2 266.6,183.2 268.0,182.3 269.4,181.3 270.8,180.3 272.1,179.3 273.5,178.4 274.9,177.4 276.2,176.4 277.6,175.4 279.0,174.5 280.4,173.5 281.8,172.5 283.1,171.6 284.5,170.6 285.9,169.7 287.2,168.7 288.6,167.8 290.0,166.9 291.4,166.0 292.8,165.1 294.1,164.2 295.5,163.3 296.9,162.5 298.2,161.6 299.6,160.8 301.0,159.9 302.4,159.1 303.8,158.3 305.1,157.6 306.5,156.8 307.9,156.0 309.2,155.3 310.6,154.6 312.0,153.8 313.4,153.1 314.8,152.5 316.1,151.8 317.5,151.1 318.9,150.5 320.2,149.8 321.6,149.2 323.0,148.6 324.4,148.0 325.8,147.4 327.1,146.8 328.5,146.3 329.9,145.7 331.2,145.2 332.6,144.6 334.0,144.1 335.4,143.6 336.8,143.1 338.1,142.6 339.5,142.1 340.9,141.6 342.2,141.1 343.6,140.7 345.0,140.2 346.4,139.8 347.8,139.3 349.1,138.9 350.5,138.5 351.9,138.0 353.2,137.6 354.6,137.2 356.0,136.8 357.4,136.4 358.8,136.0 360.1,135.6 361.5,135.3 362.9,134.9 364.2,134.5 365.6,134.2 367.0,133.8 368.4,133.5 369.8,133.1 371.1,132.8 372.5,132.4 373.9,132.1 375.2,131.8 376.6,131.4 378.0,131.1 379.4,130.8 380.8,130.5 382.1,130.2 383.5,129.9 384.9,129.6 386.2,129.3 387.6,129.0 389.0,128.7 390.4,128.4 391.8,128.1 393.1,127.8 394.5,127.6 395.9,127.3 397.2,127.0 398.6,126.8 400.0,126.5 401.4,126.2 402.8,126.0 404.1,125.7 405.5,125.5 406.9,125.2 408.2,125.0 409.6,124.7 411.0,124.5 412.4,124.2 413.8,124.0 415.1,123.8 416.5,123.5 417.9,123.3 419.2,123.1 420.6,122.8 422.0,122.6 423.4,122.4 424.8,122.2 426.1,122.0 427.5,121.7 428.9,121.5 430.2,121.3 431.6,121.1 433.0,120.9 434.4,120.7 435.8,120.5 437.1,120.3 438.5,120.1 439.9,119.9 441.2,119.7 442.6,119.5 444.0,119.3 445.4,119.1 446.8,118.9 448.1,118.7 449.5,118.5 450.9,118.3 452.3,118.2 453.6,118.0 455.0,117.8 456.4,117.6 457.8,117.4 459.1,117.3 460.5,117.1 461.9,116.9 463.3,116.7 464.6,116.6 466.0,116.4 467.4,116.2 468.8,116.0 470.1,115.9 471.5,115.7 472.9,115.5 474.3,115.4 475.6,115.2 477.0,115.1 478.4,114.9 479.8,114.7 481.1,114.6 482.5,114.4 483.9,114.3 485.3,114.1 486.6,114.0 488.0,113.8 489.4,113.7 490.8,113.5 492.1,113.4 493.5,113.2 494.9,113.1 496.2,112.9 497.6,112.8 499.0,112.6 500.4,112.5 501.8,112.3 503.1,112.2 504.5,112.0 505.9,111.9 507.2,111.8 508.6,111.6 510.0,111.5 511.4,111.4 512.8,111.2 514.1,111.1 515.5,110.9 516.9,110.8 518.2,110.7 519.6,110.6 521.0,110.4 522.4,110.3 523.8,110.2 525.1,110.0 526.5,109.9 527.9,109.8 529.2,109.6 530.6,109.5 532.0,109.4 533.4,109.3 534.8,109.1 536.1,109.0 537.5,108.9 538.9,108.8 540.2,108.7 541.6,108.5 543.0,108.4 544.4,108.3 545.8,108.2 547.1,108.1 548.5,107.9 549.9,107.8 551.2,107.7 552.6,107.6 554.0,107.5 555.4,107.4 556.8,107.2 558.1,107.1 559.5,107.0 560.9,106.9 562.2,106.8 563.6,106.7 565.0,106.6 566.4,106.5 567.8,106.4 569.1,106.2 570.5,106.1 571.9,106.0 573.2,105.9 574.6,105.8 576.0,105.7 577.4,105.6 578.8,105.5 580.1,105.4 581.5,105.3 582.9,105.2 584.2,105.1 585.6,105.0 587.0,104.9 588.4,104.8 589.8,104.7 591.1,104.6 592.5,104.5 593.9,104.4 595.2,104.3 596.6,104.2 598.0,104.1 599.4,104.0 600.8,103.9 602.1,103.8 603.5,103.7 604.9,103.6 606.2,103.5 607.6,103.4 609.0,103.3 610.4,103.2 611.8,103.1 613.1,103.0 614.5,102.9 615.9,102.8 617.3,102.7 618.6,102.7 620.0,102.6" fill="none" stroke="#D97706" stroke-width="2.6"/><line x1="287.4" y1="30" x2="287.4" y2="300" stroke="#E11D48" stroke-width="1.2" stroke-dasharray="4 4"/><text x="293.4" y="44" font-size="12" fill="#E11D48" font-weight="700">V<tspan font-size="9" dy="3">E</tspan><tspan dy="-3"> ≈ 16 mL</tspan></text><rect x="370" y="218" width="240" height="56" rx="6" fill="#fff" stroke="#CBD5E1"/><line x1="382" y1="238" x2="410" y2="238" stroke="#2A6BC4" stroke-width="3"/><text x="418" y="242" font-size="12" fill="#1E293B">soude (HO⁻, base forte)</text><line x1="382" y1="260" x2="410" y2="260" stroke="#D97706" stroke-width="3"/><text x="418" y="264" font-size="12" fill="#1E293B">carbonate (CO₃²⁻, base faible)</text></svg>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir les éléments de réponse</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>La concentration est-elle adaptée&nbsp;?</b>
<ol class="nt-steps">
<li><p><b>Réaction support du titrage.</b> Avec la soude&nbsp;: $\ce{H3O+ + HO- -> 2 H2O}$. Avec le carbonate&nbsp;: $\ce{H3O+ + CO3^{2-} -> HCO3- + H2O}$. Dans les deux cas, un ion oxonium réagit avec une entité de la base.</p></li>
<li><p><b>À l'équivalence, les réactifs ont été introduits dans les proportions stœchiométriques</b>&nbsp;: la quantité de matière d'ions oxonium initialement présente est égale à la quantité de matière de base versée, $n_\mathrm{A} = n_\mathrm{B,E}$, soit&nbsp;:</p>
<p class="nt-center">$C_\mathrm{A}\times V_\mathrm{A} = C_\mathrm{B}\times V_\mathrm{E} \quad\Longrightarrow\quad V_\mathrm{E}=\dfrac{C_\mathrm{A}\times V_\mathrm{A}}{C_\mathrm{B}}$</p></li>
<li><p><b>Concentration de l'eau du lac en ions oxonium</b>&nbsp;: $C_\mathrm{A} = c°\times10^{-\mathrm{pH}} = 1{,}0\times10^{-5{,}5} \approx \pu{3,2E-6 mol*L-1}$.</p></li>
<li><p><b>Application numérique</b>&nbsp;: $V_\mathrm{E}=\dfrac{3{,}2\times10^{-6}\times 1{,}0}{2{,}0\times10^{-4}} = \pu{1,6E-2 L} = \pu{16 mL}$.</p></li>
<li><p><b>Conclusion.</b> Une burette usuelle contient 25&nbsp;mL&nbsp;: on vise un volume équivalent d'une dizaine de millilitres, en pratique entre 10 et 20&nbsp;mL environ. Assez grand pour que l'incertitude de lecture (de l'ordre d'une goutte, 0,05&nbsp;mL) reste faible devant $V_\mathrm{E}$&nbsp;; assez petit pour pouvoir verser encore un peu au-delà de l'équivalence sans remplir à nouveau la burette, ce qui compte pour tracer une courbe pH-métrique. Avec $V_\mathrm{E} \approx \pu{16 mL}$, la concentration est adaptée.</p>
<p class="nt-note">Si $V_\mathrm{E}$ est trop faible, on dilue la solution titrante (la diluer 2 fois multiplie $V_\mathrm{E}$ par 2)&nbsp;; s'il est trop grand, on utilise une solution titrante plus concentrée.</p></li>
</ol>
</li>
<li><b>Pourquoi le carbonate&nbsp;?</b> Autour de l'équivalence, le pH monte plus progressivement avec le carbonate&nbsp;; les couples de l'ion carbonate ($\ce{CO2,H2O}/\ce{HCO3-}$, puis $\ce{HCO3-}/\ce{CO3^{2-}}$) jouent le rôle de tampon, ce qui limite les conséquences d'un surdosage.</li>
<li><b>Sur le terrain</b>&nbsp;: le carbonate de calcium est très peu soluble. Il ne se dissout vraiment que s'il y a de l'acide à neutraliser&nbsp;: un excès reste au fond sous forme solide au lieu de rendre l'eau basique, et continue d'agir lors des pluies acides suivantes. C'est aussi un produit naturel (le calcaire), bon marché et sans danger, contrairement à la soude, très corrosive.</li>
</ul>
</div>
</details>

<script>
(function () {
  'use strict';
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CAC = '#E11D48', CBA = '#2A6BC4', CNE = '#16A34A', KE = 1e-14;   /* acide, base, neutre */
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function sci(x, nd) {
    if (x === 0) { return '0'; }
    var n = Math.floor(Math.log10(x) + 1e-9), a = x / Math.pow(10, n), t = a.toFixed(nd);
    if (parseFloat(t) >= 10) { n += 1; t = (a / 10).toFixed(nd); }
    return t.replace('.', ',') + ' \u00d7 10<sup>' + String(n).replace('-', '\u2212') + '</sup>';
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
    for (var gx = o.x0; gx <= o.x1 + 1e-9; gx += o.dx) { c.beginPath(); c.moveTo(X(gx), T); c.lineTo(X(gx), B); c.stroke(); }
    c.strokeStyle = col('--ink'); c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
    c.fillStyle = col('--slate'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'right';
    for (gy = o.y0; gy <= o.y1 + 1e-9; gy += o.dy) { c.fillText(o.fy ? o.fy(gy) : fr(gy, o.ndy || 0), L - 5, Y(gy) + 4); }
    c.textAlign = 'center';
    for (gx = o.x0; gx <= o.x1 + 1e-9; gx += o.dx) { c.fillText(o.fx ? o.fx(gx) : fr(gx, o.ndx || 0), X(gx), B + 14); }
    c.fillText(o.xl, (L + R) / 2, h - 3);
    c.save(); c.translate(12, (T + B) / 2); c.rotate(-Math.PI / 2); c.fillText(o.yl, 0, 0); c.restore();
    return { X: X, Y: Y, L: L, R: R, T: T, B: B };
  }
  function curve(c, F, f, x0, x1, color, w, dash) {
    c.strokeStyle = color; c.lineWidth = w || 2.4; c.setLineDash(dash || []); c.beginPath();
    for (var i = 0; i <= 300; i++) { var x = x0 + (x1 - x0) * i / 300, y = f(x); if (i === 0) { c.moveTo(F.X(x), F.Y(y)); } else { c.lineTo(F.X(x), F.Y(y)); } }
    c.stroke(); c.setLineDash([]);
  }
  function vline(c, F, x, color) { c.strokeStyle = color || 'rgba(30,41,59,.45)'; c.lineWidth = 1.2; c.setLineDash([4, 4]); c.beginPath(); c.moveTo(F.X(x), F.T); c.lineTo(F.X(x), F.B); c.stroke(); c.setLineDash([]); }
  function sup(n) { var m = { '-': '\u207b', 0: '\u2070', 1: '\u00b9', 2: '\u00b2', 3: '\u00b3', 4: '\u2074', 5: '\u2075', 6: '\u2076', 7: '\u2077', 8: '\u2078', 9: '\u2079' }; return String(n).split('').map(function (ch) { return m[ch]; }).join(''); }
  /* pH d'une solution : on cherche h = [H3O+] tel que la fonction (croissante en h) « bilan des charges » s'annule */
  function solvePH(f) { var lo = -15, hi = 1; for (var i = 0; i < 90; i++) { var m = (lo + hi) / 2; if (f(Math.pow(10, m)) > 0) { hi = m; } else { lo = m; } } return -(lo + hi) / 2; }
  /* acide faible AH (pKa, concentration C) seul dans l'eau */
  function phWeak(pKa, C) { var Ka = Math.pow(10, -pKa); return solvePH(function (h) { return h - C * Ka / (Ka + h) - KE / h; }); }
  function mix(c1, c2, t) {
    var a = [parseInt(c1.substr(1, 2), 16), parseInt(c1.substr(3, 2), 16), parseInt(c1.substr(5, 2), 16)], b = [parseInt(c2.substr(1, 2), 16), parseInt(c2.substr(3, 2), 16), parseInt(c2.substr(5, 2), 16)];
    return 'rgb(' + a.map(function (v, i) { return Math.round(v + (b[i] - v) * t); }).join(',') + ')';
  }
  /* ================= 1. L'autoprotolyse de l'eau ================= */
  (function () {
    var root = document.getElementById('lab-auto');
    if (!root) { return; }
    var cv = $(root, 'canvas'), r = $(root, 'input[type="range"]'), oP = $(root, '.out-ph'), oH = $(root, '.out-h'), oO = $(root, '.out-o'), msg = $(root, '.nt-msg'), S;
    function draw() {
      var pH = +r.value, h = Math.pow(10, -pH), o = KE / h, c = S.ctx, w = S.w, H = S.h;
      oP.textContent = fr(pH, 1); oH.innerHTML = sci(h, 1) + ' mol\u00b7L<sup>\u22121</sup>'; oO.innerHTML = sci(o, 1) + ' mol\u00b7L<sup>\u22121</sup>';
      c.clearRect(0, 0, w, H);
      /* barres en échelle logarithmique : de 10^-14 à 1 mol/L */
      var L = 70, B = H - 90, T = 16, bw = 70;
      function Y(c0) { return B - (Math.log10(c0) + 14) / 14 * (B - T); }
      c.strokeStyle = col('--ink'); c.lineWidth = 1; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.stroke();
      for (var e = 0; e >= -14; e -= 2) { c.fillStyle = col('--slate'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'right'; c.fillText('10' + sup(e), L - 6, Y(Math.pow(10, e)) + 4); c.strokeStyle = col('--line'); c.beginPath(); c.moveTo(L, Y(Math.pow(10, e))); c.lineTo(w - 20, Y(Math.pow(10, e))); c.stroke(); }
      txt(c, 'concentration (mol\u00b7L\u207b\u00b9, échelle log.)', L + 8, T + 2, col('--slate'), '600 11px system-ui, sans-serif', 'left');
      [[h, CAC, 'H\u2083O\u207a', 0.3], [o, CBA, 'HO\u207b', 0.62]].forEach(function (q) {
        var x = w * q[3] - bw / 2; c.fillStyle = q[1]; c.globalAlpha = 0.85; c.fillRect(x, Y(q[0]), bw, B - Y(q[0])); c.globalAlpha = 1;
        txt(c, '[' + q[2] + ']', x + bw / 2, B + 18, q[1], '700 14px system-ui, sans-serif');
      });
      /* échelle de pH colorée */
      var y0 = H - 46, x0 = L, x1 = w - 20;
      var g = c.createLinearGradient(x0, 0, x1, 0); g.addColorStop(0, '#FCA5A5'); g.addColorStop(0.5, '#86EFAC'); g.addColorStop(1, '#93C5FD');
      c.fillStyle = g; c.fillRect(x0, y0, x1 - x0, 14);
      for (var p = 0; p <= 14; p += 2) { txt(c, String(p), x0 + p / 14 * (x1 - x0), y0 + 30, col('--slate'), '11px system-ui, sans-serif'); }
      txt(c, 'acide', x0 + 0.2 * (x1 - x0), y0 - 4, CAC, '700 11px system-ui, sans-serif'); txt(c, 'neutre', x0 + 0.5 * (x1 - x0), y0 - 4, CNE, '700 11px system-ui, sans-serif'); txt(c, 'basique', x0 + 0.8 * (x1 - x0), y0 - 4, CBA, '700 11px system-ui, sans-serif');
      var xm = x0 + pH / 14 * (x1 - x0); c.fillStyle = col('--ink'); c.beginPath(); c.moveTo(xm, y0 + 16); c.lineTo(xm - 7, y0 + 26); c.lineTo(xm + 7, y0 + 26); c.closePath(); c.fill();
      msg.textContent = Math.abs(pH - 7) < 0.05 ? 'Solution neutre : [H\u2083O\u207a] = [HO\u207b] = 1,0 \u00d7 10\u207b\u2077 mol/L.' : (pH < 7 ? 'Solution acide : [H\u2083O\u207a] > [HO\u207b]. Quand l\u2019une augmente, l\u2019autre diminue d\u2019autant : leur produit reste égal à Ke.' : 'Solution basique : [HO\u207b] > [H\u2083O\u207a]. Quand l\u2019une augmente, l\u2019autre diminue d\u2019autant : leur produit reste égal à Ke.');
    }
    r.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 2. Acide fort ou acide faible ================= */
  (function () {
    var root = document.getElementById('lab-force');
    if (!root) { return; }
    var c1 = $(root, 'canvas.c1'), c2 = $(root, 'canvas.c2'), rK = $(root, '[data-p="pka"]'), rC = $(root, '[data-p="c"]');
    var oK = $(root, '.out-pka'), oC = $(root, '.out-c'), oT = $(root, '.out-tau'), oW = $(root, '.out-phw'), oS = $(root, '.out-phs'), S1, S2;
    function draw() {
      var pKa = +rK.value, lc = +rC.value, C = Math.pow(10, lc), Ka = Math.pow(10, -pKa);
      function tau(l) { var cc = Math.pow(10, l), h = Math.pow(10, -phWeak(pKa, cc)); return Ka / (Ka + h); }
      function phS(l) { var cc = Math.pow(10, l); return solvePH(function (h) { return h - cc - KE / h; }); }
      oK.textContent = fr(pKa, 1); oC.innerHTML = sci(C, 1) + ' mol\u00b7L<sup>\u22121</sup>';
      oT.textContent = fr(100 * tau(lc), 1) + ' %'; oW.textContent = fr(phWeak(pKa, C), 2); oS.textContent = fr(phS(lc), 2);
      var fx = function (v) { return '10' + sup(v); };
      var a = S1.ctx; a.clearRect(0, 0, S1.w, S1.h);
      var F = frame(a, S1.w, S1.h, { x0: -6, x1: 0, dx: 1, y0: 0, y1: 1, dy: 0.25, ndy: 2, fx: fx, xl: 'concentration apportée C (mol\u00b7L\u207b\u00b9)', yl: 'taux d\u2019avancement \u03c4' });
      curve(a, F, function () { return 1; }, -6, 0, CAC, 2, [6, 4]); curve(a, F, tau, -6, 0, '#7C3AED');
      txt(a, 'acide fort', F.R - 6, F.Y(1) + 15, CAC, '700 11px system-ui, sans-serif', 'right'); txt(a, 'acide faible', F.R - 6, F.Y(tau(0)) - 6, '#7C3AED', '700 11px system-ui, sans-serif', 'right');
      vline(a, F, lc);
      var b = S2.ctx; b.clearRect(0, 0, S2.w, S2.h);
      var G = frame(b, S2.w, S2.h, { x0: -6, x1: 0, dx: 1, y0: 0, y1: 8, dy: 1, fx: fx, xl: 'concentration apportée C (mol\u00b7L\u207b\u00b9)', yl: 'pH' });
      curve(b, G, phS, -6, 0, CAC, 2, [6, 4]); curve(b, G, function (l) { return phWeak(pKa, Math.pow(10, l)); }, -6, 0, '#7C3AED');
      txt(b, 'acide fort : pH = \u2212log(C/c°)', G.L + 8, G.B - 8, CAC, '700 11px system-ui, sans-serif', 'left');
      vline(b, G, lc);
    }
    [rK, rC].forEach(function (r) { r.addEventListener('input', draw); });
    function setup() { S1 = canvasCtx(c1); S2 = canvasCtx(c2); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 3. Diagrammes de distribution et de prédominance ================= */
  var COUPLES = {
    ethan: { pka: 4.8, a: 'CH\u2083COOH', b: 'CH\u2083COO\u207b' },
    ammon: { pka: 9.2, a: 'NH\u2084\u207a', b: 'NH\u2083' },
    meth: { pka: 3.8, a: 'HCOOH', b: 'HCOO\u207b' },
    bbt: { pka: 7.1, a: 'forme acide', b: 'forme basique', ca: '#FDE047', cm: '#22C55E', cb: '#2563EB', nom: 'bleu de bromothymol' },
    phph: { pka: 9.4, a: 'forme acide', b: 'forme basique', ca: '#F8FAFC', cm: '#F9A8D4', cb: '#DB2777', nom: 'phénolphtaléine' },
    hel: { pka: 3.7, a: 'forme acide', b: 'forme basique', ca: '#DC2626', cm: '#F97316', cb: '#FDE047', nom: 'hélianthine' }
  };
  (function () {
    var root = document.getElementById('lab-distrib');
    if (!root) { return; }
    var cv = $(root, 'canvas'), r = $(root, 'input[type="range"]'), oP = $(root, '.out-ph'), oA = $(root, '.out-ra'), oB = $(root, '.out-rb'), msg = $(root, '.nt-msg'), S, key = 'ethan';
    function draw() {
      var cp = COUPLES[key], pH = +r.value, c = S.ctx, w = S.w, h = S.h, rb = 1 / (1 + Math.pow(10, cp.pka - pH)), ra = 1 - rb;
      oP.textContent = fr(pH, 1); oA.textContent = fr(100 * ra, 1) + ' %'; oB.textContent = fr(100 * rb, 1) + ' %';
      c.clearRect(0, 0, w, h);
      var F = frame(c, w, h, { x0: 0, x1: 14, dx: 1, y0: 0, y1: 1, dy: 0.25, fy: function (v) { return Math.round(v * 100) + ' %'; }, xl: 'pH', yl: 'proportion', L: 56, B: 96 });
      function lum(hx) { return 0.299 * parseInt(hx.substr(1, 2), 16) + 0.587 * parseInt(hx.substr(3, 2), 16) + 0.114 * parseInt(hx.substr(5, 2), 16); }
      var ca = cp.ca || CAC, cb = cp.cb || CBA, ka = ca === '#F8FAFC' ? '#94A3B8' : ca;
      var ta = lum(ka) > 190 ? '#A16207' : ka, tb = lum(cb) > 190 ? '#A16207' : cb;   /* jaune clair : texte plus foncé */
      curve(c, F, function (p) { return 1 - 1 / (1 + Math.pow(10, cp.pka - p)); }, 0, 14, ka);
      curve(c, F, function (p) { return 1 / (1 + Math.pow(10, cp.pka - p)); }, 0, 14, cb);
      txt(c, cp.a, F.X(Math.max(0.6, cp.pka - 3.2)), F.Y(1) + 16, ta, '700 12px system-ui, sans-serif');
      txt(c, cp.b, F.X(Math.min(13.4, cp.pka + 3.2)), F.Y(1) + 16, tb, '700 12px system-ui, sans-serif');
      c.strokeStyle = 'rgba(22,163,74,.6)'; c.setLineDash([3, 3]); c.lineWidth = 1.2; c.beginPath(); c.moveTo(F.L, F.Y(0.5)); c.lineTo(F.X(cp.pka), F.Y(0.5)); c.lineTo(F.X(cp.pka), F.B); c.stroke(); c.setLineDash([]);
      txt(c, 'pK\u2090 = ' + fr(cp.pka, 1), F.X(cp.pka) + 4, F.Y(0.5) - 6, CNE, '700 12px system-ui, sans-serif', 'left');
      vline(c, F, pH, 'rgba(30,41,59,.6)');
      /* diagramme de prédominance */
      var yP = h - 50, xk = F.X(cp.pka);
      c.fillStyle = cp.ca ? cp.ca : 'rgba(225,29,72,.18)'; c.fillRect(F.L, yP, xk - F.L, 24);
      c.fillStyle = cp.cb ? cp.cb : 'rgba(42,107,196,.18)'; c.fillRect(xk, yP, F.R - xk, 24);
      c.strokeStyle = col('--ink'); c.lineWidth = 1; c.strokeRect(F.L, yP, F.R - F.L, 24);
      c.lineWidth = 2; c.beginPath(); c.moveTo(xk, yP - 6); c.lineTo(xk, yP + 30); c.stroke();
      function ink(hex) { if (!hex) { return null; } var r0 = parseInt(hex.substr(1, 2), 16), g0 = parseInt(hex.substr(3, 2), 16), b0 = parseInt(hex.substr(5, 2), 16); return 0.299 * r0 + 0.587 * g0 + 0.114 * b0 > 150 ? '#1E293B' : '#FFFFFF'; }   /* texte lisible sur la couleur du fond */
      c.font = '700 12px system-ui, sans-serif'; c.textAlign = 'center';
      c.fillStyle = ink(cp.ca) || CAC; c.fillText(cp.a + ' prédomine', (F.L + xk) / 2, yP + 16);
      c.fillStyle = ink(cp.cb) || CBA; c.fillText(cp.b + ' prédomine', (xk + F.R) / 2, yP + 16);
      var xm = F.X(pH); c.fillStyle = col('--ink'); c.beginPath(); c.moveTo(xm, yP + 26); c.lineTo(xm - 6, yP + 36); c.lineTo(xm + 6, yP + 36); c.closePath(); c.fill();
      txt(c, 'diagramme de prédominance', F.L, yP - 8, col('--slate'), '600 11px system-ui, sans-serif', 'left');
      if (cp.ca) {   /* indicateur : couleur de la solution, mélange des deux formes */
        var sw = rb < 0.5 ? mix(cp.ca, cp.cm, 2 * rb) : mix(cp.cm, cp.cb, 2 * rb - 1);   /* teinte de la zone de virage au milieu (vert pour le BBT) */
        c.fillStyle = sw; c.strokeStyle = col('--slate'); c.lineWidth = 1.5; c.beginPath(); c.rect(F.R - 70, F.T + 34, 56, 56); c.fill(); c.stroke();
        txt(c, 'couleur', F.R - 42, F.T + 104, col('--slate'), '600 11px system-ui, sans-serif');
        msg.textContent = cp.nom + ' : ' + (Math.abs(pH - cp.pka) <= 1 ? 'dans la zone de virage (autour du pKa), les deux formes coexistent et la couleur est un mélange des deux.' : (pH < cp.pka ? 'la forme acide prédomine : on voit sa couleur.' : 'la forme basique prédomine : on voit sa couleur.'));
      } else {
        msg.textContent = Math.abs(pH - cp.pka) < 0.05 ? 'pH = pKa : l\u2019acide et sa base conjuguée sont en quantités égales (50 % chacun).' : (pH < cp.pka ? 'pH < pKa : l\u2019acide ' + cp.a + ' prédomine.' : 'pH > pKa : la base ' + cp.b + ' prédomine.');
      }
    }
    r.addEventListener('input', draw);
    $$(root, 'input[name="couple"]').forEach(function (x) { x.addEventListener('change', function () { key = x.value; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 4. Choisir un indicateur coloré ================= */
  (function () {
    var root = document.getElementById('lab-indic');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), S, ind = 'phph';
    var IND = { hel: ['hélianthine', 3.1, 4.4, '#DC2626', '#FDE047'], rm: ['rouge de méthyle', 4.2, 6.2, '#DC2626', '#FDE047'], bbt: ['bleu de bromothymol', 6.0, 7.6, '#FDE047', '#2563EB'], phph: ['phénolphtaléine', 8.2, 10.0, '#F1F5F9', '#DB2777'] };
    var Ca = 0.10, Va = 10, Cb = 0.10, pKa = 4.8, Ka = Math.pow(10, -pKa), VE = Ca * Va / Cb;
    function pHV(V) {   /* titrage de l'acide éthanoïque par la soude : bilan des charges exact */
      var Vt = Va + V, CT = Ca * Va / Vt, Na = Cb * V / Vt;
      return solvePH(function (h) { return h + Na - CT * Ka / (Ka + h) - KE / h; });
    }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, it = IND[ind];
      c.clearRect(0, 0, w, h);
      var F = frame(c, w, h, { x0: 0, x1: 20, dx: 2, y0: 0, y1: 14, dy: 2, xl: 'volume de soude versé V (mL)', yl: 'pH' });
      c.fillStyle = it[3] === '#F1F5F9' ? 'rgba(219,39,119,.12)' : 'rgba(234,179,8,.18)';
      var g = c.createLinearGradient(0, F.Y(it[1]), 0, F.Y(it[2])); g.addColorStop(0, it[3] === '#F1F5F9' ? 'rgba(226,232,240,.6)' : it[3] + '55'); g.addColorStop(1, it[4] + '66');
      c.fillStyle = g; c.fillRect(F.L, F.Y(it[2]), F.R - F.L, F.Y(it[1]) - F.Y(it[2]));
      txt(c, 'zone de virage : ' + it[0], F.R - 6, F.Y(it[2]) - 5, col('--slate'), '700 11px system-ui, sans-serif', 'right');
      curve(c, F, pHV, 0, 20, CBA);
      var pE = pHV(VE); c.fillStyle = CAC; c.beginPath(); c.arc(F.X(VE), F.Y(pE), 5, 0, 2 * Math.PI); c.fill();
      txt(c, 'E (pH = ' + fr(pE, 1) + ')', F.X(VE) + 8, F.Y(pE) + 4, CAC, '700 12px system-ui, sans-serif', 'left');
      var ok = pE >= it[1] && pE <= it[2];
      msg.innerHTML = ok ? '<b style="color:#16A34A;">Indicateur adapté</b> : sa zone de virage contient pH<sub>E</sub>, elle est entièrement dans le saut de pH. Le changement de couleur se fait à la goutte près, à l\u2019équivalence.'
        : '<b style="color:#E11D48;">Indicateur mal adapté</b> : sa zone de virage ne contient pas pH<sub>E</sub>. Le changement de couleur aurait lieu ' + (it[2] < pE ? 'avant' : 'après') + ' l\u2019équivalence.';
    }
    $$(root, 'input[name="ind2"]').forEach(function (x) { x.addEventListener('change', function () { ind = x.value; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 5. L'effet tampon ================= */
  (function () {
    var root = document.getElementById('lab-tampon');
    if (!root) { return; }
    var cv = $(root, 'canvas'), oW = $(root, '.out-w'), oT = $(root, '.out-t'), S, add = 0, vol = 0.1, hist = [];
    /* 100 mL d'eau pure, ou de tampon (10 mmol d'acide éthanoïque + 10 mmol d'éthanoate de sodium) ; add > 0 : soude, add < 0 : acide chlorhydrique (en mmol) */
    var Ka = Math.pow(10, -4.8);
    function phWater(n, V) { var c = n * 1e-3 / V; return solvePH(function (h) { return h + Math.max(c, 0) - Math.max(-c, 0) - KE / h; }); }
    function phBuf(n, V) {
      var CT = 20e-3 / V, Na = (10e-3 + Math.max(n, 0) * 1e-3) / V, Cl = Math.max(-n, 0) * 1e-3 / V;
      return solvePH(function (h) { return h + Na - Cl - CT * Ka / (Ka + h) - KE / h; });
    }
    function record() { hist.push([add, phWater(add, vol), phBuf(add, vol)]); }
    function draw() {
      var pw = phWater(add, vol), pb = phBuf(add, vol), c = S.ctx, w = S.w, h = S.h;
      oW.textContent = fr(pw, 2); oT.textContent = fr(pb, 2);
      c.clearRect(0, 0, w, h);
      var F = frame(c, w, h, { x0: -5, x1: 5, dx: 1, y0: 0, y1: 14, dy: 2, xl: 'acide (\u2212) ou base (+) ajoutés (mmol)', yl: 'pH' });
      curve(c, F, function (n) { return phWater(n, vol); }, -5, 5, '#64748B', 2, [6, 4]);
      curve(c, F, function (n) { return phBuf(n, vol); }, -5, 5, '#7C3AED', 2.6);
      txt(c, 'eau pure', F.X(1.2), F.Y(phWater(1.2, vol)) - 8, '#475569', '700 12px system-ui, sans-serif', 'left');
      txt(c, 'solution tampon (pK\u2090 = 4,8)', F.X(-4.8), F.Y(phBuf(-4.8, vol)) - 10, '#7C3AED', '700 12px system-ui, sans-serif', 'left');
      [[pw, '#64748B'], [pb, '#7C3AED']].forEach(function (q) { c.fillStyle = q[1]; c.beginPath(); c.arc(F.X(add), F.Y(q[0]), 6, 0, 2 * Math.PI); c.fill(); });
      vline(c, F, add);
      txt(c, 'volume : ' + Math.round(vol * 1000) + ' mL', F.L + 8, F.T + 14, col('--slate'), '600 11px system-ui, sans-serif', 'left');
    }
    $$(root, '[data-add]').forEach(function (b) { b.addEventListener('click', function () { add = Math.max(-5, Math.min(5, add + parseFloat(b.getAttribute('data-add')))); draw(); }); });
    $(root, '[data-act="dil"]').addEventListener('click', function () { vol = vol >= 10 ? 0.1 : vol * 10; draw(); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { add = 0; vol = 0.1; draw(); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
})();
</script>
