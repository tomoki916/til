
from main import Solution


def test__case1():
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    result = 6

    assert solution.maxSubArray(nums) == result


def test__case2():
    solution = Solution()
    nums = [1]

    result = 1

    assert solution.maxSubArray(nums) == result


def test__case3():
    solution = Solution()
    nums = [5, 4, -1, 7, 8]

    result = 23

    assert solution.maxSubArray(nums) == result


def test__case4():
    solution = Solution()
    nums = [-1]

    result = -1

    assert solution.maxSubArray(nums) == result
