# ===== Zadanie 17 =====

import re                                                   # moduł wyrażeń regularnych
import os                                                   # moduł obsługi ścieżek

folder = os.path.dirname(os.path.abspath(__file__))         # folder programu

file_path = os.path.join(folder, "files.txt")               # ścieżka do pliku

with open(file_path, "r") as file:                          # otwarcie pliku

    for line in file:                                       # pobiera kolejne nazwy plików

        line = line.strip()                                 # usuwa znak końca linii

        if re.search(r"\.[a-zA-Z]{4}$", line):              # rozszerzenie ma dokładnie 4 znaki

            print(line)                                     # wyświetla nazwę pliku