def checkithbit(n,i):
    if (n >> i) & 1:
        return "Set" 
    else:
        return "not set"

print(checkithbit(13,2))