# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
from boutons import clear_quit_button
from couleurs import colors, melangeur_colors
from menu import menu
from restart import restart
from texte import *
from calcul import calcul_aire, in_cercle, intersection
from variantes import sablier, scores, terminaison, obstacles, taille_des_boules, version_dynamique
from time import sleep


def crayon(color, compteur, tour, pseudo):
    """Cette fonction permet d'afficher le numéro du tour et l'indication pour savoir qui doit jouer.

    Args:
        color (_type_): Couleur du texte.
        compteur (int): Compteur du tour.
        tour (int): Nombre de tours.
        pseudo (str): Pseudo du joueur.
    """
    txt = f"Tour de {pseudo}"
    txt_tour = f"Tour : {compteur}/{tour}"
    upemtk.texte(largeur_Fenetre // 2, hauteur_Fenetre // 18, txt, color, police=game_font, ancrage='center', taille=20, tag="joueur")
    upemtk.texte(largeur_Fenetre // 2, hauteur_Fenetre - hauteur_Fenetre // 18, txt_tour, color, police=game_font, ancrage='center', taille=20, tag="tour")


def gomme():
    """Cette fonction efface le numéro (nombre) de tour et l'indication pour savoir qui doit jouer."""
    upemtk.efface("joueur"), upemtk.efface("tour")


def vainqueur(dico_j1, dico_j2, pseudo1, pseudo2, lst_colors):
    """
    Détermine et affiche le vainqueur de la partie en fonction des aires occupées par chaque joueur.

    Args:
        dico_j1 (dict): Dictionnaire du Joueur 1 (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_j2 (dict): Dictionnaire du Joueur 2 (clé : identifiant du cercle ; valeur : [x, y, r]).
        pseudo1 (str): Pseudo du Joueur 1.
        pseudo2 (str): Pseudo du Joueur 2.
        lst_colors (list): Liste des couleurs des joueurs ([couleur Joueur 1, couleur Joueur 2]).
    """
    # Affiche une fenêtre de calcul en cours
    upemtk.rectangle(0, hauteur_Fenetre//2 - 50, largeur_Fenetre, hauteur_Fenetre//2 + 50, remplissage='white')
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Calcul en cours...", ancrage='center', police=game_font, taille=35, tag='calcul')
    upemtk.mise_a_jour()

    # Calcul des aires des cercles
    aire_j1, aire_j2 = calcul_aire(dico_j1, dico_j2)
    total_aire = aire_j1 + aire_j2

    # Efface le message de calcul
    upemtk.efface('calcul')
    # Gestion des cas particuliers (aucune aire occupée)
    if total_aire == 0:
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Personne n'a joué... Essayez encore !", ancrage='center', taille=25, police=game_font)
        upemtk.mise_a_jour()
        return

    # Calcul des pourcentages
    pourcentage_j1 = (aire_j1 / total_aire) * 100
    pourcentage_j2 = (aire_j2 / total_aire) * 100

    # Détermine le résultat et affiche le message approprié
    if pourcentage_j1 > pourcentage_j2:
        message = f"Félicitations ! {pseudo1} a gagné avec {pourcentage_j1:.2f}% !"
        couleur = lst_colors[0]
    elif pourcentage_j1 < pourcentage_j2:
        message = f"Félicitations ! {pseudo2} a gagné avec {pourcentage_j2:.2f}% !"
        couleur = lst_colors[1]
    else:
        message = "C'est une égalité parfaite !"
        couleur = melangeur_colors(lst_colors[0], lst_colors[1])  # Mélange des couleurs des deux joueurs

    # Affiche le résultat final
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, message, ancrage="center", police=game_font, taille=25, couleur=couleur)
    upemtk.mise_a_jour()


def joueur(x, y, dico_actif, dico_adverse, rayon, banque, color_actif, color_adverse, number):
    """Cette fonction permet de gérer les actions du joueur actif après un clic.

    Args:
        x (int): Coordonnée x du clic.
        y (int): Coordonnée y du clic.
        dico_actif (dict): Dictionnaire du Joueur actif (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_adverse (dict): Dictionnaire du Joueur adverse (clé : identifiant du cercle ; valeur : [x, y, r]).
        rayon (int): Rayon par défaut des cercles.
        banque (int): Budget du joueur.
        color_actif (str): Couleur du Joueur actif.
        color_adverse (str): Couleur du Joueur adverse.
        number (int): Numéro du joueur.

    Returns:
        dico_actif (dict): Dictionnaire du Joueur actif (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_adverse (dict): Dictionnaire du Joueur adverse (clé : identifiant du cercle ; valeur : [x, y, r]).
        banque (int): Budget du joueur.
    """
    diviser = False

    # Vérifie si un cercle adverse est touché et le divise en deux.
    if dico_adverse:
        diviser, dico_adverse = in_cercle(dico_adverse, x, y, color_adverse)

    # Si aucun cercle adverse n'est touché, le joueur va poser un cercle.
    if not diviser:
        if isinstance(banque, int):
            banque, rayon = taille_des_boules(banque, color_actif)

        # Crée un cercle pour le joueur actif.
        c = upemtk.cercle(x, y, rayon, couleur=color_actif, remplissage=color_actif)
        dico_actif[c] = [x, y, rayon]

        # Vérifie les intersections avec les cercles adverses.
        if intersection(dico_adverse, x, y, rayon):
            upemtk.efface(c)
            dico_actif.pop(c)

    return dico_actif, dico_adverse, banque


def process_player_actions(dico_actif, dico_adverse, rayon, variantes, banque, dico_obs, number, color_actif, color_adverse):
    """Cette fonction permet de gérer les actions avant le jeu, comme le temps de réaction, les scores, les obstacles et les variantes.

    Args:
        dico_actif (dict): Dictionnaire du joueur actif (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_adverse (dict): Dictionnaire du joueur adverse (clé : identifiant du cercle ; valeur : [x, y, r]).
        rayon (int): Rayon par défaut des cercles.
        variantes (dict): Dictionnaire des variantes.
        banque (int): Budget du joueur.
        dico_obs (dict): Dictionnaire des obstacles.
        number (int): Numéro du joueur.
        color_actif (str): Couleur du joueur actif.
        color_adverse (str): Couleur du joueur adverse.

    Returns:
        dico_actif (dict): Dictionnaire du joueur actif (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_adverse (dict): Dictionnaire du joueur adverse (clé : identifiant du cercle ; valeur : [x, y, r]).
        banque (int): Budget du joueur.
    """
    timing = False
    x, y, e = None, None, None
    if variantes["sablier"]:
        x, y, e = sablier(10, variantes["scores"])
        if x is None and y is None and e is None:
            timing = True
        if variantes["scores"] and y == 's':
            scores(dico_actif, dico_adverse, color_actif, color_adverse)
    else:
        if variantes["scores"]:
            e = 'Touche'
            while e == 'Touche':
                x, y, e = upemtk.attente_clic_ou_touche()
                if e == 'Touche' and y == 's':
                    scores(dico_actif, dico_adverse, color_actif, color_adverse)
        else:
            x, y, e = upemtk.attente_clic()
    if not timing:
        if e == "Touche":
            x, y , e = upemtk.attente_clic()
        if variantes["obstacle"] == True and intersection(dico_obs, x, y, rayon) == True:
            return dico_actif, dico_adverse, banque
        dico_actif, dico_adverse, banque = joueur(x, y, dico_actif, dico_adverse, rayon, banque, color_actif, color_adverse, number)
    return dico_actif, dico_adverse, banque


def game():
    """Cette fonction permet de jouer une partie de jeu.
    Elle permet de gérer les actions avant le jeu comme le choix des variantes, des pseudos et des couleurs."""
    dico_j1, dico_j2 = dict(), dict() # Forme du dictionnaire : clé : identifiant du cercle ; valeur : [x, y, r].
    dict()
    rayon = 50
    compteur = 1
    variantes, V_menu = menu()
    if not V_menu:
        return
    player_colors = colors()
    if 'quit' in player_colors:
        return
    pseudo_j1, pseudo_j2 = surname(player_colors)
    if pseudo_j1 == "quit" or pseudo_j2 == "quit":
        return
    tour = enter_numbers(melangeur_colors(player_colors[0], player_colors[1]))
    if tour == "quit":
        return
    clear_quit_button()
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, f"Bonne chance à vous {pseudo_j1} et {pseudo_j2} !", couleur=melangeur_colors(player_colors[0], player_colors[1]), police=game_font, ancrage="center", tag='jouer')
    upemtk.attente_clic_ou_touche()
    upemtk.efface('jouer')
    dico_obs = obstacles(variantes["obstacle"])
    banque1, banque2 = None, None
    if variantes["taille"]:
        banque1, banque2 = 10000, 10000
    while compteur <= tour: # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        # pause_button(), quit_button()
        crayon(player_colors[0], compteur, tour, pseudo_j1)
        dico_j1, dico_j2, banque1 = process_player_actions(dico_j1, dico_j2, rayon, variantes, banque1, dico_obs, 1, player_colors[0], player_colors[1])
        gomme()
        crayon(player_colors[1], compteur, tour, pseudo_j2)
        dico_j1, dico_j2, banque2 = process_player_actions(dico_j2, dico_j1, rayon, variantes, banque2, dico_obs, 2, player_colors[1], player_colors[0])
        gomme()
        variantes["terminaison"], tour = terminaison(variantes["terminaison"], tour, compteur)
        upemtk.mise_a_jour()
        compteur += 1
        if variantes["dynamique"]:
            dico_j1 = version_dynamique(dico_j1, dico_j2, dico_obs, player_colors[0])
            dico_j2 = version_dynamique(dico_j2, dico_j1, dico_obs, player_colors[1])
            upemtk.mise_a_jour()
        # clear_pause_button(), clear_quit_button()
    upemtk.attente_clic_ou_touche()
    vainqueur(dico_j1, dico_j2, pseudo_j1, pseudo_j2, player_colors)
    upemtk.attente_clic_ou_touche()
    if restart():
        upemtk.efface_tout()
        game()
    return
