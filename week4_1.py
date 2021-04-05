order=[]
while(len(order)!=3):
    menu=input("주문하고 싶은 음식을 알려주세요. ")
    order.append(menu)
    print(f"주문내역: {order}\n")
print(f"{order[0]}, {order[1]}, {order[2]} 주문되었습니다.")