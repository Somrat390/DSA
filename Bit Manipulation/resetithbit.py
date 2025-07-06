def reset_ith_bit(n, i):
    return (1 << i-1) ^ n

n = int(input("Enter a number:"))
i = int(input("Enter the bit position"))

print(reset_ith_bit(n,i))