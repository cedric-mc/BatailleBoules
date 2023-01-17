Wilson Groevius
Cédric Mariya Constantine
SAE : Initiation au développement 
Projet: Bataille des boules
Rendu n°3




 — l’organisation du programme :
Pour organiser notre programme nous avons utilisé les logiciels suivant :
- Visual studio code : Pour programmer avec les extensions python ainsi que l’extension Extension Live Share pour travailler ensemble et en même temps.
- Discord : pour communiquer et partager nos écran respectif
- Mega : Pour transférer nos programme
- Github : Pour la mise en commun des programmes créés.
Le programme est constitué des importations de modules, des valeurs par défaut, des fonctions dont celles des variantes juste en dessous de celles du menu.




 — les choix techniques : 
Il est demandé dans le terminal, le nombre de tours à jouer (un tour représente 2 joueurs).
Utilisation de la boucle while afin de pouvoir définir le nombre de tours de chaque joueur (remplacement de la boucle for à while) mais également pour “manipuler” le nombre de tours (nécessaire à la variante Terminaison).
Utilisation de dictionnaire (les listes du premier rendu ont été remplacées par des dictionnaires)  pour les coordonnées des cercles (leurs centres) et leur rayon dans des listes. Ces listes sont chacune associées à une clé, l’identifiant des cercles.
Le dictionnaire est plus pratique car chaque boule est définie par la clé et à une valeur à lui. Il est donc plus utile que la liste pour l’organisation et la création des fonctions.




Utilisation de la formule de distance entre deux cercles : 
racine carrée(((Xb-Xa)^2 + (Yb-Ya)^2)).
Utilisation de formules pour créer les deux cercles, le petit et le grand lors de la division des boules : 
dx = x1 - xc 
dy = y1 - yc  La distance entre le clic et le centre du cercle
angle = atan2(dy, dx):  La tangente entre les distances 
x2 = x1-rc * cos(angle) 
y2 = y1-rc * sin(angle):les coordonnées du centre du nouveau cercle
rp = rc-distance: rayon du petit cercle
rg = rc -rp: rayon du grand cercle


Mise en place de variables pour régler la taille de fenêtre upemtk dans un objectif de manipulation de ces valeurs (tel que le placement du texte ou des boutons du menu initial).
Les modules utilisés sont : upemtk, math et random (uniquement pour randint), ctypes, string, time.
Module math, importation des fonctions  : sqrt, atan2, cos, sin, dist.
“sqrt” pour les calculs d’intersections
“atan2” pour le calcul de la tangente d’angle
“cos” et “sin” pour les calculs de divisions de boules (un vers deux).
“dist” pour calculer les intersections.
upemtk : Pour créer et afficher les cercles.
string : Utiliser pour différencier les lettres ascii, c’est-à-dire l’alphabet en minuscule et majuscule.
time : Utiliser pour la variante Sablier




Modification du menu :
- l'écran change de taille en fonction de l'écran utilisé avec le module ctypes.




— les éventuels problèmes rencontrés :
Nous avons eu des problèmes finalisés le projet, en effet je n’ai pas fait de bonus mais également pour leur difficulté.




— Le bonus et les variantes qui ont été implémentés :
Mise en place des boutons pour chacune des variantes, avec le fonctionnement de chacune des variantes : Sablier, Scores, Taille des Boules, Version Dynamique, Terminaison et Obstacles.
