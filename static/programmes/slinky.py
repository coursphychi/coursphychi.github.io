Web VPython 3.2

scene.width,scene.height = 800,600

def generate_rainbow_colors(num_colors):
    colors = []
    for i in range(num_colors):
        hue = i * 360.0 / num_colors
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
        colors.append([r/255, g/255, b/255])
    return colors

Disques = []
N = 20   # nombre de disques
ep = 0.1 # épaisseur des disques
R = 2    # rayon des disques

Couleurs = generate_rainbow_colors(N)
for i in range(N):
    Disques.append(cylinder(pos=vector(0,20-i,0),axis=vector(0,ep,0),radius=R,v=vec(0,0,0),a=vec(0,0,0),color=vec(Couleurs[i][0],Couleurs[i][1],Couleurs[i][2])))


m = 1 # masse disque
g = vec(0,-9.8,0)
n_haut = 1
n_bas = N-1
t = 0
dt = 5e-4

while t<1:
    rate(0.5/dt)
    for i in range(n_haut):
        Disques[i].a = (m*n_bas*g + m*n_haut*g)/(m*n_haut)
        Disques[i].v += Disques[i].a*dt
        Disques[i].pos += Disques[i].v*dt
        if (n_haut != N) and (Disques[n_haut-1].pos.y < Disques[n_haut].pos.y+ep+0.01):
            Disques[n_haut].v = Disques[n_haut-1].v
            n_haut += 1
            n_bas = N - n_haut
            break
    t += dt
  