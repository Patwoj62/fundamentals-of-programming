# ===== Zadanie 21 =====

import csv  # obsługa plików csv

provinces = {}  # słownik województw

with open(r"C:\Users\Patryk\OneDrive\Desktop\fundamentals-of-programming\09-DictionariesStacksAndQueues\exercises\province.csv", "r", encoding="utf-8") as file:  
    # otwarcie pliku csv (with open("province.csv", "r", encoding="utf-8") as file:  # otwarcie pliku csv)

    reader = csv.DictReader(file)  # odczyt danych csv

    for row in reader:  # przejście po rekordach

        provinces[row["Letter"]] = row["Name"]  # litera -> województwo

counter = {}  # licznik pojazdów

for province in provinces.values():  # inicjalizacja liczników

    counter[province] = 0  # początkowo 0 pojazdów

with open(r"C:\Users\Patryk\OneDrive\Desktop\fundamentals-of-programming\09-DictionariesStacksAndQueues\exercises\vehicle.txt", "r", encoding="utf-8" ) as file:  
    # otwarcie pliku z numerami (with open("vehicle.txt", "r", encoding="utf-8") as file:) 

    for line in file:  # przejście po numerach rejestracyjnych

        registration = line.strip()  # usunięcie białych znaków

        if registration != "":  # pominięcie pustych linii

            letter = registration[0]  # pierwsza litera rejestracji

            if letter in provinces:  # sprawdzenie czy litera istnieje

                province = provinces[letter]  # pobranie nazwy województwa

                counter[province] += 1  # zwiększenie licznika

for province, count in counter.items():  # wyświetlenie wyników

    print(f"{province}: {count}")