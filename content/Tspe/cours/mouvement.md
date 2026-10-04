+++
title = "Mouvement"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Cinématique {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp nt-hole">cinématique</span> est l'étude du mouvement.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un mouvement s'étudie dans un <span class="imp nt-hole">référentiel</span>.</p>
<p>Un référentiel est un solide (ensemble de points fixes entre eux) par rapport auquel on repère la position ou le mouvement.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Un référentiel est composé&nbsp;:</p>
<ul class="nt-facts">
<li>d'un <span class="imp nt-hole">repère d'espace</span> $(\mathrm{O};\vec{i},\vec{j},\vec{k})$ permettant de définir la position,</li>
<li>d'un <span class="imp nt-hole">repère de temps</span> ou horloge $(t)$ permettant d'associer une date à chaque position.</li>
</ul>
</div>

<div class="nt-lab" id="lab-ref">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Un même mouvement, deux référentiels</p>
<p class="nt-note">Un passager lâche une balle dans un train qui roule à vitesse constante (animation au ralenti).</p>
<canvas style="height:260px;" aria-label="Chute d'une balle lâchée dans un train en mouvement, vue depuis le quai ou depuis le wagon"></canvas>
<div class="nt-ctrl">Référentiel&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="ref" value="sol" checked><span>terrestre (le quai)</span></label>
<label><input type="radio" name="ref" value="train"><span>le train</span></label>
</div>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">La trajectoire d'un objet dépend du référentiel choisi&nbsp;: c'est pourquoi il faut toujours le préciser avant d'étudier un mouvement.</p>
</div>

<p class="nt-lead">Référentiels usuels&nbsp;:</p>

<div class="nt-grid3">
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-earth-europe"></i>Terrestre</p>
<p><span class="imp nt-hole">Référentiel terrestre</span>&nbsp;: tout solide immobile à la surface de la Terre.</p>
<p class="nt-note">Pour étudier les mouvements à la surface de la Terre (chute d'un objet, voiture, ballon…).</p>
</div>
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-satellite"></i>Géocentrique</p>
<p>Référentiel <span class="imp nt-hole">géocentrique</span>&nbsp;: solide défini par le centre de la Terre et 3 étoiles lointaines considérées comme fixes.</p>
<p class="nt-note">Pour étudier le mouvement de la Lune et des satellites autour de la Terre.</p>
</div>
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-sun"></i>Héliocentrique</p>
<p>Référentiel <span class="imp nt-hole">héliocentrique</span>&nbsp;: solide défini par le centre du Soleil et 3 étoiles lointaines considérées comme fixes.</p>
<p class="nt-note">Pour étudier le mouvement des planètes et des comètes autour du Soleil.</p>
</div>
</div>

## Vecteur position {.nt-h2}

<svg class="nt-svg nt-svg-m" viewBox="0 0 660 380" role="img" aria-label="Vecteur position : dans un repère d'origine O, le point M de la trajectoire est repéré par le vecteur OM, de coordonnées x(t) et y(t)"><polyline points="150.0,300.0 154.7,293.9 159.4,287.8 164.1,281.9 168.8,276.1 173.5,270.5 178.2,265.1 182.9,259.7 187.6,254.6 192.3,249.6 197.0,244.9 201.7,240.3 206.4,235.9 211.1,231.8 215.8,227.8 220.5,224.1 225.2,220.6 229.9,217.3 234.6,214.3 239.3,211.5 244.0,209.0 248.7,206.7 253.4,204.6 258.1,202.8 262.8,201.2 267.5,199.9 272.2,198.8 276.9,198.0 281.6,197.4 286.3,197.0 291.0,196.8 295.7,196.9 300.4,197.2 305.1,197.7 309.8,198.4 314.5,199.2 319.2,200.3 323.9,201.5 328.6,202.9 333.3,204.5 338.0,206.2 342.7,208.0 347.4,209.9 352.1,211.9 356.8,214.0 361.5,216.2 366.2,218.4 370.9,220.7 375.6,222.9 380.3,225.2 385.0,227.5 389.7,229.8 394.4,232.0 399.1,234.2 403.8,236.3 408.5,238.3 413.2,240.3 417.9,242.1 422.6,243.7 427.3,245.2 432.0,246.6 436.7,247.8 441.4,248.7 446.1,249.5 450.8,250.0 455.5,250.3 460.2,250.4 464.9,250.2 469.6,249.7 474.3,249.0 479.0,247.9 483.7,246.6 488.4,244.9 493.1,242.9 497.8,240.6 502.5,237.9 507.2,234.9 511.9,231.5 516.6,227.8 521.3,223.8 526.0,219.4 530.7,214.6 535.4,209.4 540.1,203.9 544.8,198.0 549.5,191.8 554.2,185.2 558.9,178.2 563.6,170.9 568.3,163.2 573.0,155.1 577.7,146.8 582.4,138.0 587.1,129.0 591.8,119.6 596.5,109.9 601.2,99.8 605.9,89.5 610.6,78.9 615.3,68.0 620.0,56.8" fill="none" stroke="var(--rose)" stroke-width="3" stroke-linecap="round"/><polygon points="620.0,56.8 620.7,67.9 611.5,64.0" fill="var(--rose)"/><line x1="60" y1="330" x2="631.0" y2="330.0" stroke="var(--slate)" stroke-width="1.5" stroke-linecap="round"/><polygon points="640.0,330.0 630.0,335.0 630.0,325.0" fill="var(--slate)"/><line x1="90" y1="360" x2="90.0" y2="29.0" stroke="var(--slate)" stroke-width="1.5" stroke-linecap="round"/><polygon points="90.0,20.0 95.0,30.0 85.0,30.0" fill="var(--slate)"/><text x="632" y="354" font-size="16" fill="var(--slate)" font-family="Georgia, serif" font-style="italic" font-weight="700">x</text><text x="68" y="30" font-size="16" fill="var(--slate)" font-family="Georgia, serif" font-style="italic" font-weight="700">y</text><line x1="90" y1="330" x2="136.0" y2="330.0" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/><polygon points="145.0,330.0 135.0,335.0 135.0,325.0" fill="var(--ink)"/><line x1="90" y1="330" x2="90.0" y2="284.0" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/><polygon points="90.0,275.0 95.0,285.0 85.0,285.0" fill="var(--ink)"/><text x="120" y="356" font-size="17" fill="var(--ink)" font-family="Georgia, serif" font-style="italic" font-weight="700">i</text><line x1="117" y1="339" x2="128" y2="339" stroke="var(--ink)" stroke-width="1.4"/><polygon points="131.0,339.0 126.0,341.6 126.0,336.4" fill="var(--ink)"/><text x="68" y="306" font-size="17" fill="var(--ink)" font-family="Georgia, serif" font-style="italic" font-weight="700">j</text><line x1="65" y1="288" x2="76" y2="288" stroke="var(--ink)" stroke-width="1.4"/><polygon points="79.0,288.0 74.0,290.6 74.0,285.4" fill="var(--ink)"/><text x="70" y="352" font-size="17" fill="var(--ink)" font-family="Georgia, serif">O</text><line x1="375.6" y1="222.9" x2="375.6" y2="330" stroke="var(--muted)" stroke-dasharray="5 4"/><line x1="375.6" y1="222.9" x2="90" y2="222.9" stroke="var(--muted)" stroke-dasharray="5 4"/><text x="375.6" y="354" font-size="16" fill="var(--blue)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">x(t)</text><text x="80" y="227.9" font-size="16" fill="var(--blue)" text-anchor="end" font-family="Georgia, serif" font-style="italic" font-weight="700">y(t)</text><line x1="90" y1="330" x2="367.2" y2="226.1" stroke="var(--blue)" stroke-width="3.2" stroke-linecap="round"/><polygon points="375.6,222.9 368.0,231.1 364.5,221.8" fill="var(--blue)"/><circle cx="375.6" cy="222.9" r="6" fill="var(--rose)"/><text x="387.6" y="212.9" font-size="18" fill="var(--rose)" font-family="Georgia, serif">M(<tspan font-style="italic">t</tspan>)</text><text x="246.8" y="300.5" font-size="18" fill="var(--blue)" font-family="Georgia, serif">OM(<tspan font-style="italic">t</tspan>)</text><line x1="246.8" y1="282.5" x2="276.8" y2="282.5" stroke="var(--blue)" stroke-width="1.5"/><polygon points="279.8,282.5 273.8,285.5 273.8,279.5" fill="var(--blue)"/><text x="520" y="70" font-size="14" fill="var(--rose)" font-weight="700">trajectoire</text></svg>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Dans un repère orthonormé $(\mathrm{O};\vec{i},\vec{j},\vec{k})$, la position d'un point $\mathrm{M}$ à la date $t$ est donnée par son <span class="imp nt-hole">vecteur position</span>&nbsp;:</p>
<p class="nt-center">${\color{#2A6BC4}\overrightarrow{\mathrm{OM}}(t)\begin{pmatrix}x(t)\\y(t)\\z(t)\end{pmatrix}} \quad\text{soit}\quad {\color{#2A6BC4}\overrightarrow{\mathrm{OM}}(t)=x(t)\,\vec{i}+y(t)\,\vec{j}+z(t)\,\vec{k}}$</p>
</div>

<p class="nt-lead">On notera fréquemment&nbsp;:</p>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Coordonnées du vecteur position</p>
<p class="nt-f-math">$$\begin{cases}x(t)=\ldots\\y(t)=\ldots\\z(t)=\ldots\end{cases}$$</p>
</div>
<div class="nt-b nt-demo-box" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>En pratique, les mouvements seront presque toujours à 2 dimensions seulement&nbsp;:</p>
<p class="nt-center">$\begin{cases}x(t)=\ldots\\y(t)=\ldots\end{cases}$</p>
</div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La <span class="imp">norme</span> $\mathrm{OM}(t)$ du vecteur position vaut&nbsp;:</p>
<p class="nt-center">$\mathrm{OM}(t)=\left\|\overrightarrow{\mathrm{OM}}(t)\right\|=\sqrt{x(t)^2+y(t)^2+z(t)^2}$</p>
<p>Unité&nbsp;: <span class="imp nt-hole">$\pu{m}$</span></p>
</div>

## Vecteur vitesse {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le vecteur vitesse moyenne d'un point $\mathrm{M}$ entre deux instants $t$ et $t+\Delta t$ est défini par&nbsp;:</p>
<p class="nt-center">$\begin{aligned}\vec{v}_m(t) &= \frac{\overrightarrow{\mathrm{M}(t)\mathrm{M}(t+\Delta t)}}{\Delta t}\\ &= \frac{\overrightarrow{\mathrm{OM}}(t+\Delta t)-\overrightarrow{\mathrm{OM}}(t)}{\Delta t}\\ &=\frac{\Delta\overrightarrow{\mathrm{OM}}(t)}{\Delta t}\end{aligned}$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>On obtient le vecteur vitesse $\vec{v}(t)$ en faisant tendre $\Delta t$ vers $0$. On obtient alors la <span class="imp nt-hole">dérivée</span> du vecteur position.</p>
</div>

<div class="nt-lab" id="lab-vmoy">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Du vecteur vitesse moyenne au vecteur vitesse</p>
<canvas style="height:300px;" aria-label="Trajectoire avec les points M(t) et M(t+Δt), le vecteur vitesse moyenne et le vecteur vitesse"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Date $t$ du point M&nbsp;: <input type="range" data-p="t" min="0.2" max="1.5" step="0.01" value="0.6"></label>
<label class="nt-ctrl">Durée $\Delta t$&nbsp;: <b class="out-dt"></b><input type="range" data-p="dt" min="0.02" max="1.2" step="0.01" value="0.9"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$\|\vec{v}_m\|$ = <b class="out-vm"></b></span><span>$\|\vec{v}\|$ = <b class="out-v"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">En bleu&nbsp;: le vecteur $\overrightarrow{\mathrm{M}(t)\mathrm{M}(t+\Delta t)}$&nbsp;; en vert pointillé&nbsp;: le vecteur vitesse moyenne&nbsp;; en orange&nbsp;: le vecteur vitesse (les deux vitesses sont tracées à la même échelle). Réduisez $\Delta t$.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vecteur vitesse</p>
<p class="nt-f-math">$$\vec{v}(t)=\frac{\mathrm{d}\overrightarrow{\mathrm{OM}}}{\mathrm{d}t}$$</p>
<div class="nt-f-units"><span>le vecteur vitesse est la <b>dérivée par rapport au temps du vecteur position</b></span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Notation</p>
<p>En physique, $\Delta$ correspond à une variation et $\mathrm{d}$ à une variation infinitésimale.</p>
<p>La notation physique $\dfrac{\mathrm{d}x}{\mathrm{d}t}$ correspond à la notation mathématique $x'(t)$.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Coordonnées du vecteur vitesse</p>
<p class="nt-center">$\vec{v}(t) = v_x(t)\,\vec{i}+v_y(t)\,\vec{j}+v_z(t)\,\vec{k} = \dfrac{\mathrm{d}x}{\mathrm{d}t}\,\vec{i}+\dfrac{\mathrm{d}y}{\mathrm{d}t}\,\vec{j}+\dfrac{\mathrm{d}z}{\mathrm{d}t}\,\vec{k}$</p>
<p class="nt-center">$\begin{cases}v_x(t)=\dfrac{\mathrm{d}x}{\mathrm{d}t}=\ldots\\[2mm] v_y(t)=\dfrac{\mathrm{d}y}{\mathrm{d}t}=\ldots\\[2mm] v_z(t)=\dfrac{\mathrm{d}z}{\mathrm{d}t}=\ldots\end{cases}$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le vecteur vitesse est porté par la <span class="imp nt-hole">tangente à la trajectoire</span> et orienté dans le sens du mouvement.</p>
<p>La <span class="imp">norme</span> $v(t)$ du vecteur vitesse vaut&nbsp;: $v(t)=\left\|\vec{v}(t)\right\|=\sqrt{v_x(t)^2+v_y(t)^2+v_z(t)^2}$. Unité&nbsp;: <span class="imp nt-hole">$\pu{m*s-1}$</span>.</p>
</div>

## Vecteur accélération {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le vecteur accélération moyenne d'un point $\mathrm{M}$ entre deux instants $t$ et $t+\Delta t$ est défini à partir du vecteur variation de vitesse&nbsp;:</p>
<p class="nt-center">$\vec{a}_m(t) = \dfrac{\vec{v}(t+\Delta t)-\vec{v}(t)}{\Delta t} = \dfrac{\Delta\vec{v}(t)}{\Delta t}$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>On obtient le vecteur accélération $\vec{a}(t)$ en faisant tendre $\Delta t$ vers $0$. Cela donne la <span class="imp nt-hole">dérivée</span> du vecteur vitesse et donc la <span class="imp nt-hole">dérivée seconde</span> du vecteur position.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vecteur accélération</p>
<p class="nt-f-math">$$\vec{a}(t)=\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}=\frac{\mathrm{d}^2\overrightarrow{\mathrm{OM}}}{\mathrm{d}t^2}$$</p>
<div class="nt-f-units"><span>dérivée par rapport au temps du vecteur vitesse, et <b>dérivée seconde du vecteur position</b></span></div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Coordonnées du vecteur accélération</p>
<p class="nt-center">$\vec{a}(t) = a_x(t)\,\vec{i}+a_y(t)\,\vec{j}+a_z(t)\,\vec{k} = \dfrac{\mathrm{d}v_x}{\mathrm{d}t}\,\vec{i}+\dfrac{\mathrm{d}v_y}{\mathrm{d}t}\,\vec{j}+\dfrac{\mathrm{d}v_z}{\mathrm{d}t}\,\vec{k}$</p>
<p class="nt-center">$\begin{cases}a_x(t)=\dfrac{\mathrm{d}v_x}{\mathrm{d}t}=\ldots\\[2mm] a_y(t)=\dfrac{\mathrm{d}v_y}{\mathrm{d}t}=\ldots\\[2mm] a_z(t)=\dfrac{\mathrm{d}v_z}{\mathrm{d}t}=\ldots\end{cases}$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le vecteur accélération est dans la direction et le sens du <span class="imp nt-hole">vecteur variation de vitesse</span>.</p>
<p>Dans le cas d'une trajectoire courbe, il pointe vers l'<span class="imp nt-hole">intérieur de la courbe</span>.</p>
<p>La <span class="imp">norme</span> $a(t)$ du vecteur accélération vaut&nbsp;: $a(t)=\left\|\vec{a}(t)\right\|=\sqrt{a_x(t)^2+a_y(t)^2+a_z(t)^2}$. Unité&nbsp;: <span class="imp nt-hole">$\pu{m*s-2}$</span>.</p>
</div>

<div class="nt-lab" id="lab-chrono">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Construire les vecteurs vitesse et accélération sur une chronophotographie</p>
<canvas style="height:430px;" aria-label="Chronophotographie d'un mouvement avec construction des vecteurs vitesse, variation de vitesse et accélération"></canvas>
<div class="nt-ctrl">Mouvement&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="mov" value="para" checked><span>chute libre</span></label>
<label><input type="radio" name="mov" value="circ"><span>circulaire uniforme</span></label>
<label><input type="radio" name="mov" value="frein"><span>rectiligne freiné</span></label>
</div>
</div>
<div class="nt-ctrl">Méthode&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="meth" value="mil" checked><span>point milieu</span></label>
<label><input type="radio" name="meth" value="apr"><span>point d'après</span></label>
</div>
</div>
<label class="nt-ctrl">Point M<sub>i</sub> étudié&nbsp;: <input type="range" min="2" max="12" step="1" value="4"></label>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="v" checked> vecteurs vitesse</label>
<label class="nt-check"><input type="checkbox" data-p="dv" checked> construction de $\Delta\vec{v}_i$</label>
<label class="nt-check"><input type="checkbox" data-p="a" checked> $\vec{a}_i$</label>
<label class="nt-check"><input type="checkbox" data-p="ex"> vraie accélération</label>
</div>
<p class="nt-center nt-chrono-form">Point milieu&nbsp;: $\vec{v}_i \approx \dfrac{\overrightarrow{\mathrm{M}_{i-1}\mathrm{M}_{i+1}}}{2\tau}$, puis $\Delta\vec{v}_i = \vec{v}_{i+1}-\vec{v}_{i-1}$ et $\vec{a}_i \approx \dfrac{\Delta\vec{v}_i}{2\tau}$.</p>
<div class="nt-read" aria-live="polite"><span>écart avec la vraie accélération&nbsp;: <b class="out-err"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Les points sont séparés par une durée constante $\tau$. On reporte les deux vecteurs vitesse à partir de $\mathrm{M}_i$ pour construire $\Delta\vec{v}_i$. Les échelles des vecteurs sont arbitraires&nbsp;; la vraie accélération (en pointillés gris) est calculée à partir de l'équation du mouvement.</p>
</div>

<details class="nt-d">
<summary><span class="nt-tag"><i class="fa-solid fa-scale-balanced"></i>Méthode</span><span class="nt-sum">Point d'après ou point milieu&nbsp;?</span></summary>
<div class="nt-d-body">
<div class="nt-scroll">
<table class="nt-t nt-t-cmp">
<thead><tr><th></th><th><span class="nt-cmp-h nt-cmp-a">Point d'après</span></th><th><span class="nt-cmp-h nt-cmp-b">Point milieu</span></th></tr></thead>
<tbody>
<tr><th>Vitesse en $\mathrm{M}_i$</th><td>$\vec{v}_i \approx \dfrac{\overrightarrow{\mathrm{M}_{i}\mathrm{M}_{i+1}}}{\tau}$</td><td>$\vec{v}_i \approx \dfrac{\overrightarrow{\mathrm{M}_{i-1}\mathrm{M}_{i+1}}}{2\tau}$</td></tr>
<tr><th>Accélération en $\mathrm{M}_i$</th><td>$\vec{a}_i \approx \dfrac{\vec{v}_{i+1}-\vec{v}_{i}}{\tau}$</td><td>$\vec{a}_i \approx \dfrac{\vec{v}_{i+1}-\vec{v}_{i-1}}{2\tau}$</td></tr>
<tr><th>Lien avec la dérivée</th><td>taux d'accroissement entre $t_i$ et $t_i+\tau$&nbsp;: c'est la définition même de la dérivée</td><td>taux d'accroissement entre $t_i-\tau$ et $t_i+\tau$, symétrique autour de $t_i$</td></tr>
<tr><th>Direction de $\vec{v}_i$</th><td>celle de la corde $\mathrm{M}_i\mathrm{M}_{i+1}$&nbsp;: un peu décalée par rapport à la tangente en $\mathrm{M}_i$</td><td>quasiment celle de la tangente en $\mathrm{M}_i$</td></tr>
<tr><th>Mouvement circulaire uniforme</th><td>$\vec{a}_i$ ne pointe pas vers le centre&nbsp;: il est décalé de l'angle balayé entre deux positions (environ 12° dans l'animation)</td><td>$\vec{a}_i$ pointe exactement vers le centre, par symétrie</td></tr>
</tbody>
</table>
</div>
<p><b>Pourquoi cette différence&nbsp;?</b> Le vecteur $\overrightarrow{\mathrm{M}_i\mathrm{M}_{i+1}}/\tau$ est une vitesse moyenne entre $t_i$ et $t_i+\tau$&nbsp;: elle représente plutôt la vitesse au milieu de cet intervalle, à $t_i+\tau/2$, qu'à $t_i$. Avec la méthode du point d'après, on attribue donc au point $\mathrm{M}_i$ des vecteurs qui correspondent en fait à des instants un peu plus tardifs. La méthode du point milieu, symétrique, évite ce décalage. Les deux méthodes donnent le même résultat quand l'accélération est constante (chute libre, mouvement rectiligne uniformément freiné)&nbsp;: la différence se voit surtout sur le mouvement circulaire.</p>
<p><b>Laquelle utiliser&nbsp;?</b> En seconde et en première, on utilise généralement la méthode du point d'après, qui colle à la définition de la dérivée. En terminale, on lui préfère souvent la méthode du point milieu, plus précise. Dans tous les cas, appliquer la méthode indiquée par l'énoncé.</p>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-car"></i>Le point de vue du physicien</p>
<p>Dans une voiture, on parle de pédale de frein, de pédale d'accélérateur et de volant. Pour un physicien, ce sont trois accélérateurs&nbsp;! Freiner, accélérer ou tourner, c'est toujours modifier le vecteur vitesse, en norme ou en direction&nbsp;: dans les trois cas, le vecteur accélération n'est pas nul.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Deux vidéos pour revoir les vecteurs vitesse et accélération</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://www.youtube.com/watch?v=Ooe94mPwXEY" target="_blank" rel="noopener">Vecteurs vitesse et accélération</a>, jusqu'à 3'22'' (la méthode d'Euler, introduite ensuite, est utile pour le supérieur mais pas au programme de terminale).</li>
<li><a href="https://www.youtube.com/watch?v=9W6zhF1cdso" target="_blank" rel="noopener">Mouvement circulaire</a>, jusqu'à 4'51'' (la suite, qui décrit le mouvement circulaire uniforme dans un repère orthonormé fixe, n'est pas au programme).</li>
</ul>
</div>
</details>

## Mouvements rectilignes {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un mouvement est rectiligne si sa trajectoire est une <span class="imp nt-hole">droite</span>.</p>
<p>Le vecteur vitesse conserve alors la même direction (celle du mouvement).</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Si le vecteur vitesse est constant, le mouvement est dit <span class="imp">rectiligne <span class="nt-hole">uniforme</span></span>.</p>
<p>Que vaut alors le vecteur accélération&nbsp;? $\vec{a}=\dfrac{\mathrm{d}\vec{v}}{\mathrm{d}t}=\vec{0}$</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Mouvement rectiligne uniforme</p>
<p class="nt-f-math">$$\text{MRU} \Leftrightarrow \vec{a}=\vec{0}$$</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un mouvement rectiligne avec un vecteur accélération constant ($\vec{a}(t)=\overrightarrow{\text{cte}}$) est dit <span class="imp nt-hole">rectiligne uniformément accéléré</span>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Tracer les évolutions de la position $\color{#2A6BC4}x(t)$, de la vitesse $\color{#D97706}v(t)$ et de l'accélération $\color{#059669}a(t)$ pour un mouvement rectiligne uniforme, puis pour un mouvement rectiligne uniformément accéléré.</p>
</div>

<div class="nt-lab" id="lab-xva">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Position, vitesse et accélération d'un mouvement rectiligne</p>
<canvas style="height:430px;" aria-label="Mobile sur une piste rectiligne et graphes de x(t), v(t) et a(t)"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Position initiale $x_0$&nbsp;: <b class="out-x0"></b><input type="range" data-p="x0" min="-10" max="10" step="0.5" value="-8"></label>
<label class="nt-ctrl">Vitesse initiale $v_0$&nbsp;: <b class="out-v0"></b><input type="range" data-p="v0" min="-6" max="10" step="0.5" value="5"></label>
<label class="nt-ctrl">Accélération $a$&nbsp;: <b class="out-a"></b><input type="range" data-p="a" min="-4" max="4" step="0.1" value="0"></label>
</div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-preset="-8,5,0">MRU</button>
<button type="button" class="nt-btn" data-preset="-8,0,2">MRUA (départ arrêté)</button>
<button type="button" class="nt-btn" data-preset="0,8,-3">MRUA freiné puis retour</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

### Petit exercice {.nt-h3}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-flag-checkered"></i>Exercice</p>
<p>Avant d'aborder le virage des Combes (virage n°5) du circuit de Spa-Francorchamps, un pilote de F1 freine fortement pour passer sa vitesse de 327&nbsp;km/h à 176&nbsp;km/h en 1,48&nbsp;s.</p>
<ol class="nt-steps">
<li><p>En supposant le mouvement rectiligne uniformément accéléré, décrire le vecteur accélération de la F1.</p></li>
<li><p>Sur combien de mètres a lieu le freinage&nbsp;?</p></li>
<li><p>Il se fait en réalité sur 93&nbsp;m, que peut-on conclure&nbsp;?</p></li>
</ol>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>On convertit les vitesses&nbsp;: $v_0 = \dfrac{327}{3{,}6} = \pu{90,8 m*s-1}$ et $v_1 = \dfrac{176}{3{,}6} = \pu{48,9 m*s-1}$.</p>
<p>Le mouvement étant rectiligne uniformément accéléré, $a = \dfrac{\Delta v}{\Delta t} = \dfrac{48{,}9 - 90{,}8}{1{,}48} = \pu{-28,3 m*s-2}$.</p>
<p>Le vecteur accélération a donc la direction du mouvement (la ligne droite), il est de sens opposé au mouvement, et sa norme vaut environ $\pu{28 m*s-2}$, soit près de 3 fois l'intensité de la pesanteur.</p></li>
<li><p>La vitesse variant linéairement avec le temps, la distance parcourue est celle qu'on parcourrait à la vitesse moyenne $\dfrac{v_0+v_1}{2}$&nbsp;: $d = \dfrac{v_0+v_1}{2}\times\Delta t = \dfrac{90{,}8+48{,}9}{2}\times 1{,}48 = \pu{103 m}$.</p></li>
<li><p>Le freinage réel est plus court (93&nbsp;m) pour la même durée&nbsp;: la F1 a donc perdu sa vitesse plus tôt que prévu. Le mouvement n'est pas uniformément accéléré&nbsp;: la décélération est plus forte au début du freinage, à grande vitesse, car la traînée aérodynamique et l'appui (qui plaque la voiture au sol et améliore l'adhérence des pneus) augmentent fortement avec la vitesse.</p></li>
</ol>
</div>
</details>

## Mouvements circulaires {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un mouvement est <span class="imp">circulaire</span> si sa trajectoire est un <span class="imp nt-hole">cercle</span> (ou un arc de cercle).</p>
<p>On parle de <span class="imp">mouvement circulaire uniforme</span> si <span class="imp nt-hole">la norme du vecteur vitesse est constante</span>.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Le repère de Frenet</p>
<p>Pour décrire le mouvement circulaire d'un point M sur un cercle de centre O, on utilise un <span class="imp nt-hole">repère de Frenet</span>. C'est un repère mobile centré au point étudié M et de vecteurs unitaires&nbsp;:</p>
<ul class="nt-facts">
<li>$\color{#D97706}\vec{u}_T$&nbsp;: <b style="color:#D97706;">vecteur tangent</b>, tangent à la trajectoire, orienté dans le sens du mouvement&nbsp;;</li>
<li>$\color{#059669}\vec{u}_N$&nbsp;: <b style="color:#059669;">vecteur normal</b>, de direction (OM), orienté vers le centre O.</li>
</ul>
<p class="nt-note">$\vec{u}_T$ est parfois noté $\vec{T}$ et $\vec{u}_N$ noté $\vec{N}$.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vecteur vitesse</p>
<p class="nt-f-math">$$\vec{v}(t)\begin{cases}v_T(t)=v(t)\\v_N(t)=0\end{cases}$$</p>
<p class="nt-f-soit">soit&nbsp; <b>$\vec{v}(t)=v(t)\,\vec{u}_T$</b></p>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vecteur accélération</p>
<p class="nt-f-math">$$\vec{a}(t)\begin{cases}a_T(t)=\dfrac{\mathrm{d}v}{\mathrm{d}t}\\[2mm] a_N(t)=\dfrac{v^2}{R}\end{cases}$$</p>
<p class="nt-f-soit">soit&nbsp; <b>$\vec{a}(t)=\dfrac{\mathrm{d}v}{\mathrm{d}t}\,\vec{u}_T+\dfrac{v^2}{R}\,\vec{u}_N$</b></p>
</div>
</div>

<div class="nt-lab" id="lab-frenet">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le repère de Frenet en mouvement</p>
<canvas style="height:340px;" aria-label="Point en mouvement circulaire avec son repère de Frenet, son vecteur vitesse et son vecteur accélération"></canvas>
<div class="nt-ctrl">Mouvement&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="circ" value="unif" checked><span>uniforme</span></label>
<label><input type="radio" name="circ" value="acc"><span>accéléré</span></label>
<label><input type="radio" name="circ" value="frein"><span>freiné</span></label>
</div>
</div>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="comp" checked> Composantes $a_T$ et $a_N$</label>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<div class="nt-read" aria-live="polite"><span>$v$ = <b class="out-v"></b></span><span>$a_T$ = <b class="out-at"></b></span><span>$a_N = v^2/R$ = <b class="out-an"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Et si le mouvement est circulaire uniforme&nbsp;?</p>
<p>On a $\dfrac{\mathrm{d}v}{\mathrm{d}t}=0$ puisque $v=\mathrm{cte}$. Et donc&nbsp;:</p>
<p class="nt-center">$\vec{a}(t)\begin{cases}a_T(t)=0\\[1mm] a_N(t)=\dfrac{v^2}{R}\end{cases}$</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Mouvement circulaire uniforme</p>
<p class="nt-f-math">$$\vec{a}(t)= \frac{v^2}{R}\,\vec{u}_N$$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>L'accélération est <span class="imp nt-hole">centripète</span> (dirigée vers le centre) et de <span class="imp nt-hole">norme constante</span>.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">D'où vient le $v^2/R$&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Dans un mouvement circulaire uniforme, le vecteur vitesse garde la même norme $v$, mais il tourne avec le point M. Pendant une petite durée $\mathrm{d}t$, M parcourt l'arc $v\,\mathrm{d}t$, donc le rayon OM (et avec lui le vecteur vitesse, qui lui est perpendiculaire) tourne d'un petit angle $\mathrm{d}\theta = \dfrac{v\,\mathrm{d}t}{R}$.</p>
<p>Un vecteur de norme $v$ qui tourne d'un petit angle $\mathrm{d}\theta$ varie d'un petit vecteur de norme $v\,\mathrm{d}\theta$, perpendiculaire à lui, donc dirigé vers le centre. D'où&nbsp;:</p>
<p class="nt-center">$a = \dfrac{\|\mathrm{d}\vec{v}\|}{\mathrm{d}t} = \dfrac{v\,\mathrm{d}\theta}{\mathrm{d}t} = v\times\dfrac{v}{R} = \dfrac{v^2}{R}$</p>
<p>On retrouve le résultat sans calcul de dérivée&nbsp;: il suffit de comprendre que «&nbsp;tourner&nbsp;», c'est déjà accélérer.</p>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CP = '#2A6BC4', CV = '#D97706', CA = '#059669', CT = '#E11D48';   /* position, vitesse, accélération, trajectoire */
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
  /* flèche (vecteur) dans un canevas */
  function arrow(c, x1, y1, x2, y2, color, w, dash) {
    var dx = x2 - x1, dy = y2 - y1, n = Math.hypot(dx, dy);
    if (n < 1) { return; }
    var ux = dx / n, uy = dy / n, L = Math.min(12, n * 0.45), W = L * 0.5;
    c.strokeStyle = color; c.fillStyle = color; c.lineWidth = w || 2.6; c.lineCap = 'round'; c.setLineDash(dash || []);
    c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2 - ux * L * 0.8, y2 - uy * L * 0.8); c.stroke(); c.setLineDash([]);
    c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - ux * L - uy * W, y2 - uy * L + ux * W); c.lineTo(x2 - ux * L + uy * W, y2 - uy * L - ux * W); c.closePath(); c.fill();
  }
  function txt(c, s, x, y, color, font, align, halo) {
    c.font = font || '700 13px system-ui, sans-serif'; c.textAlign = align || 'center';
    if (halo) { c.lineJoin = 'round'; c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.95)'; c.strokeText(s, x, y); }
    c.fillStyle = color; c.fillText(s, x, y);
  }
  function vecLabel(c, s, x, y, color, noBg) {   /* lettre surmontée d'une flèche ; un fin contour clair la détache des tracés (sauf noBg) */
    c.font = 'italic 700 15px Georgia, serif'; c.textAlign = 'center'; c.lineJoin = 'round'; c.lineCap = 'round';
    var w = c.measureText(s).width;
    function arrowPath() { c.beginPath(); c.moveTo(x - w / 2, y - 14); c.lineTo(x + w / 2, y - 14); c.moveTo(x + w / 2, y - 14); c.lineTo(x + w / 2 - 4, y - 16.5); c.moveTo(x + w / 2, y - 14); c.lineTo(x + w / 2 - 4, y - 11.5); }
    if (!noBg) {
      c.strokeStyle = 'rgba(248,250,252,.9)'; c.lineWidth = 4; c.strokeText(s, x, y);
      c.lineWidth = 4.3; arrowPath(); c.stroke();
    }
    c.fillStyle = color; c.fillText(s, x, y);
    c.strokeStyle = color; c.lineWidth = 1.3; arrowPath(); c.stroke();
  }
  function tipLabel(c, s, x1, y1, x2, y2, color) {
    var dx = x2 - x1, dy = y2 - y1, n = Math.hypot(dx, dy) || 1;
    vecLabel(c, s, x2 + dx / n * 16, y2 + dy / n * 16 + 6, color);
  }
  /* ================= 1. Relativité du mouvement ================= */
  (function () {
    var root = document.getElementById('lab-ref');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), btn = $(root, '[data-act="play"]'), S, mode = 'sol', playing = !RM, visible = true, t = 0, last = null;
    var U = 2.0, H = 1.25, G = 9.81, TF = Math.sqrt(2 * H / G), SLOW = 4, CYCLE = TF * SLOW + 1.2;
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, k = Math.min(78, w / 8.5), yg = h - 30;
      c.clearRect(0, 0, w, h);
      var TL = Math.sqrt(2 * (H - 7 / k) / G);                       /* instant où la balle touche le plancher */
      var tc = t % CYCLE, tp = Math.min(tc / SLOW, TL);           /* temps physique (ralenti), figé à l'arrivée */
      var sol = mode === 'sol', x0 = 0.8;
      /* dans le référentiel terrestre le train avance ; dans celui du train, c'est le sol qui recule */
      var xTrain = sol ? x0 + U * tp : x0, shift = sol ? 0 : U * tp;
      function X(xm) { return 20 + xm * k; }
      function Y(ym) { return yg - ym * k; }
      var gg = c.createLinearGradient(0, yg, 0, h); gg.addColorStop(0, '#E2E8F0'); gg.addColorStop(1, '#F1F5F9');
      c.fillStyle = gg; c.fillRect(0, yg, w, h - yg);
      c.strokeStyle = '#CBD5E1'; c.lineWidth = 1.5; c.beginPath(); c.moveTo(0, yg); c.lineTo(w, yg); c.stroke();
      /* petits piquets le long de la voie (repères fixes du sol) */
      for (var p = -10; p < 40; p++) {
        var xp = X(p - shift);
        if (xp > -10 && xp < w + 10) { c.fillStyle = '#CBD5E1'; c.beginPath(); if (c.roundRect) { c.roundRect(xp - 2, yg - 16, 4, 16, 2); } else { c.rect(xp - 2, yg - 16, 4, 16); } c.fill(); }
      }
      txt(c, 'sol', 30, yg + 20, col('--slate'), '600 12px system-ui, sans-serif', 'left');
      /* wagon */
      var wx = X(xTrain), ww = 4.2 * k, wh = 2.3 * k;
      c.fillStyle = 'rgba(42,107,196,.08)'; c.strokeStyle = CP; c.lineWidth = 2.5;
      c.beginPath(); c.rect(wx, Y(2.5), ww, wh); c.fill(); c.stroke();
      /* roues : elles tournent quand le train avance par rapport au sol */
      var rw = 0.18 * k, rot = U * tp / 0.18;
      [0.8, 3.4].forEach(function (r) {
        var cx0 = wx + r * k, cy0 = yg - rw;
        c.fillStyle = '#94A3B8'; c.beginPath(); c.arc(cx0, cy0, rw, 0, 2 * Math.PI); c.fill();
        c.fillStyle = '#E2E8F0'; c.beginPath(); c.arc(cx0, cy0, rw * 0.55, 0, 2 * Math.PI); c.fill();
        c.strokeStyle = '#94A3B8'; c.lineWidth = 1.5;
        for (var q = 0; q < 3; q++) { var an = rot + q * Math.PI / 3; c.beginPath(); c.moveTo(cx0 - Math.cos(an) * rw * 0.55, cy0 - Math.sin(an) * rw * 0.55); c.lineTo(cx0 + Math.cos(an) * rw * 0.55, cy0 + Math.sin(an) * rw * 0.55); c.stroke(); }
      });
      txt(c, 'wagon', wx + ww - 30, Y(2.5) + 18, CP, '600 12px system-ui, sans-serif');
      /* traces de la balle (une position tous les 0,04 s) */
      function bxAt(s) { return sol ? x0 + 1.6 + U * s : x0 + 1.6; }
      var tr = [];
      for (var s = 0; s <= tp + 1e-9; s += 0.04) { tr.push([bxAt(s), Math.max(0.2 + 7 / k, 0.2 + H - 0.5 * G * s * s)]); }
      tr.forEach(function (q, i) { c.fillStyle = 'rgba(225,29,72,' + (0.25 + 0.5 * i / tr.length) + ')'; c.beginPath(); c.arc(X(q[0]), Y(q[1]), 3, 0, 2 * Math.PI); c.fill(); });
      var rb = 7 / k, bx = bxAt(tp), by = Math.max(0.2 + rb, 0.2 + H - 0.5 * G * tp * tp);   /* la balle s'arrête sur le plancher */
      c.fillStyle = CT; c.beginPath(); c.arc(X(bx), Y(by), 7, 0, 2 * Math.PI); c.fill();
      /* le passager, debout dans le wagon, bras tendu */
      var px = xTrain + 1.15;
      c.strokeStyle = '#94A3B8'; c.lineWidth = 3; c.lineCap = 'round';
      c.beginPath(); c.moveTo(X(px), Y(1.55)); c.lineTo(X(px), Y(0.95));
      c.moveTo(X(px), Y(0.95)); c.lineTo(X(px - 0.15), Y(0.2)); c.moveTo(X(px), Y(0.95)); c.lineTo(X(px + 0.15), Y(0.2));
      c.moveTo(X(px), Y(1.45)); c.lineTo(X(xTrain + 1.6) - 9, Y(0.2 + H) - 3);
      c.moveTo(X(px), Y(1.45)); c.lineTo(X(px - 0.2), Y(1.05)); c.stroke();
      c.fillStyle = '#94A3B8'; c.beginPath(); c.arc(X(px), Y(1.72), 0.14 * k, 0, 2 * Math.PI); c.fill();
      txt(c, mode === 'sol' ? 'Vue depuis le quai (référentiel terrestre)' : 'Vue depuis le wagon (référentiel du train)', w / 2, 20, col('--ink'));
      msg.textContent = mode === 'sol' ? 'Pour une personne sur le quai, la balle avance avec le train pendant sa chute : sa trajectoire est une portion de parabole.'
        : 'Pour le passager, la balle tombe à la verticale, juste sous sa main : sa trajectoire est un segment de droite.';
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    $$(root, 'input[name="ref"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; t = 0; draw(); }); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    if (RM) { t = TF * SLOW; }
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* trajectoire commune aux animations 2 : M(t) = (x(t), y(t)) en mètres */
  function Mx(t) { return 0.4 + 1.7 * t; }
  function My(t) { return 0.5 + 2.8 * t - 1.05 * t * t; }
  /* ================= 2. Du vecteur vitesse moyenne au vecteur vitesse ================= */
  (function () {
    var root = document.getElementById('lab-vmoy');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rT = $(root, '[data-p="t"]'), rD = $(root, '[data-p="dt"]'), oD = $(root, '.out-dt'), oVm = $(root, '.out-vm'), oV = $(root, '.out-v'), msg = $(root, '.nt-msg'), S;
    var KV = 0.32;   /* échelle : longueur de la flèche (m) pour 1 m/s */
    function draw() {
      var t0 = parseFloat(rT.value), dt = parseFloat(rD.value), t1 = t0 + dt;
      var c = S.ctx, w = S.w, h = S.h, k = Math.min((w - 40) / 5.2, (h - 30) / 2.6), ox = 20, oy = h - 18;
      function X(x) { return ox + x * k; }
      function Y(y) { return oy - y * k; }
      c.clearRect(0, 0, w, h);
      c.strokeStyle = CT; c.lineWidth = 3; c.beginPath();
      for (var s = 0; s <= 2.75; s += 0.02) { if (s === 0) { c.moveTo(X(Mx(s)), Y(My(s))); } else { c.lineTo(X(Mx(s)), Y(My(s))); } }
      c.stroke();
      var A = [Mx(t0), My(t0)], B = [Mx(t1), My(t1)], vx = (B[0] - A[0]) / dt, vy = (B[1] - A[1]) / dt;
      var Vx = 1.7, Vy = 2.8 - 2.1 * t0;
      /* corde */
      arrow(c, X(A[0]), Y(A[1]), X(B[0]), Y(B[1]), CP, 2.2);
      /* tangente */
      c.strokeStyle = 'rgba(217,119,6,.45)'; c.setLineDash([5, 5]); c.lineWidth = 1.5;
      c.beginPath(); c.moveTo(X(A[0] - Vx * 0.6), Y(A[1] - Vy * 0.6)); c.lineTo(X(A[0] + Vx * 0.9), Y(A[1] + Vy * 0.9)); c.stroke(); c.setLineDash([]);
      arrow(c, X(A[0]), Y(A[1]), X(A[0] + Vx * KV), Y(A[1] + Vy * KV), CV, 3.2);
      arrow(c, X(A[0]), Y(A[1]), X(A[0] + vx * KV), Y(A[1] + vy * KV), CA, 2.6, [6, 4]);
      [[A, 'M(t)'], [B, 'M(t+\u0394t)']].forEach(function (q, i) {
        c.fillStyle = CT; c.beginPath(); c.arc(X(q[0][0]), Y(q[0][1]), 5.5, 0, 2 * Math.PI); c.fill();
        txt(c, q[1], X(q[0][0]) + (i === 0 ? -12 : 10), Y(q[0][1]) - 12, CT, 'italic 700 14px Georgia, serif', i === 0 ? 'right' : 'left', true);
      });
      oD.textContent = fr(dt, 2) + ' s';
      oVm.textContent = fr(Math.hypot(vx, vy), 2) + ' m\u00b7s\u207b\u00b9'; oV.textContent = fr(Math.hypot(Vx, Vy), 2) + ' m\u00b7s\u207b\u00b9';
      msg.textContent = dt > 0.3 ? 'Le vecteur vitesse moyenne (pointillés verts) a la direction de la corde M(t)M(t+\u0394t), qui s\u2019écarte nettement de la tangente.'
        : (dt > 0.08 ? 'Quand \u0394t diminue, la corde se rapproche de la tangente et le vecteur vitesse moyenne se rapproche du vecteur vitesse.' : 'Pour \u0394t très petit, le vecteur vitesse moyenne se confond avec le vecteur vitesse (en orange), tangent à la trajectoire.');
    }
    [rT, rD].forEach(function (r) { r.addEventListener('input', draw); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 3. Chronophotographie : vitesse et accélération ================= */
  (function () {
    var root = document.getElementById('lab-chrono');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rI = $(root, 'input[type="range"]'), cbV = $(root, '[data-p="v"]'), cbD = $(root, '[data-p="dv"]'), cbA = $(root, '[data-p="a"]'), cbE = $(root, '[data-p="ex"]');
    var msg = $(root, '.nt-msg'), oE = $(root, '.out-err'), oF = $(root, '.nt-chrono-form'), S, mode = 'para', meth = 'mil';
    var TAU = 0.08;
    var MOV = {
      para: { n: 15, i0: 4, f: function (t) { return [0.3 + 3.2 * t, 0.3 + 4.6 * t - 4.905 * t * t]; }, kv: 0.28, ka: 0.065, m: 'Chute libre (lancer oblique) : le vecteur accélération est le même en tout point, vertical et vers le bas.' },
      circ: { n: 17, i0: 8, f: function (t) { var w = 2.6; return [2.1 + 1.0 * Math.cos(w * t - 2.6), 1.15 + 1.0 * Math.sin(w * t - 2.6)]; }, kv: 0.22, ka: 0.07, m: 'Mouvement circulaire uniforme : la vitesse garde la même norme, mais sa direction tourne ; le vecteur accélération pointe vers le centre du cercle.' },
      frein: { n: 14, i0: 5, f: function (t) { return [0.3 + 4.4 * t - 2.6 * t * t, 1.0]; }, kv: 0.12, ka: 0.08, m: 'Mouvement rectiligne freiné : les vecteurs vitesse raccourcissent ; le vecteur accélération est opposé au mouvement.' }
    };
    var FORM = {
      mil: 'Point milieu : $\\vec{v}_i \\approx \\dfrac{\\overrightarrow{\\mathrm{M}_{i-1}\\mathrm{M}_{i+1}}}{2\\tau}$, puis $\\Delta\\vec{v}_i = \\vec{v}_{i+1}-\\vec{v}_{i-1}$ et $\\vec{a}_i \\approx \\dfrac{\\Delta\\vec{v}_i}{2\\tau}$.',
      apr: 'Point d\u2019après : $\\vec{v}_i \\approx \\dfrac{\\overrightarrow{\\mathrm{M}_{i}\\mathrm{M}_{i+1}}}{\\tau}$, puis $\\Delta\\vec{v}_i = \\vec{v}_{i+1}-\\vec{v}_{i}$ et $\\vec{a}_i \\approx \\dfrac{\\Delta\\vec{v}_i}{\\tau}$.'
    };
    function pts() { var m = MOV[mode], P = []; for (var i = 0; i < m.n; i++) { P.push(m.f(i * TAU)); } return P; }
    function draw() {
      var P = pts(), m = MOV[mode], c = S.ctx, w = S.w, h = S.h;
      /* cadrage : les points ET les extrémités de tous les vecteurs vitesse possibles doivent rester visibles */
      var xs = P.map(function (p) { return p[0]; }), ys = P.map(function (p) { return p[1]; });
      for (var jj = 1; jj < P.length - 1; jj++) {
        var vxj = (P[jj + 1][0] - P[jj - 1][0]) / (2 * TAU), vyj = (P[jj + 1][1] - P[jj - 1][1]) / (2 * TAU);
        xs.push(P[jj][0] + vxj * m.kv); ys.push(P[jj][1] + vyj * m.kv);
      }
      var x0 = Math.min.apply(null, xs) - 0.35, x1 = Math.max.apply(null, xs) + 0.35, y0 = Math.min.apply(null, ys) - 0.45, y1 = Math.max.apply(null, ys) + 0.45;
      var k = Math.min(w / (x1 - x0), h / (y1 - y0));
      function X(x) { return (w - (x1 - x0) * k) / 2 + (x - x0) * k; }
      function Y(y) { return h - (h - (y1 - y0) * k) / 2 - (y - y0) * k; }
      rI.max = m.n - 3; if (+rI.value > m.n - 3) { rI.value = m.n - 3; } if (+rI.value < 2) { rI.value = 2; }
      var i = parseInt(rI.value, 10), mil = meth === 'mil';
      if (mode === 'circ') { c.save(); }
      /* points utilisés par la méthode choisie */
      var jlo = mil ? i - 2 : i, jhi = i + 2;
      var lab = [];
      c.clearRect(0, 0, w, h);
      if (mode === 'circ') {   /* centre du cercle */
        c.strokeStyle = col('--ink'); c.lineWidth = 1.5; c.beginPath(); c.moveTo(X(2.1) - 6, Y(1.15)); c.lineTo(X(2.1) + 6, Y(1.15)); c.moveTo(X(2.1), Y(1.15) - 6); c.lineTo(X(2.1), Y(1.15) + 6); c.stroke();
        txt(c, 'O', X(2.1) - 10, Y(1.15) - 8, col('--ink'), 'italic 700 13px Georgia, serif');
        c.restore();
      }
      P.forEach(function (p, j) {
        c.fillStyle = (j >= jlo && j <= jhi) ? CT : 'rgba(225,29,72,.40)';
        c.beginPath(); c.arc(X(p[0]), Y(p[1]), j === i ? 6 : 4, 0, 2 * Math.PI); c.fill();
        if (j >= (mil ? i - 1 : i) && j <= i + 1) { lab.push([j, p]); }
      });
      var KV = m.kv, KA = m.ka, va, vb, Pa, Pb, la, lb, div, labels = [];
      if (mil) {
        var vm = function (j) { return [(P[j + 1][0] - P[j - 1][0]) / (2 * TAU), (P[j + 1][1] - P[j - 1][1]) / (2 * TAU)]; };
        va = vm(i - 1); vb = vm(i + 1); Pa = P[i - 1]; Pb = P[i + 1]; la = 'v' + (i - 1); lb = 'v' + (i + 1); div = 2 * TAU;
      } else {
        var vp = function (j) { return [(P[j + 1][0] - P[j][0]) / TAU, (P[j + 1][1] - P[j][1]) / TAU]; };
        va = vp(i); vb = vp(i + 1); Pa = P[i]; Pb = P[i + 1]; la = 'v' + i; lb = 'v' + (i + 1); div = TAU;
      }
      if (cbV.checked) {
        arrow(c, X(Pa[0]), Y(Pa[1]), X(Pa[0] + va[0] * KV), Y(Pa[1] + va[1] * KV), CV, 2.6);
        arrow(c, X(Pb[0]), Y(Pb[1]), X(Pb[0] + vb[0] * KV), Y(Pb[1] + vb[1] * KV), CV, 2.6);
        if (mode === 'frein') {   /* vecteurs horizontaux : étiquettes au-dessus du milieu de chaque vecteur */
          labels.push(function () { vecLabel(c, la, X(Pa[0] + va[0] * KV / 2), Y(Pa[1]) - 14, CV); });
          labels.push(function () { vecLabel(c, lb, X(Pb[0] + vb[0] * KV / 2), Y(Pb[1]) - 14, CV); });
        } else {   /* au milieu de chaque vecteur, décalée du côté convexe de la trajectoire (à l'opposé de l'accélération) */
          labels.push(function () { sideLabel(la, Pa, va); });
          labels.push(function () { sideLabel(lb, Pb, vb); });
        }
      }
      var Mi = P[i], ax = (vb[0] - va[0]) / div, ay = (vb[1] - va[1]) / div;
      function sideLabel(s, Q, vv) {
        var x1p = X(Q[0]), y1p = Y(Q[1]), x2p = X(Q[0] + vv[0] * KV), y2p = Y(Q[1] + vv[1] * KV);
        var dx = x2p - x1p, dy = y2p - y1p, nn = Math.hypot(dx, dy) || 1, nx = -dy / nn, ny = dx / nn;
        if (nx * ax - ny * ay > 0) { nx = -nx; ny = -ny; }   /* l'axe y de l'écran est inversé */
        vecLabel(c, s, (x1p + x2p) / 2 + nx * 20, (y1p + y2p) / 2 + ny * 20 + 6, CV);
      }
      if (cbD.checked) {
        var e1 = [Mi[0] + vb[0] * KV, Mi[1] + vb[1] * KV], e2 = [e1[0] - va[0] * KV, e1[1] - va[1] * KV];
        arrow(c, X(Mi[0]), Y(Mi[1]), X(e1[0]), Y(e1[1]), CV, 2, [5, 4]);
        arrow(c, X(e1[0]), Y(e1[1]), X(e2[0]), Y(e2[1]), '#B45309', 2, [5, 4]);
        arrow(c, X(Mi[0]), Y(Mi[1]), X(e2[0]), Y(e2[1]), CA, 2.4);
        /* étiquette de Δv : au milieu du vecteur, du côté opposé au triangle de construction */
        var mx = (X(Mi[0]) + X(e2[0])) / 2, my = (Y(Mi[1]) + Y(e2[1])) / 2, dx = X(e2[0]) - X(Mi[0]), dy = Y(e2[1]) - Y(Mi[1]), nn = Math.hypot(dx, dy) || 1;
        var nx = -dy / nn, ny = dx / nn; if (nx * (X(e1[0]) - mx) + ny * (Y(e1[1]) - my) > 0) { nx = -nx; ny = -ny; }
        if (mode === 'frein') { labels.push(function () { vecLabel(c, '\u0394v' + i, mx, my + 46, CA); }); }   /* sous l'axe, les étiquettes de vitesse étant au-dessus */
        else { labels.push(function () { vecLabel(c, '\u0394v' + i, mx + nx * 22, my + ny * 22 + 6, CA); }); }
      }
      /* vraie accélération en M_i (dérivée seconde calculée avec un pas minuscule) */
      var hh = 1e-3, ti = i * TAU, fp = m.f(ti + hh), f0 = m.f(ti), fm = m.f(ti - hh);
      var tx = (fp[0] - 2 * f0[0] + fm[0]) / (hh * hh), ty = (fp[1] - 2 * f0[1] + fm[1]) / (hh * hh);
      if (cbE.checked) { arrow(c, X(Mi[0]), Y(Mi[1]), X(Mi[0] + tx * KA), Y(Mi[1] + ty * KA), 'rgba(30,41,59,.55)', 2, [3, 3]); }
      if (cbA.checked) {
        arrow(c, X(Mi[0]), Y(Mi[1]), X(Mi[0] + ax * KA), Y(Mi[1] + ay * KA), CA, 3.4);
        labels.push(function () { tipLabel(c, 'a' + i, X(Mi[0]), Y(Mi[1]), X(Mi[0] + ax * KA), Y(Mi[1] + ay * KA), CA); });
      }
      /* toutes les étiquettes en dernier, par-dessus les tracés */
      lab.forEach(function (q) { txt(c, 'M' + q[0], X(q[1][0]) + 4, Y(q[1][1]) + 21, CT, 'italic 700 12px Georgia, serif', 'center', true); });
      labels.forEach(function (f) { f(); });
      var ang = Math.abs(Math.atan2(ax * ty - ay * tx, ax * tx + ay * ty)) * 180 / Math.PI, nr = Math.hypot(ax, ay) / Math.hypot(tx, ty) - 1;
      oE.textContent = fr(ang, 1) + '\u00b0 en direction, ' + (Math.abs(nr) < 0.0005 ? '0' : fr(nr * 100, 1)) + ' % en norme';
      msg.textContent = m.m;
    }
    function form() { oF.innerHTML = FORM[meth]; if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([oF]); } else if (window.renderMathInElement) { window.renderMathInElement(oF); } }
    rI.addEventListener('input', draw);
    [cbV, cbD, cbA, cbE].forEach(function (x) { x.addEventListener('change', draw); });
    $$(root, 'input[name="mov"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; rI.value = MOV[mode].i0; draw(); }); });
    $$(root, 'input[name="meth"]').forEach(function (x) { x.addEventListener('change', function () { meth = x.value; form(); draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 4. Position, vitesse et accélération d'un mouvement rectiligne ================= */
  (function () {
    var root = document.getElementById('lab-xva');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rX = $(root, '[data-p="x0"]'), rV = $(root, '[data-p="v0"]'), rA = $(root, '[data-p="a"]'), btn = $(root, '[data-act="play"]');
    var oX = $(root, '.out-x0'), oV = $(root, '.out-v0'), oA = $(root, '.out-a'), msg = $(root, '.nt-msg'), S, playing = !RM, visible = true, t = 0, last = null, TM = 5;
    function p() { return { x0: +rX.value, v0: +rV.value, a: +rA.value }; }
    function X(q, s) { return q.x0 + q.v0 * s + 0.5 * q.a * s * s; }
    function V(q, s) { return q.v0 + q.a * s; }
    function draw() {
      var q = p(), c = S.ctx, w = S.w, h = S.h, ts = t % (TM + 1.0), tt = Math.min(ts, TM);
      oX.textContent = fr(q.x0, 1) + ' m'; oV.textContent = fr(q.v0, 1) + ' m\u00b7s\u207b\u00b9'; oA.textContent = fr(q.a, 1) + ' m\u00b7s\u207b\u00b2';
      c.clearRect(0, 0, w, h);
      /* piste */
      var trackY = 34, xs = [];
      for (var s0 = 0; s0 <= TM; s0 += 0.1) { xs.push(X(q, s0)); }
      var lo = Math.min.apply(null, xs), hi = Math.max.apply(null, xs), span = Math.max(10, hi - lo);
      var stp = span > 120 ? 25 : (span > 60 ? 10 : 5);   /* pas des graduations selon l'étendue */
      var XMIN = Math.floor(lo / stp) * stp - stp, XMAX = Math.ceil(hi / stp) * stp + stp;
      function PX(x) { return 40 + (x - XMIN) / (XMAX - XMIN) * (w - 80); }
      c.strokeStyle = col('--slate'); c.lineWidth = 2; c.beginPath(); c.moveTo(PX(XMIN), trackY + 10); c.lineTo(PX(XMAX), trackY + 10); c.stroke();
      for (var g = XMIN; g <= XMAX; g += stp) { c.beginPath(); c.moveTo(PX(g), trackY + 6); c.lineTo(PX(g), trackY + 14); c.stroke(); txt(c, g + ' m', PX(g), trackY + 27, col('--muted'), '10px system-ui, sans-serif'); }
      var xc = Math.max(XMIN, Math.min(XMAX, X(q, tt)));
      c.fillStyle = CP; c.beginPath(); if (c.roundRect) { c.roundRect(PX(xc) - 14, trackY - 8, 28, 16, 5); } else { c.rect(PX(xc) - 14, trackY - 8, 28, 16); } c.fill();
      var vv = V(q, tt);
      /* échelle choisie pour que la plus grande vitesse atteinte donne une flèche de 60 px */
      var vmax = 0.1; for (var s1 = 0; s1 <= TM; s1 += 0.1) { vmax = Math.max(vmax, Math.abs(V(q, s1))); }
      if (Math.abs(vv) > 0.05) { arrow(c, PX(xc), trackY - 16, PX(xc) + vv / vmax * 60, trackY - 16, CV, 2.6); }
      /* trois graphes */
      var G = [{ f: function (s) { return X(q, s); }, c: CP, n: 'x(t) (m)' }, { f: function (s) { return V(q, s); }, c: CV, n: 'v(t) (m\u00b7s\u207b\u00b9)' }, { f: function () { return q.a; }, c: CA, n: 'a(t) (m\u00b7s\u207b\u00b2)' }];
      var top = 66, gh = (h - top - 22) / 3;
      G.forEach(function (gr, k) {
        var y0 = top + k * gh, L = 46, R = w - 14, T = y0 + 6, B = y0 + gh - 10, vals = [];
        for (var s = 0; s <= TM; s += 0.05) { vals.push(gr.f(s)); }
        var mn = Math.min(0, Math.min.apply(null, vals)), mx = Math.max(0, Math.max.apply(null, vals));
        if (mx - mn < 1) { mx += 0.5; mn -= 0.5; }
        function GX(s) { return L + s / TM * (R - L); }
        function GY(v) { return B - (v - mn) / (mx - mn) * (B - T); }
        c.strokeStyle = col('--line'); c.lineWidth = 1; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.stroke();
        c.strokeStyle = col('--muted'); c.beginPath(); c.moveTo(L, GY(0)); c.lineTo(R, GY(0)); c.stroke();
        txt(c, gr.n, L + 8, T + 10, gr.c, '700 12px system-ui, sans-serif', 'left');
        [mn, mx].forEach(function (v) { if (Math.abs(v) > 1e-9 && Math.abs(GY(v) - GY(0)) > 12) { txt(c, fr(v, Math.abs(v) < 10 ? 1 : 0), L - 6, GY(v) + 4, col('--muted'), '10px system-ui, sans-serif', 'right'); c.strokeStyle = col('--line'); c.beginPath(); c.moveTo(L - 3, GY(v)); c.lineTo(L, GY(v)); c.stroke(); } });
        txt(c, '0', L - 6, GY(0) + 4, col('--muted'), '10px system-ui, sans-serif', 'right');
        c.strokeStyle = gr.c; c.lineWidth = 2.4; c.beginPath();
        vals.forEach(function (v, j) { var xx = GX(j * 0.05), yy = GY(v); if (j === 0) { c.moveTo(xx, yy); } else { c.lineTo(xx, yy); } });
        c.stroke();
        c.fillStyle = gr.c; c.beginPath(); c.arc(GX(tt), GY(gr.f(tt)), 5, 0, 2 * Math.PI); c.fill();
        if (k === 2) { for (var s2 = 0; s2 <= TM; s2++) { txt(c, s2 + ' s', GX(s2), B + 14, col('--muted'), '10px system-ui, sans-serif'); } }
      });
      c.strokeStyle = 'rgba(30,41,59,.25)'; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(46 + tt / TM * (w - 60), top); c.lineTo(46 + tt / TM * (w - 60), h - 22); c.stroke(); c.setLineDash([]);
      msg.textContent = q.a === 0 ? (q.v0 === 0 ? 'Le mobile est immobile.' : 'Mouvement rectiligne uniforme : v(t) est constante, x(t) est une fonction affine du temps et a(t) est nulle.')
        : 'Mouvement rectiligne uniformément ' + (q.v0 * q.a < 0 ? 'varié : ' : 'accéléré : ') + 'a(t) est constante, v(t) est une fonction affine du temps et x(t) une parabole.' + (q.v0 * q.a < 0 ? ' Ici le mobile freine, s\u2019arrête (v = 0, sommet de la parabole) puis repart en sens inverse.' : '');
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts; if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    [rX, rV, rA].forEach(function (r) { r.addEventListener('input', function () { t = 0; draw(); }); });
    $$(root, '[data-preset]').forEach(function (b) {
      b.addEventListener('click', function () { var v = b.getAttribute('data-preset').split(','); rX.value = v[0]; rV.value = v[1]; rA.value = v[2]; t = 0; draw(); });
    });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (v) { visible = v; });
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 5. Mouvement circulaire et repère de Frenet ================= */
  (function () {
    var root = document.getElementById('lab-frenet');
    if (!root) { return; }
    var cv = $(root, 'canvas'), cbC = $(root, '[data-p="comp"]'), btn = $(root, '[data-act="play"]'), oV = $(root, '.out-v'), oT = $(root, '.out-at'), oN = $(root, '.out-an'), msg = $(root, '.nt-msg');
    var S, mode = 'unif', playing = !RM, visible = true, t = 0, last = null, R = 1.0, theta = 0, v = 1.2, AT = { unif: 0, acc: 0.6, frein: -0.6 }, SLOWF = 0.55, VMIN = 0.6, VMAX = 2.0;
    function reset() { theta = Math.PI * 0.15; v = mode === 'frein' ? VMAX : (mode === 'acc' ? VMIN : 1.4); }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, k = Math.min(w, h) * 0.36, cx = w * 0.45, cy = h / 2;
      c.clearRect(0, 0, w, h);
      c.strokeStyle = CT; c.lineWidth = 2.5; c.beginPath(); c.arc(cx, cy, R * k, 0, 2 * Math.PI); c.stroke();
      c.fillStyle = col('--ink'); c.beginPath(); c.arc(cx, cy, 4, 0, 2 * Math.PI); c.fill(); txt(c, 'O', cx - 12, cy + 4, col('--ink'), 'italic 700 14px Georgia, serif');
      var mx = cx + R * k * Math.cos(theta), my = cy - R * k * Math.sin(theta);
      var uT = [-Math.sin(theta), -Math.cos(theta)], uN = [-Math.cos(theta), Math.sin(theta)];   /* en coordonnées écran, sens trigonométrique */
      c.strokeStyle = 'rgba(30,41,59,.25)'; c.setLineDash([4, 4]); c.lineWidth = 1; c.beginPath(); c.moveTo(cx, cy); c.lineTo(mx, my); c.stroke(); c.setLineDash([]);
      var aT = AT[mode], aN = v * v / R, KV = 0.45 * k, KA = 0.24 * k;
      arrow(c, mx, my, mx + uT[0] * v * KV, my + uT[1] * v * KV, CV, 3.2);
      /* étiquette au milieu du vecteur, décalée vers l'extérieur du cercle : elle suit le vecteur sans jamais le couvrir */
      var ro = [Math.cos(theta), -Math.sin(theta)];
      vecLabel(c, 'v', mx + uT[0] * v * KV * 0.6 + ro[0] * 20, my + uT[1] * v * KV * 0.6 + ro[1] * 20 + 6, CV, true);
      var axs = mx + (uT[0] * aT + uN[0] * aN) * KA, ays = my + (uT[1] * aT + uN[1] * aN) * KA;
      if (cbC.checked && Math.abs(aT) > 1e-6) {
        arrow(c, mx, my, mx + uT[0] * aT * KA, my + uT[1] * aT * KA, CA, 2, [5, 4]);
        arrow(c, mx, my, mx + uN[0] * aN * KA, my + uN[1] * aN * KA, CA, 2, [5, 4]);
        c.strokeStyle = 'rgba(5,150,105,.4)'; c.setLineDash([2, 3]); c.lineWidth = 1;
        c.beginPath(); c.moveTo(mx + uT[0] * aT * KA, my + uT[1] * aT * KA); c.lineTo(axs, ays); c.lineTo(mx + uN[0] * aN * KA, my + uN[1] * aN * KA); c.stroke(); c.setLineDash([]);
      }
      arrow(c, mx, my, axs, ays, CA, 3.2);
      vecLabel(c, 'a', axs + (axs - mx) * 0.12, ays + (ays - my) * 0.12 + 4, CA);
      var U = 0.26 * k;
      arrow(c, mx, my, mx + uT[0] * U, my + uT[1] * U, col('--slate'), 1.6); arrow(c, mx, my, mx + uN[0] * U, my + uN[1] * U, col('--slate'), 1.6);
      /* étiquettes des vecteurs unitaires, décalées sur le côté pour ne pas chevaucher v et a */
      txt(c, 'u\u209c', mx + uT[0] * U * 0.6 - uN[0] * 16, my + uT[1] * U * 0.6 - uN[1] * 16 + 4, col('--slate'), 'italic 700 13px Georgia, serif');
      txt(c, 'u\u2099', mx + uN[0] * U * 0.6 - uT[0] * 16, my + uN[1] * U * 0.6 - uT[1] * 16 + 4, col('--slate'), 'italic 700 13px Georgia, serif');
      c.fillStyle = CT; c.beginPath(); c.arc(mx, my, 6, 0, 2 * Math.PI); c.fill();
      /* le nom du point reste à l'extérieur du cercle, sur le rayon prolongé */
      txt(c, 'M', cx + (R * k + 22) * Math.cos(theta), cy - (R * k + 22) * Math.sin(theta) + 5, CT, 'italic 700 15px Georgia, serif', 'center', true);
      oV.textContent = fr(v, 2) + ' m\u00b7s\u207b\u00b9'; oT.textContent = fr(aT, 2) + ' m\u00b7s\u207b\u00b2'; oN.textContent = fr(aN, 2) + ' m\u00b7s\u207b\u00b2';
      msg.textContent = mode === 'unif' ? 'Mouvement circulaire uniforme : a\u209c = dv/dt = 0, le vecteur accélération est porté par u\u2099 : il est centripète.'
        : (mode === 'acc' ? 'Le mobile accélère : a\u209c > 0, le vecteur accélération penche vers l\u2019avant. Sa composante normale v\u00b2/R augmente avec la vitesse.'
          : 'Le mobile freine : a\u209c < 0, le vecteur accélération penche vers l\u2019arrière.');
    }
    function step(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (playing && visible) {
        var ds = dt * SLOWF;   /* temps ralenti : chaque phase accélérée ou freinée dure environ 4 s */
        v += AT[mode] * ds; theta += v / R * ds;
        if (v > VMAX + 1e-9 || v < VMIN - 1e-9) { reset(); }
      }
      if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    $$(root, 'input[name="circ"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; reset(); draw(); }); });
    cbC.addEventListener('change', draw);
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); draw(); }
    watchVisible(cv, function (vv) { visible = vv; });
    reset(); playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
})();
</script>
