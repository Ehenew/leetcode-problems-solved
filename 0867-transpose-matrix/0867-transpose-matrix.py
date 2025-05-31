class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        transposed_matrix = []
        for _ in range(cols):
            transposed_matrix.append([0] * rows)

        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = matrix[i][j]
        return transposed_matrix