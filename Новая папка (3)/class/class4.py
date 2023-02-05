import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def chage(self, x, y):
        self.x += x
        self.y += y

    def dist(self, sq, sw):
        print(math.sqrt((sq - self.x) ** 2 + (sw - self.y) ** 2))

x, y = input().split()
x = int(x)
y = int(y)

ans = Point(x, y)
ans.show()
ans.chage(1, 1)
ans.dist(5, 5)