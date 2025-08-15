class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(row, cols, pos_diag, neg_diag):
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                backtrack(row + 1, cols, pos_diag, neg_diag)

                # backtrack
                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        res = []
        backtrack(0, set(), set(), set())
        return res
