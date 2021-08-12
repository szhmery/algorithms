# [-1, 0, 0, 1, 1, 4]
#   0
#  1 2
# 3 4
#  5
# force brute
def levels_tree(array):
    levels = {}
    ans = 0
    for i in range(len(array)):
        level = 1
        node_value = array[i]
        if node_value in levels.keys():
            ans = max(ans, levels[node_value])
        else:
            while node_value != -1:
                if node_value in levels.keys():
                    level = levels[node_value] + level - 1
                    break
                node_value = array[node_value]
                level += 1
            levels[array[i]] = level
            ans = max(ans, level)
    return ans


def levels_tree2(array):
    ans = 0
    for i in range(len(array)):
        level = 1
        node_value = array[i]
        while node_value != -1:
            level += 1
            node_value = array[node_value]
        ans = max(ans, level)
    return ans


array = [-1, 0, 0, 1, 1, 4]

print(levels_tree(array))
print(levels_tree2(array))

array = [-1, 0, 0, 1, 1, 4, 5, 6, 4]
#   0
#  1 2
# 3 4
#  5 8
#  6
#  7
print(levels_tree(array))
print(levels_tree2(array))
