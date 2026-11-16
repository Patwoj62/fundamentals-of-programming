# ===== Zadanie 24 =====

def f(detector):  # detector to ciąg znaków + i -
    people = 0  # aktualna liczba osób w sali
    maximum = 0  # maksymalna liczba osób

    for sign in detector:  # przejście po wszystkich znakach
        if sign == '+':  # osoba weszła
            people += 1  # zwiększenie liczby osób

        elif sign == '-':  # osoba wyszła
            people -= 1  # zmniejszenie liczby osób

        if people > maximum:  # sprawdzenie nowego maksimum
            maximum = people  # zapis największej wartości

    return maximum >= 3  # zwrócenie True jeśli były min. 3 osoby

print(f("+-+++-+---"))  # True
print(f("+-+-+-+-"))  # False
print(f("+-++-+--"))  # False
print(f("+-++-++-+---"))  # True