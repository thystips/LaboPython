#!/usr/bin/python3

def indice(l,c):
    return l * largeur + c

from PIL import Image # Importation du package PIL
while True:
    interrupt = input("Écrivez stop si vous voulez arrêter le programme,\nsinon appuyez sur Entrée : ")
    if interrupt.lower() == "stop":
        print("\n! Interruption du programme !")
        break
    ligne = int(input("\nEntrez la valeur de la ligne: "))
    colonne = int(input("Entrez la valeur de la colonne: "))
    im = Image.open('img1.png') # Chargement de l'image img1.png
    largeur,hauteur = im.size # Récupération de la largeur et de la hauteur
    pixels = list(im.getdata())
    print(pixels)
    p = pixels[indice(ligne,colonne)]
    if p == (0,0,0):
        print('\nLa couleur du pixel correspondant est: Noir\n')
    elif p == (255,255,255):
        print('\nLa couleur du pixel correspondant est: Blanc\n')
    else:
        print('\nLa couleur du pixel correspondant est: Gris\n')
