# ===== Zadanie 3 =====

total_tasks = 20  # całkowita liczba zadań
tasks_ok = int(input('Number of correctly completed tasks: '))  # liczba poprawnych odpowiedzi
test_passed = False  # początkowo test nie jest zdany

if tasks_ok >= total_tasks / 2:  # sprawdzenie czy uzyskano minimum 50%
    test_passed = True  # ustawienie informacji o zdanym teście

if test_passed:  # jeśli test został zdany
    print('Congratulations! You passed the test.')  # komunikat o sukcesie
else:  # jeśli test nie został zdany
    print('Unfortunately, you failed the test.')  # komunikat o niepowodzeniu