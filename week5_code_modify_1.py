def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
num = int(input("숫자를 입력하세요. "))
# Modified Source Code
print(fact(num))