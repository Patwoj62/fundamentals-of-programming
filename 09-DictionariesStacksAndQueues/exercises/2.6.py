# ===== Zadanie 10 =====

required_permissions = {  # wymagane uprawnienia
    "read",
    "write",
    "execute"
}

user_permissions = {  # uprawnienia użytkownika
    "read",
    "write"
}

has_permissions = required_permissions.issubset(user_permissions)  # sprawdzenie podzbioru

print(has_permissions)  # False, ponieważ brakuje uprawnienia execute