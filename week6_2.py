from random import *
class Student:
    name = None
    kor = None
    eng = None
    math = None

    def __init__(self, name = '', kor = 0, eng = 0, math = 0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def getSum(self):
        sum = self.kor + self.eng + self.math
        return sum

    def getAvg(self):
        average = self.getSum() / 3
        return average

std = []
name = [ '성민이', '철수', '지영이', '영희', '주영이', '늘이', '경준이', '수영이', '희진이', '찬희', 
         '송강', '지연이', '상혁이', '양호', '대훈이', '정인이', '지수', '준서', '상준이', '경민이' ]
members = 20
for member in range(members):
    std.append(Student(name[member], randint(0, 100), randint(0, 100), randint(0, 100)))
    print(f"{std[member].name}의 총 점수는 {std[member].getSum()}이고, 평균은 {std[member].getAvg():.2f}입니다.")