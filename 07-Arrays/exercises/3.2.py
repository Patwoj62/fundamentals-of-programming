# ===== Zadanie 20 =====

numbers = [34, 7, 19, 4, 21, 8]  # lista liczb całkowitych

count = 0  # licznik liczb parzystych
i = 0  # indeks

while i < len(numbers):  # przejście po wszystkich elementach
    if numbers[i] % 2 == 0:  # sprawdza parzystość
        count += 1  # zwiększa licznik
    i += 1  # kolejny indeks

print("Even numbers:", count)  # wyświetla wynik