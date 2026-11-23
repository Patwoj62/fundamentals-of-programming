# ===== Zadanie 15 =====

import os                                                   # moduł obsługi ścieżek

file_name = input("File name: ")                            # str - nazwa pliku podana przez użytkownika

folder = os.path.dirname(os.path.abspath(__file__))         # str - folder programu

file_path = os.path.join(folder, file_name)                # str - pełna ścieżka do pliku

try:                                                        # początek obsługi wyjątków

    with open(file_path, "r", encoding="utf-8") as file:   # otwarcie pliku

        content = file.read()                               # str - zawartość pliku

    lines = content.splitlines()                            # list - linie tekstu

    line_count = len(lines)                                 # int - liczba linii

    char_count = len(content)                               # int - liczba znaków

    word_count = len(content.split())                       # int - liczba słów

    print("Number of lines:", line_count)                   # wyświetlenie liczby linii

    print("Number of characters:", char_count)              # wyświetlenie liczby znaków

    print("Number of words:", word_count)                   # wyświetlenie liczby słów

except FileNotFoundError:                                   # obsługa błędu braku pliku

    print("File not found.")                                # komunikat błędu