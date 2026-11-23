# ===== Zadanie 7 =====

# definicja klasy Song opisującej utwór muzyczny
class Song:

    # konstruktor uruchamiany przy tworzeniu obiektu
    def __init__(self, artist, title, album, year):

        # wykonawca utworu, typ str
        self.artist = artist

        # tytuł utworu, typ str
        self.title = title

        # nazwa albumu, typ str
        self.album = album

        # rok wydania utworu, typ int
        self.year = year

    # specjalna metoda zwracająca reprezentację tekstową obiektu
    def __str__(self):

        # zwrócenie danych utworu w postaci tekstu wieloliniowego
        return (f"Performer: {self.artist}\n"
                f"Title:     {self.title}\n"
                f"Album:     {self.album}\n"
                f"Year:      {self.year}")


# utworzenie pierwszego obiektu klasy Song
song1 = Song(
    "Ed Sheeran",  # wykonawca
    "Hearts Don't Break Around Here",  # tytuł
    "Divide",  # album
    2017  # rok wydania
)

# utworzenie drugiego obiektu klasy Song
song2 = Song(
    "Queen",  # wykonawca
    "Bohemian Rhapsody",  # tytuł
    "A Night at the Opera",  # album
    1975  # rok wydania
)

# wyświetlenie informacji o pierwszym utworze
print(song1)

# pusty wiersz pomiędzy utworami
print()

# wyświetlenie informacji o drugim utworze
print(song2)