# ===== Zadanie 27 =====

import json  # obsługa json

with open(r"C:\Users\Patryk\OneDrive\Desktop\fundamentals-of-programming\09-DictionariesStacksAndQueues\exercises\computer.json", "r", encoding="utf-8") as file: #
    # otwarcie pliku csv (with open("cities.json", "r", encoding="utf-8") as file:)
    data = json.load(file)

for key, value in data.items():

    print(key, ":", value)