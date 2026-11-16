# ===== Zadanie 44 =====

import math  # biblioteka matematyczna

import matplotlib.pyplot as plt  # biblioteka wykresów

x = []  # lista kątów

y = []  # lista wartości funkcji

for angle in range(0, 361):  # zakres 0-360 stopni

    x.append(angle)  # zapisuje kąt

    y.append(math.sin(math.radians(angle)))  # zamienia stopnie na radiany i liczy sinus

plt.plot(x, y)  # rysuje wykres

plt.show()  # wyświetla wykres