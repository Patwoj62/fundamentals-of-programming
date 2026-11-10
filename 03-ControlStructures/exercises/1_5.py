# ===== Zadanie 5 =====

basic_salary = 5000  # podstawowe wynagrodzenie
total_salary = 0  # zmienna przechowująca końcową pensję
bonus = 0.15  # premia 15%
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'  # sprawdzenie czy pracownik dostaje premię

if is_bonus:  # jeśli premia jest przyznana
    total_salary = basic_salary + (basic_salary * bonus)  # dodanie premii do pensji
else:  # jeśli brak premii
    total_salary = basic_salary  # wynagrodzenie pozostaje bez zmian

print(f'Basic salary: {basic_salary}')  # wyświetlenie podstawowej pensji
print(f'Bonus included? {is_bonus}')  # informacja czy uwzględniono premię
print(f'Total salary: {total_salary}')  # wyświetlenie całkowitej pensji

