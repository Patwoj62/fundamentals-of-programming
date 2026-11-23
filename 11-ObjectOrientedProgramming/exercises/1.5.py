# ===== Zadanie 5 =====

# definicja klasy Book opisującej książkę

class Book:

    # konstruktor uruchamiany podczas tworzenia obiektu
    def __init__(self, title, author, pages, price):

        # tytuł książki, typ str
        self.title = title
        
        # autor książki, typ str
        self.author = author

        # liczba stron książki, typ int
        self.pages = pages

        # cena książki, typ int
        self.price = price

        # aktualna strona książki, typ int
        self.current_page = 1

        # informacja czy książka jest otwarta, typ bool
        self.is_open = False

    # metoda otwierająca książkę
    def open(self):

        # zmiana stanu książki na otwartą
        self.is_open = True

    # metoda zamykająca książkę
    def close(self):

        # zmiana stanu książki na zamkniętą
        self.is_open = False

    # metoda zmieniająca aktualną stronę
    def change_page(self, page):

        # zapis numeru strony przekazanej do metody
        self.current_page = page

    # metoda wyświetlająca informacje o książce
    def display_info(self):

        # wyświetlenie tytułu książki
        print(f"My favourite book is {self.title}.")

        # wyświetlenie autora książki
        print(f"Written by {self.author}.")

        # wyświetlenie liczby stron
        print(f"This book has {self.pages} pages.")

        # wyświetlenie ceny książki
        print(f"The price of this book is {self.price} PLN.")

        # sprawdzenie czy książka jest otwarta
        if self.is_open:

            # wyświetlenie aktualnie czytanej strony
            print(f"I am just reading the book, page {self.current_page}.")

        # wykonanie gdy książka jest zamknięta
        else:

            # komunikat o nieczytanej książce
            print("I am going to read the book later.")


# funkcja główna programu
def main():

    # utworzenie obiektu klasy Book
    favourite_book = Book(

        # tytuł książki, typ str
        "Harry Potter and the Philosopher's Stone",

        # autor książki, typ str
        "J. K. Rowling",

        # liczba stron, typ int
        223,

        # cena książki podana w poleceniu, typ int
        48
    )

    # otwarcie książki
    favourite_book.open()

    # przejście na stronę 15
    favourite_book.change_page(15)

    # wyświetlenie wszystkich informacji o książce
    favourite_book.display_info()

    # zamknięcie książki
    favourite_book.close()


# sprawdzenie czy plik został uruchomiony bezpośrednio
if __name__ == "__main__":

    # uruchomienie funkcji głównej
    main()