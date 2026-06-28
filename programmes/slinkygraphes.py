Web VPython 3.2

largeur, hauteur = 300,600
scene.width,scene.height = 0,0
scene.align = 'none'
scene.visible = False
def generate_rainbow_colors(num_colors):
    colors = []
    for i in range(num_colors):
        # Calculez la valeur de la teinte (H) en fonction de la position dans l'arc-en-ciel
        hue = i * 360.0 / num_colors
        
        # Convertissez la teinte en RVB
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
        
        # Ajoutez la couleur à la liste sous forme de liste [R, G, B]
        colors.append([r/255, g/255, b/255])
    
    return colors
    
    
Disques = []
N = 20
ep = 0.1
R = 2

Couleurs = generate_rainbow_colors(N)
for i in range(N):
    Disques.append(cylinder(pos=vector(0,20-i,0),axis=vector(0,ep,0),radius=R,v=vec(0,0,0),a=vec(0,0,0),color=vec(Couleurs[i][0],Couleurs[i][1],Couleurs[i][2])))


Gpos = graph(width=largeur, height=hauteur, title='<b>Position</b>',xtitle='<i>t</i>', ytitle='y',align='left',fast=False)
PlotsY = []
for i in range(N):
    PlotsY.append(gcurve(graph=Gpos,color=vec(Couleurs[i][0],Couleurs[i][1],Couleurs[i][2])))
PlotYtot = gcurve(graph=Gpos,color=vec(0.4,0.4,0.4),width=5)

Gvit = graph(width=largeur, height=hauteur, title='<b>Vitesse</b>',xtitle='<i>t</i>', ytitle='v<sub>y</sub>',align='left',fast=False)
PlotsVy = []
for i in range(N):
    PlotsVy.append(gcurve(graph=Gvit,color=vec(Couleurs[i][0],Couleurs[i][1],Couleurs[i][2])))
PlotVtot = gcurve(graph=Gvit,color=vec(0.4,0.4,0.4),width=5)

Ga = graph(width=largeur, height=hauteur, title='<b>Accélération</b>',xtitle='<i>t</i>', ytitle='a<sub>y</sub>',align='left',fast=False)
PlotsAy = []
for i in range(N):
    PlotsAy.append(gcurve(graph=Ga,color=vec(Couleurs[i][0],Couleurs[i][1],Couleurs[i][2])))
PlotAtot = gcurve(graph=Ga,color=vec(0.4,0.4,0.4),width=5)

m = 1 # masse disque
g = vec(0,-9.8,0)
haut = 1
bas = N-1
t = 0
dt = 5e-4

while t<1:
    rate(0.5/dt)
    for i in range(haut):
        Disques[i].a = (m*bas*g + m*haut*g)/(m*haut)
        Disques[i].v += Disques[i].a*dt
        Disques[i].pos += Disques[i].v*dt
        if (haut != N) and (Disques[haut-1].pos.y < Disques[haut].pos.y+ep+0.01):
            Disques[haut].v = Disques[haut-1].v
            haut += 1
            bas = N - haut
            break
    Ytot = vec(0,0,0)
    Vtot = vec(0,0,0)
    Atot = vec(0,0,0)
    for i in range(N):
        PlotsY[i].plot(t,Disques[i].pos.y)
        PlotsVy[i].plot(t,m*Disques[i].v.y)
        PlotsAy[i].plot(t,m*Disques[i].a.y)
        Atot += Disques[i].a*m
        Ytot += Disques[i].pos*m
        Vtot += Disques[i].v*m
    Atot /= m*N
    Vtot /= m*N
    Ytot /= m*N
    PlotVtot.plot(t,Vtot.y)
    PlotYtot.plot(t,Ytot.y)
    PlotAtot.plot(t,Atot.y)
    t += dt