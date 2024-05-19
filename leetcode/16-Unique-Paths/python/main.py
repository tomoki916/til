class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [[1]]

    #     for i in range(m):
    #         dp.append([])
    #         for j in range(n):
    #             if i == 0 and j == 0:
    #                 continue
    #             up = 0 if i - 1 < 0 else dp[i-1][j]
    #             left = 0 if j - 1 < 0 else dp[i][j-1]
    #             dp[i].append(up + left)

    #     return dp[m-1][n-1]

    def uniquePaths(self, m, n):
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i == m - 1 or j == n-1:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = solve(i+1, j) + solve(i, j+1)
            return dp[i][j]

        return solve(0, 0)
