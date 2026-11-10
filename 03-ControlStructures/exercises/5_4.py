# ===== Zadanie 26 =====

total_sum = 0  # przechowuje sumę liczb
count = 0  # licznik podanych liczb

while True:  # pętla nieskończona

    number = int(input("Enter a number (0 to stop): "))  # pobranie liczby

    if number == 0:  # zakończenie programu
        break  # wyjście z pętli

    total_sum += number  # dodanie liczby do sumy
    count += 1  # zwiększenie licznika

if count > 0:  # jeżeli podano co najmniej jedną liczbę
    average = total_sum / count  # obliczenie średniej
else:  # jeśli nie podano żadnej liczby
    average = 0  # średnia równa 0

print(f"The total sum of the numbers is: {total_sum}")  # wyświetlenie sumy
print(f"The arithmetic mean is: {average}")  # wyświetlenie średniej