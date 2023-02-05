def solve(a):
    used = {}
    for i in range(0, len(a), 1):
        key = int(a[i])
        if key in used:
            continue
        used[int(a[i])] = 1
        print(a[i], end=" ")

a = input().split()
solve(a)