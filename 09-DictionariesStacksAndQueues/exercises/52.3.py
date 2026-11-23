# ===== Zadanie 34 =====

import json  # obsługa json

with open(r"C:\Users\Patryk\OneDrive\Desktop\fundamentals-of-programming\09-DictionariesStacksAndQueues\exercises\euro.json", "r", encoding="utf-8") as file:  
    # otwarcie pliku (with open("euro.json", "r", encoding="utf-8") as file:)

    data = json.load(file)  # wczytanie danych

print("Date\t\tBuying Rate\tSelling Rate")

print("=" * 45)

for rate in data["rates"]:  # przejście po kursach

    print(
        f"{rate['effectiveDate']}\t"
        f"{rate['bid']:.4f}\t\t"
        f"{rate['ask']:.4f}"
    )