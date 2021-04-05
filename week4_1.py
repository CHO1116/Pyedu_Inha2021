order = []
while True:
    while(len(order) != 3):
        menu = input("주문하실 메뉴를 입력해주세요. ")
        order.append(menu)
        print(f"주문내역: {order}\n")
    print(f"입력하신 메뉴는 {order[0]}, {order[1]}, {order[2]}입니다. ")
    YesNo = input("이대로 주문하시겠습니까? [y/n]... ")
    if (YesNo == "y") or (YesNo == "Y"):
        print("주문이 완료되었습니다. 주문해주셔서 감사합니다.")
        print(f"----주문서----\n{order[0]}\n{order[1]}\n{order[2]}")
        break
    elif (YesNo == "n") or (YesNo == "N"):
        print("주문을 취소합니다. 다시 입력해주세요.\n")
        order = []
        continue
    else:
        continue