from upemtk import *
x = 0
cree_fenetre(400,400)
while True:
    efface_tout()
    evenement = donne_evenement()
    type_ev = type_evenement(evenement)
    if type_ev == "ClicDroit":
        cercle(50, 50, 50, couleur='red', remplissage='red', epaisseur='1')
        attente_clic()
    elif type_ev == "ClicGauche": 
        cercle(150, 150, 50, couleur='blue', remplissage='blue', epaisseur='1')
        attente_clic()
    mise_a_jour()
attente_clic()
ferme_fenetre()