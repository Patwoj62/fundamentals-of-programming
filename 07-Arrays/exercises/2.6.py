# ===== Zadanie 18 =====


matrix = [  # macierz 3x3 typu list
    [0, 0, 0],  # pierwszy wiersz
    [0, 0, 0],  # drugi wiersz
    [0, 0, 0]   # trzeci wiersz
]

for i in range(len(matrix)):  # przechodzi po indeksach wierszy
    matrix[i][i] = 1  # ustawia element głównej przekątnej na 1

for row in matrix:  # przechodzi po każdym wierszu macierzy
    for value in row:  # przechodzi po każdym elemencie wiersza
        print(value, end=" ")  # wyświetla element z odstępem
    print()  # przechodzi do nowej linii po zakończeniu wiersza