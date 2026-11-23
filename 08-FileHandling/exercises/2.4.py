# ===== Zadanie 9 =====

import os                                                     # moduł do obsługi ścieżek

employees_file = "it_company.csv"                             # str - plik z pracownikami

position_file = "software_engineer.txt"                       # str - plik wynikowy

job_title = "Software Engineer"                               # str - szukane stanowisko

folder = os.path.dirname(os.path.abspath(__file__))           # str - folder programu

employees_path = os.path.join(folder, employees_file)         # str - pełna ścieżka do pliku pracowników

position_path = os.path.join(folder, position_file)           # str - pełna ścieżka do pliku wynikowego

with open(employees_path, "r") as employees:                 # otwarcie pliku wejściowego

    with open(position_path, "w") as output:                 # utworzenie pliku wynikowego

        for line in employees:                               # pobiera kolejne wiersze pliku

            if job_title in line:                            # sprawdza czy wiersz zawiera stanowisko

                output.write(line)                           # zapisuje wiersz do pliku wynikowego

print("Data saved to file.")                                 # komunikat końcowy