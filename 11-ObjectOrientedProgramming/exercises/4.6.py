# ===== Zadanie 16 =====

# import klasy BankAccount
from bank_account import BankAccount


# funkcja główna programu
def main():

    # utworzenie obiektu konta bankowego
    account = BankAccount(
        "12 3456 5555 9090 1111 0000 7722"
    )

    # wyświetlenie salda początkowego
    account.show_balance()

    print()

    # wpłata 25.30 PLN
    account.deposit(25.30)

    # wyświetlenie salda
    account.show_balance()

    print()

    # próba wypłaty 31.70 PLN
    account.withdraw(31.70)

    # wyświetlenie salda
    account.show_balance()

    print()

    # wypłata 14 PLN
    account.withdraw(14)

    # wyświetlenie salda
    account.show_balance()


# uruchomienie programu
if __name__ == "__main__":
    main()