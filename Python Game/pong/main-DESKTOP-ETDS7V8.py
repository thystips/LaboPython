# coding: utf-8
from tkinter import *


def gameTick():
    canvas.move(ball, 0, 0)

    fenetre.after(10, gameTick)


fenetre = Tk()
canvas = Canvas(fenetre, width=1080, height=720, bg="black")
canvas.pack()
ball = canvas.create_oval(510, 300, 570, 350, fill="red")
line = canvas.create_line(540, 0, 540, 720, fill="white", width)

gameTick()

fenetre.mainloop()
