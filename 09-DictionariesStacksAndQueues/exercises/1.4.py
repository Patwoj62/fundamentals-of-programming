# ===== Zadanie 2 =====

person = {  # słownik zawierający dane osoby
    "name": "Marek",  # imię, str
    "surname": "Banach",  # nazwisko, str
    "age": 25,  # wiek, int
    "hobby": ["swimming", "excursions"],  # lista hobby, list
    "married": True,  # stan cywilny, bool
    "phone": {  # zagnieżdżony słownik
        "landline": "123444321",  # telefon stacjonarny, str
        "mobile": "777888999"  # telefon komórkowy, str
    }
}

print(person["name"])  # wyświetlenie imienia

print(person["hobby"])  # wyświetlenie hobby

print(person)  # wyświetlenie całego słownika

person["surname"] = "Nowak"  # zmiana nazwiska

person["married"] = False  # zmiana statusu małżeńskiego

person["gender"] = "male"  # dodanie nowego klucza gender

person["hobby"].append("bicycle")  # dodanie nowego hobby do listy

person["phone"]["work"] = "313131444"  # dodanie telefonu służbowego

for key, value in person.items():  # iteracja po słowniku
    print(f"{key}: {value}")  # wyświetlenie danych osoby