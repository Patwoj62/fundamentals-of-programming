# ===== Zadanie 28 =====

def f(number):  # funkcja przyjmuje liczbę
    text = str(number)  # zamiana liczby na napis
    total = 0  # suma powtarzających się cyfr

    for digit in text:  # przejście po wszystkich cyfrach
        if text.count(digit) > 1:  # jeśli cyfra występuje więcej niż raz
            total += int(digit)  # dodanie cyfry do sumy

    return total  # zwrócenie wyniku

print(f(1027))  # 0
print(f(230335))  # 9
print(f(513553007))  # 21