from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        q = deque([(0, 0)])
        
        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    new_cost = dp[i][j] + grid[x][y]
                    if new_cost < dp[x][y]:
                        dp[x][y] = new_cost
                        if grid[x][y] == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
        
        return dp[m-1][n-1] < health
