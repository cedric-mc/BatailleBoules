# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis la bibliothèque Python
from time import sleep


# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import largeur_Fenetre, hauteur_Fenetre
from calcul import calcul_aire
from game import GAME
from colors import melangeur_colors


def VAINQUEUR(dico_j1, dico_j2, pseudo1, pseudo2, color1, color2):
    """Cette fonction prend en paramètre la largeur et la hauteur de la fenêtre (maximale)
    et les cercles des 2 joueurs pour déterminer en parcourant l'aire de jeu et annoncé le vainqueur.
    dico_j1 et dico_j2 sont des dictionnaires sous la forme (identifiant du cercle: [x, y, r] ;
    x et y représente le centre du cercle)."""
    rectangle(0, hauteur_Fenetre//2-50, largeur_Fenetre, hauteur_Fenetre//2+50, remplissage='white')
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Calcul en cours...", ancrage='center', police="Monocraft", taille=35, tag='calcul')
    mise_a_jour()
    # Calcul d'aire des cercles, en comptant les pixels. Le calcul est effectué en se basant sur l'aire autour des cercles.
    S1, S2 = calcul_aire(dico_j1, dico_j2)
    rouge, bleu = len(S1), len(S2)
    sleep(1)
    mise_a_jour()
    efface('calcul')
    if rouge == 0 and bleu == 0:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Vous êtes pas doué pour jouer !", ancrage='center', taille=25, police="Monocraft")
    elif rouge > bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo1 + " !", ancrage="center", police="Monocraft", taille=25, couleur=color1)
    elif rouge < bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Félicitation ! Tu as gagné " + pseudo2 + " !", ancrage="center", police="Monocraft", taille=25, couleur=color2)
    elif rouge == bleu:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Égalité !", ancrage="center", police="Monocraft", taille=25, couleur=melangeur_colors(color1, color2))


def INTERFACE():
    """Corps principal du jeu avec création et destruction de l'interface"""
    dico_j1, dico_j2 = dict(), dict() # Forme du dictionnaire : clé : identifiant du cercle ; valeur : [x, y, r].
    dico_obs = dict()
    rayon = 50
    compteur = 1
    cree_fenetre(largeur_Fenetre, hauteur_Fenetre)
    dico_j1, dico_j2, pseudo1, pseudo2, color1, color2 = GAME(dico_j1, dico_j2, dico_obs, rayon, compteur)
    attente_clic_ou_touche()
    VAINQUEUR(dico_j1, dico_j2, pseudo1, pseudo2, color1, color2)
    attente_clic_ou_touche()
    ferme_fenetre()

if __name__ == '__main__':
    """Programme principal qui fait appel à la fonction GAME, le corps principal du jeu."""
    INTERFACE()
