# 함수를 활용하여 메뉴판 메뉴 고르기
def price(menu):
    if menu == 1:
        m = "아메리카노"
        p = "2500원"
    elif menu == 2:
        m = "카페라떼"
        p = "3000원"
    elif menu == 3:
        m = "바닐라라떼"
        p = "3000원"
    else:
        print("다시 선택해주세요.")
        m ="메뉴없음"
        p = "0원"
    print(m, p)

print("메뉴를 보시고 드실 음료의 번호를 입력해주세요.")
menu = int(input("------메뉴------\n[1] 아메리카노\n[2] 카페라떼\n[3] 바닐라라떼\n"))
price(menu)