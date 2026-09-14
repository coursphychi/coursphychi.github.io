---
title: "Train et caisse"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
hidden: true
---


<style>
 	#correc
  {
    color: #006C65;
    border-left: solid 10px #C7DDDC;
  }
 	#comm
  {
    color: #004D80;
    border-left: solid 10px #B3CAD9;
  }
 	#commsum
  {
    color: #004D80;
  }
 	#correcsum
  {
    color: #006C65;
  }

details > summary:first-of-type {
  display: list-item;    
  cursor: pointer;       
}

details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
</style>





# Train et caisse

<div style="position:relative;margin-left:auto;margin-right:auto;width:700px;max-width:100%;margin-bottom:-1em;margin-top:-1em;">
<img src="/traincaisse.png" style="box-shadow:none;background:none;">
</div>

On considère deux roues d'un train à vapeur accouplées par une bielle. Un travailleur oublie sa caisse (de masse m) sur la bielle d'accouplement et démarre ensuite le train puis roule à vitesse constante $v$.
Il y a roulement sans glissement des roues sur le sol. Le rayon des roues est noté $R$, la vitesse angulaire $\omega$. Le coefficient de frottement de la caisse sur la bielle est noté $f$.

On considère dans un premier temps la caisse en équilibre sur la bielle.

1. Écrire le PFD dans le référentiel de la bielle.

2. En déduire la vitesse maximale $v_{max1}$ que doit avoir le train pour que la caisse reste toujours en contact de la bielle.

3. Déterminer la vitesse $v_{max2}$ au-delà de laquelle la caisse glisse sur la bielle. 

On donne un code Python qui permet de représenter les normes des réactions tangentielles et normales de la bielle sur la caisse.

```python
import numpy as np
import matplotlib.pyplot as plt

# paramètres
R = 0.70          # rayon roue [m]
f = 0.30          # coeff. frottement
g = 9.81
vmax1 = np.sqrt(g*R)
v = 2             # vitesse
ω = v/R

t = np.linspace(0, 2*np.pi/ω, 600)
θ = ω*t
N = g - ω**2*R*np.sin(θ)
T = np.abs(ω**2*R*np.cos(θ))

plt.figure(figsize=(7,4))
plt.plot(t, T, label=r'$T/m$ (tangentielle)')
plt.plot(t, N, label=r'$N/m$ (normale)')
plt.xlabel('temps (s)'); plt.ylabel('force spécifique (m·s$^{-2}$)')
plt.title('Réactions bielle → caisse sur un tour'); plt.legend(); plt.tight_layout()
plt.show()
```


4. En modifiant le code, vérifier la réponse à la question 3. puis déterminer graphiquement les laps de temps sur lesquels la caisse glisse lorsque $v_{max2}<v<v_{max1}$.

