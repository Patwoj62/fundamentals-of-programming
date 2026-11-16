# ===== Zadanie 13 =====

import letter_counter  # import modułu

text = 'You never get a second chance to make a first impression'  # tekst do analizy

result = letter_counter.count_letter(text, 'e')  # zliczanie liter e

print(text)  # wyświetlenie tekstu
print("The number of letter 'e':", result)  # wyświetlenie wyniku