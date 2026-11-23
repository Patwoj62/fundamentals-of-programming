# ===== Zadanie 14 =====

import queue  # import modułu kolejek

files_to_print = queue.Queue()  # utworzenie kolejki FIFO

while True:  # pętla programu

    print("1. Add file to print")  # opcja dodawania pliku
    print("2. Print file")  # opcja drukowania pliku
    print("0. Quit")  # opcja zakończenia programu

    menu = input("Select an option: ")  # pobranie wyboru użytkownika

    if menu == "1":  # dodawanie pliku do kolejki

        file_name = input("Enter file name to print: ")  # nazwa pliku

        files_to_print.put(file_name)  # dodanie pliku na koniec kolejki

        print("File added to queue.")  # komunikat

    elif menu == "2":  # drukowanie pliku

        if not files_to_print.empty():  # sprawdzenie czy kolejka nie jest pusta

            file_to_print = files_to_print.get()  # pobranie pierwszego pliku z kolejki

            print(f"File {file_to_print} is currently being printed. Please wait!")  # komunikat

        else:  # gdy kolejka jest pusta

            print("No files to print.")  # komunikat o pustej kolejce

    elif menu == "0":  # zakończenie programu

        break  # wyjście z pętli