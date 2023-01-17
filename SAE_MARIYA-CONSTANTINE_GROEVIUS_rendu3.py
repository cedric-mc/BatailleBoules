# Programmeur : Cédric Mariya Constantine et Wilson Groevius
# Imports ---------------------------------------------------------------------
from upemtk import *
from math import sqrt, atan2, cos, sin, dist
from random import randint
from time import time, sleep
import string
import ctypes

# Valeurs initialisées par défaut ---------------------------------------------
largeur_Fenetre, hauteur_Fenetre = ctypes.windll.user32.GetSystemMetrics(0)-10, ctypes.windll.user32.GetSystemMetrics(1)-50 # 1650, 800 # 1850, 1000
print("Largeur de la Fenêtre = ", largeur_Fenetre), print("Hauteur de la Fenêtre = ", hauteur_Fenetre)
caracteres_speciaux = ['ampersand', 'eacute', 'quotedbl', 'apostrophe', 'parenleft', 'minus', 'egrave', 'underscore', 'ccedilla', 'agrave', 'parenright', 'equal']

# Fonctions -------------------------------------------------------------------
def VAINQUEUR(dico_j1, dico_j2, pseudo1, pseudo2):
    """Cette fonction prend en paramètre la largeur et la hauteur de la fenêtre (maximale)
    et les cercles des 2 joueurs pour déterminer en parcourant l'aire de jeu et annoncé le vainqueur.
    dico_j1 et dico_j2 sont des dictionnaires sous la forme (identifiant du cercle: [x, y, r] ;
    x et y représente le centre du cercle)."""
    rectangle(0, hauteur_Fenetre//2-50, largeur_Fenetre, hauteur_Fenetre//2+50, remplissage='white')
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Calcul en cours...", ancrage='center', taille=35, tag='calcul')
    mise_a_jour()
    # Calcul d'aire des cercles, en comptant les pixels. Le calcul est effectué en se basant sur l'aire autour des cercles.
    S1 = {(i, j) for x, y, r in dico_j1.values() for i in range(int(x-r), int(x+r)) for j in range(int(y-r), int(y+r)) if dist((i, j), (x, y)) <= r}
    S2 = {(i, j) for x, y, r in dico_j2.values() for i in range(int(x-r), int(x+r)) for j in range(int(y-r), int(y+r)) if dist((i, j), (x, y)) <= r}
    rouge, bleu = len(S1), len(S2)
    sleep(1)
    mise_a_jour()
    efface('calcul')
    if rouge > bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo1 + " !", ancrage="center", taille=20, couleur='red')
    elif rouge < bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo2 + " !", ancrage="center", taille=20, couleur='blue')
    elif rouge == bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Égalité !", ancrage="center", taille=20)


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
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(lst), couleur=color, ancrage='center', taille=20, tag='pseudo')
        key = attente_touche()
        if key in string.ascii_letters:
            lst.append(key)
        elif key in caracteres_speciaux:
            lst.append(f_caracteres_speciaux(key))
        elif key == '1' or key == 'ampersand' or key == 'KP_1':
            lst.append('1')
        elif key == '2' or key == 'eacute' or key == 'KP_2':
            lst.append('2')
        elif key == '3' or key == 'quotedbl' or key == 'KP_3':
            lst.append('3')
        elif key == '4' or key == 'apostrophe' or key == 'KP_4':
            lst.append('4')
        elif key == '5' or key == 'parenleft' or key == 'KP_5':
            lst.append('5')
        elif key == '6' or key == 'minus' or key == 'KP_6':
            lst.append('6')
        elif key == '7' or key == 'egrave' or key == 'KP_7':
            lst.append('7')
        elif key == '8' or key == 'underscore' or key == 'KP_8':
            lst.append('8')
        elif key == '9' or key == 'ccedilla' or key == 'KP_9':
            lst.append('9')
        elif key == '0' or key == 'agrave' or key == 'KP_0':
            lst.append('0')
        elif key == 'BackSpace' and lst != []:
            lst.pop()
        efface('pseudo')
        mise_a_jour()
    if not(lst):
        pseudo = str("Joueur " + str(joueur))
    else:
        pseudo = "".join(lst)
    return pseudo


def surname():
    """Fait appel à la fonction enter_surname pour entrer les noms des deux joueurs, c'est accompagné d'un texte pour indiqué pour qui doit être entrer le pseudo.
    Elle renvoie les deux pseudos, type : str"""
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du premier Joueur", couleur='red', ancrage='center', taille=20, tag='names')
    pseudo1 = enter_surname(1, "red")
    efface('names')
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le pseudo du deuxième Joueur", couleur='blue', ancrage='center', taille=20, tag='names')
    pseudo2 = enter_surname(2, "blue")
    efface('names')
    return pseudo1, pseudo2


def f_boutons(variante, rec_x1, rec_x2, rec_y1, rec_y2, txt_x, txt_y, txt_in, color1, color2, color3, tag1, tag2):
    """Cette fonction prend en paramètre une variante booléenne correspond à une des six variantes,
    rec_x1 : la coordonnée x du point supérieur gauche (première valeur pour dessiner un rectangle) ; type : int.
    rec_x2 : la coordonnée x du point inférieur droit (quatrième valeur pour dessiner un rectangle) ; type : int.
    rec_y1 : la coordonnée y du point supérieur gauche (deuxième valeur pour dessiner un rectangle) ; type : int.
    rec_y2 : la coordonnée y du point inférieur droit (troisième valeur pour dessiner un rectangle) ; type : int.
    txt_x : position x du texte ; type : int.
    txt_y : position y du texte ; type : int.
    txt_in : chaîne de caractères pour indiquer le texte à l'intérieur du bouton.
    color1, color2, color3 : trois couleurs différentes dont color2 et color3 "black" et "white" ; type : str.
    tag1, tag2 : chaînes de caractères correspondant aux identifiants des composantes du bouton (rectangle + texte).
    Renvoie la variante.
    La fonction permet de changer l'apparence du bouton."""
    if variante:
        variante = False
        efface(tag1), efface(tag2)
        rectangle(rec_x1, rec_y1, rec_x2, rec_y2, couleur=color1, epaisseur=3, tag=tag1)
        texte(txt_x, txt_y, txt_in, couleur=color1, ancrage="center", taille=20, tag=tag2)
    else:
        variante = True
        efface(tag1), efface(tag2)
        rectangle(rec_x1, rec_y1, rec_x2, rec_y2, couleur=color2, remplissage=color1, epaisseur=3, tag=tag1)
        texte(txt_x, txt_y, txt_in, couleur=color3, ancrage="center", taille=20, tag=tag2)
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
        if (largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and hauteur_Fenetre//2-200 < y < hauteur_Fenetre//2-100) or y == "1" or y == 'KP_1' or y == "ampersand":
            V_sablier = f_boutons(V_sablier, largeur_Fenetre//2-700, largeur_Fenetre//2-400, hauteur_Fenetre//2-200, hauteur_Fenetre//2-100, largeur_Fenetre//2-550, hauteur_Fenetre//2-150, "Sablier", "brown", "black", "white", "sablier", "text_sablier")
        elif (largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50) or y == "2" or y == 'KP_2' or y == "eacute":
            V_scores = f_boutons(V_scores, largeur_Fenetre//2-700, largeur_Fenetre//2-400, hauteur_Fenetre//2-50, hauteur_Fenetre//2+50, largeur_Fenetre//2-550, hauteur_Fenetre//2, "Scores", "orange", "white", "black", "scores", "text_scores")
        elif (largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and hauteur_Fenetre//2+100 < y < hauteur_Fenetre//2+200) or y == "3" or y == "KP_3" or y == "quotedbl":
            V_taille = f_boutons(V_taille, largeur_Fenetre//2-700, largeur_Fenetre//2-400, hauteur_Fenetre//2+100, hauteur_Fenetre//2+200, largeur_Fenetre//2-550, hauteur_Fenetre//2+150, "Taille Des Boules", "green", "black", "white", "taille_des_boules", "text_taille_des_boules")
        elif (largeur_Fenetre//2+700 > x > largeur_Fenetre//2+400 and hauteur_Fenetre//2-200 < y < hauteur_Fenetre//2-100) or y == "4" or y == "KP_4" or y == "apostrophe":
            V_dynamique = f_boutons(V_dynamique, largeur_Fenetre//2+700, largeur_Fenetre//2+400, hauteur_Fenetre//2-200, hauteur_Fenetre//2-100, largeur_Fenetre//2+550, hauteur_Fenetre//2-150, "Version Dynamique", "turquoise", "white", "black", "dynamique", "text_dynamique")
        elif (largeur_Fenetre//2+700 > x > largeur_Fenetre//2+400 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50) or y == "5" or y == "KP_5" or y == "parenleft":
            V_terminaison = f_boutons(V_terminaison, largeur_Fenetre//2+700, largeur_Fenetre//2+400, hauteur_Fenetre//2-50, hauteur_Fenetre//2+50, largeur_Fenetre//2+550, hauteur_Fenetre//2, "Terminaison", "purple", "black", "white", "terminaison", "text_terminaison")
        elif (largeur_Fenetre//2+700 > x > largeur_Fenetre//2+400 and hauteur_Fenetre//2+100 < y < hauteur_Fenetre//2+200) or y == "6" or y == "KP_6" or y == "minus":
            V_obstacle = f_boutons(V_obstacle, largeur_Fenetre//2+700, largeur_Fenetre//2+400, hauteur_Fenetre//2+100, hauteur_Fenetre//2+200, largeur_Fenetre//2+550, hauteur_Fenetre//2+150, "Obstacles", "magenta", "white", "black", "obstacles", "text_obstacles")
        elif largeur_Fenetre//2-150 < x < largeur_Fenetre//2+150 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50:
            V_menu = Start_bouton(V_menu)
    return V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle


def MENU():
    """Cette fonction renvoie les variables booléennes des six variantes.
    MENU permet de créer le menu."""
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = True, True, True, True, True, True
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bienvenue !", taille=40, ancrage="center", tag='jouer')
    attente_clic_ou_touche()
    efface('jouer')
    V_sablier = f_boutons(V_sablier, largeur_Fenetre//2-700, largeur_Fenetre//2-400, hauteur_Fenetre//2-200, hauteur_Fenetre//2-100, largeur_Fenetre//2-550, hauteur_Fenetre//2-150, "Sablier", "brown", "black", "white", "sablier", "text_sablier")
    V_scores = f_boutons(V_scores, largeur_Fenetre//2-700, largeur_Fenetre//2-400, hauteur_Fenetre//2-50, hauteur_Fenetre//2+50, largeur_Fenetre//2-550, hauteur_Fenetre//2, "Scores", "orange", "white", "black", "scores", "text_scores")
    V_taille = f_boutons(V_taille, largeur_Fenetre//2-700, largeur_Fenetre//2-400, hauteur_Fenetre//2+100, hauteur_Fenetre//2+200, largeur_Fenetre//2-550, hauteur_Fenetre//2+150, "Taille Des Boules", "green", "black", "white", "taille_des_boules", "text_taille_des_boules")
    V_dynamique = f_boutons(V_dynamique, largeur_Fenetre//2+700, largeur_Fenetre//2+400, hauteur_Fenetre//2-200, hauteur_Fenetre//2-100, largeur_Fenetre//2+550, hauteur_Fenetre//2-150, "Version Dynamique", "turquoise", "white", "black", "dynamique", "text_dynamique")
    V_terminaison = f_boutons(V_terminaison, largeur_Fenetre//2+700, largeur_Fenetre//2+400, hauteur_Fenetre//2-50, hauteur_Fenetre//2+50, largeur_Fenetre//2+550, hauteur_Fenetre//2, "Terminaison", "purple", "black", "white", "terminaison", "text_terminaison")
    V_obstacle = f_boutons(V_obstacle, largeur_Fenetre//2+700, largeur_Fenetre//2+400, hauteur_Fenetre//2+100, hauteur_Fenetre//2+200, largeur_Fenetre//2+550, hauteur_Fenetre//2+150, "Obstacles", "magenta", "white", "black", "obstacles", "text_obstacles")
    rectangle(largeur_Fenetre//2-150, hauteur_Fenetre//2-50, largeur_Fenetre//2+150, hauteur_Fenetre//2+50, couleur='white', remplissage='black', epaisseur=3, tag='play')
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Start", couleur='white', ancrage='center', tag='text_play')
    mise_a_jour()
    # Initialisation des coordonnées de chaque coins des rectangles / boutons en fonction de la largeur et de la hauteur de la fenêtre, la première ligne d'intialisation correspond au quatre point y.
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = boutons(V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle)
    return V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle

# Fonctions des variantes -----------------------------------------------------
def sablier(minuteur, V_scores):
    """Paramètres : 
    - minuteur : temps en secondes (10 secondes ici), type : int ;
    - V_scores : indique si la variante Scores est activée, type : bool.
    Renvoie :
    - Si clic, les coordonnées x et y ainsi que le clic soit Clic Droit ou Gauche ;
    - Si touche, -1, l'identité de la touche et son type soit Touche.
    sablier permet d'afficher et calculer si le bouton est cliqué avant le temps imparti (minuteur)."""
    texte(largeur_Fenetre-500, hauteur_Fenetre-100, "Temps restant : " + str(minuteur) + "s", tag="sablier")
    # t1 correspond au temps actuel du programme (fonction time()) et le temps en secondes du minuteur.
    t1 = time() + minuteur
    while time() < t1:
        efface("sablier")
        ev = donne_evenement()
        type_ev = type_evenement(ev)
        if "Clic" in type_ev:
            return clic_x(ev), clic_y(ev), type_ev
        elif V_scores == True and type_ev == "Touche" and touche(ev) == "s":
            return -1, touche(ev), type_ev
        texte(largeur_Fenetre-500, hauteur_Fenetre-100, "Temps restant : " + str(int(t1 - time() + 1)) + " s", tag="sablier")
        mise_a_jour()
    return None, None, None


def scores(dico_j1, dico_j2):
    """Paramètres : 
    - dico_j1 : dictionnaire du Joueur 1 ;*
    - dico_j2 : dictionnaire du Joueur 2.
    Cette fonction d'utilisée la variante et permettant de calculer le score de chaque joueur et de l'afficher dans le coin supérieur gauche et droit."""
    # Calcul identique de la fonction VAINQUEUR.
    S1 = {(i, j) for x, y, r in dico_j1.values() for i in range(int(x-r), int(x+r)) for j in range(int(y-r), int(y+r)) if dist((i, j), (x, y)) <= r}
    S2 = {(i, j) for x, y, r in dico_j2.values() for i in range(int(x-r), int(x+r)) for j in range(int(y-r), int(y+r)) if dist((i, j), (x, y)) <= r}
    rouge, bleu = len(S1), len(S2)
    r1 = rectangle(0, 0, 300, 100, remplissage='white', epaisseur=3)
    txt1 = texte(150, 50, "Score : " + str(rouge), couleur='red', ancrage="center")
    r2 = rectangle(largeur_Fenetre-300, 0, largeur_Fenetre, 100, remplissage='white', epaisseur=3)
    txt2 = texte(largeur_Fenetre-150, 50, "Score : " + str(bleu), couleur='blue', ancrage="center")
    mise_a_jour()
    sleep(2)
    efface(r1), efface(txt1), efface(r2), efface(txt2)
    mise_a_jour()


def taille_des_boules(banque, color):
    """Paramètres : 
    - banque : type : int, indique le budget restant du joueur ;
    - color : type : str, indiquant la couleur du joueur.
    Renvoie le budget du joueur (modifié) et le rayon du cercle à poser.
    Cette fonction permet de demander au joueur le rayon du cercle du joueur."""
    rectangle(0, hauteur_Fenetre//3-50, largeur_Fenetre, hauteur_Fenetre//3+50, remplissage='white', tag='fond1')
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrer le nombre de pixels pour déterminer le rayon du cercle à poser (rayon par défaut 50) :", taille=20, couleur=color, ancrage='center', tag='demande')
    rectangle(0, hauteur_Fenetre//2-50, largeur_Fenetre, hauteur_Fenetre//2+50, remplissage='white', tag='fond2')
    carte_credit = []
    key = None
    # boucle while basée sur celle de enter_numbers() (identique).
    while key != 'Return' and key != 'KP_Enter':
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(carte_credit), taille=20, couleur=color, ancrage='center', tag='liste')
        key = attente_touche()
        if key == '1' or key == 'ampersand' or key == 'KP_1':
            carte_credit.append('1')
        elif key == '2' or key == 'eacute' or key == 'KP_2':
            carte_credit.append('2')
        elif key == '3' or key == 'quotedbl' or key == 'KP_3':
            carte_credit.append('3')
        elif key == '4' or key == 'apostrophe' or key == 'KP_4':
            carte_credit.append('4')
        elif key == '5' or key == 'parenleft' or key == 'KP_5':
            carte_credit.append('5')
        elif key == '6' or key == 'minus' or key == 'KP_6':
            carte_credit.append('6')
        elif key == '7' or key == 'egrave' or key == 'KP_7':
            carte_credit.append('7')
        elif key == '8' or key == 'underscore' or key == 'KP_8':
            carte_credit.append('8')
        elif key == '9' or key == 'ccedilla' or key == 'KP_9':
            carte_credit.append('9')
        elif key == '0' or key == 'agrave' or key == 'KP_0':
            carte_credit.append('0')
        elif key == 'BackSpace' and carte_credit != []:
            carte_credit.pop()
        efface('liste')
    if not carte_credit:
        rayon = 50
        banque -= 50
    else:
        virement = int("".join(carte_credit))
        rayon = virement
        banque -= virement
    efface('fond1')
    efface('demande')
    efface('fond2')
    return banque, rayon


def version_dynamique(dico1, dico2, dico_obs, color):
    """Paramètres :
    - dico1, dico2 : dictionnaire des joueurs, le premier représente celui dont on vérifie qu'il peut y avoir un agrandissement et le deuxième vérifier la correspondance avec celle du premier.
    - dico_obs : dictionnaire ayant la même fonction que dico2.
    - color : indique la couleur du joueur, type : str.
    Renvoie le nouveau dico1 (new_dico), type : dict.
    Cette fonction permet de "dynamiser" les cercles du joueur en y incrémentant 5 pixels pour son rayon soit rayon + 5."""
    # Vérification d'intersection avec les cercles du joueurs adverse et les obstacles.
    new_dico = dict()
    for id, coordonnees in dico1.items():
        x, y, r = coordonnees[0], coordonnees[1], coordonnees[2]
        if intersection(dico2, x, y, r+5) or intersection(dico_obs, x, y, r+5):
            new_dico[id] = [x, y, r]
        else:
            efface(id)
            c = cercle(x, y, r+5, couleur=color, remplissage=color)
            new_dico[c] = [x, y, r+5]
    return new_dico


def terminaison(V_terminaison, tour, compteur):
    """La fonction prend en paramètres la variable booléenne V_terminaison, le nombre de tour initialisé en début de partie et le compteur du tour actuel.
    La fonction renvoie la variable booléenne V_terminaison et le nombre tour qui peut avoir été modifié.
    La fonction permet d'utiliser la variante Terminaison qui demande aux joueurs une fois par tour et alternativement s'ils veulent terminer dans 5 tours (par rapport au compteur)."""
    # Attente que le joueur appuie sur 'Y' ou sur 'N'.
    if V_terminaison:
        if tour > 5 and compteur < tour-5:
            texte(largeur_Fenetre//2, hauteur_Fenetre//7, "Taper 'Y' pour arrêter la partie dans 5 tours ou 'N' pour continuer.", couleur='black', ancrage='center', tag='terminaison')
            key = attente_touche()
            efface('terminaison')
            if key == 'y':
                tour = compteur + 5
                return False, tour
            elif key == 'n':
                return True, tour
            else:
                return True, tour
        else:
            return V_terminaison, tour
    else:
        return V_terminaison, tour


def obstacles(V_obstacle, dico_obs):
    """La fonction prend en paramètre la variable booléenne V_obstacle et le dictionnaire dico_obs sous forme {identifiant du cercle: [position x du cercle, position y du cercle, rayon du cerlce].
    La fonction renvoie le dictionnaire dico_obs.
    La fonction permet de placer et d'enregistrer les cercles des obstacles, sous forme de cercle de la variante Obstacles."""
    if V_obstacle == True:
        for i in range(randint(1, 15)):
            x = randint(0, largeur_Fenetre)
            y = randint(0, hauteur_Fenetre)
            r = randint(25, 60)
            cercle_obs = cercle(x, y, r, couleur="grey", remplissage="grey")
            dico_obs[cercle_obs] = [x, y, r]
        return dico_obs


# Vérification de la position des cercles ------------------------------------
def intersection(dico, x, y, rayon):
    """Paramètres : 
    - dico : dictionnaire pour vérifier l'intersection entre les coordonnées et les autres cercles ;
    - x, y : coordonnées du cercle ;
    - rayon : type : int, rayon du cercle a posé.
    Fonction de vérification des intersections entre les cercles des adversaires. 
    Calcul utilisé : racine carré de ((Xb-Xa)^2 + (Yb-Ya)^2), peut être remplacer par dist((x1, x2), (y1, y2)).
    Retourne vrai s'il y a une intersection, sinon faux"""
    if dico:
        for x_cercle, y_cercle, rayon_ennemie in dico.values():
            distance = sqrt((x_cercle-x)**2 + (y_cercle-y)**2) # cette formule calcule la disatance entre les deux coordonnées des points
            if distance <= rayon + rayon_ennemie: # Le r*2 correspond au diamètre du cercle
                return True
    return False


def in_cercle(dico, x, y, color):
    """Paramètres : 
    - dico : dictionnaire de cercles ;
    - x, y : coordonnées du clic ;
    - color : couleur du cercle à divisé.
    Renvoie s'il y a eu division de cercle et le dictionnaire avec les deux nouveaux cercles.
    Cette fonction vérifie si le clique est à l'intérieur d'un cercle."""
    # Le clic est-il dans un cercle ?
    for cle, valeur in dico.items():
            distance = sqrt((valeur[0]-x)**2 + (valeur[1]-y)**2)
            if distance <= valeur[2]:
                dico = div_cercle(color, cle, x, y, valeur[0], valeur[1], valeur[2], dico)
                return True, dico
    return False, dico


def div_cercle(color, key, x1, y1, xc, yc, rc, dico):
    """Paramètres : 
    - color : couleur du cercle à diviser, type : str ;
    - key : identifiant du cercle ;
    - x1, y1 : coordonnées du clic.
    - xc, yc, rc : informations relatives au cercle du clic (coordonnées (x, y) et le rayon), type : int ou float ;
    - dico : dictionnaire contenant le cercle.
    Renvoie le dictionnaire avec les deux nouveaux cercles et celui du clic supprimer.
    Cette fonction permet de diviser le cercle du clic en deux, selon l'intersection, le cosinus, le sinus et la tangente."""
    efface(key)       #supprimer le cercle qui va être divisé en deux
    dico.pop(key)
    dx, dy = x1 - xc, y1 - yc  #la distance entre le clic et le centre du cercle
    angle = atan2(dy, dx)  #la tangente entre les distances 
    x2, y2 = x1 - rc * cos(angle), y1 - rc * sin(angle)  # les coordonnées du centre du nouveau cercle
    distance = sqrt(dx**2 + dy**2)  #la distance entre deux cercle
    rp = rc - distance  #rayon du petit cercle
    rg = rc - rp       #rayon du grand cercle
    c1 = cercle(x1, y1, rp, couleur=color, remplissage=color)  # représente le petit cercle
    c2 = cercle(x2, y2, rg, couleur=color, remplissage=color) # le grand cercle
    dico[c1] = [x1, y1, rp]
    dico[c2] = [x2, y2, rg]
    return dico


def enter_numbers():
    """Renvoie le nombre de tours, type : int.
    Cette fonction demande aux joueurs le nombre de tours, le minimum est 5."""
    numbers = []
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrez le nombre de tours en chiffre (réfléchissez avant d'entrer, 5 tours minimum par joueur) puis appuyez sur Entrée", \
        couleur='purple', ancrage='center', police='Z003', taille=20, tag='tours')
    key = None
    while key != 'Return' and key != 'KP_Enter':
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(numbers), couleur='purple', ancrage='center', police='Z003', taille=20, tag='liste')
        key = attente_touche()
        # Seul les nombres peuvent être entrés.
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
        elif key == 'BackSpace' and numbers != []:
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
    texte(largeur_Fenetre//2, 50, txt, color, police='Z003', ancrage='center', taille=20, tag="joueur") # police : donne l'impression d'avoir été écrit par plume
    texte(largeur_Fenetre//2, hauteur_Fenetre-50, txt_tour, color, ancrage='center', police='DejaVu Serif', tag="tour")


def gomme():
    """Cette fonction efface le numéro (nombre) de tour et l'indication pour savoir qui doit jouer."""
    efface("joueur")
    efface("tour")


def J1(x, y, dico_j1, dico_j2, compteur, tour, rayon, banque1, V_terminaison):
    """Paramètres :
    - x, y : position du clic et donc du potentiel futur emplacement d'un cercle ;
    - dico_j1, dico_j2 : dictionnaires des deux joueurs ;
    - compteur : le numéro du tour, type : int ;
    - tour : nombre de tours, type : int ;
    - rayon : rayon du cercle à poser en pixels ;
    - banque1 : budget du joueur pour la variante Taille des Boules, type : int ;
    - V_terminaison : variable booléenne indiquant si la variante Terminaison est activée.
    Renvoie les dictionnaires des deux joueurs, le nombre de tours et le budget du joueur pour la variante Taille des Boules.
    Cette fonction permet de créer le cercle du Joueur 1 ou diviser un cercle adverse."""
    diviser = False
    if dico_j2 != {}:  # Si le joueur 2 a posé un cercle
        diviser, dico_j2 = in_cercle(dico_j2, x, y, 'blue') # Vérification en cas de clic dans un cercle, et division de cercle.
    if diviser == False:
        if type(banque1) == int: # Parti réservé à la variante Taille des Boules.
            banque1, rayon = taille_des_boules(banque1, 'red')
        c = cercle(x, y, rayon, couleur='red', remplissage='red') # insère un cercle d'une certaine couleur dans la fenêtre
        dico_j1[c] = [x, y, rayon]
        if intersection(dico_j2, x, y, rayon) == True:
            efface(c)
            dico_j1.pop(c)
    if compteur % 2 == 0 and V_terminaison:
        V_terminaison, tour = terminaison(V_terminaison, tour, compteur) # Pour la variante Terminaison.
    return dico_j1, dico_j2, tour, banque1


def J2(x, y, dico_j2, dico_j1, compteur, tour, rayon, banque2, V_terminaison):
    """Paramètres :
    - x, y : position du clic et donc du potentiel futur emplacement d'un cercle ;
    - dico_j2, dico_j1 : dictionnaires des deux joueurs ;
    - compteur : le numéro du tour, type : int ;
    - tour : nombre de tours, type : int ;
    - rayon : rayon du cercle à poser en pixels ;
    - banque2 : budget du joueur pour la variante Taille des Boules, type : int ;
    - V_terminaison : variable booléenne indiquant si la variante Terminaison est activée.
    Renvoie les dictionnaires des deux joueurs, le nombre de tours et le budget du joueur pour la variante Taille des Boules.
    Cette fonction permet de créer le cercle du Joueur 2 ou diviser un cercle adverse."""
    diviser = False
    if dico_j1 != {}: # Si le joueur 1 a posé un cercle.
        diviser, dico_j1 = in_cercle(dico_j1, x, y, 'red') # division des cercles si clic dans un cercle.
    if diviser == False:
        if type(banque2) == int: # Pour la variante Taille des Boules
            banque2, rayon = taille_des_boules(banque2, 'blue')
        c = cercle(x, y, rayon, couleur='blue', remplissage='blue')
        dico_j2[c] = [x, y, rayon]
        if intersection(dico_j1, x, y, rayon):
            efface(c)
            dico_j2.pop(c)
    if compteur%2 == 1 and V_terminaison:  # Pour la variante Terminaison.
        V_terminaison, tour = terminaison(V_terminaison, tour, compteur)
    return dico_j2, dico_j1, tour, banque2


def avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, V_sablier, V_scores, banque, V_terminaison, V_obstacle, dico_obs, joueur):
    """Paramètres :
    - dico_j1, dico_j2 : dictionnaires des deux joueurs ;
    - rayon : rayon par défaut de 50 pixels ;
    - compteur : numéro du tour ;
    - tour : nombre de tours ;
    - V_sablier, V_scores, V_terminaison, V_obstacles : variables booléennes indiquant si les variantes Sablier, Scores, Terminaison et Obstacles sont activées ;
    - banque : budget du joueur, type : int ;
    - dico_obs : dictionnaire des obstacles ;
    - joueur : numéro du joueur, type : int.
    Renvoie les dictionnaires des deux joueurs, le nombre de tours et le budget du joueur.
    La fonction vérifie d'abord le temps de réaction si la variante Sablier est activée.
    Si la variante Scores est activée et enfin faire jouer le joueur (poser le cercle)."""
    timing = False
    x, e = None, None
    if V_sablier: # Pour variante Sablier
        x, y, e = sablier(10, V_scores)
        if x == None and y == None == e == None: # Si le temps est écoulé.
            timing = True
        if V_scores and y == 's': # En cas d'utilisation simultanée des variantes Sablier et Scores.
            scores(dico_j1, dico_j2)
    else:
        if V_scores: # Pour la variante Scores.
            e = 'Touche'
            while e == 'Touche': # Affichage du Scores pendant, sans s'arrêter tant que l'interaction n'est pas un clic.
                x, y, e = attente_clic_ou_touche()
                if e == 'Touche' and y == 's':
                    scores(dico_j1, dico_j2)
        else:
            x, y, e = attente_clic() # Lorsqu'aucune variante concernée (Sablier et Scores) n'est activée. 
    if not timing:
        if e == "Touche":
            x, y , e = attente_clic()
        if V_obstacle == True and intersection(dico_obs, x, y, rayon) == True:
            return dico_j1, dico_j2, tour # En cas d'intersection avec les cercles adverses ou les obstacles
        if joueur == 1:
            dico_j1, dico_j2, tour, banque = J1(x, y, dico_j1, dico_j2, compteur, tour, rayon, banque, V_terminaison)
        elif joueur == 2:
            dico_j2, dico_j1, tour, banque = J2(x, y, dico_j2, dico_j1, compteur, tour, rayon, banque, V_terminaison)
    return dico_j1, dico_j2, tour, banque


def GAME(dico_j1, dico_j2, dico_obs, rayon, compteur):
    """Paramètres :
    - dico_j1, dico_j2, dico_obs : dictionnaires des cercles des deux joueurs et les obstacles ;
    - rayon : rayon par défaut des cercles soit 50 pixels ;
    - compteur : numéro du tour, type : int.
    Renvoie les dictionnaires des deux joueurs et les deux pseudos des joueurs (type : str).
    La fonction permet de Jouer."""
    fond = rectangle(0, 0, largeur_Fenetre, hauteur_Fenetre, remplissage="grey75", couleur="black")
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = MENU()
    pseudo1, pseudo2 = surname()
    tour = enter_numbers()
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bonne chance à vous " + pseudo1 + " et " + pseudo2 + " !", ancrage="center", tag='jouer')
    attente_clic_ou_touche()
    efface('jouer')
    efface(fond)
    fond = rectangle(0, 0, largeur_Fenetre, hauteur_Fenetre, couleur="grey75")
    dico_obs = obstacles(V_obstacle, dico_obs)
    banque1, banque2 = None, None
    if V_taille: # Ajout d'argent dans les banques en cas d'activation de la variante Taille des Boules
        banque1, banque2 = 10000, 10000
    while compteur <= tour: # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        crayon('red', compteur, tour, pseudo1)
        dico_j1, dico_j2, tour, banque1 = avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, V_sablier, V_scores, banque1, V_terminaison, V_obstacle, dico_obs, 1)
        gomme()
        crayon('blue', compteur, tour, pseudo2)
        dico_j1, dico_j2, tour, banque2 = avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, V_sablier, V_scores, banque2, V_terminaison, V_obstacle, dico_obs, 2)
        gomme()
        mise_a_jour()
        compteur += 1
        if V_dynamique == True:  # Si la variante Version Dynamique est activée.
            dico_j1 = version_dynamique(dico_j1, dico_j2, dico_obs, 'red')
            dico_j2 = version_dynamique(dico_j2, dico_j1, dico_obs, 'blue')
            mise_a_jour()
    return dico_j1, dico_j2, pseudo1, pseudo2


def INTERFACE():
    """Corps principal du jeu avec création et destruction de l'interface"""
    dico_j1, dico_j2 = dict(), dict() # Forme du dictionnaire : clé : identifiant du cercle ; valeur : [x, y, r].
    dico_obs = dict()
    rayon = 50
    compteur = 1
    coin = (True, False)
    cree_fenetre(largeur_Fenetre, hauteur_Fenetre)
    dico_j1, dico_j2, pseudo1, pseudo2 = GAME(dico_j1, dico_j2, dico_obs, rayon, compteur)
    attente_clic_ou_touche()
    VAINQUEUR(dico_j1, dico_j2, pseudo1, pseudo2) # Détermination du vainqueur.
    attente_clic_ou_touche()
    # time.sleep(3)
    ferme_fenetre()

# Programme principal ----------------------------------------------------------------------
if __name__ == '__main__':
    """Programme principal qui fait appel à la fonction GAME, le corps principal du jeu."""
    INTERFACE()
