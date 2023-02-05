class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,ln,wd):
        super().__init__()
        self.s=ln
        self.s1=wd

    def area(self):
        return self.s*self.s1

x,y=input().split()
x=int(x)
y=int(y)
ans=Rectangle(x,y)
print(ans.area())

