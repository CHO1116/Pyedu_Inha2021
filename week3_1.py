# 심화예제 1번 비밀번호 구하기 문제
print("비밀번호 일치여부를 판단하는 문제입니다.")
password = input("비밀번호를 설정해 주세요. ")
print("확인을 위해 다시 한번 입력해주세요. ")
confirm = input()
while password != confirm:
  confirm = input("일치하지 않습니다.\n")
print("확인되었습니다!")
print("프로그램을 종료합니다.")