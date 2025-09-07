
numb = ""
def num(n):
    global numb
    if n == 0:
        return ""
    numb +=  str(n%10) 
    num(n//10)
    return int(numb)

print(num(1234))