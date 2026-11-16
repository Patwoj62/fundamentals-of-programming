# ===== Zadanie 26 =====

def star(n):  # funkcja zwraca podaną liczbę gwiazdek

    return "*" * n  # tworzy napis z gwiazdek

numbers = [2, 6, 4, 9, 7]  # lista liczb

for number in numbers:  # przechodzi po wszystkich liczbach
    print(str(number) + ":", star(number))  # wyświetla liczbę i gwiazdki