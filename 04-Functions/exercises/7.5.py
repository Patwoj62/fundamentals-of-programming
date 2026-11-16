# ===== Zadanie 14 =====

import range_check  # import modułu

number = 7  # testowana liczba

result = range_check.in_range(number, 2, 15)  # sprawdzenie przedziału

if result:  # jeśli wynik True
    print(f'Number {number} in the range <2,15>: yes')  # wyświetlenie yes
else:  # jeśli wynik False
    print(f'Number {number} in the range <2,15>: no')  # wyświetlenie no