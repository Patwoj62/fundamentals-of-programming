# ===== Zadanie 33 =====

import json  # obsługa json

product = {}  # pusty słownik

product["name"] = input("Product name: ")  # nazwa produktu typu str

product["price"] = float(input("Price: "))  # cena typu float

paid = input("Paid (yes/no): ")  # odpowiedź użytkownika

product["paid"] = paid.lower() == "yes"  # konwersja na bool

with open("product.json", "w") as file:  # otwarcie pliku

    json.dump(product, file, indent=4)  # zapis do json

print("Product saved")  # komunikat