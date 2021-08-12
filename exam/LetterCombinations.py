#input: morgan stanley investment bank
# 6 7 10 4
#output: msib
# msia
# msin
# msik
# msnb
# nytk
def getCombinations(str):
    def helper(cur, letters, ans, index):
        if index == len(letters):
            ans.append(cur)
            return ans
        letter = letters[index]
        for i in range(len(letter)):
            helper(cur + letter[i], letters, ans, index + 1)

    ans = []
    if not str or len(str) == 0:
        return ans
    letters = str.split()
    cur = ''
    helper(cur, letters, ans, 0)
    return ans

print(getCombinations('morgan stanley investment bank'))
print(getCombinations('morgan stanley bank'))
print(getCombinations(''))