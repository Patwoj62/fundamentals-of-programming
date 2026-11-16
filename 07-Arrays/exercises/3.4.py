# ===== Zadanie 22 =====

numbers = [-15, 8, -31, 47, -2, 19]  # lista liczb

minimum = numbers[0]  # początkowe minimum
maximum = numbers[0]  # początkowe maksimum

for number in numbers:  # przejście po elementach

    if number < minimum:  # znalezienie nowego minimum
        minimum = number  # zapis minimum

    if number > maximum:  # znalezienie nowego maksimum
        maximum = number  # zapis maksimum

print("Minimum:", minimum)  # wyświetla minimum
print("Maximum:", maximum)  # wyświetla maksimum