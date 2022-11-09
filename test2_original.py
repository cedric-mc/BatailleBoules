from upemtk import *
from math import *


def joueur1():
    x1, y1, e1 = attente_clic()
    cercle(x1, y1, 50, couleur=color, remplissage=color)
    position_joueur=str(str(x1) + "," + str(y1))
    print(position_joueur)
    liste_position_joueur.append(position_joueur)
    print(liste_position_joueur)
    color = 'blue'


if __name__ == '__main__':
    tour = int(input('Le nombre de tour : '))
    txt1=""
    txt2=""
    liste_position_joueur=[]
    position_joueur=""
    joueur=""
    distance = []
    intersection= False
    cree_fenetre(400, 400)
    color = 'red'
    for i in range(tour):
        if not intersection:
        
            x1, y1, e1 = attente_clic()
            cercle(x1, y1, 50, couleur=color, remplissage=color)
            position_joueur=str(str(x1) + "," + str(y1))
            print(position_joueur)
            liste_position_joueur.append(position_joueur)
            print(liste_position_joueur)
            color = 'blue'
        
        
            x2, y2, e2 = attente_clic()
            cercle(x2, y2, 50, couleur=color, remplissage=color)
            color = 'red'
            position_joueur=str(str(x2) + "," + str(y2))
            print(position_joueur)
            liste_position_joueur.append(position_joueur)
            print(liste_position_joueur)

        distance=sqrt((x2-x1)**2 +(y2-y1)**2)
        print("distance",distance)
        if distance <= 100:
            intersection=True
            if color == 'blue':
                color ='red'
            else:
                color ='blue'
            print("intersection",intersection)
            print ("intersecte")
        else:
            intersection=False
            print("ne intersecte pas")
    attente_clic()
    ferme_fenetre()