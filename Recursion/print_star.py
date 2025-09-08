def print_star(row,column):
    if row==0:
        return
    print(column*"*",end="\n")
    print_star(row-1,column-1)

print_star(5,5)