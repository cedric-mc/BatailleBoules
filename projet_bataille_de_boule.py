######  import  #####

from upemtk import *
from time import *
######  import  #####

#####   fonction ###


if __name__=='__main__':
 cree_fenetre(400,400)
 compteur=0
while True:
    evenement = donne_evenement()
    type_ev = type_evenement(evenement)
    if type_ev == "ClicGauche": 
        cercle((clic_x(evenement)),(clic_y(evenement)), 50,couleur="red",remplissage="red") 
        txt1=  texte(300, 300, "Tour joueur 1 ", couleur="red",taille ="12")
        

    elif type_ev == "ClicDroit":
        efface(txt1)
        cercle((clic_x(evenement)),(clic_y(evenement)), 50,couleur="blue",remplissage="blue") 
        txt2=  texte(300, 313, "Tour joueur 2 ", couleur="blue",taille ="12")           
    mise_a_jour()    

ferme_fenetre()