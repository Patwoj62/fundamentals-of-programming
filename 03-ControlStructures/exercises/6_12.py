# ===== Zadanie 41 =====

facebook = True  # konto Facebook
twitter = False  # konto Twitter
instagram = True  # konto Instagram

accounts = 0  # licznik kont

if facebook:  # sprawdzenie Facebooka
    accounts += 1  # zwiększenie licznika

if twitter:  # sprawdzenie Twittera
    accounts += 1  # zwiększenie licznika

if instagram:  # sprawdzenie Instagrama
    accounts += 1  # zwiększenie licznika

if accounts >= 2:  # co najmniej dwa konta
    print('You are a good influencer!')  # komunikat