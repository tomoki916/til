from main import Solution


def test__case1():
    solution = Solution()
    assert solution.isValid("()") == True


def test__case2():
    solution = Solution()
    assert solution.isValid("()[]{}") == True


def test__case3():
    solution = Solution()
    assert solution.isValid("(]") == False


def test__case4():
    solution = Solution()
    assert solution.isValid("]") == False


def test__case5():
    solution = Solution()
    assert solution.isValid("[") == False


def test__case6():
    solution = Solution()
    assert solution.isValid("(()())") == True
