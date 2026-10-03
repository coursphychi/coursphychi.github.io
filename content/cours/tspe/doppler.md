+++
title = "Effet Doppler"
draft = false
hidden = true
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Une expérience du quotidien {.nt-h2}

<p class="nt-lead">Quand une voiture, une moto ou une ambulance passe devant nous, le son qu'elle émet paraît plus aigu pendant qu'elle approche, puis brusquement plus grave dès qu'elle s'éloigne. Pourtant, pour le conducteur, le son ne change pas.</p>

<div class="nt-lab" id="lab-passage">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Une voiture passe devant vous</p>
<p class="nt-note">Le moteur émet un son de fréquence 500&nbsp;Hz. Vous êtes au bord de la route&nbsp;; cochez «&nbsp;avec le son&nbsp;» pour l'entendre (baissez d'abord le volume).</p>
<canvas class="scene" style="height:120px;" aria-label="Vue de dessus de la route : la voiture passe devant l'auditeur"></canvas>
<canvas class="graph" style="height:200px; margin-top:8px; background:#fff;" aria-label="Fréquence perçue en fonction de la position de la voiture"></canvas>
<div class="nt-read" aria-live="polite"><span>fréquence perçue = <b class="out-f"></b></span><span>décalage = <b class="out-d"></b></span></div>
<label class="nt-ctrl">Vitesse de la voiture&nbsp;: <b class="out-v"></b><input type="range" data-p="v" min="30" max="150" step="5" value="90"></label>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="son"> avec le son</label>
<button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Lancer le passage</button>
</div>
<p class="nt-msg">Les pointillés bleu et rose donnent les fréquences perçues quand la voiture arrive de loin et quand elle repart au loin. Plus la voiture est rapide, plus l'écart entre les deux est grand.</p>
</div>

## Définition et formule {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'effet Doppler correspond au <span class="imp nt-hole">décalage</span> de la fréquence de l'onde reçue par un récepteur lorsque l'émetteur <span class="imp nt-hole">se rapproche ou s'éloigne</span> du récepteur.</p>
<p>Le <span class="imp">décalage Doppler</span> <span class="imp">$\Delta f$</span> est lié à la vitesse <span class="imp">$v$</span> de l'émetteur par rapport au récepteur.</p>
</div>

<div class="nt-lab" id="lab-fronts">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Les crêtes se resserrent devant l'émetteur</p>
<canvas style="height:280px;" aria-label="Crêtes d'onde circulaires émises par une source qui se déplace vers la droite ; elles sont resserrées devant et espacées derrière"></canvas>
<label class="nt-ctrl">Vitesse de l'émetteur&nbsp;: <b class="out-b"></b><input type="range" data-p="beta" min="0" max="0.9" step="0.01" value="0.4"></label>
<div class="nt-read"><span>récepteur A (devant)&nbsp;: <b class="out-a"></b>, soit <b class="out-fa"></b></span><span>récepteur B (derrière)&nbsp;: <b class="out-r"></b>, soit <b class="out-fr"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg">Chaque cercle est une crête émise une période plus tôt que la suivante, depuis la position qu'occupait alors l'émetteur. Devant lui, les crêtes s'entassent&nbsp;: la longueur d'onde reçue est plus courte, donc la fréquence plus grande. Derrière, c'est l'inverse.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-arrow-right-to-bracket"></i>L'émetteur se rapproche</p>
<p class="nt-f-math">$$\Delta f = f\times\frac{v}{c-v}$$</p>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-arrow-right-from-bracket"></i>L'émetteur s'éloigne</p>
<p class="nt-f-math">$$\Delta f = -f\times\frac{v}{c+v}$$</p>
</div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-ruler"></i>Grandeurs et unités</p>
<ul class="nt-facts">
<li>$v$&nbsp;: norme de la vitesse de l'émetteur par rapport au récepteur en <span class="imp nt-hole">$\pu{m*s-1}$</span></li>
<li>$f$&nbsp;: fréquence de l'émetteur en <span class="imp nt-hole">Hz</span></li>
<li>$c$&nbsp;: célérité de l'onde en <span class="imp nt-hole">$\pu{m*s-1}$</span></li>
</ul>
<p>On considèrera qu'on a toujours $v<c$.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>L'émetteur se rapproche</p>
<p>$\Delta f$ <span class="imp nt-hole">$>$</span> 0</p>
<p>Le son perçu est plus <span class="imp nt-hole">aigu</span>.<br>La lumière perçue est plus <span class="imp nt-hole">bleue</span>.</p>
</div>
<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>L'émetteur s'éloigne</p>
<p>$\Delta f$ <span class="imp nt-hole">$<$</span> 0</p>
<p>Le son perçu est plus <span class="imp nt-hole">grave</span>.<br>La lumière perçue est plus <span class="imp nt-hole">rouge</span>.</p>
</div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>On établit l'expression du décalage Doppler $\Delta f = f' - f$ (fréquence reçue moins fréquence émise) pour un récepteur fixe et un émetteur qui se rapproche de lui en ligne droite à la vitesse $v$.</p>
<svg class="nt-svg" viewBox="0 0 720 250" role="img" aria-label="Pendant une période T, la première crête parcourt cT tandis que l'émetteur avance de vT : la distance entre deux crêtes devient λ' = (c − v)T"><line x1="40" y1="120" x2="690" y2="120" stroke="var(--line)" stroke-width="2"/><line x1="450" y1="70" x2="450" y2="170" stroke="var(--blue)" stroke-width="4" stroke-linecap="round"/><text x="450" y="62" font-size="13" fill="var(--blue)" text-anchor="middle" font-weight="700">crête émise à t = 0</text><line x1="210" y1="70" x2="210" y2="170" stroke="var(--blue)" stroke-width="4" stroke-linecap="round" opacity=".55"/><text x="210" y="62" font-size="13" fill="var(--blue)" text-anchor="middle" font-weight="700" opacity=".8">crête émise à t = T</text><circle cx="90" cy="120" r="11" fill="none" stroke="var(--rose)" stroke-width="2" stroke-dasharray="3 3"/><circle cx="210" cy="120" r="11" fill="var(--rose)"/><line x1="226" y1="120" x2="270" y2="120" stroke="var(--rose)" stroke-width="2.5"/><polygon points="276.0,120.0 267.0,124.5 267.0,115.5" fill="var(--rose)"/><text x="250" y="108" font-size="17" fill="var(--rose)" font-family="Georgia, serif" font-style="italic" font-weight="700">v</text><text x="90" y="154" font-size="12" fill="var(--rose)" text-anchor="middle">émetteur à t = 0</text><circle cx="650" cy="120" r="12" fill="var(--amber)"/><text x="650" y="154" font-size="12" fill="var(--amber)" text-anchor="middle" font-weight="700">récepteur</text><line x1="90" y1="160" x2="90" y2="218" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3"/><line x1="210" y1="172" x2="210" y2="218" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3"/><line x1="450" y1="172" x2="450" y2="218" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3"/><line x1="98.0" y1="172.0" x2="442.0" y2="172.0" stroke="var(--slate)" stroke-width="1.6"/><polygon points="450.0,172.0 441.0,176.5 441.0,167.5" fill="var(--slate)"/><polygon points="90.0,172.0 99.0,167.5 99.0,176.5" fill="var(--slate)"/><text x="270.0" y="166" font-size="15" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">cT = λ</text><line x1="98.0" y1="206.0" x2="202.0" y2="206.0" stroke="var(--rose)" stroke-width="1.8"/><polygon points="210.0,206.0 201.0,210.5 201.0,201.5" fill="var(--rose)"/><polygon points="90.0,206.0 99.0,201.5 99.0,210.5" fill="var(--rose)"/><text x="150.0" y="232" font-size="15" fill="var(--rose)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">vT</text><line x1="218.0" y1="206.0" x2="442.0" y2="206.0" stroke="var(--emerald)" stroke-width="2.4"/><polygon points="450.0,206.0 441.0,210.5 441.0,201.5" fill="var(--emerald)"/><polygon points="210.0,206.0 219.0,201.5 219.0,210.5" fill="var(--emerald)"/><text x="330.0" y="232" font-size="16" fill="var(--emerald)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">λ′ = (c − v)T</text></svg>
<p>L'émetteur produit une crête toutes les périodes $T = 1/f$. Pendant une période, la crête émise à $t = 0$ parcourt la distance $cT = \lambda$&nbsp;; pendant ce temps, l'émetteur, qui la suit, avance de $vT$. Quand il émet la crête suivante, les deux crêtes ne sont donc plus séparées de $\lambda$ mais de&nbsp;:</p>
<p class="nt-center">$\lambda' = cT - vT = (c - v)\,T$</p>
<p>Ces crêtes se propagent ensuite toutes à la célérité $c$ jusqu'au récepteur, qui les reçoit avec la période $T' = \dfrac{\lambda'}{c} = \dfrac{(c-v)\,T}{c}$, soit avec la fréquence&nbsp;:</p>
<p class="nt-center">$f' = \dfrac{1}{T'} = f\times\dfrac{c}{c-v}$</p>
<p>D'où le décalage&nbsp;: $\Delta f = f' - f = f\left(\dfrac{c}{c-v} - 1\right) = f\times\dfrac{v}{c-v}$.</p>
<p>Si l'émetteur s'éloigne, il «&nbsp;fuit&nbsp;» la crête précédente&nbsp;: $\lambda' = (c+v)\,T$, d'où $f' = f\times\dfrac{c}{c+v}$ et $\Delta f = f\left(\dfrac{c}{c+v} - 1\right) = -f\times\dfrac{v}{c+v}$.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">En longueur d'onde, et aux faibles vitesses</span></summary>
<div class="nt-d-body">
<p>En longueur d'onde, les deux formules deviennent&nbsp;: $\lambda' = \lambda\left(1 \pm \dfrac{v}{c}\right)$, avec le signe + quand l'émetteur s'éloigne et le signe − quand il se rapproche. Le décalage relatif vaut donc exactement $\dfrac{\Delta\lambda}{\lambda} = \pm\dfrac{v}{c}$.</p>
<p>Quand $v \ll c$, on peut négliger $v$ devant $c$ au dénominateur, et les deux formules deviennent&nbsp;: $\Delta f \approx \pm f\,\dfrac{v}{c}$.<br>
C'est presque toujours le cas en pratique&nbsp;: une voiture roule à moins d'un dixième de la vitesse du son, et une étoile se déplace à moins d'un millième de la vitesse de la lumière.</p>
<p>Pour la lumière, ces formules ne valent d'ailleurs qu'aux faibles vitesses&nbsp;: au-delà, il faut tenir compte de la relativité restreinte (hors programme).</p>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple&nbsp;: déterminer une vitesse</p>
<p>La sirène d'une ambulance émet un son de fréquence $f = \pu{680 Hz}$. Pendant qu'elle approche, un piéton perçoit un son de fréquence $\pu{720 Hz}$. Quelle est la vitesse de l'ambulance&nbsp;? (On prend $c = \pu{340 m*s-1}$.)</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p>L'ambulance se rapproche, donc $\Delta f = f\times\dfrac{v}{c-v}$ avec $\Delta f = 720 - 680 = \pu{40 Hz}$.</p>
<p>On isole $v$&nbsp;: $\Delta f\,(c - v) = f\,v \iff \Delta f\,c = (f + \Delta f)\,v \iff v = \dfrac{\Delta f\times c}{f + \Delta f}$.</p>
<p>Application numérique&nbsp;: $v = \dfrac{40\times 340}{720} = \pu{19 m*s-1}$, soit environ $\pu{68 km*h-1}$.</p>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-graduation-cap"></i>Ce que dit le programme</p>
<ul class="nt-facts">
<li>Décrire et interpréter qualitativement les observations correspondant à une manifestation de l'effet Doppler.</li>
<li>Établir l'expression du décalage Doppler dans le cas d'un observateur fixe, d'un émetteur mobile et dans une configuration à une dimension.</li>
<li>Exploiter l'expression du décalage Doppler dans des situations variées utilisant des ondes acoustiques ou des ondes électromagnétiques.</li>
<li>Exploiter l'expression du décalage Doppler en acoustique pour déterminer une vitesse.</li>
</ul>
</div>

## Applications {.nt-h2}

### Radars routiers {.nt-h3}

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-car-side"></i>Exemple</p>
<p>Un radar routier émet une onde électromagnétique (souvent de fréquence voisine de $\pu{24 GHz}$) vers les véhicules. L'onde réfléchie par un véhicule en mouvement revient avec une fréquence décalée par effet Doppler&nbsp;: le radar mesure ce décalage et en déduit la vitesse du véhicule.</p>
<p>Pour une voiture à $\pu{90 km*h-1}$, le décalage n'est que de quelques kilohertz, pour une onde de plusieurs dizaines de milliards de hertz&nbsp;!</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Le décalage doublé par la réflexion</span></summary>
<div class="nt-d-body">
<p>Lors d'une mesure par réflexion, l'effet Doppler intervient deux fois&nbsp;: la voiture reçoit l'onde en se déplaçant par rapport au radar (récepteur mobile), puis la renvoie en se déplaçant (émetteur mobile). Pour $v \ll c$, le décalage total vaut $\Delta f \approx 2f\,\dfrac{v}{c}$.</p>
<p>Avec $f = \pu{24,125 GHz}$ et $v = \pu{25 m*s-1}$ ($\pu{90 km*h-1}$)&nbsp;: $\Delta f \approx \dfrac{2\times 24{,}125\times 10^{9}\times 25}{3{,}00\times 10^{8}} \approx \pu{4,0 kHz}$. En pratique, le radar vise la route en biais et corrige sa mesure de l'angle entre son faisceau et la trajectoire.</p>
</div>
</details>

### Échographie Doppler {.nt-h3}

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-heart-pulse"></i>Exemple</p>
<p>Une sonde émet des ultrasons (de quelques mégahertz) dans le corps. Les globules rouges, en mouvement dans les vaisseaux sanguins, renvoient des ultrasons de fréquence décalée&nbsp;: on en déduit la vitesse et le sens de circulation du sang.</p>
<p>Pour des vitesses sanguines de quelques dizaines de centimètres par seconde, le décalage est de l'ordre du kilohertz, c'est-à-dire audible&nbsp;: les appareils le restituent d'ailleurs sous forme de son, le «&nbsp;souffle&nbsp;» caractéristique de cet examen.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Ce que permet de diagnostiquer l'échographie Doppler</span></summary>
<div class="nt-d-body">
<p>L'échographie Doppler est utilisée dans le diagnostic des atteintes des vaisseaux et du cœur&nbsp;:</p>
<ul class="nt-facts">
<li>cœur&nbsp;: cardiopathies congénitales, valvulopathies, péricardites&nbsp;;</li>
<li>artères&nbsp;: sténoses, thromboses (athérosclérose), anévrismes, claudication intermittente, ischémie aiguë&nbsp;;</li>
<li>veines&nbsp;: thromboses veineuses profondes, varices.</li>
</ul>
<p>C'est souvent un examen de première intention&nbsp;: il est relativement peu coûteux et très sensible, en particulier pour le diagnostic des thromboses veineuses profondes.</p>
</div>
</details>

### Radars météorologiques {.nt-h3}

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-cloud-showers-heavy"></i>Exemple</p>
<p>Un radar météorologique envoie des ondes radio qui se réfléchissent sur les gouttes de pluie ou les flocons. L'intensité de l'écho renseigne sur la quantité de précipitations, et son décalage Doppler sur leur vitesse vers le radar ou en s'éloignant de lui.</p>
<p>On peut ainsi suivre le déplacement des nuages d'orage, et repérer les zones où des précipitations proches s'approchent et s'éloignent à la fois du radar&nbsp;: c'est la signature d'une rotation, qui peut annoncer une tornade.</p>
</div>

### Astrophysique {.nt-h3}

<p class="nt-lead">Pour la lumière d'une étoile ou d'une galaxie, on mesure le décalage Doppler sur les <b>raies</b> de son spectre, dont on connaît la position exacte en laboratoire.</p>

<div class="nt-lab" id="lab-spectre">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Les raies de l'hydrogène se décalent</p>
<canvas style="height:178px;" aria-label="Spectre de référence de l'hydrogène et spectre décalé reçu d'une source en mouvement"></canvas>
<label class="nt-ctrl">Vitesse de la source&nbsp;: <b class="out-v"></b> (positive si elle s'éloigne)<input type="range" data-p="v" min="-30000" max="30000" step="500" value="12000"></label>
<div class="nt-read"><span>raie H<sub>α</sub> (656,3&nbsp;nm au repos)&nbsp;: <b class="out-l"></b></span><span>décalage&nbsp;: <b class="out-d"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-meteor"></i>Découverte de l'expansion de l'Univers</p>
<p>Découverte de l'expansion de l'univers (loi de Hubble-Lemaître, 1929)&nbsp;: plus une galaxie est lointaine, plus elle s'éloigne vite de nous.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi de Hubble-Lemaître</p>
<p class="nt-f-math">$$v=H_0\times d$$</p>
<div class="nt-f-units"><span>$v$&nbsp;: vitesse d'éloignement de la galaxie</span><span>$d$&nbsp;: distance de la galaxie</span><span>$H_0 \approx \pu{70 km*s-1*Mpc-1}$&nbsp;: constante de Hubble</span></div>
</div>

<p class="nt-cap">1&nbsp;Mpc (mégaparsec) vaut environ 3,3&nbsp;millions d'années-lumière. Une galaxie située à 100&nbsp;Mpc s'éloigne donc de nous à environ $\pu{7000 km*s-1}$&nbsp;: sa raie H<sub>α</sub> est observée vers 672&nbsp;nm.</p>

<div class="nt-lab" id="lab-expansion">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Toutes les galaxies s'éloignent… de toutes les autres</p>
<div class="nt-lab-pair">
<figure><canvas class="sky" style="height:260px; background:#0B1024; cursor:pointer;" aria-label="Galaxies qui s'éloignent les unes des autres ; cliquer sur une galaxie pour se placer sur elle"></canvas><figcaption>Cliquez sur une autre galaxie pour vous y installer</figcaption></figure>
<figure><canvas class="graph" style="height:260px; background:#fff;" aria-label="Vitesse d'éloignement des autres galaxies en fonction de leur distance"></canvas><figcaption>Vitesse d'éloignement en fonction de la distance</figcaption></figure>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg">Les traits roses représentent les vitesses d'éloignement, proportionnelles aux distances&nbsp;: c'est la loi de Hubble-Lemaître. Quelle que soit la galaxie choisie, on observe la même chose&nbsp;: il n'y a pas de centre de l'expansion, c'est l'espace entre les galaxies qui grandit.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Hubble, Lemaître, et un décalage «&nbsp;pas tout à fait&nbsp;» Doppler</span></summary>
<div class="nt-d-body">
<p>Georges Lemaître avait prédit dès 1927 que les galaxies devaient s'éloigner à une vitesse proportionnelle à leur distance, et en avait donné une première estimation. Edwin Hubble a établi cette relation à partir de ses observations en 1929. Depuis 2018, l'Union astronomique internationale recommande de parler de loi de Hubble-Lemaître.</p>
<p>Pour les galaxies proches, interpréter leur décalage vers le rouge comme un effet Doppler donne le bon résultat. Pour les galaxies très lointaines, c'est plutôt l'expansion de l'espace elle-même qui «&nbsp;étire&nbsp;» la longueur d'onde de la lumière pendant son long voyage&nbsp;: on parle de décalage vers le rouge cosmologique.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La «&nbsp;tension de Hubble&nbsp;», une des grandes crises de la physique actuelle</span></summary>
<div class="nt-d-body">
<p>On sait mesurer $H_0$ de deux façons indépendantes. La première exploite le fond diffus cosmologique (voir plus bas) et un modèle de l'histoire de l'Univers. La seconde mesure directement les distances et les vitesses de galaxies proches, à l'aide d'étoiles variables (céphéides) et de supernovæ. Au début des années 2020, les deux méthodes donnent des valeurs incompatibles&nbsp;:</p>
<svg class="nt-svg nt-svg-m" viewBox="0 0 560 220" role="img" aria-label="Deux mesures incompatibles de la constante de Hubble : 67,4 ± 0,5 et 73,0 ± 1,0 km/s/Mpc"><rect x="186.0" y="20" width="40.0" height="150" fill="var(--blue)" opacity=".12"/><rect x="390.0" y="20" width="80.0" height="150" fill="var(--rose)" opacity=".12"/><line x1="70" y1="170" x2="550" y2="170" stroke="var(--ink)" stroke-width="1.5"/><line x1="70" y1="170" x2="70" y2="176" stroke="var(--ink)"/><text x="70" y="192" font-size="12" text-anchor="middle" fill="var(--ink)">64</text><line x1="150" y1="170" x2="150" y2="176" stroke="var(--ink)"/><text x="150" y="192" font-size="12" text-anchor="middle" fill="var(--ink)">66</text><line x1="230" y1="170" x2="230" y2="176" stroke="var(--ink)"/><text x="230" y="192" font-size="12" text-anchor="middle" fill="var(--ink)">68</text><line x1="310" y1="170" x2="310" y2="176" stroke="var(--ink)"/><text x="310" y="192" font-size="12" text-anchor="middle" fill="var(--ink)">70</text><line x1="390" y1="170" x2="390" y2="176" stroke="var(--ink)"/><text x="390" y="192" font-size="12" text-anchor="middle" fill="var(--ink)">72</text><line x1="470" y1="170" x2="470" y2="176" stroke="var(--ink)"/><text x="470" y="192" font-size="12" text-anchor="middle" fill="var(--ink)">74</text><line x1="550" y1="170" x2="550" y2="176" stroke="var(--ink)"/><text x="550" y="192" font-size="12" text-anchor="middle" fill="var(--ink)">76</text><text x="310" y="212" font-size="12" text-anchor="middle" fill="var(--slate)">H₀ (km·s⁻¹·Mpc⁻¹)</text><line x1="186.0" y1="70" x2="226.0" y2="70" stroke="var(--blue)" stroke-width="2.5"/><line x1="186.0" y1="63" x2="186.0" y2="77" stroke="var(--blue)" stroke-width="2.5"/><line x1="226.0" y1="63" x2="226.0" y2="77" stroke="var(--blue)" stroke-width="2.5"/><circle cx="206.0" cy="70" r="6" fill="var(--blue)"/><text x="238.0" y="75" font-size="13" text-anchor="start" fill="var(--blue)" font-weight="700">fond diffus cosmologique (Planck)</text><line x1="390.0" y1="125" x2="470.0" y2="125" stroke="var(--rose)" stroke-width="2.5"/><line x1="390.0" y1="118" x2="390.0" y2="132" stroke="var(--rose)" stroke-width="2.5"/><line x1="470.0" y1="118" x2="470.0" y2="132" stroke="var(--rose)" stroke-width="2.5"/><circle cx="430.0" cy="125" r="6" fill="var(--rose)"/><text x="378.0" y="130" font-size="13" text-anchor="end" fill="var(--rose)" font-weight="700">céphéides et supernovæ (SH0ES)</text></svg>
<p>L'écart dépasse cinq fois les incertitudes&nbsp;: en physique, on parle de «&nbsp;tension&nbsp;». Soit l'une des mesures comporte une erreur systématique encore inconnue, soit notre modèle de l'Univers est incomplet. La question est toujours ouverte.</p>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-earth-europe"></i>Détection d'exoplanètes</p>
<p>Une planète et son étoile tournent toutes deux autour de leur centre de masse commun. L'étoile décrit donc un petit cercle&nbsp;: elle s'approche puis s'éloigne périodiquement de nous, et les raies de son spectre oscillent autour de leur position moyenne. C'est ainsi qu'a été découverte en 1995, à l'Observatoire de Haute-Provence, la première planète en orbite autour d'une étoile semblable au Soleil, 51&nbsp;Pegasi&nbsp;b (prix Nobel 2019 pour Michel Mayor et Didier Queloz).</p>
</div>

<div class="nt-lab" id="lab-exo">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">La danse d'une étoile autour de son centre de masse</p>
<div class="nt-lab-pair">
<figure><canvas class="orbit" style="height:230px; background:#0B1024;" aria-label="Vue de dessus : la planète et l'étoile tournent autour de leur centre de masse"></canvas><figcaption>Vue de dessus (la croix marque le centre de masse&nbsp;; mouvement de l'étoile exagéré)</figcaption></figure>
<figure><canvas class="graph" style="height:230px; background:#fff;" aria-label="Vitesse radiale de l'étoile au cours du temps"></canvas><figcaption>Vitesse de l'étoile le long de la ligne de visée (positive si elle s'éloigne)</figcaption></figure>
</div>
<canvas class="line" style="height:34px;" aria-label="Raie spectrale de l'étoile qui oscille autour de sa position moyenne"></canvas>
<p class="nt-note nt-center">Raie H<sub>α</sub> de l'étoile, avec un décalage très fortement exagéré (le trait blanc marque sa position au repos).</p>
<div class="nt-ctrls">
<label class="nt-ctrl">Masse de la planète&nbsp;: <b class="out-m"></b><input type="range" data-p="m" min="0" max="100" step="0.5" value="66.8"></label>
<label class="nt-ctrl">Période de révolution&nbsp;: <b class="out-P"></b><input type="range" data-p="P" min="0" max="100" step="0.5" value="17"></label>
</div>
<div class="nt-read"><span>vitesse maximale de l'étoile&nbsp;: <b class="out-K"></b></span><span>décalage maximal de H<sub>α</sub>&nbsp;: <b class="out-dl"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-preset="0.47,4.23">51 Pegasi b</button>
<button type="button" class="nt-btn" data-preset="1,4333">Jupiter</button>
<button type="button" class="nt-btn" data-preset="0.00315,365.25">Terre</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-msg">Pour une étoile semblable au Soleil. Jupiter fait osciller le Soleil à environ 13&nbsp;m/s, ce qui décale ses raies d'environ trois cent-millièmes de nanomètre&nbsp;; la Terre ne le fait osciller qu'à 9&nbsp;cm/s, un effet encore 150 fois plus petit, à la limite des meilleurs spectrographes actuels.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-satellite-dish"></i>Anisotropie dipolaire du CMB</p>
<p>Le fond diffus cosmologique (CMB, pour <i>cosmic microwave background</i>) est un rayonnement micro-onde qui baigne tout l'Univers, émis environ 380&nbsp;000 ans après le Big Bang. Il nous parvient de toutes les directions, avec un spectre dont l'intensité est maximale vers 160&nbsp;GHz.</p>
<p>Pourtant, dans une direction du ciel, toutes ses fréquences sont très légèrement plus élevées que la moyenne, et dans la direction opposée, légèrement plus basses&nbsp;: c'est l'effet Doppler dû à notre propre mouvement à travers ce rayonnement. Cette anisotropie dipolaire permet de savoir dans quelle direction et à quelle vitesse nous nous déplaçons par rapport à lui&nbsp;: environ 370&nbsp;km/s pour le Soleil, vers la constellation de la Coupe.</p>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 560 300" role="img" aria-label="Carte de tout le ciel : les fréquences du fond diffus cosmologique sont légèrement augmentées dans la direction de notre mouvement et légèrement diminuées dans la direction opposée"><defs><linearGradient id="gDip" x1="0" x2="1"><stop offset="0" stop-color="#3B82F6"/><stop offset=".5" stop-color="#F1F5F9"/><stop offset="1" stop-color="#EF4444"/></linearGradient></defs><ellipse cx="280" cy="140" rx="250" ry="125" fill="url(#gDip)" stroke="var(--slate)" stroke-width="1.5"/><ellipse cx="280" cy="140" rx="125" ry="125" fill="none" stroke="var(--slate)" stroke-opacity=".25"/><line x1="30" y1="140" x2="530" y2="140" stroke="var(--slate)" stroke-opacity=".25"/><circle cx="110" cy="140" r="7" fill="#fff" stroke="var(--ink)" stroke-width="2"/><text x="110" y="120" font-size="14" text-anchor="middle" font-weight="700" fill="#fff">Δf &gt; 0</text><text x="110" y="170" font-size="12" text-anchor="middle" font-weight="700" fill="#fff">+ 0,12 %</text><circle cx="450" cy="140" r="7" fill="#fff" stroke="var(--ink)" stroke-width="2"/><text x="450" y="120" font-size="14" text-anchor="middle" font-weight="700" fill="#fff">Δf &lt; 0</text><text x="450" y="170" font-size="12" text-anchor="middle" font-weight="700" fill="#fff">− 0,12 %</text><text x="160" y="290" font-size="13" text-anchor="middle" fill="#1D4ED8" font-weight="700">direction de notre mouvement</text><text x="420" y="290" font-size="13" text-anchor="middle" fill="#B91C1C" font-weight="700">direction opposée</text></svg>

<p class="nt-cap">Décalage Doppler des fréquences du fond diffus cosmologique dû à notre mouvement (carte de tout le ciel). Comme $v \ll c$, le décalage relatif vaut $\dfrac{\Delta f}{f} \approx \pm\dfrac{v}{c} = \pm\dfrac{370}{300\,000} \approx \pm 1{,}2\times 10^{-3}$&nbsp;: au maximum du spectre, vers 160&nbsp;GHz, cela représente un décalage d'environ 0,2&nbsp;GHz.</p>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Le CMB définit un référentiel privilégié&nbsp;: celui dans lequel ce rayonnement est le même dans toutes les directions. Ce n'est pas pour autant un référentiel «&nbsp;absolu&nbsp;» au sens où les lois de la physique y seraient différentes&nbsp;: la relativité reste valable. C'est simplement le référentiel au repos par rapport au contenu moyen de l'Univers.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La découverte du CMB par Penzias et Wilson</span></summary>
<div class="nt-d-body">
<p>En 1964, Arno Penzias et Robert Wilson, des laboratoires Bell, utilisent une grande antenne cornet à Holmdel (New Jersey), construite pour les premières télécommunications par satellite. Ils l'écoutent à une fréquence de 4,08&nbsp;GHz (longueur d'onde de 7,35&nbsp;cm). Après avoir éliminé toutes les sources connues (atmosphère, instrument, sol, Galaxie… et même des fientes de pigeons dans le cornet&nbsp;!), il leur reste un faible bruit radio, identique dans toutes les directions, de jour comme de nuit et en toute saison.</p>
<p><b>Pourquoi une découverte à 4,08&nbsp;GHz, si loin du maximum du spectre (vers 160&nbsp;GHz)&nbsp;?</b> D'abord parce que Penzias et Wilson ne cherchaient pas le CMB&nbsp;: la fréquence leur était imposée par leur antenne, conçue pour les télécommunications, mais qui était alors le récepteur radio le plus sensible au monde. Ensuite parce que le spectre du CMB est très étalé&nbsp;: il couvre toutes les fréquences, des ondes radio à l'infrarouge lointain. À 4,08&nbsp;GHz, son intensité est environ 300 fois plus faible qu'à son maximum, mais pas nulle&nbsp;: c'est pour cela qu'ils n'ont perçu qu'un faible bruit.</p>
<p>Enfin, mesurer le CMB près de son maximum depuis le sol est très difficile&nbsp;: dans cette gamme de fréquences, la vapeur d'eau et le dioxygène de l'atmosphère absorbent et émettent eux-mêmes beaucoup de rayonnement. Il a fallu attendre le satellite COBE, en 1990, pour mesurer son spectre complet au-dessus de l'atmosphère (prix Nobel 2006 pour John Mather et George Smoot).</p>
<p>Au même moment, l'équipe de Robert Dicke à Princeton s'apprêtait à chercher ce rayonnement, prédit par la théorie du Big Bang. En apprenant la nouvelle, Dicke aurait lancé à ses collègues&nbsp;: «&nbsp;Les gars, on s'est fait doubler&nbsp;!&nbsp;» Penzias et Wilson ont reçu le prix Nobel de physique en 1978.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Fréquence et température&nbsp;: le CMB est un corps noir</span></summary>
<div class="nt-d-body">
<p><b>Un spectre de corps noir.</b> Le spectre du fond diffus cosmologique est celui d'un corps noir, comme celui d'un objet chaud (une étoile, un filament de lampe), mais extrêmement froid&nbsp;: sa température vaut 2,725&nbsp;K. Pour un corps noir, la forme du spectre ne dépend que de la température, et la fréquence du maximum lui est proportionnelle&nbsp;: plus le corps est chaud, plus son spectre est décalé vers les hautes fréquences.</p>
<p><b>Le lien avec l'effet Doppler.</b> Dans la direction de notre mouvement, l'effet Doppler multiplie toutes les fréquences reçues par un même facteur, légèrement supérieur à 1. Le spectre garde donc exactement sa forme de corps noir, mais il est décalé vers les hautes fréquences&nbsp;: c'est celui d'un corps noir un peu plus chaud. Dans la direction opposée ($\Delta f &lt; 0$), il ressemble à celui d'un corps noir un peu plus froid.</p>
<p>C'est pourquoi les cartes du CMB sont graduées en températures&nbsp;: un décalage relatif de $\pm 1{,}2\times 10^{-3}$ sur les fréquences correspond à un écart de température de $\pm 1{,}2\times 10^{-3}\times \pu{2,725 K} \approx \pm 3{,}4$&nbsp;millièmes de kelvin. Une fois ce dipôle retiré, le CMB est uniforme sur tout le ciel à environ 1 partie sur 25&nbsp;000 près&nbsp;: ses minuscules fluctuations restantes sont les germes des futures galaxies.</p>
<p><b>Un piège classique.</b> Quand on trace l'intensité en fonction de la longueur d'onde, le maximum est vers 1&nbsp;mm&nbsp;; en fonction de la fréquence, il est vers 160&nbsp;GHz. Or $c/(\pu{1 mm}) \approx \pu{300 GHz}$&nbsp;: on ne passe pas d'un maximum à l'autre avec $f = c/\lambda$, car la répartition de l'énergie «&nbsp;par nanomètre&nbsp;» et «&nbsp;par hertz&nbsp;» n'est pas la même.</p>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-circle-nodes"></i>Anomalie des courbes de rotation des galaxies</p>
<p>En mesurant le décalage Doppler de différents nuages d'hydrogène dans la galaxie d'Andromède (puis dans d'autres galaxies), Vera Rubin montre à la fin des années 60 que les objets éloignés du centre galactique ne tournent pas à la vitesse prévue par Kepler.</p>
<p>D'un côté de la galaxie, les nuages s'approchent de nous&nbsp;; de l'autre, ils s'éloignent&nbsp;: le décalage Doppler donne leur vitesse de rotation à chaque distance du centre.</p>
</div>

<div class="nt-lab" id="lab-rotation">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Une galaxie qui tourne trop vite</p>
<div class="nt-lab-pair">
<figure><canvas class="disk" style="height:250px; background:#0B1024;" aria-label="Galaxie spirale vue de face en rotation"></canvas><figcaption>Galaxie vue de face</figcaption></figure>
<figure><canvas class="graph" style="height:250px; background:#fff;" aria-label="Vitesse de rotation en fonction de la distance au centre"></canvas><figcaption>Courbe de rotation&nbsp;: prévision (pointillés roses) et mesures (points)</figcaption></figure>
</div>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="halo"> Ajouter un halo de matière noire</label>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Courbes d'allure typique pour une grande galaxie spirale (1&nbsp;kpc ≈ 3&nbsp;260 années-lumière).</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Une explication populaire parmi les astrophysiciens serait la présence d'un <span class="imp nt-hole">halo de matière noire</span>.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les nuages d'hydrogène d'Andromède, et les autres pistes</span></summary>
<div class="nt-d-body">
<p>Les nuages observés par Vera Rubin et Kent Ford sont des régions H II&nbsp;: de l'hydrogène ionisé par le rayonnement ultraviolet d'étoiles très chaudes. Ils émettent la raie H<sub>α</sub>, ce qui permet de mesurer leur décalage Doppler un par un.</p>
<p>La matière noire n'a jamais été détectée directement&nbsp;: on ne connaît que ses effets gravitationnels. Certains physiciens explorent une autre piste, qui consiste à modifier les lois de la gravitation aux très faibles accélérations (théorie MOND). La question reste débattue.</p>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function sci(x, nd) {
    if (x === 0) { return '0'; }
    var s = x < 0 ? '\u2212' : ''; x = Math.abs(x);
    var n = Math.floor(Math.log10(x) + 1e-9), a = x / Math.pow(10, n), t = a.toFixed(nd);
    if (parseFloat(t) >= 10) { n += 1; t = (a / 10).toFixed(nd); }
    return s + t.replace('.', ',') + ' \u00d7 10<sup>' + String(n).replace('-', '\u2212') + '</sup>';
  }
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
  function $(root, sel) { return root.querySelector(sel); }
  function rng(seed) {
    return function () {
      seed |= 0; seed = seed + 0x6D2B79F5 | 0;
      var q = Math.imul(seed ^ seed >>> 15, 1 | seed);
      q = q + Math.imul(q ^ q >>> 7, 61 | q) ^ q;
      return ((q ^ q >>> 14) >>> 0) / 4294967296;
    };
  }
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
    return [Math.round(255 * Math.pow(r * f, 0.8)), Math.round(255 * Math.pow(g * f, 0.8)), Math.round(255 * Math.pow(b * f, 0.8))];
  }
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function audioCtx() { var C = window.AudioContext || window.webkitAudioContext; return C ? new C() : null; }
  /* ================= 1. Le passage d'une voiture ================= */
  (function () {
    var root = document.getElementById('lab-passage');
    if (!root) { return; }
    var cvS = $(root, 'canvas.scene'), cvG = $(root, 'canvas.graph'), rV = $(root, '[data-p="v"]'), cbS = $(root, '[data-p="son"]');
    var btn = $(root, '[data-act="go"]'), oV = $(root, '.out-v'), oF = $(root, '.out-f'), oD = $(root, '.out-d');
    var F0 = 500, C = 340, B = 12, XL = 100, LEN = 200, S1, S2, x = 10, running = false, last = null, AC = null, osc = null, gn = null;
    function v() { return parseFloat(rV.value) / 3.6; }
    function fr_(xc) { var dx = XL - xc, d = Math.hypot(dx, B), vr = v() * dx / d; return F0 * C / (C - vr); }
    function drawScene() {
      var c = S1.ctx, w = S1.w, h = S1.h, k = w / LEN, yr = 46;
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#CBD5E1'; c.fillRect(0, yr - 22, w, 44);
      c.strokeStyle = '#fff'; c.setLineDash([14, 12]); c.lineWidth = 2; c.beginPath(); c.moveTo(0, yr); c.lineTo(w, yr); c.stroke(); c.setLineDash([]);
      var xl = XL * k, yl = yr + B * k * 0.9;
      c.fillStyle = col('--amber'); c.beginPath(); c.arc(xl, Math.min(h - 18, yl), 9, 0, 2 * Math.PI); c.fill();
      c.font = '600 12px system-ui, sans-serif'; c.textAlign = 'center'; c.fillText('vous', xl, Math.min(h - 18, yl) + 24);
      var xc = x * k;
      c.strokeStyle = col('--muted'); c.setLineDash([4, 4]); c.lineWidth = 1;
      c.beginPath(); c.moveTo(xc, yr); c.lineTo(xl, Math.min(h - 18, yl)); c.stroke(); c.setLineDash([]);
      c.fillStyle = col('--blue'); c.beginPath();
      if (c.roundRect) { c.roundRect(xc - 22, yr - 12, 44, 24, 7); } else { c.rect(xc - 22, yr - 12, 44, 24); }
      c.fill();
      c.fillStyle = '#BFDBFE'; c.fillRect(xc + 4, yr - 8, 12, 16);
    }
    var curve = [];
    function compute() {
      curve = [];
      for (var i = 0; i <= 300; i++) { var xc = i / 300 * LEN; curve.push([xc, fr_(xc)]); }
    }
    function drawGraph() {
      var c = S2.ctx, w = S2.w, h = S2.h, vv = v(), fa = F0 * C / (C - vv), fe = F0 * C / (C + vv);
      var fmin = F0 * C / (C + 42), fmax = F0 * C / (C - 42), L = 50, R = w - 10, T = 12, Bt = h - 26;
      function Y(f) { return Bt - (f - fmin) / (fmax - fmin) * (Bt - T); }
      function X(xc) { return L + xc / LEN * (R - L); }
      c.clearRect(0, 0, w, h);
      c.font = '11px system-ui, sans-serif'; c.fillStyle = col('--muted'); c.textAlign = 'right';
      [fa, F0, fe].forEach(function (f, i) {
        c.strokeStyle = i === 1 ? col('--line') : (i === 0 ? col('--blue') : col('--rose'));
        c.setLineDash(i === 1 ? [] : [5, 4]); c.lineWidth = 1;
        c.beginPath(); c.moveTo(L, Y(f)); c.lineTo(R, Y(f)); c.stroke();
        c.fillStyle = i === 1 ? col('--muted') : (i === 0 ? col('--blue') : col('--rose'));
        c.fillText(Math.round(f) + ' Hz', L - 4, Y(f) + 4);
      });
      c.setLineDash([]);
      c.strokeStyle = col('--ink'); c.lineWidth = 2.4; c.beginPath();
      curve.forEach(function (p, i) { if (i === 0) { c.moveTo(X(p[0]), Y(p[1])); } else { c.lineTo(X(p[0]), Y(p[1])); } });
      c.stroke();
      var fn = fr_(x);
      c.fillStyle = col('--amber'); c.beginPath(); c.arc(X(x), Y(fn), 6, 0, 2 * Math.PI); c.fill();
      c.fillStyle = col('--muted'); c.textAlign = 'center';
      c.fillText('position de la voiture le long de la route \u2192', (L + R) / 2, h - 6);
      oF.textContent = Math.round(fn) + ' Hz'; oD.textContent = (fn >= F0 ? '+ ' : '\u2212 ') + Math.round(Math.abs(fn - F0)) + ' Hz';
    }
    function sound(on) {
      if (on) {
        AC = AC || audioCtx(); if (!AC) { return; }
        if (AC.state === 'suspended') { AC.resume(); }
        gn = AC.createGain(); gn.gain.value = 0; gn.connect(AC.destination);
        osc = AC.createOscillator(); osc.type = 'triangle'; osc.frequency.value = fr_(x); osc.connect(gn); osc.start();
      } else if (osc) {
        var o = osc; gn.gain.setTargetAtTime(0, AC.currentTime, 0.05); setTimeout(function () { try { o.stop(); } catch (e) {} }, 300); osc = null;
      }
    }
    function step(ts) {
      if (!running) { return; }
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      x += v() * dt;
      if (osc) {
        var d = Math.hypot(XL - x, B);
        osc.frequency.setTargetAtTime(fr_(x), AC.currentTime, 0.02);
        gn.gain.setTargetAtTime(Math.min(0.3, 3 / d), AC.currentTime, 0.05);
      }
      drawScene(); drawGraph();
      if (x >= LEN - 5) { running = false; sound(false); btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Relancer le passage'; return; }
      requestAnimationFrame(step);
    }
    btn.addEventListener('click', function () {
      if (running) { running = false; sound(false); btn.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Lancer le passage'; return; }
      if (x >= LEN - 5) { x = 10; }
      running = true; last = null;
      if (cbS.checked) { sound(true); }
      btn.innerHTML = '<i class="fa-solid fa-stop"></i>&nbsp; Arrêter';
      requestAnimationFrame(step);
    });
    rV.addEventListener('input', function () { oV.textContent = rV.value + ' km/h'; compute(); drawScene(); drawGraph(); });
    document.addEventListener('visibilitychange', function () { if (document.hidden && osc) { sound(false); } });
    function setup() { S1 = canvasCtx(cvS); S2 = canvasCtx(cvG); oV.textContent = rV.value + ' km/h'; compute(); drawScene(); drawGraph(); }
    setup(); onResize(setup);
  })();
  /* ================= 2. Fronts d'onde d'un émetteur en mouvement ================= */
  (function () {
    var root = document.getElementById('lab-fronts');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rB = $(root, '[data-p="beta"]'), btn = $(root, '[data-act="play"]');
    var oB = $(root, '.out-b'), oA = $(root, '.out-a'), oR = $(root, '.out-r'), oFA = $(root, '.out-fa'), oFR = $(root, '.out-fr');
    var S, playing = !RM, visible = true, t = 0, last = null, CPX = 90, T = 0.5;
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, yc = h / 2, b = parseFloat(rB.value), v = b * CPX, lam = CPX * T;
      c.clearRect(0, 0, w, h);
      var span = 0.55 * w, xs = b < 0.01 ? w / 2 : 0.22 * w + ((v * t) % span);
      c.strokeStyle = col('--line'); c.lineWidth = 1; c.beginPath(); c.moveTo(0, yc); c.lineTo(w, yc); c.stroke();
      var phase = t % T, crestsR = [], crestsL = [];
      for (var n = 0; n < 40; n++) {
        var age = phase + n * T, r = CPX * age, cx = xs - v * age;
        if (r > 1.6 * w) { break; }
        c.strokeStyle = col('--blue'); c.globalAlpha = Math.max(0.15, 1 - age / 9); c.lineWidth = 2;
        c.beginPath(); c.arc(cx, yc, r, 0, 2 * Math.PI); c.stroke();
        crestsR.push(cx + r); crestsL.push(cx - r);
      }
      c.globalAlpha = 1;
      /* récepteurs */
      var xA = w - 26, xR = 26;
      [[xA, col('--blue'), 'A'], [xR, col('--rose'), 'B']].forEach(function (o) {
        c.fillStyle = o[1]; c.beginPath(); c.arc(o[0], yc, 9, 0, 2 * Math.PI); c.fill();
        c.fillStyle = '#fff'; c.font = '700 11px system-ui, sans-serif'; c.textAlign = 'center'; c.fillText(o[2], o[0], yc + 4);
      });
      /* émetteur */
      c.fillStyle = col('--amber'); c.beginPath(); c.arc(xs, yc, 8, 0, 2 * Math.PI); c.fill();
      if (b >= 0.01) {
        c.strokeStyle = col('--amber'); c.lineWidth = 2.5; c.beginPath(); c.moveTo(xs + 12, yc); c.lineTo(xs + 36, yc); c.stroke();
        c.beginPath(); c.moveTo(xs + 42, yc); c.lineTo(xs + 33, yc - 5); c.lineTo(xs + 33, yc + 5); c.closePath(); c.fillStyle = col('--amber'); c.fill();
      }
      /* écart entre deux crêtes devant et derrière */
      c.font = '700 12px system-ui, sans-serif';
      function mark(a, bb, y, color, label) {
        if (a == null || bb == null) { return; }
        c.strokeStyle = color; c.fillStyle = color; c.lineWidth = 2;
        c.beginPath(); c.moveTo(a, y); c.lineTo(bb, y); c.moveTo(a, y - 5); c.lineTo(a, y + 5); c.moveTo(bb, y - 5); c.lineTo(bb, y + 5); c.stroke();
        c.textAlign = 'center'; c.fillText(label, (a + bb) / 2, y - 8);
      }
      var aR = crestsR.filter(function (q) { return q > xs + 4 && q < w - 40; }).sort(function (p, q) { return p - q; });
      var aL = crestsL.filter(function (q) { return q < xs - 4 && q > 40; }).sort(function (p, q) { return q - p; });
      /* on mesure l'écart entre les deux crêtes les plus proches de chaque récepteur */
      if (aR.length >= 2) { mark(aR[aR.length - 2], aR[aR.length - 1], yc + 46, col('--blue'), '\u03bb devant'); }
      if (aL.length >= 2) { mark(aL[aL.length - 1], aL[aL.length - 2], yc + 46, col('--rose'), '\u03bb derrière'); }
      oB.textContent = fr(b, 2) + ' c  (soit ' + Math.round(b * 340) + ' m/s pour le son dans l\u2019air)';
      oA.textContent = fr(1 - b, 2) + ' \u03bb'; oR.textContent = fr(1 + b, 2) + ' \u03bb';
      oFA.textContent = fr(1 / (1 - b), 2) + ' f'; oFR.textContent = fr(1 / (1 + b), 2) + ' f';
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    rB.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (vv) { visible = vv; });
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 3. Décalage des raies d'un spectre ================= */
  (function () {
    var root = document.getElementById('lab-spectre');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rV = $(root, '[data-p="v"]'), oV = $(root, '.out-v'), oL = $(root, '.out-l'), oD = $(root, '.out-d'), msg = $(root, '.nt-msg'), S;
    var LINES = [656.3, 486.1, 434.0, 410.2], LMIN = 380, LMAX = 750, CL = 299792;
    function draw() {
      var v = parseFloat(rV.value), c = S.ctx, w = S.w, h = S.h, k = 1 + v / CL;
      function X(l) { return (l - LMIN) / (LMAX - LMIN) * w; }
      c.clearRect(0, 0, w, h);
      var bands = [[22, 46, 'spectre de référence (laboratoire)', 1], [104, 46, 'spectre reçu de la source', k]];
      bands.forEach(function (bd) {
        for (var px = 0; px < w; px++) {
          var rgb = lambdaRGB(LMIN + px / w * (LMAX - LMIN));
          c.fillStyle = 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')'; c.fillRect(px, bd[0], 1, bd[1]);
        }
        c.fillStyle = '#111';
        LINES.forEach(function (l) { var xx = X(l * bd[3]); if (xx > 0 && xx < w) { c.fillRect(xx - 1.5, bd[0], 3, bd[1]); } });
        c.fillStyle = col('--ink'); c.font = '600 12px system-ui, sans-serif'; c.textAlign = 'left'; c.fillText(bd[2], 2, bd[0] - 6);
      });
      c.strokeStyle = col('--muted'); c.setLineDash([3, 3]); c.lineWidth = 1;
      LINES.forEach(function (l) { var a = X(l), b = X(l * k); c.beginPath(); c.moveTo(a, 68); c.lineTo(b, 104); c.stroke(); });
      c.setLineDash([]);
      c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
      [400, 450, 500, 550, 600, 650, 700, 750].forEach(function (l) { c.fillText(l + ' nm', Math.min(w - 22, Math.max(20, X(l))), h - 4); });
      oV.textContent = (v > 0 ? '+ ' : (v < 0 ? '\u2212 ' : '')) + Math.abs(v).toLocaleString('fr-FR') + ' km/s';
      oL.textContent = fr(656.3 * k, 1) + ' nm'; oD.textContent = (v >= 0 ? '+ ' : '\u2212 ') + fr(Math.abs(656.3 * k - 656.3), 1) + ' nm';
      msg.textContent = v > 0 ? 'La source s\u2019éloigne : les raies sont décalées vers les grandes longueurs d\u2019onde, c\u2019est le décalage vers le rouge.' :
        (v < 0 ? 'La source se rapproche : les raies sont décalées vers les courtes longueurs d\u2019onde, c\u2019est le décalage vers le bleu.' : 'La source est immobile par rapport à nous : aucun décalage.');
    }
    rV.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 4. Un Univers en expansion ================= */
  (function () {
    var root = document.getElementById('lab-expansion');
    if (!root) { return; }
    var cv = $(root, 'canvas.sky'), cvG = $(root, 'canvas.graph'), btn = $(root, '[data-act="play"]');
    var S, SG, playing = !RM, visible = true, t = 0, last = null, obs = 0, R = rng(42), GAL = [];
    for (var i = 0; i < 46; i++) {
      var a = R() * 2 * Math.PI, r = Math.sqrt(R()) * 0.95;
      GAL.push({ x: r * Math.cos(a), y: r * Math.sin(a) * 0.62, ang: R() * Math.PI, s: 0.6 + R() * 0.8 });
    }
    GAL[0].x = 0; GAL[0].y = 0;
    var PERIOD = 7, AMAX = 1.7;
    function scale() { return 1 + (AMAX - 1) * ((t % PERIOD) / PERIOD); }
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, a = scale(), k = Math.min(w, h / 0.62) * 0.47, o = GAL[obs];
      c.fillStyle = '#0B1024'; c.fillRect(0, 0, w, h);
      var pts = [];
      GAL.forEach(function (g, j) {
        var dx = (g.x - o.x) * a, dy = (g.y - o.y) * a, X = w / 2 + dx * k, Y = h / 2 + dy * k;
        pts.push([dx, dy]);
        if (j !== obs && X > -20 && X < w + 20 && Y > -20 && Y < h + 20) {
          var L = 0.55 * Math.hypot(dx, dy), n = Math.hypot(dx, dy) || 1;
          c.strokeStyle = 'rgba(252,165,165,.75)'; c.lineWidth = 1.5;
          c.beginPath(); c.moveTo(X, Y); c.lineTo(X + dx / n * L * k * 0.5, Y + dy / n * L * k * 0.5); c.stroke();
        }
        c.save(); c.translate(X, Y); c.rotate(g.ang);
        c.fillStyle = j === obs ? '#FBBF24' : 'rgba(219,234,254,.9)';
        c.beginPath(); c.ellipse(0, 0, 6 * g.s, 2.6 * g.s, 0, 0, 2 * Math.PI); c.fill(); c.restore();
      });
      c.fillStyle = '#FBBF24'; c.font = '700 12px system-ui, sans-serif'; c.textAlign = 'center';
      c.fillText('notre galaxie', w / 2, h / 2 - 12);
      /* loi de Hubble vue depuis la galaxie choisie */
      var g = SG.ctx, W = SG.w, H = SG.h, L = 36, B = H - 24, T = 10, Rr = W - 10, DM = 1.2 * AMAX, VM = 0.55 * DM;
      g.clearRect(0, 0, W, H);
      g.strokeStyle = col('--line'); g.beginPath(); g.moveTo(L, T); g.lineTo(L, B); g.lineTo(Rr, B); g.stroke();
      g.fillStyle = col('--muted'); g.font = '11px system-ui, sans-serif'; g.textAlign = 'center';
      g.fillText('distance d', (L + Rr) / 2, H - 6);
      g.save(); g.translate(12, (T + B) / 2); g.rotate(-Math.PI / 2); g.fillText('vitesse v', 0, 0); g.restore();
      g.strokeStyle = col('--rose'); g.setLineDash([5, 4]); g.beginPath(); g.moveTo(L, B); g.lineTo(Rr, T); g.stroke(); g.setLineDash([]);
      g.fillStyle = col('--blue');
      pts.forEach(function (p, j) {
        if (j === obs) { return; }
        var d = Math.hypot(p[0], p[1]), v = 0.55 * d;
        if (d > DM) { return; }
        g.beginPath(); g.arc(L + d / DM * (Rr - L), B - v / VM * (B - T), 3.2, 0, 2 * Math.PI); g.fill();
      });
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    cv.addEventListener('click', function (e) {
      var rc = cv.getBoundingClientRect(), mx = e.clientX - rc.left, my = e.clientY - rc.top;
      var a = scale(), k = Math.min(S.w, S.h / 0.62) * 0.47, o = GAL[obs], best = obs, bd = 1e9;
      GAL.forEach(function (g, j) {
        var X = S.w / 2 + (g.x - o.x) * a * k, Y = S.h / 2 + (g.y - o.y) * a * k, d = Math.hypot(X - mx, Y - my);
        if (d < bd) { bd = d; best = j; }
      });
      if (bd < 30) { obs = best; draw(); }
    });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); SG = canvasCtx(cvG); draw(); }
    watchVisible(cv, function (vv) { visible = vv; });
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 5. Détection d'une exoplanète ================= */
  (function () {
    var root = document.getElementById('lab-exo');
    if (!root) { return; }
    var cvO = $(root, 'canvas.orbit'), cvG = $(root, 'canvas.graph'), cvL = $(root, 'canvas.line');
    var rM = $(root, '[data-p="m"]'), rP = $(root, '[data-p="P"]'), btn = $(root, '[data-act="play"]');
    var oM = $(root, '.out-m'), oP = $(root, '.out-P'), oK = $(root, '.out-K'), oL = $(root, '.out-dl');
    var S1, S2, S3, playing = !RM, visible = true, t = 0, last = null, TA = 6;
    function mass() { return 0.001 * Math.pow(10, 4 * parseFloat(rM.value) / 100); }      /* 0,001 à 10 MJ */
    function period() { return Math.pow(10, 3.7 * parseFloat(rP.value) / 100); }         /* 1 à 5000 jours */
    function K() { return 28.43 * mass() * Math.pow(period() / 365.25, -1 / 3); }
    function readouts() {
      var m = mass(), P = period(), k = K();
      oM.textContent = (m < 0.1 ? fr(m * 317.8, 1) + ' masses terrestres' : fr(m, 2) + ' masse' + (m >= 2 ? 's' : '') + ' de Jupiter');
      oP.textContent = P < 100 ? fr(P, 1) + ' jours' : Math.round(P).toLocaleString('fr-FR') + ' jours';
      oK.textContent = k < 1 ? fr(k * 100, 1) + ' cm/s' : fr(k, k < 10 ? 1 : 0) + ' m/s';
      oL.innerHTML = sci(656.3 * k / 2.998e8, 1) + ' nm';
    }
    function draw() {
      if (!S1) { return; }
      var th = 2 * Math.PI * t / TA, k = K(), vr = k * Math.sin(th);  /* > 0 : l'étoile s'éloigne de nous */
      /* orbite vue de dessus */
      var c = S1.ctx, w = S1.w, h = S1.h, cx = w / 2, cy = h / 2 - 8, Rp = Math.min(w, h) * 0.36, rs = Math.min(14, 2 + 4 * Math.log10(1 + mass() * 30));
      c.fillStyle = '#0B1024'; c.fillRect(0, 0, w, h);
      c.strokeStyle = 'rgba(148,163,184,.35)'; c.beginPath(); c.arc(cx, cy, Rp, 0, 2 * Math.PI); c.stroke();
      var px = cx + Rp * Math.sin(th), py = cy - Rp * Math.cos(th);
      var sx = cx - rs * Math.sin(th), sy = cy + rs * Math.cos(th);
      var tint = vr > 0 ? [255, 120 + 100 * (1 - Math.min(1, vr / k)), 110] : [130 + 100 * (1 - Math.min(1, -vr / k)), 170, 255];
      c.fillStyle = 'rgb(' + Math.round(tint[0]) + ',' + Math.round(tint[1]) + ',' + Math.round(tint[2]) + ')';
      c.beginPath(); c.arc(sx, sy, 15, 0, 2 * Math.PI); c.fill();
      c.fillStyle = '#93C5FD'; c.beginPath(); c.arc(px, py, 5, 0, 2 * Math.PI); c.fill();
      c.strokeStyle = 'rgba(226,232,240,.8)'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(cx - 5, cy); c.lineTo(cx + 5, cy); c.moveTo(cx, cy - 5); c.lineTo(cx, cy + 5); c.stroke();
      c.fillStyle = '#E2E8F0'; c.font = '600 11px system-ui, sans-serif'; c.textAlign = 'center';
      c.fillText('vers la Terre \u2193', cx, h - 6);
      /* vitesse radiale */
      var g = S2.ctx, W = S2.w, H = S2.h, L = 50, Rr = W - 8, Tm = 12, Bm = H - 22, ym = (Tm + Bm) / 2, A = (Bm - Tm) / 2 * 0.85;
      g.clearRect(0, 0, W, H);
      g.strokeStyle = col('--line'); g.beginPath(); g.moveTo(L, ym); g.lineTo(Rr, ym); g.moveTo(L, Tm); g.lineTo(L, Bm); g.stroke();
      g.fillStyle = col('--muted'); g.font = '11px system-ui, sans-serif'; g.textAlign = 'right';
      var kt = k < 1 ? fr(k * 100, 0) + ' cm/s' : fr(k, 0) + ' m/s';
      g.fillText('+' + kt, L - 4, ym - A + 4); g.fillText('\u2212' + kt, L - 4, ym + A + 4); g.fillText('0', L - 4, ym + 4);
      g.textAlign = 'center'; g.fillText('temps \u2192 (deux périodes orbitales)', (L + Rr) / 2, H - 4);
      g.strokeStyle = col('--blue'); g.lineWidth = 2.2; g.beginPath();
      for (var i = 0; i <= 200; i++) { var tt = i / 200 * 2 * TA, yy = ym - A * Math.sin(2 * Math.PI * tt / TA); if (i === 0) { g.moveTo(L + i / 200 * (Rr - L), yy); } else { g.lineTo(L + i / 200 * (Rr - L), yy); } }
      g.stroke();
      var tm = t % (2 * TA);
      g.fillStyle = col('--amber'); g.beginPath(); g.arc(L + tm / (2 * TA) * (Rr - L), ym - A * Math.sin(th), 6, 0, 2 * Math.PI); g.fill();
      /* raie spectrale (décalage très exagéré) */
      var l = S3.ctx, W3 = S3.w, H3 = S3.h;
      var grd = l.createLinearGradient(0, 0, W3, 0);
      grd.addColorStop(0, '#F59E0B'); grd.addColorStop(0.5, '#F97316'); grd.addColorStop(1, '#DC2626');
      l.fillStyle = grd; l.fillRect(0, 0, W3, H3);
      l.fillStyle = 'rgba(255,255,255,.7)'; l.fillRect(W3 / 2 - 1, 0, 2, H3);
      var shift = Math.max(-W3 / 2 + 6, Math.min(W3 / 2 - 6, vr * 0.12));
      l.fillStyle = '#111'; l.fillRect(W3 / 2 + shift - 2, 0, 4, H3);
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    [rM, rP].forEach(function (r) { r.addEventListener('input', function () { readouts(); draw(); }); });
    Array.prototype.forEach.call(root.querySelectorAll('[data-preset]'), function (b) {
      b.addEventListener('click', function () {
        var p = b.getAttribute('data-preset').split(','), m = parseFloat(p[0]), P = parseFloat(p[1]);
        rM.value = (Math.log10(m / 0.001) / 4 * 100).toFixed(1); rP.value = (Math.log10(P) / 3.7 * 100).toFixed(1);
        readouts(); draw();
      });
    });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S1 = canvasCtx(cvO); S2 = canvasCtx(cvG); S3 = canvasCtx(cvL); readouts(); draw(); }
    watchVisible(cvO, function (vv) { visible = vv; });
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 6. Courbe de rotation d'une galaxie ================= */
  (function () {
    var root = document.getElementById('lab-rotation');
    if (!root) { return; }
    var cvD = $(root, 'canvas.disk'), cvG = $(root, 'canvas.graph'), cbH = $(root, '[data-p="halo"]'), btn = $(root, '[data-act="play"]'), msg = $(root, '.nt-msg');
    var S1, S2, playing = !RM, visible = true, t = 0, last = null, RMAX = 30, R = rng(7), STARS = [];
    function vVis(r) { var x = r / 3; return 322 * x / Math.pow(1 + x * x, 0.75); }
    function vHalo(r) { var rh = 5; return r < 1e-3 ? 0 : 200 * Math.sqrt(Math.max(0, 1 - rh / r * Math.atan(r / rh))); }
    function vTot(r) { return Math.sqrt(vVis(r) * vVis(r) + vHalo(r) * vHalo(r)); }
    for (var i = 0; i < 420; i++) {
      var r = 1 + Math.pow(R(), 0.7) * (RMAX - 1), arm = (R() < 0.5 ? 0 : Math.PI), ph = arm + 0.35 * r + (R() - 0.5) * 0.7;
      STARS.push({ r: r, ph: ph, s: 0.8 + R() * 1.2 });
    }
    function draw() {
      if (!S1) { return; }
      var halo = cbH.checked;
      var c = S1.ctx, w = S1.w, h = S1.h, cx = w / 2, cy = h / 2, k = Math.min(w, h) / 2 / RMAX * 0.95;
      c.fillStyle = '#0B1024'; c.fillRect(0, 0, w, h);
      var g0 = c.createRadialGradient(cx, cy, 0, cx, cy, 5 * k);
      g0.addColorStop(0, 'rgba(255,240,200,.9)'); g0.addColorStop(1, 'rgba(255,240,200,0)');
      c.fillStyle = g0; c.beginPath(); c.arc(cx, cy, 5 * k, 0, 2 * Math.PI); c.fill();
      STARS.forEach(function (s) {
        var v = halo ? vTot(s.r) : vVis(s.r), om = v / s.r * 0.004, a = s.ph + om * t;
        c.fillStyle = s.r < 8 ? 'rgba(254,243,199,.9)' : 'rgba(191,219,254,.85)';
        c.beginPath(); c.arc(cx + s.r * k * Math.cos(a), cy + s.r * k * Math.sin(a), s.s, 0, 2 * Math.PI); c.fill();
      });
      var g = S2.ctx, W = S2.w, H = S2.h, L = 44, Rr = W - 10, T = 12, B = H - 26, VM = 300;
      function X(r) { return L + r / RMAX * (Rr - L); }
      function Y(v) { return B - v / VM * (B - T); }
      g.clearRect(0, 0, W, H);
      g.strokeStyle = col('--line'); g.beginPath(); g.moveTo(L, T); g.lineTo(L, B); g.lineTo(Rr, B); g.stroke();
      g.fillStyle = col('--muted'); g.font = '11px system-ui, sans-serif'; g.textAlign = 'right';
      [0, 100, 200, 300].forEach(function (v) { g.fillText(v, L - 4, Y(v) + 4); });
      g.textAlign = 'center';
      [0, 10, 20, 30].forEach(function (r) { g.fillText(r, X(r), B + 13); });
      g.fillText('distance au centre (kpc)', (L + Rr) / 2, H - 2);
      g.save(); g.translate(10, (T + B) / 2); g.rotate(-Math.PI / 2); g.fillText('vitesse (km/s)', 0, 0); g.restore();
      function curve(f, color, dash) {
        g.strokeStyle = color; g.lineWidth = 2.4; g.setLineDash(dash); g.beginPath();
        for (var q = 0; q <= 150; q++) { var r = 0.2 + q / 150 * (RMAX - 0.2); if (q === 0) { g.moveTo(X(r), Y(f(r))); } else { g.lineTo(X(r), Y(f(r))); } }
        g.stroke(); g.setLineDash([]);
      }
      curve(vVis, col('--rose'), [6, 4]);
      if (halo) { curve(vTot, col('--blue'), []); }
      var RR = rng(3);
      g.fillStyle = col('--ink');
      for (var r2 = 2; r2 <= RMAX; r2 += 2) { var vv = vTot(r2) * (1 + (RR() - 0.5) * 0.06); g.beginPath(); g.arc(X(r2), Y(vv), 3.4, 0, 2 * Math.PI); g.fill(); }
      msg.textContent = halo ? 'Avec un halo de matière noire, la vitesse prévue reste presque constante loin du centre, comme les mesures : les étoiles lointaines filent aussi vite (en km/s) que celles proches du centre.' :
        'Avec la seule matière visible, la vitesse devrait diminuer loin du centre (comme pour les planètes du Système solaire). Les mesures (points noirs) ne suivent pas cette prévision.';
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    cbH.addEventListener('change', draw);
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S1 = canvasCtx(cvD); S2 = canvasCtx(cvG); draw(); }
    watchVisible(cvD, function (vv) { visible = vv; });
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
})();
</script>
