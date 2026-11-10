# ===== Zadanie 43 ====

import random                               # import modułu random

# COMPUTER TURN

computer = random.randint(1, 6)            # komputer losuje liczbę

# YOUR TURN

you = int(input("Enter a number from 1 to 6: "))  # użytkownik podaje liczbę
won = computer == you                      # sprawdzenie czy użytkownik zgadł

print(f"You won: {won}")                   # wyświetlenie wyniku