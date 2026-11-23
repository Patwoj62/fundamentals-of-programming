# ===== Zadanie 1 =====

with open("countries.txt", "r") as file:   # otwarcie pliku do odczytu, file = obiekt pliku
    number = 1                             # int - licznik pozycji

    for line in file:                      # pobiera kolejne linie z pliku
        print(f"{number}. {line}", end="") # wyświetla numer i linię, end="" usuwa dodatkową pustą linię
        number += 1                        # zwiększa licznik o 1