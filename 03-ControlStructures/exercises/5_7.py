# ===== Zadanie 29 =====

balance = 1000  # początkowe saldo
pin = '1111'  # początkowy 4-cyfrowy PIN

while True:  # główna pętla programu

    print()  # pusta linia

    print("ATM Menu:")  # nagłówek menu
    print("1. Check balance")  # sprawdzenie salda
    print("2. Deposit")  # wpłata
    print("3. Withdraw")  # wypłata
    print("4. Check PIN")  # sprawdzenie PIN
    print("5. Change PIN")  # zmiana PIN
    print("6. Exit")  # wyjście

    choice = input("Choose an option (1-6): ")  # pobranie wyboru

    print()  # pusta linia

    if choice == '1':  # sprawdzanie salda
        print(f"Your current balance is: €{balance}")  # wyświetlenie salda

    elif choice == '2':  # wpłata środków
        amount = float(input("Enter the amount to deposit: "))  # kwota wpłaty
        balance += amount  # zwiększenie salda

        print(f"€{amount} has been deposited. New balance: €{balance}")  # komunikat

    elif choice == '3':  # wypłata środków
        amount = float(input("Enter the amount to withdraw: "))  # kwota wypłaty

        if amount <= balance:  # sprawdzenie dostępnych środków
            balance -= amount  # zmniejszenie salda
            print(f"€{amount} has been withdrawn. New balance: €{balance}")  # komunikat

        else:  # brak środków
            print("Insufficient balance.")  # komunikat błędu

    elif choice == '4':  # sprawdzenie PIN
        entered_pin = input("Enter PIN: ")  # pobranie PIN

        if entered_pin == pin:  # porównanie PIN
            print("PIN is correct")  # poprawny PIN

        else:  # błędny PIN
            print("Incorrect PIN")  # komunikat błędu

    elif choice == '5':  # zmiana PIN
        current_pin = input("Enter current PIN: ")  # pobranie starego PIN

        if current_pin == pin:  # sprawdzenie poprawności PIN
            new_pin = input("Enter new PIN: ")  # pobranie nowego PIN

            if len(new_pin) == 4 and new_pin.isdigit():  # dokładnie 4 cyfry
                pin = new_pin  # zapis nowego PIN
                print("PIN changed successfully")  # potwierdzenie zmiany

            else:  # błędny format PIN
                print("PIN must contain exactly 4 digits")  # komunikat błędu

        else:  # niepoprawny aktualny PIN
            print("Incorrect current PIN")  # komunikat błędu

    elif choice == '6':  # zakończenie programu

        print("Exiting... Thank you for using the ATM!")  # komunikat końcowy
        break  # wyjście z pętli

    else:  # niepoprawna opcja

        print("Invalid option. Please try again.")  # komunikat błędu