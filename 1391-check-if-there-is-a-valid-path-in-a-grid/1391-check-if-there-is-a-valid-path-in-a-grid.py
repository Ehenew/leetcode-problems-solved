class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        from collections import deque

        n, m = len(grid), len(grid[0])

        directions = {
            1: [(0, -1), (0, 1)],    
            2: [(-1, 0), (1, 0)],    
            3: [(0, -1), (1, 0)],    
            4: [(0, 1), (1, 0)],     
            5: [(0, -1), (-1, 0)],   
            6: [(0, 1), (-1, 0)]     
        }

        opposite = {
            (0, 1):  (0, -1),  
            (0, -1): (0, 1),
            (1, 0):  (-1, 0),  
            (-1, 0): (1, 0)
        }

        visited = [[False] * m for _ in range(n)]

        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(x, y):
            if x == n - 1 and y == m - 1:
                return True

            visited[x][y] = True
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and not visited[nx][ny]:
                    if opposite[(dx, dy)] in directions[grid[nx][ny]]:
                        if dfs(nx, ny):
                            return True
            return False

        return dfs(0, 0)
