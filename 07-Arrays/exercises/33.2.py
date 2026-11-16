# ===== Zadanie 50 =====

# Swaps first and last row

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")  # nagłówek

for row in array:  # wyświetla tablicę przed zmianą

    print(row)  # wyświetla wiersz

array[0], array[-1] = array[-1], array[0]  # zamienia pierwszy i ostatni wiersz

print("After:")  # nagłówek

for row in array:  # wyświetla tablicę po zmianie

    print(row)  # wyświetla wiersz