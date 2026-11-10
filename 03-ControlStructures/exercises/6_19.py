# ===== Zadanie 48 =====

amount = int(input('Enter the amount in PLN: '))  # pobranie kwoty

coins5 = amount // 5  # liczba monet 5 PLN
amount %= 5  # pozostała kwota

coins2 = amount // 2  # liczba monet 2 PLN
amount %= 2  # pozostała kwota

coins1 = amount  # liczba monet 1 PLN

print('The amount in coins:')  # nagłówek
print(f'5 PLN coins: {coins5}')  # wynik dla 5 PLN
print(f'2 PLN coins: {coins2}')  # wynik dla 2 PLN
print(f'1 PLN coins: {coins1}')  # wynik dla 1 PLN