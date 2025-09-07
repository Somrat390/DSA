def sum(n):
    if n == 0:
        return 0
    print(n)
    return sum(n//10) + n % 10

print(sum(1234))