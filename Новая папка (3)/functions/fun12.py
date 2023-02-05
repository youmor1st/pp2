def histogram(a):
    for i in range(0, len(a), 1):
        for j in range(1, int(a[i]) + 1, 1):
            print("*", end="")
        print(end="\n")

a = input().split()
histogram(a)