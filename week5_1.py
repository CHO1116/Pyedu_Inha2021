def Bmi_Calculator(Height, Weight):
    bmi = Weight / Height ** 2
    return bmi
h = float(input("키를 입력해주세요(단위: m)\n"))
w = float(input("체중을 입력해주세요(단위: kg\n"))
print(f"your bmi is {Bmi_Calculator(h, w):.2f}")