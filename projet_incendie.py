from tkinter import *
from random import *

window = Tk()
window.title(" PI")
window.geometry("600x600")

WIDTH = 500
HEIGHT = 500
largeur_case = WIDTH // 20
hauteur_case = HEIGHT // 20
cpt = 1
speed = 500

c = Canvas(window, width=WIDTH, height=HEIGHT, bg= "blue")

def genere_terrain() :
    c.delete("all")
    can()
    can2()
    print(liste , "cc")

def ev (event):
    print("CLIQUE")

    n = event.x  // 25
    u = event.y // 25
    if liste[n][u] == 3 or liste[n][u] == 0:
        return
    draw_rect(n, u)
    if cpt == 1 :
        change(n, u)

def prop ():
    global p, hor, ver, n, u
    c.bind("<Button-1>", ev)

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


def can () :
    global color, p
    for loop in range(200) :
        i = randint(1,18)
        j = randint(1, 18)
        liste[i][j] = 1
        if liste[i][j] == 1:
            color = "#07680A"
        p = c.create_rectangle((i * largeur_case, j * hauteur_case),
                                ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return liste

def can2 () :
    global color, p
    for loop in range(250) :
        i = randint(1,18)
        j = randint(1, 18)

        liste[i][j] = 2
        if liste[i][j] == 2 :
            color = "#E0EC02"

            p = c.create_rectangle((i * largeur_case, j * hauteur_case),
                                ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)

    return liste


def can3 (l) :
    global color, p, hor, ver
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
        c.after(speed, change, i - 1, j)
        c.after(speed, change, i + 1, j)
        c.after(speed, change, i, j - 1)
        c.after(speed, change, i, j + 1)


liste = [20*[0] for i in range(20)]


button_genere_terrain = Button(window, text="génèrer un terrain" , font=("Courrier", 16), bg='white', fg='BLUE', command = genere_terrain)

button_change_etape = Button(window, text="next" , font=("Courrier", 16), bg='white', fg='BLUE')
print(liste)
prop()
c.grid(row = 1, column = 1)
button_genere_terrain.grid(row = 0, column = 1)
button_change_etape.grid(row = 2, column = 1)


window.mainloop()
print(speed)