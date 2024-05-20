class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        if obstacleGrid[rows-1][cols-1] == 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                up = 0 if i - 1 < 0 else obstacleGrid[i-1][j]
                left = 0 if j - 1 < 0 else obstacleGrid[i][j-1]

                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else up + left

                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1

        return obstacleGrid[rows - 1][cols - 1]
