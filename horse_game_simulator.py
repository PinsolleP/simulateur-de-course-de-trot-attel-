#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
simulateur_course_hippique
"""
import random


def correct_number_entry(message="Entrez le nombre de chevaux entre 12 et 20 :"):
    """Fonction qui vérifie la bonne saisie utilisateur d'un entier positif entre 12 et 20."""

    while True:
        number = input(message).strip()  # ignore les espaces avant et après la saisie
        if number.lstrip("-").isdigit():  # isdigit() = est numérique
            nb_int = int(number)
            if 12 <= nb_int <= 20:
                return nb_int
        else:
            print("saisie invalide.")


def correct_race_entry(message="Quel type de course souhaitez vous? tiercé , quarté , quinté :"):
    """Fonction qui vérifie la bonne saisie utilisateur du type de course souhaité."""

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
    participant = {}

    for i in range(1, nb_int + 1):
        numero = int(i)
        horse_speed = 0
        distance = 0
        race_time = 0
        eliminated = False

        participant[numero] = {
            "horse_speed": horse_speed,
            "distance": distance,
            "race_time": race_time,
            "eliminated": eliminated
        }

    return participant


def dice_roll():
    """
        Retourne un entier aléatoire entre 1 et 6 inclus.
        Simule un lancer de dé.
        """
    roll = random.randint(1, 6)
    return roll


def roll_one(participant):

    match participant["horse_speed"]:
        case 0:
            participant["horse_speed"] += 0
            participant["distance"] += 0

        case 1:
            participant["horse_speed"] += 0
            participant["distance"] += 23

        case 2:
            participant["horse_speed"] += 0
            participant["distance"] += 46

        case 3:
            participant["horse_speed"] -= 1
            participant["distance"] += 46

        case 4:
            participant["horse_speed"] -= 1
            participant["distance"] += 69

        case 5:
            participant["horse_speed"] -= 2
            participant["distance"] += 69

        case 6:
            participant["horse_speed"] -= 2
            participant["distance"] += 92

    participant["race_time"] += 10
    return participant


def roll_two(participant):

    match participant["horse_speed"]:
        case 0:
            participant["horse_speed"] += 1
            participant["distance"] += 23

        case 1:
            participant["horse_speed"] += 0
            participant["distance"] += 23

        case 2:
            participant["horse_speed"] += 0
            participant["distance"] += 46

        case 3:
            participant["horse_speed"] += 0
            participant["distance"] += 69

        case 4:
            participant["horse_speed"] += 0
            participant["distance"] += 92

        case 5:
            participant["horse_speed"] -= 1
            participant["distance"] += 92

        case 6:
            participant["horse_speed"] -= 1
            participant["distance"] += 115

    participant["race_time"] += 10
    return participant


def roll_three(participant):

    match participant["horse_speed"]:
        case 0:
            participant["horse_speed"] += 1
            participant["distance"] += 23

        case 1:
            participant["horse_speed"] += 1
            participant["distance"] += 46

        case 2:
            participant["horse_speed"] += 1
            participant["distance"] += 69

        case 3:
            participant["horse_speed"] += 0
            participant["distance"] += 69

        case 4:
            participant["horse_speed"] += 0
            participant["distance"] += 92

        case 5:
            participant["horse_speed"] += 0
            participant["distance"] += 115

        case 6:
            participant["horse_speed"] += 0
            participant["distance"] += 138

    participant["race_time"] += 10
    return participant


def roll_four(participant):

    match participant["horse_speed"]:
        case 0:
            participant["horse_speed"] += 1
            participant["distance"] += 23

        case 1:
            participant["horse_speed"] += 1
            participant["distance"] += 46

        case 2:
            participant["horse_speed"] += 1
            participant["distance"] += 69

        case 3:
            participant["horse_speed"] += 1
            participant["distance"] += 92

        case 4:
            participant["horse_speed"] += 0
            participant["distance"] += 92

        case 5:
            participant["horse_speed"] += 0
            participant["distance"] += 115

        case 6:
            participant["horse_speed"] += 0
            participant["distance"] += 138

    participant["race_time"] += 10
    return participant


def roll_five(participant):

    match participant["horse_speed"]:
        case 0:
            participant["horse_speed"] += 2
            participant["distance"] += 46

        case 1:
            participant["horse_speed"] += 1
            participant["distance"] += 46

        case 2:
            participant["horse_speed"] += 1
            participant["distance"] += 69

        case 3:
            participant["horse_speed"] += 1
            participant["distance"] += 92

        case 4:
            participant["horse_speed"] += 1
            participant["distance"] += 115

        case 5:
            participant["horse_speed"] += 0
            participant["distance"] += 115

        case 6:
            participant["horse_speed"] += 0
            participant["distance"] += 138

    participant["race_time"] += 10
    return participant


def roll_six(participant):

    match participant["horse_speed"]:
        case 0:
            participant["horse_speed"] += 2
            participant["distance"] += 46

        case 1:
            participant["horse_speed"] += 2
            participant["distance"] += 69

        case 2:
            participant["horse_speed"] += 2
            participant["distance"] += 92

        case 3:
            participant["horse_speed"] += 1
            participant["distance"] += 92

        case 4:
            participant["horse_speed"] += 1
            participant["distance"] += 115

        case 5:
            participant["horse_speed"] += 1
            participant["distance"] += 138

        case 6:
            participant["eliminated"] = True
            return participant

    participant["race_time"] += 10
    return participant


def update_participant(participant, roll):

    if roll == 1:
        roll_one(participant)
    elif roll == 2:
        roll_two(participant)
    elif roll == 3:
        roll_three(participant)
    elif roll == 4:
        roll_four(participant)
    elif roll == 5:
        roll_five(participant)
    else:
        roll_six(participant)
        
    return participant


def game_mechanic(participant,):

    nb_horse = correct_number_entry()
    correct_race_entry()
    print(init_horses(nb_horse))
    arrival_distance = 2400




if __name__ == '__main__':
    game_mechanic()
