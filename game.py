# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from variantes import *
from calcul import *
from joueur import *
from default import *
from menu import MENU
from colors import colors, melangeur_colors
from texte import *
from interface import *
from restart import RESTART


def VAINQUEUR(dico_j1, dico_j2, pseudo1, pseudo2, color1, color2):
    """Cette fonction permet de déterminer et d'annoncer le vainqueur de la partie.

    Args:
        dico_j1 (dict): Dictionnaire du Joueur 1 (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_j2 (dict): Dictionnaire du Joueur 2 (clé : identifiant du cercle ; valeur : [x, y, r]).
        pseudo1 (str): Pseudo du Joueur 1.
        pseudo2 (str): Pseudo du Joueur 2.
        color1 (str): Couleur du Joueur 1.
        color2 (str): Couleur du Joueur 2.

    Returns:
        None: Rien n'est retourné.
    """
    rectangle(0, hauteur_Fenetre//2-50, largeur_Fenetre, hauteur_Fenetre//2+50, remplissage='white')
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Calcul en cours...", ancrage='center', police=game_font, taille=35, tag='calcul')
    mise_a_jour()
    # Calcul d'aire des cercles, en comptant les pixels. Le calcul est effectué en se basant sur l'aire autour des cercles.
    S1, S2 = calcul_aire(dico_j1, dico_j2)
    rouge, bleu = len(S1), len(S2)
    sleep(0.5)
    mise_a_jour()
    efface('calcul')
    if rouge == 0 and bleu == 0:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Vous êtes pas doué pour jouer !", ancrage='center', taille=25, police=game_font)
    elif rouge > bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo1 + " !", ancrage="center", police=game_font, taille=25, couleur=color1)
    elif rouge < bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo2 + " !", ancrage="center", police=game_font, taille=25, couleur=color2)
    elif rouge == bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Égalité !", ancrage="center", police=game_font, taille=25, couleur=melangeur_colors(color1, color2))
    mise_a_jour()


def avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, variantes, banque, dico_obs, joueur, color1, color2):
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
    if variantes["sablier"]:
        x, y, e = sablier(10, variantes["scores"])
        if x == None and y == None == e == None:
            timing = True
        if variantes["scores"] and y == 's':
            scores(dico_j1, dico_j2, color1, color2)
    else:
        if variantes["scores"]:
            e = 'Touche'
            while e == 'Touche':
                x, y, e = attente_clic_ou_touche()
                if e == 'Touche' and y == 's':
                    scores(dico_j1, dico_j2, color1, color2)
        else:
            x, y, e = attente_clic()
    if not timing:
        if e == "Touche":
            x, y , e = attente_clic()
        if variantes["obstacle"] == True and intersection(dico_obs, x, y, rayon) == True:
            return dico_j1, dico_j2, tour, banque
        dico_j1, dico_j2, tour, banque = JOUEUR(x, y, dico_j1, dico_j2, compteur, tour, rayon, banque, variantes["terminaison"], color1, color2, joueur)
    return dico_j1, dico_j2, tour, banque


def JOUEUR(x, y, dico_j1, dico_j2, compteur, tour, rayon, banque, V_terminaison, color1, color2, joueur):
    if joueur == 1:
            dico_j1, dico_j2, tour, banque = J1(x, y, dico_j1, dico_j2, compteur, tour, rayon, banque, V_terminaison, color1, color2)
    elif joueur == 2:
        dico_j2, dico_j1, tour, banque = J2(x, y, dico_j2, dico_j1, compteur, tour, rayon, banque, V_terminaison, color1, color2)
    return dico_j1, dico_j2, tour, banque


def GAME():
    """Paramètres :
    - dico_j1, dico_j2, dico_obs : dictionnaires des cercles des deux joueurs et les obstacles ;
    - rayon : rayon par défaut des cercles soit 50 pixels ;
    - compteur : numéro du tour, type : int.
    Renvoie les dictionnaires des deux joueurs et les deux pseudos des joueurs (type : str).
    La fonction permet de Jouer."""
    dico_j1, dico_j2 = dict(), dict() # Forme du dictionnaire : clé : identifiant du cercle ; valeur : [x, y, r].
    dico_obs = dict()
    rayon = 50
    compteur = 1
    variantes, V_menu = MENU()
    if not V_menu:
        return
    color1, color2 = colors()
    if color1 == "quit" or color2 == "quit":
        return
    pseudo1, pseudo2 = surname(color1, color2)
    if pseudo1 == "quit" or pseudo2 == "quit":
        return
    tour = enter_numbers(melangeur_colors(color1, color2))
    if tour == "quit":
        return
    efface("quit"), efface("croix1"), efface("croix2")
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bonne chance à vous " + pseudo1 + " et " + pseudo2 + " !", couleur=melangeur_colors(color1, color2), police=game_font, ancrage="center", tag='jouer')
    attente_clic_ou_touche()
    efface('jouer')
    dico_obs = obstacles(variantes["obstacle"], dico_obs)
    banque1, banque2 = None, None
    # create_Interface(variantes)
    if variantes["taille"]:
        banque1, banque2 = 10000, 10000
    while compteur <= tour: # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        crayon(color1, compteur, tour, pseudo1)
        dico_j1, dico_j2, tour, banque1 = avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, variantes, banque1, dico_obs, 1, color1, color2)
        gomme()
        crayon(color2, compteur, tour, pseudo2)
        dico_j1, dico_j2, tour, banque2 = avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, variantes, banque2, dico_obs, 2, color1, color2)
        gomme()
        variantes["terminaison"], tour = terminaison(variantes["terminaison"], tour, compteur)
        mise_a_jour()
        compteur += 1
        if variantes["dynamique"]:
            dico_j1 = version_dynamique(dico_j1, dico_j2, dico_obs, color1)
            dico_j2 = version_dynamique(dico_j2, dico_j1, dico_obs, color2)
            mise_a_jour()
    attente_clic_ou_touche()
    VAINQUEUR(dico_j1, dico_j2, pseudo1, pseudo2, color1, color2)
    attente_clic_ou_touche()
    isRestart = RESTART()
    if isRestart:
        GAME()
    return