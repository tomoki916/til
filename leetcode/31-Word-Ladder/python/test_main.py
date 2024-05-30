
from main import Solution


def test__case1():
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = 5

    assert solution.ladderLength(beginWord, endWord, wordList) == result


def test__case2():
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    result = 0

    assert solution.ladderLength(beginWord, endWord, wordList) == result


def test__case3():
    solution = Solution()
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog", "dot"]
    result = 3

    assert solution.ladderLength(beginWord, endWord, wordList) == result
