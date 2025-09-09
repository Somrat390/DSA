def skip_char(given_string, new_string):
    if len(given_string) == 0:
        return new_string
    first_char = given_string[0]
    if first_char == 'a':
        return skip_char(given_string[1:], new_string)
    else:
        new_string += first_char
        return skip_char(given_string[1:], new_string)
    

print(skip_char("baccad", ""))
