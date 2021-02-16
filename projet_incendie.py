from tkinter import *
from random import *

window = Tk()
window.title(" Exercice 1")
window.geometry("600x600")

WIDTH = 600
HEIGHT = 600
largeur_case = WIDTH // 20
hauteur_case = HEIGHT // 20

c = Canvas(window, width=WIDTH, height=HEIGHT, bg= "blue")

def can (l) :
    for loop in range(100) :
        i = randint(1,18)
        j = randint(1, 18)
        liste[i][j] = 1
        if liste[i][j] == 1 :
            color = "gray80"
        c.create_rectangle((i * largeur_case, j * hauteur_case),
                                ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return l





def can2 (l) :
    for loop in range(100) :
        i = randint(1,18)
        j = randint(1, 18)
        liste[i][j] = 1
        if liste[i][j] == 1 :
            color = "orange"

        c.create_rectangle((i * largeur_case, j * hauteur_case),
                                ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return l

liste = [20*[0] for i in range(20)]

can(liste)
can2(liste)
print(liste)

c.grid()

window.mainloop()


