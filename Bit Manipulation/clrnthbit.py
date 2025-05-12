def clrbit(n,i):
    return n & ~(1 << i)

n = int(input())

i = int(input())

print(clrbit(n,i))