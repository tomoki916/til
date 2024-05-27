
from main import Solution


def test__case1():
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    result = 5

    assert solution.maxProfit(prices) == result


def test__case2():
    solution = Solution()
    prices = [7, 6, 4, 3, 1]
    result = 0

    assert solution.maxProfit(prices) == result


def test__case3():
    solution = Solution()
    prices = [7]
    result = 0

    assert solution.maxProfit(prices) == result


def test__case4():
    solution = Solution()
    prices = [0, 1, 2, 3, 4, 5, 6, 7]
    result = 7

    assert solution.maxProfit(prices) == result
