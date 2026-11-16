# ===== Zadanie 19 =====

def f(x, y):  # funkcja przyjmująca początek i koniec przedziału
    counter = 0  # licznik liczb

    for number in range(x, y + 1):  # przejście po przedziale
        if number < 0 and number % 2 == 0:  # liczba ujemna i parzysta
            counter += 1  # zwiększenie licznika

    return counter  # zwrócenie wyniku

print(f(-7, 8))  # 3
print(f(-1, 11))  # 0
