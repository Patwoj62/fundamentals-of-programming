# ===== Zadanie 28 ====

phone = input("Enter phone number: ")           # pobranie numeru telefonu
formatted_phone = phone[0:3] + "-" + phone[3:6] + "-" + phone[6:9]  # formatowanie numeru

print(f"Phone number: {formatted_phone}")       # wyświetlenie numeru