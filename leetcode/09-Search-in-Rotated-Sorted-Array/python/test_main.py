
from main import Solution


def test__case1():
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert solution.search(nums, target) == 4


def test__case2():
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert solution.search(nums, target) == -1


def test__case3():
    solution = Solution()
    nums = [1]
    target = 0
    assert solution.search(nums, target) == -1


def test__case4():
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 4
    assert solution.search(nums, target) == 0


def test__case5():
    solution = Solution()
    nums = [1, 3]
    target = 3
    assert solution.search(nums, target) == 1
