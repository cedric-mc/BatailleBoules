# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *

# ------------------------------ Importation depuis la bibliothèque Python


def crayon(color, compteur, tour, pseudo):
    """Paramètres :
    - color : couleur du joueur, type : str ;
    - compteur : le nombre de tour(s) écoulé, type : int ;
    - tour : le nombre de tours pour la partie, type : int ;
    - pseudo : le pseudo / surnom du joueur, type : str.
    Cette fonction permet d'afficher le numéro (nombre) du tour et indique qui doit jouer."""
    txt = "Tour de " + pseudo
    txt_tour = 'Tour : ' + str(compteur) + '/' + str(tour)
    texte(largeur_Fenetre//2, hauteur_Fenetre//18, txt, color, police=game_font, ancrage='center', taille=20, tag="joueur")
    texte(largeur_Fenetre//2, hauteur_Fenetre-hauteur_Fenetre//18, txt_tour, color, police=game_font, ancrage='center', taille=20, tag="tour")


def gomme():
    """Cette fonction efface le numéro (nombre) de tour et l'indication pour savoir qui doit jouer."""
    efface("joueur")
    efface("tour")