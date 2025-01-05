# Programmeurs : Cédric Mariya Constantine, Wilson Groevius et Enzo Létocart
# ------------------------------ Importation
from boutons import clear_quit_button
from calcul import calcul_aire, in_cercle, intersection
from couleurs import colors, melangeur_colors
from menu import menu
from texte import *
from variantes import sablier, scores, terminaison, obstacles, taille_des_boules, version_dynamique


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


def vainqueur(dico_j1, dico_j2, pseudo_j1, pseudo_j2, lst_colors):
    """
    Détermine et affiche le vainqueur de la partie en fonction des aires occupées par chaque joueur.

    Args:
        dico_j1 (dict): Dictionnaire du Joueur 1 (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_j2 (dict): Dictionnaire du Joueur 2 (clé : identifiant du cercle ; valeur : [x, y, r]).
        pseudo_j1 (str): Pseudo du Joueur 1.
        pseudo_j2 (str): Pseudo du Joueur 2.
        lst_colors (list): Liste des couleurs des joueurs ([couleur Joueur 1, couleur Joueur 2]).
    """
    def victory_message_color(pourcentage_j1, pourcentage_j2, pseudo1, pseudo2, lst_colors):
        """Cette fonction permet de déterminer le message de victoire en fonction des pourcentages de chaque joueur mais aussi de la couleur du texte."""
        if pourcentage_j1 > pourcentage_j2:
            return f"Félicitations ! {pseudo1} a gagné avec {pourcentage_j1:.2f}% !", lst_colors[0]
        elif pourcentage_j1 < pourcentage_j2:
            return f"Félicitations ! {pseudo2} a gagné avec {pourcentage_j2:.2f}% !", lst_colors[1]
        else:
            return "C'est une égalité parfaite !", melangeur_colors(lst_colors[0], lst_colors[1])

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
    message, couleur = victory_message_color(pourcentage_j1, pourcentage_j2, pseudo_j1, pseudo_j2, lst_colors)

    # Affiche le résultat final
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2, message, ancrage="center", police=game_font, taille=25, couleur=couleur)
    upemtk.mise_a_jour()


def restart():
    """Cette fonction permet de demander au joueur s'il veut rejouer ou non.

    Returns:
        bool: Renvoie vrai si le joueur veut rejouer, sinon faux.
    """
    upemtk.efface_tout()
    upemtk.texte(largeur_Fenetre//2, hauteur_Fenetre//2-150, "Voulez-vous rejouer ?", ancrage='center', police=game_font, taille=35, couleur='black', tag='restart-text')
    upemtk.rectangle(largeur_Fenetre//2-400, hauteur_Fenetre//2-50, largeur_Fenetre//2-200, hauteur_Fenetre//2+50, couleur='black', remplissage='white', epaisseur=4, tag='restart-yes')
    upemtk.texte(largeur_Fenetre//2-300, hauteur_Fenetre//2, "Oui", ancrage='center', police=game_font, taille=25, couleur='black', tag='restart-yes-text')
    upemtk.rectangle(largeur_Fenetre//2+200, hauteur_Fenetre//2-50, largeur_Fenetre//2+400, hauteur_Fenetre//2+50, couleur='black', remplissage='white', epaisseur=4, tag='restart-no')
    upemtk.texte(largeur_Fenetre//2+300, hauteur_Fenetre//2, "Non", ancrage='center', police=game_font, taille=25, couleur='black', tag='restart-no-text')
    isRestart = None
    while isRestart is None:
        x, y, e = upemtk.attente_clic()
        if largeur_Fenetre//2-400 < x < largeur_Fenetre//2-200 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50:
            isRestart = True
        elif largeur_Fenetre//2+200 < x < largeur_Fenetre//2+400 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50:
            isRestart = False
    upemtk.efface('restart-text')
    upemtk.efface('restart-yes')
    upemtk.efface('restart-yes-text')
    upemtk.efface('restart-no')
    upemtk.efface('restart-no-text')
    return isRestart


def joueur(x, y, dico_actif, dico_adverse, rayon, banque, color_actif, color_adverse):
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
        if isinstance(banque, int): # La banque est un nombre entier (variante taille des boules activée).
            banque, rayon = taille_des_boules(banque, color_actif)

        # Crée un cercle pour le joueur actif.
        c = upemtk.cercle(x, y, rayon, couleur=color_actif, remplissage=color_actif)
        dico_actif[c] = [x, y, rayon]

        # Vérifie les intersections avec les cercles adverses.
        if intersection(dico_adverse, x, y, rayon):
            upemtk.efface(c)
            dico_actif.pop(c)

    return dico_actif, dico_adverse, banque


def process_player_actions(dico_actif, dico_adverse, rayon, variantes, banque, dico_obs, color_actif, color_adverse):
    """Cette fonction permet de gérer les actions avant le jeu, comme le temps de réaction, les scores, les obstacles et les variantes.

    Args:
        dico_actif (dict): Dictionnaire du joueur actif (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_adverse (dict): Dictionnaire du joueur adverse (clé : identifiant du cercle ; valeur : [x, y, r]).
        rayon (int): Rayon par défaut des cercles.
        variantes (dict): Dictionnaire des variantes.
        banque (int): Budget du joueur.
        dico_obs (dict): Dictionnaire des obstacles.
        color_actif (str): Couleur du joueur actif.
        color_adverse (str): Couleur du joueur adverse.

    Returns:
        dico_actif (dict): Dictionnaire du joueur actif (clé : identifiant du cercle ; valeur : [x, y, r]).
        dico_adverse (dict): Dictionnaire du joueur adverse (clé : identifiant du cercle ; valeur : [x, y, r]).
        banque (int): Budget du joueur.
    """
    def handle_scores():
        """Cette fonction permet d'afficher les scores des joueurs."""
        scores(dico_actif, dico_adverse, color_actif, color_adverse)

    def handle_input():
        """Gère les clics ou touches selon les variantes."""
        if variantes["scores"]:
            while True:
                x, y, e = upemtk.attente_clic_ou_touche()
                if e == "Touche" and y == 's':
                    handle_scores()
                else:
                    return x, y, e
        else:
            return upemtk.attente_clic()

    timing = False
    # Gestion du sablier
    if variantes["sablier"]:
        x, y, e = sablier(10, variantes["scores"])
        if x is None and y is None and e is None:
            timing = True
        elif variantes["scores"] and y == 's':
            handle_scores()
    else:
        x, y, e = handle_input()

    if not timing:
        if e == "Touche":
            x, y, e = upemtk.attente_clic()

        # Vérification des obstacles
        if variantes["obstacle"] and intersection(dico_obs, x, y, rayon):
            return dico_actif, dico_adverse, banque
        # Mise à jour des joueurs
        dico_actif, dico_adverse, banque = joueur(x, y, dico_actif, dico_adverse, rayon, banque, color_actif, color_adverse)
    return dico_actif, dico_adverse, banque


def game():
    """Cette fonction permet de jouer une partie de jeu.
    Elle permet de gérer les actions avant le jeu comme le choix des variantes, des pseudos et des couleurs."""
    dico_j1, dico_j2 = dict(), dict() # Forme du dictionnaire : clé : identifiant du cercle ; valeur : [x, y, r].
    rayon = 50
    compteur = 1
    variantes, V_menu = menu()
    if not V_menu:
        return
    player_colors = colors() # Récupération des couleurs des joueurs dans une liste
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

    # Initialisation des banques des joueurs si la variante taille des boules est activée
    banque_j1, banque_j2 = 10000 if variantes["taille"] else None, 10000 if variantes["taille"] else None

    while compteur <= tour: # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        # pause_button(), quit_button()
        crayon(player_colors[0], compteur, tour, pseudo_j1)
        dico_j1, dico_j2, banque_j1 = process_player_actions(dico_j1, dico_j2, rayon, variantes, banque_j1, dico_obs, player_colors[0], player_colors[1])
        gomme()
        crayon(player_colors[1], compteur, tour, pseudo_j2)
        dico_j1, dico_j2, banque_j2 = process_player_actions(dico_j2, dico_j1, rayon, variantes, banque_j2, dico_obs, player_colors[1], player_colors[0])
        gomme()
        variantes["terminaison"], tour = terminaison(variantes["terminaison"], tour, compteur)
        compteur += 1
        if variantes["dynamique"]:
            # Pour une raison inconnue, la couleur des cercles des joueurs s'inverse à chaque tour, sachant que ce problème n'apparaît qu'avec la variante dynamique.
            # Si vous avez une idée de pourquoi cela se produit, n'hésitez pas à nous le dire.
            dico_j1 = version_dynamique(dico_j1, dico_j2, dico_obs, player_colors[0])
            dico_j2 = version_dynamique(dico_j2, dico_j1, dico_obs, player_colors[1])
        upemtk.mise_a_jour()
        # clear_pause_button(), clear_quit_button()
    upemtk.attente_clic_ou_touche()
    vainqueur(dico_j1, dico_j2, pseudo_j1, pseudo_j2, player_colors)
    upemtk.attente_clic_ou_touche()
    if restart():
        game()
    return
