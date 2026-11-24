# definicja klasy Contact
class Contact:

    # konstruktor klasy
    def __init__(self, name, email, telephone):

        # imię i nazwisko kontaktu, typ str
        self.name = name

        # adres e-mail, typ str
        self.email = email

        # numer telefonu, typ str
        self.telephone = telephone

    # tekstowa reprezentacja obiektu
    def __str__(self):

        # zwrócenie danych kontaktu w postaci tekstu
        return (
            f"{self.name} | "
            f"{self.email} | "
            f"{self.telephone}"
        )