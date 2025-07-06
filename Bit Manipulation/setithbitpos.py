def setithbit(n,i):
    return n | (1 << i-1)
n = int(input("Enter a number:"))
i = int(input("Enter the bit position"))

print(setithbit(n,i))