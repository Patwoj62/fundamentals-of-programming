# ===== Zadanie 10 =====

month = int(input('Enter month number (1..12): '))  # pobranie numeru miesiąca

if month >= 10:  # miesiące 10-12
    quarter = 4  # czwarty kwartał
elif month >= 7:  # miesiące 7-9
    quarter = 3  # trzeci kwartał
elif month >= 4:  # miesiące 4-6
    quarter = 2  # drugi kwartał
else:  # miesiące 1-3
    quarter = 1  # pierwszy kwartał

print(f'Month {month} is in quarter {quarter}')  # wyświetlenie wyniku