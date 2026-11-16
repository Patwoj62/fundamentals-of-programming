# ===== Zadanie 18 =====

def f(number, even):  # number - liczba, even - bool
    total = 0  # suma cyfr

    for digit in str(abs(number)):  # przejście po cyfrach liczby
        digit = int(digit)  # konwersja na int

        if even and digit % 2 == 0:  # gdy sumujemy cyfry parzyste
            total += digit  # dodanie cyfry

        elif not even and digit % 2 != 0:  # gdy sumujemy cyfry nieparzyste
            total += digit  # dodanie cyfry

    return total  # zwrócenie wyniku

print(f(3124, True))  # 6
print(f(3124, False))  # 4
print(f(20576, False))  # 12
print(f(20576, True))  # 8