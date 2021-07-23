from tree.PrintBST import PrintBST


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def MirrorTree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = root.right, root.left
        MirrorTree(root.left)
        MirrorTree(root.right)
    return root


root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root.left = a
root.right = b
a.left = TreeNode(4)
a.right = TreeNode(5)
PrintBST.printBST(root)
MirrorTree(root)
PrintBST.printBST(root)
