# ===== Zadanie 40 =====

# Returns number of words

def word_count(text):  # funkcja licząca słowa

    words = text.split()  # dzieli tekst na słowa

    return len(words)  # zwraca liczbę słów


# Returns words ordered by length

def longest_words(text):  # funkcja sortująca od najdłuższych słów

    words = text.split()  # tworzy listę słów

    return sorted(words, key=len, reverse=True)  # sortuje malejąco po długości


# Returns words in alphabetical order

def alphabetical_words(text):  # funkcja sortująca alfabetycznie

    words = text.split()  # tworzy listę słów

    return sorted(words)  # sortuje alfabetycznie