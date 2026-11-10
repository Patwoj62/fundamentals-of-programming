# ===== Zadanie 18 =====

university = 'Krakow University of Economics'  # nazwa uczelni
university_expanded = ''  # pusty napis na wynik

for char in university:  # przejście po wszystkich znakach napisu
    university_expanded = university_expanded + char + ' '  # dodanie znaku i spacji

print(university)  # oryginalna nazwa uczelni
print(university_expanded)  # nazwa z odstępami