class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  
        self._balance = balance              

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Đã nạp {amount:,} VNĐ vào tài khoản {self.account_number}.") 
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Đã rút {amount:,} VNĐ từ tài khoản {self.account_number}.")
        else:
            print("Giao dịch thất bại: Số dư không đủ.")

    def get_balance(self):
        return self._balance

my_account = BankAccount(account_number="Quanh", balance=1000000)
print(f"--- Giao dịch tài khoản: {my_account.account_number} ---")

my_account.deposit(500000)
my_account.withdraw(200000)
current_balance = my_account.get_balance()
print(f"Số dư hiện tại của bạn là: {current_balance:,} VNĐ")