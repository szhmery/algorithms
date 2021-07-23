from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.pre = None
def ConvertBSTToList(root:'TreeNode')->'ListNode':
    if not root:
        return
    stack = []
    node = root
    pre = None
    next = None

    head_f = True
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        if head_f:
            node = stack.pop()
            head = ListNode(node.val)
            l = head
            head_f = False
        node = stack.pop()
        next = ListNode(node.val)
        pre = l
        next.pre = pre
        l.next = next
        l = next

        node = node.right
    return head

root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(8)

newList = ConvertBSTToList(root)
print("\nAfter:")
tmp_list = newList
while tmp_list:
    print(str(tmp_list.val), end='->')
    tmp_list = tmp_list.next
root = TreeNode(10)
a = TreeNode(6)
b = TreeNode(14)
root.left = a
root.right = b
a.left = TreeNode(4)
a.right    = TreeNode(8)
b.left = TreeNode(12)
b.right = TreeNode(16)

newList = ConvertBSTToList(root)
print("\nAfter:")
tmp_list = newList
while tmp_list:
    print(str(tmp_list.val), end='->')
    pre = tmp_list
    tmp_list = tmp_list.next
print("\nPre:")
tmp_list = pre
while tmp_list:
    print(str(tmp_list.val), end='->')
    tmp_list = tmp_list.pre