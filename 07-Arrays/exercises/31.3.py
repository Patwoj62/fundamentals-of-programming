# ===== Zadanie 31 =====

def occurs(number, array):  # funkcja sprawdzająca występowanie liczby

    return number in array  # zwraca True lub False


array = [15, 38, 7, 23, 14]  # lista liczb

number = int(input("Number: "))  # pobiera liczbę od użytkownika

print("Array:", *array)  # wyświetla zawartość tablicy

if occurs(number, array):  # sprawdza obecność liczby

    print("Result: number", number, "appears in the array")  # komunikat pozytywny

else:  # gdy liczby nie ma

    print("Result: number", number, "does not appear in the array")  # komunikat negatywny