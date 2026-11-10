# ===== Zadanie 27 =====

N = 10  # górna granica zakresu
sum_even = 0  # zmienna przechowująca sumę

i = 1  # licznik

while i <= N:  # wykonuj aż do N

    if i % 2 == 0:  # sprawdzenie liczby parzystej
        sum_even += i  # dodanie do sumy

    i += 1  # przejście do następnej liczby

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")  # wynik