# ===== Zadanie 17 =====

paragraph = "cat dog mouse cat rat cat mouse"  # tekst

words = paragraph.split()  # podział tekstu na listę słów

counter = {}  # pusty słownik

for word in words:  # przejście po słowach

    if word in counter:  # słowo już istnieje
        counter[word] += 1  # zwiększenie licznika
    else:
        counter[word] = 1  # pierwsze wystąpienie

for word, count in counter.items():  # wyświetlenie wyników
    print(word, count)