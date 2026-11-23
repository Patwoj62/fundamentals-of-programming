# ===== Zadanie 20 =====

prices = {  # cennik
    "milk": 1.49,
    "butter": 2.09,
    "juice": 1.19,
    "bread": 1.99
}

cart = {  # koszyk
    "juice": 3,
    "bread": 1,
    "milk": 2
}

total = 0  # suma zakupów

for product, quantity in cart.items():

    total += prices[product] * quantity

print(f"Total cost: {total:.2f}")