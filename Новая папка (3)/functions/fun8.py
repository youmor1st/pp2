def spy_game(nums):
    for i in range(2, len(nums), 1):
        if int(nums[i - 2]) == 0 and int(nums[i - 1]) == 0 and int(nums[i]) == 7:
            return True
    return False

a = input().split()
print(spy_game(a))