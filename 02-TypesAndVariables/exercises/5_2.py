# ===== Zadanie 22 ====

cube_side_string = input("Enter cube side: ")     # pobranie długości krawędzi jako tekst
cube_side = int(cube_side_string)                 # zamiana tekstu na liczbę całkowitą
cube_volume = cube_side ** 3                      # obliczenie objętości sześcianu
cube_surface_area = 6 * cube_side ** 2            # obliczenie pola powierzchni sześcianu

print(f"The volume of a cube with side {cube_side} is {cube_volume}")  # wyświetlenie objętości
print(f"The surface area of a cube with side {cube_side} is {cube_surface_area}")  # wyświetlenie pola powierzchni