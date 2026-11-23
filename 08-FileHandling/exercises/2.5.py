# ===== Zadanie 10 =====

import os                                                     # moduł do obsługi ścieżek

folder = os.path.dirname(os.path.abspath(__file__))           # str - folder programu

shopping_list = os.path.join(folder, "shopping_list.txt")     # str - pełna ścieżka do pliku

def add_product(file_name, product_name):                    # funkcja zapisująca produkt

    with open(file_name, "a") as file:                       # otwarcie pliku w trybie dopisywania

        file.write(product_name + "\n")                      # zapis produktu do nowej linii

product = ""                                                 # str - nazwa produktu

while product != "0":                                        # pętla działa do wpisania 0

    product = input("Enter product name (0 stops): ")        # pobranie danych od użytkownika

    if product == "0":                                       # sprawdza warunek zakończenia

        break                                                # kończy pętlę

    else:                                                    # dla zwykłych produktów

        add_product(shopping_list, product)                  # zapisuje produkt do pliku

print("Shopping list saved.")                                # komunikat końcowy