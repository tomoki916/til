from main import Solution
from mylib.python.binary_search_tree import convertArrayToBinarySearchTree


def test__case1():
    solution = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    result = [[3], [20, 9], [15, 7]]

    assert solution.zigzagLevelOrder(
        convertArrayToBinarySearchTree(root)) == result


def test__case2():
    solution = Solution()
    root = [1]
    result = [[1]]

    assert solution.zigzagLevelOrder(
        convertArrayToBinarySearchTree(root)) == result


def test__case3():
    solution = Solution()
    root = []
    result = []

    assert solution.zigzagLevelOrder(
        convertArrayToBinarySearchTree(root)) == result


def test__case4():
    solution = Solution()
    root = [1, 2, 3, 4, None, None, 5]
    result = [[1], [3, 2], [4, 5]]

    assert solution.zigzagLevelOrder(
        convertArrayToBinarySearchTree(root)) == result
