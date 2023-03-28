# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *
from menu import choose_colors


def colors():
    """
    #FF7900 et #F7E360 (orange et jaune)
    #F33129 et #0179C0 (rouge et bleu)
    #2C6452 et #F7777F (vert et rose)
    #552B24 et #F33129 (marron et rouge)
    #0179C0 et #65419C (bleu et violet)
    #F7777F et #0179C0 (rose et bleu)
    #65419C et #F7777F (violet et rose)
    #2C6452 et #F7E360 (vert et jaune)
    #F33129 et #F7E360 (rouge et jaune)
    #552B24 et #F7777F (marron et rose)
    """
    color1, color2 = None, None
    rec1 = rectangle(largeur_Fenetre//2-700, 100, largeur_Fenetre//2-550, 250, remplissage="#FF7900", epaisseur=0)
    rec2 = rectangle(largeur_Fenetre//2-550, 100, largeur_Fenetre//2-400, 250, remplissage="#F7E360", epaisseur=0)
    rec3 = rectangle(largeur_Fenetre//2-350, 100, largeur_Fenetre//2-200, 250, remplissage="#F33129", epaisseur=0)
    rec4 = rectangle(largeur_Fenetre//2-200, 100, largeur_Fenetre//2-50, 250, remplissage="#0179C0", epaisseur=0)
    rec5 = rectangle(largeur_Fenetre//2+50, 100, largeur_Fenetre//2+200, 250, remplissage="#2C6452", epaisseur=0)
    rec6 = rectangle(largeur_Fenetre//2+200, 100, largeur_Fenetre//2+350, 250, remplissage="#F7777F", epaisseur=0)
    rec7 = rectangle(largeur_Fenetre//2+400, 100, largeur_Fenetre//2+550, 250, remplissage="#552B24", epaisseur=0)
    rec8 = rectangle(largeur_Fenetre//2+550, 100, largeur_Fenetre//2+700, 250, remplissage="#F33129", epaisseur=0)
    
    rec9 = rectangle(largeur_Fenetre//2-700, hauteur_Fenetre//2-75, largeur_Fenetre//2-550, hauteur_Fenetre//2+75, remplissage="#0179C0", epaisseur=0)
    rec10 = rectangle(largeur_Fenetre//2-550, hauteur_Fenetre//2-75, largeur_Fenetre//2-400, hauteur_Fenetre//2+75, remplissage="#65419C", epaisseur=0)
    rec11 = rectangle(largeur_Fenetre//2+400, hauteur_Fenetre//2-75, largeur_Fenetre//2+550, hauteur_Fenetre//2+75, remplissage="#F7777F", epaisseur=0)
    rec12 = rectangle(largeur_Fenetre//2+550, hauteur_Fenetre//2-75, largeur_Fenetre//2+700, hauteur_Fenetre//2+75, remplissage="#0179C0", epaisseur=0)
    
    rec13 = rectangle(largeur_Fenetre//2-700, hauteur_Fenetre-100, largeur_Fenetre//2-550, hauteur_Fenetre-250, remplissage="#65419C", epaisseur=0)
    rec14 = rectangle(largeur_Fenetre//2-550, hauteur_Fenetre-100, largeur_Fenetre//2-400, hauteur_Fenetre-250, remplissage="#F7777F", epaisseur=0)
    rec15 = rectangle(largeur_Fenetre//2-350, hauteur_Fenetre-100, largeur_Fenetre//2-200, hauteur_Fenetre-250, remplissage="#2C6452", epaisseur=0)
    rec16 = rectangle(largeur_Fenetre//2-200, hauteur_Fenetre-100, largeur_Fenetre//2-50, hauteur_Fenetre-250, remplissage="#F7E360", epaisseur=0)
    rec17 = rectangle(largeur_Fenetre//2+50, hauteur_Fenetre-100, largeur_Fenetre//2+200, hauteur_Fenetre-250, remplissage="#F33129", epaisseur=0)
    rec18 = rectangle(largeur_Fenetre//2+200, hauteur_Fenetre-100, largeur_Fenetre//2+350, hauteur_Fenetre-250, remplissage="#F7E360", epaisseur=0)
    rec19 = rectangle(largeur_Fenetre//2+400, hauteur_Fenetre-100, largeur_Fenetre//2+550, hauteur_Fenetre-250, remplissage="#552B24", epaisseur=0)
    rec20 = rectangle(largeur_Fenetre//2+550, hauteur_Fenetre-100, largeur_Fenetre//2+700, hauteur_Fenetre-250, remplissage="#F7777F", epaisseur=0)
    
    color1, color2 = choose_colors()
    efface(rec1), efface(rec2), efface(rec3), efface(rec4), efface(rec5), efface(rec6), efface(rec7), efface(rec8)
    efface(rec9), efface(rec10), efface(rec11), efface(rec12)
    efface(rec13), efface(rec14), efface(rec15), efface(rec16), efface(rec17), efface(rec18), efface(rec19), efface(rec20)
    return color1, color2


def melangeur_colors(color1, color2):
    # Convertir les couleurs hexadécimales en tuples de valeurs RGB
    r1, g1, b1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
    r2, g2, b2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
    # Calculer la moyenne des valeurs RGB de chaque couleur
    r3 = (r1 + r2)//2
    g3 = (g1 + g2)//2
    b3 = (b1 + b2)//2
    # Convertir les valeurs RGB moyennes en une couleur hexadécimale
    color3 = "#{:02x}{:02x}{:02x}".format(r3, g3, b3)
    return color3