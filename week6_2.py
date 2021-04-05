import random
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
members = 20
for member in range(members):
    name = ''.join(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    std.append(Student(name, randint(0, 100), randint(0, 100), randint(0, 100)))
    print(f"{std[member].name}의 총 점수는 {std[member].getSum()}이고, 평균은 {std[member].getAvg():.2f}입니다.")
