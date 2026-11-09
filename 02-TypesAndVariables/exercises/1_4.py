# ===== Zadanie 4 =====

import random                               # import biblioteki do losowania

print("Dice rolling simulator")             # wyświetlenie tytułu programu

for i in range(5):                          # wykonanie pętli 5 razy
    dice_roll = random.randint(1, 6)        # losowanie liczby od 1 do 6
    print(dice_roll, end=" ")               # wyświetlenie wyniku rzutu