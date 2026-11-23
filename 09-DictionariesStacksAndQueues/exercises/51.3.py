# ===== Zadanie 24 =====

stack = []  # utworzenie pustego stosu

expression = input("Enter RPN expression: ")  # pobranie całego wyrażenia

tokens = expression.split()  # podział na elementy

for token in tokens:  # przejście po wszystkich elementach

    if token in ["+", "-", "*", "/"]:  # sprawdzenie operatora

        b = stack.pop()  # pobranie drugiej liczby

        a = stack.pop()  # pobranie pierwszej liczby

        if token == "+":  # dodawanie
            stack.append(a + b)

        elif token == "-":  # odejmowanie
            stack.append(a - b)

        elif token == "*":  # mnożenie
            stack.append(a * b)

        elif token == "/":  # dzielenie
            stack.append(a / b)

    elif token == "=":  # wyświetlenie wyniku

        print("Result:", stack.pop())

    else:  # liczba

        stack.append(float(token))