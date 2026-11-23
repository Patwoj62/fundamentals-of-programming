# ===== Zadanie 26 =====

import json  # import modułu json

person = {  # słownik Python
    "name": "Barbara",  # str
    "age": 21,  # int
    "student": True  # bool
}

with open("person.json", "w", encoding="utf-8") as file:  # utworzenie pliku

    json.dump(person, file, indent=4)  # zapis danych do JSON

print("File saved")  # komunikat