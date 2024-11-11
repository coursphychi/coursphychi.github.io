/* eslint-env es6 */
/* eslint-env browser */
/* exported recap, myChart, valide */
/* global Chart */ 

const taille = 40;
var arrDeg = Array(taille);
var arrRep = Array(taille); 
var corrArray = [0,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1];
var myChart; // Variable globale pour stocker l'instance du graphique

function recap(element) {
  var valeur = element.selectedIndex;
  var id = element.id;
  var type = id.slice(0,3);
  var num = parseInt(id.slice(3));
  if (type == "deg") {
    arrDeg[num-1] = valeur-1;
  } else {
    arrRep[num-1] = valeur-1;
  }
}

function updateChart(yArray, yParfait, pointSizes) {
    var ctx = document.getElementById('myPlot').getContext('2d');
    if (window.myChart) {
        window.myChart.destroy();
    }

    window.myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [50,67,83,100],
            datasets: [{
                label: 'Vous',
                data: yArray,
                borderColor: 'blue',
                backgroundColor: 'transparent',
                pointBackgroundColor: 'blue',
                pointRadius: pointSizes,
                fill: false
            }, {
                label: 'Idéal',
                data: yParfait,
                borderColor: 'red',
                backgroundColor: 'transparent',
                pointBackgroundColor: 'red',
                pointRadius: 5,
                fill: false
            }]
        },
        options: {
            responsive: true,
            devicePixelRatio: 3,
            scales: {
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Pourcentage de confiance'
                    }
                },
               y: {
    beginAtZero: true,
    title: {
        display: true,
        text: 'Pourcentage de bonnes réponses'
    },
    ticks: {
        stepSize: 10,
        max: 100,  // valeur maximale des étiquettes de l'axe des ordonnées
        suggestedMax: 105  // valeur maximale suggérée
    }
}

            }
        }
    });
}



function valide() {
    var degEff = [0,0,0,0];
    var degBonne = [0,0,0,0];
    var xArray = [50,67,83,100];
    var yArray = [0,0,0,0];
    var yParfait = xArray;
    for (let i = 0; i < taille; i++) {
        degEff[arrDeg[i]] += 1;
        if (arrRep[i] == corrArray[i]) {
            degBonne[arrDeg[i]] += 1;
        }
    }
    for (let i = 0; i < 4; i++) {
        yArray[i] = degBonne[i]/degEff[i]*100 || 0;
    }

    // tableau de tailles de points basé sur degEff
    var pointSizes = degEff.map(value => Math.min(20,1 + value*2)); // taille minimale de 5 pour la visibilité
    
    updateChart(yArray, yParfait, pointSizes);
    
    for (let i = 1; i < 5; i++) {
        var x = document.getElementById("tableau").rows[i].cells;
        x[1].innerHTML = degEff[i-1];
        x[2].innerHTML = degBonne[i-1];
    }
}

