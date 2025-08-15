class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check_inbound(r, c):
            return  0 <= r < rows and 0 <= c < cols

        def dfs(row, col):
            if  not check_inbound(row, col) or grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))

            area = 1
            for dx, dy in directions:
                area += dfs(row + dx, col + dy)

            return area

        visited = set()
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))

        return max_area

