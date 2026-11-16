# ===== Zadanie 39 =====

def sum_natural(n):  # funkcja przyjmująca liczbę naturalną
    if n == 1:  # przypadek podstawowy
        return 1  # zwrócenie 1

    return n + sum_natural(n - 1)  # wywołanie rekurencyjne

print(sum_natural(10))  # 55