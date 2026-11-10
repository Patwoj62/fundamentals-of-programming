# ===== Zadanie 42 =====

ean = input('Enter EAN-13 article number: ')  # pobranie numeru

if len(ean) == 13 and ean.isdigit():  # sprawdzenie długości i cyfr

    print('Article number is correct')  # numer poprawny

    if ean.startswith('590'):  # produkty z Polski
        print('Article manufactured in Poland')  # komunikat o pochodzeniu