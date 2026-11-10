# ===== Zadanie 48 ====

distance = int(input("Enter distance in km: "))     # pobranie odległości
fuel_price = float(input("Enter fuel price per liter: "))  # pobranie ceny paliwa
fuel_consumption = float(input("Enter fuel consumption per 100 km: "))  # spalanie
total_fuel_consumption = distance * fuel_consumption / 100  # całkowite zużycie paliwa
total_cost = total_fuel_consumption * fuel_price    # całkowity koszt transportu

print(f"Total fuel consumption: {total_fuel_consumption}")  # wyświetlenie spalania
print(f"Total transport cost: {total_cost}")        # wyświetlenie kosztu