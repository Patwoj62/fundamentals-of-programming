# ===== Zadanie 37 ====

import math                                   # import biblioteki matematycznej

circumference = float(input("Enter tree circumference in cm: "))  # pobranie obwodu
diameter = circumference / math.pi            # obliczenie średnicy
can_be_cut = diameter >= 50                   # sprawdzenie warunku wycinki

print(f"Tree can be cut down: {can_be_cut}")  # wyświetlenie wyniku