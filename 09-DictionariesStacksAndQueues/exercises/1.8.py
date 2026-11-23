# ===== Zadanie 6 =====

price_list = {  # słownik z cenami produktów
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

print("PRODUCTS BEFORE DISCOUNT")  # nagłówek

for product, price in price_list.items():  # iteracja po słowniku
    print(f"{product}: {price:.2f}")  # wyświetlenie ceny przed rabatem

total_before = sum(price_list.values())  # suma cen przed rabatem

print(f"\nTotal before discount: {total_before:.2f}")  # wyświetlenie sumy

for product in price_list:  # przejście po wszystkich kluczach
    price_list[product] = round(price_list[product] * 0.9, 2)  # obniżka 10%

print("\nPRODUCTS AFTER DISCOUNT")  # nagłówek

for product, price in price_list.items():  # iteracja po słowniku
    print(f"{product}: {price:.2f}")  # wyświetlenie nowej ceny

total_after = sum(price_list.values())  # suma cen po rabacie

print(f"\nTotal after discount: {total_after:.2f}")  # wyświetlenie końcowej sumy