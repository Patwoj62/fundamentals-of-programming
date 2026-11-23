# ===== Zadanie 2 =====

def read_from_file(name):                  # funkcja odczytująca cały plik
    with open(name, "r") as file:          # otwarcie pliku do odczytu
        content = file.read()              # str - odczyt całej zawartości pliku
    return content                         # zwraca tekst z pliku

file_content = read_from_file("countries.txt")  # str - cała zawartość pliku

file_lines = file_content.splitlines()     # list - podział tekstu na linie

file_lines = sorted(file_lines)            # list - sortowanie alfabetyczne

for line in file_lines:                    # przechodzi przez wszystkie elementy listy
    print(line)                            # wyświetla każdą linię