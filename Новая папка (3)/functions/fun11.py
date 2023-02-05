def ch(s):
    l = 0
    r = len(s) - 1

    while l < (len(s) // 2):
        if s[l] != s[r]:
            return "NO"
        l += 1
        r -= 1
    return "YES"

s = str(input())
print(ch(s))