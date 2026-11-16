# ===== Zadanie 22 =====

def f(n):  # funkcja przyjmująca liczbę n
    result = ''  # pusty napis

    for i in range(1, n + 1):  # przejście od 1 do n
        result += str(i)  # dopisanie liczby do napisu

    return result  # zwrócenie wyniku

print(f(11))  # 1234567891011
print(f(4))  # 1234