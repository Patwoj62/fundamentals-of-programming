# ===== Zadanie 51 =====

# Swaps first and last column

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")  # nagłówek

for row in array:  # wyświetla tablicę przed zmianą

    print(row)  # wyświetla wiersz

for row in array:  # przechodzi po wszystkich wierszach

    row[0], row[-1] = row[-1], row[0]  # zamienia pierwszą i ostatnią kolumnę

print("After:")  # nagłówek

for row in array:  # wyświetla tablicę po zmianie

    print(row)  # wyświetla wiersz