from tkinter import *
from random import *

window = Tk()
window.title(" Exercice 1")
window.geometry("600x600")

WIDTH = 600
HEIGHT = 600
largeur_case = WIDTH // 20
hauteur_case = HEIGHT // 20
cpt = 0

c = Canvas(window, width=WIDTH, height=HEIGHT, bg="blue")

def prop():
    global p,i,j, i2, j2

    liste[i2][i] = 3
    print(liste)
    i =i2
    j = j2
    can3(liste)


def can(l):
    global color, p
    for loop in range(200):
        i = randint(1, 18)
        j = randint(1, 18)
        liste[i][j] = 1
        if liste[i][j] == 1:
            color = "#07680A"
        p = c.create_rectangle((i * largeur_case, j * hauteur_case),
                               ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return l


def can2(l):
    global color, p
    for loop in range(200):
        i = randint(1, 18)
        j = randint(1, 18)
        if liste[i][j] == 0:
            liste[i][j] = 2
        if liste[i][j] == 2:
            color = "#E0EC02"

        p = c.create_rectangle((i * largeur_case, j * hauteur_case),
                               ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return l


def can3(l):
    global color, p, i2, j2
    for loop in range(1):
        i = randint(1, 18)
        j = randint(1, 18)
        liste[i][j] = 3

        if liste[i][j] == 3:
            color = "orange"
        p = c.create_rectangle((i * largeur_case, j * hauteur_case),
                               ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)
        i2 = i +1
        j2 = j +1

    return l


liste = [20 * [0] for i in range(20)]

can(liste)
can2(liste)

print(liste)


def ss():
    inn = 0
    for i in liste:
        for j in i:
            if j == 3:
                print(i, j)

    print(inn)


ss()
prop()
c.after(3,prop)
c.grid()

window.mainloop()
