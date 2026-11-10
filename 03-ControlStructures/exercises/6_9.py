# ===== Zadanie 38 =====

human_years = int(input('Enter the dog age in human years: '))  # wiek psa

if human_years <= 2:  # pierwsze dwa lata
    dog_years = human_years * 10.5  # przeliczenie wieku

else:  # kolejne lata
    dog_years = 21 + (human_years - 2) * 4  # wzór z treści zadania

print(f"The dog's age in dog years is {dog_years} years.")  # wynik