
from main import Solution


def test__case1():
    solution = Solution()
    x = 2.00000
    n = 10
    result = 1024.00000

    assert solution.myPow(x, n) == result


def test__case2():
    solution = Solution()
    x = 2.10000
    n = 3
    result = 9.26100

    assert solution.myPow(x, n) == result


def test__case3():
    solution = Solution()
    x = 2.00000
    n = -2
    result = 0.25000

    assert solution.myPow(x, n) == result


def test__case4():
    solution = Solution()
    x = 2.00000
    n = 3
    result = 8

    assert solution.myPow(x, n) == result


def test__case5():
    solution = Solution()
    x = 2.00000
    n = 4
    result = 16

    assert solution.myPow(x, n) == result
