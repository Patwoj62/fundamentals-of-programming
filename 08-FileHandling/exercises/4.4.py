# ===== Zadanie 13 =====

import os                                                   # moduł do obsługi ścieżek

folder = os.path.dirname(os.path.abspath(__file__))         # folder programu

file_path = os.path.join(folder, "it_company.csv")          # ścieżka do pliku

with open(file_path, "r") as file:                          # otwarcie pliku

    lines = file.readlines()                                # list - wszystkie linie pliku

for i in range(0, len(lines), 5):                           # co 5 linii

    for line in lines[i:i+5]:                               # pobiera kolejne 5 linii

        print(line.strip())                                 # wyświetla linię

    input("Press Enter key...")                             # oczekiwanie na Enter