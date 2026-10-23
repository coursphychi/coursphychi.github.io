---
title: "Partie python du TP"
date: 2021-03-06T14:23:56+01:00
draft: false
hidden: true
---

<style>
ul {
  text-align: left;
}
table {
  border-collapse: collapse;
  border: 0;
}
td, th {
  border-collapse: collapse;
  text-align: center;
  vertical-align: middle;
}
</style>

## Lien entre masse et poids

- Dans le programme suivant, il faut dans un premier temps que vous modifiiez la liste des masses (`masses`) et la liste des poids (`poids`) avec vos propres valeurs.

- Exécuter le programme et constater que les deux droites ne prennent pas vos points en sandwich.

- Modifier alors `borne_inf` et `borne_sup` pour que cela soit le cas (et le plus serré possible).


{{< runpython lang="pyodide" height="auto">}}
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# liste des masses (en kg)
masses = [0.100,0.200,0.300,0.400,0.500]
# liste des poids correspondants (en N)
poids = [2.1,4.3,6.2,8.9,10.9]

###################### PARTIE À MODIFIER ################################
borne_inf = 12  # plus petit coefficient directeur
borne_sup = 30  # plus grand coefficient dirrecteur
#########################################################################

# Création du graphique
fig = go.Figure()

coefficients = [borne_inf,borne_sup]
x_vals = np.linspace(0, max(masses), 100)  # Valeurs de x pour tracer les fonctions linéaires

# Tracé des droites
for coeff in coefficients:
    y_vals = coeff * x_vals
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines',
                             hovertemplate=f'Coefficient = {coeff:.2f}<extra></extra>',
                             name=f'Coefficient = {coeff:.2f}'))

# Ajout des points de coordonnées (masse, poids)
fig.add_trace(go.Scatter(x=masses, y=poids, mode='markers', name='Mesures', marker_color="crimson", marker_size=10, marker_symbol='x'))

# Ajout du titre du graphique et des axes
fig.update_layout(title_text="Poids en fonction de la masse", title_x=0.5, height=800)
fig.update_xaxes(title_text='masse (kg)')
fig.update_yaxes(title_text='poids (N)')

# Affichage du graphique
fig.show()
{{< /runpython >}}
