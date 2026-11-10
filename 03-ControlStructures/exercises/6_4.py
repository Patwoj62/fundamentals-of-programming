# ===== Zadanie 33 =====

temperature = int(input('Enter temperature: '))  # pobranie temperatury

if temperature > 35:  # powyżej 35 stopni
    print("It is extremely hot")  # bardzo gorąco

elif temperature > 30:  # powyżej 30 stopni
    print("It is hot")  # gorąco

elif temperature >= 15:  # od 15 stopni
    print("It is warm")  # ciepło

elif temperature >= 0:  # od 0 do 14 stopni
    print("It is cold")  # zimno

else:  # poniżej zera
    print("Warning, frost")  # ostrzeżenie o mrozie