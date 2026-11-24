# ===== Zadanie 15 =====

# import klasy Thermometer
from thermometer import Thermometer


# funkcja główna programu
def main():

    # utworzenie obiektu termometru
    thermometer = Thermometer()

    # włączenie termometru
    thermometer.turn_on()

    # wykonanie pomiaru
    thermometer.measure_temperature()

    # wyświetlenie wyniku pomiaru
    thermometer.show_temperature()

    # wyłączenie termometru
    thermometer.turn_off()


# uruchomienie programu
if __name__ == "__main__":
    main()