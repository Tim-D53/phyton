import unittest

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self._interest = interest
    
    def add_interest(self):
        self._balance += self._balance * self._interest


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit


class Bank:
    def __init__(self):
        self._accounts = []

    def open_account(self, account):
        self._accounts.append(account)

    def close_account(self, account_number):
        self._accounts = [acc for acc in self._accounts if acc.get_account_number() != account_number]

    def pay_dividend(self, dividend):
        for account in self._accounts:
            account.deposit(dividend)

    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount) and account.get_balance() < 0:
                print(f"Sending letter to account {account.get_account_number()}: You are in overdraft.")


# tests

class TestBankMethods(unittest.TestCase):
    def test_open_account(self):
        bank = Bank()
        initial_balance = 1000
        account_number = "SA123"
        savings_acc = SavingsAccount(initial_balance, account_number, 0.05)
        
        bank.open_account(savings_acc)

        # Check if account is opened
        self.assertIn(savings_acc, bank._accounts)
        
        # Check if the account has the correct balance
        for account in bank._accounts:
            if account.get_account_number() == account_number:
                self.assertEqual(account.get_balance(), initial_balance)
                break

    def test_update_method(self):
        bank = Bank()
        initial_balance = 1000
        account_number = "SA123"
        savings_acc = SavingsAccount(initial_balance, account_number, 0.05)
        
        bank.open_account(savings_acc)

        # Mock the print function
        original_print = __builtins__.print
        try:
            # Redirect print to a buffer
            messages_sent = []
            def mock_print(*args, **kwargs):
                messages_sent.append(args[0])
            __builtins__.print = mock_print
            # Call update method
            bank.update()
        finally:
            # Restore print function
            __builtins__.print = original_print
        
        # Check if interest was added
        updated_balance = initial_balance + initial_balance * 0.05
        for account in bank._accounts:
            if account.get_account_number() == account_number:
                self.assertEqual(account.get_balance(), updated_balance)
                break
        
        # Check if message was sent
        self.assertIn("Sending letter to account", messages_sent)
