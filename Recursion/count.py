def countf(num: int, count=0):
    if num == 0:
        return count
    if num % 10 == 0:
        return countf(num // 10, count + 1)
    else:
        return countf(num // 10, count)

print(countf(100200, 0))
