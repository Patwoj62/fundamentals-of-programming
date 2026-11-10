# ===== Zadanie 31 =====

light_switch1 = False  # pierwszy przełącznik
light_switch2 = False  # drugi przełącznik
bulbs_on = 0  # liczba zapalonych żarówek

if light_switch1:  # pierwszy przełącznik steruje jedną żarówką
    bulbs_on += 1  # dodanie jednej żarówki
    
if light_switch2:  # drugi przełącznik steruje dwiema żarówkami
    bulbs_on += 2  # dodanie dwóch żarówek

print(f'Bulbs on: {bulbs_on}')  # wyświetlenie liczby zapalonych żarówek