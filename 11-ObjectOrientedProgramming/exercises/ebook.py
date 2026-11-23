# definicja klasy Ebook
class Ebook:

    # konstruktor klasy
    def __init__(self, title, author, pages):

        # tytuł książki, typ str
        self.title = title

        # autor książki, typ str
        self.author = author

        # liczba stron, typ int
        self.pages = pages

        # aktualna strona, typ int
        self.current_page = 1

        # informacja czy książka jest otwarta, typ bool
        self.is_open = False

    # otwarcie książki
    def open_book(self):

        # ustawienie stanu otwarcia
        self.is_open = True

        # komunikat
        print("Book opened")

    # zamknięcie książki
    def close_book(self):

        # ustawienie stanu zamknięcia
        self.is_open = False

        # komunikat
        print("Book closed")

    # przejście do następnej strony
    def next_page(self):

        # sprawdzenie czy książka jest otwarta
        if self.is_open:

            # sprawdzenie czy nie osiągnięto końca książki
            if self.current_page < self.pages:

                # przejście do następnej strony
                self.current_page += 1

        else:

            # komunikat gdy książka jest zamknięta
            print("Book is closed")

    # przejście do poprzedniej strony
    def previous_page(self):

        # sprawdzenie czy książka jest otwarta
        if self.is_open:

            # sprawdzenie czy aktualna strona jest większa od 1
            if self.current_page > 1:

                # przejście do poprzedniej strony
                self.current_page -= 1

        else:

            # komunikat gdy książka jest zamknięta
            print("Book is closed")

    # wyświetlenie informacji o książce
    def show_status(self):

        # wyświetlenie tytułu
        print(f"Title: {self.title}")

        # wyświetlenie autora
        print(f"Author: {self.author}")

        # wyświetlenie liczby stron
        print(f"Pages: {self.pages}")

        # wyświetlenie aktualnej strony
        print(f"Current page: {self.current_page}")

        # wyświetlenie stanu książki
        print(f"Opened: {self.is_open}")