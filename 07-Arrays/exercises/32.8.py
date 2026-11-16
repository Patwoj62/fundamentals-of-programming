# ===== Zadanie 46 =====

array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

column_sum = 0  # suma ostatniej kolumny

for row in array:  # przechodzi po wszystkich wierszach

    column_sum += row[-1]  # dodaje ostatni element wiersza

print("Last column sum:", column_sum)  # wyświetla wynik