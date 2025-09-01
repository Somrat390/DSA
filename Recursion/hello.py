

def message(i=0):
    print('hello world')
    i += 1
    if i == 5:
        return
    return message(i)

message()


