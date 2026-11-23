# ===== Zadanie 30 =====

import json  # import modułu json

def count_rooms(reservations):  # liczba rezerwacji

    return len(reservations)  # zwrócenie liczby pokoi

def count_paid(reservations):  # liczba opłaconych

    count = 0  # licznik

    for reservation in reservations:

        if reservation["paid"]:

            count += 1

    return count

def count_unpaid(reservations):  # liczba nieopłaconych

    count = 0

    for reservation in reservations:

        if not reservation["paid"]:

            count += 1

    return count

def total_paid_value(reservations):  # suma opłaconych

    total = 0

    for reservation in reservations:

        if reservation["paid"]:

            total += reservation["nights"] * reservation["price_per_night"]

    return total

def total_unpaid_value(reservations):  # suma nieopłaconych

    total = 0

    for reservation in reservations:

        if not reservation["paid"]:

            total += reservation["nights"] * reservation["price_per_night"]

    return total

with open(r"C:\Users\Patryk\OneDrive\Desktop\fundamentals-of-programming\09-DictionariesStacksAndQueues\exercises\reservations.json", "r", encoding="utf-8") as file:  
    # otwarcie pliku with open("reservations.json", "r", encoding="utf-8") as file: 

    data = json.load(file)  # odczyt danych

reservations = data["reservations"]  # pobranie listy rezerwacji

print("Number of rooms:", count_rooms(reservations))  # liczba pokoi

print("Number of paid reservations:", count_paid(reservations))  # opłacone

print("Number of unpaid reservations:", count_unpaid(reservations))  # nieopłacone

print("Total value of paid reservations:", total_paid_value(reservations))  # suma opłaconych

print("Total value of unpaid reservations:", total_unpaid_value(reservations))  # suma nieopłaconych