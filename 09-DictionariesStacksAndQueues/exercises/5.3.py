# ===== Zadanie 15 =====

translations = {  # słownik tłumaczeń
    "computer": "komputer",  # str -> str
    "mouse": "myszka",
    "keyboard": "klawiatura",
    "printer": "drukarka"
}

word = input("Enter English word: ")  # pobranie słowa

if word in translations:  # sprawdzenie czy istnieje w słowniku
    print(translations[word])  # wyświetlenie tłumaczenia
else:
    print("Translation unavailable")  # brak tłumaczenia