# ===== Zadanie 33 =====

numbers = (10, 20, 30, 40, 50)  # krotka typu tuple

print("Tuple:", numbers)  # wyświetla oryginalną krotkę

print("Reverse order:", end=" ")  # nagłówek

for i in range(len(numbers) - 1, -1, -1):  # przejście od końca

    print(numbers[i], end=" ")  # wyświetla element
