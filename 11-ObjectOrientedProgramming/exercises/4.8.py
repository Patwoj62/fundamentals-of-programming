# ===== Zadanie 18 =====

# import klasy Contact
from contact import Contact

# import klasy ContactList
from contact_list import ContactList


# funkcja główna programu
def main():

    # utworzenie obiektu listy kontaktów
    phone_contacts = ContactList()

    # utworzenie pierwszego kontaktu
    contact1 = Contact(
        "John Brown",
        "brown@onet.pl",
        "555234000"
    )

    # utworzenie drugiego kontaktu
    contact2 = Contact(
        "Anna May",
        "am@o2.pl",
        "232000199"
    )

    # utworzenie trzeciego kontaktu
    contact3 = Contact(
        "George Small",
        "smallg@google.pl",
        "222999100"
    )

    # utworzenie czwartego kontaktu
    contact4 = Contact(
        "Paola Big",
        "bigpaola@poczta.pl",
        "100200300"
    )

    # dodanie pierwszego kontaktu
    phone_contacts.add_contact(contact1)

    # dodanie drugiego kontaktu
    phone_contacts.add_contact(contact2)

    # dodanie trzeciego kontaktu
    phone_contacts.add_contact(contact3)

    # dodanie czwartego kontaktu
    phone_contacts.add_contact(contact4)

    # dodanie nowego kontaktu
    phone_contacts.add_contact(
        Contact(
            "Tom White",
            "white@gmail.com",
            "777888999"
        )
    )

    # wyświetlenie wszystkich kontaktów
    phone_contacts.display_contacts()


# uruchomienie programu
if __name__ == "__main__":
    main()