/* eslint-env es6 */
/* eslint-env browser */
/* exported prepareData, updateGraph, showRegression */
/* global Chart */ 

let A = [];
let C = [];
let coeff = 0;
let chart;

function prepareData() {
  A = document.getElementById('inputA').value.split(',').map(Number);
  C = document.getElementById('inputC').value.split(',').map(value => Number(value) / 1000);

  // Masquer le message et afficher le bouton de mise à jour
  document.getElementById('validationMessage').style.display = 'none';
  document.querySelector('.update-button').style.display = 'block';

  // Masquer le bouton de traçage du graphique
  document.querySelector('.custom-button').style.display = 'none';

  // Calcul du coefficient de la courbe de tendance
  coeff = calculateRegressionCoefficient();

  // Configuration initiale du graphique
  let config = {
    type: 'scatter',
    data: {
      datasets: [{
        label: 'Évolution de A en fonction de C',
        data: C.map((value, index) => ({ x: value, y: A[index] })),
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
            text: 'C (mmol/L)',
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
            text: 'A',
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
          },
        },
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

function formatScientificNotation(coeff) {
  const exponent = Math.floor(Math.log10(coeff));
  const mantissa = coeff / Math.pow(10, exponent);
  return `${mantissa.toFixed(2).replace('.', ',')}.10${convertToSuperscript(exponent)}`;
}

function convertToSuperscript(number) {
  const superscriptDigits = {
    '0': '⁰',
    '1': '¹',
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵',
    '6': '⁶',
    '7': '⁷',
    '8': '⁸',
    '9': '⁹',
    '-': '⁻'
  };
  return number.toString().split('').map(digit => superscriptDigits[digit]).join('');
}

function calculateRegressionCoefficient() {
  let sumAC = 0;
  let sumC2 = 0;
  for (let I = 0; I < A.length; I++) {
    sumAC += A[I] * C[I];
    sumC2 += C[I] * C[I];
  }
  return sumAC / sumC2;
}

function generateIntermediatePoints() {
  const minC = Math.min(...C);
  const maxC = Math.max(...C);
  const step = (maxC - minC) / 100;
  let points = [];
  for (let i = minC; i <= maxC; i += step) {
    points.push(i);
  }
  return points;
}

function updateGraph() {
  // Mise à jour des données
  A = document.getElementById('inputA').value.split(',').map(Number);
  C = document.getElementById('inputC').value.split(',').map(value => Number(value) / 1000);

  // Recalcul du coefficient de la courbe de tendance
  coeff = calculateRegressionCoefficient();

  // Mise à jour du dataset du graphique
  chart.data.datasets[0].data = C.map((value, index) => ({ x: value, y: A[index] }));

  // Mise à jour du dataset du graphique pour la régression linéaire
  const regressionData = generateIntermediatePoints().map(value => ({ x: value, y: coeff * value }));
  if (chart.data.datasets.length > 1) {
    chart.data.datasets[1].data = regressionData;
    chart.data.datasets[1].label = `Régression linéaire (A = ${formatScientificNotation(coeff)}×C)`;
  } else {
    chart.data.datasets.push({
      label: `Régression linéaire (A = ${formatScientificNotation(coeff)}×C)`,
      data: regressionData,
      type: 'line',
      borderColor: '#FF7D74',
      fill: false,
      pointRadius: 0 // Make points invisible
    });
  }

  chart.update();
}

function showRegression() {
  const regressionData = generateIntermediatePoints().map(I => ({ x: I, y: coeff * I }));

  chart.data.datasets.push({
    label: `Régression linéaire (A = ${formatScientificNotation(coeff)}×C)`,
    data: regressionData,
    type: 'line',
    borderColor: '#FF7D74',
    fill: false,
    pointRadius: 0 // Make points invisible
  });

  chart.update();
  document.getElementById('regressionButton').style.display = 'none';
}