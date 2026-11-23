# ===== Zadanie 28 =====

import json  # import modułu do obsługi JSON

with open(r"C:\Users\Patryk\OneDrive\Desktop\fundamentals-of-programming\09-DictionariesStacksAndQueues\exercises\cities.json", "r", encoding="utf-8") as file:  
    # otwarcie pliku JSON (with open("cities.json", "r", encoding="utf-8") as file:)

    data = json.load(file)  # wczytanie tablicy słowników

for city in data:  # przejście po wszystkich miastach

    for key, value in city.items():  # przejście po parach klucz-wartość

        print(key, ":", value)  # wyświetlenie danych

    print()  # pusta linia między miastami