# ===== Zadanie 23 =====

def reverse_text(text):  # funkcja odwracająca tekst

    stack = []  # stos

    for char in text:
        stack.append(char)

    reversed_text = ""

    while len(stack) > 0:
        reversed_text += stack.pop()

    return reversed_text

text = input("Enter text: ")

print(reverse_text(text))