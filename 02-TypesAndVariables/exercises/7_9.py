# ===== Zadanie 42 ====

import random                               # import modułu random

dice_roll = random.randint(1, 6)            # rzut kostką
special_number = dice_roll == 1 or dice_roll == 6  # sprawdzenie wartości

print(f"Dice rolled: {dice_roll}")          # wyświetlenie liczby
print(f"Special number (1 or 6): {special_number}")  # wyświetlenie wyniku