def toggle(n,i):
    return n ^ (1<<i)

n = int(input())

i = int(input())

print(toggle(n,i))