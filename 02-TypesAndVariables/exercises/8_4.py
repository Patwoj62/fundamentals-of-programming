# ===== Zadanie 47 ====

swift = input("Enter SWIFT code: ")        # pobranie kodu SWIFT

print(f"Bank Code: {swift[0:4]}")          # pierwsze 4 znaki - kod banku
print(f"Country Code: {swift[4:6]}")       # znaki 5-6 - kod kraju