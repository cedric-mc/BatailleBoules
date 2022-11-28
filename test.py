# Imports ---------------------------------------------------------------------
from upemtk import *
from math import *
import doctest
# Imports ---------------------------------------------------------------------
# Fonctions -------------------------------------------------------------------
def terminaison():
    """"Fonction  permettant à un joueur de décider une fois 
    par tour que le jeu se termine dans 5 tours (en cours de préparation pour le prochain rendu).
    """
    ferme_fenetre()


def longueur(color, lst1, lst2, x, y, c):
    """Fonction de vérification des intersections 
    entre les cercles des adversaires. 
    Calcul utilisé : racine carré de ((Xb-Xa)^2 + (Yb-Ya)^2)
    """
    if lst1 != []:
        for lignes in range(len(lst1)):
            distance = sqrt((lst1[lignes][0]-x)**2 + (lst1[lignes][1]-y)**2) #cette formule calcule la disatance entre les deux coordonnées des points
            if distance <= 100: # Le 100 correspond au diamètre du cercle
                if color == 'blue':
                    color ='red'
                else:
                    color ='blue'
                efface(c)    #la boule est efffacée afin que le programme passe le tour de l'adversaire
                lst2.pop()   # Le dernier élément de la liste des positions du du joueur est effacé, soit la dernière position.
                return distance


def j1(color, lst_j1, liste_position_joueur):
    """Fonction du joueur 1 avec les différentes coordonnées listée du joueur et de tout les joueurs"""
    x1, y1, e1 = attente_clic()
    c = cercle(x1, y1, 50, couleur=color, remplissage=color) #insère un cercle de couleur dans la fenêtre
    position_joueur=str(str(x1) + "," + str(y1)) #cette variable permet de  récupérer les coordonnées du centre des centres (exemple 292,157 (x1, y1) ceci sont les coordonnées cliqué par le joeur dans la fenêtre<))
    liste_position_joueur.append(position_joueur) #on rajoute les position des boules dans la liste_position_joueur.
    lst_j1.append([x1, y1])
    color = 'blue'   #changement de
    return x1, y1, lst_j1, color, c 


def j2(color, lst_j2, liste_position_joueur):
    """Fonction du joueur 2 avec les différentes coordonnées listée du joueur et de tout les joueurs"""
    x2, y2, e2 = attente_clic()
    c = cercle(x2, y2, 50, couleur=color, remplissage=color)  
    color = 'red'
    position_joueur=str(str(x2) + "," + str(y2))  #cette variable permet de  récupérer les coordonnées du centre des centres (exemple 292,157 (x1, y1) ceci sont les coordonnées cliqué par le joeur dans la fenêtre<)
    liste_position_joueur.append(position_joueur) #on rajoute les position des boules dans la liste_position_joueur.
    lst_j2.append([x2, y2])
    return x2, y2, lst_j2, color, c
# Fonctions -------------------------------------------------------------------
# Fonction principale -----------------------------------------------
def GAME():
    tour = int(input('Le nombre de tour pour chaque joueur : '))
    liste_position_joueur = [] #cette variable stockera au fur et à mesure les coordonnées de position_joueur.
    lst_j1 = []
    lst_j2 = []
    color = 'red' #couleur de la boule
    largeur_Fenetre = 1650
    hauteur_Fenetre = 900
    cree_fenetre(largeur_Fenetre, hauteur_Fenetre)
    Terminaison = rectangle(50, 50, 500, 250, couleur='black', epaisseur=3, tag='terminaison')
    x, y, e = attente_clic()
    if (50 < x < 500 and 50 < y < 250):
        print(True)
    for compteur in range(tour): # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        """appel des fontions"""
        txt = 'Tour du joueur ' + '1'
        txt_tour = 'Tour : ' + str(compteur + 1) + '/' + str(tour)
        txt_joueur, txt_compteur = texte(largeur_Fenetre//2 - largeur_Fenetre//10, 0, txt, color), texte(largeur_Fenetre//2 - largeur_Fenetre//10, hauteur_Fenetre-50, txt_tour, color, police='')
        x1, y1, lst_j1, color, c = j1(color, lst_j1, liste_position_joueur)
        longueur(color, lst_j2, lst_j1, x1, y1, c)
        efface(txt_joueur), efface(txt_compteur)
        txt = 'Tour du joueur ' + '2'        
        txt_joueur, txt_compteur = texte(largeur_Fenetre//2-largeur_Fenetre//10, 0, txt, color), texte(largeur_Fenetre//2 - largeur_Fenetre//10, hauteur_Fenetre-50, txt_tour, color, police='')
        x2, y2, lst_j2, color, c = j2(color, lst_j2, liste_position_joueur)
        longueur(color, lst_j1, lst_j2, x2, y2, c)
        efface(txt_joueur), efface(txt_compteur)
        print("Coordonnées des boules de tous les joueurs : ",liste_position_joueur)
    attente_clic()
    ferme_fenetre()
# Fonction principale ---------------------------------------------------------
# Programme principal ---------------------------------------------------------
if __name__ == '__main__':
    GAME()