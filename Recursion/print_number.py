def printf(n):
    print(n)
    if n==1:
        return
    printf(n-1)

printf(5)


def print_reverse(n):
    if n==0:
        return
    print_reverse(n-1)
    print(n)

print_reverse(5)