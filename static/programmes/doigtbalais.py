Web VPython 3.2

scene.width,scene.height = 600,200
scene.align = 'left'
scene.range = 0.8
xG = -1.
xD = 1.4
L = 3
g = 9.8
m = 0.3
mu_c = 0.4
mu_s = 0.6
v0 = 0.1
rayon_doigt = 0.05
hauteur = 0.05
DoigtDglisse = True
DoigtGglisse = False
versG = False
T_G = 0
T_D = 0

DoigtG = cylinder(pos=vec(xG,0,0.1),radius=rayon_doigt,axis=vec(0,0,-0.2),velocity=vec(v0/2,0,0),color=vec(248,209,166)/255)
DoigtD = cylinder(pos=vec(xD,0,0.1),radius=rayon_doigt,axis=vec(0,0,-0.2),velocity=vec(-v0/2,0,0),color=vec(248,209,166)/255)
Balai = box(pos=vec(0,rayon_doigt+hauteur/2,0),length=3,height=0.05,width=0.1,velocity=vec(0,0,0),color=vec(89,157,255)/255)
G = sphere(pos=Balai.pos+vec(0,0,hauteur),radius=hauteur/2,color=vec(1,0,0),emissive=True)

g1 = graph(width=600,height=300,xtitle='t',ytitle='x_G',fast=False,align='left')
plotxG = gcurve(graph=g1,color=vec(89,157,255)/255) 

t = 0
dt = 1e-4


while DoigtG.pos.x < DoigtD.pos.x:
  
  rate(4/dt)
  DoigtG.pos += DoigtG.velocity*dt
  DoigtD.pos += DoigtD.velocity*dt
  N_D = abs(DoigtG.pos.x-Balai.pos.x)/abs(DoigtD.pos.x-DoigtG.pos.x)*m*g
  N_G = abs(DoigtD.pos.x-Balai.pos.x)/abs(DoigtD.pos.x-DoigtG.pos.x)*m*g
  
  if DoigtGglisse:
    T_G = mu_c*N_G
  else:
    T_G = T_D
    Balai.velocity = DoigtG.velocity
    Balai.pos += Balai.velocity*dt
    if T_G > mu_s*N_G:
      DoigtGglisse = True
      T_G = mu_c*N_G
      #DoigtDglisse = False # pour squizzer la phase transitoire
      
  if DoigtDglisse:
    T_D = mu_c*N_D
  else:
    T_D = T_G
    Balai.velocity = DoigtD.velocity
    Balai.pos += Balai.velocity*dt
    if T_D > mu_s*N_D:
      DoigtDglisse = True
      T_D = mu_c*N_D
      #DoigtGglisse = False # pour squizzer la phase transitoire
  
  if DoigtGglisse and DoigtDglisse:
    Balai.velocity += vec(T_G-T_D,0,0)*dt
    Balai.pos += Balai.velocity*dt
    if versG and abs(Balai.velocity.x - DoigtG.velocity.x)<1e-3:
      DoigtGglisse = False
      versG = False
    if not versG and abs(Balai.velocity.x - DoigtD.velocity.x)<1e-3:
      DoigtDglisse = False
      versG = True
  
  G.pos = Balai.pos+vec(0,0,hauteur)
  plotxG.plot(t,Balai.pos.x)
  t += dt
  