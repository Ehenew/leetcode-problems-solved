class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total = 0
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < rows and 0 <= nj < cols:
                            total += img[ni][nj]
                            count += 1
                res[i][j] = total // count  
        return res
