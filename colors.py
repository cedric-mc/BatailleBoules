# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis le dossier source
from upemtk import *
from default import *
import menu

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
    # ------------------------------ Choix des couleurs des joueurs première ligne
    rec1 = rectangle(largeur_Fenetre//2-700, 100, largeur_Fenetre//2-550, 250, remplissage="#FF7900", epaisseur=0)
    rec2 = rectangle(largeur_Fenetre//2-550, 100, largeur_Fenetre//2-400, 250, remplissage="#F7E360", epaisseur=0)
    rec3 = rectangle(largeur_Fenetre//2-350, 100, largeur_Fenetre//2-200, 250, remplissage="#F33129", epaisseur=0)
    rec4 = rectangle(largeur_Fenetre//2-200, 100, largeur_Fenetre//2-50, 250, remplissage="#0179C0", epaisseur=0)
    rec5 = rectangle(largeur_Fenetre//2+50, 100, largeur_Fenetre//2+200, 250, remplissage="#2C6452", epaisseur=0)
    rec6 = rectangle(largeur_Fenetre//2+200, 100, largeur_Fenetre//2+350, 250, remplissage="#F7777F", epaisseur=0)
    rec7 = rectangle(largeur_Fenetre//2+400, 100, largeur_Fenetre//2+550, 250, remplissage="#552B24", epaisseur=0)
    rec8 = rectangle(largeur_Fenetre//2+550, 100, largeur_Fenetre//2+700, 250, remplissage="#F33129", epaisseur=0)
    # ------------------------------ Choix des couleurs des joueurs deuxième ligne
    rec9 = rectangle(largeur_Fenetre//2-700, hauteur_Fenetre//2-75, largeur_Fenetre//2-550, hauteur_Fenetre//2+75, remplissage="#0179C0", epaisseur=0)
    rec10 = rectangle(largeur_Fenetre//2-550, hauteur_Fenetre//2-75, largeur_Fenetre//2-400, hauteur_Fenetre//2+75, remplissage="#65419C", epaisseur=0)
    rec11 = rectangle(largeur_Fenetre//2+400, hauteur_Fenetre//2-75, largeur_Fenetre//2+550, hauteur_Fenetre//2+75, remplissage="#F7777F", epaisseur=0)
    rec12 = rectangle(largeur_Fenetre//2+550, hauteur_Fenetre//2-75, largeur_Fenetre//2+700, hauteur_Fenetre//2+75, remplissage="#0179C0", epaisseur=0)
    # ------------------------------ Choix des couleurs des joueurs troisième ligne
    rec13 = rectangle(largeur_Fenetre//2-700, hauteur_Fenetre-100, largeur_Fenetre//2-550, hauteur_Fenetre-250, remplissage="#65419C", epaisseur=0)
    rec14 = rectangle(largeur_Fenetre//2-550, hauteur_Fenetre-100, largeur_Fenetre//2-400, hauteur_Fenetre-250, remplissage="#F7777F", epaisseur=0)
    rec15 = rectangle(largeur_Fenetre//2-350, hauteur_Fenetre-100, largeur_Fenetre//2-200, hauteur_Fenetre-250, remplissage="#2C6452", epaisseur=0)
    rec16 = rectangle(largeur_Fenetre//2-200, hauteur_Fenetre-100, largeur_Fenetre//2-50, hauteur_Fenetre-250, remplissage="#F7E360", epaisseur=0)
    rec17 = rectangle(largeur_Fenetre//2+50, hauteur_Fenetre-100, largeur_Fenetre//2+200, hauteur_Fenetre-250, remplissage="#F33129", epaisseur=0)
    rec18 = rectangle(largeur_Fenetre//2+200, hauteur_Fenetre-100, largeur_Fenetre//2+350, hauteur_Fenetre-250, remplissage="#F7E360", epaisseur=0)
    rec19 = rectangle(largeur_Fenetre//2+400, hauteur_Fenetre-100, largeur_Fenetre//2+550, hauteur_Fenetre-250, remplissage="#552B24", epaisseur=0)
    rec20 = rectangle(largeur_Fenetre//2+550, hauteur_Fenetre-100, largeur_Fenetre//2+700, hauteur_Fenetre-250, remplissage="#F7777F", epaisseur=0)
    # ------------------------------ Texte des couleurs des joueurs première ligne
    txt1 = texte(largeur_Fenetre//2-625, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt2 = texte(largeur_Fenetre//2-475, 175, "J2", taille=45, couleur="white", ancrage="center")
    txt3 = texte(largeur_Fenetre//2-275, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt4 = texte(largeur_Fenetre//2-125, 175, "J2", taille=45, couleur="white", ancrage="center")
    txt5 = texte(largeur_Fenetre//2+125, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt6 = texte(largeur_Fenetre//2+275, 175, "J2", taille=45, couleur="white", ancrage="center")
    txt7 = texte(largeur_Fenetre//2+475, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt8 = texte(largeur_Fenetre//2+625, 175, "J2", taille=45, couleur="white", ancrage="center")
    # ------------------------------ Texte des couleurs des joueurs deuxième ligne
    txt9 = texte(largeur_Fenetre//2-625, hauteur_Fenetre//2, "J1", taille=45, couleur="white", ancrage="center")
    txt10 = texte(largeur_Fenetre//2-475, hauteur_Fenetre//2, "J2", taille=45, couleur="white", ancrage="center")
    txt11 = texte(largeur_Fenetre//2+475, hauteur_Fenetre//2, "J1", taille=45, couleur="white", ancrage="center")
    txt12 = texte(largeur_Fenetre//2+625, hauteur_Fenetre//2, "J2", taille=45, couleur="white", ancrage="center")
    # ------------------------------ Texte des couleurs des joueurs troisième ligne
    txt13 = texte(largeur_Fenetre//2-625, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt14 = texte(largeur_Fenetre//2-475, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    txt15 = texte(largeur_Fenetre//2-275, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt16 = texte(largeur_Fenetre//2-125, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    txt17 = texte(largeur_Fenetre//2+125, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt18 = texte(largeur_Fenetre//2+275, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    txt19 = texte(largeur_Fenetre//2+475, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt20 = texte(largeur_Fenetre//2+625, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    
    color1, color2 = menu.choose_colors()
    if color1 == "quit" or color2 == "quit":
        return color1, color2
    # Efface les rectangles de la première ligne
    efface(rec1), efface(rec2), efface(rec3), efface(rec4), efface(rec5), efface(rec6), efface(rec7), efface(rec8)
    efface(rec9), efface(rec10), efface(rec11), efface(rec12) # Efface les rectangles de la deuxième ligne
    # Efface les rectangles de la troisième ligne
    efface(rec13), efface(rec14), efface(rec15), efface(rec16), efface(rec17), efface(rec18), efface(rec19), efface(rec20)
    # Efface les textes de la première ligne
    efface(txt1), efface(txt2), efface(txt3), efface(txt4), efface(txt5), efface(txt6), efface(txt7), efface(txt8)
    efface(txt9), efface(txt10), efface(txt11), efface(txt12) # Efface les textes de la deuxième ligne
    # Efface les textes de la troisième ligne
    efface(txt13), efface(txt14), efface(txt15), efface(txt16), efface(txt17), efface(txt18), efface(txt19), efface(txt20)
    return color1, color2


def melangeur_colors(color1, color2):
    # # Convertir les couleurs hexadécimales en tuples de valeurs RGB
    # r1, g1, b1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
    # r2, g2, b2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
    # # Calculer la moyenne des valeurs RGB de chaque couleur
    # r3 = (r1 + r2)//2
    # g3 = (g1 + g2)//2
    # b3 = (b1 + b2)//2
    # # Convertir les valeurs RGB moyennes en une couleur hexadécimale
    # color3 = "#{:02x}{:02x}{:02x}".format(r3, g3, b3)
    # return color3
    
    if color1 == "#FF7900" and color2 == "#F7E360":
        return "#F33129"
    elif color1 == "#F33129" and color2 == "#0179C0":
        return "#65419C"
    elif color1 == "#2C6452" and color2 == "#F7777F":
        return "#FF7900"
    elif color1 == "#552B24" and color2 == "#F33129":
        return "#F7777F"
    
    elif color1 == "#0179C0" and color2 == "#65419C":
        return "#F33129"
    elif color1 == "#F7777F" and color2 == "#0179C0":
        return "#65419C"
    
    elif color1 == "#65419C" and color2 == "#F7777F":
        return "#0179C0"
    elif color1 == "#2C6452" and color2 == "#F7E360":
        return "#0179C0"
    elif color1 == "#F33129" and color2 == "#F7E360":
        return "#FF7900"
    elif color1 == "#552B24" and color2 == "#F7777F":
        return "#F33129"


def choose_colors(x, y):
    if largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and 100 < y < 250:
        color1, color2 = "#FF7900", "#F7E360"
        isColors = True
    elif largeur_Fenetre//2-350 < x < largeur_Fenetre//2-50 and 100 < y < 250:
        color1, color2 = "#F33129", "#0179C0"
        isColors = True
    elif largeur_Fenetre//2+50 < x < largeur_Fenetre//2+350 and 100 < y < 250:
        color1, color2 = "#2C6452", "#F7777F"
        isColors = True
    elif largeur_Fenetre//2+400 < x < largeur_Fenetre//2+700 and 100 < y < 250:
        color1, color2 = "#552B24", "#F33129"
        isColors = True
    elif largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and hauteur_Fenetre//2-75 < y < hauteur_Fenetre//2+75:
        color1, color2 = "#0179C0", "#65419C"
        isColors = True
    elif largeur_Fenetre//2+400 < x < largeur_Fenetre//2+700 and hauteur_Fenetre//2-75 < y < hauteur_Fenetre//2+75:
        color1, color2 = "#F7777F", "#0179C0"
        isColors = True
    elif largeur_Fenetre//2-700 < x < largeur_Fenetre//2-400 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#65419C", "#F7777F"
        isColors = True
    elif largeur_Fenetre//2-350 < x < largeur_Fenetre//2-50 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#2C6452", "#F7E360"
        isColors = True
    elif largeur_Fenetre//2+50 < x < largeur_Fenetre//2+350 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#F33129", "#F7E360"
        isColors = True
    elif largeur_Fenetre//2+400 < x < largeur_Fenetre//2+700 and hauteur_Fenetre-100 > y > hauteur_Fenetre-250:
        color1, color2 = "#552B24", "#F7777F"
        isColors = True
    elif (largeur_Fenetre-75 < x < largeur_Fenetre-25 and 25 < y < 75) or y == "Escape" or y == "KP_Escape":
        color1, color2 = "quit", "quit"
        isColors = True
    else:
        color1, color2 = None, None
        isColors = False
    return color1, color2, isColors