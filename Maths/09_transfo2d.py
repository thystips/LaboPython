# coding: utf-8
from tkinter import *

def transfo2d():
    taille = 500
    tline = 510
    dt = taille / 2
    dligne = tline / 2 + 5
    tc = dligne / 10

    fenetre = Tk()
    fenetre.title("transfo2d")

    canvas = Canvas(
        fenetre, width=taille, height=taille, bg="grey", bd=8, relief="ridge"
    )
    canvas.pack()

    Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
    Bouton_Quitter.pack()

    line1 = canvas.create_line(0, dligne, tline, dligne, fill="blue", width=4)
    line2 = canvas.create_line(dligne, tline, dligne, 0, fill="blue", width=4)

    # i = tline / 10

    # carreau = [[canvas.create_rectangle(i, i, i, i, fill="#FFFFFF") for i in range(10)]]
    
    fenetre.mainloop()


transfo2d()
