# ===== Zadanie 22 =====

import json  # obsługa plików json

try:  # próba odczytu pliku

    with open("voting.json", "r") as file:
        votes = json.load(file)

except FileNotFoundError:  # jeśli plik nie istnieje

    votes = {}  # utworzenie pustego słownika

person_name = input("Name of the person you are voting for: ")

if person_name in votes:

    votes[person_name] += 1

else:

    votes[person_name] = 1

with open("voting.json", "w") as file:

    json.dump(votes, file, indent=4)

print("Vote saved")