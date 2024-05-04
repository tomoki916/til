from main import Solution


def test__case1():
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"


def test__case2():
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


def test__case3():
    solution = Solution()
    assert solution.convert("A", 1) == "A"


def test__case4():
    solution = Solution()
    assert solution.convert("AB", 1) == "AB"
