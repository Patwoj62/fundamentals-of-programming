# ===== Zadanie 8 =====

import os                                                     # moduł do obsługi ścieżek

original_file = "healthy_lifestyle.txt"                       # str - plik źródłowy

target_file = "copy_healthy_lifestyle.txt"                    # str - plik docelowy

folder = os.path.dirname(os.path.abspath(__file__))           # str - pełna ścieżka folderu z 2.3.py

source_path = os.path.join(folder, original_file)             # str - pełna ścieżka do healthy_lifestyle.txt

target_path = os.path.join(folder, target_file)               # str - pełna ścieżka do pliku kopii

with open(source_path, "r") as file:                          # otwarcie pliku źródłowego

    content = file.read()                                     # str - odczyt całej zawartości

with open(target_path, "w") as file:                          # utworzenie pliku docelowego

    file.write(content)                                       # zapis treści do kopii

print("File copied.")                                         # komunikat końcowy