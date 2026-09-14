+++
title = "Modèles démographiques"
date = 2021-03-06T14:20:50+01:00
weight = 3
chapter = false

+++


<script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/luxon@^2"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-luxon@^1"></script>

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
</style>




<h1 style="overflow-x:auto;">Les modèles démographiques</h1>

## Les croissances exponentielles


<div style="position:relative; width:836px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube DiMRTyl4538 >}}
</div>
<br>

<div style="position:relative;margin-left:auto;margin-right:auto;width:700px;max-width:100%;">
<img src="/expgrowth.png" style="box-shadow:none;background:none;">
</div>


{{< runpython lang="python" mode="toggle" >}}
somme = 0.01
nb_pieces = 1
for i in range(2,65):
    nb_pieces *= 2
    somme += nb_pieces*0.01
    print(f"À la case {i}, on possède {somme:_.2f} €")
{{< /runpython >}}

Question bonus : pourquoi la longueur des cordes d'un piano suit-elle une progression géométrique comme dans le dessin ci-dessous (réinvestissement du programme de 1ES)&nbsp;? Quelle est la raison de la suite&nbsp;?

![](/pianoexp2.png?width=300px)

<br>

## Croissance démographique

Selon **Malthus** (*Essai sur le principe de population*, 1798), en l'absence de limitation par la quantité de ressources disponibles, toute population croîtrait selon une progression géométrique. Et c'est bien ce que l'on observe un peu partout dans le monde au 19<sup>e</sup> et 20<sup>e</sup> siècle.

Malthus prévoyait par ailleurs que les moyens de subsistances ne pouvaient croître que de manière arithmétique rendant inéluctable le croisement entre ces deux croissances (population et ressources). L'économiste britannique prophétisait alors une paupérisation générale des populations si aucune politique de restriction des naissances n'était appliquée.

Ces idées ont eu un fort retentissement et sont parfois encore présentées comme du bon sens aujourd'hui bien que la réalité ait violemment battu en brèche le pronostic pessimiste de Malthus&nbsp;:

- 1960 : 3 milliards d'habitants, 2 milliards souffrant de malnutrition (soit 66&nbsp;%)
- 2000 : 6 milliards d'habitants, 800 millions souffrant de malnutrition (soit 13,3&nbsp;%)

Est-ce que cela nous assure pour autant que les ressources resteront suffisantes à l'avenir&nbsp;? Réchauffement climatique, pollution, appauvrissement génétique des cultures, etc., peuvent malheureusement rebattre les cartes.

L'évolution des populations humaines au 21<sup>e</sup> siècle vient elle aussi contredire Malthus puisqu'on observe partout un décrochage par rapport aux croissances exponentielles du 20<sup>e</sup> siècle indépendant des moyens de subsistance.


<canvas id="line-chart2" ></canvas>
<script>
new Chart(document.getElementById("line-chart2"), {
  type: 'line',
  data: {
    labels: ["-10000","-9000","-8000","-7000","-6000","-5000","-4000","-3000","-2000","-1000","0","100","200","300","400","500","600","700","800","900","1000","1100","1200","1300","1400","1500","1600","1700","1710","1720","1730","1740","1750","1760","1770","1780","1790","1800","1801","1802","1803","1804","1805","1806","1807","1808","1809","1810","1811","1812","1813","1814","1815","1816","1817","1818","1819","1820","1821","1822","1823","1824","1825","1826","1827","1828","1829","1830","1831","1832","1833","1834","1835","1836","1837","1838","1839","1840","1841","1842","1843","1844","1845","1846","1847","1848","1849","1850","1851","1852","1853","1854","1855","1856","1857","1858","1859","1860","1861","1862","1863","1864","1865","1866","1867","1868","1869","1870","1871","1872","1873","1874","1875","1876","1877","1878","1879","1880","1881","1882","1883","1884","1885","1886","1887","1888","1889","1890","1891","1892","1893","1894","1895","1896","1897","1898","1899","1900","1901","1902","1903","1904","1905","1906","1907","1908","1909","1910","1911","1912","1913","1914","1915","1916","1917","1918","1919","1920","1921","1922","1923","1924","1925","1926","1927","1928","1929","1930","1931","1932","1933","1934","1935","1936","1937","1938","1939","1940","1941","1942","1943","1944","1945","1946","1947","1948","1949","1950","1951","1952","1953","1954","1955","1956","1957","1958","1959","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"],
    datasets: [{ 
        data: [4432266,5616996,7242892,9577918,13201832,19075771,28774661,44487162,72586076,110419521,232123764,236904172,240611571,227549847,241539639,253237316,271478693,278185334,285713840,310967715,323407571,397923813,444750779,456389076,442480757,503240579,515751843,591721866,613189754,642718425,664734940,695347041,745664504,779892249,818828314,891049119,931578147,984741159,987628322,991098738,994610260,998163240,1001758044,1005395067,1009074742,1012797513,1016563866,1022630209,1027487469,1033631136,1040443689,1047427292,1054586106,1061924513,1069447070,1077158552,1084757875,1092947430,1099331577,1106253783,1113514792,1120876169,1128342960,1135961188,1143684846,1151515422,1158898384,1166619866,1172266726,1178216298,1183674995,1189194865,1194777021,1200422586,1206132721,1211908617,1217612799,1224118700,1228821489,1234333753,1239786237,1245319917,1250936428,1256637463,1262424720,1268300005,1273394934,1278698177,1281044111,1283605123,1285405357,1287317863,1289344086,1291485555,1293743896,1296120810,1298874784,1303155270,1305490771,1309347024,1313556287,1317850567,1322223328,1326674072,1331210602,1335831902,1341040002,1348154278,1353185947,1360191149,1367778454,1375441175,1383207445,1391057502,1398962396,1406939006,1415456507,1425998659,1434253944,1444559322,1455464560,1466507494,1477744363,1489095893,1500609770,1512259811,1523683199,1536461994,1545852788,1556562451,1567026235,1577633469,1588397643,1599255683,1610265238,1621405678,1633219852,1647405028,1658785643,1672564382,1687012805,1701647404,1716473051,1731494784,1746736854,1762200207,1777067748,1793323600,1804920684,1817990952,1830461187,1843131589,1855949027,1868851504,1881853176,1895037042,1909044309,1926217432,1939587826,1955971631,1973057174,1990416385,2008052088,2025945381,2044097070,2062543972,2081683468,2104067387,2122176586,2143517525,2165540428,2187836793,2210412972,2233367401,2256671866,2280342907,2303096438,2327357744,2344788534,2363887111,2381758939,2399659920,2417413700,2435048602,2454045831,2474648090,2500821769,2499322112,2543130368,2590270976,2640278784,2691979264,2746072064,2801002752,2857866752,2916108032,2970292224,3019233536,3068370688,3126686720,3195779328,3267212288,3337112064,3406416896,3475448064,3546810880,3620655360,3695390208,3770163200,3844800768,3920251392,3995516928,4069437184,4142505728,4215772416,4289657600,4365582848,4444007936,4524627456,4607984640,4691884032,4775836160,4861730816,4950063104,5040984576,5132294144,5223704064,5316175872,5406245888,5492686336,5577433600,5660727808,5743219712,5825145344,5906481152,5987312640,6067758592,6148898816,6230747136,6312407552,6393898496,6475751424,6558176256,6641416192,6725948416,6811597312,6898306048,6985603072,7073125376,7161697792,7250593280,7339013632,7426597376,7513474048,7599822336,7683789824,7764951040,7840952832,7909295104,7980000000,8045000000,8142000000],
        borderColor: "#3e95cd",
        backgroundColor: "#9FCAE6",
        fill: true
      }
    ]
  },
  options: {
    plugins: {
            title: {
      display: true,
      text: 'Évolution de la population mondiale'
    },
            legend: {
                display:false
            }
    },
    scales: {
            x: {
                type: 'time',
                time: {
                tooltipFormat:' y ',
                }
            }
        }
  }
});
</script>


<canvas id="line-chart" ></canvas>
<script>
new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: ["1500","1600","1700","1750","1800","1850","1900","1950","1975","2000","2025","2050","2075","2100"],
    datasets: [{ 
        data: [86,114,106,106,107,111,133,221,418,819,1530,2478,3362,3924],
        label: "Afrique",
        borderColor: "#3e95cd",
        fill: false
      }, { 
        data: [282,350,411,502,635,809,947,1402,2396,3736,4816,5267,5141,4674],
        label: "Asie",
        borderColor: "#8e5ea2",
        fill: false
      }, { 
        data: [168,170,178,190,203,276,408,547,677,727,741,734,636,587],
        label: "Europe",
        borderColor: "#3cba9f",
        fill: false
      }, { 
        data: [40,20,10,16,24,38,74,167,216,350,446,491,476,426],
        label: "Amérique du Sud",
        borderColor: "#e8c3b9",
        fill: false
      }, { 
        data: [6,3,2,2,7,26,82,172,235,313,383,421,440,448],
        label: "Amérique du Nord",
        borderColor: "#c45850",
        fill: false
      }
    ]
  },
  options: {
  plugins: {
    title: {
      display: true,
      text: 'Population mondiale par continent (en millions)'
    }},
    scales: {
            x: {
                type: 'time',
                time: {
                    tooltipFormat:' y ',
                }
            }
            }

  }
});
</script>

[Petit article en anglais](https://ourworldindata.org/world-population-growth-past-future) qui décrit l'évolution de la population mondiale de 1700 à ajourd'hui puis jusqu'à la fin du siècle grâce aux prédictions de l'ONU.

![](/datapopfutur.png?width=1000px)

<p style="text-align:center;"><a href="https://colab.research.google.com/drive/1Yr7roqIeHO5NIdHjDhFUMbfi-CM1mFEq?usp=sharing" style="color:green">$\rightarrow$ Correction</a></p>


Un [**article de CulturMaths**](https://culturemath.ens.fr/thematiques/lycee/comment-construire-un-modele-logistique) pour les matheux curieux qui voudraient en savoir plus sur les **modèles logistiques**.

![](/sabliertemps.png?width=500)


<iframe src="https://embed.radiofrance.fr/franceculture/diffusion/b6e0bae4-bf5c-4e46-a1b8-e9c9dcd611ad" frameborder="0" width="100%" height="auto"></iframe>


<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube LBudghsdByQ >}}
</div>


<br>

<div style="position:relative; width:800px; max-width: 100%; margin-left: auto;margin-right: auto;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
{{< youtube r6sa_fWQB_4 >}}
</div>

<br>


## Activités

<table style="text-align: center;">
  <tr >
    <th style="text-align: center;"><a href="/actdemo1.pdf">Maths et croissance</a></th>
    <th style="text-align: center;"><a href="/actdemo2.pdf">Modèle de Malthus</a></th> 
    <th style="text-align: center;"><a href="/actdemo3.pdf">Japon</a></th>
  </tr>
  <tr>
    <td><a href="https://www.geogebra.org/m/uetyvjer">appliquette geogebra</a></td>
    <td><a href="https://www.geogebra.org/m/bhuustyj">appliquette geogebra</a></td> 
    <td><a href="https://www.geogebra.org/m/vyyahdpq">appliquette geogebra 1</a><br><a href="https://www.geogebra.org/m/tf3qeh4z">appliquette geogebra 2</a><br><a href="https://www.geogebra.org/m/eean6ute">appliquette geogebra 3</a></td>
  </tr>
</table>

