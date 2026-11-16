# ===== Zadanie 15 =====

def hide(card_number):  # funkcja przyjmująca numer karty jako str
    return card_number[:2] + '*' * 10 + card_number[-4:]  # pozostawia 2 pierwsze i 4 ostatnie cyfry

print(hide("5290312400019022"))  # test funkcji