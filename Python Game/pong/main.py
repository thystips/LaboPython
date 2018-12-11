# coding: utf-8
from tkinter import *


def gameTick():
    canvas.move(ball, dx, dy)

    fenetre.after(10, gameTick)


dx = 3
dy = 0

largeur = 1080
longueur = 720
dla = largeur / 2
dlo = longueur / 2


fenetre = Tk()
canvas = Canvas(fenetre, width=largeur, height=longueur, bg="black")
canvas.pack()
Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
Bouton_Quitter.pack()

ball = canvas.create_oval(510, 300, 570, 350, fill="red")
line = canvas.create_line(dla, 0, 540, longueur, fill="white", dash=(20, 10), width=4)

gameTick()


fenetre.mainloop()
