class Solution:
    def latestDayToCross(self, row, col, cells):
        def canWalk(day):
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1

            queue = collections.deque()
            for j in range(col):
                if grid[0][j] == 0:
                    queue.append((0, j))
                    grid[0][j] = 1

            while queue:
                x, y = queue.popleft()
                if x == row - 1:
                    return True
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx, ny))
            return False

        left, right = 1, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if canWalk(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans