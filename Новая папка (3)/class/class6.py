def ch(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True

nums = input().split()
prime_nums = list(filter(lambda x: ch(int(x)), nums))
print(prime_nums)