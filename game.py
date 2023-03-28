# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from variantes import *
from calcul import *
from joueur import *
from default import *
from menu import MENU, choose_colors
from colors import colors, melangeur_colors
from texte import *


def avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, V_sablier, V_scores, banque, V_terminaison, V_obstacle, dico_obs, joueur, color1, color2):
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
    if V_sablier:
        x, y, e = sablier(10, V_scores)
        if x == None and y == None == e == None:
            timing = True
        if V_scores and y == 's':
            scores(dico_j1, dico_j2)
    else:
        if V_scores:
            e = 'Touche'
            while e == 'Touche':
                x, y, e = attente_clic_ou_touche()
                if e == 'Touche' and y == 's':
                    scores(dico_j1, dico_j2)
        else:
            x, y, e = attente_clic()
    if not timing:
        if e == "Touche":
            x, y , e = attente_clic()
        if V_obstacle == True and intersection(dico_obs, x, y, rayon) == True:
            return dico_j1, dico_j2, tour, banque
        if joueur == 1:
            dico_j1, dico_j2, tour, banque = J1(x, y, dico_j1, dico_j2, compteur, tour, rayon, banque, V_terminaison, color1, color2)
        elif joueur == 2:
            dico_j2, dico_j1, tour, banque = J2(x, y, dico_j2, dico_j1, compteur, tour, rayon, banque, V_terminaison, color1, color2)
    return dico_j1, dico_j2, tour, banque


def GAME(dico_j1, dico_j2, dico_obs, rayon, compteur):
    """Paramètres :
    - dico_j1, dico_j2, dico_obs : dictionnaires des cercles des deux joueurs et les obstacles ;
    - rayon : rayon par défaut des cercles soit 50 pixels ;
    - compteur : numéro du tour, type : int.
    Renvoie les dictionnaires des deux joueurs et les deux pseudos des joueurs (type : str).
    La fonction permet de Jouer."""
    fond = rectangle(0, 0, largeur_Fenetre, hauteur_Fenetre, remplissage="white", couleur="black")
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = MENU()
    color1, color2 = colors()
    pseudo1, pseudo2 = surname(color1, color2)
    tour = enter_numbers(melangeur_colors(color1, color2))
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bonne chance à vous " + pseudo1 + " et " + pseudo2 + " !", police="Monocraft", ancrage="center", tag='jouer')
    attente_clic_ou_touche()
    efface('jouer')
    efface(fond)
    fond = rectangle(0, 0, largeur_Fenetre, hauteur_Fenetre, couleur="grey75")
    dico_obs = obstacles(V_obstacle, dico_obs)
    banque1, banque2 = None, None
    if V_taille:
        banque1, banque2 = 10000, 10000
    while compteur <= tour: # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        crayon(color1, compteur, tour, pseudo1)
        dico_j1, dico_j2, tour, banque1 = avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, V_sablier, V_scores, banque1, V_terminaison, V_obstacle, dico_obs, 1, color1, color2)
        gomme()
        crayon(color2, compteur, tour, pseudo2)
        dico_j1, dico_j2, tour, banque2 = avant_jeu(dico_j1, dico_j2, rayon, compteur, tour, V_sablier, V_scores, banque2, V_terminaison, V_obstacle, dico_obs, 2, color1, color2)
        gomme()
        mise_a_jour()
        compteur += 1
        if V_dynamique == True:
            dico_j1 = version_dynamique(dico_j1, dico_j2, dico_obs, color1)
            dico_j2 = version_dynamique(dico_j2, dico_j1, dico_obs, color2)
            mise_a_jour()
    return dico_j1, dico_j2, pseudo1, pseudo2, color1, color2