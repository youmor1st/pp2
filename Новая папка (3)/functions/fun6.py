def solve(x):
    cur = ""
    for i in range(len(x) - 1, -1, -1):
        if x[i] == ' ':
            print(cur[::-1], end=" ")
            cur = ""
        else:
            cur = cur + x[i]
    print(cur[::-1])

s = str(input())
solve(s)