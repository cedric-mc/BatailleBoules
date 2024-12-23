# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le doissier source
from variantes import *


def J1(x, y, dico_j1, dico_j2, rayon, banque1, color1, color2):
    """Paramètres :
    - x, y : position du clic et donc du potentiel futur emplacement d'un cercle ;
    - dico_j1, dico_j2 : dictionnaires des deux joueurs ;
    - compteur : le numéro du tour, type : int ;
    - tour : nombre de tours, type : int ;
    - rayon : rayon du cercle à poser en pixels ;
    - banque1 : budget du joueur pour la variante Taille des Boules, type : int ;
    - V_terminaison : variable booléenne indiquant si la variante Terminaison est activée.
    Renvoie les dictionnaires des deux joueurs, le nombre de tours et le budget du joueur pour la variante Taille des Boules.
    Cette fonction permet de créer le cercle du Joueur 1 ou diviser un cercle adverse."""
    diviser = False
    if dico_j2 != {}:  # Si le joueur 2 a jouer
        diviser, dico_j2 = in_cercle(dico_j2, x, y, color2)
    if not diviser:
        if type(banque1) == int:
            banque1, rayon = taille_des_boules(banque1, color1)
        c = cercle(x, y, rayon, couleur=color1, remplissage=color1) # insère un cercle d'une certaine couleur dans la fenêtre
        dico_j1[c] = [x, y, rayon]
        if intersection(dico_j2, x, y, rayon):
            efface(c)
            dico_j1.pop(c)
    return dico_j1, dico_j2, banque1


def J2(x, y, dico_j2, dico_j1, rayon, banque2, color1, color2):
    """Paramètres :
    - x, y : position du clic et donc du potentiel futur emplacement d'un cercle ;
    - dico_j2, dico_j1 : dictionnaires des deux joueurs ;
    - compteur : le numéro du tour, type : int ;
    - tour : nombre de tours, type : int ;
    - rayon : rayon du cercle à poser en pixels ;
    - banque2 : budget du joueur pour la variante Taille des Boules, type : int ;
    - V_terminaison : variable booléenne indiquant si la variante Terminaison est activée.
    Renvoie les dictionnaires des deux joueurs, le nombre de tours et le budget du joueur pour la variante Taille des Boules.
    Cette fonction permet de créer le cercle du Joueur 2 ou diviser un cercle adverse."""
    diviser = False
    if dico_j1 != {}:
        diviser, dico_j1 = in_cercle(dico_j1, x, y, color1)
    if not diviser:
        if type(banque2) == int:
            banque2, rayon = taille_des_boules(banque2, color2)
        c = cercle(x, y, rayon, couleur=color2, remplissage=color2)
        dico_j2[c] = [x, y, rayon]
        if intersection(dico_j1, x, y, rayon):
            efface(c)
            dico_j2.pop(c)
    return dico_j2, dico_j1, banque2
