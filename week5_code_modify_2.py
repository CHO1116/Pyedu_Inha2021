def get_2CirclesArea(Radius1, Radius2):
    Pi = 3.141592
    Area1 = Radius1 ** 2 * Pi
    Area2 = Radius2 ** 2 * Pi

    if Area1 > Area2:
        Area = Area1 - Area2
    else: # Modified Source Code
        Area = Area2 - Area1
    return Area

for i in range(3):
    r1, r2 = map(int, input("서로 다른 반지름의 길이를 입력하세요. ").split())
    S1 = get_2CirclesArea(r1, r2)
    print(S1)
print("감사합니다.")