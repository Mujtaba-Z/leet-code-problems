# Pair Programming OOP Interview Exercise

class BankAccount:
    """
    A simple BankAccount class to demonstrate OOP principles.
    """
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """
        Initialize the bank account with an account holder and an optional initial balance.
        """
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float):
        """
        Deposit a specified amount into the account.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        """
        Withdraw a specified amount from the account.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """
        Return the current balance of the account.
        """
        return self.balance

# Example usage for pair programming:
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("John Doe", 100.0)

    # Perform some operations
    print("Initial Balance:", account.get_balance())
    account.deposit(50.0)
    print("Balance after deposit:", account.get_balance())
    account.withdraw(30.0)
    print("Balance after withdrawal:", account.get_balance())