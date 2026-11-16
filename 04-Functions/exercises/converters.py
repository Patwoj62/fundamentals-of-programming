# ===== Zadanie 8 =====

def m_to_cm(n):  # funkcja zamieniająca metry na centymetry
    return n * 100  # zwraca wynik w cm

def cm_to_m(n):  # funkcja zamieniająca centymetry na metry
    return n / 100  # zwraca wynik w m

def cm_to_inches(n):  # funkcja zamieniająca centymetry na cale
    return n / 2.54  # 1 cal = 2.54 cm

def feet_inches_to_cm(feet, inches):  # funkcja zamieniająca stopy i cale na cm
    total_inches = feet * 12 + inches  # przeliczenie wszystkiego na cale
    return total_inches * 2.54  # zamiana cali na cm

if __name__ == "__main__":  # wykonaj tylko przy uruchomieniu tego pliku
    print(f'2m = {m_to_cm(2)}cm')  # test funkcji m_to_cm
    print(f'532cm = {cm_to_m(532)}m')  # test funkcji cm_to_m
    print(f'10cm = {cm_to_inches(10)}in')  # test funkcji cm_to_inches
    print(f'5ft 10in = {feet_inches_to_cm(5,10)}cm')  # test funkcji feet_inches_to_cm
