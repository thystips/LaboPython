#/usr/bin/python3.7
# coding: utf-8
from tkinter import *

def gameTick():
    canvas.move(ball, 3, 3)

    fenetre.after(10, gameTick)


fenetre = Tk()
canvas = Canvas(fenetre,width=1080, height=720,  bg="black")
canvas.pack()
ball = canvas.create_oval(50, 50, 100, 100, fill="white")

gameTick()

fenetre.mainloop()
