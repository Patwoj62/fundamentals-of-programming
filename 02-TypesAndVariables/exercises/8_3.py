# ===== Zadanie 46 ====

cm = 170                                   # wzrost w centymetrach
total_inches = int(cm / 2.54)              # zamiana cm na cale
feet = total_inches // 12                  # liczba pełnych stóp
inches = total_inches % 12                 # pozostałe cale

print(f"I am {cm}cm tall, i.e. {feet} feet and {inches} inches")  # wyświetlenie wyniku
