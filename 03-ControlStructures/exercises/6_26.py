# ===== Zadanie 54 =====

a = 0  # pierwszy wyraz
b = 1  # drugi wyraz

print(a, end=' ')  # wyświetlenie pierwszego wyrazu
print(b, end=' ')  # wyświetlenie drugiego wyrazu

for i in range(18):  # pozostałe 18 wyrazów

    c = a + b  # kolejny wyraz

    print(c, end=' ')  # wyświetlenie

    a = b  # przesunięcie wartości
    b = c  # przesunięcie wartości