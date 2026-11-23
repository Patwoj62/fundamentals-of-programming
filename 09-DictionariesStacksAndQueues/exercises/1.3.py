# ===== Zadanie 1 =====

mobile = {  # słownik (dict) przechowujący dane telefonu
    "Brand": "Samsung",  # klucz Brand, wartość typu str
    "Model": "Galaxy S23",  # klucz Model, wartość typu str
    "OS": "Android",  # system operacyjny, str
    "Storage": "256 GB",  # pamięć telefonu, str
    "RAM": "8 GB",  # pamięć RAM, str
    "Color": "Black"  # kolor telefonu, str
}

for key, value in mobile.items():  # przejście po wszystkich parach klucz-wartość
    print(f"{key} : {value}")  # wyświetlenie klucza i wartości