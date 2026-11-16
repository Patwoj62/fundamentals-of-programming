# ===== Zadanie 31 =====

def f(name):  # funkcja przyjmuje tekst
    words = name.split()  # podział tekstu na wyrazy
    acronym = ''  # zmienna na akronim

    for word in words:  # przejście po wszystkich wyrazach
        acronym += word[0]  # dodanie pierwszej litery wyrazu

    return acronym  # zwrócenie akronimu

print(f("Internet of Things"))  # IoT
print(f("For Your Information"))  # FYI
print(f("Python"))  # P