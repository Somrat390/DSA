def TwoSum(arr,target):
    num_dict = {}
    for i,num in enumerate(arr):

        diff = target - num
        if diff in num_dict:
            return (num_dict[diff],i)
        num_dict[num] = i

print(TwoSum([2,7,11,15],9)) 