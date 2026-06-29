scene.userzoom=False
L = 700
scene.width=L 
scene.height=L/3
scene.align = 'left'
scene.background = vec(0.9,0.9,0.9)  # couleur du fond

# parametres :
rayon_masse = 0.02
rayon_ressort = 0.008
l0 = 0.1              # m 
k = 20                # N/m 
masse = 0.20          # kg
x0 = 2*l0             # m
v0 = 0                # m/s
g = 9.81              # m/s2
mu = 0.02             #
h = 0.2               # Ns/m
cx = 0.47             #
A = pi*rayon_masse**2 # m2
rho = 1.2             # kg/m3

# initialisation :
t = 0
ressort = helix(pos = vec(0, 0, 0), axis = vec(x0, 0, 0))
ressort.radius = 0.008
ressort.coils = 15
vitesse = vec(v0,0,0)   # v0 = 0 m/s
M = cylinder(color = vec(0.2,0.4,0.8)) 
M.radius = 0.02
M.pos = ressort.pos + ressort.axis
M.axis = vec(0.02, 0, 0)

dt = 0.001     

table = box(pos = vec(l0-rayon_masse/2,-rayon_masse-rayon_masse/2,0), axis = vec(1,0,0), size = vec(l0*2+rayon_masse, rayon_masse, 0.05), color=vec(0.6,0.6,0.6))
mur = box(pos = vec(-rayon_masse/2, 0, 0), size = vec(rayon_masse, rayon_masse*2, 0.05), color = vec(0.6,0.6,0.6))

scene.center = vec(l0,0,0)    # position de la camera 

# graphes :
g1=graph(width=L/2, height=L/2, align='left', fast = False, xtitle='<i>t</i>', ytitle='<i>x</i>')
g2=graph(width=L/2, height=L/2, align='left', fast = False, xtitle='<i>x</i>',ytitle='<i>v</i><sub>x</sub>')
posgraph = gcurve(graph=g1,color=vec(0.2,0.4,0.8))
polgraph = gcurve(graph=g2,color=color.red)

# evolution :
while(t<10):
    rate(1.5/dt)        
    t = t + dt  
    # forces agissant sur la masse :
    force_rappel = -k * (M.pos - l0 * M.pos.norm())
    frottements_solides = - mu * masse * g * vitesse.norm() 
    frottements_fluides = - h * vitesse
    frottements_trainee = - 0.5*cx*rho*A*vitesse*vitesse.mag*1e4
    
    force_resultante = force_rappel + frottements_fluides          

    # incrementation de la vitesse en suivant la methode d'Euler (2eme loi de Newton) :
    vitesse = vitesse + (force_resultante / masse) * dt
    # incrementation de la position :
    M.pos = M.pos + vitesse * dt      

    # ajuster le ressort :
    ressort.axis = M.pos   
    
    # graphes :
    posgraph.plot(pos=(t, M.pos.x))
    polgraph.plot(pos=(M.pos.x, vitesse.x))
