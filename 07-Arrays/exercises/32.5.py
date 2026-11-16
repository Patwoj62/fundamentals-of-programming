# ===== Zadanie 43 =====

import matplotlib.pyplot as plt  # biblioteka wykresów

x = []  # lista argumentów

y = []  # lista wartości funkcji

for n in range(-100, 101):  # liczby od -100 do 100

    x.append(n)  # dodaje argument

for n in x:  # przechodzi po argumentach

    y.append((n ** 2) - 3)  # oblicza wartość funkcji

plt.plot(x, y)  # rysuje wykres

plt.show()  # wyświetla wykres