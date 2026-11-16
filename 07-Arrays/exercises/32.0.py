# ===== Zadanie 38 =====

arr = [7, 9, 2, 4, 5, 6]  # lista liczb

even = []  # lista liczb parzystych

odd = []  # lista liczb nieparzystych

for number in arr:  # przechodzi po wszystkich elementach

    if number % 2 == 0:  # sprawdza parzystość

        even.append(number)  # dodaje do listy parzystych

    else:  # dla liczb nieparzystych

        odd.append(number)  # dodaje do listy nieparzystych

arr = even + odd  # łączy listy

print(arr)  # wyświetla wynik