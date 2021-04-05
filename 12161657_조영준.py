# 심화예제 1번 비밀번호 구하기 문제
print("비밀번호 일치여부를 판단하는 문제입니다.")
password = input("비밀번호를 설정해 주세요. ")
print("확인을 위해 다시 한번 입력해주세요. ")
confirm = input()
while password != confirm:
  confirm = input("일치하지 않습니다.\n")
print("확인되었습니다!\n")

# 심화예제 2번 약수의 개수 구하기 문제
print("양의 정수를 입력하시면 약수의 개수를 알려드립니다.")
div = int(input("0보다 큰 정수를 입력해주세요. "))
cnt = 0
for i in range(1, div + 1):
  if div % i == 0:
   cnt += 1
print(f"입력하신 정수 {div}의 약수의 개수는 {cnt}개 입니다.")