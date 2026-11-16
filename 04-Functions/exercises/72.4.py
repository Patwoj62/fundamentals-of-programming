# ===== Zadanie 33 =====

def f(expression):  # funkcja przyjmuje wyrażenie tekstowe
    return eval(expression)  # obliczenie wartości wyrażenia

print(f("2+3"))  # 5
print(f("3+8+1"))  # 12
print(f("2+3-4+5-0"))  # 6