#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bibpromo import *

#le tableau à 2 dimensions
data=[['Riri',12,14],['Fifi',13,9],['Loulou',14,11],['Méchant Loup',4,6]]


mpe=moyenne_par_eleve(data)
print(data)
print(mpe)

print("*****************************************")
print("          Donnees par matière            ")
print("-----------------------------------------")

notes_f=extrait_col(data,1)
meilleur_f=meilleur(notes_f)
print('Notes français : {}. Moyenne : {:.1f}'.format(notes_f,moyenne(notes_f)))
print('\tLa meilleur note est {:.1f} ({})'.format(notes_f[meilleur_f],data[meilleur_f][0]))

notes_m=extrait_col(data,2)
meilleur_m=meilleur(notes_m)
print('Notes maths : {}. Moyenne : {:.1f}'.format(notes_m,moyenne(notes_m)))
print('\tLa meilleur note est {:.1f} ({})'.format(notes_m[meilleur_m],data[meilleur_m][0]))

print('\n')

print("*****************************************")
print("           Donnees par étudiant          ")
print("-----------------------------------------")
for i in range(len(data)):
    print('{:15s} a pour moyenne {:4.1f} - Avis : {}'.format(data[i][0],mpe[i],avis(mpe[i])))