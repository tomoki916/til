
from main import Solution


def test__case1():
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    result = 7

    assert solution.maxProfit(prices) == result


def test__case2():
    solution = Solution()
    prices = [1, 2, 3, 4, 5]
    result = 4

    assert solution.maxProfit(prices) == result


def test__case3():
    solution = Solution()
    prices = [7, 6, 4, 3, 1]
    result = 0

    assert solution.maxProfit(prices) == result


def test__case4():
    solution = Solution()
    prices = [1]
    result = 0

    assert solution.maxProfit(prices) == result


def test__case5():
    solution = Solution()
    prices = [1, 2, 6, 4, 5]
    result = 4

    assert solution.maxProfit(prices) == result
