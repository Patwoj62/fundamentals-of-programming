# ===== Zadanie 29 =====

def bubblesort(array):  # funkcja sortowania bąbelkowego

    n = len(array)  # liczba elementów

    for i in range(n):  # liczba przebiegów

        for j in range(0, n - i - 1):  # porównywanie sąsiednich elementów

            if array[j] > array[j + 1]:  # sprawdza kolejność elementów

                array[j], array[j + 1] = array[j + 1], array[j]  # zamiana miejscami

    return array  # zwraca posortowaną listę


arr1 = [7, 3, 9, 1, 5]  # pierwsza tablica
arr2 = [20, 15, 10, 5]  # druga tablica
arr3 = [100, 25, 75, 50]  # trzecia tablica

print(bubblesort(arr1.copy()))  # sortuje pierwszą tablicę
print(bubblesort(arr2.copy()))  # sortuje drugą tablicę
print(bubblesort(arr3.copy()))  # sortuje trzecią tablicę