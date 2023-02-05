def has_33(nums):
    for i in range(0, len(nums) - 1, 1):
        cur = int(nums[i])
        if nums[i] == nums[i + 1] and cur == 3:
            return True
    return False

a = input().split()
print(has_33(a))