GlowScript 2.9 VPython

scene.width=800
scene.height=500
Ly = 2
L = -Ly/2*(-pi-sin(-pi))
scene.center.x = L/2 
scene.center.y = -Ly/2
scene.range = 1.5
#scene.userzoom=False
#scene.userspin=False
#scene.userpan=False
#scene.axis = vec(0,0,0)

running = False

label(pos=vec(L/2,0.2,0),text='Vous pouvez changer la position initiale\n de la balle verte', xoffset=0,yoffset=0, space=0,height=15, border=5, box=False, color=vec(0.8,1,0.8))

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
    
bbutton=button(text="Run", pos=scene.title_anchor, bind=Run)

def Reset(c):
    global  t1, t2, ball1, ball2

    t1=t2=0
    ball1.pos=p[1].pos+vec(0,Rball,-0.05)
    ball2.pos=p[int(2*N/3)].pos+vec(0,Rball,-0.15)
    ball1.v=ball2.v=vector(0,0,0)
    tlabel1.text=tlabel2.text=t
    
cbutton = button(text="Reset", pos=scene.title_anchor, bind=Reset)


rcylindre = 0.006
rball = 0.02
g = vector(0,-9.8,0)
a1 = a2 = vector(0,0,0)

p=[]
track=[]
socle=[]

start = vector(-Ly/2*(-1/8*pi-sin(-1/8*pi)),-Ly/2*(1-cos(-1/8*pi)),0)
end = vector(-Ly/2*(-pi-sin(-pi)),-Ly/2*(1-cos(-pi)),0)

brach = sphere(pos=start, radius=.5*rball, color=color.yellow, make_trail=True, visible=False)
theta = -pi/8
k = 0
while theta>=-pi:
    xb = -Ly/2*(theta-sin(theta))
    yb = -Ly/2*(1-cos(theta))
    theta -= pi/1000
    brach.pos = vector(xb,yb,0)
    if k%2 == 0 :
      p=p+[sphere(pos=vec(xb,yb,0), radius=rball, color=vec(0.2,0.4,0.7), visible = False)]
    k += 1
    
p = p+[sphere(pos=end, radius=rball, color=vec(0.2,0.4,0.7),visible=False)]

N = len(p)

colorsocle=vec(0.5,0.7,0.8)
for i in range(N):
  socle.append([p[i].pos.x,p[i].pos.y])
socle.append([p[-1].pos.x,-Ly-0.2])
socle.append([p[0].pos.x,-Ly-0.2])
socle.append([p[0].pos.x,p[0].pos.y])
ex = extrusion(path=[vec(0,0,0), vec(0,0,-0.2)], shape=socle, color=colorsocle)

Rball = rball*2
ball1 = sphere(pos=p[1].pos+vec(0,Rball,-0.05), radius=Rball, color=vec(1,0.2,0.2))
ball2 = sphere(pos=p[int(2*N/3)].pos+vec(0,Rball,-0.15), radius=Rball, color=vec(0.2,0.9,0.2))
ball1.v = ball2.v = vector(0,0,0)

t1 = t2 = 0
dt = 0.0005

tlabel1=label(pos=p[-1].pos+vec(0,0.4,0), text=t1, xoffset=20, yoffset=-20, line=False, color=vec(1,0.8,0.8))
tlabel2=label(pos=p[-1].pos+vec(0,0,0), text=t1, xoffset=20, yoffset=-20, line=False, color=vec(0.8,1,0.8))

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
        for k in range(N):
            if R.x>(p[k].pos.x-L/N/2) and R.x<(p[k].pos.x+L/N/2):
              ball2.visible = False
              ball2 = sphere(pos=p[k].pos+vec(0,Rball,-0.15), radius=Rball, color=vec(0.2,0.9,0.2))
              ball2.v = vector(0,0,0)

    if running:
        
        for j in range(N-1):
            if ball1.pos.x>=(p[j].pos.x):
               ball1.v = mag(ball1.v)*norm(p[j+1].pos-p[j].pos)
               a1 = dot(g,norm(p[j+1].pos-p[j].pos))*norm(p[j+1].pos-p[j].pos)
            if ball2.pos.x>=(p[j].pos.x):
               ball2.v = mag(ball2.v)*norm(p[j+1].pos-p[j].pos)
               a2 = dot(g,norm(p[j+1].pos-p[j].pos))*norm(p[j+1].pos-p[j].pos)
               
        ball1.v += a1*dt
        ball2.v += a2*dt

        if ball1.pos.x>=p[-1].pos.x*.9999:
            ball1.v = vector(0,0,0)
        else:
            ball1.pos += ball1.v*dt
            t1 = t1 + dt
            tlabel1.text = t1
                
        if ball2.pos.x>=p[-1].pos.x*.9999:
            ball2.v = vector(0,0,0)
        else:
            ball2.pos += ball2.v*dt
            t2 = t2 + dt
            tlabel2.text = t2