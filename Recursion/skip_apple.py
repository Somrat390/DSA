def skipapple(given_string):
    if len(given_string) == 0:
        return ""
    if given_string.startswith("apple"):
        return skipapple(given_string[5:])
    else:
        return given_string[0] + skipapple(given_string[1:])

print(skipapple("bcappleccadapple"))  # bccad