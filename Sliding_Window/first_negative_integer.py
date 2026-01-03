def negative_int(arr,k):
    Num = []
    window = arr[:k]
    end = k
    for i in range(k,len(arr)):
        negative = False
        for num in window:
            if num < 0:
                Num.append(num)
                negative = True
                break
        if not negative:
            Num.append(0)     
        end = end + 1
        start = end - i       
        window = window[start:end+1]
    return Num
print(negative_int([-8, 2, 3, -6, 10], 2))


