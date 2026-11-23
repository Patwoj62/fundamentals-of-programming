# ===== Zadanie 31 =====

import json  # obsługa json

data = {  # słownik danych pacjenta

    "patient_record": {

        "patient_id": "P001234",

        "first_name": "John",

        "last_name": "Doe",

        "date_of_birth": "1985-05-15",

        "gender": "Male"
    }
}

file_name = "patient.json"  # nazwa pliku

with open(file_name, "w") as file:  # otwarcie pliku do zapisu

    json.dump(data, file, indent=4)  # zapis json

print("Data has been written to", file_name)  # komunikat