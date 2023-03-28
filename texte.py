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
    key = None
    while key != 'Return' and key != 'KP_Enter':
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(lst), couleur=color, police="Monocraft", ancrage='center', taille=20, tag='pseudo')
        key = attente_touche()
        if key in ascii_letters:
            lst.append(key)
        elif key in caracteres_speciaux:
            lst.append(f_caracteres_speciaux(key))
        elif key == '1' or key == 'KP_1':
            lst.append('1')
        elif key == '2' or key == 'KP_2':
            lst.append('2')
        elif key == '3' or key == 'KP_3':
            lst.append('3')
        elif key == '4' or key == 'KP_4':
            lst.append('4')
        elif key == '5' or key == 'KP_5':
            lst.append('5')
        elif key == '6' or key == 'KP_6':
            lst.append('6')
        elif key == '7' or key == 'KP_7':
            lst.append('7')
        elif key == '8' or key == 'KP_8':
            lst.append('8')
        elif key == '9' or key == 'KP_9':
            lst.append('9')
        elif key == '0' or key == 'KP_0':
            lst.append('0')
        elif (key == 'BackSpace' or key == 'Delete') and lst != []:
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
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du premier Joueur", couleur=color1, police="Monocraft", ancrage='center', taille=20, tag='names')
    pseudo1 = enter_surname(1, color1)
    efface('names')
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du deuxième Joueur", couleur=color2, police="Monocraft", ancrage='center', taille=20, tag='names')
    pseudo2 = enter_surname(2, color2)
    efface('names')
    return pseudo1, pseudo2


def enter_numbers(color):
    """Renvoie le nombre de tours, type : int.
    Cette fonction demande aux joueurs le nombre de tours, le minimum est 5."""
    numbers = []
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le nombre de tours en chiffre puis appuyez sur Entrée.\n(réfléchissez avant d'entrer, 5 tours minimum par joueur)", ancrage='center', police="Monocraft", taille=18, tag='tours', couleur=color)
    key = None
    while key != 'Return' and key != 'KP_Enter':
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(numbers), ancrage='center', police="Monocraft", taille=20, tag='liste')
        key = attente_touche()
        if key == '1' or key == 'ampersand' or key == 'KP_1':
            numbers.append('1')
        elif key == '2' or key == 'eacute' or key == 'KP_2':
            numbers.append('2')
        elif key == '3' or key == 'quotedbl' or key == 'KP_3':
            numbers.append('3')
        elif key == '4' or key == 'apostrophe' or key == 'KP_4':
            numbers.append('4')
        elif key == '5' or key == 'parenleft' or key == 'KP_5':
            numbers.append('5')
        elif key == '6' or key == 'minus' or key == 'KP_6':
            numbers.append('6')
        elif key == '7' or key == 'egrave' or key == 'KP_7':
            numbers.append('7')
        elif key == '8' or key == 'underscore' or key == 'KP_8':
            numbers.append('8')
        elif key == '9' or key == 'ccedilla' or key == 'KP_9':
            numbers.append('9')
        elif key == '0' or key == 'agrave' or key == 'KP_0':
            numbers.append('0')
        elif (key == 'BackSpace' or key == 'Delete') and numbers != []:
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


def crayon(color, compteur, tour, pseudo):
    """Paramètres :
    - color : couleur du joueur, type : str ;
    - compteur : le nombre de tour(s) écoulé, type : int ;
    - tour : le nombre de tours pour la partie, type : int ;
    - pseudo : le pseudo / surnom du joueur, type : str.
    Cette fonction permet d'afficher le numéro (nombre) du tour et indique qui doit jouer."""
    txt = "Tour de " + pseudo
    txt_tour = 'Tour : ' + str(compteur) + '/' + str(tour)
    texte(largeur_Fenetre//2, 50, txt, color, police="Monocraft", ancrage='center', taille=20, tag="joueur") # police : donne l'impression d'avoir été écrit par plume
    texte(largeur_Fenetre//2, hauteur_Fenetre-50, txt_tour, color, ancrage='center', police="Monocraft", tag="tour")


def gomme():
    """Cette fonction efface le numéro (nombre) de tour et l'indication pour savoir qui doit jouer."""
    efface("joueur")
    efface("tour")