# ===== Zadanie 44 =====

time24 = input('Enter time (24-hour format): ')  # pobranie czasu
hour, minute = time24.split(':')  # rozdzielenie godzin i minut
hour = int(hour)  # konwersja godzin na liczbę

if hour == 0:  # północ
    hour12 = 12  # godzina 12 AM
    suffix = 'am'  # oznaczenie am

elif hour < 12:  # godziny poranne
    hour12 = hour  # bez zmian
    suffix = 'am'  # oznaczenie am

elif hour == 12:  # południe
    hour12 = 12  # bez zmian
    suffix = 'pm'  # oznaczenie pm

else:  # godziny popołudniowe
    hour12 = hour - 12  # konwersja
    suffix = 'pm'  # oznaczenie pm

print(f'Time in 12-hour format: {hour12}:{minute}{suffix}')  # wynik