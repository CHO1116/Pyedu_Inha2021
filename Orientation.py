# 함수 정의
def twice(x):
    return x * x
print(twice(5)) # 25

# 람다 함수의 정의: x goes to x * x
twice2 = lambda x : x ** x +1   # x의 x제곱 표현법
print(twice2(3)) # 28

# 코드 수정 오리엔테이션
toeic = int(input("토익 점수를 입력하세요: "))
if not toeic > 800: # Modified Source Code
    print("장학금을 받을 수 없습니다. ")
else:
    print("장학금을 받을 수 있습니다. ")

# range 속성 (시작점, 끝점 + 1, 간격)
for i in range(1, 10, 2):   # 1에서 9까지 두칸씩
    print(f"9 * {i} = {9 * i}")