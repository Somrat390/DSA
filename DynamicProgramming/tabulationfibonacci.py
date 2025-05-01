prev = 1
prev2 = 0
n = int(input())
for i in range(2,n+1):
    current = prev + prev2
    prev2 = prev
    prev = current

print(current)


    