def fun(n):
    res = ""
    ls = list(res)
    while n != 0:
        ls += '1' if n%2 == 1 else '0'
        n //= 2
    ls = list(reversed(ls))
    print(''.join(ls))

n = 10
fun(n)