def check(n):
    if n & (n-1) == 0:
        print("Set")
    else:
        print("not set")

n = int(input())
check(n)