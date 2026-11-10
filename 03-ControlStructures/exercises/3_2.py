# ===== Zadanie 13 =====

age = int(input('Enter your age: '))  # pobranie wieku

if age < 18 or age >= 65:  # sprawdzenie warunku zniżki
    print('Discount available')  # zniżka przysługuje
else:  # brak zniżki
    print('No discount')  # komunikat o braku zniżki