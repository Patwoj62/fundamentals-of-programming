# ===== Zadanie 8 =====

temperatures = [  # lista temperatur z marca typu list
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

measurements = len(temperatures)  # liczba wykonanych pomiarów

temp_total = 0  # zmienna przechowująca sumę temperatur typu int

for temp in temperatures:  # przechodzi przez wszystkie temperatury
    temp_total = temp_total + temp  # dodaje kolejną temperaturę do sumy

avg_temp = temp_total / measurements  # oblicza średnią temperaturę

min_temp = min(temperatures)  # znajduje najmniejszą temperaturę
max_temp = max(temperatures)  # znajduje największą temperaturę

negative_temp = 0  # licznik dni z temperaturą poniżej 0
i = 0  # indeks typu int

while i < len(temperatures):  # wykonuje pętlę dla wszystkich elementów listy
    if temperatures[i] < 0:  # sprawdza czy temperatura jest ujemna
        negative_temp += 1  # zwiększa licznik temperatur ujemnych
    i += 1  # przechodzi do kolejnego indeksu

print("TEMPERATURE REPORT")  # nagłówek raportu
print("Month: March")  # nazwa miesiąca
print("Number of measurements:", measurements)  # liczba pomiarów
print("Average temperature in the month:", avg_temp)  # średnia temperatura
print("Minimum temperature:", min_temp)  # temperatura minimalna
print("Maximum temperature:", max_temp)  # temperatura maksymalna
print("Number of days with negative temperature:", negative_temp)  # liczba dni z mrozem