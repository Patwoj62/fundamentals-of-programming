# ===== Zadanie 12 =====

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # nawiasy poprawne
expression2 = "[(2+3]/4)"  # nawiasy niepoprawne
expression3 = "(2-3*4+(5/6)"  # nawiasy niepoprawne

def brackets_ok(expression):  # definicja funkcji sprawdzającej nawiasy

    stack = []  # pusty stos

    pairs = {  # słownik dopasowanych nawiasów
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:  # przechodzenie po wszystkich znakach

        if char in "([{":  # jeśli nawias otwierający
            stack.append(char)  # włóż go na stos

        elif char in ")]}":  # jeśli nawias zamykający

            if len(stack) == 0:  # brak otwierającego nawiasu
                return False  # wyrażenie niepoprawne

            top = stack.pop()  # pobranie ostatniego nawiasu

            if top != pairs[char]:  # sprawdzenie zgodności pary
                return False  # błędna para nawiasów

    return len(stack) == 0  # True jeśli stos jest pusty

if brackets_ok(expression1):  # sprawdzenie pierwszego wyrażenia
    print("Expression 1: brackets are correct")
else:
    print("Expression 1: brackets are NOT correct")

if brackets_ok(expression2):  # sprawdzenie drugiego wyrażenia
    print("Expression 2: brackets are correct")
else:
    print("Expression 2: brackets are NOT correct")

if brackets_ok(expression3):  # sprawdzenie trzeciego wyrażenia
    print("Expression 3: brackets are correct")
else:
    print("Expression 3: brackets are NOT correct")