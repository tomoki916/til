
from main import Solution


def test__case1():
    solution = Solution()
    nums = [1, 2, 3]

    result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    assert solution.subsets(nums) == result


def test__case2():
    solution = Solution()
    nums = [0]

    result = [[], [0]]

    assert solution.subsets(nums) == result
