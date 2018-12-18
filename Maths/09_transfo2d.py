# coding: utf-8
from tkinter import *
import tkinter as tk
from math import *
import numpy as np


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

    # def rotation(x):
    #     theta = np.radians(x)
    #     c, s = np.cos(theta), np.sin(theta)
    #     if theta > 0:
    #         R = np.matrix("{} {}; {} {}".format(c, -s, s, c))
    #         return R
    #     elif theta == 0:
    #         return "Erreur"
    #     else:
    #         R = np.matrix("{} {}; {} {}".format(c, s, -s, c))
    #         return R

    def rotate():
        def mult_mat_vect(m, v):
            res = [0] * 3
            for l in range(3):
                for k in range(3):
                    res[l] += m[l][k] * v[k]
            return res

        def rotation():
            a = int(e.angle.get()) / 180 * pi
            r = [[cos(a), -sin(a)], [sin(a), cos(a)]]
            points2 = mult_mat_vect(a, points)
            dessine_forme(points2)

    taille = 515
    tline = 510
    dligne = tline / 2 + 6
    points = [[2, 2], [6, 2], [4, 6]]
    traits = [[0, 1], [1, 2], [2, 0]]
    x = 30
    theta = x

    fenetre = tk.Tk()
    fenetre.title("transfo2d")

    canvas = tk.Canvas(fenetre, width=taille, height=taille, bg="grey", bd=8)
    canvas.pack()

    Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
    Bouton_Quitter.pack()

    init_canevas()

    dessine_forme(points)

    # rotation(x)
    # print(rotation(x))

    rotate()

    fenetre.mainloop()


transfo2d()
