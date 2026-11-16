# ===== Zadanie 7 =====

def time_string(hours, minutes, time_format):  # definicja funkcji
    if time_format == '24':  # format 24-godzinny
        return f'{hours:02}:{minutes:02}'  # np. 08:03

    elif time_format == '12':  # format 12-godzinny
        suffix = 'am'  # domyślnie am

        if hours >= 12:  # godziny popołudniowe
            suffix = 'pm'  # pm

        display_hour = hours % 12  # zamiana na zakres 0-11

        if display_hour == 0:  # północ lub południe
            display_hour = 12  # zapis jako 12

        return f'{display_hour}:{minutes:02}{suffix}'  # zwrócenie czasu

print(time_string(15, 38, '24'))  # 15:38
print(time_string(8, 3, '24'))  # 08:03
print(time_string(0, 5, '24'))  # 00:05

print(time_string(11, 15, '12'))  # 11:15am
print(time_string(0, 7, '12'))  # 12:07am
print(time_string(7, 30, '12'))  # 7:30am
print(time_string(12, 46, '12'))  # 12:46pm
print(time_string(13, 10, '12'))  # 1:10pm
print(time_string(19, 2, '12'))  # 7:02pm