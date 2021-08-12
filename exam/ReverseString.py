def ReverseString(source):
    def reverse(start, end):
        while start <= end:
            source[start], source[end] = source[end], source[start]
            start += 1
            end -= 1
    source = list(source)
    n = len(source)
    reverse(0, n - 1)
    print(source)
    i = 0
    j = 0
    while j <= n and i < n:
        if source[i] == ' ':
            i += 1
            j += 1
        elif j == n or source[j] == ' ':
            reverse(i, j-1)
            i = j
        else:
            j += 1
    print(source)
    return ''.join(source)

print(ReverseString('I am a student.'))
print(ReverseString("the sky is blue"))
print(ReverseString("  hello world  "))
print(ReverseString("  hello  world  "))



