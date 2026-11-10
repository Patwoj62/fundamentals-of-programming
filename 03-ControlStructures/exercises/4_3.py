# ===== Zadanie 19 =====

plain_text = 'The early bird catches the worm'  # tekst jawny
encrypted_text = ''  # pusty tekst zaszyfrowany

for char in plain_text:  # przejście po wszystkich znakach tekstu

    char_code = ord(char)  # odczytanie kodu ASCII znaku
    char_code = char_code + 1  # zwiększenie kodu o 1
    encrypted_char = chr(char_code)  # zamiana kodu na znak
    encrypted_text = encrypted_text + encrypted_char  # dodanie znaku do zaszyfrowanego tekstu

print(f'Plain text: {plain_text}')  # wyświetlenie tekstu oryginalnego
print(f'Encrypted text: {encrypted_text}')  # wyświetlenie tekstu zaszyfrowaneg