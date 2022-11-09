from upemtk import *
from time import *
from math import sqrt as racine


def verification_1(lst, x, y, distance):
    if lst == []:
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                distance = racine(((lst[i][j])-x)**2 + ((lst[i][j])-y)**2)
        return distance
    return None


def verification_2(lst, x, y, distance):
    if lst == []:
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                distance = racine((x-(lst[i][j]))**2 + (y-(lst[i][j]))**2)
    return distance


def main():
    tour = int(input('Le nombre de tour : '))
    largeurFenetre = 400
    hauteurFenetre = 400
    cree_fenetre(largeurFenetre, hauteurFenetre) # mettre 2000 et 1200
    lst_pos_j1 = []
    lst_pos_j2 = []
    color = 'red'
    distance = 0
    r = 50
    for compteur in range(tour):
        x1, x2, y1, y2 = 0, 0, 0, 0
        x1, y1, e1 = attente_clic() # Récupération de l'emplacement du clic
        lst_pos_j1.append([x1, y1])
        resultat = verification_2(lst_pos_j2, x1, x2, distance)
        if resultat <= r*2:
            print("Il s'intersecte")
            lst_pos_j1.pop()
            continue
        else:
            cercle(x1, y1, r, couleur=color, remplissage=color) # La boule du joueur 1 apparaît à l'emplacement du clic
            pos_j1 = str(str(x1) + ',' + str(y1))
        color, j = 'blue', 2
        x2, y2, e2 = attente_clic() # Récupération de l'emplacement du clic
        resultat = verification_1(lst_pos_j1, x2, y2, distance)
        lst_pos_j1.append([x2, y2])
        cercle(x2, y2, r, couleur=color, remplissage=color) # La boule du joueur 2 apparait à l'emplacement du clic
        pos_j2 = str(str(x2) + ',' + str(y2))
        color = 'red'
    attente_clic()
    ferme_fenetre()


if __name__ == '__main__':
    main()