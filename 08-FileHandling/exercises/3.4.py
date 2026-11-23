# ===== Zadanie 11 =====

# Calculates the total value of money spent

import re                                                    # moduł wyrażeń regularnych
import os                                                    # moduł obsługi ścieżek

email_file = "report.txt"                                   # str - nazwa pliku z raportem

folder = os.path.dirname(os.path.abspath(__file__))         # str - folder programu

file_path = os.path.join(folder, email_file)               # str - pełna ścieżka do pliku

with open(file_path, "r", encoding="utf-8") as file:       # otwarcie pliku UTF-8

    email = file.read()                                     # str - odczyt całej zawartości pliku

pattern = r"€(\d+)"                                         # regex - liczba występująca po znaku euro

amounts = re.findall(pattern, email)                        # list - znalezione kwoty

total = 0                                                   # int - suma wydatków

for amount in amounts:                                      # przejście po znalezionych kwotach

    total += int(amount)                                    # zamiana tekstu na liczbę i dodanie do sumy

print("Total spent:", total)                                # wyświetlenie wyniku
