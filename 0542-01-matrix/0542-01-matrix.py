from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        result = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    q.append((i, j))

        while q:
            row, col = q.popleft()
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if 0 <= new_row < m and 0 <= new_col < n and result[new_row][new_col] == -1:
                    result[new_row][new_col] = result[row][col] + 1
                    q.append((new_row, new_col))
        
        return result