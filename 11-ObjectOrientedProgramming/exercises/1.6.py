# ===== Zadanie 6 =====

# definicja klasy Phone
class Phone:

    def __init__(self, brand):  # konstruktor
        self.brand = brand  # marka telefonu, typ str
        self.battery_level = 50  # poziom baterii, typ int
        self.is_on = False  # stan telefonu, typ bool

    def turn_on(self):  # włączenie telefonu
        self.is_on = True  # zmiana stanu na włączony

    def turn_off(self):  # wyłączenie telefonu
        self.is_on = False  # zmiana stanu na wyłączony

    def charge(self):  # ładowanie telefonu
        self.battery_level = 100  # pełne naładowanie

    def display_info(self):  # wyświetlenie informacji
        print(f"Brand: {self.brand}")  # marka
        print(f"Battery: {self.battery_level}%")  # bateria
        print(f"Power state: {self.is_on}")  # stan telefonu


phone = Phone("Samsung")  # utworzenie obiektu

phone.turn_on()  # włączenie telefonu
phone.charge()  # naładowanie telefonu

phone.display_info()  # wyświetlenie danych

phone.turn_off()  # wyłączenie telefonu