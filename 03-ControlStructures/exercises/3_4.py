# ===== Zadanie 15 =====

month = int(input('Enter month number (1..12): '))  # pobranie numeru miesiąca

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # miesiące mające 31 dni
    days = 31  # liczba dni w miesiącu
elif month == 4 or month == 6 or month == 9 or month == 11:  # miesiące mające 30 dni
    days = 30  # liczba dni w miesiącu
elif month == 2:  # luty
    days = 28  # luty ma 28 dni

print(f'Month {month} has {days} days')  # wyświetlenie wyniku