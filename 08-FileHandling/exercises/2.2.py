# ===== Zadanie 7 =====

# Writes Seven Wonders of the World to a file

seven_wonders = [                                  # list - lista siedmiu cudów świata
    "Great Wall of China",                         # str - element listy
    "Petra",                                       # str - element listy
    "Christ the Redeemer",                         # str - element listy
    "Machu Picchu",                                # str - element listy
    "Chichen Itza",                                # str - element listy
    "Roman Colosseum",                             # str - element listy
    "Taj Mahal"                                    # str - element listy
]

file_name = "seven_wonders.txt"                    # str - nazwa pliku

seven_wonders = sorted(seven_wonders)              # list - sortowanie alfabetyczne

with open(file_name, "w") as file:                 # otwarcie pliku do zapisu

    for item in seven_wonders:                     # pobiera kolejne elementy listy

        file.write(item + "\n")                    # zapisuje nazwę i przechodzi do nowej linii

print("Data saved to file.")                       # informacja o zakończeniu programu