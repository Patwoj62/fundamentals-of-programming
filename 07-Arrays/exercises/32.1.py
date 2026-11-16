# ===== Zadanie 39 =====

# Checks if first array is subset of second array

array1 = [2, 4, 6]  # pierwsza lista liczb

array2 = [1, 2, 3, 4, 5, 6, 7]  # druga lista liczb

is_subset = True  # zakładamy że pierwszy zbiór jest podzbiorem

for element in array1:  # przechodzi po wszystkich elementach pierwszej tablicy

    if element not in array2:  # sprawdza czy element istnieje w drugiej tablicy

        is_subset = False  # znaleziono brakujący element

        break  # kończy dalsze sprawdzanie

print("Array1:", array1)  # wyświetla pierwszą tablicę

print("Array2:", array2)  # wyświetla drugą tablicę

print("Subset:", is_subset)  # wyświetla wynik