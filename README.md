# Ce projet est un simulateur de course de chevaux développé en Python.

# Objectifs

Ce projet a été réalisé afin de mettre en pratique les notions suivantes :

- les fonctions Python ;
- les boucles (`while`, `for`) ;
- les conditions (`if`, `match/case`) ;
- les dictionnaires ;
- la manipulation des listes ;
- le tri de données avec `sorted()` ;
- la gestion des entrées utilisateur ;
- la génération aléatoire avec le module `random

# Règlr du jeu :

    Une course de trot attelé2 rassemble 12 à 20 chevaux, chacun tractant un sulky, et 
étant mené par un driver. Elle peut faire l’objet d’un tiercé, d’un quarté, ou d’un 
quinté. La course est supposée se dérouler sur un hippodrome rectiligne (chaque cheval disposant de 
son propre couloir), d’une longueur de 2 400 m. Il est à noter que chaque cheval doit respecter 
l’allure du trot de bout en bout, le passage au galop entrainant sa disqualification. L’utilisateur saisit 
au démarrage le nombre de chevaux et le type de la course. 

    La course se déroule à la manière d’un « jeu de plateau » : à chaque tour de jeu, chaque cheval fait 
l’objet d’un jet de dé (à 6 faces), qui décide d’une altération possible de sa vitesse (augmentation, 
stabilisation, diminution). La nouvelle vitesse détermine alors la distance dont il avance. Chaque tour 
de jeu représente 10 secondes du déroulement de la course, mais le temps ne sera pas rendu dans le 
programme. C’est l’utilisateur qui fera avancer la course de tour en tour, à la suite d’un message du 
programme l’y invitant. 

    Le tableau suivant indique les évolutions de la vitesse d’un cheval, selon sa vitesse actuelle, et le jet 
d’un dé (DQ indique que le cheval est disqualifié). 
 
| Victesse actuelle | 🎲 1 | 🎲 2 | 🎲 3 | 🎲 4 | 🎲 5 | 🎲 6 |
|-------------------|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0  | +1 | +1 | +1 | +2 | +2 |
| 1 | 0  | 0  | +1 | +1 | +1 | +2 |
| 2 | 0  | 0  | +1 | +1 | +1 | +2 |
| 3 | -1 | 0  | 0  | +1 | +1 | +1 |
| 4 | -1 | 0  | 0  | 0  | +1 | +1 |
| 5 | -2 | -1 | 0  | 0  | 0  | +1 |
| 6 | -2 | -1 | 0  | 0  | 0  | DQ |

 
 
    Le tableau qui suit donne pour sa part la distance dont avance un cheval lors d’un tour de jeu suivant 
sa vitesse. 

|                 /Vitesse → | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|----------------------------|--:|--:|--:|--:|--:|---:|---:|
| Distance (m)               | 0 | 23 | 46 | 69 | 92 | 115 | 138 |

    Chaque cheval démarre la course à l’arrêt. Lors de chaque tour, chaque cheval voit sa vitesse évoluer, 
puis parcourir la distance correspondant à sa nouvelle vitesse. Il peut être intéressant d’afficher alors 
le temps écoulé, la vitesse et la distance parcourue par chaque cheval. La course se déroule jusqu’à ce 
que le dernier cheval non disqualifié ait franchit la ligne d’arrivée. On n’affichera cependant que les 3, 
4 ou 5 premiers chevaux arrivés (suivant le type de la course). 

# Fonctionnalités

Le simulateur permet :

- de choisir le nombre de chevaux (12 à 20)  
- de choisir le type de course :
    - tiercé (3 arrivées)
    - quarté (4 arrivées)
    - quinté (5 arrivées)

- de simuler les déplacements des chevaux  
- de gérer l'évolution de la vitesse  
- d'éliminer certains chevaux pendant la course  
- d'afficher un classement provisoire  
- d'afficher le classement final

# Technologies utilisées

- Python 3.14
- Module standard `random`
- Git / GitHub

# Améliorations possibles

Quelques évolutions possibles :

- ajouter une interface graphique ;
- ajouter des chevaux avec des caractéristiques différentes ;
- ajouter une sauvegarde des résultats ;
- gérer une vraie photo-finish en cas d'égalité ;
- ajouter plusieurs courses avec un classement général.