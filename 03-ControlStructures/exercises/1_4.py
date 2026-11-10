# ===== Zadanie 4 =====

number = int(input('Enter number: '))  # pobranie liczby od użytkownika

if number % 2 == 0:  # reszta z dzielenia przez 2 równa 0 oznacza liczbę parzystą
    print(f'{number} is even')  # wyświetlenie informacji o liczbie parzystej
else:  # w przeciwnym razie liczba jest nieparzysta
    print(f'{number} is odd')  # wyświetlenie informacji o liczbie nieparzystej