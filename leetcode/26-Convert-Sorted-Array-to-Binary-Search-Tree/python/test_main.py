
from main import Solution
from mylib.python.binary_search_tree import convertArrayToBinarySearchTree


def test__case1():
    solution = Solution()
    nums = [-10, -3, 0, 5, 9]
    result = [0, -3, 9, -10, None, 5]

    assert solution.sortedArrayToBST(nums) == result


def test__case2():
    solution = Solution()
    nums = [1, 3]
    result = [3, 1]
    assert solution.sortedArrayToBST(nums) == result
