# ===== Zadanie 20 =====

# Calculates, prints and saves numbers
# from 1 to 100 with their powers

import os                                                   # moduł do obsługi ścieżek

folder = os.path.dirname(os.path.abspath(__file__))         # str - folder programu

file_path = os.path.join(folder, "powers.txt")             # str - ścieżka do pliku wynikowego

with open(file_path, "w") as file:                         # utworzenie pliku do zapisu

    for number in range(1, 101):                           # int - liczby od 1 do 100

        square = number ** 2                               # int - druga potęga liczby

        cube = number ** 3                                 # int - trzecia potęga liczby

        line = f"{number},{square},{cube}"                 # str - dane do wyświetlenia i zapisania

        print(line)                                         # wyświetlenie danych na ekranie

        file.write(line + "\n")                            # zapis danych do pliku

print("Data saved to powers.txt")                          # komunikat końcowy