# 有一个5*5的格子，在格子中可以放入 红黄蓝绿紫 5种颜色的小球，可以放入，也可以不放入。相同颜色的球，
# 如果相连（横竖）超过4个就可以消除，给定任意一种小球在格子中的分布作为输入，求消除后最终格子中小球的分布。
# 你可以自己定义输入输出的数据结构
# 0 = null
# 1,2,3,4,5 = colors
def removeBalls(grid):
    # red, yellow, blue, green, purple = 1,2,3,4,5
    colors = [1, 2, 3, 4, 5]
    R, C = 5, 5
    pos = []
    seen = set()

    def dfs(r, c, pos, color):
        if r < 0 or r >= R or c < 0 or c >= C or (r, c) in seen or grid[r][c] != color:
            return

        pos.append((r, c))
        seen.add((r, c))
        dfs(r + 1, c, pos, color)
        dfs(r, c + 1, pos, color)

    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0:
                dfs(i, j, pos, grid[i][j])
                if len(pos) >= 4:
                    for m, n in pos:
                        grid[m][n] = 0
                pos = []

    return


grid = [[2, 0, 3, 0, 0], [2, 0, 3, 3, 3], [2, 0, 0, 0, 0], [2, 0, 4, 4, 0], [0, 0, 4, 4, 0]]
removeBalls(grid)
print(grid)
grid = [[0, 0, 3, 0, 0], [2, 0, 3, 3, 3], [2, 0, 0, 0, 0], [2, 0, 4, 4, 0], [0, 0, 4, 4, 0]]
removeBalls(grid)
print(grid)
grid = [[2, 0, 3, 0, 0], [2, 0, 3, 3, 3], [2, 0, 0, 0, 0], [2, 0, 4, 4, 0], [2, 0, 4, 4, 0]]
removeBalls(grid)
print(grid)
grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
removeBalls(grid)
print(grid)
grid = [[2, 3, 0, 0, 0], [2, 0, 0, 3, 3], [2, 0, 0, 0, 0], [2, 0, 4, 4, 0], [0, 0, 4, 4, 0]]
removeBalls(grid)
print(grid)
