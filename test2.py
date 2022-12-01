# Imports ---------------------------------------------------------------------
from upemtk import *
from math import *
# Imports ---------------------------------------------------------------------
# Fonctions -------------------------------------------------------------------
def bouton():
    """"""
    rectangle(255, 255, 655, 355, couleur='red', epaisseur=3, tag='sablier'), texte(395, 285, "Sablier", tag='text_sablier')
    rectangle(755, 255, 1155, 355, couleur='yellow', epaisseur=3, tag='scores'), texte(905, 285, "Scores", tag='text_scores')
    rectangle(1255, 255, 1655, 355, couleur='green', epaisseur=3, tag='taille_des_boules'), texte(1315, 285, "Taille des Boules", tag='text_taille_des_boules')
    rectangle(255, 755, 655, 855, couleur='blue', epaisseur=3, tag='dynamique'), texte(290, 785, "Version Dynamique", tag='text_dynamique')
    rectangle(755, 755, 1155, 855, couleur='purple', epaisseur=3, tag='terminaison'), texte(855, 785, "Terminaison", tag='text_terminaison')
    rectangle(1255, 755, 1655, 855, couleur='black', epaisseur=3, tag='obstacles'), texte(1380, 785, "Obstacles", tag='text_obstacles')
    rectangle(755, 505, 1155, 605, couleur='black', epaisseur=3, tag='play'), texte(915, 535, "Start", tag='text_play')


def MENU(largeur_Fenetre, hauteur_Fenetre):
    """
    """
    """"""
    texte(largeur_Fenetre//2, 125, "Bataille des boules", ancrage="center", taille=30, tag='game')
    bouton()
    x, y, e = attente_clic()
    """"""
    if 255 < x < 655 and 255 < y < 355:
        V_sablier = True
        MENU(largeur_Fenetre, hauteur_Fenetre)
    elif 755 < x < 1155 and 255 < y < 355:
        V_scores = True
        MENU(largeur_Fenetre, hauteur_Fenetre)
    elif 1255 < x < 1655 and 255 < y < 355:
        V_taille = True
        MENU(largeur_Fenetre, hauteur_Fenetre)
    elif 255 < x < 655 and 755 < y < 855:
        MENU(largeur_Fenetre, hauteur_Fenetre)
    elif 755 < x < 1155 and 755 < y < 855:
        print("terminaison")
        MENU(largeur_Fenetre, hauteur_Fenetre)
    elif 1255 < x < 1655 and 755 < y < 855:
        print("obstacle")
        MENU(largeur_Fenetre, hauteur_Fenetre)
    elif 755 < x < 1155 and 505 < y < 605:
        efface('game')
        efface('sablier'), efface('text_sablier')
        efface('scores'), efface('text_scores')
        efface('taille_des_boules'), efface('text_taille_des_boules')
        efface('dynamique'), efface('text_dynamique')
        efface('terminaison'), efface('text_terminaison')
        efface('obstacles'), efface('text_obstacles')
        efface('play'), efface('text_play')
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bonne chance à vous deux !", ancrage="center", tag='jouer')#, image()
        attente_clic()
        efface('jouer')
    else:
        MENU(largeur_Fenetre, hauteur_Fenetre)
    """"""


# Fonctions des variantes -----------------------------------------------------
def SABLIER():
    """"""
    return None


def SCORES():
    """"""
    return None


def TAILLE_DES_BOULES():
    """"""
    return None


def VERSION_DYNAMIQUE():
    """"""
    return None


def TERMINAISON():
    """"Fonction  permettant à un joueur de décider une fois 
    par tour que le jeu se termine dans 5 tours 
    (le choix se propose un tour sur deux par joueur)."""
    ferme_fenetre()


def OBSTACLES():
    """"""
    return None
# Fonctions des variantes -----------------------------------------------------
def crayon(largeur_Fenetre, hauteur_Fenetre, color, compteur, tour):
    """
    """
    if color == 'red':
        txt = 'Tour du joueur ' + '1'
    elif color == 'blue':
        txt = 'Tour du joueur ' + '2'
    txt_tour = 'Tour : ' + str(compteur + 1) + '/' + str(tour)
    texte(largeur_Fenetre//2 - largeur_Fenetre//10, 0, txt, color, police='Dyuthi', taille=30, tag="joueur")
    texte(largeur_Fenetre//2 - largeur_Fenetre//10+100, hauteur_Fenetre-50, txt_tour, color, police='', tag="tour")


def gomme():
    """
    """
    efface("joueur")
    efface("tour")

# Vérification de la position des cercles ------------------------------------
def longueur(color, lst1, lst2, x, y, c):
    """Fonction de vérification des intersections 
    entre les cercles des adversaires. 
    Calcul utilisé : racine carré de ((Xb-Xa)^2 + (Yb-Ya)^2)
    """
    if lst1 != []:
        for lignes in range(len(lst1)):
            distance = sqrt((lst1[lignes][0]-x)**2 + (lst1[lignes][1]-y)**2) #cette formule calcule la disatance entre les deux coordonnées des points
            if distance <= 100: # Le 100 correspond au diamètre du cercle
                if color == 'blue':
                    color ='red'
                else:
                    color ='blue'
                efface(c)    #la boule est efffacée afin que le programme passe le tour de l'adversaire
                lst2.pop()   # Le dernier élément de la liste des positions du du joueur est effacé, soit la dernière position.
                return distance
            

def division(matrice, x1, y1):
    """Prend en paramètres:
    - Une matrice des coordonnées du cercle sous forme [absice,ordonnée,rayon] pour chaques lignes,
    - x1,y1 les coordonnées (absice,ordonnée) du cercle dont on recherche si l'on peut diviser le cercle
    renvoie True si on peut le diviser, renvoie False s'il ne peut pas"""
    for lignes in range(len(matrice)):
        d = sqrt((x1 - matrice[lignes][0])**2 + (y1 - matrice[lignes][1])**2)
        if d < matrice[lignes][2]:
            return True
    return False


def div_cercle(mat,x,y):
    """Prend en paramètres:
    - Une matrice des coordonnées du cercle sous forme [absice,ordonnée,rayon] pour chaques lignes,
    - x,y les coordonnées (absice,ordonnée) du cercle que l'on cherche à diviser en deux cercles
    renvoie c (position du cercle dans la matrice),
    rpc (Rayon du premier cercle),
    xgc,ygc (Coordonnées du deuxième cercle),
    rgc (Rayon du deuxième cercle)"""
    for lignes in range(len(mat)): # Stock les valeurs du cercle à diviser
        d = sqrt(( x - mat[lignes][0] )**2 + ( y - mat[lignes][1] )**2 )
        if d < mat[lignes][2]:
           xc = mat[lignes][0]
           yc = mat[lignes][1]
           rc = mat[lignes][2]
           c = lignes
           break
    rpc = rc - d # Calcul du rayon du petit cercle
    rgc = rc - rpc # Calcul du rayon du grand cercle
    dis = rgc+rpc
    dis2 = sqrt((rpc**2) + (dis**2))
    Sin = rpc / dis2
    Cos = dis / dis2
    if x >= xc and y >= yc:
        xgc = xc - (rpc*Cos)
        ygc = yc - (rpc*Sin)
    if x >= xc and y < yc:
        xgc = xc - (rpc*Cos)
        ygc = yc + (rpc*Sin)
    if x < xc and y >= yc:
        xgc = xc + (rpc*Cos)
        ygc = yc - (rpc*Sin)
    if x < xc and y < yc:
        xgc = xc + (rpc*Cos)
        ygc = yc + (rpc*Sin)
    return c, rpc,xgc,ygc,rgc
# Vérification de la position des cercles ------------------------------------
# Tour des joueurs -----------------------------------------------------------
def j1(color, lst_j1, liste_position_joueur, r):
    """Fonction du joueur 1 avec les différentes coordonnées listée du joueur et de tout les joueurs"""
    x1, y1, e1 = attente_clic()
    c = cercle(x1, y1, r, couleur=color, remplissage=color, tag="circle") #insère un cercle de couleur dans la fenêtre
    position_joueur = ([x1, y1, r]) # position_joueur = str(str(x1) + "," + str(y1)) #cette variable permet de  récupérer les coordonnées du centre des centres (exemple 292,157 (x1, y1) ceci sont les coordonnées cliqué par le joeur dans la fenêtre<))
    liste_position_joueur.append(position_joueur) #on rajoute les position des boules dans la liste_position_joueur.
    lst_j1.append(position_joueur)
    color = 'blue'   #changement de couleur
    return x1, y1, lst_j1, color, c, r


def j2(color, lst_j2, liste_position_joueur, r):
    """Fonction du joueur 2 avec les différentes coordonnées listée du joueur et de tout les joueurs"""
    x2, y2, e2 = attente_clic()
    c = cercle(x2, y2, r, couleur=color, remplissage=color, tag="circle")  
    color = 'red'
    position_joueur = ([x2, y2, r])# position_joueur = str(str(x2) + "," + str(y2))  #cette variable permet de  récupérer les coordonnées du centre des centres (exemple 292,157 (x1, y1) ceci sont les coordonnées cliqué par le joeur dans la fenêtre<)
    liste_position_joueur.append(position_joueur) #on rajoute les position des boules dans la liste_position_joueur.
    lst_j2.append(position_joueur)
    return x2, y2, lst_j2, color, c, r
# Tour des joueurs -----------------------------------------------------------
# Fonctions -------------------------------------------------------------------
# Fonction principale -----------------------------------------------
def GAME():
    """
    """
    tour = 3#int(input("Décidez du nombre de tour pour cette partie : "))
    lst_pos_j = [] #cette variable stockera au fur et à mesure les coordonnées de position_joueur.
    lst_j1 = []
    lst_j2 = []
    color = 'red' #couleur de la boule
    largeur_Fenetre = 1925
    hauteur_Fenetre = 1010
    r = 50
    cree_fenetre(largeur_Fenetre, hauteur_Fenetre)
    mise_a_jour()
    MENU(largeur_Fenetre, hauteur_Fenetre)
    for compteur in range(tour): # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        """appel des fontions"""
        crayon(largeur_Fenetre, hauteur_Fenetre, color, compteur, tour)
        x1, y1, lst_j1, color, c, r = j1(color, lst_j1, lst_pos_j, r)
        longueur(color, lst_j2, lst_j1, x1, y1, c)
        gomme()
        crayon(largeur_Fenetre, hauteur_Fenetre, color, compteur, tour)
        x2, y2, lst_j2, color, c, r = j2(color, lst_j2, lst_pos_j, r)
        longueur(color, lst_j1, lst_j2, x2, y2, c)
        gomme()
        print("Coordonnées des boules de tous les joueurs : ",lst_pos_j)
        # r += 1
    attente_clic()
    ferme_fenetre()
# Fonction principale ---------------------------------------------------------
# Programme principal ---------------------------------------------------------
if __name__ == '__main__':
    """
    """
    GAME()