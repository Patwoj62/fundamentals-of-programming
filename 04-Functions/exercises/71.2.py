# ===== Zadanie 21 =====

def f(n):  # funkcja przyjmująca liczbę gwiazdek
    return "/*".join(["*"] * n)  # połączenie znaków *

print(f(4))  # */*/*/*
print(f(1))  # *