# ===== Zadanie 28 =====

# Prints numbers from first array that do not appear in second array
array1 = [4, 36, 12, 28, 9, 44, 5]  # pierwsza lista liczb
array2 = [5, 1, 36]  # druga lista liczb

print("Numbers not present in second array:")  # nagłówek

for number in array1:  # przechodzi po pierwszej tablicy

    if number not in array2:  # sprawdza czy liczby nie ma w drugiej tablicy
        print(number)  # wyświetla liczbę