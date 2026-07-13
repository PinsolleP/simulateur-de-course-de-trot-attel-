#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
simulateur_course_hippique
"""


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
            race = race_name
            return race
        else:
            print("Choix invalide.")


def init_horses(nb_int):
    participant = {}

    for i in range(1, nb_int + 1):
        numero = int(i)
        horse_speed = 0
        distance = 0
        race_time = 0

        participant[numero] = {
            "horse_speed": horse_speed,
            "distance": distance,
            "race_time": race_time
        }

    return participant


if __name__ == '__main__':
    nb_horse = correct_number_entry()
    race = correct_race_entry()
    print(init_horses(nb_horse))
