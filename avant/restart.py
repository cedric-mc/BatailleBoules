#!/usr/bin/env python
# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import largeur_Fenetre, hauteur_Fenetre

def RESTART():
    efface_tout()
    texte(largeur_Fenetre//2, hauteur_Fenetre//2-150, "Voulez-vous rejouer ?", ancrage='center', police="Monocraft", taille=35, couleur='black', tag='restart-text')
    rectangle(largeur_Fenetre//2-400, hauteur_Fenetre//2-50, largeur_Fenetre//2-200, hauteur_Fenetre//2+50, couleur='black', remplissage='white', epaisseur=4, tag='restart-yes')
    texte(largeur_Fenetre//2-300, hauteur_Fenetre//2, "Oui", ancrage='center', police="Monocraft", taille=25, couleur='black', tag='restart-yes-text')
    rectangle(largeur_Fenetre//2+200, hauteur_Fenetre//2-50, largeur_Fenetre//2+400, hauteur_Fenetre//2+50, couleur='black', remplissage='white', epaisseur=4, tag='restart-no')
    texte(largeur_Fenetre//2+300, hauteur_Fenetre//2, "Non", ancrage='center', police="Monocraft", taille=25, couleur='black', tag='restart-no-text')
    isRestart = None
    while isRestart is None:
        x, y, e = attente_clic()
        if largeur_Fenetre//2-400 < x < largeur_Fenetre//2-200 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50:
            efface('restart-text')
            efface('restart-yes')
            efface('restart-yes-text')
            efface('restart-no')
            efface('restart-no-text')
            isRestart = True
        elif largeur_Fenetre//2+200 < x < largeur_Fenetre//2+400 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50:
            efface('restart-text')
            efface('restart-yes')
            efface('restart-yes-text')
            efface('restart-no')
            efface('restart-no-text')
            isRestart = False
    return isRestart