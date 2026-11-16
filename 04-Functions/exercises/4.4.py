# ===== Zadanie 3 =====

def sum_digits(number):  # definicja funkcji obliczającej sumę cyfr
    number = abs(number)  # usunięcie znaku minus jeśli liczba jest ujemna
    total = 0  # zmienna przechowująca sumę cyfr, typ int

    for digit in str(number):  # przejście po każdej cyfrze liczby jako tekst
        total += int(digit)  # zamiana znaku na int i dodanie do sumy

    return total  # zwrócenie wyniku

any_number = int(input('Enter integer number: '))  # pobranie liczby całkowitej
result = sum_digits(any_number)  # wywołanie funkcji

print('The sum of the digits in the number', any_number, 'is', result)  # wyświetlenie wyniku