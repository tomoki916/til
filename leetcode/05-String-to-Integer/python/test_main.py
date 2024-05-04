from main import Solution


def test__case1():
    solution = Solution()
    assert solution.myAtoi("42") == 42


def test__case2():
    solution = Solution()
    assert solution.myAtoi(" -042") == -42


def test__case3():
    solution = Solution()
    assert solution.myAtoi("1337c0d3") == 1337


def test__case4():
    solution = Solution()
    assert solution.myAtoi("ab") == 0


def test__case5():
    solution = Solution()
    assert solution.myAtoi("") == 0


def test__case6():
    solution = Solution()
    assert solution.myAtoi("   +0 123") == 0
