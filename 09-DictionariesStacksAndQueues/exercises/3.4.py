# ===== Zadanie 13 =====

number = int(input("Enter a natural number: "))  # pobranie liczby od użytkownika

original_number = number  # zapamiętanie oryginalnej liczby

stack = []  # utworzenie pustego stosu

print("Division\tRemainder")  # nagłówek

while number > 0:  # wykonuj dopóki liczba jest większa od 0

    remainder = number % 2  # obliczenie reszty z dzielenia przez 2

    quotient = number // 2  # wynik dzielenia całkowitego

    print(f"{number} / 2 = {quotient}\t{remainder}")  # wyświetlenie działania

    stack.append(remainder)  # zapisanie reszty na stos

    number = quotient  # przejście do kolejnego kroku

binary_number = ""  # pusty napis na wynik binarny

while len(stack) > 0:  # dopóki na stosie są elementy
    binary_number += str(stack.pop())  # zdejmowanie cyfr ze stosu

print(f"Natural number: {original_number}")  # wyświetlenie liczby dziesiętnej

print(f"Binary number: {binary_number}")  # wyświetlenie liczby binarnej