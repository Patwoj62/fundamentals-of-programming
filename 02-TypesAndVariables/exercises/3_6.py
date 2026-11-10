# ===== Zadanie 13 ====

import math                                   # import modułu matematycznego

h = float(input("Height in meters: "))        # pobranie wysokości obserwatora
d = 3.57 * math.sqrt(h)                       # obliczenie odległości do horyzontu

print("Distance to horizon:", round(d, 2), "km")  # wyświetlenie wyniku