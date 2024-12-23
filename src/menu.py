# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import efface, attente_clic_ou_touche, texte, rectangle, mise_a_jour
from default import b_gauche_x1, b_gauche_x2, b1_y1, b1_y2, largeur_Fenetre, hauteur_Fenetre, b_milieu_y1, b_milieu_y2, b3_y1, b3_y2, b_droit_x1, b_droit_x2, b4_y1, b4_y2, b6_y1, b6_y2, txt_y2, game_font
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
    """Permet de changer les activations/désactivations des six variantes dans le menu, tout est stocker dans le dictionnaire (len(dict() = 6)).

    Args:
        variantes (dict): Dictionnaire de variantes qui permet de savoir si une variante est activée ou non.

    Returns:
        variantes (dict): Renvoie un dictionnaire de variantes avec les variantes activées ou désactivées.
        V_menu (bool): Variable booléenne qui permet de savoir si le menu est activé ou non.
    """
    def verifyButton(variation, x, y, key, bouton):
        """Vérifie si le bouton a été cliqué ou une touche a été pressée et change la valeur de la variante."""
        if (bouton["x1"] < x < bouton["x2"] and bouton["y1"] < y < bouton["y2"]) or y in bouton["keys"]:
            variantes[variation] = buttons.f_boutons(variantes[variation], bouton["x1"], bouton["x2"], bouton["y1"], bouton["y2"], bouton["text_x"], bouton["text_y"], bouton["label"], variation, bouton["text_tag"])
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
        x, y, e = attente_clic_ou_touche()

        # Vérification des boutons de variantes
        for button in buttons_info:
            if verifyButton(button["variation"], x, y, e, button):
                break

        # Bouton "Start"
        if largeur_Fenetre//2-150 < x < largeur_Fenetre//2+150 and b_milieu_y1 < y < b_milieu_y2 or e == "Return" or e == "KP_Return":
            V_menu = Start_bouton()
        # Bouton "Quitter"
        elif largeur_Fenetre - 75 < x < largeur_Fenetre - 25 and 25 < y < 75 or e == "Escape" or e == "KP_Escape":
            return variantes, False
        mise_a_jour()
    return variantes, V_menu


def menu():
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
    texte(largeur_Fenetre//2, 50, "Choisissez vos variantes !", taille=36, police=game_font, ancrage="center", tag='variantes')
    variantes = buttons.default_buttons(variantes)
    rectangle(largeur_Fenetre//2-150, b_milieu_y1, largeur_Fenetre//2+150, b_milieu_y2, couleur='white', remplissage='black', epaisseur=3, tag='play')
    texte(largeur_Fenetre//2, txt_y2, "Start", couleur='white', police=game_font, ancrage='center', tag='text_play')
    buttons.quit_button()
    mise_a_jour()
    # Initialisation des coordonnées de chaque coins des rectangles / boutons en fonction de la largeur et de la hauteur de la fenêtre, la première ligne d’initialisation correspond au quatre point y.
    variantes, V_menu = boutons(variantes)
    return variantes, V_menu


def choose_colors():
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Choisissez une paire de couleurs\nqui représentera la couleur\nde chacun des joueurs", ancrage='center', police=game_font, taille=18, tag="question")
    isColors = False
    color1, color2 = None, None
    while isColors is False:
        x, y, e = attente_clic_ou_touche()
        color1, color2, isColors = colors.choose_colors(x, y)
    efface("question")
    if color1 == "quit" and color2 == "quit":
        return "quit", "quit"
    return color1, color2
