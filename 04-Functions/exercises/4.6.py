# ===== Zadanie 5 =====

def day_name(day_number):  # definicja funkcji
    result = ''  # zmienna na nazwę dnia

    if day_number == 1:  # sprawdzenie numeru dnia
        result = 'Monday'  # poniedziałek
    elif day_number == 2:  # dzień 2
        result = 'Tuesday'  # wtorek
    elif day_number == 3:  # dzień 3
        result = 'Wednesday'  # środa
    elif day_number == 4:  # dzień 4
        result = 'Thursday'  # czwartek
    elif day_number == 5:  # dzień 5
        result = 'Friday'  # piątek
    elif day_number == 6:  # dzień 6
        result = 'Saturday'  # sobota
    elif day_number == 7:  # dzień 7
        result = 'Sunday'  # niedziela

    return result  # zwrócenie nazwy dnia

print('The name of day 5 in the week is', day_name(5))  # Friday
print('The name of day 3 in the week is', day_name(3))  # Wednesday
print('The name of day 7 in the week is', day_name(7))  # Sunday