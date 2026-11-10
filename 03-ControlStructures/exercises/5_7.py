# ===== Zadanie 29 =====

pin = "1234"  # domyślny PIN

while True:  # menu główne programu

    print("1 - Check PIN")  # opcja sprawdzenia PIN
    print("2 - Change PIN")  # opcja zmiany PIN
    print("3 - Exit")  # zakończenie programu

    choice = input("Choose option: ")  # wybór użytkownika

    if choice == "1":  # sprawdzanie PIN

        entered_pin = input("Enter PIN: ")  # pobranie PIN

        if entered_pin == pin:  # porównanie PIN
            print("Correct PIN")  # poprawny PIN
        else:  # błędny PIN
            print("Incorrect PIN")  # komunikat błędu

    elif choice == "2":  # zmiana PIN

        new_pin = input("Enter new PIN: ")  # pobranie nowego PIN

        if len(new_pin) == 4 and new_pin.isdigit():  # PIN ma dokładnie 4 cyfry
            pin = new_pin  # zapis nowego PIN
            print("PIN changed successfully")  # potwierdzenie
        else:  # nieprawidłowy PIN
            print("PIN must contain exactly 4 digits")  # komunikat błędu

    elif choice == "3":  # wyjście z programu
        break  # zakończenie pętli

    else:  # błędny wybór
        print("Incorrect option")  # komunikat błędu