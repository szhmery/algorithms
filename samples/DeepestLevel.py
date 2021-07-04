# [-1, 0, 0, 1, 1, 4]
#   0
#  1 2
# 3 4
#  5
# force brute
def levels_tree(array):
    ans = 0
    for i in range(len(array)):
        level = 1
        node_value = array[i]
        while node_value != -1:
            level += 1
            node_value = array[node_value]
        ans = max(ans, level)
    return ans

def levels_tree2(array):
    pass

array = [-1, 0, 0, 1, 1, 4]

print(levels_tree(array))
