# Projet : Bataille des boules

Le but de ce projet est de réaliser un jeu de placement de boules. Chaque utilisateur joue avec une couleur. Le but du jeu est d'occuper la plus grande aire coloriée avec sa couleur. Les joueurs contrôlent la souris chacun à leur tour, et on décide à l'avance du nombre de tours.

## Le programme à réaliser : le jeu de base

Dans sa version de base, l'aire de jeu est initialement vide. Le jeu montre à qui est le tour. À la fin, il doit indiquer qui a gagné. Voici les règles du jeu :

1. Les intérieurs de deux boules de couleurs différentes ne peuvent pas s'intersecter. Si un joueur essaye d'inclure une boule qui intersecte l'intérieur d'une boule de la couleur opposée, rien ne se passe et il perd son tour.
2. Si un joueur clique dans l'intérieur d'une boule de l'adversaire, il la transforme en deux boules de même couleur plus petites.

## Variantes

Dans un deuxième temps, vous devrez fournir une version du jeu avec un menu initial qui permet d'utiliser une combinaison des alternatives suivantes :

1. **Sablier** : chaque joueur a un temps prédéterminé pour jouer à chaque tour; s'il ne réagit pas à temps, il perd son tour.
2. **Scores** : un joueur peut vérifier quelle aire ses boules totalisent à chaque instant en appuyant sur la touche 's'.
3. **Taille des boules** : à chaque tour, on demande au joueur le rayon de la boule qu'il veut introduire.
4. **Version dynamique** : les rayons de toutes les boules s'incrémentent à chaque tour.
5. **Terminaison** : ajouter une règle permettant à un joueur de décider une fois par partie que le jeu se termine dans 5 tours.
6. **Obstacles** : le tableau commence avec certains obstacles que les boules ne peuvent pas toucher.

<!--## Bonus et améliorations

Finalement, vous devrez implémenter au moins deux des améliorations suivantes :

1. **IA** : ajoutez un mode où l'ordinateur joue tout seul.
2. **Classement** : si vous implémentez l'IA, rajoutez de quoi mémoriser / afficher le classement des meilleurs scores.
3. **Mode billard** : les boules bougent selon les règles d'un billard.
4. **Création des obstacles** : rajoutez la possibilité de charger une aire de jeu agrémentée d'obstacles à partir d'un fichier texte.
5. **Pause et sauvegarde** : rajoutez la possibilité de mettre en pause le jeu et de reprendre la partie, et de sauvegarder l'état du jeu à ce moment-là.
6. **Sauvegarde des paramètres** : rajoutez un fichier de configuration pour le jeu afin de fixer les valeurs des différents paramètres.-->
