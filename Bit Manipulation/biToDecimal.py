def fun(s):
    i = 0
    res = 0
    for char in reversed(s):
        res += int(char) * pow(2,i)
        i += 1
    return res

s = "1010"
print(fun(s))