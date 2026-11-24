# definicja klasy BankAccount
class BankAccount:

    # konstruktor klasy
    def __init__(self, account_number):

        # numer konta, typ str
        self.account_number = account_number

        # saldo początkowe, typ float
        self.balance = 0.0

    # metoda wpłaty środków
    def deposit(self, amount):

        # zwiększenie salda o wpłaconą kwotę
        self.balance += amount

    # metoda wypłaty środków
    def withdraw(self, amount):

        # sprawdzenie czy na koncie są wystarczające środki
        if amount <= self.balance:

            # zmniejszenie salda
            self.balance -= amount

        else:

            # komunikat o braku środków
            print("Insufficient funds on the account")

    # metoda wyświetlająca dane konta
    def show_balance(self):

        # wyświetlenie numeru konta
        print(f"Bank Account No: {self.account_number}")

        # wyświetlenie stanu konta
        print(f"Balance: PLN {self.balance:.2f}")