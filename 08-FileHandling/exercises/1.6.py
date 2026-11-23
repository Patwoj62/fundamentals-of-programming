# ===== Zadanie 2 =====

import os                                                     # moduł do obsługi ścieżek plików

def read_from_file(name):                                     # funkcja odczytująca cały plik

    with open(name, "r") as file:                             # otwarcie pliku do odczytu

        content = file.read()                                 # str - odczyt całej zawartości pliku

    return content                                            # zwraca zawartość pliku

folder = os.path.dirname(__file__)                            # str - folder zawierający bieżący program

file_path = os.path.join(folder, "countries.txt")             # str - pełna ścieżka do pliku countries.txt

file_content = read_from_file(file_path)                      # str - zawartość pliku

file_lines = file_content.splitlines()                        # list - podział tekstu na osobne linie

file_lines = sorted(file_lines)                               # list - sortowanie alfabetyczne

for line in file_lines:                                       # przechodzi po wszystkich liniach listy

    print(line)                                               # wyświetla kolejną linię