+++
title = "Écoulement d'un fluide"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Fluide incompressible {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définitions</p>
<p>Un <span class="imp">fluide</span> est un <span class="imp nt-hole">liquide</span> ou un <span class="imp nt-hole">gaz</span>.</p>
<p>Un <span class="imp">fluide incompressible</span> est un fluide dont la <span class="imp nt-hole">masse volumique</span> est <span class="imp nt-hole">constante</span>&nbsp;: $\rho=\mathrm{cte}$.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Le modèle nécessite une température constante et homogène dans le fluide. Les vitesses d'écoulement doivent aussi être petites devant la célérité des ondes sonores dans le fluide ($v\ll c_\mathrm{son}$). Ainsi, même l'air peut être considéré comme incompressible pour des vitesses de quelques dizaines de mètres par seconde.</p>
</div>

## Poussée d'Archimède {.nt-h2}

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Rappel&nbsp;: force pressante</p>
<p class="nt-f-math">$$F = P\times S$$</p>
<div class="nt-f-units"><span>$F$, force pressante exercée par un fluide sur une surface plane, en <b>$\pu{N}$</b></span><span>$P$, pression du fluide, en <b>$\pu{Pa}$</b></span><span>$S$, aire de la surface, en <b>$\pu{m2}$</b></span><span>direction&nbsp;: perpendiculaire à la surface, dirigée vers elle</span></div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un corps plongé dans un fluide incompressible au repos reçoit une force opposée au <span class="imp nt-hole">poids du fluide déplacé</span>. C'est la <span class="imp">poussée d'Archimède</span>, notée $\vec{\pi}_\mathrm{A}$.</p>
<p>Cette action est la <span class="imp nt-hole">résultante des forces de pression</span> du fluide sur le corps. Elle est non nulle à cause de la pesanteur, qui rend la pression plus grande en profondeur.</p>
</div>

<p class="nt-lead">Calculons la résultante des forces de pression sur un cylindre vertical de hauteur $h$ et de section $S$, immergé dans un fluide incompressible au repos de masse volumique $\rho$.</p>

<svg class="nt-svg nt-svg-m" viewBox="0 0 640 396" role="img" aria-label="Cylindre vertical immergé : les forces de pression latérales se compensent ; la force sur la face du bas, plus profonde, est plus grande que celle sur la face du haut"><defs><linearGradient id="gEau" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#DBEAFE"/><stop offset="1" stop-color="#60A5FA"/></linearGradient><linearGradient id="gCyl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#CBD5E1"/><stop offset=".5" stop-color="#F8FAFC"/><stop offset="1" stop-color="#94A3B8"/></linearGradient><linearGradient id="gP" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBCFE8"/><stop offset="1" stop-color="#BE185D"/></linearGradient></defs><rect x="0" y="20" width="640" height="376" fill="url(#gEau)"/><line x1="60" y1="360" x2="60" y2="40" stroke="#1E293B" stroke-width="1.6"/><polygon points="60.0,34.0 65.0,44.0 55.0,44.0" fill="#1E293B"/><text x="68" y="44" font-size="16" fill="#1E293B" font-family="Georgia, serif" font-style="italic">z</text><line x1="60.0" y1="360.0" x2="60.0" y2="328.0" stroke="#CA8A04" stroke-width="2.4" stroke-linecap="round"/><polygon points="60.0,320.0 65.0,330.0 55.0,330.0" fill="#CA8A04"/><text x="70" y="330" font-size="15" fill="#CA8A04" font-family="Georgia, serif" font-style="italic" font-weight="500">k</text><line x1="70" y1="316" x2="78.25" y2="316" stroke="#CA8A04" stroke-width="1.3"/><polygon points="81.2,316.0 76.2,318.6 76.2,313.4" fill="#CA8A04"/><line x1="280.0" y1="340.0" x2="280.0" y2="284.0" stroke="#E11D48" stroke-width="2.6" stroke-linecap="round"/><polygon points="280.0,276.0 285.0,286.0 275.0,286.0" fill="#E11D48"/><path d="M190,110 L190,270 A90,22 0 0 0 370,270 L370,110 Z" fill="url(#gCyl)" fill-opacity=".88"/><ellipse cx="280" cy="110" rx="90" ry="22" fill="#F1F5F9" stroke="#94A3B8"/><ellipse cx="280" cy="270" rx="90" ry="22" fill="none" stroke="#94A3B8" stroke-dasharray="4 4"/><text x="280" y="116" font-size="15" text-anchor="middle" fill="#475569" font-family="Georgia, serif" font-style="italic">S</text><line x1="50" y1="110" x2="190" y2="110" stroke="#475569" stroke-dasharray="3 4" stroke-width=".8"/><line x1="50" y1="270" x2="190" y2="270" stroke="#475569" stroke-dasharray="3 4" stroke-width=".8"/><text x="44" y="114" font-size="14" text-anchor="end" fill="#1E293B" font-family="Georgia, serif" font-style="italic">z₀ + h</text><text x="44" y="274" font-size="14" text-anchor="end" fill="#1E293B" font-family="Georgia, serif" font-style="italic">z₀</text><line x1="118" y1="110" x2="118" y2="270" stroke="#1E293B"/><text x="110" y="196" font-size="15" text-anchor="end" fill="#1E293B" font-family="Georgia, serif" font-style="italic">h</text><line x1="156.0" y1="140.0" x2="182.0" y2="140.0" stroke="#E11D48" stroke-width="2.2" stroke-linecap="round"/><polygon points="190.0,140.0 180.0,145.0 180.0,135.0" fill="#E11D48"/><line x1="404.0" y1="140.0" x2="378.0" y2="140.0" stroke="#E11D48" stroke-width="2.2" stroke-linecap="round"/><polygon points="370.0,140.0 380.0,135.0 380.0,145.0" fill="#E11D48"/><line x1="146.0" y1="190.0" x2="182.0" y2="190.0" stroke="#E11D48" stroke-width="2.2" stroke-linecap="round"/><polygon points="190.0,190.0 180.0,195.0 180.0,185.0" fill="#E11D48"/><line x1="414.0" y1="190.0" x2="378.0" y2="190.0" stroke="#E11D48" stroke-width="2.2" stroke-linecap="round"/><polygon points="370.0,190.0 380.0,185.0 380.0,195.0" fill="#E11D48"/><line x1="136.0" y1="240.0" x2="182.0" y2="240.0" stroke="#E11D48" stroke-width="2.2" stroke-linecap="round"/><polygon points="190.0,240.0 180.0,245.0 180.0,235.0" fill="#E11D48"/><line x1="424.0" y1="240.0" x2="378.0" y2="240.0" stroke="#E11D48" stroke-width="2.2" stroke-linecap="round"/><polygon points="370.0,240.0 380.0,235.0 380.0,245.0" fill="#E11D48"/><line x1="280.0" y1="60.0" x2="280.0" y2="96.0" stroke="#E11D48" stroke-width="2.6" stroke-linecap="round"/><polygon points="280.0,104.0 275.0,94.0 285.0,94.0" fill="#E11D48"/><text x="292" y="70" font-size="16" fill="#E11D48" font-family="Georgia, serif" font-style="italic" font-weight="500">F<tspan font-size="10" dy="4">ph</tspan></text><line x1="292" y1="55" x2="300.8" y2="55" stroke="#E11D48" stroke-width="1.3"/><polygon points="303.8,55.0 298.8,57.6 298.8,52.4" fill="#E11D48"/><text x="292" y="330" font-size="16" fill="#E11D48" font-family="Georgia, serif" font-style="italic" font-weight="500">F<tspan font-size="10" dy="4">pb</tspan></text><line x1="292" y1="315" x2="300.8" y2="315" stroke="#E11D48" stroke-width="1.3"/><polygon points="303.8,315.0 298.8,317.6 298.8,312.4" fill="#E11D48"/><rect x="470" y="40" width="24" height="320" fill="url(#gP)"/><text x="482" y="382" font-size="14" text-anchor="middle" fill="#831843" font-family="Georgia, serif" font-style="italic">P</text><line x1="494" y1="110" x2="504" y2="110" stroke="#1E293B"/><line x1="494" y1="270" x2="504" y2="270" stroke="#1E293B"/><text x="510" y="106" font-size="13" fill="#1E293B" font-family="Georgia, serif" font-style="italic">P(z₀ + h)</text><text x="510" y="124" font-size="13" fill="#1E293B" font-family="Georgia, serif" font-style="italic">= P(z₀) − ρgh</text><text x="510" y="274" font-size="13" fill="#1E293B" font-family="Georgia, serif" font-style="italic">P(z₀)</text></svg>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<ol class="nt-steps">
<li><p>Les forces pressantes sur la face latérale <b>s'annulent deux à deux</b> à une altitude donnée. Il ne reste plus qu'à considérer les deux faces horizontales.</p></li>
<li><p>Sur la face du bas&nbsp;: $\vec{F}_\mathrm{pb} = P(z_0)\times S\times \vec{k}$. Sur la face du haut&nbsp;: $\vec{F}_\mathrm{ph}=-P(z_0+h) \times S\times \vec{k}$.</p></li>
<li><p>D'après le principe fondamental de l'hydrostatique&nbsp;: $P(z_0+h)=P(z_0)-\rho \, g \, h$.</p></li>
<li><p>D'où&nbsp;: $\vec{\pi}_\mathrm{A} = \vec{F}_\mathrm{pb}+\vec{F}_\mathrm{ph} = \big(P(z_0)-P(z_0+h) \big)\, S\, \vec{k} = \rho \, g \, {\color{#2A6BC4} h \, S}\, \vec{k} = \rho \, g \, {\color{#2A6BC4} V}\, \vec{k} = -\rho  \,  V \, \vec{g}$, car $\vec{g} = -g\,\vec{k}$.</p></li>
</ol>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Poussée d'Archimède (généralisable à tout corps)</p>
<p class="nt-f-math">$$\vec{\pi}_\mathrm{A} = - \rho \, V \, \vec{g}$$</p>
<div class="nt-f-units"><span>$\pi_\mathrm{A}$ en <b>$\pu{N}$</b></span><span>$\rho$, masse volumique du fluide, en <b>$\pu{kg*m-3}$</b></span><span>$V$, volume immergé du corps, en <b>$\pu{m3}$</b></span><span>$g$ en <b>$\pu{m*s-2}$</b></span></div>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Si le corps flotte, $V$ désigne seulement le volume de la <b>partie immergée</b> du corps&nbsp;! Et $\rho$ est la masse volumique du <b>fluide</b>, pas celle du corps.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag">🧊&nbsp; Application</p>
<p>Quelle est la proportion immergée du volume d'un glaçon&nbsp;? Données&nbsp;: masse volumique de l'eau $\rho_\ell = \pu{1,0E3 kg*m-3}$&nbsp;; masse volumique de la glace $\rho_\mathrm{g} = \pu{9,2E2 kg*m-3}$.</p>
<p>Question subsidiaire&nbsp;: qu'en est-il pour un iceberg dans l'océan 🚢&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li><p><b>Bilan des forces</b> sur le glaçon&nbsp;: son poids $\vec{P}=m\vec{g}=\rho_\mathrm{g} V_\mathrm{tot} \,\vec{g}$ et la poussée d'Archimède $\vec{\pi}_\mathrm{A} = -\rho_\ell V_\mathrm{imm} \, \vec{g}$.</p></li>
<li><p>Le glaçon est à l'équilibre&nbsp;: dans le référentiel terrestre supposé galiléen, la 1<sup>re</sup> loi de Newton donne $\vec{P}+\vec{\pi}_\mathrm{A}= \vec{0}$, soit $\rho_\mathrm{g} V_\mathrm{tot} \, \vec{g} - \rho_\ell V_\mathrm{imm} \, \vec{g} = \vec{0}$.</p></li>
<li><p>D'où $\dfrac{V_\mathrm{imm}}{V_\mathrm{tot}} = \dfrac{\rho_\mathrm{g}}{\rho_\ell} = \dfrac{920}{1000} = 0{,}92$&nbsp;: <b>92&nbsp;% du glaçon est immergé</b>&nbsp;!</p></li>
<li><p><b>Iceberg</b>&nbsp;: l'eau de mer, salée, est plus dense que l'eau douce ($\rho \approx \pu{1,03E3 kg*m-3}$). La proportion immergée est un peu plus faible&nbsp;: $\dfrac{920}{1030} \approx 89\ \%$. C'est la fameuse «&nbsp;partie immergée de l'iceberg&nbsp;».</p></li>
</ol>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Mesurer la poussée d'Archimède</p>
<ul class="nt-facts">
<li><b>Au dynamomètre.</b> Suspendu à un dynamomètre, l'objet est soumis à son poids $\vec{P}$, à la force $\vec{F}_\mathrm{dyn}$ exercée par le dynamomètre et, s'il est immergé, à la poussée d'Archimède. À l'équilibre, $F_\mathrm{dyn} = P - \pi_\mathrm{A}$&nbsp;: la différence entre la mesure dans l'air et la mesure dans le liquide donne $\pi_\mathrm{A}$.</li>
<li><b>Par le liquide déplacé.</b> On immerge l'objet dans un vase rempli à ras bord, muni d'un bec. Le liquide qui déborde, de même volume que la partie immergée, est recueilli dans un bécher posé sur une balance tarée&nbsp;: on mesure directement la masse $m$ du liquide déplacé, donc son poids $m\,g$.</li>
</ul>
<p>L'animation réunit les deux mesures&nbsp;: elles donnent la même valeur.</p>
</div>

<div class="nt-lab" id="lab-dyna">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Dynamomètre et vase à trop-plein</p>
<canvas style="height:440px;" aria-label="Un objet suspendu à un dynamomètre est descendu dans un vase rempli à ras bord ; le liquide qui déborde par le bec est recueilli dans un bécher posé sur une balance"></canvas>
<label class="nt-ctrl">Descendre l'objet&nbsp;: <input type="range" min="0" max="1" step="0.005" value="0"></label>
<div class="nt-ctrl">Liquide&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="liq" value="eau" checked><span>eau</span></label>
<label><input type="radio" name="liq" value="sale"><span>eau très salée</span></label>
<label><input type="radio" name="liq" value="huile"><span>huile</span></label>
<label><input type="radio" name="liq" value="ethanol"><span>éthanol</span></label>
</div>
</div>
<div class="nt-btns"><button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Vider le bécher et remplir le vase à ras bord</button></div>
<div class="nt-read" aria-live="polite"><span>dans l'air&nbsp;: $P$ = <b class="out-p"></b></span><span>dynamomètre&nbsp;: $F_\mathrm{dyn}$ = <b class="out-f"></b></span><span>$P - F_\mathrm{dyn}$ = <b class="out-d"></b></span></div>
<div class="nt-read" aria-live="polite"><span>liquide débordé&nbsp;: $m$ = <b class="out-m"></b></span><span>son poids&nbsp;: $m\,g$ = <b class="out-mg"></b></span></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Objet&nbsp;: cylindre d'aluminium de 100&nbsp;mL et de 270&nbsp;g. Dans l'eau, on trouve $P - F_\mathrm{dyn} = \pu{0,981 N}$ et $m = \pu{100 g}$, soit $m\,g = \pu{0,981 N}$&nbsp;: la poussée d'Archimède est bien égale au poids du liquide déplacé. Plus le liquide est dense, plus elle est grande.</p>
</div>

### Exercice&nbsp;: la tour Eiffel dans la balance {.nt-h3}

<svg class="nt-svg nt-svg-s" viewBox="0 0 440 380" role="img" aria-label="Une tour Eiffel miniature suspendue par une ficelle à une potence est entièrement immergée dans un cristallisoir d'eau posé sur une balance"><defs><linearGradient id="gEau2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#BFDBFE"/><stop offset="1" stop-color="#60A5FA"/></linearGradient><linearGradient id="gBal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5EEAD4"/><stop offset="1" stop-color="#0F766E"/></linearGradient></defs><rect x="372" y="36" width="12" height="318" rx="2" fill="#64748B"/><rect x="190" y="30" width="194" height="12" rx="2" fill="#64748B"/><rect x="330" y="350" width="96" height="12" rx="2" fill="#64748B"/><line x1="210" y1="42" x2="210" y2="160" stroke="#334155" stroke-width="1.6"/><path d="M96,118 L108,262 Q110,272 120,272 L300,272 Q310,272 312,262 L324,118" fill="#F8FAFC" fill-opacity=".35" stroke="#64748B" stroke-width="2.5"/><path d="M210,160 L214.32,186.88 L221.52,212.8 L231.6,234.88 L246.0,256 L230.16,256 Q210,236.8 189.84,256 L174.0,256 L188.4,234.88 L198.48,212.8 L205.68,186.88 Z" fill="#78716C"/><rect x="192.72" y="210.88" width="34.56" height="3.84" fill="#57534E"/><rect x="184.08" y="232.96" width="51.839999999999996" height="3.84" fill="#57534E"/><path d="M99,146 L108,262 Q110,272 120,272 L300,272 Q310,272 312,262 L321,146 Z" fill="url(#gEau2)" opacity=".62"/><line x1="99" y1="146" x2="321" y2="146" stroke="#3B82F6" stroke-width="1.5"/><rect x="86" y="276" width="248" height="12" rx="4" fill="#5EEAD4"/><path d="M120,288 L100,356 Q98,362 106,362 L314,362 Q322,362 320,356 L300,288 Z" fill="url(#gBal)"/><circle cx="210" cy="324" r="24" fill="#0F172A"/><circle cx="210" cy="324" r="19" fill="#F8FAFC"/><text x="210" y="330" font-size="15" text-anchor="middle" fill="#0F172A" font-weight="500">?</text><text x="66" y="200" font-size="13" text-anchor="end" fill="#1D4ED8" font-weight="500">eau</text><line x1="70" y1="196" x2="112" y2="196" stroke="#1D4ED8"/></svg>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice</p>
<p>On tare la balance avant d'immerger la tour Eiffel, suspendue à une ficelle. Que mesure alors la balance après immersion de la tour&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<ol class="nt-steps">
<li>
<p><b>Ce que mesure la balance.</b> La balance mesure la force que le système posé sur elle exerce sur son plateau, et affiche la norme de cette force divisée par $g$. D'après la 3<sup>e</sup> loi de Newton, cette force est l'opposée de la réaction $\vec{N}$ du plateau sur le système&nbsp;:</p>
<p class="nt-center">$\vec{F}_\mathrm{syst/balance}= -\vec{N} \qquad\text{donc la balance affiche}\qquad \dfrac{\|\vec{N}\|}{g}$</p>
</li>
<li>
<p><b>Avant la tare. Système {eau + cristallisoir}</b>, dans le référentiel terrestre supposé galiléen.</p>
<p>Bilan des forces&nbsp;:</p>
<ul class="nt-facts">
<li>le poids du système&nbsp;: $(m_\mathrm{eau}+m_\mathrm{crist})\,\vec{g}$&nbsp;;</li>
<li>la réaction du plateau de la balance&nbsp;: $\vec{N}$.</li>
</ul>
<p>Le système est immobile&nbsp;: d'après la 1<sup>re</sup> loi de Newton, la somme des forces est nulle.</p>
<p class="nt-center">$(m_\mathrm{eau}+m_\mathrm{crist})\,\vec{g} + \vec{N} = \vec{0}$</p>
<p class="nt-center">$\vec{N} = -(m_\mathrm{eau}+m_\mathrm{crist})\,\vec{g} \qquad\text{donc}\qquad \dfrac{\|\vec{N}\|}{g} = m_\mathrm{eau}+m_\mathrm{crist}$</p>
<p>La balance affiche bien la masse du système. Comme on a taré, elle indique zéro pour cette valeur $m_\mathrm{eau}+m_\mathrm{crist}$.</p>
</li>
<li>
<p><b>Après immersion. Système {tour}.</b></p>
<p>Bilan des forces&nbsp;:</p>
<ul class="nt-facts">
<li>le poids de la tour&nbsp;: $m_\mathrm{tour}\,\vec{g}$&nbsp;;</li>
<li>la tension de la ficelle&nbsp;: $\vec{T}$&nbsp;;</li>
<li>la poussée d'Archimède exercée par l'eau&nbsp;: $\vec{\pi}_\mathrm{A} = -\rho_\mathrm{eau}V_\mathrm{tour}\,\vec{g}$.</li>
</ul>
<p>La tour est immobile&nbsp;: d'après la 1<sup>re</sup> loi de Newton,</p>
<p class="nt-center">$m_\mathrm{tour}\,\vec{g}+\vec{T}+\vec{\pi}_\mathrm{A}=\vec{0}$</p>
<p class="nt-center">${\color{#CA8A04} m_\mathrm{tour}\,\vec{g}=-\vec{T}-\vec{\pi}_\mathrm{A}}$</p>
</li>
<li>
<p><b>Après immersion. Système {eau + cristallisoir + tour}.</b></p>
<p>Bilan des forces&nbsp;:</p>
<ul class="nt-facts">
<li>le poids du système&nbsp;: $(m_\mathrm{tour}+m_\mathrm{eau}+m_\mathrm{crist})\,\vec{g}$&nbsp;;</li>
<li>la tension de la ficelle&nbsp;: $\vec{T}$&nbsp;;</li>
<li>la réaction du plateau&nbsp;: $\vec{N}$.</li>
</ul>
<p class="nt-note">La poussée d'Archimède n'apparaît pas&nbsp;: c'est une force exercée par l'eau sur la tour, deux parties du système. C'est une force <b>intérieure</b>.</p>
<p>Le système est immobile&nbsp;: d'après la 1<sup>re</sup> loi de Newton,</p>
<p class="nt-center">$(m_\mathrm{tour}+m_\mathrm{eau}+m_\mathrm{crist})\,\vec{g}+\vec{T}+\vec{N}=\vec{0}$</p>
<p>On développe le poids, puis on remplace $m_\mathrm{tour}\,\vec{g}$ grâce au résultat précédent&nbsp;:</p>
<p class="nt-center">${\color{#CA8A04} m_\mathrm{tour}\,\vec{g}}+m_\mathrm{eau}\,\vec{g}+m_\mathrm{crist}\,\vec{g}+\vec{T}+\vec{N}=\vec{0}$</p>
<p class="nt-center">${\color{#CA8A04} -\vec{T}-\vec{\pi}_\mathrm{A}}+m_\mathrm{eau}\,\vec{g}+m_\mathrm{crist}\,\vec{g}+\vec{T}+\vec{N}=\vec{0}$</p>
<p class="nt-center">$\vec{N}=\vec{\pi}_\mathrm{A}-m_\mathrm{eau}\,\vec{g}-m_\mathrm{crist}\,\vec{g}$</p>
<p class="nt-center">$\vec{N}=-\rho_\mathrm{eau}V_\mathrm{tour}\,\vec{g}-m_\mathrm{eau}\,\vec{g}-m_\mathrm{crist}\,\vec{g}$</p>
<p class="nt-center">$\dfrac{\|\vec{N}\|}{g}=\rho_\mathrm{eau}V_\mathrm{tour} + m_\mathrm{eau}+m_\mathrm{crist}$</p>
</li>
<li>
<p><b>Conclusion.</b> La tare retranche $m_\mathrm{eau}+m_\mathrm{crist}$&nbsp;: la balance affiche $\rho_\mathrm{eau}V_\mathrm{tour}$.</p>
<p>Comme $\rho_\mathrm{eau}=\pu{1,00 g*mL-1}$, une balance réglée en grammes affiche directement le volume de la tour en millilitres&nbsp;: c'est une façon élégante de mesurer un volume.</p>
</li>
</ol>
</div>
</details>

## Conservation du débit volumique {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp">débit volumique</span> est le <span class="imp nt-hole">volume de fluide</span> qui traverse une section droite du conduit où s'écoule le fluide, <span class="imp nt-hole">par unité de temps</span>.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Débit volumique</p>
<p class="nt-f-math">$$D_V = \frac{V}{\Delta t}$$</p>
<div class="nt-f-units"><span>$D_V$ en <b>$\pu{m3*s-1}$</b></span><span>$V$ en <b>$\pu{m3}$</b></span><span>$\Delta t$ en <b>$\pu{s}$</b></span></div>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 620 230" role="img" aria-label="Pendant la durée delta t, le fluide qui traverse la section S remplit un cylindre de longueur v fois delta t"><rect x="20" y="40" width="580" height="130" fill="#BFDBFE"/><line x1="20" y1="40" x2="600" y2="40" stroke="#475569" stroke-width="2.5"/><line x1="20" y1="170" x2="600" y2="170" stroke="#475569" stroke-width="2.5"/><rect x="180" y="40" width="250" height="130" fill="#60A5FA" opacity=".45"/><ellipse cx="180" cy="105" rx="22" ry="65" fill="#93C5FD" stroke="#1D4ED8" stroke-width="1.4"/><ellipse cx="430" cy="105" rx="22" ry="65" fill="#93C5FD"/><path d="M430,40 A22,65 0 0 0 430,170" fill="none" stroke="#1D4ED8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M430,40 A22,65 0 0 1 430,170" fill="none" stroke="#1D4ED8" stroke-width="1.4"/><text x="180" y="112" font-size="18" text-anchor="middle" fill="#1E3A8A" font-family="Georgia, serif" font-style="italic">S</text><text x="430" y="112" font-size="18" text-anchor="middle" fill="#1E3A8A" font-family="Georgia, serif" font-style="italic">S</text><line x1="220.0" y1="70.0" x2="282.0" y2="70.0" stroke="#D97706" stroke-width="2.4" stroke-linecap="round"/><polygon points="290.0,70.0 280.0,75.0 280.0,65.0" fill="#D97706"/><line x1="470.0" y1="70.0" x2="532.0" y2="70.0" stroke="#D97706" stroke-width="2.4" stroke-linecap="round"/><polygon points="540.0,70.0 530.0,75.0 530.0,65.0" fill="#D97706"/><line x1="220.0" y1="105.0" x2="282.0" y2="105.0" stroke="#D97706" stroke-width="2.4" stroke-linecap="round"/><polygon points="290.0,105.0 280.0,110.0 280.0,100.0" fill="#D97706"/><line x1="470.0" y1="105.0" x2="532.0" y2="105.0" stroke="#D97706" stroke-width="2.4" stroke-linecap="round"/><polygon points="540.0,105.0 530.0,110.0 530.0,100.0" fill="#D97706"/><line x1="220.0" y1="140.0" x2="282.0" y2="140.0" stroke="#D97706" stroke-width="2.4" stroke-linecap="round"/><polygon points="290.0,140.0 280.0,145.0 280.0,135.0" fill="#D97706"/><line x1="470.0" y1="140.0" x2="532.0" y2="140.0" stroke="#D97706" stroke-width="2.4" stroke-linecap="round"/><polygon points="540.0,140.0 530.0,145.0 530.0,135.0" fill="#D97706"/><text x="296" y="76" font-size="15" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="500">v</text><line x1="296" y1="62" x2="304.25" y2="62" stroke="#D97706" stroke-width="1.3"/><polygon points="307.2,62.0 302.2,64.6 302.2,59.4" fill="#D97706"/><line x1="305.0" y1="200.0" x2="422.0" y2="200.0" stroke="#1D4ED8" stroke-width="1.6" stroke-linecap="round"/><polygon points="430.0,200.0 420.0,205.0 420.0,195.0" fill="#1D4ED8"/><line x1="305.0" y1="200.0" x2="188.0" y2="200.0" stroke="#1D4ED8" stroke-width="1.6" stroke-linecap="round"/><polygon points="180.0,200.0 190.0,195.0 190.0,205.0" fill="#1D4ED8"/><text x="305" y="224" font-size="15" text-anchor="middle" fill="#1D4ED8" font-family="Georgia, serif" font-style="italic">L = v × Δt</text><text x="305" y="30" font-size="13" text-anchor="middle" fill="#475569" font-weight="500">volume écoulé pendant Δt : V = S × L = S × v × Δt</text></svg>

<p class="nt-lead">Si $S$ est l'aire de la section droite et $v$ la vitesse de l'écoulement à cet endroit, alors&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Débit, section et vitesse</p>
<p class="nt-f-math">$$D_V = \frac{S\times v\times \Delta t}{\Delta t} = v\times S$$</p>
<div class="nt-f-units"><span>si la vitesse n'est pas uniforme sur la section, on remplace $v$ par la vitesse moyenne $\bar{v}$</span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Pour un <span class="imp nt-hole">fluide incompressible</span>, le <span class="imp nt-hole">débit se conserve</span>. Dans un conduit de section variable&nbsp;:</p>
<p class="nt-center">${\color{#D97706}v_1}\times {\color{#2A6BC4}S_1} = {\color{#D97706}v_2}\times  {\color{#2A6BC4}S_2}$</p>
<p>La <b style="color:#D97706;">vitesse d'écoulement</b> est <span class="imp nt-hole">inversement proportionnelle</span> à l'<b style="color:#2A6BC4;">aire de la section</b> du conduit&nbsp;: le fluide accélère dans un rétrécissement. C'est ce qu'on fait en bouchant à moitié l'embout d'un tuyau d'arrosage.</p>
</div>

## Fluide parfait, écoulement permanent, lignes de courant {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Fluide parfait</p>
<p>Un <span class="imp">fluide</span> est dit <span class="imp">parfait</span> si on peut décrire son écoulement <span class="imp nt-hole">sans prendre en compte les effets de la viscosité</span>.</p>
<p>En pratique, si les effets de la viscosité sont suffisamment faibles par rapport aux effets inertiels (liés à la vitesse), l'approximation de fluide parfait est adaptée, d'autant plus qu'on est loin d'un obstacle ou d'une paroi.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Des fluides vraiment parfaits, et des fluides jamais parfaits près d'une paroi</span></summary>
<div class="nt-d-body">
<p>L'hélium liquide, refroidi en dessous de 2,17&nbsp;K, devient <b>superfluide</b>&nbsp;: sa viscosité s'annule. Il en devient fondamentalement étrange&nbsp;: un film invisible remonte le long de la paroi intérieure d'un récipient, redescend à l'extérieur et forme des gouttes qui tombent, jusqu'à ce que le récipient soit vide. 
<div style="position:relative;margin-left:auto;margin-right:auto;width:400px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="https://upload.wikimedia.org/wikipedia/commons/f/f8/Liquid_helium_Rollin_film.jpg" style="box-shadow:none;background:none;border-radius:5px;">
</div>
Les condensats de Bose-Einstein sont aussi superfluides, et le plasma de quarks et de gluons créé dans les collisionneurs de particules est le fluide le moins visqueux connu, presque parfait.</p>
<p>Près d'une paroi, en revanche, un fluide réel est toujours visqueux&nbsp;: il «&nbsp;colle&nbsp;» à la paroi. On sépare alors l'étude en deux domaines&nbsp;: une mince <b>couche limite</b> près de la paroi, où la viscosité compte, et le reste de l'écoulement, où le fluide peut être considéré comme parfait.</p>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Écoulement permanent</p>
<p>Un <span class="imp">écoulement en régime permanent</span> (ou stationnaire) est un écoulement où la <span class="imp nt-hole">vitesse en chaque point ne varie pas au cours du temps</span>.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Ligne de courant</p>
<p>Une <span class="imp">ligne de courant</span> d'un écoulement est une courbe <span class="imp nt-hole">tangente en chacun de ses points au vecteur vitesse</span>. Les lignes de courant permettent de cartographier le champ des vitesses du fluide.</p>
<p>Ce n'est pas la même chose qu'une trajectoire&nbsp;: on ne suit pas une particule dans le temps, on regarde à un instant donné les vitesses d'un ensemble de particules. Mais <b>en régime permanent, les lignes de courant se confondent avec les trajectoires des particules</b>.</p>
</div>

<div class="nt-lab" id="lab-lignes">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Lignes de courant autour d'un obstacle</p>
<canvas style="height:320px;" aria-label="Écoulement permanent d'un fluide parfait autour d'un cylindre : lignes de courant et particules de fluide"></canvas>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="vec"> vecteurs vitesse</label>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<p class="nt-note">Écoulement permanent d'un fluide parfait autour d'un cylindre (modèle de l'écoulement potentiel). Les particules suivent exactement les lignes de courant&nbsp;: en régime permanent, lignes de courant et trajectoires se confondent. Elles vont plus vite là où les lignes se resserrent, sur les flancs de l'obstacle. Un fluide réel, visqueux, formerait en plus des tourbillons derrière l'obstacle.</p>
</div>

## Relation de Bernoulli {.nt-h2}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Relation de Bernoulli</p>
<p>L'écoulement d'un fluide <b style="color:#DB2777;">incompressible</b>, <b style="color:#CA8A04;">parfait</b>, en <b style="color:#2A6BC4;">régime permanent</b> suit la <span class="imp">relation de Bernoulli</span> entre deux points $\mathrm{M_1}$ et $\mathrm{M_2}$ d'une même ligne de courant.</p>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 640 340" role="img" aria-label="Conduite montante qui se rétrécit : en M1, à l'altitude z1, la pression vaut P1 et la vitesse v1 ; en M2, à l'altitude z2, la pression vaut P2 et la vitesse v2"><defs><linearGradient id="gTube" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#BFDBFE"/><stop offset="1" stop-color="#93C5FD"/></linearGradient></defs><line x1="40" y1="330" x2="40" y2="20" stroke="#1E293B" stroke-width="1.2"/><polygon points="40.0,12.0 44.5,21.0 35.5,21.0" fill="#1E293B"/><text x="50" y="22" font-size="15" fill="#1E293B" font-family="Georgia, serif" font-style="italic">z</text><path d="M70,200 L240,200 C320,200 350,92 440,86 L620,86 L620,154 L460,154 C380,160 340,316 240,316 L70,316 Z" fill="url(#gTube)"/><path d="M70,200 L240,200 C320,200 350,92 440,86 L620,86" fill="none" stroke="#334155" stroke-width="1.6"/><path d="M70,316 L240,316 C340,316 380,160 460,154 L620,154" fill="none" stroke="#334155" stroke-width="1.6"/><path d="M70,258 L240,258 C340,258 368,122 450,120 L620,120" fill="none" stroke="#16A34A" stroke-width="1.5"/><line x1="40" y1="258" x2="140" y2="258" stroke="#CA8A04" stroke-width=".9" stroke-dasharray="3 4"/><line x1="40" y1="120" x2="510" y2="120" stroke="#CA8A04" stroke-width=".9" stroke-dasharray="3 4"/><text x="32" y="262" font-size="14" text-anchor="end" fill="#A16207" font-family="Georgia, serif" font-style="italic">z₁</text><text x="32" y="124" font-size="14" text-anchor="end" fill="#A16207" font-family="Georgia, serif" font-style="italic">z₂</text><circle cx="150" cy="258" r="4.5" fill="#CA8A04"/><circle cx="520" cy="120" r="4.5" fill="#CA8A04"/><text x="140" y="284" font-size="15" fill="#A16207" font-family="Georgia, serif" font-style="italic">M₁</text><text x="508" y="143" font-size="15" fill="#A16207" font-family="Georgia, serif" font-style="italic">M₂</text><line x1="150.0" y1="258.0" x2="184.0" y2="258.0" stroke="#D97706" stroke-width="2" stroke-linecap="round"/><polygon points="192.0,258.0 182.0,263.0 182.0,253.0" fill="#D97706"/><line x1="520.0" y1="120.0" x2="584.0" y2="120.0" stroke="#D97706" stroke-width="2" stroke-linecap="round"/><polygon points="592.0,120.0 582.0,125.0 582.0,115.0" fill="#D97706"/><text x="164" y="250" font-size="14" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="500">v<tspan font-size="9" dy="4">1</tspan></text><line x1="164" y1="237" x2="171.7" y2="237" stroke="#D97706" stroke-width="1.3"/><polygon points="174.7,237.0 169.7,239.6 169.7,234.4" fill="#D97706"/><text x="546" y="112" font-size="14" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="500">v<tspan font-size="9" dy="4">2</tspan></text><line x1="546" y1="99" x2="553.7" y2="99" stroke="#D97706" stroke-width="1.3"/><polygon points="556.7,99.0 551.7,101.6 551.7,96.4" fill="#D97706"/><line x1="150" y1="200" x2="150" y2="174" stroke="#64748B" stroke-width="3"/><circle cx="150" cy="158" r="16" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.6"/><line x1="150" y1="158" x2="158" y2="150" stroke="#0F172A" stroke-width="1.4"/><circle cx="150" cy="158" r="2" fill="#0F172A"/><text x="172" y="162" font-size="15" fill="#0F766E" font-family="Georgia, serif" font-style="italic">P₁</text><line x1="520" y1="86" x2="520" y2="60" stroke="#64748B" stroke-width="3"/><circle cx="520" cy="44" r="16" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.6"/><line x1="520" y1="44" x2="528" y2="36" stroke="#0F172A" stroke-width="1.4"/><circle cx="520" cy="44" r="2" fill="#0F172A"/><text x="542" y="48" font-size="15" fill="#0F766E" font-family="Georgia, serif" font-style="italic">P₂</text><line x1="470" y1="326" x2="496" y2="326" stroke="#16A34A" stroke-width="2"/><text x="504" y="330" font-size="13" fill="#16A34A">ligne de courant</text></svg>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Relation de Bernoulli</p>
<p class="nt-f-math">$${\color{#5EEAD4}P_1}+{\color{#FDE047}\rho g z_1} + {\color{#FDBA74}\frac12 \rho v_1^{\,2}} = {\color{#5EEAD4}P_2}+{\color{#FDE047}\rho g z_2}+ {\color{#FDBA74}\frac12 \rho v_2^{\,2}}$$</p>
<div class="nt-f-units"><span>toujours fournie dans les sujets</span></div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-bolt"></i>Une conservation de l'énergie</p>
<p>Cette relation exprime la conservation de l'énergie volumique d'une particule de fluide&nbsp;:</p>
<ul class="nt-facts">
<li>$\frac12\rho v^2$ est une densité volumique d'<span class="imp nt-hole">énergie cinétique</span>&nbsp;;</li>
<li>$\rho g z$ est une densité volumique d'<span class="imp nt-hole">énergie potentielle de pesanteur</span>&nbsp;;</li>
<li>$P$ est une densité volumique d'énergie potentielle dont dérivent les <span class="imp nt-hole">forces de pression</span>.</li>
</ul>
<p class="nt-note">Cette conservation est valable le long d'une ligne de courant. Mais si l'écoulement est irrotationnel (nulle part dans le fluide, un petit moulinet ne se mettrait à tourner), elle est valable entre deux points quelconques du fluide&nbsp;: on dit que l'écoulement est potentiel.</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Fluide au repos ($v_1=v_2=0$)</p>
<p class="nt-f-math">$$P_1+\rho g z_1 = P_2 + \rho g z_2$$</p>
<div class="nt-f-units"><span>la <b>loi fondamentale de la statique des fluides</b></span></div>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Écoulement horizontal ($z_1=z_2$)</p>
<p class="nt-f-math">$$P_1+\frac12\rho v_1^{\,2}=P_2+\frac12\rho v_2^{\,2}$$</p>
<div class="nt-f-units"><span>l'<b>effet Venturi</b></span></div>
</div>
</div>

### L'effet Venturi {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>L'effet Venturi indique que si la vitesse de l'écoulement augmente, alors la pression <span class="imp nt-hole">diminue</span>. Or la conservation du débit volumique nous a appris que si l'écoulement devient plus étroit, sa vitesse <span class="imp nt-hole">augmente</span>.</p>
<p>On en déduit que la pression <span class="imp nt-hole">diminue dans un étranglement</span>.</p>
</div>

<div class="nt-lab" id="lab-venturi">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Débit, vitesse et pression dans un étranglement</p>
<canvas style="height:340px;" aria-label="Écoulement d'eau dans un tube qui se rétrécit puis s'élargit, avec trois tubes manométriques"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Rapport des sections $S_2/S_1$&nbsp;: <b class="out-s"></b><input type="range" data-p="s" min="0.25" max="1" step="0.01" value="0.5"></label>
<label class="nt-ctrl">Vitesse à l'entrée $v_1$&nbsp;: <b class="out-v"></b><input type="range" data-p="v" min="0.5" max="3" step="0.1" value="1.5"></label>
</div>
<div class="nt-read" aria-live="polite"><span>$v_2 = v_1 S_1/S_2$ = <b class="out-v2"></b></span><span>$P_1 - P_2$ = <b class="out-dp"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-note">Les particules accélèrent dans l'étranglement (conservation du débit), et le niveau d'eau du tube manométrique central baisse&nbsp;: la pression y est plus faible (effet Venturi). Après l'étranglement, la vitesse et la pression reprennent leurs valeurs d'entrée, puisque le fluide est parfait.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples d'applications</p>
<ul class="nt-facts">
<li><b>La trompe à eau</b>&nbsp;: l'eau du robinet accélère dans un étranglement&nbsp;; la dépression créée aspire l'air d'un récipient (par exemple pour une filtration sous vide, au laboratoire).</li>
<li><b>Les vaporisateurs</b>&nbsp;: l'air chassé à grande vitesse au-dessus d'un petit tube y crée une dépression, qui aspire le liquide et le pulvérise.</li>
<li><b>Le carburateur</b> des moteurs à essence (tondeuses, mobylettes, voitures anciennes)&nbsp;: l'air aspiré par le moteur accélère dans un étranglement, et la dépression aspire l'essence par un petit gicleur, qui se mélange à l'air.</li>
</ul>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Vidéos et simulation</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://upload.wikimedia.org/wikipedia/commons/5/58/Venturi_Tube_en.webm" target="_blank" rel="noopener">Une animation du tube de Venturi</a>&nbsp;;</li>
<li><a href="https://presentationssite.github.io/ecoulement.html" target="_blank" rel="noopener">La simulation d'écoulement du cours</a>&nbsp;;</li>
<li>Expériences illustrant l'effet Venturi&nbsp;: <a href="https://www.youtube.com/watch?v=Ye3QPgDdJNg" target="_blank" rel="noopener">lévitation d'une balle</a>, <a href="https://www.youtube.com/watch?v=BWvGE238DdE" target="_blank" rel="noopener">table et feuille</a>, <a href="https://www.youtube.com/watch?v=51_Rzpw119o" target="_blank" rel="noopener">feuille collée en soufflant</a> et <a href="https://www.youtube.com/shorts/XP6oqIic4lo" target="_blank" rel="noopener">gros sac gonflé d'un seul souffle</a>.</li>
</ul>
</div>
</details>

### Une autre application&nbsp;: le tube de Pitot {.nt-h3}

<p class="nt-lead">Comment un avion mesure-t-il sa vitesse par rapport à l'air&nbsp;? Grâce à un petit tube pointé face au vent, inventé par Henri Pitot au XVIII<sup>e</sup> siècle pour mesurer la vitesse de l'eau dans les rivières.</p>

<svg class="nt-svg" viewBox="0 0 720 360" role="img" aria-label="Tube de Pitot : un canal central ouvert face au vent en A, où l'air s'arrête, et un canal extérieur percé de trous latéraux en B ; chacun est relié à une branche d'un manomètre en U. Les lignes de courant qui aboutissent en A et passent en B partent de points O et O' loin en amont"><rect x="0" y="0" width="720" height="236" fill="#F0F9FF"/><path d="M20,46 L700,46" fill="none" stroke="#16A34A" stroke-width="1.1" opacity=".75"/><path d="M20,214 L700,214" fill="none" stroke="#16A34A" stroke-width="1.1" opacity=".75"/><path d="M20,120 L196,120 C228,120 236,114 262,114 L700,114" fill="none" stroke="#16A34A" stroke-width="1.1" opacity=".75"/><path d="M20,180 L196,180 C228,180 236,186 262,186 L700,186" fill="none" stroke="#16A34A" stroke-width="1.1" opacity=".75"/><path d="M20,150 L238,150" fill="none" stroke="#16A34A" stroke-width="1.1" opacity=".75"/><line x1="150.0" y1="46.0" x2="182.0" y2="46.0" stroke="#D97706" stroke-width="1.6" stroke-linecap="round"/><polygon points="190.0,46.0 180.0,51.0 180.0,41.0" fill="#D97706"/><line x1="150.0" y1="214.0" x2="182.0" y2="214.0" stroke="#D97706" stroke-width="1.6" stroke-linecap="round"/><polygon points="190.0,214.0 180.0,219.0 180.0,209.0" fill="#D97706"/><text x="162" y="38" font-size="14" fill="#D97706" font-family="Georgia, serif" font-style="italic" font-weight="500">v</text><line x1="162" y1="25" x2="169.7" y2="25" stroke="#D97706" stroke-width="1.3"/><polygon points="172.7,25.0 167.7,27.6 167.7,22.4" fill="#D97706"/><circle cx="90" cy="150" r="4" fill="#475569"/><text x="90" y="170" font-size="14" text-anchor="middle" fill="#475569" font-family="Georgia, serif" font-style="italic">O</text><circle cx="90" cy="120" r="4" fill="#475569"/><text x="90" y="110" font-size="14" text-anchor="middle" fill="#475569" font-family="Georgia, serif" font-style="italic">O′</text><text x="20" y="80" font-size="12" fill="#475569">loin du tube : pression P₀, vitesse v</text><path d="M262,128 L560,128 L560,172 L530,172 Q526,172 526,176 L526,246 L514,246 L514,176 Q514,172 510,172 L262,172 Q240,172 240,150 Q240,128 262,128 Z" fill="#BFDBFE" stroke="#334155" stroke-width="1.4"/><rect x="414" y="126.5" width="8" height="3" fill="#BFDBFE"/><rect x="436" y="126.5" width="8" height="3" fill="#BFDBFE"/><path d="M240,144 L590,144 Q612,144 612,166 L612,246 L600,246 L600,166 Q600,156 590,156 L240,156 Z" fill="#FECDD3" stroke="#334155" stroke-width="1.2"/><rect x="238.5" y="145" width="3" height="10" fill="#FECDD3"/><rect x="601" y="244" width="10" height="4" fill="#FECDD3"/><rect x="515" y="244" width="10" height="4" fill="#BFDBFE"/><path d="M514,246 L514,316 Q514,334 532,334 L594,334 Q612,334 612,316 L612,246" fill="none" stroke="#334155" stroke-width="1.2"/><path d="M526,246 L526,312 Q526,322 536,322 L590,322 Q600,322 600,312 L600,246" fill="none" stroke="#334155" stroke-width="1.2"/><path d="M515,262 L515,316 Q515,333 532,333 L594,333 Q611,333 611,316 L611,292 L601,292 L601,312 Q601,323 590,323 L536,323 Q525,323 525,312 L525,262 Z" fill="#60A5FA"/><line x1="622" y1="262" x2="622" y2="292" stroke="#0F172A" stroke-width="1"/><polygon points="622.0,262.0 625.0,268.0 619.0,268.0" fill="#0F172A"/><polygon points="622.0,292.0 619.0,286.0 625.0,286.0" fill="#0F172A"/><text x="630" y="282" font-size="14" fill="#0F172A" font-family="Georgia, serif" font-style="italic">Δh</text><circle cx="240" cy="150" r="4" fill="#E11D48"/><text x="224" y="140" font-size="14" text-anchor="end" fill="#E11D48" font-family="Georgia, serif" font-style="italic">A</text><circle cx="429" cy="114" r="4" fill="#2A6BC4"/><text x="429" y="104" font-size="14" text-anchor="middle" fill="#2A6BC4" font-family="Georgia, serif" font-style="italic">B</text><rect x="30" y="262" width="22" height="12" fill="#FECDD3" stroke="#334155" stroke-width=".8"/><text x="60" y="272" font-size="12.5" fill="#334155">canal relié à A (pression totale)</text><rect x="30" y="286" width="22" height="12" fill="#BFDBFE" stroke="#334155" stroke-width=".8"/><text x="60" y="296" font-size="12.5" fill="#334155">canal relié aux trous B (pression statique)</text><text x="30" y="322" font-size="12.5" fill="#334155">le manomètre mesure P(A) − P(B)</text></svg>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Le principe</p>
<ol class="nt-steps">
<li><p><b>Le dispositif.</b> Le tube contient deux canaux. Le canal central (en rose) s'ouvre face au vent, en A&nbsp;; le canal extérieur (en bleu) communique avec l'air par de petits trous latéraux, en B. Chacun est relié à une branche d'un manomètre en U, qui mesure l'écart $P_\mathrm{A} - P_\mathrm{B}$.</p></li>
<li><p><b>En A.</b> Le canal central est fermé à l'autre bout&nbsp;: l'air qui arrive en A ne peut pas y entrer et s'arrête, $v_\mathrm{A} = 0$ (c'est un point d'arrêt). Prenons la ligne de courant qui aboutit en A, et un point O de cette ligne, loin en amont, là où l'air n'est pas encore perturbé par le tube (pression $P_0$, vitesse $v$). Avec la relation de Bernoulli entre O et A, à la même altitude&nbsp;:</p>
<p class="nt-center">$P_0 + \frac12\rho v^2 = P_\mathrm{A} + \frac12\rho\times 0^2 \qquad\text{soit}\qquad P_\mathrm{A} = P_0 + \frac12\rho v^2$</p></li>
<li><p><b>En B.</b> Prenons maintenant une autre ligne de courant, celle qui passe juste au-dessus des trous B, et un point O′ de cette ligne, lui aussi loin en amont. Le tube est fin et aligné avec l'écoulement&nbsp;: le long de ses flancs, l'air a pratiquement retrouvé sa vitesse $v$. Avec la relation de Bernoulli entre O′ et B&nbsp;:</p>
<p class="nt-center">$P_0 + \frac12\rho v^2 = P_\mathrm{B} + \frac12\rho v^2 \qquad\text{soit}\qquad P_\mathrm{B} = P_0$</p></li>
<li><p><b>Pourquoi a-t-on le droit d'utiliser deux lignes de courant différentes&nbsp;?</b> La relation de Bernoulli ne relie que des points d'une même ligne de courant&nbsp;: c'est pourquoi on l'applique séparément, entre O et A, puis entre O′ et B. Ce qui permet de comparer les résultats, c'est que les deux lignes partent de la même région, loin en amont, où l'écoulement est uniforme&nbsp;: O et O′ y ont la même pression $P_0$, la même vitesse $v$ et (presque) la même altitude. La quantité $P + \rho g z + \frac12\rho v^2$, constante le long de chaque ligne, a donc la même valeur sur les deux lignes.</p></li>
<li><p><b>Conclusion.</b> L'écart mesuré vaut $P_\mathrm{A} - P_\mathrm{B} = \frac12\rho v^2$, d'où la vitesse&nbsp;:</p></li>
</ol>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Vitesse mesurée par un tube de Pitot</p>
<p class="nt-f-math">$$v = \sqrt{\frac{2\,(P_\mathrm{A} - P_\mathrm{B})}{\rho}}$$</p>
<div class="nt-f-units"><span>$\rho$&nbsp;: masse volumique de l'<b>air</b>, en <b>$\pu{kg*m-3}$</b></span><span>pressions en <b>$\pu{Pa}$</b></span></div>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Au décollage, le tube de Pitot d'un avion de ligne mesure un écart de pression $P_\mathrm{A} - P_\mathrm{B} = \pu{3,8 kPa}$. Quelle est la vitesse de l'avion par rapport à l'air&nbsp;? On prendra $\rho_\mathrm{air} = \pu{1,2 kg*m-3}$.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p class="nt-center">$v = \sqrt{\dfrac{2\times 3{,}8\times10^{3}}{1{,}2}} \approx \pu{80 m*s-1}$, soit environ 290&nbsp;km/h.</p>
<p class="nt-note">C'est bien l'ordre de grandeur de la vitesse de décollage d'un avion de ligne. Remarquez que l'écart de pression reste faible, environ 4&nbsp;% de la pression atmosphérique&nbsp;: il faut un manomètre sensible.</p>
</div>
</details>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-plane"></i>Un instrument vital</p>
<p>Sans la vitesse par rapport à l'air, les pilotes et les automatismes ne peuvent plus piloter correctement l'avion. C'est pourquoi les avions portent plusieurs tubes de Pitot, chauffés pour éviter qu'ils ne givrent. En 2009, le givrage des sondes Pitot du vol Rio-Paris AF447 a privé l'équipage d'indications de vitesse fiables, ce qui a été l'événement déclencheur de l'accident.</p>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  var CP = '#E11D48', CA = '#059669', CV = '#D97706', CPR = '#2A6BC4';   /* poids, poussée, vitesse, pression */
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
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '500 12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(255,255,255,.92)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  function arrow(c, x1, y1, x2, y2, color, w) {
    var dx = x2 - x1, dy = y2 - y1, n = Math.hypot(dx, dy); if (n < 3) { return; }
    var ux = dx / n, uy = dy / n, L = Math.min(12, n * 0.4), W = L * 0.55;
    c.strokeStyle = color; c.fillStyle = color; c.lineWidth = w || 2; c.lineCap = 'round';
    c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2 - ux * L * 0.8, y2 - uy * L * 0.8); c.stroke();
    c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - ux * L - uy * W, y2 - uy * L + ux * W); c.lineTo(x2 - ux * L + uy * W, y2 - uy * L - ux * W); c.closePath(); c.fill();
  }
  function loop(cv, btn, f) {
    var st = { playing: !RM, visible: true, last: null };
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { st.visible = es[0].isIntersecting; }).observe(cv); }
    if (btn) { playLabel(btn, st.playing); btn.addEventListener('click', function () { st.playing = !st.playing; playLabel(btn, st.playing); }); }
    (function step(ts) { var dt = st.last === null ? 0 : Math.min(0.05, (ts - st.last) / 1000); st.last = ts; if (st.visible) { f(st.playing ? dt : 0); } requestAnimationFrame(step); })(performance.now());
  }
  /* ================= 1. Mesurer la poussée d'Archimède : dynamomètre et vase à trop-plein ================= */
  (function () {
    var root = document.getElementById('lab-dyna');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rP = $(root, 'input[type="range"]'), oF = $(root, '.out-f'), oP = $(root, '.out-p'), oD = $(root, '.out-d'), oM = $(root, '.out-m'), oMg = $(root, '.out-mg'), msg = $(root, '.nt-msg'), S;
    var G = 9.81, V = 100, MOBJ = 270, liq = 'eau', vMax = 0, drops = [], last = null, visible = true;   /* V en mL (cm³), masses en g */
    var LIQ = { eau: [1.00, 'eau', [96, 165, 250]], sale: [1.20, 'eau très salée', [45, 212, 191]], huile: [0.92, 'huile', [250, 204, 21]], ethanol: [0.79, 'éthanol', [203, 213, 225]] };
    var INK = '#475569', GLASS = 'rgba(241,245,249,.55)';
    function rgba(c, a) { return 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + a + ')'; }
    function rr(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
    /* légende centrée sous un élément, recadrée pour ne jamais sortir du dessin */
    function legende(c, s, x, y, w) {
      c.font = '12px system-ui, sans-serif'; var lw = c.measureText(s).width;
      x = Math.max(6 + lw / 2, Math.min(w - 6 - lw / 2, x));
      c.textAlign = 'center'; c.fillStyle = '#475569'; c.fillText(s, x, y);
      return [x - lw / 2, x + lw / 2];
    }
    function geom(w, h) {
      /* tailles adaptées à la largeur, puis montage recentré dans le cadre */
      var canW = Math.max(96, Math.min(160, w * 0.3)), bw = Math.max(92, Math.min(124, w * 0.24));
      var gx = { baseL: 0, rod: 30, cx: 30 + 34 + canW / 2 };
      gx.x0 = gx.cx - canW / 2; gx.x1 = gx.cx + canW / 2; gx.bc = gx.x1 + bw / 2 + 10; gx.bR = gx.bc + bw / 2;   /* la balance ne touche pas le vase */
      var spout = gx.bc - gx.x1 - (bw - 34) * 0.18;   /* le bec s'arrête au-dessus de l'ouverture du bécher */
      var off = Math.max(8, (w - gx.bR) / 2);
      var g = { canW: canW, bw: bw, spout: spout, rod: gx.rod + off, cx: gx.cx + off, x0: gx.x0 + off, x1: gx.x1 + off, bc: gx.bc + off, baseL: gx.baseL + off };
      g.bench = h - 46;                 /* paillasse : potence, vase et balance y sont posés */
      g.canB = g.bench; g.canT = g.bench - 150; g.surf0 = g.canT + 14;   /* niveau du liquide = lèvre inférieure du bec */
      g.objW = Math.min(52, canW * 0.38); g.objH = 70; g.wire = 30;
      g.bot0 = g.canT - 16;             /* bas de l'objet au départ : au-dessus du bord du vase */
      g.bot1 = g.surf0 + 8 + g.objH;   /* fin de course : objet entièrement immergé, juste sous la surface ; le dynamomètre reste au-dessus du vase */
      g.dyn = 104;                      /* longueur du dynamomètre (anneau compris jusqu'au crochet) */
      g.balH = 16; g.balTop = g.bench - g.balH;
      g.bkH = 58; g.bkW = bw - 34;
      return g;
    }
    function draw(dt) {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, s = +rP.value, L = LIQ[liq], rho = L[0], g = geom(w, h);
      var bot = g.bot0 + s * (g.bot1 - g.bot0), objTop = bot - g.objH;
      var dBot = bot - g.surf0, f = Math.max(0, Math.min(1, dBot / g.objH)), Vimm = f * V;
      if (Vimm > vMax + 1e-9) { var add = Vimm - vMax; vMax = Vimm; for (var k = 0; k < Math.min(6, Math.ceil(add / 3)); k++) { drops.push({ t: -k * 0.08 }); } }
      var Fdyn = (MOBJ * G - rho * Vimm * G) / 1000, P = MOBJ * G / 1000, mDeb = rho * vMax;
      var surf = g.surf0 + (vMax - Vimm) / V * 22;   /* le niveau baisse si l'on remonte l'objet */
      /* positions qui suivent la noix : crochet du dynamomètre, dynamomètre, bras de la potence */
      var hookY = objTop - g.wire, dTop = hookY - g.dyn, armY = dTop - 10;
      c.clearRect(0, 0, w, h);
      /* paillasse */
      c.fillStyle = '#E7E5E4'; c.fillRect(0, g.bench, w, 5); c.strokeStyle = '#A8A29E'; c.lineWidth = 1; c.beginPath(); c.moveTo(0, g.bench + 0.5); c.lineTo(w, g.bench + 0.5); c.stroke();
      /* potence : socle, tige, noix et bras */
      c.fillStyle = '#94A3B8'; rr(c, g.baseL, g.bench - 7, 64, 7, 2); c.fill();
      var gr = c.createLinearGradient(g.rod - 4, 0, g.rod + 4, 0); gr.addColorStop(0, '#94A3B8'); gr.addColorStop(0.5, '#E2E8F0'); gr.addColorStop(1, '#94A3B8');
      c.fillStyle = gr; c.fillRect(g.rod - 3.5, 3, 7, g.bench - 10);
      c.fillStyle = '#475569'; rr(c, g.rod - 8, armY - 7, 16, 14, 2); c.fill();                 /* noix */
      c.fillStyle = '#94A3B8'; c.fillRect(g.rod + 8, armY - 2.5, g.cx - g.rod - 8, 5);            /* bras */
      c.strokeStyle = '#475569'; c.lineWidth = 1.6; c.beginPath(); c.moveTo(g.cx, armY + 2); c.lineTo(g.cx, armY + 6); c.arc(g.cx - 3, armY + 6, 3, 0, Math.PI); c.stroke();   /* crochet du bras */
      /* dynamomètre : anneau, tube gradué, ressort, index, crochet */
      var tx = g.cx - 11, tTop = dTop + 10, tLen = g.dyn - 26, sc = (tLen - 12) / 3;   /* 0 à 3 N */
      c.strokeStyle = INK; c.lineWidth = 1.3; c.beginPath(); c.ellipse(g.cx, dTop + 4, 4, 5, 0, 0, 2 * Math.PI); c.stroke();   /* anneau passé dans le crochet */
      c.fillStyle = '#F8FAFC'; rr(c, tx, tTop, 22, tLen, 4); c.fill(); c.lineWidth = 1; c.stroke();
      c.font = '9.5px system-ui, sans-serif'; c.textAlign = 'right'; c.fillStyle = INK;
      for (var n = 0; n <= 3; n += 0.5) { var yy = tTop + 6 + n * sc; c.strokeStyle = INK; c.lineWidth = 0.7; c.beginPath(); c.moveTo(tx, yy); c.lineTo(tx + (n % 1 === 0 ? 7 : 4), yy); c.stroke(); if (n % 1 === 0) { c.fillText(String(n), tx - 3, yy + 3); } }
      var yI = tTop + 6 + Fdyn * sc;
      c.strokeStyle = '#94A3B8'; c.lineWidth = 1; c.beginPath(); c.moveTo(g.cx, tTop + 2);
      for (var q = 1; q <= 12; q++) { c.lineTo(g.cx + (q % 2 ? 5 : -5), tTop + 2 + (yI - tTop - 2) * q / 12); } c.stroke();
      c.fillStyle = '#E11D48'; c.fillRect(tx + 2, yI - 1.2, 18, 2.4);
      c.strokeStyle = INK; c.lineWidth = 1.2; c.beginPath(); c.moveTo(g.cx, tTop + tLen); c.lineTo(g.cx, hookY - 4); c.stroke();
      c.beginPath(); c.arc(g.cx + 2.5, hookY - 2, 2.5, Math.PI, 2.2 * Math.PI, true); c.stroke();   /* crochet du dynamomètre */
      c.font = '12px system-ui, sans-serif'; c.textAlign = 'left'; c.fillStyle = '#475569'; c.fillText('dynamomètre', tx + 30, tTop + tLen / 2 + 4);
      /* fil */
      c.strokeStyle = '#334155'; c.lineWidth = 1; c.beginPath(); c.moveTo(g.cx, hookY); c.lineTo(g.cx, objTop); c.stroke();
      /* vase à trop-plein : liquide, objet, liquide devant la partie immergée, parois et bec */
      var Lc = rgba(L[2], 0.5);
      c.fillStyle = GLASS; c.fillRect(g.x0, g.canT, g.canW, g.canB - g.canT);
      c.fillStyle = Lc; c.fillRect(g.x0 + 1, surf, g.canW - 2, g.canB - surf - 1);
      var og = c.createLinearGradient(g.cx - g.objW / 2, 0, g.cx + g.objW / 2, 0); og.addColorStop(0, '#94A3B8'); og.addColorStop(0.45, '#F1F5F9'); og.addColorStop(1, '#94A3B8');
      c.fillStyle = og; rr(c, g.cx - g.objW / 2, objTop, g.objW, g.objH, 3); c.fill(); c.strokeStyle = '#64748B'; c.lineWidth = 1; c.stroke();
      var yi = Math.max(objTop, surf); if (yi < bot) { c.fillStyle = Lc; c.fillRect(g.cx - g.objW / 2, yi, g.objW, bot - yi); }
      c.strokeStyle = rgba(L[2], 0.9); c.lineWidth = 1; c.beginPath(); c.moveTo(g.x0 + 1, surf); c.lineTo(g.x1 - 1, surf); c.stroke();
      c.strokeStyle = INK; c.lineWidth = 1.3; c.lineJoin = 'round';
      c.beginPath(); c.moveTo(g.x0, g.canT); c.lineTo(g.x0, g.canB); c.lineTo(g.x1, g.canB); c.lineTo(g.x1, g.surf0); c.lineTo(g.x1 + g.spout, g.surf0 + 9); c.stroke();
      c.beginPath(); c.moveTo(g.x1, g.canT); c.lineTo(g.x1, g.surf0 - 7); c.lineTo(g.x1 + g.spout, g.surf0 + 2); c.stroke();
      var lv = legende(c, 'vase à trop-plein', g.cx, g.bench + 20, w);
      /* balance et bécher de récupération sous l'extrémité du bec */
      var bL = g.bc - g.bw / 2;
      c.fillStyle = '#E2E8F0'; c.strokeStyle = '#64748B'; c.lineWidth = 1; rr(c, bL, g.balTop, g.bw, g.balH, 4); c.fill(); c.stroke();
      c.fillStyle = '#CBD5E1'; rr(c, g.bc - g.bw * 0.32, g.balTop - 3, g.bw * 0.64, 3, 1); c.fill();
      c.fillStyle = '#0F172A'; rr(c, g.bc - 26, g.balTop + 3, 52, g.balH - 6, 2); c.fill();
      c.fillStyle = '#4ADE80'; c.font = '9.5px ui-monospace, Menlo, monospace'; c.textAlign = 'center'; c.fillText(fr(mDeb, 1) + ' g', g.bc, g.balTop + g.balH - 5.5);
      var bkB = g.balTop - 3, bkT = bkB - g.bkH, bkL = g.bc - g.bkW / 2, bkR = g.bc + g.bkW / 2;
      var hl = Math.min(1, vMax / 130) * (g.bkH - 10);
      c.fillStyle = GLASS; c.fillRect(bkL, bkT, g.bkW, g.bkH);
      if (hl > 0) { c.fillStyle = Lc; c.fillRect(bkL + 1, bkB - hl, g.bkW - 2, hl); }
      c.strokeStyle = INK; c.lineWidth = 1.2; c.beginPath(); c.moveTo(bkL - 4, bkT - 3); c.quadraticCurveTo(bkL, bkT - 1, bkL, bkT + 5); c.lineTo(bkL, bkB); c.lineTo(bkR, bkB); c.lineTo(bkR, bkT); c.stroke();
      for (var m = 1; m <= 3; m++) { var ym = bkB - m * (g.bkH - 10) / 4; c.strokeStyle = 'rgba(71,85,105,.6)'; c.lineWidth = 0.7; c.beginPath(); c.moveTo(bkR - 9, ym); c.lineTo(bkR - 2, ym); c.stroke(); }
      c.font = '12px system-ui, sans-serif'; var lb = c.measureText('balance tarée').width;
      legende(c, 'balance tarée', g.bc, (g.bc - lb / 2 < lv[1] + 10) ? g.bench + 36 : g.bench + 20, w);   /* sur une seconde ligne si la place manque */
      /* gouttes qui tombent du bec dans le bécher */
      var xd = g.x1 + g.spout + 1, y0d = g.surf0 + 10, ySurf = bkB - hl;
      drops.forEach(function (d) { d.t += dt; if (d.t < 0) { return; } var yd = y0d + d.t * d.t * 900; if (yd < ySurf) { c.fillStyle = rgba(L[2], 0.95); c.beginPath(); c.ellipse(xd, yd, 2.4, 3.2, 0, 0, 2 * Math.PI); c.fill(); } });
      drops = drops.filter(function (d) { return y0d + d.t * d.t * 900 < ySurf; });
      /* lectures et commentaire */
      oP.textContent = fr(P, 2) + ' N'; oF.textContent = fr(Fdyn, 2) + ' N'; oD.textContent = fr(P - Fdyn, 3) + ' N';
      oM.textContent = fr(mDeb, 1) + ' g'; oMg.textContent = fr(mDeb * G / 1000, 3) + ' N';
      msg.innerHTML = f === 0 && vMax === 0 ? 'Dans l\u2019air, le dynamomètre indique le poids de l\u2019objet, P = ' + fr(P, 2) + ' N. Descendez l\u2019objet dans le liquide.'
        : (f > 0 && Math.abs(Vimm - vMax) < 1e-6 ? 'Le dynamomètre indique moins que le poids : la différence P \u2212 F<sub>dyn</sub> est la poussée d\u2019Archimède. Le volume de liquide qui a débordé est égal au volume immergé, et le poids de ce liquide (m \u00d7 g) est exactement égal à la poussée d\u2019Archimède.'
        : 'En remontant l\u2019objet, la poussée diminue et le niveau du vase baisse ; le liquide déjà débordé reste dans le bécher. Videz et remplissez le vase à ras bord pour recommencer.');
    }
    rP.addEventListener('input', function () { draw(0); });
    $$(root, 'input[name="liq"]').forEach(function (x) { x.addEventListener('change', function () { liq = x.value; vMax = 0; drops = []; rP.value = 0; draw(0); }); });
    $(root, '[data-act="reset"]').addEventListener('click', function () { vMax = 0; drops = []; rP.value = 0; draw(0); });
    function setup() { S = canvasCtx(cv); draw(0); }
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(cv); }
    setup(); onResize(setup);
    /* animation des gouttes ; un dernier dessin efface la dernière goutte arrivée */
    (function step(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (visible && drops.length) { draw(dt); if (!drops.length) { draw(0); } }
      requestAnimationFrame(step);
    })(performance.now());
  })();
  /* ================= 2. Débit et effet Venturi ================= */
  (function () {
    var root = document.getElementById('lab-venturi');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rS = $(root, '[data-p="s"]'), rV = $(root, '[data-p="v"]'), oS = $(root, '.out-s'), oV = $(root, '.out-v'), oV2 = $(root, '.out-v2'), oDP = $(root, '.out-dp'), btn = $(root, '[data-act="play"]'), S, parts = [], RHO = 1000;
    for (var i = 0; i < 90; i++) { parts.push({ u: Math.random(), y: Math.random() * 2 - 1 }); }   /* u : abscisse (0 → 1), y : position relative dans la section (−1 → 1) */
    function halfH(u, r) {   /* demi-hauteur du tube : large, étranglement de rapport r au milieu, puis large */
      var H = 1, Hm = r, g = Math.exp(-Math.pow((u - 0.5) / 0.13, 2));
      return H - (H - Hm) * g;
    }
    function draw(dt) {
      if (!S) { return; }
      var r = +rS.value, v1 = +rV.value, v2 = v1 / r, dp = 0.5 * RHO * (v2 * v2 - v1 * v1), c = S.ctx, w = S.w, h = S.h;
      oS.textContent = fr(r, 2); oV.textContent = fr(v1, 1) + ' m\u00b7s\u207b\u00b9'; oV2.textContent = fr(v2, 1) + ' m\u00b7s\u207b\u00b9'; oDP.textContent = fr(dp / 1000, 2) + ' kPa';
      var L = 30, R = w - 30, ym = h * 0.64, Hpx = h * 0.25;
      function X(u) { return L + u * (R - L); }
      c.clearRect(0, 0, w, h);
      /* tube */
      c.fillStyle = 'rgba(96,165,250,.35)'; c.beginPath();
      for (var k = 0; k <= 200; k++) { var u = k / 200; c.lineTo(X(u), ym - halfH(u, r) * Hpx); }
      for (k = 200; k >= 0; k--) { u = k / 200; c.lineTo(X(u), ym + halfH(u, r) * Hpx); }
      c.closePath(); c.fill(); c.strokeStyle = '#475569'; c.lineWidth = 1.6; c.stroke();
      /* lignes de courant */
      c.strokeStyle = 'rgba(22,163,74,.55)'; c.lineWidth = 1.2;
      [-0.7, -0.35, 0, 0.35, 0.7].forEach(function (yy) { c.beginPath(); for (var q = 0; q <= 200; q++) { var uu = q / 200; c.lineTo(X(uu), ym + yy * halfH(uu, r) * Hpx); } c.stroke(); });
      /* particules : vitesse locale inversement proportionnelle à la section (conservation du débit) */
      parts.forEach(function (p) {
        var hh = halfH(p.u, r), vloc = v1 / hh;
        p.u += dt * vloc * 0.05; if (p.u > 1) { p.u -= 1; p.y = Math.random() * 2 - 1; }
        c.fillStyle = '#1D4ED8'; c.beginPath(); c.arc(X(p.u), ym + p.y * 0.9 * hh * Hpx, 2.6, 0, 2 * Math.PI); c.fill();
      });
      /* vecteurs vitesse à l'entrée et au col */
      [[0.12, 1], [0.5, r]].forEach(function (q) { var vv = v1 / q[1]; arrow(c, X(q[0]) - 4, ym, X(q[0]) - 4 + vv * 9, ym, CV, 2.2); });
      txt(c, 'v\u2081', X(0.12), ym - 10, CV, 'italic 500 14px Georgia, serif'); txt(c, 'v\u2082', X(0.5), ym - 10, CV, 'italic 500 14px Georgia, serif');
      /* manomètres : la hauteur de liquide traduit la pression (Bernoulli) */
      [[0.12, 0, 'P\u2081'], [0.5, dp, 'P\u2082'], [0.88, 0, 'P\u2083']].forEach(function (q) {
        var x = X(q[0]), top = ym - halfH(q[0], r) * Hpx, base = 64, hc = Math.max(2, base - q[1] / 1000 * 4);
        c.strokeStyle = '#64748B'; c.lineWidth = 1.4; c.strokeRect(x - 7, top - 90, 14, 90);
        c.fillStyle = 'rgba(96,165,250,.8)'; c.fillRect(x - 6, top - hc, 12, hc);
        txt(c, q[2], x, top - 98, CPR, 'italic 500 14px Georgia, serif');
      });
    }
    [rS, rV].forEach(function (x) { x.addEventListener('input', function () { draw(0); }); });
    function setup() { S = canvasCtx(cv); draw(0); }
    setup(); onResize(setup); loop(cv, btn, draw);
  })();
  /* ================= 3. Lignes de courant autour d'un obstacle ================= */
  (function () {
    var root = document.getElementById('lab-lignes');
    if (!root) { return; }
    var cv = $(root, 'canvas'), cbV = $(root, '[data-p="vec"]'), btn = $(root, '[data-act="play"]'), S, parts = [], Rc = 1;
    /* écoulement potentiel d'un fluide parfait autour d'un cylindre : ψ = U (r − R²/r) sin θ */
    function vel(x, y) {
      var r2 = x * x + y * y, R2 = Rc * Rc;
      if (r2 < R2) { return [0, 0]; }
      var vx = 1 - R2 * (x * x - y * y) / (r2 * r2), vy = -2 * R2 * x * y / (r2 * r2);
      return [vx, vy];
    }
    function seed() { parts = []; for (var i = 0; i < 160; i++) { parts.push([-4 + Math.random() * 8, -2.2 + Math.random() * 4.4]); } }
    function draw(dt) {
      if (!S) { return; }
      var c = S.ctx, w = S.w, h = S.h, k = Math.min(w / 8.4, h / 4.8), cx = w / 2, cy = h / 2;
      function X(x) { return cx + x * k; }
      function Y(y) { return cy - y * k; }
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#EFF6FF'; c.fillRect(0, 0, w, h);
      /* lignes de courant : courbes ψ = constante, obtenues en suivant le champ des vitesses */
      c.strokeStyle = 'rgba(22,163,74,.7)'; c.lineWidth = 1.3;
      for (var y0 = -2.2; y0 <= 2.21; y0 += 0.3) {
        if (Math.abs(y0) < 0.02) { continue; }
        var x = -4.2, y = y0; c.beginPath(); c.moveTo(X(x), Y(y));
        for (var s = 0; s < 900; s++) { var v = vel(x, y), n = Math.hypot(v[0], v[1]) || 1; x += 0.012 * v[0] / n; y += 0.012 * v[1] / n; c.lineTo(X(x), Y(y)); if (x > 4.2) { break; } }
        c.stroke();
      }
      c.beginPath(); c.moveTo(X(-4.2), Y(0)); c.lineTo(X(-Rc), Y(0)); c.moveTo(X(Rc), Y(0)); c.lineTo(X(4.2), Y(0)); c.stroke();
      c.fillStyle = '#94A3B8'; c.beginPath(); c.arc(cx, cy, Rc * k, 0, 2 * Math.PI); c.fill();
      txt(c, 'obstacle', cx, cy + 4, '#1E293B', '500 12px system-ui, sans-serif');
      /* particules de fluide */
      parts.forEach(function (p) {
        var v = vel(p[0], p[1]); p[0] += v[0] * dt * 0.9; p[1] += v[1] * dt * 0.9;
        if (p[0] > 4.3 || p[0] * p[0] + p[1] * p[1] < Rc * Rc) { p[0] = -4.3; p[1] = -2.2 + Math.random() * 4.4; }
        c.fillStyle = '#1D4ED8'; c.beginPath(); c.arc(X(p[0]), Y(p[1]), 2.4, 0, 2 * Math.PI); c.fill();
      });
      if (cbV.checked) {
        for (var gx = -3.6; gx <= 3.61; gx += 0.6) {
          for (var gy = -1.8; gy <= 1.81; gy += 0.6) {
            if (gx * gx + gy * gy < 1.25) { continue; }
            var vv = vel(gx, gy); arrow(c, X(gx), Y(gy), X(gx + vv[0] * 0.32), Y(gy + vv[1] * 0.32), CV, 1.8);
          }
        }
      }
    }
    cbV.addEventListener('change', function () { draw(0); });
    function setup() { S = canvasCtx(cv); draw(0); }
    seed(); setup(); onResize(setup); loop(cv, btn, draw);
  })();
})();
</script>
