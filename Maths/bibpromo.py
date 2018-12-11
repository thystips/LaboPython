#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def moyenne_par_eleve(t2d):
    '''
    Calcule la moyenne de chaque étudiants à partir d'un tableau 2 dimensions :
    - chaque ligne représente un étudiant
    - la colonne 0 : son nom
    - les autres colonnes (2)
    Retourne un tableau 1 dimension contenant les moyennes
    '''
    #créer un tableau 'res' vide
    res=[]
    #boucler sur chaque étudiant
    for i in range(len(t2d)):
        #m <- la moyenne de français (col 1) et de maths (col 2) 
        m=(t2d[i][1]+t2d[i][2])/2
        #ajouter m au tableau res
        res.append(m) 
    #retourner res 
    return(res)

def extrait_col(t2d,indice):
    '''
    Extrait d'un tableau à 2 dimensions la colonne indice
    Retourne un tableau à 1 dim
    '''
    # initialiser un tableau vide 'res'
    res=[]
    #boucler sur toutes les lignes
    for i in range(len(t2d)):
        #insérer au tableau 'res' la ligne 'i' colonne 'indice'
        res.append(t2d[i][indice])
    #retourner 'res'
    return res

def moyenne(t1d):
    '''
    calcule la moyenne des valeurs d'un tableau 1 dimension
    '''
    #initialiser une variable 'res' à 0
    res=0
    #boucler sur les indices
    for i in range(len(t1d)):
        #cumuler dans 'res' l'élément du tableau
        res+=t1d[i]
    #retourner res/taille du tableau
    return res/len(t1d)

def meilleur(t1d):
    '''
    retourne l'indice de l'élément max du tableau
    '''
    meilleur_indice=0
    for i in range(1,len(t1d)):
        if t1d[i]>t1d[meilleur_indice]:
            meilleur_indice=i
    return meilleur_indice

def avis(note):
    if note<7:
        return 'Défavorable'
    elif note<10:
        return 'Doit faire ses preuves'
    else:
        return'Favorable'