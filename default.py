# Programmeurs : Cédric Mariya Constantine et Wilson Groevius
# ------------------------------ Importation depuis la bibliothèque Python
import ctypes
import platform


# Déclaration des différentes variables utilisées à travers tout le programme
if platform.system() == 'Windows':
    largeur_Fenetre, hauteur_Fenetre = ctypes.windll.user32.GetSystemMetrics(0)-10, ctypes.windll.user32.GetSystemMetrics(1)-50 # 1650, 800 # 1850, 1000
elif platform.system() == 'Linux':
    largeur_Fenetre, hauteur_Fenetre = 1850, 1000
elif platform.system() == 'Darwin':
    largeur_Fenetre, hauteur_Fenetre = 1850, 1000
b_gauche_x1, b_gauche_x2 = largeur_Fenetre//2-700, largeur_Fenetre//2-400
b_droit_x1, b_droit_x2 = largeur_Fenetre//2+400, largeur_Fenetre//2+700
b1_y1, b1_y2 = hauteur_Fenetre//2-200, hauteur_Fenetre//2-100
b3_y1, b3_y2 = hauteur_Fenetre//2+100, hauteur_Fenetre//2+200
b4_y1, b4_y2 = hauteur_Fenetre//2-200, hauteur_Fenetre//2-100
b6_y1, b6_y2 = hauteur_Fenetre//2+100, hauteur_Fenetre//2+200
b_milieu_y1, b_milieu_y2 = hauteur_Fenetre//2-50, hauteur_Fenetre//2+50
txt_gauche_x, txt_droite_x = largeur_Fenetre//2-550, largeur_Fenetre//2+550
txt_y1, txt_y2, txt_y3 = hauteur_Fenetre//2-150, hauteur_Fenetre//2, hauteur_Fenetre//2+150
caracteres_speciaux = ['ampersand', 'eacute', 'quotedbl', 'apostrophe', 'parenleft', 'minus', 'egrave', 'underscore', 'ccedilla', 'agrave', 'parenright', 'equal']