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

std1 = Student('Kim', 90, 50, 88)
print(std1.getSum())
print(std1.getAvg())