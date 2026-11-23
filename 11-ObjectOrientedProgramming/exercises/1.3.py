# ===== Zadanie 3 =====

# definicja klasy TaxiRide
class TaxiRide:

    def __init__(self, rate_per_km):  # konstruktor
        self.rate_per_km = rate_per_km  # stawka za kilometr, typ float
        self.distance = 0  # dystans przejazdu
        self.fare = 0  # koszt przejazdu

    def calculate_fare(self, distance):  # obliczanie ceny
        self.distance = distance  # zapis dystansu
        self.fare = self.distance * self.rate_per_km  # obliczenie należności

    def print_receipt(self):  # drukowanie rachunku
        print("RECEIPT")  # nagłówek
        print(f"Distance: {self.distance} km")  # dystans
        print(f"Rate: €{self.rate_per_km}/km")  # stawka
        print(f"Fare: €{self.fare}")  # należność
        print()  # pusta linia


def main():  # funkcja główna

    ride1 = TaxiRide(2)  # pierwszy kurs
    ride2 = TaxiRide(3)  # drugi kurs

    ride1.calculate_fare(10)  # obliczenie ceny kursu
    ride2.calculate_fare(8)  # obliczenie ceny kursu

    ride1.print_receipt()  # wydruk rachunku
    ride2.print_receipt()  # wydruk rachunku


if __name__ == "__main__":  # sprawdzenie uruchomienia pliku
    main()  # uruchomienie programu