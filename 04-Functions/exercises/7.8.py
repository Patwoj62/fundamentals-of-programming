# ===== Zadanie 17 =====

def f(amount_to_pay):  # funkcja obliczająca minimalną liczbę monet
    coins = 0  # licznik monet

    coins += amount_to_pay // 5  # użycie monet 5 PLN
    amount_to_pay %= 5  # pozostała kwota

    coins += amount_to_pay // 2  # użycie monet 2 PLN
    amount_to_pay %= 2  # pozostała kwota

    coins += amount_to_pay  # użycie monet 1 PLN

    return coins  # zwrócenie liczby monet

print(f(23))  # 6
print(f(8))  # 3
print(f(2))  # 1
print(f(0))  # 0