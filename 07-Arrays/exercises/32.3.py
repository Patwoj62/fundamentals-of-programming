# ===== Zadanie 41 =====

import MyText  # import modułu

text = "An apple a day keeps the doctor away"  # tekst typu string

print("Text:", text)  # wyświetla tekst

print("Number of words:", MyText.word_count(text))  # liczba słów

print("Words from the longest:", MyText.longest_words(text))  # słowa od najdłuższego

print("Words ordered alphabetically:", MyText.alphabetical_words(text))  # słowa alfabetycznie