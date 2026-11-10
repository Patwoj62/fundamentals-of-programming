# ===== Zadanie 25 ====

price = float(input("Enter price: "))       # pobranie ceny produktu
discount = float(input("Enter discount %: "))  # pobranie procentu rabatu
reduction = price * discount / 100          # obliczenie kwoty obniżki
discount_price = price - reduction          # obliczenie ceny po rabacie

print(f"Price with discount: {discount_price:.2f}")  # wyświetlenie ceny po rabacie
print(f"Reduction: {reduction:.2f}")        # wyświetlenie kwoty obniżki