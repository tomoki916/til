
from main import Solution
from mylib.python.binary_search_tree import convertArrayToBinarySearchTree


def test__case1():
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = [3, 9, 20, None, None, 15, 7]

    assert solution.buildTree(preorder, inorder) == result


def test__case2():
    solution = Solution()
    preorder = [-1]
    inorder = [-1]
    result = [-1]

    assert solution.buildTree(preorder, inorder) == result
