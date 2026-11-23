# ===== Zadanie 3 =====

countries = [  # lista słowników
    {"name": "Poland", "population": 38000000},  # słownik nr 1
    {"name": "Germany", "population": 83000000},  # słownik nr 2
    {"name": "France", "population": 68000000},  # słownik nr 3
    {"name": "Spain", "population": 48000000},  # słownik nr 4
    {"name": "Italy", "population": 59000000}  # słownik nr 5
]

print("COUNTRY\tPOPULATION")  # nagłówek tabeli

for country in countries:  # przejście po elementach listy
    print(f"{country['name']}\t{country['population']}")  # wyświetlenie danych kraju