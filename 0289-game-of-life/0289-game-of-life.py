class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        def count_live_neighbors(r, c):
            live_neighbors = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if abs(board[nr][nc]) == 1:
                        live_neighbors += 1
            return live_neighbors


        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r,c) 

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1 
                
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2
    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0