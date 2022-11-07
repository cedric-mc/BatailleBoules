from turtle import color
from upemtk import *



def main(tour):
    color = 'red'
    for i in range(tour):
        x, y, e = attente_clic()
        cercle(x, y, 50, couleur=color, remplissage=color)
        color = 'blue'
        x, y, e = attente_clic()
        cercle(x, y, 50, couleur=color, remplissage=color)
        color = 'red'



if __name__ == '__main__':
    tour = int(input('Le nombre de tour : '))
    cree_fenetre(400, 400)
    main(tour)
    attente_clic()
    ferme_fenetre()