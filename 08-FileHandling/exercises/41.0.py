# ===== Zadanie 19 =====

# Prints products with price less than 60
# and stock quantity less than 40

import csv                                                  # moduł do obsługi plików CSV
import os                                                   # moduł do obsługi ścieżek

folder = os.path.dirname(os.path.abspath(__file__))         # str - folder programu

file_path = os.path.join(folder, "clothing.csv")            # str - ścieżka do pliku clothing.csv

with open(file_path, "r", newline="") as file:             # otwarcie pliku CSV

    reader = csv.DictReader(file)                           # odczyt danych jako słownik

    print("PRODUCTS")                                       # nagłówek

    print("========")                                       # separator

    for row in reader:                                      # przechodzi przez wszystkie rekordy

        price = float(row["Price"])                         # float - cena produktu

        stock = int(row["Stock_Quantity"])                  # int - ilość sztuk w magazynie

        if price < 60 and stock < 40:                       # sprawdza warunek zadania

            print(
                f'{row["Product_Name"]}, {price}, {stock}'
            )                                               # wyświetla dane produktu