# ===== Zadanie 26 =====

def f(palindrome):  # funkcja przyjmuje tekst
    return palindrome == palindrome[::-1]  # porównanie tekstu z odwróconym

print(f("radar"))  # True
print(f("12-11-21"))  # True
print(f("book"))  # False