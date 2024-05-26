
from main import Solution
from mylib.python.binary_search_tree import convertArrayToBinarySearchTree


def test__case1():
    solution = Solution()
    nums = [3, 9, 20, None, None, 15, 7]
    result = 2

    assert solution.minDepth(convertArrayToBinarySearchTree(nums)) == result


def test__case2():
    solution = Solution()
    nums = [2, None, 3, None, 4, None, 5, None, 6]
    result = 5

    assert solution.minDepth(convertArrayToBinarySearchTree(nums)) == result


def test__case3():
    solution = Solution()
    nums = [1]
    result = 1

    assert solution.minDepth(convertArrayToBinarySearchTree(nums)) == result
