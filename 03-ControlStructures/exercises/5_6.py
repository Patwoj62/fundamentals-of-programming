# ===== Zadanie 28 =====

import time  # moduł obsługujący opóźnienia

countdown = int(input("Enter the number of seconds to count down: "))  # pobranie liczby sekund

while countdown > 0:  # wykonuj dopóki licznik jest większy od zera

    if countdown == 5:  # gdy pozostało 5 sekund
        print("five")  # wyświetlenie słowa five

    elif countdown == 4:  # gdy pozostały 4 sekundy
        print("four")  # wyświetlenie słowa four

    elif countdown == 3:  # gdy pozostały 3 sekundy
        print("three")  # wyświetlenie słowa three

    elif countdown == 2:  # gdy pozostały 2 sekundy
        print("two")  # wyświetlenie słowa two

    elif countdown == 1:  # gdy pozostała 1 sekunda
        print("one")  # wyświetlenie słowa one

    else:  # dla pozostałych wartości
        print(countdown)  # wyświetlenie liczby

    countdown -= 1  # zmniejszenie licznika o 1

    time.sleep(1)  # odczekanie jednej sekundy

print("Time's up!")  # zakończenie odliczania