/* eslint-env es6 */
/* eslint-env browser */
/* exported prepareData, updateGraph, showRegression */
/* global Chart */ 

let U = [];
let I = [];
let coeff = 0;
let chart;

function prepareData() {
U = document.getElementById('inputU').value.split(',').map(Number);
I = document.getElementById('inputI').value.split(',').map(value => Number(value) / 1000);


// Masquer le message et afficher le bouton de mise à jour
document.getElementById('validationMessage').style.display = 'none';
document.querySelector('.update-button').style.display = 'block';

// Masquer le bouton de traçage du graphique
document.querySelector('.custom-button').style.display = 'none';

// Calcul du coefficient de la courbe de tendance
let sumUI = 0;
let sumI2 = 0;
for (let i = 0; i < U.length; i++) {
sumUI += U[i] * I[i];
sumI2 += I[i] * I[i];
}
coeff = sumUI / sumI2;

// Configuration initiale du graphique
let config = {
type: 'scatter',
data: {
datasets: [{
label: 'Caractéristique de la thermistance',
data: I.map((value, index) => ({ x: value, y: U[index] })),
backgroundColor: '#599DFF'
}]
},
options: {
responsive: true,
devicePixelRatio: 3,
scales: {
x: {
title: {
display: true,
text: 'I (A)',
color: 'white'
},
grid: {
color: 'rgba(255, 255, 255, 0.3)'
},
ticks: {
color: 'white'
}
},
y: {
title: {
display: true,
text: 'U (V)',
color: 'white'
},
grid: {
color: 'rgba(255, 255, 255, 0.1)'
},
ticks: {
color: 'white'
}
}
},
plugins: {
legend: {
labels: {
color: 'white',
font: {
     size: 18
      }
}
}
}
}
};

// Création du graphique si ce n'est pas déjà fait
if (!chart) {
let ctx = document.getElementById('chart').getContext('2d');
chart = new Chart(ctx, config);
}


document.getElementById('regressionButton').style.display = 'block';
}


function calculateRegressionCoefficient() {
let sumUI = 0;
let sumI2 = 0;
for (let i = 0; i < U.length; i++) {
sumUI += U[i] * I[i];
sumI2 += I[i] * I[i];
}
return sumUI / sumI2;
}

function updateGraph() {
// Mise à jour des données
U = document.getElementById('inputU').value.split(',').map(Number);
I = document.getElementById('inputI').value.split(',').map(value => Number(value) / 1000);


// Recalcul du coefficient de la courbe de tendance
coeff = calculateRegressionCoefficient();

// Mise à jour du dataset du graphique
chart.data.datasets[0].data = I.map((value, index) => ({ x: value, y: U[index] }));

// Mise à jour du dataset du graphique pour la régression linéaire
if (chart.data.datasets.length > 1) {
chart.data.datasets[1].data = I.map(i => ({ x: i, y: coeff * i }));
chart.data.datasets[1].label = `Régression linéaire (y = ${coeff.toFixed(0)}x)`;
}

chart.update();
}


function showRegression() {
let regressionData = I.map(i => ({ x: i, y: coeff * i }));

chart.data.datasets.push({
label: `Régression linéaire (y = ${coeff.toFixed(0)}x)`,
data: regressionData,
type: 'line',
borderColor: '#FF7D74',
fill: false
});

chart.update();
document.getElementById('regressionButton').style.display = 'none';
}