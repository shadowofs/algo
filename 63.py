from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j != 0:
                    dp[j] += dp[j-1]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))