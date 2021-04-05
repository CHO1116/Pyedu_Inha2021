text = open('inha.txt', 'r', encoding = 'UTF8')
data = text.readline()  # 첫번째 줄만 read
print(data)

data = text.readlines() # 각 줄을 모두 read
each_data = []
for element in data:
    each_data = element.rstrip()
    print(each_data)
text.close()