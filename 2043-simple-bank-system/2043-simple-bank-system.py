class Bank:

    def __init__(self, balance: List[int]):
        self.bank = {}
        for account,amount in enumerate(balance):
            self.bank[account+1] = amount

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.bank and account2 in self.bank:
            if self.bank[account1] >= money:
                self.bank[account1] -= money
                self.bank[account2] += money
                return True
            else:
                return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.bank:
            self.bank[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.bank:
            if self.bank[account] >= money:
                self.bank[account] -= money
                return True
            else:
                return False
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)