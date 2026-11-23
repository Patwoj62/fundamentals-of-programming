# ===== Zadanie 16 =====

import re                                                   # moduł wyrażeń regularnych

text = input("Enter text: ")                                # str - tekst użytkownika

vowels = re.findall(r"[aeiouAEIOU]", text)                  # list - znalezione samogłoski

print("Number of vowels:", len(vowels))                     # liczba samogłosek