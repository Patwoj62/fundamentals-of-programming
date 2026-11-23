# ===== Zadanie 3 =====

import os                                                     # moduł do obsługi ścieżek

def read_from_file(name):                                     # funkcja odczytująca cały plik

    with open(name, "r") as file:                             # otwarcie pliku

        content = file.read()                                 # str - zawartość pliku

    return content                                            # zwrot zawartości

folder = os.path.dirname(__file__)                            # str - folder programu

file_path = os.path.join(folder, "car_park.txt")              # str - ścieżka do pliku car_park.txt

file_content = read_from_file(file_path)                      # str - zawartość pliku

file_lines = file_content.splitlines()                        # list - lista liczb zapisanych jako tekst

total = 0                                                     # int - suma wszystkich samochodów

for line in file_lines:                                       # przechodzenie po kolejnych liniach

    total += int(line)                                        # zamiana str na int i dodanie do sumy

print("Total cars parked:", total)                            # wyświetlenie wyniku