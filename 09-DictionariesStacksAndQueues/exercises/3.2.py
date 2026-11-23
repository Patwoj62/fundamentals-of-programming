# ===== Zadanie 11 =====


stack = []  # stos przechowujący odwiedzone strony

while True:  # pętla działa do momentu zakończenia programu
    website = input("Website name or BACK: ")  # pobranie danych od użytkownika

    if website.upper() == "BACK":  # sprawdzenie czy użytkownik wybrał BACK

        if len(stack) > 0:  # sprawdzenie czy stos nie jest pusty
            print("Previous website:", stack.pop())  # pobranie ostatniej strony
        else:  # gdy nie ma zapisanych stron
            print("No previously visited websites")  # komunikat

    elif website.upper() == "EXIT":  # zakończenie programu
        break  # wyjście z pętli

    else:  # użytkownik podał nową stronę
        stack.append(website)  # zapisanie strony na stos