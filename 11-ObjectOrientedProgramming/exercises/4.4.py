# ===== Zadanie 14 =====

# import klasy Ebook z pliku ebook.py
from ebook import Ebook


# funkcja główna programu
def main():

    # utworzenie obiektu książki
    book = Ebook(
        "Harry Potter and the Philosopher's Stone",
        "J. K. Rowling",
        223
    )

    # otwarcie książki
    book.open_book()

    # wyświetlenie danych książki
    book.show_status()

    print()

    # przeczytanie kilku stron
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()

    # ponowne wyświetlenie statusu
    book.show_status()

    print()

    # zamknięcie książki
    book.close_book()

    print()

    # próba czytania po zamknięciu
    book.next_page()
    book.next_page()


# uruchomienie programu
if __name__ == "__main__":
    main()