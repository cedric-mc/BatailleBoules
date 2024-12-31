# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
from variantes import *
import upemtk


def crayon(color, compteur, tour, pseudo):
    """Cette fonction permet d'afficher le numéro du tour et l'indication pour savoir qui doit jouer.

    Args:
        color (_type_): Couleur du texte.
        compteur (int): Compteur du tour.
        tour (int): Nombre de tours.
        pseudo (str): Pseudo du joueur.
    """
    txt = f"Tour de {pseudo}"
    txt_tour = f"Tour : {compteur}/{tour}"
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//18, txt, color, police=game_font, ancrage='center', taille=20, tag="joueur")
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre-hauteur_Fenetre//18, txt_tour, color, police=game_font, ancrage='center', taille=20, tag="tour")


def gomme():
    """Cette fonction efface le numéro (nombre) de tour et l'indication pour savoir qui doit jouer."""
    upemtk.efface("joueur"), upemtk.efface("tour")


# TODO: Ajouter la fonction tour() afin de remplacer les doubles fonctions J1() et J2().
def tour():
    """Description.

    Args:
        _type_ (type): Description.

    Returns:
        _type_ (type): Description.
    """
    pass


def J1(x, y, dico_j1, dico_j2, rayon, banque1, color1, color2):
    """Cette fonction permet de créer le cercle du Joueur 1 ou diviser un cercle adverse.

    Args:
        x (int): Coordonnée x du clic.
        y (int): Coordonnée y du clic.
        dico_j1 (dict): Dictionnaire des cercles du joueur 1.
        dico_j2 (dict): Dictionnaire des cercles du joueur 2.
        rayon (int): Rayon du cercle à poser.
        banque1 (int): Budget du joueur 1 pour la variante Taille des Boules.
        color1 (str): Couleur du joueur 1.
        color2 (str): Couleur du joueur 2.

    Returns:
        dico_j1 (dict): Dictionnaire des cercles du joueur 1.
        dico_j2 (dict): Dictionnaire des cercles du joueur 2.
        banque1 (int): Budget du joueur 1 pour la variante Taille des Boules.
    """
    diviser = False
    if dico_j2 != {}:  # Si le joueur 2 a jouer
        diviser, dico_j2 = in_cercle(dico_j2, x, y, color2)
    if not diviser:
        if type(banque1) == int:
            banque1, rayon = taille_des_boules(banque1, color1)
        c = upemtk.cercle(x, y, rayon, couleur=color1, remplissage=color1) # insère un cercle d'une certaine couleur dans la fenêtre
        dico_j1[c] = [x, y, rayon]
        if intersection(dico_j2, x, y, rayon):
            upemtk.efface(c)
            dico_j1.pop(c)
    return dico_j1, dico_j2, banque1


def J2(x, y, dico_j2, dico_j1, rayon, banque2, color1, color2):
    """Cette fonction permet de créer le cercle du Joueur 2 ou diviser un cercle adverse.

    Args:
        x (int): Coordonnée x du clic.
        y (int): Coordonnée y du clic.
        dico_j2 (dict): Dictionnaire des cercles du joueur 2.
        dico_j1 (dict): Dictionnaire des cercles du joueur 1.
        rayon (int): Rayon du cercle à poser.
        banque2 (int): Budget du joueur 2 pour la variante Taille des Boules.
        color1 (str): Couleur du joueur 1.
        color2 (str): Couleur du joueur 2.

    Returns:
        dico_j2 (dict): Dictionnaire des cercles du joueur 2.
        dico_j1 (dict): Dictionnaire des cercles du joueur 1.
        banque2 (int): Budget du joueur 2 pour la variante Taille des Boules.
    """
    diviser = False
    if dico_j1 != {}:
        diviser, dico_j1 = in_cercle(dico_j1, x, y, color1)
    if not diviser:
        if type(banque2) == int:
            banque2, rayon = taille_des_boules(banque2, color2)
        c = upemtk.cercle(x, y, rayon, couleur=color2, remplissage=color2)
        dico_j2[c] = [x, y, rayon]
        if intersection(dico_j1, x, y, rayon):
            upemtk.efface(c)
            dico_j2.pop(c)
    return dico_j2, dico_j1, banque2
