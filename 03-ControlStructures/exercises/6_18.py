# ===== Zadanie 47 =====

decimal = int(input('Enter decimal number: '))  # pobranie liczby

number = decimal  # kopia liczby
binary = ''  # wynik binarny

while number > 0:  # wykonuj do momentu uzyskania 0

    remainder = number % 2  # obliczenie reszty z dzielenia przez 2
    binary = str(remainder) + binary  # dopisanie bitu na początek
    number = number // 2  # dzielenie całkowite przez 2

print(f'{decimal}(10) = {binary}(2)')  # wyświetlenie wyniku