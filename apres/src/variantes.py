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
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/BatailleBoules/.

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
        elif V_scores and "Touche" in type_ev and upemtk.touche(ev) is "s":
            return -1, upemtk.touche(ev), type_ev
        upemtk.texte(largeur_Fenetre-500, hauteur_Fenetre-100, "Temps restant : " + str(int(t1 - time() + 1)) + " s", police=game_font, tag="sablier")
        upemtk.mise_a_jour()
    return None, None, None


def scores(dico_j1, dico_j2, color1, color2):
    """Cette fonction représente la variante Scores et permet de calculer le score de chaque joueur et de l'afficher dans le coin supérieur gauche et droit.
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/BatailleBoules/.

    Args:
        dico_j1 (dict): Dictionnaire du Joueur 1.
        dico_j2 (dict): Dictionnaire du Joueur 2.
        color1 (str): Couleur du Joueur 1.
        color2 (str): Couleur du Joueur 2.
    """
    # Calcul des scores des joueurs.
    S1, S2 = calcul_aire(dico_j1, dico_j2)
    j1, j2 = len(S1), len(S2)

    # Position et dimensions de l'affichage des scores.
    zones = [
        (0, 0, 300, 100, 150, 50, f"Score : {j1}", color1), # Joueur 1.
        (largeur_Fenetre - 300, 0, largeur_Fenetre, 100, largeur_Fenetre - 150, 50, f"Score : {j2}", color2) # Joueur 2.
    ]

    elements = [] # Liste des éléments à afficher.
    for x1, y1, x2, y2, tx, ty, text, color in zones:
        r = upemtk.rectangle(x1, y1, x2, y2, remplissage='white', epaisseur=3)
        txt = upemtk.texte(tx, ty, text, couleur=color, police=game_font, ancrage="center")
        elements.append((r, txt))

    upemtk.mise_a_jour() # Mise à jour de l'affichage.
    sleep(2) # Attente de 2 secondes.

    # Effacement des éléments.
    for r, txt in elements:
        upemtk.efface(r), upemtk.efface(txt)
    upemtk.mise_a_jour()


def taille_des_boules(banque, color):
    """Cette fonction représente la variante Taille des Boules et permet de demander au joueur le rayon du cercle à poser.
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/BatailleBoules/.

    Args:
        banque (int): Budget restant du joueur.
        color (str): Couleur du joueur.

    Returns:
          banque (int): Budget du joueur (modifié).
          rayon (int): Rayon du cercle à poser.
    """
    # Affichage des instructions et de la demande de la taille du cercle.
    upemtk.rectangle(0, hauteur_Fenetre // 3 - 50, largeur_Fenetre, hauteur_Fenetre // 3 + 50, remplissage='white', tag='fond1')
    upemtk.texte(largeur_Fenetre // 2, hauteur_Fenetre // 3, "Entrer le nombre de pixels pour déterminer \nle rayon du cercle à poser (rayon par défaut 50) :", taille=20, couleur=color, police=game_font, ancrage='center', tag='demande')
    upemtk.rectangle(0, hauteur_Fenetre // 2 - 50, largeur_Fenetre, hauteur_Fenetre // 2 + 50, remplissage='white', tag='fond2')

    # Initialisation de la liste des chiffres entrés par le joueur.
    carte_credit = []
    key = None
    touche_to_chiffre = {
        '1': '1', 'ampersand': '1', 'KP_1': '1',
        '2': '2', 'eacute': '2', 'KP_2': '2',
        '3': '3', 'quotedbl': '3', 'KP_3': '3',
        '4': '4', 'apostrophe': '4', 'KP_4': '4',
        '5': '5', 'parenleft': '5', 'KP_5': '5',
        '6': '6', 'minus': '6', 'KP_6': '6',
        '7': '7', 'egrave': '7', 'KP_7': '7',
        '8': '8', 'underscore': '8', 'KP_8': '8',
        '9': '9', 'ccedilla': '9', 'KP_9': '9',
        '0': '0', 'agrave': '0', 'KP_0': '0'
    }

    # Récupération de l'entrée du joueur
    while key not in {'Return', 'KP_Enter'}:
        # Affichage de la liste des chiffres entrés par le joueur.
        upemtk.texte(largeur_Fenetre // 2, hauteur_Fenetre // 2, "".join(carte_credit), taille=20, couleur=color, police=game_font, ancrage='center', tag='liste')
        key = upemtk.attente_touche()

        # Ajout du chiffre à la liste si la touche est un chiffre.
        if key in touche_to_chiffre:
            carte_credit.append(touche_to_chiffre[key])
        # Suppression du dernier chiffre si la touche est 'BackSpace'.
        elif key == 'BackSpace' and carte_credit != []:
            carte_credit.pop()

        # Mettre à jour l'affichage de la liste des chiffres.
        upemtk.efface('liste')

    # Validation et calcul du rayon.
    if not carte_credit:
        rayon = 50
    else:
        rayon = int("".join(carte_credit))

    if rayon > banque:
        rayon = banque # Si le joueur n'a pas assez d'argent, le rayon est égal à la banque.
    banque -= rayon # Déduction du budget du joueur.

    # Effacement des éléments.
    upemtk.efface('fond1')
    upemtk.efface('demande')
    upemtk.efface('fond2')

    return banque, rayon


def version_dynamique(dico1, dico2, dico_obs, color):
    """Cette fonction représente la variante Dynamique et permet d'agrandir les cercles des joueurs et de vérifier les intersections avec les obstacles et les cercles adverses.
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/BatailleBoules/.

    Args:
        dico1 (dict): Dictionnaire du Joueur 1.
        dico2 (dict): Dictionnaire du Joueur 2.
        dico_obs (dict): Dictionnaire des obstacles.
        color (str): Couleur du joueur.

    Returns:
        new_dico (dict): Dictionnaire des cercles du joueur 1 (modifié).
    """
    # Vérification d'intersection avec les cercles du joueurs adverse et les obstacles.
    new_dico = {}

    for circle_id, (x, y, r) in dico1.items():
        new_radius = r + 5

        # Vérification des intersections avec les obstacles et les cercles adverses.
        if any(intersection(d, x, y, new_radius) for d in (dico2, dico_obs)):
            new_dico[circle_id] = [x, y, r] # Pas de changement si une intersection est détectée.
        else:
            # Suppression et recréation du cercle avec le nouveau rayon.
            upemtk.efface(circle_id)
            new_id = upemtk.cercle(x, y, new_radius, couleur=color, remplissage=color)
            new_dico[new_id] = [x, y, new_radius]

    return new_dico


def terminaison(V_terminaison, tour, compteur):
    """Cette fonction représente la variante Terminaison et permet de demander aux joueurs s'ils veulent terminer la partie dans 5 tours.
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/BatailleBoules/.

    Args:
        V_terminaison (bool): Variable booléenne de la variante.
        tour (int): Nombre de tours.
        compteur (int): Compteur de tours.

    Returns:
        V_terminaison (bool): Variable booléenne de la variante (modifiée).
        tour (int): Nombre de tours (modifié).
    """
    # Vérifie si la variante Terminaison est active
    if V_terminaison and tour > 5 and compteur < tour - 5:
        # Affichage du choix
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//7, "Taper 'Y' pour arrêter la partie dans 5 tours ou 'N' pour continuer.", couleur='black', police=game_font, ancrage='center', tag='terminaison')
        key = upemtk.attente_touche()

        # Attente de la réponse du joueur
        key = upemtk.attente_touche()
        upemtk.efface('terminaison')

        if key == 'y': # Si le joueur choisit d'arrêter dans 5 tours
            return False, compteur + 5
        elif key == 'n': # Si le joueur choisit de continuer
            return True, tour
    return V_terminaison, tour # Aucun changement, on retourne donc les valeurs initiales


def obstacles(V_obstacle, dico_obs):
    """Cette fonction prend en paramètre la variable booléenne V_obstacle et le dictionnaire dico_obs sous forme
    {identifiant du cercle: [position x du cercle, position y du cercle, rayon du cercle].
    La description de la variante est disponible dans le README.md ou au lien suivant : https://cedric-mc.github.io/BatailleBoules/.

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
