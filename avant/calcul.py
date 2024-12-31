# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis la bibliothèque Python
from math import sqrt, dist, atan2, cos, sin


# ------------------------------ Importation depuis le dossier source
from upemtk import *


def intersection(dico, x, y, rayon):
    """Paramètres : 
    - dico : dictionnaire pour vérifier l'intersection entre les coordonnées et les autres cercles ;
    - x, y : coordonnées du cercle ;
    - rayon : type : int, rayon du cercle a posé.
    Fonction de vérification des intersections entre les cercles des adversaires. 
    Calcul utilisé : racine carré de ((Xb-Xa)^2 + (Yb-Ya)^2), peut être remplacer par dist((x1, x2), (y1, y2)).
    Retourne vrai s'il y a une intersection, sinon faux"""
    if dico:
        for x_cercle, y_cercle, rayon_ennemie in dico.values():
            distance = sqrt((x_cercle-x)**2 + (y_cercle-y)**2) # cette formule calcule la disatance entre les deux coordonnées des points
            if distance <= rayon + rayon_ennemie: # Le r*2 correspond au diamètre du cercle
                return True
    return False


def in_cercle(dico, x, y, color):
    """Paramètres : 
    - dico : dictionnaire de cercles ;
    - x, y : coordonnées du clic ;
    - color : couleur du cercle à divisé.
    Renvoie s'il y a eu division de cercle et le dictionnaire avec les deux nouveaux cercles.
    Cette fonction vérifie si le clique est à l'intérieur d'un cercle."""
    for cle, valeur in dico.items():
            distance = sqrt((valeur[0]-x)**2 + (valeur[1]-y)**2)
            if distance <= valeur[2]:
                dico = div_cercle(color, cle, x, y, valeur[0], valeur[1], valeur[2], dico)
                return True, dico
    return False, dico


def div_cercle(color, key, x1, y1, xc, yc, rc, dico):
    """Paramètres : 
    - color : couleur du cercle à diviser, type : str ;
    - key : identifiant du cercle ;
    - x1, y1 : coordonnées du clic.
    - xc, yc, rc : informations relatives au cercle du clic (coordonnées (x, y) et le rayon), type : int ou float ;
    - dico : dictionnaire contenant le cercle.
    Renvoie le dictionnaire avec les deux nouveaux cercles et celui du clic supprimer.
    Cette fonction permet de diviser le cercle du clic en deux, selon l'intersection, le cosinus, le sinus et la tangente."""
    efface(key)       #supprimer le cercle qui va être divisé en deux
    dico.pop(key)
    dx, dy = x1 - xc, y1 - yc  #la distance entre le clic et le centre du cercle
    angle = atan2(dy, dx)  #la tangente entre les distances 
    x2, y2 = x1 - rc * cos(angle), y1 - rc * sin(angle)  # les coordonnées du centre du nouveau cercle
    distance = sqrt(dx**2 + dy**2)  #la distance entre deux cercle
    rp = rc - distance  #rayon du petit cercle
    rg = rc - rp       #rayon du grand cercle
    c1 = cercle(x1, y1, rp, couleur=color, remplissage=color)  # représente le petit cercle
    c2 = cercle(x2, y2, rg, couleur=color, remplissage=color) # le grand cercle
    dico[c1] = [x1, y1, rp]
    dico[c2] = [x2, y2, rg]
    return dico


def calcul_aire(dico_j1, dico_j2):
    S1 = {(i, j) for x, y, r in dico_j1.values() for i in range(int(x-r), int(x+r)) for j in range(int(y-r), int(y+r)) if dist((i, j), (x, y)) <= r}
    S2 = {(i, j) for x, y, r in dico_j2.values() for i in range(int(x-r), int(x+r)) for j in range(int(y-r), int(y+r)) if dist((i, j), (x, y)) <= r}
    return S1, S2