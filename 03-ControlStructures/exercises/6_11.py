# ===== Zadanie 40 =====

speed_limit_min = 40  # minimalna prędkość
speed_limit_max = 140  # maksymalna prędkość

car_speed = int(input('Enter car speed: '))  # pobranie prędkości

if car_speed < speed_limit_min or car_speed > speed_limit_max:  # sprawdzenie zakresu
    print('Warning: invalid car speed!!')  # komunikat ostrzegawczy