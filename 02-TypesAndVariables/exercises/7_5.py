# ===== Zadanie 38 ====

car_number = input("Enter car registration number: ")  # pobranie numeru
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"  # sprawdzenie prefiksu

print(f"Car is from Krakow: {is_krakow}")   # wyświetlenie wyniku