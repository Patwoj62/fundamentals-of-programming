# ===== Zadanie 26 =====

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]  # lista imion

longest_name = names[0]  # początkowo pierwsze imię

for name in names:  # przejście po imionach

    if len(name) > len(longest_name):  # sprawdza długość tekstu
        longest_name = name  # zapamiętuje najdłuższe imię

print("Names:", " ".join(names))  # wyświetla wszystkie imiona
print("Longest name:", longest_name)  # wyświetla najdłuższe imię