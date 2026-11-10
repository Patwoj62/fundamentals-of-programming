# ===== Zadanie 46 =====

computer_science = input('Are you interested in computer science? (y/n): ') == 'y'  # odpowiedź 1
computer_games = input('Do you like playing computer games? (y/n): ') == 'y'  # odpowiedź 2
instagram = input('Do you have an Instagram account? (y/n): ') == 'y'  # odpowiedź 3

print('SURVEY RESULTS')  # nagłówek wyników
print(f'Interested in computer science: {"Yes" if computer_science else "No"}')  # wynik 1
print(f'Playing computer games: {"Yes" if computer_games else "No"}')  # wynik 2
print(f'Has an Instagram account: {"Yes" if instagram else "No"}')  # wynik 3