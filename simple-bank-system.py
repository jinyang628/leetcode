class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
    def is_valid_account(self, account: int) -> bool:
        if 1 <= account <= self.n:
            return True
        return False
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid_account(account1) or not self.is_valid_account(account2):
            return False
        account1 -= 1
        account2 -= 1
        amt1 = self.balance[account1]
        amt2 = self.balance[account2]
        if amt1 < money:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True
    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            return False
        account -= 1
        self.balance[account] += money
        return True
    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            return False
        account -= 1
        amt = self.balance[account]
        if amt < money:
            return False
        self.balance[account] -= money
        return True
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)