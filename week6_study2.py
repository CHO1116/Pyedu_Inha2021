class Circle:
    r = None

    def __init__(self, radius = 20):
        print("Circle 객체가 생성됩니다.")
        self.r = radius

    def SetRadius(self, radius):
        self.r = radius

    def Area(self):
        area = self.r ** 2 * 3.14
        print(f"원의 넓이는 {area:.2f}")

    def Perimeter(self):
        perimeter = 2 * self.r * 3.14
        print(f"원의 둘레는 {perimeter:.2f}")

circle1 = Circle()

print(circle1.r)    # r = 20
circle1.Area()      # 20 * 20 * 3.14
circle1.Perimeter() # 2 * 20 * 3.14

circle1.SetRadius(10)   # r = 10
print(circle1.r)        # r = 10
circle1.Area()          # 10 * 10 * 3.14
circle1.Perimeter()     # 2 * 10 * 3.14