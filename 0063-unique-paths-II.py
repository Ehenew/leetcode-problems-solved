class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = 1
        
        for j in range(1, n):
            if grid[0][j] == 0:  # No obstacle
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, m):
            if grid[i][0] == 0:  # No obstacle
                dp[i][0] = dp[i - 1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:  # No obstacle
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The bottom-right corner will contain the answer
        return dp[m - 1][n - 1]
