# ===== Zadanie 53 =====

i = 6  # początkowa wartość

while i >= 0:  # kolejne wiersze
    j = 1  # pierwsza kolumna

    while j <= 3:  # trzy kolumny
        print(f'{i + j}', end=' ')  # wyświetlenie liczby
        j += 1  # następna kolumna
        
    print()  # nowa linia

    i -= 3  # przejście do kolejnego wiersza