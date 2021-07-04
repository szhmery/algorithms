def minPathSum1(m):
    if m is None or len(m) == 0 or m[0] is None or len(m[0]) == 0:
        return 0
    row = len(m)
    col = len(m[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = m[0][0]
    for i in range(1, row):
        dp[i][0] = dp[i-1][0] + m[i][0]
    for j in range(1, col):
        dp[0][j] = dp[0][j-1] + m[0][j]
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + m[i][j]
    return dp[row - 1][col - 1]


def minPathSum2(m):
    if m is None or len(m) == 0 or m[0] is None or len(m[0]) == 0:
        return 0
    more = max(len(m), len(m[0]))
    less = min(len(m), len(m[0]))
    rowmore = True if more == len(m) else False
    arr = [0 for _ in range(less)]
    arr[0] = m[0][0]
    for i in range(1, less):
        arr[i] = arr[i-1] + m[0][i] if rowmore else arr[i-1] + m[i][0]

    for i in range(1, more):
        arr[0] = arr[0] + m[i][0] if rowmore else arr[0] + m[0][i]
        for j in range(1, less):
            arr[j] = min(arr[j-1], arr[j]) + m[i][j] if rowmore else min(arr[j-1], arr[j]) + m[j][i]
    return arr[less - 1]

if __name__ == '__main__':
    m = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
    min_step = minPathSum1(m)
    print(min_step)
    min_step = minPathSum2(m)
    print(min_step)