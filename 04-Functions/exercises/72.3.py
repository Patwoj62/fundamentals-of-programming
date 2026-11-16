# ===== Zadanie 32 =====

def f(password):  # funkcja przyjmuje hasło
    if len(password) < 6:  # hasło musi mieć co najmniej 6 znaków
        return False  # niepoprawne hasło

    return len(password) == len(set(password))  # sprawdzenie unikalności znaków

print(f("ax15"))  # False
print(f("book123"))  # False
print(f("A2water3"))  # True
print(f("qwerty"))  # True
print(f(""))  # False