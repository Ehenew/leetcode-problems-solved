class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Create an n x n matrix filled with 0s
        matrix = [[0] * n for _ in range(n)]
        
        # Define boundaries
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        
        while top <= bottom and left <= right:
            # Fill top row (left to right)
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move the top boundary down
            
            # Fill right column (top to bottom)
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move the right boundary left
            
            if top <= bottom:
                # Fill bottom row (right to left)
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1  # Move the bottom boundary up
            
            if left <= right:
                # Fill left column (bottom to top)
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1  # Move the left boundary right
        
        return matrix
