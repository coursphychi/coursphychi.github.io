+++
title = "Gravitation"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Les lois de Kepler {.nt-h2}

<p class="nt-lead">Johannes Kepler a énoncé trois lois empiriques concernant les mouvements des planètes autour du Soleil, qu'on peut étendre aux mouvements des satellites autour des planètes.</p>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Ces lois sont valables pour tout problème à deux corps en interaction gravitationnelle&nbsp;: une planète autour du Soleil, la Lune autour de la Terre, un satellite artificiel…</p>
</div>

### Première loi&nbsp;: la loi des orbites {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Première loi de Kepler</p>
<p>Dans le référentiel héliocentrique, les trajectoires des planètes du système solaire sont des <span class="imp nt-hole">ellipses</span>, dont le Soleil occupe l'un des <span class="imp nt-hole">foyers</span>.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>L'ellipse</p>
<p>Une <span class="imp">ellipse</span> est une sorte de cercle aplati. Elle est caractérisée par&nbsp;:</p>
<ul class="nt-facts">
<li>son <span class="imp nt-hole">excentricité $e$</span> (écart au cercle), comprise entre 0 et 1&nbsp;;</li>
<li>son <span class="imp nt-hole">grand axe</span>, noté $2a$&nbsp;: la plus grande distance entre deux points de l'ellipse&nbsp;;</li>
<li>son <span class="imp nt-hole">petit axe</span>, noté $2b$&nbsp;: la plus petite distance entre deux points de l'ellipse.</li>
</ul>
<p>Si $e=0$, $a=b$&nbsp;: l'ellipse est un cercle. Si $0 &lt; e &lt; 1$, $a > b$.</p>
</div>

<div class="nt-lab" id="lab-ellipse">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'ellipse et ses foyers</p>
<canvas style="height:320px;" aria-label="Ellipse d'excentricité réglable, avec ses deux foyers, son grand axe et son petit axe"></canvas>
<label class="nt-ctrl">Excentricité $e$&nbsp;: <b class="out-e"></b><input type="range" min="0" max="0.97" step="0.001" value="0.5"></label>
<div class="nt-read" aria-live="polite"><span>$b/a = \sqrt{1-e^2}$ = <b class="out-ba"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-e="0.0167">Terre</button>
<button type="button" class="nt-btn" data-e="0.0934">Mars</button>
<button type="button" class="nt-btn" data-e="0.2056">Mercure</button>
<button type="button" class="nt-btn" data-e="0.249">Pluton</button>
<button type="button" class="nt-btn" data-e="0.967">comète de Halley</button>
</div>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="jardinier" checked> propriété des foyers</label>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-note">Pour tout point M de l'ellipse, la somme des distances aux deux foyers est constante&nbsp;: $\mathrm{MF_1}+\mathrm{MF_2}=2a$. C'est la «&nbsp;méthode du jardinier&nbsp;»&nbsp;: une ficelle de longueur $2a$ attachée à deux piquets, tendue par un crayon, trace une ellipse. Pour la Terre, l'ellipse est indiscernable d'un cercle&nbsp;!</p>
</div>

<p class="nt-lead">À part Mercure, les planètes du système solaire ont une très faible excentricité&nbsp;:</p>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Planète</th><th>Mercure</th><th>Vénus</th><th>Terre</th><th>Mars</th><th>Jupiter</th><th>Saturne</th><th>Uranus</th><th>Neptune</th></tr></thead>
<tbody><tr><td>$e$</td><td>0,2056</td><td>0,0068</td><td>0,0167</td><td>0,0934</td><td>0,0489</td><td>0,0565</td><td>0,0457</td><td>0,0113</td></tr></tbody>
</table>
</div>

### Deuxième loi&nbsp;: la loi des aires {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Deuxième loi de Kepler</p>
<p>Le segment [SP] qui relie le centre P de la planète au centre S du Soleil balaie des <span class="imp nt-hole">aires égales</span> pendant des <span class="imp nt-hole">durées égales</span>.</p>
</div>

<div class="nt-lab" id="lab-aires">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Des aires égales en des durées égales</p>
<canvas style="height:340px;" aria-label="Orbite elliptique découpée en douze secteurs balayés pendant des durées égales, avec la planète et son vecteur vitesse"></canvas>
<label class="nt-ctrl">Excentricité $e$&nbsp;: <b class="out-e"></b><input type="range" min="0" max="0.8" step="0.01" value="0.5"></label>
<div class="nt-read" aria-live="polite"><span>vitesse (en unités de la vitesse moyenne) = <b class="out-v"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-note">L'orbite est découpée en 12 secteurs, chacun balayé pendant un douzième de la période&nbsp;: ils ont tous la même aire. Près du Soleil, les secteurs sont courts et larges, donc la planète parcourt un grand arc&nbsp;: elle va plus vite.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Conséquence sur la vitesse des planètes</p>
<p>La <span class="imp">vitesse</span> de la planète évolue le long de son orbite en fonction de la <span class="imp">distance</span> au Soleil&nbsp;:</p>
<ul class="nt-facts">
<li>elle est <span class="imp nt-hole">maximale</span> au <span class="imp nt-hole">périhélie</span> (point le plus proche du Soleil)&nbsp;;</li>
<li>elle est <span class="imp nt-hole">minimale</span> à l'<span class="imp nt-hole">aphélie</span> (point le plus éloigné du Soleil).</li>
</ul>
</div>

### Troisième loi&nbsp;: la loi des périodes {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Troisième loi de Kepler</p>
<p>Le quotient du <span class="imp">carré de la période de révolution $T$</span> d'une planète par le <span class="imp">cube de la longueur $a$ du demi-grand axe</span> de son orbite est égal à une <span class="imp nt-hole">même constante</span> pour toutes les planètes du système solaire.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi des périodes</p>
<p class="nt-f-math">$$\frac{T^2}{a^3} = k$$</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarques</p>
<ul class="nt-facts">
<li>La constante dépend de l'astre «&nbsp;central&nbsp;». Ainsi, tous les satellites de la Terre partagent eux aussi un même quotient, mais différent de celui des planètes autour du Soleil&nbsp;: $\dfrac{T^2}{a^3}=k'\neq k$.</li>
<li>Ces lois ne sont qu'approximatives&nbsp;: leur validité supposerait que la masse du Soleil soit infiniment plus grande que celle des planètes. En réalité, le petit astre ne tourne pas autour du gros&nbsp;: les deux astres tournent autour de leur centre de masse commun.</li>
</ul>
</div>

<div class="nt-lab" id="lab-kepler3">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Vérifier la troisième loi… et peser l'astre central</p>
<canvas style="height:320px; background:#fff;" aria-label="Carré de la période en fonction du cube du demi-grand axe pour les planètes, les satellites de Jupiter ou ceux de la Terre"></canvas>
<div class="nt-ctrl">Astre central&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="sys" value="soleil" checked><span>le Soleil (planètes)</span></label>
<label><input type="radio" name="sys" value="jupiter"><span>Jupiter (satellites galiléens)</span></label>
<label><input type="radio" name="sys" value="terre"><span>la Terre (Lune et satellites)</span></label>
</div>
</div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-p="log"> échelles logarithmiques</label></div>
<div class="nt-read" aria-live="polite"><span>$k = T^2/a^3$ = <b class="out-k"></b></span><span>masse <span class="out-nom"></span> déduite&nbsp;: <b class="out-m"></b></span></div>
<p class="nt-note">Données réelles. Les points s'alignent sur une droite passant par l'origine&nbsp;: $T^2$ est proportionnel à $a^3$. Comme on le démontre plus bas, $k = \dfrac{4\pi^2}{GM}$&nbsp;: mesurer $k$ permet de «&nbsp;peser&nbsp;» l'astre central. En échelles logarithmiques, les points très éloignés deviennent lisibles.</p>
</div>

## Système en orbite circulaire {.nt-h2}

### Champ et force de gravitation {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>D'après la loi d'interaction gravitationnelle, un astre de masse $M_\mathcal{A}$ et de centre de masse O crée en tout point M de l'espace un <span class="imp nt-hole">champ de gravitation</span> $\vec{\mathcal{G}}$.</p>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 600 420" role="img" aria-label="Champ de gravitation créé par un astre de centre O : en chaque point, le vecteur champ est dirigé vers O, et sa norme diminue avec la distance ; au point M, le champ, le vecteur unitaire et la force subie par un système placé en M"><defs><radialGradient id="gAstre" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#93C5FD"/><stop offset="1" stop-color="#1D4ED8"/></radialGradient></defs><circle cx="300" cy="210" r="55" fill="url(#gAstre)"/><circle cx="300" cy="210" r="3.5" fill="#fff"/><text x="292" y="204" font-size="15" text-anchor="end" fill="#fff" font-family="Georgia, serif" font-style="italic" font-weight="700">O</text><line x1="395.0" y1="210.0" x2="371.0" y2="210.0" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="363.0,210.0 373.0,205.0 373.0,215.0" fill="#94A3B8"/><line x1="382.3" y1="257.5" x2="361.5" y2="245.5" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="354.6,241.5 365.7,242.2 360.7,250.8" fill="#94A3B8"/><line x1="347.5" y1="292.3" x2="335.5" y2="271.5" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="331.5,264.6 340.8,270.7 332.2,275.7" fill="#94A3B8"/><line x1="300.0" y1="305.0" x2="300.0" y2="281.0" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="300.0,273.0 305.0,283.0 295.0,283.0" fill="#94A3B8"/><line x1="252.5" y1="292.3" x2="264.5" y2="271.5" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="268.5,264.6 267.8,275.7 259.2,270.7" fill="#94A3B8"/><line x1="217.7" y1="257.5" x2="238.5" y2="245.5" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="245.4,241.5 239.3,250.8 234.3,242.2" fill="#94A3B8"/><line x1="205.0" y1="210.0" x2="229.0" y2="210.0" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="237.0,210.0 227.0,215.0 227.0,205.0" fill="#94A3B8"/><line x1="217.7" y1="162.5" x2="238.5" y2="174.5" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="245.4,178.5 234.3,177.8 239.3,169.2" fill="#94A3B8"/><line x1="252.5" y1="127.7" x2="264.5" y2="148.5" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="268.5,155.4 259.2,149.3 267.8,144.3" fill="#94A3B8"/><line x1="300.0" y1="115.0" x2="300.0" y2="139.0" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="300.0,147.0 295.0,137.0 305.0,137.0" fill="#94A3B8"/><line x1="347.5" y1="127.7" x2="335.5" y2="148.5" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="331.5,155.4 332.2,144.3 340.8,149.3" fill="#94A3B8"/><line x1="448.7" y1="229.4" x2="440.4" y2="228.4" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="432.4,227.3 443.0,223.7 441.7,233.6" fill="#94A3B8"/><line x1="419.1" y1="301.2" x2="412.4" y2="296.1" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="406.0,291.2 417.0,293.3 410.9,301.3" fill="#94A3B8"/><line x1="357.5" y1="348.5" x2="354.3" y2="340.7" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="351.2,333.4 359.7,340.7 350.4,344.5" fill="#94A3B8"/><line x1="280.6" y1="358.7" x2="281.6" y2="350.4" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="282.7,342.4 286.3,353.0 276.4,351.7" fill="#94A3B8"/><line x1="208.8" y1="329.1" x2="213.9" y2="322.4" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="218.8,316.0 216.7,327.0 208.7,320.9" fill="#94A3B8"/><line x1="161.5" y1="267.5" x2="169.3" y2="264.3" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="176.6,261.2 169.3,269.7 165.5,260.4" fill="#94A3B8"/><line x1="151.3" y1="190.6" x2="159.6" y2="191.6" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="167.6,192.7 157.0,196.3 158.3,186.4" fill="#94A3B8"/><line x1="180.9" y1="118.8" x2="187.6" y2="123.9" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="194.0,128.8 183.0,126.7 189.1,118.7" fill="#94A3B8"/><line x1="242.5" y1="71.5" x2="245.7" y2="79.3" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="248.8,86.6 240.3,79.3 249.6,75.5" fill="#94A3B8"/><line x1="319.4" y1="61.3" x2="318.4" y2="69.6" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="317.3,77.6 313.7,67.0 323.6,68.3" fill="#94A3B8"/><line x1="391.2" y1="90.9" x2="386.1" y2="97.6" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="381.2,104.0 383.3,93.0 391.3,99.1" fill="#94A3B8"/><line x1="505.0" y1="210.0" x2="501.4" y2="210.0" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="493.4,210.0 503.4,205.0 503.4,215.0" fill="#94A3B8"/><line x1="489.4" y1="288.5" x2="486.1" y2="287.1" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="478.7,284.0 489.8,283.2 486.0,292.5" fill="#94A3B8"/><line x1="445.0" y1="355.0" x2="442.4" y2="352.4" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="436.8,346.8 447.4,350.3 440.3,357.4" fill="#94A3B8"/><line x1="378.5" y1="399.4" x2="377.1" y2="396.1" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="374.0,388.7 382.5,396.0 373.2,399.8" fill="#94A3B8"/><line x1="221.5" y1="399.4" x2="222.9" y2="396.1" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="226.0,388.7 226.8,399.8 217.5,396.0" fill="#94A3B8"/><line x1="155.0" y1="355.0" x2="157.6" y2="352.4" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="163.2,346.8 159.7,357.4 152.6,350.3" fill="#94A3B8"/><line x1="110.6" y1="288.5" x2="113.9" y2="287.1" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="121.3,284.0 114.0,292.5 110.2,283.2" fill="#94A3B8"/><line x1="95.0" y1="210.0" x2="98.6" y2="210.0" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="106.6,210.0 96.6,215.0 96.6,205.0" fill="#94A3B8"/><line x1="110.6" y1="131.5" x2="113.9" y2="132.9" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="121.3,136.0 110.2,136.8 114.0,127.5" fill="#94A3B8"/><line x1="155.0" y1="65.0" x2="157.6" y2="67.6" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="163.2,73.2 152.6,69.7 159.7,62.6" fill="#94A3B8"/><line x1="221.5" y1="20.6" x2="222.9" y2="23.9" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="226.0,31.3 217.5,24.0 226.8,20.2" fill="#94A3B8"/><line x1="378.5" y1="20.6" x2="377.1" y2="23.9" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"/><polygon points="374.0,31.3 373.2,20.2 382.5,24.0" fill="#94A3B8"/><line x1="300" y1="210" x2="463.8" y2="95.3" stroke="var(--ink)" stroke-width="1.2" stroke-dasharray="4 4"/><text x="364.2" y="155.3" font-size="14" text-anchor="middle" fill="var(--ink)" font-family="Georgia, serif" transform="rotate(-35.0 364.2 155.3)">OM</text><line x1="463.8" y1="95.3" x2="398.3" y2="141.2" stroke="#E11D48" stroke-width="4.6" stroke-linecap="round"/><polygon points="391.7,145.8 397.1,135.9 402.8,144.1" fill="#E11D48"/><line x1="463.8" y1="95.3" x2="421.2" y2="125.1" stroke="#fff" stroke-width="6.4" stroke-linecap="round"/><polygon points="414.7,129.7 420.0,119.9 425.7,128.1" fill="#fff"/><line x1="463.8" y1="95.3" x2="422.9" y2="124.0" stroke="#FB8A72" stroke-width="3.6" stroke-linecap="round"/><polygon points="416.3,128.6 421.6,118.7 427.4,126.9" fill="#FB8A72"/><line x1="463.8" y1="95.3" x2="445.8" y2="107.9" stroke="#fff" stroke-width="5" stroke-linecap="round"/><polygon points="439.3,112.5 444.6,102.7 450.3,110.9" fill="#fff"/><line x1="463.8" y1="95.3" x2="447.4" y2="106.8" stroke="#059669" stroke-width="2.4" stroke-linecap="round"/><polygon points="440.9,111.3 446.2,101.5 452.0,109.7" fill="#059669"/><circle cx="463.8" cy="95.3" r="5" fill="var(--ink)"/><text x="472.8" y="88.3" font-size="16" fill="var(--ink)" font-family="Georgia, serif" font-style="italic" font-weight="700">M</text><text x="402.05727957315406" y="114.00425471142131" font-size="18" fill="#F26B52" font-family="Georgia, serif" font-style="italic" font-weight="700">G</text><line x1="402.05727957315406" y1="97.00425471142131" x2="411.95727957315404" y2="97.00425471142131" stroke="#F26B52" stroke-width="1.3"/><polygon points="415.0,97.0 410.0,99.6 410.0,94.4" fill="#F26B52"/><text x="401.64031873724605" y="171.48647835763649" font-size="18" fill="#E11D48" font-family="Georgia, serif" font-style="italic" font-weight="700">F</text><line x1="401.64031873724605" y1="154.48647835763649" x2="411.540318737246" y2="154.48647835763649" stroke="#E11D48" stroke-width="1.3"/><polygon points="414.5,154.5 409.5,157.1 409.5,151.9" fill="#E11D48"/><text x="438.33221012883786" y="93.84665421865954" font-size="15" fill="#059669" font-family="Georgia, serif" font-style="italic" font-weight="700">u<tspan font-size="10" dy="4">N</tspan></text><line x1="438.33221012883786" y1="79.84665421865954" x2="446.58221012883786" y2="79.84665421865954" stroke="#059669" stroke-width="1.3"/><polygon points="449.6,79.8 444.6,82.4 444.6,77.2" fill="#059669"/><text x="300" y="234" font-size="11.5" text-anchor="middle" fill="#fff" font-weight="700">astre de</text><text x="300" y="248" font-size="11.5" text-anchor="middle" fill="#fff" font-weight="700">masse M<tspan font-size="8.5" dy="3">A</tspan></text></svg>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Champ de gravitation</p>
<p class="nt-f-math">$$\vec{\mathcal{G}}= G\frac{M_\mathcal{A}}{\mathrm{OM}^2}\,{\color{#6EE7B7}\vec{u}_N}$$</p>
<div class="nt-f-units"><span>$M_\mathcal{A}$ en <b>kg</b></span><span>$\mathrm{OM}$ en <b>m</b></span><span>$G=$ <b>$\pu{6,67E-11 N*m^2*kg^-2}$</b></span><span>${\color{#6EE7B7}\vec{u}_N}$&nbsp;: vecteur unitaire de direction (OM), orienté vers O</span></div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Champ newtonien</p>
<p>Si un système de masse $m$ n'est soumis qu'à l'attraction d'un seul astre de masse $M_\mathcal{A}$, le champ est dit <span class="imp nt-hole">newtonien</span>&nbsp;; la seule force est la force d'interaction gravitationnelle <span class="imp nt-hole">$\vec{F}=m\vec{\mathcal{G}}$</span>.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Référentiel astrocentrique</p>
<p>On se place dans un <span class="imp nt-hole">référentiel astrocentrique</span>&nbsp;: il est lié au centre de masse O de l'astre et à 3 étoiles lointaines supposées fixes. Il est supposé <span class="imp nt-hole">galiléen</span>.</p>
<p class="nt-note">Si l'astre est la Terre, c'est le référentiel <b>géocentrique</b>&nbsp;; si c'est le Soleil, le référentiel <b>héliocentrique</b>.</p>
<p>La trajectoire du système de masse $m$ et de centre de masse M est appelée <span class="imp nt-hole">orbite</span>.</p>
</div>

### Mouvement circulaire uniforme {.nt-h3}

<p class="nt-lead">Étudions le mouvement de M dans le cas d'une <b>orbite circulaire</b>. Si $M_\mathcal{A}\gg m$, l'orbite pourra être considérée comme centrée en O, le centre de l'astre.</p>

<ol class="nt-steps">
<li>
<p><b>Deuxième loi de Newton</b>&nbsp;: $m{\color{#059669}\vec{a}}={\color{#E11D48}m\vec{\mathcal{G}}}\ \Rightarrow\ {\color{#059669}\vec{a}}={\color{#E11D48}\vec{\mathcal{G}}}$.</p>
</li>
<li>
<p><b>Projection dans le repère de Frenet</b>&nbsp;: le champ est dirigé vers O, donc selon $\vec{u}_N$, et n'a pas de composante tangentielle&nbsp;:</p>
<p class="nt-center">$\begin{cases}{\color{#059669}a_T=\dfrac{\mathrm{d}v}{\mathrm{d}t}}={\color{#E11D48}0}\\[3mm] {\color{#059669}a_N = \dfrac{v^2}{R}} = {\color{#E11D48}G\dfrac{M_\mathcal{A}}{R^2}}\end{cases}$</p>
<p class="nt-note">$R$ est le rayon de l'orbite ($R=\mathrm{OM}=\mathrm{cte}$).</p>
</li>
</ol>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Accélération sur une orbite circulaire</p>
<p class="nt-f-math">$$\vec{a}=G\frac{M_\mathcal{A}}{R^2}\,\vec{u}_N$$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>L'accélération est <span class="imp nt-hole">centripète</span> (dirigée vers le centre), et sa norme est <span class="imp nt-hole">constante</span>.</li>
<li>De $\dfrac{\mathrm{d}v}{\mathrm{d}t} = 0$, on déduit que le mouvement est <span class="imp nt-hole">uniforme</span> ($v=\mathrm{cte}$).</li>
<li>De $\dfrac{v^2}{R} = G\dfrac{M_\mathcal{A}}{R^2}$, on obtient la norme de la vitesse&nbsp;: <span class="imp nt-hole">$v = \sqrt{\dfrac{GM_\mathcal{A}}{R}}$</span>.</li>
</ul>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vecteur vitesse sur une orbite circulaire</p>
<p class="nt-f-math">$$\vec{v}=\sqrt{\frac{G M_\mathcal{A}}{R}} \, \vec{u}_T$$</p>
<div class="nt-f-units"><span>$\vec{v}$ <b>ne dépend pas</b> de la masse $m$ du système</span></div>
</div>

### Période de révolution et troisième loi de Kepler {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">période de révolution $T$</span> est la durée pour parcourir une fois l'orbite circulaire de rayon $R$. On a donc&nbsp;: <span class="imp nt-hole">$v\times T = 2\pi R$</span>.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>On élève au carré, puis on remplace $v^2$ par son expression&nbsp;:</p>
<p class="nt-center">${\color{#D97706}v^2} \times T^2 = 4\pi^2 R^2 \quad\Rightarrow\quad {\color{#D97706}\dfrac{G M_\mathcal{A}}{R}}\times T^2 = 4\pi^2 R^2$</p>
<p>Et en réarrangeant&nbsp;:</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Troisième loi de Kepler (orbite circulaire)</p>
<p class="nt-f-math">$$\frac{T^2}{R^3} = \frac{4\pi^2}{G M_\mathcal{A}}$$</p>
<div class="nt-f-units"><span>soit <b>$T = 2\pi \sqrt{\dfrac{R^3}{G M_\mathcal{A}}}$</b></span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Comme $\dfrac{T^2}{R^3}$ ne dépend pas de la masse $m$ du système, on vient de démontrer <span class="imp nt-hole">la troisième loi de Kepler</span> dans le cas d'une orbite circulaire.</p>
<p>La période de révolution est d'autant plus grande que l'orbite est éloignée de l'astre, et la vitesse d'autant plus petite.</p>
</div>

<div class="nt-lab" id="lab-circ">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Satellites en orbite circulaire autour de la Terre</p>
<canvas style="height:380px;" aria-label="Satellite sur une orbite circulaire autour de la Terre, avec ses vecteurs vitesse et accélération"></canvas>
<label class="nt-ctrl">Altitude $h$&nbsp;: <b class="out-h"></b><input type="range" min="200" max="40000" step="50" value="420"></label>
<div class="nt-btns">
<button type="button" class="nt-btn" data-h="420">ISS (420 km)</button>
<button type="button" class="nt-btn" data-h="20200">GPS (20 200 km)</button>
<button type="button" class="nt-btn" data-h="35786">géostationnaire (35 786 km)</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<div class="nt-read" aria-live="polite"><span>$v = \sqrt{GM_\mathrm{T}/R}$ = <b class="out-v"></b></span><span>$T$ = <b class="out-T"></b></span></div>
<p class="nt-note">Plus le satellite est haut, plus il va lentement, et plus sa période est longue&nbsp;: l'ISS fait le tour de la Terre en 1&nbsp;h&nbsp;30 environ, à près de 28&nbsp;000&nbsp;km/h.</p>
</div>

### Le satellite géostationnaire {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-satellite"></i>Définition</p>
<p>Un satellite géostationnaire est un satellite <span class="imp nt-hole">immobile</span> dans le référentiel <span class="imp nt-hole">terrestre</span>&nbsp;:</p>
<ul class="nt-facts">
<li>son orbite est <span class="imp nt-hole">circulaire</span>,</li>
<li>dans le <span class="imp nt-hole">plan équatorial</span> de la Terre,</li>
<li>et sa période vaut <span class="imp nt-hole">la période de rotation de la Terre</span>.</li>
</ul>
<p class="nt-note">La période de rotation de la Terre par rapport aux étoiles (le jour sidéral) vaut 23&nbsp;h&nbsp;56&nbsp;min&nbsp;4&nbsp;s. Les 24&nbsp;h correspondent au jour solaire, qui tient compte du déplacement de la Terre autour du Soleil.</p>
</div>

<p class="nt-lead">Posons $R=R_\mathrm{T}+h$, où $R_\mathrm{T}$ est le rayon terrestre et $h$ l'altitude du satellite, puis isolons $h$&nbsp;:</p>

<p class="nt-center">$\dfrac{T^2}{(R_\mathrm{T}+h)^3} = \dfrac{4\pi^2}{GM_\mathrm{T}} \quad\Longrightarrow\quad h = \sqrt[3]{\dfrac{GM_\mathrm{T}\, T^2}{4\pi^2}}-R_\mathrm{T}$</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-calculator"></i>Application numérique</p>
<p>Données&nbsp;: $M_\mathrm{T}=\pu{6,0E24 kg}$&nbsp;; $R_\mathrm{T}=\pu{6,4E6 m}$&nbsp;; $T \approx \pu{24 h}$.</p>
<p class="nt-center">$h=\left(\dfrac{6{,}67\times10^{-11}\times 6{,}0\times 10^{24}\times( 24 \times 3600)^2 }{4\pi^2}\right)^{1/3}-6{,}4\times 10^{6} = \pu{3,6E7 m}$</p>
<p>Les satellites géostationnaires orbitent à une altitude d'environ <b>36&nbsp;000&nbsp;km</b>. Avec le jour sidéral, plus rigoureux, on trouve 35&nbsp;800&nbsp;km&nbsp;: la différence est invisible à deux chiffres significatifs.</p>
</div>

### Orbiter autour d'un caillou {.nt-h3}

<figure class="nt-fig">
<video src="https://presentationssite.github.io/javelotobelix.mp4" poster="/obelixjavelot.jpg" controls preload="none" style="width:100%; max-width:500px; aspect-ratio:4/3; object-fit:cover; background:#0B1220; border-radius:12px; display:block; margin:auto;"></video>
</figure>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pourquoi cette scène n'est-elle pas réaliste (à part la présence de frottements)&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la démonstration</span></summary>
<div class="nt-d-body">
<p>Car tout objet qui orbite autour d'un «&nbsp;caillou&nbsp;» près de sa surface le fait en environ 1&nbsp;h&nbsp;30&nbsp;!</p>
<ol class="nt-steps">
<li><p>Supposons une boule rocheuse de densité uniforme égale à 5 (la densité moyenne de la Terre)&nbsp;: $\rho\approx\pu{5E3 kg*m-3}$, et sa masse vaut $M = \rho\times V= \rho\times\frac 43 \pi R^3$.</p></li>
<li><p>Or, on a obtenu plus haut $T^2 = \dfrac{4\pi^2 R^3}{GM}$. En remplaçant $M$&nbsp;: $T^2 = \dfrac{4\pi^2 R^3}{G \rho \frac 43 \pi R^3}$.</p></li>
<li><p>Après simplification&nbsp;: $T^2 = \dfrac{3\pi }{G \rho}$, soit $T = \sqrt{\dfrac{3\pi}{G\rho}}$.</p></li>
</ol>
<p><b>Le résultat ne dépend plus de $R$&nbsp;!</b> Pour toute boule d'à peu près la même densité, on obtient la même période de révolution près de sa surface.</p>
<p>A.N.&nbsp;: $T = \sqrt{\dfrac{3\pi}{6{,}67\times10^{-11}\times 5{,}0\times10^{3}}} \approx \pu{5E3 s}$, soit entre 1&nbsp;h et 2&nbsp;h (environ 1&nbsp;h&nbsp;30). Si Obélix recommençait la même expérience sur la Lune, il trouverait un temps comparable.</p>
<p class="nt-note">En réalité, la Lune est un peu moins dense (densité 3,3 environ, car elle n'a qu'un tout petit noyau de fer)&nbsp;: on trouve plutôt 1&nbsp;h&nbsp;50.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Et si Obélix lançait le javelot plus fort&nbsp;?</p>
</div>

<div class="nt-lab" id="lab-canon">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le canon de Newton</p>
<p class="nt-note">On lance horizontalement un objet depuis le sommet d'une très haute montagne (200&nbsp;km&nbsp;!), sans frottements.</p>
<canvas style="height:420px;" aria-label="Trajectoires d'un objet lancé horizontalement depuis une montagne, selon sa vitesse : il retombe, se satellise ou s'échappe"></canvas>
<label class="nt-ctrl">Vitesse de lancement $v_0$&nbsp;: <b class="out-v"></b><input type="range" min="1" max="12" step="0.05" value="5"></label>
<div class="nt-btns">
<button type="button" class="nt-btn" data-v="5">5 km/s</button>
<button type="button" class="nt-btn" data-v="v1">vitesse de l'orbite circulaire</button>
<button type="button" class="nt-btn" data-v="9.5">9,5 km/s</button>
<button type="button" class="nt-btn" data-v="11.5">11,5 km/s</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Une orbite circulaire de rayon $R$ donné correspond à <span class="imp nt-hole">une et une seule vitesse</span>&nbsp;: $v = \sqrt{GM/R}$. Plus lent, l'objet retombe&nbsp;; plus rapide, son orbite devient elliptique (elle n'est plus circulaire).</p>
<p>Au-delà de la <span class="imp nt-hole">vitesse de libération</span> (11,2&nbsp;km/s depuis la surface de la Terre), l'objet échappe définitivement à l'attraction gravitationnelle de la Terre.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les grandes familles d'orbites et les débris spatiaux</span></summary>
<div class="nt-d-body">
<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Orbite</th><th>Altitude</th><th>Usages</th></tr></thead>
<tbody>
<tr><td>basse (LEO)</td><td>160 à 2&nbsp;000 km</td><td>station spatiale, constellations Internet, observation de la Terre&nbsp;; lancement peu coûteux, faible délai radio</td></tr>
<tr><td>moyenne (MEO)</td><td>2&nbsp;000 à 35&nbsp;786 km</td><td>navigation&nbsp;: GPS (20&nbsp;200 km), Galileo (23&nbsp;200 km)</td></tr>
<tr><td>géostationnaire (GEO)</td><td>35&nbsp;786 km</td><td>télécommunications, météorologie&nbsp;: le satellite reste au-dessus d'un même point de l'équateur</td></tr>
<tr><td>héliosynchrone (SSO)</td><td>600 à 800 km environ</td><td>orbite quasi polaire qui passe toujours à la même heure solaire locale&nbsp;: idéale pour l'imagerie</td></tr>
<tr><td>Molniya</td><td>très elliptique</td><td>apogée haut au-dessus de l'hémisphère Nord, pour les liaisons aux hautes latitudes</td></tr>
</tbody>
</table>
</div>
<p><b>Les débris spatiaux.</b> Autour de la Terre gravitent des satellites en service, des étages de fusée abandonnés et une multitude de débris. Le 10 février 2009, le satellite de téléphonie Iridium 33 et le satellite militaire russe hors service Kosmos-2251 sont entrés en collision à 776&nbsp;km d'altitude au-dessus de la Sibérie, à environ 11,6&nbsp;km/s&nbsp;: la collision a produit des centaines de débris. Les agences de surveillance préviennent désormais les opérateurs, et la Station spatiale internationale manœuvre régulièrement pour éviter des débris.</p>
<p><b>À explorer en ligne&nbsp;:</b></p>
<ul class="nt-facts">
<li><a href="https://satellitetracker3d.com/track?norad-id=25544" target="_blank" rel="noopener">Suivre l'ISS en temps réel</a>&nbsp;: on peut y vérifier que les orbites sont des ellipses dont la Terre occupe un foyer, que les satellites lointains vont moins vite, et utiliser les périodes affichées pour tester la troisième loi de Kepler et retrouver la masse de la Terre.</li>
<li><a href="https://stuffin-space.vader.zone" target="_blank" rel="noopener">Stuff in Space</a>&nbsp;: tous les objets en orbite, classés en charges utiles (rouge), corps de fusées (bleu) et débris (gris).</li>
<li><a href="https://scienceetonnante.substack.com/p/orbiter-autour-dun-corps-rocheux" target="_blank" rel="noopener">«&nbsp;Orbiter autour d'un corps rocheux&nbsp;»</a>, le billet de David Louapre (Science étonnante) qui a inspiré la question sur Obélix.</li>
</ul>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CV = '#D97706', CA = '#059669', CS = '#F59E0B', CPL = '#2A6BC4';
  var GRAV = 6.674e-11, ME = 5.972e24, RE = 6.371e6;
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function sci(x, nd) {
    if (x === 0) { return '0'; }
    var n = Math.floor(Math.log10(Math.abs(x)) + 1e-9), a = x / Math.pow(10, n), t = a.toFixed(nd);
    if (Math.abs(parseFloat(t)) >= 10) { n += 1; t = (a / 10).toFixed(nd); }
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
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '700 12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.9)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  function arrow(c, x1, y1, x2, y2, color, w) {
    var dx = x2 - x1, dy = y2 - y1, n = Math.hypot(dx, dy); if (n < 2) { return; }
    var ux = dx / n, uy = dy / n, L = Math.min(11, n * 0.45), W = L * 0.5;
    c.strokeStyle = color; c.fillStyle = color; c.lineWidth = w || 2.6; c.lineCap = 'round';
    c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2 - ux * L * 0.8, y2 - uy * L * 0.8); c.stroke();
    c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - ux * L - uy * W, y2 - uy * L + ux * W); c.lineTo(x2 - ux * L + uy * W, y2 - uy * L - ux * W); c.closePath(); c.fill();
  }
  function sun(c, x, y, r) {
    var g = c.createRadialGradient(x, y, 0, x, y, r * 1.8); g.addColorStop(0, '#FEF3C7'); g.addColorStop(0.45, '#FBBF24'); g.addColorStop(1, 'rgba(251,191,36,0)');
    c.fillStyle = g; c.beginPath(); c.arc(x, y, r * 1.8, 0, 2 * Math.PI); c.fill();
  }
  function loopVisible(cv, btn, f) {
    var st = { playing: !RM, visible: true, last: null };
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { st.visible = es[0].isIntersecting; }).observe(cv); }
    if (btn) { playLabel(btn, st.playing); btn.addEventListener('click', function () { st.playing = !st.playing; playLabel(btn, st.playing); }); }
    (function step(ts) { var dt = st.last === null ? 0 : Math.min(0.05, (ts - st.last) / 1000); st.last = ts; if (st.visible) { f(st.playing ? dt : 0); } requestAnimationFrame(step); })(performance.now());
    return st;
  }
  /* résolution de l'équation de Kepler : position sur l'ellipse à une date donnée (anomalie moyenne Mm) */
  function keplerPos(e, Mm) {
    var E = Mm; for (var i = 0; i < 30; i++) { E -= (E - e * Math.sin(E) - Mm) / (1 - e * Math.cos(E)); }
    return [Math.cos(E) - e, Math.sqrt(1 - e * e) * Math.sin(E)];   /* foyer (Soleil) à l'origine, demi-grand axe = 1 */
  }
  /* ================= 1. L'ellipse ================= */
  (function () {
    var root = document.getElementById('lab-ellipse');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rE = $(root, 'input[type="range"]'), cbJ = $(root, '[data-p="jardinier"]'), oE = $(root, '.out-e'), oB = $(root, '.out-ba'), btn = $(root, '[data-act="play"]'), S, th = 0.6;
    function draw(dt) {
      if (!S) { return; }
      th += dt * 0.6;
      var e = +rE.value, c = S.ctx, w = S.w, h = S.h, cx = w / 2, cy = h / 2 + 6;
      var a = Math.min(w * 0.4, h * 0.44), b = a * Math.sqrt(1 - e * e), f = a * e;   /* demi-axes et distance centre-foyer c = ae */
      oE.textContent = fr(e, 3); oB.textContent = fr(b / a, 3);
      c.clearRect(0, 0, w, h);
      c.strokeStyle = 'rgba(30,41,59,.25)'; c.setLineDash([4, 4]); c.lineWidth = 1;
      c.beginPath(); c.moveTo(cx - a - 10, cy); c.lineTo(cx + a + 10, cy); c.moveTo(cx, cy - b - 10); c.lineTo(cx, cy + b + 10); c.stroke(); c.setLineDash([]);
      c.strokeStyle = CPL; c.lineWidth = 2.6; c.beginPath(); c.ellipse(cx, cy, a, b, 0, 0, 2 * Math.PI); c.stroke();
      /* grand axe et petit axe */
      c.strokeStyle = '#7C3AED'; c.lineWidth = 1.6; c.beginPath(); c.moveTo(cx - a, cy - 3); c.lineTo(cx + a, cy - 3); c.stroke();
      txt(c, '2a (grand axe)', cx - a / 2, cy - 10, '#7C3AED');
      c.strokeStyle = '#059669'; c.lineWidth = 1.6; c.beginPath(); c.moveTo(cx + 3, cy - b); c.lineTo(cx + 3, cy + b); c.stroke();   /* même épaisseur que le grand axe */
      txt(c, '2b', cx + 18, cy - b / 2, '#059669');
      /* foyers */
      sun(c, cx + f, cy, 10); c.fillStyle = CS; c.beginPath(); c.arc(cx + f, cy, 6, 0, 2 * Math.PI); c.fill();
      txt(c, 'F\u2081 (Soleil)', cx + f, cy + 26, '#B45309');
      c.fillStyle = col('--slate'); c.beginPath(); c.arc(cx - f, cy, 3.5, 0, 2 * Math.PI); c.fill(); txt(c, 'F\u2082', cx - f, cy + 20, col('--slate'));
      /* point courant et construction du jardinier */
      var px = cx + a * Math.cos(th), py = cy - b * Math.sin(th);
      if (cbJ.checked) {
        c.strokeStyle = '#E11D48'; c.lineWidth = 1.8; c.beginPath(); c.moveTo(cx + f, cy); c.lineTo(px, py); c.lineTo(cx - f, cy); c.stroke();
        var d1 = Math.hypot(px - cx - f, py - cy) / a, d2 = Math.hypot(px - cx + f, py - cy) / a;
        txt(c, 'MF\u2081 + MF\u2082 = ' + fr(d1, 2) + 'a + ' + fr(d2, 2) + 'a = 2a', w / 2, h - 10, '#E11D48', '700 13px system-ui, sans-serif');
      }
      c.fillStyle = CPL; c.beginPath(); c.arc(px, py, 6, 0, 2 * Math.PI); c.fill(); txt(c, 'M', px + 12, py - 8, CPL, 'italic 700 13px Georgia, serif');
    }
    rE.addEventListener('input', function () { draw(0); }); cbJ.addEventListener('change', function () { draw(0); });
    $$(root, '[data-e]').forEach(function (b) { b.addEventListener('click', function () { rE.value = b.getAttribute('data-e'); draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    setup(); onResize(setup); loopVisible(cv, btn, draw);
  })();
  /* ================= 2. La loi des aires ================= */
  (function () {
    var root = document.getElementById('lab-aires');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rE = $(root, 'input[type="range"]'), oE = $(root, '.out-e'), oV = $(root, '.out-v'), btn = $(root, '[data-act="play"]'), S, t = 0, NS = 12;
    function draw(dt) {
      if (!S) { return; }
      t += dt * 0.12;
      var e = +rE.value, c = S.ctx, w = S.w, h = S.h, A = Math.min(w * 0.36, h * 0.46 / Math.sqrt(1 - e * e)), cx = w / 2 + A * e, cy = h / 2;
      oE.textContent = fr(e, 2);
      function P(q) { return [cx + q[0] * A, cy - q[1] * A]; }
      c.clearRect(0, 0, w, h);
      /* secteurs balayés pendant des durées égales (T/12) */
      for (var k = 0; k < NS; k++) {
        c.fillStyle = k % 2 ? 'rgba(42,107,196,.16)' : 'rgba(42,107,196,.30)';
        c.beginPath(); c.moveTo(cx, cy);
        for (var j = 0; j <= 20; j++) { var q = P(keplerPos(e, 2 * Math.PI * (k + j / 20) / NS)); c.lineTo(q[0], q[1]); }
        c.closePath(); c.fill();
      }
      c.strokeStyle = CPL; c.lineWidth = 2.2; c.beginPath();
      for (var i = 0; i <= 200; i++) { var p = P(keplerPos(e, 2 * Math.PI * i / 200)); if (i === 0) { c.moveTo(p[0], p[1]); } else { c.lineTo(p[0], p[1]); } }
      c.stroke();
      sun(c, cx, cy, 12); c.fillStyle = CS; c.beginPath(); c.arc(cx, cy, 7, 0, 2 * Math.PI); c.fill();
      var peri = P([1 - e, 0]), aph = P([-1 - e, 0]);
      txt(c, 'périhélie', peri[0] + 8, peri[1] + 4, col('--slate'), '700 12px system-ui, sans-serif', 'left');
      txt(c, 'aphélie', aph[0] - 8, aph[1] + 4, col('--slate'), '700 12px system-ui, sans-serif', 'right');
      /* planète et vecteur vitesse */
      var Mm = (t % 1) * 2 * Math.PI, pos = keplerPos(e, Mm), pp = P(pos), dM = 1e-3, p2 = keplerPos(e, Mm + dM);
      var vx = (p2[0] - pos[0]) / dM, vy = (p2[1] - pos[1]) / dM, v = Math.hypot(vx, vy);
      c.strokeStyle = 'rgba(30,41,59,.5)'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(cx, cy); c.lineTo(pp[0], pp[1]); c.stroke();
      arrow(c, pp[0], pp[1], pp[0] + vx * A * 0.18, pp[1] - vy * A * 0.18, CV, 2.8);
      c.fillStyle = CPL; c.beginPath(); c.arc(pp[0], pp[1], 7, 0, 2 * Math.PI); c.fill();
      var vmax = Math.sqrt((1 + e) / (1 - e)), vmin = Math.sqrt((1 - e) / (1 + e));
      oV.textContent = fr(v, 2) + ' (de ' + fr(vmin, 2) + ' à l\u2019aphélie à ' + fr(vmax, 2) + ' au périhélie)';
    }
    rE.addEventListener('input', function () { draw(0); });
    function setup() { S = canvasCtx(cv); draw(0); }
    setup(); onResize(setup); loopVisible(cv, btn, draw);
  })();
  /* ================= 3. La troisième loi avec de vraies données ================= */
  (function () {
    var root = document.getElementById('lab-kepler3');
    if (!root) { return; }
    var cv = $(root, 'canvas'), cbL = $(root, '[data-p="log"]'), oK = $(root, '.out-k'), oM = $(root, '.out-m'), oN = $(root, '.out-nom'), S, sys = 'soleil';
    var UA = 1.496e11, AN = 3.156e7, J = 86400;
    var SYS = {
      soleil: { nom: 'du Soleil', vrai: '1,99 \u00d7 10<sup>30</sup> kg', pts: [['Mercure', 0.387 * UA, 0.241 * AN], ['Vénus', 0.723 * UA, 0.615 * AN], ['Terre', 1.000 * UA, 1.000 * AN], ['Mars', 1.524 * UA, 1.881 * AN], ['Jupiter', 5.203 * UA, 11.86 * AN], ['Saturne', 9.537 * UA, 29.46 * AN], ['Uranus', 19.19 * UA, 84.01 * AN], ['Neptune', 30.07 * UA, 164.8 * AN]] },
      jupiter: { nom: 'de Jupiter', vrai: '1,90 \u00d7 10<sup>27</sup> kg', pts: [['Io', 4.217e8, 1.769 * J], ['Europe', 6.710e8, 3.551 * J], ['Ganymède', 1.0704e9, 7.155 * J], ['Callisto', 1.8827e9, 16.69 * J]] },
      terre: { nom: 'de la Terre', vrai: '5,97 \u00d7 10<sup>24</sup> kg', pts: [['ISS', 6.791e6, 92.7 * 60], ['GPS', 2.656e7, 717.97 * 60], ['géostationnaire', 4.2164e7, 1436.07 * 60], ['Lune', 3.844e8, 27.32 * J]] }
    };
    function draw() {
      var s = SYS[sys], c = S.ctx, w = S.w, h = S.h, lg = cbL.checked;
      var X = s.pts.map(function (p) { return Math.pow(p[1], 3); }), Y = s.pts.map(function (p) { return p[2] * p[2]; });
      var k = 0; s.pts.forEach(function (p, i) { k += Y[i] / X[i]; }); k /= s.pts.length;
      oN.textContent = s.nom; oK.innerHTML = sci(k, 2) + ' s\u00b2\u00b7m<sup>\u22123</sup>';
      oM.innerHTML = sci(4 * Math.PI * Math.PI / (GRAV * k), 2) + ' kg <span class="nt-note">(valeur tabulée\u00a0: ' + s.vrai + ')</span>';
      c.clearRect(0, 0, w, h);
      var L = 64, R = w - 20, T = 16, B = h - 40;
      var xmin, xmax, ymin, ymax, fx, fy;
      if (lg) {
        xmin = Math.floor(Math.log10(Math.min.apply(null, X))); xmax = Math.ceil(Math.log10(Math.max.apply(null, X)));
        ymin = Math.floor(Math.log10(Math.min.apply(null, Y))); ymax = Math.ceil(Math.log10(Math.max.apply(null, Y)));
        fx = function (v) { return L + (Math.log10(v) - xmin) / (xmax - xmin) * (R - L); }; fy = function (v) { return B - (Math.log10(v) - ymin) / (ymax - ymin) * (B - T); };
      } else {
        xmax = Math.max.apply(null, X) * 1.08; ymax = Math.max.apply(null, Y) * 1.08;
        fx = function (v) { return L + v / xmax * (R - L); }; fy = function (v) { return B - v / ymax * (B - T); };
      }
      c.strokeStyle = col('--ink'); c.lineWidth = 1; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
      c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
      c.fillText('a\u00b3 (m\u00b3)' + (lg ? ', échelle logarithmique' : ''), (L + R) / 2, h - 6);
      c.save(); c.translate(14, (T + B) / 2); c.rotate(-Math.PI / 2); c.fillText('T\u00b2 (s\u00b2)' + (lg ? ', échelle log.' : ''), 0, 0); c.restore();
      if (lg) {
        for (var gx = xmin; gx <= xmax; gx += Math.max(1, Math.round((xmax - xmin) / 6))) { c.textAlign = 'center'; c.fillText('10' + sup(gx), fx(Math.pow(10, gx)), B + 15); }
        for (var gy = ymin; gy <= ymax; gy += Math.max(1, Math.round((ymax - ymin) / 5))) { c.textAlign = 'right'; c.fillText('10' + sup(gy), L - 6, fy(Math.pow(10, gy)) + 4); }
      }
      /* droite T² = k a³ */
      c.save(); c.beginPath(); c.rect(L, T, R - L, B - T); c.clip();
      c.strokeStyle = 'rgba(5,150,105,.7)'; c.lineWidth = 2; c.setLineDash([6, 4]); c.beginPath();
      if (lg) { c.moveTo(fx(Math.pow(10, xmin)), fy(k * Math.pow(10, xmin))); c.lineTo(fx(Math.pow(10, xmax)), fy(k * Math.pow(10, xmax))); }
      else { c.moveTo(fx(0), fy(0)); c.lineTo(fx(xmax), fy(k * xmax)); }
      c.stroke(); c.restore(); c.setLineDash([]);
      var lx = lg ? Math.pow(10, xmin + 0.35 * (xmax - xmin)) : 0.45 * xmax;   /* étiquette posée le long de la droite */
      txt(c, 'T\u00b2 = k a\u00b3', fx(lx) - 6, fy(k * lx) - 10, '#059669', '700 12px system-ui, sans-serif', 'right');
      s.pts.forEach(function (p, i) {
        var x = fx(X[i]), y = fy(Y[i]);
        c.fillStyle = CPL; c.beginPath(); c.arc(x, y, 5.5, 0, 2 * Math.PI); c.fill();
        txt(c, p[0], x + 9, y - 7, col('--ink'), '600 11px system-ui, sans-serif', 'left');
      });
    }
    function sup(n) { var m = { '-': '\u207b', 0: '\u2070', 1: '\u00b9', 2: '\u00b2', 3: '\u00b3', 4: '\u2074', 5: '\u2075', 6: '\u2076', 7: '\u2077', 8: '\u2078', 9: '\u2079' }; return String(n).split('').map(function (ch) { return m[ch]; }).join(''); }
    $$(root, 'input[name="sys"]').forEach(function (x) { x.addEventListener('change', function () { sys = x.value; draw(); }); });
    cbL.addEventListener('change', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 4. Les orbites circulaires autour de la Terre ================= */
  (function () {
    var root = document.getElementById('lab-circ');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rH = $(root, 'input[type="range"]'), oH = $(root, '.out-h'), oV = $(root, '.out-v'), oT = $(root, '.out-T'), btn = $(root, '[data-act="play"]'), S, th = 0;
    function draw(dt) {
      if (!S) { return; }
      var h = +rH.value * 1000, R = RE + h, v = Math.sqrt(GRAV * ME / R), T = 2 * Math.PI * R / v;
      th += dt * 2 * Math.PI / T * 3000;   /* accéléré 3 000 fois */
      oH.textContent = Math.round(h / 1000).toLocaleString('fr-FR') + ' km';
      oV.textContent = fr(v / 1000, 2) + ' km\u00b7s\u207b\u00b9';
      oT.textContent = T < 7200 ? fr(T / 60, 0) + ' min' : fr(T / 3600, 1) + ' h';
      var c = S.ctx, w = S.w, hh = S.h, cx = w / 2, cy = hh / 2, k = Math.min(w, hh) * 0.46 / (RE + 36e6);
      c.clearRect(0, 0, w, hh);
      c.fillStyle = '#0B1220'; c.fillRect(0, 0, w, hh);
      [[2.02e7 + RE, 'GPS'], [3.5786e7 + RE, 'géostationnaire']].forEach(function (q) {
        c.strokeStyle = 'rgba(148,163,184,.35)'; c.setLineDash([3, 5]); c.lineWidth = 1; c.beginPath(); c.arc(cx, cy, q[0] * k, 0, 2 * Math.PI); c.stroke(); c.setLineDash([]);
        c.fillStyle = 'rgba(203,213,225,.75)'; c.font = '600 11px system-ui, sans-serif'; c.textAlign = 'left'; c.fillText(q[1], cx + q[0] * k * 0.72 + 4, cy - q[0] * k * 0.72 - 4);
      });
      var g = c.createRadialGradient(cx - RE * k * 0.3, cy - RE * k * 0.3, 2, cx, cy, RE * k); g.addColorStop(0, '#93C5FD'); g.addColorStop(1, '#1D4ED8');
      c.fillStyle = g; c.beginPath(); c.arc(cx, cy, RE * k, 0, 2 * Math.PI); c.fill();
      c.strokeStyle = '#FDE68A'; c.lineWidth = 1.8; c.beginPath(); c.arc(cx, cy, R * k, 0, 2 * Math.PI); c.stroke();
      var sx = cx + R * k * Math.cos(th), sy = cy - R * k * Math.sin(th), ut = [-Math.sin(th), -Math.cos(th)], un = [-Math.cos(th), Math.sin(th)];
      arrow(c, sx, sy, sx + ut[0] * v / 1000 * 9, sy + ut[1] * v / 1000 * 9, CV, 2.8);
      var a = GRAV * ME / (R * R); arrow(c, sx, sy, sx + un[0] * (8 + a * 5), sy + un[1] * (8 + a * 5), '#34D399', 2.8);
      c.fillStyle = '#F8FAFC'; c.beginPath(); c.arc(sx, sy, 5, 0, 2 * Math.PI); c.fill();
      c.fillStyle = '#FDE68A'; c.font = '700 12px system-ui, sans-serif'; c.textAlign = 'left'; c.fillText('v', sx + ut[0] * v / 1000 * 9 + 6, sy + ut[1] * v / 1000 * 9);
      c.fillStyle = '#34D399'; c.fillText('a', sx + un[0] * (8 + a * 5) + 6, sy + un[1] * (8 + a * 5) + 4);
      c.fillStyle = 'rgba(248,250,252,.6)'; c.font = '11px system-ui, sans-serif'; c.textAlign = 'right'; c.fillText('animation accélérée 3 000 fois (orbites à l\u2019échelle)', w - 10, hh - 10);
    }
    rH.addEventListener('input', function () { draw(0); });
    $$(root, '[data-h]').forEach(function (b) { b.addEventListener('click', function () { rH.value = b.getAttribute('data-h'); draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    setup(); onResize(setup); loopVisible(cv, btn, draw);
  })();
  /* ================= 5. Le canon de Newton ================= */
  (function () {
    var root = document.getElementById('lab-canon');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rV = $(root, 'input[type="range"]'), oV = $(root, '.out-v'), msg = $(root, '.nt-msg'), btn = $(root, '[data-act="play"]'), S, traj = [], t = 0, GM = GRAV * ME, H0 = 2e5;
    var R0 = RE + H0, V1 = Math.sqrt(GM / R0), VL = Math.sqrt(2 * GM / R0);
    function compute() {
      var v0 = +rV.value * 1000, x = 0, y = R0, vx = v0, vy = 0, dt = 5, out = [[x, y, 0]], tt = 0, ang = 0, prev = Math.atan2(x, y);
      for (var i = 0; i < 40000; i++) {
        /* méthode de Verlet (vitesse) : conserve bien l'énergie sur une orbite complète */
        var r = Math.hypot(x, y), ax = -GM * x / (r * r * r), ay = -GM * y / (r * r * r);
        x += vx * dt + 0.5 * ax * dt * dt; y += vy * dt + 0.5 * ay * dt * dt;
        var r2 = Math.hypot(x, y), bx = -GM * x / (r2 * r2 * r2), by = -GM * y / (r2 * r2 * r2);
        vx += 0.5 * (ax + bx) * dt; vy += 0.5 * (ay + by) * dt; tt += dt;
        var cur = Math.atan2(x, y), d = cur - prev; if (d < -Math.PI) { d += 2 * Math.PI; } if (d > Math.PI) { d -= 2 * Math.PI; } ang += d; prev = cur;
        out.push([x, y, tt]);
        if (r2 < RE || ang > 2 * Math.PI || r2 > 9 * RE) { break; }
      }
      traj = out; t = 0;
      var en = 0.5 * v0 * v0 - GM / R0;
      if (Math.abs(v0 - V1) < 60) { msg.textContent = 'Orbite circulaire : à cette altitude, il faut exactement v\u2081 = ' + fr(V1 / 1000, 2) + ' km/s. Période : ' + Math.round(2 * Math.PI * R0 / V1 / 60) + ' min.'; }
      else if (v0 < V1) {
        var lastP = out[out.length - 1];
        msg.textContent = Math.hypot(lastP[0], lastP[1]) < RE + 1 ? 'Trop lent : l\u2019objet retombe sur la Terre (sa trajectoire est une portion d\u2019ellipse). Plus on lance vite, plus il tombe loin.'
          : 'Orbite elliptique : le point de lancement devient l\u2019apogée (point le plus éloigné de la Terre).';
      }
      else if (en < 0) { var a = -GM / (2 * en); msg.textContent = 'Orbite elliptique : le point de lancement devient le périgée. Période : ' + (2 * Math.PI * Math.sqrt(a * a * a / GM) / 3600).toFixed(1).replace('.', ',') + ' h.'; }
      else { msg.textContent = 'Vitesse supérieure à la vitesse de libération (' + fr(VL / 1000, 1) + ' km/s à cette altitude) : l\u2019objet échappe à l\u2019attraction de la Terre et ne revient jamais.'; }
    }
    function draw(dt) {
      if (!S) { return; }
      oV.textContent = fr(+rV.value, 1) + ' km\u00b7s\u207b\u00b9';
      var c = S.ctx, w = S.w, h = S.h, k = Math.min(w, h) / (7 * RE), cx = w / 2, cy = h / 2;
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#0B1220'; c.fillRect(0, 0, w, h);
      var g = c.createRadialGradient(cx - RE * k * 0.3, cy - RE * k * 0.3, 2, cx, cy, RE * k); g.addColorStop(0, '#93C5FD'); g.addColorStop(1, '#1D4ED8');
      c.fillStyle = g; c.beginPath(); c.arc(cx, cy, RE * k, 0, 2 * Math.PI); c.fill();
      /* montagne (très exagérée) et lanceur */
      c.fillStyle = '#A8A29E'; c.beginPath(); c.moveTo(cx - 18, cy - RE * k + 4); c.lineTo(cx, cy - R0 * k); c.lineTo(cx + 18, cy - RE * k + 4); c.closePath(); c.fill();
      if (traj.length) {
        t += dt * 900;   /* temps accéléré */
        var tEnd = traj[traj.length - 1][2]; if (t > tEnd + 1500) { t = 0; }
        c.strokeStyle = 'rgba(253,224,71,.85)'; c.lineWidth = 2; c.beginPath();
        var last = traj[0];
        for (var i = 0; i < traj.length && traj[i][2] <= t; i++) { var p = traj[i]; if (i === 0) { c.moveTo(cx + p[0] * k, cy - p[1] * k); } else { c.lineTo(cx + p[0] * k, cy - p[1] * k); } last = p; }
        c.stroke();
        c.fillStyle = '#FDE047'; c.beginPath(); c.arc(cx + last[0] * k, cy - last[1] * k, 4.5, 0, 2 * Math.PI); c.fill();
      }
    }
    rV.addEventListener('input', function () { compute(); draw(0); });
    $$(root, '[data-v]').forEach(function (b) { b.addEventListener('click', function () { rV.value = b.getAttribute('data-v') === 'v1' ? (V1 / 1000).toFixed(2) : b.getAttribute('data-v'); compute(); draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    compute(); setup(); onResize(setup); loopVisible(cv, btn, draw);
  })();
})();
</script>
