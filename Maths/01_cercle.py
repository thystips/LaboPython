from math import pi

#saisie du rayon
r= int(input('Donner : '))
#calcul de la circonférence, de la surface et du volume
circonf=2*pi*r
surface=pi*r*2
volume=4/3*pi*r**3
#affichage du résultats
print('Circonférence : {0:.2} ; Surface : {1} ; Volume : {2}'.format(circonf,surface,volume))
