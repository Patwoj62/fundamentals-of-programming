# ===== Zadanie 20 =====

# import klasy C
from stadium import C

# utworzenie obiektu stadionu
stadium = C({
    "A": 120,
    "D": 150,
    "G": 90,
    "K": 110
})

# zmiana liczby kibiców w sektorze G
stadium.m1("G", 130)

# suma sektorów G i D
print(stadium.m2("GD"))

# suma sektorów K, E i J
print(stadium.m2("KEJ"))