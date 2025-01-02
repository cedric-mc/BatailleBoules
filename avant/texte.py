# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis la bibliothèque Python
from string import ascii_letters


# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *


def f_caracteres_speciaux(key):
    """Cette fonction prend en paramètre la chaîne de caractères de la touche appuyée.
    Elle renvoie la chaîne correspondant à la touche de clavier (exemple : la touche "eacute" équivaut au caractère 'é'.
    Les touches prises en compte dans la fonction sont uniquement celles présentes entre la touche du carré et celle de suppression."""
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
    Elle prend comme paramètre le numéro du joueur 1 ou 2, c'est un entier.
    Elle renvoie le pseudo du joueur entré ou celui par défaut, type : str."""
    # Incrémentation des touches du clavier dans une liste s'ils correspondent aux critères.
    lst = list()
    x, y, e = None, None, None
    while y != 'Return' and y != 'KP_Enter':
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(lst), couleur=color, police=game_font, ancrage='center', taille=20, tag='pseudo')
        x, y, e = attente_clic_ou_touche()
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
        efface('pseudo')
        mise_a_jour()
    if not(lst):
        pseudo = str("Joueur " + str(joueur))
    else:
        pseudo = "".join(lst)
    return pseudo


def surname(color1, color2):
    """Fait appel à la fonction enter_surname pour entrer les noms des deux joueurs, c'est accompagné d'un texte pour indiqué pour qui doit être entrer le pseudo.
    Elle renvoie les deux pseudos, type : str"""
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du premier Joueur, (pseudo 'quit' interdit)", couleur=color1, police=game_font, ancrage='center', taille=20, tag='names')
    pseudo1 = enter_surname(1, color1)
    efface('names')
    if pseudo1 == "quit":
        return "quit", "quit"
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du deuxième Joueur, (pseudo 'quit' interdit)", couleur=color2, police=game_font, ancrage='center', taille=20, tag='names')
    pseudo2 = enter_surname(2, color2)
    efface('names')
    return pseudo1, pseudo2


def enter_numbers(color):
    """Renvoie le nombre de tours, type : int.
    Cette fonction demande aux joueurs le nombre de tours, le minimum est 5."""
    numbers = []
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le nombre de tours en chiffre puis appuyez sur Entrée.\n(réfléchissez avant d'entrer, 5 tours minimum par joueur)", ancrage='center', police=game_font, taille=18, tag='tours', couleur=color)
    x, y, e = None, None, None
    while y != 'Return' and y != 'KP_Enter':
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(numbers),couleur=color, ancrage='center', police=game_font, taille=20, tag='liste')
        x, y, e = attente_clic_ou_touche()
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
        efface('liste')
        mise_a_jour()
    if not numbers:
        efface('tours')
        return 5
    else:
        nb_tours = int("".join(numbers))
        if nb_tours < 5:
            nb_tours = 5
    efface('tours')
    return nb_tours
