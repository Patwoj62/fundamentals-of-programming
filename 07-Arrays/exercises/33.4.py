# ===== Zadanie 52 =====

def identity_matrix(n):  # funkcja tworząca macierz jednostkową

    matrix = [[0 for i in range(n)] for j in range(n)]  # tworzy macierz n x n

    for i in range(n):  # przechodzi po przekątnej

        matrix[i][i] = 1  # wpisuje jedynkę na głównej przekątnej

    return matrix  # zwraca gotową macierz


def print_matrix(matrix):  # funkcja wyświetlająca macierz

    for row in matrix:  # przechodzi po wierszach

        for value in row:  # przechodzi po elementach wiersza

            print(value, end=" ")  # wyświetla liczbę

        print()  # przejście do nowej linii


print("Matrix 3x3")  # nagłówek

print_matrix(identity_matrix(3))  # wyświetla macierz 3x3

print()  # pusta linia

print("Matrix 5x5")  # nagłówek

print_matrix(identity_matrix(5))  # wyświetla macierz 5x5

print()  # pusta linia

print("Matrix 8x8")  # nagłówek

print_matrix(identity_matrix(8))  # wyświetla macierz 8x8