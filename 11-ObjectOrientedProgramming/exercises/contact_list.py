# ===== Zadanie 18 =====

# import klasy Contact
from contact import Contact


# definicja klasy ContactList
class ContactList:

    # konstruktor klasy
    def __init__(self):

        # lista kontaktów, typ list
        self.contacts = []

    # dodawanie nowego kontaktu
    def add_contact(self, contact):

        # dodanie obiektu Contact do listy
        self.contacts.append(contact)

    # wyświetlenie wszystkich kontaktów
    def display_contacts(self):

        # nagłówek
        print("CONTACT LIST")
        print("============")

        # przejście po wszystkich kontaktach
        for contact in self.contacts:

            # wyświetlenie kontaktu
            print(contact)