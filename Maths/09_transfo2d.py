# coding: utf-8
from tkinter import *
import tkinter as tk


def transfo2d():
    def px(x, y):
        x_ = (25 * (x + 10)) + 10
        y_ = 510 - 25 * (y + 10)
        return (x_, y_)

    def init_canevas():
        line1 = canvas.create_line(10, dligne, 510, dligne, fill="black", width=4)
        line2 = canvas.create_line(dligne, 510, dligne, 10, fill="black", width=4)
        # Horizontal
        x1 = 10
        x2 = 510
        for k in range(10, 511, 25):
            y1 = k
            y2 = k
            canvas.create_line(x1, y1, x2, y2)
        # Vertical
        y1 = 10
        y2 = 510
        for k in range(10, 511, 25):
            x1 = k
            x2 = k
            canvas.create_line(x1, y1, x2, y2)

    def dessine_forme(pts):
        p0 = pts[traits[0][0]]
        p1 = pts[traits[0][1]]
        canvas.create_line(px(p0[0], p0[1]), px(p1[0], p1[1]), fill="red", width=4)
        p0 = pts[traits[1][0]]
        p1 = pts[traits[1][1]]
        canvas.create_line(px(p0[0], p0[1]), px(p1[0], p1[1]), fill="red", width=4)
        p0 = pts[traits[2][0]]
        p1 = pts[traits[2][1]]
        canvas.create_line(px(p0[0], p0[1]), px(p1[0], p1[1]), fill="red", width=4)

    taille = 515
    tline = 510
    dligne = tline / 2 + 6
    points = [[2, 2], [6, 2], [4, 6]]
    traits = [[0, 1], [1, 2], [2, 0]]

    fenetre = tk.Tk()
    fenetre.title("transfo2d")

    canvas = tk.Canvas(fenetre, width=taille, height=taille, bg="grey", bd=8)
    canvas.pack()

    Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
    Bouton_Quitter.pack()
    init_canevas()
    dessine_forme(points)

    # p1 = canvas.create_line(px(2, 2), px(6, 2), fill="red", width=4)
    # p2 = canvas.create_line(px(6, 2), px(4, 6), fill="red", width=4)
    # p3 = canvas.create_line(px(4, 6), px(2, 2), fill="red", width=4)

    fenetre.mainloop()


transfo2d()
