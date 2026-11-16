# ===== Zadanie 45 =====

array = [
    [4, 8, 2, 1],
    [7, 3, 6, 9]
] # tablica dwuwymiarowa 2x4

for row in array:  # przechodzi po wierszach

    for value in row:  # przechodzi po elementach wiersza

        print(value, end=" ")  # wyświetla element

    print()  # nowa linia