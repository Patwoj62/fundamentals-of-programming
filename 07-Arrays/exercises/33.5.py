# ===== Zadanie 53 =====

def transpose_matrix(matrix):  # funkcja transponująca macierz

    rows = len(matrix)  # liczba wierszy

    cols = len(matrix[0])  # liczba kolumn

    result = []  # nowa macierz wynikowa

    for col in range(cols):  # przechodzi po wszystkich kolumnach

        new_row = []  # nowy wiersz macierzy wynikowej

        for row in range(rows):  # przechodzi po wszystkich wierszach

            new_row.append(matrix[row][col])  # zamienia kolumny na wiersze

        result.append(new_row)  # dodaje nowy wiersz do macierzy

    return result  # zwraca transponowaną macierz


def print_matrix(matrix):  # funkcja wyświetlająca macierz

    for row in matrix:  # przechodzi po wszystkich wierszach

        for value in row:  # przechodzi po elementach wiersza

            print(value, end=" ")  # wyświetla element

        print()  # nowa linia


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]  # pierwsza macierz

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]  # druga macierz

matrix3 = [
    [5, 6, 7, 8]
]  # trzecia macierz

print("Matrix 1 transposed:")  # nagłówek
print_matrix(transpose_matrix(matrix1))  # wyświetla macierz w wierszach i kolumnach

print()  # pusta linia

print("Matrix 2 transposed:")  # nagłówek
print_matrix(transpose_matrix(matrix2))  # wyświetla macierz w wierszach i kolumnach

print()  # pusta linia

print("Matrix 3 transposed:")  # nagłówek
print_matrix(transpose_matrix(matrix3))  # wyświetla macierz w wierszach i kolumnach
