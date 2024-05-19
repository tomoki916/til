
from main import Solution


def test__case1():
    solution = Solution()
    m = 3
    n = 7

    result = 28

    assert solution.uniquePaths(m, n) == result


def test__case2():
    solution = Solution()
    m = 3
    n = 2

    result = 3

    assert solution.uniquePaths(m, n) == result


def test__case3():
    solution = Solution()
    m = 1
    n = 1

    result = 1

    assert solution.uniquePaths(m, n) == result


def test__case4():
    solution = Solution()
    m = 4
    n = 1

    result = 1

    assert solution.uniquePaths(m, n) == result
