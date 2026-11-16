# ===== Zadanie 30 =====

def f(number1, number2, number3):  # funkcja przyjmuje trzy liczby
    return max(number1, number2, number3) - min(number1, number2, number3)  # obliczenie różnicy

print(f(7, 4, 9))  # 5
print(f(2, 12, 8))  # 10