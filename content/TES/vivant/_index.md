+++
title = "Une histoire du vivant"
date = 2021-03-06T14:20:50+01:00
weight = 3
chapter = true

+++

<script>
window.onload = function() {
    document.getElementById('imageCliqueable').addEventListener('click', function(event) {
        event.preventDefault(); // Empêche l'action par défaut
        event.stopPropagation(); // Empêche la propagation de l'événement
        var audioPlayer = document.getElementById('audioPlayer');
        if (audioPlayer.paused) {
            audioPlayer.play();
        } else {
            audioPlayer.currentTime = 0;
        }
    });
};
</script>

# Une histoire du vivant

## [Les modèles démographiques](./demographie/)



- Passé et futur
- Croissance exponentielle
- Stagnation et décroissance


---

## [Intelligence Artificielle](./ia/)

<div style="position:relative; width:300px; max-width: 100%; margin-left: auto;margin-right: auto; cursor:pointer !important;">
<img src="/hal.png"  id="imageCliqueable" style="border-radius:50%; cursor:pointer !important; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
</div>

<audio id="audioPlayer" src="/cantdo.mp3"></audio>

- Histoire de l'IA
- Apprentissage machine (KNN et K-Means)
- IA et éthique


---

## [Inférences bayésiennes](./bayes/)



- Motivation
- Théorème de Bayes
- Exemples
- Aide au diagnostic médical
