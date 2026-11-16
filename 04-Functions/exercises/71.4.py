# ===== Zadanie 23 =====

def f(number1, number2, operator):  # funkcja przyjmuje dwie liczby i operator
    if operator == '+':  # sprawdzenie dodawania
        return number1 + number2  # zwrócenie sumy

    elif operator == '-':  # sprawdzenie odejmowania
        return number1 - number2  # zwrócenie różnicy

    elif operator == '*':  # sprawdzenie mnożenia
        return number1 * number2  # zwrócenie iloczynu

    elif operator == '%':  # sprawdzenie modulo
        return number1 % number2  # zwrócenie reszty z dzielenia

    elif operator == '**':  # sprawdzenie potęgowania
        return number1 ** number2  # zwrócenie wyniku potęgowania

print(f(2, 3, "+"))  # 5
print(f(2, 3, "%"))  # 2
print(f(2, 3, "**"))  # 8
print(f(2, 3, "*"))  # 6
print(f(2, 3, "-"))  # -1