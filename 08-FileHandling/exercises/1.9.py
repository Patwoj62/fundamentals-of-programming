# ===== Zadanie 5 =====

import os                                                     # moduł do obsługi ścieżek

file_name = "it_company.csv"                                  # str - nazwa pliku

job_title = "Software Engineer"                               # str - szukane stanowisko

number = 1                                                    # int - numer znalezionego pracownika

folder = os.path.dirname(__file__)                            # str - folder programu

file_path = os.path.join(folder, file_name)                   # str - pełna ścieżka do pliku

with open(file_path, "r") as file:                            # otwarcie pliku do odczytu

    for line in file:                                         # pobieranie kolejnych wierszy

        if job_title in line:                                 # sprawdzenie czy stanowisko występuje w wierszu

            print(f"{number}. {line.strip()}")                # wyświetlenie numeru i danych pracownika

            number += 1                                       # zwiększenie numeru o 1