class account():
    M_name = None
    M_balance = None 
    
    def __init__(self, name, balance = 100000):
        # 계좌 초기 잔액 십만원 설정
        self.M_name = name
        self.M_balance = balance
    
    def deposit(self, amount):
        self.M_balance += amount
        print(f"{self.M_name} 고객님의 계좌에 {amount:,}원이 성공적으로 입금되었습니다. 잔액은 {self.M_balance:,}원입니다.")

    def withdraw(self, amount):
        self.M_balance -= amount
        print(f"{self.M_name} 고객님의 계좌로부터 {amount:,}원이 성공적으로 출금되었습니다. 잔액은 {self.M_balance:,}원입니다.")
    
    def print_balnce(self):
        print(f"[현재 계좌 정보] {self.M_name} 고객님의 계좌 잔액은 {self.M_balance:,}원입니다.")

num = int(input("진행하실 입금 및 출금 횟수를 1이상의 정수로 입력해주세요. "))
MyAccount = account("Jay")
MyAccount.print_balnce()

for index in range(num):
    flag = False
    option = int(input("[진행하실 업무를 선택해주세요.]\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 거래 종료\n"))
    while option:
        if option == 1:
            amount = int(input("입금하실 금액을 입력하세요. "))
            if amount <= 0:
                amount = int(input("입금하실 금액을 올바르게 입력해주세요. "))
            while 0 < amount:
                recheck = input(f"입금하실 금액이 {amount:,}원이 맞습니까? [y/n]...")
                if recheck == "y" or recheck == "Y":
                    MyAccount.deposit(amount)
                    option  = False
                    print(f"-----{index + 1}번째 거래가 성공적으로 완료되었습니다.-----\n")
                    break
                elif recheck == "n" or recheck == "N":
                    amount = 0
                    option = int(input("초기 화면으로 돌아갑니다.\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 거래 종료\n"))
                else:
                    continue
        elif option == 2:
            if MyAccount.M_balance == 0:
                print("현재 고객님의 잔액이 0원입니다. 출금 업무를 진행하실 수 없습니다.")
                option = int(input("다른 업무를 선택해주시기 바랍니다.\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 거래 종료\n"))
            else:                
                amount = int(input("출금하실 금액을 입력해주세요. "))
                if amount <= 0:
                    amount = int(input("출금하실 금액을 올바르게 입력해주세요. "))
                elif amount > MyAccount.M_balance:
                    amount = int(input("잔액이 부족합니다. 금액을 다시 입력해주세요. "))
                while 0 < amount <= MyAccount.M_balance:
                    recheck = input(f"출금하실 금액이 {amount:,}원이 맞습니까? [y/n]...")
                    if recheck == "y" or recheck == "Y":
                        MyAccount.withdraw(amount)
                        option = False
                        print(f"-----{index + 1}번째 거래가 성공적으로 완료되었습니다.-----\n")
                        break
                    elif recheck == "n" or recheck == "N":
                        amount = 0
                        option = int(input("초기 화면으로 돌아갑니다.\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 거래 종료\n"))
                    else:
                        continue
        elif option == 3:
            MyAccount.print_balnce()
            print(f"-----{index + 1}번째 거래가 완료되었습니다.-----")
            break
        elif option == 4:
            recheck = input("남은 횟수를 모두 무시하고 거래를 종료하시겠습니까? [y/n]...")
            if recheck == "y" or recheck == "Y":
                flag = True
                break
            elif recheck == "n" or recheck == "N":
                option = int(input("초기 화면으로 돌아갑니다.\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 거래 종료\n"))
            else:
                continue
        else:
            option = int(input("다시 입력해주세요.\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 거래 종료\n"))
    if flag:
        break
print("이용해주셔서 감사합니다. 거래를 종료합니다. ")