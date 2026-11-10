# ===== Zadanie 35 =====

age = int(input('Enter your age: '))  # pobranie wieku

if age < 13:  # mniej niż 13 lat
    print('Child')  # dziecko

elif age <= 19:  # od 13 do 19 lat
    print('Teen')  # nastolatek

elif age <= 64:  # od 20 do 64 lat
    print('Adult')  # dorosły

else:  # 65+
    print('Senior')  # senior