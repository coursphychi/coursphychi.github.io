+++
title = "Méthodes physiques d'analyse"
draft = false
hidden = "true"
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Analyser un système chimique par des méthodes physiques&nbsp;: déterminer la nature ou la quantité des espèces présentes en mesurant une grandeur physique (absorbance, conductivité, pression…), sans les faire réagir.</p>

## Spectroscopie {.nt-h2}

### Spectroscopie UV-Visible {.nt-h3}

<svg class="nt-svg" viewBox="0 0 760 230" role="img" aria-label="Principe du spectrophotomètre : une lumière monochromatique d'intensité I0 traverse une cuve d'épaisseur ℓ ; le détecteur mesure l'intensité transmise I"><defs><linearGradient id="gW" x1="0" x2="1"><stop offset="0" stop-color="#8B5CF6"/><stop offset=".25" stop-color="#3B82F6"/><stop offset=".5" stop-color="#22C55E"/><stop offset=".75" stop-color="#EAB308"/><stop offset="1" stop-color="#EF4444"/></linearGradient></defs><circle cx="60" cy="110" r="26" fill="#FDE68A" stroke="var(--slate)" stroke-width="2"/><text x="60" y="160" font-size="13" text-anchor="middle" fill="var(--slate)">lampe</text><rect x="96" y="104" width="64" height="12" fill="url(#gW)" opacity=".85"/><polygon points="170,140 200,80 230,140" fill="#E2E8F0" stroke="var(--slate)" stroke-width="2"/><text x="200" y="166" font-size="13" text-anchor="middle" fill="var(--slate)">monochromateur</text><text x="200" y="182" font-size="12" text-anchor="middle" fill="var(--slate)">(choix de λ)</text><line x1="240" y1="110" x2="382.0" y2="110.0" stroke="#22C55E" stroke-width="4"/><polygon points="390.0,110.0 381.0,114.5 381.0,105.5" fill="#22C55E"/><text x="314" y="96" font-size="20" fill="#16A34A" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">I<tspan font-size="13" dy="5">0</tspan></text><rect x="400" y="62" width="80" height="96" rx="4" fill="#38BDF8" fill-opacity=".35" stroke="var(--slate)" stroke-width="2"/><text x="440" y="116" font-size="18" fill="var(--blue)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">C</text><text x="440" y="50" font-size="13" text-anchor="middle" fill="var(--slate)">cuve + solution</text><line x1="408.0" y1="178.0" x2="472.0" y2="178.0" stroke="var(--slate)" stroke-width="1.6"/><polygon points="480.0,178.0 471.0,182.5 471.0,173.5" fill="var(--slate)"/><polygon points="400.0,178.0 409.0,173.5 409.0,182.5" fill="var(--slate)"/><text x="440" y="200" font-size="18" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">ℓ</text><line x1="490" y1="110" x2="602.0" y2="110.0" stroke="#22C55E" stroke-width="2"/><polygon points="610.0,110.0 601.0,114.5 601.0,105.5" fill="#22C55E"/><text x="550" y="96" font-size="20" fill="#16A34A" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">I</text><rect x="620" y="82" width="56" height="56" rx="8" fill="var(--slate)"/><text x="648" y="160" font-size="13" text-anchor="middle" fill="var(--slate)">détecteur</text><rect x="630" y="96" width="36" height="20" rx="3" fill="#0B1220"/><text x="648" y="111" font-size="11" text-anchor="middle" fill="#4ADE80" font-family="monospace">0,42</text></svg>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp">absorbance $A_\lambda$</span> d'une solution quantifie la proportion d'un rayonnement incident $I_0$ monochromatique absorbée en mesurant l'intensité du rayonnement transmis $I$.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">L'absorbance n'est pas un pourcentage</span></summary>
<div class="nt-d-body">
<p>L'absorbance est définie par $A_\lambda = \log\left(\dfrac{I_0}{I}\right)$. Elle peut donc être supérieure à 1&nbsp;: ce n'est pas un pourcentage.</p>
<ul class="nt-facts">
<li>$A = 0$&nbsp;: toute la lumière est transmise ($I = I_0$)&nbsp;;</li>
<li>$A = 1$&nbsp;: seulement 10&nbsp;% de la lumière est transmise&nbsp;;</li>
<li>$A = 2$&nbsp;: seulement 1&nbsp;% de la lumière est transmise.</li>
</ul>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le spectre ultraviolet-visible d'une solution est la courbe représentant l'<span class="imp">absorbance $A_\lambda$</span> (<span class="nt-hole">sans unité</span>) en fonction de la <span class="imp">longueur d'onde $\lambda$</span>, pour $\lambda$ pouvant aller d'environ 200 à 800&nbsp;nm.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Lorsque la solution absorbe dans le visible, comment peut-on relier un spectre d'absorption à la couleur perçue&nbsp;?</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La solution agit comme un <span class="imp nt-hole">filtre</span>. La couleur absorbée est donc <span class="imp nt-hole">complémentaire</span> de la couleur perçue.</p>
</div>

<div class="nt-lab" id="lab-roue">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le cercle chromatique</p>
<svg class="nt-svg nt-svg-m nt-wheel" viewBox="0 0 600 460" role="img" aria-label="Cercle chromatique : chaque couleur est diamétralement opposée à sa couleur complémentaire"><path class="nt-wseg" data-i="0" d="M258.6,75.5 A160,160 0 0,1 341.4,75.5 L323.8,141.1 A92,92 0 0,0 276.2,141.1 Z" fill="#F5D90A" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="jaune"/><text x="300.0" y="28.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">jaune</text><text x="300.0" y="43.0" font-size="11" text-anchor="middle" fill="var(--slate)">560–590 nm</text><path class="nt-wseg" data-i="1" d="M341.4,75.5 A160,160 0 0,1 413.1,116.9 L365.1,164.9 A92,92 0 0,0 323.8,141.1 Z" fill="#F59E0B" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="orange"/><text x="400.0" y="54.8" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">orange</text><text x="400.0" y="69.8" font-size="11" text-anchor="middle" fill="var(--slate)">590–625 nm</text><path class="nt-wseg" data-i="2" d="M413.1,116.9 A160,160 0 0,1 454.5,188.6 L388.9,206.2 A92,92 0 0,0 365.1,164.9 Z" fill="#EF5A2A" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="rouge-orange"/><text x="473.2" y="128.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">rouge-orange</text><text x="473.2" y="143.0" font-size="11" text-anchor="middle" fill="var(--slate)">625–650 nm</text><path class="nt-wseg" data-i="3" d="M454.5,188.6 A160,160 0 0,1 454.5,271.4 L388.9,253.8 A92,92 0 0,0 388.9,206.2 Z" fill="#DC2626" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="rouge"/><text x="500.0" y="228.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">rouge</text><text x="500.0" y="243.0" font-size="11" text-anchor="middle" fill="var(--slate)">650–800 nm</text><path class="nt-wseg" data-i="4" d="M454.5,271.4 A160,160 0 0,1 413.1,343.1 L365.1,295.1 A92,92 0 0,0 388.9,253.8 Z" fill="#D6338A" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="magenta"/><text x="473.2" y="328.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">magenta</text><path class="nt-wseg" data-i="5" d="M413.1,343.1 A160,160 0 0,1 341.4,384.5 L323.8,318.9 A92,92 0 0,0 365.1,295.1 Z" fill="#7C3AED" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="violet"/><text x="400.0" y="401.2" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">violet</text><text x="400.0" y="416.2" font-size="11" text-anchor="middle" fill="var(--slate)">400–420 nm</text><path class="nt-wseg" data-i="6" d="M341.4,384.5 A160,160 0 0,1 258.6,384.5 L276.2,318.9 A92,92 0 0,0 323.8,318.9 Z" fill="#4F46E5" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="bleu indigo"/><text x="300.0" y="428.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">bleu indigo</text><text x="300.0" y="443.0" font-size="11" text-anchor="middle" fill="var(--slate)">420–465 nm</text><path class="nt-wseg" data-i="7" d="M258.6,384.5 A160,160 0 0,1 186.9,343.1 L234.9,295.1 A92,92 0 0,0 276.2,318.9 Z" fill="#2563EB" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="bleu"/><text x="200.0" y="401.2" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">bleu</text><text x="200.0" y="416.2" font-size="11" text-anchor="middle" fill="var(--slate)">465–485 nm</text><path class="nt-wseg" data-i="8" d="M186.9,343.1 A160,160 0 0,1 145.5,271.4 L211.1,253.8 A92,92 0 0,0 234.9,295.1 Z" fill="#06B6D4" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="cyan"/><text x="126.8" y="328.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">cyan</text><text x="126.8" y="343.0" font-size="11" text-anchor="middle" fill="var(--slate)">485–510 nm</text><path class="nt-wseg" data-i="9" d="M145.5,271.4 A160,160 0 0,1 145.5,188.6 L211.1,206.2 A92,92 0 0,0 211.1,253.8 Z" fill="#14B8A6" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="bleu-vert"/><text x="100.0" y="228.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">bleu-vert</text><text x="100.0" y="243.0" font-size="11" text-anchor="middle" fill="var(--slate)">510–520 nm</text><path class="nt-wseg" data-i="10" d="M145.5,188.6 A160,160 0 0,1 186.9,116.9 L234.9,164.9 A92,92 0 0,0 211.1,206.2 Z" fill="#22C55E" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="vert"/><text x="126.8" y="128.0" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">vert</text><text x="126.8" y="143.0" font-size="11" text-anchor="middle" fill="var(--slate)">520–550 nm</text><path class="nt-wseg" data-i="11" d="M186.9,116.9 A160,160 0 0,1 258.6,75.5 L276.2,141.1 A92,92 0 0,0 234.9,164.9 Z" fill="#A3E635" stroke="#fff" stroke-width="2" tabindex="0" role="button" aria-label="jaune-vert"/><text x="200.0" y="54.8" font-size="13" text-anchor="middle" font-weight="700" fill="var(--ink)">jaune-vert</text><text x="200.0" y="69.8" font-size="11" text-anchor="middle" fill="var(--slate)">550–560 nm</text><circle cx="300" cy="230" r="82" fill="#fff"/><text class="nt-wtxt1" x="300" y="224" font-size="13" text-anchor="middle" fill="var(--slate)">cliquez sur</text><text class="nt-wtxt2" x="300" y="242" font-size="13" text-anchor="middle" fill="var(--slate)">une couleur</text></svg>
<p class="nt-msg" aria-live="polite">Cliquez sur la couleur absorbée par une solution pour trouver sa couleur perçue.</p>
</div>

<div class="nt-lab" id="lab-couleur">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Du spectre d'absorption à la couleur de la solution</p>
<div class="nt-spec-wrap">
<canvas style="height:220px;" aria-label="Spectre d'absorption de la solution"></canvas>
<div class="nt-swatches">
<div><div class="nt-swatch nt-swatch-abs"></div><p class="nt-note">couleur la plus absorbée</p></div>
<div><div class="nt-swatch nt-swatch-sol"></div><p class="nt-note">couleur de la solution</p></div>
</div>
</div>
<div class="nt-ctrl">Colorant&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="colorant" value="e102"><span>tartrazine E102</span></label>
<label><input type="radio" name="colorant" value="e110"><span>jaune orangé E110</span></label>
<label><input type="radio" name="colorant" value="e129"><span>rouge allura E129</span></label>
<label><input type="radio" name="colorant" value="e127"><span>érythrosine E127</span></label>
<label><input type="radio" name="colorant" value="e132"><span>indigo carmin E132</span></label>
<label><input type="radio" name="colorant" value="e133" checked><span>bleu brillant E133</span></label>
<label><input type="radio" name="colorant" value="cuso4"><span>sulfate de cuivre</span></label>
<label><input type="radio" name="colorant" value="chloro"><span>chlorophylle</span></label>
</div>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">Position de la bande&nbsp;: <b class="out-l0"></b><input type="range" data-p="l0" min="380" max="780" step="1" value="630"></label>
<label class="nt-ctrl">Largeur de la bande&nbsp;: <b class="out-w"></b><input type="range" data-p="w" min="20" max="200" step="1" value="75"></label>
<label class="nt-ctrl">Absorbance maximale&nbsp;: <b class="out-a"></b><input type="range" data-p="a" min="0" max="1.2" step="0.01" value="1"></label>
</div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Les spectres sont simplifiés (bandes en forme de cloche). La couleur affichée est calculée à partir de la lumière transmise, pour une solution éclairée en lumière blanche.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Quel devrait être le spectre d'un colorant vert&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Il doit absorber le magenta, donc à la fois le rouge et le bleu. C'est le cas de la chlorophylle, dont le spectre présente deux grandes zones d'absorption, l'une dans le bleu-violet et l'autre dans le rouge&nbsp;: choisissez-la dans l'animation ci-dessus.</p>
</div>
</details>

### Spectroscopie infrarouge {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La spectroscopie IR consiste à établir le spectre de <span class="imp nt-hole">transmittance</span> d'un échantillon.</p>
<p>On trace la <span class="imp">transmittance</span> (en %) en fonction du <span class="imp">nombre d'onde</span> (en $\pu{cm^-1}$), une grandeur proportionnelle à la fréquence.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Plus la transmittance est faible et plus l'absorbance est <span class="imp nt-hole">grande</span>.</li>
<li>Le nombre d'onde est l'<span class="imp nt-hole">inverse de la longueur d'onde</span>&nbsp;: $\dfrac{1}{\lambda} = \dfrac{f}{c}$.</li>
</ul>
</div>

<p class="nt-lead">La spectroscopie infrarouge exploite le fait que les molécules possèdent des fréquences spécifiques pour lesquelles elles vibrent en correspondance avec des niveaux d'énergie discrets (modes vibratoires).</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Ces fréquences de résonance dépendent de <span class="imp nt-hole">la nature de la liaison</span> entre les atomes.</p>
<p>Et pour chaque résonance, on obtient un <span class="imp nt-hole">creux</span> dans le spectre de transmittance (correspondant à une forte absorbance du rayonnement IR).</p>
</div>

<div class="nt-lab" id="lab-co2">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Les 4 modes de vibration de la molécule de $\ce{CO2}$</p>
<canvas style="height:200px;" aria-label="Animation d'un mode de vibration de la molécule de dioxyde de carbone"></canvas>
<div class="nt-ctrl">Mode de vibration&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="mode" value="sym"><span>élongation symétrique</span></label>
<label><input type="radio" name="mode" value="asym" checked><span>élongation antisymétrique</span></label>
<label><input type="radio" name="mode" value="def1"><span>déformation dans le plan</span></label>
<label><input type="radio" name="mode" value="def2"><span>déformation hors du plan</span></label>
</div>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi l'élongation symétrique n'absorbe-t-elle pas&nbsp;?</span></summary>
<div class="nt-d-body">
Pourtant son nombre d'onde est bien dans l'infrarouge 🧐
<p>Avoir une fréquence propre dans l'infrarouge est nécessaire, mais pas suffisant. Il faut aussi que l'onde puisse «&nbsp;mettre en mouvement&nbsp;» la molécule selon ce mode de vibration.</p>
<p>Le champ électrique de l'onde infrarouge oscille et exerce des forces sur les charges de la molécule. Dans $\ce{CO2}$, les atomes d'oxygène portent une petite charge négative, l'atome de carbone une charge positive. La longueur d'onde (quelques micromètres) étant immense devant la taille de la molécule (un dixième de nanomètre), le champ est le même partout sur la molécule à un instant donné&nbsp;: il pousse les deux atomes d'oxygène <i>dans le même sens</i>, et le carbone dans le sens opposé.</p>
<p>Dans l'élongation antisymétrique et dans les déformations, les deux atomes d'oxygène se déplacent justement dans le même sens, le carbone dans l'autre&nbsp;: l'onde peut entretenir ces mouvements et leur céder de l'énergie, d'où l'absorption. Dans l'élongation symétrique, au contraire, les deux oxygènes partent dans des sens opposés&nbsp;: une force identique sur les deux ne peut pas provoquer ce mouvement. L'onde passe sans être absorbée, quelle que soit sa fréquence.</p>
<p>Les physiciens le formulent ainsi&nbsp;: une vibration n'absorbe l'infrarouge que si elle fait varier le moment dipolaire de la molécule (la séparation moyenne entre ses charges + et −). L'élongation symétrique de $\ce{CO2}$ s'observe d'ailleurs par une autre technique, la spectroscopie Raman.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Simuler et explorer des spectres IR</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://ir.cheminfo.org" target="_blank" rel="noopener">Une application</a> pour simuler le spectre de n'importe quelle molécule et visualiser ses vibrations.</li>
<li><a href="http://chimie.ostralo.net/spectreIR/" target="_blank" rel="noopener">Des exemples de spectres interactifs</a>.</li>
<li>Juste pour les curieux&nbsp;: <a href="https://archive.org/details/vibration_of_molecules" target="_blank" rel="noopener">un film ancien sur la vibration des molécules</a>.</li>
</ul>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-table"></i>Données&nbsp;: bandes d'absorption caractéristiques</p>
<div class="nt-scroll">
<table class="nt-t nt-t-ir">
<thead><tr><th>Liaison</th><th>Nombre d'onde (cm<sup>−1</sup>)</th><th>Position sur le spectre<div class="nt-irscale"><span>4 000</span><span>1 500</span><span>400</span></div></th><th>Allure de la bande</th></tr></thead><tbody>
<tr><td><span class="nt-ir-name">O–H</span><span class="nt-ir-fam">alcool (libre, état gazeux)</span></td><td class="nt-ir-range">3 580 – 3 670</td><td><div class="nt-irbar"><span class="nt-ir-fp" style="left:69.4%;right:0;"></span><span class="nt-ir-band" style="left:9.2%;width:2.5%;"></span></div></td><td><span class="nt-chip nt-chip-m">moyenne</span><span class="nt-chip nt-chip-l">fine</span></td></tr>
<tr><td><span class="nt-ir-name">O–H</span><span class="nt-ir-fam">alcool (lié)</span></td><td class="nt-ir-range">3 200 – 3 400</td><td><div class="nt-irbar"><span class="nt-ir-fp" style="left:69.4%;right:0;"></span><span class="nt-ir-band" style="left:16.7%;width:5.6%;"></span></div></td><td><span class="nt-chip nt-chip-f">forte</span><span class="nt-chip nt-chip-l">large</span></td></tr>
<tr><td><span class="nt-ir-name">O–H</span><span class="nt-ir-fam">acide carboxylique</span></td><td class="nt-ir-range">2 500 – 3 200</td><td><div class="nt-irbar"><span class="nt-ir-fp" style="left:69.4%;right:0;"></span><span class="nt-ir-band" style="left:22.2%;width:19.4%;"></span></div></td><td><span class="nt-chip nt-chip-f">forte</span><span class="nt-chip nt-chip-l">très large</span></td></tr>
<tr><td><span class="nt-ir-name">N–H</span><span class="nt-ir-fam">amine</span></td><td class="nt-ir-range">3 100 – 3 500</td><td><div class="nt-irbar"><span class="nt-ir-fp" style="left:69.4%;right:0;"></span><span class="nt-ir-band" style="left:13.9%;width:11.1%;"></span></div></td><td><span class="nt-chip nt-chip-m">moyenne</span></td></tr>
<tr><td><span class="nt-ir-name">C–H</span><span class="nt-ir-fam">toutes les molécules organiques</span></td><td class="nt-ir-range">2 800 – 3 100</td><td><div class="nt-irbar"><span class="nt-ir-fp" style="left:69.4%;right:0;"></span><span class="nt-ir-band" style="left:25.0%;width:8.3%;"></span></div></td><td><span class="nt-chip nt-chip-m">moyenne à forte</span></td></tr>
<tr><td><span class="nt-ir-name">C=O</span><span class="nt-ir-fam">aldéhyde, cétone, acide, ester</span></td><td class="nt-ir-range">1 650 – 1 750</td><td><div class="nt-irbar"><span class="nt-ir-fp" style="left:69.4%;right:0;"></span><span class="nt-ir-band" style="left:62.5%;width:2.8%;"></span></div></td><td><span class="nt-chip nt-chip-f">forte</span><span class="nt-chip nt-chip-l">fine</span></td></tr>
<tr><td><span class="nt-ir-name">C=C</span><span class="nt-ir-fam">alcène</span></td><td class="nt-ir-range">1 620 – 1 680</td><td><div class="nt-irbar"><span class="nt-ir-fp" style="left:69.4%;right:0;"></span><span class="nt-ir-band" style="left:64.4%;width:1.7%;"></span></div></td><td><span class="nt-chip nt-chip-m">moyenne</span></td></tr>
</tbody>
</table>
</div>
<p class="nt-note">En dessous de 1 500 cm<sup>−1</sup> (zone grisée), la «&nbsp;zone d'empreinte digitale&nbsp;» contient de nombreuses bandes propres à chaque molécule, difficiles à attribuer individuellement.</p>
</div>


<div class="nt-lab" id="lab-ir">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Reconnaître une famille de molécules à son spectre</p>
<canvas style="height:260px;" aria-label="Spectre infrarouge de la molécule choisie"></canvas>
<div class="nt-ctrl">Molécule&nbsp;:
<div class="nt-seg nt-mols" role="radiogroup"></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">O–H «&nbsp;lié&nbsp;» ou O–H «&nbsp;libre&nbsp;»&nbsp;?</span></summary>
<div class="nt-d-body">
<p><b>Un O–H «&nbsp;lié&nbsp;».</b> Dans un alcool liquide, l'atome d'hydrogène du groupe O–H, porteur d'une charge partielle positive, est attiré par un atome d'oxygène d'une molécule voisine, porteur d'une charge partielle négative&nbsp;: c'est une <b>liaison hydrogène</b> ou <b>pont hydrogène</b>. Chaque groupe O–H est ainsi «&nbsp;lié&nbsp;» à ses voisins.</p>
<svg class="nt-svg nt-svg-m" viewBox="0 0 540 190" role="img" aria-label="Liaison hydrogène entre deux molécules d'éthanol : l'atome d'hydrogène du groupe O–H de l'une est attiré par un atome d'oxygène de l'autre"><text x="50" y="108" font-size="22" text-anchor="start" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C<tspan font-size="14" dy="5">2</tspan><tspan dy="-5">H</tspan><tspan font-size="14" dy="5">5</tspan></text><line x1="106" y1="101" x2="138" y2="101" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="156" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><line x1="174" y1="101" x2="204" y2="101" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="220" y="108" font-size="22" text-anchor="middle" fill="#C026D3" font-family="Georgia, 'Times New Roman', serif">H</text><text x="156" y="78" font-size="15" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">δ−</text><text x="220" y="78" font-size="15" text-anchor="middle" fill="var(--blue)" font-family="Georgia, 'Times New Roman', serif">δ+</text><line x1="238" y1="101" x2="314" y2="101" stroke="#C026D3" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/><text x="276" y="134" font-size="13" text-anchor="middle" fill="#C026D3" font-weight="700">liaison hydrogène</text><text x="332" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><text x="318" y="78" font-size="15" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">δ−</text><line x1="344" y1="90" x2="372" y2="60" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="378" y="58" font-size="22" text-anchor="start" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C<tspan font-size="14" dy="5">2</tspan><tspan dy="-5">H</tspan><tspan font-size="14" dy="5">5</tspan></text><line x1="344" y1="112" x2="372" y2="142" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="384" y="162" font-size="22" text-anchor="middle" fill="#C026D3" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="400" y1="155" x2="456" y2="155" stroke="#C026D3" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/><text x="476" y="160" font-size="22" text-anchor="middle" fill="var(--slate)" font-family="Georgia, 'Times New Roman', serif">…</text></svg>
<p><b>Ce que cela change sur le spectre.</b> L'atome d'hydrogène, tiré à la fois par son propre oxygène et par celui du voisin, est un peu moins fermement retenu&nbsp;: la liaison O–H est affaiblie et vibre à une fréquence plus basse, d'où une bande vers 3&nbsp;200 – 3&nbsp;400&nbsp;cm<sup>−1</sup>. Et comme les liaisons hydrogène n'ont pas toutes la même longueur ni la même orientation dans le liquide, chaque groupe O–H vibre à une fréquence légèrement différente&nbsp;: toutes ces bandes se superposent en une bande <b>large</b>.</p>
<p><b>Un O–H «&nbsp;libre&nbsp;».</b> À l'état gazeux (ou en solution très diluée dans un solvant qui ne forme pas de liaisons hydrogène), les molécules sont trop éloignées les unes des autres pour interagir. Le groupe O–H n'est plus lié&nbsp;: sa liaison n'est pas affaiblie, et tous les groupes O–H vibrent à la même fréquence. On obtient une bande <b>fine</b>, à plus grand nombre d'onde, vers 3&nbsp;600 – 3&nbsp;700&nbsp;cm<sup>−1</sup>. Comparez «&nbsp;éthanol&nbsp;» et «&nbsp;éthanol gazeux&nbsp;» dans l'animation ci-dessus.</p>
<p>Dans un acide carboxylique, les molécules s'associent entre elles par deux liaisons hydrogène très fortes&nbsp;: la liaison O–H est encore plus affaiblie, d'où une bande encore plus basse et très large (2&nbsp;500 – 3&nbsp;200&nbsp;cm<sup>−1</sup>).</p>
</div>
</details>
<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Petite bizarrerie</p>
<p>L'axe des abscisses (le nombre d'onde en $\pu{cm^-1}$) est orienté vers la gauche&nbsp;!</p>
</div>

## Dosage par étalonnage {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Type de dosage <span class="imp nt-hole">non destructif</span> consistant à&nbsp;:</p>
<ol class="nt-steps">
<li><p>mesurer une <span class="imp">propriété physique</span> sur une <span class="imp nt-hole">gamme étalon</span> de solutions de concentrations connues (obtenues par dilution d'une solution mère),</p></li>
<li><p>tracer la <span class="imp nt-hole">courbe d'étalonnage</span>,</p></li>
<li><p>mesurer la propriété physique sur la solution mystère et utiliser la courbe d'étalonnage (ou la proportionnalité si possible) pour déterminer sa concentration.</p></li>
</ol>
</div>

### Spectrophotométrique {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Dans le cas d'un dosage par étalonnage spectrophotométrique, la propriété physique mesurée est l'<span class="imp nt-hole">absorbance</span> de la solution à une longueur d'onde donnée.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Conditions d'application</p>
<ul class="nt-facts">
<li>la solution doit absorber la lumière UV-visible (la solution est généralement colorée),</li>
<li>à la longueur d'onde choisie, l'espèce dosée doit être <span class="imp nt-hole">la seule</span> à absorber le rayonnement.</li>
</ul>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour une sensibilité maximale et se prémunir au mieux de l'absorbance d'autres espèces, on choisit pour longueur d'onde de travail la longueur d'onde <span class="imp">$\lambda_{max}$</span> correspondant au <span class="imp nt-hole">maximum d'absorbance</span> du spectre de l'espèce étudiée.</p>
</div>

<p class="nt-lead">Les mesures se font au spectrophotomètre (voir son principe au début de la page).</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Loi de Beer-Lambert</p>
<p>Pour une longueur d'onde $\lambda$ donnée et une largeur de cuve fixée, l'<span class="imp">absorbance $A_\lambda$</span> d'une espèce chimique en solution diluée <span class="imp nt-hole">est proportionnelle à la concentration $C$ en quantité de matière</span> de cette espèce chimique.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Version simple</p>
<p class="nt-f-math">$$A_\lambda=k\times C$$</p>
<div class="nt-f-units"><span>$A_\lambda$ <b>sans unité</b></span><span>$C$ en <b>$\pu{mol*L-1}$</b></span><span>$k$ en <span class="nt-hole">$\pu{L*mol-1}$</span></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Version complète</p>
<p class="nt-f-math">$$A_\lambda=\varepsilon_\lambda \times \ell \times C$$</p>
<div class="nt-f-units"><span>$\ell$ (en <b>$\pu{cm}$</b>)&nbsp;: épaisseur de la cuve</span><span>$\varepsilon_\lambda$ (en <span class="nt-hole">$\pu{L*mol-1*cm-1}$</span>)&nbsp;: coefficient d'absorption molaire</span></div>
</div>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Le domaine de validité de la loi de Beer-Lambert suppose que l'absorbance et donc la <span class="imp nt-hole">concentration reste modérée</span>.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-list-ol"></i>Protocole du dosage</p>
<ol class="nt-steps">
<li><p>Tracer ou obtenir dans la littérature le spectre de l'espèce étudiée puis régler le spectrophotomètre sur $\lambda_{max}$.</p></li>
<li><p>Réaliser une <b>gamme étalon</b> par dilution d'une solution mère de concentration connue contenant l'espèce absorbante étudiée.</p></li>
<li><p>Faire <b>le zéro</b> du spectrophotomètre en plaçant une cuve ne contenant que le solvant de la solution mère (ou du moins ne contenant pas l'espèce absorbante étudiée).</p></li>
<li><p>Mesurer l'absorbance des solutions étalons au spectrophotomètre et tracer la <b>courbe d'étalonnage</b> $A = f(C)$.</p></li>
<li><p>Mesurer l'absorbance $A_x$ de la solution mystère. Si $A_x$ sort de la gamme, diluer la solution.</p></li>
<li><p>Déterminer $\mathbf{C_x}$ grâce à la courbe (détermination graphique) ou grâce à la loi de Beer-Lambert si elle est vérifiée avec $C_x = \dfrac{A_x}{k}$ (détermination par le calcul).</p></li>
</ol>
</div>

<div class="nt-lab" id="lab-gamme">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive (1/2)</p>
<p class="nt-lab-title">Établir la courbe d'étalonnage</p>
<p class="nt-note">Solution mère&nbsp;: colorant bleu de concentration $C_0 = \pu{0,120 mol*L-1}$. Chaque solution fille est préparée dans une fiole jaugée de $\pu{50,0 mL}$&nbsp;: $C = C_0\times\dfrac{V_{\text{mère}}}{V_{\text{fiole}}}$.</p>
<div class="nt-gamme">
<div class="nt-tubes" aria-hidden="true"></div>
<canvas style="height:250px;" aria-label="Absorbance des solutions étalons en fonction de leur concentration"></canvas>
</div>
<div class="nt-scroll"><table class="nt-t nt-gamme-tab"><thead><tr><th>Solution</th><th>$V_{\text{mère}}$ prélevé (mL)</th><th>$C$ (mol·L<sup>−1</sup>)</th><th>$A$ mesurée</th></tr></thead><tbody></tbody></table></div>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-vial"></i>&nbsp; Préparer et mesurer la solution suivante</button>
<button type="button" class="nt-btn" data-act="all">Tout préparer</button>
<button type="button" class="nt-btn" data-act="reset">Recommencer</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-lab" id="lab-etal">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive (2/2)</p>
<p class="nt-lab-title">Exploiter la courbe&nbsp;: doser une solution mystère</p>
<div class="nt-gamme">
<div class="nt-tubes" aria-hidden="true"><div class="nt-tubebox"><div class="nt-tube"><div class="nt-liq nt-liq-x" style="height:80%;"></div></div><span class="nt-tube-lab">mystère</span></div></div>
<canvas style="height:280px;" aria-label="Courbe d'étalonnage et lecture de la concentration de la solution mystère"></canvas>
</div>
<div class="nt-read" aria-live="polite"><span>coefficient directeur $k$ = <b class="out-k"></b></span><span>$A_x$ = <b class="out-ax"></b></span><span>$C_x$ = <b class="out-cx"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="new"><i class="fa-solid fa-flask"></i>&nbsp; Nouvelle solution mystère</button>
<label class="nt-check"><input type="checkbox" data-p="large"> Étendre la gamme aux fortes concentrations</label>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>


### Conductimétrique {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une autre propriété physique utilisable est la <span class="imp nt-hole">conductivité $\sigma$</span> de la solution.</p>
<p>La présence d'ions dans une solution lui confère des propriétés de conduction électrique que mesure la conductivité (mieux la solution conduit et plus sa conductivité est grande).</p>
</div>

<p class="nt-lead">La conductivité $\sigma_i$ de chaque ion i en solution contribue à la conductivité totale $\sigma$&nbsp;:</p>

<p class="nt-center">$\sigma=\displaystyle\sum_i \sigma_i$</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Loi de Kohlrausch</p>
<p>Pour une concentration suffisamment faible, la conductivité d'un ion est <span class="imp nt-hole">proportionnelle à sa concentration</span>.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$\sigma_i = \lambda_i\times C_i$$</p>
<div class="nt-f-units"><span>$\sigma_i$&nbsp;: conductivité de l'ion i en <b>$\pu{S*m-1}$</b> (siemens par mètre)</span><span>$C_i$&nbsp;: concentration de l'ion i en ⚠️ <span class="nt-hole">$\pu{mol*m-3}$</span> ⚠️</span><span>$\lambda_i$&nbsp;: conductivité molaire ionique de l'ion i en <span class="nt-hole">$\pu{S*m^2*mol-1}$</span></span></div>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Ici, $\lambda_i$ ne désigne pas une longueur d'onde, mais la conductivité molaire ionique.</p>
<p>Les concentrations doivent être exprimées en $\pu{mol*m-3}$&nbsp;: $\pu{1 mol*L-1} = \pu{1000 mol*m-3}$, et donc $\pu{1 mmol*L-1} = \pu{1 mol*m-3}$.</p>
</div>

<p class="nt-lead">La formule de la conductivité de la solution devient alors&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$\sigma = \sum_i\lambda_i\times C_i$$</p>
</div>

<p class="nt-lead">Pour obtenir la conductivité d'une solution, on utilise un <span class="imp">conductimètre</span> qui mesure sa <span class="imp">conductance G</span>, à l'aide d'une cellule plongée dans la solution.</p>

<svg class="nt-svg nt-svg-m" viewBox="0 0 560 280" role="img" aria-label="Cellule de conductimétrie : deux plaques de surface S distantes de ℓ, reliées à un ohmmètre ; les ions de la solution se déplacent entre les plaques"><rect x="60" y="90" width="440" height="170" rx="14" fill="#38BDF8" fill-opacity=".18" stroke="var(--slate)" stroke-width="2"/><text x="80" y="250" font-size="12" fill="var(--slate)">solution</text><polygon points="200,110 230,98 230,218 200,230" fill="#CBD5E1" stroke="var(--slate)" stroke-width="2"/><polygon points="330,110 360,98 360,218 330,230" fill="#CBD5E1" stroke="var(--slate)" stroke-width="2"/><text x="374" y="132" font-size="18" fill="var(--amber)" font-family="Georgia, serif" font-style="italic" font-weight="700">S</text><line x1="370" y1="128" x2="352" y2="138" stroke="var(--amber)" stroke-width="1.2"/><line x1="223.0" y1="236.0" x2="337.0" y2="236.0" stroke="var(--amber)" stroke-width="1.8"/><polygon points="345.0,236.0 336.0,240.5 336.0,231.5" fill="var(--amber)"/><polygon points="215.0,236.0 224.0,231.5 224.0,240.5" fill="var(--amber)"/><text x="280" y="229" font-size="18" fill="var(--amber)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700" paint-order="stroke" stroke="#E6F4FB" stroke-width="5">ℓ</text><line x1="215" y1="104" x2="215" y2="40" stroke="var(--ink)" stroke-width="2"/><line x1="345" y1="104" x2="345" y2="40" stroke="var(--ink)" stroke-width="2"/><line x1="215" y1="40" x2="258" y2="40" stroke="var(--ink)" stroke-width="2"/><line x1="302" y1="40" x2="345" y2="40" stroke="var(--ink)" stroke-width="2"/><circle cx="280" cy="40" r="22" fill="#fff" stroke="var(--ink)" stroke-width="2"/><text x="280" y="47" font-size="20" text-anchor="middle" fill="var(--ink)">Ω</text><circle cx="262" cy="132" r="9" fill="var(--rose)" fill-opacity=".85"/><text x="262" y="136.5" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">+</text><circle cx="300" cy="165" r="9" fill="var(--blue)" fill-opacity=".85"/><text x="300" y="169.5" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">−</text><circle cx="272" cy="192" r="9" fill="var(--rose)" fill-opacity=".85"/><text x="272" y="196.5" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">+</text><circle cx="308" cy="122" r="9" fill="var(--blue)" fill-opacity=".85"/><text x="308" y="126.5" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">−</text><circle cx="250" cy="160" r="9" fill="var(--blue)" fill-opacity=".85"/><text x="250" y="164.5" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">−</text><circle cx="318" cy="196" r="9" fill="var(--rose)" fill-opacity=".85"/><text x="318" y="200.5" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">+</text></svg>

<p class="nt-cap">La cellule est formée de deux plaques de surface $S$, distantes de $\ell$. L'appareil mesure la résistance $R$ de la portion de solution comprise entre les plaques, dans laquelle les ions se déplacent.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La conductance est l'<span class="imp nt-hole">inverse de la résistance électrique</span>&nbsp;: $G=\dfrac{1}{R}$.</p>
<p>Elle se mesure en siemens&nbsp;: <span class="imp nt-hole">$\mathrm{S}=\Omega^{-1}$</span>.</p>
</div>

<p class="nt-lead">On passe de la conductance à la conductivité à partir de la géométrie des électrodes&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$\sigma=G\times k =G\times\frac{\ell}{S}$$</p>
<div class="nt-f-units"><span>$\sigma$&nbsp;: conductivité (en <b>$\pu{S*m-1}$</b>)</span><span>$G$&nbsp;: conductance (en <b>$\pu{S}$</b>)</span><span>$k$&nbsp;: «&nbsp;constante de cellule&nbsp;» (en <b>$\pu{m-1}$</b>)</span><span>$S$&nbsp;: surface d'une plaque (en <b>$\pu{m2}$</b>)</span><span>$\ell$&nbsp;: distance entre les plaques (en <b>$\pu{m}$</b>)</span></div>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Un conductimètre peut mesurer directement la conductivité mais il faut pour cela l'étalonner (la constante de cellule dépend de la température et évolue en fonction de la détérioration des plaques).</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Condition pour réaliser un dosage par étalonnage</p>
<p>Il faut qu'<span class="imp nt-hole">un seul soluté ionique</span> soit dissous dans la solution à doser (apportant un seul cation et un seul anion).</p>
<p>C'est ce qui permet d'avoir une conductivité <b>proportionnelle à la concentration apportée</b>&nbsp;: les concentrations de tous les ions présents sont alors proportionnelles à cette seule concentration, comme le montre l'exemple ci-dessous.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Exemple d'une solution de chlorure de fer III $\ce{(Fe^3+ + 3Cl^-)}$. La concentration apportée en $\ce{FeCl3 (s)}$ vaut $C$.</p>
<p>Les concentrations des ions en solution sont alors&nbsp;: $\ce{[Fe^3+]}=$ <span class="imp nt-hole">$C$</span> et $\ce{[Cl^-]}=$ <span class="imp nt-hole">$3\times C$</span>.</p>
<p>Et d'après la loi de Kohlrausch&nbsp;:</p>
<p class="nt-center">$\begin{aligned}\sigma&=\lambda_{\mathrm{Fe^{3+}}}\left[\mathrm{Fe^{3+}}\right]+\lambda_{\mathrm{Cl^-}}\left[\mathrm{Cl^-}\right]\\ &=\left(\lambda_{\mathrm{Fe^{3+}}}+3\lambda_{\mathrm{Cl^-}}\right)\times C\end{aligned}$</p>
<p>Si la loi s'applique, on doit obtenir une <b>conductivité proportionnelle à la concentration</b> apportée.</p>
</div>

<div class="nt-lab" id="lab-kohl">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Calculer une conductivité avec la loi de Kohlrausch</p>
<div class="nt-ctrl">Soluté dissous&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="solute" value="nacl"><span>NaCl</span></label>
<label><input type="radio" name="solute" value="kcl"><span>KCl</span></label>
<label><input type="radio" name="solute" value="cacl2"><span>CaCl<sub>2</sub></span></label>
<label><input type="radio" name="solute" value="fecl3" checked><span>FeCl<sub>3</sub></span></label>
<label><input type="radio" name="solute" value="hcl"><span>HCl (acide chlorhydrique)</span></label>
</div>
</div>
<label class="nt-ctrl">Concentration apportée $C$&nbsp;: <b class="out-c"></b><input type="range" min="0" max="10" step="0.1" value="2"></label>
<div class="nt-scroll"><table class="nt-t nt-kohl-tab"></table></div>
<div class="nt-read" aria-live="polite"><span>$\sigma$ = <b class="out-s"></b></span><span>soit <b class="out-s2"></b> (unité affichée par beaucoup de conductimètres)</span></div>
<p class="nt-note">Conductivités molaires ioniques à 25&nbsp;°C. Faites varier $C$&nbsp;: toutes les contributions, et donc $\sigma$, sont proportionnelles à $C$.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-list-ol"></i>Le protocole du dosage est toujours le même</p>
<ol class="nt-steps">
<li><p>on réalise une <b>gamme étalon</b> en diluant une solution contenant le composé ionique présent dans la solution à doser&nbsp;;</p></li>
<li><p>on mesure les conductivités des solutions étalons et on trace la <b>courbe d'étalonnage</b>&nbsp;;</p></li>
<li><p>on mesure la conductivité de la solution à doser et on détermine sa concentration grâce à la courbe.</p></li>
</ol>
</div>

## Loi des gaz parfaits {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Loi de Mariotte</p>
<p>Le produit de la pression d'un gaz par son volume <span class="imp nt-hole">à température fixée</span> est une constante.</p>
<p class="nt-center">$PV = C(T)$</p>
<p>On va maintenant généraliser cette loi en explicitant cette constante dépendant de la température.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un gaz est dit <span class="imp">parfait</span> si la <span class="imp nt-hole">taille des entités est négligeable</span> devant la distance qui les sépare et si les <span class="imp nt-hole">interactions</span> entre elles sont négligeables.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi des gaz parfaits</p>
<p class="nt-f-math">$$PV = nRT$$</p>
<div class="nt-f-units"><span>$P$&nbsp;: pression (en <span class="nt-hole">$\pu{Pa}$</span>)</span><span>$V$&nbsp;: volume (en <span class="nt-hole">$\pu{m3}$</span>)</span><span>$n$&nbsp;: quantité de matière (en <span class="nt-hole">$\pu{mol}$</span>)</span><span>$T$&nbsp;: température (en <span class="nt-hole">$\pu{K}$</span>)</span><span>$R= 8{,}314$ <span class="nt-hole">$\pu{Pa*m3*K-1*mol-1}$</span>&nbsp;: constante des gaz parfaits</span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>La pression est aussi une énergie par unité de volume&nbsp;: $\Rightarrow \pu{Pa} =$ <span class="imp nt-hole">$\pu{J*m-3}$</span>.</p>
<p>Et donc $R$ s'exprime en <span class="imp nt-hole">$\pu{J*K-1*mol-1}$</span>.</p>
</div>

<div class="nt-lab" id="lab-gaz">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Un gaz parfait dans une enceinte</p>
<canvas style="height:220px;" aria-label="Particules de gaz qui s'agitent dans une enceinte fermée par un piston"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Quantité de matière $n$&nbsp;: <b class="out-n"></b><input type="range" data-p="n" min="0.5" max="3" step="0.1" value="1"></label>
<label class="nt-ctrl">Température $T$&nbsp;: <b class="out-T"></b><input type="range" data-p="T" min="150" max="600" step="1" value="293"></label>
<label class="nt-ctrl">Volume $V$&nbsp;: <b class="out-V"></b><input type="range" data-p="V" min="5" max="40" step="0.5" value="24"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$P$ = <b class="out-P"></b></span><span>$PV$ = <b class="out-pv"></b></span><span>$nRT$ = <b class="out-nrt"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg">Plus les particules sont nombreuses, rapides (température élevée) ou à l'étroit (petit volume), plus elles frappent souvent les parois&nbsp;: la pression augmente. À $n$ et $T$ fixés, réduisez le volume de moitié&nbsp;: la pression double (loi de Mariotte).</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Une simulation plus complète</span></summary>
<div class="nt-d-body">
<p>La simulation <a href="https://phet.colorado.edu/sims/html/gases-intro/latest/gases-intro_all.html?locale=fr" target="_blank" rel="noopener">«&nbsp;Gaz : introduction&nbsp;» de PhET</a> permet de jouer sur les mêmes grandeurs, de chauffer l'enceinte ou de déplacer sa paroi.</p>
</div>
</details>

<p class="nt-lead">La loi des gaz parfaits permet donc de déterminer la quantité de matière d'un gaz si on connaît sa pression, son volume et sa température&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$n=\frac{PV}{RT}$$</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Quelle quantité de matière d'air contient un ballon de $\pu{5,0 L}$ à $20\,^\circ\mathrm{C}$ sous une pression de $\pu{1,0E5 Pa}$&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p>On convertit dans les unités de la loi&nbsp;: $V = \pu{5,0E-3 m3}$ et $T = 20 + 273{,}15 = \pu{293 K}$.</p>
<p class="nt-center">$n = \dfrac{PV}{RT} = \dfrac{1{,}0\times10^{5}\times 5{,}0\times10^{-3}}{8{,}314\times 293} = \pu{0,21 mol}$</p>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>À température et pression fixées, une même quantité de gaz parfait occupe <span class="imp nt-hole">le même volume</span> <span class="imp nt-hole">quel que soit le gaz</span>.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp">volume molaire $V_m$</span> d'un gaz parfait est le volume occupé par une mole de ce gaz&nbsp;:</p>
<p class="nt-center">$V_m=\dfrac{V}{n}=$ <span class="imp nt-hole">$\dfrac{RT}{P}$</span></p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Valeurs à connaître</p>
<ul class="nt-facts">
<li>À 0&nbsp;°C (<span class="nt-hole">$\pu{273,15 K}$</span>) et pression atmosphérique (<span class="nt-hole">$\pu{1 atm}=\pu{1,013 bar}=\pu{1,013E5 Pa}$</span>), $V_m=$ <span class="imp nt-hole">$\pu{22,4E-3 m^3*mol-1}=\pu{22,4 L*mol-1}$</span>&nbsp;;</li>
<li>Et à 20&nbsp;°C et sous $\pu{1 atm}$, $V_m=$ <span class="imp nt-hole">$\pu{24 L*mol-1}$</span>.</li>
</ul>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function canvasCtx(cv) {
    var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function watchVisible(el, cb) {
    if (!('IntersectionObserver' in window)) { cb(true); return; }
    new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }).observe(el);
  }
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function lambdaRGB(nm) {
    var r = 0, g = 0, b = 0;
    if (nm < 440) { r = -(nm - 440) / 60; b = 1; }
    else if (nm < 490) { g = (nm - 440) / 50; b = 1; }
    else if (nm < 510) { g = 1; b = -(nm - 510) / 20; }
    else if (nm < 580) { r = (nm - 510) / 70; g = 1; }
    else if (nm < 645) { r = 1; g = -(nm - 645) / 65; }
    else { r = 1; }
    var f = nm < 420 ? 0.3 + 0.7 * (nm - 380) / 40 : (nm > 700 ? 0.3 + 0.7 * (780 - nm) / 80 : 1);
    f = Math.max(0, f);
    return 'rgb(' + Math.round(255 * Math.pow(r * f, 0.8)) + ',' + Math.round(255 * Math.pow(g * f, 0.8)) + ',' + Math.round(255 * Math.pow(b * f, 0.8)) + ')';
  }
  /* ================= 1. Spectre d'absorption et couleur perçue ================= */
  (function () {
    var root = document.getElementById('lab-couleur');
    if (!root) { return; }
    var cv = $(root, 'canvas'), sw = $(root, '.nt-swatch-sol'), swA = $(root, '.nt-swatch-abs');
    var rL = $(root, '[data-p="l0"]'), rW = $(root, '[data-p="w"]'), rA = $(root, '[data-p="a"]');
    var oL = $(root, '.out-l0'), oW = $(root, '.out-w'), oA = $(root, '.out-a'), msg = $(root, '.nt-msg'), S;
    /* bandes d'absorption [λ centrale (nm), largeur à mi-hauteur (nm), absorbance maximale] */
    var PRESETS = {
      e102: { name: 'tartrazine (E102)', b: [[427, 95, 1.0]] },
      e110: { name: 'jaune orangé S (E110)', b: [[482, 100, 1.0]] },
      e129: { name: 'rouge allura AC (E129)', b: [[504, 95, 1.0]] },
      e127: { name: 'érythrosine (E127)', b: [[527, 55, 1.0]] },
      e132: { name: 'indigo carmin (E132)', b: [[610, 95, 1.0]] },
      e133: { name: 'bleu brillant FCF (E133)', b: [[630, 75, 1.0], [409, 60, 0.25]] },
      cuso4: { name: 'sulfate de cuivre (II)', b: [[800, 220, 1.0]] },
      chloro: { name: 'chlorophylle', b: [[430, 70, 1.2], [470, 60, 1.0], [640, 90, 1.2], [590, 60, 0.3]] }
    };
    var bands = PRESETS.e133.b;
    /* fonctions colorimétriques CIE 1931, approximation analytique de Wyman, Sloan et Shirley (2013) */
    function g(x, m, s1, s2) { var t = (x - m) / (x < m ? s1 : s2); return Math.exp(-0.5 * t * t); }
    function cmf(l) {
      return [1.056 * g(l, 599.8, 37.9, 31.0) + 0.362 * g(l, 442.0, 16.0, 26.7) - 0.065 * g(l, 501.1, 20.4, 26.2),
        0.821 * g(l, 568.8, 46.9, 40.5) + 0.286 * g(l, 530.9, 16.3, 31.1),
        1.217 * g(l, 437.0, 11.8, 36.0) + 0.681 * g(l, 459.0, 26.0, 13.8)];
    }
    function toRGB(X, Y, Z) { return [3.2406 * X - 1.5372 * Y - 0.4986 * Z, -0.9689 * X + 1.8758 * Y + 0.0415 * Z, 0.0557 * X - 0.2040 * Y + 1.0570 * Z]; }
    function gam(u) { u = Math.max(0, Math.min(1, u)); return Math.round(255 * (u <= 0.0031308 ? 12.92 * u : 1.055 * Math.pow(u, 1 / 2.4) - 0.055)); }
    function A(l) { var s = 0; bands.forEach(function (b) { var sg = b[1] / 2.355; s += b[2] * Math.exp(-0.5 * Math.pow((l - b[0]) / sg, 2)); }); return s; }
    function perceived() {
      var X = 0, Y = 0, Z = 0, Xw = 0, Yw = 0, Zw = 0;
      for (var l = 380; l <= 780; l += 2) {
        var c = cmf(l), T = Math.pow(10, -A(l));
        X += T * c[0]; Y += T * c[1]; Z += T * c[2]; Xw += c[0]; Yw += c[1]; Zw += c[2];
      }
      var rgb = toRGB(X, Y, Z), w = toRGB(Xw, Yw, Zw);
      return 'rgb(' + gam(rgb[0] / w[0]) + ',' + gam(rgb[1] / w[1]) + ',' + gam(rgb[2] / w[2]) + ')';
    }
    function draw() {
      var mx = 0; for (var q = 380; q <= 780; q += 4) { mx = Math.max(mx, A(q)); }
      var c = S.ctx, w = S.w, h = S.h, L = 40, Rr = w - 10, T = 10, B = h - 26, AM = Math.max(1.2, Math.ceil(mx * 1.1 * 2) / 2);
      function X(l) { return L + (l - 380) / 400 * (Rr - L); }
      function Y(a) { return B - a / AM * (B - T); }
      c.clearRect(0, 0, w, h);
      for (var px = L; px < Rr; px++) { c.fillStyle = lambdaRGB(380 + (px - L) / (Rr - L) * 400); c.globalAlpha = 0.18; c.fillRect(px, T, 1, B - T); }
      c.globalAlpha = 1;
      c.strokeStyle = col('--ink'); c.lineWidth = 1; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(Rr, B); c.stroke();
      c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
      [400, 450, 500, 550, 600, 650, 700, 750].forEach(function (l) { c.fillText(l, X(l), B + 13); });
      c.fillText('longueur d\u2019onde \u03bb (nm)', (L + Rr) / 2, h - 2);
      c.textAlign = 'right'; for (var ta = 0; ta <= AM + 1e-9; ta += 0.5) { c.fillText(fr(ta, 1), L - 4, Y(ta) + 4); }
      c.save(); c.translate(11, (T + B) / 2); c.rotate(-Math.PI / 2); c.textAlign = 'center'; c.fillText('absorbance A', 0, 0); c.restore();
      c.strokeStyle = col('--ink'); c.lineWidth = 2.6; c.beginPath();
      for (var l = 380; l <= 780; l += 2) { var y = Y(Math.min(AM, A(l))); if (l === 380) { c.moveTo(X(l), y); } else { c.lineTo(X(l), y); } }
      c.stroke();
      var main = bands.reduce(function (p, q) { return q[2] > p[2] ? q : p; });
      sw.style.background = perceived();
      swA.style.background = main[0] > 780 ? lambdaRGB(700) : lambdaRGB(Math.max(390, Math.min(770, main[0])));
    }
    function fromSliders() {
      bands = [[parseFloat(rL.value), parseFloat(rW.value), parseFloat(rA.value)]];
      $$(root, 'input[name="colorant"]').forEach(function (r) { r.checked = false; });
      msg.textContent = 'Bande d\u2019absorption personnalisée.';
      labels(); draw();
    }
    function labels() { oL.textContent = rL.value + ' nm'; oW.textContent = rW.value + ' nm'; oA.textContent = fr(parseFloat(rA.value), 2); }
    [rL, rW, rA].forEach(function (r) { r.addEventListener('input', fromSliders); });
    $$(root, 'input[name="colorant"]').forEach(function (r) {
      r.addEventListener('change', function () {
        var p = PRESETS[r.value]; bands = p.b;
        rL.value = Math.min(780, p.b[0][0]); rW.value = Math.min(200, p.b[0][1]); rA.value = p.b[0][2]; labels();
        msg.textContent = p.name + (r.value === 'chloro' ? ' : deux bandes, dans le bleu et dans le rouge.' : (r.value === 'cuso4' ? ' : absorbe surtout le rouge et le proche infrarouge.' : '.'));
        draw();
      });
    });
    function setup() { S = canvasCtx(cv); labels(); draw(); }
    msg.textContent = PRESETS.e133.name + '.';
    setup(); onResize(setup);
  })();
  /* ================= 2. Cercle chromatique ================= */
  (function () {
    var root = document.getElementById('lab-roue');
    if (!root) { return; }
    var svg = $(root, 'svg'), segs = $$(svg, '.nt-wseg'), t1 = $(svg, '.nt-wtxt1'), t2 = $(svg, '.nt-wtxt2'), msg = $(root, '.nt-msg');
    var NAMES = ['jaune', 'orange', 'rouge-orange', 'rouge', 'magenta', 'violet', 'bleu indigo', 'bleu', 'cyan', 'bleu-vert', 'vert', 'jaune-vert'];
    function pick(i) {
      var j = (i + 6) % 12;
      segs.forEach(function (s, k) { s.style.opacity = (k === i || k === j) ? 1 : 0.28; });
      t1.textContent = 'absorbée : ' + NAMES[i]; t2.textContent = 'perçue : ' + NAMES[j];
      msg.textContent = 'Une solution qui absorbe le ' + NAMES[i] + ' apparaît ' + NAMES[j] + ' : les deux couleurs sont diamétralement opposées sur le cercle.';
    }
    segs.forEach(function (s, i) {
      s.style.cursor = 'pointer'; s.style.transition = 'opacity .25s';
      s.addEventListener('click', function () { pick(i); });
      s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i); } });
    });
  })();
  /* ================= 3. Les vibrations de la molécule de CO2 ================= */
  (function () {
    var root = document.getElementById('lab-co2');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), btn = $(root, '[data-act="play"]'), S, mode = 'asym', playing = !RM, visible = true, t = 0, last = null;
    var MODES = {
      sym: { t: 'Élongation symétrique', k: '\u2248 1 340 cm\u207b\u00b9', ir: false, why: 'Les deux atomes d\u2019oxygène s\u2019écartent et se rapprochent ensemble : la molécule reste symétrique, la répartition des charges ne change pas. Cette vibration n\u2019absorbe pas l\u2019infrarouge, bien que sa fréquence soit dans l\u2019infrarouge : voir l\u2019encadré ci-dessous.' },
      asym: { t: 'Élongation antisymétrique', k: '\u2248 2 350 cm\u207b\u00b9', ir: true, why: 'Une liaison s\u2019allonge pendant que l\u2019autre se raccourcit : la symétrie des charges est rompue à chaque instant. Cette vibration absorbe fortement l\u2019infrarouge.' },
      def1: { t: 'Déformation dans le plan', k: '\u2248 667 cm\u207b\u00b9', ir: true, why: 'La molécule se plie : elle n\u2019est plus rectiligne, la répartition des charges oscille. Cette vibration absorbe l\u2019infrarouge.' },
      def2: { t: 'Déformation hors du plan', k: '\u2248 667 cm\u207b\u00b9', ir: true, why: 'Même pliage, mais perpendiculairement au plan de l\u2019écran (les atomes d\u2019oxygène s\u2019approchent de nous quand le carbone s\u2019éloigne). Même nombre d\u2019onde que la précédente.' }
    };
    function atom(c, x, y, r, fill, label, scale) {
      var rr = r * scale;
      var gr = c.createRadialGradient(x - rr * 0.35, y - rr * 0.35, rr * 0.1, x, y, rr);
      gr.addColorStop(0, '#fff'); gr.addColorStop(0.35, fill); gr.addColorStop(1, fill);
      c.fillStyle = gr; c.beginPath(); c.arc(x, y, rr, 0, 2 * Math.PI); c.fill();
      c.fillStyle = '#fff'; c.font = '700 ' + Math.round(14 * scale) + 'px system-ui, sans-serif'; c.textAlign = 'center'; c.fillText(label, x, y + 5 * scale);
    }
    function bond(c, a, b) {
      var dx = b[0] - a[0], dy = b[1] - a[1], n = Math.hypot(dx, dy), ox = -dy / n * 4, oy = dx / n * 4;
      c.strokeStyle = '#64748B'; c.lineWidth = 3;
      [1, -1].forEach(function (s) { c.beginPath(); c.moveTo(a[0] + s * ox, a[1] + s * oy); c.lineTo(b[0] + s * ox, b[1] + s * oy); c.stroke(); });
    }
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, cx = w / 2, cy = h / 2, d = 95, ph = Math.sin(2 * Math.PI * 0.8 * t), A = 16;
      c.clearRect(0, 0, w, h);
      var O1 = [cx - d, cy], C = [cx, cy], O2 = [cx + d, cy], s1 = 1, s2 = 1, sc = 1;
      if (mode === 'sym') { O1[0] -= A * ph; O2[0] += A * ph; }
      else if (mode === 'asym') { O1[0] += A * ph; O2[0] += A * ph; C[0] -= 2 * A * 0.6 * ph; }
      else if (mode === 'def1') { O1[1] += A * ph; O2[1] += A * ph; C[1] -= 1.4 * A * ph; }
      else { s1 = s2 = 1 + 0.18 * ph; sc = 1 - 0.22 * ph; }
      bond(c, O1, C); bond(c, C, O2);
      atom(c, O1[0], O1[1], 26, '#DC2626', 'O', s1); atom(c, O2[0], O2[1], 26, '#DC2626', 'O', s2); atom(c, C[0], C[1], 22, '#334155', 'C', sc);
    }
    function info() {
      var m = MODES[mode];
      msg.innerHTML = '<b>' + m.t + '</b> \u2014 nombre d\u2019onde ' + m.k + ' \u2014 ' + (m.ir ? '<span class="nt-role nt-role-b">active en IR</span>' : '<span class="nt-role nt-role-a">inactive en IR</span>') + '<br>' + m.why;
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    $$(root, 'input[name="mode"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; info(); draw(); }); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    playLabel(btn, playing); info(); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 4. Spectres infrarouges ================= */
  (function () {
    var root = document.getElementById('lab-ir');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), S, cur = 'ethanol';
    /* bandes : [nombre d'onde (cm-1), largeur (cm-1), profondeur (%), étiquette ou ''] */
    var MOL = {
      ethanol: { lab: 'éthanol', n: 'éthanol (alcool)', b: [[3340, 300, 72, 'O\u2013H lié'], [2975, 60, 50, 'C\u2013H'], [2890, 40, 30, ''], [1450, 35, 25, ''], [1380, 25, 20, ''], [1050, 45, 70, 'C\u2013O'], [880, 25, 30, '']] },
      ethgaz: { lab: 'éthanol gazeux', n: 'éthanol à l\u2019état gazeux (O\u2013H libre)', b: [[3655, 25, 40, 'O\u2013H libre'], [2985, 45, 45, 'C\u2013H'], [2900, 30, 25, ''], [1395, 30, 18, ''], [1240, 30, 15, ''], [1065, 35, 55, 'C\u2013O'], [885, 25, 25, '']] },
      acide: { lab: 'acide éthanoïque', n: 'acide éthanoïque (acide carboxylique)', b: [[3000, 600, 55, 'O\u2013H acide'], [1715, 50, 85, 'C=O'], [1410, 30, 30, ''], [1290, 40, 60, 'C\u2013O'], [940, 50, 35, '']] },
      propanone: { lab: 'propanone', n: 'propanone (cétone)', b: [[3005, 50, 15, 'C\u2013H'], [1715, 40, 88, 'C=O'], [1360, 30, 50, ''], [1220, 30, 55, ''], [530, 30, 30, '']] },
      amine: { lab: 'butan-1-amine', n: 'butan-1-amine (amine)', b: [[3370, 60, 30, 'N\u2013H'], [3290, 60, 25, ''], [2930, 70, 70, 'C\u2013H'], [2860, 40, 50, ''], [1600, 50, 25, ''], [1460, 30, 30, ''], [1070, 40, 25, ''], [780, 60, 40, '']] },
      hexane: { lab: 'hexane', n: 'hexane (alcane)', b: [[2960, 40, 70, 'C\u2013H'], [2930, 40, 72, ''], [2860, 40, 60, ''], [1465, 30, 40, ''], [1380, 25, 25, ''], [725, 25, 20, '']] }
    };
    /* les boutons sont construits à partir des données : ils ne peuvent pas se désynchroniser */
    var seg = $(root, '.nt-mols');
    seg.innerHTML = Object.keys(MOL).map(function (k) {
      return '<label><input type="radio" name="mol" value="' + k + '"' + (k === cur ? ' checked' : '') + '><span>' + MOL[k].lab + '</span></label>';
    }).join('');
    function T(s) {
      var t = 100;
      MOL[cur].b.forEach(function (b) { var sg = b[1] / 2.355; t -= b[2] * Math.exp(-0.5 * Math.pow((s - b[0]) / sg, 2)); });
      return Math.max(2, t);
    }
    function draw() {
      if (!MOL[cur]) { cur = 'ethanol'; }
      var c = S.ctx, w = S.w, h = S.h, L = 42, Rr = w - 12, Tp = 26, B = h - 30;
      function X(s) { return L + (4000 - s) / 3600 * (Rr - L); }
      function Y(t) { return B - t / 100 * (B - Tp); }
      c.clearRect(0, 0, w, h);
      c.fillStyle = 'rgba(148,163,184,.12)'; c.fillRect(X(1500), Tp, X(400) - X(1500), B - Tp);
      c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
      c.fillText('zone d\u2019empreinte digitale', (X(1500) + X(400)) / 2, B - 6);
      c.strokeStyle = col('--ink'); c.lineWidth = 1; c.beginPath(); c.moveTo(L, Tp); c.lineTo(L, B); c.lineTo(Rr, B); c.stroke();
      c.fillStyle = col('--muted');
      [4000, 3500, 3000, 2500, 2000, 1500, 1000, 500].forEach(function (s) { c.fillText(s, X(s), B + 13); });
      c.fillText('nombre d\u2019onde (cm\u207b\u00b9)  \u2190 attention, l\u2019axe est orienté vers la gauche', (L + Rr) / 2, h - 3);
      c.textAlign = 'right'; [0, 50, 100].forEach(function (t) { c.fillText(t, L - 4, Y(t) + 4); });
      c.save(); c.translate(11, (Tp + B) / 2); c.rotate(-Math.PI / 2); c.textAlign = 'center'; c.fillText('transmittance (%)', 0, 0); c.restore();
      c.strokeStyle = col('--blue'); c.lineWidth = 2; c.beginPath();
      for (var s = 4000; s >= 400; s -= 4) { var y = Y(T(s)); if (s === 4000) { c.moveTo(X(s), y); } else { c.lineTo(X(s), y); } }
      c.stroke();
      c.font = '700 12px system-ui, sans-serif';
      MOL[cur].b.forEach(function (b) {
        if (!b[3]) { return; }
        var x = X(b[0]), y = Y(T(b[0]));
        c.fillStyle = col('--rose'); c.textAlign = 'center';
        c.fillText(b[3], x, Math.min(B - 4, y + 16));
      });
      msg.textContent = 'Spectre simplifié (allure) : ' + MOL[cur].n + '.';
    }
    $$(root, 'input[name="mol"]').forEach(function (r) { r.addEventListener('change', function () { cur = r.value; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 5. Dosage par étalonnage spectrophotométrique ================= */
  /* données communes aux deux animations : même colorant, mêmes « mesures » */
  var ETAL = {
    K: 11.6, C0: 0.120, VF: 50,
    noise: function (c) { return c === 0 ? 0 : 1 + 0.025 * Math.sin(c * 997 + 1.3); },
    meas: function (A) { return A < 1.5 ? A : 1.5 + 0.8 * Math.tanh((A - 1.5) / 0.8); },   /* linéaire, puis l'appareil sature */
    color: function (c) { return 'rgba(37, 99, 235, ' + Math.min(0.95, 0.06 + 0.85 * c / 0.120).toFixed(3) + ')'; }
  };
  ETAL.A = function (c) { return ETAL.meas(ETAL.K * c) * ETAL.noise(c); };
  function axes(c, w, h, L, Rr, T, B, CM, AM, dc, da) {
    c.strokeStyle = col('--ink'); c.lineWidth = 1; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(Rr, B); c.stroke();
    c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
    for (var v = 0; v <= CM + 1e-9; v += dc) { c.fillText(fr(v, dc < 0.03 ? 3 : 2), L + v / CM * (Rr - L), B + 13); }
    c.fillText('concentration C (mol\u00b7L\u207b\u00b9)', (L + Rr) / 2, h - 3);
    c.textAlign = 'right'; for (var a = 0; a <= AM + 1e-9; a += da) { c.fillText(fr(a, 1), L - 4, B - a / AM * (B - T) + 4); }
    c.save(); c.translate(11, (T + B) / 2); c.rotate(-Math.PI / 2); c.textAlign = 'center'; c.fillText('absorbance A', 0, 0); c.restore();
  }
  /* --- 5a. Établir la courbe d'étalonnage --- */
  (function () {
    var root = document.getElementById('lab-gamme');
    if (!root) { return; }
    var cv = $(root, 'canvas'), tubes = $(root, '.nt-tubes'), tb = $(root, '.nt-gamme-tab tbody'), msg = $(root, '.nt-msg'), S, done = 0;
    var VM = [0, 10, 20, 30, 40, 50], SOL = VM.map(function (v, i) { return { n: 'S' + i, vm: v, c: ETAL.C0 * v / ETAL.VF }; });
    tubes.innerHTML = '<div class="nt-tubebox"><div class="nt-tube nt-tube-mere"><div class="nt-liq" style="height:85%;background:' + ETAL.color(ETAL.C0) + ';"></div></div><span class="nt-tube-lab">mère</span></div>' +
      SOL.map(function (s) { return '<div class="nt-tubebox"><div class="nt-tube"><div class="nt-liq"></div></div><span class="nt-tube-lab">' + s.n + '</span></div>'; }).join('');
    var T = $$(tubes, '.nt-tube').slice(1);
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, L = 46, Rr = w - 12, Tp = 12, B = h - 32, CM = 0.13, AM = 1.6;
      function X(v) { return L + v / CM * (Rr - L); }
      function Y(a) { return B - a / AM * (B - Tp); }
      c.clearRect(0, 0, w, h); axes(c, w, h, L, Rr, Tp, B, CM, AM, 0.024, 0.4);
      var P = SOL.slice(0, done);
      if (done === SOL.length) {
        var k = P.reduce(function (s, p) { return s + p.c * ETAL.A(p.c); }, 0) / P.reduce(function (s, p) { return s + p.c * p.c; }, 0);
        c.strokeStyle = col('--blue'); c.lineWidth = 2; c.setLineDash([6, 4]); c.beginPath(); c.moveTo(X(0), Y(0)); c.lineTo(X(CM), Y(k * CM)); c.stroke(); c.setLineDash([]);
        c.fillStyle = col('--blue'); c.font = '700 12px system-ui, sans-serif'; c.textAlign = 'left';
        c.textAlign = 'right'; c.fillText('A = ' + fr(k, 1) + ' \u00d7 C', X(0.06) - 8, Y(k * 0.06) - 10);
      }
      P.forEach(function (p, i) {
        c.fillStyle = i === done - 1 ? col('--amber') : col('--blue');
        c.beginPath(); c.arc(X(p.c), Y(ETAL.A(p.c)), i === done - 1 ? 6 : 5, 0, 2 * Math.PI); c.fill();
      });
    }
    function step() {
      if (done >= SOL.length) { return; }
      var s = SOL[done], A = ETAL.A(s.c);
      T.forEach(function (x) { x.classList.remove('nt-tube-active'); });
      var liq = T[done].querySelector('.nt-liq'); T[done].classList.add('nt-tube-active');
      liq.style.height = '85%'; liq.style.background = s.c === 0 ? 'rgba(186, 230, 253, .45)' : ETAL.color(s.c);
      tb.insertAdjacentHTML('beforeend', '<tr><td><b>' + s.n + '</b></td><td>' + fr(s.vm, 1) + '</td><td>' + fr(s.c, 3) + '</td><td>' + fr(A, 2) + '</td></tr>');
      done++;
      if (s.vm === 0) { msg.textContent = 'S0 ne contient que de l\u2019eau distillée : c\u2019est le « blanc », qui sert à régler le zéro d\u2019absorbance de l\u2019appareil.'; }
      else if (s.vm === ETAL.VF) { msg.textContent = 'S5 est la solution mère elle-même (aucune dilution) : C = ' + fr(s.c, 3) + ' mol\u00b7L\u207b\u00b9, A = ' + fr(A, 2) + '.'; }
      else { msg.textContent = s.n + ' : on prélève ' + fr(s.vm, 1) + ' mL de solution mère à la pipette jaugée, on complète à 50,0 mL avec de l\u2019eau distillée. C = 0,120 \u00d7 ' + s.vm + '/50 = ' + fr(s.c, 3) + ' mol\u00b7L\u207b\u00b9. On mesure A = ' + fr(A, 2) + '.'; }
      if (done === SOL.length) { msg.textContent += ' Les points sont alignés sur une droite passant par l\u2019origine : la loi de Beer-Lambert est vérifiée, et la droite d\u2019étalonnage est prête à servir.'; }
      draw();
    }
    function reset() {
      done = 0; tb.innerHTML = '';
      T.forEach(function (x) { x.classList.remove('nt-tube-active'); var l = x.querySelector('.nt-liq'); l.style.height = '0'; });
      msg.textContent = 'Cliquez pour préparer les solutions étalons une à une.'; draw();
    }
    $(root, '[data-act="next"]').addEventListener('click', step);
    $(root, '[data-act="all"]').addEventListener('click', function () { while (done < SOL.length) { step(); } });
    $(root, '[data-act="reset"]').addEventListener('click', reset);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup); reset();
  })();
  /* --- 5b. Exploiter la courbe : doser une solution mystère --- */
  (function () {
    var root = document.getElementById('lab-etal');
    if (!root) { return; }
    var cv = $(root, 'canvas'), cb = $(root, '[data-p="large"]'), btn = $(root, '[data-act="new"]'), liqX = $(root, '.nt-liq-x');
    var oA = $(root, '.out-ax'), oC = $(root, '.out-cx'), oK = $(root, '.out-k'), msg = $(root, '.nt-msg'), S;
    var STD = [0, 0.024, 0.048, 0.072, 0.096, 0.120], BIG = [0.16, 0.20, 0.25, 0.30], cx = 0.065;
    function draw() {
      var P = (cb.checked ? STD.concat(BIG) : STD).map(function (cc) { return [cc, ETAL.A(cc)]; }), lin = P.filter(function (p) { return p[0] <= 0.12; });
      var k = lin.reduce(function (s, p) { return s + p[0] * p[1]; }, 0) / lin.reduce(function (s, p) { return s + p[0] * p[0]; }, 0);
      var Ax = ETAL.meas(ETAL.K * cx), Cx = Ax / k, CM = cb.checked ? 0.32 : 0.16, AM = cb.checked ? 2.6 : 2.0;
      var c = S.ctx, w = S.w, h = S.h, L = 46, Rr = w - 14, T = 12, B = h - 32;
      function X(v) { return L + v / CM * (Rr - L); }
      function Y(a) { return B - a / AM * (B - T); }
      c.clearRect(0, 0, w, h);
      if (cb.checked) { c.fillStyle = 'rgba(225,29,72,.07)'; c.fillRect(X(0.13), T, Rr - X(0.13), B - T); c.fillStyle = col('--rose'); c.font = '700 11px system-ui, sans-serif'; c.textAlign = 'center'; c.fillText('hors du domaine de validité', (X(0.13) + Rr) / 2, T + 14); }
      axes(c, w, h, L, Rr, T, B, CM, AM, cb.checked ? 0.05 : 0.04, 0.5);
      c.strokeStyle = col('--blue'); c.lineWidth = 2; c.setLineDash([6, 4]); c.beginPath(); c.moveTo(X(0), Y(0)); c.lineTo(X(Math.min(CM, AM / k)), Y(Math.min(AM, k * CM))); c.stroke(); c.setLineDash([]);
      P.forEach(function (p) { c.fillStyle = p[0] > 0.12 ? col('--rose') : col('--blue'); c.beginPath(); c.arc(X(p[0]), Y(p[1]), 5, 0, 2 * Math.PI); c.fill(); });
      var inRange = Ax <= ETAL.A(0.120) * 1.02;
      c.strokeStyle = col('--amber'); c.lineWidth = 1.8; c.setLineDash([4, 4]);
      c.beginPath(); c.moveTo(L, Y(Ax)); c.lineTo(X(Cx), Y(Ax)); c.lineTo(X(Cx), B); c.stroke(); c.setLineDash([]);
      c.fillStyle = col('--amber'); c.beginPath(); c.arc(X(Cx), Y(Ax), 6, 0, 2 * Math.PI); c.fill();
      c.font = '700 12px system-ui, sans-serif'; c.textAlign = 'left'; c.fillText('A\u2093', L + 4, Y(Ax) - 6); c.textAlign = 'center'; c.fillText('C\u2093', X(Cx), B - 6);
      liqX.style.background = ETAL.color(cx);
      oA.textContent = fr(Ax, 2); oC.textContent = fr(Cx, 3) + ' mol\u00b7L\u207b\u00b9'; oK.textContent = fr(k, 1) + ' L\u00b7mol\u207b\u00b9';
      msg.textContent = inRange ? 'On reporte A\u2093 sur la droite d\u2019étalonnage et on lit C\u2093, ou on calcule C\u2093 = A\u2093 / k.' :
        'A\u2093 est plus grande que l\u2019absorbance de l\u2019étalon le plus concentré : la solution mystère sort de la gamme. Il faut la diluer (par exemple 2 fois), refaire la mesure, puis multiplier le résultat par le facteur de dilution.';
    }
    btn.addEventListener('click', function () { cx = 0.015 + Math.random() * 0.145; draw(); });
    cb.addEventListener('change', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 6. Loi de Kohlrausch ================= */
  (function () {
    var root = document.getElementById('lab-kohl');
    if (!root) { return; }
    var r = $(root, 'input[type="range"]'), oC = $(root, '.out-c'), tab = $(root, '.nt-kohl-tab'), oS = $(root, '.out-s'), oS2 = $(root, '.out-s2');
    /* conductivités molaires ioniques à 25 °C, en mS·m²·mol⁻¹ */
    var ION = { 'Na+': ['Na<sup>+</sup>', 5.01], 'K+': ['K<sup>+</sup>', 7.35], 'Ca2+': ['Ca<sup>2+</sup>', 11.9], 'Fe3+': ['Fe<sup>3+</sup>', 20.4], 'H3O+': ['H<sub>3</sub>O<sup>+</sup>', 35.0], 'Cl-': ['Cl<sup>\u2212</sup>', 7.63] };
    var SOL = { nacl: [['Na+', 1], ['Cl-', 1]], kcl: [['K+', 1], ['Cl-', 1]], cacl2: [['Ca2+', 1], ['Cl-', 2]], fecl3: [['Fe3+', 1], ['Cl-', 3]], hcl: [['H3O+', 1], ['Cl-', 1]] };
    var cur = 'fecl3';
    function upd() {
      var C = parseFloat(r.value), tot = 0, rows = '', maxS = 0;
      oC.innerHTML = fr(C, 1) + ' mmol\u00b7L<sup>\u22121</sup> = ' + fr(C, 1) + ' mol\u00b7m<sup>\u22123</sup>';
      var lines = SOL[cur].map(function (p) { var ion = ION[p[0]], ci = p[1] * C, s = ion[1] * ci; tot += s; maxS = Math.max(maxS, s); return [ion, p[1], ci, s]; });
      lines.forEach(function (L) {
        rows += '<tr><td>' + L[0][0] + '</td><td>' + (L[1] > 1 ? L[1] + ' C' : 'C') + ' = ' + fr(L[2], 1) + '</td><td>' + fr(L[0][1], 2) + '</td><td><b>' + fr(L[3], 1) + '</b></td>' +
          '<td style="min-width:110px;"><div class="nt-bar nt-bar-I"><div style="width:' + (L[3] / 260 * 100) + '%"></div></div></td></tr>';
      });
      tab.innerHTML = '<thead><tr><th>ion</th><th>C<sub>i</sub> (mol\u00b7m<sup>\u22123</sup>)</th><th>\u03bb<sub>i</sub> (mS\u00b7m\u00b2\u00b7mol<sup>\u22121</sup>)</th><th>\u03c3<sub>i</sub> (mS\u00b7m<sup>\u22121</sup>)</th><th></th></tr></thead><tbody>' + rows + '</tbody>';
      oS.textContent = fr(tot, 1) + ' mS\u00b7m\u207b\u00b9'; oS2.textContent = Math.round(tot * 10).toLocaleString('fr-FR') + ' \u00b5S\u00b7cm\u207b\u00b9';
    }
    $$(root, 'input[name="solute"]').forEach(function (x) { x.addEventListener('change', function () { cur = x.value; upd(); }); });
    r.addEventListener('input', upd); upd();
  })();
  /* ================= 7. Un gaz parfait dans une enceinte ================= */
  (function () {
    var root = document.getElementById('lab-gaz');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rN = $(root, '[data-p="n"]'), rT = $(root, '[data-p="T"]'), rV = $(root, '[data-p="V"]');
    var oN = $(root, '.out-n'), oT = $(root, '.out-T'), oV = $(root, '.out-V'), oP = $(root, '.out-P'), oPV = $(root, '.out-pv'), oNRT = $(root, '.out-nrt');
    var btn = $(root, '[data-act="play"]'), S, playing = !RM, visible = true, last = null, PART = [], hits = 0, hitT = 0, R = 8.314;
    function sync() {
      var N = Math.round(parseFloat(rN.value) * 40);
      while (PART.length < N) { var a = Math.random() * 2 * Math.PI; PART.push({ x: Math.random(), y: Math.random(), dx: Math.cos(a), dy: Math.sin(a) }); }
      PART.length = N;
    }
    function upd() {
      var n = parseFloat(rN.value), T = parseFloat(rT.value), V = parseFloat(rV.value) * 1e-3, P = n * R * T / V;
      oN.textContent = fr(n, 1) + ' mol'; oT.textContent = Math.round(T) + ' K (' + Math.round(T - 273.15) + ' \u00b0C)'; oV.textContent = fr(V * 1e3, 1) + ' L';
      oP.textContent = Math.round(P / 1000).toLocaleString('fr-FR') + ' kPa (' + fr(P / 1e5, 2) + ' bar)';
      oPV.textContent = Math.round(P * V).toLocaleString('fr-FR') + ' J'; oNRT.textContent = Math.round(n * R * T).toLocaleString('fr-FR') + ' J';
      sync();
    }
    function draw(dt) {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, V = parseFloat(rV.value), T = parseFloat(rT.value);
      var bx = 20, by = 16, bh = h - 32, bwMax = w - 60, bw = bwMax * V / 40, sp = 0.18 * Math.sqrt(T / 300);
      c.clearRect(0, 0, w, h);
      c.fillStyle = 'rgba(56,189,248,.08)'; c.fillRect(bx, by, bw, bh);
      c.strokeStyle = col('--slate'); c.lineWidth = 3; c.beginPath(); c.moveTo(bx + bw, by); c.lineTo(bx, by); c.lineTo(bx, by + bh); c.lineTo(bx + bw, by + bh); c.stroke();
      c.fillStyle = col('--slate'); c.fillRect(bx + bw, by - 6, 10, bh + 12); c.fillRect(bx + bw + 10, by + bh / 2 - 4, 30, 8);
      var t = T / 600, pc = 'rgb(' + Math.round(42 + 190 * t) + ',' + Math.round(107 - 40 * t) + ',' + Math.round(196 - 150 * t) + ')';
      PART.forEach(function (p) {
        p.x += p.dx * sp * dt * (bh / bw); p.y += p.dy * sp * dt;
        if (p.x < 0) { p.x = -p.x; p.dx = -p.dx; hits++; } if (p.x > 1) { p.x = 2 - p.x; p.dx = -p.dx; hits++; }
        if (p.y < 0) { p.y = -p.y; p.dy = -p.dy; hits++; } if (p.y > 1) { p.y = 2 - p.y; p.dy = -p.dy; hits++; }
        c.fillStyle = pc; c.beginPath(); c.arc(bx + 6 + p.x * (bw - 12), by + 6 + p.y * (bh - 12), 4, 0, 2 * Math.PI); c.fill();
      });
    }
    function step(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (visible) { draw(playing ? dt : 0); }
      requestAnimationFrame(step);
    }
    [rN, rT, rV].forEach(function (x) { x.addEventListener('input', function () { upd(); if (!playing) { draw(0); } }); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(0); }
    watchVisible(cv, function (v) { visible = v; });
    upd(); playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
})();
</script>
