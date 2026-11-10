# ===== Zadanie 35 ====

password = input("Enter password: ")          # pobranie hasła
password_ok = len(password) >= 8              # sprawdzenie długości hasła

print(f"Password length is valid: {password_ok}")  # wyświetlenie wyniku