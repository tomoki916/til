
from main import Solution


def test__case1():
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = [[2, 2, 3], [7]]
    assert solution.combinationSum(candidates, target) == result


def test__case2():
    solution = Solution()
    candidates = [2, 3, 5]
    target = 8
    result = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    assert solution.combinationSum(candidates, target) == result


def test__case3():
    solution = Solution()
    candidates = [2]
    target = 1
    result = []
    assert solution.combinationSum(candidates, target) == result
