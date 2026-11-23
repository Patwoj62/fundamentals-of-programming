# ===== Zadanie 6 =====

# Program to write movie details to a text file

movie_title = "Inception"                          # str - tytuł filmu

director = "Christopher Nolan"                     # str - reżyser filmu

lead_actor = "Leonardo DiCaprio"                   # str - główny aktor

file_name = "movie_details.txt"                    # str - nazwa pliku wyjściowego

with open(file_name, "w") as file:                 # otwarcie pliku w trybie zapisu (write)

    file.write(f"Movie Title: {movie_title}\n")    # zapisuje tytuł filmu i przechodzi do nowej linii

    file.write(f"Director: {director}\n")          # zapisuje nazwisko reżysera i przechodzi do nowej linii

    file.write(f"Lead Actor: {lead_actor}\n")      # zapisuje nazwisko głównego aktora i przechodzi do nowej linii

print(f"Movie details have been written to {file_name}.")  # wyświetla komunikat o zapisaniu danych