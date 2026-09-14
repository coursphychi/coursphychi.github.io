# =============================================
# TEST DE LA DEUXIÈME LOI DE KEPLER SUR MERCURE
# =============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Charger les données -------------------------------------------------
FILENAME = "ephemerides.csv"           # le fichier doit être dans le même dossier
df = pd.read_csv(FILENAME, sep=';')    # données exportées avec des « ; »

# On récupère la date et la position x, y (en unités astronomiques = UA)
dates_iso = df['Date (undefined)']
x = df['px (au)'].values
y = df['py (au)'].values

# Pour un affichage plus compact des dates : 1/3/25
def format_date(iso):
    ymd = iso.split('T')[0]              # "2025-03-01"
    y, m, d = map(int, ymd.split('-'))
    return f"{d}/{m}/{str(y)[-2:]}"      # "1/3/25"
dates = [format_date(s) for s in dates_iso]

# 2) Calcul des aires en UA² --------------------------------------------
areas = []
for i in range(len(x)-1):
    # Formule de l’aire d’un triangle (produit vectoriel 2D)
    area = 0.5 * abs(x[i]*y[i+1] - y[i]*x[i+1])
    areas.append(area)

# 3) Tracé ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 7),dpi=250)
ax.set_aspect('equal')
ax.axis('off')

couleurs = ['#0076BA', '#FF42A1']     # bleu puis rose
alpha  = 0.4                          # transparence

# Secteurs colorés
for i in range(len(x)-1):
    ax.fill((0,x[i],x[i+1]),(0,y[i],y[i+1]), color=couleurs[i % 2], alpha=alpha, edgecolor='none')
    # Rayon pointillé vers la position i
    ax.plot([0, x[i]], [0, y[i]], ls='--', lw=0.7, c='grey')

# Dernier rayon
ax.plot([0, x[-1]], [0, y[-1]], ls='--', lw=0.7, c='grey', alpha=0.7)

# Positions et dates (décalage léger pour ne pas coller le point)
ax.scatter(x, y, s=45, c='#00A2FF', zorder=3)
for xi, yi, t in zip(x, y, dates):
    r = np.hypot(xi, yi)
    ax.text(xi*1.05, yi*1.05, t, fontsize=6, ha='center', va='center')

# Soleil
ax.scatter(0, 0, s=120, c='#FFD932', zorder=4)

plt.show()

# 4) Affichage des aires --------------------------------------------------
print("Aires balayées entre positions successives (UA²) :")
for d1, d2, a in zip(dates[:-1], dates[1:], areas):
    print(f"{d1} → {d2} : {a:.4e}")
print(f"\nMoyenne des aires = {np.mean(areas):.4e} UA²")
print(f"incertitude-type = {np.std(areas,ddof=1)/np.sqrt(len(areas)):.1e}  UA²")