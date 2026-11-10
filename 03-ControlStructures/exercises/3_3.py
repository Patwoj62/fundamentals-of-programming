# ===== Zadanie 14 =====

x = int(input('Enter first number: '))  # pobranie pierwszej liczby
y = int(input('Enter second number: '))  # pobranie drugiej liczby

if not x < 0 or not y < 0:  # sprawdzenie czy przynajmniej jedna liczba nie jest ujemna
    print(f'At least one of the numbers {x} and {y} is not negative')  # wyświetlenie komunikatu