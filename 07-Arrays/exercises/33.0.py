# ===== Zadanie 48 =====

array = [  # tablica 5x5 wypełniona zerami
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for row in range(5):  # przechodzi po wszystkich wierszach

    for column in range(5):  # przechodzi po wszystkich kolumnach

        array[row][column] = (row + 1) * (column + 1)  # wpisuje wynik mnożenia

for row in array:  # przechodzi po wierszach tablicy

    for value in row:  # przechodzi po elementach wiersza

        print(value, end="\t")  # wyświetla wartość wraz z tabulatorem

    print()  # przechodzi do nowej linii