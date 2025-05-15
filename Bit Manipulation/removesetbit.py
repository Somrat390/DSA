def remove(n):
    return n & (n-1)

n = int(input())
print(remove(n))