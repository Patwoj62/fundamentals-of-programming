# ===== Zadanie 15 =====

monthly_expenses = [
    [200, 50, 100],   # Week 1
    [180, 60, 110],   # Week 2
    [220, 55, 105],   # Week 3
    [210, 65, 95]     # Week 4
]

food_total = 0  # suma wydatków na jedzenie
transport_total = 0  # suma wydatków na transport
utilities_total = 0  # suma wydatków na media

for week in monthly_expenses:  # przechodzi po wszystkich tygodniach
    food_total += week[0]  # dodaje koszt jedzenia
    transport_total += week[1]  # dodaje koszt transportu
    utilities_total += week[2]  # dodaje koszt mediów

week1 = sum(monthly_expenses[0])  # suma wydatków tygodnia 1
week2 = sum(monthly_expenses[1])  # suma wydatków tygodnia 2
week3 = sum(monthly_expenses[2])  # suma wydatków tygodnia 3
week4 = sum(monthly_expenses[3])  # suma wydatków tygodnia 4

total = 0  # całkowita suma wydatków

for week in monthly_expenses:  # przechodzi po wszystkich tygodniach
    for expense in week:  # przechodzi po wszystkich wydatkach tygodnia
        total += expense  # dodaje wydatek do całkowitej sumy

print("MONTHLY EXPENSES")
print("----------------")
print("Food:", food_total)
print("Transport:", transport_total)
print("Utilities:", utilities_total)

print("Week 1:", week1)
print("Week 2:", week2)
print("Week 3:", week3)
print("Week 4:", week4)

print("---------------")
print("TOTAL:", total)