from main import Solution


def test__case1():
    solution = Solution()
    nums = [1, 2, 3, 1]
    result = 4

    assert solution.rob(nums) == result


def test__case2():
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    result = 12

    assert solution.rob(nums) == result


def test__case3():
    solution = Solution()
    nums = [2, 7, 9, 3, 1, 2]
    result = 13

    assert solution.rob(nums) == result
