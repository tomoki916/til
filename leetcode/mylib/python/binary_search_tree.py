class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is not None:
            temp = TreeNode(arr[i])
            root = temp

            # insert left child
            root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)

            # insert right child
            root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)

    return root


def convertArrayToBinarySearchTree(arr):
    n = len(arr)
    root = None
    return insertLevelOrder(arr, root, 0, n)


def preOrder(node):
    if not node:
        return
    print(node.val, end=" ")
    preOrder(node.left)
    preOrder(node.right)
