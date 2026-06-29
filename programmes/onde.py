scene.width,scene.height = 800,550

# fonction gérant les couleurs des anneaux
def fabrique_couleurs(nb_couleurs):
    couleurs = []
    for i in range(nb_couleurs):
        hue = i * 360.0 / nb_couleurs
        r, g, b = 0, 0, 0
        if 0 <= hue < 60:
            r = 255
            g = int(255 * (hue / 60))
        elif 60 <= hue < 120:
            r = 255 - int(255 * ((hue - 60) / 60))
            g = 255
        elif 120 <= hue < 180:
            g = 255
            b = int(255 * ((hue - 120) / 60))
        elif 180 <= hue < 240:
            g = 255 - int(255 * ((hue - 180) / 60))
            b = 255
        elif 240 <= hue < 300:
            r = int(255 * ((hue - 240) / 60))
            b = 255
        else:
            r = 255
            b = 255 - int(255 * ((hue - 300) / 60))
        couleurs.append([r/255, g/255, b/255])
    return couleurs

# Initialisation des listes
Anneaux = []
Ressorts = []

# Paramètres :
N = 50      # nombre d'anneaux
ep = 0.01   # épaisseur d'un anneau (en m)
R = 0.8     # rayon d'un anneau (en m)
d = 0.1     # distance entre les anneaux (en m)
c = 2       # célérité de l'onde (en m/s)
A = d/2     # amplitude de l'onde (en m)
f = 2       # fréquence de l'onde (en Hz)

scene.center = vec((N-1)*d/2,0,0)

# Liste des positions des anneaux sur l'axe des x :
Positions = [i*d for i in range(N)]

# Construction des anneaux et ressorts dans les deux listes dédiées :
Couleurs = fabrique_couleurs(N)
for i in range(N):
    Anneaux.append(extrusion(path=[vec(0,0,0), vec(ep,0,0)], shape=shapes.circle(radius=R, thickness=R/5),pos=vec(Positions[i],0,0), axis=vec(1,0,0), color=vec(Couleurs[i][0],Couleurs[i][1],Couleurs[i][2])))
for i in range(N-1):
    Ressorts.append(helix(pos=Anneaux[i].pos, axis=Anneaux[i+1].pos-Anneaux[i].pos, radius=.9*R, coils=5, thickness=R/100))


# MOUVEMENT :
t = 0          # temps en s
dt = 1e-3      # en s
while t < 2/f:
    rate(1/dt)   # vitesse de l'animation
    for i in range(N):
        Anneaux[i].pos.x = i*d + A*sin(2*pi*f*t) # position de l'anneau i sur l'axe des x
    for i in range(N-1):
        Ressorts[i].pos = Anneaux[i].pos
        Ressorts[i].axis = Anneaux[i+1].pos - Anneaux[i].pos
    t += dt