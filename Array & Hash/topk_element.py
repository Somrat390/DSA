def topk_element(arr, k):   
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1

    freq_buckets = [[] for _ in range(len(arr) + 1)]
    for num, freq in count.items():
        freq_buckets[freq].append(num)
    result = []
    for i in range(len(freq_buckets) - 1, 0, -1):
        for num in freq_buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

print(topk_element([1,1,1,2,2,3], 2))