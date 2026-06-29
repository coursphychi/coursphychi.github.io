# Paramètres
l = 1
m = 2
O = vec(0, 0, 0)
N = 10
k = 2e7
masse_corde = 0.01
alpha = 0.02
g = vec(0, -9.81, 0)

# Configuration de la scène
scene.width,scene.height = 800,600
scene.background = vec(4,63,97)/255
scene.range = 2*l
scene.center = O

# Masse finale M
M = sphere(pos=vec(0, -l, 0), color=vec(1, 0, 0), emissive=True, radius=l/20, make_trail=True)
M.m = m
v0 = 0
M.v = vec(v0, 0, 0)

# Initialisation des points de la corde
X = [sphere(pos=O, visible=True, radius=l/20, color=vec(0, 0, 0), emissive=True)]
X += [sphere(pos=vec(0, -l*i/N, 0), visible=False, m=masse_corde/N, v=vec(0, 0, 0)) for i in range(1, N)]
X.append(M)

# Initialisation des courbes
points = [p.pos for p in X]
C = curve(points)

# Initialisation des forces
F = [vec(0, 0, 0) for _ in range(N+1)]

# Fonction pour calculer la force de rappel entre deux points
def force_rappel(p1, p2, l0, k):
    deplacement = p1 - p2
    longueur = mag(deplacement)
    allongement = longueur - l0
    # Pour éviter la division par zéro
    if allongement != 0:
        force = -k * allongement * norm(deplacement)
    else:
        force = vec(0, 0, 0)
    return force

# Boucle de simulation
t = 0
dt = 5e-6
test = True
while True :
    rate(10/dt)
  
    # Calcul des forces pour les points intermédiaires
    for i in range(1,N):
        # force due au point précédent
        force_prec = force_rappel(X[i].pos, X[i-1].pos, l/N, k)
        # force due au point suivant
        force_suiv = force_rappel(X[i].pos, X[i+1].pos, l/N, k)
        # Somme des forces
        F[i] = force_prec + force_suiv
  
    # Force sur la pierre
    F_M = M.m * g + force_rappel(M.pos, X[N-1].pos, l/N, k)
  
    # Mise à jour de la vitesse et de la position de M
    M.v += F_M/M.m*dt
    M.pos += M.v*dt
    X[N] = M

    # Mise à jour des forces et des positions des points intermédiaires
    for i in range(1,N) :
        X[i].v += (X[i].m*g+F[i]-alpha*X[i].v*mag(X[i].v))/X[i].m*dt
        X[i].pos += X[i].v*dt

    # Mise à jour de la courbe
    for i in range(N+1) :
        C.modify(i,pos=X[i].pos)
    t += dt
