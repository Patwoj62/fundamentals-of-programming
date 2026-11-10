# ===== Zadanie 16 =====

month = int(input('Enter month number (1..12): '))  # pobranie miesiąca
day = int(input('Enter the day number of the month: '))  # pobranie dnia

day_ok = False  # początkowo dzień uznajemy za niepoprawny

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # miesiące 31-dniowe
    if day >= 1 and day <= 31:  # sprawdzenie zakresu dni
        day_ok = True  # dzień poprawny

elif month == 4 or month == 6 or month == 9 or month == 11:  # miesiące 30-dniowe
    if day >= 1 and day <= 30:  # sprawdzenie zakresu dni
        day_ok = True  # dzień poprawny

elif month == 2:  # luty
    if day >= 1 and day <= 28:  # zakres dni dla lutego
        day_ok = True  # dzień poprawny

message = f'Day {day} for the month {month}'  # przygotowanie komunikatu

if day_ok:  # jeśli dzień jest poprawny
    print(f'{message} is correct')  # wyświetlenie poprawnej daty
else:  # jeśli dzień nie jest poprawny
    print(f'{message} is incorrect')  # wyświetlenie błędnej daty