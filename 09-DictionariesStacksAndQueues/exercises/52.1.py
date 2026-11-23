# ===== Zadanie 32 =====

import json  # obsługa json

favourite = {  # słownik filmu

    "title": "Interstellar",  # str

    "director": "Christopher Nolan",  # str

    "year": 2014,  # int

    "genre": "Science Fiction",  # str

    "rating": 10  # int

}

with open("favourite.json", "w") as file:  # utworzenie pliku

    json.dump(favourite, file, indent=4)  # zapis danych

print("File saved")  # komunikat