# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *


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


def Start_bouton(V_menu):
    """La fonction prend en paramètre la variable booléenne V_menu et retourne cette même variable.
    Cette fonction permet de supprimer les six boutons ainsi que le bouton 'Start' pour commencer le jeu."""
    V_menu = True
    efface('fond')
    efface('game')
    efface('sablier'), efface('text_sablier')
    efface('scores'), efface('text_scores')
    efface('taille_des_boules'), efface('text_taille_des_boules')
    efface('dynamique'), efface('text_dynamique')
    efface('terminaison'), efface('text_terminaison')
    efface('obstacles'), efface('text_obstacles')
    efface('play'), efface('text_play')
    efface("rules"), efface("text_rules")
    return V_menu


def boutons(V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle):
    """Cette fonction prend en paramètre les variables booléennes des six variantes (en False au départ).
    Renvoie les 6 variables booléennes.
    Cette fonction permet de changer les activations/désactivations des six variantes dans le menu."""
    V_menu = False
    while V_menu != True:
        x, y, e = attente_clic_ou_touche()
        if (b_gauche_x1 < x < b_gauche_x2 and b1_y1 < y < b1_y2) or y == "1" or y == 'KP_1' or y == "ampersand":
            V_sablier = f_boutons(V_sablier, b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, largeur_Fenetre//2-550, hauteur_Fenetre//2-150, "Sablier", "sablier", "text_sablier")
        elif (b_gauche_x1 < x < b_gauche_x2 and b_milieu_y1 < y < b_milieu_y2) or y == "2" or y == 'KP_2' or y == "eacute":
            V_scores = f_boutons(V_scores, b_gauche_x1, b_gauche_x2, b_milieu_y1, b_milieu_y2, largeur_Fenetre//2-550, hauteur_Fenetre//2, "Scores", "scores", "text_scores")
        elif (b_gauche_x1 < x < b_gauche_x2 and b3_y1 < y < b3_y2) or y == "3" or y == "KP_3" or y == "quotedbl":
            V_taille = f_boutons(V_taille, b_gauche_x1, b_gauche_x2, b3_y1, b3_y2, largeur_Fenetre//2-550, hauteur_Fenetre//2+150, "Taille Des Boules", "taille_des_boules", "text_taille_des_boules")
        elif (b_droit_x1 < x < b_droit_x2 and hauteur_Fenetre//2-200 < y < hauteur_Fenetre//2-100) or y == "4" or y == "KP_4" or y == "apostrophe":
            V_dynamique = f_boutons(V_dynamique, b_droit_x1, b_droit_x2, b4_y1, b4_y2, largeur_Fenetre//2+550, hauteur_Fenetre//2-150, "Version Dynamique", "dynamique", "text_dynamique")
        elif (b_droit_x1 < x < b_droit_x2 and b_milieu_y1 < y < b_milieu_y2) or y == "5" or y == "KP_5" or y == "parenleft":
            V_terminaison = f_boutons(V_terminaison, b_droit_x1, b_droit_x2, b_milieu_y1, b_milieu_y2, largeur_Fenetre//2+550, hauteur_Fenetre//2, "Terminaison", "terminaison", "text_terminaison")
        elif (b_droit_x1 < x < b_droit_x2 and b6_y1 < y < b6_y2) or y == "6" or y == "KP_6" or y == "minus":
            V_obstacle = f_boutons(V_obstacle, b_droit_x1, b_droit_x2, b6_y1, b6_y2, largeur_Fenetre//2+550, hauteur_Fenetre//2+150, "Obstacles", "obstacles", "text_obstacles")
        elif (largeur_Fenetre//2-150 < x < largeur_Fenetre//2+150 and b_milieu_y1 < y < b_milieu_y2) or y == "Return" or y == "KP_Return":
            V_menu = Start_bouton(V_menu)
    return V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle


def MENU():
    """Cette fonction renvoie les variables booléennes des six variantes.
    MENU permet de créer le menu."""
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = True, True, True, True, True, True
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bienvenue !", taille=40, police="Monocraft", ancrage="center", tag='jouer')
    attente_clic_ou_touche()
    efface('jouer')
    V_sablier = f_boutons(V_sablier, b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, txt_gauche_x, txt_y1, "Sablier", "sablier", "text_sablier")
    V_scores = f_boutons(V_scores, b_gauche_x1, b_gauche_x2, b_milieu_y1, b_milieu_y2, txt_gauche_x, txt_y2, "Scores", "scores", "text_scores")
    V_taille = f_boutons(V_taille, b_gauche_x1, b_gauche_x2, b3_y1, b3_y2, txt_gauche_x, txt_y3, "Taille Des Boules", "taille_des_boules", "text_taille_des_boules")
    V_dynamique = f_boutons(V_dynamique, b_droit_x1, b_droit_x2, b4_y1, b4_y2, txt_droite_x, txt_y1, "Version Dynamique", "dynamique", "text_dynamique")
    V_terminaison = f_boutons(V_terminaison, b_droit_x1, b_droit_x2, b_milieu_y1, b_milieu_y2, txt_droite_x, txt_y2, "Terminaison", "terminaison", "text_terminaison")
    V_obstacle = f_boutons(V_obstacle, b_droit_x1, b_droit_x2, b6_y1, b6_y2, txt_droite_x, txt_y3, "Obstacles", "obstacles", "text_obstacles")
    rectangle(largeur_Fenetre//2-150, b_milieu_y1, largeur_Fenetre//2+150, b_milieu_y2, couleur='white', remplissage='black', epaisseur=3, tag='play')
    texte(largeur_Fenetre//2, txt_y2, "Start", couleur='white', police="Monocraft", ancrage='center', tag='text_play')
    mise_a_jour()
    # Initialisation des coordonnées de chaque coins des rectangles / boutons en fonction de la largeur et de la hauteur de la fenêtre, la première ligne d’initialisation correspond au quatre point y.
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = boutons(V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle)
    return V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle


def choose_colors():
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Choisissez une paire de couleurs\nqui représentera la couleur de chacun", ancrage='center', police="Monocraft", taille=18, tag="question")
    x, y, e = attente_clic()
    if largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and 100 < y < 250:
        color1, color2 = "#FF7900", "#F7E360"
    elif largeur_Fenetre//2-350 < x < largeur_Fenetre//2-50 and 100 < y < 250:
        color1, color2 = "#F33129", "#0179C0"
    elif largeur_Fenetre//2+50 < x < largeur_Fenetre+350 and 100 < y < 250:
        color1, color2 = "#2C6452", "#F7777F"
    elif largeur_Fenetre//2+400 < x < largeur_Fenetre//2+700 and 100 < y < 250:
        color1, color2 = "#552B24", "#F33129"
    
    if largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and hauteur_Fenetre//2-75 < y < hauteur_Fenetre//2+75:
        color1, color2 = "#0179C0", "#65419C"
    elif largeur_Fenetre//2+400 < x < largeur_Fenetre//2+700 and hauteur_Fenetre//2-75 < y < hauteur_Fenetre//2+75:
        color1, color2 = "#F7777F", "#0179C0"

    elif largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#65419C", "#F7777F"
    elif largeur_Fenetre//2-350 < x < largeur_Fenetre//2-50 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#2C6452", "#F7E360"
    elif largeur_Fenetre//2+50 < x < largeur_Fenetre+350 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#F33129", "#F7E360"
    elif largeur_Fenetre//2+400 < x < largeur_Fenetre//2+700 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#552B24", "#F7777F"
    efface("question")
    return color1, color2