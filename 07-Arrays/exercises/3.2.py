# ===== Zadanie 20 =====

numbers = [15, 8, 31, 47, 2, 19]  # lista liczb

print("Existing array:", end=" ")  # napis bez nowej linii

for number in numbers:  # przejście po liście
    print(number, end=" ")  # wyświetla element

print()  # nowa linia

print("Reverse array:", end=" ")  # nagłówek

for i in range(len(numbers) - 1, -1, -1):  # przejście od końca do początku
    print(numbers[i], end=" ")  # wyświetla odwróconą kolejność