# ===== Zadanie 24 =====

numbers = [15, 8, 31, 47, 2, 19]  # lista liczb

total = 0  # suma elementów

for number in numbers:  # przejście po liczbach
    total += number  # dodaje liczbę do sumy

average = total / len(numbers)  # oblicza średnią

print("Array:", numbers)  # wyświetla listę
print("Average:", average)  # wyświetla średnią