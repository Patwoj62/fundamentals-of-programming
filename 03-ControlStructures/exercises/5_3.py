# ===== Zadanie 25 =====

import random  # moduł do losowania liczb

number_to_guess = random.randint(1, 100)  # losowanie liczby od 1 do 100
user_guess = 0  # początkowa wartość zgadywanej liczby

print("Guess the number between 1 and 100!")  # komunikat startowy

while user_guess != number_to_guess:  # pętla działa do odgadnięcia liczby

    user_guess = int(input("Enter your guess: "))  # pobranie liczby od użytkownika

    if user_guess < number_to_guess:  # liczba za mała
        print("Too low! Try again.")  # komunikat

    elif user_guess > number_to_guess:  # liczba za duża
        print("Too high! Try again.")  # komunikat

    else:  # liczba prawidłowa
        print("Congratulations! You guessed the correct number.")  # sukces