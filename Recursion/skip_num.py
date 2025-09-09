def skip_char(s,char):
    result = "" 
    for i in s:
        if i != char:
            result = result + i
    return result

print(skip_char("hello","l"))