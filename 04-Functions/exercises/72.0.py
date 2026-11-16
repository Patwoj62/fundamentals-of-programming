# ===== Zadanie 29 =====

def f(n):  # funkcja przyjmująca numer liczby pierwszej
    count = 0  # licznik znalezionych liczb pierwszych
    number = 1  # aktualnie sprawdzana liczba

    while count < n:  # dopóki nie znajdziemy n liczb pierwszych
        number += 1  # przejście do kolejnej liczby
        is_prime = True  # zakładamy że liczba jest pierwsza

        for i in range(2, number):  # sprawdzanie dzielników
            if number % i == 0:  # znaleziono dzielnik
                is_prime = False  # liczba nie jest pierwsza
                break  # przerwanie pętli

        if is_prime:  # jeśli liczba jest pierwsza
            count += 1  # zwiększenie licznika

    return number  # zwrócenie znalezionej liczby pierwszej

print(f(1))  # 2
print(f(5))  # 11