# 함수를 활용하여 BMI지수 측정하기
def Bmi_Calculator(Height, Weight):
    bmi = Weight / Height ** 2  # 제곱표현법
    return bmi

h = float(input("키를 입력해주세요(단위: m)\n"))
w = float(input("체중을 입력해주세요(단위: kg\n"))
print(f"your bmi is {Bmi_Calculator(h, w):.2f}")    # 소수점 아래 자리수 표현법