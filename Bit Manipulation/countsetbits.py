def count(n):
    cnt = 0
    while n > 0:
        cnt += (n & 1)
        n = n >> 1
    return cnt

n = int(input())
print(count(n))

    