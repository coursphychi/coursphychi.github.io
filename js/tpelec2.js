/* eslint-env es6 */
/* eslint-env browser */
/* exported prepareData, updateGraph, showRegression */
/* global Chart */ 

// Déclarations de variables
let theta = [];
let R = [];
let chart;

// Configuration pour le graphique
let config = {
type: 'scatter',
data: {
datasets: [{
//label: 'Courbe d\'étalonnage de la thermistance',
data: theta.map((value, index) => ({ x: value, y: R[index] })),
backgroundColor: '#599DFF',
showLine: false
}, {
//label: 'Ligne de liaison',
data: theta.map((value, index) => ({ x: value, y: R[index] })),
borderColor: 'red',
backgroundColor: 'transparent',
showLine: true,
fill: false,
pointRadius: 0,
borderWidth: 2,
borderDash: [5, 5]
}]
},
options: {
responsive: true,
devicePixelRatio: 3,
scales: {
x: {
title: {
display: true,
text: 'θ (°C)',
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
text: 'R (Ω)',
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
title: {
display: true,
text: "Courbe d'étalonnage de la thermistance",
font: {
size: 16
},
color: 'white'
},
legend: {
display: false
}
}
}
};

// Fonction pour préparer les données
function prepareData() {
theta = document.getElementById('inputtheta').value.split(',').map(Number);
R = document.getElementById('inputR').value.split(',').map(Number);

if (theta.length !== R.length) {
document.getElementById('validationMessage').innerHTML = "Il faut autant de valeurs<br>dans chaque champ !";
return;
}

// Masquer le message et afficher le bouton de mise à jour
document.getElementById('validationMessage').style.display = 'none';
document.querySelector('.update-button').style.display = 'block';

// Masquer le bouton de traçage du graphique
document.querySelector('.custom-button').style.display = 'none';

const newData = theta.map((value, index) => ({ x: value, y: R[index] }));

// Si le graphique n'a pas été créé
if (!chart) {
let ctx = document.getElementById('chart').getContext('2d');

// Mettre à jour le dataset avant de créer le graphique
config.data.datasets[0].data = newData;
config.data.datasets[1].data = newData;

chart = new Chart(ctx, config);
} else {
updateGraph();
}
}

// Fonction pour mettre à jour le graphique
function updateGraph() {
theta = document.getElementById('inputtheta').value.split(',').map(Number);
R = document.getElementById('inputR').value.split(',').map(Number);

if (theta.length !== R.length) {
document.getElementById('validationMessage').innerHTML = "Il faut autant de valeurs<br>dans chaque champ !";
document.getElementById('validationMessage').style.display = 'block';
return;
}

const newData = theta.map((value, index) => ({ x: value, y: R[index] }));

// Mise à jour du dataset des points
chart.data.datasets[0].data = newData;

// Mise à jour du dataset de la courbe de liaison
chart.data.datasets[1].data = newData;

// Force une mise à jour de l'échelle
chart.options.scales.y.min = Math.min(...R) - 50; // Pour donner une petite marge
chart.options.scales.y.max = Math.max(...R) + 50; // Pour donner une petite marge

chart.update();
}