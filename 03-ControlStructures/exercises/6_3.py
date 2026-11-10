# ===== Zadanie 32 =====

new_password = input('Enter new password: ')  # pobranie hasła

if len(new_password) < 12:  # sprawdzenie długości
    print('Password too short (min. 12 chars)')  # hasło za krótkie
else:  # hasło poprawne
    print('Password accepted')  # komunikat sukcesu