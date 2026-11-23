# ===== Zadanie 21 =====

# Copies books of selected genres
# to separate files

import csv                                                  # moduł do obsługi CSV
import os                                                   # moduł do obsługi ścieżek

def save_books_by_genre(input_file, genre, output_file):    # funkcja zapisująca książki danego gatunku

    with open(input_file, "r", encoding="utf-8", newline="") as file: # otwarcie books.csv

        reader = csv.DictReader(file)                       # odczyt danych CSV jako słownik

        with open(output_file, "w", encoding="utf-8") as out: # utworzenie pliku wynikowego

            for row in reader:                              # przejście po wszystkich książkach

                if row["Genre"] == genre:                   # sprawdzenie gatunku książki

                    out.write(
                        f'{row["Title"]},{row["Author"]},{row["Year"]}\n'
                    )                                       # zapis danych książki do pliku

folder = os.path.dirname(os.path.abspath(__file__))         # str - folder programu

books_file = os.path.join(folder, "books.csv")             # str - ścieżka do books.csv

fantasy_file = os.path.join(folder, "books_fantasy.txt")   # str - plik Fantasy

historical_file = os.path.join(folder, "books_historical.txt") # str - plik Historical

romance_file = os.path.join(folder, "books_romance.txt")   # str - plik Romance

classic_file = os.path.join(folder, "books_classic.txt")   # str - plik Classic

save_books_by_genre(
    books_file,                                             # plik źródłowy
    "Fantasy",                                              # gatunek
    fantasy_file                                            # plik wynikowy
)

save_books_by_genre(
    books_file,                                             # plik źródłowy
    "Historical",                                           # gatunek
    historical_file                                         # plik wynikowy
)

save_books_by_genre(
    books_file,                                             # plik źródłowy
    "Romance",                                              # gatunek
    romance_file                                            # plik wynikowy
)

save_books_by_genre(
    books_file,                                             # plik źródłowy
    "Classic",                                              # gatunek
    classic_file                                            # plik wynikowy
)

print("Books saved to files.")                              # komunikat końcowy