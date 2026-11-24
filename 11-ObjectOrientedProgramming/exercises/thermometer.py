# import modułu random do losowania temperatury
import random


# definicja klasy Thermometer
class Thermometer:

    # konstruktor klasy
    def __init__(self):

        # informacja czy termometr jest włączony, typ bool
        self.is_on = False

        # aktualna temperatura, typ float
        self.temperature = 34.0

    # włączenie termometru
    def turn_on(self):

        # zmiana stanu na włączony
        self.is_on = True

        # komunikat
        print("Thermometer ON")

    # wyłączenie termometru
    def turn_off(self):

        # zmiana stanu na wyłączony
        self.is_on = False

        # komunikat
        print("Thermometer OFF")

    # pomiar temperatury
    def measure_temperature(self):

        # sprawdzenie czy termometr jest włączony
        if self.is_on:

            # losowanie temperatury od 34.0 do 42.0
            self.temperature = round(
                random.uniform(34.0, 42.0),
                1
            )

        else:

            # komunikat jeśli termometr jest wyłączony
            print("Thermometer is OFF")

    # wyświetlenie temperatury
    def show_temperature(self):

        # sprawdzenie czy termometr jest włączony
        if self.is_on:

            # temperatura krytyczna
            if self.temperature >= 41.0:

                print(
                    f"Temperature: {self.temperature}C "
                    f"(fever)"
                )

                print("CRITICAL TEMPERATURE!!")

            # gorączka
            elif self.temperature >= 37.0:

                print(
                    f"Temperature: {self.temperature}C "
                    f"(fever)"
                )

            # temperatura normalna
            else:

                print(
                    f"Temperature: {self.temperature}C"
                )

        else:

            # komunikat gdy termometr jest wyłączony
            print("Thermometer is OFF")