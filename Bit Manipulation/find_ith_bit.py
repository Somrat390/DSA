def find_ith_bit(n, i):
    return (n >> i-1) & 1

n = int(input("Enter a number:"))
i = int(input("Enter the bit position"))

print(find_ith_bit(n,i))