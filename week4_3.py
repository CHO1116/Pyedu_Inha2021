math = open('score.txt', 'r')
data = math.readlines()
sum = 0
for element in data:
    sum += int(element.rstrip())
avg = sum / len(data)
print(f"읽어온 점수 합: {sum}\n응시 학생 수: {len(data)}\n평균: {avg}")
math.close()