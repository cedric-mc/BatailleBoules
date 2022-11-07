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
    
    #if position_joueur in liste_position_joueur:
        #pass
    #else:
    #for i in range(len(liste_position_joueur)):     #  pour chaque élément de la ligne de la matrice
            #for j in range(len(liste_position_joueur[0])):   #  pour chaque élément de la colonne de la matrice
                #if liste_position_joueur[i][j]  in [i][j] : #si l'élement de la ligne n'est pas dans la liste vide
                   #pass 
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
    txt=texte(300, 313, "Tour"+str(joueur), couleur="red",taille ="12")
            

ferme_fenetre()


    

#####   Principal i###