# ===== Zadanie 14 =====

# Functions for reading email data

import re                                                   # moduł wyrażeń regularnych

def email_sender(email):                                    # funkcja zwraca adres nadawcy

    match = re.search(r"From:.*<([^>]+)>", email)           # wyszukiwanie adresu nadawcy

    return match.group(1) if match else ""                  # zwrot adresu lub pustego tekstu

def email_recipient(email):                                 # funkcja zwraca adres odbiorcy

    match = re.search(r"To:.*<([^>]+)>", email)             # wyszukiwanie adresu odbiorcy

    return match.group(1) if match else ""                  # zwrot adresu lub pustego tekstu

def email_subject(email):                                   # funkcja zwraca temat wiadomości

    match = re.search(r"Subject:\s*(.+)", email)            # wyszukiwanie tematu

    return match.group(1) if match else ""                  # zwrot tematu lub pustego tekstu

def email_body(email):                                      # funkcja zwraca treść wiadomości

    match = re.search(                                      # wyszukiwanie treści wiadomości
        r"Content-Transfer-Encoding:.*?\n\n(.*)",
        email,
        re.DOTALL
    )

    return match.group(1).strip() if match else ""          # zwrot treści bez zbędnych spacji