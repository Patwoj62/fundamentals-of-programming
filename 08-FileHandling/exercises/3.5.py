# ===== Zadanie 12 =====

# Checks the correctness of username and password

import re                                                   # moduł wyrażeń regularnych

username = input("Enter username: ")                        # str - nazwa użytkownika

password = input("Enter password: ")                        # str - hasło

username_pattern = r"^[a-z]{6,}$"                           # min. 6 małych liter

password_pattern = r"^[A-Za-z0-9_]{8,}$"                    # min. 8 znaków, litery/cyfry/_

username_match = re.match(username_pattern, username)       # sprawdzenie loginu

password_match = re.match(password_pattern, password)       # sprawdzenie hasła

if username_match and password_match:                       # oba warunki spełnione

    print("Username and password are correct.")             # komunikat poprawności

else:                                                       # któryś warunek niespełniony

    print("Username or password is incorrect.")             # komunikat błędu