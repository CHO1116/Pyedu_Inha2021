class account():
    M_name = None
    M_balance = None

    def __init__(self, name, balance):
        self.M_name = name
        self.M_balance = balance
    
    def deposit(self, amount):
        self.M_balance += amount
        print(self.M_name, "님의 계좌에", amount, "원이 성공적으로 입금되었습니다.\t잔액은 ", self.M_balance)

    def withdraw(self, amount):
        self.M_balance -= amount
        print(self.M_name, "님의 계좌에서", amount, "원이 성공적으로 출금되었습니다.  잔액은 ", self.M_balance)
    
    def print_balnce(self):
        print(self.M_name, "님의 계좌 잔액은", self.M_balance, "원 입니다.")

John = account("John", 10000)
John.deposit(7500)
John.withdraw(1500)
John.deposit(3000)
John.print_balnce()