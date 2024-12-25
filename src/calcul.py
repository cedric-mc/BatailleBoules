# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation
from math import sqrt, dist, atan2, cos, sin
import upemtk


def intersection(dico, x, y, rayon):
    """Cette fonction permet de vérifier l'intersection entre les cercles des adversaires
    avec la formule de la distance entre deux points (racine carrée de ((Xb-Xa)^2 + (Yb-Ya)^2)) soit dist((x1, x2), (y1, y2)).

    Args:
        dico (dict): Dictionnaire pour vérifier l'intersection entre les coordonnées et les autres cercles.
        x (int): Coordonnée x du cercle.
        y (int): Coordonnée y du cercle.
        rayon (int): Rayon du cercle à poser.

    Returns:
        bool: Retourne vrai s'il y a une intersection, sinon faux.
    """
    if dico:
        for x_cercle, y_cercle, rayon_ennemie in dico.values():
            distance = sqrt((x_cercle-x)**2 + (y_cercle-y)**2) # cette formule calcule la distance entre les deux coordonnées des points
            if distance <= rayon + rayon_ennemie: # Le r*2 correspond au diamètre du cercle
                return True
    return False


def in_cercle(dico, x, y, color):
    """Cette fonction permet de vérifier si le clic est à l'intérieur d'un cercle et de le diviser en deux si c'est le cas.
    On utilise la formule de la distance entre deux points (racine carrée de ((Xb-Xa)^2 + (Yb-Ya)^2)) soit dist((x1, x2), (y1, y2)).

    Args:
        dico (dict): Dictionnaire de cercles.
        x (int): Coordonnée x du clic.
        y (int): Coordonnée y du clic.
        color (str): Couleur du cercle à diviser.

    Returns:
        _type_ (bool): Retourne vrai s'il y a une intersection, sinon faux.
        dict: Retourne le dictionnaire avec les deux nouveaux cercles et celui du clic supprimé.
    """
    for circle_id, circle_data in dico.items():
            distance = sqrt((circle_data[0]-x)**2 + (circle_data[1]-y)**2)
            if distance <= circle_data[2]:
                dico = div_cercle(color, circle_id, x, y, circle_data[0], circle_data[1], circle_data[2], dico)
                return True, dico
    return False, dico


def div_cercle(color, key, x1, y1, xc, yc, rc, dico):
    """Cette fonction permet de diviser un cercle en deux en fonction de l'intersection, du cosinus, du sinus et de la tangente.

    Args:
        color (str): Couleur du cercle à diviser.
        key (int): Identifiant du cercle.
        x1 (int): Coordonnée x du clic.
        y1 (int): Coordonnée y du clic.
        xc (int): Coordonnée x du centre du cercle.
        yc (int): Coordonnée y du centre du cercle.
        rc (int): Rayon du cercle.
        dico (dict): Dictionnaire contenant le cercle.

    Returns:
        dico (dict) : Retourne le dictionnaire avec les deux nouveaux cercles et celui du clic supprimé.
    """
    upemtk.efface(key) # Suppression du cercle qui va être divisé en deux
    dico.pop(key)
    dx, dy = x1 - xc, y1 - yc # La distance entre le clic et le centre du cercle
    angle = atan2(dy, dx) # La tangente entre les distances
    x2, y2 = x1 - rc * cos(angle), y1 - rc * sin(angle) # Les coordonnées du centre du nouveau cercle
    distance = sqrt(dx**2 + dy**2) # La distance entre deux cercle
    rp = rc - distance # Rayon du petit cercle
    rg = rc - rp # Rayon du grand cercle
    c1 = upemtk.cercle(x1, y1, rp, couleur=color, remplissage=color) # Représente le petit cercle
    c2 = upemtk.cercle(x2, y2, rg, couleur=color, remplissage=color) # Le grand cercle
    dico[c1] = [x1, y1, rp]
    dico[c2] = [x2, y2, rg]
    return dico


def calcul_aire(dico_j1, dico_j2):
    """Cette fonction permet de calculer l'aire des cercles des deux joueurs en fonction de leurs coordonnées et de leurs rayons.

    Args:
        dico_j1 (dict): Dictionnaire des cercles du joueur 1.
        dico_j2 (dict): Dictionnaire des cercles du joueur 2.

    Returns:
        _type_ (set): Retourne un ensemble de coordonnées du joueur 1.
        _type_ (set): Retourne un ensemble de coordonnées du joueur 2.
    """
    def inter_calcul_aire(dico):
        return {(i, j) for x, y, r in dico.values() for i in range(int(x-r), int(x+r)) for j in range(int(y-r), int(y+r)) if dist((i, j), (x, y)) <= r}
    return inter_calcul_aire(dico_j1), inter_calcul_aire(dico_j2)
