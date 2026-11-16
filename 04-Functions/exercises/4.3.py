# ===== Zadanie 2 =====

import math  # import modułu math potrzebnego do pierwiastka

def triangle_area(a, b, c):  # definicja funkcji przyjmującej 3 boki trójkąta
    s = (a + b + c) / 2  # półobwód trójkąta, typ float
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # wzór Herona
    return area  # zwrócenie pola trójkąta

a = float(input("Enter side a: "))  # odczyt boku a z klawiatury
b = float(input("Enter side b: "))  # odczyt boku b z klawiatury
c = float(input("Enter side c: "))  # odczyt boku c z klawiatury

area = triangle_area(a, b, c)  # wywołanie funkcji
print("The area of the triangle is", area)  # wyświetlenie wyniku

print('The area of a triangle with sides 3, 4, 5 is', triangle_area(3, 4, 5))  # wynik 6
print('The area of a triangle with sides 5, 12, 13 is', triangle_area(5, 12, 13))  # wynik 30
print('The area of a triangle with sides 7, 24, 25 is', triangle_area(7, 24, 25))  # wynik 84