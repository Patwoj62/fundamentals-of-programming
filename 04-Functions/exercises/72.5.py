# ===== Zadanie 34 =====

def f(x, y):  # funkcja przyjmuje zakres
    total = 0  # suma liczb

    for number in range(x, y + 1):  # przejście po przedziale
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:  # sprawdzenie warunków
            total += number  # dodanie liczby do sumy

    return total  # zwrócenie wyniku

print(f(1, 20))  # 24
print(f(10, 30))  # 48