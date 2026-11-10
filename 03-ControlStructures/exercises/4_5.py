# ===== Zadanie 21 =====

sum = 0  # zmienna przechowująca sumę

for i in range(1,11):  # liczby od 1 do 10

    if not i % 2 == 0:  # pominięcie liczb nieparzystych
        continue  # przejście do następnej iteracji

    sum += i  # dodanie liczby parzystej do sumy

print(f'Sum of even numbers in the range <1,10> is {sum}')  # wyświetlenie wyniku