# ===== Zadanie 30 =====

text = "This is a sample text."  # tekst do analizy
vowels = "aeiouAEIOU"  # zbiór samogłosek
vowel_count = 0  # licznik samogłosek
i = 0  # indeks pierwszego znaku tekstu

while i < len(text):  # wykonuj dopóki indeks mieści się w długości tekstu
    if text[i] in vowels:  # sprawdzenie czy aktualny znak jest samogłoską
        vowel_count += 1  # zwiększenie licznika samogłosek
    i += 1  # przejście do następnego znaku

print(f"The number of vowels in the text is: {vowel_count}")  # wyświetlenie liczby samogłosek