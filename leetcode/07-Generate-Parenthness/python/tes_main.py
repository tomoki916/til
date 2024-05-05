from main import Solution


def test__case1():
    solution = Solution()
    assert solution.generateParenthesis(
        3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


def test__case2():
    solution = Solution()
    assert solution.generateParenthesis(1) == ["()"]


def test__case3():
    solution = Solution()
    assert solution.generateParenthesis(2) == ["()()", "(())"]
