def longest_subarray(arr):
    l = 0
    longest = 0
    unique_elements = set()
    for r in range(len(arr)):
        while arr[r] in unique_elements:
            unique_elements.remove(arr[l])
            l += 1
        w = r - l + 1
        longest = max(longest, w)
        unique_elements.add(arr[r])
    return longest

print(longest_subarray([5,1,3,5,2,3,4,1]))  