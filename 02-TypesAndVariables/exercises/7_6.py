# ===== Zadanie 39 ====

speed = int(input("Enter vehicle speed: "))  # pobranie prędkości
speed_valid = speed >= 40 and speed <= 140   # sprawdzenie zakresu

print(f"Speed is valid: {speed_valid}")      # wyświetlenie wyniku