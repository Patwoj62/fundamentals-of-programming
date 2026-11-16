# ===== Zadanie 27 =====

def compare(array1, array2):  # funkcja porównująca listy

    if len(array1) != len(array2):  # różna liczba elementów
        return False  # tablice są różne

    for i in range(len(array1)):  # przejście po indeksach

        if array1[i] != array2: # porównanie elementów
            return False  # znaleziono różnicę

    return True  # tablice są identyczne


arr1 = ["water", "book", "sky"]  # pierwsza lista
arr2 = ["water", "book", "sky"]  # druga lista

print("Array1:", arr1)
print("Array2:", arr2)
print("Comparison:", compare(arr1, arr2))

arr1 = [True, False]  # pierwsza lista
arr2 = [True, False, True]  # druga lista

print("Array1:", arr1)
print("Array2:", arr2)
print("Comparison:", compare(arr1, arr2))

arr1 = [5, 3, 1]  # pierwsza lista
arr2 = [5, 3, 1]  # druga lista

print("Array1:", arr1)
print("Array2:", arr2)
print("Comparison:", compare(arr1, arr2))

arr1 = [3, 2, 1]  # pierwsza lista
arr2 = [3, 2]  # druga lista

print("Array1:", arr1)
print("Array2:", arr2)
print("Comparison:", compare(arr1, arr2))