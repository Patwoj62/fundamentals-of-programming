# ===== Zadanie 55 =====

n = int(input('How many prime numbers?: '))  # liczba liczb pierwszych
count = 0  # licznik znalezionych liczb pierwszych
number = 2  # pierwsza liczba do sprawdzenia

while count < n:  # szukaj aż znajdziesz n liczb
    is_prime = True  # zakładamy że liczba jest pierwsza
    for i in range(2, number):  # sprawdzanie dzielników
        if number % i == 0:  # znaleziono dzielnik
            is_prime = False  # liczba nie jest pierwsza
            break  # zakończenie sprawdzania
        
    if is_prime:  # liczba pierwsza
        print(number, end=' ')  # wyświetlenie liczby
        count += 1  # zwiększenie licznika
        
    number += 1  # następna liczba