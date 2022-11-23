######  import  #####
from upemtk import *
from time import *
######  import  #####

#####   fonction ###




#####   fonction ###


#####   Principal i###
if __name__=='__main__':
    cree_fenetre(400,400)
    txt1=""
    txt2=""
    liste_position_joueur=[]
    position_joueur=""
    joueur=""
    while True:
        evenement = donne_evenement()
        type_ev = type_evenement(evenement)
        if type_ev == "ClicGauche":
            efface(txt2) 
            cercle((clic_x(evenement)),(clic_y(evenement)), 50,couleur="red",remplissage="red") #la boule du joueur 1 apparaît à l'emplacement du clic gauche 
            position_joueur=str(str(clic_x(evenement)) + "," + str(clic_y(evenement)) )
            print(position_joueur)
            liste_position_joueur.append(position_joueur)
            print(liste_position_joueur)
            joueur="bleu"

        
        elif type_ev == "ClicDroit":
            efface(txt1)
            cercle((clic_x(evenement)),(clic_y(evenement)), 50,couleur="blue",remplissage="blue") #la boule du joueur 2 apparait à l'emplacement du clic droite 
            position_joueur=str(str(clic_x(evenement)) + "," + str(clic_y(evenement)) )
            print(position_joueur)
            liste_position_joueur.append(position_joueur)
            print(liste_position_joueur)
            joueur="rouge"
        mise_a_jour()
    ferme_fenetre()