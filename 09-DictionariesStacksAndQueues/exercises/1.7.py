# ===== Zadanie 5 =====

products = {  # słownik produktów sklepu komputerowego
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

print("PRODUCT\tQUANTITY")  # nagłówek

for product, quantity in products.items():  # przejście po produktach
    print(f"{product}\t{quantity}")  # wyświetlenie nazwy i ilości

total = sum(products.values())  # suma wszystkich ilości produktów

print(f"\nTotal products: {total}")  # wyświetlenie sumy