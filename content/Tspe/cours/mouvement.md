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
<canvas style="height:300px;" aria-label="Chute d'une balle lâchée dans un train en mouvement, vue depuis le quai ou depuis le wagon"></canvas>
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

<details class="nt-d nt-plus" id="memo-primitives">
<summary><span class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Mémo maths</span><span class="nt-sum">La dérivée</span></summary>
<div class="nt-d-body">
La dérivée d'une fonction mesure la rapidité avec laquelle elle varie, à un instant donné.<br>
Pour l'obtenir, on calcule un taux de variation sur un petit intervalle, puis on fait tendre cet intervalle vers zéro. Graphiquement, c'est la <b>pente de la tangente</b> à la courbe.</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Définition</p>
<p class="nt-f-math">$$f'(t) = \dfrac{\mathrm{d}f}{\mathrm{d}t} = \displaystyle\lim_{\Delta t \to 0} \dfrac{f(t+\Delta t)-f(t)}{\Delta t}$$</p>
</div>

<p><b>Les dérivées utiles en physique</b> ($a$ est une constante, la variable est le temps $t$)&nbsp;:</p>
<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>fonction $f(t)$</th><th>dérivée $f'(t)$</th><th>exemple en physique</th></tr></thead>
<tbody>
<tr><td>$a$ (constante)</td><td>$0$</td><td>une position constante&nbsp;: vitesse nulle</td></tr>
<tr><td>$a\,t$</td><td>$a$</td><td>$x(t) = 3\,t$&nbsp;: $v_x = 3~\pu{m*s-1}$</td></tr>
<tr><td>$a\,t^2$</td><td>$2\,a\,t$</td><td>$x(t) = 5\,t^2$&nbsp;: $v_x(t) = 10\,t$</td></tr>
<tr><td>$\mathrm{e}^{kt}$</td><td>$k\,\mathrm{e}^{t}$</td><td>la décharge d'un condensateur, la radioactivité</td></tr>
<tr><td>$\cos t$</td><td>$-\sin t$</td><td>les oscillations</td></tr>
<tr><td>$\sin t$</td><td>$\cos t$</td><td>les oscillations</td></tr>
</tbody>
</table>
</div>
<p><b>Deux règles de calcul</b>&nbsp;:</p>
<ul style="margin-top:0;margin-bottom:0;">
<li>la dérivée d'une somme est la somme des dérivées, $(u+v)' = u'+v'$,</li> 
<li>et on peut sortir une constante, $(a\,u)' = a\,u'$.</li>
</div>
</details>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Un point se déplace sur un axe selon $x(t) = 4\,t^2 - 3\,t + 2$ (en mètres, $t$ en secondes). Sa vitesse est&nbsp;:</p>
<p class="nt-center">$v_x(t) = \dfrac{\mathrm{d}x}{\mathrm{d}t} = 4 \times 2\,t - 3 + 0 = 8\,t - 3$</p>
<p>À $t = 2~\text{s}$, $v_x = 8 \times 2 - 3 = 13~\pu{m*s-1}$.</p>
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

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-arrows-rotate"></i>Rappel&nbsp;: convertir une vitesse</p>
<p>Dans la vie courante, les vitesses s'expriment souvent en kilomètres par heure ($\pu{km*h-1}$), mais l'unité du Système international est le mètre par seconde ($\pu{m*s-1}$). Comme $1~\text{km} = 1\,000~\text{m}$ et $1~\text{h} = 3\,600~\text{s}$&nbsp;:</p>
<p class="nt-center">$1~\pu{km*h-1} = \dfrac{1\,000~\text{m}}{3\,600~\text{s}} = \dfrac{1}{3{,}6}~\pu{m*s-1}$</p>
<svg class='nt-svg nt-svg-s' viewBox='0 0 440 200' role='img' aria-label="Conversion des vitesses : pour passer des kilomètres par heure aux mètres par seconde, on divise par 3,6 ; pour passer des mètres par seconde aux kilomètres par heure, on multiplie par 3,6"><defs><marker id='mkB' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 z' fill='#2563EB'/></marker><marker id='mkO' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 z' fill='#EA580C'/></marker></defs><rect x='40' y='70' width='100' height='50' rx='12' fill='#EFF6FF' stroke='#2563EB' stroke-width='1.5'/><text x='90' y='102' font-size='20' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif'>km·h⁻¹</text><rect x='300' y='70' width='100' height='50' rx='12' fill='#FFF7ED' stroke='#EA580C' stroke-width='1.5'/><text x='350' y='102' font-size='20' text-anchor='middle' fill='#1E293B' font-family='system-ui, sans-serif'>m·s⁻¹</text><path d='M110,66 Q220,-6 330,66' fill='none' stroke='#2563EB' stroke-width='2.2' marker-end='url(#mkB)'/><text x='220' y='20' font-size='19' text-anchor='middle' fill='#2563EB' font-family='system-ui, sans-serif'>÷ 3,6</text><path d='M330,124 Q220,196 110,124' fill='none' stroke='#EA580C' stroke-width='2.2' marker-end='url(#mkO)'/><text x='220' y='188' font-size='19' text-anchor='middle' fill='#EA580C' font-family='system-ui, sans-serif'>× 3,6</text></svg>
<p>Exemples&nbsp;: $90~\pu{km*h-1} = \dfrac{90}{3{,}6}~\pu{m*s-1} = 25~\pu{m*s-1}$, et $10~\pu{m*s-1} = 10 \times 3{,}6~\pu{km*h-1} = 36~\pu{km*h-1}$.</p>
<p class="nt-note">Pour ne pas se tromper de sens&nbsp;: penser au sprinter qui parcourt le 100&nbsp;m en 10&nbsp;s à peu près. Cela correspond à une vitesse moyenne de $\pu{10 m*s-1}$. On a alors le choix entre $10/3,6$ et $10\times 3,6$ pour la vitesse en km·h⁻¹&nbsp;; une vitesse de $\pu{36 km*h-1}$ semble la réponse évidente.</p>
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
<button type="button" class="nt-btn nt-btn-main" data-act="replay"><i class="fa-solid fa-rotate-right"></i>&nbsp; Revoir la construction</button>
<label class="nt-check"><input type="checkbox" data-p="v" checked> vecteurs vitesse</label>
<label class="nt-check"><input type="checkbox" data-p="dv" checked> construction de $\Delta\vec{v}_i$</label>
<label class="nt-check"><input type="checkbox" data-p="a" checked> $\vec{a}_i$</label>
<label class="nt-check"><input type="checkbox" data-p="ex"> vraie accélération</label>
</div>
<p class="nt-center nt-chrono-form">Point milieu&nbsp;: $\vec{v}_i \approx \dfrac{\overrightarrow{\mathrm{M}_{i-1}\mathrm{M}_{i+1}}}{2\tau}$, puis $\Delta\vec{v}_i = \vec{v}_{i+1}-\vec{v}_{i-1}$ et $\vec{a}_i \approx \dfrac{\Delta\vec{v}_i}{2\tau}$.</p>
<div class="nt-read" aria-live="polite"><span>écart avec la vraie accélération&nbsp;: <b class="out-err"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Les points sont séparés par une durée constante $\tau$. Pour construire $\Delta\vec{v}_i$, on reporte en $\mathrm{M}_i$ le vecteur $\vec{v}_{i+1}$, puis, à son extrémité, le vecteur $-\vec{v}_{i-1}$&nbsp;: $\Delta\vec{v}_i$ va de $\mathrm{M}_i$ à l'extrémité de $-\vec{v}_{i-1}$. Les échelles des vecteurs sont arbitraires&nbsp;; la vraie accélération (en pointillés gris) est calculée à partir de l'équation du mouvement.</p>
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
<p>Tracer les évolutions de la position $\color{#2A6BC4}x(t)$, de la vitesse $\color{#A16207}v(t)$ et de l'accélération $\color{#059669}a(t)$ pour un mouvement rectiligne uniforme, puis pour un mouvement rectiligne uniformément accéléré.</p>
</div>

<div class="nt-lab" id="lab-xva">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Position, vitesse et accélération d'un mouvement rectiligne</p>
<canvas style="height:540px;" aria-label="Mobile sur une piste rectiligne et graphes de x(t), v(t) et a(t)"></canvas>
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
<p>Avant d'aborder le virage des Combes (virage n°5) du circuit de Spa-Francorchamps, un pilote de F1 freine fortement pour passer sa vitesse de 327&nbsp;km·h⁻¹ à 176&nbsp;km·h⁻¹ en 1,48&nbsp;s.</p>
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
<li><p>La vitesse variant linéairement avec le temps, la distance parcourue est celle qu'on parcourrait à la vitesse moyenne $\dfrac{v_0+v_1}{2}$&nbsp;: $d = \dfrac{v_0+v_1}{2}\times\Delta t = \dfrac{90{,}8+48{,}9}{2}\times 1{,}48 = \pu{103 m}$.</p>
<p class="nt-note">On aurait aussi pu primitiver $v(t) = v_0 + a\times t$ pour obtenir $x(t)$.</p>
</li>
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
<li>$\color{#A16207}\vec{u}_T$&nbsp;: <b style="color:#A16207;">vecteur tangent</b>, tangent à la trajectoire, orienté dans le sens du mouvement&nbsp;;</li>
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

## Testez-vous {.nt-h2}

<div class="nt-lab nt-quizlab" id="quiz-final">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Testez-vous sur la description d'un mouvement</p>
<p class="nt-qnum"></p>
<div class="nt-prog" aria-hidden="true"></div>
<div class="nt-qcard">
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
</div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CP = '#2A6BC4', CV = '#F59E0B', CA = '#059669', CT = '#E11D48';   /* position, vitesse (texte : #A16207, plus foncé), accélération, trajectoire */
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
  function rr(c, x, y, w, h, r) {   /* rectangle à coins arrondis (repli si roundRect absent) */
    c.beginPath(); if (c.roundRect) { c.roundRect(x, y, w, h, r); } else { c.rect(x, y, w, h); }
  }
  function ind(n) { return String(n).replace(/[0-9]/g, function (d) { return '\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089'[+d]; }); }   /* indice en caractères souscrits : v₃, M₄… */
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
    /* grandeurs physiques (m, s) : vitesse du train, hauteur de lâcher au-dessus du plancher, rayon de la balle */
    var U = 2.0, H = 1.25, G = 9.81, RB = 0.09, FL = 0.45, LW = 4.4, XB = 2.05;   /* FL : hauteur du plancher ; LW : longueur du wagon ; XB : abscisse du lâcher dans le wagon */
    var TL = Math.sqrt(2 * (H - RB) / G), SLOW = 4, HOLD = 0.5, REST = 1.4, CYCLE = HOLD + TL * SLOW + REST;
    var C_SKY1 = '#DCEEFB', C_SKY2 = '#F5FAFE', C_GRASS = '#E4F0DF', C_TREE = '#B9DBB4', C_TREE2 = '#A3CF9F', C_TRUNK = '#C8B8A6', C_POLE = '#CBD5E1';
    var C_BODY = CP, C_WALL = '#F1F6FD', C_DARK = '#334155';
    function hash(i) { var s = Math.sin(i * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); }
    function draw() {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, yg = h - 40, narrow = w < 500;
      var travel = U * TL, sol = mode === 'sol';
      var k = Math.min(68, (yg - 74) / (FL + 2.4), (w - 28) / (LW + travel));   /* échelle (px/m) adaptée à la largeur */
      var tc = t % CYCLE, tp = Math.min(Math.max((tc - HOLD) / SLOW, 0), TL);   /* temps physique (ralenti), figé à l'arrivée */
      /* dans le référentiel terrestre le train avance ; dans celui du train, c'est le sol qui recule */
      var span = sol ? LW + travel : LW, ox = (w - span * k) / 2;
      var xTrain = sol ? U * tp : 0, shift = sol ? 0 : U * tp;
      function X(xm) { return ox + xm * k; }
      function Y(ym) { return yg - ym * k; }
      c.clearRect(0, 0, w, h);
      /* ciel et talus */
      var gs = c.createLinearGradient(0, 0, 0, yg); gs.addColorStop(0, C_SKY1); gs.addColorStop(1, C_SKY2);
      c.fillStyle = gs; c.fillRect(0, 0, w, yg);
      c.fillStyle = C_GRASS; c.fillRect(0, Y(0.32), w, yg - Y(0.32));
      /* décor lié au sol : arbres, buissons et poteaux (tous immobiles dans le référentiel terrestre) */
      var D = 1.15, x0m = (0 - ox) / k + shift, x1m = (w - ox) / k + shift;
      for (var i = Math.floor(x0m / D) - 2; i <= Math.ceil(x1m / D) + 2; i++) {
        var hh = hash(i), xs = X(i * D + hh * 0.5 - shift), base = Y(0.32);
        if (((i % 5) + 5) % 5 === 0) {   /* poteau de caténaire */
          c.fillStyle = C_POLE; c.fillRect(xs - 0.04 * k, Y(3.35), 0.08 * k, base - Y(3.35));
          c.fillRect(xs - 0.04 * k, Y(3.3), 0.75 * k, 0.05 * k);
        } else if (hh > 0.4) {             /* arbre */
          var th = 0.75 + 0.55 * hash(i + 50), rf = 0.38 + 0.18 * hash(i + 90);
          c.fillStyle = C_TRUNK; c.fillRect(xs - 0.045 * k, base - th * k, 0.09 * k, th * k);
          c.fillStyle = hh > 0.7 ? C_TREE2 : C_TREE;
          [[0, 0.6, 1], [-0.55, 0.15, 0.7], [0.55, 0.2, 0.72]].forEach(function (f) {   /* trois disques, chacun dans son propre chemin */
            c.beginPath(); c.arc(xs + f[0] * rf * k, base - (th + f[1] * rf) * k, f[2] * rf * k, 0, 2 * Math.PI); c.fill();
          });
        } else {                            /* buisson */
          c.fillStyle = C_TREE; c.beginPath(); c.ellipse(xs, base, 0.32 * k, 0.2 * k, 0, Math.PI, 2 * Math.PI); c.fill();
        }
      }
      /* voie : ballast, traverses, rail */
      var gb = c.createLinearGradient(0, yg, 0, h); gb.addColorStop(0, '#DAD6D2'); gb.addColorStop(1, '#ECEAE7');
      c.fillStyle = gb; c.fillRect(0, yg, w, h - yg);
      c.fillStyle = '#B5ACA3';
      for (var q = Math.floor(x0m / 0.55) - 1; q <= Math.ceil(x1m / 0.55) + 1; q++) {
        var xq = X(q * 0.55 - shift); rr(c, xq - 0.11 * k, yg + 3, 0.22 * k, 6, 2); c.fill();
      }
      c.fillStyle = '#64748B'; c.fillRect(0, yg, w, 4); c.fillStyle = 'rgba(255,255,255,.55)'; c.fillRect(0, yg, w, 1.2);
      /* wagon en coupe : paroi du fond percée de fenêtres (on voit le décor défiler à travers) */
      var wx = X(xTrain), wr = X(xTrain + LW), yF = Y(FL), yR = Y(FL + 2.4), post = 0.13 * k, roof = 0.24 * k;
      c.fillStyle = C_WALL; c.beginPath(); c.rect(wx, yR, wr - wx, yF - yR);
      for (var j = 0; j < 4; j++) {
        var wl = X(xTrain + 0.45 + j * 0.95), wy = Y(FL + 2.05);   /* bas des fenêtres à 1,05 m du plancher, nettement sous le bras tendu (1,25 m) */
        if (c.roundRect) { c.roundRect(wl, wy, 0.7 * k, 1.0 * k, 0.12 * k); } else { c.rect(wl, wy, 0.7 * k, 1.0 * k); }
      }
      c.fill('evenodd');
      c.strokeStyle = 'rgba(42,107,196,.25)'; c.lineWidth = 1.5;
      for (j = 0; j < 4; j++) { rr(c, X(xTrain + 0.45 + j * 0.95), Y(FL + 2.05), 0.7 * k, 1.0 * k, 0.12 * k); c.stroke(); }
      c.fillStyle = 'rgba(42,107,196,.07)'; c.fillRect(wx, Y(FL + 0.95), wr - wx, Y(FL) - Y(FL + 0.95));   /* soubassement de la paroi */
      /* le passager (bonhomme fil de fer), debout, bras tendu vers le point de lâcher */
      var px = xTrain + XB - 0.45, released = tp > 0, handX = X(xTrain + XB) - (RB + 0.03) * k, handY = Y(FL + H);
      c.strokeStyle = '#94A3B8'; c.lineWidth = Math.max(2.5, 0.045 * k); c.lineCap = 'round'; c.lineJoin = 'round';
      c.beginPath(); c.moveTo(X(px), Y(FL + 1.35)); c.lineTo(X(px), Y(FL + 0.75));   /* tronc */
      c.moveTo(X(px), Y(FL + 0.75)); c.lineTo(X(px - 0.15), Y(FL)); c.moveTo(X(px), Y(FL + 0.75)); c.lineTo(X(px + 0.15), Y(FL));   /* jambes */
      c.moveTo(X(px), Y(FL + 1.25)); c.lineTo(handX, handY);   /* bras tendu */
      c.moveTo(X(px), Y(FL + 1.25)); c.lineTo(X(px - 0.2), Y(FL + 0.85)); c.stroke();   /* autre bras */
      c.fillStyle = '#94A3B8'; c.beginPath(); c.arc(X(px), Y(FL + 1.52), 0.14 * k, 0, 2 * Math.PI); c.fill();   /* tête */
      /* trajectoire de la balle : chronophotographie (une position toutes les 0,04 s) + tracé continu */
      function bx(s) { return sol ? XB + U * s : XB; }
      function by(s) { return Math.max(FL + RB, FL + H - 0.5 * G * s * s); }
      if (released) {
        c.strokeStyle = 'rgba(225,29,72,.35)'; c.lineWidth = 1.6; c.setLineDash([]);
        c.beginPath(); for (var s2 = 0; s2 <= tp; s2 += 0.01) { var a = X(bx(s2)), b = Y(by(s2)); if (s2 === 0) { c.moveTo(a, b); } else { c.lineTo(a, b); } }
        c.lineTo(X(bx(tp)), Y(by(tp))); c.stroke();
        var n = 0; for (var s = 0; s <= tp + 1e-9; s += 0.04) { n++; }
        var m = 0;
        for (s = 0; s <= tp + 1e-9; s += 0.04) {
          m++; c.fillStyle = 'rgba(225,29,72,' + (0.25 + 0.45 * m / n) + ')';
          c.beginPath(); c.arc(X(bx(s)), Y(by(s)), Math.max(2.2, 0.035 * k), 0, 2 * Math.PI); c.fill();
        }
      }
      /* plancher, balle */
      c.fillStyle = '#CBD5E1'; c.fillRect(wx, yF - 0.06 * k, wr - wx, 0.06 * k);
      var bX = X(bx(tp)), bY = Y(by(tp)), rpx = RB * k;
      var gball = c.createRadialGradient(bX - rpx * 0.35, bY - rpx * 0.35, rpx * 0.1, bX, bY, rpx);
      gball.addColorStop(0, '#FB7185'); gball.addColorStop(1, '#BE123C');
      c.fillStyle = gball; c.beginPath(); c.arc(bX, bY, rpx, 0, 2 * Math.PI); c.fill();
      /* caisse du wagon : toit, montants, châssis */
      c.fillStyle = C_BODY;
      rr(c, wx - 0.04 * k, yR - roof, wr - wx + 0.08 * k, roof + 0.04 * k, [0.18 * k, 0.18 * k, 3, 3]); c.fill();
      c.fillStyle = '#458EEC'; c.fillRect(wx + 0.1 * k, yR - roof * 0.62, wr - wx - 0.2 * k, 2);
      c.fillStyle = C_BODY; c.fillRect(wx, yR, post, yF - yR); c.fillRect(wr - post, yR, post, yF - yR);
      c.fillStyle = C_DARK; rr(c, wx - 0.04 * k, yF, wr - wx + 0.08 * k, 0.16 * k, 3); c.fill();
      /* bogies et roues : elles tournent par rapport au wagon, quel que soit le référentiel */
      var rw = 0.2 * k, rot = U * tp / 0.2;
      [0.75, LW - 0.75].forEach(function (cb) {
        c.fillStyle = '#475569'; rr(c, X(xTrain + cb - 0.48), Y(0.3), 0.96 * k, 0.12 * k, 3); c.fill();
        [-0.26, 0.26].forEach(function (dx) {
          var cx0 = X(xTrain + cb + dx), cy0 = Y(0.2);
          c.fillStyle = C_DARK; c.beginPath(); c.arc(cx0, cy0, rw, 0, 2 * Math.PI); c.fill();
          c.fillStyle = '#CBD5E1'; c.beginPath(); c.arc(cx0, cy0, rw * 0.68, 0, 2 * Math.PI); c.fill();
          c.strokeStyle = '#64748B'; c.lineWidth = Math.max(1.2, 0.025 * k);
          for (var e = 0; e < 3; e++) { var an = rot + e * Math.PI / 3; c.beginPath(); c.moveTo(cx0 - Math.cos(an) * rw * 0.66, cy0 - Math.sin(an) * rw * 0.66); c.lineTo(cx0 + Math.cos(an) * rw * 0.66, cy0 + Math.sin(an) * rw * 0.66); c.stroke(); }
          c.fillStyle = C_DARK; c.beginPath(); c.arc(cx0, cy0, rw * 0.18, 0, 2 * Math.PI); c.fill();
        });
      });
      /* ce qui bouge dans le référentiel choisi : le train (vu du quai) ou le sol (vu du wagon) */
      var mid = (wx + wr) / 2, La = Math.min(0.9 * k, 60);
      if (sol) {
        var ya = yR - roof - 16;
        arrow(c, mid - La / 2, ya, mid + La / 2, ya, C_BODY, 2.6);
        vecLabel(c, 'v', mid + La / 2 + 12, ya + 5, C_BODY);
        txt(c, 'train', mid + La / 2 + 22, ya + 5, C_BODY, '600 12px system-ui, sans-serif', 'left', true);
      } else {
        var yb = yg + 26;
        arrow(c, mid + La / 2, yb, mid - La / 2, yb, col('--slate'), 2.6);
        txt(c, 'sol', mid - La / 2 - 10, yb + 5, col('--slate'), '600 12px system-ui, sans-serif', 'right');
        vecLabel(c, 'v', mid - La / 2 - 10 - c.measureText('sol').width - 9, yb + 5, col('--slate'), true);
      }
      /* étiquette du référentiel et chronomètre */
      var lab = sol ? (narrow ? 'Vu du quai' : 'Référentiel terrestre · vu depuis le quai') : (narrow ? 'Vu du wagon' : 'Référentiel du train · vu depuis le wagon');
      c.font = '700 12.5px system-ui, sans-serif'; var lw = c.measureText(lab).width;
      c.fillStyle = 'rgba(255,255,255,.92)'; c.strokeStyle = col('--line'); c.lineWidth = 1;
      rr(c, 10, 10, lw + 34, 26, 13); c.fill(); c.stroke();
      c.fillStyle = sol ? '#059669' : C_BODY; c.beginPath(); c.arc(24, 23, 4.5, 0, 2 * Math.PI); c.fill();
      txt(c, lab, 34, 27.5, col('--ink'), '700 12.5px system-ui, sans-serif', 'left');
      var ts = 't = ' + fr(tp, 2) + ' s';
      c.font = '600 12px ui-monospace, SFMono-Regular, Menlo, monospace'; var tw = c.measureText(ts).width;
      c.fillStyle = 'rgba(255,255,255,.92)'; rr(c, w - tw - 30, 10, tw + 20, 26, 13); c.fill(); c.stroke();
      txt(c, ts, w - 20, 27.5, col('--slate'), '600 12px ui-monospace, SFMono-Regular, Menlo, monospace', 'right');
      msg.textContent = sol ? 'Pour une personne sur le quai, la balle avance avec le train pendant sa chute : sa trajectoire est une portion de parabole.'
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
    if (RM) { t = HOLD + TL * SLOW; }
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
      var c = S.ctx, w = S.w, h = S.h, k = Math.min((w - 40) / 5.2, (h - 30) / 2.6), oy = h - 18;
      var ox = w / 2 - k * (Mx(0) + Mx(2.75)) / 2;   /* trajectoire centrée horizontalement dans le cadre */
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
      c.strokeStyle = 'rgba(245,158,11,.5)'; c.setLineDash([5, 5]); c.lineWidth = 1.5;
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
    var msg = $(root, '.nt-msg'), oE = $(root, '.out-err'), oF = $(root, '.nt-chrono-form'), bR = $(root, '[data-act="replay"]'), S, mode = 'para', meth = 'mil';
    var TAU = 0.08, prog = 4, anim = null, box = {}, cam = null;
    var MOV = {
      para: { n: 15, i0: 4, f: function (t) { return [0.3 + 3.2 * t, 0.3 + 4.6 * t - 4.905 * t * t]; }, kv: 0.2, ka: 0.05, m: 'Chute libre (lancer oblique) : le vecteur accélération est le même en tout point, vertical et vers le bas.' },
      circ: { n: 17, i0: 8, f: function (t) { var w = 2.6; return [2.1 + 1.0 * Math.cos(w * t - 2.6), 1.15 + 1.0 * Math.sin(w * t - 2.6)]; }, kv: 0.3, ka: 0.09, m: 'Mouvement circulaire uniforme : la vitesse garde la même norme, mais sa direction tourne ; le vecteur accélération pointe vers le centre du cercle.' },
      frein: { n: 14, i0: 5, f: function (t) { return [0.3 + 4.4 * t - 2.6 * t * t, 1.0]; }, kv: 0.12, ka: 0.08, m: 'Mouvement rectiligne freiné : les vecteurs vitesse raccourcissent ; le vecteur accélération est opposé au mouvement.' }
    };
    var FORM = {
      mil: 'Point milieu : $\\vec{v}_i \\approx \\dfrac{\\overrightarrow{\\mathrm{M}_{i-1}\\mathrm{M}_{i+1}}}{2\\tau}$, puis $\\Delta\\vec{v}_i = \\vec{v}_{i+1}-\\vec{v}_{i-1}$ et $\\vec{a}_i \\approx \\dfrac{\\Delta\\vec{v}_i}{2\\tau}$.',
      apr: 'Point d’après : $\\vec{v}_i \\approx \\dfrac{\\overrightarrow{\\mathrm{M}_{i}\\mathrm{M}_{i+1}}}{\\tau}$, puis $\\Delta\\vec{v}_i = \\vec{v}_{i+1}-\\vec{v}_{i}$ et $\\vec{a}_i \\approx \\dfrac{\\Delta\\vec{v}_i}{\\tau}$.'
    };
    var CVc = 'rgba(245,158,11,.85)';   /* copies reportées en M_i */
    function pts() { var m = MOV[mode], P = []; for (var i = 0; i < m.n; i++) { P.push(m.f(i * TAU)); } return P; }
    /* vecteurs utiles à la construction au point M_i, selon la méthode */
    function cons(P, i) {
      var r = {};
      if (meth === 'mil') {
        var vm = function (j) { return [(P[j + 1][0] - P[j - 1][0]) / (2 * TAU), (P[j + 1][1] - P[j - 1][1]) / (2 * TAU)]; };
        r.va = vm(i - 1); r.vb = vm(i + 1); r.Pa = P[i - 1]; r.Pb = P[i + 1]; r.ja = i - 1; r.jb = i + 1; r.div = 2 * TAU;
      } else {
        var vp = function (j) { return [(P[j + 1][0] - P[j][0]) / TAU, (P[j + 1][1] - P[j][1]) / TAU]; };
        r.va = vp(i); r.vb = vp(i + 1); r.Pa = P[i]; r.Pb = P[i + 1]; r.ja = i; r.jb = i + 1; r.div = TAU;
      }
      r.ax = (r.vb[0] - r.va[0]) / r.div; r.ay = (r.vb[1] - r.va[1]) / r.div;
      return r;
    }
    function trueAcc(i) {   /* dérivée seconde calculée avec un pas minuscule */
      var m = MOV[mode], hh = 1e-3, ti = i * TAU, fp = m.f(ti + hh), f0 = m.f(ti), fm = m.f(ti - hh);
      return [(fp[0] - 2 * f0[0] + fm[0]) / (hh * hh), (fp[1] - 2 * f0[1] + fm[1]) / (hh * hh)];
    }
    /* cadrage fixe pour un mouvement et une méthode : tous les points et toutes les constructions possibles restent visibles */
    function frame(P) {
      var key = mode + meth;
      if (box[key]) { return box[key]; }
      var m = MOV[mode], xs = [], ys = [];
      function add(p) { xs.push(p[0]); ys.push(p[1]); }
      P.forEach(add);
      for (var i = 2; i <= m.n - 3; i++) {
        var r = cons(P, i), Mi = P[i], ta = trueAcc(i);
        add([r.Pa[0] + r.va[0] * m.kv, r.Pa[1] + r.va[1] * m.kv]); add([r.Pb[0] + r.vb[0] * m.kv, r.Pb[1] + r.vb[1] * m.kv]);
        if (mode !== 'frein') {
          add([Mi[0] + r.vb[0] * m.kv, Mi[1] + r.vb[1] * m.kv]); add([Mi[0] + (r.vb[0] - r.va[0]) * m.kv, Mi[1] + (r.vb[1] - r.va[1]) * m.kv]);
          add([Mi[0] + r.ax * m.ka, Mi[1] + r.ay * m.ka]); add([Mi[0] + ta[0] * m.ka, Mi[1] + ta[1] * m.ka]);
        }
      }
      box[key] = [Math.min.apply(null, xs), Math.max.apply(null, xs), Math.min.apply(null, ys), Math.max.apply(null, ys)];
      return box[key];
    }
    function ease(u) { u = Math.max(0, Math.min(1, u)); return u * u * (3 - 2 * u); }
    function lerp(a, b, u) { return [a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u]; }
    function draw(smooth) {
      var P = pts(), m = MOV[mode], c = S.ctx, w = S.w, h = S.h, lin = mode === 'frein';
      rI.max = m.n - 3; if (+rI.value > m.n - 3) { rI.value = m.n - 3; } if (+rI.value < 2) { rI.value = 2; }
      var i = parseInt(rI.value, 10), r = cons(P, i), Mi = P[i], KV = m.kv, KA = m.ka, ta = trueAcc(i);
      /* échelle et centrage : cadrage resserré sur la construction en cours (points voisins de M_i et extrémités
         des vecteurs), qui glisse en douceur quand on change de point. Rectiligne : seule l'abscisse compte. */
      var pad = 40, tg;
      if (lin) {
        var lx = [];
        for (var jl = Math.max(0, i - 3); jl <= Math.min(P.length - 1, i + 3); jl++) { lx.push(P[jl][0]); }
        lx.push(r.Pa[0] + r.va[0] * KV, r.Pb[0] + r.vb[0] * KV, Mi[0] + r.vb[0] * KV, Mi[0] + (r.vb[0] - r.va[0]) * KV, Mi[0] + r.ax * KA, Mi[0] + ta[0] * KA);
        var lx0 = Math.min.apply(null, lx), lx1 = Math.max.apply(null, lx), kl = (w - 2 * pad - 30) / (lx1 - lx0);
        tg = { k: kl, ox: w / 2 - (lx0 + lx1) / 2 * kl, oy: h * 0.4 + 1.0 * kl };
      } else {
        var bx = [], by = [];
        var addB = function (q) { bx.push(q[0]); by.push(q[1]); };
        for (var jb = Math.max(0, i - 3); jb <= Math.min(P.length - 1, i + 3); jb++) { addB(P[jb]); }
        addB([r.Pa[0] + r.va[0] * KV, r.Pa[1] + r.va[1] * KV]); addB([r.Pb[0] + r.vb[0] * KV, r.Pb[1] + r.vb[1] * KV]);
        addB([Mi[0] + r.vb[0] * KV, Mi[1] + r.vb[1] * KV]); addB([Mi[0] + (r.vb[0] - r.va[0]) * KV, Mi[1] + (r.vb[1] - r.va[1]) * KV]);
        addB([Mi[0] + r.ax * KA, Mi[1] + r.ay * KA]); if (cbE.checked) { addB([Mi[0] + ta[0] * KA, Mi[1] + ta[1] * KA]); }
        if (mode === 'circ') { addB([2.0, 1.25]); }   /* le centre O (et son nom) reste visible */
        var x0 = Math.min.apply(null, bx), x1 = Math.max.apply(null, bx), y0 = Math.min.apply(null, by), y1 = Math.max.apply(null, by);
        var kk = Math.min((w - 2 * pad) / (x1 - x0), (h - 2 * pad) / (y1 - y0));
        tg = { k: kk, ox: w / 2 - (x0 + x1) / 2 * kk, oy: h / 2 + (y0 + y1) / 2 * kk };
      }
      if (!cam || !smooth) { cam = tg; }
      else { cam = { k: cam.k + (tg.k - cam.k) * 0.16, ox: cam.ox + (tg.ox - cam.ox) * 0.16, oy: cam.oy + (tg.oy - cam.oy) * 0.16 }; }
      var k = cam.k;
      function X(x) { return cam.ox + x * k; }
      function Y(y) { return cam.oy - y * k; }
      function S2(p) { return [X(p[0]), Y(p[1])]; }
      /* directions à l'écran : la normale « extérieure » est opposée à l'accélération */
      var aS = [r.ax, -r.ay], aN = Math.hypot(aS[0], aS[1]) || 1;
      function outN(d) {   /* normale unitaire à d, du côté opposé à l'accélération */
        var n = Math.hypot(d[0], d[1]) || 1, nx = -d[1] / n, ny = d[0] / n;
        if (nx * aS[0] + ny * aS[1] > 0) { nx = -nx; ny = -ny; }
        return [nx, ny];
      }
      var labels = [], obst = [];
      function seg(id, x1, y1, x2, y2) {   /* une flèche tracée devient un obstacle pour les étiquettes (sauf la sienne) */
        var n = Math.max(1, Math.ceil(Math.hypot(x2 - x1, y2 - y1) / 6));
        for (var q = 0; q <= n; q++) { obst.push({ x: x1 + (x2 - x1) * q / n, y: y1 + (y2 - y1) * q / n, w: 4, h: 4, id: 'seg' }); }
      }
      function vec(id, x1, y1, x2, y2, color, lw, dash) { arrow(c, x1, y1, x2, y2, color, lw, dash); seg(id, x1, y1, x2, y2); }
      var FV = 'italic 700 15px Georgia, serif', FM = 'italic 700 13px Georgia, serif';
      function boxW(s, font) { c.font = font; return c.measureText(s).width + 4; }
      /* étiquette au bout d'une flèche : positions candidates toutes collées à l'extrémité, la première libre est retenue */
      function tipLab(id, name, x1, y1, x2, y2, n, color, pr, neg) {
        var d = [x2 - x1, y2 - y1], dn = Math.hypot(d[0], d[1]) || 1; d = [d[0] / dn, d[1] / dn];
        var bw = boxW((neg ? '−' : '') + name, FV), bh = 22, r1 = bh / 2 + 5, r2 = bw / 2 + 6;
        var C = [[n[0] * r1 - d[0] * 2, n[1] * r1 - d[1] * 2], [d[0] * r2, d[1] * r2], [n[0] * r1 + d[0] * 8, n[1] * r1 + d[1] * 8],
                 [-n[0] * r1 - d[0] * 2, -n[1] * r1 - d[1] * 2], [n[0] * r1 - d[0] * 14, n[1] * r1 - d[1] * 14], [-n[0] * r1 + d[0] * 8, -n[1] * r1 + d[1] * 8]];
        C = C.concat(C.slice(0, 4).map(function (o) { return [o[0] * 1.5, o[1] * 1.5]; }));
        labels.push({ id: id, w: bw, h: bh, pr: pr, c: C.map(function (o) { return [x2 + o[0], y2 + o[1]]; }), f: function (x, y) { drawVec(name, x, y, color, neg); } });
      }
      /* étiquette au milieu d'une flèche (pour Δv) */
      function midLab(id, name, x1, y1, x2, y2, n, color, pr) {
        var mx = (x1 + x2) / 2, my = (y1 + y2) / 2, d = [x2 - x1, y2 - y1], dn = Math.hypot(d[0], d[1]) || 1; d = [d[0] / dn, d[1] / dn];
        var bw = boxW(name, FV), bh = 22, r1 = Math.abs(n[0]) * bw / 2 + Math.abs(n[1]) * bh / 2 + 6;
        var C = [[0, 0], [10, 0], [-10, 0], [0, 8]].map(function (o) { return [mx + n[0] * (r1 + o[1]) + d[0] * o[0], my + n[1] * (r1 + o[1]) + d[1] * o[0]]; });
        C = C.concat([[0, 0], [10, 0], [-10, 0]].map(function (o) { return [mx - n[0] * r1 + d[0] * o[0], my - n[1] * r1 + d[1] * o[0]]; }));
        labels.push({ id: id, w: bw, h: bh, pr: pr, c: C, f: function (x, y) { drawVec(name, x, y, color, false); } });
      }
      function drawVec(name, x, y, color, neg) {   /* nom de vecteur centré en (x, y) ; « − » éventuel hors de la flèche */
        if (!neg) { vecLabel(c, name, x, y + 6, color); return; }
        c.font = FV; var wm = c.measureText('−').width, wv = c.measureText(name).width, x0 = x - (wm + wv) / 2;
        txt(c, '−', x0 + wm / 2, y + 6, color, FV, 'center', true);
        vecLabel(c, name, x0 + wm + wv / 2, y + 6, color);
      }
      c.clearRect(0, 0, w, h);
      if (mode === 'circ') {   /* centre du cercle */
        var cx = X(2.1), cy = Y(1.15);
        c.strokeStyle = col('--slate'); c.lineWidth = 1.5; c.beginPath(); c.moveTo(cx - 6, cy); c.lineTo(cx + 6, cy); c.moveTo(cx, cy - 6); c.lineTo(cx, cy + 6); c.stroke();
        txt(c, 'O', cx - 12, cy - 9, col('--slate'), 'italic 700 14px Georgia, serif');
      }
      if (lin) { c.strokeStyle = '#E2E8F0'; c.lineWidth = 1.5; c.beginPath(); c.moveTo(pad / 2, Y(1)); c.lineTo(w - pad / 2, Y(1)); c.stroke(); }
      /* points de la chronophotographie ; ceux qui servent à la construction sont pleins */
      var jlo = meth === 'mil' ? i - 2 : i, jhi = i + 2;
      P.forEach(function (p, j) {
        var on = j >= jlo && j <= jhi, s = S2(p);
        if (j === i) { c.fillStyle = '#FFFFFF'; c.beginPath(); c.arc(s[0], s[1], 8, 0, 2 * Math.PI); c.fill(); }
        c.fillStyle = on ? CT : 'rgba(225,29,72,.32)';
        c.beginPath(); c.arc(s[0], s[1], j === i ? 5.5 : (on ? 4.2 : 3.6), 0, 2 * Math.PI); c.fill();
        obst.push({ x: s[0], y: s[1], w: 10, h: 10, id: 'p' + j });
      });
      /* noms des points M : on essaie des positions tout autour du point, en commençant par la préférée */
      var nameJ = meth === 'mil' ? [i - 1, i, i + 1] : [i, i + 1];
      nameJ.forEach(function (j) {
        var s = S2(P[j]), tg2 = [X(P[Math.min(j + 1, P.length - 1)][0]) - X(P[Math.max(j - 1, 0)][0]), Y(P[Math.min(j + 1, P.length - 1)][1]) - Y(P[Math.max(j - 1, 0)][1])], tn = Math.hypot(tg2[0], tg2[1]) || 1;
        var pref;
        if (lin) { pref = Math.PI / 2; }
        else {
          var no = outN(tg2), t1 = [tg2[0] / tn, tg2[1] / tn], v0;
          if (j === i) { v0 = [no[0] - t1[0] * 0.7, no[1] - t1[1] * 0.7]; }   /* M_i : côté extérieur, un peu en arrière */
          else { var sg = j < i ? -1 : 1; v0 = [-no[0] + sg * t1[0] * 0.6, -no[1] + sg * t1[1] * 0.6]; }   /* voisins : côté intérieur, écartés de a_i */
          pref = Math.atan2(v0[1], v0[0]);
        }
        var bw = boxW('M' + ind(j), FM), C = [];
        [0, 0.6, -0.6, 1.2, -1.2, 1.9, -1.9, Math.PI].forEach(function (da) { C.push([s[0] + Math.cos(pref + da) * 16, s[1] + Math.sin(pref + da) * 15]); });
        labels.push({ id: 'p' + j, w: bw, h: 15, pr: 4, c: C, f: function (x, y) { txt(c, 'M' + ind(j), x, y + 5, CT, FM, 'center', true); } });
      });
      /* vecteurs vitesse aux points */
      if (cbV.checked) {
        [[r.Pa, r.va, r.ja], [r.Pb, r.vb, r.jb]].forEach(function (q) {
          var a = S2(q[0]), b = S2([q[0][0] + q[1][0] * KV, q[0][1] + q[1][1] * KV]);
          vec('v' + q[2], a[0], a[1], b[0], b[1], CV, 2.8);
          tipLab('v' + q[2], 'v' + ind(q[2]), a[0], a[1], b[0], b[1], lin ? [0, -1] : outN([b[0] - a[0], b[1] - a[1]]), CV, 0);
        });
      }
      /* construction de Δv_i, qui part de M_i :
         1) on reporte v_{i+1} en M_i ; 2) à son extrémité, on reporte −v_{i−1} (le vecteur se retourne) ;
         3) Δv_i va de M_i à l'extrémité de −v_{i−1} ; 4) a_i, de même direction et de même sens que Δv_i */
      var u1 = ease(prog), u2 = ease(prog - 1), u3 = ease(prog - 2), u4 = cbD.checked ? ease(prog - 3) : 1;
      var Ms = S2(Mi), CDV = '#065F46';
      var vA = [r.va[0] * KV * k, -r.va[1] * KV * k], vB = [r.vb[0] * KV * k, -r.vb[1] * KV * k];   /* vecteurs vitesse à l'écran (px) */
      function rot(v, t) { var cs = Math.cos(t), sn = Math.sin(t); return [v[0] * cs - v[1] * sn, v[0] * sn + v[1] * cs]; }
      var aRow = lin ? Ms[1] - 30 : Ms[1], eRow = lin ? Ms[1] - 52 : Ms[1];
      var aEnd = [Ms[0] + r.ax * KA * k * u4, aRow - r.ay * KA * k * u4];
      /* a_i d'abord (il est plus long que Δv_i et sur la même droite : Δv_i est tracé par-dessus, plus fin et plus foncé) */
      if (cbE.checked) { vec('ex', Ms[0], eRow, Ms[0] + ta[0] * KA * k, eRow - ta[1] * KA * k, 'rgba(30,41,59,.5)', 2, [3, 3]); }
      if (lin && (cbA.checked || cbE.checked)) {
        c.strokeStyle = 'rgba(71,85,105,.35)'; c.lineWidth = 1; c.setLineDash([3, 3]);
        c.beginPath(); c.moveTo(Ms[0], Ms[1] - 9); c.lineTo(Ms[0], (cbE.checked ? eRow : aRow) - 4); c.stroke(); c.setLineDash([]);
      }
      if (cbA.checked && u4 > 0) {
        vec('a', Ms[0], aRow, aEnd[0], aEnd[1], CA, 3.8);
        if (u4 >= 1) { var ad = [aEnd[0] - Ms[0], aEnd[1] - aRow], an = Math.hypot(ad[0], ad[1]) || 1; tipLab('a', 'a' + ind(i), Ms[0], aRow, aEnd[0], aEnd[1], [-ad[1] / an, ad[0] / an], CA, 2); }
      }
      if (cbD.checked && prog > 0) {
        var rows = lin ? [Ms[1] + 44, Ms[1] + 66, Ms[1] + 90] : [Ms[1], Ms[1], Ms[1]];
        var pb = S2(r.Pb), pa = S2(r.Pa);
        /* 1) copie de v_{i+1} en M_i */
        var b0 = lerp(pb, [Ms[0], rows[0]], u1), b1 = [b0[0] + vB[0], b0[1] + vB[1]];
        vec('cb', b0[0], b0[1], b1[0], b1[1], CVc, 2.2, [6, 4]);
        var tipB = [Ms[0] + vB[0], rows[0] + vB[1]];
        if (lin) {
          c.strokeStyle = 'rgba(71,85,105,.35)'; c.lineWidth = 1; c.setLineDash([3, 3]);
          c.beginPath(); c.moveTo(Ms[0], Ms[1] + 9); c.lineTo(Ms[0], rows[2] + 6); c.stroke(); c.setLineDash([]);
        }
        /* 2) −v_{i−1} reporté à l'extrémité de la copie de v_{i+1} */
        if (prog > 1) {
          /* d'abord v_{i−1} glisse, à l'endroit, jusqu'à sa place finale ; puis il se retourne sur place (rotation autour de son milieu) */
          var startA = lin ? [tipB[0], rows[1]] : tipB, mid = [startA[0] - vA[0] / 2, startA[1] - vA[1] / 2];
          var ut = ease(2 * (prog - 1)), ur = ease(2 * (prog - 1.5));
          var va2 = lin ? [vA[0] * Math.cos(Math.PI * ur), 0] : rot(vA, Math.PI * ur);   /* sur une droite : il se replie puis s'allonge en sens inverse */
          var m0 = lerp([pa[0] + vA[0] / 2, pa[1] + vA[1] / 2], mid, ut);
          var a0 = [m0[0] - va2[0] / 2, m0[1] - va2[1] / 2], a1 = [m0[0] + va2[0] / 2, m0[1] + va2[1] / 2];
          vec('ca', a0[0], a0[1], a1[0], a1[1], CVc, 2.2, [6, 4]);
          if (lin) {
            c.strokeStyle = 'rgba(71,85,105,.35)'; c.lineWidth = 1; c.setLineDash([3, 3]);
            c.beginPath(); c.moveTo(tipB[0], rows[0]); c.lineTo(tipB[0], rows[1]); c.stroke(); c.setLineDash([]);
          }
          if (u2 >= 1) { tipLab('ca', 'v' + ind(r.ja), a0[0], a0[1], a1[0], a1[1], lin ? [0, 1] : outN([a1[0] - a0[0], a1[1] - a0[1]]), CV, 1, true); }
        }
        /* 3) Δv_i, de M_i à l'extrémité de −v_{i−1} */
        if (prog > 2) {
          var dv = [vB[0] - vA[0], vB[1] - vA[1]], d0 = [Ms[0], rows[2]], d1 = [d0[0] + dv[0] * u3, d0[1] + dv[1] * u3];
          if (lin) {
            c.strokeStyle = 'rgba(71,85,105,.35)'; c.lineWidth = 1; c.setLineDash([3, 3]);
            c.beginPath(); c.moveTo(Ms[0] + dv[0], rows[1]); c.lineTo(Ms[0] + dv[0], rows[2]); c.stroke(); c.setLineDash([]);
          }
          vec('dv', d0[0], d0[1], d1[0], d1[1], CDV, 2.4);
          if (u3 >= 1) {   /* nom de Δv : au milieu, du côté opposé au triangle de construction */
            var dd = [dv[0], dv[1]], dn2 = Math.hypot(dd[0], dd[1]) || 1, nn2 = [-dd[1] / dn2, dd[0] / dn2];
            if (nn2[0] * (tipB[0] - d0[0]) + nn2[1] * (tipB[1] - d0[1]) > 0) { nn2 = [-nn2[0], -nn2[1]]; }
            midLab('dv', 'Δv' + ind(i), d0[0], d0[1], d1[0], d1[1], lin ? [0, 1] : nn2, CDV, 1);
          }
        }
      }
      /* toutes les étiquettes en dernier, par-dessus les tracés : pour chacune, la première position candidate
         qui ne chevauche ni une étiquette déjà placée, ni un point, ni une autre flèche */
      var placed = [];
      function cost(L, x, y) {   /* nombre de chevauchements (une étiquette compte beaucoup plus qu'un bout de trait) */
        if (x - L.w / 2 < 2 || x + L.w / 2 > w - 2 || y - L.h / 2 < 2 || y + L.h / 2 > h - 2) { return 1e6; }
        function hit(q) { return q.id !== L.id && Math.abs(q.x - x) < (q.w + L.w) / 2 && Math.abs(q.y - y) < (q.h + L.h) / 2; }
        return placed.filter(hit).length * 50 + obst.filter(hit).length;
      }
      labels.sort(function (a, b) { return a.pr - b.pr; }).forEach(function (L) {
        var best = L.c[0], bc = Infinity;
        for (var q = 0; q < L.c.length; q++) { var cq = cost(L, L.c[q][0], L.c[q][1]); if (cq < bc) { bc = cq; best = L.c[q]; } if (cq === 0) { break; } }
        var bx2 = Math.max(L.w / 2 + 2, Math.min(w - L.w / 2 - 2, best[0])), by2 = Math.max(L.h / 2 + 2, Math.min(h - L.h / 2 - 2, best[1]));
        placed.push({ x: bx2, y: by2, w: L.w, h: L.h, id: L.id }); L.f(bx2, by2);
      });
      var ang = Math.abs(Math.atan2(r.ax * ta[1] - r.ay * ta[0], r.ax * ta[0] + r.ay * ta[1])) * 180 / Math.PI, nr = Math.hypot(r.ax, r.ay) / Math.hypot(ta[0], ta[1]) - 1;
      oE.textContent = fr(ang, 1) + '° en direction, ' + (Math.abs(nr) < 0.0005 ? '0' : fr(nr * 100, 1)) + ' % en norme';
      msg.textContent = m.m;
    }
    /* déroulé de la construction : 4 étapes d'environ 0,8 s */
    function replay() {
      if (RM) { prog = 4; draw(); return; }
      prog = 0; var t0 = null;
      if (anim) { cancelAnimationFrame(anim); }
      function stepC(ts) {
        if (t0 === null) { t0 = ts; }
        prog = Math.min(4, (ts - t0) / 800);
        draw(true);
        anim = prog < 4 ? requestAnimationFrame(stepC) : null;
      }
      anim = requestAnimationFrame(stepC);
    }
    function form() { oF.innerHTML = FORM[meth]; if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([oF]); } else if (window.renderMathInElement) { window.renderMathInElement(oF); } }
    rI.addEventListener('input', replay);
    [cbV, cbA, cbE].forEach(function (x) { x.addEventListener('change', draw); });
    cbD.addEventListener('change', replay);
    bR.addEventListener('click', replay);
    $$(root, 'input[name="mov"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; cam = null; rI.value = MOV[mode].i0; replay(); }); });
    $$(root, 'input[name="meth"]').forEach(function (x) { x.addEventListener('change', function () { meth = x.value; form(); replay(); }); });
    function setup() {
      cv.style.height = Math.round(Math.max(300, Math.min(430, cv.clientWidth * 0.62))) + 'px';   /* moins haut sur téléphone */
      S = canvasCtx(cv); draw();
    }
    var seen = false;
    watchVisible(cv, function (v) { if (v && !seen) { seen = true; replay(); } });   /* la construction se joue quand on arrive sur l'animation */
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
    var CPd = '#1E4E9C', CVd = '#A16207', CAd = '#047857';   /* versions foncées, pour le texte des pastilles */
    function nice(range, n) {   /* pas « rond » (1, 2, 2,5 ou 5 × 10ⁿ) donnant environ n intervalles */
      var r = range / Math.max(1, n), pw = Math.pow(10, Math.floor(Math.log(r) / Math.LN10)), m = r / pw;
      return (m <= 1 ? 1 : (m <= 2 ? 2 : (m <= 2.5 ? 2.5 : (m <= 5 ? 5 : 10)))) * pw;
    }
    function pill(c, s, x, y, fg, base) {   /* étiquette sur pastille teintée */
      c.font = '700 11.5px system-ui, sans-serif'; var tw = c.measureText(s).width;
      c.fillStyle = 'rgba(255,255,255,.92)'; rr(c, x, y, tw + 14, 19, 9.5); c.fill();
      c.globalAlpha = 0.14; c.fillStyle = base; rr(c, x, y, tw + 14, 19, 9.5); c.fill(); c.globalAlpha = 1;
      txt(c, s, x + 7, y + 13.5, fg, '700 11.5px system-ui, sans-serif', 'left');
    }
    function draw() {
      var q = p(), c = S.ctx, w = S.w, h = S.h, ts = t % (TM + 1.0), tt = Math.min(ts, TM);
      oX.textContent = fr(q.x0, 1) + ' m'; oV.textContent = fr(q.v0, 1) + ' m·s⁻¹'; oA.textContent = fr(q.a, 1) + ' m·s⁻²';
      c.clearRect(0, 0, w, h);
      /* ---- piste ---- */
      var trackY = 76, xs = [];
      for (var s0 = 0; s0 <= TM; s0 += 0.1) { xs.push(X(q, s0)); }
      var lo = Math.min.apply(null, xs), hi = Math.max.apply(null, xs), span = Math.max(10, hi - lo);
      var stp = span > 120 ? 25 : (span > 60 ? 10 : 5);   /* pas des graduations selon l'étendue */
      var XMIN = Math.floor(lo / stp) * stp - stp, XMAX = Math.ceil(hi / stp) * stp + stp;
      function PX(x) { return 30 + (x - XMIN) / (XMAX - XMIN) * (w - 60); }
      c.lineCap = 'round'; c.strokeStyle = '#CBD5E1'; c.lineWidth = 4;
      c.beginPath(); c.moveTo(PX(XMIN), trackY); c.lineTo(PX(XMAX), trackY); c.stroke();
      var sk = Math.max(1, Math.ceil(34 / Math.abs(PX(XMIN + stp) - PX(XMIN)))), ig = 0;   /* graduations écrites une sur deux (ou trois…) si la place manque */
      c.strokeStyle = '#94A3B8'; c.lineWidth = 1;
      for (var g = XMIN; g <= XMAX + 1e-9; g += stp, ig++) {
        c.beginPath(); c.moveTo(PX(g), trackY + 4); c.lineTo(PX(g), trackY + 9); c.stroke();
        if (ig % sk === 0) { txt(c, g + ' m', PX(g), trackY + 21, col('--muted'), '600 10px system-ui, sans-serif'); }
      }
      /* positions passées, toutes les 0,5 s : leur espacement montre la vitesse */
      for (var sp = 0; sp <= tt + 1e-9; sp += 0.5) {
        c.fillStyle = 'rgba(42,107,196,.30)'; c.beginPath(); c.arc(PX(X(q, sp)), trackY, 3.5, 0, 2 * Math.PI); c.fill();
      }
      /* le mobile : un petit chariot */
      var xc = Math.max(XMIN, Math.min(XMAX, X(q, tt))), cx = PX(xc);
      c.fillStyle = CP; rr(c, cx - 15, trackY - 21, 30, 13, 4); c.fill();
      c.fillStyle = 'rgba(255,255,255,.35)'; rr(c, cx - 10, trackY - 18.5, 20, 4, 2); c.fill();
      c.fillStyle = '#334155';
      [-8, 8].forEach(function (d) { c.beginPath(); c.arc(cx + d, trackY - 6, 4, 0, 2 * Math.PI); c.fill(); });
      /* vecteurs vitesse et accélération, portés par le mobile */
      var vv = V(q, tt), vmax = 0.1;
      for (var s1 = 0; s1 <= TM; s1 += 0.1) { vmax = Math.max(vmax, Math.abs(V(q, s1))); }   /* la plus grande vitesse atteinte donne une flèche de 60 px */
      function vecOn(val, len, y, color, colorTxt, name) {
        if (Math.abs(val) < 0.05 || Math.abs(len) < 8) { return; }   /* flèche trop courte : ni flèche ni étiquette */
        var x2 = cx + len, sg = len > 0 ? 1 : -1;
        arrow(c, cx, y, x2, y, color, 2.6);
        vecLabel(c, name, Math.max(12, Math.min(w - 12, x2 + sg * 12)), y + 5, colorTxt);
      }
      vecOn(vv, vv / vmax * 60, trackY - 32, CV, CV, 'v');
      vecOn(q.a, q.a / 4 * 45, trackY - 56, CA, CA, 'a');
      /* ---- trois graphes, chacun dans sa carte ---- */
      var G = [{ f: function (s) { return X(q, s); }, c: CP, d: CPd, n: 'x (m)' },
               { f: function (s) { return V(q, s); }, c: CV, d: CVd, n: 'v (m·s⁻¹)' },
               { f: function () { return q.a; }, c: CA, d: CAd, n: 'a (m·s⁻²)' }];
      var top = trackY + 34, gap = 10, ph = (h - top - 22 - 2 * gap) / 3, L = 48, R = w - 16;
      function GX(s) { return L + s / TM * (R - L); }
      G.forEach(function (gr, k) {
        var y0 = top + k * (ph + gap), T = y0 + 32, B = y0 + ph - 10, vals = [];   /* bande d'en-tête réservée à la pastille */
        for (var s = 0; s <= TM + 1e-9; s += 0.05) { vals.push(gr.f(s)); }
        var mn = Math.min(0, Math.min.apply(null, vals)), mx = Math.max(0, Math.max.apply(null, vals));
        if (mx - mn < 1e-9) { mn -= 1; mx += 1; }
        var st = nice(mx - mn, Math.max(2, Math.floor((B - T) / 26)));
        mn = Math.floor(mn / st + 1e-9) * st; mx = Math.ceil(mx / st - 1e-9) * st;
        function GY(v) { return B - (v - mn) / (mx - mn) * (B - T); }
        c.fillStyle = '#FFFFFF'; c.strokeStyle = col('--line'); c.lineWidth = 1; rr(c, 6.5, y0 + 0.5, w - 13, ph, 10); c.fill(); c.stroke();
        /* quadrillage fin (0,5 s ; demi-pas) puis principal (1 s ; pas) */
        c.lineWidth = 1;
        for (var gs = 0; gs <= TM + 1e-9; gs += 0.5) {
          c.strokeStyle = (Math.abs(gs - Math.round(gs)) < 1e-9) ? '#E2E8F0' : '#F1F5F9';
          c.beginPath(); c.moveTo(Math.round(GX(gs)) + 0.5, T); c.lineTo(Math.round(GX(gs)) + 0.5, B); c.stroke();
        }
        var nd = st >= 1 && Math.abs(st - Math.round(st)) < 1e-9 ? 0 : (st >= 0.1 ? 1 : 2);
        for (var gv = mn; gv <= mx + st / 4; gv += st / 2) {
          var major = Math.abs(gv / st - Math.round(gv / st)) < 1e-6, yy = Math.round(GY(gv)) + 0.5;
          c.strokeStyle = Math.abs(gv) < 1e-9 ? '#94A3B8' : (major ? '#E2E8F0' : '#F1F5F9');
          c.beginPath(); c.moveTo(L, yy); c.lineTo(R, yy); c.stroke();
          if (major) { txt(c, Math.abs(gv) < 1e-9 ? '0' : fr(gv, nd), L - 7, yy + 3.5, col('--slate'), '10px system-ui, sans-serif', 'right'); }
        }
        /* curseur de l'instant t */
        c.strokeStyle = 'rgba(30,41,59,.28)'; c.setLineDash([3, 3]);
        c.beginPath(); c.moveTo(GX(tt), T - 4); c.lineTo(GX(tt), B + 4); c.stroke(); c.setLineDash([]);
        /* courbe : en léger pour la suite, en plein jusqu'à l'instant t */
        function path(t1) {
          c.beginPath();
          for (var j = 0; j * 0.05 <= t1 + 1e-9; j++) { var px = GX(j * 0.05), py = GY(gr.f(j * 0.05)); if (j === 0) { c.moveTo(px, py); } else { c.lineTo(px, py); } }
          c.lineTo(GX(t1), GY(gr.f(t1)));
        }
        c.lineJoin = 'round'; c.strokeStyle = gr.c;
        c.globalAlpha = 0.25; c.lineWidth = 2; path(TM); c.stroke(); c.globalAlpha = 1;
        c.lineWidth = 2.8; path(tt); c.stroke();
        c.fillStyle = '#FFFFFF'; c.beginPath(); c.arc(GX(tt), GY(gr.f(tt)), 6.5, 0, 2 * Math.PI); c.fill();
        c.fillStyle = gr.c; c.beginPath(); c.arc(GX(tt), GY(gr.f(tt)), 4.5, 0, 2 * Math.PI); c.fill();
        pill(c, gr.n, 14, y0 + 7, gr.d, gr.c);
        if (k === 2) { for (var s2 = 0; s2 <= TM; s2++) { txt(c, s2 + ' s', GX(s2), y0 + ph + 15, col('--slate'), '10px system-ui, sans-serif'); } }
      });
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
      vecLabel(c, 'u\u209c', mx + uT[0] * U * 0.6 - uN[0] * 18, my + uT[1] * U * 0.6 - uN[1] * 18 + 6, col('--slate'));   /* vecteurs unitaires : notés avec leur flèche */
      vecLabel(c, 'u\u2099', mx + uN[0] * U * 0.6 - uT[0] * 18, my + uN[1] * U * 0.6 - uT[1] * 18 + 6, col('--slate'));
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

<script>
/* ================= Quiz de fin de chapitre (autonome) ================= */
(function () {
  var root = document.getElementById('quiz-final'); if (!root) { return; }
  var Q = [
    [
    "Le vecteur vitesse est…",
    [
    "la dérivée du vecteur position par rapport au temps",
    "la dérivée du vecteur accélération",
    "la primitive du vecteur position",
    "le produit de la position par le temps"
    ],
    "$\\vec{v} = \\dfrac{\\mathrm{d}\\overrightarrow{\\mathrm{OM}}}{\\mathrm{d}t}$."
    ],
    [
    "Le vecteur vitesse d'un point est toujours…",
    [
    "tangent à la trajectoire, dans le sens du mouvement",
    "perpendiculaire à la trajectoire",
    "dirigé vers le centre de la trajectoire",
    "nul dans un virage"
    ],
    "C'est une conséquence de sa définition comme dérivée de la position."
    ],
    [
    "Le vecteur accélération est…",
    [
    "la dérivée du vecteur vitesse par rapport au temps",
    "la dérivée du vecteur position",
    "la vitesse divisée par la durée totale",
    "toujours tangent à la trajectoire"
    ],
    "$\\vec{a} = \\dfrac{\\mathrm{d}\\vec{v}}{\\mathrm{d}t} = \\dfrac{\\mathrm{d}^2\\overrightarrow{\\mathrm{OM}}}{\\mathrm{d}t^2}$, en $\\pu{m*s-2}$."
    ],
    [
    "Dans un mouvement curviligne, le vecteur accélération est orienté…",
    [
    "vers l'intérieur de la courbe",
    "vers l'extérieur de la courbe",
    "selon la tangente uniquement",
    "dans le sens opposé à la vitesse"
    ],
    "Il a une composante normale dirigée vers l'intérieur du virage."
    ],
    [
    "Un mouvement rectiligne uniforme a…",
    [
    "un vecteur vitesse constant et une accélération nulle",
    "une accélération constante non nulle",
    "une vitesse qui augmente",
    "une trajectoire circulaire"
    ],
    "Vecteur vitesse constant&nbsp;: même direction, même sens, même norme."
    ],
    [
    "Un mouvement est rectiligne uniformément accéléré si…",
    [
    "la trajectoire est une droite et le vecteur accélération est constant",
    "la vitesse est constante",
    "l'accélération augmente",
    "la trajectoire est un cercle"
    ],
    "Exemple&nbsp;: la chute libre verticale."
    ],
    [
    "Dans un mouvement circulaire uniforme de rayon $R$, l'accélération vaut…",
    [
    "$a = \\dfrac{v^2}{R}$, dirigée vers le centre",
    "$a = 0$",
    "$a = v \\times R$, tangente",
    "$a = \\dfrac{v}{R^2}$"
    ],
    "Elle est centripète&nbsp;: dans le repère de Frenet, $a_t = 0$ et $a_n = \\dfrac{v^2}{R}$."
    ],
    [
    "Dans le repère de Frenet, la composante tangentielle de l'accélération vaut…",
    [
    "$a_t = \\dfrac{\\mathrm{d}v}{\\mathrm{d}t}$",
    "$a_t = \\dfrac{v^2}{R}$",
    "$a_t = v \\times R$",
    "$a_t = 0$ toujours"
    ],
    "Elle traduit la variation de la norme de la vitesse."
    ]
    ];   /* [question, [bonne réponse, autres réponses…], explication] */
  function $(s) { return root.querySelector(s); }
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function compose(el) { if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([el]).catch(function () {}); } }   /* formules des questions et des réponses */
  var qEl = $('.nt-ql-q'), bx = $('.nt-ql-btns'), msg = $('.nt-msg'), sc = $('.out-score'), next = $('[data-act="next"]'), prog = $('.nt-prog'), num = $('.nt-qnum');
  var lbl = '<i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante', order = [], k = 0, good = 0, answered = false, fini = false, res = [];
  function bilan(r) { return r === 1 ? 'Parfait&nbsp;: tout est juste&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;: relisez seulement les points manqués.' : (r >= 0.5 ? 'C\u2019est un début&nbsp;: reprenez les parties du cours correspondant aux erreurs.' : 'Relisez le cours, puis recommencez le quiz.')); }
  function progres() { prog.innerHTML = order.map(function (_, i) { return '<i class="' + (res[i] === true ? 'ok' : (res[i] === false ? 'ko' : '')) + (i === k && !fini ? ' cur' : '') + '"></i>'; }).join(''); num.textContent = fini ? 'Bilan' : 'Question ' + (k + 1) + ' sur ' + order.length; }
  function show() {
    answered = false; var q = Q[order[k]], idx = melange(q[1].map(function (_, i) { return i; }));
    qEl.innerHTML = q[0]; msg.textContent = ''; msg.className = 'nt-msg'; bx.innerHTML = '';
    idx.forEach(function (i) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn nt-choix'; b.innerHTML = q[1][i];
      b.addEventListener('click', function () {
        if (answered) { return; } answered = true; var ok = i === 0; res[k] = ok; if (ok) { good++; }
        b.classList.add(ok ? 'nt-choix-ok' : 'nt-choix-ko'); if (!ok) { bx.children[idx.indexOf(0)].classList.add('nt-choix-ok'); }
        msg.className = 'nt-msg nt-fb ' + (ok ? 'ok' : 'ko'); msg.innerHTML = (ok ? '<b>Bravo&nbsp;!</b> ' : '<b>Non.</b> ') + q[2]; compose(msg);
        sc.textContent = good + ' / ' + (k + 1); progres();
      });
      bx.appendChild(b);
    });
    compose(qEl); compose(bx);
    next.innerHTML = k === order.length - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lbl; progres();
  }
  function start() { order = melange(Q.map(function (_, i) { return i; })); k = 0; good = 0; fini = false; res = []; bx.hidden = false; sc.textContent = '0 / 0'; show(); }
  next.addEventListener('click', function () {
    if (fini) { start(); return; }
    if (!answered) { msg.className = 'nt-msg'; msg.textContent = 'Choisissez d\u2019abord une réponse.'; return; }
    k++;
    if (k >= order.length) { fini = true; bx.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + order.length + '</span> ' + bilan(good / order.length); msg.textContent = ''; msg.className = 'nt-msg'; next.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; progres(); return; }
    show();
  });
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', start); } else { start(); }
})();
</script>
