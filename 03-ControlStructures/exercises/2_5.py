# ===== Zadanie 11 =====

number = int(input('Enter number: '))  # pobranie liczby

if number > 0:  # sprawdzenie czy liczba jest dodatnia
    print(f'Number {number} is positive')  # komunikat dla liczby dodatniej
elif number < 0:  # sprawdzenie czy liczba jest ujemna
    print(f'Number {number} is negative')  # komunikat dla liczby ujemnej
else:  # gdy liczba jest równa zero
    print('Number is 0')  # komunikat dla zera