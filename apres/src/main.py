#!/usr/bin/env python
# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
import upemtk
from default import largeur_Fenetre, hauteur_Fenetre, game_font
from game import game


def main():
    """Fonction principale qui permet de lancer le jeu."""
    upemtk.cree_fenetre(largeur_Fenetre, hauteur_Fenetre)
    upemtk.rectangle(0, 0, largeur_Fenetre, hauteur_Fenetre, remplissage="white", couleur="black")
    upemtk.texte(largeur_Fenetre // 2, hauteur_Fenetre // 2, "Bienvenue !", taille=40, police=game_font, ancrage="center", tag='jouer')
    upemtk.clic()
    upemtk.efface('jouer')
    game()
    upemtk.ferme_fenetre()

if __name__ == '__main__':
    main()
