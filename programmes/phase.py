Web VPython 3.2


scene.width, scene.height = 500,400
scene.background = vec(4,63,97)/255
textmoon = "https://upload.wikimedia.org/wikipedia/commons/2/26/Solarsystemscope_texture_2k_moon.jpg"
scene.lights = []
distant_light(direction=vector(-1,0,0), color=color.white)
R_T = 6371
R_L = 1737
O = vec(0,0,0)
d_TL =  15000
omega_L = 2*pi/29.5
t = 0
Laxe = 1.4*R_T
Inc = 23.5/180*pi
L = vec(d_TL*cos(omega_L*t),d_TL*sin(omega_L*t),0)
Terre = sphere(pos = O,radius=R_T,texture=textures.earth)
Terre.rotate(angle=pi/2, axis=vector(1,0,0))
Terre.rotate(angle=-Inc, axis=vector(1,0,0))
Lune = sphere(pos = L,radius=R_L,texture=textmoon)
Debaxe = vec(0,-Laxe*sin(Inc),-Laxe*cos(Inc))
Finaxe = vec(0,Laxe*sin(Inc),Laxe*cos(Inc))
Axe = arrow(pos=Debaxe,axis=Finaxe-Debaxe,round=True,shaftwidth=200,visible=False)
#Lune.rotate(angle=pi,axis=vec(0,0,1))

cr = shapes.circle(radius=50)
circpath = paths.circle(radius=d_TL)
Orb = extrusion(path=circpath, shape=cr, color=color.red)
ar = shapes.arc(radius=R_L*1.01, angle1=0, angle2=pi)
arcpath = paths.arc(radius=1e-12, angle1=0, angle2=pi*1.05)
#HS = extrusion(path=arcpath, shape=ar, color=color.black, emissive=True)
#HS.pos = L+ vec(R_L/2,0,0)
#HS.rotate(angle=3*pi/2, axis=vector(0,0,1))
Orb.rotate(angle=pi/2, axis=vector(1,0,0))

R_obs = R_T*1.1

Lamp = local_light(pos=vector(-30*d_TL,0,0), color=color.white)
Soleil = sphere(pos=Lamp.pos, radius=10*R_T, color=color.white, emissive=True)

Obs_pole = vec(0,0,R_T*1.3)
#scene.camera.pos = Obs_pole
#scene.camera.pos = vec(0,0,10*R_T)
scene.center = O
#scene.up = vec(0,0,1)
scene.range = 20000
#scene.camera.axis = (L-Obs_pole)

suivrelune = False

scene.append_to_caption('\n')
def suivre():
    suivrelune = True
    scene.up = vec(0,0,1)
    scene.camera.pos = Obs_pole
    scene.camera.axis = (Lune.pos-Obs_pole)
r = radio(bind=suivre, text=' Suivre la Lune depuis la Terre')
scene.append_to_caption('\n\n')

def acc(s):
  wt.text = '{}'.format(s.value)
s = slider(bind=acc,min=1,max=10,step=1,length=250)
scene.append_to_caption('\n\n')
scene.append_to_caption(' accélérer ×')
wt = wtext(text='{}'.format(s.value))
scene.append_to_caption('\n\n')

dt = 0.001
while True:
  rate(s.value/dt)
  Lune.pos = vec(d_TL*cos(omega_L*t),d_TL*sin(omega_L*t),0)
  #HS.pos = Lune.pos + vec(R_L/2,0,0)
  if r.checked:
    scene.up = vec(0,0,1)
    scene.camera.pos = Obs_pole
    scene.camera.axis = (Lune.pos-Obs_pole)
  Lune.rotate(angle=omega_L*dt,axis=vector(0,0,1))
  Terre.rotate(angle=2*pi*dt,axis=Finaxe-Debaxe)
  t += dt