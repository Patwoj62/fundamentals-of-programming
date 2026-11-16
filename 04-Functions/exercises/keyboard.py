# ===== Zadanie 9 =====

def input_string(message):  # funkcja zwracająca napis
    text = input(message)  # wczytanie tekstu typu str
    return text  # zwrócenie tekstu

def input_integer(message):  # funkcja zwracająca liczbę całkowitą
    number = input(message)  # odczyt danych jako str
    return int(number)  # konwersja na int

def input_real(message):  # funkcja zwracająca liczbę rzeczywistą
    number = input(message)  # odczyt danych jako str
    return float(number)  # konwersja na float

def input_boolean(message):  # funkcja zwracająca wartość logiczną
    value = input(message)  # odczyt odpowiedzi użytkownika
    return value.lower() == 'y'  # True dla y, False dla innych znaków