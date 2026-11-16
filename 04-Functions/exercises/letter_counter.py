# ===== Zadanie 13 =====

def count_letter(text, letter):  # funkcja licząca wystąpienia znaku
    counter = 0  # licznik wystąpień

    for char in text:  # przejście po każdym znaku tekstu
        if char == letter:  # sprawdzenie czy znak jest szukaną literą
            counter += 1  # zwiększenie licznika

    return counter  # zwrócenie wyniku