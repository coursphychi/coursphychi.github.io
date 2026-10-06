+++
title = "Transformations nucléaires"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour commencer</span><span class="nt-sum">La découverte de la radioactivité</span></summary>
<div class="nt-d-body">
<p><a href="https://www.youtube.com/watch?v=clRcF7emyiM" target="_blank" rel="noopener">Comment Henri Becquerel a découvert la radioactivité «&nbsp;par hasard&nbsp;»</a>.</p>
</div>
</details>

## Diagramme (N, Z) {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Rappel&nbsp;: notation symbolique d'un noyau</p>
<p class="nt-center" style="font-size:1.6em;">$\ce{^{\color{#2A6BC4}A}_{\color{#E11D48}Z} X}$</p>
<ul class="nt-facts">
<li>$\ce{X}$ est le symbole chimique de l'élément&nbsp;;</li>
<li>$\color{#E11D48}Z$ est le nombre de <span class="imp nt-hole">protons</span> du noyau&nbsp;;</li>
<li>$\color{#2A6BC4}A$ est le nombre de <span class="imp nt-hole">nucléons</span> du noyau.</li>
</ul>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarques</p>
<ul class="nt-facts">
<li>$\color{#E11D48}Z$ (le numéro atomique) permet de déterminer <span class="imp nt-hole">la charge</span> du noyau&nbsp;: $Q={\color{#E11D48}Z}\times e$.</li>
<li>$\color{#2A6BC4}A$ (aussi appelé <b>nombre de masse</b>) permet de déterminer approximativement <span class="imp nt-hole">la masse</span> du noyau&nbsp;: $m_\text{noyau}\approx{\color{#2A6BC4}A}\times m_\text{nucléon}$ (car $m_p\approx m_n$).</li>
</ul>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Nombre de neutrons du noyau</p>
<p class="nt-f-math">$${\color{#FDE68A}N} = {\color{#93C5FD}A}-{\color{#FCA5A5}Z}$$</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>On appelle <span class="imp nt-hole">isotopes</span> deux noyaux ayant le même nombre de protons $Z$ mais un nombre différent de neutrons $N$ (ou, ce qui revient au même, un nombre différent de nucléons $A$).</p>
<p>On désigne généralement un isotope par son nom chimique suivi de son nombre $A$&nbsp;: le carbone 14 ou l'uranium 235, par exemple.</p>
</div>

<p class="nt-lead">On peut ranger tous les isotopes connus dans un <b>diagramme $(N,Z)$</b>, avec $Z$ en abscisse et $N$ en ordonnée.</p>

<div class="nt-lab" id="lab-nz">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le diagramme (N, Z)</p>
<canvas style="height:600px; background:#fff; cursor:pointer;" aria-label="Diagramme (N, Z) des noyaux : chaque case est un noyau, coloré selon qu'il est stable ou selon son type de radioactivité"></canvas>
<p class="nt-msg nt-nz-info" aria-live="polite"></p>
<div class="nt-btns">
<button type="button" class="nt-btn" data-nuc="6,8">carbone 14</button>
<button type="button" class="nt-btn" data-nuc="9,9">fluor 18</button>
<button type="button" class="nt-btn" data-nuc="19,21">potassium 40</button>
<button type="button" class="nt-btn" data-nuc="27,33">cobalt 60</button>
<button type="button" class="nt-btn" data-nuc="53,78">iode 131</button>
<button type="button" class="nt-btn" data-nuc="88,138">radium 226</button>
<button type="button" class="nt-btn" data-nuc="92,146">uranium 238</button>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="all"><i class="fa-solid fa-expand"></i>&nbsp; Vue d'ensemble</button></div>
<p class="nt-note">Environ 1&nbsp;250 noyaux (les stables et les radioactifs répertoriés par la base de données de la Commission internationale de protection radiologique, CIPR 107). Cliquez sur un noyau&nbsp;: le diagramme zoome sur sa chaîne de désintégration, jusqu'à un noyau stable (en suivant le mode de désintégration principal&nbsp;; les états excités métastables, comme le protactinium 234m de la chaîne de l'uranium 238, ne sont pas représentés).</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>On constate que les noyaux <span class="imp nt-hole">stables</span> sont très minoritaires et se concentrent dans une <span class="imp nt-hole">vallée de la stabilité</span> (autour de $N=Z$) pour les petits noyaux, puis se décalent vers $N>Z$.</p>
<p>À partir du bismuth ($Z=83$), il n'y a plus d'isotopes stables.</p>
<p class="nt-note">Le bismuth 209 a longtemps été considéré comme stable&nbsp;: sa radioactivité α n'a été détectée qu'en 2003, avec une demi-vie d'environ $2\times10^{19}$ ans, un milliard de fois l'âge de l'Univers.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Vidéo et diagramme complet</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://www.youtube.com/embed/VZHpAwSGYZE?start=0&end=573&autoplay=1" target="_blank" rel="noopener">Magnifique vidéo du CEA sur la vallée de la stabilité</a> (le lien s'arrête à 9'33")&nbsp;;</li>
<li>Pour explorer un diagramme complet (plus de 3&nbsp;000 noyaux connus)&nbsp;: <a href="https://physique.ostralo.net/diagramme_NZ/" target="_blank" rel="noopener">le diagramme (N, Z) d'Ostralo</a>.</li>
</ul>
</div>
</details>

## Transformations nucléaires {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Les noyaux instables subissent des <span class="imp nt-hole">désintégrations radioactives</span> mettant en jeu une ou plusieurs <span class="imp nt-hole">transformation(s) nucléaire(s)</span> du noyau visant à le rapprocher de la vallée de la stabilité.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Lois de conservation</p>
<p>Lors d'une <b>transformation nucléaire</b>, il y a&nbsp;:</p>
<ul class="nt-facts">
<li><span class="imp nt-hole">conservation de la charge</span> (la somme des $Z$ se conserve)&nbsp;;</li>
<li><span class="imp nt-hole">conservation du nombre de nucléons</span> (la somme des $A$ se conserve).</li>
</ul>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exemple</p>
<p>Lorsqu'un noyau d'uranium 235 absorbe un neutron, il peut fissionner en deux noyaux fils dont l'un est le strontium 94, tout en émettant 2 neutrons. Déterminer l'autre noyau fils.</p>
<p class="nt-center">${}^{\square}_{\square}\mathrm{n} + \ce{^\square_\square U} \longrightarrow \ce{^\square_\square Sr} + {}^{\square}_{\square}\mathrm{?} + 2\,{}^{\square}_{\square}\mathrm{n}$</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p class="nt-center">${}^{1}_{0}\mathrm{n} + \ce{^{235}_{92}U} \longrightarrow \ce{^{94}_{38}Sr} + {}^{A}_{Z}\mathrm{X} + 2\,{}^{1}_{0}\mathrm{n}$</p>
<p>Conservation du nombre de nucléons&nbsp;: $1 + 235 = 94 + A + 2$, donc $A = 140$.</p>
<p>Conservation de la charge&nbsp;: $0 + 92 = 38 + Z + 0$, donc $Z = 54$&nbsp;: c'est le xénon.</p>
<p class="nt-center">${}^{1}_{0}\mathrm{n} + \ce{^{235}_{92}U} \longrightarrow \ce{^{94}_{38}Sr} + \ce{^{140}_{54}Xe} + 2\,{}^{1}_{0}\mathrm{n}$</p>
</div>
</details>

## Types de radioactivité {.nt-h2}

<p class="nt-lead">Lors d'une désintégration radioactive, différentes transformations nucléaires peuvent permettre de rapprocher le noyau fils de la stabilité. Historiquement, on a classé ces différents types de radioactivité en fonction du rayonnement émis&nbsp;: <b style="color:#D97706;">α</b>, <b style="color:#2A6BC4;">β<sup>−</sup></b>, <b style="color:#DB2777;">β<sup>+</sup></b> et <b style="color:#CA8A04;">γ</b>.</p>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Radioactivité alpha $(\alpha)$</p>
<p class="nt-center">$\ce{^{238}_{92} U -> ^{234}_{90} Th} + {\color{#D97706}\alpha}$</p>
<p>Par conservation de la charge et du nombre de nucléons, déterminer la nature des rayons alpha.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Radioactivité alpha $(\alpha)$</p>
<p>La <b>radioactivité alpha</b> correspond à l'émission de <span class="imp nt-hole">noyaux d'hélium $\ce{^4_2He}$</span> (particule α). Elle concerne les noyaux lourds.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Radioactivité bêta moins $(\beta^-)$</p>
<p class="nt-center">$\ce{^{14}_{6} C -> ^{14}_{7} N} + {\color{#2A6BC4}\beta^-} + \ce{^0_0\bar{\nu}_e}$</p>
<p>Par conservation de la charge et du nombre de nucléons, déterminer la nature des rayons $\beta^-$.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Radioactivité bêta moins $(\beta^-)$</p>
<p>La radioactivité $\beta^-$ correspond à la transformation d'un neutron en proton en émettant <span class="imp nt-hole">un électron $\ce{^{\;\;0}_{-1}e}$</span> (particule $\beta^-$), accompagné d'un antineutrino.</p>
<p>Elle concerne des noyaux comportant trop de <span class="imp nt-hole">neutrons</span>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Radioactivité bêta plus $(\beta^+)$</p>
<p class="nt-center">$\ce{^{18}_{9} F -> ^{18}_{8} O} + {\color{#DB2777}\beta^+} + \ce{^0_0\nu_e}$</p>
<p>Par conservation de la charge et du nombre de nucléons, déterminer la nature des rayons $\beta^+$.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Radioactivité bêta plus $(\beta^+)$</p>
<p>La radioactivité $\beta^+$ correspond à la transformation d'un proton en neutron en émettant <span class="imp nt-hole">un positon $\ce{^{\;\;0}_{+1}e}$</span> (antiparticule de l'électron), accompagné d'un neutrino.</p>
<p>Elle concerne des noyaux comportant trop de <span class="imp nt-hole">protons</span>.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Radioactivité gamma $(\gamma)$</p>
<p class="nt-center">$\ce{^{60}_{28} Ni^* -> ^{60}_{28} Ni} + {\color{#CA8A04}\gamma}$</p>
<p>Par conservation de la charge et du nombre de nucléons, déterminer la nature des rayons gamma.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Radioactivité gamma $(\gamma)$</p>
<p>La radioactivité gamma correspond à la <span class="imp nt-hole">désexcitation d'un noyau</span> en émettant un <span class="imp nt-hole">photon</span> (généralement dans le domaine électromagnétique des rayons gamma). Elle accompagne souvent une désintégration α ou β, qui laisse le noyau fils dans un état excité (noté $^*$).</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque&nbsp;: d'autres désintégrations</p>
<p>Les noyaux très éloignés de la vallée de stabilité peuvent aussi se désintégrer en émettant <b>un ou plusieurs neutrons</b> (ou protons). C'est le cas de certains produits de fission très riches en neutrons&nbsp;: après une désintégration $\beta^-$, ils émettent un neutron avec un léger retard. Ces «&nbsp;neutrons retardés&nbsp;» sont essentiels au pilotage des réacteurs nucléaires.</p>
<p>Enfin, les noyaux les plus lourds peuvent subir une <b>fission spontanée</b>&nbsp;: ils se cassent d'eux-mêmes en deux noyaux plus légers, en libérant quelques neutrons.</p>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 660 360" role="img" aria-label="Schéma de désintégration du cobalt 60 : désintégration bêta moins vers un niveau excité du nickel 60 à 2,51 MeV, puis deux émissions gamma successives de 1,17 MeV et 1,33 MeV jusqu'à l'état fondamental"><line x1="46" y1="336" x2="46.0" y2="36.0" stroke="var(--slate)" stroke-width="1.6"/><polygon points="46.0,28.0 51.0,38.0 41.0,38.0" fill="var(--slate)"/><text x="40" y="22" font-size="12" fill="var(--slate)" font-weight="700" text-anchor="start">énergie</text><line x1="41" y1="318.0" x2="51" y2="318.0" stroke="var(--slate)" stroke-width="1.4"/><text x="58" y="322.0" font-size="11" fill="var(--slate)">0</text><line x1="41" y1="195.4" x2="51" y2="195.4" stroke="var(--slate)" stroke-width="1.4"/><text x="58" y="199.4" font-size="11" fill="var(--slate)">1,33 MeV</text><line x1="41" y1="87.4" x2="51" y2="87.4" stroke="var(--slate)" stroke-width="1.4"/><text x="58" y="91.4" font-size="11" fill="var(--slate)">2,51 MeV</text><line x1="41" y1="58.2" x2="51" y2="58.2" stroke="var(--slate)" stroke-width="1.4"/><text x="58" y="62.2" font-size="11" fill="var(--slate)">2,82 MeV</text><line x1="130" y1="58.2" x2="260" y2="58.2" stroke="#1E293B" stroke-width="3.5" stroke-linecap="round"/><text x="195" y="48.2" font-size="14" text-anchor="middle" fill="var(--ink)" font-weight="700">cobalt 60</text><line x1="330" y1="87.4" x2="600" y2="87.4" stroke="#1E293B" stroke-width="3.5" stroke-linecap="round"/><line x1="330" y1="195.4" x2="600" y2="195.4" stroke="#1E293B" stroke-width="3.5" stroke-linecap="round"/><line x1="330" y1="318.0" x2="600" y2="318.0" stroke="#1E293B" stroke-width="4.5" stroke-linecap="round"/><line x1="260" y1="58.2" x2="600" y2="58.2" stroke="var(--muted)" stroke-dasharray="3 4"/><line x1="130" y1="87.4" x2="330" y2="87.4" stroke="var(--muted)" stroke-dasharray="3 4"/><line x1="130" y1="195.4" x2="330" y2="195.4" stroke="var(--muted)" stroke-dasharray="3 4"/><line x1="130" y1="318.0" x2="330" y2="318.0" stroke="var(--muted)" stroke-dasharray="3 4"/><line x1="230" y1="62.19200000000001" x2="344.1" y2="82.1" stroke="#2A6BC4" stroke-width="2.6"/><polygon points="352.0,83.4 341.3,86.7 343.0,76.8" fill="#2A6BC4"/><text x="262" y="92.2" font-size="14" fill="#2A6BC4" font-weight="700">β⁻</text><text x="604" y="105.4" font-size="12" text-anchor="end" fill="var(--ink)" font-weight="700">nickel 60 excité</text><text x="604" y="213.4" font-size="12" text-anchor="end" fill="var(--ink)" font-weight="700">nickel 60 excité</text><text x="604" y="338.0" font-size="12" text-anchor="end" fill="var(--ink)" font-weight="700">nickel 60 (état fondamental)</text><polyline points="398.7,91 401.6,92 404.1,93 405.7,94 405.9,95 404.9,96 402.7,97 399.8,98 397.1,99 395.0,100 394.0,101 394.4,102 396.1,103 398.7,104 401.6,105 404.1,106 405.7,107 405.9,108 404.9,109 402.7,110 399.8,111 397.1,112 395.0,113 394.0,114 394.4,115 396.1,116 398.7,117 401.6,118 404.1,119 405.7,120 405.9,121 404.9,122 402.7,123 399.8,124 397.1,125 395.0,126 394.0,127 394.4,128 396.1,129 398.7,130 401.6,131 404.1,132 405.7,133 405.9,134 404.9,135 402.7,136 399.8,137 397.1,138 395.0,139 394.0,140 394.4,141 396.1,142 398.7,143 401.6,144 404.1,145 405.7,146 405.9,147 404.9,148 402.7,149 399.8,150 397.1,151 395.0,152 394.0,153 394.4,154 396.1,155 398.7,156 401.6,157 404.1,158 405.7,159 405.9,160 404.9,161 402.7,162 399.8,163 397.1,164 395.0,165 394.0,166 394.4,167 396.1,168 398.7,169 401.6,170 404.1,171 405.7,172 405.9,173 404.9,174 402.7,175 399.8,176 397.1,177 395.0,178 394.0,179 394.4,180" fill="none" stroke="#CA8A04" stroke-width="2.6" stroke-linejoin="round"/><polygon points="400.0,191.4 394.0,179.4 406.0,179.4" fill="#CA8A04"/><text x="414" y="146.4" font-size="14" fill="#CA8A04" font-weight="700">γ</text><text x="428" y="146.4" font-size="12" fill="#CA8A04">(1,17 MeV)</text><polyline points="478.9,199 481.8,200 484.3,201 485.7,202 485.9,203 484.7,204 482.4,205 479.6,206 476.9,207 474.8,208 474.0,209 474.5,210 476.3,211 478.9,212 481.8,213 484.3,214 485.7,215 485.9,216 484.7,217 482.4,218 479.6,219 476.9,220 474.8,221 474.0,222 474.5,223 476.3,224 478.9,225 481.8,226 484.3,227 485.7,228 485.9,229 484.7,230 482.4,231 479.6,232 476.9,233 474.8,234 474.0,235 474.5,236 476.3,237 478.9,238 481.8,239 484.3,240 485.7,241 485.9,242 484.7,243 482.4,244 479.6,245 476.9,246 474.8,247 474.0,248 474.5,249 476.3,250 478.9,251 481.8,252 484.3,253 485.7,254 485.9,255 484.7,256 482.4,257 479.6,258 476.9,259 474.8,260 474.0,261 474.5,262 476.3,263 478.9,264 481.8,265 484.3,266 485.7,267 485.9,268 484.7,269 482.4,270 479.6,271 476.9,272 474.8,273 474.0,274 474.5,275 476.3,276 478.9,277 481.8,278 484.3,279 485.7,280 485.9,281 484.7,282 482.4,283 479.6,284 476.9,285 474.8,286 474.0,287 474.5,288 476.3,289 478.9,290 481.8,291 484.3,292 485.7,293 485.9,294 484.7,295 482.4,296 479.6,297 476.9,298 474.8,299 474.0,300 474.5,301 476.3,302 478.9,303" fill="none" stroke="#CA8A04" stroke-width="2.6" stroke-linejoin="round"/><polygon points="480.0,314.0 474.0,302.0 486.0,302.0" fill="#CA8A04"/><text x="494" y="261.7" font-size="14" fill="#CA8A04" font-weight="700">γ</text><text x="508" y="261.7" font-size="12" fill="#CA8A04">(1,33 MeV)</text></svg>

<p class="nt-cap">Le cobalt 60 se désintègre ($\beta^-$) en un nickel 60 excité, qui revient à son état fondamental en émettant deux photons γ successifs. L'énergie est typiquement de l'ordre du MeV ($\approx\pu{1E-13 J}$).</p>

<svg class="nt-svg nt-svg-m" viewBox="0 0 700 320" role="img" aria-label="Pouvoir de pénétration : les particules alpha sont arrêtées par une feuille de papier, les particules bêta par quelques millimètres d'aluminium, les rayons gamma sont fortement atténués par plusieurs centimètres de plomb, et les neutrons sont arrêtés par une grande épaisseur d'eau ou de béton"><rect x="160" y="28" width="6" height="250" fill="#F8FAFC" stroke="var(--slate)"/><rect x="270" y="28" width="16" height="250" fill="#CBD5E1" stroke="var(--slate)"/><rect x="390" y="28" width="56" height="250" fill="#64748B" stroke="var(--slate)"/><rect x="540" y="28" width="100" height="250" fill="#BAE6FD" stroke="var(--slate)"/><text x="163" y="296" font-size="12" text-anchor="middle" fill="var(--slate)" font-weight="700">papier</text><text x="278" y="296" font-size="12" text-anchor="middle" fill="var(--slate)" font-weight="700">aluminium</text><text x="278" y="310" font-size="11" text-anchor="middle" fill="var(--slate)">(quelques mm)</text><text x="418" y="296" font-size="12" text-anchor="middle" fill="var(--slate)" font-weight="700">plomb</text><text x="418" y="310" font-size="11" text-anchor="middle" fill="var(--slate)">(plusieurs cm)</text><text x="590" y="296" font-size="12" text-anchor="middle" fill="var(--slate)" font-weight="700">eau, béton</text><text x="590" y="310" font-size="11" text-anchor="middle" fill="var(--slate)">(plusieurs dizaines de cm)</text><text x="22" y="66" font-size="17" fill="#E11D48" font-weight="700">α</text><line x1="40" y1="60" x2="150.0" y2="60.0" stroke="#E11D48" stroke-width="3"/><polygon points="158.0,60.0 148.0,65.0 148.0,55.0" fill="#E11D48"/><text x="22" y="126" font-size="17" fill="#2A6BC4" font-weight="700">β</text><line x1="40" y1="120" x2="260.0" y2="120.0" stroke="#2A6BC4" stroke-width="3"/><polygon points="268.0,120.0 258.0,125.0 258.0,115.0" fill="#2A6BC4"/><text x="22" y="186" font-size="17" fill="#CA8A04" font-weight="700">γ</text><polyline points="40.0,180.0 41.0,182.2 42.0,183.9 43.0,184.9 44.0,184.9 45.0,183.9 46.0,182.2 47.0,180.0 48.0,177.8 49.0,176.1 50.0,175.1 51.0,175.1 52.0,176.1 53.0,177.8 54.0,180.0 55.0,182.2 56.0,183.9 57.0,184.9 58.0,184.9 59.0,183.9 60.0,182.2 61.0,180.0 62.0,177.8 63.0,176.1 64.0,175.1 65.0,175.1 66.0,176.1 67.0,177.8 68.0,180.0 69.0,182.2 70.0,183.9 71.0,184.9 72.0,184.9 73.0,183.9 74.0,182.2 75.0,180.0 76.0,177.8 77.0,176.1 78.0,175.1 79.0,175.1 80.0,176.1 81.0,177.8 82.0,180.0 83.0,182.2 84.0,183.9 85.0,184.9 86.0,184.9 87.0,183.9 88.0,182.2 89.0,180.0 90.0,177.8 91.0,176.1 92.0,175.1 93.0,175.1 94.0,176.1 95.0,177.8 96.0,180.0 97.0,182.2 98.0,183.9 99.0,184.9 100.0,184.9 101.0,183.9 102.0,182.2 103.0,180.0 104.0,177.8 105.0,176.1 106.0,175.1 107.0,175.1 108.0,176.1 109.0,177.8 110.0,180.0 111.0,182.2 112.0,183.9 113.0,184.9 114.0,184.9 115.0,183.9 116.0,182.2 117.0,180.0 118.0,177.8 119.0,176.1 120.0,175.1 121.0,175.1 122.0,176.1 123.0,177.8 124.0,180.0 125.0,182.2 126.0,183.9 127.0,184.9 128.0,184.9 129.0,183.9 130.0,182.2 131.0,180.0 132.0,177.8 133.0,176.1 134.0,175.1 135.0,175.1 136.0,176.1 137.0,177.8 138.0,180.0 139.0,182.2 140.0,183.9 141.0,184.9 142.0,184.9 143.0,183.9 144.0,182.2 145.0,180.0 146.0,177.8 147.0,176.1 148.0,175.1 149.0,175.1 150.0,176.1 151.0,177.8 152.0,180.0 153.0,182.2 154.0,183.9 155.0,184.9 156.0,184.9 157.0,183.9 158.0,182.2 159.0,180.0 160.0,177.8 161.0,176.1 162.0,175.1 163.0,175.1 164.0,176.1 165.0,177.8 166.0,180.0 167.0,182.2 168.0,183.9 169.0,184.9 170.0,184.9 171.0,183.9 172.0,182.2 173.0,180.0 174.0,177.8 175.0,176.1 176.0,175.1 177.0,175.1 178.0,176.1 179.0,177.8 180.0,180.0 181.0,182.2 182.0,183.9 183.0,184.9 184.0,184.9 185.0,183.9 186.0,182.2 187.0,180.0 188.0,177.8 189.0,176.1 190.0,175.1 191.0,175.1 192.0,176.1 193.0,177.8 194.0,180.0 195.0,182.2 196.0,183.9 197.0,184.9 198.0,184.9 199.0,183.9 200.0,182.2 201.0,180.0 202.0,177.8 203.0,176.1 204.0,175.1 205.0,175.1 206.0,176.1 207.0,177.8 208.0,180.0 209.0,182.2 210.0,183.9 211.0,184.9 212.0,184.9 213.0,183.9 214.0,182.2 215.0,180.0 216.0,177.8 217.0,176.1 218.0,175.1 219.0,175.1 220.0,176.1 221.0,177.8 222.0,180.0 223.0,182.2 224.0,183.9 225.0,184.9 226.0,184.9 227.0,183.9 228.0,182.2 229.0,180.0 230.0,177.8 231.0,176.1 232.0,175.1 233.0,175.1 234.0,176.1 235.0,177.8 236.0,180.0 237.0,182.2 238.0,183.9 239.0,184.9 240.0,184.9 241.0,183.9 242.0,182.2 243.0,180.0 244.0,177.8 245.0,176.1 246.0,175.1 247.0,175.1 248.0,176.1 249.0,177.8 250.0,180.0 251.0,182.2 252.0,183.9 253.0,184.9 254.0,184.9 255.0,183.9 256.0,182.2 257.0,180.0 258.0,177.8 259.0,176.1 260.0,175.1 261.0,175.1 262.0,176.1 263.0,177.8 264.0,180.0 265.0,182.2 266.0,183.9 267.0,184.9 268.0,184.9 269.0,183.9 270.0,182.2 271.0,180.0 272.0,177.8 273.0,176.1 274.0,175.1 275.0,175.1 276.0,176.1 277.0,177.8 278.0,180.0 279.0,182.2 280.0,183.9 281.0,184.9 282.0,184.9 283.0,183.9 284.0,182.2 285.0,180.0 286.0,177.8 287.0,176.1 288.0,175.1 289.0,175.1 290.0,176.1 291.0,177.8 292.0,180.0 293.0,182.2 294.0,183.9 295.0,184.9 296.0,184.9 297.0,183.9 298.0,182.2 299.0,180.0 300.0,177.8 301.0,176.1 302.0,175.1 303.0,175.1 304.0,176.1 305.0,177.8 306.0,180.0 307.0,182.2 308.0,183.9 309.0,184.9 310.0,184.9 311.0,183.9 312.0,182.2 313.0,180.0 314.0,177.8 315.0,176.1 316.0,175.1 317.0,175.1 318.0,176.1 319.0,177.8 320.0,180.0 321.0,182.2 322.0,183.9 323.0,184.9 324.0,184.9 325.0,183.9 326.0,182.2 327.0,180.0 328.0,177.8 329.0,176.1 330.0,175.1 331.0,175.1 332.0,176.1 333.0,177.8 334.0,180.0 335.0,182.2 336.0,183.9 337.0,184.9 338.0,184.9 339.0,183.9 340.0,182.2 341.0,180.0 342.0,177.8 343.0,176.1 344.0,175.1 345.0,175.1 346.0,176.1 347.0,177.8 348.0,180.0 349.0,182.2 350.0,183.9 351.0,184.9 352.0,184.9 353.0,183.9 354.0,182.2 355.0,180.0 356.0,177.8 357.0,176.1 358.0,175.1 359.0,175.1 360.0,176.1 361.0,177.8 362.0,180.0 363.0,182.2 364.0,183.9 365.0,184.9 366.0,184.9 367.0,183.9 368.0,182.2 369.0,180.0 370.0,177.8 371.0,176.1 372.0,175.1 373.0,175.1 374.0,176.1 375.0,177.8 376.0,180.0 377.0,182.2 378.0,183.9" fill="none" stroke="#CA8A04" stroke-width="2.4"/><polygon points="388.0,180.0 378.0,185.0 378.0,175.0" fill="#CA8A04"/><polyline points="448.0,180.0 449.0,181.3 450.0,182.3 451.0,182.9 452.0,182.9 453.0,182.3 454.0,181.3 455.0,180.0 456.0,178.7 457.0,177.7 458.0,177.1 459.0,177.1 460.0,177.7 461.0,178.7 462.0,180.0 463.0,181.3 464.0,182.3 465.0,182.9 466.0,182.9 467.0,182.3 468.0,181.3 469.0,180.0 470.0,178.7 471.0,177.7 472.0,177.1 473.0,177.1 474.0,177.7 475.0,178.7 476.0,180.0 477.0,181.3 478.0,182.3 479.0,182.9 480.0,182.9 481.0,182.3 482.0,181.3 483.0,180.0 484.0,178.7 485.0,177.7 486.0,177.1 487.0,177.1 488.0,177.7 489.0,178.7 490.0,180.0 491.0,181.3 492.0,182.3 493.0,182.9 494.0,182.9 495.0,182.3 496.0,181.3 497.0,180.0 498.0,178.7 499.0,177.7 500.0,177.1 501.0,177.1 502.0,177.7 503.0,178.7 504.0,180.0 505.0,181.3 506.0,182.3 507.0,182.9 508.0,182.9 509.0,182.3 510.0,181.3 511.0,180.0 512.0,178.7 513.0,177.7 514.0,177.1 515.0,177.1 516.0,177.7 517.0,178.7 518.0,180.0 519.0,181.3 520.0,182.3 521.0,182.9 522.0,182.9 523.0,182.3 524.0,181.3 525.0,180.0 526.0,178.7 527.0,177.7 528.0,177.1 529.0,177.1 530.0,177.7 531.0,178.7 532.0,180.0 533.0,181.3 534.0,182.3 535.0,182.9 536.0,182.9 537.0,182.3 538.0,181.3 539.0,180.0 540.0,178.7 541.0,177.7 542.0,177.1 543.0,177.1 544.0,177.7 545.0,178.7 546.0,180.0 547.0,181.3 548.0,182.3 549.0,182.9 550.0,182.9 551.0,182.3 552.0,181.3 553.0,180.0 554.0,178.7 555.0,177.7 556.0,177.1 557.0,177.1 558.0,177.7 559.0,178.7 560.0,180.0 561.0,181.3 562.0,182.3 563.0,182.9 564.0,182.9 565.0,182.3 566.0,181.3 567.0,180.0 568.0,178.7 569.0,177.7 570.0,177.1 571.0,177.1 572.0,177.7 573.0,178.7 574.0,180.0 575.0,181.3 576.0,182.3 577.0,182.9 578.0,182.9 579.0,182.3 580.0,181.3 581.0,180.0 582.0,178.7 583.0,177.7 584.0,177.1 585.0,177.1 586.0,177.7 587.0,178.7 588.0,180.0 589.0,181.3 590.0,182.3 591.0,182.9 592.0,182.9 593.0,182.3 594.0,181.3 595.0,180.0 596.0,178.7 597.0,177.7 598.0,177.1 599.0,177.1 600.0,177.7 601.0,178.7 602.0,180.0 603.0,181.3 604.0,182.3 605.0,182.9 606.0,182.9 607.0,182.3 608.0,181.3 609.0,180.0 610.0,178.7 611.0,177.7 612.0,177.1 613.0,177.1 614.0,177.7 615.0,178.7 616.0,180.0 617.0,181.3 618.0,182.3 619.0,182.9 620.0,182.9 621.0,182.3 622.0,181.3 623.0,180.0 624.0,178.7 625.0,177.7 626.0,177.1 627.0,177.1 628.0,177.7 629.0,178.7 630.0,180.0 631.0,181.3 632.0,182.3 633.0,182.9 634.0,182.9 635.0,182.3 636.0,181.3 637.0,180.0 638.0,178.7 639.0,177.7 640.0,177.1 641.0,177.1 642.0,177.7 643.0,178.7 644.0,180.0 645.0,181.3 646.0,182.3 647.0,182.9 648.0,182.9 649.0,182.3 650.0,181.3 651.0,180.0 652.0,178.7 653.0,177.7 654.0,177.1 655.0,177.1 656.0,177.7 657.0,178.7 658.0,180.0 659.0,181.3 660.0,182.3 661.0,182.9 662.0,182.9 663.0,182.3 664.0,181.3 665.0,180.0 666.0,178.7 667.0,177.7 668.0,177.1 669.0,177.1 670.0,177.7 671.0,178.7 672.0,180.0 673.0,181.3 674.0,182.3 675.0,182.9" fill="none" stroke="#CA8A04" stroke-width="1.5" opacity=".45"/><text x="22" y="246" font-size="17" fill="#475569" font-weight="700">n</text><line x1="40" y1="240" x2="380.0" y2="240.0" stroke="#475569" stroke-width="3"/><polygon points="388.0,240.0 378.0,245.0 378.0,235.0" fill="#475569"/><line x1="448" y1="240" x2="530" y2="240" stroke="#475569" stroke-width="3"/><polygon points="538.0,240.0 528.0,245.0 528.0,235.0" fill="#475569"/><text x="70" y="52" font-size="11" fill="#E11D48">noyaux d'hélium</text><text x="70" y="112" font-size="11" fill="#2A6BC4">électrons ou positons</text><text x="70" y="168" font-size="11" fill="#A16207">photons</text><text x="70" y="232" font-size="11" fill="#475569">neutrons</text></svg>

<p class="nt-cap">Les rayonnements n'ont pas du tout le même pouvoir de pénétration&nbsp;: les particules α sont arrêtées par une feuille de papier (ou quelques centimètres d'air), les particules β par quelques millimètres d'aluminium, et les rayons γ ne sont qu'atténués, même par plusieurs centimètres de plomb. Les neutrons, sans charge, traversent bien le plomb&nbsp;; on les arrête avec de grandes épaisseurs de matériaux riches en hydrogène, comme l'eau ou le béton.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Retour au diagramme (N, Z)</p>
<p>Dans le diagramme $(N,Z)$, on voit les trois types à l'œuvre&nbsp;: les noyaux $\beta^-$ (trop de neutrons) sont <span class="imp nt-hole">au-dessus</span> de la vallée de stabilité, les noyaux $\beta^+$ (trop de protons) <span class="imp nt-hole">en dessous</span>, et les noyaux $\alpha$ parmi les <span class="imp nt-hole">plus lourds</span>. Chaque désintégration rapproche le noyau fils de la vallée&nbsp;: cliquez sur un noyau du diagramme pour suivre sa chaîne jusqu'à un noyau stable.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Vidéos sur des chambres à brouillard</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><a href="https://www.youtube.com/watch?v=i15ef618DP0" target="_blank" rel="noopener">Sans source</a>&nbsp;;</li>
<li><a href="https://www.youtube.com/watch?v=1_zwLuNJ5Ck" target="_blank" rel="noopener">Avec sources</a>.</li>
</ul>
<p><b>Le principe.</b> Une chambre à brouillard contient de l'air saturé de vapeur d'alcool, refroidi par le bas&nbsp;: la vapeur est sur le point de se condenser. En traversant l'air, une particule ionisante arrache des électrons aux molécules sur son passage&nbsp;; ces ions servent de germes de condensation, et un fin sillage de gouttelettes matérialise sa trajectoire pendant une fraction de seconde. Les particules α laissent des traces courtes et épaisses, les électrons des traces fines et sinueuses, et les muons venus des rayons cosmiques de longues traces fines et rectilignes.</p>
<p><b>La recette.</b></p>
<ol class="nt-steps">
<li><p>Prendre une boîte transparente (petit aquarium, boîte en plastique) et coller une bande de feutre ou d'éponge sur le fond, qui sera en haut une fois la boîte retournée.</p></li>
<li><p>Imbiber généreusement le feutre d'alcool isopropylique.</p></li>
<li><p>Poser la boîte, ouverture vers le bas, sur une plaque métallique peinte en noir, elle-même posée sur de la carboglace (−78&nbsp;°C).</p></li>
<li><p>Attendre une dizaine de minutes, dans la pénombre, puis éclairer horizontalement près du fond avec une lampe puissante&nbsp;: les traces apparaissent juste au-dessus de la plaque.</p></li>
</ol>
<p class="nt-note">Sécurité&nbsp;: manipuler la carboglace avec des gants (brûlures par le froid), aérer la pièce, et tenir l'alcool isopropylique, très inflammable, à l'écart de toute flamme.</p>
</div>
</details>

## Loi de décroissance radioactive {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Un noyau radioactif a une certaine probabilité $\lambda\,\mathrm{d}t$ de se désintégrer pendant le prochain petit laps de temps $\mathrm{d}t$ (avec $\mathrm{d}t \ll 1/\lambda$).</p>
<p>$\lambda$ (en $\pu{s^-1}$) est la <span class="imp nt-hole">constante radioactive</span>. Elle est <span class="imp nt-hole">indépendante du temps</span>&nbsp;!</p>
<p>Après 1&nbsp;s ou 1&nbsp;000 ans, la probabilité pour un noyau de se désintégrer pendant les prochains $\mathrm{d}t$ vaut toujours $\lambda\,\mathrm{d}t$&nbsp;: un noyau ne «&nbsp;vieillit&nbsp;» pas.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Tous les noyaux d'un même isotope ont la même constante radioactive $\lambda$, et donc la même probabilité de se désintégrer pendant le prochain laps de temps infinitésimal $\mathrm{d}t$.</p>
<p>La désintégration d'un noyau radioactif est donc un phénomène <span class="imp nt-hole">aléatoire</span>, et l'évolution d'une population de noyaux suit une loi <span class="imp nt-hole">statistique</span>.</p>
</div>

<p class="nt-lead">Soit $N(t)$ la population de noyaux non désintégrés à un instant $t$. La variation $\mathrm{d}N=N(t+\mathrm{d}t)-N(t)$ de la population pendant le laps de temps infinitésimal $\mathrm{d}t$ vaut&nbsp;:</p>

<p class="nt-center">$\mathrm{d}N=-N(t)\,\lambda\,\mathrm{d}t \qquad \text{soit} \qquad \dfrac{\mathrm{d}N}{\mathrm{d}t} =-\lambda N(t)$</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Équation différentielle</p>
<p>On reconnaît une <span class="imp nt-hole">équation différentielle</span> linéaire homogène <span class="imp nt-hole">du premier ordre</span> à coefficient constant&nbsp;: elle lie la fonction $N(t)$ à sa dérivée première. Ses solutions sont de la forme&nbsp;:</p>
<p class="nt-center">$N(t)=C\,\mathrm{e}^{-\lambda t}$</p>
</div>

<details class="nt-d nt-plus" id="memo-exp">
<summary><span class="nt-tag"><i class="fa-solid fa-square-root-variable"></i>Mémo maths</span><span class="nt-sum">Exponentielle et logarithme népérien</span></summary>
<div class="nt-d-body">
<p>$\mathrm{e}^x = \exp(x)$ est la <b>fonction exponentielle</b>&nbsp;: elle est égale à sa propre dérivée, $\left(\mathrm{e}^{x}\right)' = \mathrm{e}^{x}$. Plus généralement, pour une fonction $u$ dérivable, $\left(\mathrm{e}^{u}\right)' = u'\,\mathrm{e}^{u}$&nbsp;; par exemple $\left(\mathrm{e}^{-\lambda t}\right)' = -\lambda\,\mathrm{e}^{-\lambda t}$.</p>
<p>Sa fonction réciproque est le <b>logarithme népérien</b>, noté $\ln$&nbsp;: $\ln\left(\mathrm{e}^x\right)=x$ et $\mathrm{e}^{\ln x} = x$.</p>
<ul class="nt-facts">
<li>$\mathrm{e}^0 = 1$ et $\ln(1) = 0$&nbsp;;</li>
<li>$\ln(a\times b) = \ln a + \ln b$ et $\ln\left(\dfrac ab\right) = \ln a - \ln b$&nbsp;;</li>
<li>$\ln(2) \approx 0{,}69$&nbsp;;</li>
<li>à la calculatrice&nbsp;: touches <kbd>e<sup>x</sup></kbd> et <kbd>ln</kbd> (à ne pas confondre avec <kbd>10<sup>x</sup></kbd> et <kbd>log</kbd>).</li>
</ul>
<p><b>Vérification</b>&nbsp;: si $N(t) = C\,\mathrm{e}^{-\lambda t}$, alors $\dfrac{\mathrm{d}N}{\mathrm{d}t} = -\lambda C\,\mathrm{e}^{-\lambda t} = -\lambda N(t)$&nbsp;: c'est bien une solution.</p>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-flag"></i>Conditions initiales</p>
<p>Si on connaît la population à l'instant initial, $N(t=0)=N_0$, on en déduit $C$&nbsp;: $N(t=0)=C\,\mathrm{e}^{-\lambda \times 0} = C = N_0$.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Loi de décroissance radioactive</p>
<p class="nt-f-math">$$N(t)=N_0\,\mathrm{e}^{-\lambda t}$$</p>
<div class="nt-f-units"><span>$N$ <span class="nt-hole">sans unité</span></span><span>$t$ en <span class="nt-hole">$\pu{s}$</span> (ou l'inverse de l'unité de $\lambda$)</span></div>
</div>

<div class="nt-lab" id="lab-decay">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Le hasard… et la loi qui en sort</p>
<p class="nt-note">Chaque disque orange est un noyau. À chaque instant, chacun a la même petite probabilité $\lambda\,\mathrm{d}t$ de se désintégrer (il devient gris), indépendamment des autres et de son «&nbsp;âge&nbsp;».</p>
<div class="nt-lab-pair">
<figure><canvas class="grid" style="height:260px;" aria-label="Population de noyaux qui se désintègrent au hasard"></canvas><figcaption>Population de noyaux</figcaption></figure>
<figure><canvas class="graph" style="height:260px; background:#fff;" aria-label="Nombre de noyaux restants au cours du temps, comparé à la loi exponentielle"></canvas><figcaption>Noyaux restants au cours du temps</figcaption></figure>
</div>
<div class="nt-ctrl">Nombre initial de noyaux $N_0$&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="n0" value="25"><span>25</span></label>
<label><input type="radio" name="n0" value="100"><span>100</span></label>
<label><input type="radio" name="n0" value="400" checked><span>400</span></label>
<label><input type="radio" name="n0" value="2500"><span>2 500</span></label>
</div>
</div>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="demi"> demi-vies successives</label>
<button type="button" class="nt-btn nt-btn-main" data-act="go"><i class="fa-solid fa-play"></i>&nbsp; Lancer</button>
</div>
<div class="nt-read" aria-live="polite"><span>noyaux restants&nbsp;: <b class="out-n"></b></span><span>moitié de $N_0$&nbsp;: <b class="out-th">—</b></span></div>
<p class="nt-msg">Avec peu de noyaux, chaque simulation est différente et s'écarte nettement de l'exponentielle. Avec beaucoup de noyaux, le hasard se «&nbsp;moyenne&nbsp;» et la courbe colle à la loi $N_0\,\mathrm{e}^{-\lambda t}$&nbsp;: c'est une loi statistique.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On peut aussi écrire $N(t) = N_0\,\mathrm{e}^{-t/\tau}$, où $\tau=1/\lambda$ est le <span class="imp nt-hole">temps de vie moyen</span> d'un noyau.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi $\tau = 1/\lambda$ est-il la durée de vie moyenne&nbsp;?</span></summary>
<div class="nt-d-body">
<p>La population survivante suit $N(t)=N_0\,\mathrm{e}^{-\lambda t}$. Le temps total vécu par tous les noyaux est l'aire sous cette courbe&nbsp;: $\displaystyle\int_0^\infty N_0\,\mathrm{e}^{-\lambda t}\,\mathrm{d}t=\frac{N_0}{\lambda}$.</p>
<p>Le temps moyen vécu par chaque noyau est ce total divisé par $N_0$&nbsp;: $\tau=\dfrac{1}{\lambda}$.</p>
</div>
</details>

## Activité {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp nt-hole">activité $A$</span> d'un échantillon radioactif est l'opposée de la dérivée temporelle du nombre de noyaux. C'est le nombre de désintégrations par seconde.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Activité</p>
<p class="nt-f-math">$$A(t)=-\frac{\mathrm{d}N}{\mathrm{d}t}$$</p>
<div class="nt-f-units"><span>$A$ en <span class="nt-hole">becquerels (Bq)</span>&nbsp;: 1&nbsp;Bq correspond à 1 désintégration par seconde</span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>On dérive la loi de décroissance radioactive, avec $\left(\mathrm{e}^{u}\right)' = u'\,\mathrm{e}^{u}$ et $(-\lambda t)' = -\lambda$&nbsp;:</p>
<p class="nt-center">$A(t) = -\dfrac{\mathrm{d}}{\mathrm{d}t}\left(N_0\,\mathrm{e}^{-\lambda t}\right) = -N_0\times(-\lambda)\,\mathrm{e}^{-\lambda t} = \lambda N_0\,\mathrm{e}^{-\lambda t}$</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Évolution de l'activité</p>
<p class="nt-f-math">$$A(t)=\lambda N_0\,\mathrm{e}^{-\lambda t} = A_0\,\mathrm{e}^{-\lambda t}$$</p>
<div class="nt-f-units"><span><b>$A_0 = \lambda N_0$</b> $= A(t=0)$ est l'activité initiale</span><span>plus généralement, $A(t) = \lambda N(t)$</span></div>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Quelques activités typiques</p>
<div class="nt-scroll">
<table class="nt-t nt-t-act">
<thead><tr><th>Échantillon ou source</th><th>Activité (ordre de grandeur)</th><th>Principal radionucléide</th><th>Échelle logarithmique</th></tr></thead>
<tbody>
<tr><td>une banane</td><td><b>15 Bq</b></td><td>potassium 40</td><td><span class="nt-logbar" style="width:10%;"></span></td></tr>
<tr><td>1 litre de lait</td><td><b>50 Bq</b></td><td>potassium 40</td><td><span class="nt-logbar" style="width:14%;"></span></td></tr>
<tr><td>1 kg de granite</td><td><b>1 000 Bq</b></td><td>potassium 40, uranium, thorium</td><td><span class="nt-logbar" style="width:25%;"></span></td></tr>
<tr><td>le corps humain (70 kg)</td><td><b>8 000 Bq</b></td><td>potassium 40 et carbone 14</td><td><span class="nt-logbar" style="width:32%;"></span></td></tr>
<tr><td>un détecteur de fumée (ancien modèle)</td><td><b>37 000 Bq</b> (37 kBq)</td><td>américium 241</td><td><span class="nt-logbar" style="width:38%;"></span></td></tr>
<tr><td>une injection pour une TEP</td><td><b>2,5 × 10⁸ Bq</b> (250 MBq)</td><td>fluor 18</td><td><span class="nt-logbar" style="width:70%;"></span></td></tr>
<tr><td>une source de curiethérapie à haut débit</td><td><b>4 × 10¹¹ Bq</b> (400 GBq)</td><td>iridium 192</td><td><span class="nt-logbar" style="width:97%;"></span></td></tr>
</tbody>
</table>
</div>
<p class="nt-note">Le becquerel est une unité minuscule&nbsp;: notre propre corps est le siège de quelque 8&nbsp;000 désintégrations par seconde. Les barres sont proportionnelles au logarithme de l'activité&nbsp;: chaque douzième de la largeur représente un facteur 10.</p>
</div>

## Temps de demi-vie {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">demi-vie</span> $t_{1/2}$ mesure la durée au bout de laquelle la population radioactive est <span class="imp nt-hole">divisée par deux</span>.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Demi-vie</p>
<p class="nt-f-math">$$t_{1/2}= \frac{\ln(2)}{\lambda} = \tau\times \ln(2)$$</p>
<div class="nt-f-units"><span>on peut aussi l'obtenir graphiquement</span></div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>$N(t_{1/2}) = \dfrac{N_0}{2}$ s'écrit $N_0\,\mathrm{e}^{-\lambda t_{1/2}} = \dfrac{N_0}{2}$, soit $\mathrm{e}^{\lambda t_{1/2}} = 2$, et donc $\lambda\,t_{1/2} = \ln 2$.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Au bout de $n$ demi-vies, la population restante vaut <span class="imp nt-hole">$\dfrac{N_0}{2^{n}}$</span>.</p>
<p class="nt-note">Cochez «&nbsp;demi-vies successives&nbsp;» dans l'animation ci-dessus&nbsp;: à chaque demi-vie, la population est de nouveau divisée par deux, quelle que soit la population de départ.</p>
</div>

## Déterminer l'âge d'un échantillon {.nt-h2}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>On connaît $A_0$ et $A(t)$ (ou $N_0$ et $N(t)$). Que vaut $t$&nbsp;?</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>On prend le logarithme de l'activité&nbsp;:</p>
<p class="nt-center">$\ln (A(t)) = \ln\left(A_0\,\mathrm{e}^{-\lambda t}\right) = \ln (A_0) + \ln\left(\mathrm{e}^{-\lambda t}\right) = \ln (A_0) -\lambda t$</p>
<p class="nt-note nt-center">car $\ln(a\times b)=\ln(a)+\ln(b)$</p>
<p>D'où $t = -\dfrac{\ln (A(t)) - \ln (A_0)}{\lambda} = \dfrac{\ln (A_0) - \ln (A(t))}{\lambda}$, et comme $\ln\left(\dfrac ab\right)=\ln(a)-\ln(b)$&nbsp;:</p>
</div>

<div class="nt-grid">
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>À partir des activités</p>
<p class="nt-f-math">$$t = \frac1\lambda \times \ln \left(\frac{A_0}{A(t)} \right)$$</p>
</div>
<div class="nt-f" style="margin:0 auto;">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>À partir des populations</p>
<p class="nt-f-math">$$t = \frac1\lambda \times \ln \left(\frac{N_0}{N(t)} \right)$$</p>
</div>
</div>

## Simulation en Python {.nt-h2}

<p class="nt-lead">Le programme ci-dessous simule la décroissance de $N_0 = 100\,000$ noyaux&nbsp;: à chaque pas de temps $\mathrm{d}t$, chaque noyau restant se désintègre avec la probabilité $\lambda\,\mathrm{d}t$.</p>

{{< runpython lang="pyodide" mode="toggle" height="auto">}}
from random import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

N0 = 100000
N = N0
t = 0
dt = 1E-2
lbda = 2
plt.scatter(t, N, color = '#88c999', s = 10)

while N:
    for i in range(N):
        if random() < lbda*dt:
            N -= 1
    t += dt
    plt.scatter(t, N, color = '#88c999', s = 10)

plt.show()
{{< /runpython >}}

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Comment pourrait-on afficher aussi le temps de demi-vie&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Une solution possible</span></summary>
<div class="nt-d-body">
<p>On mémorise la première date à laquelle $N$ devient inférieur ou égal à $N_0/2$, puis on la compare à la valeur théorique $\ln(2)/\lambda$&nbsp;:</p>
<pre><code>from random import random
from math import log
N0 = 100000
N = N0
t = 0
dt = 1E-2
lbda = 2
t_demi = None
while N:
    for i in range(N):
        if random() &lt; lbda*dt:
            N -= 1
    t += dt
    if t_demi is None and N &lt;= N0/2:
        t_demi = t
print(f"t1/2 simulé : {t_demi:.2f} s")
print(f"t1/2 théorique : {log(2)/lbda:.2f} s")</code></pre>
<p class="nt-note">Avec $\lambda = \pu{2 s^-1}$, on attend $t_{1/2} \approx \pu{0,35 s}$. Le pas $\mathrm{d}t$ limite la précision&nbsp;: le résultat est arrondi au centième de seconde près.</p>
</div>
</details>

## Applications {.nt-h2}

### Datation {.nt-h3}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Principe</p>
<p>On utilise la loi de décroissance radioactive pour déterminer une date. Exemples&nbsp;:</p>
<ul class="nt-facts">
<li>datation de matière organique au <b>carbone 14</b> ($t_{1/2} = 5\,730$ ans, valeur usuelle&nbsp;; les mesures les plus récentes donnent plutôt 5&nbsp;700 ans), jusqu'à environ 50&nbsp;000 ans&nbsp;;</li>
<li>datation de roches au <b>rubidium-strontium</b> (rubidium 87, $t_{1/2} \approx 50$ milliards d'années), pour des âges géologiques.</li>
</ul>
<p>Un être vivant échange du carbone avec son environnement&nbsp;: sa teneur en carbone 14 reste constante. À sa mort, les échanges cessent et le carbone 14 qu'il contient se désintègre sans être renouvelé.</p>
</div>

<div class="nt-lab" id="lab-datation">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Dater un échantillon au carbone 14</p>
<canvas style="height:280px; background:#fff;" aria-label="Activité du carbone 14 en fonction de l'âge de l'échantillon, et lecture de l'âge correspondant à l'activité mesurée"></canvas>
<label class="nt-ctrl">Activité mesurée de l'échantillon&nbsp;: <b class="out-a"></b><input type="range" min="0.002" max="0.226" step="0.001" value="0.119"></label>
<div class="nt-btns">
<button type="button" class="nt-btn" data-a="0.119">Ötzi (≈ 5 300 ans)</button>
<button type="button" class="nt-btn" data-a="0.029">charbon de Lascaux (≈ 17 000 ans)</button>
<button type="button" class="nt-btn" data-a="0.003">charbon de la grotte Chauvet (≈ 36 000 ans)</button>
</div>
<div class="nt-read" aria-live="polite"><span>$A/A_0$ = <b class="out-r"></b></span><span>âge $t = \frac{1}{\lambda}\ln\left(\frac{A_0}{A}\right)$ = <b class="out-age"></b></span></div>
<p class="nt-note">Activité d'un gramme de carbone d'un être vivant&nbsp;: $A_0 \approx \pu{0,226 Bq}$. Les points verts marquent les demi-vies successives. Au-delà de 50&nbsp;000 ans environ, il reste trop peu de carbone 14 pour une mesure fiable.</p>
</div>

### Domaine médical {.nt-h3}

<p class="nt-lead">La médecine nucléaire fournit à la fois des techniques d'imagerie et de traitement.</p>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-x-ray"></i>Imagerie médicale</p>
<p>Contrairement à la radiographie traditionnelle où on observe l'ombre d'un rayonnement extérieur, le rayonnement est ici émis directement au niveau des organes, en faisant ingérer ou en injectant au patient une substance radioactive.</p>
<ul class="nt-facts">
<li><b>Scintigraphie</b>&nbsp;: utilisation de gamma-caméras à scintillation&nbsp;;</li>
<li><b>Tomographie par émission de positons</b> (TEP, ou PET scan en anglais).</li>
</ul>
</div>

<div class="nt-lab" id="lab-tep">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Comment la TEP fabrique une image</p>
<canvas style="height:400px;" aria-label="Annihilations dans le corps d'un patient, photons détectés en coïncidence par une couronne de détecteurs, et droites de réponse accumulées"></canvas>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" data-p="lignes" checked> droites accumulées</label>
<button type="button" class="nt-btn" data-act="reset"><i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer</button>
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button>
</div>
<div class="nt-read" aria-live="polite"><span>annihilations détectées&nbsp;: <b class="out-ev"></b></span></div>
<p class="nt-msg">Chaque annihilation (éclair violet) émet deux photons dos à dos. Les deux détecteurs touchés au même instant définissent une droite. Une seule droite ne dit pas où a eu lieu l'émission, mais en accumulant les droites, une zone brillante apparaît là où le traceur s'est concentré&nbsp;: la tumeur.</p>
</div>

<p class="nt-cap">En TEP, on injecte un traceur émetteur $\beta^+$ (souvent du fluor 18, $t_{1/2} \approx 110$&nbsp;min, fixé sur une molécule de glucose). Chaque positon s'annihile presque aussitôt avec un électron&nbsp;: deux photons γ de 511&nbsp;keV partent dans des directions opposées. Les deux détecteurs touchés au même instant définissent une droite qui passe par le lieu de l'émission&nbsp;; en combinant des millions de ces droites, l'ordinateur reconstruit une image 3D.</p>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi les tumeurs «&nbsp;brillent&nbsp;» en TEP, et pourquoi on n'utilise pas que la TEP</span></summary>
<div class="nt-d-body">
<p><b>Les cellules cancéreuses consomment beaucoup de sucre.</b> Pour une raison encore mal comprise, la plupart d'entre elles préfèrent la fermentation à la respiration, même en présence de dioxygène (c'est l'effet Warburg). La fermentation est bien plus rapide mais bien moins efficace (environ 6&nbsp;% de l'énergie tirée de la respiration)&nbsp;: elles consomment donc énormément de glucose, et le glucose marqué au fluor 18 s'y accumule.</p>
<p><b>TEP ou scintigraphie&nbsp;?</b> La TEP offre une meilleure résolution (quelques millimètres) et une meilleure sensibilité, car la détection en coïncidence remplace le collimateur en plomb. Mais ses traceurs ont des demi-vies courtes (110&nbsp;min pour le fluor 18) et demandent souvent un cyclotron proche. La scintigraphie, avec par exemple le technétium 99m ($t_{1/2} = 6$&nbsp;h, produit sur place par un générateur), reste moins chère, très répandue et suffisante pour de nombreux examens (os, thyroïde, reins, cœur…).</p>
<p>Quelques vidéos&nbsp;: <a href="https://www.youtube.com/watch?v=QoS1H7J-86w" target="_blank" rel="noopener">vidéo 1</a>, <a href="https://www.youtube.com/watch?v=yrTy03O0gWw" target="_blank" rel="noopener">vidéo 2</a>, <a href="https://www.youtube.com/watch?v=TYGa4KBu5oo&t=132s" target="_blank" rel="noopener">vidéo 3</a> (à partir de 2'12'').</p>
</div>
</details>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-syringe"></i>Radiothérapie</p>
<ul class="nt-facts">
<li><b>Radiothérapie externe</b>&nbsp;: on focalise un faisceau de particules (photons X, électrons, neutrons, protons, ions carbone) issu d'un accélérateur sur les cellules cancéreuses.</li>
<li><b>Curiethérapie</b>&nbsp;: une source radioactive scellée est placée à l'intérieur ou à proximité immédiate de la zone à traiter. La technique doit son nom aux travaux menés à l'Institut du radium de Marie Curie.</li>
</ul>
<p class="nt-note">Pour la prostate, par exemple, on implante de petits grains radioactifs d'iode 125 ($t_{1/2} \approx 59$&nbsp;jours), de palladium 103 (17&nbsp;jours) ou de césium 131 (9,7&nbsp;jours).</p>
</div>

### Radioprotection&nbsp;: protection contre les rayonnements ionisants {.nt-h3}

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-shield-halved"></i>À vous de jouer</p>
<ul class="nt-facts">
<li><a href="https://expop.asnr.fr" target="_blank" rel="noopener">Estimez votre exposition aux rayonnements ionisants</a> (site de l'Autorité de sûreté nucléaire et de radioprotection).</li>
<li><a href="https://xkcd.com/radiation/" target="_blank" rel="noopener">Le tableau des doses de rayonnement de xkcd</a>&nbsp;: une banane, un vol en avion, un scanner…</li>
<li><a href="https://www.youtube.com/watch?v=x_UtBSJtF30" target="_blank" rel="noopener">Une vidéo sur la radioprotection</a>.</li>
</ul>
<p>Les trois règles de base de la radioprotection découlent des propriétés des rayonnements&nbsp;: <b>s'éloigner</b> de la source, <b>réduire la durée</b> d'exposition, et <b>interposer un écran</b> adapté au rayonnement (voir le schéma du pouvoir de pénétration).</p>
</div>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
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
  function playLabel(btn, playing) { btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture'; }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function txt(c, s, x, y, color, font, align) {
    c.font = font || '700 12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.lineJoin = 'round';
    c.lineWidth = 4; c.strokeStyle = 'rgba(248,250,252,.9)'; c.strokeText(s, x, y);
    c.fillStyle = color; c.fillText(s, x, y);
  }
  function frame(c, w, h, o) {
    var L = o.L || 58, R = w - (o.R || 16), T = o.T || 14, B = h - (o.B || 34);
    function X(v) { return L + (v - o.x0) / (o.x1 - o.x0) * (R - L); }
    function Y(v) { return B - (v - o.y0) / (o.y1 - o.y0) * (B - T); }
    c.strokeStyle = col('--line'); c.lineWidth = 1;
    for (var gx = o.x0; gx <= o.x1 + 1e-9; gx += o.dx) { c.beginPath(); c.moveTo(X(gx), T); c.lineTo(X(gx), B); c.stroke(); }
    for (var gy = o.y0; gy <= o.y1 + 1e-9; gy += o.dy) { c.beginPath(); c.moveTo(L, Y(gy)); c.lineTo(R, Y(gy)); c.stroke(); }
    c.strokeStyle = col('--ink'); c.beginPath(); c.moveTo(L, T); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
    c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
    for (gx = o.x0; gx <= o.x1 + 1e-9; gx += o.dx) { c.fillText(o.fx ? o.fx(gx) : fr(gx, 0), X(gx), B + 14); }
    c.fillText(o.xl, (L + R) / 2, h - 3);
    c.textAlign = 'right';
    for (gy = o.y0; gy <= o.y1 + 1e-9; gy += o.dy) { c.fillText(o.fy ? o.fy(gy) : fr(gy, 0), L - 5, Y(gy) + 4); }
    c.save(); c.translate(12, (T + B) / 2); c.rotate(-Math.PI / 2); c.textAlign = 'center'; c.fillText(o.yl, 0, 0); c.restore();
    return { X: X, Y: Y, L: L, R: R, T: T, B: B };
  }
  function duree(s) {
    var an = 3.156e7;
    if (s < 1) { return fr(s * 1000, 1) + ' ms'; }
    if (s < 120) { return fr(s, 1) + ' s'; }
    if (s < 7200) { return fr(s / 60, 1) + ' min'; }
    if (s < 3 * 86400) { return fr(s / 3600, 1) + ' h'; }
    if (s < an) { return fr(s / 86400, 1) + ' jours'; }
    if (s < 100 * an) { return fr(s / an, 1) + ' ans'; }
    if (s < 1e5 * an) { return Math.round(s / an).toLocaleString('fr-FR') + ' ans'; }
    return sci(s / an, 1) + ' ans';
  }
  /* ================= 1. Le diagramme (N, Z) ================= */
  (function () {
    var root = document.getElementById('lab-nz');
    if (!root) { return; }
    var D = {"n":[[1,0,"s",0.0],[1,1,"s",0.0],[1,2,"m",389000000.0],[2,1,"s",0.0],[2,2,"s",0.0],[3,3,"s",0.0],[3,4,"s",0.0],[4,3,"p",4600000.0],[4,5,"s",0.0],[4,6,"m",47700000000000.0],[5,5,"s",0.0],[5,6,"s",0.0],[6,4,"p",19.3],[6,5,"p",1220.0],[6,6,"s",0.0],[6,7,"s",0.0],[6,8,"m",180000000000.0],[7,6,"p",598.0],[7,7,"s",0.0],[7,8,"s",0.0],[7,9,"m",7.13],[8,6,"p",70.6],[8,7,"p",122.0],[8,8,"s",0.0],[8,9,"s",0.0],[8,10,"s",0.0],[8,11,"m",26.5],[9,8,"p",64.5],[9,9,"p",6590.0],[9,10,"s",0.0],[10,9,"p",17.2],[10,10,"s",0.0],[10,11,"s",0.0],[10,12,"s",0.0],[10,14,"m",203.0],[11,11,"p",82100000.0],[11,12,"s",0.0],[11,13,"m",53900.0],[12,12,"s",0.0],[12,13,"s",0.0],[12,14,"s",0.0],[12,15,"m",567.0],[12,16,"m",75300.0],[13,13,"p",22600000000000.0],[13,14,"s",0.0],[13,15,"m",134.0],[13,16,"m",394.0],[14,14,"s",0.0],[14,15,"s",0.0],[14,16,"s",0.0],[14,17,"m",9440.0],[14,18,"m",4170000000.0],[15,15,"p",150.0],[15,16,"s",0.0],[15,17,"m",1230000.0],[15,18,"m",2190000.0],[16,16,"s",0.0],[16,17,"s",0.0],[16,18,"s",0.0],[16,19,"m",7560000.0],[16,20,"s",0.0],[16,21,"m",303.0],[16,22,"m",10200.0],[17,17,"p",1.53],[17,18,"s",0.0],[17,19,"m",9500000000000.0],[17,20,"s",0.0],[17,21,"m",2230.0],[17,22,"m",3340.0],[17,23,"m",81.0],[18,18,"s",0.0],[18,19,"p",3030000.0],[18,20,"s",0.0],[18,21,"m",8490000000.0],[18,22,"s",0.0],[18,23,"m",6580.0],[18,24,"m",1040000000.0],[18,25,"m",322.0],[18,26,"m",712.0],[19,19,"p",458.0],[19,20,"s",0.0],[19,21,"m",3.95e+16],[19,22,"s",0.0],[19,23,"m",44500.0],[19,24,"m",80300.0],[19,25,"m",1330.0],[19,26,"m",1040.0],[19,27,"m",105.0],[20,20,"s",0.0],[20,21,"p",3220000000000.0],[20,22,"s",0.0],[20,23,"s",0.0],[20,24,"s",0.0],[20,25,"m",14100000.0],[20,26,"s",0.0],[20,27,"m",392000.0],[20,28,"s",0.0],[20,29,"m",523.0],[21,22,"p",14000.0],[21,23,"p",14300.0],[21,24,"s",0.0],[21,25,"m",7240000.0],[21,26,"m",289000.0],[21,27,"m",157000.0],[21,28,"m",3430.0],[21,29,"m",102.0],[22,22,"p",1890000000.0],[22,23,"p",11100.0],[22,24,"s",0.0],[22,25,"s",0.0],[22,26,"s",0.0],[22,27,"s",0.0],[22,28,"s",0.0],[22,29,"m",346.0],[22,30,"m",102.0],[23,24,"p",1960.0],[23,25,"p",1380000.0],[23,26,"p",28500000.0],[23,27,"p",4.73e+24],[23,28,"s",0.0],[23,29,"m",225.0],[23,30,"m",96.6],[24,24,"p",77600.0],[24,25,"p",2540.0],[24,26,"s",0.0],[24,27,"p",2390000.0],[24,28,"s",0.0],[24,29,"s",0.0],[24,30,"s",0.0],[24,31,"m",210.0],[24,32,"m",356.0],[25,26,"p",2770.0],[25,27,"p",483000.0],[25,28,"p",117000000000000.0],[25,29,"p",27000000.0],[25,30,"s",0.0],[25,31,"m",9280.0],[25,32,"m",85.4],[26,26,"p",29800.0],[26,27,"p",511.0],[26,28,"s",0.0],[26,29,"p",86400000.0],[26,30,"s",0.0],[26,31,"s",0.0],[26,32,"s",0.0],[26,33,"m",3840000.0],[26,34,"m",47300000000000.0],[26,35,"m",359.0],[26,36,"m",68.0],[27,28,"p",63100.0],[27,29,"p",6670000.0],[27,30,"p",23500000.0],[27,31,"p",6120000.0],[27,32,"s",0.0],[27,33,"m",166000000.0],[27,34,"m",5940.0],[27,35,"m",90.0],[28,28,"p",525000.0],[28,29,"p",128000.0],[28,30,"s",0.0],[28,31,"p",3190000000000.0],[28,32,"s",0.0],[28,33,"s",0.0],[28,34,"s",0.0],[28,35,"m",3160000000.0],[28,36,"s",0.0],[28,37,"m",9060.0],[28,38,"m",197000.0],[29,28,"p",0.196],[29,30,"p",81.5],[29,31,"p",1420.0],[29,32,"p",12000.0],[29,33,"p",580.0],[29,34,"s",0.0],[29,35,"p",45700.0],[29,36,"s",0.0],[29,37,"m",307.0],[29,38,"m",223000.0],[29,40,"m",171.0],[30,30,"p",143.0],[30,31,"p",89.1],[30,32,"p",33100.0],[30,33,"p",2310.0],[30,34,"s",0.0],[30,35,"p",21100000.0],[30,36,"s",0.0],[30,37,"s",0.0],[30,38,"s",0.0],[30,39,"m",3380.0],[30,40,"s",0.0],[30,41,"m",147.0],[30,42,"m",167000.0],[31,33,"p",158.0],[31,34,"p",912.0],[31,35,"p",34200.0],[31,36,"p",282000.0],[31,37,"p",4060.0],[31,38,"s",0.0],[31,39,"m",1270.0],[31,40,"s",0.0],[31,41,"m",50800.0],[31,42,"m",17500.0],[31,43,"m",487.0],[32,34,"p",8140.0],[32,35,"p",1130.0],[32,36,"p",23400000.0],[32,37,"p",141000.0],[32,38,"s",0.0],[32,39,"p",988000.0],[32,40,"s",0.0],[32,41,"s",0.0],[32,42,"s",0.0],[32,43,"m",4970.0],[32,44,"s",0.0],[32,45,"m",40700.0],[32,46,"m",5280.0],[33,35,"p",152.0],[33,36,"p",914.0],[33,37,"p",3160.0],[33,38,"p",235000.0],[33,39,"p",93600.0],[33,40,"p",6940000.0],[33,41,"p",1540000.0],[33,42,"s",0.0],[33,43,"m",93100.0],[33,44,"m",140000.0],[33,45,"m",5440.0],[33,46,"m",541.0],[34,36,"p",2470.0],[34,37,"p",284.0],[34,38,"p",726000.0],[34,39,"p",25700.0],[34,40,"s",0.0],[34,41,"p",10300000.0],[34,42,"s",0.0],[34,43,"s",0.0],[34,44,"s",0.0],[34,45,"m",9310000000000.0],[34,46,"s",0.0],[34,47,"m",1110.0],[34,48,"s",0.0],[34,49,"m",1340.0],[34,50,"m",186.0],[35,37,"p",78.6],[35,38,"p",204.0],[35,39,"p",1520.0],[35,40,"p",5800.0],[35,41,"p",58300.0],[35,42,"p",205000.0],[35,43,"p",388.0],[35,44,"s",0.0],[35,45,"m",1060.0],[35,46,"s",0.0],[35,47,"m",127000.0],[35,48,"m",8640.0],[35,49,"m",1910.0],[35,50,"m",174.0],[36,38,"p",690.0],[36,39,"p",257.0],[36,40,"p",53300.0],[36,41,"p",4460.0],[36,42,"s",0.0],[36,43,"p",126000.0],[36,44,"s",0.0],[36,45,"p",7230000000000.0],[36,46,"s",0.0],[36,47,"s",0.0],[36,48,"s",0.0],[36,49,"m",339000000.0],[36,50,"s",0.0],[36,51,"m",4580.0],[36,52,"m",10200.0],[36,53,"m",189.0],[37,40,"p",226.0],[37,41,"p",1060.0],[37,42,"p",1370.0],[37,43,"p",33.4],[37,44,"p",16500.0],[37,45,"p",76.4],[37,46,"p",7450000.0],[37,47,"p",2830000.0],[37,48,"s",0.0],[37,49,"m",1610000.0],[37,50,"m",1.55e+18],[37,51,"m",1070.0],[37,52,"m",909.0],[37,53,"m",158.0],[38,41,"p",135.0],[38,42,"p",6380.0],[38,43,"p",1340.0],[38,44,"p",2190000.0],[38,45,"p",117000.0],[38,46,"s",0.0],[38,47,"p",5600000.0],[38,48,"s",0.0],[38,49,"s",0.0],[38,50,"s",0.0],[38,51,"m",4370000.0],[38,52,"m",909000000.0],[38,53,"m",34700.0],[38,54,"m",9580.0],[38,55,"m",445.0],[38,56,"m",75.3],[39,42,"p",70.4],[39,44,"p",425.0],[39,46,"p",9650.0],[39,47,"p",53100.0],[39,48,"p",287000.0],[39,49,"p",9210000.0],[39,50,"s",0.0],[39,51,"m",231000.0],[39,52,"m",5060000.0],[39,53,"m",12700.0],[39,54,"m",36600.0],[39,55,"m",1120.0],[39,56,"m",618.0],[40,45,"p",472.0],[40,46,"p",59400.0],[40,47,"p",6050.0],[40,48,"p",7210000.0],[40,49,"p",282000.0],[40,50,"s",0.0],[40,51,"s",0.0],[40,52,"s",0.0],[40,53,"m",48300000000000.0],[40,54,"s",0.0],[40,55,"m",5530000.0],[40,56,"s",0.0],[40,57,"m",60300.0],[41,46,"p",225.0],[41,47,"p",870.0],[41,48,"p",7310.0],[41,49,"p",52600.0],[41,50,"p",21500000000.0],[41,51,"p",1100000000000000.0],[41,52,"s",0.0],[41,53,"m",641000000000.0],[41,54,"m",3020000.0],[41,55,"m",84100.0],[41,56,"m",4330.0],[41,58,"m",15.0],[42,47,"p",127.0],[42,48,"p",20000.0],[42,49,"p",929.0],[42,50,"s",0.0],[42,51,"p",126000000000.0],[42,52,"s",0.0],[42,53,"s",0.0],[42,54,"s",0.0],[42,55,"s",0.0],[42,56,"s",0.0],[42,57,"m",237000.0],[42,58,"s",0.0],[42,59,"m",877.0],[42,60,"m",678.0],[43,48,"p",188.0],[43,49,"p",255.0],[43,50,"p",9900.0],[43,51,"p",17600.0],[43,52,"p",72000.0],[43,53,"p",370000.0],[43,54,"p",82000000000000.0],[43,55,"m",133000000000000.0],[43,56,"m",6660000000000.0],[43,58,"m",852.0],[43,59,"m",5.28],[43,61,"m",1100.0],[43,62,"m",456.0],[44,48,"p",219.0],[44,50,"p",3110.0],[44,51,"p",5910.0],[44,52,"s",0.0],[44,53,"p",251000.0],[44,54,"s",0.0],[44,55,"s",0.0],[44,56,"s",0.0],[44,57,"s",0.0],[44,58,"s",0.0],[44,59,"m",3390000.0],[44,60,"s",0.0],[44,61,"m",16000.0],[44,62,"m",32300000.0],[44,63,"m",225.0],[44,64,"m",273.0],[45,49,"p",70.6],[45,50,"p",301.0],[45,51,"p",594.0],[45,52,"p",1840.0],[45,53,"p",522.0],[45,54,"p",1390000.0],[45,55,"p",74900.0],[45,56,"p",104000000.0],[45,57,"p",17900000.0],[45,58,"s",0.0],[45,59,"m",42.3],[45,60,"m",127000.0],[45,61,"m",29.8],[45,62,"m",1300.0],[45,63,"m",16.8],[45,64,"m",80.0],[46,50,"p",122.0],[46,51,"p",186.0],[46,52,"p",1060.0],[46,53,"p",1280.0],[46,54,"p",314000.0],[46,55,"p",30500.0],[46,56,"s",0.0],[46,57,"p",1470000.0],[46,58,"s",0.0],[46,59,"s",0.0],[46,60,"s",0.0],[46,61,"m",205000000000000.0],[46,62,"s",0.0],[46,63,"m",49300.0],[46,64,"s",0.0],[46,65,"m",1400.0],[46,66,"m",75700.0],[46,68,"m",145.0],[47,52,"p",124.0],[47,54,"p",666.0],[47,55,"p",774.0],[47,56,"p",3940.0],[47,57,"p",4150.0],[47,58,"p",3570000.0],[47,59,"p",1440.0],[47,60,"s",0.0],[47,61,"m",142.0],[47,62,"s",0.0],[47,63,"m",24.6],[47,64,"m",644000.0],[47,65,"m",11300.0],[47,66,"m",19300.0],[47,67,"m",4.6],[47,68,"m",1200.0],[47,69,"m",161.0],[47,70,"m",73.6],[48,53,"p",81.6],[48,54,"p",330.0],[48,55,"p",438.0],[48,56,"p",3460.0],[48,57,"p",3330.0],[48,58,"s",0.0],[48,59,"p",23400.0],[48,60,"s",0.0],[48,61,"p",39900000.0],[48,62,"s",0.0],[48,63,"s",0.0],[48,64,"s",0.0],[48,65,"m",2.43e+23],[48,66,"s",0.0],[48,67,"m",192000.0],[48,68,"s",0.0],[48,69,"m",8960.0],[48,70,"m",3020.0],[48,71,"m",161.0],[49,54,"p",60.0],[49,56,"p",304.0],[49,57,"p",372.0],[49,58,"p",1940.0],[49,59,"p",3480.0],[49,60,"p",15100.0],[49,61,"p",17600.0],[49,62,"p",242000.0],[49,63,"p",898.0],[49,64,"s",0.0],[49,65,"m",71.9],[49,66,"m",1.39e+22],[49,68,"m",2590.0],[49,69,"m",5.0],[49,70,"m",144.0],[49,72,"m",23.1],[50,56,"p",115.0],[50,58,"p",618.0],[50,59,"p",1080.0],[50,60,"p",14800.0],[50,61,"p",2120.0],[50,62,"s",0.0],[50,63,"p",9940000.0],[50,64,"s",0.0],[50,65,"s",0.0],[50,66,"s",0.0],[50,67,"s",0.0],[50,68,"s",0.0],[50,69,"s",0.0],[50,70,"s",0.0],[50,71,"m",97300.0],[50,72,"s",0.0],[50,73,"m",11200000.0],[50,74,"s",0.0],[50,75,"m",833000.0],[50,76,"m",7260000000000.0],[50,77,"m",7560.0],[50,78,"m",3540.0],[50,79,"m",134.0],[50,80,"m",223.0],[51,60,"p",75.0],[51,62,"p",400.0],[51,63,"p",209.0],[51,64,"p",1930.0],[51,65,"p",948.0],[51,66,"p",10100.0],[51,67,"p",216.0],[51,68,"p",137000.0],[51,69,"p",953.0],[51,70,"s",0.0],[51,71,"m",235000.0],[51,72,"s",0.0],[51,73,"m",5200000.0],[51,74,"m",87100000.0],[51,75,"m",1070000.0],[51,76,"m",333000.0],[51,77,"m",32400.0],[51,78,"m",15800.0],[51,79,"m",2370.0],[51,80,"m",1380.0],[51,82,"m",150.0],[52,61,"p",102.0],[52,62,"p",912.0],[52,63,"p",348.0],[52,64,"p",8960.0],[52,65,"p",3720.0],[52,66,"p",518000.0],[52,67,"p",57800.0],[52,68,"s",0.0],[52,69,"p",1660000.0],[52,70,"s",0.0],[52,71,"p",1.89e+22],[52,72,"s",0.0],[52,73,"s",0.0],[52,74,"s",0.0],[52,75,"m",33700.0],[52,76,"s",0.0],[52,77,"m",4180.0],[52,78,"s",0.0],[52,79,"m",1500.0],[52,80,"m",277000.0],[52,81,"m",750.0],[52,82,"m",2510.0],[53,65,"p",822.0],[53,66,"p",1150.0],[53,67,"p",4900.0],[53,68,"p",7630.0],[53,69,"p",218.0],[53,70,"p",47800.0],[53,71,"p",361000.0],[53,72,"p",5130000.0],[53,73,"p",1120000.0],[53,74,"s",0.0],[53,75,"m",1500.0],[53,76,"m",495000000000000.0],[53,77,"m",44500.0],[53,78,"m",693000.0],[53,79,"m",8260.0],[53,80,"m",74900.0],[53,81,"m",3150.0],[53,82,"m",23700.0],[54,66,"p",2400.0],[54,67,"p",2410.0],[54,68,"p",72400.0],[54,69,"p",7490.0],[54,70,"s",0.0],[54,71,"p",60800.0],[54,72,"s",0.0],[54,73,"p",3140000.0],[54,74,"s",0.0],[54,75,"s",0.0],[54,76,"s",0.0],[54,77,"s",0.0],[54,78,"s",0.0],[54,79,"m",453000.0],[54,80,"s",0.0],[54,81,"m",32900.0],[54,82,"s",0.0],[54,83,"m",229.0],[54,84,"m",845.0],[55,66,"p",155.0],[55,68,"p",353.0],[55,69,"p",30.8],[55,70,"p",2700.0],[55,71,"p",98.4],[55,72,"p",22500.0],[55,73,"p",218.0],[55,74,"p",115000.0],[55,75,"p",1750.0],[55,76,"p",837000.0],[55,77,"p",560000.0],[55,78,"s",0.0],[55,79,"m",65200000.0],[55,80,"m",72600000000000.0],[55,81,"m",1140000.0],[55,82,"m",952000000.0],[55,83,"m",2000.0],[55,84,"m",556.0],[55,85,"m",63.7],[56,68,"p",660.0],[56,70,"p",6000.0],[56,71,"p",762.0],[56,72,"p",210000.0],[56,73,"p",8030.0],[56,74,"s",0.0],[56,75,"p",994000.0],[56,76,"s",0.0],[56,77,"p",332000000.0],[56,78,"s",0.0],[56,79,"s",0.0],[56,80,"s",0.0],[56,81,"s",0.0],[56,82,"s",0.0],[56,83,"m",4980.0],[56,84,"m",1100000.0],[56,85,"m",1100.0],[56,86,"m",636.0],[57,71,"p",311.0],[57,72,"p",696.0],[57,73,"p",522.0],[57,74,"p",3540.0],[57,75,"p",17300.0],[57,76,"p",14100.0],[57,77,"p",387.0],[57,78,"p",70200.0],[57,79,"p",592.0],[57,80,"p",1890000000000.0],[57,81,"p",3.22e+18],[57,82,"s",0.0],[57,83,"m",145000.0],[57,84,"m",14100.0],[57,85,"m",5470.0],[57,86,"m",852.0],[58,72,"p",1370.0],[58,73,"p",612.0],[58,74,"p",12600.0],[58,75,"p",5820.0],[58,76,"p",273000.0],[58,77,"p",63700.0],[58,78,"s",0.0],[58,79,"p",32400.0],[58,80,"s",0.0],[58,81,"p",11900000.0],[58,82,"s",0.0],[58,83,"m",2810000.0],[58,84,"s",0.0],[58,85,"m",119000.0],[58,86,"m",24600000.0],[58,87,"m",181.0],[59,75,"p",660.0],[59,76,"p",1440.0],[59,77,"p",786.0],[59,78,"p",4610.0],[59,79,"p",87.0],[59,80,"p",15900.0],[59,81,"p",203.0],[59,82,"s",0.0],[59,83,"m",68800.0],[59,84,"m",1170000.0],[59,85,"m",1040.0],[59,86,"m",21500.0],[59,87,"m",1450.0],[59,88,"m",804.0],[59,89,"m",137.0],[60,74,"p",510.0],[60,75,"p",744.0],[60,76,"p",3040.0],[60,77,"p",2310.0],[60,78,"p",18100.0],[60,79,"p",1780.0],[60,80,"p",291000.0],[60,81,"p",8960.0],[60,82,"s",0.0],[60,83,"s",0.0],[60,84,"a",7.23e+22],[60,85,"s",0.0],[60,86,"s",0.0],[60,87,"m",949000.0],[60,88,"s",0.0],[60,89,"m",6220.0],[60,90,"s",0.0],[60,91,"m",746.0],[60,92,"m",684.0],[61,75,"p",107.0],[61,78,"p",249.0],[61,79,"p",9.2],[61,80,"p",1250.0],[61,81,"p",40.5],[61,82,"p",22900000.0],[61,83,"p",31400000.0],[61,84,"p",559000000.0],[61,85,"p",175000000.0],[61,86,"m",82800000.0],[61,87,"m",464000.0],[61,88,"m",191000.0],[61,89,"m",9650.0],[61,90,"m",102000.0],[61,91,"m",247.0],[61,92,"m",315.0],[61,93,"m",104.0],[62,77,"p",154.0],[62,78,"p",889.0],[62,79,"p",612.0],[62,80,"p",4350.0],[62,81,"p",525.0],[62,82,"s",0.0],[62,83,"p",29400000.0],[62,84,"a",3250000000000000.0],[62,85,"a",3.35e+18],[62,86,"a",2.21e+23],[62,87,"s",0.0],[62,88,"s",0.0],[62,89,"m",2840000000.0],[62,90,"s",0.0],[62,91,"m",167000.0],[62,92,"s",0.0],[62,93,"m",1340.0],[62,94,"m",33800.0],[62,95,"m",482.0],[63,79,"p",2.34],[63,80,"p",155.0],[63,81,"p",10.2],[63,82,"p",512000.0],[63,83,"p",398000.0],[63,84,"p",2080000.0],[63,85,"p",4710000.0],[63,86,"p",8040000.0],[63,87,"p",1160000000.0],[63,88,"s",0.0],[63,89,"p",427000000.0],[63,90,"s",0.0],[63,91,"m",271000000.0],[63,92,"m",150000000.0],[63,93,"m",1310000.0],[63,94,"m",54600.0],[63,95,"m",2750.0],[63,96,"m",1090.0],[64,78,"p",70.2],[64,80,"p",268.0],[64,81,"p",1380.0],[64,82,"p",4170000.0],[64,83,"p",137000.0],[64,84,"a",2350000000.0],[64,85,"p",802000.0],[64,86,"a",56500000000000.0],[64,87,"p",10700000.0],[64,88,"a",3.41e+21],[64,89,"p",20800000.0],[64,90,"s",0.0],[64,91,"s",0.0],[64,92,"s",0.0],[64,93,"s",0.0],[64,94,"s",0.0],[64,95,"m",66500.0],[64,96,"s",0.0],[64,98,"m",504.0],[65,81,"p",23.0],[65,82,"p",5900.0],[65,83,"p",3600.0],[65,84,"p",14800.0],[65,85,"p",12500.0],[65,86,"p",63400.0],[65,87,"p",63000.0],[65,88,"p",202000.0],[65,89,"p",77400.0],[65,90,"p",460000.0],[65,91,"p",462000.0],[65,92,"p",2240000000.0],[65,93,"p",5680000000.0],[65,94,"s",0.0],[65,95,"m",6250000.0],[65,96,"m",597000.0],[65,97,"m",456.0],[65,98,"m",1170.0],[65,99,"m",180.0],[65,100,"m",127.0],[66,82,"p",198.0],[66,83,"p",252.0],[66,84,"p",430.0],[66,85,"p",1070.0],[66,86,"p",8570.0],[66,87,"p",23000.0],[66,88,"a",94700000000000.0],[66,89,"p",35600.0],[66,90,"s",0.0],[66,91,"p",29300.0],[66,92,"s",0.0],[66,93,"p",12500000.0],[66,94,"s",0.0],[66,95,"s",0.0],[66,96,"s",0.0],[66,97,"s",0.0],[66,98,"s",0.0],[66,99,"m",8400.0],[66,100,"m",294000.0],[66,101,"m",372.0],[66,102,"m",522.0],[67,83,"p",76.8],[67,86,"p",121.0],[67,87,"p",706.0],[67,88,"p",2880.0],[67,89,"p",3360.0],[67,90,"p",756.0],[67,92,"p",1980.0],[67,93,"p",1540.0],[67,94,"p",8930.0],[67,95,"p",900.0],[67,96,"p",144000000000.0],[67,97,"p",1740.0],[67,98,"s",0.0],[67,99,"m",96500.0],[67,100,"m",11200.0],[67,101,"m",179.0],[67,103,"m",166.0],[68,86,"p",224.0],[68,88,"p",1170.0],[68,91,"p",2160.0],[68,93,"p",11600.0],[68,94,"s",0.0],[68,95,"p",4500.0],[68,96,"s",0.0],[68,97,"p",37300.0],[68,98,"s",0.0],[68,99,"s",0.0],[68,100,"s",0.0],[68,101,"m",812000.0],[68,102,"s",0.0],[68,103,"m",27100.0],[68,104,"m",177000.0],[68,105,"m",86.0],[69,92,"p",1810.0],[69,93,"p",1300.0],[69,94,"p",6520.0],[69,95,"p",120.0],[69,96,"p",108000.0],[69,97,"p",27700.0],[69,98,"p",799000.0],[69,99,"p",8040000.0],[69,100,"s",0.0],[69,101,"m",11100000.0],[69,102,"m",60600000.0],[69,103,"m",229000.0],[69,104,"m",29700.0],[69,105,"m",324.0],[69,106,"m",912.0],[69,107,"m",111.0],[70,92,"p",1130.0],[70,93,"p",663.0],[70,94,"p",4550.0],[70,95,"p",594.0],[70,96,"p",204000.0],[70,97,"p",1050.0],[70,98,"s",0.0],[70,99,"p",2770000.0],[70,100,"s",0.0],[70,101,"s",0.0],[70,102,"s",0.0],[70,103,"s",0.0],[70,104,"s",0.0],[70,105,"m",362000.0],[70,106,"s",0.0],[70,107,"m",6880.0],[70,108,"m",4440.0],[70,109,"m",480.0],[71,94,"p",644.0],[71,96,"p",3090.0],[71,98,"p",123000.0],[71,99,"p",174000.0],[71,100,"p",712000.0],[71,101,"p",579000.0],[71,102,"p",43200000.0],[71,103,"p",104000000.0],[71,104,"s",0.0],[71,105,"m",1.21e+18],[71,106,"m",574000.0],[71,107,"m",1700.0],[71,108,"m",16500.0],[71,109,"m",342.0],[71,110,"m",210.0],[72,95,"p",123.0],[72,97,"p",194.0],[72,98,"p",57600.0],[72,100,"p",59000000.0],[72,101,"p",85000.0],[72,102,"a",6.31e+22],[72,103,"p",6050000.0],[72,104,"s",0.0],[72,105,"s",0.0],[72,106,"s",0.0],[72,107,"s",0.0],[72,108,"s",0.0],[72,109,"m",3660000.0],[72,110,"m",284000000000000.0],[72,111,"m",3840.0],[72,112,"m",14800.0],[73,97,"p",406.0],[73,99,"p",2210.0],[73,100,"p",11300.0],[73,101,"p",4100.0],[73,102,"p",37800.0],[73,103,"p",29100.0],[73,104,"p",204000.0],[73,105,"p",559.0],[73,106,"p",57400000.0],[73,107,"p",29300.0],[73,108,"s",0.0],[73,109,"m",9890000.0],[73,110,"m",441000.0],[73,111,"m",31300.0],[73,112,"m",2960.0],[73,113,"m",630.0],[74,103,"p",7920.0],[74,104,"p",1870000.0],[74,105,"p",2220.0],[74,106,"s",0.0],[74,107,"p",10500000.0],[74,108,"s",0.0],[74,109,"s",0.0],[74,110,"s",0.0],[74,111,"m",6490000.0],[74,112,"s",0.0],[74,113,"m",85400.0],[74,114,"m",6030000.0],[74,116,"m",1800.0],[75,103,"p",792.0],[75,104,"p",1170.0],[75,105,"p",146.0],[75,106,"p",71600.0],[75,107,"p",230000.0],[75,108,"p",6050000.0],[75,109,"p",3280000.0],[75,110,"s",0.0],[75,111,"m",321000.0],[75,112,"m",1.3e+18],[75,113,"m",61200.0],[75,114,"m",87500.0],[75,115,"m",186.0],[76,104,"p",1290.0],[76,105,"p",6300.0],[76,106,"p",79600.0],[76,107,"p",46800.0],[76,108,"s",0.0],[76,109,"p",8090000.0],[76,110,"a",6.31e+22],[76,111,"s",0.0],[76,112,"s",0.0],[76,113,"s",0.0],[76,114,"s",0.0],[76,115,"m",1330000.0],[76,116,"s",0.0],[76,117,"m",108000.0],[76,118,"m",189000000.0],[76,120,"m",2090.0],[77,103,"p",90.0],[77,105,"p",900.0],[77,106,"p",3480.0],[77,107,"p",11100.0],[77,108,"p",51800.0],[77,109,"p",59900.0],[77,110,"p",37800.0],[77,111,"p",149000.0],[77,112,"p",1140000.0],[77,113,"p",1020000.0],[77,114,"s",0.0],[77,115,"m",6380000.0],[77,116,"s",0.0],[77,117,"m",69400.0],[77,118,"m",9000.0],[77,119,"m",52.0],[78,106,"p",1040.0],[78,108,"p",7490.0],[78,109,"p",8460.0],[78,110,"p",881000.0],[78,111,"p",39100.0],[78,112,"a",2.05e+19],[78,113,"p",242000.0],[78,114,"s",0.0],[78,115,"p",1580000000.0],[78,116,"s",0.0],[78,117,"s",0.0],[78,118,"s",0.0],[78,119,"m",71600.0],[78,120,"s",0.0],[78,121,"m",1850.0],[78,122,"m",45000.0],[78,124,"m",158000.0],[79,107,"p",642.0],[79,108,"p",504.0],[79,111,"p",2570.0],[79,112,"p",11400.0],[79,113,"p",17800.0],[79,114,"p",63500.0],[79,115,"p",137000.0],[79,116,"p",16100000.0],[79,117,"p",534000.0],[79,118,"s",0.0],[79,119,"m",233000.0],[79,120,"m",271000.0],[79,121,"m",2900.0],[79,122,"m",1560.0],[79,123,"m",28.8],[80,110,"p",1200.0],[80,112,"p",17500.0],[80,113,"p",13700.0],[80,114,"p",13900000000.0],[80,115,"p",37900.0],[80,116,"s",0.0],[80,117,"p",234000.0],[80,118,"s",0.0],[80,119,"s",0.0],[80,120,"s",0.0],[80,121,"s",0.0],[80,122,"s",0.0],[80,123,"m",4030000.0],[80,124,"s",0.0],[80,125,"m",312.0],[80,126,"m",489.0],[80,127,"m",174.0],[81,109,"p",156.0],[81,113,"p",1980.0],[81,114,"p",4180.0],[81,115,"p",6620.0],[81,116,"p",10200.0],[81,117,"p",19100.0],[81,118,"p",26700.0],[81,119,"p",94000.0],[81,120,"p",262000.0],[81,121,"p",1060000.0],[81,122,"s",0.0],[81,123,"m",119000000.0],[81,124,"s",0.0],[81,125,"m",252.0],[81,126,"m",286.0],[81,127,"m",183.0],[81,128,"m",130.0],[81,129,"m",78.0],[82,112,"p",720.0],[82,114,"p",2220.0],[82,115,"p",480.0],[82,116,"p",8640.0],[82,117,"p",5400.0],[82,118,"p",77400.0],[82,119,"p",33600.0],[82,120,"p",1660000000000.0],[82,121,"p",187000.0],[82,122,"s",0.0],[82,123,"p",483000000000000.0],[82,124,"s",0.0],[82,125,"s",0.0],[82,126,"s",0.0],[82,127,"m",11700.0],[82,128,"m",701000000.0],[82,129,"m",2170.0],[82,130,"m",38300.0],[82,132,"m",1610.0],[83,114,"p",558.0],[83,117,"p",2180.0],[83,118,"p",6480.0],[83,119,"p",6190.0],[83,120,"p",42300.0],[83,121,"p",40400.0],[83,122,"p",1320000.0],[83,123,"p",539000.0],[83,124,"p",1040000000.0],[83,125,"p",11600000000000.0],[83,126,"a",6e+26],[83,127,"m",433000.0],[83,128,"a",128.0],[83,129,"m",3630.0],[83,130,"m",2740.0],[83,131,"m",1190.0],[83,132,"m",456.0],[83,133,"m",130.0],[84,119,"p",2200.0],[84,120,"p",12700.0],[84,121,"p",5980.0],[84,122,"p",760000.0],[84,123,"p",20900.0],[84,124,"a",91500000.0],[84,125,"a",3220000000.0],[84,126,"a",12000000.0],[84,127,"a",0.516],[84,128,"a",2.99e-07],[84,129,"a",4.2e-06],[84,130,"a",0.000164],[84,131,"a",0.00178],[84,132,"a",0.145],[84,134,"a",186.0],[85,119,"p",552.0],[85,120,"p",1570.0],[85,121,"p",1840.0],[85,122,"p",6480.0],[85,123,"p",5870.0],[85,124,"p",19500.0],[85,125,"p",29200.0],[85,126,"p",26000.0],[85,130,"a",0.0001],[85,131,"a",0.0003],[85,132,"a",0.0323],[85,133,"a",1.5],[85,134,"a",56.0],[85,135,"m",223.0],[86,121,"p",555.0],[86,123,"p",1710.0],[86,124,"a",8640.0],[86,125,"p",52600.0],[86,126,"a",1430.0],[86,129,"a",2.3e-06],[86,130,"a",4.5e-05],[86,131,"a",0.00054],[86,132,"a",0.035],[86,133,"a",3.96],[86,134,"a",55.6],[86,136,"a",330000.0],[86,137,"m",1460.0],[87,125,"p",1200.0],[87,132,"a",0.02],[87,133,"a",27.4],[87,134,"a",294.0],[87,135,"m",852.0],[87,136,"m",1320.0],[87,137,"m",200.0],[87,140,"m",148.0],[88,131,"a",0.01],[88,132,"a",0.0179],[88,133,"a",28.0],[88,134,"a",38.0],[88,135,"a",988000.0],[88,136,"a",316000.0],[88,137,"m",1290000.0],[88,138,"a",50500000000.0],[88,139,"m",2530.0],[88,140,"m",181000000.0],[88,142,"m",5580.0],[89,134,"a",126.0],[89,135,"p",10000.0],[89,136,"a",864000.0],[89,137,"m",106000.0],[89,138,"m",687000000.0],[89,139,"m",22100.0],[89,141,"m",122.0],[89,142,"m",450.0],[89,143,"m",119.0],[89,144,"m",145.0],[90,133,"a",0.6],[90,134,"a",1.05],[90,136,"a",1830.0],[90,137,"a",1610000.0],[90,138,"a",60300000.0],[90,139,"a",232000000000.0],[90,140,"a",2380000000000.0],[90,141,"m",91900.0],[90,142,"a",4.43e+17],[90,143,"m",1340.0],[90,144,"m",2080000.0],[90,145,"m",426.0],[90,146,"m",2250.0],[91,136,"a",2300.0],[91,137,"p",79200.0],[91,138,"p",130000.0],[91,139,"p",1500000.0],[91,140,"a",1030000000000.0],[91,141,"m",113000.0],[91,142,"m",2330000.0],[91,143,"m",24100.0],[91,144,"m",1470.0],[91,145,"m",546.0],[91,146,"m",522.0],[92,135,"a",66.0],[92,136,"a",546.0],[92,138,"a",1800000.0],[92,139,"p",363000.0],[92,140,"a",2170000000.0],[92,141,"a",5020000000000.0],[92,142,"a",7750000000000.0],[92,143,"a",2.22e+16],[92,144,"a",739000000000000.0],[92,145,"m",583000.0],[92,146,"a",1.41e+17],[92,147,"m",1410.0],[92,148,"m",50800.0],[92,150,"m",1010.0],[93,139,"p",882.0],[93,140,"p",2170.0],[93,141,"p",380000.0],[93,142,"p",34200000.0],[93,143,"p",4860000000000.0],[93,144,"a",67700000000000.0],[93,145,"m",183000.0],[93,146,"m",204000.0],[93,147,"m",3710.0],[93,148,"m",834.0],[93,149,"m",132.0],[94,138,"p",2020.0],[94,140,"p",31700.0],[94,141,"p",1520.0],[94,142,"a",90200000.0],[94,143,"p",3910000.0],[94,144,"a",2770000000.0],[94,145,"a",761000000000.0],[94,146,"a",207000000000.0],[94,147,"m",453000000.0],[94,148,"a",11800000000000.0],[94,149,"m",17800.0],[94,150,"a",2520000000000000.0],[94,151,"m",37800.0],[94,152,"m",937000.0],[95,142,"p",4380.0],[95,143,"p",5880.0],[95,144,"p",42800.0],[95,145,"p",183000.0],[95,146,"a",13600000000.0],[95,147,"m",57700.0],[95,148,"a",233000000000.0],[95,149,"m",36400.0],[95,150,"m",7380.0],[95,151,"m",2340.0],[95,152,"m",1380.0],[96,142,"p",8640.0],[96,143,"p",10400.0],[96,144,"a",2330000.0],[96,145,"p",2830000.0],[96,146,"a",14100000.0],[96,147,"a",918000000.0],[96,148,"a",571000000.0],[96,149,"a",268000000000.0],[96,150,"a",150000000000.0],[96,151,"a",492000000000000.0],[96,152,"a",11000000000000.0],[96,153,"m",3850.0],[96,154,"f",262000000000.0],[96,155,"m",1010.0],[97,148,"p",427000.0],[97,149,"p",156000.0],[97,150,"a",43500000000.0],[97,152,"m",28500000.0],[97,153,"m",11600.0],[97,154,"m",3340.0],[98,146,"a",1160.0],[98,148,"a",129000.0],[98,149,"p",11200.0],[98,150,"a",28900000.0],[98,151,"a",11100000000.0],[98,152,"a",413000000.0],[98,153,"a",28400000000.0],[98,154,"a",83500000.0],[98,155,"m",1540000.0],[98,156,"f",5230000.0],[98,157,"m",5100.0],[99,150,"p",6130.0],[99,151,"p",31000.0],[99,152,"p",119000.0],[99,154,"a",1770000.0],[99,155,"a",23800000.0],[99,156,"m",3440000.0],[99,157,"m",1520.0],[100,151,"p",19100.0],[100,152,"a",91400.0],[100,153,"p",259000.0],[100,154,"a",11700.0],[100,155,"a",72300.0],[100,156,"f",9460.0],[100,157,"a",8680000.0]],"s":{"1":"H","2":"He","3":"Li","4":"Be","5":"B","6":"C","7":"N","8":"O","9":"F","10":"Ne","11":"Na","12":"Mg","13":"Al","14":"Si","15":"P","16":"S","17":"Cl","18":"Ar","19":"K","20":"Ca","21":"Sc","22":"Ti","23":"V","24":"Cr","25":"Mn","26":"Fe","27":"Co","28":"Ni","29":"Cu","30":"Zn","31":"Ga","32":"Ge","33":"As","34":"Se","35":"Br","36":"Kr","37":"Rb","38":"Sr","39":"Y","40":"Zr","41":"Nb","42":"Mo","43":"Tc","44":"Ru","45":"Rh","46":"Pd","47":"Ag","48":"Cd","49":"In","50":"Sn","51":"Sb","52":"Te","53":"I","54":"Xe","55":"Cs","56":"Ba","57":"La","58":"Ce","59":"Pr","60":"Nd","61":"Pm","62":"Sm","63":"Eu","64":"Gd","65":"Tb","66":"Dy","67":"Ho","68":"Er","69":"Tm","70":"Yb","71":"Lu","72":"Hf","73":"Ta","74":"W","75":"Re","76":"Os","77":"Ir","78":"Pt","79":"Au","80":"Hg","81":"Tl","82":"Pb","83":"Bi","84":"Po","85":"At","86":"Rn","87":"Fr","88":"Ra","89":"Ac","90":"Th","91":"Pa","92":"U","93":"Np","94":"Pu","95":"Am","96":"Cm","97":"Bk","98":"Cf","99":"Es","100":"Fm","101":"Md","102":"No","103":"Lr","104":"Rf","105":"Db","106":"Sg","107":"Bh","108":"Hs","109":"Mt","110":"Ds","111":"Rg","112":"Cn","113":"Nh","114":"Fl","115":"Mc","116":"Lv","117":"Ts","118":"Og"}};
    var COLS = { s: '#1E293B', m: '#2A6BC4', p: '#DB2777', a: '#D97706', f: '#16A34A' };
    var NOMS = { s: 'stable', m: '\u03b2\u207b', p: '\u03b2\u207a (ou capture électronique)', a: '\u03b1', f: 'fission spontanée' };
    var cv = $(root, 'canvas'), info = $(root, '.nt-nz-info'), btnAll = $(root, '[data-act="all"]'), S, sel = null, chain = [], view = null, G = null;
    var ALL = [0, 100, 0, 160], cur = ALL.slice(), curH = 600, anim = null;   /* vue affichée (interpolée pendant les transitions) */
    var IDX = {}; D.n.forEach(function (r) { IDX[r[0] + ',' + r[1]] = r; });
    function fille(r) {
      if (r[2] === 'a') { return [r[0] - 2, r[1] - 2]; } if (r[2] === 'm') { return [r[0] + 1, r[1] - 1]; } if (r[2] === 'p') { return [r[0] - 1, r[1] + 1]; } return null;
    }
    function nom(Z, N) { return (D.s[Z] || '?') + '\u00a0' + (Z + N); }
    /* chaîne de désintégration (mode principal) jusqu'à un noyau stable */
    function buildChain(r) {
      var c = [r], cur = r, guard = 0;
      while (cur[2] !== 's' && guard++ < 40) { var f = fille(cur); if (!f) { break; } var nx = IDX[f[0] + ',' + f[1]]; if (!nx) { c.push([f[0], f[1], '?', 0]); break; } c.push(nx); cur = nx; }
      return c;
    }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, z0, z1, n0, n1;
      c.clearRect(0, 0, w, h);
      z0 = cur[0]; z1 = cur[1]; n0 = cur[2]; n1 = cur[3];
      var L = 44, B = 30, T = 10, cs = Math.min((w - L - 20) / (z1 - z0 + 1), (h - B - T) / (n1 - n0 + 1));   /* cases carrées */
      var gw = cs * (z1 - z0 + 1), gh = cs * (n1 - n0 + 1), ox = L + (w - L - 20 - gw) / 2, oy = T + (h - B - T - gh) / 2;
      function X(z) { return ox + (z - z0 + 0.5) * cs; }
      function Y(n) { return oy + gh - (n - n0 + 0.5) * cs; }
      G = { X: X, Y: Y, cs: cs };
      /* axes */
      c.strokeStyle = col('--ink'); c.lineWidth = 1; c.beginPath(); c.moveTo(ox, oy); c.lineTo(ox, oy + gh); c.lineTo(ox + gw, oy + gh); c.stroke();
      var sz = z1 - z0 > 50 ? 20 : (z1 - z0 > 20 ? 5 : 2), sn = n1 - n0 > 50 ? 20 : (n1 - n0 > 20 ? 5 : 2);
      c.fillStyle = col('--muted'); c.font = '11px system-ui, sans-serif'; c.textAlign = 'center';
      for (var z = Math.ceil(z0 / sz) * sz; z <= z1 + 1e-9; z += sz) { c.fillText(z, X(z), oy + gh + 14); }
      c.textAlign = 'right'; for (var n = Math.ceil(n0 / sn) * sn; n <= n1 + 1e-9; n += sn) { c.fillText(n, ox - 5, Y(n) + 4); }
      c.textAlign = 'center'; c.fillText('nombre de protons Z', ox + gw / 2, h - 3);
      c.save(); c.translate(ox - 30, oy + gh / 2); c.rotate(-Math.PI / 2); c.fillText('nombre de neutrons N', 0, 0); c.restore();
      /* droite N = Z */
      var a0 = Math.max(z0, n0), a1 = Math.min(z1, n1);
      if (a1 > a0) { c.strokeStyle = 'rgba(30,41,59,.3)'; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(X(a0), Y(a0)); c.lineTo(X(a1), Y(a1)); c.stroke(); c.setLineDash([]); }
      var inChain = {}; chain.forEach(function (r) { inChain[r[0] + ',' + r[1]] = true; });
      var labels = cs >= 20;
      D.n.forEach(function (r) {
        if (r[0] < z0 || r[0] > z1 || r[1] < n0 || r[1] > n1) { return; }
        var on = !chain.length || inChain[r[0] + ',' + r[1]];
        c.globalAlpha = on ? 1 : 0.18; c.fillStyle = COLS[r[2]];
        c.fillRect(X(r[0]) - cs * 0.46, Y(r[1]) - cs * 0.46, cs * 0.92, cs * 0.92);
        if (labels) {
          c.fillStyle = '#fff'; c.textAlign = 'center';
          c.font = '700 ' + Math.round(cs * 0.34) + 'px system-ui, sans-serif'; c.fillText(D.s[r[0]] || '', X(r[0]), Y(r[1]) + cs * 0.02);
          c.font = Math.round(cs * 0.26) + 'px system-ui, sans-serif'; c.fillText(r[0] + r[1], X(r[0]), Y(r[1]) + cs * 0.32);
        }
      });
      c.globalAlpha = 1;
      /* flèches de la chaîne : trait sombre bordé de blanc, bien visible sur toutes les couleurs */
      for (var i = 0; i + 1 < chain.length; i++) {
        var p = chain[i], q = chain[i + 1], x1 = X(p[0]), y1 = Y(p[1]), x2 = X(q[0]), y2 = Y(q[1]);
        var dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy), ux = dx / len, uy = dy / len, s0 = cs * 0.3, s1 = cs * 0.3;
        var ax = x1 + ux * s0, ay = y1 + uy * s0, bx = x2 - ux * s1, by = y2 - uy * s1, hl = Math.max(8, cs * 0.28), hw = hl * 0.55;
        [['#fff', 6], ['#0F172A', 2.6]].forEach(function (st) {
          c.strokeStyle = st[0]; c.fillStyle = st[0]; c.lineWidth = st[1]; c.lineCap = 'round';
          c.beginPath(); c.moveTo(ax, ay); c.lineTo(bx - ux * hl * 0.6, by - uy * hl * 0.6); c.stroke();
          var e = st[0] === '#fff' ? 2 : 0;
          c.beginPath(); c.moveTo(bx + ux * e, by + uy * e); c.lineTo(bx - ux * (hl + e) - uy * (hw + e), by - uy * (hl + e) + ux * (hw + e)); c.lineTo(bx - ux * (hl + e) + uy * (hw + e), by - uy * (hl + e) - ux * (hw + e)); c.closePath(); c.fill();
        });
      }
      if (sel) { c.strokeStyle = '#F59E0B'; c.lineWidth = 3; c.strokeRect(X(sel[0]) - cs * 0.55, Y(sel[1]) - cs * 0.55, cs * 1.1, cs * 1.1); }
      /* légende */
      var outside = w - (ox + gw) > 80, lx = outside ? ox + gw + 14 : ox + 8, ly = oy + 14;   /* légende à droite du diagramme quand il y a la place */
      ['s', 'm', 'p', 'a'].forEach(function (k, j) {
        c.fillStyle = COLS[k]; c.fillRect(lx, ly + j * 18 - 9, 11, 11);
        txt(c, { s: 'stable', m: '\u03b2\u207b', p: '\u03b2\u207a', a: '\u03b1' }[k], lx + 16, ly + j * 18 + 1, col('--ink'), '600 12px system-ui, sans-serif', 'left');
      });
    }
    /* transition douce : la fenêtre (Z, N) et la hauteur du canevas glissent vers leur cible */
    function goTo(target, h) {
      var from = cur.slice(), h0 = curH, t0 = null, DUR = RM ? 1 : 650;
      if (anim) { cancelAnimationFrame(anim); }
      function frameStep(ts) {
        if (t0 === null) { t0 = ts; }
        var u = Math.min(1, (ts - t0) / DUR), e = u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
        for (var k = 0; k < 4; k++) { cur[k] = from[k] + (target[k] - from[k]) * e; }
        var hh = h0 + (h - h0) * e; if (Math.abs(hh - curH) > 0.5 || u === 1) { curH = hh; cv.style.height = Math.round(curH) + 'px'; S = canvasCtx(cv); }
        draw();
        anim = u < 1 ? requestAnimationFrame(frameStep) : null;
      }
      anim = requestAnimationFrame(frameStep);
    }
    function select(r) {
      sel = r; chain = r ? buildChain(r) : [];
      if (!r) { view = null; btnAll.disabled = true; goTo(ALL, 600); info.innerHTML = 'Cliquez sur un noyau (ou un raccourci) pour zoomer sur sa chaîne de désintégration.'; draw(); return; }
      var zs = chain.map(function (q) { return q[0]; }), ns = chain.map(function (q) { return q[1]; });
      var zmin = Math.min.apply(null, zs) - 2, zmax = Math.max.apply(null, zs) + 2, nmin = Math.min.apply(null, ns) - 2, nmax = Math.max.apply(null, ns) + 2;
      while (zmax - zmin < 9) { zmin--; zmax++; } while (nmax - nmin < 11) { nmin--; nmax++; }
      view = [Math.max(0, zmin), zmax, Math.max(0, nmin), nmax]; btnAll.disabled = false;
      var need = (view[3] - view[2] + 1) * 34 + 44, wmax = cv.clientWidth - 64;
      if ((view[1] - view[0] + 1) * 34 > wmax) { need = (view[3] - view[2] + 1) * wmax / (view[1] - view[0] + 1) + 44; }
      goTo(view, Math.max(420, Math.min(1000, need)));
      var parts = chain.map(function (q, i) {
        var s = '<b>' + nom(q[0], q[1]) + '</b>';
        if (i + 1 < chain.length) { s += ' <span style="color:' + COLS[q[2]] + ';font-weight:700;">\u2014' + NOMS[q[2]].split(' ')[0] + ' (' + duree(q[3]) + ')\u2192</span> '; }
        return s;
      });
      var last = chain[chain.length - 1];
      info.innerHTML = '<b>' + nom(r[0], r[1]) + '</b> (Z = ' + r[0] + ', N = ' + r[1] + ') : ' + (r[2] === 's' ? 'noyau stable.' : 'radioactif ' + NOMS[r[2]] + ', demi-vie ' + duree(r[3]) + '.') +
        (chain.length > 1 ? '<br><span class="nt-note">Chaîne de désintégration (mode principal, avec les demi-vies)&nbsp;: ' + parts.join('') + (last[2] === 's' ? ' (stable)' : '') + '</span>' : '');
    }
    cv.addEventListener('click', function (e) {
      if (!G) { return; }
      var rc = cv.getBoundingClientRect(), mx = e.clientX - rc.left, my = e.clientY - rc.top, best = null, bd = 1e9;
      D.n.forEach(function (r) { var d = Math.hypot(G.X(r[0]) - mx, G.Y(r[1]) - my); if (d < bd) { bd = d; best = r; } });
      if (bd < Math.max(10, G.cs)) { select(best); }
    });
    btnAll.addEventListener('click', function () { select(null); });
    $$(root, '[data-nuc]').forEach(function (b) { b.addEventListener('click', function () { var p = b.getAttribute('data-nuc').split(','); var r = IDX[p[0] + ',' + p[1]]; if (r) { select(r); } }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup); select(null);
  })();
  /* ================= 2. Le hasard et la loi de décroissance ================= */
  (function () {
    var root = document.getElementById('lab-decay');
    if (!root) { return; }
    var cv = $(root, 'canvas.grid'), cg = $(root, 'canvas.graph'), btn = $(root, '[data-act="go"]'), cbD = $(root, '[data-p="demi"]'), oN = $(root, '.out-n'), oT = $(root, '.out-th');
    var S, SG, N0 = 400, alive = [], t = 0, hist = [], running = false, last = null, LAM = Math.log(2), TMAX = 6, SPEED = 1.0;
    function reset() { alive = []; for (var i = 0; i < N0; i++) { alive.push(true); } t = 0; hist = [[0, N0]]; }
    function count() { var n = 0; alive.forEach(function (a) { if (a) { n++; } }); return n; }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, cols = Math.ceil(Math.sqrt(N0 * w / h)), rows = Math.ceil(N0 / cols), cs = Math.min(w / cols, h / rows);
      c.clearRect(0, 0, w, h);
      for (var i = 0; i < N0; i++) {
        var x = (i % cols) * cs, y = Math.floor(i / cols) * cs;
        c.fillStyle = alive[i] ? '#F59E0B' : '#E2E8F0'; c.beginPath(); c.arc(x + cs / 2, y + cs / 2, Math.max(1.2, cs * 0.38), 0, 2 * Math.PI); c.fill();
      }
      var g = SG.ctx, W = SG.w, H = SG.h; g.clearRect(0, 0, W, H);
      var F = frame(g, W, H, { x0: 0, x1: TMAX, dx: 1, y0: 0, y1: N0, dy: N0 / 4, xl: 'temps (en demi-vies)', yl: 'noyaux restants N', L: 50 });
      if (cbD.checked) {
        g.strokeStyle = 'rgba(5,150,105,.6)'; g.setLineDash([4, 4]); g.lineWidth = 1.2;
        for (var k = 1; k <= 4; k++) { g.beginPath(); g.moveTo(F.L, F.Y(N0 / Math.pow(2, k))); g.lineTo(F.X(k), F.Y(N0 / Math.pow(2, k))); g.lineTo(F.X(k), F.B); g.stroke(); txt(g, 'N\u2080/' + Math.pow(2, k), F.X(k) + 4, F.Y(N0 / Math.pow(2, k)) - 5, '#059669', '600 11px system-ui, sans-serif', 'left'); }
        g.setLineDash([]);
      }
      g.strokeStyle = 'rgba(42,107,196,.8)'; g.lineWidth = 2; g.setLineDash([6, 4]); g.beginPath();
      for (var s = 0; s <= TMAX; s += 0.02) { var yv = F.Y(N0 * Math.exp(-LAM * s)); if (s === 0) { g.moveTo(F.X(s), yv); } else { g.lineTo(F.X(s), yv); } }
      g.stroke(); g.setLineDash([]);
      g.strokeStyle = '#D97706'; g.lineWidth = 2.4; g.beginPath();
      hist.forEach(function (p, j) { if (j === 0) { g.moveTo(F.X(p[0]), F.Y(p[1])); } else { g.lineTo(F.X(p[0]), F.Y(hist[j - 1][1])); g.lineTo(F.X(p[0]), F.Y(p[1])); } });
      g.stroke();
      txt(g, 'simulation', F.R - 70, F.T + 14, '#D97706', '700 12px system-ui, sans-serif', 'left');
      txt(g, 'N\u2080 e^(\u2212\u03bbt)', F.R - 70, F.T + 30, '#2A6BC4', '700 12px system-ui, sans-serif', 'left');
      var n = count(); oN.textContent = n + ' (modèle\u00a0: ' + Math.round(N0 * Math.exp(-LAM * t)) + ')';
    }
    function step(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (running) {
        var d = dt * SPEED; t += d;
        for (var i = 0; i < N0; i++) { if (alive[i] && Math.random() < LAM * d) { alive[i] = false; } }
        var n = count(); if (n !== hist[hist.length - 1][1]) { hist.push([t, n]); }
        if (oT.dataset.done !== '1' && n <= N0 / 2) { oT.textContent = 'atteinte à t = ' + fr(t, 2) + ' (théorie\u00a0: 1)'; oT.dataset.done = '1'; }
        if (t >= TMAX || n === 0) { running = false; hist.push([t, n]); btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; }
        draw();
      }
      requestAnimationFrame(step);
    }
    btn.addEventListener('click', function () { if (running) { return; } reset(); oT.textContent = '\u2014'; oT.dataset.done = ''; running = true; btn.innerHTML = '<i class="fa-solid fa-radiation"></i>&nbsp; En cours\u2026'; });
    $$(root, 'input[name="n0"]').forEach(function (x) { x.addEventListener('change', function () { N0 = +x.value; running = false; reset(); oT.textContent = '\u2014'; oT.dataset.done = ''; btn.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Lancer'; draw(); }); });
    cbD.addEventListener('change', draw);
    function setup() { S = canvasCtx(cv); SG = canvasCtx(cg); draw(); }
    reset(); setup(); onResize(setup); requestAnimationFrame(step);
  })();
  /* ================= 3. Dater un échantillon au carbone 14 ================= */
  (function () {
    var root = document.getElementById('lab-datation');
    if (!root) { return; }
    var cv = $(root, 'canvas'), r = $(root, 'input[type="range"]'), oA = $(root, '.out-a'), oR = $(root, '.out-r'), oT = $(root, '.out-age'), S;
    var A0 = 0.226, TH = 5730, LAM = Math.log(2) / TH;   /* Bq par gramme de carbone ; années */
    function draw() {
      var A = +r.value, age = Math.log(A0 / A) / LAM, c = S.ctx, w = S.w, h = S.h;
      oA.textContent = fr(A, 3) + ' Bq par gramme de carbone'; oR.textContent = fr(100 * A / A0, 1) + ' %'; oT.textContent = Math.round(age / 10) * 10 > 0 ? Math.round(age / 10) * 10 + ' ans' : '0 an';
      c.clearRect(0, 0, w, h);
      var F = frame(c, w, h, { x0: 0, x1: 40000, dx: 5000, y0: 0, y1: 0.25, dy: 0.05, xl: 'âge (années)', yl: 'activité (Bq/g de carbone)', L: 54, fx: function (v) { return v === 0 ? '0' : (v / 1000) + '\u202f000'; }, fy: function (v) { return fr(v, 2); } });
      c.strokeStyle = '#2A6BC4'; c.lineWidth = 2.4; c.beginPath();
      for (var s = 0; s <= 40000; s += 200) { var y = F.Y(A0 * Math.exp(-LAM * s)); if (s === 0) { c.moveTo(F.X(s), y); } else { c.lineTo(F.X(s), y); } }
      c.stroke();
      for (var k = 1; k <= 6; k++) { c.fillStyle = 'rgba(5,150,105,.7)'; c.beginPath(); c.arc(F.X(k * TH), F.Y(A0 / Math.pow(2, k)), 3, 0, 2 * Math.PI); c.fill(); }
      if (age <= 40000) {
        c.strokeStyle = '#D97706'; c.setLineDash([5, 4]); c.lineWidth = 1.6;
        c.beginPath(); c.moveTo(F.L, F.Y(A)); c.lineTo(F.X(age), F.Y(A)); c.lineTo(F.X(age), F.B); c.stroke(); c.setLineDash([]);
        c.fillStyle = '#D97706'; c.beginPath(); c.arc(F.X(age), F.Y(A), 6, 0, 2 * Math.PI); c.fill();
      }
    }
    r.addEventListener('input', draw);
    $$(root, '[data-a]').forEach(function (b) { b.addEventListener('click', function () { r.value = b.getAttribute('data-a'); draw(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); onResize(setup);
  })();
  /* ================= 4. La tomographie par émission de positons ================= */
  (function () {
    var root = document.getElementById('lab-tep');
    if (!root) { return; }
    var cv = $(root, 'canvas'), btn = $(root, '[data-act="play"]'), rst = $(root, '[data-act="reset"]'), cbL = $(root, '[data-p="lignes"]'), oN = $(root, '.out-ev'), S;
    var playing = !RM, visible = true, last = null, ev = [], acc = 0, nEv = 0, NDET = 48, RATE = 12, layer = null, lctx = null;
    var TUM = [0.28, -0.18];   /* position de la tumeur (en rayons de la couronne) */
    function rnd() { var u = Math.random() || 1e-9, v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
    function newEvent() {
      var p;
      if (Math.random() < 0.55) { p = [TUM[0] + 0.035 * rnd(), TUM[1] + 0.035 * rnd()]; }   /* le traceur s'accumule dans la tumeur */
      else { do { p = [(Math.random() * 2 - 1) * 0.52, (Math.random() * 2 - 1) * 0.62]; } while (p[0] * p[0] / 0.27 + p[1] * p[1] / 0.384 > 1); }
      var a = Math.random() * Math.PI, u = [Math.cos(a), Math.sin(a)];
      function hit(sg) {   /* intersection de la demi-droite avec la couronne (rayon 1) */
        var b = p[0] * u[0] * sg + p[1] * u[1] * sg, cc = p[0] * p[0] + p[1] * p[1] - 1, s = -b + Math.sqrt(b * b - cc);
        return [p[0] + sg * u[0] * s, p[1] + sg * u[1] * s];
      }
      ev.push({ p: p, h1: hit(1), h2: hit(-1), t: 0 }); nEv++;
    }
    /* chaque droite est tracée une seule fois sur un calque hors écran : la mémoire et le temps de calcul restent constants */
    function makeLayer() {
      layer = document.createElement('canvas'); layer.width = cv.width; layer.height = cv.height;
      lctx = layer.getContext('2d'); var dpr = window.devicePixelRatio || 1; lctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    function addLine(a, b) {
      if (!lctx) { return; }
      var R = Math.min(S.w, S.h) * 0.42, cx = S.w / 2, cy = S.h / 2;
      lctx.strokeStyle = 'rgba(253,224,71,.09)'; lctx.lineWidth = 1;
      lctx.beginPath(); lctx.moveTo(cx + a[0] * R, cy - a[1] * R); lctx.lineTo(cx + b[0] * R, cy - b[1] * R); lctx.stroke();
    }
    function det(q) { var a = Math.atan2(q[1], q[0]); return Math.round(((a + 2 * Math.PI) % (2 * Math.PI)) / (2 * Math.PI) * NDET) % NDET; }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, R = Math.min(w, h) * 0.42, cx = w / 2, cy = h / 2;
      function P(q) { return [cx + q[0] * R, cy - q[1] * R]; }
      c.clearRect(0, 0, w, h);
      c.fillStyle = '#0B1220'; c.fillRect(0, 0, w, h);
      c.fillStyle = 'rgba(251,207,232,.10)'; c.strokeStyle = 'rgba(251,207,232,.45)'; c.lineWidth = 1.2;
      c.beginPath(); c.ellipse(cx, cy, 0.52 * R, 0.62 * R, 0, 0, 2 * Math.PI); c.fill(); c.stroke();
      /* droites de réponse accumulées */
      if (cbL.checked && layer) { c.drawImage(layer, 0, 0, w, h); }   /* calque des droites accumulées */
      /* détecteurs */
      var lit = {};
      ev.forEach(function (e) { if (e.t >= 1) { lit[det(e.h1)] = 1; lit[det(e.h2)] = 1; } });
      for (var i = 0; i < NDET; i++) {
        var a = 2 * Math.PI * i / NDET, x = cx + (R + 9) * Math.cos(a), y = cy - (R + 9) * Math.sin(a);
        c.save(); c.translate(x, y); c.rotate(-a); c.fillStyle = lit[i] ? '#FDE047' : '#334155'; c.fillRect(-6, -R * 2 * Math.PI / NDET / 2 + 1, 12, R * 2 * Math.PI / NDET - 2); c.restore();
      }
      /* photons en vol */
      ev.forEach(function (e) {
        var o = P(e.p), f = Math.min(e.t, 1);
        if (e.t < 0.15) { c.fillStyle = 'rgba(232,121,249,' + (1 - e.t / 0.15) + ')'; c.beginPath(); c.arc(o[0], o[1], 6, 0, 2 * Math.PI); c.fill(); }
        [e.h1, e.h2].forEach(function (hq) {
          var hp = P(hq), x = o[0] + (hp[0] - o[0]) * f, y = o[1] + (hp[1] - o[1]) * f;
          c.fillStyle = '#FDE047'; c.beginPath(); c.arc(x, y, 3, 0, 2 * Math.PI); c.fill();
        });
        if (e.t >= 1 && e.t < 1.6) { var a1 = P(e.h1), a2 = P(e.h2); c.strokeStyle = 'rgba(253,224,71,' + (1.6 - e.t) + ')'; c.lineWidth = 1.5; c.beginPath(); c.moveTo(a1[0], a1[1]); c.lineTo(a2[0], a2[1]); c.stroke(); }
      });
      oN.textContent = nEv;
    }
    function step(ts) {
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      if (playing && visible && S) {
        acc += dt * RATE; while (acc > 1) { newEvent(); acc -= 1; }   /* débit constant */
        ev.forEach(function (e) { e.t += dt * 2.2; if (e.t >= 1 && !e.done) { addLine(e.h1, e.h2); e.done = true; } });
        ev = ev.filter(function (e) { return e.t < 1.6; });
      }
      if (visible && S) { draw(); }
      requestAnimationFrame(step);
    }
    btn.addEventListener('click', function () { playing = !playing; playLabel(btn, playing); });
    rst.addEventListener('click', function () { ev = []; nEv = 0; makeLayer(); });
    cbL.addEventListener('change', draw);
    function setup() { S = canvasCtx(cv); makeLayer(); draw(); }
    if ('IntersectionObserver' in window) { new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(cv); }
    playLabel(btn, playing); setup(); onResize(setup); requestAnimationFrame(step);
  })();
})();
</script>
