# definicja klasy C
class C:

    # konstruktor klasy
    def __init__(self, name, surname, age, seniority):

        # imię pracownika, typ str
        self.name = name

        # nazwisko pracownika, typ str
        self.surname = surname

        # wiek pracownika, typ int
        self.age = age

        # staż pracy, typ int
        self.seniority = seniority

    # tekstowa reprezentacja obiektu
    def __str__(self):

        # utworzenie tekstu zgodnie z poleceniem
        result = (
            self.surname +
            self.name[0] +
            str(self.seniority)
        )

        # sprawdzenie pełnoletności
        if self.age >= 18:

            # zwrócenie wielkich liter
            return result.upper()

        else:

            # zwrócenie małych liter
            return result.lower()