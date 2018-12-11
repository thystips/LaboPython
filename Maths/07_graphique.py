from tkinter import *


def change_coo(x, y):
    x1 = taille_cube * (x + 1)
    y1 = hauteur - taille_cube * (y + 1)
    return x1, y1


def init_canevas():
    canevas.create_line(
        0,
        hauteur - taille_cube,
        largeur,
        hauteur - taille_cube,
        fill="green",
        dash=(2, 2, 4, 2),
        width=2,
    )

    # #Dessiner l'Histogramme du port 1080
    # canevas.create_rectangle(change_coo(0, 0), change_coo(1, 3), fil="red")
    # #Dessiner l'Histogramme du port 533
    # canevas.create_rectangle(change_coo(2, 0), change_coo(3, 2), fil="red")
    # #Dessiner l'Histogramme du port 22
    # canevas.create_rectangle(change_coo(4, 0), change_coo(5, 1), fil="red")

    i = 0

    for cle, valeur in attaques.items():
        canevas.create_rectangle(
            change_coo(i, 0), change_coo(i + 1, valeur), fill="red"
        )
        # affichage de l'étiquette sous l'abscisse
        canevas.create_text(change_coo(i + 0.5, -0.2), text=cle, fill="white")
        i += 2


def raz():
    pass


attaques = {"1080": 3, "533": 2, "22": 1, "8080": 8}

taille_cube = 90
l = len(attaques.keys())
h = max(attaques.values())
largeur = taille_cube * (2.2 * l)
hauteur = taille_cube * (2 + h)

# Fenêtre graphique
fenetre = Tk()
canevas = Canvas(fenetre, width=largeur, height=hauteur, bg="black")
btn_Raz = Button(fenetre, text="RAZ", command=raz)
btn_Quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)

# Placements de widgets
canevas.grid(row=0, column=0, columnspan=3)
btn_Raz.grid(row=1, column=1)
btn_Quitter.grid(row=1, column=2)

init_canevas()
# Boucle infinie
fenetre.mainloop()
