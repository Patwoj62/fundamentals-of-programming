# ===== Zadanie 35 =====

numbers = (50, 20, 40, 50, 30, 50)  # krotka liczb

value = 50  # szukana wartość

counter = 0  # licznik wystąpień

for number in numbers:  # przechodzi po elementach

    if number == value:  # sprawdza zgodność wartości

        counter += 1  # zwiększa licznik

print("Tuple:", numbers)  # wyświetla krotkę

print("Value:", value)  # wyświetla szukaną wartość

print("Number of occurrences:", counter)  # wyświetla liczbę wystąpień