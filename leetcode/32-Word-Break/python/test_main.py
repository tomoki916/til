
from main import Solution


def test__case1():
    solution = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    result = True

    assert solution.wordBreak(s, wordDict) == result


def test__case2():
    solution = Solution()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    result = True

    assert solution.wordBreak(s, wordDict) == result


def test__case3():
    solution = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    result = False

    assert solution.wordBreak(s, wordDict) == result


def test__case4():
    solution = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand",  "cat", "og"]
    result = True

    assert solution.wordBreak(s, wordDict) == result
