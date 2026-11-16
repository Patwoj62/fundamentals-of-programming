# ===== Zadanie 36 =====

def f(product_code):  # funkcja przyjmuje kod produktu jako str
    first_digit = int(product_code[0])  # pobranie pierwszej cyfry
    second_digit = int(product_code[1])  # pobranie drugiej cyfry
    third_digit = int(product_code[2])  # pobranie trzeciej cyfry
    control_digit = int(product_code[3])  # pobranie cyfry kontrolnej

    calculated_digit = (first_digit + second_digit + third_digit) % 7  # obliczenie cyfry kontrolnej

    return calculated_digit == control_digit  # zwrócenie True lub False

print(f("1082"))  # True
print(f("2035"))  # True
print(f("1114"))  # False
print(f("7071"))  # False