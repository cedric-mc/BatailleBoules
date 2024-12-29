# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
from string import ascii_letters
import upemtk
from default import *


def f_caracteres_speciaux(key):
    """Cette fonction permet de convertir les touches spéciales du clavier en caractères spéciaux.
    Les touches prises en compte dans la fonction sont uniquement celles des caractères spéciaux (du 1 au +).

    Args:
        key (str): La touche appuyée.

    Returns:
        str: La chaîne correspondant à la touche de clavier (exemple : la touche "eacute" équivaut au caractère 'é').
    """
    # Vérification de la correspondance de la touche avec celles des caractères spéciaux (du 1 au +).
    if key == 'ampersand':
        return "&"
    elif key == 'eacute':
        return "é"
    elif key == 'quotedbl':
        return '"'
    elif key == 'apostrophe':
        return "'"
    elif key == 'parenleft':
        return "("
    elif key == 'minus':
        return "-"
    elif key == 'egrave':
        return "è"
    elif key == 'underscore':
        return "_"
    elif key == 'ccedilla':
        return "ç"
    elif key == 'agrave':
        return "à"
    elif key == 'parenright':
        return ")"
    elif key == 'equal':
        return "="


def enter_surname(joueur, color):
    """Cette fonction permet d'entrer un pseudo pour le joueur.

    Args:
        joueur (int): Le numéro du joueur 1 ou 2.
        color (str): Couleur du texte.

    Returns:
        str: Le pseudo du joueur entré ou celui par défaut.
    """
    # Incrémentation des touches du clavier dans une liste s'ils correspondent aux critères.
    lst = list()
    x, y, e = None, None, None
    while y != 'Return' and y != 'KP_Enter':
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(lst), couleur=color, police=game_font, ancrage='center', taille=20, tag='pseudo')
        x, y, e = upemtk.attente_clic_ou_touche()
        if ((e == "ClicGauche" or e == "ClicDroit") and (largeur_Fenetre-75 <= x <= largeur_Fenetre-25) and (25 <= y <= 75)) or y == "Escape" or y == "KP_Escape":
            return "quit"
        elif e == "Touche":
            if y in ascii_letters:
                lst.append(y)
            elif y in caracteres_speciaux:
                lst.append(f_caracteres_speciaux(y))
            elif y == '1' or y == 'KP_1':
                lst.append('1')
            elif y == '2' or y == 'KP_2':
                lst.append('2')
            elif y == '3' or y == 'KP_3':
                lst.append('3')
            elif y == '4' or y == 'KP_4':
                lst.append('4')
            elif y == '5' or y == 'KP_5':
                lst.append('5')
            elif y == '6' or y == 'KP_6':
                lst.append('6')
            elif y == '7' or y == 'KP_7':
                lst.append('7')
            elif y == '8' or y == 'KP_8':
                lst.append('8')
            elif y == '9' or y == 'KP_9':
                lst.append('9')
            elif y == '0' or y == 'KP_0':
                lst.append('0')
            elif (y == 'BackSpace' or y == 'Delete') and lst != []:
                lst.pop()
        upemtk.efface('pseudo')
        upemtk.mise_a_jour()
    if not lst:
        pseudo = str("Joueur " + str(joueur))
    else:
        pseudo = "".join(lst)
    return pseudo


def surname(lst_colors):
    """Cette fonction permet d'entrer les pseudos des deux joueurs.

    Args:
        lst_colors (list): Liste des couleurs des joueurs.

    Returns:
        pseudo1 (str): Pseudo du joueur 1.
        pseudo2 (str): Pseudo du joueur 2.
    """
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du premier Joueur, (pseudo 'quit' interdit)", couleur=lst_colors[0], police=game_font, ancrage='center', taille=20, tag='names')
    pseudo1 = enter_surname(1, lst_colors[0])
    upemtk.efface('names')
    if pseudo1 == "quit":
        return "quit", "quit"
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du deuxième Joueur, (pseudo 'quit' interdit)", couleur=lst_colors[1], police=game_font, ancrage='center', taille=20, tag='names')
    pseudo2 = enter_surname(2, lst_colors[1])
    upemtk.efface('names')
    return pseudo1, pseudo2


def enter_numbers(color):
    """Cette fonction permet d'entrer le nombre de tours.

    Args:
        color (str): Couleur du texte.

    Returns:
        nb_tours (int): Nombre de tours.
    """
    numbers = []
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le nombre de tours en chiffre puis appuyez sur Entrée.\n(réfléchissez avant d'entrer, 5 tours minimum par joueur)", ancrage='center', police=game_font, taille=18, tag='tours', couleur=color)
    x, y, e = None, None, None
    while y != 'Return' and y != 'KP_Enter':
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(numbers),couleur=color, ancrage='center', police=game_font, taille=20, tag='liste')
        x, y, e = upemtk.attente_clic_ou_touche()
        if ((e == "ClicGauche" or e == "ClicDroit") and (largeur_Fenetre-75 <= x <= largeur_Fenetre-25) and (25 <= y <= 75)) or y == "Escape" or y == "KP_Escape":
            return "quit"
        elif e == "Touche":
            if y == '1' or y == 'ampersand' or y == 'KP_1':
                numbers.append('1')
            elif y == '2' or y == 'eacute' or y == 'KP_2':
                numbers.append('2')
            elif y == '3' or y == 'quotedbl' or y == 'KP_3':
                numbers.append('3')
            elif y == '4' or y == 'apostrophe' or y == 'KP_4':
                numbers.append('4')
            elif y == '5' or y == 'parenleft' or y == 'KP_5':
                numbers.append('5')
            elif y == '6' or y == 'minus' or y == 'KP_6':
                numbers.append('6')
            elif y == '7' or y == 'egrave' or y == 'KP_7':
                numbers.append('7')
            elif y == '8' or y == 'underscore' or y == 'KP_8':
                numbers.append('8')
            elif y == '9' or y == 'ccedilla' or y == 'KP_9':
                numbers.append('9')
            elif y == '0' or y == 'agrave' or y == 'KP_0':
                numbers.append('0')
            elif (y == 'BackSpace' or y == 'Delete') and numbers != []:
                numbers.pop()
        upemtk.efface('liste')
        upemtk.mise_a_jour()
    if not numbers:
        upemtk.efface('tours')
        return 5
    else:
        nb_tours = int("".join(numbers))
        if nb_tours < 5:
            nb_tours = 5
    upemtk.efface('tours')
    return nb_tours
