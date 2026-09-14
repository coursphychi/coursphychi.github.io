+++
title = "Inférences bayésiennes"
date = 2021-03-06T14:20:50+01:00
weight = 6
chapter = false
+++

<style>
 #correc
  {
    color: #006C65;
    border-left: solid 10px #C7DDDC;
  }
 #comm
  {
    color: #004D80;
    border-left: solid 10px #B3CAD9;
  }
 #commsum
  {
    color: #004D80;
  }
 #correcsum
  {
    color: #006C65;
  }
  #grosseformule 
{
    overflow-x: auto; 
  }
  /* 1. Rétablir la déclaration que votre reset a écrasée */
details > summary:first-of-type {
  display: list-item;     /* remet le triangle + l’accessibilité */
  cursor: pointer;        /* optionnel : feedback visuel */
}
/* 2. Si vous aviez aussi supprimé le list-style */
details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
</style>


#  Inférence bayésienne


<p style="text-align:center;font-size: 25px;border-top:solid  lightgray 5px;padding-top:20px;border-bottom:solid  lightgray 5px;padding-bottom:20px;font-weight:bold"><a href="https://presentationssite.github.io/tes/bayes">Présentation</a></p>



>En s'appuyant sur le théorème de Bayes, l'inférence bayésienne permet de structurer et mathématiser le <b>raisonnement inductif</b>.

Le raisonnement inductif vise à déduire des faits généraux à partir d'observations ponctuelles, à dévoiler le tableau complet sans n'en avoir vu que des morceaux.

Contrairement au raisonnement déductif dont la conclusion est nécessairement vraie, le raisonnement inductif est, lui, probabiliste et peut donc très bien aboutir à des conclusions fausses. Le logicien anglais Russel prend l'exemple du poulet qui a appris à associer la main qui le nourrit à quelque chose de bénéfique jusqu'au jour où cette même main vient lui tordre le cou. Il s'agit avant tout d'un pari... Parfois perdant.

<div style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;margin-bottom:-1em;margin-top:-1em;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);border-radius:10px;">
<img src="https://media.istockphoto.com/id/1803791347/photo/farmer-is-feeding-hen-from-hand.jpg?s=612x612&w=0&k=20&c=SQgBpyF27UqHag0WFJRvaXyacL7ldeyXp7aLkk_VDpM=" style="box-shadow:none;background:none;border-radius:10px;">
</div>

Malgré son imperfection logique, le raisonnement inductif est partout. Les sciences naturelles se sont en grande partie construites sur lui en proposant des règles extrapolées depuis des résultats d'expériences. On le trouve aussi au cœur des tribunaux (les preuves et témoins sont autant de points de données partiels utilisés pour établir la "vérité"). Et c'est encore lui qui se cache derrière tout diagnostic médical (les indices que sont les symptômes ou les résultats de tests permettent d'inférer l'état du patient).

La recherche en neuroscience va même jusqu'à supposer que nos cerveaux ont une structure biologique adaptée à ce type de raisonnement. Comme le poulet de Russel, notre cerveau semble tirer instinctivement des conclusions des régularités rencontrées. Une étude parue dans Science en 2012[^1] l'illustre bien en montrant que des bébés de 8 mois regardent plus longtemps une boite remplie de boules blanches et rouges lorsqu'on dévoile son contenu si le mélange ne semble pas correspondre à celui inféré à partir d'un échantillon de boules sorties préalablement de la boite&nbsp;!

[^1]: Alison Gopnik, “Scientific Thinking in Young Children: Theoretical Advances, Empirical Research, and Policy Implications”, *Science*, 337(6102), 1623–1627 (2012). DOI: 10.1126/science.1223416. <a href="https://www.alisongopnik.com/Papers_Alison/Scientific%20Thinking%20in%20young%20Children.pdf" target="_blank"><i class="fa-solid fa-book"></i></a>

[^2]: Hansem Sohn & Devika Narain, “Neural implementations of Bayesian inference”, *Current Opinion in Neurobiology*, 70, 121–129 (oct. 2021). DOI: 10.1016/j.conb.2021.09.008. <a href="https://neuro.nl/content/uploads/docs/1_222506087_1635319077.pdf" target="_blank"><i class="fa-solid fa-book"></i></a>

<div style="position:relative;margin-left:auto;margin-right:auto;width:400px;max-width:100%;margin-bottom:-1em;margin-top:-1em; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);border-radius:10px; ">
<img src="/bayesscience.png" style="box-shadow:none;background:none;border-radius:10px; ">
</div>

L'inférence bayésienne est considérée par des chercheurs en neuroscience comme le processus même du traitement de l'information par le cerveau[^2]. Le psychologue spécialisé en neuropsychologie Stanislas Dehaene le présente ainsi dans <a href="https://www.college-de-france.fr/chaire/stanislas-dehaene-psychologie-cognitive-experimentale-chaire-statutaire/annual-summaries" target="_blank">ses leçons</a> au Collège de France&nbsp;:


>Un vaste courant récent des sciences cognitives s’appuie sur la théorie mathématique de l’inférence bayésienne pour modéliser une très grande diversité de phénomènes psychologiques&nbsp;: perception, inférence statistique, prise de décision, apprentissage, traitement du langage... La rapidité avec laquelle cette théorie envahit et unifie divers domaines de la cognition, la simplicité de ses fondements axiomatiques, et la profondeur de ses conclusions justifient de parler d’une véritable « révolution bayésienne » en sciences cognitives.<br>
>
>Pour résumer, la théorie bayésienne fournit un modèle mathématique de la manière optimale de mener un raisonnement plausible en présence d’incertitudes. Dès la naissance, le bébé semble doté de compétences pour ce type de raisonnement probabiliste. L’inférence bayésienne rend également bien compte des processus de perception : étant donné des entrées ambigües, le cerveau en reconstruit l’interprétation la plus probable. La règle de Bayes indique comment combiner, de façon optimale, les <i>a priori</i> issus de notre évolution ou de notre mémoire avec les données reçues du monde extérieur. En cela, elle offre une nouvelle vision de l’apprentissage qui dépasse le dilemme classique entre théories empiristes et nativistes. Enfin, de nombreuses décisions humaines semblent résulter d’une approximation de la règle bayésienne d’accumulation d’évidence, combinée à une estimation de la valeur attendue des conséquences de nos choix. <br>
>
>Dans la mesure où les principes de l’inférence bayésienne sont ainsi partagés par de multiples domaines de la cognition, il se pourrait que l’architecture du cortex ait évolué pour approximer ce type de calcul probabiliste à grande vitesse, et de façon massivement parallèle. L’algorithme utilisé pourrait expliquer non seulement l’organisation du cortex en couches, mais aussi la manière dont notre cerveau anticipe sur le monde extérieur (codage prédictif) et dont il répond à la nouveauté (propagation des signaux d’erreur).


---

[Digression sur le raisonnement avec une autre vidéo d'Hygiéne Mentale.](https://www.youtube.com/watch?v=1c1jZQ9Bkq0&t=17s)

<br>

<div style="text-align: center;">
<iframe width="600" height="360" src="https://www.youtube.com/embed/x-2uVNze56s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);border-radius:15px;max-width:100%;"></iframe>
</div>

<br>

<div style="text-align: center;">
<iframe width="600" height="360" src="https://www.youtube.com/embed/1LzdESG6-2E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);border-radius:15px;max-width:100%;"></iframe>
</div>



<br>

### [Bibliothécaire vs agriculteur](/act1bayes.pdf)

On trouve dans le livre "*Système 1 / Système 2. Les deux vitesses de la pensée*" du prix Nobel d'économie Daniel Kahneman une expérience illustrant ce que peut nous apporter une meilleur familiarité avec le bayésianisme. 

L'expérience consistait à présenter à un amphi le portrait suivant&nbsp;: 

<p style="border:solid 4px gray;padding:10px">
<em>Steve est très timide et réservé, toujours prêt à rendre service, mais sans vraiment s'intéresser aux gens ou à la réalité. Personnalité docile et méticuleuse, il a besoin d'ordre et de structure, et se passionne pour les détails.</em>
</p>

Puis on demande à l'audience si Steve est plus susceptible d'être bibliothécaire ou agriculteur.

![](/portraitsteve.png?width=1000px)

Une large majorité répond alors bibliothécaire tant le portrait est proche du stéréotype associé à cette profession.<br>
Et c'était aussi le cas de ChatGPT 3.5 au départ (rappelons qu'il ne s'agit pas d'une IA qui raisonne mais d'une IA produisant un discours visant à satisfaire l'utilisateur)&nbsp;:

<div style="position:relative; width:600px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);border-radius:10px;">
<img src="/chatgptbayesagriculteur.png"  style="border-radius:10px;">
</div>

Mais sachant qu'aux Etats-Unis, où l'étude a été menée, il y a au moins 20 fois plus d'agriculteurs que de bibliothécaires, les chances que Steve soit bibliothécaire sont minces.

Un **raisonnement bayésien** nous aurait prémuni d'une conclusion trop hâtive sur la profession de Steve. Il consiste non pas à déduire une probabilité d'une information donnée mais à **mettre à jour** une **probabilité *a priori*** à partir de cette information. 

La probabilité *a priori* de l'hypothèse $H$ est $\textcolor{#0076BA}{P(H)}$.<br>
Ici, l'hypothèse est que Steve est bibliothécaire et la probabilité *a priori* vaut 4,8% $\left(\frac{1}{20+1}\right)$.

La probabilité *a priori* de l'hypothèse contraire $\overline{H}$ vaut $\textcolor{#56C1FF}{P(\overline{H})}=1-\textcolor{#0076BA}{P(H)}$.<br>
Ici, cela correspond à un Steve agriculteur puisqu'on suppose qu'il est soit bibliothécaire, soit agriculteur. La probabilité *a priori* d'un Steve agriculteur vaut 95,2%.

Le portrait de Steve est l'information nouvelle apportée $I$, elle modifie la plausibilité que Steve soit bibliothécaire tel un curseur qui va tirer la probabilité dans un sens ou dans l'autre. La probabilité de l'information $I$ est notée $\textcolor{#1DB100}{P(I)}$.

La **probabilité *a posteriori*** correspond alors à la probabilité de $H$ sachant  $I$, qu'on note $\textcolor{#CB297B}{P(H|I)}$ (que devient la probabilité de $H$ une fois qu'on a connaissance de l'information $I$).

C'est le **théorème de Bayes** qui va nous permettre de **mettre à jour** la probabilité *a priori* pour obtenir la probabilité *a posteriori*&nbsp;:


<div style="position:relative;border:solid 4px red;padding:10px;margin-left:auto;margin-right:auto; width:fit-content;max-width:100%;">
$
\displaystyle
\textcolor{#CB297B}{P(H|I)}=\frac{ \textcolor{#FF644E}{P(I|H)}\times \textcolor{#0076BA}{P(H)}}{\textcolor{#1DB100}{P(I)}}=\frac{ \textcolor{#FF644E}{P(I|H)}\times \textcolor{#0076BA}{P(H)}}{ \textcolor{#FF644E}{P(I|H)}\times \textcolor{#0076BA}{P(H)} + \textcolor{#00A89D}{P(I|\overline{H})} \times \textcolor{#56C1FF}{P(\overline{H})}}
$
</div>


- $\textcolor{#FF644E}{P(I|H)}$ est la probabilité d'avoir $I$ si $H$ est vraie (probabilité que Steve corresponde à la description s'il est bibliothécaire).

- $\textcolor{#00A89D}{P(I|\overline{H})}$ est la probabilité d'avoir $I$ si $H$ est fausse (probabilité que Steve corresponde à la description s'il est agriculteur).


Ces deux probabilités ne sont pas connues, mais on peut les estimer&nbsp;!

L'illustration ci-dessous permet de se rendre compte que le théorème de Bayes est finalement assez trivial&nbsp;:
![](/bayesensemble.png?width=600px)

Et encore plus trivial avec le plus grand effort pédagogique fait ci-dessous&nbsp;:

<div style="position:relative;margin-left:auto;margin-right:auto;width:800px;max-width:100%;">
<img src="/preuvebayes.png" style="border-radius:15px;">
</div>

On peut utiliser la représentation graphique décrite dans la vidéo d'introduction pour nous aider à faire les calculs en fonction de nos estimations. C'est ce qui est fait dans l'appliquette Geogebra ci-dessous (cliquer pour l'ouvrir).

<!--
<p style="position:relative;margin-left:auto;margin-right:auto;width:800px;max-width:100%;">
<a href="https://www.geogebra.org/m/czdbpj6b" style="position:relative;">
<img src="/bayesgeogebra.png"  style="border:solid 4px #1C90F3;border-radius:2%;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
</a>
</p>
-->

{{< geogebra id="jy5thkeg" maxwidth="800" rounded="true" shadow="true" >}}

> En supposant que le portrait corresponde à 40% des bibliothécaires et à 5% des agriculteurs, que vaut la probabilité a posteriori que Steve soit bibliothécaire ?

> La probabilté que le portrait corresponde à un bibliothécaire devrait être combien de fois supérieure à celle qu'il corresponde à un agriculteur pour faire basculer la probabilité a posteriori que Steve soit bibliothécaire au-delà de 50% ? Comparez au ratio bibliothécaires sur agriculteurs.

Moralité, le portrait correspond probablement plus à un agriculteur !


{{%notice info%}}
Les **fréquentistes** et les **bayésiens** interprètent les probabilités différemment.<br>
Pour les fréquentistes, une probabilité est la limite vers laquelle tendrait une fréquence mesurée sur un échantillon lorsqu'on fait tendre la taille de l'échantillon vers l'infini.<br>
Pour les bayésiens, une probabilité mesure un degré de conviction qui est mis à jour à chaque nouvelle information obtenue.<br><br>
Exemple d'énoncé où les deux approches divergent&nbsp;:<br>
Dire &laquo;&nbsp;<b>il y a 95 % de chances que le dé soit pipé</b>&nbsp;&raquo; est mathématiquement rigoureux en approche bayésienne mais est dénué de sens en approche fréquentiste.<br>
En effet, pour un **fréquentiste**, le dé est soit pipé, soit équilibré, il n'y a pas de hasard là-dedans : ce n'est pas une variable aléatoire. La probabilité étant considérée comme une réalité physique objective, attribuer une probabilité à une hypothèse concernant un objet dont la nature est fixe est impossible. La démarche est alors de calculer la probabilité d'obtenir un tel résultat (ou un résultat plus extrême) sous l'hypothèse que le dé est équilibré. Et si cette probabilité est inférieure à un <b>seuil</b> que l'on s'est fixé au préalable, on rejette l'hypothèse. L'hypothèse n'est donc pas plus ou moins probable mais acceptée ou rejetée. Le fréquentiste dira par exemple &laquo;&nbsp;je peux affirmer que le dé est pipé avec un risque d'erreur de 5%&nbsp;&raquo;.<br>
Pour un **bayésien**, la probabilité change de nature&nbsp;; c'est un état de connaissance ou un <b>degré de croyance</b> de l'observateur face à l'incertitude. Le dé possède une nature fixe, mais puisque on l'ignore, sa nature devient bien pour nous une variable aléatoire. Cela semble bien plus intuitif&nbsp;!
{{%/notice%}}


Autre célèbre exemple de portrait tiré du même livre de Kahneman (et toujours avec ChatGPT comme cobaye) :
<div style="display:flex;justify-content:center">
{{%x  user="FerryDanini" id="1624761081691340802"%}}
</div>


<br>

### Le paradoxe des deux enfants

Un couple a deux enfants. On nous informe que l'un des deux est une fille. Quelle est la probabilté que les deux enfants soient des filles&nbsp;?


![](/deuxfilles.png?width=200px)


> Utilisez le théorème de Bayes pour répondre en précisant d'abord $H$ et $I$, puis en déterminant les différentes probabilités $P(H)$, $P(I)$ et $P(I|H)$.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$H$ : les deux enfants sont des filles.<br>
$I$ : l'un des deux enfants est une fille.<br>
$P(H) = 1/4$ (dans l'hypothèse où il y a autant de chance d'avoir une fille qu'un garçon).<br>
$P(I) = 3/4$ (puisque cela correspond à 3 possibilités parmi 4 équiprobables&nbsp;: GG, FF, FG et GF). <br>
$P(I|H)$ : la probabilité qu'un des deux enfants soit une fille sachant que les deux enfants sont des filles est bien sûr de 100%.<br>
C'est tout l'intérêt du théorème de Bayes de permettre de retourner $P(I|H)$ qui est évident en $P(H|I)$ que l'on cherche&nbsp;:<br>
<div id="grosseformule" style="color:#006C65;">

$$
\begin{aligned}
\color{#006C65}P(H|I)&= \color{#006C65}\frac{P(I|H)\times P(H)}{P(I)}\\\\
&\color{#006C65}=\frac{1\times 1/4}{3/4}\\\\
&\color{#006C65}=\frac13
\end{aligned}
$$

</div>
</blockquote>
</details>

> Vérifier votre résultat en complétant le code python suivant afin qu'il simule une expérience sur 100000 couples de deux enfants.


{{< runpython lang="python" mode="toggle" >}}
from random import randint

aumoinsunefille = 0
deuxfilles = 0
n = 100000

for i in range(n):
	enfant1 = randint(0,1)
	enfant2 = randint(0,1)
	if (enfant1 == 1) or (enfant2 == 1) : # or n'exclut pas la possibilité que les deux soient des filles
		aumoinsunefille = aumoinsunefille + 1
		if enfant1 == enfant2:
			deuxfilles = deuxfilles + 1

P = ... # à compléter
print("Probabilité que l'autre enfant soit une fille :")
print(f"{P:.1f}%")
{{< /runpython >}}

Un couple a deux enfants. On apperçoit une fille dans le jardin. Quelle est la probabilté que les deux enfants soient des filles&nbsp;?

> La réponse change-t-elle ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Oui !<br>
Dans l'hypothèse $H$ où il y a deux filles (1 chance sur 4), il y a 100% de chance de voir une fille dans le jardin. On a donc comme précédemment $P(I|H)=1$.<br> 
Mais dans l'hypothèse où les deux enfants ne sont pas deux filles ($P(\bar{H})=3/4$), la probabilité de voir une fille dans le jardin vaut $P(I|\bar{H})=1/3$. En effet, il faut à la fois que les parents aient un garçon et une fille (2 chances sur 3 dans l'hypothèse $\bar{H}$), et il faut que cela soit la fille dans le jardin et non le garçon (1 chance sur 2).<br>
Par conséquent $P(I)$ devient&nbsp;: $P(I)=P(I|H)\times P(H) + P(I|\bar{H})\times P(\bar{H})=1\times 1/4 + 1/3\times 3/4 = 1/2 $<br>
On a donc $P(H|I)=\frac{1\times 1/4}{1\times 1/4 + 1/3\times 3/4}=\frac{1}{2}$.
</blockquote>
</details>

> Comment modifier le code pour qu'il corresponde à cette situation&nbsp;?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">from random import randint
vufillejardin = 0
deuxfilles = 0
n = 100000
enfants = [None,None]
for i in range(n):
  enfants[0] = randint(0,1)
  enfants[1] = randint(0,1)
  if enfants[randint(0,1)] == 1: # on voit une fille dans le jardin (on tire au sort l'enfant)
    vufillejardin += 1
    if enfants[0] == enfants[1]: # deux filles
      deuxfilles += 1
P = deuxfilles/vufillejardin*100
print(f"Probabilité qe les parents aient deux filles sachant qu'on a vu une fille dans le jardin : {P:.1f}%")
</code></pre>
</blockquote>
</details>


{{%notice note%}}
la probabilité a priori d'avoir deux filles vaut 1/4.<br>
L'information apportée tire cette probabilité vers le haut.<br>
Elle tire plus dans le second cas que dans le premier, car l'information est plus précise ; un tirage a été fait.<br>
Dans le premier cas, l'information supplémentaire laisse trois possibilités équiprobables (on sait seulement que le couple ne peut pas avoir deux garçons), alors que dans le second, il n'y en a plus que deux (l'autre enfant est soit une fille, soit un garçon)&nbsp;!
{{%/notice%}}

<br>

### Problème de Monty Hall

Dans un ancien jeu télévisé américain, présenté par Monty Hall, un candidat devait choisir une porte parmi trois. Derrière l'une d'elles se cache une voiture et derrière les deux autres une chèvre.

Après que le candidat ait indiqué son choix, Monty ouvre une des deux autres portes derrière laquelle il sait que se trouve une chèvre (s'il y a une chèvre derrière les deux portes non choisies, il en choisit une au hasard).

Il demande ensuite au candidat s'il veut garder sa porte ou s'il veut choisir l'autre porte.

Doit-il changer de porte ?


> <span style="font-size: 1.1rem;color: #999;">Supposons que vous ayez préalablement choisi la porte 1 et que Monty ouvre la porte 2. Montrez en utilisant le théorème de Bayes que le candidat a intérêt à changer de porte.<br>Pour raisonner, on va prendre pour hypothèse $H$ "il y a une voiture derrière la porte 3" et pour information $I$  : "Monty ouvre la porte 2".</span>

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<div style="position:relative; width:800px; max-width:100%; margin-left: auto; margin-right: auto; border-radius:10px; aspect-ratio:800/450;">
<iframe width="800" height="450"  src="https://www.youtube.com/embed/J94PPS0qkAw?si=y-DGc1EiTtr3oNZs&amp;start=318" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="max-width:100%;border-radius:10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); aspect-ratio:800/450; height:auto;"></iframe>
</div>
</blockquote>
</details>


![](https://imgs.xkcd.com/comics/monty_hall.png)

<p style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;">
<img src="/chevre.png"  style="border-radius:2%;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
</p>


<br>

### L'argument de l'Apocalypse

Le philosophe Nick Bolstrom présente sa version du "Doomsday Argument" à peu près ainsi&nbsp;:

**1<sup>re</sup> étape :<br>**
Imaginez un univers constitué de 100 boites habitées chacune par un humain.<br>
L'extérieur des boites est peint en bleu pour 90 d'entre elles et en rouge pour les 10 autres.<br> Chaque personne connaît la situation et on leur demande de deviner la couleur de leur boite.<br>


> Que répondez-vous ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Si vous supposez qu'il y a 90% de chance que votre boite soit bleue, vous êtes SSA (self-sampling assumption) dans la terminologie de Bostrom. Et si vous pensez plutôt qu'il n'y a que 50% de chance qu'elle soit bleue, vous échappez à la conclusion du Doomsday.
</blockquote>
</details>

<br>

**2<sup>e</sup> étape :<br>**
On modifie un peu l'expérience en remplaçant la couleur des boites par une numérotation entre 1 et 100 (le numéro est, là encore, peint à l'extérieur).<br>
Maintenant, un dieu bizarre lance une pièce. Si ça tombe sur face, il crée une personne dans chaque boite et si ça tombe sur pile, il ne crée des personnes que dans les boites 1 à 10.<br>
Vous vous retrouvez dans une de ces boites et on vous demande s'il y a 10 ou 100 personnes dans l'univers.<br>

> N'ayant pas d'information supplémentaire, que répondez-vous&nbsp;?

> Et si on vous demande d'estimer la probabilité que le numéro de votre pièce soit entre 1 et 10 selon chacune des deux possibilités pour le pile ou face&nbsp;?

Supposons maintenant que vous sortiez de votre boite pour découvrir que son numéro est le 7. 

> On vous demande alors d'estimer la probabilité que la pièce soit tombée sur pile maintenant que vous connaissez le numéro de votre boite.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<div id="grosseformule">

$$
\color{#006C65}
\begin{aligned}
P(\text{Pile}|7)&=\frac{P(7|\text{Pile})P(\text{pile})}{P(7|\text{Pile})P(\text{pile})+P(7|\text{face})P(\text{face})}\\\\
&=\frac{1/10\times 1/2}{1/10\times 1/2 + 1/100\times 1/2}\\\\
&=\frac{10}{11}\\\\
&=91\\%
\end{aligned}
$$

</div>
</blockquote>
</details>


<br>

**3<sup>e</sup> étape :<br>**
On transpose ces résultats à la situation actuelle sur Terre.<br>
Posons les deux hypothèses rivales suivantes&nbsp;:
- apocalypes précoce : l'humanité va s'éteindre dans le prochain siècle et la quantité totale d'humain ayant existé sera d'environ 200 milliards.
- apocalypse tardive : l'humanité va survivre le prochain siècle et coloniser la galaxie. Le nombre total d'humain ayant existé s'élèvera à 200 mille milliards.

> Quelle probabilité a priori attribuez-vous à chacun de ces scénarios&nbsp;?

Vous n'êtes pas loin d'être l'humain n°100 milliards (en terme d'ordre de naissance).

> Comme le théorème de Bayes va-t-il faire glisser les probabilités attribuées à chacun des scénarios sachant cela (faire le parallèle avec l'univers des boites numérotées).



<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)</summary>
<blockquote id="comm">
On peut échapper à cette conclusion sinistre en rejetant SSA. On peut en effet considérer qu'il y a plus de chance qu'il y ait 100 personnes que 10 car le fait que j'existe devient alors plus probable.<br>
Sans connaître le numéro de la boite, on peut donc penser qu'il y a 10 fois plus de chances que dieu ait tiré face. Cela rééquilibre <i>a posteriori</i> les deux hypothèses car maintenant, $P(\text{Pile}|7)$ vaut 1/2 et de même, les deux scénarios d'apocalypse retrouvent leurs probabilités <i>a priori</i>.
</blockquote>
</details>

<img src="/doomsday.png" style="border-radius:20px">

Nick Bostrom a aussi développé des arguments semblables sur la probabilité que l'on vive dans une simulation. 


<br>
<br>

### Bayes et cote

Le théorème de Bayes peut se réexprimer en terme de cotes. Cela permet de simplifier à la fois son calcul et son interprétation.

La **cote** d'un événement (*odds* en anglais) est le ratio de la probabilité que l'événement se produise par la probabilité qu'il ne se produise pas. On l'exprime en général comme une paire de nombres (le numérateur et le dénominateur). 

Par exemple, si un évènement a une probabilité de 5% de se produire, il a donc aussi une probabilité de 95% de ne pas se produire et sa cote est alors de 5 contre 95 (ou 1 contre 19 qu'on peut aussi noter $1:19$).

> Si un pari consiste à obtenir un 5 ou un 6 au dé, que vaut alors sa cote&nbsp;?

> À quelle cote correspond une probabilité de 50%&nbsp;?

L'utilisation des cotes est très commune pour les paris sportifs en Angleterre.

**Théorème de Bayes exprimé en termes de cote**&nbsp;:

<div style="position:relative;border:solid 4px red;padding:10px;margin-left:auto;margin-right:auto; width:50%;text-align:center">
La cote de $H$ sachant $I$ vaut la cote de $H$ multipliée par le facteur de Bayes $\left(\frac{P(I|H)}{P(I|\overline{H})}\right)$.
</div>


Le facteur de Bayes mesure le mérite relatif des deux hypothèses $H$ et $\bar{H}$, le rapport de leurs vraisemblances.<br>


Vérifions avec Steve :

La cote de $H$ correspond au ratio bibliothécaires/agriculteurs (soit 1/20) et le facteur de Bayes correspond à combien de fois le portrait $I$ correspond plus à un bibliothécaire qu'à un agriculteur. Si le facteur de Bayes vaut 20, on trouve une cote de 1 pour la cote a posteriori, ce qui correspond bien à une probabilité de 50% que Steve soit bibliothécaire.

> <span style="font-size: 1.1rem;color: #999;">Reprenez la première questions du paradoxe des deux filles en utilisant les cotes.</span>



<br>



### [Inférence bayésienne et diagnostic médical](/act-diagno.pdf)


Le psychologue Gerd Gigerenzer présente le problème suivant dans un séminaire de statistique à des gynécologues en activité&nbsp;:

<p style="border:solid 4px gray;padding:10px">
<em>Une femme de 50 ans sans symptôme passe une mammographie de routine. L'examen se révèle positif. Alarmée, elle veut savoir avec quelle certitude cela implique qu'elle a un cancer du sein.<br>À part le résultat du test, vous ne savez rien sur cette femme.<br>La prévalence des cancers du sein est de 1% chez les femmes de cet âge.<br>La sensibilité du test est de 90%.<br>Et sa spécificité est de 91%.<br><br>
Parmi les femmes dont le test est positif, combien sont atteintes d'un cancer du sein&nbsp;?<br>A : 9 sur 10 ; B : 8 sur 10 ; C : 1 sur 10 ; D : 1 sur 100</em>
</p>

<p style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;">
<img src="/mammo.png"  style="border-radius:5%;">
</p>


---

Un peu de vocabulaire :

- La **sensibilité** d'un test mesure sa capacité à donner un résultat positif lorsqu'une hypothèse est vérifiée = capacité à détecter un maximum de malades (avoir le moins possible de faux négatifs).
- La **spécificité** d'un test mesure sa capacité à donner une résultat négatif lorsque l'hypothèse n'est pas vérifiée = capacité à ne détecter que les malades (avoir le moins possible de faux positifs).

En notant VP et FP les vrais et les faux positifs, et VN et FN les vrais et faux négatifs, on a&nbsp;:

|                  | Malade | Non malade |
| :--------------: | :----: | :--------: |
| **Test positif** |   VP   |     FP     |
| **Test négatif** |   FN   |     VN     |

- sensibilité $=\frac{VP}{VP+FN}$

- spécificité $=\frac{VN}{VN+FP}$

<div style="position:relative;margin-left:auto;margin-right:auto;width:800px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/senssib.png" style="box-shadow:none;background:none;">
</div>

En utilisant le code couleur du schéma précédent, un test sera d'autant plus sensible que l'ensemble des malades (hachuré rouge) ne déborde pas de l'ensemble des tests positifs (hachuré bleu). La **sensibilité** est en effet donnée par la proportion entre l'aire à la fois hachurée rouge et bleue (les VP) sur toute l'aire hachurée rouge (les malades).

Et la **spécificité** correspond à la proportion d'aire verte seule (les non malades avec un test négatifs, VN) sur toute l'aire verte (verte seule + verte hachurée bleue, alias l'ensemble des non malades). 

---


{{%notice info%}}
En bon bayésien, il ne faut pas considérer qu'un test détermine si on a une maladie, ni même qu'il détermine les chances d'avoir une maladie.<br>
Tout ce qu'il fait, c'est **mettre à jour** les chances d'avoir une maladie&nbsp;!
{{%/notice%}}


> Que vaut le facteur de Bayes dans cet exemple&nbsp;?<br>

<details>
<summary id="correcsum">
Réponse (cliquer pour afficher)</summary>
<blockquote id="correc">
$\displaystyle
\frac{P(+|\text{Cancer})}{P(+|\overline{\text{Cancer}})}=\frac{\text{probabilité de vrais positifs}}{\text{probabilité de faux positifs}}=\frac{\text{sensibilité}}{\text{1-spécificité}}
$
</blockquote>
</details>


Le théorème de Bayes version cote devient donc&nbsp;:

<div style="position:relative;border:solid 4px black;padding:20px;margin-left:auto;margin-right:auto; width:fit-content;max-width:100%;text-align:center">

$\displaystyle
cote(\text{cancer}|+)=\frac{\text{sensibilité}}{\text{1-spécificité}}\times cote(\text{cancer})
$

</div>



> <span style="font-size: 1.1rem;color: #999;">Quelle est la bonne réponse (les cotes permettent de l'estimer facilement)&nbsp;?</span>

Plus de la moitié des docteurs présents ont choisi la réponse A, ce qui est très à côté de la plaque, et seulement 1 sur 5 ont choisi la bonne réponse...

Changeons la prévalence à 10 %&nbsp;:

<div>
<table>
<tr>
<th>prévalence</th> <td> 10% </td>
</tr>
<tr>
<th>sensibilité</th> <td> 90% </td>
</tr>
<tr>
<th>spécificité</th> <td> 91% </td>
</tr>
</table>
</div>

> <span style="font-size: 1.1rem;color: #999;">Que devient la probabilité d'avoir un cancer en cas de test positif&nbsp;?</span>


Passons-la maintenant à 0,1 %&nbsp;:

<table>
<tr>
<th>prévalence</th> <td> 0,1% </td>
</tr>
<tr>
<th>sensibilité</th> <td> 90% </td>
</tr>
<tr>
<th>spécificité</th> <td> 91% </td>
</tr>
</table>

> <span style="font-size: 1.1rem;color: #999;">Que vaut $P(cancer|+)$  maintenant&nbsp;?
</span>

Augmentons la spécificité à 99 % et reprenant une prévalence de 1 %.

<table>
<tr>
<th>prévalence</th> <td> 1% </td>
</tr>
<tr>
<th>sensibilité</th> <td> 90% </td>
</tr>
<tr>
<th>spécificité</th> <td> 99% </td>
</tr>
</table>


> <span style="font-size: 1.1rem;color: #999;">Que devient la probabilité&nbsp;?</span>

Et si le test est négatif ?

> <span style="font-size: 1.1rem;color: #999;">Reprendre les données de départ et trouvez la probabilité de ne pas avoir de cancer si on a été testé négatif.</span>

> <span style="font-size: 1.1rem;color: #999;">Et si on passe un second test négatif&nbsp;?</span>


<br>


#### [Moustiques](/act3bayes.pdf)

Trois maladies virales peuvent être transmises par les moustiques&nbsp;: 
- dengue 
- chikungunya 
- zika

Elles provoquent des symptômes qui peuvent être assez proches, ce qui les rend difficiles à différencier directement. 


<p style="position:relative;margin-left:auto;margin-right:auto;width:500px;max-width:100%;">
<img src="/moustiques.png"  style="border-radius:10%;">
</p>


Ici on s’intéresse à la mise en place d’une aide statistique
au diagnostic. Pour cela, on va s’appuyer sur des données obtenues chez des personnes dont le diagnostic a pu être certifié par des examens biologiques. Pour simplifier, on supposera que ces caractères apparaissent indépendamment chez les personnes infectées.

<br>

|        symptômes        | Dengue | Chikungunya | Zika |
| :---------------------: | :----: | :---------: | :--: |
|         Fièvre          |  95%   |     75%     | 75%  |
|       Courbatures       |  75%   |     95%     | 50%  |
|   Douleurs oculaires    |  50%   |     25%     | 50%  |
| Déficit globules blancs |  50%   |     50%     | 25%  |
|       Hémorragie        |  25%   |     5%      |  5%  |

<br>

À partir de ces données, on veut déterminer les probabilités de chaque maladie selon les symptômes présentés et dans des conditions différentes.<br>
La forme du théorème de Bayes la plus pratique est dans ce cas&nbsp;: 

<div style="overflow-x:auto;">
$$\displaystyle
P(\text{maladie}|\text{symptômes})=\frac{P(\text{symptômes}|\text{maladie})\times P(\text{maladie})}{P(\text{symptômes})}
$$
</div>

> Vous êtes internes au service de maladies infectieuses du CHU de Limoges et une personne se présente avec à la fois de la fièvre, pas de courbatures et des douleurs oculaires. La personne revient d’un pays dans lequel aucune des trois maladies n’est épidémique. On considère donc a priori que les trois maladies sont équiprobables.
>
>	- Calculer la probabilité que la personne présente ces 3 symptômes ensemble pour chacune des maladies $P(\text{symptômes}|\text{maladie})$.
>		
>	- Calculer la probabilité d'avoir ces symptômes quelle que soit la maladie $P(\text{symptômes})$ <br>aide&nbsp;: $P(\text{symptômes})=\sum_{\text{maladie}}P(\text{symptômes}|\text{maladie})\times P(\text{maladie})$
>
> - Quelles sont les probabilités a posteriori de chaque maladie si cette personne présente ces symptômes&nbsp;? Quel est selon vous le diagnostic le plus probable dans ce cas&nbsp;?
>
> Si vous apprenez maintenant qu'en fait la personne revient d'un pays dans lequel sévit une épidémie de Chikungunya. A priori, il y a 90&nbsp;% de chances qu’elle ait été infectée par le Chikungunya et 5&nbsp;% par chacune des deux autres maladies. Quel est le diagnostic le plus probable dans ce cas&nbsp;?


<br>



<style>
#spam p:first-child:after {
    content: 'Inférence bayésienne et détection de spams';
}
</style>

{{%notice note spam%}}
Un des premiers programmes de filtrage bayésien du courrier électronique était le programme iFile de Jason Rennie, publié en 1996.<br><br>
Le principe, analogue à celui du diagnostic médical, repose sur le fait que les mots du dictionnaire ont des probabilités différentes d’apparaître dans les spams et dans les courriers légitimes.<br><br>
Le filtre de détection des spams ne connaît pas à l’avance les probabilités d’apparition de ces mots, c’est pourquoi il lui faut une phase d’apprentissage pour les évaluer. Cette phase d’apprentissage est analogue à la phase de calibrage du test médical étudié ci-dessus.<br><br>
L’apprentissage se fait à partir de l’observation du comportement des utilisateurs, qui doivent indiquer manuellement si un message est un spam ou non. Pour chaque mot de chaque message « appris », le filtre ajustera les probabilités de rencontrer ce mot dans un spam ou dans un courrier légitime et le stockera dans sa base de données.<br><br>
On note $P(M|S)$  la probabilité qu’un spam contienne le mot $M$ et $P(M|\overline{S})$  la probabilité qu’un courrier légitime contienne le mot $M$. Ces deux probabilités sont estimées au cours de la phase d’apprentissage, tout comme la probabilité $P(S)$ qu’un message quelconque soit un spam (analogue à la prévalence $P(\text{maladie})$  dans le test médical).<br><br>
Une fois ces valeurs déterminées, la formule de Bayes permet de calculer la probabilité qu’un message donné soit un spam sachant qu’il contient le mot $M$ selon la formule&nbsp;:<br>
$\displaystyle P(S|M)=\frac{P(M\cap S)}{P(M)}=\frac{P(M|S)P(S)}{P(M|S)P(S)+P(M|\bar{S})P(\bar{S})}$<br>
Cette probabilité est comparée à un seuil ; si elle est supérieure au seuil,
le filtre classera ce message dans les spams.<br><br>
Dans la réalité, on travaille non pas sur un seul mot $M$, mais sur un stock de mots, en faisant l'hypothèse naïve que les mots présents dans un message sont indépendants les uns des autres. Cela est faux dans les langages naturels, où par exemple la probabilité de trouver un adjectif est influencée par celle de trouver un nom. De plus, cette technique
de filtrage, connue sous le nom de filtrage bayésien naïf, ne tient pas compte du sens
des mots, alors qu’il a une incidence sur la présence simultanée de certains mots à l'intérieur du message. Par exemple, la présence du mot « anniversaire » n’est pas indépendante de celle du mot « joyeux ».
{{%/notice%}}