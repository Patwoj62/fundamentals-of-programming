# ===== Zadanie 10 =====

product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]  # ceny produktów typu float

product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]  # ilości produktów typu int

total_value = 0  # całkowita wartość magazynu typu float

for i in range(len(product_prices)):  # przechodzi przez wszystkie indeksy list
    total_value += product_prices[i] * product_quantities[i]  # dodaje wartość produktu do sumy

print("Total stock value:", total_value)  # wyświetla wartość wszystkich produktów