# ===== Zadanie 54 =====

def to_1d(array_2d):  # funkcja zamieniająca tablicę 2D na 1D

    result = []  # lista wynikowa

    for row in array_2d:  # przechodzi po wszystkich wierszach

        for value in row:  # przechodzi po wszystkich elementach

            result.append(value)  # dodaje element do listy wynikowej

    return result  # zwraca tablicę jednowymiarową


def print_matrix(matrix):  # funkcja wyświetlająca tablicę 2D

    for row in matrix:  # przechodzi po wszystkich wierszach

        for value in row:  # przechodzi po elementach

            print(value, end=" ")  # wyświetla wartość

        print()  # nowa linia


array1 = [
    [2, 3],
    [1, 5]
]  # pierwsza tablica

array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]  # druga tablica

array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]  # trzecia tablica

print("Array 1:")  # nagłówek
print_matrix(array1)  # wyświetla tablicę 2D
print("1D:", to_1d(array1))  # wyświetla wynik

print()  # pusta linia

print("Array 2:")  # nagłówek
print_matrix(array2)  # wyświetla tablicę 2D
print("1D:", to_1d(array2))  # wyświetla wynik

print()  # pusta linia

print("Array 3:")  # nagłówek
print_matrix(array3)  # wyświetla tablicę 2D
print("1D:", to_1d(array3))  # wyświetla wynik