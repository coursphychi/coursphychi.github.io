/* eslint-env es6 */
/* eslint-env browser */

let canvas = document.getElementById('myCanvas');
let ctx = canvas.getContext('2d');

let color1 = [255, 100, 78];
let color2 = [255, 217, 50];
let color3 = [0, 162, 255];

let freq = 0.2;

function interpolateColor(color1, color2, ratio) {

return [Math.round(ratio*color1[0] + (1-ratio) * color2[0]), Math.round(ratio*color1[1] + (1-ratio) * color2[1]), Math.round(ratio*color1[2] + (1-ratio) * color2[2])];
}



function drawCircle(color) {
ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
ctx.beginPath();
ctx.arc(canvas.width / 2, canvas.height / 2, 150, 2 * Math.PI, false);
ctx.fillStyle = 'rgb(' + color[0] + ',' + color[1] + ',' + color[2] + ')';
ctx.fill();
}

function animate() {
let now = Date.now() / 1000;
let ratio = Math.cos(2 * Math.PI * freq * now);
let color;
if (ratio < 0) {
// First half of the cycle: interpolate between color1 and color2
ratio = -ratio;
color = interpolateColor(color1, color2, ratio);
} else {
// Second half of the cycle: interpolate between color2 and color3
color = interpolateColor(color2, color3, 1-ratio);
}

drawCircle(color);
    
requestAnimationFrame(animate);
}

animate();