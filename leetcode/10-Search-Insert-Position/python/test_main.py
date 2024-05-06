
from main import Solution


def test__case1():
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    result = 2
    assert solution.searchInsert(nums, target) == result


def test__case2():
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    result = 1
    assert solution.searchInsert(nums, target) == result


def test__case3():
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    result = 4
    assert solution.searchInsert(nums, target) == result
