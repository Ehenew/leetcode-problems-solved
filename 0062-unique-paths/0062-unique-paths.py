class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]    

        def dp(row, col):
            if row >= m or col >= n:
                return 0 

            if row == m - 1 and col == n - 1:
                return 1
            
            if memo[row][col] == -1:
                memo[row][col] = dp(row + 1, col) + dp(row, col + 1)

            return memo[row][col]        
        return dp(0,0)