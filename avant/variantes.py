# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis la bibliothèque Python
from time import time, sleep
from random import randint


# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *
from calcul import *


def sablier(minuteur, V_scores):
    """Paramètres : 
    - minuteur : temps en secondes (10 secondes ici), type : int ;
    - V_scores : indique si la variante Scores est activée, type : bool.
    Renvoie :
    - Si clic, les coordonnées x et y ainsi que le clic soit Clic Droit ou Gauche ;
    - Si touche, -1, l'identité de la touche et son type soit Touche.
    sablier permet d'afficher et calculer si le bouton est cliqué avant le temps imparti (minuteur)."""
    texte(largeur_Fenetre-500, hauteur_Fenetre-100, "Temps restant : " + str(minuteur) + "s", police=game_font, tag="sablier")
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
        texte(largeur_Fenetre-500, hauteur_Fenetre-100, "Temps restant : " + str(int(t1 - time() + 1)) + " s", police=game_font, tag="sablier")
        mise_a_jour()
    return None, None, None


def scores(dico_j1, dico_j2, color1, color2):
    """Paramètres : 
    - dico_j1 : dictionnaire du Joueur 1 ;*
    - dico_j2 : dictionnaire du Joueur 2.
    Cette fonction d'utilisée la variante et permettant de calculer le score de chaque joueur et de l'afficher dans le coin supérieur gauche et droit."""
    # Calcul identique de la fonction VAINQUEUR.
    S1, S2 = calcul_aire(dico_j1, dico_j2)
    j1, j2 = len(S1), len(S2)
    r1 = rectangle(0, 0, 300, 100, remplissage='white', epaisseur=3)
    txt1 = texte(150, 50, "Score : " + str(j1), couleur=color1, police=game_font, ancrage="center")
    r2 = rectangle(largeur_Fenetre-300, 0, largeur_Fenetre, 100, remplissage='white', epaisseur=3)
    txt2 = texte(largeur_Fenetre-150, 50, "Score : " + str(j2), couleur=color2, police=game_font, ancrage="center")
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
    texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrer le nombre de pixels pour déterminer \nle rayon du cercle à poser (rayon par défaut 50) :", taille=20, couleur=color, police=game_font, ancrage='center', tag='demande')
    rectangle(0, hauteur_Fenetre//2-50, largeur_Fenetre, hauteur_Fenetre//2+50, remplissage='white', tag='fond2')
    carte_credit = []
    key = None
    # boucle while basée sur celle de enter_numbers() (identique).
    while key != 'Return' and key != 'KP_Enter':
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(carte_credit), taille=20, couleur=color, police=game_font, ancrage='center', tag='liste')
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
            texte(largeur_Fenetre//2, hauteur_Fenetre//7, "Taper 'Y' pour arrêter la partie dans 5 tours ou 'N' pour continuer.", couleur='black', police=game_font, ancrage='center', tag='terminaison')
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