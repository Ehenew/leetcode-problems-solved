class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[False for _ in range(m)] for _ in range(n)]

        self.ans = 0

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m


        def dfs(row, col):
            visited[row] [col] = True
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    self.ans += 1

                elif not visited[new_row][new_col]:
                    dfs(new_row, new_col)

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return self.ans
