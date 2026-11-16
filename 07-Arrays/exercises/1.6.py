# ===== Zadanie 3 =====

def weekday(n):  # funkcja przyjmująca numer dnia tygodnia
    weekdays = [  # lista nazw dni tygodnia
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    return weekdays[n - 1]  # zwraca dzień dla numeru 1-7

print(weekday(1))  # wypisuje Monday
print(weekday(4))  # wypisuje Thursday
print(weekday(7))  # wypisuje Sunday