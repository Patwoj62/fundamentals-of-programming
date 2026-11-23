# ===== Zadanie 18 =====

import csv                                                  # moduł do obsługi CSV
import os                                                   # moduł do obsługi ścieżek

folder = os.path.dirname(os.path.abspath(__file__))         # str - folder programu

file_path = os.path.join(folder, "it_company.csv")          # str - plik znajduje się obok programu

print("GRAPHIC DESIGNERS")                                  # nagłówek

print("=================")                                    # separator

with open(file_path, "r", newline="") as file:             # otwarcie pliku CSV

    reader = csv.DictReader(file)                           # odczyt CSV jako słownik

    for row in reader:                                      # przejście po rekordach

        if row["Job Title"] == "Graphic Designer":          # sprawdzenie stanowiska

            print(f'{row["First Name"]} {row["Last Name"]},{row["Email"]}') # wyświetlenie danych