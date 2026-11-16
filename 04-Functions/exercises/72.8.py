# ===== Zadanie 37 =====

def f(dice):  # funkcja przyjmuje ciąg wyników rzutu kostką
    longest_digit = dice[0]  # aktualny rekordzista
    longest_count = 1  # długość najdłuższej serii

    current_digit = dice[0]  # aktualnie sprawdzana cyfra
    current_count = 1  # długość bieżącej serii

    for i in range(1, len(dice)):  # przejście po kolejnych cyfrach
        if dice[i] == current_digit:  # jeśli cyfra powtarza się
            current_count += 1  # zwiększenie długości serii
        else:  # jeśli seria się zakończyła
            if current_count > longest_count:  # sprawdzenie rekordu
                longest_count = current_count  # zapis długości rekordu
                longest_digit = current_digit  # zapis cyfry rekordu

            current_digit = dice[i]  # rozpoczęcie nowej serii
            current_count = 1  # licznik nowej serii

    if current_count > longest_count:  # sprawdzenie ostatniej serii
        longest_digit = current_digit  # zapis rekordowej cyfry

    return int(longest_digit)  # zwrócenie cyfry

print(f("5233165554211"))  # 5
print(f("2133"))  # 3