# ===== Zadanie 8 =====

driving_mode = input('Enter driving mode (A/M/E): ')  # pobranie trybu jazdy
distance = int(input('Enter distance in km: '))  # pobranie dystansu

if driving_mode == 'A':  # tryb Auto
    fuel_consumption = 7  # spalanie 7 l/100 km
elif driving_mode == 'M':  # tryb Manual
    fuel_consumption = 9  # spalanie 9 l/100 km
elif driving_mode == 'E':  # tryb Eco
    fuel_consumption = 6  # spalanie 6 l/100 km
else:  # nieprawidłowy tryb
    fuel_consumption = 0  # zabezpieczenie przed błędem

total_consumption = distance * fuel_consumption / 100  # obliczenie całkowitego spalania

print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')  # wyświetlenie wyniku