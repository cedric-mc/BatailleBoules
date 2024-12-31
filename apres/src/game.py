# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
from boutons import pause_button, quit_button, clear_pause_button, clear_quit_button
from couleurs import colors, melangeur_colors
from joueur import *
from menu import menu
from restart import restart
from texte import *


def vainqueur(dico_j1, dico_j2, pseudo1, pseudo2, lst_colors):
    """Cette fonction permet de déterminer et d'annoncer le vainqueur de la partie.

    Args:
        dico_j1 (dict): Dictionnaire du Joueur 1 (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_j2 (dict): Dictionnaire du Joueur 2 (clé : identifiant du cercle ; valeur : [x, y, r]).
        pseudo1 (str): Pseudo du Joueur 1.
        pseudo2 (str): Pseudo du Joueur 2.
        lst_colors (list): Liste des couleurs des joueurs (lst_colors[0] : couleur du Joueur 1, lst_colors[1] : couleur du Joueur 2).
    """
    upemtk.rectangle(0, hauteur_Fenetre//2-50, largeur_Fenetre, hauteur_Fenetre//2+50, remplissage='white')
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Calcul en cours...", ancrage='center', police=game_font, taille=35, tag='calcul')
    upemtk.mise_a_jour()
    # Calcul d'aire des cercles, en comptant les pixels. Le calcul est effectué en se basant sur l'aire autour des cercles.
    S1, S2 = calcul_aire(dico_j1, dico_j2)
    rouge, bleu = len(S1), len(S2)
    # Génération d'un pourcentage pour chaque joueur.
    rouge, bleu = (rouge/(rouge+bleu))*100, (bleu/(rouge+bleu))*100 # TODO: Ajouter le pourcentage de victoire.
    sleep(0.5)
    upemtk.mise_a_jour()
    upemtk.efface('calcul')
    if rouge == 0 and bleu == 0:
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Vous êtes pas doué pour jouer !", ancrage='center', taille=25, police=game_font)
    elif rouge > bleu:
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo1 + " !", ancrage="center", police=game_font, taille=25, couleur=lst_colors[0])
    elif rouge < bleu:
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo2 + " !", ancrage="center", police=game_font, taille=25, couleur=lst_colors[1])
    elif rouge == bleu:
        upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Égalité !", ancrage="center", police=game_font, taille=25, couleur=melangeur_colors(lst_colors[0], lst_colors[1]))
    upemtk.mise_a_jour()


def avant_jeu(dico_j1, dico_j2, rayon, variantes, banque, dico_obs, number, color1, color2):
    """Cette fonction permet de gérer les actions avant le jeu, comme le temps de réaction, les scores, les obstacles et les variantes.

    Args:
        dico_j1 (dict): Dictionnaire du Joueur 1 (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_j2 (dict): Dictionnaire du Joueur 2 (clé : identifiant du cercle ; valeur : [x, y, r]).
        rayon (int): Rayon par défaut des cercles.
        variantes (dict): Dictionnaire des variantes.
        banque (int): Budget du joueur.
        dico_obs (dict): Dictionnaire des obstacles.
        number (int): Numéro du joueur.
        color1 (str): Couleur du Joueur 1.
        color2 (str): Couleur du Joueur 2.

    Returns:
        dico_j1 (dict): Dictionnaire du Joueur 1 (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_j2 (dict): Dictionnaire du Joueur 2 (clé : identifiant du cercle ; valeur : [x, y, r]).
        banque (int): Budget du joueur.
    """
    timing = False
    x, y, e = None, None, None
    if variantes["sablier"]:
        x, y, e = sablier(10, variantes["scores"])
        if x is None and y is None and e is None:
            timing = True
        if variantes["scores"] and y == 's':
            scores(dico_j1, dico_j2, color1, color2)
    else:
        if variantes["scores"]:
            e = 'Touche'
            while e == 'Touche':
                x, y, e = upemtk.attente_clic_ou_touche()
                if e == 'Touche' and y == 's':
                    scores(dico_j1, dico_j2, color1, color2)
        else:
            x, y, e = upemtk.attente_clic()
    if not timing:
        if e == "Touche":
            x, y , e = upemtk.attente_clic()
        if variantes["obstacle"] == True and intersection(dico_obs, x, y, rayon) == True:
            return dico_j1, dico_j2, banque
        dico_j1, dico_j2, banque = joueur(x, y, dico_j1, dico_j2, rayon, banque, color1, color2, number)
    return dico_j1, dico_j2, banque


def joueur(x, y, dico_j1, dico_j2, rayon, banque, color1, color2, number):
    if number == 1:
            dico_j1, dico_j2, banque = J1(x, y, dico_j1, dico_j2, rayon, banque, color1, color2)
    elif number == 2:
        dico_j2, dico_j1, banque = J2(x, y, dico_j2, dico_j1, rayon, banque, color1, color2)
    return dico_j1, dico_j2, banque


def game():
    """Cette fonction permet de jouer une partie de jeu.
    Elle permet de gérer les actions avant le jeu comme le choix des variantes, des pseudos et des couleurs."""
    dico_j1, dico_j2 = dict(), dict() # Forme du dictionnaire : clé : identifiant du cercle ; valeur : [x, y, r].
    dico_obs = dict()
    rayon = 50
    compteur = 1
    variantes, V_menu = menu()
    if not V_menu:
        return
    player_colors = colors()
    if 'quit' in player_colors:
        return
    pseudo1, pseudo2 = surname(player_colors)
    if pseudo1 == "quit" or pseudo2 == "quit":
        return
    tour = enter_numbers(melangeur_colors(player_colors[0], player_colors[1]))
    if tour == "quit":
        return
    clear_quit_button()
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bonne chance à vous " + pseudo1 + " et " + pseudo2 + " !", couleur=melangeur_colors(player_colors[0], player_colors[1]), police=game_font, ancrage="center", tag='jouer')
    upemtk.attente_clic_ou_touche()
    upemtk.efface('jouer')
    dico_obs = obstacles(variantes["obstacle"], dico_obs)
    banque1, banque2 = None, None
    if variantes["taille"]:
        banque1, banque2 = 10000, 10000
    while compteur <= tour: # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        pause_button(), quit_button()
        crayon(player_colors[0], compteur, tour, pseudo1)
        dico_j1, dico_j2, banque1 = avant_jeu(dico_j1, dico_j2, rayon, variantes, banque1, dico_obs, 1, player_colors[0], player_colors[1])
        gomme()
        crayon(player_colors[1], compteur, tour, pseudo2)
        dico_j1, dico_j2, banque2 = avant_jeu(dico_j1, dico_j2, rayon, variantes, banque2, dico_obs, 2, player_colors[0], player_colors[1])
        gomme()
        variantes["terminaison"], tour = terminaison(variantes["terminaison"], tour, compteur)
        upemtk.mise_a_jour()
        compteur += 1
        if variantes["dynamique"]:
            dico_j1 = version_dynamique(dico_j1, dico_j2, dico_obs, player_colors[0])
            dico_j2 = version_dynamique(dico_j2, dico_j1, dico_obs, player_colors[1])
            upemtk.mise_a_jour()
        clear_pause_button(), clear_quit_button()
    upemtk.attente_clic_ou_touche()
    vainqueur(dico_j1, dico_j2, pseudo1, pseudo2, player_colors)
    upemtk.attente_clic_ou_touche()
    if restart():
        game()
    return
