# ===== Zadanie 23 ====

a = float(input("a="))                      # pobranie pierwszego boku
b = float(input("b="))                      # pobranie drugiego boku
c = float(input("c="))                      # pobranie trzeciego boku
volume = a * b * c                          # obliczenie objętości (w zadaniu literówka jest a = 3, b = 4, c = 5 --> volume = 94, surface area = 60)
surface_area = 2 * (a * b + a * c + b * c) # obliczenie pola powierzchni

print(f"Volume = {volume}")                 # wyświetlenie objętości
print(f"Surface area = {surface_area}")     # wyświetlenie pola powierzchni889