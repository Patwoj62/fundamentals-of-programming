# ===== Zadanie 25 =====

def f(n):  # funkcja przyjmująca numer elementu ciągu
    a = 0  # pierwszy element ciągu
    b = 1  # drugi element ciągu

    for i in range(1, n):  # obliczanie kolejnych elementów
        a, b = b, a + b  # przesunięcie wartości

    return a  # zwrócenie n-tego elementu

print(f(5))  # 3
print(f(9))  # 21