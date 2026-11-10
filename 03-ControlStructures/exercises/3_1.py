# ===== Zadanie 12 =====

login = 'joe'  # poprawny login
password = 'abcd'  # poprawne hasło

entered_login = input('Login: ')  # pobranie loginu od użytkownika
entered_password = input('Password: ')  # pobranie hasła od użytkownika

if login == entered_login and password == entered_password:  # sprawdzenie loginu i hasła
    print('You are logged in')  # komunikat poprawnego logowania
else:  # gdy login lub hasło są błędne
    print('Incorrect login or password!!')  # komunikat błędu