# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
import upemtk
from default import largeur_Fenetre, game_font, b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, txt_gauche_x, txt_y1, b_milieu_y1, b_milieu_y2, txt_y2, b3_y1, b3_y2, txt_y3, b_droit_x1, b_droit_x2, b4_y1, b4_y2, txt_droite_x, b6_y1, b6_y2


def button_background(isActive):
    """Cette fonction prend en paramètre une variable booléenne et renvoie une couleur en fonction de la valeur de la variable.

    Args:
        isActive (bool): Variable booléenne qui permet de savoir si la variante est activée ou non.

    Returns:
        _type_ (str): Retourne une couleur en fonction de la valeur de la variable.
    """
    return '#00FF00' if isActive else '#FF0000'


def default_buttons(variantes):
    """Cette fonction prend en paramètre un dictionnaire de variantes et permet de changer l'apparence des boutons en fonction de la valeur des variantes.

    Args:
        variantes (dict): Dictionnaire de variantes qui permet de savoir si une variante est activée ou non.

    Returns:
        variantes (dict): Renvoie un dictionnaire de variantes avec les boutons modifiés.
    """
    # TODO: Changer l'apparence des boutons pour un carré avec une image en haut et un texte en bas (tout centré et à l'intérieur du carré).
    variantes["sablier"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, txt_gauche_x, txt_y1, "Sablier", "sablier", "text_sablier")
    variantes["scores"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b_milieu_y1, b_milieu_y2, txt_gauche_x, txt_y2, "Scores", "scores", "text_scores")
    variantes["taille"] = f_boutons(True, b_gauche_x1, b_gauche_x2, b3_y1, b3_y2, txt_gauche_x, txt_y3, "Taille Des Boules", "taille_des_boules", "text_taille_des_boules")
    variantes["dynamique"] = f_boutons(True, b_droit_x1, b_droit_x2, b4_y1, b4_y2, txt_droite_x, txt_y1, "Version Dynamique", "dynamique", "text_dynamique")
    variantes["terminaison"] = f_boutons(True, b_droit_x1, b_droit_x2, b_milieu_y1, b_milieu_y2, txt_droite_x, txt_y2, "Terminaison", "terminaison", "text_terminaison")
    variantes["obstacle"] = f_boutons(True, b_droit_x1, b_droit_x2, b6_y1, b6_y2, txt_droite_x, txt_y3, "Obstacles", "obstacles", "text_obstacles")
    return variantes


def f_boutons(variante, rec_x1, rec_x2, rec_y1, rec_y2, txt_x, txt_y, txt_in, tag1, tag2):
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
        tag1 (str): Chaînes de caractères correspondant aux identifiants des composantes du bouton (rectangle + texte).
        tag2 (str): Chaînes de caractères correspondant aux identifiants des composantes du bouton (rectangle + texte).
        
    Returns:
        variante (bool): Renvoie la variante."""
    upemtk.efface(tag1), upemtk.efface(tag2)
    variante = not variante
    upemtk.rectangle(rec_x1, rec_y1, rec_x2, rec_y2, couleur='black', remplissage=button_background(variante), epaisseur=3, tag=tag1)
    upemtk.texte(txt_x, txt_y, txt_in, couleur='black', ancrage="center", police=game_font, taille=18, tag=tag2)
    return variante


def pause_button():
    """Cette fonction permet de dessiner un bouton pause au centre de l'écran de jeu."""
    # rectangle(largeur_Fenetre//2-150, b_milieu_y1, largeur_Fenetre//2+150, b_milieu_y2, couleur='black', remplissage='black', epaisseur=3, tag='pause')
    # texte(largeur_Fenetre//2, txt_y2, "Pause", couleur='white', police=game_font, ancrage='center', tag='text_pause')
    # Dessine le bouton pause
    upemtk.rectangle(75, 25, 25, 75, remplissage='green', epaisseur=3, tag='pause')
    # Coordonnées x et y des 2 traits verticaux
    x1 = 40 # Coordonnée x du premier point du premier trait vertical
    y1 = 35 # Coordonnée y du premier point du premier trait vertical
    y2 = 65 # Coordonnée y du deuxième point du premier trait vertical
    x2 = 60 # Coordonnée x du deuxième point du deuxième trait vertical

    # Trace les 2 traits verticaux
    upemtk.ligne(x1, y1, x1, y2, epaisseur=4, tag="trait1") # Premier trait vertical
    upemtk.ligne(x2, y1, x2, y2, epaisseur=4, tag="trait2") # Deuxième trait vertical
    upemtk.mise_a_jour()


def quit_button():
    """Cette fonction permet de dessiner un bouton quitter en haut à droite de l'écran de jeu."""
    # Dessine le bouton quitter
    upemtk.rectangle(largeur_Fenetre-75, 25, largeur_Fenetre-25, 75, remplissage='red', epaisseur=3, tag='quit')
    # Coordonnées x et y des 2 traits diagonaux
    x1 = largeur_Fenetre-65 # Coordonnée x du premier point du premier trait diagonal
    y1 = 35 # Coordonnée y du premier point du premier trait diagonal
    x2 = largeur_Fenetre-35 # Coordonnée x du deuxième point du premier trait diagonal
    y2 = 65 # Coordonnée y du deuxième point du premier trait diagonal

    # Trace les deux traits diagonaux
    upemtk.ligne(x1, y1, x2, y2, epaisseur=4, tag="croix1") # Premier trait diagonal
    upemtk.ligne(x1, y2, x2, y1, epaisseur=4, tag="croix2") # Deuxième trait diagonal
    upemtk.mise_a_jour()


def clear_quit_button():
    """Cette fonction permet de supprimer le bouton quitter."""
    upemtk.efface("quit"), upemtk.efface("croix1"), upemtk.efface("croix2")
    upemtk.mise_a_jour()
