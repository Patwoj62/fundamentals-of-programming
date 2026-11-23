# ===== Zadanie 9 =====

contacts_A = {  # pierwszy zbiór kontaktów
    "john@example.com",
    "alice@example.com",
    "bob@example.com"
}

contacts_B = {  # drugi zbiór kontaktów
    "bob@example.com",
    "michael@example.com",
    "sara@example.com"
}

merged_contacts = contacts_A | contacts_B  # suma zbiorów (Union)

print("Merged contacts:", merged_contacts)  # wyświetlenie połączonych kontaktów