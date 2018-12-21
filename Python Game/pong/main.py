# coding: utf-8
from tkinter import *


vx = 0
vy = 0


def gameTick():
    canvas.move(ball, vx, vy)

    fenetre.after(10, gameTick)


vx = 5
vy = 0

x1 = 510
y1 = 320
x2 = 570
y2 = 370

largeur = 1080
longueur = 720
dla = largeur / 2
dlo = longueur / 2


fenetre = Tk()
fenetre.title("Pong")
canvas = Canvas(fenetre, width=largeur, height=longueur, bg="black")
canvas.pack()
Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
Bouton_Quitter.pack()

ball = canvas.create_oval(x1, y1, x2, y2, fill="red", tag="ball")
line = canvas.create_line(dla, 0, dla, longueur, fill="white", dash=(20, 10), width=4)

gameTick()

fenetre.mainloop()
