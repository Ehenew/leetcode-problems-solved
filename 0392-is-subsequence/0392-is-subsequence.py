class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == m or j == n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if s[i] == t[j]:
                memo[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                memo[i][j] = dfs(i, j + 1)
            
            return memo[i][j]

        return dfs(0,0) == m













        # m, n = len(s), len(t)

        # dp = [[0] * (n+1) for _ in range(m+1)]

        # for i in range(1,m):
        #     for j in range(1,n):
        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1] 
        #         else:
        #             dp[i][j] = dp[i][j - 1]
        
        # return dp[m][n] == m

