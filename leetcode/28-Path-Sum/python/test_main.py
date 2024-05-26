
from main import Solution
from mylib.python.binary_search_tree import convertArrayToBinarySearchTree


def test__case1():
    solution = Solution()
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    result = True

    assert solution.hasPathSum(
        convertArrayToBinarySearchTree(nums), targetSum) == result


def test__case2():
    solution = Solution()
    nums = [1, 2, 3]
    targetSum = 5
    result = False

    assert solution.hasPathSum(
        convertArrayToBinarySearchTree(nums), targetSum) == result
