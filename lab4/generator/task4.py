def square(a,b):
    for i in range(a,b+1):
        yield i*2
a,b=input().split()
a=int(a)
b=int(b)
for i in square (a,b):
    print(i)
