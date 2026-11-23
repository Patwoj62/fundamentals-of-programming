# ===== Zadanie 29 =====

import json  # obsługa plików json

with open(r"C:\Users\Patryk\OneDrive\Desktop\fundamentals-of-programming\09-DictionariesStacksAndQueues\exercises\dogs.json", "r", encoding="utf-8") as file:  
    # otwarcie pliku (with open("dogs.json", "r", encoding="utf-8") as file:)
    dogs = json.load(file)  # wczytanie danych

for dog in dogs:  # przejście po wszystkich psach

    if dog["age"] < 5:  # sprawdzenie wieku

        print("Name:", dog["name"])  # wyświetlenie imienia

        print("Breed:", dog["breed"])  # wyświetlenie rasy

        print("Age:", dog["age"])  # wyświetlenie wieku

        print("Weight:", dog["weight_kg"])  # wyświetlenie wagi

        print("Owner:", dog["owner"])  # wyświetlenie właściciela

        print("Vaccinated:", dog["vaccinated"])  # szczepienie

        print()  # pusta linia między rekordami