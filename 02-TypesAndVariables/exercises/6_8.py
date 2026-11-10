# ===== Zadanie 31 ====

first = input("Enter first letter: ")          # pobranie pierwszej litery
last = input("Enter last letter: ")            # pobranie drugiej litery
first_letter_code = ord(first)                 # kod pierwszej litery
last_letter_code = ord(last)                   # kod drugiej litery
number_of_letters = abs(last_letter_code - first_letter_code) - 1  # liczba liter pomiędzy

print(f"Between {first} and {last} is {number_of_letters} letters")  # wynik