# definicja klasy Statistics
class Statistics:

    # konstruktor klasy
    def __init__(self):

        # lista liczb, typ list
        self.numbers = []

    # dodanie liczby do zbioru
    def add_number(self, number):

        # dopisanie liczby do listy
        self.numbers.append(number)

    # wyświetlenie wszystkich liczb
    def display_numbers(self):

        # wyświetlenie nagłówka
        print("Numbers:")

        # przejście po wszystkich liczbach
        for number in self.numbers:

            # wyświetlenie liczby z odstępem
            print(number, end=" ")

        # przejście do nowej linii
        print()

    # wyznaczenie największej liczby
    def maximum(self):

        # zwrócenie maksimum
        return max(self.numbers)

    # wyznaczenie najmniejszej liczby
    def minimum(self):

        # zwrócenie minimum
        return min(self.numbers)

    # obliczenie średniej
    def mean(self):

        # suma liczb podzielona przez ich ilość
        return sum(self.numbers) / len(self.numbers)

    # obliczenie mediany
    def median(self):

        # utworzenie posortowanej kopii listy
        sorted_numbers = sorted(self.numbers)

        # liczba elementów
        n = len(sorted_numbers)

        # środkowy indeks
        middle = n // 2

        # przypadek nieparzystej liczby elementów
        if n % 2 == 1:

            # zwrócenie środkowej liczby
            return sorted_numbers[middle]

        # przypadek parzystej liczby elementów
        else:

            # obliczenie średniej dwóch środkowych liczb
            return (
                sorted_numbers[middle - 1]
                + sorted_numbers[middle]
            ) / 2

    # wyświetlenie statystyk
    def display_statistics(self):

        # wyświetlenie minimum
        print(f"Minimum: {self.minimum()}")

        # wyświetlenie maksimum
        print(f"Maximum: {self.maximum()}")

        # wyświetlenie średniej
        print(f"Mean: {self.mean():.2f}")

        # wyświetlenie mediany
        print(f"Median: {self.median()}")