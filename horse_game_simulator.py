#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulateur de course hippique.

Ce programme simule une course de chevaux basée sur des lancers de dés.
Le joueur choisit – le nombre de chevaux participants (12 à 20). Le type de course (tiercé, quarté ou quinté).

Chaque cheval possède – une vitesse
– une distance parcourue
– un temps de course
– un statut d'élimination
- un temps d'arrivée.

Le programme gère – le déplacement des chevaux selon le résultat du dé
– les éliminations
- le classement provisoire
– le classement final des chevaux arrivés.
"""

import random


def correct_number_entry(message="Entrez le nombre de chevaux entre 12 et 20 :"):
    """
    Demande à l'utilisateur le nombre de chevaux participant à la course.

    Vérifie que la saisie est un entier compris entre 12 et 20.

    Args:
        message (str) : Message affiché à l'utilisateur.

    Returns:
        nb_int: Nombre de chevaux validé.
    """

    while True:
        number = input(message).strip()  # ignore les espaces avant et après la saisie
        if number.lstrip("-").isdigit():  # isdigit() = est numérique
            nb_int = int(number)
            if 12 <= nb_int <= 20:
                return nb_int
            else:
                print("Le nombre doit être compris entre 12 et 20.")
        else:
            print("saisie invalide.")


def correct_race_entry(message="Quel type de course souhaitez vous? tiercé , quarté , quinté :"):
    """
    Demande le type de course choisi par le joueur.

    Les choix possibles sont tiercé : 3 chevaux gagnants
    – quarté : 4 chevaux gagnants
    – quinté : 5 chevaux gagnants.

    Args:
        message (str) : Message affiché à l'utilisateur.

    Returns:
        nb_winners : Nombre de chevaux gagnants attendus.
    """

    valid_name = ["tiercé", "quarté", "quinté"]
    while True:
        race_name = input(message).strip().lower()  # lower() = toutes les lettres en minuscule
        if race_name in valid_name:
            if race_name == "tiercé":
                nb_winner = 3
            elif race_name == "quarté":
                nb_winner = 4
            else:
                nb_winner = 5

            return nb_winner
        else:
            print("Choix invalide.")


def init_horses(nb_int):
    """
        Initialise les chevaux participant à la course.

        Chaque cheval reçoit un dictionnaire contenant – sa vitesse initiale
        – sa distance parcourue
        – son temps de course
        – son temps d'arrivée
        – son statut d'élimination

        Args:
            nb_int (int) : Nombre de chevaux participants.

        Returns:
            participants : Dictionnaire contenant tous les chevaux.
        """
    participants = {}

    for i in range(1, nb_int + 1):
        participants[i] = {
            "horse_speed": 0,
            "distance": 0,
            "race_time": 0,
            "arrival_time": 0,
            "eliminated": False
        }
    return participants


def dice_roll():
    """
        Retourne un entier aléatoire entre 1 et 6 inclus.
        Simule un lancer de dé.
        """
    roll = random.randint(1, 6)
    return roll


def roll_one(horse):
    """
    Met à jour la position d'un cheval selon le résultat du dé.

    La vitesse du cheval peut évoluer et la distance parcourue
    est augmentée selon sa vitesse actuelle.

    Args:
        horse (dict) : Informations du cheval.

    Returns:
        horse: Cheval mis à jour.
    """
    match horse["horse_speed"]:
        case 0:
            horse["horse_speed"] += 0
            horse["distance"] += 0

        case 1:
            horse["horse_speed"] += 0
            horse["distance"] += 23

        case 2:
            horse["horse_speed"] += 0
            horse["distance"] += 46

        case 3:
            horse["horse_speed"] -= 1
            horse["distance"] += 46

        case 4:
            horse["horse_speed"] -= 1
            horse["distance"] += 69

        case 5:
            horse["horse_speed"] -= 2
            horse["distance"] += 69

        case 6:
            horse["horse_speed"] -= 2
            horse["distance"] += 92

    horse["race_time"] += 10
    return horse


def roll_two(horse):
    """
        Met à jour la position d'un cheval selon le résultat du dé.

        La vitesse du cheval peut évoluer et la distance parcourue
        est augmentée selon sa vitesse actuelle.

        Args:
            horse (dict) : Informations du cheval.

        Returns:
            horse: Cheval mis à jour.
        """
    match horse["horse_speed"]:
        case 0:
            horse["horse_speed"] += 1
            horse["distance"] += 23

        case 1:
            horse["horse_speed"] += 0
            horse["distance"] += 23

        case 2:
            horse["horse_speed"] += 0
            horse["distance"] += 46

        case 3:
            horse["horse_speed"] += 0
            horse["distance"] += 69

        case 4:
            horse["horse_speed"] += 0
            horse["distance"] += 92

        case 5:
            horse["horse_speed"] -= 1
            horse["distance"] += 92

        case 6:
            horse["horse_speed"] -= 1
            horse["distance"] += 115

    horse["race_time"] += 10
    return horse


def roll_three(horse):
    """
        Met à jour la position d'un cheval selon le résultat du dé.

        La vitesse du cheval peut évoluer et la distance parcourue
        est augmentée selon sa vitesse actuelle.

        Args:
            horse (dict) : Informations du cheval.

        Returns:
            horse: Cheval mis à jour.
        """
    match horse["horse_speed"]:
        case 0:
            horse["horse_speed"] += 1
            horse["distance"] += 23

        case 1:
            horse["horse_speed"] += 1
            horse["distance"] += 46

        case 2:
            horse["horse_speed"] += 1
            horse["distance"] += 69

        case 3:
            horse["horse_speed"] += 0
            horse["distance"] += 69

        case 4:
            horse["horse_speed"] += 0
            horse["distance"] += 92

        case 5:
            horse["horse_speed"] += 0
            horse["distance"] += 115

        case 6:
            horse["horse_speed"] += 0
            horse["distance"] += 138

    horse["race_time"] += 10
    return horse


def roll_four(horse):
    """
        Met à jour la position d'un cheval selon le résultat du dé.

        La vitesse du cheval peut évoluer et la distance parcourue
        est augmentée selon sa vitesse actuelle.

        Args:
            horse (dict) : Informations du cheval.

        Returns:
            horse: Cheval mis à jour.
        """
    match horse["horse_speed"]:
        case 0:
            horse["horse_speed"] += 1
            horse["distance"] += 23

        case 1:
            horse["horse_speed"] += 1
            horse["distance"] += 46

        case 2:
            horse["horse_speed"] += 1
            horse["distance"] += 69

        case 3:
            horse["horse_speed"] += 1
            horse["distance"] += 92

        case 4:
            horse["horse_speed"] += 0
            horse["distance"] += 92

        case 5:
            horse["horse_speed"] += 0
            horse["distance"] += 115

        case 6:
            horse["horse_speed"] += 0
            horse["distance"] += 138

    horse["race_time"] += 10
    return horse


def roll_five(horse):
    """
        Met à jour la position d'un cheval selon le résultat du dé.

        La vitesse du cheval peut évoluer et la distance parcourue
        est augmentée selon sa vitesse actuelle.

        Args:
            horse (dict) : Informations du cheval.

        Returns:
            horse: Cheval mis à jour.
        """
    match horse["horse_speed"]:
        case 0:
            horse["horse_speed"] += 2
            horse["distance"] += 46

        case 1:
            horse["horse_speed"] += 1
            horse["distance"] += 46

        case 2:
            horse["horse_speed"] += 1
            horse["distance"] += 69

        case 3:
            horse["horse_speed"] += 1
            horse["distance"] += 92

        case 4:
            horse["horse_speed"] += 1
            horse["distance"] += 115

        case 5:
            horse["horse_speed"] += 0
            horse["distance"] += 115

        case 6:
            horse["horse_speed"] += 0
            horse["distance"] += 138

    horse["race_time"] += 10
    return horse


def roll_six(horse):
    """
        Met à jour la position d'un cheval selon le résultat du dé.

        La vitesse du cheval peut évoluer et la distance parcourue
        est augmentée selon sa vitesse actuelle.

        Args:
            horse (dict) : Informations du cheval.

        Returns:
            horse: Cheval mis à jour.
        """
    match horse["horse_speed"]:
        case 0:
            horse["horse_speed"] += 2
            horse["distance"] += 46

        case 1:
            horse["horse_speed"] += 2
            horse["distance"] += 69

        case 2:
            horse["horse_speed"] += 2
            horse["distance"] += 92

        case 3:
            horse["horse_speed"] += 1
            horse["distance"] += 92

        case 4:
            horse["horse_speed"] += 1
            horse["distance"] += 115

        case 5:
            horse["horse_speed"] += 1
            horse["distance"] += 138

        case 6:
            horse["eliminated"] = True
            return horse

    horse["race_time"] += 10
    return horse


def update_participant(horse, roll):
    """
       Met à jour un participant en fonction du résultat du dé.

       Args:
           horse (dict) : Dictionnaire contenant les infos du cheval.
           Roll (int) : Résultat du lancer de dé (1 à 6).

       Returns:
           horse: Cheval mis à jour.
       """

    if roll == 1:
        roll_one(horse)
    elif roll == 2:
        roll_two(horse)
    elif roll == 3:
        roll_three(horse)
    elif roll == 4:
        roll_four(horse)
    elif roll == 5:
        roll_five(horse)
    else:
        roll_six(horse)

    return horse


def game_mechanic(participants, nb_winner):
    """
        Gère le déroulement complet de la course hippique.

        À chaque tour – chaque cheval encore en course lance un dé
        – sa vitesse et sa distance sont mises à jour
        – les chevaux éliminés sont retirés de la course
        – le classement provisoire est affiché
        – les chevaux ayant atteint la distance d'arrivée sont ajoutés aux gagnants.

        La course continue jusqu'à obtenir le nombre de gagnants
        correspondant au type de course choisi.

          Args:
            participants (dict) : Dictionnaire contenant les chevaux participants
                avec leurs caractéristiques (vitesse, distance, temps de course,
                élimination et temps d'arrivée).

            nb_winner (int) : Nombre de chevaux devant terminer la course
                pour valider l'arrivée.

        Returns:
            winners : Liste contenant les numéros des chevaux gagnants dans
            l'ordre d'arrivée.
        """
    arrival_distance = 2400
    winners = []
    turn = 1

    while len(winners) < nb_winner:
        eliminated_horse = []
        print(f"Tour {turn}")

        for numero, horse in participants.items():

            roll = dice_roll()
            update_participant(horse, roll)

            if horse["eliminated"]:
                eliminated_horse.append(numero)
                continue

            if horse["distance"] >= arrival_distance and numero not in winners:
                winners.append(numero)
                horse["arrival_time"] = horse["race_time"]

        # Suppression des chevaux éliminés après le tour complet.
        # La suppression est faite après la boucle pour éviter
        # de modifier un dictionnaire pendant son parcours.
        for numero in eliminated_horse:
            print(f"Le cheval {numero} est disqualifié")
            del participants[numero]

        # Trie les chevaux selon la distance parcourue,
        # du plus avancé au moins avancé.
        classement = sorted(
            participants.items(),
            key=lambda item: item[1]["distance"],
            reverse=True
        )

        print("Classement provisoire :")

        for numero, horse in classement[:nb_winner]:
            print(
                f"Cheval {numero}: "
                f"{horse['distance']} m"
            )

        turn += 1

    classement_final = sorted(
        winners,
        key=lambda numero: participants[numero]["arrival_time"]
    )

    print("Course terminée")
    print("Classement final :")

    for place, numero in enumerate(classement_final, start=1):
        horse = participants[numero]
        print(
            f"{place}. Cheval {numero} - "
            f"{horse['arrival_time']} secondes"
        )


if __name__ == '__main__':
    nb_horse = correct_number_entry()
    nb_winner = correct_race_entry()
    participants = init_horses(nb_horse)
    game_mechanic(participants, nb_winner)
