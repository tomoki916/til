
from main import Solution
from mylib.python.binary_search_tree import convertArrayToBinarySearchTree


def test__case1():
    solution = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    result = 3

    assert solution.maxDepth(
        convertArrayToBinarySearchTree(root)) == result


def test__case2():
    solution = Solution()
    root = [1, None, 2]
    result = 2

    assert solution.maxDepth(
        convertArrayToBinarySearchTree(root)) == result


def test__case3():
    solution = Solution()
    root = []
    result = 0

    assert solution.maxDepth(
        convertArrayToBinarySearchTree(root)) == result


def test__case4():
    solution = Solution()
    root = [1]
    result = 1

    assert solution.maxDepth(
        convertArrayToBinarySearchTree(root)) == result
