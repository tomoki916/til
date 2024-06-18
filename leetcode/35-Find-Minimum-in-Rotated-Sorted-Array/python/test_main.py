
from main import Solution


def test__case1():
    solution = Solution()
    nums = [3, 4, 5, 1, 2]
    result = 1

    assert solution.findMin(nums) == result


def test__case2():
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    result = 0

    assert solution.findMin(nums) == result


def test__case3():
    solution = Solution()
    nums = [11, 13, 15, 17]
    result = 11

    assert solution.findMin(nums) == result


def test__case4():
    solution = Solution()
    nums = [13, 11]
    result = 11

    assert solution.findMin(nums) == result


def test__case5():
    solution = Solution()
    nums = [11]
    result = 11

    assert solution.findMin(nums) == result
