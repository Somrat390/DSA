def prod(n):
    if n%10 == n:
        return n
    print(n)
    return n % 10 * prod(n//10)

print(prod(1234))