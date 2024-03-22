import os
import random

if os.path.exists("fichiers./meals.txt"):
    with open("fichiers./meals.txt", "r+") as file:
        meals_list = file.readlines()
        meal_random_choice = random.choice(meals_list)
        print("je vous propose aujourd'hui, le repas", meal_random_choice)
        file.close()
else:
    print("Le fichcier n'existe pas")


