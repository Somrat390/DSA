def findunique(arr):
    unique = 0
    for num in arr:
        unique  ^= num 
    return unique

lst =[2,3,4,2,3,4,5]
print(findunique(lst))