# ===== Zadanie 17 =====

# import klasy Statistics
from statistics import Statistics


# funkcja główna programu
def main():

    # utworzenie obiektu Statistics
    stats = Statistics()

    # dodanie liczb z polecenia
    stats.add_number(12)
    stats.add_number(37)
    stats.add_number(6)
    stats.add_number(9)
    stats.add_number(17)

    # pobranie kolejnej liczby od użytkownika
    number = int(input("Enter next number: "))

    # dodanie liczby do listy
    stats.add_number(number)

    # wyświetlenie wszystkich liczb
    stats.display_numbers()

    # wyświetlenie statystyk
    stats.display_statistics()


# uruchomienie programu
if __name__ == "__main__":
    main()