# ===== Zadanie 18 =====

basic_data = {  # pierwszy słownik
    "name": "Barbara",
    "age": 21
}

advanced_data = {  # drugi słownik
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

person = {}  # nowy słownik

person.update(basic_data)  # dodanie danych podstawowych

person.update(advanced_data)  # dodanie danych rozszerzonych

for key, value in person.items():  # wyświetlenie danych
    print(f"{key}: {value}")