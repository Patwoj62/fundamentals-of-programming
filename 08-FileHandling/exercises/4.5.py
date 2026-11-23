# ===== Zadanie 14 =====

# Prints email information

import os                                                   # moduł obsługi ścieżek

from emails import email_sender                             # import funkcji nadawcy
from emails import email_recipient                          # import funkcji odbiorcy
from emails import email_subject                            # import funkcji tematu
from emails import email_body                               # import funkcji treści

folder = os.path.dirname(os.path.abspath(__file__))         # str - folder programu

file_path = os.path.join(folder, "email.txt")              # str - ścieżka do pliku email.txt

with open(file_path, "r", encoding="utf-8") as file:       # otwarcie pliku

    email = file.read()                                     # str - odczyt całej wiadomości

print("SENDER:")                                            # nagłówek nadawcy
print(email_sender(email))                                  # wyświetlenie adresu nadawcy

print("\nRECIPIENT:")                                       # nagłówek odbiorcy
print(email_recipient(email))                               # wyświetlenie adresu odbiorcy

print("\nSUBJECT:")                                         # nagłówek tematu
print(email_subject(email))                                 # wyświetlenie tematu

print("\nBODY:")                                            # nagłówek treści
print(email_body(email))                                    # wyświetlenie treści wiadomości