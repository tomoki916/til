from main import Solution
from mylib.python.binary_search_tree import convertArrayToBinarySearchTree


def test__case1():
    solution = Solution()
    root = [2, 1, 3]
    result = True

    assert solution.isValidBST(convertArrayToBinarySearchTree(root)) == result


def test__case2():
    solution = Solution()
    root = [5, 1, 4, None, None, 3, 6]
    result = False

    assert solution.isValidBST(convertArrayToBinarySearchTree(root)) == result


def test__case3():
    solution = Solution()
    root = [5, 1, 6, None, None, 3, 5]
    result = False

    assert solution.isValidBST(convertArrayToBinarySearchTree(root)) == result


def test__case4():
    solution = Solution()
    root = [5, 4, 6, None, None, 3, 7]
    result = False

    assert solution.isValidBST(convertArrayToBinarySearchTree(root)) == result


def test__case4():
    solution = Solution()
    root = [2147483647]
    result = True

    assert solution.isValidBST(convertArrayToBinarySearchTree(root)) == result
