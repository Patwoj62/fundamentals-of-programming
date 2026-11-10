# ===== Zadanie 2 =====

account_balance = 500  # stan konta klienta
total_payment = float(input('Enter payment amount: '))  # kwota do zapłaty

if total_payment <= account_balance:  # sprawdzenie czy środków wystarczy
    print('Payment completed')  # płatność zakończona sukcesem
else:  # gdy brakuje środków
    print('No funds')  # komunikat o braku pieniędzy