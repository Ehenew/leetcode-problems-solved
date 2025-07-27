class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0,1)]

        def dfs(row , col):
            if row < 0 or row >= n or col  < 0 or col >= m:
                return 

            if board[row][col] != "O":
                return

            board[row][col] = "."

            for dx, dy in directions:
                dfs(row + dx, col + dy)


        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m - 1)

        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n-1][j] == 'O':
                dfs(n - 1, j)

        # flipping 
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
                
                
