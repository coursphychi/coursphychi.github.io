---
title: "Bac à sable Python"
description: "Environnement d'exécution Python, Pyodide et VPython directement dans le navigateur."
hidden: "true"
---

<style>
  :root {
    --sb-bg-card: #f8fafc;
    --sb-bg-hover: #f1f5f9;
    --sb-border: #e2e8f0;
    --sb-text: #0f172a;
    --sb-muted: #475569;
    --sb-accent-skulpt: #3b82f6;
    --sb-accent-pyodide: #8b5cf6;
    --sb-accent-vpython: #10b981;
    --sb-tag-bg: #e2e8f0;
    --sb-tag-text: #334155;
    --sb-warn-bg: rgba(245, 158, 11, 0.12);
    --sb-warn-border: rgba(245, 158, 11, 0.4);
    --sb-warn-text: #b45309;
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --sb-bg-card: #1e293b;
      --sb-bg-hover: #263449;
      --sb-border: #334155;
      --sb-text: #f8fafc;
      --sb-muted: #94a3b8;
      --sb-tag-bg: #0f172a;
      --sb-tag-text: #cbd5e1;
      --sb-warn-bg: rgba(245, 158, 11, 0.1);
      --sb-warn-border: rgba(245, 158, 11, 0.3);
      --sb-warn-text: #fbbf24;
    }
  }

  /* Support explicite si ton thème Hugo utilise une classe .dark ou data-theme="dark" */
  html.dark, [data-theme="dark"] {
    --sb-bg-card: #1e293b;
    --sb-bg-hover: #263449;
    --sb-border: #334155;
    --sb-text: #f8fafc;
    --sb-muted: #94a3b8;
    --sb-tag-bg: #0f172a;
    --sb-tag-text: #cbd5e1;
    --sb-warn-bg: rgba(245, 158, 11, 0.1);
    --sb-warn-border: rgba(245, 158, 11, 0.3);
    --sb-warn-text: #fbbf24;
  }

  .sb-intro {
    text-align: center;
    max-width: 720px;
    margin: 0 auto 2rem auto;
    color: var(--sb-muted);
    font-size: 1.05rem;
    line-height: 1.6;
  }

  /* Grille de sélection */
  .sb-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
    gap: 1.25rem;
    margin-bottom: 1.75rem;
  }

  .sb-card {
    background: var(--sb-bg-card);
    border: 2px solid var(--sb-border);
    border-radius: 14px;
    padding: 1.35rem;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: left;
    position: relative;
    overflow: hidden;
  }

  .sb-card:hover {
    background: var(--sb-bg-hover);
    transform: translateY(-3px);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.15);
  }

  .sb-card[data-engine="skulpt"].active {
    border-color: var(--sb-accent-skulpt);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25);
  }
  .sb-card[data-engine="pyodide"].active {
    border-color: var(--sb-accent-pyodide);
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.25);
  }
  .sb-card[data-engine="vpython"].active {
    border-color: var(--sb-accent-vpython);
    box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.25);
  }

  .sb-card-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
  }

  .sb-icon {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
  }

  .sb-card[data-engine="skulpt"] .sb-icon { background: rgba(59, 130, 246, 0.15); color: var(--sb-accent-skulpt); }
  .sb-card[data-engine="pyodide"] .sb-icon { background: rgba(139, 92, 246, 0.15); color: var(--sb-accent-pyodide); }
  .sb-card[data-engine="vpython"] .sb-icon { background: rgba(16, 185, 129, 0.15); color: var(--sb-accent-vpython); }

  .sb-card-title {
    font-weight: 700;
    font-size: 1.15rem;
    color: var(--sb-text);
    margin: 0;
    line-height: 1.25;
  }

  .sb-card-engine {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 600;
    opacity: 0.75;
  }

  .sb-card-desc {
    font-size: 0.92rem;
    color: var(--sb-muted);
    margin: 0 0 1.1rem 0;
    line-height: 1.5;
  }

  .sb-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: auto;
  }

  .sb-tag {
    background: var(--sb-tag-bg);
    color: var(--sb-tag-text);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.76rem;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    font-weight: 500;
  }

  /* Bandeau d'avertissement */
  .sb-notice {
    display: none;
    align-items: center;
    gap: 0.75rem;
    background: var(--sb-warn-bg);
    border: 1px solid var(--sb-warn-border);
    color: var(--sb-warn-text);
    padding: 0.75rem 1.1rem;
    border-radius: 10px;
    font-size: 0.9rem;
    margin-bottom: 1.25rem;
    line-height: 1.4;
  }

  .sb-notice.visible {
    display: flex;
  }

  /* Conteneur pleine largeur adaptatif pour l'éditeur */
  .sb-workspace-wrapper {
    width: min(94vw, 1300px);
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    margin-top: 0.5rem;
    margin-bottom: 3rem;
  }

  .sb-pane {
    display: none;
    width: 100%;
  }

  .sb-pane.active {
    display: block;
    animation: sbFadeIn 0.25s ease-out;
  }

  @keyframes sbFadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @media (max-width: 640px) {
    .sb-workspace-wrapper {
      width: 98vw;
    }
    .sb-card {
      padding: 1.1rem;
    }
  }
</style>

<p class="sb-intro">
  Choisissez l'environnement adapté à votre programme pour ouvrir l'éditeur. Tout s'exécute directement dans votre navigateur, sans aucune installation.
</p>

<div class="sb-grid" role="tablist" aria-label="Choix du moteur Python">
  <!-- Carte 1 : Skulpt -->
  <div class="sb-card" data-engine="skulpt" role="tab" tabindex="0" onclick="selectEngine('skulpt')" onkeydown="if(event.key==='Enter'||event.key===' ')selectEngine('skulpt')">
    <div>
      <div class="sb-card-header">
        <div class="sb-icon">⚡</div>
        <div>
          <div class="sb-card-engine">Skulpt</div>
          <h3 class="sb-card-title">Python standard</h3>
        </div>
      </div>
      <p class="sb-card-desc">
        Idéal pour l'algorithmique, les structures de base, les calculs simples et le dessin géométrique. Démarrage instantané.
      </p>
    </div>
    <div class="sb-tags">
      <span class="sb-tag">math</span>
      <span class="sb-tag">random</span>
      <span class="sb-tag">turtle</span>
      <span class="sb-tag">time</span>
    </div>
  </div>

  <!-- Carte 2 : Pyodide -->
  <div class="sb-card" data-engine="pyodide" role="tab" tabindex="0" onclick="selectEngine('pyodide')" onkeydown="if(event.key==='Enter'||event.key===' ')selectEngine('pyodide')">
    <div>
      <div class="sb-card-header">
        <div class="sb-icon">📈</div>
        <div>
          <div class="sb-card-engine">Pyodide</div>
          <h3 class="sb-card-title">Python scientifique</h3>
        </div>
      </div>
      <p class="sb-card-desc">
        Pour le traitement de données expérimentales, les tracés de courbes, les régressions, Monte-Carlo et le calcul matriciel ou formel.
      </p>
    </div>
    <div class="sb-tags">
      <span class="sb-tag">numpy</span>
      <span class="sb-tag">matplotlib</span>
      <span class="sb-tag">plotly</span>
      <span class="sb-tag">scipy</span>
      <span class="sb-tag">pandas</span>
      <span class="sb-tag">sympy</span>
      <span class="sb-tag">seaborn</span>
    </div>
  </div>

  <!-- Carte 3 : VPython -->
  <div class="sb-card" data-engine="vpython" role="tab" tabindex="0" onclick="selectEngine('vpython')" onkeydown="if(event.key==='Enter'||event.key===' ')selectEngine('vpython')">
    <div>
      <div class="sb-card-header">
        <div class="sb-icon">🪐</div>
        <div>
          <div class="sb-card-engine">GlowScript</div>
          <h3 class="sb-card-title">VPython 3D</h3>
        </div>
      </div>
      <p class="sb-card-desc">
        Pour la physique vectorielle et les animations 3D interactives (mécanique, champs, optique, cinématique) avec caméra manipulable à la souris.
      </p>
    </div>
    <div class="sb-tags">
      <span class="sb-tag">vector</span>
      <span class="sb-tag">sphere</span>
      <span class="sb-tag">arrow</span>
      <span class="sb-tag">box</span>
      <span class="sb-tag">rate</span>
      <span class="sb-tag">graph</span>
    </div>
  </div>
</div>

<!-- Bandeau d'information sur le chargement -->
<div id="sb-notice" class="sb-notice" role="status">
  <span>⏳</span>
  <span id="sb-notice-text">
    <strong>Remarque :</strong> la première exécution peut prendre quelques secondes le temps de charger le moteur et les bibliothèques en mémoire, mais les exécutions suivantes seront beaucoup plus rapides.
  </span>
</div>

<!-- Zone d'affichage des shortcodes (pleine largeur) -->
<div class="sb-workspace-wrapper">

  <div id="pane-skulpt" class="sb-pane">
{{< runpython lang="python" height="auto" upload="true" theme="auto" >}}
# Python standard (Skulpt) — math, random, turtle, time...
from math import sqrt, pi

# Écrivez votre programme ci-dessous puis cliquez sur ▶




{{< /runpython >}}
  </div>

  <div id="pane-pyodide" class="sb-pane">
{{< runpython lang="pyodide" height="auto" upload="true" theme="auto" >}}
# Python scientifique (Pyodide) — numpy, matplotlib, plotly, scipy, pandas...
import numpy as np
import matplotlib.pyplot as plt

# Écrivez votre programme ci-dessous puis cliquez sur ▶




{{< /runpython >}}
  </div>

  <div id="pane-vpython" class="sb-pane">
{{< runpython lang="vpython" height="auto" theme="auto" >}}
# VPython 3D (GlowScript) — vector, sphere, box, arrow, rate, graph...
# Clic droit + glisser pour tourner la caméra, molette pour zoomer.

axe_x = arrow(pos=vector(0,0,0), axis=vector(2,0,0), color=color.red, shaftwidth=0.05)
axe_y = arrow(pos=vector(0,0,0), axis=vector(0,2,0), color=color.green, shaftwidth=0.05)
axe_z = arrow(pos=vector(0,0,0), axis=vector(0,0,2), color=color.blue, shaftwidth=0.05)

# Complétez votre scène 3D ci-dessous puis cliquez sur ▶




{{< /runpython >}}
  </div>

</div>

<script>
  (function() {
    // 1. Différer le chargement des iframes cachées au démarrage
    // Cela évite que CodeMirror ou VPython ne s'initialisent dans un conteneur de largeur 0px.
    document.addEventListener("DOMContentLoaded", function() {
      const panes = document.querySelectorAll(".sb-pane");
      panes.forEach(function(pane) {
        const iframe = pane.querySelector("iframe");
        if (iframe && iframe.getAttribute("src")) {
          iframe.setAttribute("data-src", iframe.getAttribute("src"));
          iframe.removeAttribute("src");
        }
      });

      // Permet de pré-sélectionner un moteur via l'URL : ?moteur=pyodide
      const params = new URLSearchParams(window.location.search);
      const preset = params.get("moteur") || params.get("lang");
      if (preset && ["skulpt", "pyodide", "vpython"].includes(preset)) {
        selectEngine(preset);
      }
    });

    // 2. Fonction d'activation d'un environnement
    window.selectEngine = function(engine) {
      // Mise à jour visuelle des cartes
      document.querySelectorAll(".sb-card").forEach(function(card) {
        const isCurrent = card.getAttribute("data-engine") === engine;
        card.classList.toggle("active", isCurrent);
        card.setAttribute("aria-selected", isCurrent ? "true" : "false");
      });

      // Affichage du bandeau de remarque adapté
      const notice = document.getElementById("sb-notice");
      const noticeText = document.getElementById("sb-notice-text");
      notice.classList.add("visible");

      if (engine === "pyodide") {
        noticeText.innerHTML = "<strong>Remarque :</strong> la première exécution prend quelques secondes car votre navigateur télécharge Python et les bibliothèques scientifiques (~20 Mo). Tout est ensuite gardé en cache : les exécutions suivantes seront quasi instantanées.";
      } else {
        noticeText.innerHTML = "<strong>Remarque :</strong> la première exécution est un peu plus lente le temps d'initialiser les bibliothèques, mais les exécutions suivantes sont immédiates.";
      }

      // Bascule des panneaux et chargement à la demande de l'iframe
      ["skulpt", "pyodide", "vpython"].forEach(function(key) {
        const pane = document.getElementById("pane-" + key);
        if (!pane) return;

        if (key === engine) {
          pane.classList.add("active");
          const iframe = pane.querySelector("iframe");
          if (iframe) {
            // Premier affichage : on déclenche le vrai chargement de player.html
            if (!iframe.getAttribute("src") && iframe.getAttribute("data-src")) {
              iframe.setAttribute("src", iframe.getAttribute("data-src"));
            } else if (iframe.contentWindow) {
              // Si déjà chargée auparavant, on force un recalcul de mise en page (CodeMirror / hauteur)
              iframe.contentWindow.dispatchEvent(new Event("resize"));
            }
          }
        } else {
          pane.classList.remove("active");
        }
      });
    };
  })();
</script>