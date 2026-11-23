# ===== Zadanie 1 =====

import os                                           # moduł operacji na plikach

folder = os.path.dirname(__file__)                  # str - folder, w którym znajduje się 1.5.py

file_path = os.path.join(folder, "countries.txt")   # str - pełna ścieżka do pliku

with open(file_path, "r") as file:   # otwarcie pliku do odczytu, file = obiekt pliku
    number = 1                             # int - licznik pozycji

    for line in file:                      # pobiera kolejne linie z pliku
        print(f"{number}. {line}", end="") # wyświetla numer i linię, end="" usuwa dodatkową pustą linię
        number += 1                        # zwiększa licznik o 1