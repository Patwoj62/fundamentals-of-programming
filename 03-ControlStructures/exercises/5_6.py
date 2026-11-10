# ===== Zadanie 28 =====

seconds = int(input('Enter number of seconds: '))  # pobranie czasu

while seconds > 0:  # odliczanie do zera

    if seconds == 5:  # pięć sekund
        print('five')

    elif seconds == 4:  # cztery sekundy
        print('four')

    elif seconds == 3:  # trzy sekundy
        print('three')

    elif seconds == 2:  # dwie sekundy
        print('two')

    elif seconds == 1:  # jedna sekunda
        print('one')

    else:  # pozostałe sekundy
        print(seconds)

    seconds -= 1  # zmniejszenie licznika