# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *
import colors
import buttons


def Start_bouton():
    """La fonction prend en paramètre la variable booléenne V_menu et retourne cette même variable.
    Cette fonction permet de supprimer les six boutons ainsi que le bouton 'Start' pour commencer le jeu."""
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
    efface('variantes')
    return True


def boutons(variantes):
    """Cette fonction prend en paramètre le dictionnaire des variables booléennes des six variantes (en False au départ).
    Renvoie les 6 variables booléennes.
    Cette fonction permet de changer les activations/désactivations des six variantes dans le menu, tout est stocker dans le dictionnaire (len(dict() = 6))."""
    V_menu = False
    while V_menu != True:
        x, y, e = attente_clic_ou_touche()
        if (b_gauche_x1 < x < b_gauche_x2 and b1_y1 < y < b1_y2) or y == "1" or y == 'KP_1' or y == "ampersand":
            variantes["sablier"] = buttons.f_boutons(variantes["sablier"], b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, largeur_Fenetre//2-550, hauteur_Fenetre//2-150, "Sablier", "sablier", "text_sablier")
        elif (b_gauche_x1 < x < b_gauche_x2 and b_milieu_y1 < y < b_milieu_y2) or y == "2" or y == 'KP_2' or y == "eacute":
            variantes["scores"] = buttons.f_boutons(variantes["scores"], b_gauche_x1, b_gauche_x2, b_milieu_y1, b_milieu_y2, largeur_Fenetre//2-550, hauteur_Fenetre//2, "Scores", "scores", "text_scores")
        elif (b_gauche_x1 < x < b_gauche_x2 and b3_y1 < y < b3_y2) or y == "3" or y == "KP_3" or y == "quotedbl":
            variantes["taille"] = buttons.f_boutons(variantes["taille"], b_gauche_x1, b_gauche_x2, b3_y1, b3_y2, largeur_Fenetre//2-550, hauteur_Fenetre//2+150, "Taille Des Boules", "taille_des_boules", "text_taille_des_boules")
        elif (b_droit_x1 < x < b_droit_x2 and hauteur_Fenetre//2-200 < y < hauteur_Fenetre//2-100) or y == "4" or y == "KP_4" or y == "apostrophe":
            variantes["dynamique"] = buttons.f_boutons(variantes["dynamique"], b_droit_x1, b_droit_x2, b4_y1, b4_y2, largeur_Fenetre//2+550, hauteur_Fenetre//2-150, "Version Dynamique", "dynamique", "text_dynamique")
        elif (b_droit_x1 < x < b_droit_x2 and b_milieu_y1 < y < b_milieu_y2) or y == "5" or y == "KP_5" or y == "parenleft":
            variantes["terminaison"] = buttons.f_boutons(variantes["terminaison"], b_droit_x1, b_droit_x2, b_milieu_y1, b_milieu_y2, largeur_Fenetre//2+550, hauteur_Fenetre//2, "Terminaison", "terminaison", "text_terminaison")
        elif (b_droit_x1 < x < b_droit_x2 and b6_y1 < y < b6_y2) or y == "6" or y == "KP_6" or y == "minus":
            variantes["obstacle"] = buttons.f_boutons(variantes["obstacle"], b_droit_x1, b_droit_x2, b6_y1, b6_y2, largeur_Fenetre//2+550, hauteur_Fenetre//2+150, "Obstacles", "obstacles", "text_obstacles")
        elif (largeur_Fenetre//2-150 < x < largeur_Fenetre//2+150 and b_milieu_y1 < y < b_milieu_y2) or y == "Return" or y == "KP_Return":
            V_menu = Start_bouton()
        elif (largeur_Fenetre-75 < x < largeur_Fenetre-25 and 25 < y < 75) or y == "Escape" or y == "KP_Escape":
            return variantes, False
    return variantes, V_menu


def MENU():
    """Cette fonction renvoie les variables booléennes des six variantes.
    MENU permet de créer le menu."""
    variantes = {
        'sablier': True,
        'scores': True,
        'taille': True,
        'dynamique': True,
        'terminaison': True,
        'obstacle': True
    }
    texte(largeur_Fenetre//2, 50, "Choisissez vos variantes !", taille=36, police="Monocraft", ancrage="center", tag='variantes')
    variantes = buttons.default_buttons(variantes)
    rectangle(largeur_Fenetre//2-150, b_milieu_y1, largeur_Fenetre//2+150, b_milieu_y2, couleur='white', remplissage='black', epaisseur=3, tag='play')
    texte(largeur_Fenetre//2, txt_y2, "Start", couleur='white', police="Monocraft", ancrage='center', tag='text_play')
    buttons.quit_button()
    mise_a_jour()
    # Initialisation des coordonnées de chaque coins des rectangles / boutons en fonction de la largeur et de la hauteur de la fenêtre, la première ligne d’initialisation correspond au quatre point y.
    variantes, V_menu = boutons(variantes)
    return variantes, V_menu


def choose_colors():
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Choisissez une paire de couleurs\nqui représentera la couleur\nde chacun des joueurs", ancrage='center', police="Monocraft", taille=18, tag="question")
    isColors = False
    while isColors is False:
        x, y, e = attente_clic_ou_touche()
        color1, color2, isColors = colors.choose_colors(x, y)
    efface("question")
    if color1 == "quit" and color2 == "quit":
        return "quit", "quit"
    return color1, color2
