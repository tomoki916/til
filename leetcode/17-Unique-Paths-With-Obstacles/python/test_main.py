
from main import Solution


def test__case1():
    solution = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    result = 2

    assert solution.uniquePathsWithObstacles(obstacleGrid) == result


def test__case2():
    solution = Solution()
    obstacleGrid = [[0, 1], [0, 0]]

    result = 1

    assert solution.uniquePathsWithObstacles(obstacleGrid) == result


def test__case3():
    solution = Solution()
    obstacleGrid = [[1]]

    result = 0

    assert solution.uniquePathsWithObstacles(obstacleGrid) == result


def test__case4():
    solution = Solution()
    obstacleGrid = [[1, 0]]

    result = 0

    assert solution.uniquePathsWithObstacles(obstacleGrid) == result
