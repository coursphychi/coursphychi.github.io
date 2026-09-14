+++
title = "Le futur des énergies"
date = 2021-03-06T14:20:50+01:00
weight = 2
chapter = false
hidden = true
+++



<style>
blockquote ul, blockquote li {
font-size: 1.1rem;
color: #999;
}
</style>


<!--<p style="text-align:center;font-size: 25px"><a href="https://presentationssite.github.io/tes/expos">Exposés</a>/<a href="https://presentationssite.github.io/tes/debats">Débats</a></p>-->


# Le futur des energies

| [Exposés](https://docs.google.com/spreadsheets/d/1M9vJymBWdIucjmWlli_9FMRs11DSSPedlvV9e_nc-Cs/edit?usp=sharing) | [Débats](https://presentationssite.github.io/tes/debats) |
| :--: | :--: |


## Deux siècles d'énergie électrique

### Un peu d'histoire

<br>

Dans sa fresque monumentale commanditée par la Compagnie parisienne de distribution d'électricité pour l'exposition universelle de 1937 intitulée [la Fée électricité](https://www.parismusees.paris.fr/sites/default/files/iframe/mam_360_sisso_dufy/), Raoul Dufy représente dans la partie inférieure une flopée de  savants et penseurs ayant contribué à l'invention de l'électricité.<br>[![](/feeelec.png)](https://www.parismusees.paris.fr/sites/default/files/iframe/mam_360_sisso_dufy/)

<br>

Vidéo survolant l'histoire de l'électricité au 19<sup>e</sup> siècle&nbsp;:
<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube JoscDcbAjbY >}}
</div>


<br>


### Quelques notions physiques importantes

![](/puissbd.png?width=700px)

<style>
#puiss p:first-child:after {
    content: 'Puissance';
}
</style>

{{% notice def puiss %}}
La **puissance** est la variation d'énergie par unité de temps&nbsp;:
$$\displaystyle P=\frac{\Delta E}{\Delta t}$$
Les unités de base sont le joule ($\pu{J}$) pour la variation d'énergie $\Delta E$, la seconde ($\pu{s}$) pour la durée $\Delta t$ et le watt ($\pu{W}$) pour la puissance $P$.<br>
Mais dans le secteur de l'électricité, on utilise le plus souvent l'heure ($\pu{h}$) pour $\Delta t$ et le kilowattheure $\pu{kWh}$ pour l'énergie.
{{% /notice %}}


<style>
#rend p:first-child:after {
    content: 'Rendement';
}
</style>
{{% notice def rend %}}
Définition du rendement $r$ :<br>
$\displaystyle r=\frac{E\_{utile}}{E\_{perdue}}=\frac{P\_{utile}}{P\_{perdue}}$<br>
{{%/notice%}}

<br>

Ajourd'hui, on sait obtenir de l'énergie électrique à partir de deux sources d'énergie très différentes&nbsp;:
- l'énergie mécanique
- l'énergie de rayonnement

<br>

### Conversion électromécanique


> Comment s'appelle et à quoi sert cette pièce d'un moteur thermique&nbsp;?

<div style="display: flex;justify-content: center;">
<div style="width:600px;">
<img src="/altvoiture.png" style="border-radius:30px">
</div>
</div>

{{%notice info%}}
Principe physique du fonctionnement d'un alternateur&nbsp;: l'**induction électromagnétique**.
{{%/notice%}}

<br>

<p style="text-align:center">
<a href="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html?locale=fr"><b>Animation sur le phénomène d'induction électromagnétique découvert par Faraday</b></a></p>

<p style="text-align:center">
<a href="https://vimeopro.com/user36345481/enseignement-scientifique-terminale-videos-dexperiences/video/420612845">Vidéo experience lycéee alternateur</a></p>


<br>

- Éclaté d'un **alternateur** :
![](/eclataltern.png)

- Une **turbine** (à gaz) :

<div style="display: flex;justify-content: center;">
<div style="width:600px;">
<img src="/turbine.png" style="border-radius:30px">
</div>
</div>


L'ensemble forme un **turbo-alternateur**.

![](/chainturbogen.png?width=800px)

> Quelle conversion opère la turbine / à quoi sert-elle&nbsp;?

{{%notice info%}}
Dans ce cas, le rendement vaut : $\displaystyle r=\frac{E\_{élec}}{E\_{méca}}=\frac{P\_{élec}}{P\_{méca}}$<br>
Un alternateur peut atteindre des **rendements**  supérieurs à 99%.<br>
Globalement, le rendement d'un alternateur croît avec sa masse (et par ricochet avec la puissance électrique qu'il délivre).
{{%/notice%}}

![](/groupelectro.png?width=400px)


L'alternateur d'un groupe électrogène (utilisé par exemple pour un food truck) capable de délivré 3&nbsp;kW a un rendement autour de 85% alors que l'alternateur du réacteur nucléaire de Flamanville-3 délivrant 1750&nbsp;MW a un rendement compris entre 98,2% et 99,3%.



<br>

### Photovoltaïsme

![](/chainpv.png?width=800px)

{{%notice info%}}
Principe physique du fonctionnement d'une cellule photovoltaïque&nbsp;: l'**effet photoélectrique**.
{{%/notice%}}


<p style="text-align:center">
<a href="https://www.youtube.com/watch?v=v-1zjdUTu0o">Vidéo expérience effet photoélectrique</a></p>

<br>


<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube 8RjGHmlOu58 >}}
</div>
<br>
<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube 7BUjVyw5LaM >}}
</div>

<br>


---

<br>
<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube AHFZVn38dTM >}}
</div>
<br>

## Les atouts de l’électricité

### Obtention d'énergie électrique sans combustion

Aujourd'hui, la majorité de l'énergie électrique est obtenue à partir de sources fossiles dans des **centrales thermiques à flamme**. Mais on sait faire autrement.

#### Centrales hydrauliques :

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube vqbdbigU900 >}}
</div>

En 2020, la puissance installée des centrales hydroélectriques atteint 1330&nbsp;GW, produisant environ  4370&nbsp;TWh soit 70 % de la production mondiale d'énergie renouvelable et 15,6 % de la production mondiale d’électricité en 2019.

La centrale hydroélectrique la plus puissante de France se trouve au barrage de Grand'Maison en Isère. Elle peut délivrer une puissance de 1800&nbsp;MW.

La plus grande centrale hydroélectrique au monde est le barrage des Trois-Gorges en Chine. Sa puissance installée est de 22500&nbsp;MW.

{{%notice note%}}
On distingue les centrales gravitaires, les stations de transfert d'énergie par pompage et les centrales maritimes.
{{%/notice%}}

<br>

#### Centrales nucléaires :

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube I09DhTubNqE >}}
</div>

En France, les réacteurs nucléaires délivrent une puissance entre 900&nbsp;MW et 1450&nbsp;MW et une centrale possède entre 2 et 6 réacteurs.

![](/parcnuc.png?width=800px)

Répartition des centrales nucléaires dans le monde&nbsp;:

<div style="display: flex;justify-content: center;">
<div style="width:800px;">
<img src="/repartcentr.png" style="border-radius:30px">
</div>
</div>

#### Centrales  géothermiques :

L'efficacité énergétique des centrales géothermiques est faible, environ 10 à 23%, parce que les fluides géothermiques sont à basse température en comparaison de la vapeur des chaudières. De par les lois de la thermodynamique, cette basse température limite l'efficacité des machines thermiques dans l'extraction d'énergie utile pendant la production d'électricité. La chaleur résiduelle est perdue, à moins qu'elle puisse être utilisée directement et sur place, par exemple dans des serres, des scieries ou dans le chauffage urbain. L'efficacité énergétique médiocre du système n'affecte pas autant les coûts opérationnels que pour une centrale à charbon ou autre combustible fossile, mais elle pèse sur la viabilité de la centrale. Afin de produire plus d'énergie que les pompes n'en consomment, la production d'électricité requiert des champs géothermiques à haute température et des cycles thermiques spécialisés.

Comme la géothermie ne repose pas sur des sources d'énergie intermittentes, telles que par exemple le vent ou le solaire, son facteur de charge peut être très élevé : il a été démontré qu'il peut aller jusqu'à 96%. Cependant la moyenne du facteur de charge des centrales était de 74,5% en 2008, selon le GIEC, et les centrales récentes atteignent souvent des facteurs de charge supérieurs à 90%.

La puissance installée des centrales géothermiques s'élève à 15950&nbsp;MW en 2020.

En France, la production d'électricité géothermique provient pour l'essentiel de la Centrale géothermique de Bouillante en Guadeloupe 15&nbsp;MW.

<br>

#### Parcs éoliens :

Une éolienne sur Terre peut délivrer aujourd'hui jusqu'à 3&nbsp;MW et en mer 15&nbsp;MW, mais le facteur de charge moyen est faible.

Les éoliennes fonctionnent environ 80% du temps mais avec une puissance très variable, située entre 0 et (théoriquement) 100% ; par exemple, en 2020, en France, la puissance éolienne a atteint son maximum à 13409&nbsp;MW le 10 février à 18 h, avec un facteur de charge de 80,1% ; son minimum a été observé à 124&nbsp;MW le 24 avril à 11 h. La puissance moyenne mensuelle observée a varié de 2713&nbsp;MW en août à 8342&nbsp;MW en février, alors que la puissance installée atteignait 17616&nbsp;MW fin 2020 ; le taux d'utilisation (facteur de charge) de cette puissance (puissance moyenne/puissance nominale) a été en moyenne de 26,35% en 2020.

En France, les plus gros investissements concernent des parcs éoliens offshore. Celui prévu au large de l'île d'Oléron s'étendrait sur 300&nbsp;km<sup>2</sup> et pourrait produire jusqu'à 1&nbsp;GW.

![](/parcoleron.png?width=800px)


[Document gouvernemental de préparation au débat public sur le projet éolien en mer au large d'Oléron](https://www.debatpublic.fr/sites/default/files/2021-09/2021-09-Eolien_mer_Oleron_DMO.pdf)

<br>


#### Centrales photovoltaïques :

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube k_ut9pb3kjU >}}
</div>

![](/cestas.png)

En France, la plus grande centrale solaire photovoltaïque est situé à Cestas en Gironde. Elle s'étend sur 260&nbsp;ha et peut délivrer jusqu'à 300&nbsp;MW.

<br>

#### Centrales solaires thermiques :

<div style="display: flex;justify-content: center;">
<div style="width:600px;">
<img src="/soltherm.png" style="border-radius:30px">
</div>
</div>

Une centrale solaire thermodynamique à concentration est un site industriel qui concentre les rayons du Soleil à l'aide de miroirs afin de chauffer un fluide caloporteur, lequel permet en général de produire de l'électricité. Ce type de centrale permet, en stockant ce fluide dans un réservoir, de prolonger le fonctionnement de la centrale plusieurs heures au-delà du coucher du Soleil.


Pourquoi ne pas couvrir le Sahara en panneaux solaires pour alimenter le monde en énergie&nbsp;?

<div style="display:flex;justify-content:center">
{{<x user="engineers_feed" id="1535130921182982145">}}
</div>

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{<youtube 7OpM_zKGE4o>}}
</div>

<br>

### Dangers des énergies

#### Dangers pour la santé

- [Site sur les déchets nucléaires par l'entreprise publique en ayant la charge](https://www.andra.fr/les-dechets-radioactifs/tout-comprendre-sur-les-dechets-radioactifs)

- [Interview de Jean-Marc Jancovici à la matinale de France-Culture](https://www.radiofrance.fr/franceculture/podcasts/l-invite-e-des-matins/transition-energetique-avons-nous-encore-le-temps-8678304)

- Dangerosités comparées des différentes sources d'énergie&nbsp;:

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube Jzfpyo-q-RM >}}
</div>

<br>

#### Dangers environnementaux

- impact sur les écosystèmes

![](/risqueolien.png?width=800px)

- émission de GES

![](/co2rnv.png?width=700px)

<br>

### Problème du stockage


[Page sur le stockage de l'électricité par EDF](https://particulier.edf.fr/fr/accueil/guide-energie/electricite/stockage-energie-electricite.html)

Pour pallier l’écart temporel entre la production d’électricité et son utilisation, il convient de prévoir des dispositifs de stockage. L’énergie électrique ne pouvant être stockée, il convient de la convertir auparavant. Trois conversions (en énergie chimique, potentielle ou électromagnétique) sont actuellement envisagées, dans des proportions très différentes.


- **Stockage d’énergie potentielle de pesanteur**&nbsp;:
Une solution de stockage très rentable développée depuis longtemps et largement majoritaire en terme d'énergie stockée est la station de **transfert d’énergie par pompage** (STEP). Aux heures creuses, l’eau d’un bassin aval est pompée et relevée vers un bassin en amont. Aux heures de pointe de consommation, l’eau est turbinée, transformant ainsi de l’énergie potentielle de pesanteur en énergie électrique.

- **Stockage chimique**&nbsp;:<br>
Celui-ci induit un certain nombre d’enjeux. Le secteur R&D travaille sur de nouvelles technologies. On peut notamment évoquer les recherches concernant la **batterie** Li-Air qui permettrait un stockage de l’ordre de 2 000 Wh.kg<sup>-1</sup> contre environ 200 Wh.kg<sup>-1</sup> pour les batteries Li-Ion très utilisées à l’heure actuelle (téléphone, véhicule électrique...). Cependant, d’autres facteurs restent problématiques dans l’utilisation de celles-ci (matières premières, recyclage...).<br>
L’**hydrogène** produit par électrolyse puis utilisé dans la pile à combustible constitue une autre voie de stockage chimique.<br>


- **Stockage d’énergie électromagnétique**&nbsp;:<br>
Le SMES (Superconducting Magnetic Energy Storage) permet de stocker l’énergie sous forme d’un champ magnétique créé par un courant continu circulant dans un supraconducteur.<br>
À l’heure actuelle, ce dispositif efficace mais très couteux n’est utilisé que dans la haute technologie.<br>
On peut aussi évoquer les [super-condensateurs](https://books.openedition.org/editionscnrs/11104?lang=en) qui stocke cette fois-ci sous forme d'un champ électrique ([vidéo expérience lycée condensateur](https://vimeopro.com/user36345481/enseignement-scientifique-terminale-videos-dexperiences/video/420604013))


<br>


## Optimisation du transport de l’électricité

![](/pilone.png)

- Les transformateurs

![](/transfo_color.png?width=500px)

<p style="text-align:center">
<a href="https://vimeopro.com/user36345481/enseignement-scientifique-terminale-videos-dexperiences/video/420615225">vidéo expérience lycée transformateur</a></p>

- Les lignes électriques :

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube qjY31x0m3d8 >}}
</div>

- Réseau acctuel et du futur (**smart grid**) :

  - Présentation RTE :
<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube P9-Y2MVP_tQ >}}
</div>

<br>

Extrait du [site de RTE](https://www.rte-france.com/eco2mix/la-consommation-delectricite-en-france) qui affiche la consommation d'électricité en France ainsi que d'autres données comme celles des échanges interrégionaux et internationaux&nbsp;:
<blockquote>
<p>
Le rôle de RTE est de garantir l’équilibre entre l’offre et la demande d’électricité en France :

<ul>
<li>La demande est estimée par RTE (prévision de consommation) ;</li>
<li>L’offre est celle des producteurs, commercialisateurs et responsables de programmation (prévision de production).</li>
</ul>

La prévision de consommation en France métropolitaine effectuée la veille pour le lendemain est la résultante d’un modèle prédictif utilisant :
<ul>
<li>des données météo (historique et prévisions) ;</li>
<li>des données de consommation (historique) ;</li>
<li>des données d’effacement (historique et prévisions), soit les capacités de réduction de consommation de certains clients ;</li>
<li>la thermosensibilité et les gradients été/ hiver, soit la hausse de la consommation liée à la baisse des températures ;</li>
<li>des éléments de calendrier (jours fériés, week-end, vacances scolaires…).</li>
</ul>
</p>
</blockquote>

<br>

<ul><ul><li>Adapter le réseau à la transition écologique : <a href="https://www.ecologie.gouv.fr/sites/default/files/Plan%20ressources%20R%C3%A9seaux%20%C3%A9lectriques.pdf">document gouvernemental.</a></li></ul></ul>



<br>



## Choix énergétiques et impacts sur les sociétés

#### [L'électricité en France](https://analysesetdonnees.rte-france.com/bilan-electrique-2023/production#Vuedensemble)

<div style="position:relative; width:1000px; max-width: 100%; margin-left: auto;margin-right: auto;">
<img src="/prodelec2023.png" width="80%" style="margin-top:-10px">
</div>

<br>

#### [L'énergie en France](https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/chiffres-cles-energie-2022/7-bilan-energetique-de-la-france)

![](https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/chiffres-cles-energie-2022/image/ensemble-des-energies-cgdd.svg)
[Compléments au graphe](https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/chiffres-cles-energie-2022/7-bilan-energetique-de-la-france#images-5)

<br>

#### [Perspectives et futur énergétique (objectif 2050)](https://assets.rte-france.com/prod/public/2021-12/Futurs-Energetiques-2050-principaux-resultats.pdf)

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube ok31_F_2_I0 >}}
</div>

<br>
<br>

#### [Les émissions de GES dans le monde](https://www.wri.org/insights/4-charts-explain-greenhouse-gas-emissions-countries-and-sectors)

[<img src="https://files.wri.org/d8/s3fs-public/2022-06/world-ghg-emissions-2019.png" width="80%" style="margin-top:-20px">]()


<br>


#### Enjeux de société 

<br>

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube SD9yVca6hHI >}}
</div>

<br>

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube yiw6_JakZFc >}}
</div>

<br>

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube LxgMdjyw8uw >}}
</div>

Le pétrole a ouvert une ère d'énergie abondante qui a eu des répercussions fantastiques sur l'humanité. Le défi est de réussir à s'en passer sans sacrifier entièrement l'incroyable confort qu'il a apporté.

![](/ironman.png)

![](/egiabond.png)

<div style="display:flex;justify-content:center">
{{<x user="AEffondrement" id="1551503292898893824">}}
</div>
