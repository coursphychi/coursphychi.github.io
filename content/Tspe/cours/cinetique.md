+++
title = "Cinétique chimique"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<p class="nt-lead">Une transformation chimique peut se dérouler plus ou moins vite&nbsp;: c'est l'objet de la <b>cinétique chimique</b>.</p>

## Transformation lente ou rapide {.nt-h2}

<p class="nt-lead">Pour étudier la cinétique d'une transformation, on utilise un capteur de suivi temporel de l'évolution d'un système (pH-mètre, conductimètre, spectrophotomètre…).</p>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Ce capteur peut être simplement l'œil&nbsp;!</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Si le temps de réponse du capteur est trop grand ou si les manipulations à réaliser avant le début des mesures empêchent la mise en œuvre du suivi cinétique, la transformation est dite <span class="imp nt-hole">rapide</span>. Sinon, elle est dite <span class="imp nt-hole">lente</span>.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Une réaction spectaculairement lente</span></summary>
<div class="nt-d-body">
<p><a href="https://www.youtube.com/watch?v=-OqPbuo1S_s" target="_blank" rel="noopener">La réaction de l'horloge à iode (réaction de Landolt)</a>.</p>
</div>
</details>

## Vitesse volumique d'apparition {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Dans un réacteur de volume constant, la <span class="imp">vitesse volumique d'apparition</span> (ou de <span class="imp">formation</span>) d'une espèce <b>à une date $t$</b> est égale à la valeur de la <span class="imp nt-hole">dérivée temporelle de sa concentration</span> en quantité de matière <b>à cette date</b>.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Exemple&nbsp;: vitesse d'apparition du diiode</p>
<p class="nt-f-math">$$v_{a,\ce{I2}}(t)=\frac{\mathrm{d}\left[\ce{I2}\right](t)}{\mathrm{d}t}$$</p>
<div class="nt-f-units"><span>$v$ en <span class="nt-hole">$\pu{mol*L-1*s-1}$</span></span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Si l'espèce est <b>produite</b> au cours de la transformation, sa concentration augmente et donc sa vitesse d'apparition est <span class="imp nt-hole">positive</span>.</p>
<p>Si l'espèce est <b>consommée</b> (réactif), sa vitesse d'apparition est <span class="imp nt-hole">négative</span>.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode graphique</p>
<p>Graphiquement, la valeur de la vitesse d'apparition <b>à un instant $t$</b> est donnée par la valeur de la <span class="imp nt-hole">pente de la tangente</span> à la courbe représentant l'évolution de la concentration <b>à cette date</b>.</p>
<ol class="nt-steps">
<li><p>Tracer la tangente à la courbe au point d'abscisse $t$.</p></li>
<li><p>Choisir deux points éloignés <b>sur la tangente</b> (pas sur la courbe&nbsp;!) et lire leurs coordonnées.</p></li>
<li><p>Calculer la pente $\dfrac{\Delta C}{\Delta t}$, en n'oubliant pas les puissances de 10 et les unités des axes.</p></li>
</ol>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Questions</p>
<p>Que vaut la vitesse de formation du diiode à $t = 2$&nbsp;min&nbsp;? Et à $t = 3$&nbsp;min&nbsp;? Et la vitesse d'apparition initiale ($t = 0$&nbsp;s)&nbsp;? Utilisez l'animation pour vérifier vos lectures graphiques.</p>
</div>

<div class="nt-lab" id="lab-tangente">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">La vitesse volumique, pente de la tangente</p>
<canvas style="height:320px;" aria-label="Évolution d'une concentration au cours du temps, avec la tangente à la date choisie et son triangle de pente"></canvas>
<label class="nt-ctrl">Date $t$&nbsp;: <b class="out-t"></b><input type="range" min="0" max="280" step="5" value="120"></label>
<div class="nt-btns">
<button type="button" class="nt-btn" data-t="0">$t = 0$</button>
<button type="button" class="nt-btn" data-t="30">$t = 30$ s</button>
<button type="button" class="nt-btn" data-t="120">$t = 2$ min</button>
<button type="button" class="nt-btn" data-t="180">$t = 3$ min</button>
</div>
<div class="nt-ctrl">Espèce suivie&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="tg" value="app" checked><span>produit (apparition du diiode)</span></label>
<label><input type="radio" name="tg" value="dis"><span>réactif (disparition de H<sub>2</sub>O<sub>2</sub>)</span></label>
</div>
</div>
<div class="nt-read" aria-live="polite"><span>vitesse = <b class="out-v"></b></span></div>
<p class="nt-center nt-note out-formule"></p>
<p class="nt-msg" aria-live="polite"></p>
</div>

## Vitesse volumique de disparition {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">vitesse volumique de disparition</span> d'une espèce est l'<span class="imp nt-hole">opposé</span> de sa vitesse volumique d'apparition&nbsp;:</p>
<p class="nt-center">$v_{d,\mathrm{X}}(t) = -v_{a,\mathrm{X}}(t)$</p>
<p>Dans un réacteur de volume constant, la vitesse volumique de disparition d'une espèce à une date $t$ est donc égale à l'<span class="imp nt-hole">opposé de la dérivée temporelle de sa concentration</span> en quantité de matière à cette date.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Exemple&nbsp;: vitesse de disparition du peroxyde d'hydrogène</p>
<p class="nt-f-math">$$v_{d,\ce{H2O2}}(t)=-\frac{\mathrm{d}\left[\ce{H2O2}\right](t)}{\mathrm{d}t}$$</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Et graphiquement&nbsp;? Que vaut la vitesse de disparition du réactif à $t = \pu{30 s}$&nbsp;? Choisissez «&nbsp;réactif&nbsp;» dans l'animation ci-dessus.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Les vitesses volumiques présentent l'avantage de ne pas dépendre du volume du système.</p>
</div>

## Loi de vitesse et facteurs cinétiques {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp nt-hole">loi de vitesse</span> est l'expression de la vitesse volumique d'apparition ou de disparition d'une espèce en fonction des différents paramètres qui la modifient.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Les <span class="imp nt-hole">facteurs cinétiques</span> sont les grandeurs qui apparaissent dans la loi de vitesse (<span class="imp nt-hole">température</span>, <span class="imp nt-hole">concentration</span>).</p>
<p>Ce sont donc les paramètres qui influent sur la durée d'une transformation.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>La loi de vitesse de disparition de l'ester éthanoate d'éthyle par hydrolyse basique est de la forme&nbsp;:</p>
<p class="nt-center">$v=k(T)\,\ce{[ester]}\,\ce{[HO-]}$</p>
<p>où $k(T)$, appelée <span class="imp nt-hole">constante de vitesse</span>, rend compte de l'influence de la température sur cette réaction.</p>
</div>

### Loi de vitesse d'ordre 1 {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une réaction est dite d'<span class="imp nt-hole">ordre 1</span> si sa loi de vitesse de disparition d'une espèce se met sous la forme&nbsp;:</p>
<p class="nt-center">$v_d=k(T)\,\ce{[A]}$</p>
<p>où $\ce{A}$ représente un réactif de la réaction.</p>
</div>

<p class="nt-lead">Comme $v_d=-\dfrac{\mathrm{d}\ce{[A]}}{\mathrm{d} t}$, on a $-\dfrac{\mathrm{d}\ce{[A]}}{\mathrm{d} t} = k\ce{[A]}$, soit&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Équation différentielle</p>
<p class="nt-f-math">$$\frac{\mathrm{d}\ce{[A]}}{\mathrm{d} t} + k\ce{[A]} = 0$$</p>
<div class="nt-f-units"><span>une <b>équation différentielle du premier ordre</b> (à coefficients constants)</span></div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une <span class="imp nt-hole">équation différentielle</span> est une équation où les inconnues sont des fonctions et qui lie une fonction et ses dérivées.</p>
<p>Une équation différentielle du premier ordre fait intervenir une fonction et sa dérivée première.</p>
</div>

<details class="nt-d nt-plus" id="memo-exp">
<summary><span class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Mémo maths</span><span class="nt-sum">Exponentielle et logarithme népérien</span></summary>
<div class="nt-d-body">
<p>$\mathrm{e}^x = \exp(x)$ est la <b>fonction exponentielle</b>. Elle a une propriété remarquable&nbsp;: elle est égale à sa propre dérivée, $\left(\mathrm{e}^{x}\right)' = \mathrm{e}^{x}$. Plus généralement, pour une constante $a$&nbsp;: $\left(\mathrm{e}^{at}\right)' = a\,\mathrm{e}^{at}$.</p>
<p>Sa fonction réciproque est le <b>logarithme népérien</b> (logarithme de base $\mathrm{e}$), noté $\ln$&nbsp;: $\ln\left(\mathrm{e}^x\right)=x$ et $\mathrm{e}^{\ln x} = x$.</p>
<ul class="nt-facts">
<li>$\mathrm{e}^0 = 1$ et $\ln(1) = 0$&nbsp;;</li>
<li>$\ln(a\times b) = \ln a + \ln b$, donc $\ln\left(C\,\mathrm{e}^{-kt}\right) = \ln C - kt$&nbsp;;</li>
<li>$\ln(2) \approx 0{,}69$&nbsp;;</li>
<li>à la calculatrice&nbsp;: touches <kbd>e<sup>x</sup></kbd> et <kbd>ln</kbd> (à ne pas confondre avec <kbd>10<sup>x</sup></kbd> et <kbd>log</kbd>).</li>
</ul>
</div>
</details>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Solution de l'équation différentielle</p>
<p class="nt-f-math">$$\ce{[A]}(t)= C\times\mathrm{e}^{-kt}$$</p>
<div class="nt-f-units"><span>où $C$ est une constante</span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Vérification</p>
<p>On dérive la solution proposée&nbsp;: $\dfrac{\mathrm{d}\ce{[A]}}{\mathrm{d} t} = C\times(-k)\,\mathrm{e}^{-kt} = -k\ce{[A]}$. On a donc bien $\dfrac{\mathrm{d}\ce{[A]}}{\mathrm{d} t} + k\ce{[A]} = 0$.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-flag"></i>Conditions initiales</p>
<p>On détermine $C$ grâce aux <span class="imp nt-hole">conditions initiales</span>&nbsp;: $\ce{[A]}(t=0)=C\times\mathrm{e}^{-k\times 0} = C = \ce{[A]}_0$. D'où&nbsp;:</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Évolution de la concentration (ordre 1)</p>
<p class="nt-f-math">$$\ce{[A]}(t)= \ce{[A]}_0\times\mathrm{e}^{-kt}$$</p>
</div>

<p class="nt-lead">L'évolution de la concentration dépend donc de la <b>concentration initiale</b> $\ce{[A]}_0$ et de la <b>température</b> (via la constante de vitesse $k(T)$).</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>En prenant le logarithme de $\ce{[A]}(t)$, on peut vérifier que cette loi est d'ordre 1&nbsp;:</p>
<p class="nt-center">$\ln\left(\ce{[A]}(t)\right) = \ln(\ce{[A]}_0) -k\times t$</p>
<p>On obtient une fonction affine décroissante du temps, de pente $-k$. Donc <span class="imp nt-hole">si $\ln\left(\ce{[A]}(t)\right)$ est modélisable par une fonction affine, la loi de vitesse est d'ordre 1</span>&nbsp;!</p>
</div>

<div class="nt-lab" id="lab-ordre1">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Reconnaître une loi d'ordre 1</p>
<div class="nt-lab-pair">
<figure><canvas class="c1" style="height:260px; background:#fff;" aria-label="Concentration du réactif en fonction du temps"></canvas><figcaption>$\ce{[A]}(t)$&nbsp;: une exponentielle décroissante</figcaption></figure>
<figure><canvas class="c2" style="height:260px; background:#fff;" aria-label="Logarithme de la concentration en fonction du temps"></canvas><figcaption>$\ln\left(\ce{[A]}(t)\right)$&nbsp;: une droite de pente $-k$</figcaption></figure>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">Concentration initiale $\ce{[A]}_0$&nbsp;: <b class="out-a0"></b><input type="range" data-p="a0" min="1" max="5" step="0.1" value="4"></label>
<label class="nt-ctrl">Constante de vitesse $k$&nbsp;: <b class="out-k"></b><input type="range" data-p="k" min="2" max="25" step="0.5" value="10"></label>
</div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-p="fit" checked> modélisation affine de ln([A])</label></div>
<div class="nt-read" aria-live="polite"><span>pente de la droite&nbsp;: <b class="out-pente"></b></span><span>$t_{1/2}$ = <b class="out-th"></b></span></div>
<p class="nt-note">Les points représentent des mesures (avec un léger bruit). Changez $\ce{[A]}_0$&nbsp;: la droite se décale, mais sa pente, et le temps de demi-réaction, ne changent pas.</p>
</div>

## Catalyse et catalyseur {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un <span class="imp nt-hole">catalyseur</span> est une espèce qui augmente la vitesse d'une réaction sans en modifier le bilan ou les caractéristiques thermodynamiques.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Étant à la fois réactif et produit, <span class="imp nt-hole">il n'apparaît pas dans l'équation de la réaction</span> qui modélise la transformation.</p>
<p>Selon les états physiques du catalyseur et du milieu réactionnel, la catalyse est qualifiée d'<span class="imp nt-hole">homogène</span> (même phase) ou d'<span class="imp nt-hole">hétérogène</span> (phases différentes).</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li>Le platine (solide) catalyse la dismutation du peroxyde d'hydrogène (en solution)&nbsp;: catalyse hétérogène.</li>
<li>Les enzymes sont des catalyseurs biologiques particulièrement efficaces&nbsp;: catalyse homogène.</li>
</ul>
</div>

## Temps de demi-réaction {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp">temps de demi-réaction</span> $t_{1/2}$ est la durée au bout de laquelle l'<span class="imp nt-hole">avancement a atteint la moitié de sa valeur finale</span>.</p>
</div>

<div class="nt-lab" id="lab-tdemi">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Lire le temps de demi-réaction</p>
<canvas style="height:300px;" aria-label="Évolution de l'avancement, d'une concentration de réactif ou de produit, avec la construction du temps de demi-réaction"></canvas>
<div class="nt-ctrl">Grandeur suivie&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="td" value="x" checked><span>avancement</span></label>
<label><input type="radio" name="td" value="r"><span>réactif limitant R</span></label>
<label><input type="radio" name="td" value="p"><span>produit P</span></label>
</div>
</div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-p="constr" checked> construction de $t_{1/2}$</label></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Si $\ce{R}$ est le <b>réactif limitant</b> d'une transformation totale, $t_{1/2}$ est la durée au bout de laquelle sa concentration initiale est <span class="imp nt-hole">divisée par deux</span>.</p>
<p>Pour un <b>produit</b> de concentration initiale nulle, $t_{1/2}$ est la durée au bout de laquelle sa concentration atteint la <span class="imp nt-hole">moitié de sa valeur finale</span> $\ce{[P]}_f$.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Pourquoi&nbsp;?</p>
<p>Si $\ce{R}$ est entièrement consommé à l'avancement final, alors il est à moitié consommé à la moitié de l'avancement final (quelle que soit sa stœchiométrie dans la réaction). Et sa concentration est donc bien divisée par deux.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<ul class="nt-facts">
<li>Le temps de demi-réaction <b>ne correspond pas à la moitié de la durée de réaction</b>&nbsp;!</li>
<li>Il permet d'évaluer la durée de la transformation chimique (quelques $t_{1/2}$) et donc de comparer entre elles la rapidité des transformations.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Le temps de demi-réaction d'une loi d'ordre 1</span></summary>
<div class="nt-d-body">
<p>Pour une loi d'ordre 1, $\ce{[A]}(t_{1/2}) = \dfrac{\ce{[A]}_0}{2}$ s'écrit $\ce{[A]}_0\,\mathrm{e}^{-kt_{1/2}} = \dfrac{\ce{[A]}_0}{2}$, soit $\mathrm{e}^{-kt_{1/2}} = \dfrac12$, et donc&nbsp;:</p>
<p class="nt-center">$t_{1/2} = \dfrac{\ln 2}{k}$</p>
<p>Le temps de demi-réaction ne dépend pas de la concentration initiale&nbsp;: c'est une signature de l'ordre 1. On retrouve la même loi pour la désintégration des noyaux radioactifs, dont la «&nbsp;demi-vie&nbsp;» est justement un temps de demi-réaction.</p>
</div>
</details>

## Modélisation microscopique {.nt-h2}

### Mécanisme réactionnel {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On modélise une transformation chimique <b>à l'échelle microscopique</b> par un <span class="imp nt-hole">mécanisme réactionnel</span> qui propose un ensemble d'<span class="imp nt-hole">actes élémentaires</span> a priori réalisés lors de la conversion des entités des réactifs en entités des produits, passant éventuellement par une ou plusieurs entités d'<span class="imp nt-hole">intermédiaires réactionnels</span>.</p>
<p>Le mécanisme doit être cohérent avec la stœchiométrie de la réaction, la loi de vitesse et toute autre donnée expérimentale obtenue à l'échelle macroscopique.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Acte élémentaire</p>
<p>L'<span class="imp">acte élémentaire</span> (ou étape élémentaire) correspond à un modèle, au niveau moléculaire, de conversion d'entités se déroulant en <span class="imp nt-hole">une seule étape</span>.</p>
</div>
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Intermédiaire réactionnel</p>
<p>Un <span class="imp">intermédiaire réactionnel</span> est une entité intervenant dans un mécanisme réactionnel, formée directement ou indirectement à partir des réactifs, et convertie directement ou indirectement en produits de la réaction.</p>
<p>En d'autres mots, il est <span class="imp nt-hole">formé, puis utilisé</span>.</p>
</div>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Le mécanisme réactionnel de la réaction $\ce{(H3C)3C-Cl + HO- -> (H3C)3C-OH + Cl^-}$ se décompose en deux actes élémentaires&nbsp;:</p>
<ol class="nt-steps">
<li><p>$\ce{(H3C)3C-Cl} \;\rightleftarrows\; {\color{#2A6BC4}\ce{(H3C)3C^+}} \;+\; \ce{Cl^-}$</p></li>
<li><p>${\color{#2A6BC4}\ce{(H3C)3C^+}} \;+\; \ce{HO^-} \;\rightleftarrows\; \ce{(H3C)3C-OH}$</p></li>
</ol>
<p>Le carbocation ${\color{#2A6BC4}\ce{(H3C)3C^+}}$ est ici un <b style="color:#2A6BC4;">intermédiaire réactionnel</b>&nbsp;: formé dans l'acte 1, il est consommé dans l'acte 2.</p>
</div>

### Le formalisme de la flèche courbe {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Le formalisme de la flèche courbe</p>
<p>On représente les modifications des structures électroniques des entités au cours d'un acte élémentaire à l'aide du <span class="imp nt-hole">formalisme de la flèche courbe</span>&nbsp;: une flèche courbe symbolise le mouvement d'un <span class="imp nt-hole">doublet d'électrons</span> d'un <b style="color:#2A6BC4;">site donneur</b> vers un <b style="color:#E11D48;">site accepteur</b>.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-def" style="margin:0; --c:#2A6BC4;">
<p class="nt-tag"><i class="fa-solid fa-arrow-right-from-bracket"></i>Site donneur</p>
<ul class="nt-facts">
<li>un doublet non liant&nbsp;;</li>
<li>un doublet liant (d'une liaison multiple ou simple)&nbsp;;</li>
<li>un atome portant une charge négative ou fortement polarisé négativement.</li>
</ul>
</div>
<div class="nt-b nt-warn" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-arrow-right-to-bracket"></i>Site accepteur</p>
<ul class="nt-facts">
<li>un atome possédant une lacune électronique&nbsp;;</li>
<li>un atome portant une charge positive ou polarisé positivement.</li>
</ul>
</div>
</div>

<p class="nt-lead">Pour représenter ces mouvements de doublets, il faut partir des schémas de Lewis des entités. Prenons l'exemple du 2<sup>e</sup> acte élémentaire de l'exemple précédent&nbsp;:</p>

<svg class="nt-svg" viewBox="0 0 800 240" role="img" aria-label="Acte élémentaire : un doublet non liant de l'ion hydroxyde (site donneur) comble la lacune du carbocation (site accepteur)"><text x="150" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="150" y="58" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="150" y="193" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="62" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan>C</text><line x1="150.0" y1="100.0" x2="150.0" y2="68.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="150.0" y1="130.0" x2="150.0" y2="165.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="92.0" y1="115.0" x2="135.0" y2="115.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><rect x="168" y="105" width="12" height="20" rx="2" fill="none" stroke="var(--rose)" stroke-width="2.2"/><circle cx="186" cy="90" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="181.5" y1="90" x2="190.5" y2="90" stroke="var(--ink)" stroke-width="1.6"/><line x1="186" y1="85.5" x2="186" y2="94.5" stroke="var(--ink)" stroke-width="1.6"/><text x="225" y="123" font-size="22" text-anchor="middle" fill="var(--slate)">+</text><text x="295" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><line x1="287.0" y1="99.0" x2="303.0" y2="99.0" stroke="var(--blue)" stroke-width="2.4" stroke-linecap="round"/><line x1="303.0" y1="131.0" x2="287.0" y2="131.0" stroke="var(--blue)" stroke-width="2.4" stroke-linecap="round"/><line x1="279.0" y1="123.0" x2="279.0" y2="107.0" stroke="var(--blue)" stroke-width="2.4" stroke-linecap="round"/><circle cx="316" cy="92" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="311.5" y1="92" x2="320.5" y2="92" stroke="var(--ink)" stroke-width="1.6"/><line x1="310.0" y1="115.0" x2="338.0" y2="115.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="360" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><path d="M276,116 Q234.5,162.1 188.5,133.1" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="182,129 194.2,130.2 188.4,139.5" fill="#C026D3"/><text x="445" y="123" font-size="26" text-anchor="middle" fill="var(--slate)">⇄</text><text x="610" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="610" y="58" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="610" y="193" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="522" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan>C</text><line x1="610.0" y1="100.0" x2="610.0" y2="68.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="610.0" y1="130.0" x2="610.0" y2="165.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="552.0" y1="115.0" x2="595.0" y2="115.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="625.0" y1="115.0" x2="665.0" y2="115.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="680" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><line x1="672.0" y1="99.0" x2="688.0" y2="99.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="688.0" y1="131.0" x2="672.0" y2="131.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="695.0" y1="115.0" x2="723.0" y2="115.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="745" y="123" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="100" y="232" font-size="12.5" text-anchor="middle" fill="var(--rose)" font-weight="700">site accepteur (lacune)</text><text x="335" y="232" font-size="12.5" text-anchor="middle" fill="var(--blue)" font-weight="700">site donneur (doublet non liant)</text></svg>

<p class="nt-cap">Un doublet non liant de l'oxygène de l'ion hydroxyde (site donneur) vient combler la lacune électronique du carbone (site accepteur)&nbsp;: il devient le doublet liant de la nouvelle liaison C–O, et les charges disparaissent.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode&nbsp;: tracer une flèche courbe</p>
<ol class="nt-steps">
<li><p>Écrire les <b>schémas de Lewis complets</b> des entités qui réagissent&nbsp;: doublets non liants, charges, lacunes.</p></li>
<li><p>Repérer le <b style="color:#2A6BC4;">site donneur</b> (un doublet, non liant ou liant, riche en électrons) et le <b style="color:#E11D48;">site accepteur</b> (lacune, charge positive, atome polarisé δ+).</p></li>
<li><p>Tracer la flèche <b>en partant du doublet</b> (du trait d'un doublet non liant, ou du milieu d'une liaison) et en pointant <b>vers l'atome qui va recevoir ce doublet</b>&nbsp;: le site accepteur si une liaison se forme, l'atome le plus électronégatif si une liaison se rompt.</p></li>
<li><p>Si l'atome accepteur ne peut pas recevoir un doublet de plus sans dépasser l'octet (ou le duet pour H), une de ses liaisons doit se rompre en même temps&nbsp;: tracer une <b>deuxième flèche</b>, partant de cette liaison.</p></li>
<li><p>Vérifier dans les produits&nbsp;: la conservation de la charge totale, et la règle de l'octet (ou du duet).</p></li>
</ol>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Erreurs fréquentes</p>
<ul class="nt-facts">
<li>Faire partir la flèche d'un atome ou d'une charge&nbsp;: elle part toujours d'un <b>doublet</b> (une flèche = un doublet = deux électrons).</li>
<li>Tracer la flèche dans le mauvais sens&nbsp;: elle va du <b>riche en électrons</b> (donneur) vers le <b>pauvre en électrons</b> (accepteur), donc souvent du «&nbsp;−&nbsp;» vers le «&nbsp;+&nbsp;».</li>
<li>Oublier la deuxième flèche quand une liaison se rompt.</li>
</ul>
</div>

<p class="nt-lead"><b>Catalogue des principaux types d'actes élémentaires.</b> Presque tous les actes élémentaires rencontrés en terminale se ramènent à quelques situations types. Dans chaque cas, le <b style="color:#2A6BC4;">site donneur</b> est en bleu, le <b style="color:#E11D48;">site accepteur</b> en rouge, et les flèches courbes en violet.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-1"></i>Un doublet non liant comble une lacune</p>
<p>C'est l'exemple précédent&nbsp;: une seule flèche, du doublet non liant vers l'atome qui porte la lacune. Une liaison se forme, sans qu'aucune ne se rompe.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-2"></i>Une liaison se rompt</p>
<svg class="nt-svg" viewBox="0 0 720 210" role="img" aria-label="Rupture hétérolytique de la liaison C–Cl : le doublet liant part entièrement sur l'atome de chlore, plus électronégatif"><text x="150" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="150" y="43" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="150" y="176" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="62" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan>C</text><line x1="150.0" y1="85.0" x2="150.0" y2="53.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="150.0" y1="115.0" x2="150.0" y2="148.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="92.0" y1="100.0" x2="135.0" y2="100.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="165.0" y1="100.0" x2="230.0" y2="100.0" stroke="var(--blue)" stroke-width="2" stroke-linecap="round"/><text x="245" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">Cl</text><line x1="237.0" y1="82.0" x2="253.0" y2="82.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="253.0" y1="118.0" x2="237.0" y2="118.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="265.0" y1="92.0" x2="265.0" y2="108.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><path d="M197,94 Q213.4,80.5 223.4,89.8" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="229,95 217.2,91.5 224.7,83.5" fill="#C026D3"/><text x="335" y="108" font-size="26" text-anchor="middle" fill="var(--slate)">⇄</text><text x="500" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="500" y="43" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="500" y="176" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><text x="412" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan>C</text><line x1="500.0" y1="85.0" x2="500.0" y2="53.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="500.0" y1="115.0" x2="500.0" y2="148.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="442.0" y1="100.0" x2="485.0" y2="100.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><rect x="518" y="90" width="12" height="20" rx="2" fill="none" stroke="var(--rose)" stroke-width="2.2"/><circle cx="536" cy="76" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="531.5" y1="76" x2="540.5" y2="76" stroke="var(--ink)" stroke-width="1.6"/><line x1="536" y1="71.5" x2="536" y2="80.5" stroke="var(--ink)" stroke-width="1.6"/><text x="585" y="108" font-size="22" text-anchor="middle" fill="var(--slate)">+</text><text x="650" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">Cl</text><line x1="642.0" y1="81.0" x2="658.0" y2="81.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="658.0" y1="119.0" x2="642.0" y2="119.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="669.0" y1="92.0" x2="669.0" y2="108.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="631.0" y1="108.0" x2="631.0" y2="92.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><circle cx="675" cy="76" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="670.5" y1="76" x2="679.5" y2="76" stroke="var(--ink)" stroke-width="1.6"/><text x="200" y="204" font-size="12.5" text-anchor="middle" fill="var(--blue)" font-weight="700">doublet liant (site donneur)</text></svg>
<p>Le doublet de la liaison C–Cl part entièrement sur l'atome le plus électronégatif (le chlore)&nbsp;: c'est la première étape du mécanisme vu plus haut. La flèche part du <b>milieu de la liaison</b> et pointe vers le chlore. Le carbone perd un doublet&nbsp;: il porte une lacune et une charge +.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque&nbsp;: et le site accepteur&nbsp;?</p>
<p>Ici, la flèche ne pointe ni vers une lacune, ni vers une charge positive, ni vers un atome δ+&nbsp;: le chlore est au contraire δ−. Les définitions des sites donneur et accepteur décrivent la <b>formation</b> d'une liaison. Lors d'une <b>rupture</b>, la flèche indique simplement où part le doublet de la liaison&nbsp;: vers le plus électronégatif des deux atomes, qui le garde pour lui.</p>
<p>D'où une règle qui couvre tous les cas&nbsp;: <b>une flèche courbe va toujours d'un doublet vers l'atome qui va le recevoir</b>. Ces ruptures se rencontrent dans beaucoup de mécanismes (substitutions, départ d'une molécule d'eau dans l'estérification…), presque toujours accompagnées d'une formation de liaison, comme dans les exemples 3, 5 et 6.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-3"></i>Une réaction acide-base&nbsp;: le transfert d'un proton</p>
<svg class="nt-svg" viewBox="0 0 800 210" role="img" aria-label="Réaction acide-base : le doublet non liant de l'azote capte un proton de l'ion oxonium, et la liaison O–H se rompt"><text x="140" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">N</text><text x="80" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="140" y="50" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="140" y="166" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="90.0" y1="100.0" x2="125.0" y2="100.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="140.0" y1="85.0" x2="140.0" y2="53.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="140.0" y1="115.0" x2="140.0" y2="147.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="156.0" y1="92.0" x2="156.0" y2="108.0" stroke="var(--blue)" stroke-width="2.4" stroke-linecap="round"/><text x="205" y="108" font-size="22" text-anchor="middle" fill="var(--slate)">+</text><text x="255" y="108" font-size="22" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="265.0" y1="100.0" x2="310.0" y2="100.0" stroke="var(--blue)" stroke-width="2" stroke-linecap="round"/><text x="325" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><text x="325" y="50" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="385" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="325.0" y1="85.0" x2="325.0" y2="53.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="340.0" y1="100.0" x2="375.0" y2="100.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="333.0" y1="116.0" x2="317.0" y2="116.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><circle cx="348" cy="76" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="343.5" y1="76" x2="352.5" y2="76" stroke="var(--ink)" stroke-width="1.6"/><line x1="348" y1="71.5" x2="348" y2="80.5" stroke="var(--ink)" stroke-width="1.6"/><path d="M159,100 Q201.4,75.0 238.2,94.4" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="245,98 232.7,97.7 237.8,88.0" fill="#C026D3"/><path d="M282,95 Q294.9,78.0 304.5,87.6" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="310,93 298.3,89.2 306.0,81.4" fill="#C026D3"/><text x="445" y="108" font-size="26" text-anchor="middle" fill="var(--slate)">⇄</text><text x="545" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">N</text><text x="485" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="545" y="50" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="545" y="166" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="605" y="108" font-size="22" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="495.0" y1="100.0" x2="530.0" y2="100.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="545.0" y1="85.0" x2="545.0" y2="53.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="545.0" y1="115.0" x2="545.0" y2="147.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="560.0" y1="100.0" x2="595.0" y2="100.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><circle cx="568" cy="76" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="563.5" y1="76" x2="572.5" y2="76" stroke="var(--ink)" stroke-width="1.6"/><line x1="568" y1="71.5" x2="568" y2="80.5" stroke="var(--ink)" stroke-width="1.6"/><text x="645" y="108" font-size="22" text-anchor="middle" fill="var(--slate)">+</text><text x="705" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><text x="705" y="50" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="765" y="108" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="705.0" y1="85.0" x2="705.0" y2="53.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="720.0" y1="100.0" x2="755.0" y2="100.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="713.0" y1="116.0" x2="697.0" y2="116.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="689.0" y1="108.0" x2="689.0" y2="92.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><text x="115" y="200" font-size="12.5" text-anchor="middle" fill="var(--blue)" font-weight="700">site donneur</text><text x="300" y="200" font-size="12.5" text-anchor="middle" fill="var(--rose)" font-weight="700">site accepteur (H polarisé δ+)</text></svg>
<p>Le doublet non liant de la base (ici l'ammoniac) se lie à l'atome d'hydrogène de l'acide (ici l'ion oxonium). L'hydrogène ne peut porter qu'un doublet (règle du duet)&nbsp;: la liaison O–H doit se rompre, d'où la <b>deuxième flèche</b>, qui ramène ce doublet sur l'oxygène. Toutes les réactions acide-base se représentent ainsi.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-4"></i>Le doublet d'une liaison double attaque</p>
<svg class="nt-svg" viewBox="0 0 760 210" role="img" aria-label="Addition d'un proton sur une double liaison : le doublet de la liaison double C=C forme une liaison avec le proton"><line x1="135.0" y1="106.5" x2="195.0" y2="106.5" stroke="var(--blue)" stroke-width="2" stroke-linecap="round"/><line x1="135.0" y1="113.5" x2="195.0" y2="113.5" stroke="var(--blue)" stroke-width="2" stroke-linecap="round"/><text x="120" y="118" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="210" y="118" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="70" y="78" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="108.3" y1="100.6" x2="78.6" y2="76.9" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="70" y="158" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="108.3" y1="119.4" x2="78.6" y2="143.1" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="260" y="78" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="221.7" y1="100.6" x2="251.4" y2="76.9" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="260" y="158" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="221.7" y1="119.4" x2="251.4" y2="143.1" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="305" y="118" font-size="22" text-anchor="middle" fill="var(--slate)">+</text><text x="370" y="118" font-size="22" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">H</text><rect x="348" y="100" width="12" height="20" rx="2" fill="none" stroke="var(--rose)" stroke-width="2.2"/><circle cx="388" cy="86" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="383.5" y1="86" x2="392.5" y2="86" stroke="var(--ink)" stroke-width="1.6"/><line x1="388" y1="81.5" x2="388" y2="90.5" stroke="var(--ink)" stroke-width="1.6"/><path d="M165,100 Q255.7,13.0 344.2,90.9" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="350,96 338.1,92.9 345.4,84.6" fill="#C026D3"/><text x="450" y="118" font-size="26" text-anchor="middle" fill="var(--slate)">⇄</text><line x1="575.0" y1="110.0" x2="635.0" y2="110.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="560" y="118" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="650" y="118" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="510" y="78" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="548.3" y1="100.6" x2="518.6" y2="76.9" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="510" y="158" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="548.3" y1="119.4" x2="518.6" y2="143.1" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="560" y="56" font-size="22" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="560.0" y1="95.0" x2="560.0" y2="59.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="700" y="78" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="661.7" y1="100.6" x2="691.4" y2="76.9" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="700" y="158" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="661.7" y1="119.4" x2="691.4" y2="143.1" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><rect x="668" y="100" width="12" height="20" rx="2" fill="none" stroke="var(--rose)" stroke-width="2.2"/><circle cx="696" cy="110" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="691.5" y1="110" x2="700.5" y2="110" stroke="var(--ink)" stroke-width="1.6"/><line x1="696" y1="105.5" x2="696" y2="114.5" stroke="var(--ink)" stroke-width="1.6"/><text x="165" y="200" font-size="12.5" text-anchor="middle" fill="var(--blue)" font-weight="700">doublet de la liaison double (site donneur)</text></svg>
<p>Une liaison double contient deux doublets&nbsp;: l'un d'eux peut servir de site donneur. La flèche part du <b>milieu de la liaison double</b> et pointe vers le proton&nbsp;; la liaison double devient simple, et le carbone qui n'a pas reçu le proton se retrouve avec une lacune. C'est la première étape de l'addition d'eau ou d'un acide sur un alcène.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-5"></i>Attaque d'un carbone δ+ avec basculement d'une liaison double</p>
<svg class="nt-svg" viewBox="0 0 760 230" role="img" aria-label="Addition nucléophile sur un groupe carbonyle : l'ion hydroxyde attaque l'atome de carbone, et le doublet de la liaison double C=O bascule sur l'oxygène"><text x="100" y="133" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><text x="45" y="133" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="55.0" y1="125.0" x2="85.0" y2="125.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="92.0" y1="109.0" x2="108.0" y2="109.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="108.0" y1="141.0" x2="92.0" y2="141.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="116.0" y1="117.0" x2="116.0" y2="133.0" stroke="var(--blue)" stroke-width="2.4" stroke-linecap="round"/><circle cx="122" cy="100" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="117.5" y1="100" x2="126.5" y2="100" stroke="var(--ink)" stroke-width="1.6"/><text x="270" y="133" font-size="22" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">C</text><line x1="266.5" y1="110.0" x2="266.5" y2="70.0" stroke="var(--blue)" stroke-width="2" stroke-linecap="round"/><line x1="273.5" y1="110.0" x2="273.5" y2="70.0" stroke="var(--blue)" stroke-width="2" stroke-linecap="round"/><text x="270" y="63" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><line x1="252.6" y1="50.8" x2="262.9" y2="38.6" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="277.1" y1="38.6" x2="287.4" y2="50.8" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="285.0" y1="125.0" x2="325.0" y2="125.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="355" y="133" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><line x1="270.0" y1="140.0" x2="270.0" y2="174.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="270" y="193" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><path d="M118,126 Q185.6,95.0 246.9,121.0" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="254,124 241.7,124.8 246.0,114.6" fill="#C026D3"/><path d="M263,94 Q244.7,81.6 253.4,70.2" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="258,64 255.8,76.1 247.0,69.5" fill="#C026D3"/><text x="440" y="133" font-size="26" text-anchor="middle" fill="var(--slate)">⇄</text><text x="610" y="133" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="540" y="133" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><line x1="532.0" y1="109.0" x2="548.0" y2="109.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="548.0" y1="141.0" x2="532.0" y2="141.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><text x="485" y="133" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="495.0" y1="125.0" x2="525.0" y2="125.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="555.0" y1="125.0" x2="595.0" y2="125.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="610.0" y1="110.0" x2="610.0" y2="70.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="610" y="63" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><line x1="594.0" y1="63.0" x2="594.0" y2="47.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="626.0" y1="47.0" x2="626.0" y2="63.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="602.0" y1="39.0" x2="618.0" y2="39.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><circle cx="642" cy="36" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="637.5" y1="36" x2="646.5" y2="36" stroke="var(--ink)" stroke-width="1.6"/><line x1="625.0" y1="125.0" x2="665.0" y2="125.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="695" y="133" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">CH<tspan font-size="14" dy="5">3</tspan><tspan dy="-5"></tspan></text><line x1="610.0" y1="140.0" x2="610.0" y2="174.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="610" y="193" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><text x="110" y="222" font-size="12.5" text-anchor="middle" fill="var(--blue)" font-weight="700">site donneur</text><text x="300" y="222" font-size="12.5" text-anchor="middle" fill="var(--rose)" font-weight="700">site accepteur (C polarisé δ+)</text></svg>
<p>Dans le groupe C=O, l'oxygène, plus électronégatif, rend le carbone δ+&nbsp;: c'est un site accepteur. Mais le carbone a déjà quatre liaisons (octet)&nbsp;: quand le doublet de l'ion hydroxyde arrive, un doublet de la liaison double C=O doit <b>basculer sur l'oxygène</b>, qui devient négatif. C'est le type d'étape qu'on retrouve dans l'estérification, l'hydrolyse ou la saponification d'un ester.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-6"></i>Une liaison se forme pendant qu'une autre se rompt</p>
<svg class="nt-svg" viewBox="0 0 780 210" role="img" aria-label="Substitution en un seul acte élémentaire : l'ion hydroxyde forme une liaison avec le carbone pendant que la liaison C–Cl se rompt"><text x="95" y="113" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><text x="40" y="113" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="50.0" y1="105.0" x2="80.0" y2="105.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="87.0" y1="89.0" x2="103.0" y2="89.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="103.0" y1="121.0" x2="87.0" y2="121.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="111.0" y1="97.0" x2="111.0" y2="113.0" stroke="var(--blue)" stroke-width="2.4" stroke-linecap="round"/><circle cx="117" cy="80" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="112.5" y1="80" x2="121.5" y2="80" stroke="var(--ink)" stroke-width="1.6"/><text x="230" y="113" font-size="22" text-anchor="middle" fill="var(--rose)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="230" y="53" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="230.0" y1="90.0" x2="230.0" y2="56.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="230" y="173" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="230.0" y1="120.0" x2="230.0" y2="154.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="188" y="70" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="219.5" y1="94.3" x2="195.7" y2="69.9" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="245.0" y1="105.0" x2="310.0" y2="105.0" stroke="var(--blue)" stroke-width="2" stroke-linecap="round"/><text x="325" y="113" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">Cl</text><line x1="317.0" y1="87.0" x2="333.0" y2="87.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="333.0" y1="123.0" x2="317.0" y2="123.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="345.0" y1="97.0" x2="345.0" y2="113.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><path d="M113,106 Q163.0,79.0 207.1,100.6" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="214,104 201.7,104.1 206.5,94.2" fill="#C026D3"/><path d="M278,99 Q292.7,83.6 303.7,91.5" fill="none" stroke="#C026D3" stroke-width="2.4" stroke-linecap="butt"/><polygon points="310,96 297.9,94.0 304.3,85.1" fill="#C026D3"/><text x="388" y="113" font-size="26" text-anchor="middle" fill="var(--slate)">⇄</text><text x="500" y="113" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">O</text><text x="445" y="113" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="455.0" y1="105.0" x2="485.0" y2="105.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><line x1="492.0" y1="89.0" x2="508.0" y2="89.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="508.0" y1="121.0" x2="492.0" y2="121.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="515.0" y1="105.0" x2="570.0" y2="105.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="585" y="113" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">C</text><text x="585" y="53" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="585.0" y1="90.0" x2="585.0" y2="56.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="585" y="173" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="585.0" y1="120.0" x2="585.0" y2="154.0" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="625" y="158" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">H</text><line x1="595.0" y1="116.2" x2="617.7" y2="141.8" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/><text x="665" y="113" font-size="22" text-anchor="middle" fill="var(--slate)">+</text><text x="725" y="113" font-size="22" text-anchor="middle" fill="var(--ink)" font-family="Georgia, 'Times New Roman', serif">Cl</text><line x1="717.0" y1="86.0" x2="733.0" y2="86.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="733.0" y1="124.0" x2="717.0" y2="124.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="744.0" y1="97.0" x2="744.0" y2="113.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><line x1="706.0" y1="113.0" x2="706.0" y2="97.0" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><circle cx="750" cy="80" r="8" fill="#fff" stroke="var(--ink)" stroke-width="1.4"/><line x1="745.5" y1="80" x2="754.5" y2="80" stroke="var(--ink)" stroke-width="1.6"/><text x="95" y="200" font-size="12.5" text-anchor="middle" fill="var(--blue)" font-weight="700">site donneur</text><text x="205" y="200" font-size="12.5" text-anchor="middle" fill="var(--rose)" font-weight="700">site accepteur</text><text x="335" y="200" font-size="12.5" text-anchor="middle" fill="var(--blue)" font-weight="700">liaison qui se rompt</text></svg>
<p>C'est l'acte unique de la réaction $\ce{H3C-Cl + HO- -> H3C-OH + Cl^-}$ vue plus haut&nbsp;: le carbone, lié au chlore très électronégatif, est δ+. Pour qu'il puisse recevoir le doublet de l'ion hydroxyde sans dépasser l'octet, la liaison C–Cl se rompt <b>au même moment</b>, et son doublet part sur le chlore, plus électronégatif (comme dans l'exemple 2). Deux flèches, donc, dans un seul acte élémentaire.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Dans tous les cas, on combine seulement deux mouvements de base&nbsp;: un doublet qui forme une <span class="imp nt-hole">nouvelle liaison</span> (flèche d'un doublet vers un atome), et un doublet liant qui <span class="imp nt-hole">rompt une liaison</span> en partant sur l'un des deux atomes (flèche du milieu d'une liaison vers un atome).</p>
</div>

### Catalyseur et mécanisme réactionnel {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Un <span class="imp">catalyseur</span> <span class="imp nt-hole">modifie le mécanisme réactionnel</span>.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>La transformation modélisée par la réaction $\ce{H3C-Cl + HO- -> H3C-OH + Cl^-}$ se déroule en un seul acte élémentaire.</p>
<p>Mais en présence d'ions iodure ${\color{#B45309}\ce{I-}}$, le mécanisme est modifié&nbsp;:</p>
<ol class="nt-steps">
<li><p>$\ce{H3C-Cl} \;+\; {\color{#B45309}\ce{I-}} \;\rightleftarrows\; {\color{#2A6BC4}\ce{H3C-I}} \;+\; \ce{Cl^-}$</p></li>
<li><p>${\color{#2A6BC4}\ce{H3C-I}} \;+\; \ce{HO-} \;\rightleftarrows\; \ce{H3C-OH} \;+\; {\color{#B45309}\ce{I-}}$</p></li>
</ol>
<p>Si l'on additionne les deux actes élémentaires, comme on le ferait avec deux demi-équations, ${\color{#B45309}\ce{I-}}$ et ${\color{#2A6BC4}\ce{H3C-I}}$ apparaissent de chaque côté et se simplifient&nbsp;: on retrouve l'équation de la réaction.</p>
<p>L'ion ${\color{#B45309}\ce{I-}}$ est momentanément utilisé puis finit par être reformé&nbsp;: il n'apparaît pas dans l'équation bilan. C'est un <b style="color:#B45309;">catalyseur</b>, et $\color{#2A6BC4}\ce{H3C-I}$ est un <b style="color:#2A6BC4;">intermédiaire réactionnel</b>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Quelle est la différence entre un catalyseur et un intermédiaire réactionnel&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>L'<b style="color:#2A6BC4;">intermédiaire réactionnel</b> apparaît d'abord comme <b>produit</b> d'un acte élémentaire puis comme <b>réactif</b> d'un autre acte élémentaire, alors que pour le <b style="color:#B45309;">catalyseur</b>, c'est l'inverse&nbsp;: il apparaît d'abord comme réactif d'un acte élémentaire puis comme produit d'un autre.</p>
<p>Par conséquent, le catalyseur n'est pas nécessaire à la réaction (il ouvre seulement un chemin plus rapide), alors que l'intermédiaire réactionnel est une étape obligée du mécanisme.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi un catalyseur accélère-t-il la réaction&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Chaque acte élémentaire nécessite de franchir une «&nbsp;barrière&nbsp;» d'énergie, l'énergie d'activation. En proposant un autre mécanisme, le catalyseur remplace une barrière élevée par plusieurs barrières plus basses&nbsp;: beaucoup plus de chocs sont alors assez énergétiques pour les franchir.</p>
<svg class="nt-svg nt-svg-m" viewBox="0 0 680 320" role="img" aria-label="Profil énergétique : sans catalyseur, une seule barrière d'énergie élevée ; avec catalyseur, deux barrières plus basses"><line x1="60" y1="270" x2="60" y2="30" stroke="var(--ink)" stroke-width="1.5"/><line x1="60" y1="270" x2="650" y2="270" stroke="var(--ink)" stroke-width="1.5"/><text x="66" y="40" font-size="13" fill="var(--slate)" font-weight="700">énergie</text><text x="640" y="290" font-size="13" fill="var(--slate)" text-anchor="end" font-weight="700">avancement de la réaction</text><path d="M70.0,200.0 L72.8,200.2 L75.6,200.5 L78.4,200.7 L81.2,201.0 L84.0,201.2 L86.8,201.5 L89.6,201.7 L92.4,202.0 L95.2,202.2 L98.0,202.5 L100.8,202.7 L103.6,203.0 L106.4,203.2 L109.2,203.5 L112.0,203.7 L114.8,204.0 L117.6,204.2 L120.4,204.5 L123.2,204.7 L126.0,205.0 L128.8,205.2 L131.6,205.5 L134.4,205.7 L137.2,206.0 L140.0,206.2 L142.8,206.5 L145.6,206.7 L148.4,206.9 L151.2,207.2 L154.0,207.4 L156.8,207.6 L159.6,207.8 L162.4,208.1 L165.2,208.3 L168.0,208.5 L170.8,208.6 L173.6,208.8 L176.4,209.0 L179.2,209.1 L182.0,209.3 L184.8,209.4 L187.6,209.5 L190.4,209.5 L193.2,209.5 L196.0,209.5 L198.8,209.5 L201.6,209.4 L204.4,209.3 L207.2,209.1 L210.0,208.8 L212.8,208.4 L215.6,208.0 L218.4,207.5 L221.2,206.9 L224.0,206.2 L226.8,205.4 L229.6,204.5 L232.4,203.5 L235.2,202.3 L238.0,200.9 L240.8,199.4 L243.6,197.8 L246.4,196.0 L249.2,193.9 L252.0,191.8 L254.8,189.4 L257.6,186.8 L260.4,184.0 L263.2,181.1 L266.0,177.9 L268.8,174.5 L271.6,171.0 L274.4,167.2 L277.2,163.3 L280.0,159.2 L282.8,155.0 L285.6,150.7 L288.4,146.2 L291.2,141.6 L294.0,137.0 L296.8,132.3 L299.6,127.6 L302.4,122.9 L305.2,118.3 L308.0,113.7 L310.8,109.3 L313.6,104.9 L316.4,100.8 L319.2,96.8 L322.0,93.1 L324.8,89.7 L327.6,86.5 L330.4,83.7 L333.2,81.3 L336.0,79.2 L338.8,77.5 L341.6,76.2 L344.4,75.4 L347.2,75.0 L350.0,75.0 L352.8,75.5 L355.6,76.4 L358.4,77.7 L361.2,79.5 L364.0,81.7 L366.8,84.3 L369.6,87.2 L372.4,90.5 L375.2,94.2 L378.0,98.1 L380.8,102.3 L383.6,106.8 L386.4,111.4 L389.2,116.3 L392.0,121.2 L394.8,126.3 L397.6,131.4 L400.4,136.6 L403.2,141.8 L406.0,147.0 L408.8,152.1 L411.6,157.2 L414.4,162.2 L417.2,167.0 L420.0,171.7 L422.8,176.3 L425.6,180.7 L428.4,185.0 L431.2,189.0 L434.0,192.9 L436.8,196.6 L439.6,200.0 L442.4,203.3 L445.2,206.4 L448.0,209.3 L450.8,211.9 L453.6,214.5 L456.4,216.8 L459.2,218.9 L462.0,220.9 L464.8,222.8 L467.6,224.5 L470.4,226.0 L473.2,227.4 L476.0,228.7 L478.8,229.9 L481.6,231.0 L484.4,232.0 L487.2,232.9 L490.0,233.8 L492.8,234.6 L495.6,235.3 L498.4,235.9 L501.2,236.5 L504.0,237.0 L506.8,237.5 L509.6,238.0 L512.4,238.5 L515.2,238.9 L518.0,239.3 L520.8,239.6 L523.6,240.0 L526.4,240.3 L529.2,240.6 L532.0,241.0 L534.8,241.3 L537.6,241.6 L540.4,241.8 L543.2,242.1 L546.0,242.4 L548.8,242.7 L551.6,242.9 L554.4,243.2 L557.2,243.5 L560.0,243.7 L562.8,244.0 L565.6,244.2 L568.4,244.5 L571.2,244.7 L574.0,245.0 L576.8,245.2 L579.6,245.5 L582.4,245.7 L585.2,246.0 L588.0,246.2 L590.8,246.5 L593.6,246.7 L596.4,247.0 L599.2,247.2 L602.0,247.5 L604.8,247.7 L607.6,248.0 L610.4,248.2 L613.2,248.5 L616.0,248.7 L618.8,249.0 L621.6,249.2 L624.4,249.5 L627.2,249.7 L630.0,250.0" fill="none" stroke="var(--rose)" stroke-width="3"/><path d="M70.0,200.0 L72.8,200.2 L75.6,200.4 L78.4,200.7 L81.2,200.9 L84.0,201.2 L86.8,201.4 L89.6,201.6 L92.4,201.9 L95.2,202.1 L98.0,202.3 L100.8,202.6 L103.6,202.8 L106.4,203.0 L109.2,203.3 L112.0,203.5 L114.8,203.7 L117.6,203.9 L120.4,204.1 L123.2,204.4 L126.0,204.6 L128.8,204.8 L131.6,205.0 L134.4,205.1 L137.2,205.3 L140.0,205.5 L142.8,205.7 L145.6,205.8 L148.4,206.0 L151.2,206.1 L154.0,206.2 L156.8,206.3 L159.6,206.4 L162.4,206.4 L165.2,206.4 L168.0,206.3 L170.8,206.1 L173.6,205.9 L176.4,205.5 L179.2,205.1 L182.0,204.5 L184.8,203.8 L187.6,202.8 L190.4,201.7 L193.2,200.3 L196.0,198.7 L198.8,196.9 L201.6,194.8 L204.4,192.4 L207.2,189.8 L210.0,186.9 L212.8,183.8 L215.6,180.5 L218.4,177.0 L221.2,173.5 L224.0,169.9 L226.8,166.4 L229.6,163.1 L232.4,159.9 L235.2,157.1 L238.0,154.6 L240.8,152.5 L243.6,150.9 L246.4,149.8 L249.2,149.3 L252.0,149.4 L254.8,150.0 L257.6,151.1 L260.4,152.7 L263.2,154.8 L266.0,157.2 L268.8,159.9 L271.6,162.9 L274.4,166.0 L277.2,169.1 L280.0,172.3 L282.8,175.4 L285.6,178.4 L288.4,181.2 L291.2,183.8 L294.0,186.1 L296.8,188.3 L299.6,190.2 L302.4,191.8 L305.2,193.3 L308.0,194.5 L310.8,195.5 L313.6,196.4 L316.4,197.1 L319.2,197.7 L322.0,198.2 L324.8,198.6 L327.6,198.9 L330.4,199.2 L333.2,199.5 L336.0,199.7 L338.8,199.9 L341.6,200.1 L344.4,200.4 L347.2,200.6 L350.0,200.9 L352.8,201.1 L355.6,201.4 L358.4,201.7 L361.2,202.0 L364.0,202.3 L366.8,202.5 L369.6,202.8 L372.4,203.1 L375.2,203.3 L378.0,203.4 L380.8,203.5 L383.6,203.5 L386.4,203.4 L389.2,203.2 L392.0,202.8 L394.8,202.3 L397.6,201.6 L400.4,200.7 L403.2,199.6 L406.0,198.3 L408.8,196.8 L411.6,195.1 L414.4,193.2 L417.2,191.2 L420.0,189.1 L422.8,187.0 L425.6,184.8 L428.4,182.7 L431.2,180.7 L434.0,178.9 L436.8,177.3 L439.6,176.1 L442.4,175.3 L445.2,174.8 L448.0,174.8 L450.8,175.3 L453.6,176.3 L456.4,177.7 L459.2,179.6 L462.0,181.9 L464.8,184.6 L467.6,187.6 L470.4,190.8 L473.2,194.2 L476.0,197.7 L478.8,201.3 L481.6,204.8 L484.4,208.3 L487.2,211.6 L490.0,214.8 L492.8,217.8 L495.6,220.6 L498.4,223.1 L501.2,225.4 L504.0,227.5 L506.8,229.4 L509.6,231.0 L512.4,232.5 L515.2,233.8 L518.0,234.9 L520.8,235.9 L523.6,236.8 L526.4,237.6 L529.2,238.3 L532.0,238.9 L534.8,239.4 L537.6,239.9 L540.4,240.4 L543.2,240.8 L546.0,241.2 L548.8,241.6 L551.6,242.0 L554.4,242.3 L557.2,242.7 L560.0,243.0 L562.8,243.3 L565.6,243.7 L568.4,244.0 L571.2,244.3 L574.0,244.6 L576.8,244.9 L579.6,245.1 L582.4,245.4 L585.2,245.7 L588.0,246.0 L590.8,246.3 L593.6,246.5 L596.4,246.8 L599.2,247.1 L602.0,247.3 L604.8,247.6 L607.6,247.9 L610.4,248.1 L613.2,248.4 L616.0,248.7 L618.8,248.9 L621.6,249.2 L624.4,249.4 L627.2,249.7 L630.0,250.0" fill="none" stroke="#059669" stroke-width="3" stroke-dasharray="7 5"/><text x="81.2" y="190.0" font-size="13" fill="var(--ink)" font-weight="700">réactifs</text><text x="618.8" y="240.0" font-size="13" fill="var(--ink)" text-anchor="end" font-weight="700">produits</text><line x1="350.0" y1="200.0" x2="350.0" y2="75.0" stroke="var(--rose)" stroke-width="1.5" stroke-dasharray="3 3"/><text x="383.6" y="81.0" font-size="14" fill="var(--rose)" font-weight="700">sans catalyseur</text><text x="249.20000000000002" y="137.3" font-size="13" fill="#059669" text-anchor="middle" font-weight="700">avec catalyseur</text><line x1="81.2" y1="200.0" x2="406.0" y2="200.0" stroke="var(--muted)" stroke-dasharray="4 4"/></svg>
<p>Les réactifs et les produits, eux, restent les mêmes&nbsp;: le catalyseur ne modifie ni le bilan, ni l'état final.</p>
</div>
</details>

## Interprétation microscopique des facteurs cinétiques {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour qu'un acte élémentaire ait lieu, il faut un <span class="imp nt-hole">choc entre les entités</span>.</p>
<ul class="nt-facts">
<li>Plus la <b>concentration</b> est grande, plus la <span class="imp nt-hole">probabilité de chocs</span> est grande.</li>
<li>Plus la <b>température</b> est grande, plus les entités vont vite, et donc plus la <span class="imp nt-hole">fréquence des chocs</span> et leur <span class="imp nt-hole">énergie</span> sont élevées.</li>
</ul>
<p>Cela explique pourquoi la concentration et la température sont des <b>facteurs cinétiques</b>.</p>
</div>

<div class="nt-lab" id="lab-chocs">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Des chocs, mais pas n'importe lesquels</p>
<p class="nt-note">Des entités A (bleues) et B (rouges) s'agitent. Seuls les chocs entre A et B assez énergétiques sont <b>efficaces</b>&nbsp;: ils forment une entité C (violette).</p>
<canvas class="box" style="height:300px;" aria-label="Particules en mouvement qui se heurtent et réagissent"></canvas>
<canvas class="graph" style="height:160px; margin-top:8px; background:#fff;" aria-label="Nombre de produits formés en fonction du temps"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Nombre d'entités A&nbsp;: <b class="out-na"></b><input type="range" data-p="na" min="0" max="150" step="5" value="60"></label>
<label class="nt-ctrl">Nombre d'entités B&nbsp;: <b class="out-nb"></b><input type="range" data-p="nb" min="0" max="150" step="5" value="60"></label>
<label class="nt-ctrl">Température (unités arbitraires)&nbsp;: <b class="out-T"></b><input type="range" data-p="T" min="1" max="10" step="1" value="4"></label>
</div>
<div class="nt-read" aria-live="polite"><span>produits formés&nbsp;: <b class="out-nc"></b></span><span>chocs A–B efficaces&nbsp;: <b class="out-chocs"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button>
<button type="button" class="nt-btn" data-act="trempe"><i class="fa-solid fa-snowflake"></i>&nbsp; Trempe</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-msg">Augmentez la concentration&nbsp;: les chocs sont plus nombreux. Augmentez la température&nbsp;: les chocs sont plus fréquents et une plus grande proportion d'entre eux est efficace.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-snowflake"></i>La trempe</p>
<p>La <b>trempe</b> consiste à refroidir brutalement un prélèvement du milieu réactionnel (souvent en le diluant dans de l'eau glacée)&nbsp;: les chocs deviennent rares et peu énergétiques, la réaction est quasiment stoppée. On peut alors doser tranquillement le prélèvement, pour connaître la composition du milieu à la date du prélèvement. Essayez le bouton «&nbsp;Trempe&nbsp;» dans l'animation.</p>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CP = '#C026D3', CR = '#2A6BC4', CT = '#D97706', CK = '#059669';   /* produit, réactif, tangente, constructions */
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function sci(x, nd) {
    if (x === 0) { return '0'; }
    var s = x < 0 ? '\u2212' : ''; x = Math.abs(x);
    var n = Math.floor(Math.log10(x) + 1e-9), a = x / Math.pow(10, n), t = a.toFixed(nd);
    if (parseFloat(t) >= 10) { n += 1; t = (a / 10).toFixed(nd); }
    return s + t.replace('.', ',') + ' \u00d7 10<sup>' + String(n).replace('-', '\u2212') + '</sup>';
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
  function watchVisible(el, cb) {
    if (!('IntersectionObserver' in window)) { cb(true); return; }
    new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }).observe(el);
  }
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '700 12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.9)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  /* repère : graduations et quadrillage léger */
  function frame(c, w, h, o) {
    var L = o.L || 58, R = w - (o.R || 16), T = o.T || 14, B = h - (o.B || 34);
    function X(v) { return L + (v - o.x0) / (o.x1 - o.x0) * (R - L); }
    function Y(v) { return B - (v - o.y0) / (o.y1 - o.y0) * (B - T); }
    c.strokeStyle = col('--line'); c.lineWidth = 1;
    for (var gx = o.x0; gx <= o.x1 + 1e-9; gx += o.dx) { c.beginPath(); c.moveTo(X(gx), T); c.lineTo(X(gx), B); c.stroke(); }
    for (var gy = o.y0; gy <= o.y1 + 1e-9; gy += o.dy) { c.beginPath(); c.moveTo(L, Y(gy)); c.lineTo(R, Y(gy)); c.stroke(); }
    c.strokeStyle = col('--ink'); c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
    c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
    for (gx = o.x0; gx <= o.x1 + 1e-9; gx += o.dx) { c.fillText(fr(gx, o.ndx || 0), X(gx), B + 14); }
    c.fillText(o.xl, (L + R) / 2, h - 3);
    c.textAlign = 'right';
    for (gy = o.y0; gy <= o.y1 + 1e-9; gy += o.dy) { c.fillText(fr(gy, o.ndy || 0), L - 5, Y(gy) + 4); }
    c.save(); c.translate(12, (T + B) / 2); c.rotate(-Math.PI / 2); c.textAlign = 'center'; c.fillText(o.yl, 0, 0); c.restore();
    return { X: X, Y: Y, L: L, R: R, T: T, B: B };
  }
  function curve(c, F, f, x0, x1, color, w, dash) {
    c.strokeStyle = color; c.lineWidth = w || 2.6; c.setLineDash(dash || []); c.beginPath();
    for (var i = 0; i <= 300; i++) { var x = x0 + (x1 - x0) * i / 300, y = F.Y(f(x)); if (i === 0) { c.moveTo(F.X(x), y); } else { c.lineTo(F.X(x), y); } }
    c.stroke(); c.setLineDash([]);
  }
  /* ================= 1. Vitesse volumique : la pente de la tangente ================= */
  (function () {
    var root = document.getElementById('lab-tangente');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rT = $(root, 'input[type="range"]'), oT = $(root, '.out-t'), oV = $(root, '.out-v'), oF = $(root, '.out-formule'), msg = $(root, '.nt-msg'), S, mode = 'app';
    /* concentrations en 10^-2 mol/L, temps en s */
    var M = {
      app: { f: function (t) { return 3.46 * (1 - Math.exp(-t / 173)); }, d: function (t) { return 3.46 / 173 * Math.exp(-t / 173); }, c: CP, n: '[I\u2082]', y1: 3.6 },
      dis: { f: function (t) { return 2.7 * Math.exp(-0.010 * t); }, d: function (t) { return -0.027 * Math.exp(-0.010 * t); }, c: CR, n: '[H\u2082O\u2082]', y1: 3.0 }
    };
    function draw() {
      var m = M[mode], t0 = +rT.value, c = S.ctx, w = S.w, h = S.h;
      c.clearRect(0, 0, w, h);
      var F = frame(c, w, h, { x0: 0, x1: 300, dx: 30, y0: 0, y1: m.y1, dy: 0.3, ndy: 1, xl: 'temps (s)', yl: 'concentration (\u00d7 10\u207b\u00b2 mol\u00b7L\u207b\u00b9)' });
      curve(c, F, m.f, 0, 300, m.c);
      var y0 = m.f(t0), s = m.d(t0);
      /* tangente */
      c.save(); c.beginPath(); c.rect(F.L, F.T, F.R - F.L, F.B - F.T); c.clip();
      curve(c, F, function (x) { return y0 + s * (x - t0); }, 0, 300, CT, 2);
      /* triangle de pente : Δt = 45 s */
      var dt = 45, ta = Math.max(0, Math.min(255, t0 - dt / 2)), tb = ta + dt, ya = y0 + s * (ta - t0), yb = y0 + s * (tb - t0);
      c.fillStyle = 'rgba(56,189,248,.35)'; c.beginPath(); c.moveTo(F.X(ta), F.Y(ya)); c.lineTo(F.X(tb), F.Y(ya)); c.lineTo(F.X(tb), F.Y(yb)); c.closePath(); c.fill();
      c.restore();
      txt(c, '\u0394t = 45 s', (F.X(ta) + F.X(tb)) / 2, F.Y(ya) + (s > 0 ? 15 : -7), CT);
      txt(c, '\u0394C = ' + fr(s * dt, 2), F.X(tb) + 6, (F.Y(ya) + F.Y(yb)) / 2 + 4, CT, '700 12px system-ui, sans-serif', 'left');
      c.strokeStyle = 'rgba(30,41,59,.5)'; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(F.X(t0), F.Y(y0)); c.lineTo(F.X(t0), F.B); c.stroke(); c.setLineDash([]);
      c.fillStyle = CT; c.beginPath(); c.arc(F.X(t0), F.Y(y0), 5, 0, 2 * Math.PI); c.fill();
      var v = Math.abs(s) * 1e-2;
      oT.textContent = t0 + ' s';
      oV.innerHTML = sci(v, 1) + ' mol\u00b7L<sup>\u22121</sup>\u00b7s<sup>\u22121</sup>';
      oF.innerHTML = mode === 'app'
        ? 'v<sub>a,I\u2082</sub>(' + t0 + ' s) = pente = ' + fr(s * dt, 2) + ' \u00d7 10<sup>\u22122</sup> / 45 = ' + sci(v, 1)
        : 'v<sub>d,H\u2082O\u2082</sub>(' + t0 + ' s) = \u2212 pente = \u2212 (' + fr(s * dt, 2) + ' \u00d7 10<sup>\u22122</sup>) / 45 = ' + sci(v, 1);
      msg.textContent = mode === 'app' ? 'Le diiode est un produit : sa concentration augmente, la pente de la tangente est positive, et elle diminue au cours du temps.'
        : 'Le peroxyde d\u2019hydrogène est un réactif : la pente est négative ; la vitesse de disparition, son opposé, est positive.';
    }
    rT.addEventListener('input', draw);
    $$(root, 'input[name="tg"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; draw(); }); });
    $$(root, '[data-t]').forEach(function (b) { b.addEventListener('click', function () { rT.value = b.getAttribute('data-t'); draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 2. Loi d'ordre 1 : [A](t) et ln[A](t) ================= */
  (function () {
    var root = document.getElementById('lab-ordre1');
    if (!root) { return; }
    var c1 = $(root, 'canvas.c1'), c2 = $(root, 'canvas.c2'), rA = $(root, '[data-p="a0"]'), rK = $(root, '[data-p="k"]'), cbF = $(root, '[data-p="fit"]');
    var oA = $(root, '.out-a0'), oK = $(root, '.out-k'), oH = $(root, '.out-th'), oP = $(root, '.out-pente'), S1, S2;
    var TM = 300, PTS = [];
    for (var i = 0; i <= 12; i++) { PTS.push([i * 25, 1 + 0.03 * Math.sin(i * 2.7 + 0.4)]); }   /* « mesures » avec un léger bruit */
    function draw() {
      var a0 = +rA.value, k = +rK.value / 1000, th = Math.log(2) / k;
      oA.innerHTML = fr(a0, 1) + ' \u00d7 10<sup>\u22122</sup> mol\u00b7L<sup>\u22121</sup>'; oK.innerHTML = sci(k, 1) + ' s<sup>\u22121</sup>'; oH.textContent = fr(th, 0) + ' s';
      function A(t) { return a0 * Math.exp(-k * t); }
      var c = S1.ctx; c.clearRect(0, 0, S1.w, S1.h);
      var F = frame(c, S1.w, S1.h, { x0: 0, x1: TM, dx: 50, y0: 0, y1: 5, dy: 1, xl: 'temps (s)', yl: '[A] (\u00d7 10\u207b\u00b2 mol\u00b7L\u207b\u00b9)', L: 46 });
      curve(c, F, A, 0, TM, CR);
      PTS.forEach(function (p) { c.fillStyle = CR; c.beginPath(); c.arc(F.X(p[0]), F.Y(A(p[0]) * p[1]), 3.5, 0, 2 * Math.PI); c.fill(); });
      if (th < TM) {
        c.strokeStyle = CK; c.setLineDash([4, 4]); c.lineWidth = 1.5; c.beginPath(); c.moveTo(F.L, F.Y(a0 / 2)); c.lineTo(F.X(th), F.Y(a0 / 2)); c.lineTo(F.X(th), F.B); c.stroke(); c.setLineDash([]);
        txt(c, 't\u00bd', F.X(th), F.B - 6, CK);
      }
      var g = S2.ctx; g.clearRect(0, 0, S2.w, S2.h);
      var lmin = Math.log(a0 * 1e-2) - k * TM - 0.3, lmax = Math.log(5e-2) + 0.2;
      var lo = Math.floor(lmin), hi = Math.ceil(lmax);
      var G = frame(g, S2.w, S2.h, { x0: 0, x1: TM, dx: 50, y0: lo, y1: hi, dy: 1, xl: 'temps (s)', yl: 'ln([A])', L: 46 });
      var pts = PTS.map(function (p) { return [p[0], Math.log(A(p[0]) * p[1] * 1e-2)]; });
      pts.forEach(function (p) { g.fillStyle = CR; g.beginPath(); g.arc(G.X(p[0]), G.Y(p[1]), 3.5, 0, 2 * Math.PI); g.fill(); });
      /* régression linéaire */
      var n = pts.length, sx = 0, sy = 0, sxx = 0, sxy = 0;
      pts.forEach(function (p) { sx += p[0]; sy += p[1]; sxx += p[0] * p[0]; sxy += p[0] * p[1]; });
      var a = (n * sxy - sx * sy) / (n * sxx - sx * sx), b = (sy - a * sx) / n;
      if (cbF.checked) { curve(g, G, function (x) { return a * x + b; }, 0, TM, CT, 2); }
      oP.innerHTML = sci(a, 2) + ' s<sup>\u22121</sup>, soit k \u2248 ' + sci(-a, 2) + ' s<sup>\u22121</sup>';
    }
    [rA, rK].forEach(function (r) { r.addEventListener('input', draw); }); cbF.addEventListener('change', draw);
    function setup() { S1 = canvasCtx(c1); S2 = canvasCtx(c2); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 3. Temps de demi-réaction ================= */
  (function () {
    var root = document.getElementById('lab-tdemi');
    if (!root) { return; }
    var cv = $(root, 'canvas'), cbC = $(root, '[data-p="constr"]'), msg = $(root, '.nt-msg'), S, mode = 'x';
    var K = 0.012, TM = 400, TH = Math.log(2) / K;
    var M = {
      x: { f: function (t) { return 2.0 * (1 - Math.exp(-K * t)); }, lim: 2.0, n: 'avancement x (mmol)', c: CK, half: 1.0, lab: ['x\u2091 = 2,0 mmol', 'x\u2091/2'] },
      r: { f: function (t) { return 4.0 * Math.exp(-K * t); }, lim: 0, n: '[R] (\u00d7 10\u207b\u00b2 mol\u00b7L\u207b\u00b9)', c: CR, half: 2.0, lab: ['[R]\u2080 = 4,0', '[R]\u2080/2'] },
      p: { f: function (t) { return 3.0 * (1 - Math.exp(-K * t)); }, lim: 3.0, n: '[P] (\u00d7 10\u207b\u00b2 mol\u00b7L\u207b\u00b9)', c: CP, half: 1.5, lab: ['[P]\u2091 = 3,0', '[P]\u2091/2'] }
    };
    function draw() {
      var m = M[mode], c = S.ctx, w = S.w, h = S.h;
      c.clearRect(0, 0, w, h);
      var F = frame(c, w, h, { x0: 0, x1: TM, dx: 50, y0: 0, y1: 4.5, dy: 0.5, ndy: 1, xl: 'temps (s)', yl: m.n, L: 52 });
      curve(c, F, m.f, 0, TM, m.c);
      var ref = mode === 'r' ? 4.0 : m.lim;
      c.strokeStyle = 'rgba(30,41,59,.4)'; c.setLineDash([6, 4]); c.lineWidth = 1.2; c.beginPath(); c.moveTo(F.L, F.Y(ref)); c.lineTo(F.R, F.Y(ref)); c.stroke(); c.setLineDash([]);
      txt(c, m.lab[0], F.R - 4, F.Y(ref) - 6, col('--slate'), '700 12px system-ui, sans-serif', 'right');
      if (cbC.checked) {
        c.strokeStyle = CT; c.setLineDash([5, 4]); c.lineWidth = 1.8; c.beginPath(); c.moveTo(F.L, F.Y(m.half)); c.lineTo(F.X(TH), F.Y(m.half)); c.lineTo(F.X(TH), F.B); c.stroke(); c.setLineDash([]);
        c.fillStyle = CT; c.beginPath(); c.arc(F.X(TH), F.Y(m.half), 5, 0, 2 * Math.PI); c.fill();
        txt(c, m.lab[1], F.L + 8, F.Y(m.half) - 6, CT, '700 12px system-ui, sans-serif', 'left');
        txt(c, 't\u00bd \u2248 ' + Math.round(TH) + ' s', F.X(TH), F.B - 8, CT);
      }
      msg.textContent = 'La transformation est presque terminée vers ' + Math.round(5 * TH) + ' s, soit environ 5 t\u00bd (il reste alors 3 % du réactif limitant) : le temps de demi-réaction n\u2019est pas la moitié de la durée de la réaction !';
    }
    cbC.addEventListener('change', draw);
    $$(root, 'input[name="td"]').forEach(function (x) { x.addEventListener('change', function () { mode = x.value; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 4. Interprétation microscopique : les chocs efficaces ================= */
  (function () {
    var root = document.getElementById('lab-chocs');
    if (!root) { return; }
    var cv = $(root, 'canvas.box'), cg = $(root, 'canvas.graph'), rA = $(root, '[data-p="na"]'), rB = $(root, '[data-p="nb"]'), rT = $(root, '[data-p="T"]');
    var oA = $(root, '.out-na'), oB = $(root, '.out-nb'), oT = $(root, '.out-T'), oN = $(root, '.out-nc'), oC = $(root, '.out-chocs'), btnR = $(root, '[data-act="reset"]'), btnT = $(root, '[data-act="trempe"]'), btn = $(root, '[data-act="play"]');
    var S, SG, P = [], hist = [], t = 0, chocs = 0, eff = 0, playing = !RM, visible = true, last = null, rA_ = 7, rC = 9;
    var ETH = 16384;   /* seuil fixe (énergie d'activation) : la fraction de chocs efficaces augmente avec la température */
    function rnd() { var u = Math.random() || 1e-9, v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
    function speed() { return Math.sqrt(+rT.value) * 32; }
    function spawn(type) { var s = speed(); return { x: 20 + Math.random() * (S.w - 40), y: 20 + Math.random() * (S.h - 40), vx: rnd() * s, vy: rnd() * s, t: type }; }
    function reset() {
      P = []; hist = []; t = 0; chocs = 0; eff = 0;
      for (var i = 0; i < +rA.value; i++) { P.push(spawn('A')); }
      for (var j = 0; j < +rB.value; j++) { P.push(spawn('B')); }
    }
    function rescale() {   /* changement de température : on ajuste les vitesses */
      var cur = 0, n = 0; P.forEach(function (p) { cur += p.vx * p.vx + p.vy * p.vy; n++; });
      if (!n) { return; } var target = speed() * speed() * 2, f = Math.sqrt(target / (cur / n));
      P.forEach(function (p) { p.vx *= f; p.vy *= f; });
    }
    function stepPhys(dt) {
      var w = S.w, h = S.h;
      P.forEach(function (p) {
        p.x += p.vx * dt; p.y += p.vy * dt; var r = p.t === 'C' ? rC : rA_;
        if (p.x < r) { p.x = r; p.vx = Math.abs(p.vx); } if (p.x > w - r) { p.x = w - r; p.vx = -Math.abs(p.vx); }
        if (p.y < r) { p.y = r; p.vy = Math.abs(p.vy); } if (p.y > h - r) { p.y = h - r; p.vy = -Math.abs(p.vy); }
      });
      for (var i = 0; i < P.length; i++) {
        for (var j = i + 1; j < P.length; j++) {
          var a = P[i], b = P[j]; if (a.dead || b.dead) { continue; }
          var dx = b.x - a.x, dy = b.y - a.y, d2 = dx * dx + dy * dy, rr = (a.t === 'C' ? rC : rA_) + (b.t === 'C' ? rC : rA_);
          if (d2 < rr * rr && d2 > 0) {
            var d = Math.sqrt(d2), nx = dx / d, ny = dy / d, rv = (a.vx - b.vx) * nx + (a.vy - b.vy) * ny;
            if (rv <= 0) { continue; }
            var ab = (a.t === 'A' && b.t === 'B') || (a.t === 'B' && b.t === 'A');
            if (ab) {
              chocs++;
              /* choc efficace si l'énergie de la collision dépasse l'énergie d'activation */
              if (rv * rv > ETH) {
                eff++; a.t = 'C'; a.x = (a.x + b.x) / 2; a.y = (a.y + b.y) / 2; a.vx = (a.vx + b.vx) / 2; a.vy = (a.vy + b.vy) / 2; b.dead = true; continue;
              }
            }
            a.vx -= rv * nx; a.vy -= rv * ny; b.vx += rv * nx; b.vy += rv * ny;   /* choc élastique (masses égales) */
            var ov = (rr - d) / 2; a.x -= nx * ov; a.y -= ny * ov; b.x += nx * ov; b.y += ny * ov;
          }
        }
      }
      P = P.filter(function (p) { return !p.dead; });
    }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, Tn = +rT.value;
      c.fillStyle = 'rgb(' + Math.round(20 + Tn * 6) + ',12,' + Math.round(40 - Tn * 2) + ')'; c.fillRect(0, 0, w, h);
      P.forEach(function (p) {
        c.fillStyle = p.t === 'A' ? '#56C1FF' : (p.t === 'B' ? '#FF968D' : '#E879F9');
        c.beginPath(); c.arc(p.x, p.y, p.t === 'C' ? rC : rA_, 0, 2 * Math.PI); c.fill();
      });
      var nC = P.filter(function (p) { return p.t === 'C'; }).length;
      oN.textContent = nC; oC.textContent = chocs > 0 ? fr(100 * eff / chocs, 1) + ' %' : '\u2014';
      var g = SG.ctx, W = SG.w, H = SG.h; g.clearRect(0, 0, W, H);
      var F = frame(g, W, H, { x0: 0, x1: 30, dx: 5, y0: 0, y1: 150, dy: 50, xl: 'temps (s)', yl: 'produits formés', L: 44, B: 30 });
      g.strokeStyle = '#C026D3'; g.lineWidth = 2.2; g.beginPath();
      hist.forEach(function (q, i) { if (q[0] > 30) { return; } if (i === 0) { g.moveTo(F.X(q[0]), F.Y(q[1])); } else { g.lineTo(F.X(q[0]), F.Y(q[1])); } });
      g.stroke();
    }
    function step(ts) {
      var dt = last === null ? 0 : Math.min(0.04, (ts - last) / 1000); last = ts;
      if (playing && visible && S) { stepPhys(dt); t += dt; if (!hist.length || t - hist[hist.length - 1][0] > 0.2) { hist.push([t, P.filter(function (p) { return p.t === 'C'; }).length]); } }
      if (visible && S) { draw(); }
      requestAnimationFrame(step);
    }
    function labels() { oA.textContent = rA.value; oB.textContent = rB.value; oT.textContent = rT.value; }
    [rA, rB].forEach(function (r) { r.addEventListener('input', function () { labels(); reset(); }); });
    rT.addEventListener('input', function () { labels(); rescale(); });
    btnR.addEventListener('click', reset);
    btnT.addEventListener('click', function () { rT.value = 1; labels(); rescale(); });
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    function setup() { S = canvasCtx(cv); SG = canvasCtx(cg); if (!P.length) { reset(); } }
    watchVisible(cv, function (v) { visible = v; });
    labels(); playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
})();
</script>
