+++
title = "Intensité sonore"
draft = false
hidden = true
+++

<link rel="stylesheet" href="/css/cours.css">
<script src="/js/cours.js" defer></script>

<div class="nt-quizbar">
<button type="button" class="nt-btn nt-quiz-toggle" aria-pressed="false"><i class="fa-solid fa-eye-slash"></i>&nbsp; Mode révision</button>
<p>Le mode révision masque les mots-clés&nbsp;: essayez de les retrouver de mémoire, puis cliquez dessus pour vérifier.</p>
</div>

## Rappels {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Une onde est caractérisée par <span class="imp nt-hole">un transport d'énergie et d'information sans transport de matière</span>.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-cubes"></i>Onde mécanique</p>
<p>L'onde sonore est une onde <span class="imp nt-hole">mécanique</span> car elle nécessite un <span class="imp nt-hole">milieu matériel</span> pour se propager.</p>
</div>
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-arrows-left-right"></i>Onde longitudinale</p>
<p>L'onde sonore est une onde <span class="imp nt-hole">longitudinale</span> car la perturbation se fait <span class="imp nt-hole">dans la même direction</span> que sa propagation.</p>
</div>
</div>

<div class="nt-lab" id="lab-onde">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Une onde sonore, vue de près</p>
<canvas style="height:230px;" aria-label="Animation : des particules d'air oscillent autour de leur position de repos pendant que l'onde se propage vers la droite"></canvas>
<div class="nt-ctrls">
<label class="nt-ctrl">Amplitude <input type="range" data-p="amp" min="1" max="12" step="0.5" value="7"></label>
<label class="nt-ctrl">Fréquence <input type="range" data-p="freq" min="0.3" max="1.6" step="0.05" value="0.7"></label>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="play"><i class="fa-solid fa-pause"></i>&nbsp; Pause</button></div>
<p class="nt-msg">La particule rose oscille autour de sa position de repos (pointillés) sans avancer avec l'onde. Là où les particules se resserrent, l'air est comprimé&nbsp;; là où elles s'écartent, il est dilaté.</p>
</div>

<p class="nt-lead">Un son musical est un signal <span class="imp nt-hole">périodique</span> caractérisé par&nbsp;:</p>

<div class="nt-grid3">
<div class="nt-feat" style="--f: var(--c-haut);">
<p class="nt-feat-title"><i class="fa-solid fa-music"></i>&nbsp; sa hauteur</p>
<p>liée à <span class="nt-feat-key nt-hole">la fréquence</span> du signal</p>
<svg class="nt-wave" viewBox="0 0 200 70" role="img" aria-label="Deux signaux de même amplitude, le second de fréquence double"><line x1="0" y1="35" x2="200" y2="35" stroke="var(--line)"/><polyline points="0.0,35.0 1.0,34.1 2.0,33.2 3.0,32.4 4.0,31.5 5.0,30.7 6.0,29.8 7.0,29.0 8.0,28.3 9.0,27.5 10.0,26.8 11.0,26.1 12.0,25.4 13.0,24.8 14.0,24.2 15.0,23.7 16.0,23.2 17.0,22.7 18.0,22.3 19.0,22.0 20.0,21.7 21.0,21.4 22.0,21.2 23.0,21.1 24.0,21.0 25.0,21.0 26.0,21.0 27.0,21.1 28.0,21.2 29.0,21.4 30.0,21.7 31.0,22.0 32.0,22.3 33.0,22.7 34.0,23.2 35.0,23.7 36.0,24.2 37.0,24.8 38.0,25.4 39.0,26.1 40.0,26.8 41.0,27.5 42.0,28.3 43.0,29.0 44.0,29.8 45.0,30.7 46.0,31.5 47.0,32.4 48.0,33.2 49.0,34.1 50.0,35.0 51.0,35.9 52.0,36.8 53.0,37.6 54.0,38.5 55.0,39.3 56.0,40.2 57.0,41.0 58.0,41.7 59.0,42.5 60.0,43.2 61.0,43.9 62.0,44.6 63.0,45.2 64.0,45.8 65.0,46.3 66.0,46.8 67.0,47.3 68.0,47.7 69.0,48.0 70.0,48.3 71.0,48.6 72.0,48.8 73.0,48.9 74.0,49.0 75.0,49.0 76.0,49.0 77.0,48.9 78.0,48.8 79.0,48.6 80.0,48.3 81.0,48.0 82.0,47.7 83.0,47.3 84.0,46.8 85.0,46.3 86.0,45.8 87.0,45.2 88.0,44.6 89.0,43.9 90.0,43.2 91.0,42.5 92.0,41.7 93.0,41.0 94.0,40.2 95.0,39.3 96.0,38.5 97.0,37.6 98.0,36.8 99.0,35.9 100.0,35.0 101.0,34.1 102.0,33.2 103.0,32.4 104.0,31.5 105.0,30.7 106.0,29.8 107.0,29.0 108.0,28.3 109.0,27.5 110.0,26.8 111.0,26.1 112.0,25.4 113.0,24.8 114.0,24.2 115.0,23.7 116.0,23.2 117.0,22.7 118.0,22.3 119.0,22.0 120.0,21.7 121.0,21.4 122.0,21.2 123.0,21.1 124.0,21.0 125.0,21.0 126.0,21.0 127.0,21.1 128.0,21.2 129.0,21.4 130.0,21.7 131.0,22.0 132.0,22.3 133.0,22.7 134.0,23.2 135.0,23.7 136.0,24.2 137.0,24.8 138.0,25.4 139.0,26.1 140.0,26.8 141.0,27.5 142.0,28.3 143.0,29.0 144.0,29.8 145.0,30.7 146.0,31.5 147.0,32.4 148.0,33.2 149.0,34.1 150.0,35.0 151.0,35.9 152.0,36.8 153.0,37.6 154.0,38.5 155.0,39.3 156.0,40.2 157.0,41.0 158.0,41.7 159.0,42.5 160.0,43.2 161.0,43.9 162.0,44.6 163.0,45.2 164.0,45.8 165.0,46.3 166.0,46.8 167.0,47.3 168.0,47.7 169.0,48.0 170.0,48.3 171.0,48.6 172.0,48.8 173.0,48.9 174.0,49.0 175.0,49.0 176.0,49.0 177.0,48.9 178.0,48.8 179.0,48.6 180.0,48.3 181.0,48.0 182.0,47.7 183.0,47.3 184.0,46.8 185.0,46.3 186.0,45.8 187.0,45.2 188.0,44.6 189.0,43.9 190.0,43.2 191.0,42.5 192.0,41.7 193.0,41.0 194.0,40.2 195.0,39.3 196.0,38.5 197.0,37.6 198.0,36.8 199.0,35.9 200.0,35.0" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="0.0,35.0 1.0,33.2 2.0,31.5 3.0,29.8 4.0,28.3 5.0,26.8 6.0,25.4 7.0,24.2 8.0,23.2 9.0,22.3 10.0,21.7 11.0,21.2 12.0,21.0 13.0,21.0 14.0,21.2 15.0,21.7 16.0,22.3 17.0,23.2 18.0,24.2 19.0,25.4 20.0,26.8 21.0,28.3 22.0,29.8 23.0,31.5 24.0,33.2 25.0,35.0 26.0,36.8 27.0,38.5 28.0,40.2 29.0,41.7 30.0,43.2 31.0,44.6 32.0,45.8 33.0,46.8 34.0,47.7 35.0,48.3 36.0,48.8 37.0,49.0 38.0,49.0 39.0,48.8 40.0,48.3 41.0,47.7 42.0,46.8 43.0,45.8 44.0,44.6 45.0,43.2 46.0,41.7 47.0,40.2 48.0,38.5 49.0,36.8 50.0,35.0 51.0,33.2 52.0,31.5 53.0,29.8 54.0,28.3 55.0,26.8 56.0,25.4 57.0,24.2 58.0,23.2 59.0,22.3 60.0,21.7 61.0,21.2 62.0,21.0 63.0,21.0 64.0,21.2 65.0,21.7 66.0,22.3 67.0,23.2 68.0,24.2 69.0,25.4 70.0,26.8 71.0,28.3 72.0,29.8 73.0,31.5 74.0,33.2 75.0,35.0 76.0,36.8 77.0,38.5 78.0,40.2 79.0,41.7 80.0,43.2 81.0,44.6 82.0,45.8 83.0,46.8 84.0,47.7 85.0,48.3 86.0,48.8 87.0,49.0 88.0,49.0 89.0,48.8 90.0,48.3 91.0,47.7 92.0,46.8 93.0,45.8 94.0,44.6 95.0,43.2 96.0,41.7 97.0,40.2 98.0,38.5 99.0,36.8 100.0,35.0 101.0,33.2 102.0,31.5 103.0,29.8 104.0,28.3 105.0,26.8 106.0,25.4 107.0,24.2 108.0,23.2 109.0,22.3 110.0,21.7 111.0,21.2 112.0,21.0 113.0,21.0 114.0,21.2 115.0,21.7 116.0,22.3 117.0,23.2 118.0,24.2 119.0,25.4 120.0,26.8 121.0,28.3 122.0,29.8 123.0,31.5 124.0,33.2 125.0,35.0 126.0,36.8 127.0,38.5 128.0,40.2 129.0,41.7 130.0,43.2 131.0,44.6 132.0,45.8 133.0,46.8 134.0,47.7 135.0,48.3 136.0,48.8 137.0,49.0 138.0,49.0 139.0,48.8 140.0,48.3 141.0,47.7 142.0,46.8 143.0,45.8 144.0,44.6 145.0,43.2 146.0,41.7 147.0,40.2 148.0,38.5 149.0,36.8 150.0,35.0 151.0,33.2 152.0,31.5 153.0,29.8 154.0,28.3 155.0,26.8 156.0,25.4 157.0,24.2 158.0,23.2 159.0,22.3 160.0,21.7 161.0,21.2 162.0,21.0 163.0,21.0 164.0,21.2 165.0,21.7 166.0,22.3 167.0,23.2 168.0,24.2 169.0,25.4 170.0,26.8 171.0,28.3 172.0,29.8 173.0,31.5 174.0,33.2 175.0,35.0 176.0,36.8 177.0,38.5 178.0,40.2 179.0,41.7 180.0,43.2 181.0,44.6 182.0,45.8 183.0,46.8 184.0,47.7 185.0,48.3 186.0,48.8 187.0,49.0 188.0,49.0 189.0,48.8 190.0,48.3 191.0,47.7 192.0,46.8 193.0,45.8 194.0,44.6 195.0,43.2 196.0,41.7 197.0,40.2 198.0,38.5 199.0,36.8 200.0,35.0" fill="none" stroke="var(--f)" stroke-width="2.6" stroke-linejoin="round"/></svg>
<p class="nt-note">Fréquence doublée&nbsp;: son plus aigu.</p>
</div>
<div class="nt-feat" style="--f: var(--c-int);">
<p class="nt-feat-title"><i class="fa-solid fa-volume-high"></i>&nbsp; son intensité</p>
<p>liée à <span class="nt-feat-key nt-hole">l'amplitude</span> du signal</p>
<svg class="nt-wave" viewBox="0 0 200 70" role="img" aria-label="Deux signaux de même fréquence, le second d'amplitude plus grande"><line x1="0" y1="35" x2="200" y2="35" stroke="var(--line)"/><polyline points="0.0,35.0 1.0,34.3 2.0,33.6 3.0,32.9 4.0,32.3 5.0,31.6 6.0,31.0 7.0,30.3 8.0,29.7 9.0,29.1 10.0,28.5 11.0,28.0 12.0,27.5 13.0,27.0 14.0,26.5 15.0,26.1 16.0,25.7 17.0,25.4 18.0,25.0 19.0,24.8 20.0,24.5 21.0,24.3 22.0,24.2 23.0,24.1 24.0,24.0 25.0,24.0 26.0,24.0 27.0,24.1 28.0,24.2 29.0,24.3 30.0,24.5 31.0,24.8 32.0,25.0 33.0,25.4 34.0,25.7 35.0,26.1 36.0,26.5 37.0,27.0 38.0,27.5 39.0,28.0 40.0,28.5 41.0,29.1 42.0,29.7 43.0,30.3 44.0,31.0 45.0,31.6 46.0,32.3 47.0,32.9 48.0,33.6 49.0,34.3 50.0,35.0 51.0,35.7 52.0,36.4 53.0,37.1 54.0,37.7 55.0,38.4 56.0,39.0 57.0,39.7 58.0,40.3 59.0,40.9 60.0,41.5 61.0,42.0 62.0,42.5 63.0,43.0 64.0,43.5 65.0,43.9 66.0,44.3 67.0,44.6 68.0,45.0 69.0,45.2 70.0,45.5 71.0,45.7 72.0,45.8 73.0,45.9 74.0,46.0 75.0,46.0 76.0,46.0 77.0,45.9 78.0,45.8 79.0,45.7 80.0,45.5 81.0,45.2 82.0,45.0 83.0,44.6 84.0,44.3 85.0,43.9 86.0,43.5 87.0,43.0 88.0,42.5 89.0,42.0 90.0,41.5 91.0,40.9 92.0,40.3 93.0,39.7 94.0,39.0 95.0,38.4 96.0,37.7 97.0,37.1 98.0,36.4 99.0,35.7 100.0,35.0 101.0,34.3 102.0,33.6 103.0,32.9 104.0,32.3 105.0,31.6 106.0,31.0 107.0,30.3 108.0,29.7 109.0,29.1 110.0,28.5 111.0,28.0 112.0,27.5 113.0,27.0 114.0,26.5 115.0,26.1 116.0,25.7 117.0,25.4 118.0,25.0 119.0,24.8 120.0,24.5 121.0,24.3 122.0,24.2 123.0,24.1 124.0,24.0 125.0,24.0 126.0,24.0 127.0,24.1 128.0,24.2 129.0,24.3 130.0,24.5 131.0,24.8 132.0,25.0 133.0,25.4 134.0,25.7 135.0,26.1 136.0,26.5 137.0,27.0 138.0,27.5 139.0,28.0 140.0,28.5 141.0,29.1 142.0,29.7 143.0,30.3 144.0,31.0 145.0,31.6 146.0,32.3 147.0,32.9 148.0,33.6 149.0,34.3 150.0,35.0 151.0,35.7 152.0,36.4 153.0,37.1 154.0,37.7 155.0,38.4 156.0,39.0 157.0,39.7 158.0,40.3 159.0,40.9 160.0,41.5 161.0,42.0 162.0,42.5 163.0,43.0 164.0,43.5 165.0,43.9 166.0,44.3 167.0,44.6 168.0,45.0 169.0,45.2 170.0,45.5 171.0,45.7 172.0,45.8 173.0,45.9 174.0,46.0 175.0,46.0 176.0,46.0 177.0,45.9 178.0,45.8 179.0,45.7 180.0,45.5 181.0,45.2 182.0,45.0 183.0,44.6 184.0,44.3 185.0,43.9 186.0,43.5 187.0,43.0 188.0,42.5 189.0,42.0 190.0,41.5 191.0,40.9 192.0,40.3 193.0,39.7 194.0,39.0 195.0,38.4 196.0,37.7 197.0,37.1 198.0,36.4 199.0,35.7 200.0,35.0" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="0.0,35.0 1.0,33.2 2.0,31.5 3.0,29.8 4.0,28.0 5.0,26.3 6.0,24.7 7.0,23.1 8.0,21.5 9.0,20.0 10.0,18.5 11.0,17.2 12.0,15.8 13.0,14.6 14.0,13.4 15.0,12.3 16.0,11.4 17.0,10.5 18.0,9.7 19.0,9.0 20.0,8.4 21.0,7.9 22.0,7.5 23.0,7.2 24.0,7.1 25.0,7.0 26.0,7.1 27.0,7.2 28.0,7.5 29.0,7.9 30.0,8.4 31.0,9.0 32.0,9.7 33.0,10.5 34.0,11.4 35.0,12.3 36.0,13.4 37.0,14.6 38.0,15.8 39.0,17.2 40.0,18.5 41.0,20.0 42.0,21.5 43.0,23.1 44.0,24.7 45.0,26.3 46.0,28.0 47.0,29.8 48.0,31.5 49.0,33.2 50.0,35.0 51.0,36.8 52.0,38.5 53.0,40.2 54.0,42.0 55.0,43.7 56.0,45.3 57.0,46.9 58.0,48.5 59.0,50.0 60.0,51.5 61.0,52.8 62.0,54.2 63.0,55.4 64.0,56.6 65.0,57.7 66.0,58.6 67.0,59.5 68.0,60.3 69.0,61.0 70.0,61.6 71.0,62.1 72.0,62.5 73.0,62.8 74.0,62.9 75.0,63.0 76.0,62.9 77.0,62.8 78.0,62.5 79.0,62.1 80.0,61.6 81.0,61.0 82.0,60.3 83.0,59.5 84.0,58.6 85.0,57.7 86.0,56.6 87.0,55.4 88.0,54.2 89.0,52.8 90.0,51.5 91.0,50.0 92.0,48.5 93.0,46.9 94.0,45.3 95.0,43.7 96.0,42.0 97.0,40.2 98.0,38.5 99.0,36.8 100.0,35.0 101.0,33.2 102.0,31.5 103.0,29.8 104.0,28.0 105.0,26.3 106.0,24.7 107.0,23.1 108.0,21.5 109.0,20.0 110.0,18.5 111.0,17.2 112.0,15.8 113.0,14.6 114.0,13.4 115.0,12.3 116.0,11.4 117.0,10.5 118.0,9.7 119.0,9.0 120.0,8.4 121.0,7.9 122.0,7.5 123.0,7.2 124.0,7.1 125.0,7.0 126.0,7.1 127.0,7.2 128.0,7.5 129.0,7.9 130.0,8.4 131.0,9.0 132.0,9.7 133.0,10.5 134.0,11.4 135.0,12.3 136.0,13.4 137.0,14.6 138.0,15.8 139.0,17.2 140.0,18.5 141.0,20.0 142.0,21.5 143.0,23.1 144.0,24.7 145.0,26.3 146.0,28.0 147.0,29.8 148.0,31.5 149.0,33.2 150.0,35.0 151.0,36.8 152.0,38.5 153.0,40.2 154.0,42.0 155.0,43.7 156.0,45.3 157.0,46.9 158.0,48.5 159.0,50.0 160.0,51.5 161.0,52.8 162.0,54.2 163.0,55.4 164.0,56.6 165.0,57.7 166.0,58.6 167.0,59.5 168.0,60.3 169.0,61.0 170.0,61.6 171.0,62.1 172.0,62.5 173.0,62.8 174.0,62.9 175.0,63.0 176.0,62.9 177.0,62.8 178.0,62.5 179.0,62.1 180.0,61.6 181.0,61.0 182.0,60.3 183.0,59.5 184.0,58.6 185.0,57.7 186.0,56.6 187.0,55.4 188.0,54.2 189.0,52.8 190.0,51.5 191.0,50.0 192.0,48.5 193.0,46.9 194.0,45.3 195.0,43.7 196.0,42.0 197.0,40.2 198.0,38.5 199.0,36.8 200.0,35.0" fill="none" stroke="var(--f)" stroke-width="2.6" stroke-linejoin="round"/></svg>
<p class="nt-note">Amplitude plus grande&nbsp;: son plus fort.</p>
</div>
<div class="nt-feat" style="--f: var(--c-timbre);">
<p class="nt-feat-title"><i class="fa-solid fa-guitar"></i>&nbsp; son timbre</p>
<p>lié au <span class="nt-feat-key nt-hole">spectre</span> du signal</p>
<svg class="nt-wave" viewBox="0 0 200 70" role="img" aria-label="Deux signaux de même période, le second de forme plus complexe"><line x1="0" y1="35" x2="200" y2="35" stroke="var(--line)"/><polyline points="0.0,35.0 1.0,33.7 2.0,32.5 3.0,31.3 4.0,30.0 5.0,28.8 6.0,27.6 7.0,26.5 8.0,25.4 9.0,24.3 10.0,23.2 11.0,22.3 12.0,21.3 13.0,20.4 14.0,19.6 15.0,18.8 16.0,18.1 17.0,17.5 18.0,16.9 19.0,16.4 20.0,16.0 21.0,15.6 22.0,15.4 23.0,15.2 24.0,15.0 25.0,15.0 26.0,15.0 27.0,15.2 28.0,15.4 29.0,15.6 30.0,16.0 31.0,16.4 32.0,16.9 33.0,17.5 34.0,18.1 35.0,18.8 36.0,19.6 37.0,20.4 38.0,21.3 39.0,22.3 40.0,23.2 41.0,24.3 42.0,25.4 43.0,26.5 44.0,27.6 45.0,28.8 46.0,30.0 47.0,31.3 48.0,32.5 49.0,33.7 50.0,35.0 51.0,36.3 52.0,37.5 53.0,38.7 54.0,40.0 55.0,41.2 56.0,42.4 57.0,43.5 58.0,44.6 59.0,45.7 60.0,46.8 61.0,47.7 62.0,48.7 63.0,49.6 64.0,50.4 65.0,51.2 66.0,51.9 67.0,52.5 68.0,53.1 69.0,53.6 70.0,54.0 71.0,54.4 72.0,54.6 73.0,54.8 74.0,55.0 75.0,55.0 76.0,55.0 77.0,54.8 78.0,54.6 79.0,54.4 80.0,54.0 81.0,53.6 82.0,53.1 83.0,52.5 84.0,51.9 85.0,51.2 86.0,50.4 87.0,49.6 88.0,48.7 89.0,47.7 90.0,46.8 91.0,45.7 92.0,44.6 93.0,43.5 94.0,42.4 95.0,41.2 96.0,40.0 97.0,38.7 98.0,37.5 99.0,36.3 100.0,35.0 101.0,33.7 102.0,32.5 103.0,31.3 104.0,30.0 105.0,28.8 106.0,27.6 107.0,26.5 108.0,25.4 109.0,24.3 110.0,23.2 111.0,22.3 112.0,21.3 113.0,20.4 114.0,19.6 115.0,18.8 116.0,18.1 117.0,17.5 118.0,16.9 119.0,16.4 120.0,16.0 121.0,15.6 122.0,15.4 123.0,15.2 124.0,15.0 125.0,15.0 126.0,15.0 127.0,15.2 128.0,15.4 129.0,15.6 130.0,16.0 131.0,16.4 132.0,16.9 133.0,17.5 134.0,18.1 135.0,18.8 136.0,19.6 137.0,20.4 138.0,21.3 139.0,22.3 140.0,23.2 141.0,24.3 142.0,25.4 143.0,26.5 144.0,27.6 145.0,28.8 146.0,30.0 147.0,31.3 148.0,32.5 149.0,33.7 150.0,35.0 151.0,36.3 152.0,37.5 153.0,38.7 154.0,40.0 155.0,41.2 156.0,42.4 157.0,43.5 158.0,44.6 159.0,45.7 160.0,46.8 161.0,47.7 162.0,48.7 163.0,49.6 164.0,50.4 165.0,51.2 166.0,51.9 167.0,52.5 168.0,53.1 169.0,53.6 170.0,54.0 171.0,54.4 172.0,54.6 173.0,54.8 174.0,55.0 175.0,55.0 176.0,55.0 177.0,54.8 178.0,54.6 179.0,54.4 180.0,54.0 181.0,53.6 182.0,53.1 183.0,52.5 184.0,51.9 185.0,51.2 186.0,50.4 187.0,49.6 188.0,48.7 189.0,47.7 190.0,46.8 191.0,45.7 192.0,44.6 193.0,43.5 194.0,42.4 195.0,41.2 196.0,40.0 197.0,38.7 198.0,37.5 199.0,36.3 200.0,35.0" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="0.0,25.4 1.0,23.4 2.0,21.7 3.0,20.2 4.0,19.0 5.0,18.2 6.0,17.6 7.0,17.3 8.0,17.3 9.0,17.5 10.0,18.0 11.0,18.6 12.0,19.3 13.0,20.1 14.0,21.0 15.0,21.9 16.0,22.8 17.0,23.6 18.0,24.4 19.0,25.0 20.0,25.6 21.0,26.0 22.0,26.3 23.0,26.5 24.0,26.6 25.0,26.6 26.0,26.5 27.0,26.3 28.0,26.1 29.0,25.9 30.0,25.7 31.0,25.5 32.0,25.4 33.0,25.3 34.0,25.4 35.0,25.5 36.0,25.8 37.0,26.2 38.0,26.7 39.0,27.2 40.0,27.9 41.0,28.6 42.0,29.4 43.0,30.3 44.0,31.1 45.0,31.9 46.0,32.7 47.0,33.5 48.0,34.2 49.0,34.7 50.0,35.2 51.0,35.6 52.0,35.9 53.0,36.1 54.0,36.2 55.0,36.3 56.0,36.3 57.0,36.2 58.0,36.2 59.0,36.2 60.0,36.2 61.0,36.3 62.0,36.5 63.0,36.9 64.0,37.4 65.0,38.0 66.0,38.9 67.0,39.9 68.0,41.1 69.0,42.4 70.0,44.0 71.0,45.6 72.0,47.3 73.0,49.1 74.0,51.0 75.0,52.8 76.0,54.5 77.0,56.1 78.0,57.6 79.0,58.9 80.0,59.9 81.0,60.6 82.0,61.1 83.0,61.2 84.0,60.9 85.0,60.3 86.0,59.3 87.0,58.0 88.0,56.4 89.0,54.4 90.0,52.2 91.0,49.7 92.0,47.1 93.0,44.3 94.0,41.4 95.0,38.5 96.0,35.7 97.0,32.9 98.0,30.2 99.0,27.7 100.0,25.4 101.0,23.4 102.0,21.7 103.0,20.2 104.0,19.0 105.0,18.2 106.0,17.6 107.0,17.3 108.0,17.3 109.0,17.5 110.0,18.0 111.0,18.6 112.0,19.3 113.0,20.1 114.0,21.0 115.0,21.9 116.0,22.8 117.0,23.6 118.0,24.4 119.0,25.0 120.0,25.6 121.0,26.0 122.0,26.3 123.0,26.5 124.0,26.6 125.0,26.6 126.0,26.5 127.0,26.3 128.0,26.1 129.0,25.9 130.0,25.7 131.0,25.5 132.0,25.4 133.0,25.3 134.0,25.4 135.0,25.5 136.0,25.8 137.0,26.2 138.0,26.7 139.0,27.2 140.0,27.9 141.0,28.6 142.0,29.4 143.0,30.3 144.0,31.1 145.0,31.9 146.0,32.7 147.0,33.5 148.0,34.2 149.0,34.7 150.0,35.2 151.0,35.6 152.0,35.9 153.0,36.1 154.0,36.2 155.0,36.3 156.0,36.3 157.0,36.2 158.0,36.2 159.0,36.2 160.0,36.2 161.0,36.3 162.0,36.5 163.0,36.9 164.0,37.4 165.0,38.0 166.0,38.9 167.0,39.9 168.0,41.1 169.0,42.4 170.0,44.0 171.0,45.6 172.0,47.3 173.0,49.1 174.0,51.0 175.0,52.8 176.0,54.5 177.0,56.1 178.0,57.6 179.0,58.9 180.0,59.9 181.0,60.6 182.0,61.1 183.0,61.2 184.0,60.9 185.0,60.3 186.0,59.3 187.0,58.0 188.0,56.4 189.0,54.4 190.0,52.2 191.0,49.7 192.0,47.1 193.0,44.3 194.0,41.4 195.0,38.5 196.0,35.7 197.0,32.9 198.0,30.2 199.0,27.7 200.0,25.4" fill="none" stroke="var(--f)" stroke-width="2.6" stroke-linejoin="round"/></svg>
<p class="nt-note">Même période, autre forme&nbsp;: même note, autre instrument.</p>
</div>
</div>

<div class="nt-lab" id="lab-son">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Hauteur, intensité, timbre&nbsp;: à vous de régler</p>
<div class="nt-lab-pair">
<figure><canvas class="sig" style="height:190px;" aria-label="Signal sonore sur une durée de 10 ms"></canvas><figcaption>Signal (sur 10&nbsp;ms)</figcaption></figure>
<figure><canvas class="spec" style="height:190px;" aria-label="Spectre du signal"></canvas><figcaption>Spectre</figcaption></figure>
</div>
<div class="nt-ctrls">
<label class="nt-ctrl">Fréquence&nbsp;: <b class="out-f">220 Hz</b><input type="range" data-p="freq" min="0" max="100" step="1" value="33"></label>
<label class="nt-ctrl">Amplitude&nbsp;: <b class="out-a">70 %</b><input type="range" data-p="amp" min="5" max="100" step="1" value="70"></label>
</div>
<div class="nt-ctrl">Timbre (spectres simplifiés)&nbsp;:
<div class="nt-seg" role="radiogroup">
<label><input type="radio" name="timbre-son" value="pur" checked><span>Son pur</span></label>
<label><input type="radio" name="timbre-son" value="flute"><span>Flûte</span></label>
<label><input type="radio" name="timbre-son" value="clarinette"><span>Clarinette</span></label>
<label><input type="radio" name="timbre-son" value="violon"><span>Violon</span></label>
</div>
</div>
<div class="nt-btns"><button type="button" class="nt-btn nt-btn-main" data-act="listen"><i class="fa-solid fa-volume-high"></i>&nbsp; Écouter</button></div>
<p class="nt-msg">Pensez à baisser le volume avant d'écouter.</p>
</div>

## Intensité sonore {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp">intensité sonore $I$</span> (ou intensité acoustique) est la <span class="imp">puissance $P$</span> transportée par l'onde sonore <span class="imp">par unité de surface</span>.</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$I=\frac{P}{S}$$</p>
<div class="nt-f-units"><span>$P$ en <span class="nt-hole">$\pu{W}$</span></span><span>$S$ en <span class="nt-hole">$\pu{m2}$</span></span><span>$I$ en <span class="nt-hole">$\pu{W*m-2}$</span></span></div>
</div>

<svg class="nt-svg nt-svg-s" viewBox="0 0 440 200" role="img" aria-label="Une puissance P traverse une surface S perpendiculaire à la direction de propagation"><defs><linearGradient id="gS" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="var(--blue)" stop-opacity=".55"/><stop offset="1" stop-color="var(--sky)" stop-opacity=".7"/></linearGradient><linearGradient id="gBeam" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="400" y2="0"><stop offset="0" stop-color="var(--blue)" stop-opacity="0"/><stop offset=".45" stop-color="var(--blue)" stop-opacity=".95"/><stop offset="1" stop-color="var(--blue)" stop-opacity=".95"/></linearGradient><marker id="mS" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="var(--blue)"/></marker><marker id="mS2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="var(--blue)" fill-opacity=".35"/></marker></defs><line x1="30" y1="72" x2="404" y2="72" stroke="url(#gBeam)" stroke-width="2.5" marker-end="url(#mS)"/><line x1="30" y1="96" x2="404" y2="96" stroke="url(#gBeam)" stroke-width="2.5" marker-end="url(#mS)"/><line x1="30" y1="120" x2="404" y2="120" stroke="url(#gBeam)" stroke-width="2.5" marker-end="url(#mS)"/><line x1="30" y1="144" x2="404" y2="144" stroke="url(#gBeam)" stroke-width="2.5" marker-end="url(#mS)"/><polygon points="215,38 275,66 275,182 215,154" fill="url(#gS)" stroke="var(--blue)" stroke-width="2" stroke-linejoin="round"/><text x="40" y="52" font-size="26" font-style="italic" font-weight="700" fill="var(--blue)" font-family="Georgia, serif">P</text><text x="286" y="50" font-size="26" font-style="italic" font-weight="700" fill="var(--sky)" font-family="Georgia, serif">S</text></svg>

<p class="nt-cap">La surface doit être perpendiculaire à la direction de propagation.</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Avant l'invention du radar, pendant la Seconde Guerre mondiale, on repérait les avions ennemis à l'oreille grâce à d'immenses pavillons acoustiques, reliés par des tubes aux écouteurs d'un opérateur.</p>
<p>Pourquoi des pavillons aussi grands&nbsp;? Un pavillon recueille la puissance sonore sur une grande surface, puis la canalise vers la toute petite surface de l'écouteur. La même puissance $P$ traverse alors une surface $S$ bien plus petite&nbsp;: d'après $I = P/S$, l'intensité sonore à l'oreille est beaucoup plus grande.</p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>L'intensité sonore est <span class="imp nt-hole">additive</span>&nbsp;: s'il y a 2 ou 10 fois plus de sources sonores (de même puissance), l'intensité (à la même distance) est multipliée par 2 ou 10.</p>
</div>

<p class="nt-lead">Mais notre sensation auditive ne semble pas, elle, proportionnelle au nombre de sources. C'est cette non proportionnalité qui permet d'avoir une plage de sensibilité si étendue&nbsp;:</p>

<div class="nt-grid">
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-ear-listen"></i>Seuil d'audibilité</p>
<p>Le seuil d'audibilité à $\pu{1 kHz}$, appelé <span class="imp">intensité sonore de référence $I_0$</span>, vaut $\pu{1,0E-12 W*m-2}$.</p>
</div>
<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-bolt"></i>Seuil de douleur</p>
<p>Le seuil de douleur est de l'ordre de $\pu{1 W*m-2}$.</p>
</div>
</div>

<p class="nt-big">Il y a un facteur <span class="imp">mille milliards</span> entre les deux 🤯</p>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemple</p>
<p>Pour se représenter ce facteur $10^{12}$&nbsp;: si le seuil d'audibilité correspondait à une longueur de $\pu{1 mm}$, le seuil de douleur correspondrait à $10^{12}\ \pu{mm} = \pu{1E6 km}$, soit environ 2,6 fois la distance Terre-Lune.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">D'où vient la valeur de $I_0$&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Les sonomètres mesurent en réalité la <b>pression acoustique</b>, c'est-à-dire la petite surpression $p$ créée par l'onde (en pascals). Pour une onde plane dans l'air, l'intensité est reliée à la valeur efficace $p_{\text{eff}}$ de cette surpression par&nbsp;:</p>
<p class="nt-center">$I = \dfrac{p_{\text{eff}}^2}{\rho\, c}$</p>
<p>où $\rho \approx \pu{1,2 kg*m-3}$ est la masse volumique de l'air et $c \approx \pu{343 m*s-1}$ la célérité du son (à $20\,^\circ\mathrm{C}$), soit $\rho\, c \approx \pu{415 kg*m-2*s-1}$.</p>
<p>Le seuil d'audition correspond à $p_{\text{eff}} = \pu{2E-5 Pa}$, d'où $I_0 = \dfrac{\left(2\times 10^{-5}\right)^2}{415} \approx \pu{1,0E-12 W*m-2}$. Notre oreille détecte donc des variations de pression environ 5 milliards de fois plus petites que la pression atmosphérique&nbsp;!</p>
</div>
</details>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Notre sensibilité est <span class="imp nt-hole">logarithmique</span>.</p>
<p>On peut par exemple mesurer que l'intensité du son émis par quelqu'un qui parle fort est environ 10&nbsp;000 fois plus grande que celle d'une personne qui chuchote à la même distance&nbsp;! On n'a pourtant pas la sensation d'un son 10&nbsp;000 fois plus fort…</p>
</div>

## Point mathématique {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>$\log$ est la fonction logarithme décimal (logarithme en base 10), définie sur $]0\,;+\infty[$ par&nbsp;:</p>
<p class="nt-center">$\log(x) = \dfrac{\ln(x)}{\ln(10)}$</p>
<p>On a ainsi $\log(10)=$ <span class="imp nt-hole">$1$</span>.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Règles de calcul</p>
<p>Les règles de calcul de $\log$ sont les mêmes que celles de $\ln$ (pour $a>0$, $b>0$, $n$ réel)&nbsp;:</p>
<ul class="nt-facts">
<li>$\log(1)=$ <span class="imp nt-hole">$0$</span></li>
<li>$\log(a{\color{#B45309}\times} b)=$ <span class="nt-hole">$\log(a){\color{#B45309}+}\log(b)$</span></li>
<li>$\log(a{\color{#B45309}\,/\,}b)=$ <span class="nt-hole">$\log(a){\color{#B45309}-}\log(b)$</span></li>
<li>$\log(a^{\color{#B45309}n})=$ <span class="nt-hole">${\color{#B45309}n}\log(a)$</span></li>
</ul>
</div>
<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Fonction réciproque</p>
<p>La fonction réciproque du logarithme décimal est la fonction <span class="imp nt-hole">$10^x$</span>.</p>
<p>Ainsi, si $\log(x)=b$, alors $x=$ <span class="imp nt-hole">$10^b$</span>.</p>
</div>
</div>

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-compass"></i>L'idée</p>
<p>Le boulot de la fonction $\log$ est de fournir l'exposant d'un nombre écrit sous la forme d'une puissance de 10.</p>
</div>

<div class="nt-b nt-ex">
<p class="nt-tag"><i class="fa-solid fa-lightbulb"></i>Exemples</p>
<ul class="nt-facts">
<li>$\log(10^{\color{#047857} 7}) =$ <span class="imp nt-hole">$7$</span></li>
<li>$\log(0{,}01) = \log(10^{\color{#047857}-2}) =$ <span class="imp nt-hole">$-2$</span></li>
<li>$\log(2) \approx \log(10^{\color{#047857}0{,}3}) \approx$ <span class="imp nt-hole">$0{,}3$</span></li>
</ul>
</div>

<div class="nt-lab" id="lab-log">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">La règle logarithmique</p>
<svg class="nt-svg" viewBox="0 0 680 160" role="img" aria-label="Règle logarithmique : chaque multiplication par 10 de x ajoute 1 à log(x)"><text x="22" y="62" font-size="16" font-weight="700" fill="var(--ink)" font-style="italic" font-family="Georgia, serif">x</text><text x="22" y="112" font-size="15" font-weight="700" fill="var(--sky)">log(x)</text><line x1="80" y1="82" x2="650" y2="82" stroke="var(--ink)" stroke-width="2"/><line x1="100.0" y1="75" x2="100.0" y2="89" stroke="var(--ink)" stroke-width="2"/><text x="100.0" y="62" font-size="14" text-anchor="middle" fill="var(--ink)">0,01</text><text x="100.0" y="112" font-size="14" text-anchor="middle" fill="var(--sky)" font-weight="700">−2</text><line x1="206.0" y1="75" x2="206.0" y2="89" stroke="var(--ink)" stroke-width="2"/><text x="206.0" y="62" font-size="14" text-anchor="middle" fill="var(--ink)">0,1</text><text x="206.0" y="112" font-size="14" text-anchor="middle" fill="var(--sky)" font-weight="700">−1</text><line x1="312.0" y1="75" x2="312.0" y2="89" stroke="var(--ink)" stroke-width="2"/><text x="312.0" y="62" font-size="14" text-anchor="middle" fill="var(--ink)">1</text><text x="312.0" y="112" font-size="14" text-anchor="middle" fill="var(--sky)" font-weight="700">0</text><line x1="418.0" y1="75" x2="418.0" y2="89" stroke="var(--ink)" stroke-width="2"/><text x="418.0" y="62" font-size="14" text-anchor="middle" fill="var(--ink)">10</text><text x="418.0" y="112" font-size="14" text-anchor="middle" fill="var(--sky)" font-weight="700">1</text><line x1="524.0" y1="75" x2="524.0" y2="89" stroke="var(--ink)" stroke-width="2"/><text x="524.0" y="62" font-size="14" text-anchor="middle" fill="var(--ink)">100</text><text x="524.0" y="112" font-size="14" text-anchor="middle" fill="var(--sky)" font-weight="700">2</text><line x1="630.0" y1="75" x2="630.0" y2="89" stroke="var(--ink)" stroke-width="2"/><text x="630.0" y="62" font-size="14" text-anchor="middle" fill="var(--ink)">1 000</text><text x="630.0" y="112" font-size="14" text-anchor="middle" fill="var(--sky)" font-weight="700">3</text><path d="M312,44 Q365.0,16 418,44" fill="none" stroke="var(--blue)" stroke-width="1.5"/><text x="365.0" y="24" font-size="13" text-anchor="middle" fill="var(--blue)" font-weight="700">× 10</text><path d="M312,120 Q365.0,148 418,120" fill="none" stroke="var(--sky)" stroke-width="1.5"/><text x="365.0" y="155" font-size="13" text-anchor="middle" fill="var(--sky)" font-weight="700">+ 1</text><g class="lab-mark" transform="translate(343.9,0)"><line x1="0" y1="34" x2="0" y2="128" stroke="var(--rose)" stroke-width="2.5"/><circle cx="0" cy="82" r="6" fill="var(--rose)"/></g></svg>
<label class="nt-ctrl">Déplacez le curseur&nbsp;: <input type="range" min="-2" max="3" step="0.01" value="0.30"></label>
<div class="nt-read" aria-live="polite"><span>$x$ = <b class="out-x">2,00</b></span><span>$x \approx$ <b class="out-p">10<sup>0,30</sup></b></span><span>$\log(x)$ = <b class="out-l">0,30</b></span></div>
<p class="nt-msg">Chaque multiplication de $x$ par 10 ajoute 1 à $\log(x)$&nbsp;: le logarithme transforme les multiplications en additions.</p>
</div>

## Niveau d'intensité sonore {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>Le <span class="imp">niveau d'intensité sonore $L$</span> (pour «&nbsp;Level&nbsp;») se mesure en <span class="imp">décibels (dB)</span> et est donné par la relation&nbsp;:</p>
</div>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$L=10\log\left(\frac{I}{I_0}\right)$$</p>
<div class="nt-f-units"><span>$I_0=\pu{1,0E-12 W*m-2}$ est l'<b>intensité sonore de référence</b></span></div>
</div>

<div class="nt-lab" id="lab-db">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">L'échelle des décibels</p>
<svg class="nt-svg" viewBox="0 0 760 240" role="img" aria-label="Correspondance entre intensité sonore en W par mètre carré et niveau sonore en décibels"><defs><linearGradient id="gDB" x1="0" x2="1"><stop offset="0" stop-color="#34D399"/><stop offset=".45" stop-color="#FBBF24"/><stop offset=".75" stop-color="#F97316"/><stop offset="1" stop-color="#E11D48"/></linearGradient></defs><text x="385" y="22" font-size="13" text-anchor="middle" fill="var(--blue)" font-weight="700">Intensité sonore I (W·m⁻²) : chaque graduation multiplie I par 10</text><rect x="60" y="104" width="650" height="14" rx="7" fill="url(#gDB)"/><line x1="60" y1="98" x2="60" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="60" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−12</tspan></text><text x="60" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">0</text><line x1="110" y1="98" x2="110" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="110" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−11</tspan></text><text x="110" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">10</text><line x1="160" y1="98" x2="160" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="160" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−10</tspan></text><text x="160" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">20</text><line x1="210" y1="98" x2="210" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="210" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−9</tspan></text><text x="210" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">30</text><line x1="260" y1="98" x2="260" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="260" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−8</tspan></text><text x="260" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">40</text><line x1="310" y1="98" x2="310" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="310" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−7</tspan></text><text x="310" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">50</text><line x1="360" y1="98" x2="360" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="360" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−6</tspan></text><text x="360" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">60</text><line x1="410" y1="98" x2="410" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="410" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−5</tspan></text><text x="410" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">70</text><line x1="460" y1="98" x2="460" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="460" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−4</tspan></text><text x="460" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">80</text><line x1="510" y1="98" x2="510" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="510" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−3</tspan></text><text x="510" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">90</text><line x1="560" y1="98" x2="560" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="560" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−2</tspan></text><text x="560" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">100</text><line x1="610" y1="98" x2="610" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="610" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10<tspan dy="-7" font-size="9">−1</tspan></text><text x="610" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">110</text><line x1="660" y1="98" x2="660" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="660" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">1</text><text x="660" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">120</text><line x1="710" y1="98" x2="710" y2="124" stroke="var(--ink)" stroke-width="1.2"/><text x="710" y="88" font-size="12" text-anchor="middle" fill="var(--blue)">10</text><text x="710" y="142" font-size="12" text-anchor="middle" fill="var(--sky)" font-weight="700">130</text><line x1="60" y1="149" x2="60" y2="160" stroke="var(--muted)" stroke-dasharray="2 2"/><text x="60" y="172" font-size="12" text-anchor="start" fill="var(--ink)">seuil d'audibilité</text><line x1="210" y1="149" x2="210" y2="184" stroke="var(--muted)" stroke-dasharray="2 2"/><text x="210" y="196" font-size="12" text-anchor="middle" fill="var(--ink)">chuchotement</text><line x1="360" y1="149" x2="360" y2="160" stroke="var(--muted)" stroke-dasharray="2 2"/><text x="360" y="172" font-size="12" text-anchor="middle" fill="var(--ink)">conversation</text><line x1="410" y1="149" x2="410" y2="184" stroke="var(--muted)" stroke-dasharray="2 2"/><text x="410" y="196" font-size="12" text-anchor="middle" fill="var(--ink)">voix forte</text><line x1="660" y1="149" x2="660" y2="160" stroke="var(--muted)" stroke-dasharray="2 2"/><text x="660" y="172" font-size="12" text-anchor="end" fill="var(--ink)">seuil de douleur</text><text x="385" y="230" font-size="13" text-anchor="middle" fill="var(--sky)" font-weight="700">Niveau sonore L (dB) : chaque graduation ajoute 10 dB</text><g class="lab-mark" transform="translate(360,0)"><path d="M-8,92 L8,92 L0,103 z" fill="var(--rose)"/><line x1="0" y1="100" x2="0" y2="124" stroke="var(--rose)" stroke-width="3"/></g></svg>
<label class="nt-ctrl">Niveau sonore&nbsp;: <input type="range" min="0" max="130" step="1" value="60"></label>
<div class="nt-read" aria-live="polite"><span>$L$ = <b class="out-L">60 dB</b></span><span>$I$ = <b class="out-I">1,0 × 10<sup>−6</sup> W·m<sup>−2</sup></b></span><span>$I/I_0$ = <b class="out-r">10<sup>6,0</sup></b></span></div>
<p class="nt-msg"></p>
</div>

<p class="nt-cap">Une échelle en décibels ramène les douze puissances de 10 qui séparent le seuil d'audibilité du seuil de douleur à une échelle de 0 à 120&nbsp;dB.</p>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>À retenir</p>
<p>Doubler l'intensité acoustique revient à <span class="imp nt-hole">ajouter 3 dB</span> au niveau sonore et multiplier l'intensité par 10 <span class="imp nt-hole">ajoute 10 dB</span>.</p>
</div>

<div class="nt-lab" id="lab-src">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Ajoutez des sources identiques</p>
<p class="nt-note">Chaque source seule produit, à la même distance, un niveau sonore de 60&nbsp;dB.</p>
<div class="nt-dots" aria-hidden="true"></div>
<div class="nt-bar-row"><span>Intensité</span><div class="nt-bar nt-bar-I"><div></div></div><b class="out-I">1 × <i>I</i><sub>t</sub></b></div>
<div class="nt-bar-row"><span>Niveau sonore</span><div class="nt-bar nt-bar-L"><div></div></div><b class="out-L">60 dB</b></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-op="-1">− 1 source</button>
<button type="button" class="nt-btn" data-op="+1">+ 1 source</button>
<button type="button" class="nt-btn nt-btn-main" data-op="x2">× 2</button>
<button type="button" class="nt-btn nt-btn-main" data-op="x10">× 10</button>
<button type="button" class="nt-btn" data-op="reset">1 source</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-scroll">
<table class="nt-t">
<thead><tr><th>Nombre de sources<br>de même intensité</th><th>Intensité sonore</th><th>Niveau sonore</th></tr></thead>
<tbody>
<tr><td>1</td><td>$I_t$</td><td>$L_t$</td></tr>
<tr><td>2</td><td>$2\,I_t$</td><td><span class="nt-pill">$L_t + \pu{3 dB}$</span></td></tr>
<tr><td>4</td><td>$4\,I_t$</td><td><span class="nt-pill">$L_t + \pu{6 dB}$</span></td></tr>
<tr><td>10</td><td>$10\,I_t$</td><td><span class="nt-pill">$L_t + \pu{10 dB}$</span></td></tr>
<tr><td>100</td><td>$100\,I_t$</td><td><span class="nt-pill">$L_t + \pu{20 dB}$</span></td></tr>
</tbody>
</table>
</div>

<div class="nt-b nt-demo-box">
<p class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</p>
<p>Si $\color{#047857}I_t$ est l'intensité sonore d'une trompette, pour 2 trompettes, on a&nbsp;: ${\color{#2A6BC4}I} = 2\times {\color{#047857}I_t}$.</p>
<p>Appelons $\color{#047857}L_t$ le niveau sonore d'une trompette et cherchons le niveau sonore $\color{#2A6BC4}L$ des 2 trompettes&nbsp;:</p>
<div class="nt-scroll">$$\begin{aligned}{\color{#2A6BC4}L} &= 10\times \log\left(\frac{\color{#2A6BC4}I}{I_0}\right)\\ &= 10\times \log\left(\frac{2\times {\color{#047857}I_t}}{I_0}\right)\\ &= 10\times \log\left(2\times\frac{\color{#047857}I_t}{I_0}\right)\\ &= 10\times\left(\log(2) + \log\left(\frac{\color{#047857}I_t}{I_0}\right)\right)\\ &= 10\times \log\left(\frac{\color{#047857}I_t}{I_0}\right) + {\color{#E11D48}10\times\log(2)}\\ &= {\color{#047857}L_t} + {\color{#E11D48}\pu{3 dB}}\end{aligned}$$</div>
<p class="nt-note">car $10\times\log(2) \approx 10 \times 0{,}30 = \pu{3,0 dB}$.</p>
</div>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Les décibels de l'audiogramme</span></summary>
<div class="nt-d-body">
<p>Pour les tests audiométriques qui mesurent le degré de perte auditive, on utilise le dB HL (pour <i>hearing level</i>). Le dB HL tient compte de la variation de sensibilité de l'oreille humaine en fonction de la fréquence (donc de la hauteur des sons)&nbsp;: pour chaque fréquence testée, 0&nbsp;dB HL correspond à l'intensité minimale perçue en moyenne par les personnes normo-entendantes.</p>
</div>
</details>

<p class="nt-lead">Comment obtenir l'intensité sonore $I$ à partir du niveau d'intensité sonore $L$&nbsp;?</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$I=I_0\times 10^{\frac{L}{10}}$$</p>
</div>

<details class="nt-d">
<summary><span class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</span><span class="nt-sum">Passer de $L$ à $I$</span></summary>
<div class="nt-d-body">
<p>On isole le logarithme&nbsp;: $L = 10\log\left(\dfrac{I}{I_0}\right) \iff \dfrac{L}{10} = \log\left(\dfrac{I}{I_0}\right)$.</p>
<p>On applique la fonction réciproque $10^x$ aux deux membres&nbsp;: $\dfrac{I}{I_0} = 10^{\frac{L}{10}}$, puis on multiplie par $I_0$&nbsp;: $I = I_0\times 10^{\frac{L}{10}}$.</p>
</div>
</details>

## Atténuation {.nt-h2}

<div class="nt-b nt-def">
<p class="nt-tag"><i class="fa-solid fa-book-open"></i>Définition</p>
<p>L'<span class="imp">atténuation</span> (en dB) mesure la diminution du niveau d'intensité sonore&nbsp;: $A = L_{\text{avant}} - L_{\text{après}}$.</p>
<p>Il y a deux types d'atténuation&nbsp;: l'atténuation <span class="imp nt-hole">géométrique</span> et l'atténuation <span class="imp nt-hole">par absorption</span>.</p>
</div>

### Atténuation géométrique {.nt-h3}

<p class="nt-lead">Elle est due à l'<span class="imp">éloignement</span> entre la source et l'observateur.</p>

<p>En effet, <span class="imp">plus la source est éloignée</span> et <span class="imp">plus la surface</span> sur laquelle la puissance sonore se répartit <span class="imp nt-hole">est grande</span> et donc <span class="imp">plus l'intensité sonore</span> <span class="imp nt-hole">est faible</span>.</p>

<p>Si la source est omnidirectionnelle (même intensité sonore dans toutes les directions), alors l'intensité sonore à une distance $d$ de la source se répartit sur <span class="imp nt-hole">une sphère de rayon $d$</span> centrée sur la source. On a donc&nbsp;:</p>

<div class="nt-f">
<p class="nt-tag"><i class="fa-solid fa-equals"></i>Formule</p>
<p class="nt-f-math">$$I=\frac{P}{4\pi d^2}$$</p>
<div class="nt-f-units"><span>$4\pi d^2$&nbsp;: aire de la sphère de rayon $d$</span></div>
</div>

<svg class="nt-svg nt-svg-m" viewBox="0 0 520 350" role="img" aria-label="La même puissance se répartit sur 1, 4 puis 9 carrés quand la distance passe de d à 2d puis 3d"><line x1="40" y1="175" x2="449.5" y2="50.8" stroke="var(--muted)" stroke-dasharray="4 3"/><line x1="40" y1="175" x2="350.5" y2="119.2" stroke="var(--muted)" stroke-dasharray="4 3"/><line x1="40" y1="175" x2="449.5" y2="230.8" stroke="var(--muted)" stroke-dasharray="4 3"/><line x1="40" y1="175" x2="350.5" y2="299.2" stroke="var(--muted)" stroke-dasharray="4 3"/><polygon points="143.5,216.4 143.5,156.4 176.5,133.6 176.5,193.6" fill="var(--blue-bg)" fill-opacity=".9" stroke="var(--blue)" stroke-width="1.6" stroke-linejoin="round"/><polygon points="143.5,216.4 143.5,156.4 176.5,133.6 176.5,193.6" fill="var(--sky)" fill-opacity=".55"/><text x="148.5" y="238.4" font-size="15" font-weight="700" fill="var(--ink)" font-style="italic" font-family="Georgia, serif">d</text><text x="148.5" y="254.4" font-size="12" fill="var(--sky)" font-weight="700">1 carré</text><polygon points="247.0,257.8 247.0,137.8 313.0,92.2 313.0,212.2" fill="var(--blue-bg)" fill-opacity=".9" stroke="var(--blue)" stroke-width="1.6" stroke-linejoin="round"/><polygon points="247.0,257.8 247.0,197.8 280.0,175.0 280.0,235.0" fill="var(--sky)" fill-opacity=".55"/><line x1="247.0" y1="197.8" x2="313.0" y2="152.2" stroke="var(--blue)"/><line x1="280.0" y1="235.0" x2="280.0" y2="115.0" stroke="var(--blue)"/><text x="252.0" y="279.8" font-size="15" font-weight="700" fill="var(--ink)" font-style="italic" font-family="Georgia, serif">2d</text><text x="252.0" y="295.8" font-size="12" fill="var(--sky)" font-weight="700">4 carrés</text><polygon points="350.5,299.2 350.5,119.2 449.5,50.8 449.5,230.8" fill="var(--blue-bg)" fill-opacity=".9" stroke="var(--blue)" stroke-width="1.6" stroke-linejoin="round"/><polygon points="350.5,299.2 350.5,239.2 383.5,216.4 383.5,276.4" fill="var(--sky)" fill-opacity=".55"/><line x1="350.5" y1="239.2" x2="449.5" y2="170.8" stroke="var(--blue)"/><line x1="383.5" y1="276.4" x2="383.5" y2="96.4" stroke="var(--blue)"/><line x1="350.5" y1="179.2" x2="449.5" y2="110.8" stroke="var(--blue)"/><line x1="416.5" y1="253.6" x2="416.5" y2="73.6" stroke="var(--blue)"/><text x="355.5" y="321.2" font-size="15" font-weight="700" fill="var(--ink)" font-style="italic" font-family="Georgia, serif">3d</text><text x="355.5" y="337.2" font-size="12" fill="var(--sky)" font-weight="700">9 carrés</text><circle cx="40" cy="175" r="7" fill="var(--rose)"/><text x="34" y="161" font-size="12" fill="var(--ink)">source</text></svg>

<p class="nt-cap">La même puissance traverse 1 carré à la distance $d$, 4 carrés à $2d$, 9 carrés à $3d$&nbsp;: chaque carré coloré reçoit 4 fois, puis 9 fois moins de puissance.</p>

<div class="nt-lab" id="lab-dist">
<p class="nt-tag"><i class="fa-solid fa-hand-pointer"></i>Animation interactive</p>
<p class="nt-lab-title">Éloignez-vous de la source</p>
<p class="nt-note">Une source omnidirectionnelle de puissance $P = \pu{1,0E-2 W}$ émet dans toutes les directions.</p>
<svg class="nt-svg nt-svg-m" viewBox="0 0 460 200" role="img" aria-label="Sphère de rayon d centrée sur la source, et position de l'auditeur">
<circle class="d-sph" cx="30" cy="100" r="42" fill="var(--blue)" fill-opacity=".5" stroke="var(--sky)" stroke-width="2"/>
<line class="d-ray" x1="30" y1="100" x2="72" y2="100" stroke="var(--ink)" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="30" cy="100" r="7" fill="var(--rose)"/>
<circle class="d-ear" cx="72" cy="100" r="6" fill="#fff" stroke="var(--rose)" stroke-width="3"/>
<text class="d-lab" x="51" y="90" font-size="15" font-style="italic" font-weight="700" fill="var(--ink)" text-anchor="middle" font-family="Georgia, serif">d</text>
</svg>
<label class="nt-ctrl">Distance&nbsp;: <b class="out-d">2,0 m</b><input type="range" min="1" max="20" step="0.1" value="2"></label>
<div class="nt-read" aria-live="polite"><span>$4\pi d^2$ = <b class="out-S">50 m²</b></span><span>$I$ = <b class="out-I">2,0 × 10<sup>−4</sup> W·m<sup>−2</sup></b></span><span>$L$ = <b class="out-L">83 dB</b></span></div>
<div class="nt-btns">
<button type="button" class="nt-btn" data-k="0.5">d ÷ 2</button>
<button type="button" class="nt-btn nt-btn-main" data-k="2">d × 2</button>
<button type="button" class="nt-btn nt-btn-main" data-k="10">d × 10</button>
</div>
<p class="nt-msg" aria-live="polite"></p>
</div>

<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Conclusion</p>
<p>L'intensité sonore varie <span class="imp nt-hole">inversement proportionnellement au carré de la distance à la source</span>.</p>
</div>

<div class="nt-grid">
<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Conséquence</p>
<p><span class="imp">Doubler la distance</span> divise l'intensité sonore par <span class="imp nt-hole">4</span>, ce qui correspond à une <span class="imp">atténuation de</span> <span class="imp nt-hole">6 dB</span> du niveau sonore.</p>
<p class="nt-center">$d\rightarrow 2d\Rightarrow I\rightarrow I/4 \Leftrightarrow L\rightarrow L-6$</p>
</div>
<div class="nt-b nt-prop">
<p class="nt-tag"><i class="fa-solid fa-star"></i>Conséquence</p>
<p><span class="imp">Multiplier par 10 la distance</span> divise l'intensité sonore par <span class="imp nt-hole">100</span>, ce qui correspond à une <span class="imp">atténuation de</span> <span class="imp nt-hole">20 dB</span> du niveau sonore.</p>
<p class="nt-center">$d\rightarrow 10d\Rightarrow I\rightarrow I/100 \Leftrightarrow L\rightarrow L-20$</p>
</div>
</div>

<details class="nt-d">
<summary><span class="nt-tag"><i class="fa-solid fa-pen-nib"></i>Démonstration</span><span class="nt-sum">D'où viennent ces 6 dB et ces 20 dB&nbsp;?</span></summary>
<div class="nt-d-body">
<p>Si l'intensité est divisée par 4, le niveau sonore devient $L' = 10\log\left(\dfrac{I/4}{I_0}\right) = 10\log\left(\dfrac{I}{I_0}\right) - 10\log(4) = L - 10\log(4)$.</p>
<p>Or $10\log(4) = 10\log(2^2) = 20\log(2) \approx 20\times 0{,}30 = 6$&nbsp;: on perd environ $\pu{6 dB}$.</p>
<p>De même, si l'intensité est divisée par 100, on perd $10\log(100) = 10\times 2 = \pu{20 dB}$.</p>
</div>
</details>

### Atténuation par absorption {.nt-h3}

<p class="nt-lead">Le niveau d'intensité sonore d'une onde sonore rencontrant un obstacle est atténué car une partie de son <span class="imp">énergie est absorbée</span> par le milieu matériel composant l'obstacle.</p>

<p>La proportion d'énergie absorbée dépend du <span class="imp nt-hole">matériau</span> composant l'obstacle et de <span class="imp nt-hole">l'épaisseur</span> de celui-ci.</p>

<svg class="nt-svg nt-svg-m" viewBox="0 0 560 230" role="img" aria-label="Une onde incidente rencontre un obstacle : une partie est réfléchie, une partie absorbée, le reste transmis"><defs><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="var(--slate)" stroke-opacity=".35" stroke-width="3"/></pattern><linearGradient id="gHeat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--amber)" stop-opacity=".9"/><stop offset="1" stop-color="var(--amber)" stop-opacity="0"/></linearGradient></defs><rect x="262" y="16" width="52" height="184" rx="6" fill="var(--slate-bg)" stroke="var(--slate)" stroke-width="1.5"/><rect x="262" y="16" width="52" height="184" rx="6" fill="url(#hatch)"/><polygon points="24,66 228,66 228,54 256,80 228,106 228,94 24,94" fill="var(--blue)"/><polygon points="320,76 492,76 492,68 512,80 492,92 492,84 320,84" fill="var(--blue)" fill-opacity=".75"/><polygon points="256,128 98,156 96,146 66,168 102,176 100,166 258,138" fill="var(--sky)" fill-opacity=".18" stroke="var(--sky)" stroke-width="1.6" stroke-dasharray="5 4" stroke-linejoin="round"/><path d="M288,92 q6,8 0,16 q-6,8 0,16 q6,8 0,16 q-6,8 0,16" fill="none" stroke="url(#gHeat)" stroke-width="4" stroke-linecap="round"/><text x="30" y="50" font-size="14" font-weight="700" fill="var(--blue)">onde incidente</text><text x="330" y="64" font-size="14" font-weight="700" fill="var(--blue)" fill-opacity=".85">onde transmise</text><text x="70" y="200" font-size="14" font-weight="700" fill="var(--sky)">onde réfléchie</text><text x="288" y="222" font-size="14" font-weight="700" fill="var(--amber)" text-anchor="middle">énergie absorbée</text></svg>

<div class="nt-b nt-warn">
<p class="nt-tag"><i class="fa-solid fa-triangle-exclamation"></i>Attention</p>
<p>Une partie de l'onde est aussi réfléchie par l'obstacle. Dans les exercices de terminale, on néglige généralement cette réflexion&nbsp;: toute l'énergie qui n'est pas transmise est alors considérée comme absorbée.</p>
</div>

<div class="nt-b nt-ask">
<p class="nt-tag"><i class="fa-solid fa-circle-question"></i>Question</p>
<p>Il existe deux grandes familles de bouchons d'oreille&nbsp;: les bouchons en mousse, vendus en pharmacie, et les bouchons moulés sur mesure, munis d'un petit filtre acoustique.</p>
<p><b>Pourquoi les bouchons moulés sont-ils plus adaptés à des musiciens&nbsp;?</b></p>
</div>

<details class="nt-d nt-rep">
<summary><span class="nt-tag"><i class="fa-solid fa-key"></i>Réponse</span><span class="nt-sum">Voir un élément de réponse</span></summary>
<div class="nt-d-body">
<p>Les bouchons en mousse modifient le timbre, puisqu'ils n'atténuent pas toutes les fréquences de la même façon&nbsp;: les harmoniques (les fréquences élevées du spectre) sont bien plus atténuées que le fondamental. Et de toute façon, ils atténuent trop.</p>
<svg class="nt-svg nt-svg-m" viewBox="0 0 520 280" role="img" aria-label="Allure typique de l'atténuation de deux types de bouchons en fonction de la fréquence"><line x1="70" y1="30.0" x2="490" y2="30.0" stroke="var(--line)"/><text x="62" y="34.0" font-size="11" text-anchor="end" fill="var(--muted)">0</text><line x1="70" y1="75.0" x2="490" y2="75.0" stroke="var(--line)"/><text x="62" y="79.0" font-size="11" text-anchor="end" fill="var(--muted)">10</text><line x1="70" y1="120.0" x2="490" y2="120.0" stroke="var(--line)"/><text x="62" y="124.0" font-size="11" text-anchor="end" fill="var(--muted)">20</text><line x1="70" y1="165.0" x2="490" y2="165.0" stroke="var(--line)"/><text x="62" y="169.0" font-size="11" text-anchor="end" fill="var(--muted)">30</text><line x1="70" y1="210.0" x2="490" y2="210.0" stroke="var(--line)"/><text x="62" y="214.0" font-size="11" text-anchor="end" fill="var(--muted)">40</text><text x="80" y="250.5" font-size="11" text-anchor="middle" fill="var(--muted)">125</text><text x="145" y="250.5" font-size="11" text-anchor="middle" fill="var(--muted)">250</text><text x="210" y="250.5" font-size="11" text-anchor="middle" fill="var(--muted)">500</text><text x="275" y="250.5" font-size="11" text-anchor="middle" fill="var(--muted)">1k</text><text x="340" y="250.5" font-size="11" text-anchor="middle" fill="var(--muted)">2k</text><text x="405" y="250.5" font-size="11" text-anchor="middle" fill="var(--muted)">4k</text><text x="470" y="250.5" font-size="11" text-anchor="middle" fill="var(--muted)">8k</text><text x="280" y="268.5" font-size="12" text-anchor="middle" fill="var(--ink)">fréquence (Hz)</text><text x="18" y="150" font-size="12" fill="var(--ink)" transform="rotate(-90 18 150)" text-anchor="middle">atténuation (dB)</text><polyline points="80,156.0 145,165.0 210,174.0 275,178.5 340,187.5 405,210.0 470,219.0" fill="none" stroke="var(--rose)" stroke-width="3" stroke-linejoin="round"/><circle cx="80" cy="156.0" r="4" fill="var(--rose)"/><circle cx="145" cy="165.0" r="4" fill="var(--rose)"/><circle cx="210" cy="174.0" r="4" fill="var(--rose)"/><circle cx="275" cy="178.5" r="4" fill="var(--rose)"/><circle cx="340" cy="187.5" r="4" fill="var(--rose)"/><circle cx="405" cy="210.0" r="4" fill="var(--rose)"/><circle cx="470" cy="219.0" r="4" fill="var(--rose)"/><polyline points="80,97.5 145,97.5 210,97.5 275,102.0 340,102.0 405,102.0 470,106.5" fill="none" stroke="var(--emerald)" stroke-width="3" stroke-linejoin="round"/><circle cx="80" cy="97.5" r="4" fill="var(--emerald)"/><circle cx="145" cy="97.5" r="4" fill="var(--emerald)"/><circle cx="210" cy="97.5" r="4" fill="var(--emerald)"/><circle cx="275" cy="102.0" r="4" fill="var(--emerald)"/><circle cx="340" cy="102.0" r="4" fill="var(--emerald)"/><circle cx="405" cy="102.0" r="4" fill="var(--emerald)"/><circle cx="470" cy="106.5" r="4" fill="var(--emerald)"/><text x="80" y="196.5" font-size="12" fill="var(--rose)" font-weight="700">bouchon en mousse</text><text x="80" y="85.5" font-size="12" fill="var(--emerald)" font-weight="700">bouchon moulé « musicien »</text></svg>
<p class="nt-cap">Allure typique de l'atténuation selon la fréquence. Les bouchons moulés atténuent presque autant toutes les fréquences&nbsp;: le son est moins fort, mais son timbre est préservé.</p>
</div>
</details>

<details class="nt-d nt-plus">
<summary><span class="nt-tag"><i class="fa-solid fa-rocket"></i>Pour aller plus loin</span><span class="nt-sum">Chambre anéchoïque et temps de réverbération</span></summary>
<div class="nt-d-body">
<p>Une chambre anéchoïque («&nbsp;sans écho&nbsp;») est une salle dont les murs, le sol et le plafond sont tapissés de pointes en matériau très absorbant&nbsp;: les ondes sonores qui les atteignent ne sont quasiment pas réfléchies. On y entend sa propre voix de façon étrangement «&nbsp;sèche&nbsp;», sans aucune résonance.</p>
<p>Dans une salle ordinaire au contraire, le son continue d'être entendu un moment après l'arrêt de la source, à cause des réflexions successives sur les parois&nbsp;: c'est la réverbération. Le temps de réverbération est la durée au bout de laquelle le niveau sonore a diminué de $\pu{60 dB}$. En pratique, une telle baisse est difficile à mesurer&nbsp;: si l'on suppose que le niveau décroît de façon linéaire, on mesure la durée nécessaire pour perdre $\pu{20 dB}$ ou $\pu{30 dB}$, puis on la multiplie respectivement par 3 ou par 2.</p>
</div>
</details>

<script>
(function () {
  'use strict';
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = getComputedStyle(document.documentElement);
  function col(name) { return ROOT.getPropertyValue(name).trim() || '#2A6BC4'; }
  function fr(x, nd) { return x.toFixed(nd).replace('.', ','); }
  function minus(s) { return String(s).replace('-', '\u2212'); }
  function sci(x, nd) {
    var n = Math.floor(Math.log10(x) + 1e-9);
    var a = x / Math.pow(10, n);
    var t = a.toFixed(nd);
    if (parseFloat(t) >= 10) { n += 1; t = (a / 10).toFixed(nd); }
    return t.replace('.', ',') + ' \u00d7 10<sup>' + minus(n) + '</sup>';
  }
  function canvasCtx(cv) {
    var dpr = window.devicePixelRatio || 1;
    var w = cv.clientWidth, h = cv.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function onResize(fn) {
    var t = null;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(fn, 120); });
  }
  var LANDMARKS = [[0, "le seuil d'audibilité"], [30, 'un chuchotement'], [60, 'une conversation'], [70, 'une voix forte'], [120, 'le seuil de douleur']];
  function nearest(L) {
    var best = LANDMARKS[0];
    LANDMARKS.forEach(function (m) { if (Math.abs(m[0] - L) < Math.abs(best[0] - L)) { best = m; } });
    return best;
  }
  /* ---------------- 1. Onde longitudinale ---------------- */
  (function () {
    var root = document.getElementById('lab-onde');
    if (!root) { return; }
    var cv = root.querySelector('canvas');
    var rA = root.querySelector('[data-p="amp"]'), rF = root.querySelector('[data-p="freq"]');
    var btn = root.querySelector('[data-act="play"]');
    var playing = !RM, visible = true, t = 0, last = null, S = null, C = {}, PTS = [], HL = 0;
    /* générateur pseudo-aléatoire à graine : même nuage à chaque chargement */
    function rng(seed) {
      return function () {
        seed |= 0; seed = seed + 0x6D2B79F5 | 0;
        var q = Math.imul(seed ^ seed >>> 15, 1 | seed);
        q = q + Math.imul(q ^ q >>> 7, 61 | q) ^ q;
        return ((q ^ q >>> 14) >>> 0) / 4294967296;
      };
    }
    /* échantillonnage de Poisson (Bridson) : positions aléatoires mais sans amas */
    function poisson(x0, y0, w, h, r, rand) {
      var cell = r / Math.SQRT2, gw = Math.ceil(w / cell), gh = Math.ceil(h / cell);
      var grid = new Array(gw * gh), pts = [], active = [];
      function add(p) {
        pts.push(p); active.push(p);
        grid[Math.floor((p[1] - y0) / cell) * gw + Math.floor((p[0] - x0) / cell)] = p;
      }
      function ok(x, y) {
        if (x < x0 || x >= x0 + w || y < y0 || y >= y0 + h) { return false; }
        var gx = Math.floor((x - x0) / cell), gy = Math.floor((y - y0) / cell);
        for (var j = Math.max(0, gy - 2); j <= Math.min(gh - 1, gy + 2); j++) {
          for (var i = Math.max(0, gx - 2); i <= Math.min(gw - 1, gx + 2); i++) {
            var q = grid[j * gw + i];
            if (q && (q[0] - x) * (q[0] - x) + (q[1] - y) * (q[1] - y) < r * r) { return false; }
          }
        }
        return true;
      }
      add([x0 + rand() * w, y0 + rand() * h]);
      while (active.length) {
        var k = Math.floor(rand() * active.length), p = active[k], found = false;
        for (var n = 0; n < 30; n++) {
          var a = rand() * 2 * Math.PI, d = r * (1 + rand());
          var x = p[0] + d * Math.cos(a), y = p[1] + d * Math.sin(a);
          if (ok(x, y)) { add([x, y]); found = true; break; }
        }
        if (!found) { active.splice(k, 1); }
      }
      return pts;
    }
    function setup() {
      S = canvasCtx(cv);
      C = { ind: col('--blue'), rose: col('--rose'), mut: col('--muted') };
      PTS = poisson(-16, 34, S.w + 32, S.h - 46, 11, rng(20261003));
      var best = Infinity;
      PTS.forEach(function (p, i) {
        var dd = Math.abs(p[0] - S.w / 2) + 0.5 * Math.abs(p[1] - (S.h + 22) / 2);
        if (dd < best) { best = dd; HL = i; }
      });
      draw();
    }
    function draw() {
      if (!S) { return; }
      var ctx = S.ctx, w = S.w, h = S.h;
      ctx.clearRect(0, 0, w, h);
      var A = parseFloat(rA.value), f = parseFloat(rF.value), v = 110;
      var k = 2 * Math.PI * f / v, om = 2 * Math.PI * f;
      ctx.fillStyle = C.mut; ctx.font = '600 12px system-ui, sans-serif';
      ctx.textAlign = 'right'; ctx.fillText('propagation \u2192', w - 12, 20);
      var hp = PTS[HL];
      ctx.strokeStyle = C.rose; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(hp[0], 28); ctx.lineTo(hp[0], h - 6); ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = C.ind; ctx.globalAlpha = 0.72;
      for (var i = 0; i < PTS.length; i++) {
        if (i === HL) { continue; }
        var p = PTS[i];
        ctx.beginPath();
        ctx.arc(p[0] + A * Math.sin(om * t - k * p[0]), p[1], 3.1, 0, 2 * Math.PI);
        ctx.fill();
      }
      ctx.globalAlpha = 1; ctx.fillStyle = C.rose;
      ctx.beginPath();
      ctx.arc(hp[0] + A * Math.sin(om * t - k * hp[0]), hp[1], 5, 0, 2 * Math.PI);
      ctx.fill();
    }
    function step(ts) {
      if (last !== null && playing && visible) { t += Math.min(0.05, (ts - last) / 1000); }
      last = ts;
      if (visible) { draw(); }
      requestAnimationFrame(step);
    }
    function label() {
      btn.innerHTML = playing ? '<i class="fa-solid fa-pause"></i>&nbsp; Pause' : '<i class="fa-solid fa-play"></i>&nbsp; Lecture';
    }
    btn.addEventListener('click', function () { playing = !playing; label(); });
    [rA, rF].forEach(function (r) { r.addEventListener('input', draw); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(cv);
    }
    label(); setup(); onResize(setup);
    requestAnimationFrame(step);
  })();
  /* ---------------- 2. Hauteur, intensité, timbre ---------------- */
  (function () {
    var root = document.getElementById('lab-son');
    if (!root) { return; }
    var cvS = root.querySelector('canvas.sig'), cvP = root.querySelector('canvas.spec');
    var rF = root.querySelector('[data-p="freq"]'), rA = root.querySelector('[data-p="amp"]');
    var outF = root.querySelector('.out-f'), outA = root.querySelector('.out-a');
    var btn = root.querySelector('[data-act="listen"]');
    var REC = {
      pur: [1],
      flute: [1, 0.45, 0.2, 0.08],
      clarinette: [1, 0, 0.36, 0, 0.22, 0, 0.14, 0, 0.09],
      violon: [1, 0.5, 0.333, 0.25, 0.2, 0.167, 0.143, 0.125, 0.111, 0.1]
    };
    var S1, S2, C = {}, AC = null, osc = null, gain = null;
    function freq() { return 110 * Math.pow(2, 3 * parseFloat(rF.value) / 100); }
    function amp() { return parseFloat(rA.value) / 100; }
    function timbre() { var r = root.querySelector('input[name="timbre-son"]:checked'); return r ? r.value : 'pur'; }
    function norm(c) {
      var m = 0;
      for (var i = 0; i < 500; i++) {
        var x = 2 * Math.PI * i / 500, s = 0;
        for (var n = 0; n < c.length; n++) { s += c[n] * Math.sin((n + 1) * x); }
        m = Math.max(m, Math.abs(s));
      }
      return m || 1;
    }
    function setup() {
      S1 = canvasCtx(cvS); S2 = canvasCtx(cvP);
      C = { ind: col('--blue'), vio: col('--sky'), cyan: col('--cyan'), mut: col('--muted'), line: col('--line'), ink: col('--ink') };
      draw();
    }
    function draw() {
      var f = freq(), A = amp(), c = REC[timbre()], N = norm(c);
      outF.textContent = Math.round(f) + ' Hz';
      outA.textContent = Math.round(A * 100) + ' %';
      /* signal */
      var ctx = S1.ctx, w = S1.w, h = S1.h, mid = h / 2 - 6, H = h / 2 - 22;
      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = C.line; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(10, mid); ctx.lineTo(w - 10, mid); ctx.stroke();
      ctx.fillStyle = C.mut; ctx.font = '11px system-ui, sans-serif'; ctx.textAlign = 'center';
      [0, 5, 10].forEach(function (ms) { ctx.textAlign = ms === 0 ? 'left' : (ms === 10 ? 'right' : 'center'); ctx.fillText(ms + ' ms', 10 + (w - 20) * ms / 10, h - 6); });
      ctx.strokeStyle = C.ind; ctx.lineWidth = 2.4; ctx.lineJoin = 'round'; ctx.beginPath();
      for (var px = 0; px <= w - 20; px++) {
        var tt = 0.010 * px / (w - 20), s = 0;
        for (var n = 0; n < c.length; n++) { s += c[n] * Math.sin(2 * Math.PI * (n + 1) * f * tt); }
        var y = mid - A * H * s / N;
        if (px === 0) { ctx.moveTo(10 + px, y); } else { ctx.lineTo(10 + px, y); }
      }
      ctx.stroke();
      /* spectre */
      var g = S2.ctx, W = S2.w, Hh = S2.h, base = Hh - 24, top = 14, FMAX = 9000;
      g.clearRect(0, 0, W, Hh);
      g.strokeStyle = C.line; g.lineWidth = 1;
      g.beginPath(); g.moveTo(10, base); g.lineTo(W - 10, base); g.stroke();
      g.fillStyle = C.mut; g.font = '11px system-ui, sans-serif';
      [0, 2000, 4000, 6000, 8000].forEach(function (fk) { g.textAlign = fk === 0 ? 'left' : 'center'; g.fillText(fk === 0 ? '0' : (fk / 1000) + ' kHz', 10 + (W - 20) * fk / FMAX, Hh - 6); });
      for (var m = 0; m < c.length; m++) {
        var fn = (m + 1) * f;
        if (fn > FMAX || c[m] === 0) { continue; }
        var x = 10 + (W - 20) * fn / FMAX, bh = (base - top) * A * c[m];
        g.fillStyle = m === 0 ? C.cyan : C.vio;
        g.fillRect(x - 3, base - bh, 6, bh);
      }
      g.fillStyle = C.cyan; g.textAlign = 'left'; g.font = '600 11px system-ui, sans-serif';
      g.fillText('fondamental : ' + Math.round(f) + ' Hz', 14, 14);
      if (osc) { updateAudio(); }
    }
    function wave() {
      var c = REC[timbre()], re = new Float32Array(c.length + 1), im = new Float32Array(c.length + 1);
      for (var i = 0; i < c.length; i++) { im[i + 1] = c[i]; }
      return AC.createPeriodicWave(re, im);
    }
    function updateAudio() {
      var now = AC.currentTime;
      osc.frequency.setTargetAtTime(freq(), now, 0.02);
      gain.gain.setTargetAtTime(0.25 * amp(), now, 0.03);
      osc.setPeriodicWave(wave());
    }
    function start() {
      var Ctor = window.AudioContext || window.webkitAudioContext;
      if (!Ctor) { return; }
      AC = AC || new Ctor();
      if (AC.state === 'suspended') { AC.resume(); }
      osc = AC.createOscillator(); gain = AC.createGain(); gain.gain.value = 0;
      osc.setPeriodicWave(wave()); osc.frequency.value = freq();
      osc.connect(gain); gain.connect(AC.destination); osc.start();
      gain.gain.setTargetAtTime(0.25 * amp(), AC.currentTime, 0.03);
    }
    function stop() {
      if (!osc) { return; }
      var o = osc;
      gain.gain.setTargetAtTime(0, AC.currentTime, 0.03);
      setTimeout(function () { try { o.stop(); } catch (e) {} }, 250);
      osc = null;
    }
    btn.addEventListener('click', function () {
      if (osc) { stop(); } else { start(); }
      btn.innerHTML = osc ? '<i class="fa-solid fa-stop"></i>&nbsp; Arrêter' : '<i class="fa-solid fa-volume-high"></i>&nbsp; Écouter';
    });
    document.addEventListener('visibilitychange', function () {
      if (document.hidden && osc) { stop(); btn.innerHTML = '<i class="fa-solid fa-volume-high"></i>&nbsp; Écouter'; }
    });
    [rF, rA].forEach(function (r) { r.addEventListener('input', draw); });
    Array.prototype.forEach.call(root.querySelectorAll('input[name="timbre-son"]'), function (r) { r.addEventListener('change', draw); });
    setup(); onResize(setup);
  })();
  /* ---------------- 3. Règle logarithmique ---------------- */
  (function () {
    var root = document.getElementById('lab-log');
    if (!root) { return; }
    var r = root.querySelector('input[type="range"]'), mark = root.querySelector('.lab-mark');
    var oX = root.querySelector('.out-x'), oP = root.querySelector('.out-p'), oL = root.querySelector('.out-l');
    function fmt(x) {
      if (x >= 999.5) { return '1\u202f000'; }
      return parseFloat(x.toPrecision(3)).toString().replace('.', ',');
    }
    function upd() {
      var v = parseFloat(r.value), x = Math.pow(10, v);
      mark.setAttribute('transform', 'translate(' + (100 + (v + 2) * 106).toFixed(1) + ',0)');
      oX.textContent = fmt(x);
      oP.innerHTML = '10<sup>' + minus(fr(v, 2)) + '</sup>';
      oL.textContent = minus(fr(v, 2));
    }
    r.addEventListener('input', upd); upd();
  })();
  /* ---------------- 4. Échelle des décibels ---------------- */
  (function () {
    var root = document.getElementById('lab-db');
    if (!root) { return; }
    var r = root.querySelector('input[type="range"]'), mark = root.querySelector('.lab-mark');
    var oL = root.querySelector('.out-L'), oI = root.querySelector('.out-I'), oR = root.querySelector('.out-r'), msg = root.querySelector('.nt-msg');
    function upd() {
      var L = parseFloat(r.value), I = 1e-12 * Math.pow(10, L / 10), m = nearest(L);
      mark.setAttribute('transform', 'translate(' + (60 + 5 * L) + ',0)');
      oL.textContent = L + ' dB';
      oI.innerHTML = sci(I, 1) + ' W\u00b7m<sup>\u22122</sup>';
      oR.innerHTML = '10<sup>' + fr(L / 10, 1) + '</sup>';
      msg.textContent = 'Repère le plus proche : ' + m[1] + ' (\u2248 ' + m[0] + ' dB).';
    }
    r.addEventListener('input', upd); upd();
  })();
  /* ---------------- 5. Sources identiques ---------------- */
  (function () {
    var root = document.getElementById('lab-src');
    if (!root) { return; }
    var N = 1, Lt = 60;
    var dots = root.querySelector('.nt-dots'), bI = root.querySelector('.nt-bar-I > div'), bL = root.querySelector('.nt-bar-L > div');
    var oI = root.querySelector('.out-I'), oL = root.querySelector('.out-L'), msg = root.querySelector('.nt-msg');
    function upd(note) {
      var L = Lt + 10 * Math.log10(N);
      dots.innerHTML = new Array(N + 1).join('<i></i>');
      bI.style.width = N + '%';
      bL.style.width = (L / 100 * 100) + '%';
      oI.innerHTML = N + ' \u00d7 <i>I</i><sub>t</sub>';
      oL.textContent = fr(L, 1) + ' dB';
      var base = N === 1 ? 'Une seule source : 60 dB.' :
        'Intensité multipliée par ' + N + ', mais seulement + ' + fr(10 * Math.log10(N), 1) + ' dB.';
      msg.textContent = note ? note + ' ' + base : base;
    }
    Array.prototype.forEach.call(root.querySelectorAll('button[data-op]'), function (b) {
      b.addEventListener('click', function () {
        var op = b.getAttribute('data-op'), old = N;
        if (op === '+1') { N += 1; } else if (op === '-1') { N -= 1; }
        else if (op === 'x2') { N *= 2; } else if (op === 'x10') { N *= 10; } else { N = 1; }
        N = Math.max(1, Math.min(100, N));
        var note = (N === 100 && old * (op === 'x10' ? 10 : op === 'x2' ? 2 : 1) > 100) ? '(Limité à 100 sources.)' : '';
        upd(note);
      });
    });
    upd();
  })();
  /* ---------------- 6. Atténuation géométrique ---------------- */
  (function () {
    var root = document.getElementById('lab-dist');
    if (!root) { return; }
    var P = 1e-2, X0 = 30, PX = 21;
    var r = root.querySelector('input[type="range"]');
    var sph = root.querySelector('.d-sph'), ray = root.querySelector('.d-ray'), ear = root.querySelector('.d-ear'), lab = root.querySelector('.d-lab');
    var oD = root.querySelector('.out-d'), oS = root.querySelector('.out-S'), oI = root.querySelector('.out-I'), oL = root.querySelector('.out-L'), msg = root.querySelector('.nt-msg');
    var bts = root.querySelectorAll('button[data-k]');
    function level(d) { return 10 * Math.log10(P / (4 * Math.PI * d * d) / 1e-12); }
    function upd(note) {
      var d = parseFloat(r.value), S = 4 * Math.PI * d * d, I = P / S, L = level(d), R = PX * d;
      sph.setAttribute('r', R.toFixed(1));
      sph.setAttribute('fill-opacity', Math.max(0.07, Math.min(0.6, 0.6 / (d * d))).toFixed(3));
      ray.setAttribute('x2', (X0 + R).toFixed(1));
      ear.setAttribute('cx', (X0 + R).toFixed(1));
      lab.setAttribute('x', (X0 + R / 2).toFixed(1));
      oD.textContent = fr(d, 1) + ' m';
      oS.textContent = (S < 100 ? fr(S, 1) : Math.round(S).toLocaleString('fr-FR')) + ' m\u00b2';
      oI.innerHTML = sci(I, 1) + ' W\u00b7m<sup>\u22122</sup>';
      oL.textContent = Math.round(L) + ' dB';
      Array.prototype.forEach.call(bts, function (b) {
        var nd = d * parseFloat(b.getAttribute('data-k'));
        b.disabled = (nd > 20.0001 || nd < 0.9999);
      });
      msg.textContent = note || '';
    }
    r.addEventListener('input', function () { upd(''); });
    Array.prototype.forEach.call(bts, function (b) {
      b.addEventListener('click', function () {
        var k = parseFloat(b.getAttribute('data-k')), d = parseFloat(r.value), L0 = level(d);
        r.value = d * k;
        var dL = level(parseFloat(r.value)) - L0;
        upd('Distance \u00d7 ' + fr(k, k < 1 ? 1 : 0) + ' : intensité ' + (k > 1 ? '\u00f7 ' + (k * k) : '\u00d7 ' + Math.round(1 / (k * k))) + ', soit ' + (dL < 0 ? '\u2212 ' : '+ ') + fr(Math.abs(dL), 0) + ' dB.');
      });
    });
    upd('');
  })();
})();
</script>
