
from main import Solution


def test__case1():
    solution = Solution()
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    assert nums == [1, 3, 2]


def test__case2():
    solution = Solution()
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3]


def test__case3():
    solution = Solution()
    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    assert nums == [1, 5, 1]


def test__case4():
    solution = Solution()
    nums = [1, 2, 3, 4]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 4, 3]


def test__case5():
    solution = Solution()
    nums = [1, 3, 2]
    solution.nextPermutation(nums)
    assert nums == [2, 1, 3]


def test__case6():
    solution = Solution()
    nums = [1, 3, 5, 4, 2]
    solution.nextPermutation(nums)
    assert nums == [1, 4, 2, 3, 5]


def test__case7():
    solution = Solution()
    nums = [2, 2, 7, 5, 4, 3, 2, 2, 1]
    solution.nextPermutation(nums)
    assert nums == [2, 3, 1, 2, 2, 2, 4, 5, 7]
