# ===== Zadanie 5 =====

computer_games = [
   "Minecraft",
   "Fortnite",
   "Cyberpunk 2077",
   "The Witcher 3",
   "League of Legends",
   "Valorant",
   "Grand Theft Auto V",
   "Elden Ring",
   "Apex Legends",
   "Call of Duty: Warzone"
]

computer_games.sort()  # sortuje listę alfabetycznie

i = 0  # licznik typu int

while i < len(computer_games):  # wykonuje się dopóki indeks istnieje
    print(i + 1, computer_games[i])  # numeruje i wyświetla gry
    i += 1  # zwiększa licznik o 1