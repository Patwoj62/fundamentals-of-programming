# ===== Zadanie 20 =====

def f(n1, n2, n3):  # funkcja przyjmująca trzy liczby
    return n1 < 0 or n2 < 0 or n3 < 0  # zwrócenie wyniku logicznego

print(f(11, 6, -4))  # True
print(f(5, 4, 14))  # False