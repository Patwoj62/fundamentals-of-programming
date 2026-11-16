# ===== Zadanie 49 =====

# Finds smallest and largest values with positions

array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_value = array[0][0]  # początkowa najmniejsza wartość

max_value = array[0][0]  # początkowa największa wartość

min_row = 0  # wiersz minimum

min_col = 0  # kolumna minimum

max_row = 0  # wiersz maksimum

max_col = 0  # kolumna maksimum

for row in range(len(array)):  # przechodzi po wszystkich wierszach

    for col in range(len(array[row])):  # przechodzi po wszystkich kolumnach

        if array[row][col] < min_value:  # sprawdza nowe minimum

            min_value = array[row][col]  # zapisuje minimum

            min_row = row  # zapisuje numer wiersza

            min_col = col  # zapisuje numer kolumny

        if array[row][col] > max_value:  # sprawdza nowe maksimum

            max_value = array[row][col]  # zapisuje maksimum

            max_row = row  # zapisuje numer wiersza

            max_col = col  # zapisuje numer kolumny

print("Minimum:", min_value)  # wyświetla najmniejszą wartość

print("Row:", min_row, "Column:", min_col)  # wyświetla położenie minimum

print("Maximum:", max_value)  # wyświetla największą wartość

print("Row:", max_row, "Column:", max_col)  # wyświetla położenie maksimum