---
title: "Deux plans puis un troisième"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
hidden: true
---


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

details > summary:first-of-type {
  display: list-item;    
  cursor: pointer;       
}

details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
</style>





# Deux plans puis un troisième (CCINP)


On considère deux plans métalliques parfaits parallèles entre eux et situés en $x=0$ et $x=a$. 
Une onde électromagnétique se propage entre ces deux plan, le milieu étant assimilé au vide. Le champ électrique de l’onde est donné par :

$$\vec{\underline{E}}=E_0 \sin \left(\frac{n \pi x}{a}\right) \exp (i(\omega t-k z)) \overrightarrow{u_y}$$

<ol>
<li>Déterminer le champ magnétique associé à cette onde.</li>
<li>Quelle équation $\vec{\underline{E}}$ vérifie-t-il ? Déterminer la relation de dispersion reliant $k$ et $\omega$.</li>
<li>On ferme le guide par une paroi parfaitement conductrice en $z=L$, ce qui produit une onde réfléchie.</li>
<ol type="a">
<li>Donner la forme du champ électrique réfléchi et déterminer précisément ce champ réfléchi en utilisant les conditions aux limites sur la paroi réfléchissante.</li>
<li>Montrer que l’onde résultante est stationnaire</li>
</ol>
</ol>



<div class="phys-container">
<div class="ui-panel">
<!---<div class="header">MODE $TE_{n0}$</div>-->
<div class="control-group">
<label>Largeur <b>a</b> : <span id="aVal"></span> cm</label>
<input id="aInput" type="range" min="2" max="25" step="0.1" value="10">
</div>
<div class="control-group">
<label>Mode <b>n</b> : <span id="nVal"></span></label>
<input id="nInput" type="range" min="1" max="5" step="1" value="1">
</div>
<div class="control-group">
<label style="display: flex; align-items: center; gap: 8px; cursor: pointer;">
<input id="wallToggle" type="checkbox" unchecked> Paroi physique en $z=0$
</label>
</div>
<div class="stats">
<div id="fDisplay">f = 3.00 GHz</div>
<div id="fcDisplay">fc = -- GHz</div>
<div id="status" class="status-badge"></div>
</div>
</div>
<canvas id="renderCanvas"></canvas>
</div>

<style>
.phys-container { position: relative; width: 100%; height: 550px; background: #0f172a; border-radius: 12px; overflow: hidden; font-family: system-ui, -apple-system, sans-serif; }
.ui-panel { position: absolute; top: 15px; left: 15px; width: 220px; z-index: 10; background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(8px); padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1); color: white; }
.header { font-weight: bold; font-size: 14px; margin-bottom: 12px; color: #00d4ff; letter-spacing: 0.5px; }
.control-group { margin-bottom: 12px; }
label { display: block; font-size: 12px; margin-bottom: 4px; opacity: 0.8; }
input[type="range"] { width: 100%; cursor: pointer; }
.stats { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px; font-size: 13px; line-height: 1.5; }
.status-badge { display: inline-block; margin-top: 6px; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px; text-transform: uppercase; }
.propagative { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #4ade80; }
.evanescent { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #f87171; }
#renderCanvas { width: 100%; height: 100%; display: block; }
</style>

<script type="module">
import * as THREE from "https://esm.sh/three@0.160.0";
import { OrbitControls } from "https://esm.sh/three@0.160.0/examples/jsm/controls/OrbitControls.js";

const canvas = document.getElementById('renderCanvas');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0f172a);

const camera = new THREE.PerspectiveCamera(45, canvas.clientWidth / canvas.clientHeight, 0.01, 100);
camera.position.set(0.9, 0.7, 1.3);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// --- SHADERS ---
const vertexShader = `
varying float vAmp;
uniform float uTime, uA, uN, uKz, uAlpha, uIsEvanescent, uWallZ;
void main() {
vec3 p = position;
float x = (p.x + 0.5) * uA;
float z = (0.5 - p.y) * 1.0; // Direction de propagation

float spatialX = sin(uN * 3.14159265 * x / uA);
float field = 0.0;
float omegaT = 6.28318 * 0.5 * uTime;

if(uIsEvanescent < 0.5) {
if(uWallZ > 0.5) {
// RÉGIME STATIONNAIRE : superposition onde incidente/réfléchie
// E = E0 * sin(kx*x) * sin(kz*z) * cos(wt)
field = 2.0 * spatialX * sin(uKz * z) * cos(omegaT);
} else {
// RÉGIME PROGRESSIF : E = E0 * sin(kx*x) * sin(wt - kz*z)
field = spatialX * sin(omegaT - uKz * z);
}
} else {
// RÉGIME ÉVANESCENT
field = spatialX * exp(-uAlpha * z) * sin(omegaT);
}

p.z = field * 0.15;
vAmp = field;
gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
}
`;

const fragmentShader = `
varying float vAmp;
uniform vec3 uColor;
void main() {
gl_FragColor = vec4(mix(vec3(0.05, 0.1, 0.2), uColor, abs(vAmp)), 0.8);
}
`;

const waveMaterial = new THREE.ShaderMaterial({
uniforms: {
uTime: { value: 0 }, uA: { value: 0.1 }, uN: { value: 1.0 },
uKz: { value: 0.0 }, uAlpha: { value: 0.0 }, uIsEvanescent: { value: 0.0 },
uWallZ: { value: 1.0 }, uColor: { value: new THREE.Color(0x00d4ff) }
},
vertexShader, fragmentShader, transparent: true, side: THREE.DoubleSide
});

const mesh = new THREE.Mesh(new THREE.PlaneGeometry(1, 1, 100, 250), waveMaterial);
mesh.rotation.x = -Math.PI / 2;
scene.add(mesh);

// Parois
const wallMat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.15, side: THREE.DoubleSide, depthWrite: false });
const wallX0 = new THREE.Mesh(new THREE.PlaneGeometry(1, 0.4), wallMat);
const wallXa = new THREE.Mesh(new THREE.PlaneGeometry(1, 0.4), wallMat);
const wallZ0 = new THREE.Mesh(new THREE.PlaneGeometry(1, 0.4), wallMat);
wallX0.rotation.y = wallXa.rotation.y = Math.PI / 2;
scene.add(wallX0, wallXa, wallZ0);

function update() {
const a = parseFloat(document.getElementById('aInput').value) / 100;
const n = parseInt(document.getElementById('nInput').value);
const wallActive = document.getElementById('wallToggle').checked;

const f = 3e9, c = 299792458;
const fc = (n * c) / (2 * a), isE = f < fc;
const k0 = (2 * Math.PI * f) / c, kc = (n * Math.PI) / a;

waveMaterial.uniforms.uIsEvanescent.value = isE ? 1.0 : 0.0;
waveMaterial.uniforms.uWallZ.value = wallActive ? 1.0 : 0.0;

if (!isE) {
waveMaterial.uniforms.uKz.value = Math.sqrt(k0*k0 - kc*kc);
waveMaterial.uniforms.uColor.value.set(wallActive ? 0xffcc00 : 0x00d4ff); // Jaune pour stationnaire
} else {
waveMaterial.uniforms.uAlpha.value = Math.sqrt(kc*kc - k0*k0);
waveMaterial.uniforms.uColor.value.set(0xff4444);
}

waveMaterial.uniforms.uA.value = a;
waveMaterial.uniforms.uN.value = n;

const visualWidth = a * 4;
mesh.scale.set(visualWidth, 1, 1);
wallX0.position.set(-visualWidth/2, 0, 0);
wallXa.position.set(visualWidth/2, 0, 0);
wallZ0.position.set(0, 0, 0.5);
wallZ0.scale.x = visualWidth;
wallZ0.visible = wallActive;

document.getElementById('aVal').textContent = (a * 100).toFixed(1);
document.getElementById('nVal').textContent = n;
document.getElementById('fcDisplay').textContent = "fc = " + (fc / 1e9).toFixed(2) + " GHz";
const status = document.getElementById('status');
status.textContent = isE ? "Évanescent" : (wallActive ? "Stationnaire" : "Propagatif");
status.className = "status-badge " + (isE ? "evanescent" : "propagative");
}

document.getElementById('aInput').oninput = update;
document.getElementById('nInput').oninput = update;
document.getElementById('wallToggle').onchange = update;

function animate(t) {
requestAnimationFrame(animate);
const w = canvas.clientWidth, h = canvas.clientHeight;
if (canvas.width !== w || canvas.height !== h) {
renderer.setSize(w, h, false);
camera.aspect = w / h;
camera.updateProjectionMatrix();
}
waveMaterial.uniforms.uTime.value = t / 1000;
controls.update();
renderer.render(scene, camera);
}

update();
animate(0);
</script>