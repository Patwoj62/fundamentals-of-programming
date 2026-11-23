# ===== Zadanie 2 =====

# definicja klasy Square
class Square:

    def __init__(self, a):  # konstruktor
        self.a = a  # długość boku, typ int

    def area(self):  # metoda licząca pole
        return self.a * self.a  # wzór na pole kwadratu

    def perimeter(self):  # metoda licząca obwód
        return 4 * self.a  # wzór na obwód kwadratu


square1 = Square(4)  # utworzenie pierwszego kwadratu
square2 = Square(6)  # utworzenie drugiego kwadratu

print("Square with side 4:")  # opis pierwszego kwadratu
print(f"Area is {square1.area()}, Perimeter is {square1.perimeter()}")  # wyniki

print("Square with side 6:")  # opis drugiego kwadratu
print(f"Area is {square2.area()}, Perimeter is {square2.perimeter()}")  # wyniki