# input: Eat Apple
# Output: Eae Alppt
def sortLowChars(str):
    if not str or len(str) == 0:
        return
    low = []
    for c in str:
        if 'a' <= c <= 'z':
            low.append(c)
    low.sort()
    str = list(str)
    for i in range(len(str)):
        if 'a' <= str[i] <= 'z':
            str[i] = low.pop(0)
    return ''.join(str)

print(sortLowChars("Eat Apple"))
