# bit manipulation
def largest_power(n: int):
    n = n | (n >> 1)
    n = n | (n >> 2)
    n = n | (n >> 4)
    n = n | (n >> 8)
    n = n | (n >> 16)
    return (n + 1) >> 1


print(largest_power(10))
