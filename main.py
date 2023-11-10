#!/usr/bin/env python
# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import largeur_Fenetre, hauteur_Fenetre
from game import GAME


def INTERFACE():
    """Corps principal du jeu avec création et destruction de l'interface"""
    cree_fenetre(largeur_Fenetre, hauteur_Fenetre)
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bienvenue !", taille=40, police="Monocraft", ancrage="center", tag='jouer')
    attente_clic_ou_touche()
    efface('jouer')
    GAME()
    ferme_fenetre()

if __name__ == '__main__':
    INTERFACE()
