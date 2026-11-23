# ===== Zadanie 8 =====

emails_received = {  # zbiór otrzymanych wiadomości
    "john@example.com",
    "spam1@example.com",
    "spam2@example.com",
    "jane@example.com"
}

spam_list = {  # zbiór adresów spamowych
    "spam1@example.com",
    "spam2@example.com"
}

spam_emails = emails_received & spam_list  # część wspólna zbiorów (Intersection)

print("Spam emails:", spam_emails)  # wyświetlenie znalezionego spamu