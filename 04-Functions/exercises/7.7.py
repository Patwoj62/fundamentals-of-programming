# ===== Zadanie 16 =====

def f(binary_number):  # funkcja sprawdzająca zapis binarny
    for digit in binary_number:  # przejście po wszystkich znakach
        if digit not in '01':  # jeśli znak nie jest 0 lub 1
            return False  # zwrócenie False

    return True  # wszystkie znaki poprawne

print(f("101101"))  # True
print(f("1311a10100"))  # False