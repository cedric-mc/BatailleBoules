# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
from time import time, sleep
from random import randint
from default import *
from calcul import *
import upemtk


def sablier(minuteur, V_scores):
    """Cette fonction représente la variante du Sablier et permet d'afficher et calculer si le bouton est cliqué avant le temps imparti (minuteur).
    Cette fonction est une reprise de la fonction de la attente_touche_jusqua() de upemtk.
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/Python_Game/.

    Args:
        minuteur (int): Temps en secondes (10 secondes ici).
        V_scores (bool): Indique si la variante Scores est activée.

    Returns:
        tuple: Si clic, les coordonnées x et y ainsi que le clic soit Clic Droit ou Gauche. Si touche, -1, l'identité de la touche et son type soit Touche.
    """
    upemtk.texte(largeur_Fenetre-500, hauteur_Fenetre-100, "Temps restant : " + str(minuteur) + "s", police=game_font, tag="sablier")
    # t1 correspond au temps actuel du programme (fonction time()) et le temps en secondes du minuteur.
    t1 = time() + minuteur
    while time() < t1:
        upemtk.efface("sablier")
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if "Clic" in type_ev:
            return upemtk.clic_x(ev), upemtk.clic_y(ev), type_ev
        elif V_scores == True and type_ev == "Touche" and upemtk.touche(ev) == "s":
            return -1, upemtk.touche(ev), type_ev
        upemtk.texte(largeur_Fenetre-500, hauteur_Fenetre-100, "Temps restant : " + str(int(t1 - time() + 1)) + " s", police=game_font, tag="sablier")
        upemtk.mise_a_jour()
    return None, None, None


def scores(dico_j1, dico_j2, color1, color2):
    """Cette fonction représente la variante Scores et permet de calculer le score de chaque joueur et de l'afficher
    dans le coin supérieur gauche et droit. La description de la variante est disponible dans le README.md ou au lien
    suivant : https://cedric-mc.github.io/Python_Game/.

    Args:
        dico_j1 (dict): Dictionnaire du Joueur 1.
        dico_j2 (dict): Dictionnaire du Joueur 2.
        color1 (str): Couleur du Joueur 1.
        color2 (str): Couleur du Joueur 2.
    """
    # Calcul identique de la fonction VAINQUEUR.
    S1, S2 = calcul_aire(dico_j1, dico_j2)
    j1, j2 = len(S1), len(S2)
    r1 = upemtk.rectangle(0, 0, 300, 100, remplissage='white', epaisseur=3)
    txt1 = upemtk.texte(150, 50, "Score : " + str(j1), couleur=color1, police=game_font, ancrage="center")
    r2 = upemtk.rectangle(largeur_Fenetre-300, 0, largeur_Fenetre, 100, remplissage='white', epaisseur=3)
    txt2 = upemtk.texte(largeur_Fenetre-150, 50, "Score : " + str(j2), couleur=color2, police=game_font, ancrage="center")
    upemtk.mise_a_jour()
    sleep(2)
    upemtk.efface(r1), upemtk.efface(txt1), upemtk.efface(r2), upemtk.efface(txt2)
    upemtk.mise_a_jour()


def taille_des_boules(banque, color):
    """Cette fonction représente la variante Taille des Boules et permet de demander au joueur le rayon du cercle à poser.
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/Python_Game/.

    Args:
        banque (int): Budget restant du joueur.
        color (str): Couleur du joueur.

    Returns:
          banque (int): Budget du joueur (modifié).
          rayon (int): Rayon du cercle à poser.
    """
    upemtk.rectangle(0, hauteur_Fenetre//3-50, largeur_Fenetre, hauteur_Fenetre//3+50, remplissage='white', tag='fond1')
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//3, "Entrer le nombre de pixels pour déterminer \nle rayon du cercle à poser (rayon par défaut 50) :", taille=20, couleur=color, police=game_font, ancrage='center', tag='demande')
    upemtk.rectangle(0, hauteur_Fenetre//2-50, largeur_Fenetre, hauteur_Fenetre//2+50, remplissage='white', tag='fond2')
    carte_credit = []
    key = None
    # boucle while basée sur celle de enter_numbers() (identique).
    while key != 'Return' and key != 'KP_Enter':
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "".join(carte_credit), taille=20, couleur=color, police=game_font, ancrage='center', tag='liste')
        key = upemtk.attente_touche()
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
        upemtk.efface('liste')
    if not carte_credit:
        rayon = 50
        banque -= 50
    else:
        virement = int("".join(carte_credit))
        rayon = virement
        banque -= virement
    upemtk.efface('fond1')
    upemtk.efface('demande')
    upemtk.efface('fond2')
    return banque, rayon


def version_dynamique(dico1, dico2, dico_obs, color):
    """Cette fonction représente la variante Dynamique et permet d'agrandir les cercles des joueurs et de vérifier les intersections avec les obstacles et les cercles adverses.
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/Python_Game/.

    Args:
        dico1 (dict): Dictionnaire du Joueur 1.
        dico2 (dict): Dictionnaire du Joueur 2.
        dico_obs (dict): Dictionnaire des obstacles.
        color (str): Couleur du joueur.

    Returns:
        new_dico (dict): Dictionnaire des cercles du joueur 1 (modifié).
    """
    # Vérification d'intersection avec les cercles du joueurs adverse et les obstacles.
    new_dico = dict()
    for id, coordonnees in dico1.items():
        x, y, r = coordonnees[0], coordonnees[1], coordonnees[2]
        if intersection(dico2, x, y, r+5) or intersection(dico_obs, x, y, r+5):
            new_dico[id] = [x, y, r]
        else:
            upemtk.efface(id)
            c = upemtk.cercle(x, y, r+5, couleur=color, remplissage=color)
            new_dico[c] = [x, y, r+5]
    return new_dico


def terminaison(V_terminaison, tour, compteur):
    """Cette fonction représente la variante Terminaison et permet de demander aux joueurs s'ils veulent terminer la partie dans 5 tours.

    Args:
        V_terminaison (bool): Variable booléenne de la variante.
        tour (int): Nombre de tours.
        compteur (int): Compteur de tours.

    Returns:
        V_terminaison (bool): Variable booléenne de la variante (modifiée).
        tour (int): Nombre de tours (modifié).
    """
    # Attente que le joueur appuie sur 'Y' ou sur 'N'.
    if V_terminaison:
        if tour > 5 and compteur < tour-5:
            upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//7, "Taper 'Y' pour arrêter la partie dans 5 tours ou 'N' pour continuer.", couleur='black', police=game_font, ancrage='center', tag='terminaison')
            key = upemtk.attente_touche()
            upemtk.efface('terminaison')
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
    """Cette fonction prend en paramètre la variable booléenne V_obstacle et le dictionnaire dico_obs sous forme {identifiant du cercle: [position x du cercle, position y du cercle, rayon du cercle].

    Args:
        V_obstacle (bool): Variable booléenne de la variante.
        dico_obs (dict): Dictionnaire des obstacles.

    Returns:
        dico_obs (dict): Dictionnaire des obstacles (modifié).
    """
    if V_obstacle:
        for i in range(randint(1, 15)):
            x = randint(0, largeur_Fenetre)
            y = randint(0, hauteur_Fenetre)
            r = randint(25, 60)
            cercle_obs = upemtk.cercle(x, y, r, couleur="grey", remplissage="grey")
            dico_obs[cercle_obs] = [x, y, r]
        return dico_obs
