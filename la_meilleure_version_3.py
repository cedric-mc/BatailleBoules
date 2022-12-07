# Imports ---------------------------------------------------------------------
from upemtk import *
import math
import random
# Imports ---------------------------------------------------------------------
# Fonctions -------------------------------------------------------------------
def bouton_1(V_sablier, largeur_Fenetre, hauteur_Fenetre):
    if V_sablier == False:
        V_sablier = True
        efface('sablier'), efface('text_sablier')
        rectangle(largeur_Fenetre//4-300, hauteur_Fenetre//4-50, largeur_Fenetre//4+100, hauteur_Fenetre//4+50, couleur='black', remplissage='brown', epaisseur=3, tag='sablier')
        texte(largeur_Fenetre//4-160, hauteur_Fenetre//4-25, "Sablier", couleur='white', tag='text_sablier')
    else:
        V_sablier = False
        efface('sablier'), efface('text_sablier')
        rectangle(largeur_Fenetre//4-300, hauteur_Fenetre//4-50, largeur_Fenetre//4+100, hauteur_Fenetre//4+50, couleur='brown', epaisseur=3, tag='sablier')
        texte(largeur_Fenetre//4-160, hauteur_Fenetre//4-25, "Sablier", couleur='brown', tag='text_sablier')
    return V_sablier


def bouton_2(V_scores, largeur_Fenetre, hauteur_Fenetre):
    if V_scores == False:
        V_scores = True
        efface('scores'), efface('text_scores')
        rectangle(largeur_Fenetre//4+250, hauteur_Fenetre//4-50, largeur_Fenetre//4+650, hauteur_Fenetre//4+50, couleur='white', remplissage='orange', epaisseur=3, tag='scores')
        texte(largeur_Fenetre//4+400, hauteur_Fenetre//4-25, "Scores", couleur='black', tag='text_scores')
    else:
        V_scores = False
        efface('scores'), efface('text_scores')
        rectangle(largeur_Fenetre//4+250, hauteur_Fenetre//4-50, largeur_Fenetre//4+650, hauteur_Fenetre//4+50, couleur='orange', epaisseur=3, tag='scores')
        texte(largeur_Fenetre//4+400, hauteur_Fenetre//4-25, "Scores", couleur='orange', tag='text_scores')
    return V_scores


def bouton_3(V_taille, largeur_Fenetre, hauteur_Fenetre):
    if V_taille == False:
        V_taille = True
        efface('taille_des_boules'), efface('text_taille_des_boules')
        rectangle(largeur_Fenetre//4+800, hauteur_Fenetre//4-50, largeur_Fenetre//4+1200, hauteur_Fenetre//4+50, couleur='black', remplissage='green', epaisseur=3, tag='taille_des_boules')
        texte(largeur_Fenetre//4+850, hauteur_Fenetre//4-25, "Taille des Boules", couleur='white', tag='text_taille_des_boules')
    else:
        V_taille = False
        efface('taille_des_boules'), efface('text_taille_des_boules')
        rectangle(largeur_Fenetre//4+800, hauteur_Fenetre//4-50, largeur_Fenetre//4+1200, hauteur_Fenetre//4+50, couleur='green', epaisseur=3, tag='taille_des_boules')
        texte(largeur_Fenetre//4+850, hauteur_Fenetre//4-25, "Taille des Boules", couleur='green', tag='text_taille_des_boules')
    return V_taille


def bouton_4(V_dynamique, largeur_Fenetre, hauteur_Fenetre):
    if V_dynamique == False:
        V_dynamique = True
        efface('dynamique'), efface('text_dynamique')
        rectangle(largeur_Fenetre//4-300, hauteur_Fenetre//4+500, largeur_Fenetre//4+100, hauteur_Fenetre//4+600, couleur='white', remplissage='turquoise', epaisseur=3, tag='dynamique')
        texte(largeur_Fenetre//4-265, hauteur_Fenetre//4+525, "Version Dynamique", couleur='black', tag='text_dynamique')
    else:
        V_dynamique = False
        efface('dynamique'), efface('text_dynamique')
        rectangle(largeur_Fenetre//4-300, hauteur_Fenetre//4+500, largeur_Fenetre//4+100, hauteur_Fenetre//4+600, couleur='turquoise', epaisseur=3, tag='dynamique')
        texte(largeur_Fenetre//4-265, hauteur_Fenetre//4+525, "Version Dynamique", couleur='turquoise', tag='text_dynamique')
    return V_dynamique


def bouton_5(V_terminaison, largeur_Fenetre, hauteur_Fenetre):
    if V_terminaison == False:
        V_terminaison = True
        efface('terminaison'), efface('text_terminaison')
        rectangle(largeur_Fenetre//4+250, hauteur_Fenetre//4+500, largeur_Fenetre//4+650, hauteur_Fenetre//4+600, couleur='black', remplissage='purple', epaisseur=3, tag='terminaison')
        texte(largeur_Fenetre//4+350, hauteur_Fenetre//4+525, "Terminaison", couleur='white', tag='text_terminaison')
    else:
        V_terminaison = False
        efface('terminaison'), efface('text_terminaison')
        rectangle(largeur_Fenetre//4+250, hauteur_Fenetre//4+500, largeur_Fenetre//4+650, hauteur_Fenetre//4+600, couleur='purple', epaisseur=3, tag='terminaison')
        texte(largeur_Fenetre//4+350, hauteur_Fenetre//4+525, "Terminaison", couleur='purple', tag='text_terminaison')
    return V_terminaison


def bouton_6(V_obstacle, largeur_Fenetre, hauteur_Fenetre):
    if V_obstacle == False:
        V_obstacle = True
        efface('obstacles'), efface('text_obstacles')
        rectangle(largeur_Fenetre//4+800, hauteur_Fenetre//4+500, largeur_Fenetre//4+1200, hauteur_Fenetre//4+600, couleur='white', remplissage='magenta', epaisseur=3, tag='obstacles') # ou grey
        texte(largeur_Fenetre//4+925, hauteur_Fenetre//4+525, "Obstacles", couleur='black', tag='text_obstacles') # ou grey
    else:
        V_obstacle = False
        efface('obstacles'), efface('text_obstacles')
        rectangle(largeur_Fenetre//4+800, hauteur_Fenetre//4+500, largeur_Fenetre//4+1200, hauteur_Fenetre//4+600, couleur='magenta', epaisseur=3, tag='obstacles') # ou grey
        texte(largeur_Fenetre//4+925, hauteur_Fenetre//4+525, "Obstacles", couleur='magenta', tag='text_obstacles') # ou grey
    return V_obstacle


def boutons(largeur_Fenetre, hauteur_Fenetre):
    '''La fonction prend en paramètres la largeur et la hauteur de la fenêtre.'''
    """Création des boutons, ainsi que leur contenu (texte)."""
    pass


def MENU(largeur_Fenetre, hauteur_Fenetre, V_menu):
    """Initialisation du Menu, avec 7 boutons (pour utiliser les 6 Alternatives et pour démarrer le jeu)."""
    texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bienvenue !", ancrage="center", tag='jouer')
    attente_clic()
    efface('jouer')
    """"""
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = False, False, False, False, False, False
    # Initialisation des coordonnées de chaque coins des rectangles / boutons en fonction de la largeur et de la hauteur de la fenêtre, la première ligne d'intialisation correspond au quatre point y.
    rec_haut_y1, rec_haut_y2, rec_bas_y1, rec_bas_y2 = hauteur_Fenetre//4-50, hauteur_Fenetre//4+50, hauteur_Fenetre//4+500, hauteur_Fenetre//4+600
    rec_b1_x1, rec_b1_x2 = largeur_Fenetre//4-300, largeur_Fenetre//4+100
    rec_b2_x1, rec_b2_x2 = largeur_Fenetre//4+250, largeur_Fenetre//4+650
    rec_b3_x1, rec_b3_x2 = largeur_Fenetre//4+800, largeur_Fenetre//4+1200
    rec_b4_x1, rec_b4_x2 = largeur_Fenetre//4-300, largeur_Fenetre//4+100
    rec_b5_x1, rec_b5_x2 = largeur_Fenetre//4+250, largeur_Fenetre//4+650
    rec_b6_x1, rec_b6_x2 = largeur_Fenetre//4+800, largeur_Fenetre//4+1200

    texte(largeur_Fenetre//2, 125, "Bataille des boules", ancrage="center", taille=30, tag='game')
    
    rectangle(rec_b1_x1, rec_haut_y1, rec_b1_x2, rec_haut_y2, couleur='brown', epaisseur=3, tag='sablier')
    texte(largeur_Fenetre//4-160, hauteur_Fenetre//4-25, "Sablier", couleur='brown', tag='text_sablier')

    rectangle(rec_b2_x1, rec_haut_y1, rec_b2_x2, rec_haut_y2, couleur='orange', epaisseur=3, tag='scores')
    texte(largeur_Fenetre//4+400, hauteur_Fenetre//4-25, "Scores", couleur='orange', tag='text_scores')

    rectangle(rec_b3_x1, rec_haut_y1, rec_b3_x2, rec_haut_y2, couleur='green', epaisseur=3, tag='taille_des_boules')
    texte(largeur_Fenetre//4+850, hauteur_Fenetre//4-25, "Taille des Boules", couleur='green', tag='text_taille_des_boules')

    rectangle(rec_b4_x1, rec_bas_y1, rec_b4_x2, rec_bas_y2, couleur='turquoise', epaisseur=3, tag='dynamique')
    texte(largeur_Fenetre//4-265, hauteur_Fenetre//4+525, "Version Dynamique", couleur='turquoise', tag='text_dynamique')

    rectangle(rec_b5_x1, rec_bas_y1, rec_b5_x2, rec_bas_y2, couleur='purple', epaisseur=3, tag='terminaison')
    texte(largeur_Fenetre//4+350, hauteur_Fenetre//4+525, "Terminaison", couleur='purple', tag='text_terminaison')

    rectangle(rec_b6_x1, rec_bas_y1, rec_b6_x2, rec_bas_y2, couleur='magenta', epaisseur=3, tag='obstacles')
    texte(largeur_Fenetre//4+925, hauteur_Fenetre//4+525, "Obstacles", couleur='magenta', tag='text_obstacles')
    
    rectangle(largeur_Fenetre//2-180, hauteur_Fenetre//2-50, largeur_Fenetre//2+120, hauteur_Fenetre//2+50, couleur='white', remplissage='black', epaisseur=3, tag='play')
    texte(largeur_Fenetre//2-25, hauteur_Fenetre//2, "Start", couleur='white', ancrage='center', tag='text_play')
    """"""
    while V_menu != True:
        x, y, e = attente_clic()
        if largeur_Fenetre//4-300 < x < largeur_Fenetre//4+100 and hauteur_Fenetre//4-50 < y < hauteur_Fenetre//4+50:
            V_sablier = bouton_1(V_sablier, largeur_Fenetre, hauteur_Fenetre)
        elif largeur_Fenetre//4+250 < x < largeur_Fenetre//4+650 and hauteur_Fenetre//4-50 < y < hauteur_Fenetre//4+50:
            V_scores = bouton_2(V_scores, largeur_Fenetre, hauteur_Fenetre)
        elif largeur_Fenetre//4+800 < x < largeur_Fenetre//4+1200 and hauteur_Fenetre//4-50 < y < hauteur_Fenetre//4+50:
            V_taille = bouton_3(V_taille, largeur_Fenetre, hauteur_Fenetre)
        elif largeur_Fenetre//4-300 < x < largeur_Fenetre//4+100 and hauteur_Fenetre//4+500 < y < hauteur_Fenetre//4+600:
            V_dynamique = bouton_4(V_dynamique, largeur_Fenetre, hauteur_Fenetre)
        elif largeur_Fenetre//4+250 < x < largeur_Fenetre//4+650 and hauteur_Fenetre//4+500 < y < hauteur_Fenetre//4+600:
            V_terminaison = bouton_5(V_terminaison, largeur_Fenetre, hauteur_Fenetre)
        elif largeur_Fenetre//4+800 < x < largeur_Fenetre//4+1200 and hauteur_Fenetre//4+500 < y < hauteur_Fenetre//4+600:
            V_obstacle = bouton_6(V_obstacle, largeur_Fenetre, hauteur_Fenetre)
        elif largeur_Fenetre//2-200 < x < largeur_Fenetre//2+100 and hauteur_Fenetre//2-50 < y < hauteur_Fenetre//2+50:
            V_menu = True
            efface('fond')
            efface('game')
            efface('sablier'), efface('text_sablier')
            efface('scores'), efface('text_scores')
            efface('taille_des_boules'), efface('text_taille_des_boules')
            efface('dynamique'), efface('text_dynamique')
            efface('terminaison'), efface('text_terminaison')
            efface('obstacles'), efface('text_obstacles')
            efface('play'), efface('text_play')
            texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Bonne chance à vous !", ancrage="center", tag='jouer')
            attente_clic()
            efface('jouer')
            return V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle

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


def TERMINAISON(V_terminaison, largeur_Fenetre, hauteur_Fenetre):
    """Fonction  permettant à un joueur de décider une fois 
    par tour que le jeu se termine dans 5 tours 
    (le choix se propose un tour sur deux par joueur).
    L'alternative ne fonctionnera qu'en cas où tour > 5 (soit le nombre de tours restant excédant 5)."""
    if V_terminaison == True:
        texte(largeur_Fenetre//2, hauteur_Fenetre//2, "Voulez-vous arrêter la partie dans 5 tours ?", couleur='black', ancrage='center')
        rectangle(largeur_Fenetre//2-200, hauteur_Fenetre//3+50, largeur_Fenetre//2-50, hauteur_Fenetre//3+100)
        return False


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
    texte(largeur_Fenetre//2 - largeur_Fenetre//10, 0, txt, color, police='Z003', taille=30, tag="joueur") # police : donne l'impression d'avoir été écrit par plume
    texte(largeur_Fenetre//2 - largeur_Fenetre//10+100, hauteur_Fenetre-50, txt_tour, color, police='DejaVu Serif', tag="tour")


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
            distance = math.sqrt((lst1[lignes][0]-x)**2 + (lst1[lignes][1]-y)**2) #cette formule calcule la disatance entre les deux coordonnées des points
            if distance <= 100: # Le 100 correspond au diamètre du cercle
                if color == 'blue':
                    color ='red'
                else:
                    color ='blue'
                efface(c)    #la boule est efffacée afin que le programme passe le tour de l'adversaire
                lst2.pop()   # Le dernier élément de la liste des positions du du joueur est effacé, soit la dernière position.
                return distance


def div_cercle(color, x, y, matrice):
    pass
# def division(matrice, x1, y1):
#     """Prend en paramètres:
#     - Une matrice des coordonnées du cercle sous forme [absice,ordonnée,rayon] pour chaques lignes,
#     - x1,y1 les coordonnées (absice,ordonnée) du cercle dont on recherche si l'on peut diviser le cercle
#     renvoie True si on peut le diviser, renvoie False s'il ne peut pas"""
#     for lignes in range(len(matrice)):
#         d = sqrt((x1 - matrice[lignes][0])**2 + (y1 - matrice[lignes][1])**2)
#         if d < matrice[lignes][2]:
#             return True
#     return False


# def div_cercle(mat,x,y):
#     """Prend en paramètres:
#     - Une matrice des coordonnées du cercle sous forme [absice,ordonnée,rayon] pour chaques lignes,
#     - x,y les coordonnées (absice,ordonnée) du cercle que l'on cherche à diviser en deux cercles
#     renvoie c (position du cercle dans la matrice),
#     rpc (Rayon du premier cercle),
#     xgc,ygc (Coordonnées du deuxième cercle),
#     rgc (Rayon du deuxième cercle)"""
#     for lignes in range(len(mat)): # Stock les valeurs du cercle à diviser
#         d = sqrt(( x - mat[lignes][0] )**2 + ( y - mat[lignes][1] )**2 )
#         if d < mat[lignes][2]:
#            xc = mat[lignes][0]
#            yc = mat[lignes][1]
#            rc = mat[lignes][2]
#            c = lignes
#            break
#     rpc = rc - d # Calcul du rayon du petit cercle
#     rgc = rc - rpc # Calcul du rayon du grand cercle
#     dis = rgc+rpc
#     dis2 = sqrt((rpc**2) + (dis**2))
#     Sin = rpc / dis2
#     Cos = dis / dis2
#     if x >= xc and y >= yc:
#         xgc = xc - (rpc*Cos)
#         ygc = yc - (rpc*Sin)
#     if x >= xc and y < yc:
#         xgc = xc - (rpc*Cos)
#         ygc = yc + (rpc*Sin)
#     if x < xc and y >= yc:
#         xgc = xc + (rpc*Cos)
#         ygc = yc - (rpc*Sin)
#     if x < xc and y < yc:
#         xgc = xc + (rpc*Cos)
#         ygc = yc + (rpc*Sin)
#     return c, rpc,xgc,ygc,rgc
# Vérification de la position des cercles ------------------------------------
# Tour des joueurs -----------------------------------------------------------
def j1(largeur_Fenetre, hauteur_Fenetre, color, lst_j1, liste_position_joueur, r, compteur, tour, piece, V_terminaison):
    """Fonction du joueur 1 avec les différentes coordonnées listée du joueur et de tout les joueurs"""
    x1, y1, e1 = attente_clic()
    if piece == True:
        if tour > 5 and compteur < tour-5:
            V_terminaison = TERMINAISON(V_terminaison, largeur_Fenetre, hauteur_Fenetre)
    c = cercle(x1, y1, r, couleur=color, remplissage=color, tag="circle") #insère un cercle de couleur dans la fenêtre
    position_joueur = ([x1, y1, r, c]) # position_joueur = str(str(x1) + "," + str(y1)) # cette variable permet de  récupérer les coordonnées du centre des centres (exemple 292,157 (x1, y1) ceci sont les coordonnées cliqué par le joeur dans la fenêtre<))
    liste_position_joueur.append(position_joueur) #on rajoute les position des boules dans la liste_position_joueur.
    lst_j1.append(position_joueur)
    color = 'blue' #changement de couleur
    return x1, y1, lst_j1, color, c, r, piece, V_terminaison


def j2(largeur_Fenetre, hauteur_Fenetre, color, lst_j2, liste_position_joueur, r, compteur, tour, piece, V_terminaison):
    """Fonction du joueur 2 avec les différentes coordonnées listée du joueur et de tout les joueurs"""
    x2, y2, e2 = attente_clic()
    if piece == False:
        if tour > 5 and compteur < tour-5:
            TERMINAISON(largeur_Fenetre, hauteur_Fenetre, V_terminaison)
    c = cercle(x2, y2, r, couleur=color, remplissage=color, tag="circle")
    position_joueur = ([x2, y2, r, c])# position_joueur = str(str(x2) + "," + str(y2))  #cette variable permet de  récupérer les coordonnées du centre des centres (exemple 292,157 (x1, y1) ceci sont les coordonnées cliqué par le joeur dans la fenêtre<)
    liste_position_joueur.append(position_joueur) #on rajoute les position des boules dans la liste_position_joueur.
    lst_j2.append(position_joueur)
    color = 'red'
    return x2, y2, lst_j2, color, c, r, piece, V_terminaison
# Tour des joueurs -----------------------------------------------------------
# Fonctions -------------------------------------------------------------------
# Fonction principale -----------------------------------------------
def GAME():
    """
    """
    tour = 3 # int(input("Décidez du nombre de tour pour cette partie : "))
    lst_pos_j = [] #cette variable stockera au fur et à mesure les coordonnées de position_joueur.
    lst_j1 = []
    lst_j2 = []
    color = 'red' #couleur de la boule
    largeur_Fenetre = 1925
    hauteur_Fenetre = 1010
    r = 50
    compteur = 0
    coin = (True, False) # Pair ou False pour impair
    cree_fenetre(largeur_Fenetre, hauteur_Fenetre)
    V_menu = False
    V_sablier, V_scores, V_taille, V_dynamique, V_terminaison, V_obstacle = MENU(largeur_Fenetre, hauteur_Fenetre, V_menu)
    while compteur < tour: # permet de répéter la fonction le nombre de fois souhaiter pour définir le nombre de tour
        """appel des fontions"""
        piece = random.choice(coin)
        crayon(largeur_Fenetre, hauteur_Fenetre, color, compteur, tour)
        x1, y1, lst_j1, color, c, r, piece, V_terminaison = j1(largeur_Fenetre, hauteur_Fenetre, color, lst_j1, lst_pos_j, r, compteur, tour, piece, V_terminaison)
        longueur(color, lst_j2, lst_j1, x1, y1, c)
        gomme()
        crayon(largeur_Fenetre, hauteur_Fenetre, color, compteur, tour)
        x2, y2, lst_j2, color, c, r, piece, V_terminaison = j2(largeur_Fenetre, hauteur_Fenetre, color, lst_j2, lst_pos_j, r, compteur, tour, piece, V_terminaison)
        longueur(color, lst_j1, lst_j2, x2, y2, c)
        gomme()
        print("Coordonnées des boules de tous les joueurs : ", lst_pos_j)
        compteur += 1
    attente_clic()
    ferme_fenetre()
# Fonction principale ---------------------------------------------------------
# Programme principal ---------------------------------------------------------
if __name__ == '__main__':
    """
    """
    GAME()