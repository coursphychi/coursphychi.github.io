### ENTRER LES VALEURS OBTENUS DANS LES LISTES SUIVANTES
Hauteurs = [hauteur en km, hauteur en km, hauteur en km, ...]
Périodes = [(heures,minutes),(heures,minutes),(heures,minutes),...]

### CONVERSION DES HAUTEURS EN RAYON DE L'ORBITE (EN m)
RT = 6.378E6 # rayon de la terre en m
R = [] # Liste vide qui devra contenir les rayons des orbites en m
for h in Hauteurs:
    R.append(.......)

### CONVERSION DES PÉRIODES EN s
T = []
for (heures,minutes) in Périodes:
    T.append(...)

### POUR CHAQUE COUPLE (R,T), ON SOUHAITE CALCULER ET AFFICHER LE QUOTIENT T²/R³
for i in range(len(R)):
    quotient = ........
    print(quotien)