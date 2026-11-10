# ===== Zadanie 52 =====

correct_pin = '0805'  # poprawny PIN

attempts = 0  # licznik prób

while attempts < 3:  # maksymalnie 3 próby

    entered_pin = input('Enter the PIN code: ')  # pobranie PIN

    if entered_pin == correct_pin:  # poprawny PIN

        print('Correct PIN')  # komunikat sukcesu
        break  # zakończenie pętli

    else:  # błędny PIN

        print('Incorrect...')  # komunikat błędu
        attempts += 1  # zwiększenie licznika

if attempts == 3:  # trzy błędne próby

    print('Sorry, your payment card has been blocked.')  # blokada karty