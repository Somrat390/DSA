def duplicate(nums):
    unique_nums = set()
    for i in nums:
        if i in unique_nums:
            return True
        unique_nums.add(i)
    return False

print(duplicate([1,2,3,4,5,1]))