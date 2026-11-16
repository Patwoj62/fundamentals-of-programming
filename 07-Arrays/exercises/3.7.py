# ===== Zadanie 25 =====

numbers = [15, 8, 31, 47, 2, 19]  # lista liczb

total = 0  # suma elementów
i = 0  # indeks

while i < len(numbers):  # działa do końca listy
    total += numbers[i]  # dodaje element do sumy
    i += 1  # kolejny indeks

average = total / len(numbers)  # oblicza średnią

print("Array:", numbers)  # wyświetla listę
print("Average:", average)  # wyświetla średnią