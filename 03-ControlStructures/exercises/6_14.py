# ===== Zadanie 43 =====

total_washing_time = 0  # całkowity czas prania

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')  # wybór programu
extra_rinse = input('Extra rinse? (y/n): ')  # dodatkowe płukanie
extra_spin = input('Extra spin? (y/n): ')  # dodatkowe wirowanie

if program == 'j':  # kurtka
    total_washing_time += 40  # czas programu

elif program == 'u':  # bielizna
    total_washing_time += 70  # czas programu

elif program == 's':  # buty
    total_washing_time += 20  # czas programu

if extra_rinse == 'y':  # dodatkowe płukanie
    total_washing_time += 15  # dodanie czasu

if extra_spin == 'y':  # dodatkowe wirowanie
    total_washing_time += 9  # dodanie czasu

print(f'Total washing time: {total_washing_time} minutes')  # wynik
    
