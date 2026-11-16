# ===== Zadanie 35 =====

def f(text):  # funkcja przyjmuje tekst typu str
    return '-'.join(text)  # łączy wszystkie znaki separatorem '-'

print(f("University"))  # U-n-i-v-e-r-s-i-t-y
print(f("UE"))  # U-E
print(f("x"))  # x
print(f(""))  # pusty napis