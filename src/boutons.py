# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
import upemtk
from default import *


def button_background_variantes(isActive):
    """Cette fonction prend en paramètre une variable booléenne et renvoie une couleur en fonction de la valeur de la variable.

    Args:
        isActive (bool): Variable booléenne qui permet de savoir si la variante est activée ou non.

    Returns:
        _type_ (str): Retourne une couleur en fonction de la valeur de la variable.
    """
    return '#00FF00' if isActive else '#FF0000'


def f_boutons(variante, rec_x1, rec_x2, rec_y1, rec_y2, txt_x, txt_y, txt_in, nametag):
    """Cette fonction prend en paramètre une variante booléenne correspond à une des six variantes et permet de changer l'apparence du bouton.

    Args:
        variante (bool): Variable booléenne qui permet de savoir si la variante est activée ou non.
        rec_x1 (int): La coordonnée x du point supérieur gauche (première valeur pour dessiner un rectangle).
        rec_x2 (int): La coordonnée x du point inférieur droit (quatrième valeur pour dessiner un rectangle).
        rec_y1 (int): La coordonnée y du point supérieur gauche (deuxième valeur pour dessiner un rectangle).
        rec_y2 (int): La coordonnée y du point inférieur droit (troisième valeur pour dessiner un rectangle).
        txt_x (int): Position x du texte.
        txt_y (int): Position y du texte.
        txt_in (str): Chaîne de caractères pour indiquer le texte à l'intérieur du bouton.
        nametag (str): Chaîne de caractères correspondant aux identifiants des composantes du bouton (rectangle + texte).

    Returns:
        variante (bool): Renvoie la variante.
    """
    upemtk.efface(nametag), upemtk.efface(f"text_{nametag}")
    variante = not variante
    upemtk.rectangle(rec_x1, rec_y1, rec_x2, rec_y2, couleur='black', remplissage=button_background_variantes(variante),
                     epaisseur=3, tag=nametag)
    upemtk.texte(txt_x, txt_y, txt_in, couleur='black', ancrage="center", police=game_font, taille=18,
                 tag=f"text_{nametag}")
    return variante


def default_buttons(variantes):
    """Cette fonction prend en paramètre un dictionnaire de variantes et permet de changer l'apparence des boutons en fonction de la valeur des variantes.

    Args:
        variantes (dict): Dictionnaire de variantes qui permet de savoir si une variante est activée ou non.

    Returns:
        variantes (dict): Renvoie un dictionnaire de variantes avec les boutons modifiés.
    """
    # TODO: Changer l'apparence des boutons pour un carré avec une image en haut et un texte en bas (tout centré et à l'intérieur du carré).
    variantes["sablier"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, txt_gauche_x, txt_y1, "Sablier", "sablier")
    variantes["scores"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b_milieu_y1, b_milieu_y2, txt_gauche_x, txt_y2, "Scores", "scores")
    variantes["taille"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b3_y1, b3_y2, txt_gauche_x, txt_y3, "Taille Des Boules", "taille_des_boules")
    variantes["dynamique"] = f_boutons(True, b_droit_x1, b_droit_x2, b4_y1, b4_y2, txt_droite_x, txt_y1, "Version Dynamique", "dynamique")
    variantes["terminaison"] = f_boutons(True, b_droit_x1, b_droit_x2, b_milieu_y1, b_milieu_y2, txt_droite_x, txt_y2, "Terminaison", "terminaison")
    variantes["obstacle"] = f_boutons(True, b_droit_x1, b_droit_x2, b6_y1, b6_y2, txt_droite_x, txt_y3, "Obstacles", "obstacles")
    return variantes


def pause_button():
    """Cette fonction permet de dessiner un bouton pause au centre de l'écran de jeu."""
    upemtk.rectangle(75, 25, 25, 75, remplissage='green', epaisseur=3, tag='pause')
    x1, y1 = 40, 35 # Coordonnée x et y du premier point du premier trait horizontal
    x2, y2 = 60, 65 # Coordonnée x et y du deuxième point du premier trait horizontal

    # Trace les 2 traits verticaux
    upemtk.ligne(x1, y1, x1, y2, epaisseur=4, tag="trait1") # Premier trait vertical
    upemtk.ligne(x2, y1, x2, y2, epaisseur=4, tag="trait2") # Deuxième trait vertical
    upemtk.mise_a_jour()


def clear_pause_button():
    """Cette fonction permet de supprimer le bouton pause."""
    upemtk.efface("pause"), upemtk.efface("trait1"), upemtk.efface("trait2")
    upemtk.mise_a_jour()


def quit_button():
    """Cette fonction permet de dessiner un bouton quitter en haut à droite de l'écran de jeu."""
    upemtk.rectangle(largeur_Fenetre-75, 25, largeur_Fenetre-25, 75, remplissage='red', epaisseur=3, tag='quit')

    x1, y1 = largeur_Fenetre - 65, 35 # Coordonnée x et y du premier point du premier trait diagonal
    x2, y2 = largeur_Fenetre - 35, 65 # Coordonnée x et y du deuxième point du premier trait diagonal

    # Trace les deux traits diagonaux
    upemtk.ligne(x1, y1, x2, y2, epaisseur=4, tag="croix1") # Premier trait diagonal
    upemtk.ligne(x1, y2, x2, y1, epaisseur=4, tag="croix2") # Deuxième trait diagonal
    upemtk.mise_a_jour()


def clear_quit_button():
    """Cette fonction permet de supprimer le bouton quitter."""
    upemtk.efface("quit"), upemtk.efface("croix1"), upemtk.efface("croix2")
    upemtk.mise_a_jour()
