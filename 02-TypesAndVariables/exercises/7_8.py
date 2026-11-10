# ===== Zadanie 41 ====

import random                               # import modułu random

dice_roll_1 = random.randint(1, 6)          # pierwszy rzut
dice_roll_2 = random.randint(1, 6)          # drugi rzut
dice_roll_3 = random.randint(1, 6)          # trzeci rzut
total = dice_roll_1 + dice_roll_2 + dice_roll_3  # suma oczek

print(f"Dice roll 1: {dice_roll_1}")        # wyświetlenie pierwszego rzutu
print(f"Dice roll 2: {dice_roll_2}")        # wyświetlenie drugiego rzutu
print(f"Dice roll 3: {dice_roll_3}")        # wyświetlenie trzeciego rzutu
print(f"Total: {total}")                    # wyświetlenie sumy