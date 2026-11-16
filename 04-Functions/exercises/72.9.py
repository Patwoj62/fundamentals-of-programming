# ===== Zadanie 38 =====

def factorial(n):  # funkcja obliczająca silnię
    if n == 0 or n == 1:  # przypadek podstawowy
        return 1  # 0! = 1, 1! = 1

    if n > 1:  # dla liczb większych od 1
        return n * factorial(n - 1)  # wywołanie rekurencyjne

print(factorial(5))  # 120
