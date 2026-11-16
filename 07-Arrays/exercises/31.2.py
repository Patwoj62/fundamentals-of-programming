# ===== Zadanie 30 =====

array = [2, 3, 2, 5, 8, 1, 9, 8]  # lista liczb

print("Array:", *array)  # wyświetla elementy tablicy

print("Unique elements:", end=" ")  # nagłówek

for number in array:  # przechodzi po wszystkich liczbach

    if array.count(number) == 1:  # sprawdza czy liczba występuje tylko raz

        print(number, end=" ")  # wyświetla unikalną wartość