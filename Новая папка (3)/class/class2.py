class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, sz):
        super().__init__()
        self.sz = sz

    def area(self):
        return self.sz * self.sz

x = int(input())
ans = Square(x)

print(ans.area())