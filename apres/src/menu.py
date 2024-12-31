# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
import couleurs
import boutons
import upemtk
from default import *


def clear_menu():
    """La fonction prend en paramètre la variable booléenne V_menu et retourne cette même variable.
    Cette fonction permet de supprimer les six boutons ainsi que le bouton 'Start' pour commencer le jeu.

    Returns:
        V_menu (bool): Renvoie la variable booléenne V_menu en la mettant à True pour quitter le menu.
    """
    upemtk.efface('fond')
    upemtk.efface('game')
    upemtk.efface('sablier'), upemtk.efface('text_sablier')
    upemtk.efface('scores'), upemtk.efface('text_scores')
    upemtk.efface('taille_des_boules'), upemtk.efface('text_taille_des_boules')
    upemtk.efface('dynamique'), upemtk.efface('text_dynamique')
    upemtk.efface('terminaison'), upemtk.efface('text_terminaison')
    upemtk.efface('obstacles'), upemtk.efface('text_obstacles')
    upemtk.efface('play'), upemtk.efface('text_play')
    upemtk.efface('variantes')
    upemtk.mise_a_jour()
    return True


def init_boutons(variantes):
    """Permet de changer les activations/désactivations des six variantes dans le menu, tout est stocker dans le dictionnaire (len(dict() = 6)).

    Args:
        variantes (dict): Dictionnaire de variantes qui permet de savoir si une variante est activée ou non.

    Returns:
        variantes (dict): Renvoie un dictionnaire de variantes avec les variantes activées ou désactivées.
        V_menu (bool): Variable booléenne qui permet de savoir si le menu est activé ou non.
    """
    def verifyButton(variation, x, y, key, bouton):
        """Vérifie si le bouton a été cliqué ou une touche a été pressée et change la valeur de la variante.

        Args:
            variation (str): Nom de la variante.
            x (int): Coordonnée x du clic.
            y (int): Coordonnée y du clic.
            key (str): Touche press
            bouton (dict): Dictionnaire du bouton.

        Returns:
            bool: Renvoie vrai si le bouton a été cliqué ou une touche a été pressée, sinon faux.
        """
        if (bouton["x1"] < x < bouton["x2"] and bouton["y1"] < y < bouton["y2"]) or y in bouton["keys"]:
            variantes[variation] = boutons.f_boutons(variantes[variation], bouton["x1"], bouton["x2"], bouton["y1"], bouton["y2"], bouton["text_x"], bouton["text_y"], bouton["label"], variation)
            return True
        return False

    buttons_info = [
        {"variation": "sablier", "x1": b_gauche_x1, "x2": b_gauche_x2, "y1": b1_y1, "y2": b1_y2, "text_x": largeur_Fenetre // 2 - 550, "text_y": hauteur_Fenetre // 2 - 150, "label": "Sablier", "text_tag": "text_sablier", "keys": ["1", "KP_1", "ampersand"]},
        {"variation": "scores", "x1": b_gauche_x1, "x2": b_gauche_x2, "y1": b_milieu_y1, "y2": b_milieu_y2, "text_x": largeur_Fenetre // 2 - 550, "text_y": hauteur_Fenetre // 2, "label": "Scores", "text_tag": "text_scores", "keys": ["2", "KP_2", "eacute"]},
        {"variation": "taille", "x1": b_gauche_x1, "x2": b_gauche_x2, "y1": b3_y1, "y2": b3_y2, "text_x": largeur_Fenetre // 2 - 550, "text_y": hauteur_Fenetre // 2 + 150, "label": "Taille Des Boules", "text_tag": "text_taille_des_boules", "keys": ["3", "KP_3", "quotedbl"]},
        {"variation": "dynamique", "x1": b_droit_x1, "x2": b_droit_x2, "y1": b4_y1, "y2": b4_y2, "text_x": largeur_Fenetre // 2 + 550, "text_y": hauteur_Fenetre // 2 - 150, "label": "Version Dynamique", "text_tag": "text_dynamique", "keys": ["4", "KP_4", "apostrophe"]},
        {"variation": "terminaison", "x1": b_droit_x1, "x2": b_droit_x2, "y1": b_milieu_y1, "y2": b_milieu_y2, "text_x": largeur_Fenetre // 2 + 550, "text_y": hauteur_Fenetre // 2, "label": "Terminaison", "text_tag": "text_terminaison", "keys": ["5", "KP_5", "parenleft"]},
        {"variation": "obstacle", "x1": b_droit_x1, "x2": b_droit_x2, "y1": b6_y1, "y2": b6_y2, "text_x": largeur_Fenetre // 2 + 550, "text_y": hauteur_Fenetre // 2 + 150, "label": "Obstacles", "text_tag": "text_obstacles", "keys": ["6", "KP_6", "minus"]}
    ]

    V_menu = False
    while not V_menu:
        x, y, e = upemtk.attente_clic_ou_touche()

        # Vérification des boutons de variantes
        for button in buttons_info:
            if verifyButton(button["variation"], x, y, e, button):
                break

        # Bouton "Start"
        if largeur_Fenetre//2-150 < x < largeur_Fenetre//2+150 and b_milieu_y1 < y < b_milieu_y2 or e == "Return" or e == "KP_Return":
            V_menu = clear_menu()
        # Bouton "Quitter"
        elif largeur_Fenetre - 75 < x < largeur_Fenetre - 25 and 25 < y < 75 or e == "Escape" or e == "KP_Escape":
            return variantes, False
    return variantes, V_menu


def menu():
    """Cette fonction renvoie les variables booléennes des six variantes. Elle permet de créer le menu.

    Returns:
        variantes (dict): Renvoie un dictionnaire de variantes avec les variantes activées ou désactivées.
        V_menu (bool): Variable booléenne qui permet de savoir si le menu est activé ou non.
    """
    variantes = {
        'sablier': True,
        'scores': True,
        'taille': True,
        'dynamique': True,
        'terminaison': True,
        'obstacle': True
    }
    upemtk.texte(largeur_Fenetre // 2, 50, "Choisissez vos variantes !", taille=36, police=game_font, ancrage="center", tag='variantes')
    variantes = boutons.default_buttons(variantes)
    upemtk.rectangle(largeur_Fenetre // 2 - 150, b_milieu_y1, largeur_Fenetre // 2 + 150, b_milieu_y2, couleur='white', remplissage='black', epaisseur=3, tag='play')
    upemtk.texte(largeur_Fenetre // 2, txt_y2, "Start", couleur='white', police=game_font, ancrage='center', tag='text_play')
    boutons.quit_button()
    # Initialisation des coordonnées de chaque coins des rectangles / boutons en fonction de la largeur et de la hauteur de la fenêtre, la première ligne d’initialisation correspond au quatre point y.
    variantes, V_menu = init_boutons(variantes)
    return variantes, V_menu


def choose_colors():
    """Cette fonction permet de choisir les couleurs des joueurs.

    Returns:
        color1 (str): Couleur du joueur 1.
        color2 (str): Couleur du joueur 2.
    """
    color_selection_message = upemtk.texte(largeur_Fenetre // 2, hauteur_Fenetre // 2, "Choisissez une paire de couleurs\nqui représentera la couleur\nde chacun des joueurs", ancrage='center', police=game_font, taille=18, tag="question")
    isColors = False
    color1, color2 = None, None
    while isColors is False:
        x, y, e = upemtk.attente_clic_ou_touche()
        color1, color2, isColors = couleurs.choose_colors(x, y)
    upemtk.efface(color_selection_message)
    if color1 == "quit" and color2 == "quit":
        return "quit", "quit"
    return color1, color2
