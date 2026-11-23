# definicja klasy TV
class TV:

    # konstruktor klasy
    def __init__(self):

        # telewizor początkowo wyłączony
        self.is_on = False

    # włączenie telewizora
    def turn_on(self):
        self.is_on = True

    # wyłączenie telewizora
    def turn_off(self):
        self.is_on = False

    # wyświetlenie stanu telewizora
    def show_status(self):

        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")