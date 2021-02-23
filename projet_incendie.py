from tkinter import *
from random import *

window = Tk()
window.title(" PI")
window.geometry("600x600")

WIDTH = 600
HEIGHT = 600
largeur_case = WIDTH // 20
hauteur_case = HEIGHT // 20
cpt = 0

c = Canvas(window, width=WIDTH, height=HEIGHT, bg= "blue")
def ev (event):
    print("CLIQUE")

    n = event.x  // 30
    u = event.y // 30
    if liste[n][u] == 3 or liste[n][u] == 0:
        return
    draw_rect(n, u)
    change(n, u)

def prop ():
    global p, hor, ver, n, u
    c.bind("<Button-1>", ev)

    #print(liste)
    c.after(300, prop)

def nombre_voisin(i, j) :
    nf = 0
    if liste[i-1][j] == 3 :
        nf += 1
    if liste[i+1][j] == 3 :
        nf += 1
    if liste[i][j-1] == 3 :
        nf += 1
    if liste[i-1][j+1] == 3 :
        nf += 1
    return nf


def is_burn(nf) :
    possibilite = [i for i in range(10)]
    mutable = [i for i in range(10)]
    cle = randint(0, len (mutable))
    for i in range(nf) :
        x = randint(0, len (mutable))
        possibilite[i]= mutable.pop(x)
    return cle in possibilite

def can (l) :
    global color, p
    for loop in range(80) :
        i = randint(1,18)
        j = randint(1, 18)
        liste[i][j] = 1
        if liste[i][j] == 1:
            color = "#07680A"
        p = c.create_rectangle((i * largeur_case, j * hauteur_case),
                                ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return l

def can2 (l) :
    global color, p
    for loop in range(450) :
        i = randint(1,18)
        j = randint(1, 18)
        if liste[i][j] == 0 :
            liste[i][j] = 2
        if liste[i][j] == 2 :
            color = "#E0EC02"

            p = c.create_rectangle((i * largeur_case, j * hauteur_case),
                                ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return l

def can3 (l) :
    global color, p, hor, ver, hor1, ver1
    for loop in range(1) :
        i = randint(1, 18)
        j = randint(1, 18)
        liste[i][j] = 3

        if liste[i][j] == 3:
            color = "orange"
        p = c.create_rectangle((i * largeur_case, j* hauteur_case),
                                ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)
        hor = i
        ver = j
        hor1 = i
        ver1 = j

    return l

def draw_rect(i ,j) :
    l_c = largeur_case
    h_c = hauteur_case
    c.create_rectangle(i * l_c, j * h_c, (i + 1) * l_c, (j + 1) * h_c, fill='red')

def change(i, j):

    print("liste", i , ",", j, " = ", liste[i][j])

    if liste[i][j] == 0 or liste[i][j] == 3 :
        print("on sort")
        return

    if liste[i][j] == 1:
        nf = nombre_voisin(i,j)
        if not is_burn(nf):
            return


    liste[i][j] = 3

    #initialisation

    draw_rect(i, j)
    print("dessiné")

    if i == 0 or i == 19 or j == 0 or j == 19 :
        return

    else:
        #récurrence
        c.after(500, change, i - 1, j)
        c.after(500, change, i + 1, j)
        c.after(500, change, i, j - 1)
        c.after(500, change, i, j + 1)

liste = [20*[0] for i in range(20)]

can(liste)
can2(liste)

print(liste)
prop()
c.grid()

window.mainloop()