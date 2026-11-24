# definicja klasy C
class C:

    # konstruktor klasy
    def __init__(self, sectors):

        # słownik sektorów i liczby kibiców
        self.sectors = sectors

    # zmiana liczby kibiców lub dodanie sektora
    def m1(self, s, n):

        # zapis nowej wartości
        self.sectors[s] = n

    # obliczenie sumy kibiców dla podanych sektorów
    def m2(self, s):

        # suma kibiców
        total = 0

        # przejście przez wszystkie litery napisu
        for sector in s:

            # sprawdzenie czy sektor istnieje
            if sector in self.sectors:

                # dodanie liczby kibiców
                total += self.sectors[sector]

        # zwrócenie wyniku
        return total