# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *

# ------------------------------ Importation depuis la bibliothèque Python


def create_Interface(variantes):
    rectangle(0, 0, largeur_Fenetre, hauteur_Fenetre//10, couleur='black', remplissage='black', tag="interface1")
    rectangle(0, hauteur_Fenetre-hauteur_Fenetre//10, largeur_Fenetre, hauteur_Fenetre, couleur='black', remplissage='black', tag="interface2")
    rectangle(0, 0, largeur_Fenetre//7, hauteur_Fenetre, couleur='black', remplissage='black', tag="interface3")
    # Je voudrais créer sur l'interface 6 carrés (vert ou rouge) qui indiquent si la variante est activée ou non.
    if variantes["sablier"]:
        rectangle(10, hauteur_Fenetre//9, largeur_Fenetre//11, hauteur_Fenetre//10, couleur='green', remplissage='green', tag="sablier")
    else:
        rectangle(10, hauteur_Fenetre//10, largeur_Fenetre//11, hauteur_Fenetre//2, couleur='red', remplissage='red', tag="sablier")
    # if variantes["scores"]:
    #     rectangle(0, hauteur_Fenetre-hauteur_Fenetre//10, largeur_Fenetre//7, hauteur_Fenetre, couleur='green', remplissage='green', tag="scores")
    # else:
    #     rectangle(0, hauteur_Fenetre-hauteur_Fenetre//10, largeur_Fenetre//7, hauteur_Fenetre, couleur='red', remplissage='red', tag="scores")
    # if variantes["taille"]:
    #     rectangle(0, hauteur_Fenetre//10, largeur_Fenetre//7, hauteur_Fenetre//10*2, couleur='green', remplissage='green', tag="taille")
    # else:
    #     rectangle(0, hauteur_Fenetre//10, largeur_Fenetre//7, hauteur_Fenetre//10*2, couleur='red', remplissage='red', tag="taille")
    # if variantes["dynamique"]:
    #     rectangle(0, hauteur_Fenetre//10*2, largeur_Fenetre//7, hauteur_Fenetre//10*3, couleur='green', remplissage='green', tag="dynamique")
    # else:
    #     rectangle(0, hauteur_Fenetre//10*2, largeur_Fenetre//7, hauteur_Fenetre//10*3, couleur='red', remplissage='red', tag="dynamique")
    # if variantes["terminaison"]:
    #     rectangle(0, hauteur_Fenetre//10*3, largeur_Fenetre//7, hauteur_Fenetre//10*4, couleur='green', remplissage='green', tag="terminaison")
    # else:
    #     rectangle(0, hauteur_Fenetre//10*3, largeur_Fenetre//7, hauteur_Fenetre//10*4, couleur='red', remplissage='red', tag="terminaison")
    # if variantes["obstacle"]:
    #     rectangle(0, hauteur_Fenetre//10*4, largeur_Fenetre//7, hauteur_Fenetre//10*5, couleur='green', remplissage='green', tag="obstacle")
    # else:
    #     rectangle(0, hauteur_Fenetre//10*4, largeur_Fenetre//7, hauteur_Fenetre//10*5, couleur='red', remplissage='red', tag="obstacle")
    

def delete_Interface():
    efface("interface1")
    efface("interface2")
    efface("interface3")


def update_Interface(variantes):
    """Cette fonction permet de mettre à jour l'interface."""
    delete_Interface()
    create_Interface(variantes)


def crayon(color, compteur, tour, pseudo):
    """Cette fonction permet d'afficher le numéro du tour et l'indication pour savoir qui doit jouer.

    Args:
        color (_type_): Couleur du texte.
        compteur (int): Compteur du tour.
        tour (int): Nombre de tours.
        pseudo (str): Pseudo du joueur.
    """
    txt = "Tour de " + pseudo
    txt_tour = 'Tour : ' + str(compteur) + '/' + str(tour)
    texte(largeur_Fenetre//2, hauteur_Fenetre//18, txt, color, police=game_font, ancrage='center', taille=20, tag="joueur")
    texte(largeur_Fenetre//2, hauteur_Fenetre-hauteur_Fenetre//18, txt_tour, color, police=game_font, ancrage='center', taille=20, tag="tour")


def gomme():
    """Cette fonction efface le numéro (nombre) de tour et l'indication pour savoir qui doit jouer."""
    efface("joueur")
    efface("tour")