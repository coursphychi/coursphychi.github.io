+++
title = "Diffraction et interférences"
draft = false
hidden = true
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Signature du caractère ondulatoire {.nt-h2}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Quels indices expérimentaux témoignent-ils de la nature ondulatoire d'un phénomène&nbsp;?</p>
<ul class="nt-facts">
<li><span class="imp nt-hole">la diffraction</span></li>
<li><span class="imp nt-hole">les interférences</span></li>
</ul>
</div>

<div class="nt-grid">
<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-water"></i>Diffraction au quotidien</p>
<p>La houle qui entre dans une crique par une passe étroite s'étale ensuite en arcs de cercle et atteint toute la plage, y compris les zones abritées derrière les rochers.</p>
</div>
<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-rainbow"></i>Interférences au quotidien</p>
<p>Les reflets irisés d'un CD, d'une bulle de savon ou d'une tache de carburant sur le bitume mouillé, les couleurs de la nacre, des plumes de paon, des ailes de certains papillons ou des écailles du boa arc-en-ciel sont dus à des interférences.</p>
</div>
</div>

## Diffraction {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">diffraction</span> d'une onde correspond à l'<span class="imp nt-hole">étalement des directions de propagation</span> lorsque l'onde rencontre un <span class="imp nt-hole">obstacle</span> ou une <span class="imp nt-hole">ouverture</span>.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>L'étalement est d'autant plus marqué que l'obstacle ou l'ouverture sont <span class="imp nt-hole">petits</span>.</p>
<p>La fréquence $f$ et la célérité $c$ de l'onde, et donc sa longueur d'onde $\lambda=c/f$ sont <span class="imp nt-hole">conservées</span>.</p>
</div>

<div class="nt-lab" id="lab-cuve">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Une cuve à ondes vue de dessus</p>
<canvas style="aspect-ratio:8/5; height:auto; max-width:640px; margin:0 auto;" aria-label="Ondes planes arrivant sur une paroi percée d'une ouverture ; au-delà, l'onde s'étale plus ou moins selon la taille de l'ouverture"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Largeur de l'ouverture $a$&nbsp;: <b class="out-a"></b><input type="range" data-p="a" min="0.5" max="7" step="0.1" value="1.6"></label>
<label class="nt-ctrl">Longueur d'onde $\lambda$&nbsp;: <b class="out-l"></b><input type="range" data-p="lambda" min="0.6" max="2.5" step="0.05" value="1.2"></label>
</div>
<div class="nt-read"><span>$a/\lambda$ = <b class="out-r"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg">Les pointillés blancs marquent l'ombre géométrique, c'est-à-dire là où l'onde s'arrêterait si elle se propageait en ligne droite. Quand $a/\lambda$ devient proche de 1, l'onde s'étale dans presque toutes les directions&nbsp;; quand $a/\lambda$ est grand, elle continue presque tout droit.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le phénomène de diffraction est nettement observé lorsque la <b>taille caractéristique $a$ de l'obstacle ou de l'ouverture</b> est du <span class="imp nt-hole">même ordre de grandeur</span> que <b>la longueur d'onde $\lambda$ de l'onde</b>.</p>
<p>Dans le cas d'ondes lumineuses, le critère est moins restrictif et le phénomène est encore apparent pour des tailles $a$ jusqu'à 100 fois plus grandes que $\lambda$.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La diffraction est caractérisée par un <span class="imp">angle de diffraction</span> défini comme l'angle entre la direction de propagation sans diffraction et la direction définie par le milieu de la «&nbsp;première extinction&nbsp;».</p>
</div>

<svg class="nt-svg" viewBox="0 0 780 330" role="img" aria-label="Montage de diffraction vu de dessus : laser, fente de largeur a, écran à la distance D, tache centrale de largeur L et angle θ"><defs><linearGradient id="gCone2" gradientUnits="userSpaceOnUse" x1="262" y1="0" x2="640" y2="0"><stop offset="0" stop-color="#22C55E" stop-opacity=".5"/><stop offset="1" stop-color="#22C55E" stop-opacity=".12"/></linearGradient></defs><rect x="20" y="138" width="100" height="44" rx="9" fill="var(--slate)"/><text x="70" y="165" font-size="14" fill="#fff" text-anchor="middle" font-weight="700">laser</text><rect x="120" y="155" width="130" height="10" fill="#22C55E"/><rect x="640" y="25" width="8" height="270" rx="2" fill="var(--slate)" opacity=".3"/><polygon points="262,160 640,78 640,242" fill="url(#gCone2)"/><line x1="262" y1="160" x2="640" y2="160" stroke="var(--slate)" stroke-dasharray="6 5"/><line x1="262" y1="160" x2="640" y2="78" stroke="#16A34A" stroke-width="1.8"/><rect x="250" y="35" width="12" height="115" fill="var(--ink)"/><rect x="250" y="170" width="12" height="125" fill="var(--ink)"/><polyline points="377.0,160.0 377.0,159.2 377.0,158.4 377.0,157.5 377.0,156.7 376.9,155.9 376.9,155.1 376.9,154.3 376.8,153.5 376.8,152.6 376.7,151.8 376.6,151.0 376.6,150.2 376.5,149.4 376.4,148.6 376.3,147.7 376.3,146.9 376.2,146.1 376.1,145.3 375.9,144.5 375.8,143.7 375.7,142.9 375.6,142.1 375.5,141.2 375.3,140.4 375.2,139.6 375.0,138.8 374.9,138.0 374.7,137.2 374.6,136.4 374.4,135.6" fill="none" stroke="var(--blue)" stroke-width="2.5"/><text x="395.2" y="152.7" font-size="21" fill="var(--blue)" font-family="Georgia, serif" font-style="italic" font-weight="700">θ</text><line x1="222" y1="150" x2="250" y2="150" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3"/><line x1="222" y1="170" x2="250" y2="170" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3"/><line x1="236" y1="124" x2="236" y2="142" stroke="var(--amber)" stroke-width="2"/><polygon points="236.0,150.0 231.5,141.0 240.5,141.0" fill="var(--amber)"/><line x1="236" y1="196" x2="236" y2="178" stroke="var(--amber)" stroke-width="2"/><polygon points="236.0,170.0 240.5,179.0 231.5,179.0" fill="var(--amber)"/><text x="226" y="132" font-size="20" fill="var(--amber)" text-anchor="end" font-family="Georgia, serif" font-style="italic" font-weight="700">a</text><polyline points="660.1,27 660.1,28 660.2,29 660.3,30 660.4,31 660.5,32 660.6,33 660.6,34 660.7,35 660.7,36 660.8,37 660.8,38 660.9,39 660.9,40 660.9,41 660.9,42 660.9,43 660.9,44 660.9,45 660.9,46 660.8,47 660.8,48 660.8,49 660.7,50 660.6,51 660.6,52 660.5,53 660.4,54 660.3,55 660.2,56 660.1,57 660.0,58 659.8,59 659.7,60 659.6,61 659.5,62 659.3,63 659.2,64 659.1,65 658.9,66 658.8,67 658.7,68 658.6,69 658.5,70 658.4,71 658.3,72 658.2,73 658.1,74 658.1,75 658.0,76 658.0,77 658.0,78 658.0,79 658.0,80 658.1,81 658.2,82 658.3,83 658.4,84 658.5,85 658.7,86 658.9,87 659.1,88 659.4,89 659.7,90 660.0,91 660.4,92 660.8,93 661.2,94 661.7,95 662.2,96 662.7,97 663.3,98 663.9,99 664.5,100 665.2,101 665.9,102 666.7,103 667.5,104 668.3,105 669.2,106 670.1,107 671.0,108 672.0,109 673.0,110 674.0,111 675.0,112 676.1,113 677.2,114 678.4,115 679.5,116 680.7,117 681.9,118 683.1,119 684.4,120 685.6,121 686.9,122 688.1,123 689.4,124 690.7,125 692.0,126 693.3,127 694.5,128 695.8,129 697.1,130 698.3,131 699.6,132 700.8,133 702.0,134 703.2,135 704.4,136 705.5,137 706.6,138 707.7,139 708.8,140 709.8,141 710.8,142 711.7,143 712.6,144 713.5,145 714.3,146 715.0,147 715.8,148 716.4,149 717.0,150 717.6,151 718.1,152 718.5,153 718.9,154 719.2,155 719.5,156 719.7,157 719.9,158 720.0,159 720.0,160 720.0,161 719.9,162 719.7,163 719.5,164 719.2,165 718.9,166 718.5,167 718.1,168 717.6,169 717.0,170 716.4,171 715.8,172 715.0,173 714.3,174 713.5,175 712.6,176 711.7,177 710.8,178 709.8,179 708.8,180 707.7,181 706.6,182 705.5,183 704.4,184 703.2,185 702.0,186 700.8,187 699.6,188 698.3,189 697.1,190 695.8,191 694.5,192 693.3,193 692.0,194 690.7,195 689.4,196 688.1,197 686.9,198 685.6,199 684.4,200 683.1,201 681.9,202 680.7,203 679.5,204 678.4,205 677.2,206 676.1,207 675.0,208 674.0,209 673.0,210 672.0,211 671.0,212 670.1,213 669.2,214 668.3,215 667.5,216 666.7,217 665.9,218 665.2,219 664.5,220 663.9,221 663.3,222 662.7,223 662.2,224 661.7,225 661.2,226 660.8,227 660.4,228 660.0,229 659.7,230 659.4,231 659.1,232 658.9,233 658.7,234 658.5,235 658.4,236 658.3,237 658.2,238 658.1,239 658.0,240 658.0,241 658.0,242 658.0,243 658.0,244 658.1,245 658.1,246 658.2,247 658.3,248 658.4,249 658.5,250 658.6,251 658.7,252 658.8,253 658.9,254 659.1,255 659.2,256 659.3,257 659.5,258 659.6,259 659.7,260 659.8,261 660.0,262 660.1,263 660.2,264 660.3,265 660.4,266 660.5,267 660.6,268 660.6,269 660.7,270 660.8,271 660.8,272 660.8,273 660.9,274 660.9,275 660.9,276 660.9,277 660.9,278 660.9,279 660.9,280 660.9,281 660.8,282 660.8,283 660.7,284 660.7,285 660.6,286 660.6,287 660.5,288 660.4,289 660.3,290 660.2,291 660.1,292 660.1,293" fill="none" stroke="#16A34A" stroke-width="2"/><line x1="650" y1="78" x2="752" y2="78" stroke="var(--rose)" stroke-width="1" stroke-dasharray="3 3"/><line x1="650" y1="242" x2="752" y2="242" stroke="var(--rose)" stroke-width="1" stroke-dasharray="3 3"/><line x1="744.0" y1="86.0" x2="744.0" y2="234.0" stroke="var(--rose)" stroke-width="2"/><polygon points="744.0,242.0 739.5,233.0 748.5,233.0" fill="var(--rose)"/><polygon points="744.0,78.0 748.5,87.0 739.5,87.0" fill="var(--rose)"/><text x="754" y="167" font-size="21" fill="var(--rose)" font-family="Georgia, serif" font-style="italic" font-weight="700">L</text><line x1="262" y1="298" x2="262" y2="322" stroke="var(--slate)" stroke-width="1" stroke-dasharray="3 3"/><line x1="640" y1="298" x2="640" y2="322" stroke="var(--slate)" stroke-width="1" stroke-dasharray="3 3"/><line x1="270.0" y1="312.0" x2="632.0" y2="312.0" stroke="var(--slate)" stroke-width="1.6"/><polygon points="640.0,312.0 631.0,316.5 631.0,307.5" fill="var(--slate)"/><polygon points="262.0,312.0 271.0,307.5 271.0,316.5" fill="var(--slate)"/><text x="451.0" y="304" font-size="20" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">D</text></svg>

<p class="nt-cap">Montage vu de dessus&nbsp;: la fente, de largeur $a$, est verticale&nbsp;; la lumière s'étale horizontalement sur l'écran placé à la distance $D$. La courbe verte représente l'intensité lumineuse le long de l'écran.</p>

<p class="nt-lead">Dans le cas de la diffraction d'une onde lumineuse monochromatique de longueur d'onde $\lambda$ (produite par un laser) par une fente rectangulaire de largeur $a$, l'angle caractéristique de diffraction $\theta$ est donné par&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$\theta\approx\frac{\lambda}{a}$$</p>
<div class="nt-f-units"><span>$\lambda$ en $\pu{m}$</span><span>$a$ en $\pu{m}$</span><span>$\theta$ en <span class="nt-hole">$\pu{rad}$</span></span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Pour une longueur d'onde fixée&nbsp;: $a \searrow\;\Rightarrow\;\theta$ <span class="imp nt-hole">$\nearrow$</span></li>
<li>Pour une taille $a$ fixée&nbsp;: $\lambda \nearrow\;\Rightarrow\;\theta$ <span class="imp nt-hole">$\nearrow$</span></li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Dans l'approximation des petits angles ($\theta\ll 1$), exprimer la taille de la tache centrale $L$ en fonction de $\lambda$, $D$ et $a$.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$L\approx \frac{2\lambda D}{a}$$</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>Dans le triangle rectangle formé par la fente, le centre de la tache et le bord de la tache centrale&nbsp;:</p>
<p class="nt-center">$\tan\theta = \dfrac{L/2}{D}$</p>
<p>Or d'après l'approximation des petits angles&nbsp;: $\tan\theta \approx \theta$ (⚠️ valable uniquement en radians). D'où&nbsp;:</p>
<p class="nt-center">$\theta\approx \dfrac{L}{2D}$</p>
<p>Et comme $\theta\approx\dfrac{\lambda}{a}$, on obtient finalement&nbsp;: $\dfrac\lambda a \approx \dfrac{L}{2D} \;\Rightarrow\; L \approx \dfrac{2\lambda D}{a}$.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Jusqu'où l'approximation des petits angles est-elle valable&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Pour $\theta = \pu{0,10 rad}$ (environ 6°), $\tan\theta = 0{,}1003$&nbsp;: l'erreur commise en remplaçant $\tan\theta$ par $\theta$ est de 0,3&nbsp;%. Pour $\theta = \pu{0,30 rad}$ (environ 17°), elle atteint déjà 3&nbsp;%. En diffraction de la lumière, $\theta$ vaut typiquement quelques milliradians&nbsp;: l'approximation est excellente.</p>
<p>Elle n'est valable qu'en radians, car c'est dans cette unité que la courbe de $\tan$ «&nbsp;colle&nbsp;» à la droite $y = \theta$ au voisinage de 0. En degrés, $\tan(5°) \approx 0{,}087$, qui n'a rien à voir avec 5.</p>
</div>
</details>

<div class="nt-lab" id="lab-fente">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Diffraction d'un laser par une fente</p>
<canvas class="screen" style="height:70px;" aria-label="Figure de diffraction observée sur l'écran"></canvas>
<canvas class="plot" style="height:170px; margin-top:8px; background:#fff;" aria-label="Intensité lumineuse le long de l'écran"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Longueur d'onde $\lambda$&nbsp;: <b class="out-l"></b><input type="range" data-p="lambda" min="400" max="750" step="5" value="635"></label>
<label class="nt-ctrl">Largeur de la fente $a$&nbsp;: <b class="out-a"></b><input type="range" data-p="a" min="20" max="200" step="5" value="60"></label>
<label class="nt-ctrl">Distance fente-écran $D$&nbsp;: <b class="out-D"></b><input type="range" data-p="D" min="0.5" max="3" step="0.1" value="2"></label>
</div>
<div class="nt-read"><span>$\theta \approx \lambda/a$ = <b class="out-t"></b></span><span>$L \approx 2\lambda D/a$ = <b class="out-L"></b></span></div>
<p class="nt-msg">Vérifiez sur la courbe que la largeur $L$ de la tache centrale suit bien la formule, et repérez les deux sens de variation&nbsp;: $a$ plus petit ou $\lambda$ plus grand, et la tache s'élargit.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples de conséquences concrètes</p>
<p>L'onde diffractée peut atteindre des endroits qui seraient inaccessibles sans l'étalement des directions de propagation.</p>
<p>Un son diffracté par l'entrebâillement d'une porte peut ainsi être entendu dans toute la pièce et un bateau peut subir la houle même à l'abri d'une digue.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La figure de diffraction nous renseigne sur la <span class="imp nt-hole">forme géométrique</span> de l'obstacle qu'a rencontré l'onde&nbsp;!</p>
</div>

<div class="nt-lab" id="lab-formes">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">À chaque forme d'ouverture sa figure de diffraction</p>
<div class="nt-lab-pair">
<figure><canvas class="ap" style="aspect-ratio:1/1; height:auto; max-width:320px; margin:0 auto; background:#141E30;" aria-label="Forme de l'ouverture éclairée"></canvas><figcaption>Ouverture</figcaption></figure>
<figure><canvas class="fig" style="aspect-ratio:1/1; height:auto; max-width:320px; margin:0 auto; background:#080C1C;" aria-label="Figure de diffraction correspondante"></canvas><figcaption>Figure de diffraction (au loin)</figcaption></figure>
</div>
<div class="nt-ctrl">Forme&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="forme" value="fente" checked><span>Fente</span></label>
<label><input type="radio" name="forme" value="carre"><span>Carré</span></label>
<label><input type="radio" name="forme" value="disque"><span>Disque</span></label>
<label><input type="radio" name="forme" value="hexagone"><span>Hexagone</span></label>
<label><input type="radio" name="forme" value="grille"><span>Pixels d'écran</span></label>
<label><input type="radio" name="forme" value="hubble"><span>Hubble</span></label>
<label><input type="radio" name="forme" value="webb"><span>Webb</span></label>
</div>
</div>
<label class="nt-ctrl">Taille de l'ouverture&nbsp;: <b class="out-s"></b><input type="range" data-p="s" min="20" max="100" step="2" value="50"></label>
<p class="nt-msg"></p>
</div>

<p class="nt-cap">La figure de diffraction est calculée à partir de la forme de l'ouverture&nbsp;: plus l'ouverture est grande, plus la figure est petite (la taille de Webb est fixe). Regarder une lampe à travers l'écran allumé d'un téléphone donne une figure en croix due à la grille des pixels.</p>

<p class="nt-lead">Un grand nombre de structures de protéines ont ainsi été déterminées par diffraction (on cristallise d'abord la protéine puis on envoie le rayonnement dans le cristal).</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Dans un cristal de protéine, les atomes sont espacés d'environ $\pu{0,1 nm}$. Quel doit être l'ordre de grandeur de la longueur d'onde à utiliser&nbsp;? À quelle partie du spectre électromagnétique appartient le rayonnement&nbsp;?</p>
</div>

<svg class="nt-svg" viewBox="0 0 720 150" role="img" aria-label="Spectre électromagnétique en fonction de la longueur d'onde, des rayons gamma aux ondes radio"><defs><linearGradient id="gVis" x1="0" x2="1"><stop offset="0" stop-color="#8B5CF6"/><stop offset=".2" stop-color="#3B82F6"/><stop offset=".4" stop-color="#22C55E"/><stop offset=".6" stop-color="#EAB308"/><stop offset=".8" stop-color="#F97316"/><stop offset="1" stop-color="#EF4444"/></linearGradient></defs><rect x="40.0" y="40" width="80.0" height="34" fill="#7C3AED" fill-opacity="0.85"/><text x="80.0" y="62" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">γ</text><rect x="120.0" y="40" width="120.0" height="34" fill="#2A6BC4" fill-opacity="0.85"/><text x="180.0" y="62" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">rayons X</text><rect x="240.0" y="40" width="64.1" height="34" fill="#0EA5E9" fill-opacity="0.85"/><text x="272.0" y="62" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">UV</text><rect x="304.1" y="40" width="12.0" height="34" fill="url(#gVis)" fill-opacity="1"/><rect x="316.1" y="40" width="123.9" height="34" fill="#E11D48" fill-opacity="0.85"/><text x="378.1" y="62" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">infrarouge</text><rect x="440.0" y="40" width="80.0" height="34" fill="#D97706" fill-opacity="0.85"/><text x="480.0" y="62" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">micro-ondes</text><rect x="520.0" y="40" width="160.0" height="34" fill="#047857" fill-opacity="0.85"/><text x="600.0" y="62" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">ondes radio</text><text x="310.0" y="32" font-size="12" fill="var(--ink)" text-anchor="middle" font-weight="700">visible</text><line x1="310.0" y1="35" x2="310.0" y2="40" stroke="var(--ink)"/><line x1="40" y1="74" x2="40" y2="80" stroke="var(--ink)"/><text x="40" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">−13</tspan></text><line x1="80" y1="74" x2="80" y2="80" stroke="var(--ink)"/><line x1="120" y1="74" x2="120" y2="80" stroke="var(--ink)"/><text x="120" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">−11</tspan></text><line x1="160" y1="74" x2="160" y2="80" stroke="var(--ink)"/><line x1="200" y1="74" x2="200" y2="80" stroke="var(--ink)"/><text x="200" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">−9</tspan></text><line x1="240" y1="74" x2="240" y2="80" stroke="var(--ink)"/><line x1="280" y1="74" x2="280" y2="80" stroke="var(--ink)"/><text x="280" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">−7</tspan></text><line x1="320" y1="74" x2="320" y2="80" stroke="var(--ink)"/><line x1="360" y1="74" x2="360" y2="80" stroke="var(--ink)"/><text x="360" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">−5</tspan></text><line x1="400" y1="74" x2="400" y2="80" stroke="var(--ink)"/><line x1="440" y1="74" x2="440" y2="80" stroke="var(--ink)"/><text x="440" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">−3</tspan></text><line x1="480" y1="74" x2="480" y2="80" stroke="var(--ink)"/><line x1="520" y1="74" x2="520" y2="80" stroke="var(--ink)"/><text x="520" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">−1</tspan></text><line x1="560" y1="74" x2="560" y2="80" stroke="var(--ink)"/><text x="560" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">1</text><line x1="600" y1="74" x2="600" y2="80" stroke="var(--ink)"/><text x="600" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">1</tspan></text><line x1="640" y1="74" x2="640" y2="80" stroke="var(--ink)"/><line x1="680" y1="74" x2="680" y2="80" stroke="var(--ink)"/><text x="680" y="96" font-size="12" text-anchor="middle" fill="var(--ink)">10<tspan dy="-6" font-size="9">3</tspan></text><line x1="40" y1="74" x2="680" y2="74" stroke="var(--ink)"/><text x="360" y="128" font-size="13" text-anchor="middle" fill="var(--slate)">longueur d'onde λ (m)</text></svg>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Pour que la diffraction soit nette, la longueur d'onde doit être du même ordre de grandeur que la taille des «&nbsp;obstacles&nbsp;», ici les distances entre atomes&nbsp;: $\lambda \sim \pu{1E-10 m}$. D'après le spectre, il s'agit de <b>rayons X</b>.</p>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-dna"></i>Exemple historique</p>
<p>C'est une diffraction aux rayons X qui a permis de découvrir (grâce à Rosalind Franklin) la structure en double hélice de l'ADN.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La «&nbsp;photo 51&nbsp;» et le prix Nobel</span></summary>
<div class="nt-d-body">
<p><b>Le cliché.</b> En 1952, au King's College de Londres, Rosalind Franklin et son doctorant Raymond Gosling envoient des rayons X sur une fibre d'ADN et enregistrent la figure de diffraction obtenue. L'un de ces clichés, la «&nbsp;photo 51&nbsp;», est devenu l'une des images les plus célèbres de l'histoire des sciences.</p>
<p><b>Ce qu'il révèle.</b> On y voit un motif en forme de X&nbsp;: c'est la signature d'une molécule en forme d'hélice. Les écarts entre les taches permettent même de calculer certaines dimensions de cette hélice. Franklin avait d'ailleurs envisagé une structure hélicoïdale avant Watson et Crick.</p>
<p><b>Le rôle de Watson et Crick.</b> Début 1953, sans que Franklin le sache, son collègue Maurice Wilkins montre le cliché à James Watson. Avec Francis Crick, il s'en sert pour construire le modèle de la double hélice, publié la même année.</p>
<p><b>Le Nobel.</b> En 1962, Watson, Crick et Wilkins reçoivent le prix Nobel de médecine. Rosalind Franklin, morte d'un cancer en 1958 à 37 ans, ne pouvait plus être récompensée&nbsp;: le prix Nobel n'est pas attribué à titre posthume.</p>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La tache de diffraction correspondant à l'ouverture d'un télescope ou d'une lunette donne la <span class="imp nt-hole">résolution ultime</span> atteignable par l'appareil.</p>
<p><span class="imp">$\Rightarrow$ Plus l'ouverture est large, meilleure est la résolution.</span></p>
</div>

<div class="nt-lab" id="lab-resol">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Séparer deux étoiles proches</p>
<p class="nt-note">Deux étoiles séparées d'une seconde d'arc (1/3600 de degré) sont observées en lumière verte ($\lambda = \pu{550 nm}$).</p>
<canvas style="aspect-ratio:2/1; height:auto; max-width:560px; margin:0 auto; background:#0A0E1E;" aria-label="Images de deux étoiles proches à travers un télescope"></canvas>
<label class="nt-ctrl">Diamètre de l'ouverture du télescope&nbsp;: <b class="out-D"></b><input type="range" data-p="D" min="4" max="40" step="1" value="8"></label>
<div class="nt-read"><span>rayon angulaire de la tache = <b class="out-t"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Pour une ouverture circulaire de diamètre $D$, le rayon angulaire de la tache centrale vaut $1{,}22\,\lambda/D$&nbsp;: c'est l'équivalent de $\theta \approx \lambda/a$, avec un facteur 1,22 dû à la forme circulaire (hors programme).</p>
</div>


## Interférences de deux ondes {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Lorsque deux ondes se rencontrent en un point, leurs amplitudes en ce point <span class="imp nt-hole">s'additionnent</span>.</p>
<p>Il n'y a pas d'interaction, chaque onde évoluant indépendamment l'une de l'autre, mais il y a <span class="imp nt-hole">superposition</span> des perturbations.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Conditions d'observation</p>
<ul class="nt-facts">
<li>les ondes doivent être <span class="imp nt-hole">de même nature</span>&nbsp;;</li>
<li>les sources doivent être <span class="imp nt-hole">synchrones</span> = de même fréquence&nbsp;;</li>
<li>les sources doivent être <span class="imp nt-hole">cohérentes</span> = le retard du signal émis par l'une par rapport à l'autre reste constant (= déphasage constant).</li>
</ul>
</div>

<div class="nt-grid">
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>En phase</p>
<p>Deux signaux sont dits <span class="imp">en phase</span> s'ils coïncident (les extrema se correspondent).</p>
<p>Si en un point, les signaux des deux ondes sont en phase, on dit que <span class="imp nt-hole">l'interférence est constructive</span>.</p>
</div>
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>En opposition de phase</p>
<p>Deux signaux sont dits <span class="imp">en opposition de phase</span> si les maxima de l'un correspondent aux minima de l'autre (il y a un déphasage de π ou 180°).</p>
<p>Si en un point, les signaux des deux ondes sont en opposition de phase, on dit que <span class="imp nt-hole">l'interférence est destructive</span>.</p>
</div>
</div>

<div class="nt-lab" id="lab-signaux">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Deux ondes en un même point</p>
<canvas style="height:270px;" aria-label="Signaux des deux ondes en un point et leur somme"></canvas>
<label class="nt-ctrl">Décalage temporel $\Delta t$ de l'onde 2&nbsp;: <b class="out-dt"></b><input type="range" data-p="dt" min="0" max="1" step="0.01" value="0.2"></label>
<div class="nt-btns">
<button type="button" class="nt-btn" data-set="0">En phase</button>
<button type="button" class="nt-btn" data-set="0.5">Opposition de phase</button>
<label class="nt-check"><input type="checkbox" data-p="incoh"> Sources incohérentes</label>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<p class="nt-lead">Supposons que les oscillations issues de deux sources <span style="color:var(--blue);font-weight:700;">S<sub>1</sub></span> et <span style="color:var(--rose);font-weight:700;">S<sub>2</sub></span> soient en phase. Un récepteur est placé en un point <span style="color:var(--amber);font-weight:700;">M</span>.</p>

<p>L'onde issue de <span style="color:var(--blue);font-weight:700;">S<sub>1</sub></span> parcourt donc une distance $\color{#2A6BC4}\mathrm{S_1M}$ et celle issue de <span style="color:var(--rose);font-weight:700;">S<sub>2</sub></span> parcourt une distance $\color{#E11D48}\mathrm{S_2M}$.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Appelons enfin $\color{#047857}\delta$ la différence entre ces deux distances. On appelle $\color{#047857}\delta$ la <span class="imp nt-hole">différence de marche</span>&nbsp;: ${\color{#047857}\delta}=\mathrm{{\color{#E11D48}S_2M}-{\color{#2A6BC4}S_1M}}$.</p>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 580 300" role="img" aria-label="Deux sources S1 et S2 et un point M ; la différence des distances S2M et S1M est la différence de marche δ"><polyline points="70.0,80.0 70.4,84.3 70.9,88.6 71.4,92.8 71.9,97.1 72.5,101.4 73.2,105.6 73.8,109.9 74.5,114.1 75.3,118.3 76.1,122.6 77.0,126.8 77.8,131.0 78.8,135.2 79.7,139.4 80.7,143.6 81.8,147.7 82.9,151.9 84.0,156.0 85.2,160.2 86.4,164.3 87.7,168.4 89.0,172.5 90.3,176.6 91.7,180.7 93.1,184.7 94.6,188.8 96.1,192.8 97.6,196.8 99.2,200.8 100.8,204.8 102.5,208.8 104.2,212.7 105.9,216.7 107.7,220.6 109.5,224.5 111.4,228.4 113.3,232.2 115.2,236.1 117.2,239.9 119.2,243.7" fill="none" stroke="var(--muted)" stroke-dasharray="3 4"/><line x1="70" y1="80" x2="500" y2="40" stroke="var(--blue)" stroke-width="3"/><line x1="119.2" y1="243.7" x2="500" y2="40" stroke="var(--rose)" stroke-width="3"/><line x1="70" y1="270" x2="119.2" y2="243.7" stroke="var(--emerald)" stroke-width="6" stroke-linecap="round"/><circle cx="70" cy="80" r="9" fill="var(--blue)"/><circle cx="70" cy="270" r="9" fill="var(--rose)"/><circle cx="500" cy="40" r="8" fill="var(--amber)"/><text x="30" y="87" font-size="20" font-weight="700" fill="var(--blue)">S<tspan font-size="13" dy="5">1</tspan></text><text x="30" y="277" font-size="20" font-weight="700" fill="var(--rose)">S<tspan font-size="13" dy="5">2</tspan></text><text x="514" y="46" font-size="20" font-weight="700" fill="var(--amber)">M</text><text x="270" y="48" font-size="16" fill="var(--blue)" font-weight="700">S<tspan font-size="11" dy="4">1</tspan><tspan dy="-4">M</tspan></text><text x="300" y="180" font-size="16" fill="var(--rose)" font-weight="700">S<tspan font-size="11" dy="4">2</tspan><tspan dy="-4">M</tspan></text><text x="100.6" y="282.8" font-size="22" fill="var(--emerald)" font-family="Georgia, serif" font-style="italic" font-weight="700">δ</text></svg>

<p class="nt-cap">En reportant la longueur $\mathrm{S_1M}$ sur le segment $[\mathrm{S_2M}]$ à partir de M (arc en pointillés), on voit apparaître le chemin supplémentaire $\delta$ parcouru par l'onde issue de $\mathrm{S_2}$.</p>

<p class="nt-lead">La condition pour observer une interférence constructive en M est que la différence entre les distances parcourues sur chacun des chemins (${\color{#047857}\delta}=\mathrm{{\color{#E11D48}S_2M}-{\color{#2A6BC4}S_1M}}$) induise un déphasage valant un multiple de 2π.</p>

<p>On en déduit la condition pour obtenir en un point une <span class="imp">interférence constructive</span>&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Interférence constructive</p>
<p class="nt-f-math">$$\frac{\delta}{\lambda} = k \;,\; k\in\mathbb{Z}$$</p>
<div class="nt-f-units"><span>Autrement dit, la distance supplémentaire parcourue sur le chemin le plus long doit être un multiple de la longueur d'onde.</span></div>
</div>

<p>Et pour des <span class="imp">interférences destructives</span>, il faut&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Interférence destructive</p>
<p class="nt-f-math">$$\frac{\delta}{\lambda} = \left(k+\frac12\right) \;,\; k\in \mathbb{Z}$$</p>
<div class="nt-f-units"><span>La distance supplémentaire doit valoir un nombre impair de demi-longueurs d'onde.</span></div>
</div>

<details class="nt-d">
<summary><span class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</span><span class="nt-sum">Du déphasage à la différence de marche</span></summary>
<div class="nt-d-body">
<p>Une onde parcourt une longueur d'onde $\lambda$ pendant une période $T$. Le chemin supplémentaire $\delta$ fait donc arriver l'onde issue de $\mathrm{S_2}$ avec un retard de $\dfrac{\delta}{\lambda}$ périodes, ce qui correspond à un déphasage $2\pi\times\dfrac{\delta}{\lambda}$.</p>
<p><b>Constructive</b>&nbsp;: $2\pi\times \dfrac{\delta}{\lambda}= k\times 2\pi \iff \dfrac{\delta}{\lambda} = k\;,\; k\in\mathbb{Z}$.</p>
<p><b>Destructive</b>&nbsp;: $2\pi\dfrac{\delta}{\lambda}=\pi + k\times 2\pi =2\pi\times\left(k+\dfrac{1}{2}\right) \iff \dfrac{\delta}{\lambda} = k+\dfrac12\;,\; k\in\mathbb{Z}$.</p>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'entier $k$ est appelé <span class="imp nt-hole">ordre d'interférence</span>.</p>
</div>

<div class="nt-lab" id="lab-sources">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Deux sources dans une cuve à ondes</p>
<p class="nt-note">Faites glisser le point M (ou cliquez dans la cuve, puis utilisez les flèches du clavier).</p>
<canvas class="nt-drag" tabindex="0" style="aspect-ratio:3/2; height:auto; max-width:660px; margin:0 auto;" aria-label="Interférences de deux ondes circulaires issues de S1 et S2 ; le point M est déplaçable"></canvas>
<div class="nt-read" aria-live="polite"><span>$\mathrm{S_1M}$ = <b class="out-1"></b></span><span>$\mathrm{S_2M}$ = <b class="out-2"></b></span><span>$\delta$ = <b class="out-d"></b></span><span>$\delta/\lambda$ = <b class="out-r"></b></span></div>
<p class="nt-msg"></p>
<div class="nt-ctrls">
<label class="nt-ctrl">Longueur d'onde $\lambda$&nbsp;: <b class="out-l"></b><input type="range" data-p="lambda" min="0.8" max="3" step="0.05" value="1.6"></label>
<label class="nt-ctrl">Distance entre les sources&nbsp;: <b class="out-e"></b><input type="range" data-p="e" min="2" max="10" step="0.1" value="6"></label>
</div>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="amp"> Amplitude des oscillations</label>
<label class="nt-check"><input type="checkbox" data-p="ordres"> Lignes d'ordre $k$</label>
<label class="nt-check"><input type="checkbox" data-p="incoh"> Sources incohérentes</label>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-note">«&nbsp;Amplitude des oscillations&nbsp;» affiche une image figée&nbsp;: zones claires = fortes oscillations (constructive), zones sombres = eau quasi immobile (destructive). Les lignes vertes correspondent à $\delta/\lambda$ entier, les lignes roses à $\delta/\lambda$ demi-entier.</p>
</div>

### Les trous d'Young {.nt-h3}

<p class="nt-lead">Dans le cas de l'expérience optique des <span class="imp">trous d'Young</span> (ou des fentes d'Young), les deux trous éclairés par la source lumineuse agissent ensuite comme deux sources <span class="imp nt-hole">synchrones</span> et <span class="imp nt-hole">cohérentes</span> séparées d'une distance $a$.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On doit maintenant prendre en compte l'éventuel ralentissement de la lumière dans un milieu d'indice optique $n$, la différence de distance $\mathrm{S_2M-S_1M}$ prend alors le nom de <span class="imp nt-hole">différence de chemin optique</span>&nbsp;: $\mathrm{[S_2M]-[S_1M]}=n\times(\mathrm{S_2M-S_1M})$.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Ici, $a$ désigne la distance entre les deux trous, et non plus la largeur d'une fente comme dans la partie sur la diffraction.</p>
</div>

<svg class="nt-svg" viewBox="0 0 780 340" role="img" aria-label="Trous d'Young vus de dessus : deux trous S1 et S2 distants de a, écran à la distance D, franges brillantes d'interfrange i, point M d'abscisse x"><defs><linearGradient id="gY2" gradientUnits="userSpaceOnUse" x1="262" y1="0" x2="640" y2="0"><stop offset="0" stop-color="#22C55E" stop-opacity=".42"/><stop offset="1" stop-color="#22C55E" stop-opacity=".1"/></linearGradient></defs><rect x="20" y="121" width="230" height="88" fill="#22C55E" opacity=".35"/><text x="30" y="113" font-size="13" fill="var(--slate)">faisceau laser élargi</text><rect x="640" y="25" width="8" height="280" rx="2" fill="var(--slate)" opacity=".3"/><polygon points="262,141 640,40 640,290" fill="url(#gY2)"/><polygon points="262,189 640,40 640,290" fill="url(#gY2)"/><line x1="262" y1="165" x2="640" y2="165" stroke="var(--slate)" stroke-dasharray="6 5"/><rect x="250" y="30" width="12" height="106" fill="var(--ink)"/><rect x="250" y="146" width="12" height="38" fill="var(--ink)"/><rect x="250" y="194" width="12" height="106" fill="var(--ink)"/><rect x="641" y="266" width="6" height="14" rx="3" fill="#16A34A"/><rect x="641" y="230" width="6" height="14" rx="3" fill="#16A34A"/><rect x="641" y="194" width="6" height="14" rx="3" fill="#16A34A"/><rect x="641" y="158" width="6" height="14" rx="3" fill="#16A34A"/><rect x="641" y="122" width="6" height="14" rx="3" fill="#16A34A"/><rect x="641" y="86" width="6" height="14" rx="3" fill="#16A34A"/><rect x="641" y="50" width="6" height="14" rx="3" fill="#16A34A"/><line x1="262" y1="141" x2="642" y2="93" stroke="var(--blue)" stroke-width="1.8"/><line x1="262" y1="189" x2="642" y2="93" stroke="var(--rose)" stroke-width="1.8"/><circle cx="644" cy="93" r="6" fill="var(--amber)"/><text x="628" y="83" font-size="18" font-weight="700" fill="var(--amber)" text-anchor="end">M</text><text x="272" y="131" font-size="15" font-weight="700" fill="var(--blue)">S<tspan font-size="10" dy="4">1</tspan></text><text x="272" y="211" font-size="15" font-weight="700" fill="var(--rose)">S<tspan font-size="10" dy="4">2</tspan></text><line x1="222" y1="141" x2="250" y2="141" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3"/><line x1="222" y1="189" x2="250" y2="189" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3"/><line x1="234.0" y1="149.0" x2="234.0" y2="181.0" stroke="var(--amber)" stroke-width="2"/><polygon points="234.0,189.0 229.5,180.0 238.5,180.0" fill="var(--amber)"/><polygon points="234.0,141.0 238.5,150.0 229.5,150.0" fill="var(--amber)"/><text x="222" y="172" font-size="20" fill="var(--amber)" text-anchor="end" font-family="Georgia, serif" font-style="italic" font-weight="700" paint-order="stroke" stroke="#fff" stroke-width="4" stroke-linejoin="round">a</text><line x1="650" y1="165" x2="712" y2="165" stroke="var(--slate)" stroke-width="1" stroke-dasharray="3 3"/><line x1="650" y1="93" x2="712" y2="93" stroke="var(--slate)" stroke-width="1" stroke-dasharray="3 3"/><line x1="704.0" y1="157.0" x2="704.0" y2="101.0" stroke="var(--slate)" stroke-width="1.8"/><polygon points="704.0,93.0 708.5,102.0 699.5,102.0" fill="var(--slate)"/><polygon points="704.0,165.0 699.5,156.0 708.5,156.0" fill="var(--slate)"/><text x="714" y="136.0" font-size="20" fill="var(--slate)" font-family="Georgia, serif" font-style="italic" font-weight="700">x</text><line x1="650" y1="201" x2="682" y2="201" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3"/><line x1="650" y1="237" x2="682" y2="237" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3"/><line x1="674.0" y1="209.0" x2="674.0" y2="229.0" stroke="var(--amber)" stroke-width="2"/><polygon points="674.0,237.0 669.5,228.0 678.5,228.0" fill="var(--amber)"/><polygon points="674.0,201.0 678.5,210.0 669.5,210.0" fill="var(--amber)"/><text x="684" y="226.0" font-size="20" fill="var(--amber)" font-family="Georgia, serif" font-style="italic" font-weight="700">i</text><line x1="262" y1="306" x2="262" y2="330" stroke="var(--slate)" stroke-width="1" stroke-dasharray="3 3"/><line x1="640" y1="306" x2="640" y2="330" stroke="var(--slate)" stroke-width="1" stroke-dasharray="3 3"/><line x1="270.0" y1="320.0" x2="632.0" y2="320.0" stroke="var(--slate)" stroke-width="1.6"/><polygon points="640.0,320.0 631.0,324.5 631.0,315.5" fill="var(--slate)"/><polygon points="262.0,320.0 271.0,315.5 271.0,324.5" fill="var(--slate)"/><text x="451" y="312" font-size="20" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">D</text></svg>

<p class="nt-lead">Si la distance $D$ entre les trous et l'écran est telle que $D\gg a$, alors la différence de chemin optique en un point de l'écran d'abscisse $x$ est approximée par&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Expression donnée</p>
<p class="nt-f-math">$$\delta=\frac{nax}{D}$$</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>En déduire l'abscisse $x_k$ sur l'écran où apparaît la $k$<sup>e</sup> frange brillante. Et pour les franges sombres&nbsp;?</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>D'après la condition d'interférence constructive&nbsp;:</p>
<p class="nt-center">$\delta = k\lambda\quad \text{avec } k\in\mathbb{Z} \iff \dfrac{nax_k}{D} = k\lambda \;\Rightarrow\; x_k=\dfrac{k\lambda D}{na}$</p>
<p>Et pour les franges sombres, d'après la condition d'interférence destructive&nbsp;:</p>
<p class="nt-center">$\delta = \left(k+\dfrac12\right)\lambda \;\Rightarrow\; x'_k=\dfrac{\left(k+\frac12\right)\lambda D}{na}$</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp">interfrange $i$</span> sur l'écran est définie comme la distance entre le centre de deux franges brillantes (ou de deux franges sombres) <span class="imp nt-hole">consécutives</span>.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>Établir l'expression de l'interfrange $i$&nbsp;:</p>
<p class="nt-center">$\begin{aligned}i &= x_{k+1}-x_k\\ &=\frac{(k+1)\lambda D}{na}-\frac{k\lambda D}{na}\\ &=\frac{\lambda D}{na}\end{aligned}$</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$i=\frac{\lambda D}{na}$$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Si $\lambda\nearrow$, $i$ <span class="imp nt-hole">$\nearrow$</span></li>
<li>Si $a\nearrow$, $i$ <span class="imp nt-hole">$\searrow$</span></li>
<li>Si $D\nearrow$, $i$ <span class="imp nt-hole">$\nearrow$</span></li>
<li>$i$ est <span class="imp nt-hole">indépendante</span> de l'ordre d'interférence $k$</li>
</ul>
</div>

<div class="nt-lab" id="lab-young">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Les franges d'Young</p>
<canvas class="screen" style="height:70px;" aria-label="Franges d'interférence observées sur l'écran"></canvas>
<canvas class="plot" style="height:180px; margin-top:8px; background:#fff;" aria-label="Intensité lumineuse le long de l'écran avec les ordres d'interférence"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Longueur d'onde $\lambda$&nbsp;: <b class="out-l"></b><input type="range" data-p="lambda" min="400" max="750" step="5" value="635"></label>
<label class="nt-ctrl">Distance entre les trous $a$&nbsp;: <b class="out-a"></b><input type="range" data-p="a" min="0.2" max="1" step="0.02" value="0.4"></label>
<label class="nt-ctrl">Distance trous-écran $D$&nbsp;: <b class="out-D"></b><input type="range" data-p="D" min="0.5" max="3" step="0.1" value="2"></label>
<label class="nt-ctrl">Indice du milieu $n$&nbsp;: <b class="out-n"></b><input type="range" data-p="n" min="1" max="1.5" step="0.01" value="1"></label>
</div>
<div class="nt-read"><span>$i = \lambda D/(na)$ = <b class="out-i"></b></span></div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-p="env"> Tenir compte de la diffraction par chaque trou</label></div>
<p class="nt-msg">Le trait ambré sous la courbe mesure l'interfrange entre les franges d'ordre 0 et 1. En cochant la case, les franges sont modulées par la figure de diffraction de chaque trou&nbsp;: c'est ce qu'on observe réellement.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-graduation-cap"></i>Ce que dit le programme</p>
<ul class="nt-facts">
<li>Prévoir les lieux d'interférences constructives et les lieux d'interférences destructives dans le cas des trous d'Young, l'expression linéarisée de la différence de chemin optique étant donnée.</li>
<li>Établir l'expression de l'interfrange.</li>
</ul>
</div>

### Conséquences pratiques {.nt-h3}

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-headphones"></i>Casques et écouteurs à réduction de bruit active</p>
<p>Un microphone capte le bruit ambiant&nbsp;; l'électronique du casque émet aussitôt dans l'écouteur un signal de même forme mais en opposition de phase. Les deux ondes interfèrent de façon destructive au niveau de l'oreille&nbsp;: le bruit est fortement atténué.</p>
<svg class="nt-svg nt-svg-m" viewBox="0 0 560 250" role="img" aria-label="Le bruit et l'anti-bruit en opposition de phase s'additionnent pour donner un signal quasi nul"><polyline points="200.0,32.0 201.4,30.8 202.8,30.3 204.2,30.5 205.7,31.1 207.1,32.1 208.5,33.1 209.9,34.2 211.3,35.0 212.8,35.6 214.2,35.9 215.6,35.7 217.0,35.2 218.4,34.5 219.8,33.5 221.2,32.5 222.7,31.5 224.1,30.8 225.5,30.2 226.9,30.0 228.3,30.2 229.8,30.6 231.2,31.4 232.6,32.3 234.0,33.2 235.4,34.1 236.8,34.8 238.2,35.2 239.7,35.3 241.1,35.0 242.5,34.2 243.9,33.2 245.3,31.9 246.8,30.6 248.2,29.3 249.6,28.3 251.0,27.8 252.4,27.8 253.8,28.7 255.2,30.3 256.7,32.7 258.1,35.9 259.5,39.8 260.9,44.3 262.3,49.0 263.8,53.9 265.2,58.6 266.6,63.0 268.0,66.7 269.4,69.7 270.8,71.9 272.2,73.1 273.7,73.3 275.1,72.7 276.5,71.4 277.9,69.5 279.3,67.2 280.8,64.7 282.2,62.2 283.6,59.9 285.0,57.9 286.4,56.3 287.8,55.2 289.2,54.6 290.7,54.3 292.1,54.3 293.5,54.6 294.9,54.9 296.3,55.1 297.8,55.2 299.2,54.9 300.6,54.4 302.0,53.6 303.4,52.4 304.8,51.0 306.2,49.6 307.7,48.0 309.1,46.6 310.5,45.5 311.9,44.6 313.3,44.1 314.8,43.9 316.2,44.1 317.6,44.5 319.0,45.1 320.4,45.7 321.8,46.1 323.2,46.2 324.7,45.9 326.1,45.0 327.5,43.5 328.9,41.3 330.3,38.5 331.8,35.1 333.2,31.4 334.6,27.5 336.0,23.7 337.4,20.0 338.8,16.9 340.2,14.4 341.7,12.8 343.1,12.1 344.5,12.4 345.9,13.7 347.3,15.9 348.8,18.9 350.2,22.4 351.6,26.3 353.0,30.3 354.4,34.3 355.8,38.0 357.2,41.2 358.7,43.9 360.1,46.0 361.5,47.5 362.9,48.4 364.3,48.8 365.8,48.8 367.2,48.6 368.6,48.3 370.0,48.2 371.4,48.2 372.8,48.4 374.2,49.0 375.7,49.8 377.1,50.9 378.5,52.2 379.9,53.5 381.3,54.8 382.8,55.9 384.2,56.8 385.6,57.4 387.0,57.6 388.4,57.4 389.8,56.9 391.2,56.2 392.7,55.4 394.1,54.6 395.5,54.0 396.9,53.7 398.3,53.8 399.8,54.4 401.2,55.6 402.6,57.2 404.0,59.2 405.4,61.5 406.8,64.0 408.2,66.3 409.7,68.4 411.1,70.0 412.5,71.0 413.9,71.1 415.3,70.3 416.8,68.6 418.2,66.0 419.6,62.6 421.0,58.4 422.4,53.8 423.8,49.0 425.2,44.1 426.7,39.5 428.1,35.3 429.5,31.7 430.9,28.8 432.3,26.7 433.8,25.4 435.2,24.9 436.6,25.1 438.0,25.8 439.4,26.8 440.8,28.1 442.2,29.3 443.7,30.5 445.1,31.4 446.5,32.0 447.9,32.2 449.3,32.2 450.8,31.9 452.2,31.4 453.6,30.9 455.0,30.4 456.4,30.1 457.8,30.1 459.2,30.4 460.7,31.0 462.1,32.0 463.5,33.2 464.9,34.6 466.3,36.1 467.8,37.4 469.2,38.6 470.6,39.4 472.0,39.9 473.4,39.9 474.8,39.4 476.2,38.6 477.7,37.5 479.1,36.3 480.5,35.1 481.9,34.1 483.3,33.5 484.8,33.5 486.2,34.1 487.6,35.6 489.0,37.8 490.4,40.8 491.8,44.5 493.2,48.7 494.7,53.2 496.1,57.9 497.5,62.4 498.9,66.5 500.3,70.1 501.8,72.9 503.2,74.9 504.6,75.9 506.0,75.9 507.4,75.1 508.8,73.5 510.2,71.3 511.7,68.6 513.1,65.8 514.5,62.9 515.9,60.1 517.3,57.7 518.8,55.6 520.2,54.0 521.6,52.9 523.0,52.1 524.4,51.7 525.8,51.4 527.2,51.3 528.7,51.1 530.1,50.8 531.5,50.2 532.9,49.4 534.3,48.3 535.8,46.9 537.2,45.3 538.6,43.7 540.0,42.0" fill="none" stroke="var(--rose)" stroke-width="2.4"/><polyline points="200.0,138.0 201.4,139.2 202.8,139.7 204.2,139.5 205.7,138.9 207.1,137.9 208.5,136.9 209.9,135.8 211.3,135.0 212.8,134.4 214.2,134.1 215.6,134.3 217.0,134.8 218.4,135.5 219.8,136.5 221.2,137.5 222.7,138.5 224.1,139.2 225.5,139.8 226.9,140.0 228.3,139.8 229.8,139.4 231.2,138.6 232.6,137.7 234.0,136.8 235.4,135.9 236.8,135.2 238.2,134.8 239.7,134.7 241.1,135.0 242.5,135.8 243.9,136.8 245.3,138.1 246.8,139.4 248.2,140.7 249.6,141.7 251.0,142.2 252.4,142.2 253.8,141.3 255.2,139.7 256.7,137.3 258.1,134.1 259.5,130.2 260.9,125.7 262.3,121.0 263.8,116.1 265.2,111.4 266.6,107.0 268.0,103.3 269.4,100.3 270.8,98.1 272.2,96.9 273.7,96.7 275.1,97.3 276.5,98.6 277.9,100.5 279.3,102.8 280.8,105.3 282.2,107.8 283.6,110.1 285.0,112.1 286.4,113.7 287.8,114.8 289.2,115.4 290.7,115.7 292.1,115.7 293.5,115.4 294.9,115.1 296.3,114.9 297.8,114.8 299.2,115.1 300.6,115.6 302.0,116.4 303.4,117.6 304.8,119.0 306.2,120.4 307.7,122.0 309.1,123.4 310.5,124.5 311.9,125.4 313.3,125.9 314.8,126.1 316.2,125.9 317.6,125.5 319.0,124.9 320.4,124.3 321.8,123.9 323.2,123.8 324.7,124.1 326.1,125.0 327.5,126.5 328.9,128.7 330.3,131.5 331.8,134.9 333.2,138.6 334.6,142.5 336.0,146.3 337.4,150.0 338.8,153.1 340.2,155.6 341.7,157.2 343.1,157.9 344.5,157.6 345.9,156.3 347.3,154.1 348.8,151.1 350.2,147.6 351.6,143.7 353.0,139.7 354.4,135.7 355.8,132.0 357.2,128.8 358.7,126.1 360.1,124.0 361.5,122.5 362.9,121.6 364.3,121.2 365.8,121.2 367.2,121.4 368.6,121.7 370.0,121.8 371.4,121.8 372.8,121.6 374.2,121.0 375.7,120.2 377.1,119.1 378.5,117.8 379.9,116.5 381.3,115.2 382.8,114.1 384.2,113.2 385.6,112.6 387.0,112.4 388.4,112.6 389.8,113.1 391.2,113.8 392.7,114.6 394.1,115.4 395.5,116.0 396.9,116.3 398.3,116.2 399.8,115.6 401.2,114.4 402.6,112.8 404.0,110.8 405.4,108.5 406.8,106.0 408.2,103.7 409.7,101.6 411.1,100.0 412.5,99.0 413.9,98.9 415.3,99.7 416.8,101.4 418.2,104.0 419.6,107.4 421.0,111.6 422.4,116.2 423.8,121.0 425.2,125.9 426.7,130.5 428.1,134.7 429.5,138.3 430.9,141.2 432.3,143.3 433.8,144.6 435.2,145.1 436.6,144.9 438.0,144.2 439.4,143.2 440.8,141.9 442.2,140.7 443.7,139.5 445.1,138.6 446.5,138.0 447.9,137.8 449.3,137.8 450.8,138.1 452.2,138.6 453.6,139.1 455.0,139.6 456.4,139.9 457.8,139.9 459.2,139.6 460.7,139.0 462.1,138.0 463.5,136.8 464.9,135.4 466.3,133.9 467.8,132.6 469.2,131.4 470.6,130.6 472.0,130.1 473.4,130.1 474.8,130.6 476.2,131.4 477.7,132.5 479.1,133.7 480.5,134.9 481.9,135.9 483.3,136.5 484.8,136.5 486.2,135.9 487.6,134.4 489.0,132.2 490.4,129.2 491.8,125.5 493.2,121.3 494.7,116.8 496.1,112.1 497.5,107.6 498.9,103.5 500.3,99.9 501.8,97.1 503.2,95.1 504.6,94.1 506.0,94.1 507.4,94.9 508.8,96.5 510.2,98.7 511.7,101.4 513.1,104.2 514.5,107.1 515.9,109.9 517.3,112.3 518.8,114.4 520.2,116.0 521.6,117.1 523.0,117.9 524.4,118.3 525.8,118.6 527.2,118.7 528.7,118.9 530.1,119.2 531.5,119.8 532.9,120.6 534.3,121.7 535.8,123.1 537.2,124.7 538.6,126.3 540.0,128.0" fill="none" stroke="var(--blue)" stroke-width="2.4"/><polyline points="200.0,204.5 201.4,204.4 202.8,204.4 204.2,204.5 205.7,204.6 207.1,204.6 208.5,204.6 209.9,204.6 211.3,204.6 212.8,204.5 214.2,204.4 215.6,204.4 217.0,204.4 218.4,204.5 219.8,204.5 221.2,204.6 222.7,204.6 224.1,204.6 225.5,204.5 226.9,204.5 228.3,204.4 229.8,204.3 231.2,204.3 232.6,204.4 234.0,204.6 235.4,204.9 236.8,205.2 238.2,205.5 239.7,205.8 241.1,206.0 242.5,206.1 243.9,206.1 245.3,206.0 246.8,205.9 248.2,205.7 249.6,205.6 251.0,205.4 252.4,205.4 253.8,205.4 255.2,205.4 256.7,205.4 258.1,205.4 259.5,205.4 260.9,205.3 262.3,205.2 263.8,205.1 265.2,205.0 266.6,205.0 268.0,205.0 269.4,205.0 270.8,205.0 272.2,205.1 273.7,205.0 275.1,204.9 276.5,204.8 277.9,204.5 279.3,204.3 280.8,204.0 282.2,203.8 283.6,203.7 285.0,203.7 286.4,203.8 287.8,204.0 289.2,204.3 290.7,204.5 292.1,204.8 293.5,205.0 294.9,205.1 296.3,205.1 297.8,205.1 299.2,205.1 300.6,205.1 302.0,205.1 303.4,205.2 304.8,205.3 306.2,205.4 307.7,205.4 309.1,205.5 310.5,205.5 311.9,205.5 313.3,205.4 314.8,205.4 316.2,205.3 317.6,205.4 319.0,205.5 320.4,205.6 321.8,205.8 323.2,205.9 324.7,206.0 326.1,206.0 327.5,205.9 328.9,205.7 330.3,205.5 331.8,205.1 333.2,204.8 334.6,204.5 336.0,204.3 337.4,204.2 338.8,204.2 340.2,204.2 341.7,204.3 343.1,204.4 344.5,204.5 345.9,204.5 347.3,204.5 348.8,204.4 350.2,204.4 351.6,204.4 353.0,204.4 354.4,204.5 355.8,204.6 357.2,204.7 358.7,204.8 360.1,204.8 361.5,204.8 362.9,204.7 364.3,204.6 365.8,204.6 367.2,204.5 368.6,204.6 370.0,204.7 371.4,204.9 372.8,205.2 374.2,205.5 375.7,205.8 377.1,206.1 378.5,206.2 379.9,206.2 381.3,206.2 382.8,206.0 384.2,205.8 385.6,205.6 387.0,205.5 388.4,205.4 389.8,205.3 391.2,205.3 392.7,205.3 394.1,205.2 395.5,205.2 396.9,205.1 398.3,205.0 399.8,204.9 401.2,204.8 402.6,204.7 404.0,204.7 405.4,204.7 406.8,204.8 408.2,204.9 409.7,204.9 411.1,204.9 412.5,204.8 413.9,204.6 415.3,204.4 416.8,204.1 418.2,203.9 419.6,203.8 421.0,203.7 422.4,203.8 423.8,204.0 425.2,204.3 426.7,204.5 428.1,204.8 429.5,205.1 430.9,205.2 432.3,205.3 433.8,205.4 435.2,205.4 436.6,205.4 438.0,205.4 439.4,205.4 440.8,205.4 442.2,205.5 443.7,205.6 445.1,205.6 446.5,205.6 447.9,205.6 449.3,205.5 450.8,205.4 452.2,205.3 453.6,205.3 455.0,205.3 456.4,205.4 457.8,205.5 459.2,205.7 460.7,205.8 462.1,205.9 463.5,205.8 464.9,205.7 466.3,205.4 467.8,205.1 469.2,204.8 470.6,204.5 472.0,204.2 473.4,204.1 474.8,204.0 476.2,204.0 477.7,204.1 479.1,204.2 480.5,204.3 481.9,204.4 483.3,204.4 484.8,204.4 486.2,204.4 487.6,204.4 489.0,204.5 490.4,204.6 491.8,204.7 493.2,204.8 494.7,204.9 496.1,205.0 497.5,205.0 498.9,205.0 500.3,204.9 501.8,204.8 503.2,204.8 504.6,204.8 506.0,204.8 507.4,205.0 508.8,205.2 510.2,205.5 511.7,205.8 513.1,206.0 514.5,206.2 515.9,206.3 517.3,206.2 518.8,206.1 520.2,205.9 521.6,205.7 523.0,205.5 524.4,205.3 525.8,205.2 527.2,205.1 528.7,205.1 530.1,205.0 531.5,205.0 532.9,204.9 534.3,204.8 535.8,204.7 537.2,204.6 538.6,204.5 540.0,204.5" fill="none" stroke="var(--emerald)" stroke-width="2.4"/><text x="10" y="50" font-size="14" font-weight="700" fill="var(--rose)">bruit ambiant</text><text x="10" y="130" font-size="14" font-weight="700" fill="var(--blue)">anti-bruit émis</text><text x="10" y="210" font-size="14" font-weight="700" fill="var(--emerald)">ce qu'entend l'oreille</text><text x="190" y="92" font-size="20" font-weight="700" fill="var(--slate)" text-anchor="end">+</text><line x1="200" y1="166" x2="540" y2="166" stroke="var(--line)" stroke-width="2"/></svg>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-feather"></i>Couleurs interférentielles</p>
<p>Les reflets métalliques et changeants (irisations) de certains oiseaux, comme l'ibis chauve, proviennent du très faible écartement des barbules de leurs plumes&nbsp;: la lumière réfléchie par ces structures interfère, et la couleur renforcée dépend de l'angle d'observation.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi les bulles de savon sont-elles irisées&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Une bulle de savon est une couche d'eau savonneuse de quelques centaines de nanomètres d'épaisseur. La lumière se réfléchit en partie sur sa face extérieure, en partie sur sa face intérieure&nbsp;: les deux ondes réfléchies ont parcouru des chemins différents et interfèrent.</p>
<p>Selon l'épaisseur locale de la couche, certaines longueurs d'onde (donc certaines couleurs) interfèrent de façon constructive, d'autres de façon destructive&nbsp;: d'où les bandes colorées qui bougent quand l'épaisseur varie. C'est le même phénomène pour les taches de carburant sur le bitume mouillé.</p>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-satellite-dish"></i>Interférométrie</p>
<p>Utilisée en astronomie, métrologie, océanographie, séismologie, etc. (<a href="https://coursphychi.github.io/act-volcan.pdf">cf. exercice «&nbsp;interférométrie et volcan&nbsp;»</a>), et dans de nombreuses expériences scientifiques (comme celle de Michelson et Morley à la fin du 19<sup>e</sup> siècle).</p>
<p>Grâce à l'interférométrie, un réseau de télescopes ou radiotélescopes atteint une résolution équivalente à celle d'un miroir (ou radiotélescope) de diamètre équivalent à l'écart entre les instruments combinés. Par exemple, les 27 antennes de 25&nbsp;m du <i>Very Large Array</i> (Nouveau-Mexique), réparties sur une trentaine de kilomètres, ont la résolution d'une antenne unique de cette taille.</p>
<p><a href="https://www.canal-u.tv/chaines/cerimes/l-interferometrie-au-service-de-l-astronomie" target="_blank" rel="noopener">Pour aller plus loin sur les télescopes</a></p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-wave-square"></i>Ondes gravitationnelles</p>
<p>La détection des ondes gravitationnelles utilise aussi l'interférométrie (<a href="https://coursphychi.github.io/act-ondesgrav.pdf">cf. exercice «&nbsp;interféromètre gravitationnel&nbsp;»</a>).</p>
<p><a href="https://www.ligo.caltech.edu/video/ligo20160211v2" target="_blank" rel="noopener">La première détection</a> date de septembre 2015 (annoncée en février 2016) et elle s'est faite grâce à un interféromètre ayant des bras de 4&nbsp;km de long&nbsp;! En Europe, l'interféromètre Virgo, près de Pise, possède des bras de 3&nbsp;km.</p>
</div>

### Battements (hors programme) {.nt-h3} 

<p class="nt-lead">Enfin, si on décale légèrement la fréquence des sources, on observe non plus seulement des franges dans l'espace mais aussi dans le temps.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On les appelle <span class="imp nt-hole">battements</span>. On les utilise par exemple pour accorder les instruments.</p>
</div>

<div class="nt-lab" id="lab-batt">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Accorder deux diapasons</p>
<p class="nt-note">Le premier son est un la à 440&nbsp;Hz&nbsp;; réglez la fréquence du second et écoutez le résultat (baissez d'abord le volume).</p>
<canvas style="height:200px;" aria-label="Somme des deux signaux sur une seconde, avec son enveloppe"></canvas>
<label class="nt-ctrl">Fréquence du second son&nbsp;: <b class="out-f2"></b><input type="range" data-p="f2" min="430" max="450" step="0.5" value="443"></label>
<div class="nt-read"><span>fréquence des battements = <b class="out-fb"></b></span><span>période des battements = <b class="out-tb"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="listen"><i class="fa-solid fa-volume-high"></i>&nbsp; Écouter</button></div>
<p class="nt-msg">Le son résultant enfle et faiblit périodiquement. Quand les deux fréquences deviennent égales, les battements disparaissent&nbsp;: l'instrument est accordé.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque&nbsp;: un battement visuel</p>
<p>Sur le graphique ci-dessus, de petits fuseaux apparaissent à l'intérieur de l'enveloppe&nbsp;: ils n'existent pas dans le son&nbsp;! Pour représenter 440 oscillations par seconde, l'écran ne dispose que d'un nombre limité de colonnes de pixels&nbsp;: le signal n'est «&nbsp;relevé&nbsp;» qu'à intervalles réguliers. La fréquence du signal «&nbsp;bat&nbsp;» alors avec la fréquence de ces relevés, et un motif lent apparaît. C'est le <b>repliement de spectre</b> (<i>aliasing</i> en anglais)&nbsp;: redimensionnez la fenêtre, et ces fuseaux changent de forme, alors que les vrais battements restent les mêmes.</p>
<p>C'est le même phénomène qui fait tourner à l'envers les roues d'une voiture filmée, ou qui fait apparaître des motifs ondulés (le moiré) quand on photographie un écran ou une chemise rayée. Le moiré est un battement dans l'espace&nbsp;: deux réseaux de traits de pas voisins se superposent.</p>
</div>

<div class="nt-lab" id="lab-moire">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le moiré, des battements dans l'espace</p>
<canvas style="height:236px;" aria-label="Deux réseaux de traits de pas voisins et leur superposition, qui fait apparaître un motif de moiré"></canvas>
<label class="nt-ctrl">Pas du réseau 2&nbsp;: <b class="out-p2"></b><input type="range" data-p="p2" min="8" max="12" step="0.05" value="10.5"></label>
<div class="nt-read"><span>Motif de moiré&nbsp;: <b class="out-n"></b></span></div>
<p class="nt-msg">Là où les traits des deux réseaux coïncident, la lumière passe (bandes claires)&nbsp;; là où ils s'intercalent, ils bouchent tout (bandes sombres). Plus les deux pas sont proches, plus le motif est grand&nbsp;: exactement comme les battements, dont la période augmente quand les deux fréquences se rapprochent.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La fréquence des battements</span></summary>
<div class="nt-d-body">
<p>Les deux signaux passent alternativement d'en phase (son fort) à opposition de phase (son faible). Le nombre de battements par seconde est égal à l'écart des deux fréquences&nbsp;:</p>
<p class="nt-center">$f_{\text{batt}} = \left|f_1 - f_2\right|$</p>
<p>Avec $f_1 = \pu{440 Hz}$ et $f_2 = \pu{443 Hz}$, on entend 3 battements par seconde.</p>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
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
  /* longueur d'onde (nm) -> couleur RGB approchée */
  function lambdaRGB(nm) {
    var r = 0, g = 0, b = 0;
    if (nm < 440) { r = -(nm - 440) / 60; b = 1; }
    else if (nm < 490) { g = (nm - 440) / 50; b = 1; }
    else if (nm < 510) { g = 1; b = -(nm - 510) / 20; }
    else if (nm < 580) { r = (nm - 510) / 70; g = 1; }
    else if (nm < 645) { r = 1; g = -(nm - 645) / 65; }
    else { r = 1; }
    var f = nm < 420 ? 0.3 + 0.7 * (nm - 380) / 40 : (nm > 700 ? 0.3 + 0.7 * (780 - nm) / 80 : 1);
    return [Math.round(255 * Math.pow(r * f, 0.8)), Math.round(255 * Math.pow(g * f, 0.8)), Math.round(255 * Math.pow(b * f, 0.8))];
  }
  function rgbStr(c, a) { return 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + (a === undefined ? 1 : a) + ')'; }
  /* palette « eau » : creux bleu nuit, crêtes bleu très clair */
  var WATER = (function () {
    var lo = [11, 37, 77], mid = [42, 107, 196], hi = [226, 240, 255], tab = [];
    for (var i = 0; i < 256; i++) {
      var t = i / 255 * 2 - 1, c;
      if (t < 0) { c = [lo[0] + (mid[0] - lo[0]) * (t + 1), lo[1] + (mid[1] - lo[1]) * (t + 1), lo[2] + (mid[2] - lo[2]) * (t + 1)]; }
      else { c = [mid[0] + (hi[0] - mid[0]) * t, mid[1] + (hi[1] - mid[1]) * t, mid[2] + (hi[2] - mid[2]) * t]; }
      tab.push([c[0] | 0, c[1] | 0, c[2] | 0]);
    }
    return tab;
  })();
  function tanh(x) { var e = Math.exp(2 * x); return (e - 1) / (e + 1); }
  /* ================= 1. Cuve à ondes : diffraction par une ouverture ================= */
  (function () {
    var root = document.getElementById('lab-cuve');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rA = $(root, '[data-p="a"]'), rL = $(root, '[data-p="lambda"]');
    var oA = $(root, '.out-a'), oL = $(root, '.out-l'), oR = $(root, '.out-r'), btn = $(root, '[data-act="play"]');
    var GW = 240, GH = 150, WX = 24, WY = 15, XW = 7, TH = 0.4;
    var off = document.createElement('canvas'); off.width = GW; off.height = GH;
    var octx = off.getContext('2d'), img = octx.createImageData(GW, GH);
    var RE = new Float32Array(GW * GH), IM = new Float32Array(GW * GH), MASK = new Uint8Array(GW * GH);
    var S = null, playing = !RM, visible = true, t = 0, last = null, dirty = true;
    function compute() {
      var a = parseFloat(rA.value), lam = parseFloat(rL.value), k = 2 * Math.PI / lam;
      var N = Math.min(60, Math.max(1, Math.ceil(a / (lam / 6)))), dy = a / N, yc = WY / 2;
      var norm = dy / Math.sqrt(lam), ph0 = k * (XW + TH) - Math.PI / 4;
      for (var j = 0; j < GH; j++) {
        var y = (j + 0.5) * WY / GH;
        for (var i = 0; i < GW; i++) {
          var x = (i + 0.5) * WX / GW, p = j * GW + i;
          if (x < XW) { RE[p] = Math.cos(k * x); IM[p] = Math.sin(k * x); MASK[p] = 0; continue; }
          if (x < XW + TH) { MASK[p] = (Math.abs(y - yc) > a / 2) ? 1 : 0; RE[p] = Math.cos(k * x); IM[p] = Math.sin(k * x); continue; }
          MASK[p] = 0;
          var sr = 0, si = 0;
          for (var n = 0; n < N; n++) {
            var ys = yc - a / 2 + (n + 0.5) * dy, dx = x - (XW + TH), dd = y - ys;
            var r = Math.max(0.25, Math.sqrt(dx * dx + dd * dd)), amp = 1 / Math.sqrt(r), phs = k * r + ph0;
            sr += amp * Math.cos(phs); si += amp * Math.sin(phs);
          }
          RE[p] = sr * norm; IM[p] = si * norm;
        }
      }
      oA.textContent = fr(a, 1) + ' cm'; oL.textContent = fr(lam, 1) + ' cm'; oR.textContent = fr(a / lam, 1);
      dirty = false;
    }
    function draw() {
      if (!S) { return; }
      if (dirty) { compute(); }
      var om = 2 * Math.PI * 0.8, c = Math.cos(om * t), s = Math.sin(om * t), d = img.data;
      for (var p = 0; p < GW * GH; p++) {
        var q = p * 4;
        if (MASK[p]) { d[q] = 51; d[q + 1] = 65; d[q + 2] = 85; d[q + 3] = 255; continue; }
        var v = tanh(1.5 * (RE[p] * c + IM[p] * s)), cc = WATER[Math.max(0, Math.min(255, ((v + 1) * 127.5) | 0))];
        d[q] = cc[0]; d[q + 1] = cc[1]; d[q + 2] = cc[2]; d[q + 3] = 255;
      }
      octx.putImageData(img, 0, 0);
      var ctx = S.ctx; ctx.imageSmoothingEnabled = true;
      ctx.drawImage(off, 0, 0, S.w, S.h);
      /* limites de l'ombre géométrique */
      var a = parseFloat(rA.value), sx = S.w / WX, sy = S.h / WY, x0 = (XW + TH) * sx;
      ctx.strokeStyle = 'rgba(255,255,255,.75)'; ctx.setLineDash([6, 5]); ctx.lineWidth = 1.5;
      [WY / 2 - a / 2, WY / 2 + a / 2].forEach(function (yy) { ctx.beginPath(); ctx.moveTo(x0, yy * sy); ctx.lineTo(S.w, yy * sy); ctx.stroke(); });
      ctx.setLineDash([]);
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts;
      if (visible && (playing || dirty)) { draw(); }
      requestAnimationFrame(step);
    }
    function label() { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
    btn.addEventListener('click', function () { playing = !playing; label(); });
    [rA, rL].forEach(function (r) { r.addEventListener('input', function () { dirty = true; if (!playing) { draw(); } }); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    label(); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 2. Fente éclairée par un laser ================= */
  (function () {
    var root = document.getElementById('lab-fente');
    if (!root) { return; }
    var cvE = $(root, 'canvas.screen'), cvP = $(root, 'canvas.plot');
    var rL = $(root, '[data-p="lambda"]'), rA = $(root, '[data-p="a"]'), rD = $(root, '[data-p="D"]');
    var oL = $(root, '.out-l'), oA = $(root, '.out-a'), oD = $(root, '.out-D'), oT = $(root, '.out-t'), oW = $(root, '.out-L');
    var XMAX = 0.15, SE, SP;
    function I(x, lam, a, D) { var u = Math.PI * a * x / (lam * D); return Math.abs(u) < 1e-9 ? 1 : Math.pow(Math.sin(u) / u, 2); }
    function draw() {
      var lam = parseFloat(rL.value) * 1e-9, a = parseFloat(rA.value) * 1e-6, D = parseFloat(rD.value);
      var rgb = lambdaRGB(parseFloat(rL.value)), L = 2 * lam * D / a, th = lam / a;
      oL.textContent = rL.value + ' nm'; oA.textContent = rA.value + ' µm'; oD.textContent = fr(D, 1) + ' m';
      oT.textContent = fr(th * 1000, 1) + ' mrad'; oW.textContent = fr(L * 100, 1) + ' cm';
      /* écran */
      var c = SE.ctx, w = SE.w, h = SE.h;
      c.fillStyle = '#0B1220'; c.fillRect(0, 0, w, h);
      for (var px = 0; px < w; px++) {
        var x = (px / (w - 1) * 2 - 1) * XMAX, v = Math.pow(I(x, lam, a, D), 0.45);
        c.fillStyle = rgbStr(rgb, v); c.fillRect(px, 0, 1, h);
      }
      var g = c.createLinearGradient(0, 0, 0, h);
      g.addColorStop(0, 'rgba(11,18,32,.85)'); g.addColorStop(0.3, 'rgba(11,18,32,0)'); g.addColorStop(0.7, 'rgba(11,18,32,0)'); g.addColorStop(1, 'rgba(11,18,32,.85)');
      c.fillStyle = g; c.fillRect(0, 0, w, h);
      /* profil */
      var p = SP.ctx, W = SP.w, H = SP.h, base = H - 26, top = 10;
      p.clearRect(0, 0, W, H);
      p.strokeStyle = col('--line'); p.lineWidth = 1; p.beginPath(); p.moveTo(0, base); p.lineTo(W, base); p.stroke();
      p.fillStyle = col('--muted'); p.font = '11px system-ui, sans-serif'; p.textAlign = 'center';
      [-15, -10, -5, 0, 5, 10, 15].forEach(function (cm) {
        var X = (cm / 100 / XMAX + 1) / 2 * (W - 1);
        p.fillText(cm + ' cm', Math.min(W - 18, Math.max(18, X)), H - 8);
      });
      p.strokeStyle = rgbStr([Math.min(200, rgb[0]), Math.min(200, rgb[1]), Math.min(200, rgb[2])]); p.lineWidth = 2.2; p.beginPath();
      for (var q = 0; q < W; q++) {
        var xx = (q / (W - 1) * 2 - 1) * XMAX, y = base - (base - top) * I(xx, lam, a, D);
        if (q === 0) { p.moveTo(q, y); } else { p.lineTo(q, y); }
      }
      p.stroke();
      /* largeur L */
      var x1 = (-L / 2 / XMAX + 1) / 2 * (W - 1), x2 = (L / 2 / XMAX + 1) / 2 * (W - 1), yb = base - 6;
      p.strokeStyle = col('--rose'); p.fillStyle = col('--rose'); p.lineWidth = 2;
      p.beginPath(); p.moveTo(x1, yb); p.lineTo(x2, yb); p.stroke();
      [x1, x2].forEach(function (xx) { p.beginPath(); p.moveTo(xx, yb - 6); p.lineTo(xx, yb + 6); p.stroke(); });
      p.font = '700 13px system-ui, sans-serif'; p.fillText('L', (x1 + x2) / 2, yb - 9);
    }
    [rL, rA, rD].forEach(function (r) { r.addEventListener('input', draw); });
    function setup() { SE = canvasCtx(cvE); SP = canvasCtx(cvP); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 3. Forme de l'ouverture -> figure de diffraction (FFT 2D) ================= */
  (function () {
    var root = document.getElementById('lab-formes');
    if (!root) { return; }
    var cvA = $(root, 'canvas.ap'), cvF = $(root, 'canvas.fig'), rS = $(root, '[data-p="s"]'), oS = $(root, '.out-s'), msg = $(root, '.nt-msg');
    var N = 256, LOG = 8, CROP = 128;
    var re = new Float64Array(N * N), im = new Float64Array(N * N);
    var rev = new Uint16Array(N), cs = new Float64Array(N / 2), sn = new Float64Array(N / 2);
    for (var i = 0; i < N; i++) { var r = 0; for (var b = 0; b < LOG; b++) { r = (r << 1) | ((i >> b) & 1); } rev[i] = r; }
    for (var m = 0; m < N / 2; m++) { cs[m] = Math.cos(-2 * Math.PI * m / N); sn[m] = Math.sin(-2 * Math.PI * m / N); }
    var tr = new Float64Array(N), ti = new Float64Array(N);
    function fft1(off, stride) {
      for (var i = 0; i < N; i++) { tr[rev[i]] = re[off + i * stride]; ti[rev[i]] = im[off + i * stride]; }
      for (var size = 2; size <= N; size <<= 1) {
        var half = size >> 1, st = N / size;
        for (var s = 0; s < N; s += size) {
          for (var j = 0; j < half; j++) {
            var wr = cs[j * st], wi = sn[j * st], a = s + j, b2 = a + half;
            var xr = tr[b2] * wr - ti[b2] * wi, xi = tr[b2] * wi + ti[b2] * wr;
            tr[b2] = tr[a] - xr; ti[b2] = ti[a] - xi; tr[a] += xr; ti[a] += xi;
          }
        }
      }
      for (var k = 0; k < N; k++) { re[off + k * stride] = tr[k]; im[off + k * stride] = ti[k]; }
    }
    var SQ3 = Math.sqrt(3), shape = 'fente';
    var DESC = {
      fente: 'Fente verticale : la lumière s\u2019étale horizontalement, perpendiculairement à la fente.',
      carre: 'Ouverture carrée : deux directions d\u2019étalement, perpendiculaires aux côtés du carré.',
      disque: 'Ouverture circulaire : tache d\u2019Airy entourée d\u2019anneaux (cas d\u2019une lunette ou d\u2019un télescope sans support).',
      hexagone: 'Ouverture hexagonale : six aigrettes, perpendiculaires aux six côtés.',
      grille: 'Grille de petits carrés (comme les pixels d\u2019un écran) : un réseau de taches régulièrement espacées.',
      hubble: 'Hubble : miroir circulaire, miroir secondaire au centre et 4 tiges en croix, d\u2019où 4 aigrettes.',
      webb: 'Webb : 18 segments hexagonaux et 3 tiges, d\u2019où 6 grandes aigrettes et 2 plus petites (horizontales).'
    };
    function inside(x, y, s) {
      var R = s / 2, rr = Math.sqrt(x * x + y * y), ax = Math.abs(x), ay = Math.abs(y);
      switch (shape) {
        case 'fente': return ax <= Math.max(1, s / 10) && ay <= s * 0.9;
        case 'carre': return ax <= R && ay <= R;
        case 'disque': return rr <= R;
        case 'hexagone': return ay <= SQ3 / 2 * R && ax <= R - ay / SQ3;
        case 'grille':
          if (ax > R || ay > R) { return false; }
          var p = s / 6, u = ((x % p) + p) % p, v = ((y % p) + p) % p;
          return u < p * 0.55 && v < p * 0.55;
        case 'hubble':
          return rr <= R && rr >= 0.33 * R && ax > 0.8 && ay > 0.8;
        case 'webb':
          if (rr > R * 1.8) { return false; }
          var rho = R / 2.6, best = false;
          for (var q = -2; q <= 2 && !best; q++) {
            for (var r2 = -2; r2 <= 2 && !best; r2++) {
              var s3 = -q - r2;
              if (Math.max(Math.abs(q), Math.abs(r2), Math.abs(s3)) === 0 || Math.max(Math.abs(q), Math.abs(r2), Math.abs(s3)) > 2) { continue; }
              var cx = rho * 1.5 * q, cy = rho * SQ3 * (r2 + q / 2), dx = Math.abs(x - cx), dy = Math.abs(y - cy), rp = rho - 0.12;
              if (dy <= SQ3 / 2 * rp && dx <= rp - dy / SQ3) { best = true; }
            }
          }
          if (!best) { return false; }
          /* trois tiges : deux vers le haut (60° et 120°), une vers le bas */
          var dist60 = Math.abs(-y * Math.cos(Math.PI / 3) - x * Math.sin(Math.PI / 3));
          var dist120 = Math.abs(-y * Math.cos(2 * Math.PI / 3) - x * Math.sin(2 * Math.PI / 3));
          if (-y > 0 && x > 0 && dist60 < 0.6) { return false; }
          if (-y > 0 && x < 0 && dist120 < 0.6) { return false; }
          if (-y < 0 && ax < 0.6) { return false; }
          return true;
      }
      return false;
    }
    var SA, SF;
    function draw() {
      var s = parseFloat(rS.value);
      if (shape === 'webb') { s = 70; } else if (shape === 'hubble') { s = Math.max(s, 60); }
      oS.textContent = Math.round(parseFloat(rS.value)) + ' u.a.';
      msg.textContent = DESC[shape];
      var SS = shape === 'webb' ? 4 : 2;
      for (var j = 0; j < N; j++) {
        for (var i = 0; i < N; i++) {
          var x = i - N / 2 + 0.5, y = j - N / 2 + 0.5, p = j * N + i, v = 0;
          /* sur-échantillonnage (4x4 pour Webb, dont les joints sont très fins) */
          for (var a = 0; a < SS; a++) { for (var b = 0; b < SS; b++) { if (inside(x + (a + 0.5) / SS - 0.5, y + (b + 0.5) / SS - 0.5, s)) { v += 1 / (SS * SS); } } }
          re[p] = v; im[p] = 0;
        }
      }
      /* aperçu de l'ouverture */
      var ca = SA.ctx, ia = ca.createImageData(CROP, CROP);
      for (var jj = 0; jj < CROP; jj++) {
        for (var ii = 0; ii < CROP; ii++) {
          var vv = re[(jj + (N - CROP) / 2) * N + ii + (N - CROP) / 2], q = (jj * CROP + ii) * 4;
          ia.data[q] = 20 + 230 * vv; ia.data[q + 1] = 30 + 225 * vv; ia.data[q + 2] = 48 + 207 * vv; ia.data[q + 3] = 255;
        }
      }
      paint(SA, ia);
      for (var row = 0; row < N; row++) { fft1(row * N, 1); }
      for (var c = 0; c < N; c++) { fft1(c, N); }
      var mx = 0, P = new Float64Array(N * N);
      for (var k = 0; k < N * N; k++) { P[k] = re[k] * re[k] + im[k] * im[k]; if (P[k] > mx) { mx = P[k]; } }
      var CR = shape === 'hubble' ? 96 : CROP, DYN = shape === 'hubble' ? 1e4 : 2e3, PHOTO = shape === 'webb';
      var cf = SF.ctx, id = cf.createImageData(CR, CR);
      for (var y2 = 0; y2 < CR; y2++) {
        for (var x2 = 0; x2 < CR; x2++) {
          var sx = (x2 - CR / 2 + N) % N, sy = (y2 - CR / 2 + N) % N;
          /* Webb : rendu « photographique » saturé, comme sur les images du télescope */
          var val = PHOTO ? Math.pow(P[sy * N + sx] / (0.05 * mx), 0.3) : Math.log10(1 + DYN * P[sy * N + sx] / mx) / Math.log10(DYN + 1), o = (y2 * CR + x2) * 4;
          val = Math.max(0, Math.min(1, val));
          var rC, gC, bC;
          if (val < 0.5) { var t2 = val / 0.5; rC = 8 + 34 * t2; gC = 12 + 95 * t2; bC = 28 + 168 * t2; }
          else { var t3 = (val - 0.5) / 0.5; rC = 42 + 213 * t3; gC = 107 + 148 * t3; bC = 196 + 59 * t3; }
          id.data[o] = rC; id.data[o + 1] = gC; id.data[o + 2] = bC; id.data[o + 3] = 255;
        }
      }
      paint(SF, id);
    }
    function paint(S, imgData) {
      var o = document.createElement('canvas'); o.width = imgData.width; o.height = imgData.height;
      o.getContext('2d').putImageData(imgData, 0, 0);
      S.ctx.imageSmoothingEnabled = true; S.ctx.clearRect(0, 0, S.w, S.h);
      S.ctx.drawImage(o, 0, 0, S.w, S.h);
    }
    var pending = false;
    function schedule() { if (!pending) { pending = true; requestAnimationFrame(function () { pending = false; draw(); }); } }
    Array.prototype.forEach.call(root.querySelectorAll('input[name="forme"]'), function (r) {
      r.addEventListener('change', function () { shape = r.value; schedule(); });
    });
    rS.addEventListener('input', schedule);
    function setup() { SA = canvasCtx(cvA); SF = canvasCtx(cvF); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 4. Résolution d'un télescope (deux étoiles) ================= */
  (function () {
    var root = document.getElementById('lab-resol');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rD = $(root, '[data-p="D"]'), oD = $(root, '.out-D'), oT = $(root, '.out-t'), msg = $(root, '.nt-msg');
    function J1(x) {
      var ax = Math.abs(x), y, a1, a2;
      if (ax < 8) {
        y = x * x;
        a1 = x * (72362614232.0 + y * (-7895059235.0 + y * (242396853.1 + y * (-2972611.439 + y * (15704.48260 + y * (-30.16036606))))));
        a2 = 144725228442.0 + y * (2300535178.0 + y * (18583304.74 + y * (99447.43394 + y * (376.9991397 + y))));
        return a1 / a2;
      }
      var z = 8 / ax; y = z * z; var xx = ax - 2.356194491;
      a1 = 1 + y * (0.183105e-2 + y * (-0.3516396496e-4 + y * (0.2457520174e-5 + y * (-0.240337019e-6))));
      a2 = 0.04687499995 + y * (-0.2002690873e-3 + y * (0.8449199096e-5 + y * (-0.88228987e-6 + y * 0.105787412e-6)));
      var ans = Math.sqrt(0.636619772 / ax) * (Math.cos(xx) * a1 - z * Math.sin(xx) * a2);
      return x < 0 ? -ans : ans;
    }
    function airy(r, r0) { var v = 3.8317 * r / r0; return v < 1e-6 ? 1 : Math.pow(2 * J1(v) / v, 2); }
    var S, GW = 240, GH = 120, PXS = 34, SEP = 1.0;  /* PXS : pixels de grille par seconde d'arc */
    var off = document.createElement('canvas'); off.width = GW; off.height = GH;
    var octx = off.getContext('2d'), img = octx.createImageData(GW, GH);
    function draw() {
      var D = parseFloat(rD.value) / 100, th = 1.22 * 550e-9 / D * 206265, r0 = th * PXS;
      oD.textContent = Math.round(D * 100) + ' cm'; oT.textContent = fr(th, 2) + '\u2033';
      var x1 = GW / 2 - SEP * PXS / 2, x2 = GW / 2 + SEP * PXS / 2, yc = GH / 2, d = img.data;
      for (var j = 0; j < GH; j++) {
        for (var i = 0; i < GW; i++) {
          var I = airy(Math.hypot(i - x1, j - yc), r0) + 0.8 * airy(Math.hypot(i - x2, j - yc), r0);
          var v = Math.min(1, Math.pow(I, 0.5)), q = (j * GW + i) * 4;
          d[q] = 10 + 245 * v; d[q + 1] = 14 + 236 * v; d[q + 2] = 30 + 190 * v; d[q + 3] = 255;
        }
      }
      octx.putImageData(img, 0, 0);
      S.ctx.imageSmoothingEnabled = true; S.ctx.drawImage(off, 0, 0, S.w, S.h);
      var verdict = th < SEP * 0.9 ? 'Les deux étoiles sont séparées : leurs taches de diffraction ne se recouvrent presque pas.' :
        (th < SEP * 1.1 ? 'À la limite : les deux taches commencent à se confondre.' : 'Les deux étoiles sont confondues en une seule tache : l\u2019instrument ne les sépare pas.');
      msg.textContent = verdict;
    }
    rD.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 5. Superposition de deux signaux en un point ================= */
  (function () {
    var root = document.getElementById('lab-signaux');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rP = $(root, '[data-p="dt"]'), oP = $(root, '.out-dt'), cbI = $(root, '[data-p="incoh"]'), msg = $(root, '.nt-msg');
    var btn = $(root, '[data-act="play"]');
    var T = 1.4, WIN = 3 * T, S, C = {}, playing = !RM, visible = true, t = 0, last = null;
    var seg = [[], []];  /* sauts de phase aléatoires : [[début, phase], ...] */
    function phaseAt(n, tau) {
      if (!cbI.checked) { return 0; }
      var L = seg[n], ph = 0;
      for (var i = 0; i < L.length; i++) { if (L[i][0] <= tau) { ph = L[i][1]; } else { break; } }
      return ph;
    }
    function extend() {
      for (var n = 0; n < 2; n++) {
        var L = seg[n];
        if (!L.length) { L.push([t - WIN - 1, Math.random() * 2 * Math.PI]); }
        while (L[L.length - 1][0] < t + 1) { L.push([L[L.length - 1][0] + T * (0.6 + Math.random()), Math.random() * 2 * Math.PI]); }
        while (L.length > 2 && L[1][0] < t - WIN - 1) { L.shift(); }
      }
    }
    function sig(n, tau, dtFrac) {
      var w = 2 * Math.PI / T;
      return n === 0 ? Math.cos(w * tau + phaseAt(0, tau)) : Math.cos(w * (tau - dtFrac * T) + phaseAt(1, tau));
    }
    function lane(ctx, y0, h, color, fn, label, w) {
      ctx.strokeStyle = C.line; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(60, y0); ctx.lineTo(w - 8, y0); ctx.stroke();
      ctx.fillStyle = color; ctx.font = '700 12px system-ui, sans-serif'; ctx.textAlign = 'left'; ctx.fillText(label, 6, y0 + 4);
      ctx.strokeStyle = color; ctx.lineWidth = 2.4; ctx.beginPath();
      for (var px = 60; px <= w - 8; px++) {
        var tau = t - WIN + (px - 60) / (w - 68) * WIN, yy = y0 - h * fn(tau);
        if (px === 60) { ctx.moveTo(px, yy); } else { ctx.lineTo(px, yy); }
      }
      ctx.stroke();
    }
    function draw() {
      if (!S) { return; }
      extend();
      var ctx = S.ctx, w = S.w, h = S.h, dtF = parseFloat(rP.value), A = 22;
      ctx.clearRect(0, 0, w, h);
      lane(ctx, 36, A, C.blue, function (tau) { return sig(0, tau, dtF); }, 'onde 1', w);
      lane(ctx, 104, A, C.rose, function (tau) { return sig(1, tau, dtF); }, 'onde 2', w);
      lane(ctx, 196, A, C.emerald, function (tau) { return sig(0, tau, dtF) + sig(1, tau, dtF); }, 'somme', w);
      /* repères Δt entre maxima (cas cohérent) */
      if (!cbI.checked && dtF > 0.02 && dtF < 0.98) {
        var w0 = 2 * Math.PI / T;
        for (var m = Math.ceil((t - WIN) / T); m * T <= t; m++) {
          var ta = m * T, tb = ta + dtF * T;
          if (tb > t) { continue; }
          var xa = 60 + (ta - t + WIN) / WIN * (w - 68), xb = 60 + (tb - t + WIN) / WIN * (w - 68);
          ctx.strokeStyle = C.muted; ctx.setLineDash([2, 3]); ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(xa, 36 - A); ctx.lineTo(xa, 104); ctx.moveTo(xb, 104 - A); ctx.lineTo(xb, 104); ctx.stroke(); ctx.setLineDash([]);
          ctx.strokeStyle = C.emerald; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(xa, 70); ctx.lineTo(xb, 70); ctx.stroke();
          ctx.fillStyle = C.emerald; ctx.font = '700 11px system-ui, sans-serif'; ctx.textAlign = 'center'; ctx.fillText('\u0394t', (xa + xb) / 2, 66);
        }
      }
    }
    function verdict() {
      var dtF = parseFloat(rP.value);
      oP.textContent = fr(dtF, 2) + ' T  (déphasage ' + Math.round(dtF * 360) + '\u00b0)';
      if (cbI.checked) { msg.textContent = 'Sources incohérentes : le décalage entre les deux ondes change au hasard, la somme n\u2019est jamais stable. Aucune figure d\u2019interférence nette ne peut s\u2019installer.'; return; }
      var amp = 2 * Math.abs(Math.cos(Math.PI * dtF));
      if (amp > 1.94) { msg.textContent = 'En phase : les maxima coïncident, l\u2019amplitude de la somme est doublée. Interférence constructive.'; }
      else if (amp < 0.12) { msg.textContent = 'En opposition de phase : les maxima de l\u2019une tombent sur les minima de l\u2019autre, la somme est nulle. Interférence destructive.'; }
      else { msg.textContent = 'Cas intermédiaire : amplitude de la somme \u2248 ' + fr(amp, 2) + ' fois celle d\u2019une onde seule.'; }
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    function label() { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
    btn.addEventListener('click', function () { playing = !playing; label(); });
    rP.addEventListener('input', function () { verdict(); draw(); });
    cbI.addEventListener('change', function () { seg = [[], []]; verdict(); draw(); });
    Array.prototype.forEach.call(root.querySelectorAll('[data-set]'), function (b) {
      b.addEventListener('click', function () { rP.value = b.getAttribute('data-set'); cbI.checked = false; verdict(); draw(); });
    });
    function setup() { S = canvasCtx(cv); C = { blue: col('--blue'), rose: col('--rose'), emerald: col('--emerald'), muted: col('--muted'), line: col('--line') }; draw(); }
    watchVisible(cv, function (v) { visible = v; });
    label(); verdict(); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 6. Deux sources : cuve à ondes et point M ================= */
  (function () {
    var root = document.getElementById('lab-sources');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rL = $(root, '[data-p="lambda"]'), rE = $(root, '[data-p="e"]');
    var cbK = $(root, '[data-p="ordres"]'), cbA = $(root, '[data-p="amp"]'), cbI = $(root, '[data-p="incoh"]');
    var o1 = $(root, '.out-1'), o2 = $(root, '.out-2'), oD = $(root, '.out-d'), oR = $(root, '.out-r'), oL = $(root, '.out-l'), oE = $(root, '.out-e'), msg = $(root, '.nt-msg');
    var btn = $(root, '[data-act="play"]');
    var GW = 240, GH = 160, WX = 24, WY = 16, YS = 14.6, M = { x: 8.0, y: 5.0 };
    var off = document.createElement('canvas'); off.width = GW; off.height = GH;
    var octx = off.getContext('2d'), img = octx.createImageData(GW, GH);
    var A1r = new Float32Array(GW * GH), A1i = new Float32Array(GW * GH), A2r = new Float32Array(GW * GH), A2i = new Float32Array(GW * GH);
    var S, C = {}, playing = !RM, visible = true, t = 0, last = null, dirty = true, phi = 0, nextJump = 0;
    function src() { var e = parseFloat(rE.value); return [{ x: WX / 2 - e / 2, y: YS }, { x: WX / 2 + e / 2, y: YS }]; }
    function compute() {
      var lam = parseFloat(rL.value), k = 2 * Math.PI / lam, s = src();
      for (var j = 0; j < GH; j++) {
        var y = (j + 0.5) * WY / GH;
        for (var i = 0; i < GW; i++) {
          var x = (i + 0.5) * WX / GW, p = j * GW + i;
          var r1 = Math.max(0.3, Math.hypot(x - s[0].x, y - s[0].y)), r2 = Math.max(0.3, Math.hypot(x - s[1].x, y - s[1].y));
          var a1 = 2 / Math.sqrt(r1), a2 = 2 / Math.sqrt(r2);
          A1r[p] = a1 * Math.cos(k * r1); A1i[p] = a1 * Math.sin(k * r1);
          A2r[p] = a2 * Math.cos(k * r2); A2i[p] = a2 * Math.sin(k * r2);
        }
      }
      dirty = false;
    }
    function w2c(x, y) { return [x / WX * S.w, y / WY * S.h]; }
    function readouts() {
      var lam = parseFloat(rL.value), s = src();
      var d1 = Math.hypot(M.x - s[0].x, M.y - s[0].y), d2 = Math.hypot(M.x - s[1].x, M.y - s[1].y), del = d2 - d1, r = del / lam;
      oL.textContent = fr(lam, 1) + ' cm'; oE.textContent = fr(parseFloat(rE.value), 1) + ' cm';
      o1.textContent = fr(d1, 2) + ' cm'; o2.textContent = fr(d2, 2) + ' cm'; oD.textContent = fr(del, 2) + ' cm'; oR.textContent = fr(r, 2);
      if (cbI.checked) { msg.textContent = 'Sources incohérentes : leur déphasage change sans cesse, les zones calmes et agitées se déplacent au hasard. Pas de figure d\u2019interférence stable.'; return; }
      var dk = Math.abs(r - Math.round(r)), dh = Math.abs(r - Math.floor(r) - 0.5);
      if (dk < 0.08) { msg.textContent = '\u03b4/\u03bb \u2248 ' + fr(Math.round(r), 0) + ' : entier. Interférence constructive en M (ordre k = ' + fr(Math.round(r), 0) + ').'; }
      else if (dh < 0.08) { msg.textContent = '\u03b4/\u03bb \u2248 ' + fr(Math.floor(r) + 0.5, 1) + ' : demi-entier. Interférence destructive en M.'; }
      else { msg.textContent = '\u03b4/\u03bb n\u2019est ni entier ni demi-entier : interférence intermédiaire en M.'; }
    }
    function hyper(ctx, del, color, label) {
      var s = src(), c = (s[1].x - s[0].x) / 2, alpha = Math.abs(del) / 2, X0 = WX / 2;
      if (alpha >= c) { return; }
      var b = Math.sqrt(c * c - alpha * alpha), sg = del > 0 ? -1 : 1, pts = [];
      for (var tt = 0; tt <= 5; tt += 0.02) {
        var x = X0 + sg * alpha * Math.cosh(tt), y = YS - b * Math.sinh(tt);
        if (y < -0.5 || x < -1 || x > WX + 1) { break; }
        pts.push(w2c(x, y));
      }
      if (pts.length < 2) { return; }
      ctx.strokeStyle = color; ctx.lineWidth = 2; ctx.globalAlpha = 0.9; ctx.beginPath();
      pts.forEach(function (p, i) { if (i === 0) { ctx.moveTo(p[0], p[1]); } else { ctx.lineTo(p[0], p[1]); } });
      ctx.stroke(); ctx.globalAlpha = 1;
      var e = pts[pts.length - 1], lx = Math.max(14, Math.min(S.w - 14, e[0])), ly = Math.max(14, e[1] + 4);
      ctx.font = '700 12px system-ui, sans-serif'; ctx.textAlign = 'center';
      ctx.fillStyle = 'rgba(11,37,77,.75)'; ctx.fillRect(lx - 15, ly - 11, 30, 15);
      ctx.fillStyle = color; ctx.fillText(label, lx, ly);
    }
    function draw() {
      if (!S) { return; }
      if (dirty) { compute(); }
      var om = 2 * Math.PI * 0.8, c = Math.cos(om * t), s = Math.sin(om * t), d = img.data;
      var cp = Math.cos(phi), sp = Math.sin(phi), ampMode = cbA.checked && !cbI.checked;
      for (var p = 0; p < GW * GH; p++) {
        var br = A2r[p] * cp - A2i[p] * sp, bi = A2r[p] * sp + A2i[p] * cp;
        var Rr = A1r[p] + br, Ri = A1i[p] + bi, v, cc, q = p * 4;
        if (ampMode) { v = Math.min(1, Math.sqrt(Rr * Rr + Ri * Ri) / 2.2); cc = WATER[(v * 255) | 0]; }
        else { v = tanh(0.9 * (Rr * c + Ri * s)); cc = WATER[Math.max(0, Math.min(255, ((v + 1) * 127.5) | 0))]; }
        d[q] = cc[0]; d[q + 1] = cc[1]; d[q + 2] = cc[2]; d[q + 3] = 255;
      }
      octx.putImageData(img, 0, 0);
      var ctx = S.ctx; ctx.imageSmoothingEnabled = true; ctx.drawImage(off, 0, 0, S.w, S.h);
      var lam = parseFloat(rL.value), sr = src();
      if (cbK.checked && !cbI.checked) {
        var kmax = Math.floor((sr[1].x - sr[0].x) / lam);
        for (var k = -kmax; k <= kmax; k++) { hyper(ctx, k * lam, '#6EE7B7', fr(k, 0)); }
        for (var h = -kmax - 1; h <= kmax; h++) { hyper(ctx, (h + 0.5) * lam, '#FDA4AF', fr(h + 0.5, 1)); }
      }
      var P1 = w2c(sr[0].x, sr[0].y), P2 = w2c(sr[1].x, sr[1].y), PM = w2c(M.x, M.y);
      ctx.setLineDash([5, 4]); ctx.lineWidth = 2;
      ctx.strokeStyle = C.blueLt; ctx.beginPath(); ctx.moveTo(P1[0], P1[1]); ctx.lineTo(PM[0], PM[1]); ctx.stroke();
      ctx.strokeStyle = '#FDA4AF'; ctx.beginPath(); ctx.moveTo(P2[0], P2[1]); ctx.lineTo(PM[0], PM[1]); ctx.stroke(); ctx.setLineDash([]);
      [[P1, C.blueLt, 'S\u2081'], [P2, C.rose, 'S\u2082']].forEach(function (o) {
        ctx.fillStyle = o[1]; ctx.beginPath(); ctx.arc(o[0][0], o[0][1], 6, 0, 2 * Math.PI); ctx.fill();
        ctx.fillStyle = '#fff'; ctx.font = '700 13px system-ui, sans-serif'; ctx.textAlign = 'center'; ctx.fillText(o[2], o[0][0], o[0][1] - 10);
      });
      ctx.fillStyle = '#FBBF24'; ctx.strokeStyle = '#fff'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(PM[0], PM[1], 8, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
      ctx.fillStyle = '#fff'; ctx.font = '700 14px system-ui, sans-serif'; ctx.fillText('M', PM[0] + 15, PM[1] - 8);
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts;
      if (cbI.checked && t > nextJump) { phi = Math.random() * 2 * Math.PI; nextJump = t + 0.25 + Math.random() * 0.35; }
      if (visible && (playing || dirty || cbA.checked)) { draw(); }
      requestAnimationFrame(step);
    }
    function moveM(ev) {
      var rc = cv.getBoundingClientRect();
      M.x = Math.max(0.2, Math.min(WX - 0.2, (ev.clientX - rc.left) / rc.width * WX));
      M.y = Math.max(0.2, Math.min(WY - 0.2, (ev.clientY - rc.top) / rc.height * WY));
      readouts(); draw();
    }
    var drag = false;
    cv.addEventListener('pointerdown', function (e) { drag = true; cv.setPointerCapture(e.pointerId); moveM(e); });
    cv.addEventListener('pointermove', function (e) { if (drag) { moveM(e); } });
    cv.addEventListener('pointerup', function () { drag = false; });
    cv.addEventListener('keydown', function (e) {
      var st = 0.1, k = e.key;
      if (k === 'ArrowLeft') { M.x -= st; } else if (k === 'ArrowRight') { M.x += st; }
      else if (k === 'ArrowUp') { M.y -= st; } else if (k === 'ArrowDown') { M.y += st; } else { return; }
      e.preventDefault(); M.x = Math.max(0.2, Math.min(WX - 0.2, M.x)); M.y = Math.max(0.2, Math.min(WY - 0.2, M.y)); readouts(); draw();
    });
    function label() { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
    btn.addEventListener('click', function () { playing = !playing; label(); });
    [rL, rE].forEach(function (r) { r.addEventListener('input', function () { dirty = true; readouts(); draw(); }); });
    [cbK, cbA].forEach(function (c) { c.addEventListener('change', draw); });
    cbI.addEventListener('change', function () { if (!cbI.checked) { phi = 0; } readouts(); draw(); });
    function setup() { S = canvasCtx(cv); C = { blueLt: '#93C5FD', rose: '#FB7185' }; draw(); }
    watchVisible(cv, function (v) { visible = v; });
    label(); readouts(); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 7. Trous d'Young ================= */
  (function () {
    var root = document.getElementById('lab-young');
    if (!root) { return; }
    var cvE = $(root, 'canvas.screen'), cvP = $(root, 'canvas.plot');
    var rL = $(root, '[data-p="lambda"]'), rA = $(root, '[data-p="a"]'), rD = $(root, '[data-p="D"]'), rN = $(root, '[data-p="n"]'), cbE = $(root, '[data-p="env"]');
    var oL = $(root, '.out-l'), oA = $(root, '.out-a'), oD = $(root, '.out-D'), oN = $(root, '.out-n'), oI = $(root, '.out-i');
    var XMAX = 0.02, B = 60e-6, SE, SP;
    function I(x, lam, a, D, n) {
      var v = Math.pow(Math.cos(Math.PI * n * a * x / (lam * D)), 2);
      if (cbE.checked) { var u = Math.PI * B * x / (lam * D); v *= Math.abs(u) < 1e-9 ? 1 : Math.pow(Math.sin(u) / u, 2); }
      return v;
    }
    function draw() {
      var lam = parseFloat(rL.value) * 1e-9, a = parseFloat(rA.value) * 1e-3, D = parseFloat(rD.value), n = parseFloat(rN.value);
      var rgb = lambdaRGB(parseFloat(rL.value)), i = lam * D / (n * a);
      oL.textContent = rL.value + ' nm'; oA.textContent = fr(a * 1000, 2) + ' mm'; oD.textContent = fr(D, 1) + ' m'; oN.textContent = fr(n, 2);
      oI.textContent = fr(i * 1000, 2) + ' mm';
      var c = SE.ctx, w = SE.w, h = SE.h;
      c.fillStyle = '#0B1220'; c.fillRect(0, 0, w, h);
      for (var px = 0; px < w; px++) {
        var x = (px / (w - 1) * 2 - 1) * XMAX;
        c.fillStyle = rgbStr(rgb, Math.pow(I(x, lam, a, D, n), 0.6)); c.fillRect(px, 0, 1, h);
      }
      var p = SP.ctx, W = SP.w, H = SP.h, base = H - 30, top = 22;
      p.clearRect(0, 0, W, H);
      p.strokeStyle = col('--line'); p.beginPath(); p.moveTo(0, base); p.lineTo(W, base); p.stroke();
      p.fillStyle = col('--muted'); p.font = '11px system-ui, sans-serif'; p.textAlign = 'center';
      [-20, -10, 0, 10, 20].forEach(function (mm) { var X = (mm / 1000 / XMAX + 1) / 2 * (W - 1); p.fillText(mm + ' mm', Math.min(W - 20, Math.max(20, X)), H - 8); });
      p.strokeStyle = rgbStr([Math.min(190, rgb[0]), Math.min(190, rgb[1]), Math.min(190, rgb[2])]); p.lineWidth = 2; p.beginPath();
      for (var q = 0; q < W; q++) {
        var xx = (q / (W - 1) * 2 - 1) * XMAX, y = base - (base - top) * I(xx, lam, a, D, n);
        if (q === 0) { p.moveTo(q, y); } else { p.lineTo(q, y); }
      }
      p.stroke();
      /* ordres k au-dessus des maxima */
      var ipx = i / (2 * XMAX) * (W - 1);
      if (ipx > 26) {
        p.fillStyle = col('--blue'); p.font = '700 11px system-ui, sans-serif';
        for (var k = -6; k <= 6; k++) { var X = W / 2 + k * ipx; if (X > 10 && X < W - 10) { p.fillText('k=' + fr(k, 0), X, 14); } }
      }
      /* interfrange entre k = 0 et k = 1 */
      var x0 = W / 2, x1 = W / 2 + ipx, yb = base + 10;
      if (x1 < W - 4) {
        p.strokeStyle = col('--amber'); p.fillStyle = col('--amber'); p.lineWidth = 2;
        p.beginPath(); p.moveTo(x0, yb); p.lineTo(x1, yb); p.stroke();
        [x0, x1].forEach(function (xx) { p.beginPath(); p.moveTo(xx, yb - 5); p.lineTo(xx, yb + 5); p.stroke(); });
      }
    }
    [rL, rA, rD, rN].forEach(function (r) { r.addEventListener('input', draw); });
    cbE.addEventListener('change', draw);
    function setup() { SE = canvasCtx(cvE); SP = canvasCtx(cvP); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 8. Battements ================= */
  (function () {
    var root = document.getElementById('lab-batt');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rF = $(root, '[data-p="f2"]'), oF = $(root, '.out-f2'), oB = $(root, '.out-fb'), oT = $(root, '.out-tb'), btn = $(root, '[data-act="listen"]');
    var F1 = 440, S, AC = null, o1 = null, o2 = null, gn = null;
    function draw() {
      var f2 = parseFloat(rF.value), df = Math.abs(F1 - f2);
      oF.textContent = fr(f2, 1) + ' Hz'; oB.textContent = fr(df, 1) + ' Hz'; oT.textContent = df > 0 ? fr(1 / df, 2) + ' s' : '\u221e';
      var c = S.ctx, w = S.w, h = S.h, yc = h / 2 - 8, A = h / 2 - 26, TW = 1.0;
      c.clearRect(0, 0, w, h);
      c.strokeStyle = col('--line'); c.beginPath(); c.moveTo(0, yc); c.lineTo(w, yc); c.stroke();
      c.fillStyle = col('--blue');
      for (var px = 0; px < w; px++) {
        var t0 = px / w * TW, t1 = (px + 1) / w * TW, mn = 9, mx = -9;
        for (var k = 0; k <= 8; k++) {
          var tt = t0 + (t1 - t0) * k / 8, v = (Math.sin(2 * Math.PI * F1 * tt) + Math.sin(2 * Math.PI * f2 * tt)) / 2;
          if (v < mn) { mn = v; } if (v > mx) { mx = v; }
        }
        c.fillRect(px, yc - A * mx, 1, Math.max(1, A * (mx - mn)));
      }
      c.strokeStyle = col('--rose'); c.lineWidth = 2; c.setLineDash([6, 4]);
      [1, -1].forEach(function (sg) {
        c.beginPath();
        for (var q = 0; q <= w; q++) { var tt = q / w * TW, e = Math.abs(Math.cos(Math.PI * df * tt)); if (q === 0) { c.moveTo(q, yc - sg * A * e); } else { c.lineTo(q, yc - sg * A * e); } }
        c.stroke();
      });
      c.setLineDash([]);
      c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
      [0, 0.25, 0.5, 0.75, 1].forEach(function (s) { c.fillText(fr(s, 2) + ' s', Math.min(w - 18, Math.max(16, s / TW * w)), h - 6); });
      if (o2) { o2.frequency.setTargetAtTime(f2, AC.currentTime, 0.02); }
    }
    function start() {
      var Ctor = window.AudioContext || window.webkitAudioContext; if (!Ctor) { return; }
      AC = AC || new Ctor(); if (AC.state === 'suspended') { AC.resume(); }
      gn = AC.createGain(); gn.gain.value = 0; gn.connect(AC.destination);
      o1 = AC.createOscillator(); o2 = AC.createOscillator(); o1.frequency.value = F1; o2.frequency.value = parseFloat(rF.value);
      o1.connect(gn); o2.connect(gn); o1.start(); o2.start(); gn.gain.setTargetAtTime(0.12, AC.currentTime, 0.04);
    }
    function stop() {
      if (!o1) { return; }
      var a = o1, b = o2; gn.gain.setTargetAtTime(0, AC.currentTime, 0.04);
      setTimeout(function () { try { a.stop(); b.stop(); } catch (e) {} }, 250); o1 = o2 = null;
    }
    btn.addEventListener('click', function () {
      if (o1) { stop(); } else { start(); }
      btn.innerHTML = o1 ? '<i class="fa-solid fa-stop"></i>&nbsp; Arrêter' : '<i class="fa-solid fa-volume-high"></i>&nbsp; Écouter';
    });
    document.addEventListener('visibilitychange', function () { if (document.hidden && o1) { stop(); btn.innerHTML = '<i class="fa-solid fa-volume-high"></i>&nbsp; Écouter'; } });
    rF.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 9. Moiré : des battements dans l'espace ================= */
  (function () {
    var root = document.getElementById('lab-moire');
    if (!root) { return; }
    var cv = $(root, 'canvas'), r2 = $(root, '[data-p="p2"]'), oP2 = $(root, '.out-p2'), oN = $(root, '.out-n'), S;
    var P1 = 10;
    function grating(c, p, y0, h, w, color) {
      c.fillStyle = color;
      for (var x = 0; x < w + p; x += p) { c.fillRect(x, y0, p / 2, h); }
    }
    function draw() {
      var p2 = parseFloat(r2.value), c = S.ctx, w = S.w, ink = col('--ink');
      c.clearRect(0, 0, w, S.h);
      c.font = '700 12px system-ui, sans-serif'; c.textAlign = 'left';
      c.fillStyle = col('--blue'); c.fillText('réseau 1', 4, 14);
      grating(c, P1, 20, 34, w, col('--blue'));
      c.fillStyle = col('--rose'); c.fillText('réseau 2', 4, 74);
      grating(c, p2, 80, 34, w, col('--rose'));
      c.fillStyle = col('--emerald'); c.fillText('les deux réseaux superposés', 4, 134);
      grating(c, P1, 140, 52, w, ink); grating(c, p2, 140, 52, w, ink);
      var dp = Math.abs(P1 - p2);
      if (dp < 1e-6) { oP2.textContent = fr(p2, 2) + ' (identique au réseau 1)'; oN.textContent = 'aucun motif'; return; }
      var P = P1 * p2 / dp;
      oP2.textContent = fr(p2 / P1, 3) + ' \u00d7 pas du réseau 1';
      oN.textContent = 'tous les ' + fr(P / P1, 1) + ' traits du réseau 1';
      c.fillStyle = col('--amber');
      for (var k = 0; k * P < w; k++) {
        var X = k * P; c.beginPath(); c.moveTo(X, 196); c.lineTo(X - 6, 206); c.lineTo(X + 6, 206); c.closePath(); c.fill();
      }
      if (P < w - 10) {
        c.strokeStyle = col('--amber'); c.lineWidth = 2; c.beginPath(); c.moveTo(0, 214); c.lineTo(P, 214); c.stroke();
        c.textAlign = 'center'; c.fillText('période du motif', Math.min(P / 2, w - 60), 228);
      }
    }
    r2.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
})();
</script>

