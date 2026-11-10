# ===== Zadanie 34 =====

hours = int(input('Enter parking time in hours: '))  # liczba godzin

if hours <= 2:  # od 1 do 2 godzin
    fee = 5  # opłata 5 PLN

elif hours <= 6:  # od 3 do 6 godzin
    fee = 15  # opłata 15 PLN

else:  # powyżej 6 godzin
    fee = 20  # opłata 20 PLN

print(f'Parking fee: {fee} PLN')  # wyświetlenie wyniku