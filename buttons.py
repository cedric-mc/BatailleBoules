# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *


def default_buttons(variantes):
    variantes["sablier"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, txt_gauche_x, txt_y1, "Sablier", "sablier", "text_sablier")
    variantes["scores"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b_milieu_y1, b_milieu_y2, txt_gauche_x, txt_y2, "Scores", "scores", "text_scores")
    variantes["taille"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b3_y1, b3_y2, txt_gauche_x, txt_y3, "Taille Des Boules", "taille_des_boules", "text_taille_des_boules")
    variantes["dynamique"] = f_boutons(True, b_droit_x1, b_droit_x2, b4_y1, b4_y2, txt_droite_x, txt_y1, "Version Dynamique", "dynamique", "text_dynamique")
    variantes["terminaison"] = f_boutons(True, b_droit_x1, b_droit_x2, b_milieu_y1, b_milieu_y2, txt_droite_x, txt_y2, "Terminaison", "terminaison", "text_terminaison")
    variantes["obstacle"] = f_boutons(True, b_droit_x1, b_droit_x2, b6_y1, b6_y2, txt_droite_x, txt_y3, "Obstacles", "obstacles", "text_obstacles")
    return variantes


def f_boutons(variante, rec_x1, rec_x2, rec_y1, rec_y2, txt_x, txt_y, txt_in, tag1, tag2):
    """Cette fonction prend en paramètre une variante booléenne correspond à une des six variantes,
    rec_x1 : la coordonnée x du point supérieur gauche (première valeur pour dessiner un rectangle) ; type : int.
    rec_x2 : la coordonnée x du point inférieur droit (quatrième valeur pour dessiner un rectangle) ; type : int.
    rec_y1 : la coordonnée y du point supérieur gauche (deuxième valeur pour dessiner un rectangle) ; type : int.
    rec_y2 : la coordonnée y du point inférieur droit (troisième valeur pour dessiner un rectangle) ; type : int.
    txt_x : position x du texte ; type : int.
    txt_y : position y du texte ; type : int.
    txt_in : chaîne de caractères pour indiquer le texte à l'intérieur du bouton.
    tag1, tag2 : chaînes de caractères correspondant aux identifiants des composantes du bouton (rectangle + texte).
    Renvoie la variante.
    La fonction permet de changer l'apparence du bouton."""
    efface(tag1), efface(tag2)
    if not variante:
        variante = True
        rectangle(rec_x1, rec_y1, rec_x2, rec_y2, couleur='black', remplissage='#00FF00', epaisseur=3, tag=tag1)
        texte(txt_x, txt_y, txt_in, couleur='black', ancrage="center", police="Monocraft", taille=18, tag=tag2)
    else:
        variante = False
        rectangle(rec_x1, rec_y1, rec_x2, rec_y2, couleur='black', remplissage='#FF0000', epaisseur=3, tag=tag1)
        texte(txt_x, txt_y, txt_in, couleur='black', ancrage="center", police="Monocraft", taille=18, tag=tag2)
    return variante


def pause_button():
    rectangle(largeur_Fenetre//2-150, b_milieu_y1, largeur_Fenetre//2+150, b_milieu_y2, couleur='black', remplissage='black', epaisseur=3, tag='pause')
    texte(largeur_Fenetre//2, txt_y2, "Pause", couleur='white', police="Monocraft", ancrage='center', tag='text_pause')
    mise_a_jour()


def quit_button():
    rectangle(largeur_Fenetre-75, 25, largeur_Fenetre-25, 75, couleur='black', remplissage='red', epaisseur=3, tag='quit')
    x1_diag = largeur_Fenetre-70
    y1_diag = 30
    x2_diag = largeur_Fenetre-30
    y2_diag = 70
    # Trace les deux traits diagonaux
    ligne(x1_diag, y1_diag, x2_diag, y2_diag, epaisseur=3, tag="croix1") # Premier trait diagonal
    ligne(x1_diag, y2_diag, x2_diag, y1_diag, epaisseur=3, tag="croix2") # Deuxième trait diagonal
    mise_a_jour()