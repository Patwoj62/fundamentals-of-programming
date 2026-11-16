# ===== Zadanie 14 =====

tic_tac_toe_board = [  # dwuwymiarowa lista 3x3 typu list
    ['X', 'O', 'X'],  # pierwszy wiersz planszy
    [' ', 'X', 'O'],  # drugi wiersz planszy
    ['O', ' ', 'X']   # trzeci wiersz planszy
]

for row in tic_tac_toe_board:  # przechodzi po każdym wierszu planszy
    for value in row:  # przechodzi po każdym elemencie wiersza
        print(value, end=" ")  # wyświetla znak i spację bez przejścia do nowej linii
    print()  # przechodzi do nowej linii po każdym wierszu