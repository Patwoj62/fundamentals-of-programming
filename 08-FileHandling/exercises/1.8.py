# ===== Zadanie 4 =====

import os                                                     # moduł do obsługi ścieżek

folder = os.path.dirname(__file__)                            # str - folder programu

file_path = os.path.join(folder, "pets.txt")                  # str - ścieżka do pliku pets.txt

word_count = 0                                                # int - licznik wszystkich słów

with open(file_path, "r") as file:                            # otwarcie pliku do odczytu

    for line in file:                                         # pobieranie kolejnych linii

        print(line, end="")                                   # wyświetlenie tekstu z pliku

        words = line.split()                                  # list - podział linii na słowa

        word_count += len(words)                              # dodanie liczby słów do licznika

print("\nNumber of words:", word_count)                       # wyświetlenie łącznej liczby słów