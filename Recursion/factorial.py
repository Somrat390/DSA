def factorial(n):
    if n == 0 or n ==1:
        return 1
    result = n * factorial(n-1)
    return result

print(factorial(5))