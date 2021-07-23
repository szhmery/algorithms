from typing import List


# swap and recursion
# https://www.cnblogs.com/songchengyu/p/12640126.html
def StringPermunation(s:str) ->  List:
    def permunation(s, index, ans, length):
        if index == length:
            ans.append(''.join(s))
            return
        for i in range(index, length):
            s[i], s[index] = s[index], s[i]
            permunation(s, index + 1, ans, length) # index + 1, not i + 1!!!
            s[i], s[index] = s[index], s[i]

    if not s:
        return
    ans = []
    permunation(list(s), 0, ans, len(s))
    return ans

print(StringPermunation('abc'))
