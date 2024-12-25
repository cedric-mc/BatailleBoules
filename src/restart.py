#!/usr/bin/env python
# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
import upemtk
from default import largeur_Fenetre, hauteur_Fenetre, game_font

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
            upemtk.efface('restart-text')
            upemtk.efface('restart-yes')
            upemtk.efface('restart-yes-text')
            upemtk.efface('restart-no')
            upemtk.efface('restart-no-text')
            isRestart = True
        elif largeur_Fenetre//2+200 < x < largeur_Fenetre//2+400 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50:
            upemtk.efface('restart-text')
            upemtk.efface('restart-yes')
            upemtk.efface('restart-yes-text')
            upemtk.efface('restart-no')
            upemtk.efface('restart-no-text')
            isRestart = False
    return isRestart
