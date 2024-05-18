
from main import Solution


def test__case1():
    solution = Solution()
    nums = [1, 2, 3]
    result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    assert solution.permute(nums) == result


def test__case2():
    solution = Solution()
    nums = [0, 1]
    result = [[0, 1], [1, 0]]

    assert solution.permute(nums) == result


def test__case3():
    solution = Solution()
    nums = [1]
    result = [[1]]

    assert solution.permute(nums) == result
