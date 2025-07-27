class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        q = deque()
        q.append(entrance)
        visited[entrance[0]][entrance[1]] = True

        steps = 0
        while q:
            for _ in range(len(q)):  
                row, col = q.popleft()

                for dx, dy in directions:
                    nr, nc = row + dx, col + dy

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if visited[nr][nc]:
                            continue
                        if maze[nr][nc] == '+':
                            continue

                        if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1):
                            return steps + 1  

                        visited[nr][nc] = True
                        q.append([nr, nc])
            steps += 1
        return -1
                    

