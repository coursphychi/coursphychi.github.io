+++
title = "Champ uniforme"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Champ de pesanteur uniforme {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp nt-hole">champ de pesanteur</span> est décrit par un champ vectoriel $\vec{g}$ dont la direction est indiquée par un fil à plomb.</p>
<p>Placée dans un champ de pesanteur, toute masse $m$ subit une force <span class="imp nt-hole">$\vec{P}=m\vec{g}$</span> appelée <span class="imp nt-hole">poids</span>.</p>
</div>

<p class="nt-lead">La valeur de $g$ varie en fonction de la position sur Terre et de l'altitude.</p>

<div class="nt-lab" id="lab-g">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'intensité de la pesanteur à la surface de la Terre</p>
<canvas style="height:280px;" aria-label="Coupe de la Terre avec le point choisi et son vecteur g, et position de g sur une échelle"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Latitude&nbsp;: <b class="out-lat"></b><input type="range" data-p="lat" min="0" max="90" step="1" value="46"></label>
<label class="nt-ctrl">Altitude&nbsp;: <b class="out-alt"></b><input type="range" data-p="alt" min="0" max="9000" step="50" value="300"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$g$ = <b class="out-g"></b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-preset="0,0">équateur</button>
<button type="button" class="nt-btn" data-preset="49,35">Paris</button>
<button type="button" class="nt-btn" data-preset="90,0">pôle Nord</button>
<button type="button" class="nt-btn" data-preset="28,8849">sommet de l'Everest</button>
</div>
<p class="nt-note">Valeurs calculées pour un modèle d'ellipsoïde (sans les anomalies locales)&nbsp;: $g$ augmente de l'équateur vers les pôles, car la Terre est aplatie et tourne sur elle-même, et diminue avec l'altitude.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">La «&nbsp;patate de Potsdam&nbsp;»</span></summary>
<div class="nt-d-body">
<p>La Terre n'est même pas exactement un ellipsoïde&nbsp;: la répartition inégale des masses dans son intérieur crée de petites anomalies du champ de pesanteur. Le géoïde, la surface qu'aurait un océan au repos recouvrant toute la Terre, s'écarte de l'ellipsoïde de référence de $+80$&nbsp;m à $-100$&nbsp;m environ. Représenté avec ces écarts très exagérés, il ressemble à une pomme de terre, d'où son surnom, venu du centre de recherche de Potsdam qui l'a cartographié&nbsp;: <a href="https://apod.nasa.gov/apod/ap141215.html" target="_blank" rel="noopener">voir l'image de la «&nbsp;patate de Potsdam&nbsp;»</a>.</p>
<p>Ces anomalies ne modifient la valeur de $g$ qu'à partir du troisième chiffre après la virgule.</p>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Au voisinage de la surface d'une planète, sur des distances faibles par rapport à son rayon, le champ de pesanteur $\vec{g}$ peut être considéré comme <span class="imp nt-hole">uniforme</span>.</p>
<p class="nt-note">Uniforme signifie partout identique&nbsp;: $\vec{g}=\overrightarrow{\text{cte}}$.</p>
</div>

<div class="nt-lab" id="lab-zoom">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Zoomer pour voir le champ devenir uniforme</p>
<canvas style="height:300px;" aria-label="Vecteurs du champ de pesanteur autour de la Terre, vus de plus en plus près de la surface"></canvas>
<label class="nt-ctrl">Zoom vers la surface&nbsp;: <input type="range" min="0" max="3.6" step="0.02" value="0"></label>
<div class="nt-read" aria-live="polite"><span>largeur de la zone&nbsp;: <b class="out-w"></b></span><span>écart de direction&nbsp;: <b class="out-dir"></b></span><span>écart de norme&nbsp;: <b class="out-norm"></b></span></div>
<p class="nt-msg">Vu de loin, le champ est dirigé vers le centre de la Terre et diminue avec la distance. Sur une zone de quelques kilomètres, les vecteurs sont pratiquement parallèles et de même norme&nbsp;: le champ est uniforme.</p>
</div>

## Équations horaires du mouvement et équation de la trajectoire {.nt-h2}

<p class="nt-lead">On étudie le lancer d'une balle de basket. À l'instant $t=0$, la balle quitte les mains du joueur.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On néglige les forces de frottement $\Rightarrow$ seule force extérieure&nbsp;: <span class="imp nt-hole">le poids</span> $\Leftrightarrow$ situation de <span class="imp nt-hole">chute libre</span>.</p>
</div>

<p class="nt-lead">Dans le <b>référentiel terrestre</b>, supposé <b>galiléen</b>, le mouvement du centre de masse $\mathrm{M}$ d'un système de masse constante $m$ est étudié dans le repère d'espace $(\mathrm{O};\vec{i},\vec{j},\vec{k})$.</p>

<svg class="nt-svg nt-svg-m" viewBox="0 0 600 380" role="img" aria-label="Repère et conditions initiales : le point part de M0 à la hauteur h avec une vitesse v0 faisant l'angle alpha avec l'horizontale ; le champ de pesanteur g est vertical vers le bas"><rect x="0" y="330" width="600" height="50" fill="#F1F5F9"/><line x1="40" y1="330" x2="572.0" y2="330.0" stroke="var(--slate)" stroke-width="1.5" stroke-linecap="round"/><polygon points="580.0,330.0 570.0,335.0 570.0,325.0" fill="var(--slate)"/><line x1="90" y1="360" x2="90.0" y2="33.0" stroke="var(--slate)" stroke-width="1.5" stroke-linecap="round"/><polygon points="90.0,25.0 95.0,35.0 85.0,35.0" fill="var(--slate)"/><text x="572" y="352" font-size="15" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">x</text><text x="72" y="34" font-size="15" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">z</text><text x="74" y="352" font-size="16" fill="var(--ink)" text-anchor="middle" font-weight="700">O</text><line x1="90" y1="330" x2="132.0" y2="330.0" stroke="var(--blue)" stroke-width="3" stroke-linecap="round"/><polygon points="140.0,330.0 130.0,335.0 130.0,325.0" fill="var(--blue)"/><text x="108" y="356" font-size="16" fill="var(--blue)" font-family="Georgia, serif" font-style="italic" font-weight="700">i</text><line x1="108" y1="341" x2="116.8" y2="341" stroke="var(--blue)" stroke-width="1.4"/><polygon points="119.8,341.0 114.8,343.6 114.8,338.4" fill="var(--blue)"/><line x1="90" y1="330" x2="90.0" y2="288.0" stroke="var(--blue)" stroke-width="3" stroke-linecap="round"/><polygon points="90.0,280.0 95.0,290.0 85.0,290.0" fill="var(--blue)"/><text x="64" y="300" font-size="16" fill="var(--blue)" font-family="Georgia, serif" font-style="italic" font-weight="700">k</text><line x1="64" y1="285" x2="72.8" y2="285" stroke="var(--blue)" stroke-width="1.4"/><polygon points="75.8,285.0 70.8,287.6 70.8,282.4" fill="var(--blue)"/><line x1="70" y1="200" x2="90" y2="200" stroke="var(--muted)" stroke-dasharray="4 3"/><text x="60" y="205" font-size="17" fill="var(--ink)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">h</text><path d="M145,200 A55,55 0 0,0 135.1,168.5 L90,200 Z" fill="#F9A8D4" opacity=".45"/><text x="158" y="186" font-size="17" fill="var(--rose)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">α</text><line x1="90" y1="200" x2="204.9" y2="200.0" stroke="#D97706" stroke-width="2" stroke-linecap="round" stroke-dasharray="5 4"/><polygon points="212.9,200.0 202.9,205.0 202.9,195.0" fill="#D97706"/><line x1="212.9" y1="200" x2="212.9" y2="114.0" stroke="#D97706" stroke-width="2" stroke-dasharray="5 4"/><polygon points="212.9,115.0 217.4,124.0 208.4,124.0" fill="#D97706"/><line x1="90" y1="200" x2="206.3" y2="118.6" stroke="#D97706" stroke-width="3.2" stroke-linecap="round"/><polygon points="212.9,114.0 207.5,123.8 201.8,115.6" fill="#D97706"/><text x="130" y="138" font-size="19" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="700">v<tspan font-size="12" dy="4">0</tspan></text><line x1="130" y1="120" x2="140.45" y2="120" stroke="#D97706" stroke-width="1.4"/><polygon points="143.4,120.0 138.4,122.6 138.4,117.4" fill="#D97706"/><text x="121.4" y="224" font-size="15" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="700">v<tspan font-size="11" dy="4">0</tspan><tspan dy="-4"> cos α</tspan></text><text x="222.9" y="162.0" font-size="15" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="700">v<tspan font-size="11" dy="4">0</tspan><tspan dy="-4"> sin α</tspan></text><circle cx="90" cy="200" r="6" fill="var(--rose)"/><text x="60" y="188" font-size="16" fill="var(--rose)" font-family="Georgia, serif" font-style="italic" font-weight="700">M<tspan font-size="11" dy="4">0</tspan></text><line x1="470" y1="90" x2="470.0" y2="167.0" stroke="#059669" stroke-width="3.2" stroke-linecap="round"/><polygon points="470.0,175.0 465.0,165.0 475.0,165.0" fill="#059669"/><text x="482" y="140" font-size="19" fill="#059669" font-family="Georgia, serif" font-style="italic" font-weight="700">g</text><line x1="482" y1="122" x2="492.45" y2="122" stroke="#059669" stroke-width="1.4"/><polygon points="495.4,122.0 490.4,124.6 490.4,119.4" fill="#059669"/><text x="470" y="205" font-size="12" fill="#059669" text-anchor="middle" font-weight="700">champ de pesanteur</text></svg>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-flag"></i>Conditions initiales</p>
<p>À la date $t=0$, le point $\mathrm{M}$ est situé en $\mathrm{M_0}(0,0,h)$. Et son vecteur vitesse initial vaut&nbsp;:</p>
<p class="nt-center">$\vec{v}(t=0)=\vec{v}_0\begin{cases}v_x(0)=v_0\cos(\alpha)\\v_y(0)=0\\v_z(0)=v_0\sin(\alpha)\end{cases}$</p>
</div>

<ol class="nt-steps">
<li>
<p><b>Inventaire des forces extérieures</b>&nbsp;: <span class="imp nt-hole">le poids</span> $\vec{P}=m\vec{g}$.</p>
</li>
<li>
<p><b style="color:#059669;">Vecteur accélération.</b> Application de la deuxième loi de Newton&nbsp;:</p>
<p class="nt-center">$m{\color{#059669}\vec{a}} = \sum \vec{F}_\mathrm{ext} \Rightarrow m{\color{#059669}\vec{a}}=m\vec{g} \Rightarrow {\color{#059669}\vec{a}}=\vec{g}$</p>
<p>Le mouvement est <span class="imp nt-hole">uniformément accéléré vers le bas</span>, et les coordonnées du vecteur accélération sont&nbsp;:</p>
<p class="nt-center">${\color{#059669}\vec{a}(t)\begin{cases}a_x(t)=0\\a_y(t)=0\\a_z(t)=-g\end{cases}}$</p>
</li>
<li>
<p><b style="color:#D97706;">Vecteur vitesse.</b> Les coordonnées du vecteur vitesse sont des <span class="imp nt-hole"><a href="../primitives" target="_blank" rel="noopener noreferrer">primitives</a></span> des coordonnées du vecteur accélération&nbsp;:</p>
<p class="nt-center">${\color{#059669}\begin{cases}\frac{\mathrm{d}v_x}{\mathrm{d}t}=0\\[1mm]\frac{\mathrm{d}v_y}{\mathrm{d}t}=0\\[1mm]\frac{\mathrm{d}v_z}{\mathrm{d}t}=-g\end{cases}} \Rightarrow {\color{#D97706}\vec{v}(t)\begin{cases}v_x(t)=c_1\\v_y(t)=c_2\\v_z(t)=-gt+c_3\end{cases}}$</p>
<p>On obtient les constantes d'intégration grâce aux <span class="imp nt-hole">conditions initiales</span>&nbsp;: $v_x(0)=c_1=v_0\cos\alpha$, $v_y(0)=c_2=0$ et $v_z(0)=c_3=v_0\sin\alpha$. D'où&nbsp;:</p>
<p class="nt-center">${\color{#D97706}\vec{v}(t)\begin{cases}v_x(t)=v_0\cos\alpha\\v_y(t)=0\\v_z(t)=-gt+v_0\sin\alpha\end{cases}}$</p>
</li>
<li>
<p><b style="color:#2A6BC4;">Vecteur position.</b> Les coordonnées du vecteur position sont des primitives des coordonnées du vecteur vitesse&nbsp;:</p>
<p class="nt-center">${\color{#2A6BC4}\overrightarrow{\mathrm{OM}}(t)\begin{cases}x(t)=(v_0\cos\alpha)t+c'_1\\y(t)=c'_2\\z(t)=-\frac12 gt^2+(v_0\sin\alpha)t+c'_3\end{cases}}$</p>
<p>Avec les conditions initiales&nbsp;: $x(0)=c'_1=0$, $y(0)=c'_2=0$ et $z(0)=c'_3=h$.</p>
</li>
</ol>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Équations horaires du mouvement</p>
<p class="nt-f-math">$$\overrightarrow{\mathrm{OM}}(t)\begin{cases}x(t)=(v_0\cos\alpha)\,t\\y(t)=0\\z(t)=-\frac12 gt^2 + (v_0\sin\alpha)\,t + h\end{cases}$$</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode&nbsp;: obtenir l'équation de la trajectoire $z(x)$</p>
<ol class="nt-steps">
<li><p>On isole $t$ grâce à l'équation $x(t)$&nbsp;: $x = (v_0\cos\alpha)\,t \Rightarrow t = \dfrac{x}{v_0\cos\alpha}$.</p></li>
<li><p>On remplace dans $z(t)$&nbsp;: $z(x)=-\dfrac12 g \left(\dfrac{x}{v_0\cos\alpha}\right)^2+v_0\sin\alpha\left(\dfrac{x}{v_0\cos\alpha}\right)+h$.</p></li>
</ol>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Équation de la trajectoire</p>
<p class="nt-f-math">$$z(x)=-\frac{g}{2\left(v_0\cos\alpha\right)^2}\,x^2+\tan(\alpha)\, x+h$$</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La trajectoire est donc <span class="imp nt-hole">plane</span> (comprise dans le plan $(\mathrm{O},\vec{i},\vec{k})$).</p>
<p>Le mouvement de chute libre est <span class="imp nt-hole">parabolique</span> (la trajectoire est une portion de parabole).</p>
</div>

<div class="nt-lab" id="lab-chute">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Un lancer en chute libre</p>
<canvas style="height:320px;" aria-label="Trajectoire parabolique d'un objet lancé, avec ses vecteurs vitesse et accélération"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Vitesse initiale $v_0$&nbsp;: <b class="out-v0"></b><input type="range" data-p="v0" min="1" max="15" step="0.1" value="10"></label>
<label class="nt-ctrl">Angle $\alpha$&nbsp;: <b class="out-al"></b><input type="range" data-p="al" min="0" max="90" step="1" value="50"></label>
<label class="nt-ctrl">Hauteur initiale $h$&nbsp;: <b class="out-h"></b><input type="range" data-p="h" min="0" max="5" step="0.1" value="2"></label>
<label class="nt-ctrl">Masse $m$&nbsp;: <b class="out-m"></b><input type="range" data-p="m" min="0.1" max="10" step="0.1" value="0.6"></label>
</div>
<div class="nt-read" aria-live="polite"><span>portée = <b class="out-x"></b></span><span>hauteur maximale = <b class="out-z"></b></span><span>durée du vol = <b class="out-t"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-note">Points espacés de 0,1&nbsp;s. Changez la masse&nbsp;: rien ne change&nbsp;!</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Le mouvement de chute libre <span class="imp nt-hole">ne dépend pas de la masse</span>&nbsp;!</p>
<p>En effet, la masse a disparu dès le départ (2<sup>e</sup> loi de Newton).</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Deux vidéos sur la chute libre</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://www.youtube.com/watch?v=E43-CfukEgs" target="_blank" rel="noopener">Une vidéo sur l'indépendance de la chute libre vis-à-vis de la masse</a>.</li>
<li><a href="https://www.youtube.com/watch?v=Un5roSKDusQ" target="_blank" rel="noopener">Une vidéo consacrée aux trajectoires paraboliques des chutes libres</a>.</li>
</ul>
</div>
</details>

## Petits exercices {.nt-h2}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 1</p>
<p>Une pierre est lâchée sans vitesse initiale au-dessus d'un puits. On mesure une durée $\Delta t = \pu{2 s}$ avant d'entendre "plouf".</p>
<p>Si on néglige les frottements, quelle est la profondeur approximative du puits&nbsp;? Que peut-on supposer en réalité&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la méthode</span></summary>
<div class="nt-d-body">
<p>Avec $v_0 = 0$, l'équation horaire verticale se réduit à&nbsp;:</p>
<p class="nt-center">$z(t) = h - \frac12 g t^2$</p>
<p>La pierre touche le sol quand $z = 0$&nbsp;:</p> 
<p class="nt-center">$h = \frac12 g\,\Delta t^2$</p>
Pour $\Delta t = \pu{3,0 s}$, $h \approx \pu{20 m}$.</p>
<p>En réalité, les frottements de l'air ralentissent la pierre&nbsp;: pour une même durée de chute, elle parcourt une distance plus faible. La profondeur calculée surestime donc la profondeur réelle.<br>
Une autre raison nous fait un poil surestimer la profondeur&nbsp;: le temps que met le son pour remonter à la surface qui nous fait surestimer la durée de chute (mais ça rajouterait moins d'un dixième de seconde ici).</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-volleyball"></i>Exercice 2</p>
<p>À quelle vitesse minimale doit partir la balle 🏐 pour passer le filet&nbsp;? Le joueur frappe la balle à la hauteur $h = \pu{3,50 m}$ avec une vitesse horizontale, depuis le fond du terrain de longueur $L = \pu{18,0 m}$&nbsp;; le filet, au milieu du terrain, a une hauteur $H = \pu{2,40 m}$. Rayon de la balle&nbsp;: $r=\pu{10 cm}$.</p>
</div>

<div class="nt-lab" id="lab-volley">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le service au volley</p>
<canvas style="height:240px;" aria-label="Trajectoire d'un service au volley, du serveur jusqu'au sol, par-dessus le filet"></canvas>
<label class="nt-ctrl">Vitesse du service $v_0$&nbsp;: <b class="out-v0"></b><input type="range" min="12" max="28" step="0.1" value="17"></label>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>Ici, la vitesse initiale est purement horizontale ($\Rightarrow \alpha=0$)&nbsp;: $\vec{v}_0 \begin{cases}v_0\\0\\0\end{cases}$. L'équation de la trajectoire devient alors&nbsp;:</p>
 <p class="nt-center">$z(x) = -\dfrac{g}{2v_0^2}x^2 + h$.</p></li>
<li><p>Pour que le ballon passe au-dessus du filet, il faut&nbsp;: $z(x_\mathrm{filet})=z(L/2) > H+r$, soit</p>
<p class="nt-center">$-\dfrac{g}{2v_0^2}\left(\dfrac L2\right)^{2} + h > H+r \Leftrightarrow \dfrac{g}{2v_0^2}\left(\dfrac L2\right)^2 < h-(H+r) \Leftrightarrow v_0 > \sqrt{\dfrac{g L^2}{8\left(h-(H+r)\right)}}$</p></li>
<li><p>Application numérique&nbsp;: $v_0 > \sqrt{\dfrac{9{,}8 \times 18^2}{8\times\left(3{,}50-(2{,}40+0{,}10)\right)}}$, soit $v_0 > \pu{20 m*s-1}$.</p></li>
<li><p><b>Question subsidiaire&nbsp;: comment s'assurer que le service atterrit bien dans les limites du terrain&nbsp;?</b> On trouve la distance horizontale $x_\mathrm{sol}$ parcourue par le ballon au moment de toucher le sol en résolvant $z(x_\mathrm{sol})=r$&nbsp;:</p>
<p class="nt-center">$-\dfrac{g}{2v_0^2}x_\mathrm{sol}^2 + h = r \Rightarrow x_\mathrm{sol} = \pm v_0\sqrt{\dfrac{2(h-r)}{g}}$</p>
<p>Seule la solution positive (devant le serveur) nous intéresse. Il faut donc $v_0\sqrt{\dfrac{2(h-r)}{g}} < L$, soit $v_0 < L\sqrt{\dfrac{g}{2(h-r)}} = 18\times \sqrt{\dfrac{9{,}8}{2\times (3{,}50-0{,}10)}} = \pu{22 m*s-1}$.</p></li>
</ol>
<p>La vitesse du service doit finalement être comprise entre 20 et 22&nbsp;m/s. Easy peasy.</p>
</div>
</details>

## Aspects énergétiques {.nt-h2}

<p class="nt-lead">Rappels de première&nbsp;: le travail d'une force constante $\vec{F}$ le long d'un déplacement de A à B vaut $W_\mathrm{AB}(\vec{F}) = \vec{F}\cdot\overrightarrow{\mathrm{AB}} = F\times \mathrm{AB}\times\cos\theta$ (en joules), où $\theta$ est l'angle entre $\vec{F}$ et $\overrightarrow{\mathrm{AB}}$.</p>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Théorème de l'énergie cinétique</p>
<p class="nt-f-math">$$\Delta E_c = E_{c\mathrm{B}} - E_{c\mathrm{A}} = \sum W_\mathrm{AB}(\vec{F}_\mathrm{ext})$$</p>
<div class="nt-f-units"><span>la variation d'énergie cinétique est égale à la somme des travaux de <b>toutes</b> les forces extérieures</span><span>$E_c = \frac12 mv^2$, en <b>$\pu{J}$</b></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Théorème de l'énergie mécanique</p>
<p class="nt-f-math">$$\Delta E_m = E_{m\mathrm{B}} - E_{m\mathrm{A}} = \sum W_\mathrm{AB}(\vec{F}_\mathrm{n.c.})$$</p>
<div class="nt-f-units"><span>la variation d'énergie mécanique est égale à la somme des travaux des seules forces <b>non conservatives</b></span><span>$E_m = E_c + E_p$, en <b>$\pu{J}$</b></span></div>
</div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Une force est <b>conservative</b> si son travail ne dépend pas du chemin suivi (c'est le cas du poids et de la force électrique dans un champ uniforme). Son travail est alors compté dans l'énergie potentielle&nbsp;; les frottements, eux, sont des forces non conservatives.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Lors d'une chute libre, l'<span class="imp nt-hole">énergie mécanique $E_m$</span> du système est la somme de son <b style="color:#D97706;">énergie cinétique $E_c=\frac12 mv^2$</b> et de son <b style="color:#2A6BC4;">énergie potentielle de pesanteur $E_{pp}=mgz$</b>.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Comme la seule force agissant sur le système est conservative, le <span class="imp nt-hole">théorème de l'énergie mécanique</span>, $\Delta E_m = \sum W_\mathrm{AB}(\vec{F}_\mathrm{n.c.}) = 0$, nous assure que l'<span class="imp nt-hole">énergie mécanique est conservée</span> pendant le mouvement.</p>
<p>L'énergie cinétique est ainsi convertie en énergie potentielle de pesanteur et inversement.</p>
</div>

<div class="nt-lab" id="lab-energie">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Les énergies d'un ballon en chute libre</p>
<canvas class="scene" style="height:240px;" aria-label="Ballon en chute libre et diagrammes en barres de ses énergies"></canvas>
<canvas class="graph" style="height:170px; margin-top:8px; background:#fff;" aria-label="Énergies cinétique, potentielle et mécanique en fonction du temps"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Vitesse initiale $v_0$&nbsp;: <b class="out-v0"></b><input type="range" data-p="v0" min="2" max="12" step="0.1" value="8"></label>
<label class="nt-ctrl">Angle $\alpha$&nbsp;: <b class="out-al"></b><input type="range" data-p="al" min="0" max="90" step="1" value="55"></label>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-note">Ballon de 600&nbsp;g lancé depuis 2,0&nbsp;m de haut (origine de l'énergie potentielle au sol). En orange&nbsp;: $E_c$&nbsp;; en bleu&nbsp;: $E_{pp}$&nbsp;; en rouge&nbsp;: $E_m = E_c + E_{pp}$, constante.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Utiliser la conservation de l'énergie peut permettre de déterminer plus rapidement la valeur de certaines grandeurs que la 2<sup>e</sup> loi de Newton (équations horaires).</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Déterminer la vitesse d'arrivée au sol d'une pièce de 1&nbsp;€ qui tombe du 3<sup>e</sup> étage de la tour Eiffel ($h=\pu{276 m}$) en négligeant les frottements.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p>La pièce part sans vitesse ($E_c = 0$) à l'altitude $h$, et arrive au sol ($E_{pp} = 0$) avec la vitesse $v$. La conservation de l'énergie mécanique donne&nbsp;:</p>
<p class="nt-center">$mgh = \dfrac12 m v^2 \Rightarrow v = \sqrt{2gh} = \sqrt{2\times 9{,}81\times 276} = \pu{73,6 m*s-1}$, soit environ $\pu{265 km*h-1}$.</p>
<p>Pas besoin des équations horaires, et la masse de la pièce n'intervient pas. En réalité, les frottements de l'air limitent la vitesse de la pièce à quelques dizaines de km/h.</p>
</div>
</details>

## Champ électrique créé par un condensateur plan {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un <span class="imp nt-hole">condensateur plan</span> est constitué de deux plaques métalliques chargées, parallèles entre elles et séparées par un isolant (air, huile…).</p>
<p>Il se crée alors un <span class="imp nt-hole">champ électrique uniforme</span> dans la zone de l'espace située entre les deux plaques (suffisamment loin des bords).</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Les <span class="imp">lignes de champ</span> sont <span class="imp nt-hole">perpendiculaires</span> aux plaques, orientées de la plaque chargée <span class="imp nt-hole">positivement</span> vers la plaque chargée <span class="imp nt-hole">négativement</span>.</p>
</div>

<div class="nt-lab" id="lab-condo">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le champ électrique d'un condensateur plan</p>
<canvas style="height:260px;" aria-label="Condensateur plan : deux plaques chargées et le champ électrique uniforme entre elles"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Tension $U$&nbsp;: <b class="out-U"></b><input type="range" data-p="U" min="50" max="1000" step="10" value="400"></label>
<label class="nt-ctrl">Distance entre les plaques $d$&nbsp;: <b class="out-d"></b><input type="range" data-p="d" min="2" max="10" step="0.1" value="6"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$E = U/d$ = <b class="out-E"></b></span></div>
<div class="nt-btns"><label class="nt-check"><input type="checkbox" data-p="inv"> inverser la polarité</label></div>
<p class="nt-note">Plus les plaques sont chargées (plus de signes + et −), plus le champ est intense.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Champ créé par un condensateur plan</p>
<p class="nt-f-math">$$E=\frac U d$$</p>
<div class="nt-f-units"><span>$U$&nbsp;: tension entre les plaques (en <span class="nt-hole">$\pu{V}$</span>)</span><span>$d$&nbsp;: distance entre les plaques (en <b>$\pu{m}$</b>)</span><span>$E$ en <span class="nt-hole">$\pu{V*m-1}$</span></span></div>
</div>

## Mouvement dans un champ électrique uniforme {.nt-h2}

<p class="nt-lead">Prenons l'exemple du principe de fonctionnement des imprimantes à jet d'encre continu dévié, principalement utilisées pour imprimer les dates d'expiration figurant sur les produits alimentaires.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-print"></i>Principe</p>
<p>Le jet d'encre sort de la tête d'impression par une buse qui le décompose en très petites gouttes dont certaines sont chargées électriquement.</p>
<p>Celles-ci passent sous un déflecteur constitué de deux plaques P<sub>1</sub> et P<sub>2</sub> parallèles, chargées électriquement, assimilables à un condensateur plan. Ces plaques dévient les gouttes chargées de leur trajectoire initiale.</p>
<p>Les gouttes non chargées poursuivent leur mouvement rectiligne vers une gouttière de recyclage.</p>
</div>

<svg class="nt-svg" viewBox="0 0 700 360" role="img" aria-label="Déflecteur d'une imprimante à jet d'encre : la goutte entre en O entre les plaques P1 et P2, est déviée vers le haut, sort en S puis va en ligne droite jusqu'au point d'impact I sur le support"><rect x="90" y="180.0" width="210" height="120" fill="#E2E8F0" opacity=".6"/><rect x="90" y="170.0" width="210" height="10" fill="var(--rose)"/><text x="318" y="178.0" font-size="15" fill="var(--rose)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">P<tspan font-size="11" dy="4">1</tspan></text><rect x="90" y="300.0" width="210" height="10" fill="var(--blue)"/><text x="318" y="312.0" font-size="15" fill="var(--blue)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">P<tspan font-size="11" dy="4">2</tspan></text><text x="195.0" y="332.0" font-size="12" fill="var(--slate)" text-anchor="middle" font-weight="700">déflecteur</text><line x1="130" y1="196" x2="130.0" y2="236.0" stroke="#059669" stroke-width="2.4" stroke-linecap="round"/><polygon points="130.0,244.0 125.0,234.0 135.0,234.0" fill="#059669"/><text x="140" y="222" font-size="17" fill="#059669" font-family="Georgia, serif" font-style="italic" font-weight="700">E</text><line x1="140" y1="206" x2="149.35" y2="206" stroke="#059669" stroke-width="1.4"/><polygon points="152.3,206.0 147.3,208.6 147.3,203.4" fill="#059669"/><line x1="40" y1="240" x2="672.0" y2="240.0" stroke="var(--slate)" stroke-width="1.2" stroke-linecap="round"/><polygon points="680.0,240.0 670.0,245.0 670.0,235.0" fill="var(--slate)"/><text x="672" y="262" font-size="15" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">x</text><line x1="90" y1="310" x2="90.0" y2="118.0" stroke="var(--slate)" stroke-width="1.2" stroke-linecap="round"/><polygon points="90.0,110.0 95.0,120.0 85.0,120.0" fill="var(--slate)"/><text x="76" y="120" font-size="15" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">z</text><text x="76" y="260" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">O</text><line x1="50" y1="240" x2="80.0" y2="240.0" stroke="#D97706" stroke-width="2.8" stroke-linecap="round"/><polygon points="88.0,240.0 78.0,245.0 78.0,235.0" fill="#D97706"/><text x="46" y="230" font-size="16" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="700">v<tspan font-size="10" dy="4">0</tspan></text><line x1="46" y1="215" x2="54.8" y2="215" stroke="#D97706" stroke-width="1.4"/><polygon points="57.8,215.0 52.8,217.6 52.8,212.4" fill="#D97706"/><path d="M90,240 L90,240.0 L96,240.0 L102,239.9 L108,239.7 L114,239.5 L120,239.3 L126,238.9 L132,238.6 L138,238.1 L144,237.6 L150,237.0 L156,236.4 L162,235.7 L168,235.0 L174,234.2 L180,233.4 L186,232.4 L192,231.5 L198,230.4 L204,229.3 L210,228.2 L216,227.0 L222,225.7 L228,224.4 L234,223.0 L240,221.6 L246,220.0 L252,218.5 L258,216.9 L264,215.2 L270,213.4 L276,211.6 L282,209.8 L288,207.9 L294,205.9 L300,203.8 L300,203.8" fill="none" stroke="var(--blue)" stroke-width="2.6"/><line x1="300" y1="203.8" x2="560" y2="114.3" stroke="var(--blue)" stroke-width="2.6"/><line x1="300" y1="203.8" x2="560" y2="203.8" stroke="var(--muted)" stroke-dasharray="4 4"/><path d="M360,203.8 A60,60 0 0,0 356.7,184.3" fill="none" stroke="var(--rose)" stroke-width="1.6"/><text x="374" y="195.838" font-size="15" fill="var(--rose)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">α</text><line x1="560" y1="40" x2="560" y2="330" stroke="var(--ink)" stroke-width="4"/><text x="566" y="340" font-size="12" fill="var(--ink)" text-anchor="start" font-weight="700">support</text><line x1="300" y1="240" x2="300" y2="203.8" stroke="var(--muted)" stroke-dasharray="3 3"/><circle cx="300" cy="240.0" r="4" fill="var(--ink)"/><text x="308" y="258" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">H</text><circle cx="300" cy="203.8" r="4" fill="var(--ink)"/><text x="286" y="195.838" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">S</text><circle cx="560" cy="240.0" r="4" fill="var(--ink)"/><text x="576" y="258" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">H'</text><circle cx="560" cy="203.8" r="4" fill="var(--ink)"/><text x="576" y="207.838" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">S'</text><circle cx="560" cy="114.3" r="4" fill="var(--ink)"/><text x="574" y="118.29400000000001" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">I</text><line x1="90" y1="335" x2="292.0" y2="335.0" stroke="var(--slate)" stroke-width="1.4" stroke-linecap="round"/><polygon points="300.0,335.0 290.0,340.0 290.0,330.0" fill="var(--slate)"/><line x1="300" y1="335" x2="98.0" y2="335.0" stroke="var(--slate)" stroke-width="1.4" stroke-linecap="round"/><polygon points="90.0,335.0 100.0,330.0 100.0,340.0" fill="var(--slate)"/><text x="195.0" y="355" font-size="16" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">L</text><line x1="300" y1="335" x2="552.0" y2="335.0" stroke="var(--slate)" stroke-width="1.4" stroke-linecap="round"/><polygon points="560.0,335.0 550.0,340.0 550.0,330.0" fill="var(--slate)"/><line x1="560" y1="335" x2="308.0" y2="335.0" stroke="var(--slate)" stroke-width="1.4" stroke-linecap="round"/><polygon points="300.0,335.0 310.0,330.0 310.0,340.0" fill="var(--slate)"/><text x="430.0" y="355" font-size="16" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">D</text></svg>

<p class="nt-lead">À la date $t_0=\pu{0 s}$, la goutte d'encre G pénètre dans la zone de champ électrique uniforme au niveau du point O avec une vitesse initiale notée $\vec{v}_0=v_0\,\vec{i}$.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Sachant que la goutte, chargée négativement, est déviée vers le haut, quel est le signe des charges portées par P<sub>1</sub> et P<sub>2</sub>&nbsp;? Que peut-on dire du champ $\vec{E}$ entre les plaques&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>La goutte, négative, est attirée par la plaque positive&nbsp;: P<sub>1</sub> (en haut) est chargée <b>positivement</b>, P<sub>2</sub> (en bas) <b>négativement</b>.</p>
<p>Le champ $\vec{E}$ est uniforme entre les plaques, perpendiculaire à celles-ci et orienté de P<sub>1</sub> vers P<sub>2</sub>, donc vers le bas&nbsp;: $\vec{E} = -E\,\vec{k}$.</p>
</div>
</details>

<p class="nt-lead">Obtenons les équations horaires du mouvement de la goutte dans le déflecteur. On se place dans le <b>référentiel terrestre</b> supposé <b>galiléen</b> et muni du <b>repère d'espace</b> $(\mathrm{O};\vec{i},\vec{j},\vec{k})$.</p>

<ol class="nt-steps">
<li>
<p><b>Bilan des forces extérieures s'appliquant à la goutte&nbsp;:</b> le poids $\vec{P}=m\vec{g}$&nbsp;; la force électrique <span class="imp nt-hole">$\vec{F}_e = q\vec{E}$</span>&nbsp;; les actions de l'air sur la goutte (poussée d'Archimède, frottements).</p>
<p>Dans la suite, on négligera les autres forces que la force électrique&nbsp;: la goutte a une masse et une surface toutes petites ($m \approx \pu{2E-10 kg}$, soit un poids de l'ordre de $\pu{2E-9 N}$, alors que la force électrique vaut environ $|q|E \approx \pu{4E-7 N}$, près de deux cents fois plus).</p>
</li>
<li>
<p><b style="color:#059669;">Vecteur accélération.</b> Application de la deuxième loi de Newton&nbsp;:</p>
<p class="nt-center">$m{\color{#059669}\vec{a}} = \sum \vec{F}_\mathrm{ext} \Rightarrow m{\color{#059669}\vec{a}}=q\vec{E} \Rightarrow {\color{#059669}\vec{a}}=\dfrac {q} m \vec{E}$</p>
<p>Comme $q<0$, le mouvement est <span class="imp nt-hole">uniformément accéléré vers le haut</span>. Coordonnées du vecteur accélération (en effet, $\vec{E}=-E\,\vec{k}$)&nbsp;:</p>
<p class="nt-center">${\color{#059669}\vec{a}(t)\begin{cases}a_x(t)=0\\a_y(t)=0\\a_z(t)=-\frac {qE}{m}\end{cases}}$</p>
<p class="nt-note">Le signe − est important&nbsp;! C'est $\vec{E}$ qu'on projette, et $\vec{E}$ est orienté vers le bas.</p>
</li>
<li>
<p><b style="color:#D97706;">Vecteur vitesse.</b> On primitive les coordonnées de $\vec{a}$&nbsp;: $v_x(t)=c_1$, $v_y(t)=c_2$, $v_z(t)=-\frac{qE}{m} t+c_3$. D'après les conditions initiales, $c_1=v_0$, $c_2=0$ et $c_3=0$. D'où&nbsp;:</p>
<p class="nt-center">${\color{#D97706}\vec{v}(t)\begin{cases}v_x(t)=v_0\\v_y(t)=0\\v_z(t)=-\frac{qE}{m} t\end{cases}}$</p>
</li>
<li>
<p><b style="color:#2A6BC4;">Vecteur position.</b> On primitive les coordonnées de $\vec{v}$&nbsp;; d'après les conditions initiales, toutes les constantes sont nulles. D'où les <span class="imp nt-hole">équations horaires du mouvement</span>&nbsp;:</p>
<p class="nt-center">${\color{#2A6BC4}\overrightarrow{\mathrm{OG}}(t)\begin{cases}x_\mathrm{G}(t)=v_0 t\\y_\mathrm{G}(t)=0\\z_\mathrm{G}(t)=-\frac{qE}{2m} t^2\end{cases}}$</p>
</li>
</ol>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice</p>
<p>Déterminer la valeur de la hauteur H'I du point d'impact I de la goutte sur le support d'impression, si on suppose que le mouvement de la goutte est rectiligne uniforme en sortie du déflecteur (de S à I).</p>
<p>Données&nbsp;: $m=\pu{2E-10 kg}$&nbsp;; $q=\pu{-4E-13 C}$&nbsp;; $L=\pu{2 cm}$&nbsp;; $D=\pu{3 cm}$&nbsp;; $E=\pu{9E5 V*m-1}$&nbsp;; $v_0=\pu{20 m*s-1}$.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la marche à suivre et le résultat</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p>Déterminer la date $t_\mathrm{S}$ où la goutte sort du déflecteur grâce à $x(t_\mathrm{S})=L$, et la déviation $\mathrm{HS} = z(t_\mathrm{S})$.</p></li>
<li><p>Déterminer les coordonnées de $\vec{v}_\mathrm{S}$.</p></li>
<li><p>Montrer que $\tan\alpha=-\dfrac{qEL}{mv_0^2}$ et en déduire $\mathrm{S'I}$, puis ajouter $\mathrm{H'S'} = \mathrm{HS}$.</p></li>
</ol>
<p>On est censé trouver&nbsp;:</p>
<p class="nt-center">$\mathrm{H'I}=-\dfrac{qEL}{mv_0^2}\left(\dfrac L2+D\right)$</p>
<p class="nt-note">Le terme en facteur est bien sans dimension, car $qEL$ a la dimension d'une énergie (charge $\times$ champ $\times$ distance $=$ charge $\times$ tension $=$ énergie), et $mv_0^2$ aussi.</p>
<p>A.N.&nbsp;: $\mathrm{H'I}=-\dfrac{(\pu{-4E-13 C})\times\pu{9E5 V*m-1}\times\pu{2E-2 m}}{\pu{2E-10 kg}\times (\pu{20 m*s-1})^2}\times\left(\dfrac{\pu{2E-2 m}}{2}+\pu{3E-2 m}\right) = \pu{4E-3 m}=\pu{4 mm}$.</p>
<p>Cette déviation paraît cohérente avec la taille des caractères imprimés sur les emballages.</p>
</div>
</details>

<div class="nt-lab" id="lab-jet">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le déflecteur de l'imprimante</p>
<canvas style="height:260px;" aria-label="Gouttes d'encre déviées par le champ électrique du déflecteur, jusqu'au support d'impression"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Charge de la goutte $q$&nbsp;: <b class="out-q"></b><input type="range" data-p="q" min="0" max="6" step="0.1" value="4"></label>
<label class="nt-ctrl">Champ $E$&nbsp;: <b class="out-E"></b><input type="range" data-p="E" min="1" max="15" step="0.1" value="9"></label>
<label class="nt-ctrl">Vitesse $v_0$&nbsp;: <b class="out-v0"></b><input type="range" data-p="v0" min="10" max="30" step="1" value="20"></label>
</div>
<div class="nt-read" aria-live="polite"><span>H'I = <b class="out-hi"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-note">Avec les données de l'exercice ($q = \pu{-4E-13 C}$, $E = \pu{9E5 V*m-1}$, $v_0 = \pu{20 m*s-1}$), on retrouve H'I ≈ 3,6&nbsp;mm. En faisant varier la charge des gouttes, l'imprimante place chaque point à la hauteur voulue&nbsp;: c'est ainsi qu'elle «&nbsp;dessine&nbsp;» les caractères.</p>
</div>

## Aspect énergétique {.nt-h2}

<p class="nt-lead">On retrouve une utilisation du champ électrique uniforme d'un condensateur dans les <b>accélérateurs linéaires de particules chargées</b>. Comme leur nom l'indique, leur but est d'accélérer fortement une particule chargée (électron ou ion).</p>

<p class="nt-lead">Cette particule peut ensuite servir à une expérience de physique des particules ou en radiothérapie. Et en l'envoyant sur une cible, on crée des rayons X utilisés en imagerie médicale ou, là encore, en radiothérapie.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Imaginons qu'un électron est injecté sans vitesse initiale en A.</p>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 560 330" role="img" aria-label="Accélérateur linéaire : un électron entre sans vitesse en A dans la plaque négative et ressort en B par la plaque positive ; le champ électrique est orienté de B vers A"><rect x="110" y="60" width="14" height="110" fill="var(--blue)"/><rect x="110" y="190" width="14" height="110" fill="var(--blue)"/><rect x="420" y="60" width="14" height="110" fill="var(--rose)"/><rect x="420" y="190" width="14" height="110" fill="var(--rose)"/><text x="117" y="50" font-size="22" fill="var(--blue)" text-anchor="middle" font-weight="700">−</text><text x="427" y="50" font-size="22" fill="var(--rose)" text-anchor="middle" font-weight="700">+</text><line x1="340" y1="95" x2="228.0" y2="95.0" stroke="#059669" stroke-width="2" stroke-linecap="round"/><polygon points="220.0,95.0 230.0,90.0 230.0,100.0" fill="#059669"/><line x1="340" y1="140" x2="228.0" y2="140.0" stroke="#059669" stroke-width="2" stroke-linecap="round"/><polygon points="220.0,140.0 230.0,135.0 230.0,145.0" fill="#059669"/><line x1="340" y1="225" x2="228.0" y2="225.0" stroke="#059669" stroke-width="2" stroke-linecap="round"/><polygon points="220.0,225.0 230.0,220.0 230.0,230.0" fill="#059669"/><line x1="340" y1="270" x2="228.0" y2="270.0" stroke="#059669" stroke-width="2" stroke-linecap="round"/><polygon points="220.0,270.0 230.0,265.0 230.0,275.0" fill="#059669"/><text x="262" y="125" font-size="17" fill="#059669" font-family="Georgia, serif" font-style="italic" font-weight="700">E</text><line x1="262" y1="109" x2="271.35" y2="109" stroke="#059669" stroke-width="1.4"/><polygon points="274.4,109.0 269.4,111.6 269.4,106.4" fill="#059669"/><line x1="40" y1="180" x2="522.0" y2="180.0" stroke="var(--slate)" stroke-width="1.2" stroke-linecap="round"/><polygon points="530.0,180.0 520.0,185.0 520.0,175.0" fill="var(--slate)"/><text x="522" y="200" font-size="15" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">x</text><circle cx="117" cy="180" r="4" fill="var(--ink)"/><text x="100" y="200" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">A</text><circle cx="427" cy="180" r="4" fill="var(--ink)"/><text x="446" y="200" font-size="15" fill="var(--ink)" text-anchor="middle" font-weight="700">B</text><circle cx="170" cy="180" r="8" fill="var(--amber)"/><text x="178" y="164" font-size="12" fill="var(--amber)" text-anchor="middle" font-weight="700">électron</text><line x1="117" y1="316" x2="419.0" y2="316.0" stroke="var(--slate)" stroke-width="1.3" stroke-linecap="round"/><polygon points="427.0,316.0 417.0,321.0 417.0,311.0" fill="var(--slate)"/><line x1="427" y1="316" x2="125.0" y2="316.0" stroke="var(--slate)" stroke-width="1.3" stroke-linecap="round"/><polygon points="117.0,316.0 127.0,311.0 127.0,321.0" fill="var(--slate)"/><text x="272" y="310" font-size="16" fill="var(--slate)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">d</text><path d="M117,60 L117,20 L250,20" fill="none" stroke="var(--ink)" stroke-width="1.6"/><path d="M294,20 L427,20 L427,60" fill="none" stroke="var(--ink)" stroke-width="1.6"/><circle cx="272" cy="20" r="18" fill="#fff" stroke="var(--ink)" stroke-width="1.6"/><text x="272" y="25" font-size="14" fill="var(--ink)" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-weight="700">U</text></svg>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Rappel&nbsp;: théorème de l'énergie cinétique</p>
<p class="nt-f-math">$$\Delta E_c = E_{c\mathrm{B}} - E_{c\mathrm{A}} = \sum W_\mathrm{AB}(\vec{F}_\mathrm{ext})$$</p>
</div>

<p class="nt-lead">Si on néglige l'action de la gravité, la seule force extérieure est la force électrique, et le <b>théorème de l'énergie cinétique</b> nous dit que&nbsp;:</p>

<p class="nt-center">$\begin{aligned}\Delta E_c &= \sum W_\mathrm{AB}(\vec{F}_\mathrm{ext})\\ &=\overrightarrow{\mathrm{AB}}\cdot \vec{F}_e\\ &=-qEd\end{aligned}$</p>

<p class="nt-lead">Or $E=\dfrac Ud$. On obtient donc $E_{c\mathrm{B}}-E_{c\mathrm{A}}=-qU$. Et comme par hypothèse $v_\mathrm{A} = 0$&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vitesse en sortie de l'accélérateur</p>
<p class="nt-f-math">$$v_\mathrm{B}=\sqrt{\frac{-2qU}{m}}$$</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Application numérique</p>
<p>Pour une tension de $\pu{20,0 kV}$, on obtient une vitesse de&nbsp;:</p>
<p class="nt-center">$v_\mathrm{B} = \sqrt{\dfrac{-2\times (\pu{-1,60E-19 C})\times(\pu{20,0E3 V})}{\pu{9,11E-31 kg}}} = \pu{8,38E7 m*s-1}$</p>
</div>

<div class="nt-lab" id="lab-accel">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Jusqu'où peut-on accélérer un électron&nbsp;?</p>
<canvas style="height:260px;" aria-label="Vitesse de l'électron en fonction de la tension accélératrice, selon la mécanique de Newton et selon la relativité"></canvas>
<label class="nt-ctrl">Tension accélératrice $U$&nbsp;: <b class="out-U"></b><input type="range" min="0" max="500" step="0.5" value="20"></label>
<div class="nt-read" aria-live="polite"><span>Newton&nbsp;: <b class="out-vc"></b></span><span>relativité&nbsp;: <b class="out-vr"></b></span></div>
<p class="nt-note">À 20&nbsp;kV, l'électron atteint déjà plus du quart de la vitesse de la lumière $c$. Au-delà de quelques dizaines de kilovolts, la formule de Newton devient fausse&nbsp;: elle prédit même une vitesse supérieure à $c$ vers 256&nbsp;kV, ce qui est impossible.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Quand la mécanique de Newton ne suffit plus</span></summary>
<div class="nt-d-body">
<p>À 20&nbsp;kV, la relativité restreinte donne $v_\mathrm{B} \approx \pu{8,15E7 m*s-1}$ au lieu de $\pu{8,38E7 m*s-1}$&nbsp;: l'écart n'est encore que de 3&nbsp;%. Mais il grandit très vite avec la tension&nbsp;: aucun électron, quelle que soit la tension, ne peut atteindre la vitesse de la lumière. Dans les accélérateurs médicaux (quelques mégavolts), les électrons vont à plus de 99&nbsp;% de $c$, et c'est leur énergie, plus que leur vitesse, qui continue d'augmenter.</p>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CP = '#2A6BC4', CV = '#D97706', CA = '#059669', CF = '#E11D48';
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
  function arrow(c, x1, y1, x2, y2, color, w, dash) {
    var dx = x2 - x1, dy = y2 - y1, n = Math.hypot(dx, dy);
    if (n < 1) { return; }
    var ux = dx / n, uy = dy / n, L = Math.min(11, n * 0.45), W = L * 0.5;
    c.strokeStyle = color; c.fillStyle = color; c.lineWidth = w || 2.4; c.lineCap = 'round'; c.setLineDash(dash || []);
    c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2 - ux * L * 0.8, y2 - uy * L * 0.8); c.stroke(); c.setLineDash([]);
    c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - ux * L - uy * W, y2 - uy * L + ux * W); c.lineTo(x2 - ux * L + uy * W, y2 - uy * L - ux * W); c.closePath(); c.fill();
  }
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '700 12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.9)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  function vecLabel(c, s, x, y, color) {
    c.font = 'italic 700 15px Georgia, serif'; c.textAlign = 'center'; c.lineJoin = 'round'; c.lineCap = 'round';
    var w = c.measureText(s).width;
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.9)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
    c.strokeStyle = color; c.lineWidth = 1.3; c.beginPath();
    c.moveTo(x - w / 2, y - 14); c.lineTo(x + w / 2, y - 14); c.moveTo(x + w / 2, y - 14); c.lineTo(x + w / 2 - 4, y - 16.5); c.moveTo(x + w / 2, y - 14); c.lineTo(x + w / 2 - 4, y - 11.5); c.stroke();
  }
  /* boucle d'animation générique : f(dt) appelée à chaque image visible */
  function loop(cv, btn, f) {
    var st = { playing: !RM, visible: true, last: null };
    function step(ts) {
      var dt = st.last === null ? 0 : Math.min(0.05, (ts - st.last) / 1000); st.last = ts;
      if (st.visible) { f(st.playing ? dt : 0); }
      requestAnimationFrame(step);
    }
    if (btn) { playLabel(btn, st.playing); btn.addEventListener('click', function () { st.playing = !st.playing; playLabel(btn, st.playing); }); }
    watchVisible(cv, function (v) { st.visible = v; });
    requestAnimationFrame(step);
    return st;
  }
  /* ================= 1. g selon la latitude et l'altitude ================= */
  (function () {
    var root = document.getElementById('lab-g');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rL = $(root, '[data-p="lat"]'), rA = $(root, '[data-p="alt"]'), oL = $(root, '.out-lat'), oA = $(root, '.out-alt'), oG = $(root, '.out-g'), S;
    /* formule de Somigliana (ellipsoïde WGS 84) et correction d'altitude (air libre) */
    function g(lat, alt) {
      var s2 = Math.pow(Math.sin(lat * Math.PI / 180), 2);
      return 9.7803253359 * (1 + 0.00193185265241 * s2) / Math.sqrt(1 - 0.00669437999013 * s2) - 3.086e-6 * alt;
    }
    function draw() {
      var lat = +rL.value, alt = +rA.value, gv = g(lat, alt), c = S.ctx, w = S.w, h = S.h;
      oL.textContent = Math.round(lat) + '\u00b0'; oA.textContent = Math.round(alt).toLocaleString('fr-FR') + ' m'; oG.textContent = fr(gv, 4) + ' m\u00b7s\u207b\u00b2';
      c.clearRect(0, 0, w, h);
      /* coupe de la Terre (aplatissement exagéré) */
      var cx = w * 0.3, cy = h / 2, a = Math.min(w * 0.24, h * 0.42), b = a * 0.86, th = lat * Math.PI / 180;
      var gr = c.createRadialGradient(cx - a * 0.3, cy - b * 0.3, a * 0.1, cx, cy, a); gr.addColorStop(0, '#BFDBFE'); gr.addColorStop(1, '#60A5FA');
      c.fillStyle = gr; c.beginPath(); c.ellipse(cx, cy, a, b, 0, 0, 2 * Math.PI); c.fill();
      c.strokeStyle = 'rgba(255,255,255,.7)'; c.setLineDash([4, 4]); c.beginPath(); c.moveTo(cx - a, cy); c.lineTo(cx + a, cy); c.stroke(); c.setLineDash([]);
      txt(c, 'équateur', cx - a + 34, cy - 6, '#1E3A8A', '600 11px system-ui, sans-serif');
      txt(c, 'pôle Nord', cx, cy - b - 8, '#1E3A8A', '600 11px system-ui, sans-serif');
      /* point de la surface et normale sortante (perpendiculaire à l'ellipse) */
      var px = cx + a * Math.cos(th), py = cy - b * Math.sin(th);
      var nxo = Math.cos(th) / a, nyo = -Math.sin(th) / b, nno = Math.hypot(nxo, nyo); nxo /= nno; nyo /= nno;
      var hgt = alt / 9000 * 0.16 * a, qx = px + nxo * hgt, qy = py + nyo * hgt;
      if (alt > 0) {   /* montagne : petit triangle posé sur la surface */
        var tx = -nyo, ty = nxo, base = Math.max(8, hgt * 0.7);
        c.fillStyle = '#A16207'; c.beginPath(); c.moveTo(px + tx * base, py + ty * base); c.lineTo(qx, qy); c.lineTo(px - tx * base, py - ty * base); c.closePath(); c.fill();
      }
      /* vecteur g : du point vers l'intérieur, dessiné par-dessus la montagne */
      var L = 44 + (gv - 9.76) * 900;
      arrow(c, qx, qy, qx - nxo * L, qy - nyo * L, CA, 3.2);
      c.fillStyle = CF; c.beginPath(); c.arc(qx, qy, 5, 0, 2 * Math.PI); c.fill();
      /* étiquette décalée sur le côté de la flèche */
      vecLabel(c, 'g', qx - nxo * L * 0.55 - nyo * 16, qy - nyo * L * 0.55 + nxo * 16 + 6, CA);
      c.font = '10px system-ui, sans-serif'; c.fillStyle = col('--muted'); c.textAlign = 'center'; c.fillText('aplatissement exagéré', cx, cy + b + 18);
      /* échelle de g */
      var L0 = w * 0.62, R0 = w - 30, gmin = 9.75, gmax = 9.84, yb = h / 2;
      function X(v) { return L0 + (v - gmin) / (gmax - gmin) * (R0 - L0); }
      c.strokeStyle = col('--ink'); c.lineWidth = 1.5; c.beginPath(); c.moveTo(L0, yb); c.lineTo(R0, yb); c.stroke();
      [9.76, 9.78, 9.80, 9.82, 9.84].forEach(function (v) { c.beginPath(); c.moveTo(X(v), yb - 5); c.lineTo(X(v), yb + 5); c.stroke(); txt(c, fr(v, 2), X(v), yb + 20, col('--muted'), '11px system-ui, sans-serif'); });
      [['équateur', g(0, 0)], ['pôles', g(90, 0)]].forEach(function (q, i) { c.fillStyle = col('--muted'); c.beginPath(); c.arc(X(q[1]), yb, 3.5, 0, 2 * Math.PI); c.fill(); txt(c, q[0], X(q[1]), yb - (i ? 28 : 14), col('--slate'), '600 11px system-ui, sans-serif'); });
      c.fillStyle = CA; c.beginPath(); c.arc(X(gv), yb, 7, 0, 2 * Math.PI); c.fill();
      txt(c, 'g (m\u00b7s\u207b\u00b2)', (L0 + R0) / 2, yb + 42, col('--slate'), '600 11px system-ui, sans-serif');
    }
    [rL, rA].forEach(function (r) { r.addEventListener('input', draw); });
    $$(root, '[data-preset]').forEach(function (b) { b.addEventListener('click', function () { var v = b.getAttribute('data-preset').split(','); rL.value = v[0]; rA.value = v[1]; draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 2. Le champ devient uniforme quand on zoome ================= */
  (function () {
    var root = document.getElementById('lab-zoom');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rZ = $(root, 'input[type="range"]'), oW = $(root, '.out-w'), oD = $(root, '.out-dir'), oN = $(root, '.out-norm'), S, R = 6371;
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, z = +rZ.value, W = Math.max(3.2 * R, 2.7 * R * w / h) * Math.pow(10, -z), H = W * h / w;   /* au départ, toute la Terre est visible */
      /* au départ, la Terre entière est centrée ; en zoomant, la fenêtre glisse vers un point de la surface */
      var f = 1 - Math.exp(-2.5 * z), cx0 = 0, cy0 = f * (R + H * 0.25);
      function X(x) { return w / 2 + (x - cx0) / W * w; }
      function Y(y) { return h / 2 - (y - cy0) / W * w; }
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#E0F2FE'; c.fillRect(0, 0, w, h);
      var rpx = R / W * w;
      c.fillStyle = '#86EFAC'; c.beginPath(); c.arc(X(0), Y(0), rpx, 0, 2 * Math.PI); c.fill();
      c.strokeStyle = '#16A34A'; c.lineWidth = 2; c.stroke();
      var nx = 9, ny = 6, maxDir = 0, gmin = 1e9, gmax = 0;
      for (var i = 0; i < nx; i++) {
        for (var j = 0; j < ny; j++) {
          var sx = (i + 0.5) / nx * w, sy = (j + 0.5) / ny * h;
          var x = cx0 + (sx - w / 2) / w * W, y = cy0 - (sy - h / 2) / w * W, r = Math.hypot(x, y);
          if (r < R) { continue; }
          var gr = Math.pow(R / r, 2), L = 30 * gr, ux = -x / r, uy = -y / r;
          maxDir = Math.max(maxDir, Math.abs(Math.atan2(ux, -uy))); gmin = Math.min(gmin, gr); gmax = Math.max(gmax, gr);
          arrow(c, sx, sy, sx + ux * L, sy - uy * L, CA, 2);
        }
      }
      oW.textContent = W >= 10 ? Math.round(W).toLocaleString('fr-FR') + ' km' : fr(W * 1000, 0) + ' m';
      oD.textContent = fr(2 * maxDir * 180 / Math.PI, maxDir > 0.05 ? 0 : 2) + '\u00b0';
      oN.textContent = gmax > 0 ? fr((gmax - gmin) / gmax * 100, (gmax - gmin) / gmax > 0.1 ? 0 : 2) + ' %' : '\u2014';
    }
    rZ.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 3. La chute libre ================= */
  var G = 9.81;
  function traj(v0, al, h) {
    var vx = v0 * Math.cos(al), vz = v0 * Math.sin(al), T = (vz + Math.sqrt(vz * vz + 2 * G * h)) / G;
    return { vx: vx, vz: vz, T: T, P: function (t) { return [vx * t, -0.5 * G * t * t + vz * t + h]; } };
  }
  (function () {
    var root = document.getElementById('lab-chute');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rV = $(root, '[data-p="v0"]'), rA = $(root, '[data-p="al"]'), rH = $(root, '[data-p="h"]'), rM = $(root, '[data-p="m"]'), btn = $(root, '[data-act="play"]');
    var oV = $(root, '.out-v0'), oA = $(root, '.out-al'), oH = $(root, '.out-h'), oM = $(root, '.out-m'), oX = $(root, '.out-x'), oZ = $(root, '.out-z'), oT = $(root, '.out-t'), S, t = 0;
    function draw(dt) {
      if (!S) { return; }
      var v0 = +rV.value, al = +rA.value * Math.PI / 180, h = +rH.value, tr = traj(v0, al, h);
      oV.textContent = fr(v0, 1) + ' m\u00b7s\u207b\u00b9'; oA.textContent = Math.round(+rA.value) + '\u00b0'; oH.textContent = fr(h, 1) + ' m'; oM.textContent = fr(+rM.value, 1) + ' kg';
      var zmax = h + (tr.vz > 0 ? tr.vz * tr.vz / (2 * G) : 0), xmax = tr.vx * tr.T;
      oX.textContent = fr(xmax, 2) + ' m'; oZ.textContent = fr(zmax, 2) + ' m'; oT.textContent = fr(tr.T, 2) + ' s';
      t += dt * 0.6; var tc = t % (tr.T + 1.0), ts = Math.min(tc, tr.T);
      /* cadrage adapté à la trajectoire (même échelle sur les deux axes) */
      var c = S.ctx, w = S.w, hh = S.h, WX = Math.max(6, xmax * 1.12 + 1), WZ = Math.max(3, zmax * 1.25 + 0.5), k = Math.min((w - 40) / WX, (hh - 30) / WZ);
      function X(x) { return 30 + x * k; }
      function Y(z) { return hh - 20 - z * k; }
      c.clearRect(0, 0, w, hh);
      c.fillStyle = '#F1F5F9'; c.fillRect(0, Y(0), w, hh - Y(0));
      c.strokeStyle = col('--muted'); c.lineWidth = 1;
      var stp = WX > 30 ? 10 : (WX > 12 ? 5 : 1);
      for (var gx = 0; gx <= WX; gx += stp) { c.beginPath(); c.moveTo(X(gx), Y(0)); c.lineTo(X(gx), Y(0) + 5); c.stroke(); txt(c, gx + ' m', X(gx), Y(0) + 16, col('--muted'), '10px system-ui, sans-serif'); }
      c.strokeStyle = 'rgba(42,107,196,.35)'; c.setLineDash([5, 4]); c.lineWidth = 1.5; c.beginPath();
      for (var s = 0; s <= tr.T + 1e-9; s += tr.T / 120) { var p = tr.P(s); if (s === 0) { c.moveTo(X(p[0]), Y(p[1])); } else { c.lineTo(X(p[0]), Y(p[1])); } }
      c.stroke(); c.setLineDash([]);
      for (var s2 = 0; s2 <= ts + 1e-9; s2 += 0.1) { var q = tr.P(s2); c.fillStyle = 'rgba(42,107,196,.55)'; c.beginPath(); c.arc(X(q[0]), Y(q[1]), 2.8, 0, 2 * Math.PI); c.fill(); }
      var P = tr.P(ts), px = X(P[0]), py = Y(P[1]), vz = tr.vz - G * ts;
      c.fillStyle = '#F97316'; c.beginPath(); c.arc(px, py, 7, 0, 2 * Math.PI); c.fill();
      var KV = 0.32 * k;
      arrow(c, px, py, px + tr.vx * KV, py - vz * KV, CV, 2.8); vecLabel(c, 'v', px + tr.vx * KV + 10, py - vz * KV - 6, CV);
      arrow(c, px, py, px, py + G * 0.12 * k, CA, 2.8); vecLabel(c, 'a', px + 14, py + G * 0.12 * k, CA);
    }
    [rV, rA, rH, rM].forEach(function (r) { r.addEventListener('input', function () { t = 0; draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    setup(); onResize(setup); loop(cv, btn, draw);
  })();
  /* ================= 4. Le service au volley ================= */
  (function () {
    var root = document.getElementById('lab-volley');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rV = $(root, 'input[type="range"]'), oV = $(root, '.out-v0'), msg = $(root, '.nt-msg'), btn = $(root, '[data-act="play"]'), S, t = 0;
    var Hh = 3.5, Hn = 2.40, Lc = 18, rb = 0.10;
    function draw(dt) {
      if (!S) { return; }
      var v0 = +rV.value; oV.textContent = fr(v0, 1) + ' m\u00b7s\u207b\u00b9';
      function z(x) { return -G / (2 * v0 * v0) * x * x + Hh; }
      var zNet = z(Lc / 2), xs = v0 * Math.sqrt(2 * (Hh - rb) / G), ok1 = zNet > Hn + rb, ok2 = xs < Lc;
      var xEnd = ok1 ? xs : Lc / 2 - rb;
      var c = S.ctx, w = S.w, h = S.h, k = Math.min((w - 40) / 22, (h - 40) / 4.4);
      function X(x) { return 24 + x * k; }
      function Y(y) { return h - 24 - y * k; }
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#FDE68A'; c.fillRect(X(0), Y(0), Lc * k, 6); c.fillStyle = '#E2E8F0'; c.fillRect(X(Lc), Y(0), w, 6);
      c.strokeStyle = col('--ink'); c.lineWidth = 3; c.beginPath(); c.moveTo(X(Lc / 2), Y(0)); c.lineTo(X(Lc / 2), Y(Hn)); c.stroke();
      c.strokeStyle = 'rgba(30,41,59,.35)'; c.lineWidth = 1; for (var nt = 0.95; nt < Hn; nt += 0.15) { c.beginPath(); c.moveTo(X(Lc / 2) - 3, Y(nt)); c.lineTo(X(Lc / 2) + 3, Y(nt)); c.stroke(); }
      txt(c, 'filet (2,40 m)', X(Lc / 2), Y(Hn) - 8, col('--ink'));
      txt(c, 'fin du terrain', X(Lc), Y(0) + 18, col('--slate'));
      txt(c, '0', X(0), Y(0) + 18, col('--slate'));
      var good = ok1 && ok2, colr = good ? '#16A34A' : CF;
      c.strokeStyle = colr; c.setLineDash([6, 4]); c.lineWidth = 2; c.beginPath();
      for (var x = 0; x <= xEnd + 1e-9; x += 0.1) { if (x === 0) { c.moveTo(X(x), Y(z(x))); } else { c.lineTo(X(x), Y(z(x))); } }
      c.stroke(); c.setLineDash([]);
      t += dt; var T = xEnd / v0, ts = Math.min(t % (T + 1.2), T), xb = v0 * ts;
      c.fillStyle = '#F8FAFC'; c.strokeStyle = '#1D4ED8'; c.lineWidth = 2; c.beginPath(); c.arc(X(xb), Y(z(xb)), Math.max(5, rb * k), 0, 2 * Math.PI); c.fill(); c.stroke();
      c.strokeStyle = col('--slate'); c.lineWidth = 1; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(X(0), Y(0)); c.lineTo(X(0), Y(Hh)); c.stroke(); c.setLineDash([]);
      txt(c, 'h = 3,50 m', X(0) + 6, Y(Hh) - 10, col('--slate'), '600 11px system-ui, sans-serif', 'left');
      msg.textContent = !ok1 ? 'Le ballon est trop lent : il touche le filet (hauteur au niveau du filet : ' + fr(zNet, 2) + ' m, il faudrait plus de 2,50 m).'
        : (!ok2 ? 'Le ballon passe le filet mais sort du terrain : il touche le sol à ' + fr(xs, 1) + ' m du serveur (plus de 18 m).'
          : 'Service réussi : le ballon passe le filet (centre à ' + fr(zNet, 2) + ' m) et retombe à ' + fr(xs, 1) + ' m, dans le terrain.');
    }
    rV.addEventListener('input', function () { t = 0; draw(0); });
    function setup() { S = canvasCtx(cv); draw(0); }
    setup(); onResize(setup); loop(cv, btn, draw);
  })();
  /* ================= 5. Énergies au cours de la chute libre ================= */
  (function () {
    var root = document.getElementById('lab-energie');
    if (!root) { return; }
    var cv = $(root, 'canvas.scene'), cvG = $(root, 'canvas.graph'), rV = $(root, '[data-p="v0"]'), rA = $(root, '[data-p="al"]'), btn = $(root, '[data-act="play"]');
    var oV = $(root, '.out-v0'), oA = $(root, '.out-al'), S, SG, t = 0, M = 0.60, H0 = 2.0, CE = '#D97706', CPP = '#2A6BC4', CM = '#E11D48';
    function draw(dt) {
      if (!S) { return; }
      var v0 = +rV.value, al = +rA.value * Math.PI / 180, tr = traj(v0, al, H0);
      oV.textContent = fr(v0, 1) + ' m\u00b7s\u207b\u00b9'; oA.textContent = Math.round(+rA.value) + '\u00b0';
      t += dt * 0.6; var ts = Math.min(t % (tr.T + 1.0), tr.T);
      function En(s) { var p = tr.P(s), vz = tr.vz - G * s, v2 = tr.vx * tr.vx + vz * vz; return [0.5 * M * v2, M * G * p[1]]; }
      var Em = En(0)[0] + En(0)[1], e = En(ts);
      /* scène + barres */
      var c = S.ctx, w = S.w, h = S.h, sw = w * 0.64, k = Math.min((sw - 30) / 16, (h - 30) / 8);
      function X(x) { return 20 + x * k; }
      function Y(y) { return h - 16 - y * k; }
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#F1F5F9'; c.fillRect(0, Y(0), sw, h - Y(0));
      c.strokeStyle = 'rgba(42,107,196,.3)'; c.setLineDash([5, 4]); c.lineWidth = 1.5; c.beginPath();
      for (var s = 0; s <= tr.T + 1e-9; s += tr.T / 100) { var p = tr.P(s); if (s === 0) { c.moveTo(X(p[0]), Y(p[1])); } else { c.lineTo(X(p[0]), Y(p[1])); } }
      c.stroke(); c.setLineDash([]);
      var P = tr.P(ts); c.fillStyle = '#F97316'; c.beginPath(); c.arc(X(P[0]), Y(P[1]), 8, 0, 2 * Math.PI); c.fill();
      var bx = sw + 30, bw = (w - bx - 20) / 3 - 10, bb = h - 34, bt = 20;
      [[e[0], CE, 'Ec'], [e[1], CPP, 'Epp'], [Em, CM, 'Em']].forEach(function (q, i) {
        var x = bx + i * (bw + 10), hgt = q[0] / Em * (bb - bt) * 0.95;
        c.fillStyle = '#E2E8F0'; c.fillRect(x, bt, bw, bb - bt);
        c.fillStyle = q[1]; c.fillRect(x, bb - hgt, bw, hgt);
        txt(c, q[2], x + bw / 2, bb + 16, q[1], '700 13px system-ui, sans-serif');
        txt(c, Math.round(q[0]) + ' J', x + bw / 2, bb - hgt - 6, q[1], '600 11px system-ui, sans-serif');
      });
      /* graphe en fonction du temps */
      var g = SG.ctx, W = SG.w, HG = SG.h, L = 46, R = W - 12, T = 10, B = HG - 26;
      function GX(s) { return L + s / tr.T * (R - L); }
      function GY(v) { return B - v / (Em * 1.08) * (B - T); }
      g.clearRect(0, 0, W, HG);
      g.strokeStyle = col('--line'); g.lineWidth = 1; g.beginPath(); g.moveTo(L, T); g.lineTo(L, B); g.lineTo(R, B); g.stroke();
      txt(g, 'temps \u2192', (L + R) / 2, HG - 6, col('--muted'), '11px system-ui, sans-serif');
      txt(g, 'énergie (J)', L + 34, T + 10, col('--muted'), '11px system-ui, sans-serif');
      [[0, CE], [1, CPP]].forEach(function (q) {
        g.strokeStyle = q[1]; g.lineWidth = 2.2; g.beginPath();
        for (var s3 = 0; s3 <= tr.T + 1e-9; s3 += tr.T / 100) { var v = En(s3)[q[0]]; if (s3 === 0) { g.moveTo(GX(s3), GY(v)); } else { g.lineTo(GX(s3), GY(v)); } }
        g.stroke();
      });
      g.strokeStyle = CM; g.lineWidth = 2.2; g.beginPath(); g.moveTo(GX(0), GY(Em)); g.lineTo(GX(tr.T), GY(Em)); g.stroke();
      g.strokeStyle = 'rgba(30,41,59,.4)'; g.setLineDash([3, 3]); g.beginPath(); g.moveTo(GX(ts), T); g.lineTo(GX(ts), B); g.stroke(); g.setLineDash([]);
    }
    [rV, rA].forEach(function (r) { r.addEventListener('input', function () { t = 0; draw(0); }); });
    function setup() { S = canvasCtx(cv); SG = canvasCtx(cvG); draw(0); }
    setup(); onResize(setup); loop(cv, btn, draw);
  })();
  /* ================= 6. Le condensateur plan ================= */
  (function () {
    var root = document.getElementById('lab-condo');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rU = $(root, '[data-p="U"]'), rD = $(root, '[data-p="d"]'), cbI = $(root, '[data-p="inv"]'), oU = $(root, '.out-U'), oD = $(root, '.out-d'), oE = $(root, '.out-E'), S;
    function draw() {
      var U = +rU.value, d = +rD.value / 100, E = U / d, inv = cbI.checked, c = S.ctx, w = S.w, h = S.h;
      oU.textContent = U + ' V'; oD.textContent = fr(d * 100, 1) + ' cm'; oE.innerHTML = Math.round(E).toLocaleString('fr-FR') + ' V\u00b7m<sup>\u22121</sup>';
      c.clearRect(0, 0, w, h);
      var gap = d / 0.10 * (w * 0.55), x1 = w / 2 - gap / 2, x2 = w / 2 + gap / 2, top = 30, bot = h - 30;
      var cl = inv ? '#2A6BC4' : '#E11D48', cr = inv ? '#E11D48' : '#2A6BC4';
      c.fillStyle = cl; c.fillRect(x1 - 12, top, 12, bot - top); c.fillStyle = cr; c.fillRect(x2, top, 12, bot - top);
      var nq = Math.max(2, Math.min(14, Math.round(E / 900)));
      for (var i = 0; i < nq; i++) {
        var y = top + (i + 0.5) / nq * (bot - top);
        c.fillStyle = '#fff'; c.font = '700 13px system-ui, sans-serif'; c.textAlign = 'center';
        c.fillText(inv ? '\u2212' : '+', x1 - 6, y + 4); c.fillText(inv ? '+' : '\u2212', x2 + 6, y + 4);
      }
      var Lr = Math.min(gap * 0.5, 14 + E / 450), dir = inv ? -1 : 1;
      for (var j = 0; j < 6; j++) {
        var yy = top + (j + 0.5) / 6 * (bot - top);
        c.strokeStyle = 'rgba(5,150,105,.25)'; c.lineWidth = 1; c.beginPath(); c.moveTo(x1, yy); c.lineTo(x2, yy); c.stroke();
        for (var m = 0; m < 2; m++) { var xm = x1 + (m + 0.5) / 2 * gap; arrow(c, xm - dir * Lr / 2, yy, xm + dir * Lr / 2, yy, CA, 2.2); }
      }
      vecLabel(c, 'E', w / 2, top + (bot - top) / 12 + 22, CA);
      txt(c, 'champ uniforme entre les plaques', w / 2, h - 8, col('--slate'), '600 11px system-ui, sans-serif');
    }
    [rU, rD].forEach(function (r) { r.addEventListener('input', draw); }); cbI.addEventListener('change', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 7. L'imprimante à jet d'encre ================= */
  (function () {
    var root = document.getElementById('lab-jet');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rQ = $(root, '[data-p="q"]'), rE = $(root, '[data-p="E"]'), rV = $(root, '[data-p="v0"]'), btn = $(root, '[data-act="play"]');
    var oQ = $(root, '.out-q'), oE = $(root, '.out-E'), oV = $(root, '.out-v0'), oI = $(root, '.out-hi'), S, t = 0;
    var m = 2e-10, Lm = 0.02, Dm = 0.03;
    function draw(dt) {
      if (!S) { return; }
      var q = -(+rQ.value) * 1e-13, E = +rE.value * 1e5, v0 = +rV.value;
      oQ.innerHTML = q === 0 ? '0 C (goutte non chargée)' : sci(q, 1) + ' C'; oE.innerHTML = sci(E, 1) + ' V\u00b7m<sup>\u22121</sup>'; oV.textContent = v0 + ' m\u00b7s\u207b\u00b9';
      var K = -q * E / m;   /* accélération verticale (vers le haut si q < 0) */
      var tS = Lm / v0, zS = 0.5 * K * tS * tS, tana = K * Lm / (v0 * v0), zI = zS + tana * Dm;
      oI.textContent = fr(zI * 1000, 2) + ' mm';
      var c = S.ctx, w = S.w, h = S.h, k = (w - 80) / 0.055;   /* px par mètre (même échelle sur les deux axes) */
      var xO = 40, yO = h * 0.62;
      function X(x) { return xO + x * k; }
      function Y(z) { return yO - z * k; }
      c.clearRect(0, 0, w, h);
      c.fillStyle = 'rgba(226,232,240,.6)'; c.fillRect(X(0), Y(0.006), Lm * k, 0.012 * k);
      c.fillStyle = '#E11D48'; c.fillRect(X(0), Y(0.006) - 6, Lm * k, 6); c.fillStyle = '#2A6BC4'; c.fillRect(X(0), Y(-0.006), Lm * k, 6);
      txt(c, 'P\u2081', X(Lm) + 14, Y(0.006), '#E11D48', '700 12px system-ui, sans-serif'); txt(c, 'P\u2082', X(Lm) + 14, Y(-0.006) + 10, '#2A6BC4', '700 12px system-ui, sans-serif');
      c.strokeStyle = col('--muted'); c.setLineDash([4, 4]); c.lineWidth = 1; c.beginPath(); c.moveTo(0, yO); c.lineTo(w, yO); c.stroke(); c.setLineDash([]);
      c.strokeStyle = col('--ink'); c.lineWidth = 4; c.beginPath(); c.moveTo(X(Lm + Dm), 10); c.lineTo(X(Lm + Dm), h - 10); c.stroke();
      txt(c, 'support', X(Lm + Dm) + 4, 22, col('--ink'), '600 11px system-ui, sans-serif', 'left');
      /* trajectoire : parabole dans le déflecteur, droite ensuite */
      function z(x) { return x <= Lm ? 0.5 * K * Math.pow(x / v0, 2) : zS + tana * (x - Lm); }
      c.strokeStyle = CP; c.lineWidth = 2.2; c.beginPath();
      for (var x = 0; x <= Lm + Dm + 1e-9; x += (Lm + Dm) / 200) { var zz = Math.min(z(x), 0.02); if (x === 0) { c.moveTo(X(x), Y(zz)); } else { c.lineTo(X(x), Y(zz)); } }
      c.stroke();
      /* gouttes : une sur deux est chargée */
      t += dt;
      for (var i = 0; i < 8; i++) {
        var u = ((t * 0.35 + i / 8) % 1), xd = u * (Lm + Dm), charged = i % 2 === 0;
        var zd = charged ? z(xd) : 0;
        if (Math.abs(zd) > 0.02) { continue; }
        c.fillStyle = charged ? CP : 'rgba(100,116,139,.6)'; c.beginPath(); c.arc(X(xd), Y(zd), 4, 0, 2 * Math.PI); c.fill();
      }
      c.fillStyle = col('--ink'); c.beginPath(); c.arc(X(Lm + Dm), Y(Math.min(zI, 0.02)), 4, 0, 2 * Math.PI); c.fill();
      txt(c, 'I', X(Lm + Dm) - 10, Y(Math.min(zI, 0.02)) - 6, col('--ink'), 'italic 700 13px Georgia, serif');
      txt(c, 'gouttes non chargées \u2192 gouttière', X(Lm + Dm) - 8, yO + 18, col('--slate'), '600 11px system-ui, sans-serif', 'right');
      vecLabel(c, 'E', X(Lm * 0.15), Y(0.003) + 6, CA); arrow(c, X(Lm * 0.15) + 14, Y(0.004), X(Lm * 0.15) + 14, Y(-0.003), CA, 2);
    }
    [rQ, rE, rV].forEach(function (r) { r.addEventListener('input', function () { draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    setup(); onResize(setup); loop(cv, btn, draw);
  })();
  /* ================= 8. Accélérer un électron ================= */
  (function () {
    var root = document.getElementById('lab-accel');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rU = $(root, 'input[type="range"]'), oU = $(root, '.out-U'), oC = $(root, '.out-vc'), oR = $(root, '.out-vr'), S;
    var e = 1.602e-19, me = 9.109e-31, c0 = 2.998e8, UMAX = 500e3;
    function vc(U) { return Math.sqrt(2 * e * U / me); }
    function vr(U) { var gm = 1 + e * U / (me * c0 * c0); return c0 * Math.sqrt(1 - 1 / (gm * gm)); }
    function draw() {
      var U = +rU.value * 1e3, c = S.ctx, w = S.w, h = S.h, L = 56, R = w - 14, T = 12, B = h - 32;
      oU.textContent = fr(U / 1e3, 1) + ' kV'; oC.innerHTML = sci(vc(U), 2) + ' m\u00b7s\u207b\u00b9 (' + fr(vc(U) / c0, 2) + ' c)'; oR.innerHTML = sci(vr(U), 2) + ' m\u00b7s\u207b\u00b9 (' + fr(vr(U) / c0, 2) + ' c)';
      function X(u) { return L + u / UMAX * (R - L); }
      function Y(v) { return B - v / (1.6 * c0) * (B - T); }
      c.clearRect(0, 0, w, h);
      c.strokeStyle = col('--ink'); c.lineWidth = 1; c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
      c.strokeStyle = col('--muted'); c.setLineDash([5, 4]); c.beginPath(); c.moveTo(L, Y(c0)); c.lineTo(R, Y(c0)); c.stroke(); c.setLineDash([]);
      txt(c, 'c (vitesse de la lumière)', R - 4, Y(c0) - 6, col('--slate'), '600 11px system-ui, sans-serif', 'right');
      [[0, '0'], [0.5, '0,5 c'], [1, 'c'], [1.5, '1,5 c']].forEach(function (q) { txt(c, q[1], L - 6, Y(q[0] * c0) + 4, col('--muted'), '10px system-ui, sans-serif', 'right'); });
      txt(c, 'vitesse', L + 4, T + 10, col('--muted'), '11px system-ui, sans-serif', 'left');
      [0, 100, 200, 300, 400, 500].forEach(function (u) { txt(c, u + ' kV', X(u * 1e3), B + 14, col('--muted'), '10px system-ui, sans-serif'); });
      txt(c, 'tension accélératrice U', (L + R) / 2, h - 3, col('--muted'), '11px system-ui, sans-serif');
      [[vc, CV, 'mécanique de Newton'], [vr, CP, 'relativité restreinte']].forEach(function (f, i) {
        c.strokeStyle = f[1]; c.lineWidth = 2.4; c.beginPath();
        for (var u = 0; u <= UMAX; u += UMAX / 200) { var v = Math.min(f[0](u), 1.6 * c0); if (u === 0) { c.moveTo(X(u), Y(v)); } else { c.lineTo(X(u), Y(v)); } }
        c.stroke(); txt(c, f[2], X(UMAX * (i ? 0.75 : 0.42)), Y(Math.min(f[0](UMAX * (i ? 0.75 : 0.42)), 1.55 * c0)) + (i ? 18 : -8), f[1], '700 11px system-ui, sans-serif');
        c.fillStyle = f[1]; c.beginPath(); c.arc(X(U), Y(Math.min(f[0](U), 1.6 * c0)), 5, 0, 2 * Math.PI); c.fill();
      });
    }
    rU.addEventListener('input', draw);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
})();
</script>
