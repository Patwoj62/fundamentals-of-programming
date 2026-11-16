# ===== Zadanie 1 =====

arr = [2, 3, 7, 5, 4]  # lista (list) zawierająca 5 liczb całkowitych (int)

print(arr)  # wyświetla całą listę
print("Number of elements", len(arr))  # len() zwraca liczbę elementów listy

print("First value", arr[0])  # pierwszy element listy (indeks 0)
print("Second value", arr[1])  # drugi element listy (indeks 1)

print("Last value", arr[-1])  # ostatni element listy

print("Last but one value", arr[len(arr) - 2])  # przedostatni element bez użycia indeksu ujemnego

print("Sum of first and last value", arr[0] + arr[-1])  # suma pierwszego i ostatniego elementu

print("Middle value", arr[len(arr) // 2])  # element środkowy listy

for value in arr:  # pętla przechodząca po wszystkich elementach listy
    print(value, end=" ")  # wypisuje elementy w jednej linii oddzielone spacją