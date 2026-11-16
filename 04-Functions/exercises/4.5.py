# ===== Zadanie 4 =====

def pts_to_grade(points):  # definicja funkcji
    grade = ''  # zmienna przechowująca ocenę, typ str

    if points >= 18:  # jeśli 18 punktów lub więcej
        grade = 'Excellent'  # ocena Excellent
    elif points >= 14:  # jeśli minimum 14 punktów
        grade = 'Good'  # ocena Good
    elif points >= 10:  # jeśli minimum 10 punktów
        grade = 'Satisfactory'  # ocena Satisfactory
    else:  # mniej niż 10 punktów
        grade = 'Fail'  # ocena Fail

    return grade  # zwrócenie oceny

test_result = 15 # liczba punktów, typ int
final_grade = pts_to_grade(test_result)  # wywołanie funkcji

print('You scored', test_result, 'points on the test. Your final grade is', final_grade)  # wyświetlenie wyniku