# 함수를 활용하여 구구단 출력하기
def Multiplication_table(number):
    print("[구구단", number, "단]")
    for i in range(1, 10):
        print(number, "*", i, "=", number * i)

g = int(input("입력하신 숫자의 구구단을 출력합니다. "))
Multiplication_table(g)