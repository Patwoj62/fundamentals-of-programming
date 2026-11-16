# ===== Zadanie 16 =====

meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):  # funkcja zwracająca nazwę dnia tygodnia
    weekdays = [  # lista dni tygodnia
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    return weekdays[n - 1]  # zwraca dzień dla numeru 1-7


def day_meal_plan(meal_plan, day_number):  # funkcja tworząca plan posiłków dnia

    meals = meal_plan[day_number - 1]  # pobiera posiłki wybranego dnia

    return ", ".join(meals)  # łączy elementy w jeden napis oddzielony przecinkami


print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

for day in range(1, 8):  # przechodzi po dniach 1-7
    print(weekday(day) + ":", day_meal_plan(meal_plan, day))  # wyświetla dzień i posiłki