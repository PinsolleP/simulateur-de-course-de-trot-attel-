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
                print("Le nombre doit être compris entre 12 et 20.")
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
    participants = {}

    for i in range(1, nb_int + 1):
        participants[i]= {
            "horse_speed": 0,
            "distance": 0,
            "race_time": 0,
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
           horse (dict) : Dictionnaire contenant les infos du joueur.
           roll (int) : Résultat du lancer de dé (1 à 6).

       Returns:
           dict: Participant mis à jour.
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
    arrival_distance = 2400
    winners = []
    turn = 1

    while len(winners) < nb_winner :
        print(f"Tour {turn}")

        for numero, horse in participants.items():
            if horse["eliminated"]:
                continue

            roll = dice_roll()
            update_participant(horse, roll)

            if horse["distance"] >= arrival_distance and numero not in winners:
                winners.append(numero)

        print("classement provisoire :")
        for numero, horse in participants.items():
            print(
                f"Horse {numero} :"
                f"{horse['distance']} m "
                f"speed={horse['horse_speed']} "
                f"time={horse['race_time']} "
                f"eliminated={horse['eliminated']}"
            )

        turn += 1

    print("Course terminée")
    print(' '.join(map(str, winners)), end='')
    return winners


if __name__ == '__main__':
    nb_horse = correct_number_entry()
    nb_winner = correct_race_entry()
    participants = init_horses(nb_horse)
    game_mechanic(participants, nb_winner)
