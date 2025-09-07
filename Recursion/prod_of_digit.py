def prod(n):
    if n == 0:
        return 1
    print(n)
    return n % 10 * prod(n//10)

print(prod(1234))