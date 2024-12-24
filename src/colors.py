# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
import upemtk
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
    # ------------------------------ Choix des couleurs des joueurs première ligne
    rec1 = upemtk.rectangle(largeur_Fenetre//2-700, 100, largeur_Fenetre//2-550, 250, remplissage="#FF7900", epaisseur=0)
    rec2 = upemtk.rectangle(largeur_Fenetre // 2 - 550, 100, largeur_Fenetre // 2 - 400, 250, remplissage="#F7E360", epaisseur=0)
    rec3 = upemtk.rectangle(largeur_Fenetre // 2 - 350, 100, largeur_Fenetre // 2 - 200, 250, remplissage="#F33129", epaisseur=0)
    rec4 = upemtk.rectangle(largeur_Fenetre//2-200, 100, largeur_Fenetre//2-50, 250, remplissage="#0179C0", epaisseur=0)
    rec5 = upemtk.rectangle(largeur_Fenetre//2+50, 100, largeur_Fenetre//2+200, 250, remplissage="#2C6452", epaisseur=0)
    rec6 = upemtk.rectangle(largeur_Fenetre//2+200, 100, largeur_Fenetre//2+350, 250, remplissage="#F7777F", epaisseur=0)
    rec7 = upemtk.rectangle(largeur_Fenetre//2+400, 100, largeur_Fenetre//2+550, 250, remplissage="#552B24", epaisseur=0)
    rec8 = upemtk.rectangle(largeur_Fenetre//2+550, 100, largeur_Fenetre//2+700, 250, remplissage="#F33129", epaisseur=0)

    # ------------------------------ Choix des couleurs des joueurs deuxième ligne
    rec9 = upemtk.rectangle(largeur_Fenetre//2-700, hauteur_Fenetre//2-75, largeur_Fenetre//2-550, hauteur_Fenetre//2+75, remplissage="#0179C0", epaisseur=0)
    rec10 = upemtk.rectangle(largeur_Fenetre//2-550, hauteur_Fenetre//2-75, largeur_Fenetre//2-400, hauteur_Fenetre//2+75, remplissage="#65419C", epaisseur=0)
    rec11 = upemtk.rectangle(largeur_Fenetre//2+400, hauteur_Fenetre//2-75, largeur_Fenetre//2+550, hauteur_Fenetre//2+75, remplissage="#F7777F", epaisseur=0)
    rec12 = upemtk.rectangle(largeur_Fenetre//2+550, hauteur_Fenetre//2-75, largeur_Fenetre//2+700, hauteur_Fenetre//2+75, remplissage="#0179C0", epaisseur=0)

    # ------------------------------ Choix des couleurs des joueurs troisième ligne
    rec13 = upemtk.rectangle(largeur_Fenetre//2-700, hauteur_Fenetre-100, largeur_Fenetre//2-550, hauteur_Fenetre-250, remplissage="#65419C", epaisseur=0)
    rec14 = upemtk.rectangle(largeur_Fenetre//2-550, hauteur_Fenetre-100, largeur_Fenetre//2-400, hauteur_Fenetre-250, remplissage="#F7777F", epaisseur=0)
    rec15 = upemtk.rectangle(largeur_Fenetre//2-350, hauteur_Fenetre-100, largeur_Fenetre//2-200, hauteur_Fenetre-250, remplissage="#2C6452", epaisseur=0)
    rec16 = upemtk.rectangle(largeur_Fenetre//2-200, hauteur_Fenetre-100, largeur_Fenetre//2-50, hauteur_Fenetre-250, remplissage="#F7E360", epaisseur=0)
    rec17 = upemtk.rectangle(largeur_Fenetre//2+50, hauteur_Fenetre-100, largeur_Fenetre//2+200, hauteur_Fenetre-250, remplissage="#F33129", epaisseur=0)
    rec18 = upemtk.rectangle(largeur_Fenetre//2+200, hauteur_Fenetre-100, largeur_Fenetre//2+350, hauteur_Fenetre-250, remplissage="#F7E360", epaisseur=0)
    rec19 = upemtk.rectangle(largeur_Fenetre//2+400, hauteur_Fenetre-100, largeur_Fenetre//2+550, hauteur_Fenetre-250, remplissage="#552B24", epaisseur=0)
    rec20 = upemtk.rectangle(largeur_Fenetre//2+550, hauteur_Fenetre-100, largeur_Fenetre//2+700, hauteur_Fenetre-250, remplissage="#F7777F", epaisseur=0)

    # ------------------------------ Texte des couleurs des joueurs première ligne
    txt1 = upemtk.texte(largeur_Fenetre//2-625, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt2 = upemtk.texte(largeur_Fenetre//2-475, 175, "J2", taille=45, couleur="white", ancrage="center")
    txt3 = upemtk.texte(largeur_Fenetre//2-275, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt4 = upemtk.texte(largeur_Fenetre//2-125, 175, "J2", taille=45, couleur="white", ancrage="center")
    txt5 = upemtk.texte(largeur_Fenetre//2+125, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt6 = upemtk.texte(largeur_Fenetre//2+275, 175, "J2", taille=45, couleur="white", ancrage="center")
    txt7 = upemtk.texte(largeur_Fenetre//2+475, 175, "J1", taille=45, couleur="white", ancrage="center")
    txt8 = upemtk.texte(largeur_Fenetre//2+625, 175, "J2", taille=45, couleur="white", ancrage="center")

    # ------------------------------ Texte des couleurs des joueurs deuxième ligne
    txt9 = upemtk.texte(largeur_Fenetre//2-625, hauteur_Fenetre//2, "J1", taille=45, couleur="white", ancrage="center")
    txt10 = upemtk.texte(largeur_Fenetre//2-475, hauteur_Fenetre//2, "J2", taille=45, couleur="white", ancrage="center")
    txt11 = upemtk.texte(largeur_Fenetre//2+475, hauteur_Fenetre//2, "J1", taille=45, couleur="white", ancrage="center")
    txt12 = upemtk.texte(largeur_Fenetre//2+625, hauteur_Fenetre//2, "J2", taille=45, couleur="white", ancrage="center")

    # ------------------------------ Texte des couleurs des joueurs troisième ligne
    txt13 = upemtk.texte(largeur_Fenetre//2-625, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt14 = upemtk.texte(largeur_Fenetre//2-475, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    txt15 = upemtk.texte(largeur_Fenetre//2-275, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt16 = upemtk.texte(largeur_Fenetre//2-125, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    txt17 = upemtk.texte(largeur_Fenetre//2+125, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt18 = upemtk.texte(largeur_Fenetre//2+275, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    txt19 = upemtk.texte(largeur_Fenetre//2+475, hauteur_Fenetre-175, "J1", taille=45, couleur="white", ancrage="center")
    txt20 = upemtk.texte(largeur_Fenetre//2+625, hauteur_Fenetre-175, "J2", taille=45, couleur="white", ancrage="center")
    
    color1, color2 = menu.choose_colors()
    if color1 == "quit" or color2 == "quit":
        return [color1, color2]
    # Efface les rectangles de la première ligne
    upemtk.efface(rec1), upemtk.efface(rec2), upemtk.efface(rec3), upemtk.efface(rec4), upemtk.efface(rec5), upemtk.efface(rec6), upemtk.efface(rec7), upemtk.efface(rec8)
    upemtk.efface(rec9), upemtk.efface(rec10), upemtk.efface(rec11), upemtk.efface(rec12) # Efface les rectangles de la deuxième ligne
    # Efface les rectangles de la troisième ligne
    upemtk.efface(rec13), upemtk.efface(rec14), upemtk.efface(rec15), upemtk.efface(rec16), upemtk.efface(rec17), upemtk.efface(rec18), upemtk.efface(rec19), upemtk.efface(rec20)
    # Efface les textes de la première ligne
    upemtk.efface(txt1), upemtk.efface(txt2), upemtk.efface(txt3), upemtk.efface(txt4), upemtk.efface(txt5), upemtk.efface(txt6), upemtk.efface(txt7), upemtk.efface(txt8)
    upemtk.efface(txt9), upemtk.efface(txt10), upemtk.efface(txt11), upemtk.efface(txt12) # Efface les textes de la deuxième ligne
    # Efface les textes de la troisième ligne
    upemtk.efface(txt13), upemtk.efface(txt14), upemtk.efface(txt15), upemtk.efface(txt16), upemtk.efface(txt17), upemtk.efface(txt18), upemtk.efface(txt19), upemtk.efface(txt20)
    return [color1, color2]


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