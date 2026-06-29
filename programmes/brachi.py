scene.width=800
scene.height=500
Ly = 2
L = Ly/2*(11/8*pi-sin(11/8*pi))
scene.center.x = L/2 
scene.center.y = -Ly/2
scene.range = 2

running = False

label(pos=vec(L/2,0.2,0),text="Vous pouvez changer l'allure de la courbe\n en déplaçant les petits points bleus", xoffset=0,yoffset=0, space=0,height=15, border=5, box=False, color=vec(0.8,0.8,1))


# Nettoie un contour avant triangulation : retire les points dupliqués et les
# points colinéaires qui font planter poly2tri ("Intersecting Constraints").
def contour_propre(poly):
    # 1) retirer les points consécutifs identiques. Pas de "not pts" ni de pts[-1] :
    #    GlowScript traite [] comme VRAI (sémantique JS), donc on teste len().
    pts = []
    for q in poly:
        m = len(pts)
        if m == 0 or q[0] != pts[m-1][0] or q[1] != pts[m-1][1]:
            pts.append([q[0], q[1]])
    # 2) retirer les points colinéaires (cyclique). Pas de dépaquetage "x,y = ..."
    #    (autre construction qui peut appeler __getitem__ sur un tableau brut).
    n = len(pts)
    if n >= 4:
        out = []
        for i in range(n):
            a0 = pts[(i-1+n) % n]
            a1 = pts[i]
            a2 = pts[(i+1) % n]
            aire = (a1[0]-a0[0])*(a2[1]-a0[1]) - (a1[1]-a0[1])*(a2[0]-a0[0])
            if abs(aire) >= 1e-7:
                out.append([a1[0], a1[1]])
        pts = out
    # 3) refermer le contour : extrusion exige premier point == dernier
    k = len(pts)
    if k >= 1 and (pts[k-1][0] != pts[0][0] or pts[k-1][1] != pts[0][1]):
        pts.append([pts[0][0], pts[0][1]])
    return pts


def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
    
bbutton=button(text="Run", pos=scene.title_anchor, bind=Run)

def Reset(c):
    global  t, ball

    t = 0
    ball.pos=p[0].pos+vec(0,Rball,-0.1)
    ball.v=vec(0,0,0)
    tlabel.text="t = {:} s".format(t)
    
cbutton = button(text="Reset", pos=scene.title_anchor, bind=Reset)


rcylindre = 0.006
rball = 0.02
g = vec(0,-9.8,0)
a = vec(0,0,0)


p=[]
track=[]
socle=[]

start = vector(Ly/2*(0-sin(0)),-Ly/2*(1-cos(0)),0)
end = vector(Ly/2*(11/8*pi-sin(11/8*pi)),-Ly/2*(1-cos(11/8*pi)),0)

brach = sphere(pos=start, radius=.5*rball, color=color.yellow, make_trail=True)
theta = 0
while theta<=11*pi/8:
    rate(1000)
    xb = Ly/2*(theta-sin(theta))
    yb = -Ly/2*(1-cos(theta))
    theta += 11*pi/8/1000
    brach.pos = vec(xb,yb,0)


k = 0
nb_pts = 10
theta = 0
while theta<=11*pi/8:
    xp = Ly/2*(theta-sin(theta))
    yp = -Ly/2*(1-cos(theta))
    theta += 10*pi/8/nb_pts
    k += 1
    if k==2 :
      continue
    p += [sphere(pos=vec(xp,yp,0), radius=rball, color=vec(0.2,0.4,0.7), visible = True)]

#p += [sphere(pos=end, radius=rball, color=vec(0.2,0.4,0.7),visible=True)]

N = len(p)

colorsocle = vec(0.5,0.7,0.8)
for i in range(N):
  socle.append([p[i].pos.x,p[i].pos.y])
socle.append([p[-1].pos.x,-Ly-0.2])
socle.append([p[0].pos.x,-Ly-0.2])
# (le point de fermeture est ajouté par contour_propre, qui referme le contour)
ex = extrusion(path=[vec(0,0,0), vec(0,0,-0.2)], shape=contour_propre(socle), color=colorsocle)
track += [cylinder(pos=p[0].pos, axis=p[1].pos-p[0].pos, radius=rcylindre, visible=True)]

for j in range(1,N-1,1):
    track += [cylinder(pos=p[j].pos, axis=p[j+1].pos-p[j].pos, radius=rcylindre, visible=True)]


Rball = rball*5
ball = sphere(pos=p[0].pos+vec(0,Rball,-0.1), radius=Rball, color=vec(1,0.2,0.2))
ball.v = vector(0,0,0)

t = 0
dt = 0.0002

tlabel = label(pos=p[-1].pos, text="t = {:} s".format(t), xoffset=0, yoffset=50, line=False, color=vec(1,0.8,0.8))

drag = False
R = vector(0,0,0)
scene.bind("mousedown", def():
    global drag
    drag = True
    
    scene.bind("mouseup", def():
        global drag
        drag = False
    )
)

N = len(p)

while True:
    rate(5000)
    
    if drag:
        
        R = scene.mouse.pos
        for k in range(N-2):
            if mag(p[k+1].pos-R)<2e-1:
                if R.y>0:
                  p[k+1].pos.y = min(R.y,-0.1)
                else :
                  p[k+1].pos.y = max(R.y,-Ly-0.099)
                socle[k+1] = [p[k+1].pos.x,p[k+1].pos.y]
                track[k].axis = p[k+1].pos-p[k].pos
                track[k+1].pos.y = p[k+1].pos.y
                track[k+1].axis = p[k+2].pos-p[k+1].pos
        ex.visible = False
        ex = extrusion(path=[vec(0,0,0), vec(0,0,-0.2)], shape=contour_propre(socle), color=colorsocle)

    if running:
        
        for j in range(N-1):
            if ball.pos.x>=(p[j].pos.x):
               ball.v = mag(ball.v)*norm(p[j+1].pos-p[j].pos)
               a = dot(g,norm(p[j+1].pos-p[j].pos))*norm(p[j+1].pos-p[j].pos)

        ball.v += a*dt

        if ball.pos.x>=p[-1].pos.x*.9999:
            ball.v = vector(0,0,0)
        else:
            ball.pos += ball.v*dt
            t = t + dt
            tlabel.text = "t = {:.3f} s".format(t)
