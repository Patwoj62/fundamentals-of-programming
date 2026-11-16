# ===== Zadanie 40 =====

def power(x, n):  # x - podstawa potęgi, n - wykładnik
    if n == 0:  # przypadek podstawowy
        return 1  # każda liczba do potęgi 0 daje 1

    return x * power(x, n - 1)  # wywołanie rekurencyjne

print(power(5, 3))  # 125