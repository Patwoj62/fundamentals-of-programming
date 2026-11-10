# ===== Zadanie 39 =====

current_price = 140.00  # aktualna cena produktu
previous_price = 200.00  # poprzednia cena produktu

reduction = ((previous_price - current_price) / previous_price) * 100  # obliczenie procentowej obniżki

print(f'Current product price: {current_price:.2f}')  # wyświetlenie aktualnej ceny
print(f'Previous product price: {previous_price:.2f}')  # wyświetlenie poprzedniej ceny

if reduction >= 10:  # sprawdzenie czy obniżka wynosi co najmniej 10%
    print('Buy the product!!')  # rekomendacja zakupu
    print(f'Product price reduced by {reduction:.0f}%')  # wyświetlenie wielkości obniżki