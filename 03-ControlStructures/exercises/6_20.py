# ===== Zadanie 49 =====

for i in range(1, 31):  # zakres od 1 do 30

    if i % 3 == 0 and i % 5 == 0:  # podzielne przez 3 i 5
        print('BINGO', end=' ')  # wyświetlenie BINGO

    elif i % 3 == 0:  # podzielne przez 3
        print('THREE', end=' ')  # wyświetlenie THREE

    elif i % 5 == 0:  # podzielne przez 5
        print('FIVE', end=' ')  # wyświetlenie FIVE

    else:  # pozostałe liczby
        print(i, end=' ')  # wyświetlenie liczby