# ===== Zadanie 9 =====

import keyboard  # import własnego modułu

first_name = keyboard.input_string('Enter name: ')  # imię pracownika
last_name = keyboard.input_string('Enter surname: ')  # nazwisko pracownika
age = keyboard.input_integer('Enter age: ')  # wiek typu int
salary = keyboard.input_real('Enter salary: ')  # pensja typu float
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')  # True lub False

print('DATA RECORD')  # nagłówek
print('===========')  # linia oddzielająca

print('Name:', first_name, last_name)  # wyświetlenie imienia i nazwiska
print('Age:', age)  # wyświetlenie wieku

if not is_salary_hidden:  # jeśli pensja nie ma być ukryta
    print('Salary:', salary)  # wyświetlenie pensji