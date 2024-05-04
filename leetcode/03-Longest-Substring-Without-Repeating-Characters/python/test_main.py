from main import Solution


def test__case1():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3


def test__case2():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("bbbbb") == 1


def test__case3():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("pwwkew") == 3


def test__case4():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("dvdf") == 3
