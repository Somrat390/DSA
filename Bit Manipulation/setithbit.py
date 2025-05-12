def setbit(x,i):
    y = 1 << i
    z = x | y
    if x == z:
        return "Set"
    else:
        return "Not set"


x = int(input())
y = int(input())
print(setbit(x,y))