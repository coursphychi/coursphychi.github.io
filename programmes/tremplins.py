GlowScript 2.9 VPython

scene.width = 800
scene.height = 500
scene.center.x = 4
scene.center.y = 0
scene.range = 10
#scene.userzoom=False
#scene.userspin=False
#scene.userpan=False
scene.axis = vec(0,-0.3,-1)

running = False

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
    
bbutton = button(text="Run", pos=scene.title_anchor, bind=Run)

def Reset(c):
    global  t1,t2, ball1, ball2

    t1=t2=0
    ball1.pos = p1[0].pos+vec(0,Rball,1)
    ball2.pos = p2[0].pos+vec(0,Rball,-1)
    ball1.v = ball2.v = vector(0,0,0)
    tlabel1.text = "t = {:} s".format(t1)
    tlabel2.text = "t = {:} s".format(t2)
    ball1.clear_trail()
    ball2.clear_trail()
    
cbutton = button(text="Reset", pos=scene.title_anchor, bind=Reset)

N = 10

rcylinder = 0.1
rball = 0.1
g = vector(0,-9.8,0)
a = vector(0,0,0)

start = vector(-8,3,0)
end = vector(10,0,0)

p1 = socle1 = []
p2 = socle2 = []

p1 += [sphere(pos=start, radius=rball, visible=False)]
p1 += [sphere(pos=vec(-4,-3,0), radius=rball, visible=False)]
p1 += [sphere(pos=vec(8,-3,0), radius=rball, visible=False)]
p1 += [sphere(pos=end, radius=rball, visible=False)]

colorsocle1 = vec(0.5,0.7,0.8)
for i in range(len(p1)):
  socle1.append([p1[i].pos.x,p1[i].pos.y])
socle1.append([10,-4])
socle1.append([-8,-4])
socle1.append([p1[0].pos.x,p1[0].pos.y])
ex = extrusion(path=[vec(0,0,2), vec(0,0,0)], shape=socle1,color=colorsocle1)


p2 += [sphere(pos=start, radius=rball, visible=False)]
p2 += [sphere(pos=vec(9,-1.5,0), radius=rball, visible=False)]
p2 += [sphere(pos=end, radius=rball, visible=False)]

colorsocle2 = vec(0.2,0.8,0.6)
for i in range(len(p2)):
  socle2.append([p2[i].pos.x,p2[i].pos.y])
socle2.append([10,-4])
socle2.append([-8,-4])
socle2.append([p2[0].pos.x,p2[0].pos.y])
ex = extrusion(path=[vec(0,0,0), vec(0,0,-2)], shape=socle2,color=colorsocle2)


Rball = 0.5
ball1 = sphere(pos=p1[0].pos+vec(0,Rball,1), radius=Rball, color=vec(1,0.2,0.2),make_trail=True, trail_type="points",interval=20)
ball1.v = vector(0,0,0)

ball2 = sphere(pos=p2[0].pos+vec(0,Rball,-1), radius=Rball, color=vec(1,1,0.2),make_trail=True, trail_type="points",interval=20)
ball2.v = vector(0,0,0)

t1 = t2 = 0
dt = 0.001

tlabel1=label(pos=p1[-1].pos+vec(0,-2,2), text="t = {:} s".format(t1), xoffset=20, yoffset=-20, line=False, color=vec(1,0.8,0.8))
tlabel2=label(pos=p1[-1].pos+vec(0,0,0), text="t = {:} s".format(t2), xoffset=30, yoffset=-20, line=False, color=vec(1,1,0.8))


while True:
  
    rate(1000)
    
    if running:
        
        for j in range(len(p1)-1):
            if ball1.pos.x>=(p1[j].pos.x) & ball1.pos.x<=10:
               ball1.v = mag(ball1.v)*norm(p1[j+1].pos-p1[j].pos)
               a1 = dot(g,norm(p1[j+1].pos-p1[j].pos))*norm(p1[j+1].pos-p1[j].pos)
            elif ball1.pos.x>=10:
               a1 = g
        ball1.v += a1*dt
        
        for j in range(len(p2)-1):
            if ball2.pos.x>=(p2[j].pos.x) & ball2.pos.x<=10:
               ball2.v = mag(ball2.v)*norm(p2[j+1].pos-p2[j].pos)
               a2 = dot(g,norm(p2[j+1].pos-p2[j].pos))*norm(p2[j+1].pos-p2[j].pos)
            elif ball2.pos.x>=10:
               a2 = g
               #ball2.make_trail = True
        ball2.v += a2*dt
        
        if ball1.pos.y >= -4+Rball :
          ball1.pos += ball1.v*dt
          t1 += dt
          tlabel1.text = "t = {:.2f} s".format(t1)
        else :
          ball1.v = vec(0,0,0)
          
        if ball2.pos.y >= -4+Rball :
          ball2.pos += ball2.v*dt
          t2 += dt
          tlabel2.text = "t = {:.2f} s".format(t2)
        else :
          ball2.v = vec(0,0,0)