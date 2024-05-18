
from main import Solution


def test__case1():
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    assert solution.groupAnagrams(strs) == result


def test__case2():
    solution = Solution()
    strs = [""]
    result = [[""]]

    assert solution.groupAnagrams(strs) == result


def test__case3():
    solution = Solution()
    strs = ["a"]
    result = [["a"]]

    assert solution.groupAnagrams(strs) == result
