+++
title = "Corps purs et mélanges"
draft = false
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<style>
.nt-ql-q { font-size: 1.08em; text-align: center; margin: 0.5em 0 0.7em !important; min-height: 1.6em; }
.nt-ql-btns { display: flex; flex-wrap: wrap; gap: 0.45em; justify-content: center; }
.nt-big-score { font-size: 1.8em; font-weight: 800; color: var(--blue); margin-right: 0.3em; }
.nt-quizlab .nt-msg, .nt-lab .nt-msg { margin-top: 1em !important; }
.nt-figs { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8em; margin: 1em 0; }
.nt-figs figure { margin: 0; text-align: center; }
.nt-figs img { width: 100%; border-radius: 10px; }
.nt-figs figcaption { font-size: 0.88em; color: var(--muted); margin-top: 0.3em; }
.nt-tests { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.8em; margin: 1em 0; }
.nt-tests .nt-b { margin: 0; }
.nt-res { display: grid; grid-template-columns: auto 1fr; gap: 0.2em 0.6em; font-size: 0.95em; }
.nt-res .ok { color: #15803D; font-weight: 700; } .nt-res .ko { color: #B91C1C; font-weight: 700; }
.nt-rho-in { display: flex; align-items: center; gap: 0.5em; justify-content: center; flex-wrap: wrap; margin: 0.6em 0; }
.nt-rho-in input { font: inherit; width: 6em; padding: 0.3em 0.6em; border: 1.5px solid var(--line); border-radius: 8px; }
.nt-lab [hidden] { display: none !important; }
</style>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Les échelles de description de la matière {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Entité chimique</p>
<p>Objet pouvant être <span class="imp nt-hole">dénombré</span>. Les <span class="imp nt-hole">atomes</span> isolés, les <span class="imp nt-hole">ions</span> (entités électriquement chargées) et les <span class="imp nt-hole">molécules</span> (assemblages d'atomes) sont des entités chimiques. Une entité peut être décrite au moyen d'une formule chimique.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Il existe trois types d'entités chimiques&nbsp;:</p>
<ul class="nt-facts">
<li>un <span class="imp nt-hole">atome</span> est la plus petite entité chimique. Il est <b>électriquement neutre</b>. Exemple&nbsp;: l'atome de fer $\ce{Fe}$&nbsp;;</li>
<li>une <span class="imp nt-hole">molécule</span> est un <b>assemblage d'atomes</b> liés entre eux. Elle est électriquement neutre. Exemple&nbsp;: la molécule d'eau $\ce{H2O}$, formée de deux atomes d'hydrogène et d'un atome d'oxygène&nbsp;;</li>
<li>un <span class="imp nt-hole">ion</span> est un atome, ou un groupe d'atomes, qui a perdu ou gagné un ou plusieurs électrons&nbsp;: il est <b>électriquement chargé</b>. Exemples&nbsp;: l'ion sodium $\ce{Na+}$, l'ion chlorure $\ce{Cl-}$.</li>
</ul>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Espèce chimique</p>
<p><span class="imp nt-hole">Collection d'entités chimiques identiques</span>, à l'échelle macroscopique.</p>
<p>Le nom de l'espèce chimique (échelle macroscopique) sert souvent à désigner l'entité (échelle microscopique), et inversement, la formule de l'entité sert à désigner l'espèce&nbsp;: on parle de «&nbsp;la molécule d'eau de formule $\ce{H2O}$&nbsp;» comme de «&nbsp;l'eau de formule chimique $\ce{H2O}$&nbsp;».</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On peut préciser l'état physique d'une espèce chimique après sa formule&nbsp;: $\ce{H2O(s)}$ désigne la glace, $\ce{H2O(\ell)}$ l'eau liquide et $\ce{H2O(g)}$ la vapeur d'eau.</p>
</div>

<svg class='nt-svg' viewBox='0 0 700 300' role='img' aria-label="À gauche, un verre d'eau vu à l'échelle macroscopique : on voit l'espèce chimique eau. À droite, le même verre vu à la loupe imaginaire : on distingue les entités chimiques, les molécules d'eau"><path d='M20,30 L36,250 Q38,262 50,262 L170,262 Q182,262 184,250 L200,30' fill='#EEF4FA' stroke='#64748B' stroke-width='1.6'/><path d='M26.6,92 L41,248 Q43,258 52,258 L168,258 Q177,258 179,248 L193.4,92 Z' fill='#93C5FD' opacity='.75'/><line x1='110' y1='190' x2='208' y2='150' stroke='#1E293B' stroke-width='1'/><text x='212' y='146' font-size='14' fill='#1E293B' font-family='system-ui, sans-serif'>l'espèce</text><text x='212' y='163' font-size='14' fill='#1E293B' font-family='system-ui, sans-serif'>chimique eau</text><text x='110' y='288' font-size='13' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif'>échelle macroscopique</text><path d='M360,30 L376,250 Q378,262 390,262 L510,262 Q522,262 524,250 L540,30' fill='#EEF4FA' stroke='#64748B' stroke-width='1.6'/><path d='M366.6,92 L381,248 Q383,258 392,258 L508,258 Q517,258 519,248 L533.4,92 Z' fill='#93C5FD' opacity='.75'/><circle cx='430' cy='170' r='70' fill='#DBEAFE' stroke='#6D28D9' stroke-width='5'/><clipPath id='cLoupe'><circle cx='430' cy='170' r='67'/></clipPath><g clip-path='url(#cLoupe)'><circle cx='386.0' cy='135.6' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='371.1' cy='132.0' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='377.20747578431883' cy='139.57949029334034' r='6.8' fill='#DC2626'/><circle cx='382.9' cy='160.9' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='367.6' cy='160.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='374.9255113353007' cy='166.46399139819766' r='6.8' fill='#DC2626'/><circle cx='392.8' cy='117.5' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='403.7' cy='128.2' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='402.3961535131401' cy='118.61481699737631' r='6.8' fill='#DC2626'/><circle cx='395.3' cy='152.0' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='409.9' cy='147.3' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='400.7859117168561' cy='144.0194657792447' r='6.8' fill='#DC2626'/><circle cx='396.8' cy='176.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='412.0' cy='174.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='403.61682358894' cy='169.17344379720623' r='6.8' fill='#DC2626'/><circle cx='395.5' cy='191.0' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='391.7' cy='205.8' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='399.372661444942' cy='199.86774767238944' r='6.8' fill='#DC2626'/><circle cx='397.4' cy='211.7' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='391.8' cy='225.9' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='400.1540406668595' cy='220.94233790462695' r='6.8' fill='#DC2626'/><circle cx='442.1' cy='112.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='428.9' cy='104.5' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='432.52901087296027' cy='113.4458110393915' r='6.8' fill='#DC2626'/><circle cx='440.2' cy='138.6' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='425.6' cy='134.0' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='431.11130775140947' cy='141.97918034180586' r='6.8' fill='#DC2626'/><circle cx='418.7' cy='160.7' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='422.8' cy='175.4' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='426.5023117997866' cy='166.47680935972986' r='6.8' fill='#DC2626'/><circle cx='429.0' cy='187.0' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='422.9' cy='201.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='431.4431997854543' cy='196.42073844535523' r='6.8' fill='#DC2626'/><circle cx='427.4' cy='214.5' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='422.6' cy='229.0' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='430.6844949080611' cy='223.6254750109662' r='6.8' fill='#DC2626'/><circle cx='453.2' cy='110.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='453.7' cy='125.4' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='459.3550358521799' cy='117.59195546983656' r='6.8' fill='#DC2626'/><circle cx='456.2' cy='152.8' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='467.2' cy='142.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='457.59538968206937' cy='143.2015720304916' r='6.8' fill='#DC2626'/><circle cx='451.9' cy='175.0' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='467.1' cy='173.4' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='458.83556231551376' cy='168.3035021191215' r='6.8' fill='#DC2626'/><circle cx='459.4' cy='204.3' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='460.3' cy='189.1' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='453.94452622603967' cy='196.34498257428183' r='6.8' fill='#DC2626'/><circle cx='445.3' cy='227.8' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='460.2' cy='231.6' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='454.21587627728405' cy='223.91170480380646' r='6.8' fill='#DC2626'/><circle cx='482.1' cy='136.6' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='476.1' cy='150.7' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='484.58420752221906' cy='146.0038224946471' r='6.8' fill='#DC2626'/><circle cx='495.1' cy='169.3' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='481.8' cy='161.8' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='485.5623629301893' cy='170.75495901684016' r='6.8' fill='#DC2626'/><circle cx='478.4' cy='207.8' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='492.8' cy='202.9' r='4.2' fill='#F8FAFC' stroke='#94A3B8' stroke-width='.6'/><circle cx='483.6496426504113' cy='199.71974224410033' r='6.8' fill='#DC2626'/></g><line x1='380' y1='220' x2='348' y2='262' stroke='#6D28D9' stroke-width='12' stroke-linecap='round'/><line x1='470' y1='150' x2='552' y2='112' stroke='#1E293B' stroke-width='1'/><text x='556' y='100' font-size='14' fill='#1E293B' font-family='system-ui, sans-serif'>les entités</text><text x='556' y='117' font-size='14' fill='#1E293B' font-family='system-ui, sans-serif'>chimiques :</text><text x='556' y='134' font-size='14' fill='#1E293B' font-family='system-ui, sans-serif'>molécules H₂O</text><text x='450' y='288' font-size='13' text-anchor='middle' fill='#475569' font-family='system-ui, sans-serif'>échelle microscopique</text></svg>

<div class="nt-grid">
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Échelle microscopique</p>
<p>Échelle de description rassemblant un <span class="imp nt-hole">nombre restreint d'entités</span>, adaptée notamment à l'étude de la structure et des propriétés des entités chimiques.</p>
</div>
<div class="nt-b nt-def" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Échelle macroscopique</p>
<p>Échelle de description rassemblant un <span class="imp nt-hole">nombre</span> suffisamment <span class="imp nt-hole">élevé d'entités</span> pour que des grandeurs comme la pression, la température ou la masse volumique puissent être définies.</p>
</div>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Piège&nbsp;: «&nbsp;microscopique&nbsp;» en SVT et en physique-chimie</p>
<p>En SVT, on appelle microscopique ce qui est <b>invisible à l'œil nu</b> mais visible au microscope optique&nbsp;: une cellule, une bactérie, un globule rouge. Ces objets mesurent quelques <b>micromètres</b>. Un micromètre (1&nbsp;µm) est un millionième de mètre, soit un millième de millimètre&nbsp;: 1&nbsp;µm = 0,001&nbsp;mm.</p>
<p>En physique-chimie, l'échelle microscopique est celle des <b>entités chimiques</b>&nbsp;: atomes, ions et molécules sont <b>plus de mille fois plus petits</b> que les objets microscopiques de la SVT. Un atome mesure environ un dixième de nanomètre, et un nanomètre (1&nbsp;nm) est un milliardième de mètre, soit un millième de micromètre.</p>
<p>Le mot «&nbsp;microscopique&nbsp;» est donc mal adapté en physique-chimie&nbsp;: en toute rigueur, il faudrait parler d'échelle <b>nanoscopique</b>. On garde pourtant «&nbsp;microscopique&nbsp;», consacré par l'usage.</p>
</div>

<p class="nt-lead">Les phénomènes décrits à l'échelle macroscopique sont perceptibles par nos sens, ou mesurables avec des instruments (balance, thermomètre, capteur de pression, pH-mètre…). L'échelle microscopique, elle, échappe à nos sens.</p>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>On peut préciser l'état physique d'une espèce chimique après sa formule&nbsp;: $\ce{H2O(s)}$ désigne la glace, $\ce{H2O(\ell)}$ l'eau liquide et $\ce{H2O(g)}$ la vapeur d'eau.</p>
</div>

<div class="nt-figs" style="grid-template-columns: minmax(240px, 560px); justify-content: center;">
<figure><img src="https://presentationssite.github.io/mgmacromicro.png" alt="À gauche, des pièces de magnésium (échelle macroscopique) ; à droite, une image au microscope électronique où l'on distingue les atomes de magnésium, avec une échelle de 5 nanomètres" loading="lazy" style="margin-top:0em;margin-bottom:0em;"><figcaption>du magnésium à l'échelle macroscopique, et ses atomes vus au microscope électronique (barre d'échelle&nbsp;: 5&nbsp;nanomètres, soit 5 millionièmes de millimètre)</figcaption></figure>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Comment voir des atomes&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Un microscope optique, qui utilise la lumière, ne peut pas distinguer des détails plus petits qu'environ 0,2&nbsp;micromètre&nbsp;: c'est mille fois trop gros pour voir un atome. L'image introductive où une loupe rend visible des entités est donc impossible en réalité.<br>
Pour «&nbsp;voir&nbsp;» les atomes, on utilise un faisceau d'électrons, dans un <b>microscope électronique en transmission</b>. Ces appareils de plusieurs mètres de haut coûtent plusieurs millions d'euros.</p>
<div class="nt-figs" style="grid-template-columns: minmax(240px, 520px); justify-content: center;"><figure><img src="https://presentationssite.github.io/tem.png" alt="Deux microscopes électroniques en transmission dans un laboratoire" loading="lazy" style="margin-top:0em;margin-bottom:0em;"><figcaption>des microscopes électroniques en transmission</figcaption></figure></div>
</div>
</details>

<div class="nt-lab nt-quizlab" id="quiz-echelle">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Microscopique ou macroscopique&nbsp;?</p>
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

## Corps purs et mélanges {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Mélange et corps pur</p>
<p>Un <span class="imp">mélange</span> est un échantillon de matière constitué de <span class="imp nt-hole">plusieurs espèces chimiques</span>, par opposition à un <span class="imp">corps pur</span>, constitué d'<span class="imp nt-hole">une seule espèce chimique</span>.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<p>L'eau du robinet est un mélange d'eau et de différentes espèces dissoutes. L'air est un mélange de plusieurs espèces chimiques, dont le diazote et le dioxygène. L'or à 18 carats est un mélange de deux espèces métalliques, l'or et le cuivre.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Le corps pur est un <b>modèle</b>&nbsp;: aucun échantillon de matière naturel n'est parfaitement pur.</p>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Mélange homogène ou hétérogène</p>
<p>Un mélange est dit <span class="imp">homogène</span> s'il ne présente qu'<span class="imp nt-hole">une seule phase</span>&nbsp;: on n'y voit pas de frontière nette.</p>
<p>Un mélange est dit <span class="imp">hétérogène</span> s'il présente <span class="imp nt-hole">plusieurs phases</span>, séparées par des frontières. L'une des phases peut être dispersée dans l'autre.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<p>Le vinaigre est un mélange homogène, constitué essentiellement d'eau et d'acide éthanoïque. Le lait <b>semble</b> homogène à l'œil nu, mais il est en réalité hétérogène&nbsp;: au microscope, on voit des gouttelettes de matière grasse dispersées dans une solution aqueuse.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>La frontière entre mélange homogène et hétérogène peut dépendre de l'<b>échelle d'observation</b>&nbsp;: le lait, la mayonnaise ou le sang semblent homogènes à l'œil nu, mais pas au microscope.</p>
</div>

<div class="nt-figs">
<figure><img src="https://presentationssite.github.io/laitmicrosc.png" alt="Un verre de lait devant un microscope" loading="lazy" style="margin-top:0em;margin-bottom:0em;"><figcaption>le lait&nbsp;: homogène à l'œil nu, hétérogène au microscope</figcaption></figure>
<figure><img src="https://presentationssite.github.io/vinaigrette.png" alt="Une cuillère de vinaigrette au-dessus d'une salade" loading="lazy" style="margin-top:0em;margin-bottom:0em;"><figcaption>la vinaigrette&nbsp;: un mélange hétérogène qu'il faut agiter</figcaption></figure>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Lait, vinaigrette, mayonnaise&nbsp;: des émulsions</span></summary>
<div class="nt-d-body">
<p>Une <b>émulsion</b> est une dispersion de fines gouttelettes d'un liquide dans un autre avec lequel il ne se mélange pas. Le lait est une émulsion naturelle de matière grasse dans l'eau.</p>
<ul class="nt-facts">
<li><b>La vinaigrette</b> est une émulsion instable&nbsp;: plus on l'agite vigoureusement, plus les gouttelettes d'huile sont fines, et plus elles mettent de temps à remonter. Mais elles finissent toujours par remonter, car l'huile est moins dense que le vinaigre.</li>
<li><b>La mayonnaise</b> est stabilisée par le jaune d'œuf, qui contient des molécules capables de s'accrocher à la fois à l'huile et à l'eau. Une pointe de moutarde stabilise de la même façon une vinaigrette.</li>
<li><b>Le lait «&nbsp;homogénéisé&nbsp;»</b> vendu en France passe sous très haute pression (de l'ordre de la centaine de fois la pression atmosphérique) à travers de fines buses&nbsp;: ses gouttelettes de graisse deviennent environ trois fois plus petites. Il n'est pas réellement homogène pour autant, mais la crème ne remonte plus à la surface.</li>
</ul>
<p><a href="https://www.youtube.com/watch?v=NoMeoMygVy0" target="_blank" rel="noopener"><i class="fa-brands fa-youtube"></i> Voir le lait au microscope</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=vKVaOnBsiPY" target="_blank" rel="noopener"><i class="fa-brands fa-youtube"></i>voir une mayonnaise au microscope</a>.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>L'air est-il un corps pur&nbsp;? S'agit-il d'un mélange homogène ou hétérogène&nbsp;? Quelle est sa composition approximative&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>L'air est un <b>mélange homogène</b> de plusieurs gaz&nbsp;: on n'y voit aucune frontière. En volume, il contient environ 78&nbsp;% de diazote et 21&nbsp;% de dioxygène (on ne demande  que de retenir «&nbsp;80&nbsp;% et 20&nbsp;%&nbsp;» en seconde), et environ 1&nbsp;% d'autres gaz.</p>
<svg class='nt-svg nt-svg-m' viewBox='0 0 600 150' role='img' aria-label="Composition de l'air sec, en volume : 78 % de diazote, 21 % de dioxygène, et environ 1 % d'autres gaz, dont l'argon et le dioxyde de carbone"><rect x='20.0' y='30' width='437.4' height='54' fill='#16A34A'/><text x='238.7' y='55' font-size='15' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif'>78 %</text><text x='238.7' y='74' font-size='12.5' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif'>diazote N₂</text><rect x='457.4' y='30' width='117.0' height='54' fill='#DC2626'/><text x='515.9' y='55' font-size='15' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif'>21 %</text><text x='515.9' y='74' font-size='12.5' text-anchor='middle' fill='#fff' font-family='system-ui, sans-serif'>dioxygène O₂</text><rect x='574.4' y='30' width='5.6' height='54' fill='#64748B'/><line x1='577.0' y1='86' x2='577.0' y2='112' stroke='#64748B'/><text x='577.0' y='128' font-size='12.5' text-anchor='end' fill='#475569' font-family='system-ui, sans-serif'>1 % : argon, dioxyde de carbone (0,04 %)…</text><text x='20' y='20' font-size='13' fill='#475569' font-family='system-ui, sans-serif'>composition de l'air sec, en volume</text></svg>
</div>
</details>

<div class="nt-lab nt-quizlab" id="quiz-melange">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Quiz</p>
<p class="nt-lab-title">Corps pur, mélange homogène ou mélange hétérogène&nbsp;?</p>
<p class="nt-ql-q"></p>
<div class="nt-ql-btns"></div>
<p class="nt-msg" aria-live="polite"></p>
<div class="nt-read" aria-live="polite"><span>score&nbsp;: <b class="out-score">0 / 0</b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="next"><i class="fa-solid fa-forward-step"></i>&nbsp; Question suivante</button></div>
</div>

## Identifier des espèces chimiques {.nt-h2}

<p class="nt-lead">Pour identifier les espèces chimiques présentes dans un échantillon de matière, on dispose de <span class="imp">tests chimiques</span> et de <span class="imp">mesures physiques</span>.</p>

### Les tests chimiques {.nt-h3}

<p class="nt-lead">Un test chimique consiste à ajouter un réactif qui produit un effet visible (changement de couleur, trouble, flamme…) en présence de l'espèce recherchée. Quatre tests sont à connaître&nbsp;:</p>

<div class="nt-tests">
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-droplet"></i>Eau $\ce{H2O}$</p>
<p>On dépose un peu de <b>sulfate de cuivre anhydre</b>, une poudre blanche, au contact de l'échantillon.</p>
<div class="nt-res"><span class="ok">positif</span><span>la poudre devient <b>bleue</b></span><span class="ko">négatif</span><span>elle reste blanche</span></div>
</div>
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-smog"></i>Dioxyde de carbone $\ce{CO2}$</p>
<p>On fait barboter le gaz dans de l'<b>eau de chaux</b>, un liquide limpide et incolore.</p>
<div class="nt-res"><span class="ok">positif</span><span>l'eau de chaux se <b>trouble</b> (elle blanchit)</span><span class="ko">négatif</span><span>elle reste limpide</span></div>
</div>
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-fire-flame-curved"></i>Dioxygène $\ce{O2}$</p>
<p>On approche une <b>bûchette incandescente</b> (qui rougeoie sans flamme) du gaz.</p>
<div class="nt-res"><span class="ok">positif</span><span>la bûchette <b>se rallume</b></span><span class="ko">négatif</span><span>elle s'éteint ou continue de rougeoyer</span></div>
</div>
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-fire"></i>Dihydrogène $\ce{H2}$</p>
<p>On approche la <b>flamme d'une allumette</b> de l'ouverture du tube contenant le gaz.</p>
<div class="nt-res"><span class="ok">positif</span><span>une petite <b>détonation</b> (un «&nbsp;pop&nbsp;» ou «&nbsp;jappement&nbsp;»)</span><span class="ko">négatif</span><span>pas de détonation</span></div>
</div>
</div>

<p class="nt-center"><a href="https://presentationssite.github.io/2nde/testschimiques/#/" target="_blank" rel="noopener"><i class="fa-solid fa-flask"></i>&nbsp; Revoir les tests chimiques en images</a></p>


### Les mesures physiques&nbsp;: deux questions différentes {.nt-h3}

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Face à un échantillon inconnu, une mesure physique peut répondre à <b>deux questions bien différentes</b>&nbsp;:</p>
<ul class="nt-facts">
<li><span class="imp nt-hole">Corps pur ou mélange&nbsp;?</span> Un corps pur change d'état à température <b>constante</b> (un palier sur la courbe), un mélange sur un intervalle de températures (pas de palier). Sur une chromatographie, un mélange donne <b>plusieurs taches</b>.</li>
<li><span class="imp nt-hole">Quelle espèce chimique&nbsp;?</span> On compare une valeur mesurée à des valeurs de référence&nbsp;: la température d'un palier, ou une masse volumique, avec les valeurs des <b>tables</b>&nbsp;; la hauteur d'une tache avec celle d'un <b>témoin</b> pur.</li>
</ul>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Mesure</th><th>Corps pur ou mélange&nbsp;?</th><th>Quelle espèce&nbsp;?</th></tr></thead>
<tbody>
<tr><td>température de changement d'état</td><td>palier (corps pur) ou non (mélange)</td><td>température du palier, comparée aux tables</td></tr>
<tr><td>masse volumique</td><td>ne permet pas de conclure seule</td><td>valeur mesurée, comparée aux tables</td></tr>
<tr><td>chromatographie</td><td>une tache (corps pur) ou plusieurs (mélange)</td><td>tache à la même hauteur qu'un témoin</td></tr>
</tbody>
</table>
</div>

## Température de changement d'état {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>À connaître</p>
<p>Les <span class="imp nt-hole">températures de changement d'état</span>, comme la <span class="imp nt-hole">température de fusion</span> (passage de l'état solide à l'état liquide) et la <span class="imp nt-hole">température d'ébullition</span> (passage de l'état liquide à l'état gazeux), peuvent permettre d'identifier un corps pur, en les comparant aux valeurs des tables.</p>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Espèce chimique</th><th>eau</th><th>cyclohexane</th><th>ammoniac</th><th>aspirine</th><th>fer</th></tr></thead>
<tbody><tr><td>température de fusion</td><td>0&nbsp;°C</td><td>6,5&nbsp;°C</td><td>−78&nbsp;°C</td><td>135&nbsp;°C</td><td>1&nbsp;538&nbsp;°C</td></tr></tbody>
</table>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>La température de changement d'état d'un <span class="imp nt-hole">corps pur</span> est <span class="imp nt-hole">fixe</span>&nbsp;: elle reste constante pendant tout le changement d'état (palier). Celle d'un <span class="imp nt-hole">mélange</span> est <span class="imp nt-hole">étalée</span>&nbsp;: elle varie pendant le changement d'état. La température de fusion d'un mélange est en général <b>plus basse</b> que celle du corps pur principal.</p>
</div>

<div class="nt-lab" id="lab-refroid">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Courbe de refroidissement&nbsp;: palier ou pas&nbsp;?</p>
<div class="nt-ctrl">Substance placée dans un mélange réfrigérant&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="subst" value="eau"><span>eau</span></label>
<label><input type="radio" name="subst" value="cyclo" checked><span>cyclohexane</span></label>
<label><input type="radio" name="subst" value="sale"><span>eau salée</span></label>
</div>
</div>
<canvas style="height:260px;" aria-label="Température de la substance en fonction du temps pendant son refroidissement"></canvas>
<div class="nt-read" aria-live="polite"><span>température&nbsp;: <b class="out-t"></b></span><span>état&nbsp;: <b class="out-s"></b></span></div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-play"></i>&nbsp; Lancer le refroidissement</button></div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention aux températures d'ébullition</p>
<ul class="nt-facts">
<li>Elles dépendent beaucoup plus de la <b>pression</b> que les températures de fusion&nbsp;: l'eau bout à 85&nbsp;°C environ au sommet du mont Blanc, et à plus de 350&nbsp;°C à 2&nbsp;000&nbsp;m de profondeur dans l'océan.</li>
<li>La température d'ébullition d'un mélange n'est pas toujours plus basse que celle du corps pur&nbsp;: un mélange d'eau et d'éthanol bout à plus basse température que l'eau pure, mais l'eau salée bout à plus haute température.</li>
</ul>
</div>

### Le banc Kofler {.nt-h3}

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-flask-vial"></i>Le principe</p>
<p>Le banc Kofler sert à mesurer la température de fusion d'un solide, pour l'identifier et vérifier sa pureté. C'est une plaque chauffante dont la température varie d'une extrémité à l'autre, d'environ 50&nbsp;°C à 250&nbsp;°C&nbsp;: chaque point de la plaque est à une température différente.</p>
<ol class="nt-steps">
<li><p>On dépose une traînée de quelques grains du solide sur la plaque, de la zone chaude vers la zone froide.</p></li>
<li><p>Les grains fondent là où la plaque est plus chaude que leur température de fusion&nbsp;: une limite nette apparaît entre le liquide et la poudre.</p></li>
<li><p>On amène l'index du curseur sur cette limite, et on lit la température de fusion sur l'échelle graduée.</p></li>
<li><p>On nettoie ensuite la plaque en poussant le produit vers la zone froide, avec un coton imbibé d'éthanol.</p></li>
</ol>
<p class="nt-note">Avant une mesure, on vérifie le réglage du banc avec une substance de température de fusion connue.</p>
</div>


<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>La consigne est de ne pas porter de gants quand on utilise le banc Kofler. Pourquoi&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Les gants de laboratoire (en latex ou en nitrile) fondent au contact d'une plaque très chaude, et collent à la peau&nbsp;: la brûlure serait bien plus grave. Près d'une source de chaleur, on travaille donc sans gants, mais avec des lunettes de protection, et en manipulant avec précaution.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice</p>
<p>Un élève synthétise de l'aspirine, dont la température de fusion tabulée est 135&nbsp;°C. Au banc Kofler, son produit commence à fondre vers 124&nbsp;°C et est entièrement liquide vers 130&nbsp;°C. Que peut-il en conclure&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Le produit fond sur un <b>intervalle</b> de températures, et <b>plus bas</b> que l'aspirine pure&nbsp;: ce n'est pas un corps pur. Il s'agit probablement d'aspirine contenant des impuretés, qu'il faudra purifier.</p>
</div>
</details>

## La masse volumique {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">masse volumique</span> d'un échantillon de matière est sa <span class="imp nt-hole">masse par unité de volume</span>&nbsp;: on l'obtient en divisant sa masse par son volume.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Masse volumique</p>
<p class="nt-f-math">$$\rho = \frac{m}{V}$$</p>
<div class="nt-f-units"><span>$\rho$ («&nbsp;rhô&nbsp;») en <b>kg/m³</b></span><span>$m$ en <b>kg</b>, $V$ en <b>m³</b></span><span>on utilise aussi le <b>g/cm³</b>, le <b>g/mL</b>, le <b>kg/L</b>…</span></div>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Conversions à connaître</p>
<p class="nt-center">1&nbsp;g/cm³ = 1&nbsp;g/mL = 1&nbsp;kg/L = 1&nbsp;kg/dm³ = 1&nbsp;t/m³ = <span class="imp nt-hole">1&nbsp;000&nbsp;kg/m³</span></p>
<p>Car 1&nbsp;mL = 1&nbsp;cm³, 1&nbsp;L = 1&nbsp;dm³ = 1&nbsp;000&nbsp;cm³, et 1&nbsp;m³ = 1&nbsp;000&nbsp;L.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-ex" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-droplet"></i>L'eau</p>
<p>1&nbsp;litre d'eau a une masse de 1&nbsp;kilogramme&nbsp;: $\rho_\text{eau}$ = 1&nbsp;kg/L = <b>1&nbsp;000&nbsp;kg/m³</b> = 1&nbsp;g/cm³.</p>
</div>
<div class="nt-b nt-ex" style="margin:0;">
<p class="nt-tag"><i class="fa-solid fa-wind"></i>L'air</p>
<p>1&nbsp;litre d'air a une masse d'environ 1,2&nbsp;gramme&nbsp;: $\rho_\text{air}$ ≈ 1,2&nbsp;g/L = <b>1,2&nbsp;kg/m³</b>, environ 800 fois moins que l'eau.</p>
</div>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-eye"></i>Remarque</p>
<p>Pour l'air, on peut se contenter de retenir que sa masse volumique est d'environ <b>1&nbsp;kg/m³</b>.</p>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-list-check"></i>Méthode&nbsp;: mesurer une masse volumique</p>
<ol class="nt-steps">
<li><p><b>La masse</b>&nbsp;: on <b>tare</b> la balance (on la remet à zéro), puis on y pose l'échantillon. Pour un liquide, on tare avec le récipient vide posé sur la balance, avant de verser le liquide&nbsp;: la balance n'affiche alors que la masse du liquide.</p></li>
<li><p><b>Le volume d'un liquide</b>&nbsp;: on le mesure avec une éprouvette graduée, ou mieux, une fiole jaugée.</p></li>
<li><p><b>Le volume d'un solide</b> de forme compliquée&nbsp;: on le plonge dans une éprouvette graduée contenant de l'eau. Le solide «&nbsp;chasse&nbsp;» un volume d'eau égal au sien&nbsp;: $V_\text{solide} = V_2 - V_1$, différence entre le volume lu après et avant l'immersion. C'est la <b>méthode par déplacement d'eau</b>.</p></li>
<li><p>On calcule $\rho = \dfrac{m}{V}$, et on compare aux valeurs des tables.</p></li>
</ol>
</div>

<div class="nt-lab" id="lab-rho">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Identifier un métal ou un liquide par sa masse volumique</p>
<div class="nt-ctrl">Échantillon&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="rhomode" value="solide" checked><span>un cylindre métallique</span></label>
<label><input type="radio" name="rhomode" value="liquide"><span>un liquide incolore</span></label>
</div>
</div>
<canvas style="height:330px;" aria-label="Une balance et une éprouvette graduée contenant de l'eau, ou une fiole jaugée de 50 mL posée sur la balance"></canvas>
<div class="nt-btns nt-rho-sol">
<button type="button" class="nt-btn" data-act="peser"><i class="fa-solid fa-scale-balanced"></i>&nbsp; Poser le cylindre sur la balance</button>
<button type="button" class="nt-btn" data-act="plonger"><i class="fa-solid fa-arrow-down"></i>&nbsp; Plonger le cylindre dans l'éprouvette</button>
</div>
<div class="nt-btns nt-rho-liq" hidden>
<button type="button" class="nt-btn" data-act="poser"><i class="fa-solid fa-scale-balanced"></i>&nbsp; Poser la fiole vide sur la balance</button>
<button type="button" class="nt-btn" data-act="tarer"><i class="fa-solid fa-0"></i>&nbsp; Tarer</button>
<button type="button" class="nt-btn" data-act="remplir"><i class="fa-solid fa-fill-drip"></i>&nbsp; Remplir jusqu'au trait de jauge</button>
</div>
<div class="nt-rho-in"><label for="rho-in">Masse volumique calculée&nbsp;: $\rho$ =</label><input id="rho-in" type="text" inputmode="decimal"><span>g/cm³</span></div>
<div class="nt-btns nt-rho-sol">
<button type="button" class="nt-btn" data-met="2">aluminium (2,7)</button>
<button type="button" class="nt-btn" data-met="1">zinc (7,3)</button>
<button type="button" class="nt-btn" data-met="0">fer (7,9)</button>
<button type="button" class="nt-btn" data-met="4">cuivre (9,0)</button>
<button type="button" class="nt-btn" data-met="3">plomb (11,4)</button>
</div>
<div class="nt-btns nt-rho-liq" hidden>
<button type="button" class="nt-btn" data-liq="2">hexane (0,66)</button>
<button type="button" class="nt-btn" data-liq="0">éthanol (0,79)</button>
<button type="button" class="nt-btn" data-liq="3">benzène (0,88)</button>
<button type="button" class="nt-btn" data-liq="4">eau (1,00)</button>
<button type="button" class="nt-btn" data-liq="1">dichlorométhane (1,33)</button>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="new"><i class="fa-solid fa-rotate"></i>&nbsp; Nouvel échantillon</button></div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Masses volumiques en g/cm³, à température ambiante (20&nbsp;°C pour les liquides). Le volume d'une fiole jaugée de 50&nbsp;mL est connu avec précision&nbsp;: 50,0&nbsp;mL.</p>
</div>


<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 1</p>
<p>Un bouchon de liège a une masse de 6&nbsp;g et un volume de 25&nbsp;cm³. Calculer sa masse volumique en g/cm³, puis en kg/m³. Pourquoi flotte-t-il sur l'eau&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p>$\rho = \dfrac{m}{V} = \dfrac{6}{25} = 0{,}24$&nbsp;g/cm³, soit 240&nbsp;kg/m³ (1&nbsp;g/cm³ = 1&nbsp;000&nbsp;kg/m³). Sa masse volumique est inférieure à celle de l'eau (1&nbsp;g/cm³)&nbsp;: il flotte.</p>
</div>
</details>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Exercice 2</p>
<p>Une salle de classe mesure 8&nbsp;m de long, 7&nbsp;m de large et 3&nbsp;m de haut. Quelle est la masse de l'air qu'elle contient&nbsp;? On prendra $\rho_\text{air}$ = 1,2&nbsp;kg/m³.</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la résolution</span></summary>
<div class="nt-d-body">
<p>Volume&nbsp;: $V$ = 8 × 7 × 3 = 168&nbsp;m³. De $\rho = \dfrac{m}{V}$, on tire $m = \rho \times V$ = 1,2 × 168 ≈ 200&nbsp;kg.</p>
</div>
</details>

## La chromatographie {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>La <span class="imp">chromatographie</span> est une technique qui permet de <span class="imp nt-hole">séparer</span> et d'<span class="imp nt-hole">identifier</span> les constituants d'un mélange homogène.</p>
<p>On dépose une goutte de chaque échantillon sur une <b>ligne de dépôt</b>, tracée au crayon en bas d'une plaque (ou d'un papier). On place la plaque dans une cuve contenant un solvant, l'<b>éluant</b>, qui monte le long de la plaque en entraînant plus ou moins vite chaque espèce chimique.</p>
</div>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Il faut que ligne dépôt soit au-dessus du niveau de solvant dans la cuve, sinon les taches seront immédiatement noyées et l'expérience à recommencer.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<ul class="nt-facts">
<li>Un échantillon qui donne <span class="imp nt-hole">plusieurs taches</span> est un <b>mélange</b>&nbsp;: chaque tache correspond à au moins une espèce chimique.</li>
<li>Pour identifier les constituants, on dépose aussi des <span class="imp nt-hole">témoins</span> (des espèces pures connues). Si une tache de l'échantillon monte <span class="imp nt-hole">à la même hauteur</span> que celle d'un témoin, elle correspond probablement à la même espèce.</li>
</ul>
</div>

<div class="nt-lab" id="lab-ccm">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Quels colorants contient le M&amp;M's vert&nbsp;?</p>
<canvas style="height:420px;" aria-label="Plaque de chromatographie plongée dans l'éluant, avec quatre dépôts : un M&amp;M's vert et trois témoins, E102, E133 et E131"></canvas>
<div class="nt-btns">
<button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-play"></i>&nbsp; Lancer l'élution</button>
<button type="button" class="nt-btn" data-act="out" disabled><i class="fa-solid fa-hand"></i>&nbsp; Retirer la plaque</button>
<span class="nt-ccm-x" hidden style="align-self:center; font-weight:700; color:#B91C1C;"><i class="fa-solid fa-forward"></i>&nbsp; vitesse × 3</span>
</div>
<div class="nt-btns">
<label class="nt-check"><input type="checkbox" name="ccmc" value="E102"> E102 (jaune)</label>
<label class="nt-check"><input type="checkbox" name="ccmc" value="E133"> E133 (bleu brillant)</label>
<label class="nt-check"><input type="checkbox" name="ccmc" value="E131"> E131 (bleu patenté)</label>
<button type="button" class="nt-btn" data-act="check"><i class="fa-solid fa-check"></i>&nbsp; Vérifier</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
<p class="nt-note">Les hauteurs des taches sont illustratives&nbsp;: elles dépendent de l'éluant et du support utilisés.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Pourquoi faut-il retirer la plaque de la cuve avant que l'éluant n'atteigne son bord supérieur&nbsp;?</p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir la réponse</span></summary>
<div class="nt-d-body">
<p>Une fois l'éluant arrivé en haut, les espèces continuent d'être entraînées et s'accumulent au bord supérieur&nbsp;: toutes les taches finissent au même niveau, et on ne peut plus comparer leurs hauteurs. Il faut aussi marquer le front de l'éluant dès la sortie de la plaque, avant qu'il ne s'évapore.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Pourquoi les espèces se séparent-elles&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Une chromatographie met en jeu deux «&nbsp;phases&nbsp;»&nbsp;: la <b>phase fixe</b> (le papier, ou la fine couche de silice de la plaque) et la <b>phase mobile</b> (l'éluant, qui monte par capillarité, comme l'eau dans un sucre). Chaque espèce chimique est à la fois retenue par la phase fixe et entraînée par l'éluant, avec plus ou moins de force selon sa nature. Une espèce très attirée par la phase fixe monte peu&nbsp;; une espèce très soluble dans l'éluant monte haut.</p>
<p>Pour un même éluant et un même support, chaque espèce monte toujours à la même fraction de la hauteur atteinte par l'éluant. Cette fraction s'appelle le <b>rapport frontal</b>&nbsp;: $R_\text{f} = \dfrac{\text{hauteur de la tache}}{\text{hauteur du front de l'éluant}}$, toujours compris entre 0 et 1.</p>
<p class="nt-note">Une même hauteur n'est pas une preuve absolue&nbsp;: deux espèces différentes peuvent avoir le même rapport frontal avec un éluant donné. En cas de doute, on recommence avec un autre éluant.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les différentes techniques de chromatographie</span></summary>
<div class="nt-d-body">
<ul class="nt-facts">
<li><b>Sur papier</b>&nbsp;: la plus simple, idéale pour les colorants (encres, colorants alimentaires).</li>
<li><b>Sur couche mince</b> (CCM)&nbsp;: une fine couche de silice sur une plaque. Plus rapide et plus précise, elle sert au laboratoire à suivre une synthèse ou à contrôler la pureté d'un produit. Les espèces incolores sont révélées sous lampe UV.</li>
<li><b>Sur colonne</b>&nbsp;: la phase fixe remplit un tube vertical, que l'éluant traverse. Elle permet de séparer de plus grandes quantités, pour purifier un produit.</li>
<li><b>En phase gazeuse</b> et <b>en phase liquide à haute performance</b> (CPG, HPLC)&nbsp;: des appareils automatisés, très sensibles, utilisés pour les contrôles antidopage, les analyses médicales, la police scientifique ou le contrôle de la qualité des aliments.</li>
</ul>
<p><a href="https://www.youtube.com/watch?v=lj5OWzhZSac&amp;t=57" target="_blank" rel="noopener"><i class="fa-brands fa-youtube"></i> Voir une chromatographie en vidéo</a>.</p>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ',').replace('-', '\u2212'); }
  function canvasCtx(cv) {
    var dpr = window.devicePixelRatio || 1, w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function onResize(fn) { var t = null; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 150); }); }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function bilanTxt(r) { return r === 1 ? 'Parfait&nbsp;!' : (r >= 0.75 ? 'Très bien&nbsp;!' : (r >= 0.5 ? 'C\u2019est un bon début&nbsp;: relisez les cas manqués.' : 'Relisez le cours, puis recommencez.')); }
  function txt(c, s, x, y, color, font, align) { c.font = font || '12px system-ui, sans-serif'; c.textAlign = align || 'center'; c.fillStyle = color; c.fillText(s, x, y); }
  /* ================= 1. Quiz génériques : une question, des boutons, une correction, un bilan ================= */
  var QUIZ = {
    'quiz-echelle': { choices: ['échelle microscopique', 'échelle macroscopique'], q: [
      ['une molécule d\u2019eau $\\ce{H2O}$', 0, 'Une molécule est une entité chimique&nbsp;: on la décrit à l\u2019échelle microscopique.'],
      ['l\u2019eau contenue dans une bouteille', 1, 'C\u2019est une très grande collection de molécules&nbsp;: l\u2019espèce chimique eau, à l\u2019échelle macroscopique.'],
      ['la température d\u2019une tasse de thé', 1, 'La température n\u2019a de sens que pour un très grand nombre d\u2019entités&nbsp;: c\u2019est une grandeur macroscopique.'],
      ['un ion sodium $\\ce{Na+}$', 0, 'Un ion est une entité chimique (électriquement chargée).'],
      ['le fer d\u2019un clou', 1, 'Le fer du clou est l\u2019espèce chimique fer&nbsp;: une multitude d\u2019atomes de fer.'],
      ['un atome de cuivre', 0, 'Un atome isolé est une entité chimique.'],
      ['la masse volumique de l\u2019huile', 1, 'La masse volumique se mesure sur un échantillon&nbsp;: c\u2019est une grandeur macroscopique.'],
      ['la pression de l\u2019air dans un pneu', 1, 'La pression résulte des chocs d\u2019un nombre gigantesque de molécules&nbsp;: elle n\u2019est définie qu\u2019à l\u2019échelle macroscopique.']
    ] },
    'quiz-melange': { choices: ['corps pur', 'mélange homogène', 'mélange hétérogène'], q: [
      ['l\u2019eau du robinet', 1, 'Elle contient de l\u2019eau et des espèces dissoutes (sels minéraux, gaz…), sans frontière visible&nbsp;: mélange homogène.'],
      ['l\u2019air que l\u2019on respire', 1, 'Plusieurs gaz (diazote, dioxygène, argon…) en une seule phase&nbsp;: mélange homogène.'],
      ['une vinaigrette au repos', 2, 'L\u2019huile et le vinaigre forment deux phases bien distinctes&nbsp;: mélange hétérogène.'],
      ['l\u2019eau distillée', 0, 'Elle ne contient (presque) que de l\u2019eau&nbsp;: c\u2019est un corps pur… au modèle près, puisqu\u2019aucun échantillon réel n\u2019est parfaitement pur.'],
      ['du jus d\u2019orange avec pulpe', 2, 'On voit les morceaux de pulpe dans le liquide&nbsp;: plusieurs phases, mélange hétérogène.'],
      ['un bijou en or 18 carats', 1, 'C\u2019est un alliage d\u2019or et de cuivre (et parfois d\u2019argent), parfaitement mélangés&nbsp;: mélange homogène.'],
      ['du sirop de menthe dilué dans l\u2019eau', 1, 'Une seule phase, colorée uniformément&nbsp;: mélange homogène.'],
      ['un diamant', 0, 'Il n\u2019est constitué que de carbone&nbsp;: corps pur.'],
      ['du sable dans de l\u2019eau', 2, 'Les grains de sable restent visibles et tombent au fond&nbsp;: mélange hétérogène.']
    ] },
    'quiz-tests': { choices: ['sulfate de cuivre anhydre', 'eau de chaux', 'bûchette incandescente', 'flamme d\u2019une allumette'], q: [
      ['On veut savoir si un gaz recueilli dans un tube est du dioxyde de carbone.', 1, 'Le dioxyde de carbone trouble l\u2019eau de chaux.'],
      ['On veut savoir si un liquide incolore contient de l\u2019eau.', 0, 'L\u2019eau fait passer le sulfate de cuivre anhydre du blanc au bleu.'],
      ['On veut savoir si un gaz est du dihydrogène.', 3, 'Le dihydrogène produit une petite détonation au contact d\u2019une flamme.'],
      ['On veut savoir si un gaz est du dioxygène.', 2, 'Le dioxygène ravive une bûchette incandescente, qui se rallume.'],
      ['On souffle à l\u2019aide d\u2019une paille dans un liquide, pour vérifier que l\u2019air expiré contient du dioxyde de carbone.', 1, 'L\u2019eau de chaux se trouble&nbsp;: l\u2019air expiré contient bien du dioxyde de carbone.'],
      ['Un zeste d\u2019orange semble sec&nbsp;: contient-il quand même de l\u2019eau&nbsp;?', 0, 'On le frotte sur un peu de sulfate de cuivre anhydre&nbsp;: s\u2019il bleuit, il contient de l\u2019eau.']
    ] }
  };
  $$(document, '.nt-quizlab').forEach(function (root) {
    var D = QUIZ[root.id]; if (!D) { return; }
    var qEl = $(root, '.nt-ql-q'), bx = $(root, '.nt-ql-btns'), msg = $(root, '.nt-msg'), sc = $(root, '.out-score'), next = $(root, '[data-act="next"]'), lbl = next.innerHTML;
    var order = [], k = 0, good = 0, answered = false, fini = false;
    D.choices.forEach(function (c, i) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'nt-btn'; b.textContent = c;
      b.addEventListener('click', function () {
        if (answered || fini) { return; }
        answered = true; var q = D.q[order[k]];
        if (i === q[1]) { good++; b.classList.add('nt-btn-main'); msg.innerHTML = '<span style="color:#16A34A;">Bravo&nbsp;!</span> ' + q[2]; }
        else { b.style.borderColor = '#E11D48'; b.style.color = '#E11D48'; msg.innerHTML = '<span style="color:#E11D48;">Non</span>&nbsp;: la bonne réponse est «&nbsp;' + D.choices[q[1]] + '&nbsp;». ' + q[2]; }
        sc.textContent = good + ' / ' + (k + 1);
        if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([msg]); }
      });
      bx.appendChild(b);
    });
    function show() {
      answered = false; var q = D.q[order[k]];
      qEl.innerHTML = q[0]; msg.textContent = '';
      $$(bx, 'button').forEach(function (b) { b.classList.remove('nt-btn-main'); b.style.borderColor = ''; b.style.color = ''; });
      next.innerHTML = k === order.length - 1 ? '<i class="fa-solid fa-flag-checkered"></i>&nbsp; Voir le bilan' : lbl;
      if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([qEl]); }
    }
    function start() { order = shuffle(D.q.map(function (_, i) { return i; })); k = 0; good = 0; fini = false; bx.hidden = false; sc.textContent = '0 / 0'; show(); }
    next.addEventListener('click', function () {
      if (fini) { start(); return; }
      if (!answered) { msg.textContent = 'Choisissez d\u2019abord une réponse.'; return; }
      k++;
      if (k >= order.length) {
        fini = true; bx.hidden = true; qEl.innerHTML = '<span class="nt-big-score">' + good + ' / ' + order.length + '</span> ' + bilanTxt(good / order.length);
        msg.textContent = ''; next.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; return;
      }
      show();
    });
    start();
  });
  /* ================= 2. Courbe de refroidissement : palier ou pas ? ================= */
  (function () {
    var root = document.getElementById('lab-refroid');
    if (!root) { return; }
    var cv = $(root, 'canvas'), btn = $(root, '[data-act="play"]'), oT = $(root, '.out-t'), oS = $(root, '.out-s'), msg = $(root, '.nt-msg'), S;
    var SUB = { eau: { n: 'eau', Tf: 0, pur: true }, cyclo: { n: 'cyclohexane', Tf: 6.5, pur: true }, sale: { n: 'eau salée', Tf: -2, pur: false } };
    var sub = 'cyclo', pts = [], t = 0, T = 18, sol = 0, playing = false, last = null, TB = -20, K = 0.17, PAL = 4.5;
    function reset() { t = 0; T = 18; sol = 0; pts = [[0, 18]]; playing = false; btn.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Lancer le refroidissement'; draw(); }
    function step(dt) {
      var s = SUB[sub];
      if (s.pur) {
        if (T > s.Tf + 1e-9 || sol >= 1) { T += -K * (T - TB) * dt; if (sol < 1 && T < s.Tf) { T = s.Tf; } }
        else { sol = Math.min(1, sol + dt / PAL); }   /* palier : la température reste constante tant qu'il reste du liquide */
      } else {
        /* mélange : la solidification s'étale sur un intervalle de températures, sans palier */
        var g = (T < s.Tf && T > s.Tf - 9) ? 3.2 * Math.exp(-Math.pow((T - (s.Tf - 2)) / 3.2, 2)) : 0;
        T += -K * (T - TB) * dt / (1 + g);
        sol = T < s.Tf ? Math.min(1, (s.Tf - T) / 9) : 0;
      }
      t += dt; pts.push([t, T]);
    }
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, L = 44, R = w - 14, Tp = 14, B = h - 34;
      function X(v) { return L + v / 15 * (R - L); }
      function Y(v) { return B - (v + 10) / 30 * (B - Tp); }
      c.clearRect(0, 0, w, h);
      c.strokeStyle = '#E2E8F0'; c.lineWidth = 1;
      for (var y = -10; y <= 20; y += 5) { c.beginPath(); c.moveTo(L, Y(y)); c.lineTo(R, Y(y)); c.stroke(); txt(c, String(y).replace('-', '\u2212'), L - 6, Y(y) + 4, '#475569', '11px system-ui, sans-serif', 'right'); }
      for (var x = 0; x <= 15; x += 3) { txt(c, String(x), X(x), B + 15, '#475569', '11px system-ui, sans-serif'); }
      txt(c, 'temps (min)', (L + R) / 2, h - 4, '#475569', '11px system-ui, sans-serif');
      c.save(); c.translate(12, (Tp + B) / 2); c.rotate(-Math.PI / 2); txt(c, 'température (°C)', 0, 0, '#475569', '11px system-ui, sans-serif'); c.restore();
      c.strokeStyle = '#1E293B'; c.beginPath(); c.moveTo(L, Tp); c.lineTo(L, B); c.lineTo(R, B); c.stroke();
      c.strokeStyle = SUB[sub].pur ? '#2563EB' : '#16A34A'; c.lineWidth = 2.4; c.beginPath();
      pts.forEach(function (p, i) { if (i === 0) { c.moveTo(X(p[0]), Y(p[1])); } else { c.lineTo(X(p[0]), Y(p[1])); } }); c.stroke();
      oT.textContent = fr(T, 1) + ' °C';
      oS.textContent = sol <= 0 ? 'liquide' : (sol >= 1 ? 'solide' : 'liquide et solide');
    }
    function loop(ts) {
      if (!playing) { return; }
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      for (var i = 0; i < 6; i++) { step(dt * (RM ? 2 : 1) / 6 * 1.5); }
      draw();
      if (t >= 15) {
        playing = false; btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer';
        var s = SUB[sub];
        msg.innerHTML = s.pur ? 'Corps pur&nbsp;: la courbe présente un <b>palier</b>. Pendant toute la solidification, la température reste constante, à ' + fr(s.Tf, 1) + '&nbsp;°C&nbsp;: c\u2019est la température de changement d\u2019état de l\u2019' + (sub === 'eau' ? 'eau' : 'espèce (ici le cyclohexane)') + '.'
          : 'Mélange&nbsp;: <b>pas de palier</b>. La solidification commence vers ' + fr(s.Tf, 0) + '&nbsp;°C, puis la température continue de baisser pendant qu\u2019elle se poursuit&nbsp;: le changement d\u2019état s\u2019étale sur un intervalle de températures.';
        return;
      }
      requestAnimationFrame(loop);
    }
    btn.addEventListener('click', function () {
      if (t >= 15) { reset(); msg.textContent = ''; return; }
      playing = !playing; last = null;
      btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Reprendre';
      if (playing) { requestAnimationFrame(loop); }
    });
    $$(root, 'input[name="subst"]').forEach(function (r) { r.addEventListener('change', function () { sub = r.value; msg.textContent = ''; reset(); }); });
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); reset(); onResize(setup);
  })();
  /* ================= 3. Le banc Kofler ================= */
  (function () {
    var root = document.getElementById('lab-kofler');
    if (!root) { return; }
    var cv = $(root, 'canvas'), rX = $(root, 'input[type="range"]'), oT = $(root, '.out-t'), msg = $(root, '.nt-msg'), S;
    var ESP = [['acide benzoïque', 122], ['acide citrique', 153], ['acide ascorbique', 192]];
    var cur = null, grains = [], TMIN = 50, TMAX = 250;
    function nouvelle() {
      var k = Math.floor(Math.random() * 3), impur = Math.random() < 0.25;
      cur = { k: k, Tf: ESP[k][1] - (impur ? 9 : 0), impur: impur };
      grains = []; for (var i = 0; i < 70; i++) { grains.push({ u: 0.18 + 0.7 * Math.random(), v: Math.random(), r: 1.6 + Math.random() * 1.8 }); }
      msg.textContent = 'Déplacez l\u2019index jusqu\u2019à la limite entre la poudre et le liquide, puis identifiez l\u2019espèce.';
      $$(root, '[data-esp]').forEach(function (b) { b.classList.remove('nt-btn-main'); b.style.borderColor = ''; b.style.color = ''; });
      draw();
    }
    function Tx(u) { return TMAX - u * (TMAX - TMIN); }   /* plaque chaude à gauche (250 °C), froide à droite (50 °C) */
    function draw() {
      var c = S.ctx, w = S.w, h = S.h, L = 20, R = w - 20, y0 = 40, y1 = 110;
      function X(u) { return L + u * (R - L); }
      c.clearRect(0, 0, w, h);
      var gr = c.createLinearGradient(L, 0, R, 0); gr.addColorStop(0, '#FCA5A5'); gr.addColorStop(0.5, '#FDE68A'); gr.addColorStop(1, '#E2E8F0');
      c.fillStyle = gr; c.fillRect(L, y0, R - L, y1 - y0); c.strokeStyle = '#64748B'; c.strokeRect(L, y0, R - L, y1 - y0);
      txt(c, 'plaque chauffante : de 250 °C (à gauche) à 50 °C (à droite)', (L + R) / 2, y0 - 10, '#475569', '12px system-ui, sans-serif');
      /* grains : poudre blanche s'ils sont plus froids que la température de fusion, gouttes transparentes sinon */
      grains.forEach(function (g) {
        var T = Tx(g.u), x = X(g.u), y = y0 + 18 + g.v * (y1 - y0 - 36);
        var fondu = cur.impur ? T > cur.Tf - 6 * (1 - g.v) : T >= cur.Tf;   /* impur : fusion étalée et plus basse */
        if (fondu) { c.fillStyle = 'rgba(96,165,250,.35)'; c.strokeStyle = 'rgba(30,64,175,.55)'; c.lineWidth = 0.8; c.beginPath(); c.ellipse(x, y, g.r * 2.2, g.r * 1.4, 0, 0, 2 * Math.PI); c.fill(); c.stroke(); c.fillStyle = 'rgba(255,255,255,.9)'; c.beginPath(); c.arc(x - g.r * 0.7, y - g.r * 0.5, g.r * 0.45, 0, 2 * Math.PI); c.fill(); }
        else { c.fillStyle = '#FFFFFF'; c.strokeStyle = '#94A3B8'; c.lineWidth = 0.6; c.beginPath(); c.rect(x - g.r, y - g.r * 0.8, g.r * 2, g.r * 1.6); c.fill(); c.stroke(); }
      });
      /* échelle graduée */
      var ys = y1 + 30;
      c.fillStyle = '#F8FAFC'; c.fillRect(L, y1 + 8, R - L, 34); c.strokeStyle = '#94A3B8'; c.strokeRect(L, y1 + 8, R - L, 34);
      for (var T = 50; T <= 250; T += 10) { var xx = X((TMAX - T) / (TMAX - TMIN)); c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(xx, y1 + 8); c.lineTo(xx, y1 + (T % 50 === 0 ? 20 : 15)); c.stroke(); if (T % 50 === 0) { txt(c, String(T), xx, ys + 8, '#334155', '11px system-ui, sans-serif'); } }
      /* index du curseur */
      var u = +rX.value, xi = X(u), Ti = Tx(u);
      c.strokeStyle = '#1D4ED8'; c.lineWidth = 2; c.beginPath(); c.moveTo(xi, y0 - 2); c.lineTo(xi, y1 + 40); c.stroke();
      c.fillStyle = '#1D4ED8'; c.beginPath(); c.moveTo(xi, y0 - 2); c.lineTo(xi - 6, y0 - 12); c.lineTo(xi + 6, y0 - 12); c.fill();
      oT.textContent = Math.round(Ti) + ' °C';
    }
    rX.addEventListener('input', draw);
    $$(root, '[data-esp]').forEach(function (b) {
      b.addEventListener('click', function () {
        var k = +b.getAttribute('data-esp');
        $$(root, '[data-esp]').forEach(function (x) { x.classList.remove('nt-btn-main'); x.style.borderColor = ''; x.style.color = ''; });
        if (cur.impur) {
          b.style.borderColor = '#E11D48'; b.style.color = '#E11D48';
          msg.innerHTML = 'Attention&nbsp;: cette poudre n\u2019est pas pure. Elle fond progressivement, sur un intervalle, et plus bas que l\u2019' + ESP[cur.k][0] + ' pur (' + ESP[cur.k][1] + '&nbsp;°C)&nbsp;: c\u2019est probablement de l\u2019' + ESP[cur.k][0] + ' contenant des impuretés.';
        } else if (k === cur.k) { b.classList.add('nt-btn-main'); msg.innerHTML = '<span style="color:#16A34A;">Bravo&nbsp;!</span> La poudre fond nettement à ' + ESP[k][1] + '&nbsp;°C&nbsp;: c\u2019est l\u2019' + ESP[k][0] + '.'; }
        else { b.style.borderColor = '#E11D48'; b.style.color = '#E11D48'; msg.innerHTML = '<span style="color:#E11D48;">Non.</span> Placez l\u2019index exactement à la limite entre la poudre et le liquide, puis comparez la température lue aux valeurs du tableau.'; }
      });
    });
    $(root, '[data-act="new"]').addEventListener('click', nouvelle);
    function setup() { S = canvasCtx(cv); if (cur) { draw(); } }
    setup(); nouvelle(); onResize(setup);
  })();
  /* ================= 4. Mesurer une masse volumique : un solide, puis un liquide ================= */
  (function () {
    var root = document.getElementById('lab-rho');
    if (!root) { return; }
    var cv = $(root, 'canvas'), msg = $(root, '.nt-msg'), inp = $(root, 'input[type="text"]'), S;
    var MET = [['fer', 7.9, 'le '], ['zinc', 7.3, 'le '], ['aluminium', 2.7, "l'"], ['plomb', 11.4, 'le '], ['cuivre', 9.0, 'le ']];
    var LIQ = [['éthanol', 0.79, "l'"], ['dichlorométhane', 1.33, 'le '], ['hexane', 0.66, "l'"], ['benzène', 0.88, 'le '], ['eau', 1.00, "l'"]];
    var mode = 'solide', cur, etape = 0, MF = 38.6;   /* MF : masse de la fiole vide (g) */
    function tex() { if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([msg]); } }
    function nouveau() {
      if (mode === 'solide') {
        var k = Math.floor(Math.random() * 5), V = 20 + Math.floor(Math.random() * 16), V1 = 40 + 2 * Math.floor(Math.random() * 8);
        cur = { k: k, V: V, V1: V1, m: Math.round(MET[k][1] * V * 10) / 10 };
        msg.textContent = 'Étape 1 : la balance est tarée (elle affiche 0,0 g). Posez le cylindre dessus.';
      } else {
        var q = Math.floor(Math.random() * 5);
        cur = { k: q, m: Math.round(LIQ[q][1] * 50 * 10) / 10 };
        msg.textContent = 'Étape 1 : posez la fiole jaugée de 50,0 mL, vide et sèche, sur la balance.';
      }
      etape = 0; inp.value = '';
      $$(root, '[data-met], [data-liq]').forEach(function (b) { b.classList.remove('nt-btn-main'); b.style.borderColor = ''; b.style.color = ''; });
      maj(); draw();
    }
    function maj() {
      $$(root, '.nt-rho-sol').forEach(function (e) { e.hidden = mode !== 'solide'; });
      $$(root, '.nt-rho-liq').forEach(function (e) { e.hidden = mode !== 'liquide'; });
      $(root, '[data-act="peser"]').disabled = etape !== 0; $(root, '[data-act="plonger"]').disabled = etape !== 1;
      $(root, '[data-act="poser"]').disabled = etape !== 0; $(root, '[data-act="tarer"]').disabled = etape !== 1; $(root, '[data-act="remplir"]').disabled = etape !== 2;
    }
    function rrect(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
    function balance(c, cx, by, aff) {
      var bw = 190;
      c.fillStyle = '#E2E8F0'; c.strokeStyle = '#64748B'; c.lineWidth = 1.2; rrect(c, cx - bw / 2, by, bw, 54, 10); c.fill(); c.stroke();
      c.fillStyle = '#94A3B8'; rrect(c, cx - 62, by - 7, 124, 7, 2); c.fill();
      c.fillStyle = '#0F172A'; rrect(c, cx - 52, by + 13, 104, 28, 4); c.fill();
      txt(c, aff + ' g', cx, by + 33, '#4ADE80', '16px ui-monospace, Menlo, monospace');
      txt(c, 'balance', cx, by + 76, '#475569', '12px system-ui, sans-serif');
    }
    function cylindre(c, x, yb, hh) {
      var g = c.createLinearGradient(x - 14, 0, x + 14, 0); g.addColorStop(0, '#78716C'); g.addColorStop(0.5, '#E7E5E4'); g.addColorStop(1, '#78716C');
      c.fillStyle = g; c.fillRect(x - 14, yb - hh, 28, hh); c.strokeStyle = '#44403C'; c.lineWidth = 1; c.strokeRect(x - 14, yb - hh, 28, hh);
      c.fillStyle = '#D6D3D1'; c.beginPath(); c.ellipse(x, yb - hh, 14, 3.5, 0, 0, 2 * Math.PI); c.fill(); c.stroke();
    }
    function verre(c, x0, x1) { var g = c.createLinearGradient(x0, 0, x1, 0); g.addColorStop(0, 'rgba(203,213,225,.55)'); g.addColorStop(0.45, 'rgba(255,255,255,.35)'); g.addColorStop(1, 'rgba(203,213,225,.55)'); return g; }
    function eprouvette(c, ex, et, eb, V, plonge) {
      var ew = 44, x0 = ex - ew / 2, x1 = ex + ew / 2, sc = (eb - 30 - et) / 100;
      function Ye(v) { return eb - 4 - v * sc; }
      c.fillStyle = verre(c, x0, x1); c.fillRect(x0, et, ew, eb - et);
      if (plonge) { cylindre(c, ex, eb - 2, Math.min(30 + cur.V * 1.4, eb - Ye(V) - 6)); }
      /* eau, par transparence devant le cylindre, avec un ménisque */
      var yl = Ye(V);
      c.fillStyle = 'rgba(147,197,253,.5)'; c.beginPath(); c.moveTo(x0 + 1, yl - 3); c.quadraticCurveTo(ex, yl + 4, x1 - 1, yl - 3); c.lineTo(x1 - 1, eb); c.lineTo(x0 + 1, eb); c.closePath(); c.fill();
      /* graduations, sans chiffres : la loupe permet la lecture */
      for (var v = 2; v <= 100; v += 2) { var y = Ye(v); c.strokeStyle = 'rgba(51,65,85,.75)'; c.lineWidth = 0.7; c.beginPath(); c.moveTo(x0 + 2, y); c.lineTo(x0 + 2 + (v % 10 === 0 ? 13 : 7), y); c.stroke(); }
      /* parois : ouverture libre en haut, petit bec verseur à gauche */
      c.strokeStyle = '#64748B'; c.lineWidth = 1.5; c.lineJoin = 'round';
      c.beginPath(); c.moveTo(x0 - 7, et - 6); c.quadraticCurveTo(x0 - 1, et - 2, x0, et + 8); c.lineTo(x0, eb); c.lineTo(x1, eb); c.lineTo(x1, et); c.stroke();
      c.fillStyle = '#CBD5E1'; rrect(c, x0 - 20, eb, ew + 40, 6, 3); c.fill(); c.strokeStyle = '#64748B'; c.lineWidth = 1; c.stroke();
      txt(c, 'éprouvette graduée (100 mL)', ex, eb + 24, '#475569', '12px system-ui, sans-serif');
    }
    function fiole(c, cx, yb, plein) {
      /* fiole jaugée de 50 mL : panse en poire, col étroit avec trait de jauge, bouchon posé à côté */
      var s = 1.0;
      function P(x, y) { return [cx + x * s, yb + y * s]; }
      c.save(); c.translate(cx, yb);
      var path = function () { c.beginPath(); c.moveTo(-7, -150); c.lineTo(-7, -84); c.quadraticCurveTo(-30, -66, -38, -40); c.quadraticCurveTo(-44, -2, -18, 0); c.lineTo(18, 0); c.quadraticCurveTo(44, -2, 38, -40); c.quadraticCurveTo(30, -66, 7, -84); c.lineTo(7, -150); };
      path(); c.fillStyle = verre(c, -40, 40); c.fill();
      if (plein) {
        c.save(); path(); c.clip(); c.fillStyle = 'rgba(125,211,252,.55)'; c.fillRect(-45, -122, 90, 122);
        c.strokeStyle = 'rgba(56,189,248,.8)'; c.beginPath(); c.moveTo(-6, -122); c.quadraticCurveTo(0, -119, 6, -122); c.stroke(); c.restore();
      }
      path(); c.strokeStyle = '#64748B'; c.lineWidth = 1.4; c.lineJoin = 'round'; c.stroke();
      c.strokeStyle = '#1E293B'; c.lineWidth = 1.2; c.beginPath(); c.moveTo(-7, -122); c.lineTo(7, -122); c.stroke();
      txt(c, '50 mL', 0, -30, '#64748B', '10px system-ui, sans-serif');
      c.restore();
    }
    function loupe(c, lx, ly, lr, V) {
      c.save(); c.beginPath(); c.arc(lx, ly, lr, 0, 2 * Math.PI); c.clip();
      c.fillStyle = '#F8FAFC'; c.fillRect(lx - lr, ly - lr, 2 * lr, 2 * lr);
      var z = 12; function Yz(vv) { return ly - (vv - V) * z; }
      c.fillStyle = 'rgba(147,197,253,.7)'; c.beginPath(); c.moveTo(lx - lr, Yz(V) - 2); c.quadraticCurveTo(lx, Yz(V) + 9, lx + lr, Yz(V) - 2); c.lineTo(lx + lr, ly + lr); c.lineTo(lx - lr, ly + lr); c.fill();
      for (var q = Math.floor(V) - 6; q <= V + 6; q++) { var yy = Yz(q); c.strokeStyle = '#334155'; c.lineWidth = 1; c.beginPath(); c.moveTo(lx - lr, yy); c.lineTo(lx - lr + (q % 10 === 0 ? 40 : (q % 2 === 0 ? 28 : 16)), yy); c.stroke(); if (q % 2 === 0) { txt(c, String(q), lx - lr + 48, yy + 4, '#334155', '11px system-ui, sans-serif', 'left'); } }
      c.restore(); c.strokeStyle = '#6D28D9'; c.lineWidth = 4; c.beginPath(); c.arc(lx, ly, lr, 0, 2 * Math.PI); c.stroke();
      txt(c, 'loupe sur le ménisque', lx, ly + lr + 20, '#6D28D9', '12px system-ui, sans-serif');
    }
    function draw() {
      if (!S || !cur) { return; }
      var c = S.ctx, w = S.w, h = S.h, by = h - 98;
      c.clearRect(0, 0, w, h);
      if (mode === 'solide') {
        var bx = w * 0.22;
        balance(c, bx, by, etape === 1 ? fr(cur.m, 1) : '0,0');
        if (etape === 1) { cylindre(c, bx, by - 7, 30 + cur.V * 1.4); }
        eprouvette(c, w * 0.52, 26, h - 52, etape === 2 ? cur.V1 + cur.V : cur.V1, etape === 2);
        loupe(c, w * 0.8, h * 0.42, Math.min(72, w * 0.13), etape === 2 ? cur.V1 + cur.V : cur.V1);
      } else {
        var fx = w * 0.42, aff = etape === 0 ? '0,0' : (etape === 1 ? fr(MF, 1) : (etape === 2 ? '0,0' : fr(cur.m, 1)));
        balance(c, fx, by, aff);
        if (etape >= 1) { fiole(c, fx, by - 7, etape === 3); }
        if (etape === 0) { fiole(c, w * 0.78, by + 54, false); txt(c, 'fiole jaugée vide', w * 0.78, by + 76, '#475569', '12px system-ui, sans-serif'); }
        if (etape === 3) { txt(c, 'remplie jusqu\u2019au trait de jauge', fx + 70, by - 125, '#0369A1', '12px system-ui, sans-serif', 'left'); c.strokeStyle = '#0369A1'; c.beginPath(); c.moveTo(fx + 66, by - 129); c.lineTo(fx + 12, by - 129); c.stroke(); }
      }
    }
    $(root, '[data-act="peser"]').addEventListener('click', function () { etape = 1; msg.textContent = 'Étape 2 : notez la masse affichée. L\u2019éprouvette contient de l\u2019eau : lisez son volume V\u2081 dans la loupe (bas du ménisque), puis plongez le cylindre.'; maj(); draw(); });
    $(root, '[data-act="plonger"]').addEventListener('click', function () { etape = 2; msg.textContent = 'Étape 3 : lisez le nouveau volume V\u2082. Le volume du cylindre est V = V\u2082 \u2212 V\u2081. Calculez sa masse volumique, puis identifiez le métal.'; maj(); draw(); });
    $(root, '[data-act="poser"]').addEventListener('click', function () { etape = 1; msg.textContent = 'Étape 2 : la balance affiche la masse de la fiole vide. Tarez la balance pour qu\u2019elle n\u2019affiche ensuite que la masse du liquide.'; maj(); draw(); });
    $(root, '[data-act="tarer"]').addEventListener('click', function () { etape = 2; msg.textContent = 'Étape 3 : la balance affiche 0,0 g avec la fiole posée dessus. Remplissez la fiole jusqu\u2019au trait de jauge.'; maj(); draw(); });
    $(root, '[data-act="remplir"]').addEventListener('click', function () { etape = 3; msg.textContent = 'Étape 4 : la balance affiche la masse des 50,0 mL de liquide. Calculez sa masse volumique, puis identifiez le liquide.'; maj(); draw(); });
    function corrige(b, liste, attr, calc) {
      var k = +b.getAttribute(attr);
      $$(root, '[' + attr + ']').forEach(function (x) { x.classList.remove('nt-btn-main'); x.style.borderColor = ''; x.style.color = ''; });
      var rho = parseFloat(inp.value.replace(',', '.')), vrai = calc[0], okR = !isNaN(rho) && Math.abs(rho - vrai) / vrai < 0.04;
      var nom = liste[k][2] + liste[k][0], bon = liste[cur.k][2] + liste[cur.k][0], dens = function (x) { return fr(x, 2).replace(/0$/, ''); };
      if (k === cur.k) { b.classList.add('nt-btn-main'); msg.innerHTML = '<span style="color:#16A34A;">Bravo&nbsp;!</span> C\u2019est bien ' + nom + ' (' + dens(liste[k][1]) + '&nbsp;g/cm³). ' + (okR ? '' : 'Vérifiez tout de même votre calcul. ') + calc[1]; }
      else { b.style.borderColor = '#E11D48'; b.style.color = '#E11D48'; msg.innerHTML = '<span style="color:#E11D48;">Non.</span> ' + calc[1] + ' C\u2019est en fait ' + bon + ' (' + dens(liste[cur.k][1]) + '&nbsp;g/cm³).'; }
      tex();
    }
    $$(root, '[data-met]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (etape < 2) { msg.textContent = 'Faites d\u2019abord les deux mesures.'; return; }
        var vrai = cur.m / cur.V;
        corrige(b, MET, 'data-met', [vrai, 'Calcul&nbsp;: $V = ' + (cur.V1 + cur.V) + ' - ' + cur.V1 + ' = ' + cur.V + '$&nbsp;mL, soit ' + cur.V + '&nbsp;cm³, et $\\rho = \\dfrac{m}{V} = \\dfrac{' + fr(cur.m, 1).replace(',', '{,}') + '}{' + cur.V + '} \\approx ' + fr(vrai, 1).replace(',', '{,}') + '$&nbsp;g/cm³.']);
      });
    });
    $$(root, '[data-liq]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (etape < 3) { msg.textContent = 'Faites d\u2019abord la mesure.'; return; }
        var vrai = cur.m / 50;
        corrige(b, LIQ, 'data-liq', [vrai, 'Calcul&nbsp;: $\\rho = \\dfrac{m}{V} = \\dfrac{' + fr(cur.m, 1).replace(',', '{,}') + '}{50{,}0} \\approx ' + fr(vrai, 2).replace(',', '{,}') + '$&nbsp;g/mL, soit ' + fr(vrai, 2) + '&nbsp;g/cm³.']);
      });
    });
    $$(root, 'input[name="rhomode"]').forEach(function (r) { r.addEventListener('change', function () { mode = r.value; nouveau(); }); });
    $(root, '[data-act="new"]').addEventListener('click', nouveau);
    function setup() { S = canvasCtx(cv); draw(); }
    setup(); nouveau(); onResize(setup);
  })();

  /* ================= 5. Une chromatographie ================= */
  (function () {
    var root = document.getElementById('lab-ccm');
    if (!root) { return; }
    var cv = $(root, 'canvas'), btn = $(root, '[data-act="play"]'), btnOut = $(root, '[data-act="out"]'), msg = $(root, '.nt-msg'), S;
    /* rapport frontal (valeurs illustratives) et couleur de chaque colorant : E133 et E131 ont le même bleu, seule leur hauteur les distingue */
    var COL = { E102: [0.36, '#FACC15'], E133: [0.66, '#1E88E5'], E131: [0.84, '#1E88E5'] };
    var DEP = [['M&M\u2019s vert', ['E102', 'E133']], ['E102', ['E102']], ['E133', ['E133']], ['E131', ['E131']]];
    var f = null, run = false, sorti = false, trop = false, last = null, ext = 0;   /* f : ordonnée (px) du front ; ext : parcours supplémentaire des taches après « trop tard » */
    function geom() {
      var w = S.w, h = S.h, pw = Math.min(170, w * 0.42), pt = 44, pb = h - 30;
      return { w: w, h: h, pw: pw, pt: pt, pb: pb, px: (w - pw) / 2,
               liq: pb - 34,     /* niveau de l'éluant dans la cuve */
               base: pb - 52,    /* ligne de dépôt */
               tm: pt + 26,      /* repère « 2 cm du bord » : là où il faut retirer la plaque */
               tt: pt + 3 };     /* haut de la plaque */
    }
    function prog(g) { return Math.max(0, (g.liq - f) / (g.liq - g.tm)); }   /* 0 au départ, 1 au repère */
    function clair(hex, w) {   /* mélange d'une couleur avec du blanc (w de 0 à 1) */
      var n = parseInt(hex.slice(1), 16), r = n >> 16, g = (n >> 8) & 255, b = n & 255;
      return 'rgb(' + Math.round(r + (255 - r) * w) + ',' + Math.round(g + (255 - g) * w) + ',' + Math.round(b + (255 - b) * w) + ')';
    }
    function spot(c, x, y, k, dist, lim, a) {
      var rx = 12 + 8 * dist, ry = 10 + 48 * dist;
      if (lim !== null && y - ry < lim) { y = lim + ry; }   /* la tache ne passe pas au-dessus du front : elle se place juste sous lui */
      var col = clair(COL[k][1], 0.4 * dist), gr = c.createRadialGradient(x, y, 0, x, y, Math.max(rx, ry));
      gr.addColorStop(0, col); gr.addColorStop(0.6, col); gr.addColorStop(1, 'rgba(255,255,255,0)');
      c.save(); c.translate(x, y); c.scale(rx / Math.max(rx, ry), ry / Math.max(rx, ry)); c.translate(-x, -y);
      c.globalAlpha = a; c.fillStyle = gr; c.beginPath(); c.arc(x, y, Math.max(rx, ry), 0, 2 * Math.PI); c.fill(); c.restore();
    }
    function draw() {
      if (!S || f === null) { return; }
      var c = S.ctx, g = geom(), trav = Math.max(0, g.base - f) * (1 + ext), tf = trav / (g.base - g.tm), p = prog(g);
      c.clearRect(0, 0, g.w, g.h);
      var cx0 = g.px - 40, cx1 = g.px + g.pw + 40, ct = g.pt - 12, cb = g.pb + 8;
      if (!sorti) { c.fillStyle = 'rgba(241,245,249,.7)'; c.fillRect(cx0, ct, cx1 - cx0, cb - ct); }
      /* plaque, puis zone imprégnée d'éluant (du front jusqu'en bas) */
      c.fillStyle = '#FFFFFF'; c.fillRect(g.px, g.pt, g.pw, g.pb - g.pt);
      c.fillStyle = 'rgba(186,230,253,.38)'; c.fillRect(g.px + 1, f, g.pw - 2, g.pb - f - 1);
      c.strokeStyle = '#94A3B8'; c.lineWidth = 1; c.strokeRect(g.px, g.pt, g.pw, g.pb - g.pt);
      /* repère « 2 cm du bord », en pointillés */
      c.strokeStyle = '#94A3B8'; c.setLineDash([2, 3]); c.beginPath(); c.moveTo(g.px, g.tm); c.lineTo(g.px + g.pw, g.tm); c.stroke(); c.setLineDash([]);
      txt(c, '2 cm', g.px + g.pw - 4, g.tm - 3, '#64748B', '9.5px system-ui, sans-serif', 'right');
      /* ligne de dépôt (crayon) et légendes sous la ligne */
      c.strokeStyle = '#64748B'; c.lineWidth = 0.8; c.beginPath(); c.moveTo(g.px + 6, g.base); c.lineTo(g.px + g.pw - 6, g.base); c.stroke();
      DEP.forEach(function (dep, i) {
        var x = g.px + g.pw * (i + 0.5) / 4;
        txt(c, dep[0] === 'M&M\u2019s vert' ? 'M&M\u2019s' : dep[0], x, g.base + 13, '#475569', '9.5px system-ui, sans-serif');
      });
      /* taches : mélange soustractif des couleurs, comme des encres sur papier */
      var ft = Math.max(0, g.base - f), lim = f < g.base ? f - 10 * Math.max(0, 1 - ft / 30) : null;   /* au départ, la tache, déposée sur la plaque sèche, peut dépasser un peu du front ; cette tolérance disparaît progressivement */
      c.save(); c.globalCompositeOperation = 'multiply';
      DEP.forEach(function (dep, i) {
        var x = g.px + g.pw * (i + 0.5) / 4;
        if (dep[1].length === 2) {   /* M&M's vert : zone de mélange au départ, puis séparation */
          var mix = Math.max(0, 1 - p / 0.3), ym = g.base - 0.51 * trav;
          if (mix > 0) {
            c.globalCompositeOperation = 'source-over';
            var gg = c.createRadialGradient(x, ym, 0, x, ym, 13); gg.addColorStop(0, '#2E9E4F'); gg.addColorStop(0.6, '#2E9E4F'); gg.addColorStop(1, 'rgba(46,158,79,0)');
            c.globalAlpha = 0.9 * mix; c.fillStyle = gg; c.beginPath(); c.arc(x, ym, 13, 0, 2 * Math.PI); c.fill(); c.globalAlpha = 1;
            c.globalCompositeOperation = 'multiply';
          }
        }
        dep[1].forEach(function (k) {
          var rf = COL[k][0], y = g.base - rf * trav, dist = Math.min(1, rf * tf), al = dep[1].length === 2 ? Math.min(1, 0.35 + p / 0.2) : 1;
          spot(c, x, y, k, dist, lim, al);
        });
      });
      c.restore();
      /* front marqué (après retrait de la plaque) */
      if (sorti && f < g.liq - 2) {
        c.strokeStyle = '#334155'; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(g.px, f); c.lineTo(g.px + g.pw, f); c.stroke(); c.setLineDash([]);
        txt(c, 'front de l\u2019éluant', g.px + g.pw + 6, f + 4, '#334155', '11px system-ui, sans-serif', 'left');
      }
      /* cuve : éluant devant la plaque, par transparence, puis paroi avant et couvercle */
      if (!sorti) {
        c.fillStyle = 'rgba(191,219,254,.45)'; c.fillRect(cx0 + 1, g.liq, cx1 - cx0 - 2, cb - g.liq - 1);
        c.strokeStyle = 'rgba(96,165,250,.8)'; c.lineWidth = 1; c.beginPath(); c.moveTo(cx0, g.liq); c.lineTo(cx1, g.liq); c.stroke();
        c.strokeStyle = '#94A3B8'; c.lineWidth = 1.4; c.strokeRect(cx0, ct, cx1 - cx0, cb - ct);
        c.fillStyle = 'rgba(203,213,225,.85)'; c.fillRect(cx0 - 6, ct - 10, cx1 - cx0 + 12, 10);
        txt(c, 'éluant', cx0 - 8, g.liq + 14, '#1D4ED8', '11px system-ui, sans-serif', 'right');
      }
      /* ligne de dépôt : repère à gauche de la plaque */
      c.strokeStyle = '#94A3B8'; c.lineWidth = 0.8; c.beginPath(); c.moveTo(g.px - (sorti ? 6 : 46), g.base); c.lineTo(g.px + 4, g.base); c.stroke();
      txt(c, 'ligne de dépôt', g.px - (sorti ? 10 : 50), g.base + 4, '#475569', '11px system-ui, sans-serif', 'right');
    }
    function reset() {
      var g = geom(); f = g.liq; run = false; sorti = false; trop = false; last = null; ext = 0;
      btn.disabled = false; btnOut.disabled = true; btn.innerHTML = '<i class="fa-solid fa-play"></i>&nbsp; Lancer l\u2019élution';
      $(root, '.nt-ccm-x').hidden = true;
      msg.textContent = 'La plaque est placée dans la cuve. Lancez l\u2019élution, et retirez la plaque au repère «\u00a02\u00a0cm\u00a0du\u00a0bord\u00a0».';
      draw();
    }
    function loop(ts) {
      if (!run) { return; }
      var dt = last === null ? 0 : Math.min(0.05, (ts - last) / 1000); last = ts;
      var g = geom(), k = 0.075 * (g.liq - g.tm);   /* vitesse de référence : le repère est atteint en une quinzaine de secondes */
      if (!trop) {
        f -= dt * k * (1.25 - 0.5 * Math.min(1, prog(g)));   /* l'éluant ralentit en montant */
        if (f <= g.tm) {
          f = g.tm; trop = true; $(root, '.nt-ccm-x').hidden = false; btnOut.disabled = true;
          msg.innerHTML = '<b>Trop tard&nbsp;!</b> Le front a dépassé le repère «&nbsp;2&nbsp;cm&nbsp;du&nbsp;bord&nbsp;», où il fallait retirer la plaque. Les colorants continuent de monter&nbsp;: leurs hauteurs ne sont plus comparables. La suite est accélérée (×3).';
        }
      } else {
        var sp = k * 3 * 0.75;   /* vitesse accélérée (×3) */
        if (f > g.tt) { f = Math.max(g.tt, f - dt * sp); }
        else { ext += dt * sp / (g.base - g.tt); }   /* front bloqué en haut : les taches continuent de monter */
        if (ext >= 2) {
          ext = 2; run = false; $(root, '.nt-ccm-x').hidden = true;
          btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; btn.disabled = false;
          msg.innerHTML = '<b>Trop tard&nbsp;:</b> le front a atteint le haut de la plaque, et toutes les taches se sont accumulées en haut. La chromatographie est inexploitable&nbsp;: recommencez, en retirant la plaque au repère «&nbsp;2&nbsp;cm&nbsp;du&nbsp;bord&nbsp;».';
          draw(); return;
        }
      }
      draw();
      requestAnimationFrame(loop);
    }
    btn.addEventListener('click', function () {
      if (sorti || (trop && !run)) { reset(); return; }
      run = !run; last = null; btnOut.disabled = trop;
      btn.innerHTML = run ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Reprendre';
      if (run) { requestAnimationFrame(loop); }
    });
    btnOut.addEventListener('click', function () {
      if (trop) { return; }
      run = false; sorti = true; btnOut.disabled = true; btn.disabled = false; btn.innerHTML = '<i class="fa-solid fa-rotate-left"></i>&nbsp; Recommencer'; draw();
      msg.innerHTML = prog(geom()) < 0.6 ? 'Les taches sont encore trop proches de la ligne de dépôt pour bien les distinguer&nbsp;: attendez davantage avant de retirer la plaque.' : 'Plaque retirée, front de l\u2019éluant marqué au crayon. Quels colorants contient le M&amp;M\u2019s vert&nbsp;? Cochez-les ci-dessous, puis vérifiez.';
    });
    $(root, '[data-act="check"]').addEventListener('click', function () {
      if (!sorti || prog(geom()) < 0.6) { msg.textContent = 'Réalisez d\u2019abord une chromatographie exploitable.'; return; }
      var sel = $$(root, 'input[name="ccmc"]').filter(function (x) { return x.checked; }).map(function (x) { return x.value; }).sort().join(',');
      msg.innerHTML = sel === 'E102,E133' ? '<span style="color:#16A34A;">Bravo&nbsp;!</span> La tache verte s\u2019est séparée en deux taches, l\u2019une à la hauteur du témoin E102 (jaune), l\u2019autre à celle du témoin E133 (bleu ciel)&nbsp;: le vert est un mélange de jaune et de bleu.'
        : '<span style="color:#E11D48;">Non.</span> Comparez la hauteur de chaque tache issue du M&amp;M\u2019s à celle des taches des témoins&nbsp;: il contient E102 et E133 (et pas E131, qui monte plus haut).';
    });
    S = canvasCtx(cv); reset();
    onResize(function () { S = canvasCtx(cv); draw(); });
  })();
})();
</script>
