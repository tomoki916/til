from main import Solution, convertArrayToListNode, convertListNodeToArray


def test__case1():
    solution = Solution()
    head = [1, 2, 3, 3, 4, 4, 5]
    result = [1, 2, 5]

    assert convertListNodeToArray(
        solution.deleteDuplicates(convertArrayToListNode(head))) == result


def test__case2():
    solution = Solution()
    head = [1, 1, 1, 2, 3]
    result = [2, 3]

    assert convertListNodeToArray(
        solution.deleteDuplicates(convertArrayToListNode(head))) == result


def test__case3():
    solution = Solution()
    head = [1, 1, 1]
    result = []

    assert convertListNodeToArray(
        solution.deleteDuplicates(convertArrayToListNode(head))) == result


def test__case4():
    solution = Solution()
    head = [1, 2, 3, 4, 5]
    result = [1, 2, 3, 4, 5]

    assert convertListNodeToArray(
        solution.deleteDuplicates(convertArrayToListNode(head))) == result
